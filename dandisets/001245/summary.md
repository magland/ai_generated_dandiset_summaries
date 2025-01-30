## Abstract

This study investigates the neural correlates of song production in zebra finches by utilizing advanced Neuropixels probes to record premotor and motor neural activity from the robust nucleus of the arcopallium (RA) during natural singing behaviors. This work is part of the FALCON Benchmark, an initiative aimed at improving machine learning models for decoding neural data. The dataset provides unprocessed broadband recordings intended to serve as a calibration tool for models and includes multiple trials for validating model submissions. This experimental setup captures the complex interplay between neural signals and song acoustics, aiming to further our understanding of the motor control of vocalization and to refine neural decoding algorithms.

The experiment involves a single zebra finch subject, meticulously recording both neural and vocal data across multiple sessions. The specific focus is on synchronous data acquisition during epochs of awake singing. The dataset is divided into multiple components to cater to various analytical needs of the FALCON challenge, namely 'held-in-calib', 'held-in-minival', and 'held-out-calib'. These components are specifically designed for calibrating and validating machine learning models, as well as for testing few-shot recalibration capabilities. This comprehensive approach ensures a robust dataset that facilitates a multitude of research and development efforts within the domain of auditory neuroscience and neuroethology.

## NWB Files Data Description

The NWB files encompass two main datasets. The first type includes broadband neural recordings at a 30 kHz sampling rate, audio spectrograms, trial intervals, and vocalization waveforms synchronized with neural timestamps. The second dataset type provides threshold crossings extracted at the same neural sampling rate, along with spectrogram data and vocalization waveforms. Each file documents detailed metadata, such as session information, audio evaluation masks, and spectrogram parameters. The trials include temporal markers and associated frequency and time vectors essential for spectral analysis and evaluation within the context of song production.

## Keywords

- Zebra finch
- Neuropixels
- Neural recordings
- Birdsongs
- Song motor nucleus RA
- Vocalization
- FALCON Benchmark
- Neural decoding
- Spectrogram analysis
- Auditory neuroscience