# Large-scale Neuropixels Recordings Through SHIELD Implant During Visual Change Detection Task with Dynamic Gating of Engagement

This dataset, collected at the Allen Institute, comprises 99 electrophysiology sessions featuring multi-Neuropixel recordings across the left hemisphere of mice during a visual change detection task. The recordings capture neural activity from various brain regions, including frontal and medial cortical areas as well as the striatum. This dataset extends the Allen Institute Visual Behavior Neuropixels (VBN) dataset by including these additional brain regions and by modifying the behavioral task to experimentally manipulate engagement levels. During sessions, an active behavior block is followed by a 'no-reward' block where the lick spout remains extended, but visual changes no longer yield rewards. This setup is intended to analyze how task engagement impacts brain activity, as some mice resume licking once rewards are reintroduced at the end of this 'no-reward' block through auto-rewards.

The dataset aims to provide insights into the neural dynamics of visual processing and task engagement by using a modified visual change detection paradigm. To facilitate this, it features extensive metadata and tutorials to support users in accessing and analyzing the data. The dataset includes low-frequency (LFP) recordings for up to six probes per session, each identified by a specific probe ID. Each session's NWB file contains a probe table linking session data to corresponding LFP recordings, enabling comprehensive multi-session analysis. This dataset also includes metadata tables and example scripts (available on GitHub) to guide users through the data structure and processing methods.

## Available Data in NWB Files

The NWB files store the following types of data:

- **Session Metadata:** Contains details about the session description, session start time, and devices used (e.g., Neuropixels 1.0 Probes).
- **Electrophysiological Data:** This includes raw data from extracellular electrodes, metadata about electrode groups, filtering information, electrode impedance, and their spatial coordinates.
- **Low-Frequency (LFP) Data:** ElectricalSeries data specific to each probe, capturing the low-frequency components of the recorded signals, including metadata and references to electrodes.
- **Behavioral Data:** Time series and events related to eye tracking (e.g., pupil and corneal reflection tracking), running wheel voltage signals, licking behavior, and rewards.
- **Stimulus Presentation:** Time intervals for various stimuli (e.g., dynamic routing image sets, flash and Gabor stimuli) providing detailed information about presentation times, stimulus characteristics, and reward contingencies.
- **Trial Information:** Data on experimental trials including trial start and stop times, response times, rewarded/unrewarded flags, and lick times.

## Keywords

- Electrophysiology 
- Visual Behavior 
- Neuropixels 
- Mouse Brain 
- Task Engagement 
- Low-Frequency Potentials (LFP)
- Behavioral Neuroscience 
- Visual Change Detection 
- Brain Mapping 
- Neural Dynamics
