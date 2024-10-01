## Experiment Summary

The International Brain Laboratory (IBL) has conducted a series of standardized experiments aimed at understanding decision-making processes in mice. This collaborative effort spans multiple institutions and countries, aggregating electrophysiological and behavioral data to elucidate the neural circuits involved in cognitive functions. These experiments are designed to standardize procedures and data collection across diverse research settings, ensuring reproducibility and comparability of findings. The data generated encompasses both the behavior of the subjects during decision-making tasks and the corresponding neural activity captured via high-density NeuroPixels probes.

The collection primarily focuses on acute electrophysiology recordings in combination with behavioral tasks designed to probe decision-making mechanisms. Mice were subjected to various visual stimuli and their behavioral responses were recorded alongside neuronal spike data from multiple brain regions. These extensive datasets provide insights into the temporal dynamics of neuronal firing, neural correlates of behavior, and the functional architecture of the brain regions involved in decision-making.

## Data Available in the NWB Files

### Type 1 NWB File
- **Video**: Raw videos from body, left, and right cameras.
- **Ephys Data**: Spike data and local field potential data from probe00.
- **Electrodes Metadata**: Detailed information about the electrodes used.
- **Trials**: Behavioral trial data including choices, stimuli contrasts, feedback, timing, and reward volumes.
- **Behavioral Time Series**: Absolute position of the wheel and raw DeepLabCut (DLC) outputs for various body parts.
- **Processed Ephys Data**: RMS amplitude and spectral density.
- **Units Data**: Spike times, waveforms, firing rates, and other unit-specific statistical measures.

### Type 2 NWB File
- Similar to Type 1, but data from a different probe (probe01) and experimental session.
- **Institutions/Labs**: Different involved entities such as Cold Spring Harbor Laboratory and zadorlab.
- **Electrodes Metadata**: Expanded metadata including 3D locations relative to bregma.
- **Units Data**: Additional brain location information aligned with the 2017 Allen Common Coordinate Framework.

### Type 3 NWB File
- Similar structure with data from another experimental session.
- **Institutions/Labs**: Involves entities like Cold Spring Harbor Laboratory and churchlandlab.
- **Trials**: Includes intertrial interval duration.
- **Units Data**: Comprehensive metadata with similar structure as the other types.

### Type 4 NWB File
- **Session Description**: Focuses on behavior training/tasks.
- **Institutions/Labs**: University College London and cortexlab.
- **Trials and Behavioral Data**: Rich set of trial and behavioral time series data similar to Type 1.
- **Units Data**: Detailed statistical measures and waveform data.

## Keywords
- Decision-making
- Electrophysiology
- NeuroPixels
- Behavioral neuroscience
- Mouse
- Neural circuits
- Spike sorting
- DeepLabCut
- Visual stimuli
- Temporal dynamics
