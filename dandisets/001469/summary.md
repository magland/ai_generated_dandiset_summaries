## Abstract

This study focuses on the intraspinal recording of the mouse lumbar spinal cord, employing an advanced electrophysiological approach to unravel neural dynamics within this critical region. Conducted primarily at Rice University and the Salk Institute, the research involves chronic electrode implants in mus musculus (house mice) to investigate spinal cord function. The aim is to capture high-resolution extracellular voltage fluctuations that provide insights into neural behavior and connectivity in the spinal cord, with potential applications in understanding motor control and sensory processing. Electrophysiological data were acquired using a multi-electrode extracellular recording technique, underpinned by meticulous surgical procedures, to ensure the precision and consistency of the recordings.

The experiment extensively utilizes the Neurodata Without Borders (NWB) standard to organize the acquired data, which is significant for its interoperability within the neuroscience community. The NWB files house data from a single subject, embracing six comprehensive datasets, each comprising a time series of electrical activity. These datasets facilitate a detailed examination of electrode positions and electrical properties, such as impedance, relative coordinates, and descriptive labels. By providing a rich dataset for analysis, this work paves the way for novel insights into spinal cord neuroscience and potential breakthroughs in clinical neuroprosthetics.

## NWB File Data Description

The NWB files include data from intraspinal recordings that encompass a single session involving 32 electrodes arranged over shank 0 of the electrode array. The acquisition data, structured under the “ElectricalSeries” group, lacks a specific description but consists of dynamic table regions detailing all electrode IDs (int64), suggested intended for analysis. The general section of the files comprises metadata about the devices used, electrode specifications, and spatial positions within the target region. Coordinates in a three-dimensional space (x, y, z) detail the electrode placements, along with attributes such as impedance values and group names for precise referencing. The session started on March 29, 2022, with data highlighting OpenEphys conversion techniques, exemplifying thorough methodological practices.

## Keywords

- intraspinal recording
- lumbar spinal cord
- electrophysiology
- mus musculus
- multi-electrode recording
- extracellular recording
- neural dynamics
- NWB standard
- neuroprosthetics
- spinal cord research