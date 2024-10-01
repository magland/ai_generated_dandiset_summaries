
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000987/draft
name: Freely moving mouse retrosplenial cortex recordings
contributor: [{'name': 'Mehrotra, Dhruv ', 'email': 'mdhruv.nov21@gmail.com', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Skromne Carrasco, Sofia', 'email': 'sofia.skromnecarrasco@mail.mcgill.ca', 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Peyrache, Adrien', 'email': 'adrien.peyrache@mcgill.ca', 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Canadian Institutes of Health Research', 'roleName': ['dcite:Sponsor'], 'schemaKey': 'Organization', 'awardNumber': '', 'includeInCitation': False}, {'name': 'Natural Sciences and Engineering Research Council of Canada', 'roleName': ['dcite:Sponsor'], 'schemaKey': 'Organization', 'includeInCitation': False}]
description: Data used in "Hyperpolarization-Activated Currents Drive Neuronal Activation Sequences in Sleep", available at https://www.biorxiv.org/content/10.1101/2023.09.12.557442v1. Dataset includes 14 recordings from 3 mice, with a total of 570 isolated units (31-71 units per recording). Collected by Sofia Skromne Carrasco in the Peyrache lab. Specifically, this data was used to generate Figure 5F.

All sessions include sleep epochs and open field exploration epochs. See the file metadata for more detailed information regarding each recording.

Each NWB file contains: timestamps of detected units, LFP, animal position, head-direction, sleep scoring (REM/NREM) data as well as detected UP and DOWN states as used in the study.

Code to reproduce figures in the article can be found at: https://github.com/PeyracheLab/MehrotraLevenstein_2023

assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}, {'name': 'behavioral approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 1163037056, 'numberOfFiles': 14, 'numberOfSubjects': 3, 'variableMeasured': ['SpatialSeries', 'Position', 'Units', 'CompassDirection', 'ElectrodeGroup'], 'measurementTechnique': [{'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000987 has 14 NWB files.
6 of these NWB files are of type 1.
1 of these NWB files are of type 2.
7 of these NWB files are of type 3.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/CompassDirection (CompassDirection) 
  Group /acquisition/CompassDirection/rx (SpatialSeries) no description
  Group /acquisition/CompassDirection/ry (SpatialSeries) no description
  Group /acquisition/CompassDirection/rz (SpatialSeries) no description
  Group /acquisition/Position (Position) 
  Group /acquisition/Position/x (SpatialSeries) no description
  Group /acquisition/Position/y (SpatialSeries) no description
  Group /acquisition/Position/z (SpatialSeries) no description
  file_create_date: ['2024-05-09T14:50:57.498185-04:00']
  Group /general/devices/ASSY-156-H5-0 (Device) 64-channel linear silicon probe
  experimenter: ['Skromne Carrasco, Sofia']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering, including the filter name and frequency cutoffs | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (64,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the electrode, in ohms | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the position (+x is posterior) | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the position (+y is inferior) | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the position (+z is right) | shape = (64,) | dtype = float64
  Group /general/extracellular_ephys/group0_Shank 1 (ElectrodeGroup) 
  Group /general/extracellular_ephys/group0_Shank 1/device (Device) 64-channel linear silicon probe
  institution: MNI
  lab: Peyrache Lab
  Group /general/subject (Subject) 
  identifier: A7801-210225
  Group /intervals/DOWN (TimeIntervals) 
  Dataset /intervals/DOWN/id (ElementIdentifiers)  | shape = (14073,) | dtype = int64
  Dataset /intervals/DOWN/start_time (VectorData) Start time of epoch, in seconds | shape = (14073,) | dtype = float64
  Dataset /intervals/DOWN/stop_time (VectorData) Stop time of epoch, in seconds | shape = (14073,) | dtype = float64
  Dataset /intervals/DOWN/tags (VectorData) user-defined tags | shape = (14073,) | dtype = object
  Dataset /intervals/DOWN/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (14073,) | dtype = uint16
  Group /intervals/SWS (TimeIntervals) 
  Dataset /intervals/SWS/id (ElementIdentifiers)  | shape = (51,) | dtype = int64
  Dataset /intervals/SWS/start_time (VectorData) Start time of epoch, in seconds | shape = (51,) | dtype = float64
  Dataset /intervals/SWS/stop_time (VectorData) Stop time of epoch, in seconds | shape = (51,) | dtype = float64
  Dataset /intervals/SWS/tags (VectorData) user-defined tags | shape = (51,) | dtype = object
  Dataset /intervals/SWS/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (51,) | dtype = uint8
  Group /intervals/UP (TimeIntervals) 
  Dataset /intervals/UP/id (ElementIdentifiers)  | shape = (14072,) | dtype = int64
  Dataset /intervals/UP/start_time (VectorData) Start time of epoch, in seconds | shape = (14072,) | dtype = float64
  Dataset /intervals/UP/stop_time (VectorData) Stop time of epoch, in seconds | shape = (14072,) | dtype = float64
  Dataset /intervals/UP/tags (VectorData) user-defined tags | shape = (14072,) | dtype = object
  Dataset /intervals/UP/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (14072,) | dtype = uint16
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (5,) | dtype = int64
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (5,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (5,) | dtype = float64
  Dataset /intervals/epochs/tags (VectorData) user-defined tags | shape = (5,) | dtype = object
  Dataset /intervals/epochs/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (5,) | dtype = uint8
  Group /intervals/position_time_support (TimeIntervals) The time support of the position i.e the real start and end of the tracking
  Dataset /intervals/position_time_support/id (ElementIdentifiers)  | shape = (2,) | dtype = int64
  Dataset /intervals/position_time_support/start_time (VectorData) Start time of epoch, in seconds | shape = (2,) | dtype = float64
  Dataset /intervals/position_time_support/stop_time (VectorData) Stop time of epoch, in seconds | shape = (2,) | dtype = float64
  Dataset /intervals/position_time_support/tags (VectorData) user-defined tags | shape = (2,) | dtype = object
  Dataset /intervals/position_time_support/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (2,) | dtype = uint8
  session_description: Freely behaving mouse retrosplenial cortex data as it explores a partial circular arena, followed by the full circular arena. Exploration periods are interleaved with sleep in the home cage.
  session_start_time: 2024-05-09T18:50:57.497860+00:00
  timestamps_reference_time: 2024-05-09T18:50:57.497860+00:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (71,) | dtype = object
  Dataset /units/group (VectorData) the group of the unit | shape = (71,) | dtype = int64
  Dataset /units/id (ElementIdentifiers)  | shape = (71,) | dtype = int64
  Dataset /units/location (VectorData) the anatomical location of this unit | shape = (71,) | dtype = object
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (9210715,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (71,) | dtype = uint32


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/CompassDirection (CompassDirection) 
  Group /acquisition/CompassDirection/rx (SpatialSeries) no description
  Group /acquisition/CompassDirection/ry (SpatialSeries) no description
  Group /acquisition/CompassDirection/rz (SpatialSeries) no description
  Group /acquisition/Position (Position) 
  Group /acquisition/Position/x (SpatialSeries) no description
  Group /acquisition/Position/y (SpatialSeries) no description
  Group /acquisition/Position/z (SpatialSeries) no description
  file_create_date: ['2024-05-09T18:18:30.599082-04:00']
  Group /general/devices/-0 (Device) 
  Group /general/devices/Buzsaki64-1 (Device) 64-channel 8-shank silicon probe
  Group /general/devices/Buzsaki64-2 (Device) 64-channel 8-shank silicon probe
  Group /general/devices/Buzsaki64-3 (Device) 64-channel 8-shank silicon probe
  Group /general/devices/Buzsaki64-4 (Device) 64-channel 8-shank silicon probe
  Group /general/devices/Buzsaki64-5 (Device) 64-channel 8-shank silicon probe
  Group /general/devices/Buzsaki64-6 (Device) 64-channel 8-shank silicon probe
  Group /general/devices/Buzsaki64-7 (Device) 64-channel 8-shank silicon probe
  Group /general/devices/Buzsaki64-8 (Device) 64-channel 8-shank silicon probe
  Group /general/devices/Buzsaki64-9 (Device) 64-channel 8-shank silicon probe
  experimenter: ['Skromne Carrasco, Sofia']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering, including the filter name and frequency cutoffs | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (96,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the electrode, in ohms | shape = (96,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the position (+x is posterior) | shape = (96,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the position (+y is inferior) | shape = (96,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the position (+z is right) | shape = (96,) | dtype = float64
  Group /general/extracellular_ephys/group0_LFP (ElectrodeGroup) 
  Group /general/extracellular_ephys/group0_LFP/device (Device) 
  Group /general/extracellular_ephys/group1_Shank 1 (ElectrodeGroup) 
  Group /general/extracellular_ephys/group1_Shank 1/device (Device) 64-channel 8-shank silicon probe
  Group /general/extracellular_ephys/group2_Shank 2 (ElectrodeGroup) 
  Group /general/extracellular_ephys/group2_Shank 2/device (Device) 64-channel 8-shank silicon probe
  Group /general/extracellular_ephys/group3_Shank 3 (ElectrodeGroup) 
  Group /general/extracellular_ephys/group3_Shank 3/device (Device) 64-channel 8-shank silicon probe
  Group /general/extracellular_ephys/group4_Shank 4 (ElectrodeGroup) 
  Group /general/extracellular_ephys/group4_Shank 4/device (Device) 64-channel 8-shank silicon probe
  Group /general/extracellular_ephys/group5_Shank 5 (ElectrodeGroup) 
  Group /general/extracellular_ephys/group5_Shank 5/device (Device) 64-channel 8-shank silicon probe
  Group /general/extracellular_ephys/group6_Shank 6 (ElectrodeGroup) 
  Group /general/extracellular_ephys/group6_Shank 6/device (Device) 64-channel 8-shank silicon probe
  Group /general/extracellular_ephys/group7_Shank 7 (ElectrodeGroup) 
  Group /general/extracellular_ephys/group7_Shank 7/device (Device) 64-channel 8-shank silicon probe
  Group /general/extracellular_ephys/group8_Shank 8 (ElectrodeGroup) 
  Group /general/extracellular_ephys/group8_Shank 8/device (Device) 64-channel 8-shank silicon probe
  Group /general/extracellular_ephys/group9_unused channels (ElectrodeGroup) 
  Group /general/extracellular_ephys/group9_unused channels/device (Device) 64-channel 8-shank silicon probe
  institution: MNI
  lab: Peyrache Lab
  Group /general/subject (Subject) 
  identifier: A7803-210729
  Group /intervals/DOWN (TimeIntervals) 
  Dataset /intervals/DOWN/id (ElementIdentifiers)  | shape = (13698,) | dtype = int64
  Dataset /intervals/DOWN/start_time (VectorData) Start time of epoch, in seconds | shape = (13698,) | dtype = float64
  Dataset /intervals/DOWN/stop_time (VectorData) Stop time of epoch, in seconds | shape = (13698,) | dtype = float64
  Dataset /intervals/DOWN/tags (VectorData) user-defined tags | shape = (13698,) | dtype = object
  Dataset /intervals/DOWN/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (13698,) | dtype = uint16
  Group /intervals/SWS (TimeIntervals) 
  Dataset /intervals/SWS/id (ElementIdentifiers)  | shape = (24,) | dtype = int64
  Dataset /intervals/SWS/start_time (VectorData) Start time of epoch, in seconds | shape = (24,) | dtype = float64
  Dataset /intervals/SWS/stop_time (VectorData) Stop time of epoch, in seconds | shape = (24,) | dtype = float64
  Dataset /intervals/SWS/tags (VectorData) user-defined tags | shape = (24,) | dtype = object
  Dataset /intervals/SWS/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (24,) | dtype = uint8
  Group /intervals/UP (TimeIntervals) 
  Dataset /intervals/UP/id (ElementIdentifiers)  | shape = (13697,) | dtype = int64
  Dataset /intervals/UP/start_time (VectorData) Start time of epoch, in seconds | shape = (13697,) | dtype = float64
  Dataset /intervals/UP/stop_time (VectorData) Stop time of epoch, in seconds | shape = (13697,) | dtype = float64
  Dataset /intervals/UP/tags (VectorData) user-defined tags | shape = (13697,) | dtype = object
  Dataset /intervals/UP/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (13697,) | dtype = uint16
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (7,) | dtype = int64
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (7,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (7,) | dtype = float64
  Dataset /intervals/epochs/tags (VectorData) user-defined tags | shape = (7,) | dtype = object
  Dataset /intervals/epochs/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (7,) | dtype = uint8
  Group /intervals/position_time_support (TimeIntervals) The time support of the position i.e the real start and end of the tracking
  Dataset /intervals/position_time_support/id (ElementIdentifiers)  | shape = (4,) | dtype = int64
  Dataset /intervals/position_time_support/start_time (VectorData) Start time of epoch, in seconds | shape = (4,) | dtype = float64
  Dataset /intervals/position_time_support/stop_time (VectorData) Stop time of epoch, in seconds | shape = (4,) | dtype = float64
  Dataset /intervals/position_time_support/tags (VectorData) user-defined tags | shape = (4,) | dtype = object
  Dataset /intervals/position_time_support/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (4,) | dtype = uint8
  session_description: Freely behaving mouse retrosplenial cortex data with hippocampal LFP. Order of epochs – sleep, square arena, circular arena, sleep, square arena, circular arena, sleep
  session_start_time: 2024-05-09T22:18:30.598771+00:00
  timestamps_reference_time: 2024-05-09T22:18:30.598771+00:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (58,) | dtype = object
  Dataset /units/group (VectorData) the group of the unit | shape = (58,) | dtype = int64
  Dataset /units/id (ElementIdentifiers)  | shape = (58,) | dtype = int64
  Dataset /units/location (VectorData) the anatomical location of this unit | shape = (58,) | dtype = object
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (11206598,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (58,) | dtype = uint32


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/CompassDirection (CompassDirection) 
  Group /acquisition/CompassDirection/rx (SpatialSeries) no description
  Group /acquisition/CompassDirection/ry (SpatialSeries) no description
  Group /acquisition/CompassDirection/rz (SpatialSeries) no description
  Group /acquisition/Position (Position) 
  Group /acquisition/Position/x (SpatialSeries) no description
  Group /acquisition/Position/y (SpatialSeries) no description
  Group /acquisition/Position/z (SpatialSeries) no description
  file_create_date: ['2024-05-09T17:20:28.536322-04:00']
  Group /general/devices/-0 (Device) 
  Group /general/devices/-9 (Device) 
  Group /general/devices/Buzsaki64-1 (Device) 64-channel 8-shank silicon probe
  Group /general/devices/Buzsaki64-2 (Device) 64-channel 8-shank silicon probe
  Group /general/devices/Buzsaki64-3 (Device) 64-channel 8-shank silicon probe
  Group /general/devices/Buzsaki64-4 (Device) 64-channel 8-shank silicon probe
  Group /general/devices/Buzsaki64-5 (Device) 64-channel 8-shank silicon probe
  Group /general/devices/Buzsaki64-6 (Device) 64-channel 8-shank silicon probe
  Group /general/devices/Buzsaki64-7 (Device) 64-channel 8-shank silicon probe
  Group /general/devices/Buzsaki64-8 (Device) 64-channel 8-shank silicon probe
  experimenter: ['Skromne Carrasco, Sofia']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering, including the filter name and frequency cutoffs | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (96,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the electrode, in ohms | shape = (96,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the position (+x is posterior) | shape = (96,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the position (+y is inferior) | shape = (96,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the position (+z is right) | shape = (96,) | dtype = float64
  Group /general/extracellular_ephys/group0_LFP (ElectrodeGroup) 
  Group /general/extracellular_ephys/group0_LFP/device (Device) 
  Group /general/extracellular_ephys/group1_Shank 1 (ElectrodeGroup) 
  Group /general/extracellular_ephys/group1_Shank 1/device (Device) 64-channel 8-shank silicon probe
  Group /general/extracellular_ephys/group2_Shank 2 (ElectrodeGroup) 
  Group /general/extracellular_ephys/group2_Shank 2/device (Device) 64-channel 8-shank silicon probe
  Group /general/extracellular_ephys/group3_Shank 3 (ElectrodeGroup) 
  Group /general/extracellular_ephys/group3_Shank 3/device (Device) 64-channel 8-shank silicon probe
  Group /general/extracellular_ephys/group4_Shank 4 (ElectrodeGroup) 
  Group /general/extracellular_ephys/group4_Shank 4/device (Device) 64-channel 8-shank silicon probe
  Group /general/extracellular_ephys/group5_Shank 5 (ElectrodeGroup) 
  Group /general/extracellular_ephys/group5_Shank 5/device (Device) 64-channel 8-shank silicon probe
  Group /general/extracellular_ephys/group6_Shank 6 (ElectrodeGroup) 
  Group /general/extracellular_ephys/group6_Shank 6/device (Device) 64-channel 8-shank silicon probe
  Group /general/extracellular_ephys/group7_Shank 7 (ElectrodeGroup) 
  Group /general/extracellular_ephys/group7_Shank 7/device (Device) 64-channel 8-shank silicon probe
  Group /general/extracellular_ephys/group8_Shank 8 (ElectrodeGroup) 
  Group /general/extracellular_ephys/group8_Shank 8/device (Device) 64-channel 8-shank silicon probe
  Group /general/extracellular_ephys/group9_unused channels (ElectrodeGroup) 
  Group /general/extracellular_ephys/group9_unused channels/device (Device) 
  institution: MNI
  lab: Peyrache Lab
  Group /general/subject (Subject) 
  identifier: A7803-210722
  Group /intervals/DOWN (TimeIntervals) 
  Dataset /intervals/DOWN/id (ElementIdentifiers)  | shape = (5044,) | dtype = int64
  Dataset /intervals/DOWN/start_time (VectorData) Start time of epoch, in seconds | shape = (5044,) | dtype = float64
  Dataset /intervals/DOWN/stop_time (VectorData) Stop time of epoch, in seconds | shape = (5044,) | dtype = float64
  Dataset /intervals/DOWN/tags (VectorData) user-defined tags | shape = (5044,) | dtype = object
  Dataset /intervals/DOWN/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (5044,) | dtype = uint16
  Group /intervals/SWS (TimeIntervals) 
  Dataset /intervals/SWS/id (ElementIdentifiers)  | shape = (22,) | dtype = int64
  Dataset /intervals/SWS/start_time (VectorData) Start time of epoch, in seconds | shape = (22,) | dtype = float64
  Dataset /intervals/SWS/stop_time (VectorData) Stop time of epoch, in seconds | shape = (22,) | dtype = float64
  Dataset /intervals/SWS/tags (VectorData) user-defined tags | shape = (22,) | dtype = object
  Dataset /intervals/SWS/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (22,) | dtype = uint8
  Group /intervals/UP (TimeIntervals) 
  Dataset /intervals/UP/id (ElementIdentifiers)  | shape = (5043,) | dtype = int64
  Dataset /intervals/UP/start_time (VectorData) Start time of epoch, in seconds | shape = (5043,) | dtype = float64
  Dataset /intervals/UP/stop_time (VectorData) Stop time of epoch, in seconds | shape = (5043,) | dtype = float64
  Dataset /intervals/UP/tags (VectorData) user-defined tags | shape = (5043,) | dtype = object
  Dataset /intervals/UP/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (5043,) | dtype = uint16
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (2,) | dtype = int64
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (2,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (2,) | dtype = float64
  Dataset /intervals/epochs/tags (VectorData) user-defined tags | shape = (2,) | dtype = object
  Dataset /intervals/epochs/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (2,) | dtype = uint8
  Group /intervals/position_time_support (TimeIntervals) The time support of the position i.e the real start and end of the tracking
  Dataset /intervals/position_time_support/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /intervals/position_time_support/start_time (VectorData) Start time of epoch, in seconds | shape = (1,) | dtype = float64
  Dataset /intervals/position_time_support/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1,) | dtype = float64
  Dataset /intervals/position_time_support/tags (VectorData) user-defined tags | shape = (1,) | dtype = object
  Dataset /intervals/position_time_support/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (1,) | dtype = uint8
  session_description: Freely behaving mouse retrosplenial cortex data with hippocampal LFP. Order of epochs – sleep, square arena.
  session_start_time: 2024-05-09T21:20:28.536020+00:00
  timestamps_reference_time: 2024-05-09T21:20:28.536020+00:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (58,) | dtype = object
  Dataset /units/group (VectorData) the group of the unit | shape = (58,) | dtype = int64
  Dataset /units/id (ElementIdentifiers)  | shape = (58,) | dtype = int64
  Dataset /units/location (VectorData) the anatomical location of this unit | shape = (58,) | dtype = object
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (1416442,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (58,) | dtype = uint32
