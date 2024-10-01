## Experiment Summary

This dataset comprises extracellular electrophysiology (ecephys) recordings, sourced from the Allen Institute for Brain Science, focused on mouse visual areas. The recordings align with the stimulus set used in the Allen Brain Observatory's two-photon calcium imaging experiments. The objective is likely centered on understanding neural encoding of various visual stimuli, comparing the electrical activities gathered from Neuropixels probes with those from calcium imaging to provide a comprehensive view of visual processing in the mouse brain.

The experiments involved presenting a varied set of visual stimuli to awake, head-fixed mice, while capturing neural responses through multiple Neuropixels probes inserted into different brain regions. A range of visual stimuli including natural scenes, movies, static and drifting gratings, and Gabors were presented to assess how different types of visual information are processed across populations of neurons in the mouse visual cortex.

## Available Data in NWB Files

1. **General Metadata and Device Information**:
    - Data about extracellular electrodes, including filtering descriptions, group affiliations, impedances, locations, and coordinates.
    - Information on ecephys probes (probes A through F), electrode groups, and the dataset's subject metadata.

2. **Running Wheel**:
    - Time series data on raw running wheel rotation, signal voltage, and supply voltage.

3. **Visual Stimulus Presentations**:
    - Detailed time intervals and descriptors for various visual stimuli including drifting gratings, flashes, Gabors, natural movies, and static gratings such as start and stop times, orientation, contrast, spatial and temporal frequency, and other parameters.

4. **Neural Responses**:
    - Spike times, amplitudes, waveforms, and other metrics such as firing rates and isolation distances across recorded units.

5. **LFP Data**:
    - Local field potential (LFP) recordings and metadata, filtered for signal processing, from different probes labeled as 810755797, 810755799, 810755801, and 810755803.

6. **Current Source Density (CSD)**:
    - Precalculated CSD data based on interpolated electrode locations, providing insights into the spatial distribution of current sources and sinks in the neural tissue.

7. **Processing Modules**:
    - Various processing modules containing data and metadata related to eye-tracking, optogenetic stimulation, and running speed.

## Keywords
1. Extracellular Electrophysiology
2. Visual Cortex
3. Neuropixels
4. Mouse Brain
5. Visual Stimuli
6. Spike Sorting
7. Local Field Potentials
8. Current Source Density
9. Allen Brain Observatory
10. Neural Encoding