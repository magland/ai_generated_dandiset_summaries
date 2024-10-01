# FALCON Benchmark M1: Primary Motor Cortex Recordings in Primate During Reach-to-Grasp Task

This dataset consists of multiunit spiking times and behavioral data from a macaque performing a reach-to-grasp task. The experimental design involved a center-out reaching task with four different objects positioned in eight possible locations. Neural activity was recorded via electrode arrays implanted in the primary motor cortex (M1) while electromyographical (EMG) data was collected from upper limb muscles. The purpose of this investigation likely centered around understanding the neural and muscular dynamics involved in complex motor tasks, which can inform both basic neuroscience and applied fields such as neuroprosthetics and motor rehabilitation.

The dataset is part of the FALCON (Fast and Accurate Learning For COnscious Neurotechnology) Benchmark, providing a resource for developing and evaluating neural decoders. It is divided into three primary data types: `held-in-calib` for calibrating model decoders, `held-in-minival` for validating submission formats, and `held-out-calib` for few-shot recalibration. Each split is considered a distinct "subject" by the repository, ensuring rigorous testing and validation conditions. This structured approach allows for comprehensive analysis and improvement of neural decoding models.

The NWB (Neurodata Without Borders) files in this dataset include several types of recordings and metadata:
- **Behavioral Data**: Time series of preprocessed EMG from 16 muscles, including both the full EMG data and individual muscle recordings.
- **Spike Times**: Detailed spike time records from multiple electrode arrays.
- **Trial Metadata**: Key timestamps and identifiers for each trial, including `gocue_time`, `move_onset_time`, `contact_time`, `reward_time`, trial `result`, `number`, `tgt_loc`, `tgt_obj`, `obj_id`, and `condition_id`.
- **Electrophysiological Metadata**: Information about the implanted electrode arrays, including their locations, groupings, and filtering properties.

### Keywords
- Primary Motor Cortex (M1)
- Reach-to-Grasp Task
- Macaca mulatta
- Multiunit Spiking
- Electromyography (EMG)
- Neural Decoding
- Neurodata Without Borders (NWB)
- FALCON Benchmark
- Electrode Arrays
- Motor Neuroscience