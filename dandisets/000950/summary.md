# FALCON Benchmark H2: Human Handwriting iBCI

## Abstract

This dataset represents neural activity recorded from a single participant, T5, who was enrolled in the BrainGate2 Neural Interface System clinical trial. The primary purpose of the study was to explore the potential of intracortical brain-computer interfaces (iBCIs) to decode human handwriting. Electrodes were implanted in the precentral gyrus of T5's left hemisphere, specifically targeting the hand "knob" area. During the experiment, T5 was prompted to write individual characters to form cued sentences, with each character separated by a ">" space character. The goal was to decode these handwritten characters and display them on a screen.

The study involved multiple experimental sessions where T5's neural activity was recorded across various trials categorized into different data splits. The "held-in-calib" data provides comprehensive trials for decoder calibration in the FALCON challenge, while the "held-in-minival" data serves a similar purpose but with far fewer trials. Another category, "held-out-calib," consists of separate sessions designed for few-shot recalibration. These data splits facilitate different stages of decoder development and validation. This work contributes to the ongoing development and evaluation of neural decoding algorithms for iBCI applications.

## NWB File Data Description

The NWB files in this dataset contain several key data elements including neural spike data, trial metadata, and experimental conditions. Specifically, the `acquisitions` field encompasses `binned_spikes`, which aggregates spike data in 20ms time bins, and the `eval_mask` that specifies times when the data is applicable for FALCON model training and evaluation. The `trials` field includes metadata such as the prompt or `cue` that T5 was asked to write and the `block_num` indicating the experimental block of each trial. Each trial's start and stop times are also recorded.

The files are categorized based on the type of data split they belong to, providing flexibility for different research purposes. These categories include calibration trials, validation subsets, and few-shot training sessions. Each file is encoded with neural and behavioral data from a single subject, offering rich datasets for the development and testing of handwriting decoding algorithms.

## Keywords

1. Brain-Computer Interface (BCI)
2. Intracortical Electrode Arrays
3. Neural Decoding
4. Handwriting
5. Motor Cortex
6. Spike Data
7. Neurodata Without Borders (NWB)
8. Neural Interface System
9. BrainGate2
10. FALCON Challenge