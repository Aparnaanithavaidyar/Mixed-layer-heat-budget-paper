# ---------------------------------------------------------------------
# Paths and plot settings
# ---------------------------------------------------------------------
DATA_DIR = Path("/Load_your_file_path/")
LOCAL_DIR = Path(".")

MIN_LON, MAX_LON = 40, 130
MIN_LAT, MAX_LAT = -20, 30
MAP_EXTENT = [50, 120, -5, 30]

PROJECTION = ccrs.PlateCarree()
SPEED_LEVELS = np.arange(0, 1.1, 0.1)
BIAS_LEVELS = np.arange(-0.5, 0.6, 0.1)

STRIDE = 11
SPEED_SCALE = 7
BIAS_SCALE = 5 * 0.8

QUIVER_STYLE = {
    "width": 0.007,
    "headwidth": 3.5,
    "headlength": 5,
    "headaxislength": 4.5,
    "color": "black",
    "alpha": 1,
    "zorder": 5,
}

DATA_CONFIG = {
    "foam": {
        "u_file": DATA_DIR / (
            "foam_xcurrent_regridded.nc"
        ),
        "v_file": DATA_DIR / (
            "foam_ycurrent_regridded.nc"
        ),
        "speed_file": LOCAL_DIR / (
            "foam_currentspeed_regridded.nc"
        ),
        "speed_variable": "currentspeed",
        "mask_threshold": 15,
    },
    "control": {
        "u_file": DATA_DIR / (
            "control_ucurrentspeed_regridded.nc"
        ),
        "v_file": DATA_DIR / (
            "model_vcurrent_regridded.nc"
        ),
        "speed_file": LOCAL_DIR / (
            "model_currentspeed_regridded.nc"
        ),
        "speed_variable": "currentspeed",
        "mask_threshold": 20,
    },
    "nudged": {
        "u_file": DATA_DIR / (
            "model_xcurrent_nudged.nc"
        ),
        "v_file": LOCAL_DIR / (
            "model_ycurrent_nudged_regridded.nc"
        ),
        "speed_file": LOCAL_DIR / (
            "model_currentspeed_nudged.nc"
        ),
        "speed_variable": "current_speed",
        "mask_threshold": 20,
    },
}

REGION_BOXES = [
    ((50, -2), 10, 5, "red"),
    ((60.25, 18), 7, 6, "blue"),
    ((88, 15), 9, 8, "red"),
]

REGION_LABELS = [
    (51, 5, "WEIO", 0.2),
    (61, 14, "NAS", 0.3),
    (84, 11, "NBoB", 0.3),
]


# ---------------------------------------------------------------------
# Load and prepare current components
# ---------------------------------------------------------------------
def load_field(path, variable, first_index=False):
    """Load a field and crop it to the selected domain."""
    with xr.open_dataset(path) as dataset:
        field = dataset[variable]

        if first_index:
            field = field[0]

        return field.sel(
            longitude=slice(MIN_LON, MAX_LON),
            latitude=slice(MIN_LAT, MAX_LAT),
        ).load()


currents = {}

for name, config in DATA_CONFIG.items():
    u = load_field(config["u_file"], "vozocrtx", first_index=True)
    v = load_field(config["v_file"], "vomecrty", first_index=True)

    # Retain the speed-file coordinates used in the original plots.
    speed_grid = load_field(
        config["speed_file"],
        config["speed_variable"],
    )

    # Preserve the original masking and speed calculation.
    v.data = ma.masked_greater(v.data, config["mask_threshold"])
    speed = (u.data**2 + v**2) ** 0.5

    currents[name] = {
        "u": u,
        "v": v,
        "speed": speed,
        "longitude": speed_grid.longitude,
        "latitude": speed_grid.latitude,
    }


# ---------------------------------------------------------------------
# Plotting helper
# ---------------------------------------------------------------------
def plot_currents(ax, longitude, latitude, speed, u, v, levels, cmap, scale):
    """Plot shaded current speed and subsampled current vectors."""
    contour = ax.contourf(
        longitude,
        latitude,
        speed,
        levels=levels,
        transform=PROJECTION,
        cmap=cmap,
        extend="both",
    )

    arrows = ax.quiver(
        u.longitude[::STRIDE],
        u.latitude[::STRIDE],
        u[::STRIDE, ::STRIDE],
        v[::STRIDE, ::STRIDE],
        transform=PROJECTION,
        scale=scale,
        **QUIVER_STYLE,
    )

    return contour, arrows


# ---------------------------------------------------------------------
# Create figure and plot absolute currents
# ---------------------------------------------------------------------
fig, axes = plt.subplots(
    2,
    3,
    figsize=(10, 4.7),
    sharex=True,
    sharey=True,
    subplot_kw={"projection": PROJECTION},
    facecolor="white",
    layout="constrained",
)

experiment_order = ["foam", "control", "nudged"]

for col, name in enumerate(experiment_order):
    fields = currents[name]

    speed_contour, speed_arrows = plot_currents(
        ax=axes[0, col],
        longitude=fields["longitude"],
        latitude=fields["latitude"],
        speed=fields["speed"],
        u=fields["u"],
        v=fields["v"],
        levels=SPEED_LEVELS,
        cmap=cmo.cm.amp,
        scale=SPEED_SCALE,
    )

axes[0, 2].quiverkey(
    speed_arrows,
    0.8,
    1.07,
    0.7,
    "0.7 m s⁻¹",
    labelpos="E",
    coordinates="axes",
    fontproperties={"size": 10},
)


# ---------------------------------------------------------------------
# Plot current-speed and vector differences
# ---------------------------------------------------------------------
comparisons = [
    ("control", "foam"),
    ("nudged", "foam"),
    ("nudged", "control"),
]

for col, (experiment_name, reference_name) in enumerate(comparisons):
    experiment = currents[experiment_name]
    reference = currents[reference_name]

    u_bias = experiment["u"] - reference["u"]
    speed_bias = experiment["speed"] - reference["speed"]

    # Preserve positional subtraction for the original control v bias.
    if experiment_name == "control" and reference_name == "foam":
        v_bias = experiment["v"] - reference["v"].data
    else:
        v_bias = experiment["v"] - reference["v"]

    bias_contour, bias_arrows = plot_currents(
        ax=axes[1, col],
        longitude=speed_bias.longitude,
        latitude=speed_bias.latitude,
        speed=speed_bias,
        u=u_bias,
        v=v_bias,
        levels=BIAS_LEVELS,
        cmap=cmo.cm.curl,
        scale=BIAS_SCALE,
    )

axes[1, 2].quiverkey(
    bias_arrows,
    0.83,
    1.07,
    0.2,
    "0.2 m s⁻¹",
    labelpos="E",
    coordinates="axes",
    fontproperties={"size": 10},
)


# ---------------------------------------------------------------------
# Colour bars
# ---------------------------------------------------------------------
colorbar_config = [
    (
        speed_contour,
        [0.25, 0.52, 0.55, 0.02],
        "Current speed (m s⁻¹)",
    ),
    (
        bias_contour,
        [0.25, 0.02, 0.55, 0.02],
        "Current speed bias (m s⁻¹)",
    ),
]

for contour, position, label in colorbar_config:
    colorbar_ax = fig.add_axes(position)
    cbar = fig.colorbar(
        contour,
        cax=colorbar_ax,
        orientation="horizontal",
    )
    cbar.set_label(label, fontsize=10, loc="right")
    cbar.ax.xaxis.set_ticks_position("bottom")
    cbar.ax.tick_params(labelsize=12)


# ---------------------------------------------------------------------
# Map formatting and panel titles
# ---------------------------------------------------------------------
panel_titles = [
    "(a) UM analysis",
    "(b) Control",
    "(c) Nudged",
    "(d) Control - UM analysis",
    "(e) Nudged - UM analysis",
    "(f) Nudged - Control",
]

for index, (ax, title) in enumerate(zip(axes.flat, panel_titles)):
    ax.set_extent(MAP_EXTENT, crs=PROJECTION)
    ax.set_title(title, fontsize=10, y=0.96)

    for position, width, height, colour in REGION_BOXES:
        ax.add_patch(
            Rectangle(
                position,
                width,
                height,
                color=colour,
                fill=False,
                linewidth=2,
                transform=PROJECTION,
            )
        )

    for lon, lat, label, padding in REGION_LABELS:
        ax.text(
            lon,
            lat,
            label,
            fontsize=8,
            color="black",
            fontweight="bold",
            transform=PROJECTION,
            bbox={
                "facecolor": "wheat",
                "edgecolor": "wheat",
                "alpha": 0.8,
                "pad": padding,
            },
        )

    gridlines = ax.gridlines(
        draw_labels=True,
        linewidth=0.5,
        color="gray",
        alpha=0.5,
    )
    gridlines.top_labels = False
    gridlines.right_labels = False
    gridlines.bottom_labels = False
    gridlines.left_labels = False

    ax.add_feature(cfeature.LAND, facecolor="white", zorder=1)
    ax.coastlines(resolution="110m", color="black")
    ax.add_feature(cfeature.BORDERS, linewidth=0.5)

    ax.set_yticks(range(-5, 35, 10), crs=PROJECTION)
    ax.yaxis.set_major_formatter(LatitudeFormatter())

    ax.set_xticks(range(50, 150, 20), crs=PROJECTION)
    ax.xaxis.set_major_formatter(LongitudeFormatter())

    ax.tick_params(
        axis="x",
        which="major",
        length=7,
        labelsize=12,
    )
    ax.tick_params(
        axis="y",
        which="both",
        left=index in (0, 3),
        labelleft=index in (0, 3),
        right=False,
        labelright=False,
        length=7,
        labelsize=12,
    )

plt.show()
