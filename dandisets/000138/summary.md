## Experiment Summary

This dataset, titled "MC_Maze_Large: macaque primary motor and dorsal premotor cortex spiking activity during delayed reaching," captures neural and behavioral data from a macaque monkey performing a delayed reaching task. The experiment involved a center-out reaching task, complicated by maze-like barriers that required both straight and curved reach paths. Neural activity was recorded via electrode arrays implanted in the primary motor cortex (M1) and dorsal premotor cortex (PMd). In addition to neural data, cursor position, hand position, and eye position were tracked, with hand velocity calculated offline. This dataset aims to enhance the Neural Latents Benchmark by providing detailed recordings of neural and behavioral activity.

The primary objective of this experiment is to investigate the neural correlates of motor planning and execution in complex reaching tasks. The use of maze barriers introduces variability in movement trajectories, offering a rich dataset for studying how the brain organizes and predicts motor responses in dynamic environments. The experiment also helps in understanding the interaction between different cortical areas (M1 and PMd) during movement planning and execution, potentially contributing to the development of neural decoding algorithms and brain-machine interfaces.

## Available Data in NWB Files

### NWB File 1
- **Devices & Electrode Arrays**: Contains data from 96-electrode Utah arrays implanted in M1 and PMd.
- **Electrode Metadata**: Includes details on electrode placement, impedances, and coordinates (x, y, z).
- **Extracellular Electrophysiology Data**: Electrode group information and filtering descriptions.
- **Trials Data**: Metadata on experimental trials, including times for movement onset, start, and stop.
- **Units Data**: Spiking data across different units, including spike times and observation intervals.
- **Subject Information**: Metadata about the test subject and session specifics.

### NWB File 2
- **Devices & Electrode Arrays**: Similar to NWB File 1, contains data from 96-electrode Utah arrays in M1 and PMd.
- **Electrode Metadata**: Comprehensive data on electrode properties and spatial coordinates.
- **Trials Data**: Extensive trial information, including target positions, number of targets and barriers, and other details relevant for the Neural Latents Benchmark.
- **Processed Behavioral Data**: Includes cursor position, eye position, hand position, and hand velocity.
- **Units Data**: Spiking data with detailed observation intervals and spike timing.
- **Subject Information**: Session and subject metadata.

## Keywords
1. Motor Cortex
2. Premotor Cortex
3. Reaching Task
4. Macaque
5. Neural Spiking
6. Electrophysiology
7. Delayed Response
8. Neural Latents Benchmark
9. Electrode Arrays
10. Behavioral Data