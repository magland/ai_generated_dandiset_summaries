# Scientific Abstract

The Dandiset titled "Spike Sorting Biases in a Detailed Model of Dense Large-Scale Recordings" investigates the systematic biases that can arise in spike sorting processes when applied to densely packed neural recordings. This study utilizes biophysically detailed simulations of neuropixel probes within spontaneous activity regimes to explore these biases in the context of large-scale neural data acquisition. By fitting the background noise and gain parameters to the Marques-Smith dataset, the study aims to provide insights into how spike sorting algorithms may inaccurately represent neuronal spike data when applied to high-density settings, potentially impacting neuroscientific conclusions drawn from such data.

Core to the experiment is the examination of various configurations including disconnected circuits and different probe depths, with a particular focus on characterizing spike detection variability. The study's approach combines advanced electrophysiological simulation techniques to emulate realistic neural environments, offering a unique perspective on the effects of spike sorting under varied experimental conditions. The ultimate objective is to enhance the accuracy of neuronal data interpretation, thereby improving our understanding of neural network dynamics in both artificial and natural settings.

# Data Description

The dataset comprises 17 NWB files divided into five groups, each representing different experimental conditions. Type 1 files focus on biophysical simulations of neuropixels in spontaneous regimes with 384 electrode configurations, documenting raw electrical recordings and metadata on electrode properties, as well as spike times for each detected unit. Type 2 files similarly concern biophysical simulations, but provide additional detail on unit-specific characteristics such as dynamics and morphology. Type 3 files describe simulations at a specific probe depth with reduced electrode count, focusing on spike timing data. Type 4 and Type 5 files delve into the dynamics of a disconnected neural circuit, recording robust metadata regarding unit dynamics, electrode configurations, and spike timing across 384 electrodes. Together, these datasets enable a comprehensive analysis of spike sorting biases across varied simulation setups.

# Keywords

- Biophysical Simulation
- Dense Extracellular Recordings
- Spike Sorting
- Neuropixels
- Electrophysiology
- Neural Data Analysis
- Electrode Configuration
- Neural Network Dynamics
- Spike Times
- Disconnected Circuit