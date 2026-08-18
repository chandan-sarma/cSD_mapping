import re
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

# --------- CONFIG ---------
files = [
    "file1.txt", "file2.txt", "file3.txt",
    "file4.txt", "file5.txt", "file6.txt"
]

ref_value = -41.5038

group1 = files[:3]
group2 = files[3:]

labels = ["SD map", "pnSD map", "cSD map"]

highlight_min, highlight_max = 1000, 2600

# --------- PARSER FUNCTION ---------
def extract_data(filename):
    eval_counts = []
    energies = []
    
    pattern = r"Eval count:\s*(\d+).*?Energy:\s*([-+]?\d*\.\d+|[-+]?\d+)"
    
    with open(filename, 'r') as f:
        text = f.read()
        matches = re.findall(pattern, text)
        
        for m in matches:
            eval_counts.append(int(m[0]))
            energies.append(float(m[1]))
    
    return eval_counts, energies

# --------- STYLE ---------
plt.rcParams.update({
    "font.size": 12,
    "font.family": "serif",
    "axes.labelsize": 14,
    "legend.fontsize": 10,
    "xtick.labelsize": 11,
    "ytick.labelsize": 11
})

fig, axes = plt.subplots(2, 1, figsize=(6, 8), sharex=True)

# --------- FIRST SUBPLOT (COBYLA) ---------
for i, file in enumerate(group1):
    x, y = extract_data(file)
    axes[0].plot(x, y, linewidth=1.5, label=labels[i])

axes[0].set_xlim(0, 3000)
axes[0].set_ylabel("Binding energy (MeV)")
axes[0].grid(True, alpha=0.5)
axes[0].axhline(y=ref_value, color='k', label='Reference Energy')

axes[0].text(0.12, 0.92, "(a) COBYLA",
             transform=axes[0].transAxes,
             fontsize=13, fontweight='bold')

axes[0].legend()


# --- Inset for COBYLA ---
axins0 = inset_axes(axes[0], width="40%", height="30%", loc='center right')

for file in group1:
    x, y = extract_data(file)
    axins0.plot(x, y, linewidth=1.2)

axins0.set_xlim(highlight_min, highlight_max)

# Auto y-limits
all_y0 = []
for file in group1:
    x, y = extract_data(file)
    all_y0 += [yy for xx, yy in zip(x, y) if highlight_min <= xx <= highlight_max]

if all_y0:
    axins0.set_ylim(min(all_y0), max(all_y0))

axins0.grid(True, alpha=0.4)

# --------- SECOND SUBPLOT (SLSQP) ---------
for i, file in enumerate(group2):
    x, y = extract_data(file)
    axes[1].plot(x, y, linewidth=1.5, label=labels[i])

axes[1].set_xlim(0, 3000)
axes[1].set_xlabel("Number of iterations")
axes[1].set_ylabel("Binding energy (MeV)")
axes[1].grid(True, alpha=0.5)
axes[1].axhline(y=ref_value, color='k', label='Reference Energy')

axes[1].text(0.12, 0.92, "(b) SLSQP",
             transform=axes[1].transAxes,
             fontsize=13, fontweight='bold')

axes[1].legend()

# --- Inset for SLSQP ---
axins1 = inset_axes(axes[1], width="40%", height="30%", loc='center right')

for file in group2:
    x, y = extract_data(file)
    axins1.plot(x, y, linewidth=1.2)

axins1.set_xlim(highlight_min, highlight_max)

# Auto y-limits
all_y1 = []
for file in group2:
    x, y = extract_data(file)
    all_y1 += [yy for xx, yy in zip(x, y) if highlight_min <= xx <= highlight_max]

if all_y1:
    axins1.set_ylim(min(all_y1), max(all_y1))

axins1.grid(True, alpha=0.4)

#axins0.set_xlim(highlight_min, highlight_max + 75)
#axins1.set_xlim(highlight_min, highlight_max + 75)


# --------- LAYOUT ---------
plt.tight_layout()
plt.savefig("10B_vqe.png", dpi=300, bbox_inches='tight')
plt.savefig("10B_vqe.pdf", bbox_inches='tight')
plt.show()
