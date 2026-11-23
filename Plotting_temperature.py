# ---------------- Settings ----------------
LON_MIN, LON_MAX = 30, 130
DEPTH = 0
FILL_THRESHOLD = 5e10
PROJ = ccrs.PlateCarree()

CLEVS = np.arange(25, 31.5, 0.5)
CLEVS_BIAS = np.arange(-1.2, 1.4, 0.2)

# (x0, y0, width, height, colour)
BOXES = [
    (50,    -2, 10,  5, "red"),
    (60.25, 18,  7,  6, "blue"),
    (100,   -6,  5, -5, "blue"),
    (85.5,  14,  7,  8, "red"),
]
# (x, y, label)
LABELS = [(51, -6, "EEIO"), (61, 13, "N.AS"), (100, -15, "S.JAVA")]


# ---------------- Helpers ----------------
def prepare(da, lon_min=LON_MIN, lon_max=LON_MAX, depth=DEPTH):
    """Crop longitude, select nearest depth level, mask fill values."""
    da = da.sel(longitude=slice(lon_min, lon_max))
    da = da.sel(deptht=depth, method="nearest")
    return da.where(da <= FILL_THRESHOLD)


def decorate(ax, title, show_left_labels):
    """Coastlines, gridlines, region boxes, region labels and title."""
    ax.coastlines(resolution="110m", linewidth=1)
    gl = ax.gridlines(draw_labels=True)
    gl.top_labels = False
    gl.right_labels = False
    gl.left_labels = show_left_labels
    for x, y, w, h, colour in BOXES:
        ax.add_patch(Rectangle((x, y), w, h, edgecolor=colour,
                               fill=False, linewidth=2))
    for x, y, text in LABELS:
        ax.text(x, y, text, fontsize=8, color="black")
    ax.set_title(title)


def add_colorbar(fig, mappable, rect):
    cax = fig.add_axes(rect)
    cbar = fig.colorbar(mappable, cax=cax, orientation="horizontal")
    cbar.set_label("\u00b0C", fontweight="bold")
    cbar.ax.xaxis.set_ticks_position("bottom")
    return cbar


# ---------------- Data ----------------
foam  = prepare(foam_monsoon.votemper)
model = prepare(model_monsoon.votemper)
bias  = model - foam.data          # same grid assumed, as in the original

# ---------------- Figure ----------------
fig, axes = plt.subplots(
    1, 3, figsize=(12, 10), sharex=True, sharey=True,
    subplot_kw=dict(projection=PROJ), facecolor="white", layout="constrained",
)
fig.suptitle(
    "Lead day : 30, Composite months : JJAS, composite years: 2018-2023 Wind Reg Nudge",
    y=0.68, fontsize=10, fontweight="bold",
)

panels = [
    (foam,  "(a) FOAM",               CLEVS,      "Reds"),
    (model, "(b) Model",              CLEVS,      "Reds"),
    (bias,  "(c) Bias (Model - FOAM)", CLEVS_BIAS, "RdBu_r"),
]

contours = []
for i, (ax, (data, title, levels, cmap)) in enumerate(zip(axes, panels)):
    cs = ax.contourf(data.longitude, data.latitude, data, levels,
                     transform=PROJ, cmap=cmap, extend="both")
    decorate(ax, title, show_left_labels=(i == 0))
    contours.append(cs)

add_colorbar(fig, contours[1], [0.15, 0.34, 0.45,  0.015])
add_colorbar(fig, contours[2], [0.65, 0.34, 0.30,  0.015])

plt.show()
