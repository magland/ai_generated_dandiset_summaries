## Abstract

This dataset contains electrophysiological recordings from the dorsomedial frontal cortex (DMFC) of a Rhesus monkey (Macaca mulatta) engaged in a time-interval reproduction task. The monkey, named Haydn, was trained to reproduce a specific time interval between two sequentially presented stimuli by timing his response accordingly. The primary aim was to understand the neural substrates underlying cognitive timing and interval reproduction, focusing on spiking activity in the DMFC, a brain region implicated in such tasks. Neural activity was captured using linear probes with 24 recording channels each, and the data was utilized for the Neural Latents Benchmark project.

Neural data were recorded in sessions on December 11, 2016, and include detailed descriptions of each experimental trial, such as timings for different task-related events, success or failure of each trial, and reaction times. This information, alongside spike times and metadata about the recording electrodes, offers a comprehensive resource for investigating the neural dynamics of cognitive timing and decision-making processes.

## Data Description

### NWB File Type 1:

- **General Information**:
  - Neural recordings from 72 electrodes across three linear probes.
  - Metadata includes device descriptions and electrode coordinates.
  - Subject and institutional details: Massachusetts Institute of Technology, Monkey Haydn (subject identifier: 8d26aa92-3929-11ec-8077-43176b153428).

- **Experimental Trials**:
  - Trial timestamps for onsets and offsets.
  - Response times (go_time) and trial categorization (train, val, test).
  
- **Units Data**:
  - Spike times, observation intervals, and unit IDs.
  - Indicates whether units are held out for validation (40 units).

### NWB File Type 2:

- **General Information**:
  - Similar electrode and device metadata as Type 1.
  - Subject identifier: 8969f328-3929-11ec-8077-43176b153428.
  
- **Experimental Trials**:
  - Detailed trial metrics including fixation times, target acquisition, and reward times.
  - Additional trial attributes such as intertrial interval (iti), trial types (is_eye, is_short, is_outlier), and response direction (theta).

- **Units Data**:
  - Comprehensive spike times for 54 units.
  - Information about whether units are part of the held-out set for benchmarks.

## Keywords

1. Dorsomedial Frontal Cortex
2. Cognitive Timing
3. Time Interval Reproduction
4. Electrophysiology
5. Macaque
6. Spike Sorting
7. Neural Recording
8. Cognitive Neuroscience
9. Neurodata Without Borders (NWB)
10. Neural Latents Benchmark