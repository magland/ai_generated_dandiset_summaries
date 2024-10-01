# Dataset for "Coregistration of heading to visual cues in retrosplenial cortex" (DANDI:000483/0.230421.2321)

## Experiment Summary

The dataset presents extensive data from a study focused on the retrosplenial cortex's role in integrating heading information with visual cues in the brains of mice (`Mus musculus`). The research involves using a floating air cage to allow free movement of the animals, enabling the researchers to investigate how the retrosplenial cortex encodes directional headings in response to specific visual stimuli. Two-photon calcium imaging was employed to record the activity of neurons expressing GCaMP6s, a calcium indicator, providing critical insights into the spatiotemporal dynamics of neuronal responses.

The study's objective is likely to elucidate the neural mechanisms underlying spatial navigation and cue integration, which are essential for understanding how animals interpret their environment and make navigational decisions. The findings could have implications for unraveling complex neural circuits involved in memory and spatial awareness, contributing to broader neuroscientific knowledge and potentially informing clinical approaches to related disorders.

## Data Available in NWB Files

The dataset comprises seven NWB files containing a variety of data types. Each file includes raw and processed data from two-photon calcium imaging sessions, documenting the neuronal activity in the retrosplenial cortex. Key data entries include TwoPhotonSeries for image stacks, ImagingPlane details, OpticalChannel specifics, and device information, notably the Investigator Ultima microscope used.

Additionally, the NWB files contain processing modules for both optical physiology (ophys) and behavioral data (neurotar). The `ophys` module includes fluorescence data with RoiResponseSeries and ImageSegmentation details. The `neurotar` module comprises information on the floating cage orientation (CompassDirection) and positional data (Position) of the mice. Detailed metadata such as session descriptions, timestamps, experimenter information, and subjects' identifiers are consistently documented across all files.

## Keywords

- Retrosplenial Cortex
- Spatial Navigation
- Two-Photon Imaging
- Calcium Imaging
- GCaMP6s
- Mouse Model
- Behavioral Neuroscience
- Visual Cues
- Neurodata Without Borders (NWB)
- Coregistration
