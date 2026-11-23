# ---------------- Configuration ----------------
DATA_DIR = Path("data/winds_cloud")        # Add file path
LON_SLICE = slice(30, 130)
LAT_SLICE = slice(-30, 30)
MAP_EXTENT = [50, 120, -5, 30]
VMASK = 100                                 # mask meridional wind above this
STRIDE = 15
PROJ = ccrs.PlateCarree()
UNIT = "m s\u207B\u00B9"

FILES = {
    "foam": {
        "wind_speed":      "foam_windspeed_file.nc",
        "zonal_wind":      "foam_zonal_wind_file.nc",
        "meridional_wind": "foam_meridional_wind_file.nc",
    },
    "model": {
        "wind_speed":      "model_windspeed_file.nc",
        "zonal_wind":      "model_zonal_wind_file.nc",
        "meridional_wind": "model_meridional_wind_file.nc",
    },
}

CLEVS_WIND = np.arange(5, 14, 1)
CLEVS_BIAS = np.arange(-2.5, 3, 0.5)

BOXES = [  # (x0, y0, width, height, colour)
    (50,    -2, 10, 5, "red"),
    (60.25, 18,  7, 6, "blue"),
    (88,    15,  9, 8, "red"),
]
LABELS = [(51, 5, "WEIO", 0.2), (61, 14, "NAS", 0.3), (84, 11, "NBoB", 0.3)]


# ---------------- Helpers ----------------
def load_winds(source):
    """Return dict of cropped wind fields (speed, u, v) for 'foam' or 'model'."""
    out = {}
    for var, fname in FILES[source].items():
        with xr.open_dataset(DATA_DIR / fname) as ds:
            out[var] = ds.sel(longitude=LON_SLICE, latitude=LAT_SLICE)[var].load()
    out["meridional_wind"] = out["meridional_wind"].where(out["meridional_wind"] <= VMASK)
    return out


def plot_winds(ax, speed, u, v, levels, cmap, quiver_scale):
    """Filled wind speed with subsampled wind vectors."""
    cs = ax.contourf(speed.longitude, speed.latitude, speed, levels,
                     transform=PROJ, cmap=cmap, extend="both")
    q = ax.quiver(u.longitude[::STRIDE], u.latitude[::STRIDE],
                  u[::STRIDE, ::STRIDE], v[::STRIDE, ::STRIDE],
                  width=0.0055, scale=quiver_scale)
    return cs, q


def style_axis(ax, show_ylabels):
    """Map features, region boxes/labels, ticks."""
    ax.set_extent(MAP_EXTENT, crs=PROJ)
    ax.add_feature(cfeature.LAND, facecolor="white", zorder=1)
    ax.coastlines(resolution="110m", color="black")
    ax.add_feature(cfeature.BORDERS, linewidth=0.5)

    gl = ax.gridlines(draw_labels=False, linewidth=0.5, color="gray", alpha=0.5)

    for x, y, w, h, colour in BOXES:
        ax.add_patch(Rectangle((x, y), w, h, edgecolor=colour,
                               fill=False, linewidth=2))
    for x, y, text, pad in LABELS:
        ax.text(x, y, text, fontsize=8, color="black", fontweight="bold",
                bbox=dict(facecolor="wheat", edgecolor="wheat", alpha=0.8, pad=pad))

    ax.set_yticks(range(-5, 35, 10), crs=PROJ)
    ax.yaxis.set_major_formatter(LatitudeFormatter())
    ax.set_xticks(range(50, 150, 20), crs=PROJ)
    ax.xaxis.set_major_formatter(LongitudeFormatter())
    ax.tick_params(axis="x", which="major", length=7, labelsize=12)
    ax.tick_params(axis="y", which="both", left=show_ylabels,
                   labelleft=show_ylabels, right=False, labelright=False,
                   length=7, labelsize=12)


# ---------------- Data ----------------
foam = load_winds("foam") #Add foam file here 
model = load_winds("model") #Add model file here
bias = {k: model[k] - foam[k] for k in foam} #bias between model and foam

# ---------------- Figure ----------------
fig, axes = plt.subplots(1, 3, figsize=(12, 9), sharex=True, sharey=True,
                         subplot_kw=dict(projection=PROJ),
                         facecolor="white", layout="constrained")

cs_foam, q_foam = plot_winds(axes[0], foam["wind_speed"], foam["zonal_wind"],
                             foam["meridional_wind"], CLEVS_WIND, cmo.cm.amp, 150)
cs_model, q_model = plot_winds(axes[1], model["wind_speed"], model["zonal_wind"],
                               model["meridional_wind"], CLEVS_WIND, cmo.cm.amp, 150)
cs_bias, q_bias = plot_winds(axes[2], bias["wind_speed"], bias["zonal_wind"],
                             bias["meridional_wind"], CLEVS_BIAS, cmo.cm.curl, 30)

for i, ax in enumerate(axes):
    style_axis(ax, show_ylabels=(i == 0))

titles = ["(a) UM analysis", "(b) Model", "(c) Bias (Model - UM analysis)"]
for ax, title in zip(axes, titles):
    ax.set_title(title, fontsize=12, y=0.98)

# Quiver reference keys
axes[0].quiverkey(q_foam, 2.05, -0.45, 12, f"12 {UNIT}", labelpos="E",
                  coordinates="axes", fontproperties={"size": 10})
axes[2].quiverkey(q_bias, 0.9, -0.45, 2, f"2 {UNIT}", labelpos="E",
                  coordinates="axes", fontproperties={"size": 10})

# Colorbars
cax = fig.add_axes([0.11, 0.36, 0.5, 0.012])
cbar = fig.colorbar(cs_model, cax=cax, orientation="horizontal")
cbar.set_label(f"wind speed ({UNIT})", fontsize=10)
cbar.ax.tick_params(labelsize=12)
cbar.ax.xaxis.set_ticks_position("bottom")
cbar.ax.quiverkey(q_model, X=-15, Y=-4.8, U=12, label=f"12 {UNIT}",
                  labelpos="E", coordinates="axes", fontproperties={"size": 10})

cax_bias = fig.add_axes([0.715, 0.36, 0.23, 0.012])
cbar_bias = fig.colorbar(cs_bias, cax=cax_bias, orientation="horizontal")
cbar_bias.set_label(f"wind speed bias ({UNIT})", fontsize=10, loc="right")
cbar_bias.ax.xaxis.set_ticks_position("bottom")
cbar_bias.ax.tick_params(labelsize=12)

plt.show()
