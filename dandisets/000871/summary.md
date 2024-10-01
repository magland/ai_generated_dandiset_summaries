# Allen Institute Openscope - Predictive Learning and Somato-dendritic Coupling

## Abstract

Predictive coding hypotheses suggest that perception is an active process where neural regions generate predictions about incoming sensory inputs. These predictions are then compared with actual sensory inputs by other neural populations, generating error signals when mismatches occur. These error signals are essential for updating the neural predictive model encoded within synaptic weights, facilitating plasticity. This study investigates a crucial testable implication distinguishing various predictive coding strategies: the somato-dendritic coupling strength in layer 2/3 (L2/3) and layer 5 (L5) pyramidal neurons. Particularly, it addresses whether the coupling is reduced, correlating with zero-error apical dendrites during matching predictions, or increased, correlating with stronger coupling when top-down predictions align with bottom-up signals.

This experiment seeks to test these hypotheses by imaging L2/3 and L5 somata and distal apical dendrites in mouse visual cortical areas (V1, LM, PM, AM) using the GCaMP6f fluorescent indicator. By presenting visual stimuli with specific spatiotemporal patterns that are later violated, neuronal responses across the visual hierarchy are measured to discern the neural processes associated with predictive learning. Imaging in four distinct cortical areas also tests the consistency of cortical microcircuitry rules, contributing important insights to neuroscientific questions regarding error signal computation and predictive neural models.

## Available Data in NWB Files

The dataset comprises 61 Neurodata Without Borders (NWB) files, encompassing various types of data acquisition and processing modules. Key data elements include:

1. **Eye Tracking Data**: Captures corneal reflection, pupil tracking, and blink events using time-series data.
2. **Two-Photon Calcium Imaging**: Includes denoised and raw motion-corrected imaging sequences from Mesoscope 2P Rig, segmented ROI data, and derived fluorescence traces.
3. **Stimulus Presentation Data**: Details on stimulus types such as fixed gabors, rotating gabors, gratings, and movie presentations (e.g., 'movie_flower_fwd', 'movie_touch_of_evil_fwd', and 'movie_worms_fwd'), including presentation times, spatial positions, and other parameters.
4. **Running Wheel Data**: Time-series data for voltage signals related to running wheel movements, capturing angular changes and speeds.
5. **Ophys Processing Module**: Includes data on motion correction, neuropil traces, image segmentation, and event detection.
6. **Grayscale Images**: Average image, max projection, and segmentation mask image at pixel resolution.
7. **Device Metadata**: Information on imaging devices and Mesoscope configurations.
8. **Institutional and Experimental Metadata**: Covers experimental descriptions, institution details, and subject identifiers.

## Keywords

- Predictive Coding
- Somato-dendritic Coupling
- Two-Photon Imaging
- Visual Cortex
- Calcium Imaging
- Neural Plasticity
- Behavior
- Cortical Microcircuits
- Mouse V1
- Error Signals
