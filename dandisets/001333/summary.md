## Abstract

The Parkinson's Electrophysiological Signal Dataset (PESD) provides a comprehensive examination of electrophysiological signals obtained from both healthy and parkinsonian subjects. This dataset aims to explore the pathological biomarkers associated with Parkinson's Disease (PD) by focusing on beta oscillations, which are renowned indicators of PD symptoms. The signals were generated through a cortico-basal-ganglia network simulation based on a Parkinsonian computational model. The beta frequency band, ranging from 13 to 30 Hz, was specifically analyzed as it shows a higher power density in parkinsonian states, serving as a key symptom marker in the subthalamic nucleus (STN).

The dataset offers two types of signals: the Beta Average Rectified Voltage (ARV) and Local Field Potential (LFP) originated from synchronized neuronal activities in the cortex, STN, and thalamus. Beta ARV values are determined using a fourth-order Chebyshev band-pass filter to rectify the filtered LFP signals, which are analyzed in the frequency domain. On the other hand, LFP signals provide time-domain insights, allowing researchers to explore dynamic neurological activities. This dataset holds significant potential for informing neuromorphic controller designs for closed-loop deep brain stimulation, aiming to mitigate pathological beta oscillations in Parkinson's Disease.

## Data Description

The PESD consists of 52 NWB files capturing detailed electrophysiological data from five subjects. The data include metadata on extracellular electrodes, information on electrode groups, their locations, and their affiliations to various virtual probes utilized in NEURON simulations. Two main types of signals are outlined: Beta Band Voltage signals and LFP recordings. The files are organized into processing modules that store processed electrophysiological data from simulations. These recordings serve as a foundation for further analytical investigations focused on developing effective treatments for Parkinson's Disease.

## Keywords

- Parkinson's Disease
- Electrophysiology
- Beta Band
- Local Field Potential (LFP)
- Cortico-Basal-Ganglia Network
- Subthalamic Nucleus (STN)
- Neuromorphic Controllers
- Deep Brain Stimulation
- Computational Model
- NEURON Simulation