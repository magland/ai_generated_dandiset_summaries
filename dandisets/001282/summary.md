## Abstract

This dataset encompasses recordings from Neuropixels probes inserted into the brain of a non-human primate (Macaca mulatta) to capture neuronal activity during deep probe insertions. The recordings were coordinated by Eric Trautmann under the guidance of senior neuroscientists Mike Shadlen and Mark Churchland, and form the basis for analyses presented in Windolf et al.'s study on robust motion correction techniques for high-density extracellular recordings, which is slated for publication in *Nature Methods*. The goal of this research is to address the challenges posed by motion artifacts in recordings, a common issue when assessing neuronal activity in awake, freely-moving subjects. By enhancing the fidelity of neural data collected during such conditions, this work aids in more accurate brain mapping efforts and the study of neural dynamics.

The experiments utilized the Neuropixels 1.0 probes, which offer high-resolution recordings across numerous channels, enabling comprehensive coverage of brain activity. The recordings were completed using a multi-electrode extracellular electrophysiology approach, capturing detailed electrical series data that inform on both single-neuron and population-level neural processing. This methodology supports the investigation of large-scale, brain-wide neural interactions critical for understanding sensory processing, movement, cognition, and other complex behaviors in non-human primates.

## Data Description

The NWB files available in this dataset contain acquisition traces captured as `ElectricalSeries` for both action potentials (`ElectricalSeriesAP`) and local field potentials (`ElectricalSeriesLF`). The dataset includes metadata about the electrodes, structured in a `DynamicTable`, which provides information such as electrode identification, channel names, contact shapes, and location within the brain. Each NWB file includes a detailed mapping of 384 electrodes for each `ElectricalSeries`, reflecting the comprehensive neural data collection. The recordings also contain session-specific metadata, including device details, session timing, and subject identification. All data adhere to the Neurodata Without Borders (NWB) standard, ensuring compatibility and ease of use for future research.

## Keywords

- Neuropixels
- Macaca mulatta
- Non-human primate
- Extracellular electrophysiology
- Motion correction
- Neural recording
- Brain mapping
- High-density electrodes
- Action potentials
- Local field potentials