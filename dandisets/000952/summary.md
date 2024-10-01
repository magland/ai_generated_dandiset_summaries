### Abstract

This dataset features local field potential (LFP) recordings from 12 male Long-Evans rats during a temporal discounting task. The recordings were conducted to examine neural activity in response to decision-making processes involving immediate versus delayed rewards. Using an RHD interface board (Intantech) and Open Ephys recording software, data were acquired at a sampling rate of 1 kHz and band-pass filtered from 0.3 to 999 Hz. The experimental setup integrated electrophysiological data with behavioral measurements through a lab-streaming-layer (LSL) protocol. The aim was to dissect the neural correlates associated with choosing between smaller, immediate rewards and larger, delayed rewards, which were varied systematically across sessions.

The behavioral protocol involved choices between a small reward (10 µL delivered after 500 ms) and a larger reward (30 µL) delivered after delays ranging from 500 ms to 20 s. This paradigm provides a framework for studying the temporal dynamics of decision-making and reward processing across different brain regions. Recordings consist of sessions that span varied delay conditions, thereby capturing a comprehensive glimpse of the neural mechanisms underlying temporal discounting.

### Description of NWB Files

The dataset comprises 21 NWB files, containing both behavioral and electrophysiological recordings. Across different sessions, the files capture:

1. Behavioral data, logged under /acquisition/ in various subdirectories, detailing the interactions and choices made by the rats during the task.
2. Electrophysiological data, organized under /acquisition/ and named based on specific recording setups (e.g., neatlabsrat2, neatlabs-HP-Z2-Mini-G3-Workstation).
3. The sessions are described in metadata fields such as session_start_time and session_description, which record the context of the experiment (e.g., Probabilistic reversal learning task).
4. Each NWB file includes the identifier and subject information under /general/subject, e.g., identifier: 09212020_Rat#R125, adding clarity about specific experimental conditions and subject details.

These detailed records enable a comprehensive understanding of how decision-making processes are mapped across various brain regions in the context of temporal discounting.

### Keywords

- Local Field Potential (LFP)
- Temporal Discounting
- Electrophysiology
- Decision Making
- Reward Processing
- Long-Evans Rats
- Behavioral Neuroscience
- Lab-Streaming-Layer (LSL)
- Intantech RHD Interface Board
- Open Ephys