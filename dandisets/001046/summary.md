# FALCON Benchmark B1: Zebra Finch RA Neuropixels Recordings During Birdsong

## Scientific Abstract

This dataset is part of the FALCON Benchmark B1 project, which aims to provide a comprehensive collection of neural and vocal data from zebra finches (Taeniopygia guttata) during natural singing behavior. Neural activity was recorded using Neuropixels probes implanted in the premotor and motor nuclei of the birds while capturing simultaneous audio recordings of their vocalizations. This study's primary goal is likely to understand the neural mechanisms underlying song production and to develop and benchmark neural decoding algorithms as part of the FALCON challenge.

The recordings include unsorted spike times, raw audio data, and precomputed spectrograms, specifically focusing on the RA nucleus crucial for song production. The dataset is partitioned into three subsets: 'held-in-calib,' 'held-in-minival,' and 'held-out-calib,' each serving a distinct purpose within the evaluation framework of the FALCON challenge. This segregation aids in model calibration, validation, and few-shot learning tasks, respectively. Researchers are advised to take these distinctions into account when using the dataset for purposes beyond the stated FALCON Benchmark.

## Description of Available Data in NWB Files

Each of the 9 NWB files in this dataset contains the following data:
- **Acquisitions**:
  - **tx (Threshold Crossings)**: Raw neural data at 30 kHz sampling rate.
  - **vocalizations**: Amplitude waveform of vocal recordings at 25 kHz sampling rate.
  - **eval_mask_audio**: Mask indicating timestamps considered during FALCON evaluation.

- **Trials**:
  - **spectrogram_times**: Time steps associated with spectrogram values.
  - **spectrogram_frequencies**: Frequency bands of the spectrogram.
  - **spectrogram_values**: Values of the spectrogram data.
  - **spectrogram_eval_mask**: Mask specifying which spectrogram time-frequency points are used for evaluation.
  - **start_time** and **stop_time**: Start and stop times of each trial.

The dataset thus encompasses vital neural and audio recordings, essential for decoding tasks, and provides all necessary metadata, including the species, experiment description, and detailed trial information.

## Keywords

1. Zebra Finch
2. Birdsong
3. Neuropixels
4. Neural Recording
5. Vocalization
6. RA Nucleus
7. Spectrogram
8. Unsorte Spike Times
9. Song Production
10. Neural Decoding

---

This content is formatted in raw markdown suitable for copy/paste into a `.md` document.