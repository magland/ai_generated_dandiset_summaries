## Scientific Abstract

We investigated the functionality of novel jGCaMP8 sensors in layer 2/3 pyramidal neurons of the mouse primary visual cortex (V1). Employing a dual approach, we combined simultaneous loose-seal cell-attached electrophysiological recordings with high-resolution two-photon imaging to visualize GCaMP8 expression in neurons subjected to visual stimuli. Mice underwent a craniotomy to administer the AAV2/1-hSynapsin-1 encoding the jGCaMP8 variants, jGCaMP7f, or XCaMP-Gf. After a recovery period of 18-80 days post-viral injection, mice were lightly anesthetized and exposed to full-field drifting gratings presented to the contralateral eye. During the visual stimulation, two-photon imaging captured the activity at 122 Hz, while cell-attached recordings documented the spiking behavior of individual neurons within the imaging field.

The combination of these techniques aimed to evaluate the performance of different GCaMP variants in accurately reflecting neural activity, particularly in response to sensory stimuli. Analysis focused on comparing the signal-to-noise ratio (SNR) and the temporal dynamics of the GCaMP sensors to the electrophysiological recordings. Understanding these dynamics is crucial for enhancing the accuracy and reliability of calcium imaging methods in neuroscientific research.

## Available Data in NWB Files

The datasets contained within the NWB (Neurodata Without Borders) files provide extensive recordings and processed data from the experiments. The key available data across the eight NWB files include:

- **Two-Photon Imaging Data**: Multiple series of high-resolution imaging data capturing the activity of neurons expressing GCaMP variants in response to visual stimuli. Each series is accompanied by information about the imaging plane, device, and the optical channels used.
- **Electrophysiological Recordings**: Loose-seal, cell-attached recordings capturing the spikes from individual neurons. These recordings include data captured under both current clamp and voltage clamp techniques, along with stimuli data.
- **Imaging Processing Results**: Data segmentation results using Suite2p, which identify regions of interest (ROIs, such as specific neurons) and provide masks for cell bodies and surrounding neuropil, characterizing the types of cells recorded (e.g., pyramidal cells or interneurons).
- **Simultaneous Recording Analysis**: Tables and datasets linking electrophysiological recordings with corresponding calcium imaging data, including metadata on detected action potentials, signal-to-noise ratios, and temporal parameters.
- **Experimental Information**: Metadata including session identifiers, details of surgeries performed, viruses used for GCaMP delivery, and specific parameters of the visual stimuli presented.
- **Intracellular Responses**: Detailed intracellular response data from the recorded neurons, including references to time series data corresponding to identified responses.
- **Trial and Epoch Information**: Time intervals and parameters capturing the start and stop times of experimental trials and epochs, alongside detailed descriptions of the visual stimuli parameters during each trial.

## Keywords

- V1
- calcium imaging
- action potential
- two-photon microscopy
- layer 2/3 neurons
- adeno-associated virus (AAV)
- GCaMP sensors
- spike detection
- pyramidal neurons
- visual stimuli