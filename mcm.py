import numpy as np
import matplotlib.pyplot as plt
import itertools
from matplotlib.colors import LogNorm

delta_vec = np.array([5, 5, 5, 4, 5], dtype=int)

def circ_diff_signed(p_next, p_i):
    return ((p_next - p_i + 6) % 12) - 6

def area_shoelace_canonical(coords):
    coords = coords[np.argsort(coords[:, 0])]
    s = coords[:, 0].astype(float)
    p = coords[:, 1].astype(int)
    n = len(coords)

    p_tilde = np.empty(n, dtype=float)
    p_tilde[0] = p[0]
    for i in range(n - 1):
        dp = circ_diff_signed(p[i+1], p[i])
        p_tilde[i+1] = p_tilde[i] + dp

    s_next = np.roll(s, -1)
    p_next = np.roll(p_tilde, -1)
    return 0.5 * abs(np.sum(s * p_next - s_next * p_tilde))


def count_induced_edges(coords):
    edges = 0
    coords = coords[coords[:, 0].argsort()]
    for i in range(len(coords) - 1):
        s1, p1 = coords[i]
        s2, p2 = coords[i+1]
        if s2 - s1 == 1 and p2 == (p1 + delta_vec[int(s1)]) % 12:
            edges += 1
    return edges

iterations =  6000000
cardinalities = [3, 4, 5, 6]
results_store = {}

for n in cardinalities:
    data = np.zeros((iterations, 2))
    print(f"Generating 6M samples for |V| = {n}...")
    
    for i in range(iterations):
        active_strings = np.sort(np.random.choice(6, n, replace=False))
        p_classes = np.random.randint(0, 12, size=n)
        coords = np.column_stack((active_strings, p_classes))
        
        data[i, 0] = count_induced_edges(coords)
        data[i, 1] = area_shoelace_canonical(coords)
    
    results_store[n] = data


global_max_area = max(data[:, 1].max() for data in results_store.values())
step = 0.5 

y_edges = np.arange(0, global_max_area + step + 0.1, step)

fig, axes = plt.subplots(2, 2, figsize=(16, 12), sharey=True)
axes = axes.flatten()

for idx, n in enumerate(cardinalities):
    ax = axes[idx]
    data = results_store[n]
    
    x_bins = np.arange(-0.5, n + 0.5, 1) 

    h = ax.hist2d(data[:, 0], data[:, 1], bins=[x_bins, y_edges], 
                  cmap='magma', norm=LogNorm(vmin=1))

    ax.set_xticks(range(n))
    ax.set_ylim(0, global_max_area + step + 0.1)
    
    ax.set_title(f"Cardinality $|V(G[C])| = {n}$")
    ax.set_xlabel("Induced Edges $|E(G[C])|$")
    if idx % 2 == 0:
        ax.set_ylabel("Harmonic-Voicing Area $A(H_C)$")
    
    fig.colorbar(h[3], ax=ax, label='Log Density')

plt.subplots_adjust(hspace=0.4, wspace=0.2, top=0.9) 

plt.suptitle(f"Global Fretboard Census: State Space Expansion ($N_{{total}} = 2.4 \\times 10^7$)", fontsize=18, y=1.03)
plt.savefig("global_fretboard_census.png")
plt.show()
