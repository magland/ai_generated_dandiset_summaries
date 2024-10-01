### Effects of Periodic Visual Stimulation on Neural Activity in Mouse Visual Cortex

This study explores the impact of periodic sensory stimulation (PSS) on the activity of different neuron types in the mouse visual cortex. The stimulation is delivered via flickering light at distinct frequencies: 40 Hz (gamma frequency), 8 Hz (theta frequency), random frequency determined by a Poisson process with an average frequency of 40 Hz, and constant light. The subjects of the study are mice, and the primary measure of neuronal activity is calcium imaging, capturing responses from vasoactive intestinal peptide (VIP), somatostatin (SST), parvalbumin (PV) expressing inhibitory neurons, and excitatory neurons within the primary visual cortex (V1). The aim is to understand how these different neuronal types in various cortical layers contribute to network dynamics under visual stimulus conditions.

The experiment involved placing an LED strip in front of the mouse's right eye to deliver visual stimuli. Positioning replaced the conventional visual stimulation screen used in previous studies. Each recording session deployed only one stimulus condition at a time. Neural activity was monitored in layers 2/3 and 5 of the visual cortex, except for VIP neurons, which were imaged in layer 4. The data includes recordings from multiple sessions for each mouse, allowing cross-session comparisons. Mice remained awake and passively viewed the stimuli, ensuring the recordings reflect naturalistic visual processing without task-induced biases. All procedures were approved by the Institutional Animal Care and Use Committee (IACUC) at the Allen Institute for Brain Science, adhering to NIH guidelines.

### Data Available in NWB Files

The NWB files contain comprehensive datasets capturing various aspects of the experimental setup and collected data. Key data components include:

- Metadata on experimental sessions, devices used, and subjects.
- Detailed information on the visual stimuli presented, including start and stop times for each trial.
- Behavioral data, specifically running velocity measured via a rotating disc setup.
- Optical physiology data, including raw and processed fluorescence calcium imaging data, with ROI (Region of Interest) traces preprocessed through the OpenScope pipeline.
- Image segmentation data, detailing segmented cells and their respective image masks for each ROI in the imaging plane.
- Each NWB file also encapsulates trial-specific stimulus data and timestamps for reference against experimental start times.

### Keywords

- Periodic Sensory Stimulation (PSS)
- Visual Cortex
- Calcium Imaging
- Inhibitory Neurons
- Excitatory Neurons
- Flickering Light
- Mouse Model
- Neural Activity
- Two-Photon Microscopy
- OpenScope
