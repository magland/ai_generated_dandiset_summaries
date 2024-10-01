## Kriegstein2020 Dataset

### Experiment Summary

This dataset from the Kriegstein Lab, part of the Brain Initiative Cell Census Network (BICCN), is focused on intracellular electrophysiological recordings from human brain samples. The primary goal is likely to investigate the biophysical properties of human neurons, both under resting conditions and various stimulation protocols. It aims to characterize the electrical behavior of human brain neurons to better understand their functional roles, possibly in the context of development or neurodegenerative diseases.

The recordings were obtained using voltage clamp and current clamp techniques, facilitated by a MultiClamp 700 device and Clampex software version 10.3.2.1. Different stimulation protocols were applied to investigate neuron responses under varied conditions, including resting state, negative voltage, and different current steps. The dataset encompasses recordings from 38 cells across 4 human subjects, stored in 63 Neurodata Without Borders (NWB) files.

### Data Description

The NWB files in this dataset include various types of electrophysiological recordings:

- **Type 1 Files:** These contain IZeroClampSeries data, which consist of initial zero current clamp recordings under resting potential conditions. Each file includes metadata related to the intracellular electrode, the device used (MultiClamp 700), and sweep tables grouping different PatchClampSeries together.
- **Type 2 Files:** Comprising mainly VoltageClampSeries data, these files focus on neuron responses to negative voltage protocols. Multiple cycles of voltage clamp recordings are stored, along with the corresponding stimulus presentations.
- **Type 3 Files:** These files feature CurrentClampSeries data collected using negative current step protocols. They include the same series of intracellular electrode measurements and the associated sweep tables as in other file types.
- **Type 4 Files:** Similar to Type 3, these files also contain CurrentClampSeries data following the same negative current step protocols but might differ in specific experimental conditions or session details.
- **Type 5 Files:** These recordings are VoltageClampSeries under a protocol designed to study ionic currents (NaK step) with whole-cell compensation. Multiple cycles of voltage clamp recordings and corresponding stimulus presentations are included.

### Keywords
- Intracellular Electrophysiology
- Human Neurons
- Voltage Clamp
- Current Clamp
- PatchClampSeries
- Brain Initiative
- Neurodata Without Borders (NWB)
- Electrophysiological Techniques
- Neuronal Characterization
- UCSF
