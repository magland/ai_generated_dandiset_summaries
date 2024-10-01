# Experiment Summary

This dataset is part of the Credit Assignment project under the Allen Institute for Brain Science's OpenScope initiative. The study aimed to investigate the neural responses to inconsistent stimuli in the primary visual cortex (VisP) of mice. Mice were initially habituated to a head-fixed setup on a running disc for 11 days, during which they were exposed to consistent stimulus sequences, although no imaging was done during this period. Following habituation, inconsistent stimulus sequences were introduced over three sessions, during which two-photon calcium imaging was conducted to capture neuronal activity in pyramidal neurons. Recordings were focused on four distinct planes: L2/3 somata, L5 somata, L2/3 distal apical dendrites, and L5 distal apical dendrites.

The key finding of this study is the differential adaptation of dendritic and somatic compartments to inconsistent stimuli as mice gained experience with these sequences. The dataset includes data from 50 sessions involving 13 mice, with each subject participating in at least three sessions. This comprehensive dataset provides in-depth insights into the dynamics of visual cortex neuron responses to unexpected stimuli.

# Data Description

The NWB dataset files collectively consist of 94 files, showcasing diverse types of acquired data. Each session file includes:
1. ROI dF/F traces,
2. ROI masks,
3. ROI tracking information where applicable,
4. Running velocity traces,
5. Pupil diameter traces,
6. Pupil centroid position traces in X and Y,
7. Stimulus parameters.

Some files also include additional data such as stimulus frame images denoted by `+image` in their filenames and motion-corrected imaging stacks identified by `_obj-raw` in their filenames. The motion-corrected stacks provide a robust view of neuronal activity corrected for movement artifacts. Detailed specifics of each type of file and their content are meticulously documented for reproducibility and further analysis.

# Keywords
- Credit Assignment
- Primary Visual Cortex
- Two-Photon Calcium Imaging
- Inconsistent Stimuli
- Pyramidal Neurons
- ROI Traces
- Behavioral Tracking
- OpenScope
- Allen Institute for Brain Science
- Neurodata Without Borders (NWB)