### Abstract

In this study, we conducted a simulation of cortical Neuropixels recordings to generate ground truth data using the MEArec Python package. The simulation ran for a duration of 10 minutes and incorporated spiking activity from 250 biophysically detailed neocortical neurons. The population included 200 excitatory and 50 inhibitory cells, modeled using independent Poisson firing patterns. To replicate realistic recording conditions, Gaussian noise with a standard deviation of 10 µV was added to the signal.

The primary goal of this experiment was to create a controlled dataset that could facilitate the development and validation of spike sorting algorithms and other electrophysiological data analysis techniques. By providing a simulated environment with known ground truth, this dataset enables researchers to benchmark the performance of their analytical tools in the context of extracellular electrophysiology.

### Available Data in NWB Files

The dataset consists of three NWB files, categorized into two types. 

**Type 1 File:**
- Contains metadata about the subject and session.
- Includes spiking activity data with details on soma locations and spike times for 250 units.

**Type 2 Files:**
- Comprises acquisition details of the electrical series, metadata about extracellular electrodes (384 channels).
- Includes information on electrode group affiliation, impedance, and spatial coordinates within the electrode group.
- Metadata for each channel includes x, y, and z coordinates, as well as other relevant acquisition parameters like hardware filtering and device details.

### Keywords

- Simulated cortical recording
- Neuropixels
- Electrophysiology
- Spike sorting
- Poisson firing patterns
- Gaussian noise
- Neocortical neurons
- Extracellular recording
- MEArec Python package
- Ground truth data
