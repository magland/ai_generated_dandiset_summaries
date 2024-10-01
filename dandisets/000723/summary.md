## Scientific Abstract

The VR-SASE Virtual Reality Dendritic Spine Analysis project aims to develop and implement a novel platform for analyzing dendritic spines using virtual reality (VR) and Blender, a 3D modeling software. The research investigates the efficacy of romidepsin, a histone deacetylase inhibitor, in reducing spasticity and abnormal dendritic spine growth following a spinal cord contusion injury. This model employs Open Brush, an open-source VR art application, to create detailed 3D neuron reconstructions, which are then segmented in Blender. The platform leverages a DataJoint pipeline to determine the spatial distribution of dendritic spines and filter them based on precise morphological parameters for further analysis.

The experiment uses Mus musculus, the common house mouse, as its model organism. Coronal slices of the mouse brain are imaged, and the optical data are collected using a 488nm GFP CF40 imaging plane facilitated by an iXon EMCCD 1 device. Post-processing involves exporting traced neuron data to CSV files for detailed morphological analysis. This workflow allows comprehensive dendritic spine segmentation and quantification, which could illuminate the potential neuroprotective effects of romidepsin in spinal cord injury recovery.

## NWB File Data Description

The NWB files in this Dandiset contain various datasets and groups representing different aspects of the experiment:

1. **Reference Image Sequence**: A sequence of images used to create the 3D models of neurons.
2. **General/Devices and Optophysiology**: Information about the imaging setup, including the type of device (iXon EMCCD 1), imaging plane (488nm GFP CF40), and optical channels.
3. **Surgery and Pharmacology**: Metadata on surgeries performed (i.e., sham or contusion SCI) and pharmacological treatments administered.
4. **Processing Modules**: These include the `MorphologyData`, which holds processed morphological data from Blender, such as:
    - **Image Segmentation**: Datasets like `center_of_mass`, `id`, `length`, `surface_area`, and `volume` for various types of dendritic spines (e.g., MushroomSpine, StubbySpine, ThinSpine, DisconnectedSpine).
    - **VectorData and VectorIndex**: Detailed geometric and morphological quantifications including pixel masks.

Each NWB file represents data from different subjects and experimental conditions, collectively contributing to a comprehensive understanding of the dendritic spine morphology and potential therapeutic interventions for neurotrauma.

## Keywords
- Dendritic Spines
- Virtual Reality
- Blender
- Neurodata Without Borders (NWB)
- Spinal Cord Injury
- Romidepsin
- Mouse Model
- Microscopy
- 3D Neuron Segmentation
- Morphological Analysis