## Abstract
The NeuroTask dataset is a comprehensive benchmark aimed at advancing the analysis of neural data across multiple sessions, tasks, and subjects. This dataset encompasses recordings from motor cortical regions (M1 and S1) in 17 subjects performing seven distinct tasks. Collected data include spike counts, behavioral metrics (e.g., hand and cursor positions, velocity, and force), and event markers. Such a rich dataset seeks to facilitate the development and validation of algorithms designed for complex neural data analysis and decoding.

The specific experiments documented within this dataset involve self-paced reaches to grid-arranged targets performed by Macaca mulatta (Rhesus monkeys). These experiments were conducted without pre-movement delay intervals, aiming to study the neural underpinnings of motor control in these primates. Data were recorded at the University of California, San Francisco (UCSF), under the supervision of experimenter J. E. O'Doherty and have been structured in compliance with the Neurodata Without Borders (NWB) standard.

## Data Availability in NWB Files
The NWB files in this dataset contain a wide array of data categories. This includes:

- **Behavioral Data**: Time-series data encompassing cursor and finger positions (in x, y, and z coordinates), as well as cursor and hand velocities.
- **Neural Data**: Spike counts which were initially detected via an online thresholding mechanism and subsequently sorted offline into putative single units.
- **Event Indications**: Metadata about experiment-related events such as trial results.
- **Session Indices**: Filtering indices for differentiating sessions, animals, and trials.
 
Five NWB files, each approximately totaling 1.25 GB, store these data elements, all of which are identified under unique session IDs.

## Keywords
1. NeuroTask
2. Benchmark Dataset
3. Macaca mulatta
4. Motor Cortex
5. Self-Paced Reaches
6. Neural Data Analysis
7. Multi-Session
8. Multi-Subject
9. Neural Spikes
10. Behavioral Metrics