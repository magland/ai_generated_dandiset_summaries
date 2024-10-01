# Mapping model units to visual neurons reveals population code for social behavior

The dataset in this study investigates the neural mechanisms underlying sensorimotor transformations that drive the complex courtship behaviors in male Drosophila melanogaster. Utilizing a novel modeling approach termed "knockout training," the researchers aimed to map the internal units of a deep neural network to real neurons by predicting behavioral changes resulting from systematic perturbations across 23 different LC neuron types. The study finds that combinations of visual projection neurons, including those typically involved in non-social behaviors, constitute a rich population code that influences male-female interactions. This work integrates the analysis of neuronal perturbations into a single framework, thereby offering a comprehensive map from stimulus to neural activity to behavior.

A total of 459 courtship sessions were recorded, encompassing detailed observations of behavior and calcium imaging data. The imaging data include raw TIF images and processed dF/F responses of five different neuron types recorded using a two-photon microscope. The study also features extensive behavioral data such as raw camera recordings, joint position tracks using SLEAP, song labels, and reconstructed stimuli from the male's point of view. These data are instrumental in understanding how sensory inputs are transformed into motor outputs during social interactions.

## Available Data in NWB files

### Type 1 NWB Files
These files contain two-photon microscopy imaging data. Specifically, they include recordings of LC neuron responses using a custom-built two-photon microscope with a 40x objective and a two-photon laser tuned to 920 nm. Imaging primarily focuses on the green channel through a 562 nm dichroic filter. The data encompass image masks for each ROI, dF/F traces, and various segmented features of optical physiology in these neurons.

### Type 2 NWB Files
These files contain processed pose data derived using SLEAP. The session descriptions generally indicate the recorded session IDs and timestamps correlating with specific experiments that included pose estimations of the flies.

### Type 3 NWB Files
These files contain video and behavioral time-series data, including camera recordings of courtship behavior and position data for both the male and female flies. They document various aspects of male courtship behavior such as Pfast song presence, angular velocity, forward velocity, lateral velocity, and sine song. Additionally, these files include reconstructed stimuli from the male fly's perspective during the courtship.

## Keywords
1. Drosophila melanogaster
2. Two-photon microscopy
3. Sensorimotor transformations
4. Calcium imaging
5. Courtship behavior
6. Neural perturbations
7. Visual projection neurons
8. Population code
9. Deep learning
10. SLEAP
