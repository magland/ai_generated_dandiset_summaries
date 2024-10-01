## Experiment Summary

The dataset presented here consists of single-neuron activity recordings from the medial temporal lobes of 59 human subjects undergoing intracranial monitoring while performing a declarative memory task. The subjects, who suffer from intractable epilepsy, were involved in a recognition memory task designed to investigate the neural mechanisms underlying human memory processes. The recognition task required participants to differentiate between images they had seen before (old) and new images, with confidence ratings recorded for their responses.

This study aims to facilitate the adoption of Neurodata Without Borders: Neurophysiology 2.0 (NWB:N) as a standardized data format in systems neuroscience by providing a comprehensive dataset along with a processing pipeline. The data and code provided are compliant with NWB:N standards, enabling interoperability between different programming languages and operating systems. The dataset includes detailed metadata, stimulus information, behavioral data, and electrophysiological recordings, making it a valuable resource for research and teaching purposes.

## Available Data in the NWB Files

The NWB files include detailed metadata about the experiments, the devices used (e.g., Neuralynx cheetah systems), and the subjects involved. Each NWB file contains event annotations corresponding to TTL markers for different phases of the learning and recognition trials. Data on trial categories, stimulus presentations, and detailed descriptions of electrode groups are also available.

The primary data include:
- **Event markers**: TTL markers indicating stimulus on/off, question screen onsets, and participant responses.
- **Experiment IDs**: Corresponding to encoding (learning) and recognition trials.
- **Extracellular electrophysiology recordings**: Metadata and recordings from multiple electrode groups using Behnke-Fried microwires.
- **Units table**: Information on neural spike units, including spike times, isolation distances, signal-to-noise ratios, and mean waveform data.
- **Trials table**: Detailed information on each trial, including stimulus category, response times, and ground truth labels for new/old stimuli.

## Keywords

- Intracranial Recordings
- Intractable Epilepsy
- Single-Unit Recordings
- Cognitive Neuroscience
- Learning
- Memory
- Neurosurgery
- Electrophysiology
- Medial Temporal Lobe
- Declarative Memory Task