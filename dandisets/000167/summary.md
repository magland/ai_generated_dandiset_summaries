## Experiment Summary

In this study, two-photon calcium imaging was conducted on the piriform cortex pyramidal neurons of mice under head-fixed conditions. The experiment aimed to investigate neuronal responses to passive odor stimulation. Ten different odors were used, each delivered across eight trials with a 10-second odor presentation followed by a 20-second inter-trial interval. The data were preprocessed using Suite2p, providing insights into the spatiotemporal dynamics of neuronal activity in the piriform cortex in response to olfactory stimuli. This research was conducted in the Fleischmann lab at Brown University and data collection was led by Simon Daste.

The ultimate goal of this experiment was likely to elucidate how distinct olfactory stimuli are represented within the neuronal circuits of the piriform cortex. Understanding these dynamics could provide deeper insights into olfactory processing and the neural mechanisms underlying odor perception. By leveraging advanced calcium imaging techniques, the study offers a high-resolution view of neuronal activity patterns associated with olfactory processing.

## Data Available in the NWB Files

The NWB files encompass a comprehensive set of data components necessary to fully reconstruct and analyze the experiment. Essential metadata includes the experiment description, details of the devices used (Microscope: Ultima Investigator), and specifics about the processing methods (Suite2p). The data acquired include timestamps, trial intervals, and stimulus and acquisition-related time series.

- **Type 1 Files**: Contain detailed calcium imaging data from the piriform cortex, including fluorescence and deconvolved signal datasets across multiple planes, structured ROI information, and segmentation masks. These files also house processed images (such as max projections and mean images), and segments of motion-corrected data.
- **Type 2 Files**: In addition to the data in Type 1 files, these include demo external video files demonstrating the registration motion correction. 

Both file types record the `wheel` positions and `flow` data, though users are advised that flow data and the wheel units should be ignored. The imaging datasets are complemented by trial start and stop times, ensuring that researchers can align neuronal activity data with the corresponding stages of the odor presentation trials.

## Keywords

1. Two-photon calcium imaging
2. Piriform cortex
3. Olfactory processing
4. Passive odor presentation
5. Pyramidal neurons
6. Head-fixed mice
7. Suite2p preprocessing
8. Neuronal activity
9. Odor stimuli
10. Neurodata Without Borders (NWB)
