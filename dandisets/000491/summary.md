## Abstract
The dataset titled **_Sizes and Shapes of Perivascular Spaces Surrounding Murine Pial Arteries_** by Raicevic et al., contains comprehensive experimental data aimed at understanding the structural characteristics of perivascular spaces (PVS) in murine brains. Using 3D two-photon microscopy, the study investigates nine subjects to delineate the spatial configuration and volumetric parameters of PVS surrounding pial arteries. Each subject received a tracer injection before imaging, allowing for the visualization of the tracer in the vessels, PVS, and microspheres. These imaging datasets were subsequently segmented to create models that provide quantitative insights as presented in the referenced manuscript.

The primary purpose of these experiments is to elucidate the role of PVS in cerebrospinal fluid dynamics and to understand their morphological variability. The detailed segmentation of blood vessels and PVS from these high-resolution images is crucial for modeling fluid dynamics and improving our understanding of neurovascular health and disease. The binaries and models generated from these data sets support the statistical analysis and conclusions drawn in the manuscript.

## NWB File Description
The provided Neurodata Without Borders (NWB) files encompass raw microscopy data and segmented images from multiple imaging channels. The principal data acquisition consists of two-photon series across three channels—ChanA for Green Fluorescent Protein (GFP), and ChanB/C for Alexa Fluor dyes marking the PVS. The files also include imaging planes, devices (Bergamo II), and optical channel metadata. Segmentation data related to each channel is processed and stored as masks in the NWB format, making it feasible to load and analyze using MatNWB or PyNWB frameworks.

### Available Data in NWB Files
1. **Two-photon microscopy series**: Captures 3D imaging data for GFP and tracer in the PVS.
2. **Imaging planes and optical channels**: Metadata defining the imaging setup.
3. **Segmentation masks**: Binary masks for the blood vessels and PVS derived from ChanA, ChanB, and ChanC.
4. **Session Metadata**: Details such as session ID, start time, and experimental description.

## Keywords
1. Perivascular Spaces (PVS)
2. Two-photon Microscopy
3. Brain Imaging
4. Neurovascular
5. Murine Model
6. Image Segmentation
7. GFP
8. Alexa Fluor
9. Cerebrospinal Fluid Dynamics
10. Neurodata Without Borders (NWB)