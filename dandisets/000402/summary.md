# MICrONS Two Photon Functional Imaging

### Scientific Abstract

This experiment investigates the single-cell responses in the primary visual cortex and adjacent higher visual areas of a mouse. Utilizing a two-photon random access mesoscope (2P-RAM), the researchers captured light microscopic images from a cubic millimeter volume encompassing portions of the primary visual cortex (VISp), lateromedial area (VISlm), rostrolateral area (VISrl), and anterolateral area (VISal). The imaging was carried out on a male mouse expressing a genetically encoded calcium indicator in excitatory cells, over a time span from postnatal days P75 to P81. During the imaging sessions, the mouse was head-restrained and exposed to various visual stimuli, including natural movies and parametric stimuli. The data collected included locomotion velocity, eye movements, and pupil diameter, captured through treadmill rotation and video of the mouse’s left eye.

The calcium imaging data recorded the activity of approximately 75,000 pyramidal cells across a volume of 1200 x 1100 x 500 μm³. This functional data was co-registered with electron microscopy (EM) data, providing structural identifiers of matched cells extracted from the CAVE database. This integration aims to bridge the gap between structure and function in neural circuits, offering insights into the spatial-temporal patterns of calcium activity in response to visual stimuli. Although not all plane segmentations may contain structural ids, the latest data revisions are accessible through a linked notebook.

### Available Data in NWB Files 

The NWB files available in this dandiset contain several data types and measurements, recorded using a 2P-RAM device:

1. **Two-Photon Series**: Multiple fields of calcium imaging data recorded at 6.3009 Hz at various depths, capturing the activity of pyramidal cells over time.
2. **Imaging Planes**: Metadata describing the imaging planes, including optical channels and device-specific information.
3. **Eye-Tracking and Pupil-Tracking**: Spatial series capturing the x, y positions of the mouse’s pupil, as well as the major and minor radii of the pupil ellipse.
4. **Behavioral Data**: Treadmill velocity measurements derived from cylindrical treadmill rotations, and eye movements tracked via video.
5. **Structural Identifiers and Segmentation**: Image masks, weights, mask classification, and structural ids from the CAVE database for each imaging field.
6. **Stimulus Information**: Detailed intervals and conditions for the visual stimuli presented, including natural movie clips, rendered images, and parametric stimuli like smoothened Gaussian noise movies with various orientation and direction components.

### Keywords

- Two-photon microscopy
- Calcium imaging
- Visual cortex
- Mouse behavior
- Neural activity
- Pupil tracking
- Locomotion tracking
- Functional imaging
- Visual stimuli
- Structural-functional integration