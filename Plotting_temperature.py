# ----------- Load files ---------------------

foam_monsoon = xr.open_dataset('foam_sst.nc')
control_monsoon = xr.open_dataset('control_sst.nc')
cumulus_monsoon = xr.open_dataset('cumulus_sst.nc')
nudge_monsoon = xr.open_datast('nudged_sst.nc')

# ---------------- Configuration ----------------
LON_SLICE = slice(30, 130)
DEPTH = 0
FILL_THRESHOLD = 5e10
MAP_EXTENT = [50, 120, -15, 30]
PROJ = ccrs.PlateCarree()

CLEVS_SST = np.arange(27, 32.5, 0.5)
CLEVS_BIAS = np.arange(-1.2, 1.4, 0.2)

BOXES = [(50, -2, 10, 5), (60.25, 18, 7, 6), (88, 15, 9, 8)]   # x0, y0, w, h
LABELS = [(51, 5, "WEIO", 0.2), (61, 14, "N.AS", 0.3), (84, 11, "N.BoB", 0.3)]

# (row, col, title, experiment key)
SST_PANELS = [
    (0, 0, "(a) FOAM",    "foam"),
    (1, 0, "(b) Control", "control"),
    (2, 0, "(c) Cumulus", "cumulus"),
    (3, 0, "(d) Nudged",  "nudged"),
]
BIAS_PANELS = [
    (0, 1, "(e) Control - FOAM", "control"),
    (1, 1, "(f) Cumulus - FOAM", "cumulus"),
    (2, 1, "(g) Nudged - FOAM",  "nudged"),
]

# Input dataset
datasets = {
    "foam":    foam_monsoon,
    "control": control_monsoon,
    "cumulus": model_monsoon,
    "nudged":  nudge_monsoon,
}


# ---------------- Helpers ----------------
def prepare(da):
    """Crop longitude, select nearest depth level, mask fill values."""
    da = da.sel(longitude=LON_SLICE).sel(deptht=DEPTH, method="nearest")
    return da.where(da <= FILL_THRESHOLD)


def decorate(ax):
    """Gridlines, coastlines, region boxes and labels, extent."""
    ax.set_extent(MAP_EXTENT, crs=PROJ)
    for spine in ax.spines.values():
        spine.set_edgecolor("gray")

    gl = ax.gridlines(draw_labels=True, linestyle=(0, (1, 1)), linewidth=1,
                      color="gray", alpha=0.5)
    gl.top_labels = gl.right_labels = gl.bottom_labels = False
    gl.xlocator = mticker.FixedLocator(range(50, 121, 10))
    gl.ylabel_style = {"size": 10}
    ax.coastlines(resolution="110m", color="gray")

    for x, y, w, h in BOXES:
        ax.add_patch(Rectangle((x, y), w, h, edgecolor="black",
                               fill=False, linewidth=0.7))
    for x, y, text, pad in LABELS:
        ax.text(x, y, text, fontsize=8, color="black", fontweight="bold",
                bbox=dict(facecolor="wheat", edgecolor="wheat", alpha=0.8, pad=pad))

    ax.set_xticks(range(50, 130, 20), crs=PROJ)
    ax.xaxis.set_major_formatter(LongitudeFormatter())
    ax.tick_params(axis="x", which="major", length=0, labelsize=10)


def add_vertical_colorbar(fig, mappable, rect, label):
    cax = fig.add_axes(rect)
    cbar = fig.colorbar(mappable, cax=cax, orientation="vertical")
    cbar.set_label(label, fontsize=10, loc="bottom", rotation=0)
    cbar.ax.tick_params(labelsize=10)
    return cbar


# ---------------- Data ----------------
sst = {name: prepare(ds.votemper) for name, ds in datasets.items()}
foam_data = sst["foam"].data
bias = {name: sst[name] - foam_data for name in ("control", "cumulus", "nudged")}

# ---------------- Figure ----------------
fig, axes = plt.subplots(4, 2, figsize=(7, 8), sharex=True, sharey=True,
                         subplot_kw=dict(projection=PROJ),
                         facecolor="white", layout="constrained")

for row, col, title, key in SST_PANELS:
    ax = axes[row, col]
    cs_sst = ax.contourf(sst[key].longitude, sst[key].latitude, sst[key],
                         CLEVS_SST, transform=PROJ, cmap=cmo.cm.amp, extend="both")
    ax.set_title(title, fontsize=10)

for row, col, title, key in BIAS_PANELS:
    ax = axes[row, col]
    cs_bias = ax.contourf(bias[key].longitude, bias[key].latitude, bias[key],
                          CLEVS_BIAS, transform=PROJ, cmap=cmo.cm.balance, extend="both")
    ax.set_title(title, fontsize=10)

axes[3, 1].set_axis_off()

for ax in axes.flat:
    if ax.axison:
        decorate(ax)

add_vertical_colorbar(fig, cs_sst,  [0.44, 0.14, 0.01, 0.7], "SST (\u00b0C)")
add_vertical_colorbar(fig, cs_bias, [0.94, 0.35, 0.01, 0.5], "SST bias (\u00b0C)")

plt.show()
