## Abstract

This dataset comprises multiunit spiking times and behavioral data from a macaque performing a finger movement task. The primary objective of the experiment was to study the relationship between neural activity in the primary motor cortex (M1) and finger movement, facilitated by targets cued on a screen. Neural signals were recorded using electrode arrays implanted in the M1 area, and finger positions were captured via a manipulandum. These positions were normalized between full flexion and extension. 

This dataset is part of the FALCON Benchmark challenge aimed at evaluating neural decoding models. The data are divided into three subsets: held-in-calib, held-in-minival, and held-out-calib. The held-in-calib dataset includes numerous trials for decoder calibration. The held-in-minival dataset serves as a small validation subset, while the held-out-calib dataset contains fewer trials for the purpose of few-shot recalibration. Only one monkey was used in the experiment, and different dataset splits are considered separate subjects in this repository.

## Data Description

The NWB files contain data types including 2D kinematics (`finger_vel`), multi-unit spiking activity (`units`), and metadata for FALCON evaluation (`eval_mask`). Behavioral data are segmented into 20ms bins, with potential inclusion of neural data from partial bins observed at trial ends. The experiment utilized a Blackrock Utah Array, a 2x64-channel electrode array with 96 active channels. The dataset also includes metadata on devices, electrode groups, electrode impedance values, and positional coordinates.

## Keywords

1. Primary motor cortex (M1)
2. Multi-unit spiking activity
3. Behavioral data
4. Finger movement task
5. Neural decoding
6. Electrophysiology
7. Primate research
8. FALCON Benchmark
9. Neurodata Without Borders (NWB)
10. Macaca mulatta (Rhesus monkey)