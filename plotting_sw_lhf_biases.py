# --------------------------------------------------------------------
# Lodad the corresponding files for shortwave and latent heat fluxes for FOAM, control, cumulus and nudged model runs
# --------------------------------------------------------------------

foam_sw = xr.open_dataset('')
foam_lhf = xr.open_dataset('')
control_sw = xr.open_dataset('')
control_lhf = xr.open_dataset('')
cumulus_sw = xr.open_dataset('')
cumulus_lhf = xr.open_dataset('')
nudged_sw = xr.open_dataset('')
nudged_lhf = xr.open_dataset('')

# ---------------------------------------------------------------------
# Plot settings
# ---------------------------------------------------------------------
MIN_LON = 30
MAX_LON = 130
MASK_THRESHOLD = 5e10

CONTOUR_LEVELS = np.arange(-40, 45, 5)
MAP_EXTENT = [50, 120, -5, 30]
PROJECTION = ccrs.PlateCarree()

EXPERIMENT_NAMES = ["control", "cumulus", "Nudged"]

# Each row specifies its input datasets, variable, and sign convention.
FLUX_CONFIG = [
    {
        "name": "SW",
        "variable": "m01s01i202",
        "experiments": [control_sw, cumulus_sw, nudged_sw],
        "reference": foam_sw,
        "sign": 1,
    },
    {
        "name": "LHF",
        "variable": "surface_upward_latent_heat_flux",
        "experiments": [control_lhf, cumulus_lhf, nudged_lhf],
        "reference": foam_lhf,
        "sign": -1,
    },
]

# Rectangle position, width, height, and outline colour.
REGION_BOXES = [
    ((50, -2), 10, 5, "red"),
    ((60.25, 18), 7, 6, "blue"),
    ((88, 15), 9, 8, "red"),
]

# Label position, text, and background padding.
REGION_LABELS = [
    (51, 5, "WEIO", 0.2),
    (61, 14, "NAS", 0.3),
    (84, 11, "NBoB", 0.3),
]


def prepare_flux(dataset, variable):
    """Select the longitude range and mask large fill values."""
    flux = dataset[variable].sel(
        longitude=slice(MIN_LON, MAX_LON)
    ).copy()

    flux.data = ma.masked_greater(flux.data, MASK_THRESHOLD)
    return flux


# ---------------------------------------------------------------------
# Create panels and plot heat-flux biases
# ---------------------------------------------------------------------
fig, axes = plt.subplots(
    2,
    3,
    figsize=(10, 3.7),
    sharex=True,
    sharey=True,
    subplot_kw={"projection": PROJECTION},
    facecolor="white",
    layout="constrained",
)

for row, config in enumerate(FLUX_CONFIG):
    reference = prepare_flux(config["reference"], config["variable"])

    for col, (experiment_name, dataset) in enumerate(
        zip(EXPERIMENT_NAMES, config["experiments"])
    ):
        ax = axes[row, col]
        experiment = prepare_flux(dataset, config["variable"])

        # Retain the original subtraction conventions.
        if row == 0 and col == 0:
            bias = experiment - reference
        else:
            bias = experiment - reference.data

        # Express both flux rows using the downward-positive convention.
        bias = config["sign"] * bias

        contour = ax.contourf(
            experiment.longitude,
            experiment.latitude,
            bias,
            levels=CONTOUR_LEVELS,
            transform=PROJECTION,
            cmap=cmo.cm.curl,
            extend="both",
        )

        panel_label = chr(ord("a") + row * 3 + col)

        # Preserve the original SW panel's "Nudge" label.
        title_name = (
            "Nudge"
            if row == 0 and experiment_name == "Nudged"
            else experiment_name
        )

        ax.set_title(
            f"({panel_label}) {config['name']} bias "
            f"({title_name} - UM analysis) (↓)",
            fontsize=10,
        )


# ---------------------------------------------------------------------
# Shared colour bar
# ---------------------------------------------------------------------
colorbar_ax = fig.add_axes([0.18, -0.05, 0.65, 0.03])

cbar = fig.colorbar(
    contour,
    cax=colorbar_ax,
    orientation="horizontal",
)
cbar.set_label(
    "Heat flux bias (W m⁻²)",
    fontsize=11,
    loc="right",
)
cbar.ax.xaxis.set_ticks_position("bottom")
cbar.ax.tick_params(labelsize=10)


# ---------------------------------------------------------------------
# Map features, region annotations, and axis formatting
# ---------------------------------------------------------------------
for index, ax in enumerate(axes.flat):
    ax.set_extent(MAP_EXTENT, crs=PROJECTION)

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

    ax.add_feature(cfeature.LAND, facecolor="white", zorder=1)
    ax.coastlines(resolution="110m", color="black", linewidth=1)
    ax.add_feature(cfeature.BORDERS, linewidth=0.5)

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

    ax.set_yticks(range(-5, 35, 10), crs=PROJECTION)
    ax.yaxis.set_major_formatter(LatitudeFormatter())

    ax.set_xticks(range(50, 150, 20), crs=PROJECTION)
    ax.xaxis.set_major_formatter(LongitudeFormatter())

    ax.tick_params(
        axis="x",
        which="major",
        length=7,
        labelsize=10,
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
