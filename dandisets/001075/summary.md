## Summary of the Experiment

Neural function emerges from complex interactions within neural networks, a topic of significant interest in neuroscience. This experiment aimed to elucidate the relationship between the structure and function of a nervous system by systematically measuring signal propagation in the nematode *Caenorhabditis elegans*. Employing direct optogenetic activation in conjunction with whole-brain calcium imaging, the study evaluated neural signal attributes, such as sign, strength, temporal properties, and causal direction, between 23,433 neuron pairs in the nematode's head. One key finding was that signal propagation often differed from predictions based solely on anatomical data, suggesting that extrasynaptic signaling plays a substantial role. The research further identified dense-core-vesicle-dependent signaling in regions where no direct wired connections existed but relevant neuropeptides and receptors were expressed.

Mutant strains were used to demonstrate that extrasynaptic signaling, not visible from anatomical analysis, contributes significantly to neural dynamics. The study posited that in cases where extrasynaptically released neuropeptides are involved, these neuropeptides functionally resemble classical neurotransmitters. The comprehensive signal propagation atlas produced better predictions of neural dynamics during spontaneous activity than anatomical models alone. The findings emphasize the importance of both synaptic and extrasynaptic signaling in driving neural dynamics on short timescales and call attention to the necessity of measuring evoked signal propagation to achieve a more accurate interpretation of neural functions.

## Description of Available Data in NWB Files

The dataset consists of 71 NWB files categorized into various types based on the nature of the data. Key data include:

- **Type 1 Files**: 
  - Contain raw functional imaging data from variable-depth PumpProbe scans (Green and Red channels).
  - Static volume scans for NeuroPAL registration.
  - Details of light sources and optical channels used.
  - Detailed microscopy data (e.g., devices, light sources, imaging planes, segmentation data).

- **Type 2 Files**:
  - Include general imaging and segmentations.
  - Detailed optogenetic stimulus targeting with DynamicTableRegions for 70 targeted ROIs.
  - Raw and interpolated fluorescence signals (Green and Red channels).
  - Segmentations for NeuroPAL and PumpProbe imaging with ROI details.
  - Information on optogenetic stimulation, including power, timing, and targeted neurons.

- **Type 3 and Type 4 Files**:
  - Similar structure to Type 2 with differences in specific session parameters and targeted ROIs.
  - Include segmented imaging data and optogenetic stimulus tables for respective epochs.
  - Detailed segmentation and response data for signal processing.

- **Type 5 Files**:
  - Focus on signal propagation recording sessions with time-series data.
  - Detailed microscope and optogenetic device settings.
  - Comprehensive imaging and segmentation for both Green and Red channels.

## Keywords

- *Caenorhabditis elegans*
- Optogenetics
- Functional connectivity
- Neural dynamics
- Calcium imaging
- Signal propagation
- Extrasynaptic signaling
- Neuropeptides
- Two-photon stimulation
- NeuroPAL segmentation