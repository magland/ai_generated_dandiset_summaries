# Recordings from medial entorhinal cortex during linear track and open exploration

This dataset investigates the neural activity of the medial entorhinal cortex (MEC) during different types of navigational tasks in mice. The experiment includes two task types: open field navigation and virtual linear track navigation. Tetrode recordings capture neural activity in the open field task, where mice navigate freely within an arena while simultaneous inertial measurements of the head are taken. For the virtual linear track navigation task, Neuropixel recordings are used along with concurrent eye tracking. The objective appears to be to understand how neural circuits in the MEC encode spatial information and navigation-related behaviors under different experimental conditions.

Data from these recordings can shed light on the functioning of grid cells and their role in spatial awareness and memory. The combination of electrophysiological recordings with behavioral measurements allows for a comprehensive analysis of how specific neural patterns correlate with distinct navigational behaviors. These insights could provide a basis for understanding spatial representation and may have implications for understanding disorders of spatial memory and navigation.

## Available Data in the NWB Files

The NWB files contain extensive data from both the tetrode and Neuropixel recordings. Significant contents include:

- **Processed Behavioral Data**: As part of the `ProcessingModule`, this section includes measurements such as azimuthal head velocity, body speed, and head direction, along with the position of the subjects during the task.
- **SpatialSeries Data**: This component captures the positional data of the mice within the experimental arena.
- **Units Data**: Electrophysiological data detailing the spike times for each recorded unit (or cell), including their identification and timing details.
  
Additional metadata included in the NWB files provides context such as session descriptions, start times, and the experimental environment specifics.

## Keywords

- Medial entorhinal cortex (MEC)
- Tetrode recordings
- Neuropixel recordings
- Open field navigation
- Virtual linear track
- Spatial representation
- Grid cells
- Electrophysiology
- Behavioral neuroscience
- Mouse navigation experiments