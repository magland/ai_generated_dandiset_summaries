### Abstract

The NeuroPAL project aims to create an exhaustive multicolor atlas of neuronal identities within the _Caenorhabditis elegans_ nervous system. The primary objective of this experiment is to utilize NeuroPAL technology to capture whole-brain imaging data of neuronal locations and their corresponding fluorescent colors. This data is employed to develop and refine the 'Statistical Atlas of C. elegans Neurons,' enhancing automated neuron identification processes. The datasets encompass high-resolution structural images of the _C. elegans_ brain, leveraging multi-fluorescence techniques to generate a comprehensive mapping of neuron locations and types.

The experiment combines advanced microscopy and image processing techniques to precisely quantify and label each neuron within the brain of the NeuroPAL worms. By employing spinning disk confocal microscopy, the experiment captures volumetric image data across multiple optical channels. The resulting multichannel imaging data are meticulously processed and analyzed to segment neurons and assign unique identifiers that correspond to neuronal types and locations, contributing significantly to the field of neuroinformatics and developmental neuroscience.

### Data Description

The NeuroPAL dataset consists of 10 NWB files, each representing individual worm samples. These files contain high-resolution, multi-channel volumetric imaging data obtained using a spinning disk confocal microscope. Each file includes a set of optical channels: CyOFP1, GFP-GCaMP, Tag RFP-T, mNeptune 2.5, and mTagBFP2, documenting the fluorescence intensities for specific neuron-identifying markers. Detailed metadata include the imaging volumes, acquisition parameters, and instrumental specifics. The dataset also comprises processed data segments such as the "PlaneSegmentation" and "ProcessingModule," which contain neuron center coordinates, volumetric segmentations, and cross-sectional identifiers, essential for distinguishing individual neurons.

### Keywords

- C. elegans
- NeuroPAL
- Multicolor imaging
- Neuron identification
- Confocal microscopy
- Neuroinformatics
- Image segmentation
- Fluorescence markers
- Whole-brain imaging
- Developmental neuroscience