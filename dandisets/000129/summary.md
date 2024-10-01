## Abstract

This dataset contains recordings of neural spiking activity and behavioral data from a macaque monkey performing a self-paced reaching task. The primary aim was to study the neural correlates of motor control in the macaque motor cortex during a task involving reaching to various targets. In the experiment, the subject made self-initiated reaches between randomly selected targets arranged in an 8x8 grid with no gaps or pre-movement delay intervals. Neural data were obtained using a 96-electrode array implanted in the primary motor cortex while detailed behavioral metrics were simultaneously recorded, including the position of the monkey's finger, the cursor on a screen, and the targets.

The data are part of the Neural Latents Benchmark initiative aimed at evaluating models of neural activity. The neural data comprise sorted spiking times from individual units, with the units identified through spike sorting techniques. Behavioral data provide comprehensive coverage of the monkey's reaching movements in three-dimensional space, including the velocities of the movements. The dataset provides an extensive resource for researchers interested in motor control, neural encoding, and the development of computational models of brain activity.

## Available Data in NWB Files

The NWB files in this dataset contain comprehensive data arrays encompassing neural and behavioral data. One NWB file includes metadata about the extracellular electrodes, such as their impedance, location coordinates (x, y, z), and grouping information within a 96-electrode Utah array. It also contains trial-level data, detailing the start and stop times of experimental trials, along with the trial splits used for the Neural Latents Benchmark. Another NWB file provides detailed behavioral data, with continuous tracking of cursor positions, finger positions, and target positions, captured at 250 Hz and upsampled to 1 kHz. The file also includes the velocities of the finger movements.

Both NWB files feature data on spiking units, including spike times, observational intervals for each unit, and information on electrode groupings. Classification markers indicate whether particular units' data are held out for testing in the Neural Latents Benchmark. The complete dataset ensures that both neural and behavioral aspects of the self-paced reaching task are well-represented, offering a robust platform for investigating motor control strategies and neural activity patterns.

## Keywords

1. Macaque
2. Motor Cortex
3. Reaching Task
4. Neural Spiking Activity
5. Self-Paced Task
6. Electrode Array
7. Primary Motor Cortex
8. Behavioral Data
9. Neural Latents Benchmark
10. Spike Sorting Technique