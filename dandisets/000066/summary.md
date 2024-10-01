# Allen Mouse Common Coordinate Framework - Average Brain Template

This experiment aimed to construct a reference brain template using a population average of 1,675 young adult C57BL/6J mice brains. The brains were imaged using serial two-photon tomography (STPT) for the Allen Mouse Brain Connectivity Atlas. The average template was derived from tissue autofluorescence detected in the red channel. To ensure maximal input data, each dataset was mirrored across the midline, resulting in 3,350 hemisphere datasets. The template creation involved an iterative two-step process: deformably registering each specimen to the current template iteration and computing an intensity average, followed by averaging the deformation field, inverting it, and applying it to the initial intensity average until convergence was achieved.

The reference space volume uses a frame where the coordinate axes are defined as +X=Posterior, +Y=Inferior(Ventral), and +Z=Right, with the origin located at the corner of the volume. This dataset provides a symmetrical average anatomical brain model which can be utilized as a standard reference in neural imaging studies. It helps to mitigate individual variability and offers a consistent framework for various types of brain mapping and connectivity research.

## Data Availability

The Dandiset 000066 does not contain NWB files. The reference space or brain template is constructed using Brain Imaging Data Structure (BIDS) standards. The dataset consists of 4 files totalling 381,654,798 bytes. These files form an integral part of the Allen Mouse Brain Connectivity Atlas, providing a standardized volumetric template for subsequent analyses and reference in brain imaging studies.

## Keywords

- Allen Mouse Brain Connectivity Atlas
- Brain Imaging Data Structure (BIDS)
- C57BL/6J mice
- Serial Two-Photon Tomography (STPT)
- Tissue Autofluorescence
- Anatomical Brain Template
- Population Average
- Neuroimaging
- Reference Volume
- Symmetrical Atlas