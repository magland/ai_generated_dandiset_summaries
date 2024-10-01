
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000230/0.220506.1516
name: Jacobsen 2022
contributor: [{'name': 'Jacobsen, R Irene', 'email': 'ragnhild.i.jacobsen@ntnu.no', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0001-9521-5044', 'affiliation': [{'name': 'NTNU', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/05xg72x27'}], 'includeInCitation': True}, {'name': 'Nair, Rajeevkumar R', 'email': 'rajeevkumar.r.nair@ntnu.no', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0001-9755-0874', 'affiliation': [{'name': 'NTNU', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/05xg72x27'}], 'includeInCitation': True}, {'name': 'Obenhaus, Horst A', 'email': 'horst.obenhaus@ntnu.no', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-7670-4827', 'affiliation': [{'name': 'NTNU', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/05xg72x27'}], 'includeInCitation': True}, {'name': 'Donato, Flavio', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-0732-1654', 'affiliation': [{'name': 'Universität Basel', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/02s6k3f65'}], 'includeInCitation': True}, {'name': 'Slettmoen, Torstein', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-0959-7304', 'affiliation': [{'name': 'NTNU', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/05xg72x27'}], 'includeInCitation': True}, {'name': 'Moser, May-Britt', 'email': 'may-britt.moser@ntnu.no', 'roleName': ['dcite:Author', 'dcite:ProjectLeader'], 'schemaKey': 'Person', 'identifier': '0000-0001-7884-3049', 'affiliation': [{'name': 'NTNU', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/05xg72x27'}], 'includeInCitation': True}, {'name': 'Moser, Edvard I', 'email': 'edvard.moser@ntnu.no', 'roleName': ['dcite:Author', 'dcite:ProjectLeader', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0003-0226-5566', 'affiliation': [{'name': 'NTNU', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/05xg72x27'}], 'includeInCitation': True}, {'name': 'Ball, Simon', 'email': 'simon.ball@ntnu.no', 'roleName': ['dcite:Maintainer'], 'schemaKey': 'Person', 'affiliation': [{'name': 'NTNU', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/05xg72x27'}], 'includeInCitation': False}, {'name': 'Waade, Haagen', 'roleName': ['dcite:Maintainer'], 'schemaKey': 'Person', 'affiliation': [{'name': 'NTNU', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/05xg72x27'}], 'includeInCitation': False}, {'name': 'European Research Council', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/0472cxd90', 'awardNumber': '338865', 'contactPoint': [], 'includeInCitation': False}, {'name': 'Research Council of Norway', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/00epmv149', 'awardNumber': '223262', 'contactPoint': [], 'includeInCitation': False}, {'name': 'Research Council of Norway', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/00epmv149', 'awardNumber': '295721', 'contactPoint': [], 'includeInCitation': False}, {'name': 'The Kavli Foundation', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/00kztt736', 'contactPoint': [], 'includeInCitation': False}]
description: Data for "All-viral tracing of monosynaptic inputs to single birthdate-defined neurons in the intact brain", Jacobsen et al 2022. 

Photostimulation laser power: sessions are labelled with the set point power. Actual power can be derived as follows: (set [mW] | actual [mW]), (20 | 7.5), (40 | 15.1)

assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'behavioral approach', 'schemaKey': 'ApproachType'}, {'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 244968456, 'numberOfFiles': 9, 'numberOfSubjects': 2, 'variableMeasured': ['CompassDirection', 'Units', 'ElectrodeGroup', 'SpatialSeries', 'ElectricalSeries', 'BehavioralTimeSeries', 'ProcessingModule', 'LFP', 'Position'], 'measurementTechnique': [{'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'signal filtering technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000230 has 9 NWB files.
3 of these NWB files are of type 1.
6 of these NWB files are of type 2.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/task_events (LabeledEvents) behavioral events of the experimental paradigm
  file_create_date: ['2022-05-06T16:53:18.135921+02:00']
  Group /general/devices/optrode_58313 (Device) 4-tetrode-array
  experimenter: ['Jacobsen, Ragnhild Irene']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (16,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (16,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (16,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (16,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (16,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (16,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (16,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (16,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (16,) | dtype = float64
  Group /general/extracellular_ephys/probe_0 - g_1234-4_chn (ElectrodeGroup) 
  Group /general/extracellular_ephys/probe_0 - g_1234-4_chn/device (Device) 4-tetrode-array
  institution: Moser Group - Kavli Institute for Systems Neuroscience - NTNU
  keywords: ['N/A']
  Group /general/subject (Subject) 
  identifier: 58313_2017-Mar-20_11-34-40
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/arena (VectorData) the arena apparatus associated with a particular epoch | shape = (2,) | dtype = object
  Dataset /intervals/epochs/arena_cue_cards (VectorData) cue cards placed in the arena for the epoch | shape = (2,) | dtype = object
  Dataset /intervals/epochs/arena_curtains (VectorData) curtains placed in the arena for the epoch | shape = (2,) | dtype = object
  Dataset /intervals/epochs/arena_description (VectorData) Description of the arena | shape = (2,) | dtype = object
  Dataset /intervals/epochs/arena_dimensions (VectorData) Dimensions of the arena in cm, (x, y, z) | shape = (2, 3) | dtype = float64
  Dataset /intervals/epochs/arena_geometry (VectorData) Shape of the arena | shape = (2,) | dtype = object
  Dataset /intervals/epochs/arena_objects (VectorData) objects placed in the arena for the epoch | shape = (2,) | dtype = object
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (2,) | dtype = int64
  Dataset /intervals/epochs/light_level (VectorData) light level of the arena for the epoch | shape = (2,) | dtype = object
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (2,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (2,) | dtype = float64
  Dataset /intervals/epochs/task (VectorData) name of task the animal underwent in a particular epoch | shape = (2,) | dtype = object
  Dataset /intervals/epochs/task_desc (VectorData) description of task the animal underwent in a particular epoch | shape = (2,) | dtype = object
  Dataset /intervals/epochs/task_type_desc (VectorData) description of the type of task the animal underwent in a particular epoch | shape = (2,) | dtype = object
  Group /processing/behavior (ProcessingModule) Behavioural data of the animal - position, direction, speed etc
  Group /processing/behavior/direction (CompassDirection) 
  Group /processing/behavior/direction/head_direction (SpatialSeries) Animal's head direction data (in radian) - times x (yaw)
  Group /processing/behavior/position (Position) 
  Group /processing/behavior/position/animal_position (SpatialSeries) Animal's position data (in m) - times x (x, y)
  Group /processing/behavior/speed (BehavioralTimeSeries) 
  Group /processing/behavior/speed/head_yaw_speed (TimeSeries) Animal's head direction angular speed (in radians/s) - times x speed
  Group /processing/behavior/speed/movement_speed (TimeSeries) Animal's speed data (in m/s) - times x speed
  Group /processing/ecephys (ProcessingModule) preprocessed data
  Group /processing/ecephys/probe_0 - LFP (LFP) 
  Group /processing/ecephys/probe_0 - LFP/LFP (ElectricalSeries) LFP per electrode
  Dataset /processing/ecephys/probe_0 - LFP/LFP/electrodes (DynamicTableRegion) Electrodes table region for LFP | shape = (4,) | dtype = int64
  session_description: Day 17 after rabies injection, session 1
  Note: Only a curated subset of tasks and/or units are exported for this session in this NWB file. For a complete dataset, please reach out to the author(s).
  session_start_time: 2017-03-20T11:34:40+01:00
  timestamps_reference_time: 2017-03-20T11:34:40+01:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/cluster_quality (VectorData) unit quality from clustering | shape = (3,) | dtype = object
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (3,) | dtype = object
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (3,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex) Index for VectorData 'electrodes' | shape = (3,) | dtype = uint8
  Dataset /units/id (ElementIdentifiers)  | shape = (3,) | dtype = int64
  Dataset /units/sampling_rate (VectorData) Sampling rate of the raw voltage traces (Hz) | shape = (3,) | dtype = float64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (31179,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (3,) | dtype = uint16
  Dataset /units/waveform_mean (VectorData) the spike waveform mean for each spike unit | shape = (3, 50) | dtype = float64


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/task_events (LabeledEvents) behavioral events of the experimental paradigm
  file_create_date: ['2022-05-06T16:53:37.274351+02:00']
  Group /general/devices/optrode_70375 (Device) 4-tetrode-array
  experimenter: ['Jacobsen, Ragnhild Irene']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (16,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (16,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (16,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (16,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (16,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (16,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (16,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (16,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (16,) | dtype = float64
  Group /general/extracellular_ephys/probe_0 - g_1234-4_chn (ElectrodeGroup) 
  Group /general/extracellular_ephys/probe_0 - g_1234-4_chn/device (Device) 4-tetrode-array
  institution: Moser Group - Kavli Institute for Systems Neuroscience - NTNU
  keywords: ['N/A']
  Group /general/subject (Subject) 
  identifier: 70375_2017-Mar-16_09-55-15
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/arena (VectorData) the arena apparatus associated with a particular epoch | shape = (1,) | dtype = object
  Dataset /intervals/epochs/arena_cue_cards (VectorData) cue cards placed in the arena for the epoch | shape = (1,) | dtype = object
  Dataset /intervals/epochs/arena_curtains (VectorData) curtains placed in the arena for the epoch | shape = (1,) | dtype = object
  Dataset /intervals/epochs/arena_description (VectorData) Description of the arena | shape = (1,) | dtype = object
  Dataset /intervals/epochs/arena_dimensions (VectorData) Dimensions of the arena in cm, (x, y, z) | shape = (1, 3) | dtype = float64
  Dataset /intervals/epochs/arena_geometry (VectorData) Shape of the arena | shape = (1,) | dtype = object
  Dataset /intervals/epochs/arena_objects (VectorData) objects placed in the arena for the epoch | shape = (1,) | dtype = object
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /intervals/epochs/light_level (VectorData) light level of the arena for the epoch | shape = (1,) | dtype = object
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (1,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1,) | dtype = float64
  Dataset /intervals/epochs/task (VectorData) name of task the animal underwent in a particular epoch | shape = (1,) | dtype = object
  Dataset /intervals/epochs/task_desc (VectorData) description of task the animal underwent in a particular epoch | shape = (1,) | dtype = object
  Dataset /intervals/epochs/task_type_desc (VectorData) description of the type of task the animal underwent in a particular epoch | shape = (1,) | dtype = object
  Group /processing/behavior (ProcessingModule) Behavioural data of the animal - position, direction, speed etc
  Group /processing/behavior/direction (CompassDirection) 
  Group /processing/behavior/direction/head_direction (SpatialSeries) Animal's head direction data (in radian) - times x (yaw)
  Group /processing/behavior/position (Position) 
  Group /processing/behavior/position/animal_position (SpatialSeries) Animal's position data (in m) - times x (x, y)
  Group /processing/behavior/speed (BehavioralTimeSeries) 
  Group /processing/behavior/speed/head_yaw_speed (TimeSeries) Animal's head direction angular speed (in radians/s) - times x speed
  Group /processing/behavior/speed/movement_speed (TimeSeries) Animal's speed data (in m/s) - times x speed
  Group /processing/ecephys (ProcessingModule) preprocessed data
  Group /processing/ecephys/probe_0 - LFP (LFP) 
  Group /processing/ecephys/probe_0 - LFP/LFP (ElectricalSeries) LFP per electrode
  Dataset /processing/ecephys/probe_0 - LFP/LFP/electrodes (DynamicTableRegion) Electrodes table region for LFP | shape = (4,) | dtype = int64
  session_description: Day 14 after rabies injection, session 1
  Note: Only a curated subset of tasks and/or units are exported for this session in this NWB file. For a complete dataset, please reach out to the author(s).
  session_start_time: 2017-03-16T09:55:15+01:00
  timestamps_reference_time: 2017-03-16T09:55:15+01:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/cluster_quality (VectorData) unit quality from clustering | shape = (1,) | dtype = object
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (1,) | dtype = object
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (1,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex) Index for VectorData 'electrodes' | shape = (1,) | dtype = uint8
  Dataset /units/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /units/sampling_rate (VectorData) Sampling rate of the raw voltage traces (Hz) | shape = (1,) | dtype = float64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (2063,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (1,) | dtype = uint16
  Dataset /units/waveform_mean (VectorData) the spike waveform mean for each spike unit | shape = (1, 50) | dtype = float64
