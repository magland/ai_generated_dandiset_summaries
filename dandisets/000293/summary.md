## Summary

This dataset comprises whole-cell patch-clamp recordings from human cortical neurons, collected post-surgically from resected cortical tissue. The chief goal of the dataset appears to be to analyze the electrophysiological properties and excitability of human cortical neurons, particularly in response to various current clamp and voltage clamp stimuli. These recordings, meticulously curated, are crucial for understanding the intrinsic properties of the neurons and how they might vary across different cortical regions and patients.

The recordings involve detailed measurement of the resting membrane potential (RMP), input resistance, and dynamic responses to standardized electrophysiological protocols such as long square pulse stimulations. By deconstructing the intrinsic cellular properties and responses to controlled current injection stimuli, this data provides a valuable resource for neurophysiological studies, particularly those related to human cognition and pathology.

## Data Description

The NWB files contain electrophysiological data recorded using whole-cell patch-clamp techniques from human cortical neurons. Key data elements include:

1. **CurrentClampSeries**: This includes multiple sweeps of current clamp recordings from neurons. Each sweep is characterized by information such as the electrode used, comments on the RMP, and details on the specific current injection protocol followed.
2. **CurrentClampStimulusSeries**: These files document the stimulus current injection protocols applied during the recordings.
3. **IntracellularElectrode and Device information**: Each recording and stimulus series includes metadata about the electrode and device used, ensuring reproducibility and clarity.
4. **Sweep Table**: The table groups different PatchClampSeries together based on sweep numbers, facilitating easier data navigation and analysis.
5. **Recording Details**: Specific comments on each sweep such as neuronal layer, RMP, and additional experimental conditions provided for context.
6. **Session Metadata**: This includes session start times, session descriptions, and identifiers, alongside general information about the subject from whom the recordings were taken.

## Keywords

1. Human Cortical Neurons
2. Whole-cell Patch-Clamp
3. Electrophysiology
4. Current Clamp
5. Voltage Clamp 
6. Resting Membrane Potential
7. Intrinsic Properties
8. Cortical Excitability
9. Neuroinformatics
10. Neurodata Without Borders (NWB)