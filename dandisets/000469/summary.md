## Abstract

This dataset contains single-neuron recordings from the human medial temporal lobe (amygdala and hippocampus) and medial frontal lobe (anterior cingulate cortex, pre-supplementary motor area, ventral medial prefrontal cortex) acquired during 41 sessions from 21 patients undergoing intracranial monitoring for epilepsy. Subjects performed a screening task to identify images that elicited highly selective neuronal responses. They then participated in a Sternberg working memory task involving the sequential presentation of 1-3 images, followed by a maintenance period and a probe matching task to test working memory. These recordings provide valuable insights into the neural mechanisms underlying working memory, particularly focusing on the role and persistence of concept cells during memory maintenance.

This dataset is formatted according to the Neurodata Without Borders (NWB) standard and includes detailed information on spike times, extracellular spike waveforms, stimuli presented, behavioral responses, electrode locations, and subject demographics. Validation of the dataset replicates prior findings concerning the persistent activity of concept cells, making it a robust resource for investigating working memory at the single-neuron level.

## Data Description

The NWB files in this dataset provide detailed insights into the single-neuron recordings and associated experimental metadata. Each NWB file contains:
- **Acquisition Events**: Time series of events for each trial, marked by TTL markers indicating specific events such as the start of the experiment, picture presentations, subject responses, and end of the experiment.
- **Devices Information**: Detailed descriptions of the recording devices, which include Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundles.
- **Electrode Groups and Electrode Table**: Information about the microwire electrodes used, including their locations and groups.
- **Stimulus Information**: Metadata regarding the stimuli presented during the tasks, including indexed image data and templates.
- **Behavioral Data**: Time intervals for trials, including start and stop times, as well as timestamps for various phases of the Sternberg task.
- **Units Data**: Detailed spike times, waveforms (mean, standard deviation, isolation distance, and signal-to-noise ratio), and their corresponding electrode information for the recorded single units.

## Keywords

- Single Neuron
- Human
- Intracranial
- Persistent Activity
- Working Memory
- Electrophysiology
- Medial Temporal Lobe
- Medial Frontal Lobe
- Spike Sorting
- NWB Format