# Experiment Summary

This study aimed to evaluate the efficacy of jGCaMP8 calcium sensors in layer 2/3 pyramidal neurons of the mouse primary visual cortex (V1). To achieve this, a craniotomy was performed over the V1 region, followed by the infection of neurons with adeno-associated viruses (AAV2/1-hSynapsin-1) encoding various jGCaMP8 variants (s/m/f), jGCaMP7f, and XCaMP-Gf. Data collection commenced 18-80 days post-injection, during which the cranial window was surgically removed, the dura was exposed, and the area was stabilized with agarose and a custom coverslip. The mice were then lightly anesthetized and positioned under a custom two-photon microscope. Visual stimuli consisting of high-contrast drifting gratings were presented at eight directions to the contralateral eye, coupled with simultaneous two-photon imaging at 122 Hz and loose-seal cell-attached electrophysiological recordings from a single neuron within the imaging field.

This dual modality approach allows detailed exploration of the relationship between calcium transients and electrical activity in genetically encoded calcium indicator (GECI)-expressing neurons. Pyramidal cells and fast-spiking (FS) interneurons within the field were targeted for these recordings to study their response to visual stimuli. Such detailed mapping of neuronal activity has significant implications for understanding the role of specific neuronal subtypes in visual processing in the cortex.

# NWB File Contents

- **Raw Two-Photon Imaging Data**: Multiple files containing two-photon imaging series recorded at 122 Hz, representing the calcium dynamics in layer 2/3 neurons.
- **Imaging Metadata**: Configuration of the imaging planes, devices used (including the custom-built two-photon microscope and details about the optical channels).
- **Electrophysiological Data**: Loose-seal cell-attached electrophysiological recordings stored as CurrentClampSeries and VoltageClampSeries, with specific details about the intracellular electrodes and Multiclamp 700B amplifier settings.
- **Analysis Data**: Intracellular responses metadata, including signal-to-noise ratio (SNR) of action potentials, peak times, and references to the recorded responses.
- **Experimental Conditions**: Details about the visual stimuli used, including amplitude, angle, cycles per degree, and cycles per second.
- **Image Segmentation and Processing**: PlaneSegmentation and Fluorescence data for ROI-based analysis using Suite2p segmentation algorithms, including dynamic table regions for ROIs, cell types, and masks.
- **Supplemental Information**: Various metadata such as session start times, experiment descriptions, surgery details, virus injection specifics, and related publications.

# Keywords

1. V1
2. Calcium Imaging
3. Action Potential
4. Two-Photon Microscopy
5. Electrophysiology
6. Pyramidal Neurons
7. Fast-Spiking Interneurons
8. Adeno-Associated Virus
9. Drift Gratings
10. jGCaMP8