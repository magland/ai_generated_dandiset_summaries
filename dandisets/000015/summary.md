# A Map of Anticipatory Activity in Mouse Motor Cortex

## Abstract
In the study "A Map of Anticipatory Activity in Mouse Motor Cortex" by Chen et al., published in Neuron in 2017, the authors aimed to investigate the anticipatory neural activities in the motor cortex of mice. The primary focus was on the left vibrissa motor cortex (left_vm1) as mice engaged in a series of motor planning tasks. The study employed advanced two-photon imaging techniques to capture neural activity at the cellular level while mice performed behavioral tasks requiring precise motor planning and execution.

The experimental setup integrated behavioral techniques with cellular imaging to explore how neural circuits in the anterior lateral and medial motor cortices are involved in task anticipation and motor planning. The use of a Thorlabs resonant galvo scanner for two-photon microscopy enabled high-resolution imaging of neurons expressing GCaMP, a calcium indicator. This allowed the researchers to monitor real-time neuronal activity and correlate it with specific behavioral events such as early licking and trial outcomes.

## Data Description
The dataset comprises 100 NWB files, which include extensive recordings of neural and behavioral data. Key data components available in the NWB files include:

- **Structural Images**: Scanning images with a shape of (512, 512) pixels.
- **Behavioral Events**: Time stamps and descriptions for events such as the beginning of the delay period, sampling period, and the go cue signal.
- **Experimental Trials**: Detailed epoch data for 103 trials, including the start and stop times, outcomes, task types and instructions.
- **Fluorescence Imaging**: Data from two-photon imaging, including average fluorescence values for regions of interest (ROI) and the neuropil surrounding the ROI.
- **Image Segmentation**: Results of segmenting the imaging plane, including cell type identification (PT, IT, or unknown), image masks for each ROI, and flags for including ROIs in later analyses.

## Keywords
1. Motor Planning
2. Anterior Lateral Cortex
3. Medial Motor Cortex
4. ALM
5. MM
6. Two-photon Imaging
7. Behavioral Events
8. Cellular Imaging
9. Neural Activity
10. GCaMP