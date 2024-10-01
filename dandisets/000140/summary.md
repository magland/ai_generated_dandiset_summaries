# MC_Maze_Small: Macaque Primary Motor and Dorsal Premotor Cortex Spiking Activity During Delayed Reaching

This dataset contains spiking activity data and behavioral records from a macaque monkey, specifically during a center-out delayed reaching task with obstructive barriers that form a maze. The primary objective of the experiment appears to be to study the neural coding and motor planning processes in the motor cortex (M1) and dorsal premotor cortex (PMd) during reaching movements. Neural activity was captured using 96-electrode Utah arrays implanted in both the M1 and PMd regions. The behavioral aspect of the experiment involved recording the cursor position, hand position, and eye position of the monkey, while hand velocity was computed offline from the hand position data. The experiment was segmented into 100 training trials and 100 test trials, which are aimed at contributing to the Neural Latents Benchmark project.

The available data within the NWB files consists of detailed recordings from the implanted Utah arrays, with metadata describing the device and electrode parameters, including their arrangement and filtering specifications. Spike times, impedance, and the spatial coordinates of the electrodes are also well-documented. Furthermore, the behavioral data includes precise tracking of the monkey's cursor, hand, and eye positions, as well as computed hand velocities. Trial-specific data such as start and stop times, the onset of movements, and the conditions of each trial, including maze configurations and delays, are also present. This comprehensive dataset is poised to facilitate the understanding of neural mechanisms underlying motor control and planning.

### Data available in the NWB files:

1. **Electrode Array Data:**
   - 96-electrode Utah arrays in M1 and PMd.
   - Electrode metadata including impedance, spatial coordinates (x, y, z), and filtering details.

2. **Spiking Activity:**
   - Units spiking times and their corresponding electrodes.
   - Observation intervals for each unit.
   - Classification of units as being part of training or test data.

3. **Behavioral Data:**
   - Detailed position data (cursor, hand, eye) and calculated hand velocity.
   - Trial metadata including start/stop times, target and barrier positions, trial types, and trial success.

4. **Trial Information:**
   - Descriptions of the maze barriers and delays in the tasks.
   - Movement onset times and go-cue timings.

### Keywords:

1. Motor Cortex (M1)
2. Dorsal Premotor Cortex (PMd)
3. Spiking Activity
4. Reaching Task
5. Neural Coding
6. Electrophysiology
7. Macaque Monkey
8. Behavioral Data
9. Neural Latents Benchmark
10. Center-out Reaching Task
