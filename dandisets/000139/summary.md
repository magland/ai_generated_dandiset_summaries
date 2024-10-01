### Abstract

This dataset examines neural activity in the primary motor cortex (M1) and dorsal premotor cortex (PMd) of a macaque monkey performing a center-out delayed reaching task with obstructing barriers forming a maze. The experimental setup aimed to study the neural dynamics involved in complex motor planning and execution. By recording unit spiking activity from electrode arrays implanted in M1 and PMd, the study seeks to contribute to the understanding of motor control and planning, especially in response to varying spatial constraints presented by the maze.

The experiment involved recording neural activity, hand, eye, and cursor position, while the macaque executed both straight and curved reaches within the maze barriers. Behavioral data including hand velocity was calculated offline. The dataset provides 250 train trials and 100 test trials, offering a robust platform for benchmarking neural decoding algorithms. The availability of detailed spiking data, alongside temporal and spatial behavioral metrics, makes this dataset valuable for computational neuroscience, specifically in understanding the latent structures of neural activity during complex motor tasks.

### Data Available in NWB Files

#### File 1 Summary
- **Metadata:** Contains details about the electrode arrays (96-electrode Utah array) and their locations in M1 and PMd. 
- **General:** Includes session and subject information, trial intervals, and device metadata.
- **Spiking Data:** Provides detailed spiking information for 114 units, including spike times, observation intervals, and electrode associations.
- **Behavioral Data:** Cursor position, hand position, and eye position were not explicitly listed but are implied to be part of the dataset.

#### File 2 Summary
- **Metadata:** Similar to File 1 with 96-electrode Utah arrays in M1 and PMd.
- **General:** Contains extended trial information, such as barrier positions, go cue times, movement onset times, and success indicators.
- **Spiking Data:** Provides spiking information for 152 units, including spike times, observation intervals, and electrodes.
- **Behavioral Data:** Detailed recordings of cursor position, hand position, eye position, and calculated hand velocity.

### Keywords
1. Motor Cortex
2. Premotor Cortex
3. Reaching Task
4. Macaque
5. Neural Latents Benchmark
6. Electrophysiology
7. Spike Sorting
8. Motor Planning
9. Delayed Reaching
10. Neural Dynamics