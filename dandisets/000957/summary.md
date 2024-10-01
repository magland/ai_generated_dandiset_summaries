## Neuropixels Ultra Probe Imposed Motion Dataset

### Abstract
The Neuropixels Ultra Probe Imposed Motion Dataset investigates neural activity in the visual cortex of awake mice. Utilizing the high-density Neuropixels Ultra probe, with 6-micron center-to-center spacing between sites, the dataset encompasses 6x48 site configurations across 48x288 microns. During recording sessions, a total of 19 directional steps of 25 μm in each direction were imposed on the probes to induce motion within the brain tissue. The experiment employed two primary sessions, each featuring sequences of natural image stimuli presented before and after the imposed motion, offering detailed profiles of the visual cortical neurons' unique responses.

The dataset's objective is to design and validate spike sorting algorithms by providing neural activity data sampled at unprecedented spatiotemporal resolution. The imposed motion and neural identification pre- and post-motion serve as ground truth references, enhancing the accuracy of motion correction and spike sorting methods. This comprehensive dataset supports a deeper understanding of neural dynamics influenced by mechanical displacements and visual stimulus responses.

### Data Description
The Dandiset 000957 comprises 10 NWB files from 5 subjects, totaling over 530 GB in data. The dataset predominantly features the following types of data entries:

- **Electrical Series**: Primary recordings of neural activity, including both action potentials (ElectricalSeriesAP) and low-frequency signals (ElectricalSeriesLF), captured by 384 electrodes.
- **Manipulator Trigger Signals**: Analog signals documenting the manipulator's up and down movements during brain recordings.
- **Stimulus Presentations**: Detailed recordings of the stimulus presentations involving 118 natural images. This includes both pre-motion and post-motion stimulus indices and durations.
- **Extracellular Electrode Metadata**: Comprehensive metadata about electrode configurations, gains, locations, and groupings within subjects.
- **Devices Information**: Specifications and descriptives of the Neuropixels Ultra probes used in the experiments.

### Keywords
1. Neuropixels ultra
2. Imposed motion
3. Visual cortex
4. Spike sorting
5. Awake mouse
6. Natural image stimuli
7. Electrophysiology
8. Neural activity
9. Motion correction
10. Visual response fingerprinting