### Abstract

This study introduces the NeuroTask benchmark dataset, which aims to support the development of advanced methodologies for multi-session, multi-task, and multi-subject neural data analysis. The dataset comprises six distinct datasets collected from motor cortical regions, encompassing seven different tasks performed by 17 subjects. The main focus of the experiment was a center-out reaching task with added perturbation, where on random trials, a manipulandum applied a perturbation to the monkey's hand during the center-hold period. This setup enables the investigation of motor control and adaptation mechanisms in response to unexpected external forces, providing valuable insights for both neuroscience research and the development of brain-machine interfaces.

Data available in the NWB files includes detailed neural and behavioral recordings from Rhesus monkeys (Macaca mulatta). Specifically, users can access spike counts per unit, hand and cursor position, velocity, force recordings, and event indications. These data are essential for exploring the neural encoding of motor actions and reactions to perturbations. The dataset also includes time series data for behavior metrics such as hand positions and velocities, as well as events like bump application and go-cue signals, facilitating comprehensive analysis of the recorded sessions.

### Data Available in NWB Files

The NWB files associated with this dataset contain:
- **Behavioral Data**: Hand and cursor position, velocity, force measurements, provided in proper units (e.g., cm, mm, radians).
- **Events Indications**: Event timing information for perturbation (bump), go-cue, target-onset, and trial results.
- **Indices**: Filtering indices on session, animal, and trial basis.
- **Spike Counts**: Neural data captured from cortical areas, thresholded online and sorted offline to identify putative single units.

### Keywords

- NeuroTask
- Motor Control
- Rhesus Monkey
- Center-Out Task
- Perturbation
- Behavioral Data
- Spike Counts
- Brain-Machine Interface
- Multitask Neural Analysis
- Neuroscience Benchmark