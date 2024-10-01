## Experiment Summary

This study examines the voltage contrast of JEDI2P and Voltron2_JF525 under both one-photon (1P) and two-photon (2P) illumination conditions. Conducted at Harvard University in the Adam Cohen Lab, the experiment aimed to assess the performance and efficacy of these voltage-sensitive fluorescent probes when subjected to different photonic excitation methods. The experimental setup was configured to acquire high-resolution imaging and electrophysiological data, providing a comprehensive evaluation of these probes' behavior in response to voltage changes.

The dataset includes a total of 11 Neurodata Without Borders (NWB) files, each representing a distinct experimental session. The goal was to determine the relative advantages and limitations of these probes, which could have significant implications for future research in neurophysiology and optogenetics. By comparing the performance of JEDI2P and Voltron2_JF525, the study sought to identify the optimal conditions for utilizing these probes in various scientific investigations.

## Data Description

The NWB files contain detailed experimental data, including imaging and time-series recordings. Each file encompasses the following elements:

- **Confocal Imaging Data**: Captured using the Deepsee confocal microscope and stored in the `/acquisition/Confocal_1` group.
- **Camera Data**: Image series recorded with an Optopatch Camera, annotated in the `/acquisition/camera_1` group.
- **Electrophysiological Data**: Multiple time-series data channels, including:
  - **Patch Feedback (aif_1: PatchFB)**
  - **2P Excitation Feedback (aif_2: 2Prefpd)**
  - **488 nm Acousto-Optic Tunable Filter (aof_1: 488 AOTF)**
  - **Electro-Optic Modulator (aof_2: EOM)**
  - **Patch Voltage (aof_3: PatchV)**
  - **1P Shutter Control (dof_1: 1P Shutter)**
  - **2P Shutter Control (dof_2: 2P Shutter)**
- **Device Information**: Details about the equipment used, including the Adaptive_Upright Rig and associated Git information provided in the `/general/devices` group.
- **Subject Information**: Metadata on the experimental subjects, including unique identifiers and session descriptions under the `/general/subject` group.

## Keywords

1. JEDI2P
2. Voltron2_JF525
3. One-Photon Illumination
4. Two-Photon Illumination
5. Voltage-Sensitive Probes
6. Electrophysiology
7. Confocal Imaging
8. Harvard University
9. Adam Cohen Lab
10. Optogenetics