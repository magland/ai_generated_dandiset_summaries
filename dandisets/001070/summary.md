## Experiment Summary

The dataset titled "LITMUS: Rat-based motor unit dataset with 0 STD waveform shape variability" comprises synthetic data generated from the MUsim repository. This dataset was created using real waveforms from 10 motor units recorded intramuscularly during the locomotion of a rat on a treadmill, captured at signal-to-noise ratios (SNR) up to 200. The primary objective of the dataset appears to be to provide a clean baseline reference for intramuscular electromyography (EMG) by using data with zero standard deviation in waveform shape variability, which implies that observed variations are fundamentally due to recording conditions and not simulated waveform distortions.

This approach offers a controlled environment to study motor unit behavior under minimal noise interference, aiding in the development and validation of computational models and methods for analyzing EMG data. By leveraging the MUsim repository, researchers can investigate the precise characteristics of motor unit action potentials (MUAPs) within the specified SNR range, fostering a better understanding of neuromuscular function and its disruption in various physiological and pathological states.

## NWB File Description

The NWB file included in this dataset encompasses several key data elements:
- **ElectricalSeries Acquisition Traces:** Comprising 8-channel EMG data collected during the rat's treadmill locomotion.
- **Electrode Metadata:** Detailed information about the electrodes used, including their grouping, channel names, and specific locations within the subject.
- **Experimental Setup:** Information about the recording devices, such as the Myomatrix RF400 ecephys probe and the Open Ephys Acquisition System, is documented.
- **General Metadata:** Details about the session, including the experimenter (Sean O'Connell), the laboratory affiliations (SNEL and Sober Lab), and the institutional background (Wallace H. Coulter Department of Biomedical Engineering, Georgia Tech, and Emory University).
- **Subject Information:** The identifier and details about the subject involved in the experiment.

## Keywords

- Motor Unit
- EMG
- Synthetic Data
- Rat
- MUsim
- SNEL
- Electrophysiology
- Neuromuscular Function
- Computational Modeling
- Motor Unit Action Potentials (MUAPs)