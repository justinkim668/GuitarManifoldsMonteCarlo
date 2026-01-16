# GuitarManifoldsMonteCarlo
This repository provides the computational foundation for a 31-page research manuscript titled "METRIC INDEPENDENCE IN DISCRETE CYLINDRICAL MANIFOLDS," where we explore the geometric properties of the pitch class space in the guitar. The core of the framework is an isometric lift—conceptually analogous to a Nash Embedding—which "unrolls" the discrete cylindrical manifold $G$ of the fretboard into a Euclidean universal cover $\mathbb{R}^2$.

By mapping chordal voicings into this Euclidean plane, we derive a unique geometric signature (Harmonic Area and Shape Vector) for guitar chord vocings that resolves the "Spectral Blindness" inherent in unweighted graph models. The provided Monte Carlo simulation of $2.4 \times 10^7$ total iterations validates the Metric Independence Thesis (independence of local connectivity and global compactness), empirically identifying the chiral fault line between the G-B strings on the guitar, and parity-locked area quantization across the manifold.

# Problem Statement
Traditional unweighted graphs cannot distinguish between functionally different chord voicings because the collapse into the same "linear forest."

# Our Solution
This repository utilizes a geometric lifting logic that maps guitar chords to universal Euclidean cover $\mathbb{R}^2$ to calculate their Harmonic-Voicing Area ($A(H_C)$).
