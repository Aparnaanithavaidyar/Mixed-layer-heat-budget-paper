# ---------------- Configuration ----------------
LON_SLICE = slice(30, 130)
LAT_SLICE = slice(-30, 30)
MAP_EXTENT = [50, 120, -15, 30]
STRIDE = 15
PROJ = ccrs.PlateCarree()
UNIT = "m s\u207B\u00B9"

V_MASK = {"foam": 100, "control": 100, "cumulus": 30, "nudged": 30}   # mask |v| above

CLEVS_WIND = np.arange(5, 14, 1)
CLEVS_BIAS = np.arange(-2, 2.5, 0.5)

BOXES = [(50, -2, 10, 5), (60.25, 18, 7, 6), (88, 15, 9, 8)]           # x0, y0, w, h
LABELS = [(51, 5, "WEIO", 0.2), (61, 14, "N.AS", 0.3), (84, 11, "N.BoB", 0.3)]

WIND_PANELS = [   # row, col, title, experiment
    (0, 0, "(a) UM analysis", "foam"),
    (1, 0, "(b) Control",     "control"),
    (2, 0, "(c) Cumulus",     "cumulus"),
    (3, 0, "(d) Nudged",      "nudged"),
]
BIAS_PANELS = [
    (0, 1, "(e) Control - UM analysis", "control"),
    (1, 1, "(f) Cumulus - UM analysis", "cumulus"),
    (2, 1, "(g) Nudged - UM analysis",  "nudged"),
]

# Datasets already loaded: (wind speed, u, v) for each experiment, IMPORTANT: Load dataset for each component using xr.open_dataset('corresponding_file_for_the_model_run.nc')
raw = {
    "foam":    (windspeed_foam,    ucomp_foam,    vcomp_foam),
    "control": (windspeed_model,   ucomp_model,   vcomp_model),
    "cumulus": (windspeed_cumulus, ucomp_cumulus, vcomp_cumulus),
    "nudged":  (windspeed_nudge,   ucomp_nudge,   vcomp_nudge),
}


# ---------------- Helpers ----------------
def get_field(ds, var, vmax=None):
    """Crop to region, pick variable, optionally mask values above vmax."""
    da = ds.sel(longitude=LON_SLICE, latitude=LAT_SLICE)[var]
    return da if vmax is None else da.where(da <= vmax)


def plot_winds(ax, speed, u, v, levels, cmap, scale):
    """Filled wind speed with subsampled wind vectors."""
    cs = ax.contourf(speed.longitude, speed.latitude, speed, levels,
                     transform=PROJ, cmap=cmap, extend="both")
    q = ax.quiver(u.longitude[::STRIDE], u.latitude[::STRIDE],
                  u[::STRIDE, ::STRIDE], v[::STRIDE, ::STRIDE],
                  width=0.0055, scale=scale)
    return cs, q


def decorate(ax):
    """Extent, gridlines, coastlines, land, region boxes and labels."""
    ax.set_extent(MAP_EXTENT, crs=PROJ)
    for spine in ax.spines.values():
        spine.set_edgecolor("gray")

    gl = ax.gridlines(draw_labels=True, linestyle=(0, (1, 1)), linewidth=1,
                      color="gray", alpha=0.5)
    gl.top_labels = gl.right_labels = gl.bottom_labels = False
    gl.xlocator = mticker.FixedLocator(range(50, 121, 10))
    gl.ylabel_style = {"size": 10}

    ax.coastlines(resolution="110m", color="gray")
    ax.add_feature(cfeature.LAND, facecolor="white", zorder=1)

    for x, y, w, h in BOXES:
        ax.add_patch(Rectangle((x, y), w, h, edgecolor="black",
                               fill=False, linewidth=0.7))
    for x, y, text, pad in LABELS:
        ax.text(x, y, text, fontsize=8, color="black", fontweight="bold",
                bbox=dict(facecolor="wheat", edgecolor="wheat", alpha=0.8, pad=pad))

    ax.set_xticks(range(50, 130, 20), crs=PROJ)
    ax.xaxis.set_major_formatter(LongitudeFormatter())
    ax.tick_params(axis="x", which="major", length=0, labelsize=10)


def add_colorbar(fig, mappable, rect, text, text_xy):
    cax = fig.add_axes(rect)
    cbar = fig.colorbar(mappable, cax=cax, orientation="vertical")
    cbar.ax.tick_params(labelsize=10)
    cbar.ax.text(*text_xy, text, transform=cbar.ax.transAxes,
                 ha="right", fontsize=10, clip_on=False)
    return cbar


# ---------------- Data ----------------
winds = {
    name: dict(
        speed=get_field(ws, "wind_speed"),
        u=get_field(uc, "zonal_wind"),
        v=get_field(vc, "meridional_wind", V_MASK[name]),
    )
    for name, (ws, uc, vc) in raw.items()
}
bias = {
    name: {k: winds[name][k] - winds["foam"][k] for k in ("speed", "u", "v")}
    for name in ("control", "cumulus", "nudged")
}

# ---------------- Figure ----------------
fig, axes = plt.subplots(4, 2, figsize=(7.5, 8), sharex=True, sharey=True,
                         subplot_kw=dict(projection=PROJ),
                         facecolor="white", layout="constrained")

for row, col, title, key in WIND_PANELS:
    w = winds[key]
    cs_wind, q_wind = plot_winds(axes[row, col], w["speed"], w["u"], w["v"],
                                 CLEVS_WIND, cmo.cm.amp, scale=150)
    axes[row, col].set_title(title, fontsize=10, y=0.97)

for row, col, title, key in BIAS_PANELS:
    b = bias[key]
    cs_bias, q_bias = plot_winds(axes[row, col], b["speed"], b["u"], b["v"],
                                 CLEVS_BIAS, cmo.cm.curl, scale=30)
    axes[row, col].set_title(title, fontsize=10, y=0.97)

axes[3, 1].set_axis_off()
for ax in axes.flat:
    if ax.axison:
        decorate(ax)

# Reference vectors (both placed relative to the bottom-left panel)
axes[3, 0].quiverkey(q_wind, 1.2, 0.5, 10, f"10 {UNIT}", labelpos="E",
                     coordinates="axes", fontproperties={"size": 10})
axes[3, 0].quiverkey(q_bias, 1.0, -0.25, 2, f"2 {UNIT}", labelpos="E",
                     coordinates="axes", fontproperties={"size": 10})

# Colorbars
add_colorbar(fig, cs_wind, [0.44, 0.14, 0.01, 0.7], "Wind speed",      (10, -0.13))
add_colorbar(fig, cs_bias, [0.94, 0.28, 0.01, 0.7], "Wind speed bias", (-5.4, -0.135))

plt.show()
