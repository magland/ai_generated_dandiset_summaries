## Experiment Summary

The **HippocampusRewardDataset** investigates neural mechanisms underlying reward expectation and extinguishment in the hippocampus of wild-type (WT) mice. Mice underwent a behavioral task where rewards were administered and subsequently removed to study extinction responses. On successive days, mice were exposed to a familiar environment, followed by injections of either saline or DREADD ligands over four experimental days. The DREADD manipulation aimed to modulate VTA dopaminergic neurons to explore their role in reward processing and extinction.

This experiment utilized microscopy and cell population imaging techniques to capture raw fluorescence data across different conditions. Behavioral data, including running, licking, and reward times, were collected in conjunction with fluorescence data to draw correlations between neural activity and behavior. The data was processed using suite2p, and the results are interpreted through temporal changes in neural activity related to reward presence or absence, before and after pharmacological interventions.

### Available Data in the NWB Files

The NWB files in this dataset encompass comprehensive behavioral and fluorescence data. Specifically, each file contains:
- **Behavioral Data**: Downsampled to the imaging rate, with columns representing running behavior, reward times, and lick behavior.
- **Raw Fluorescence Traces**: Traces for each cell processed through suite2p, with frames counted for various conditions like Rewarded, Unrewarded, ReRewarded, BeforeSaline, AfterSaline, BeforeCNO, AfterCNO, BeforeDCZ, and AfterDCZ sessions.
- **Imaging Setup**: Information about the imaging plane, optical channel, and device used—Sheffield Lab's 2-photon rig.
- **Experimental Metadata**: Details about the experimental setup, including the investigator, institution, session description, and important timestamps.

### Keywords

- Hippocampus
- Reward
- Place cells
- CA1
- Virtual Reality paradigm
- DREADD manipulation
- Dopaminergic neurons
- Reward extinction
- Behavioral neuroscience
- Optical imaging

