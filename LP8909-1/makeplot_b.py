import pathlib
import sys

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
#import vplot

#import vplanet

# Path hacks
path = pathlib.Path(__file__).parents[0].absolute()
sys.path.insert(1, str(path.parents[0]))
from get_args import get_args

# Tweak
plt.rcParams.update({"font.size": 16, "legend.fontsize": 16})

# Run vplanet
#output = vplanet.run(path / "vpl.in", units=False)
output_b = np.loadtxt('/Users/mwjl/Documents/LP890-9/LP890-9/LP8909.b.forward')
output_c = np.loadtxt('/Users/mwjl/Documents/LP890-9/LP890-9/LP8909.c.in.forward')

# Age -Luminosity -LXUVStellar -Radius Temperature

time = output_b[:,0]
planets = output_b[1:]
water = output_b[:,1]
oxygen = output_b[:,3]

time_c = output_c[:,0]
planets_c = output_c[1:]
water_c = output_c[:,1]
oxygen_c = output_c[:,3]

# Plot
fig, ax = plt.subplots(1, 2, figsize=(12, 3))
fig.subplots_adjust(wspace=0.2)
ax[1].plot(time, oxygen)
ax[1].plot(time_c, oxygen_c)

# Legend
leg = ax[0].legend(
    lines,
    ("1 TO", "3 TO", "5 TO"),
    loc=("upper right"),
    handletextpad=0.1,
    title="Initial water",
)
plt.setp(leg.get_title(), fontsize=12, fontweight="bold")

# Watson et al (1981) result
ax[0].axvline(280e6, color="k", lw=1, ls="--")
ax[0].annotate(
    "Watson+81 timescale",
    xy=(280e6, 1),
    xycoords="data",
    textcoords=("offset points"),
    xytext=(5, 0),
    ha="left",
    va="center",
    fontsize=12,
    color="k",
)

# Tweaks
ax[0].set_xlabel("Time (years)")
ax[1].set_xlabel("Time (years)")
ax[0].set_ylabel("Surface Water (TO)")
ax[1].set_yscale("log")
ax[1].set_ylabel("Absorbed O$_2$ (bar)")
ax[0].set_xlim(5e7, 4.6e9)
ax[1].set_xlim(5e7, 4.6e9)
for axis in ax.flatten():
    axis.set_xscale("log")


# Save the figure
ext = get_args().ext
fig.savefig(path / f"VenusWaterLoss.{ext}", bbox_inches="tight")