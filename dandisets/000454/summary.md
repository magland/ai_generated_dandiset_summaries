### Abstract

Two-photon microscopy, combined with appropriate optical labeling, has markedly advanced the study of animal and organ system structures, particularly in the nervous system. This breakthrough technique allows for high-resolution measurement and tracking of sub-micrometer structures within brain cells, spatio-temporal mapping of neuronal spikes, and monitoring of neurotransmitter release at individual synapses. However, its spatial resolution degrades significantly when imaging deeper than 300-400 µm, which is the superficial layer of the neocortex. To overcome this limitation, we developed an adaptive optics two-photon microscope that measures the wavefront of a guide star formed by a red-shifted dye within the blood serum. By altering the incident wavefront, we achieved diffraction-limited resolution up to 900 µm deep in mouse cortex, thereby enabling more precise imaging at greater depths.

We present the construction, calibration, and operation of this adaptive optics two-photon microscope. Our setup, primarily composed of commercial optical, optomechanical, mechanical, and electronic components, includes custom components designed using computer-aided design models. The modular nature of this system allows for expansion of imaging and optical excitation capabilities. Demonstrating its application, we imaged somatostatin-expressing neurons at a depth of 700 µm, observed calcium dynamics in layer 5b projection neurons, and mapped thalamocortical glutamate transmission to layer 4 neurons in mouse neocortex.

### NWB Files Contents

The Dandiset contains four NWB files, each holding different aspects of the experimental data:
- **Type 1 NWB File**: Contains data related to a specific session for imaging two-photon microscopy using an adaptive optics configuration. It includes an `ImagingPlane`, `OpticalChannel`, and device details specifying the adaptive optics two-photon laser scanning microscope. The session description is tagged as "Fig 17".
  
- **Type 2 NWB File**: This file mirrors the structure of the Type 1 file but includes data from a different acquisition session also described under "Fig 17". It holds an `ImagingPlane`, `OpticalChannel`, and details regarding the adaptive optics setup.

- **Type 3 NWB File**: Similar in structure to the previous types, this file encompasses an `ImagingPlane`, `OpticalChannel`, and associated device information for another session, labeled "Fig 18".

- **Type 4 NWB File**: This file includes data from yet another session, again with details on the `ImagingPlane`, `OpticalChannel`, and the adaptive optics two-photon laser scanning microscope. The session is also designated under "Fig 18".

### Keywords

- Two-photon microscopy
- Adaptive optics
- Neocortex
- Neuronal imaging
- Sub-micrometer structures
- Mouse brain
- Deep tissue imaging
- Calcium dynamics
- Glutamate transmission
- Neuronal structure