
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000044/0.210812.1516
name: Diversity in neural firing dynamics supports both rigid and learned hippocampal sequences
contributor: [{'name': 'Grosmark, Andres D.', 'roleName': ['dcite:Author', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Buzsáki, György', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-3100-4800', 'affiliation': [], 'includeInCitation': True}]
description: This data set is composed of eight bilateral silicon-probe multi-cellular electrophysiological recordings performed on four male Long-Evans rats in the Buzsáki lab at NYU. These recordings were performed to assess the effect of novel spatial learning on hippocampal CA1 neural firing and LFP patterns in naïve animals. Each session consisted of a long (~4 hour) PRE rest/sleep epoch home-cage recordings performed in a familiar room, followed by a Novel MAZE running epoch (~45 minutes) in which the animals were transferred to a novel room, and water-rewarded to run on a novel maze. These mazes were either A) a wooden 1.6m linear platform, B) a wooden 1m diameter circular platform or C) a 2m metal linear platform. Animals were rewarded either at both ends of the linear platform, or at a predetermined location on the circular platform. The animal was gently encouraged to run unidirectionally on the circular platform. After the MAZE epochs the animals were transferred back to their home-cage in the familiar room where a long (~4 hour) POST rest/sleep was recorded. All eight sessions were concatenated from the PRE, MAZE, and POST recording epochs. In addition to hippocampal electrophysiological recordings, neck EMG and head-mounted accelerometer signals were recorded, and the animal’s position during MAZE running epochs was tracked via head-mounted LEDs.
assetsSummary: {'species': [{'name': 'Brown rat', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10116'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 65708919583, 'numberOfFiles': 8, 'numberOfSubjects': 4, 'variableMeasured': ['ElectricalSeries', 'LFP', 'Units'], 'measurementTechnique': [{'name': 'signal filtering technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000044 has 8 NWB files.
2 of these NWB files are of type 1.
2 of these NWB files are of type 2.
2 of these NWB files are of type 3.
1 of these NWB files are of type 4.
1 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2021-01-24T11:38:48.066582-05:00']
  Group /general/devices/Device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  experimenter: ['Andres Grosmark']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/bad_electrode (VectorData) Indicator for if the electrode was removed from analysis due to low-amplitude or instabilities. | shape = (128,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/shank_electrode_number (VectorData) 0-indexed channel within a shank. | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (128,) | dtype = float64
  Group /general/extracellular_ephys/shank1 (ElectrodeGroup) shank1 electrodes
  Group /general/extracellular_ephys/shank1/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank10 (ElectrodeGroup) shank10 electrodes
  Group /general/extracellular_ephys/shank10/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank11 (ElectrodeGroup) shank11 electrodes
  Group /general/extracellular_ephys/shank11/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank12 (ElectrodeGroup) shank12 electrodes
  Group /general/extracellular_ephys/shank12/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank13 (ElectrodeGroup) shank13 electrodes
  Group /general/extracellular_ephys/shank13/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank14 (ElectrodeGroup) shank14 electrodes
  Group /general/extracellular_ephys/shank14/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank2 (ElectrodeGroup) shank2 electrodes
  Group /general/extracellular_ephys/shank2/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank3 (ElectrodeGroup) shank3 electrodes
  Group /general/extracellular_ephys/shank3/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank4 (ElectrodeGroup) shank4 electrodes
  Group /general/extracellular_ephys/shank4/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank5 (ElectrodeGroup) shank5 electrodes
  Group /general/extracellular_ephys/shank5/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank6 (ElectrodeGroup) shank6 electrodes
  Group /general/extracellular_ephys/shank6/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank7 (ElectrodeGroup) shank7 electrodes
  Group /general/extracellular_ephys/shank7/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank8 (ElectrodeGroup) shank8 electrodes
  Group /general/extracellular_ephys/shank8/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank9 (ElectrodeGroup) shank9 electrodes
  Group /general/extracellular_ephys/shank9/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  institution: NYU
  lab: Buzsaki
  related_publications: ['Grosmark, A.D., and Buzsáki, G. (2016). Diversity in neural firing dynamics supports both rigid and learned hippocampal sequences. Science 351, 1440–1443.'
   'Chen, Z., Grosmark, A.D., Penagos, H., and Wilson, M.A. (2016). Uncovering representations of sleep-associated hippocampal ensemble spike activity. Sci. Rep. 6, 32193.']
  session_id: Achilles_10252013
  Group /general/subject (Subject) 
  identifier: fa7c8ae4-186e-4f0c-b697-70ed1633d091
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (3,) | dtype = int64
  Dataset /intervals/epochs/label (VectorData) Name of epoch. | shape = (3,) | dtype = object
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (3,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (3,) | dtype = float64
  Group /processing/behavior (ProcessingModule) Contains behavioral data.
  Group /processing/behavior/1.6mLinearMazeLinearizedPosition (Position) 
  Group /processing/behavior/1.6mLinearMazeLinearizedPosition/1.6mLinearMazeLinearizedTimeSeries (SpatialSeries) Linearized position, defined as starting at the edge of reward area, and increasing clockwise, terminating at the opposing edge of the reward area.
  Group /processing/behavior/1.6mLinearMazePosition (Position) 
  Group /processing/behavior/1.6mLinearMazePosition/1.6mLinearMazeSpatialSeries (SpatialSeries) (x,y) coordinates tracking subject movement through the maze.
  Group /processing/behavior/states (TimeIntervals) Sleep states of animal.
  Dataset /processing/behavior/states/id (ElementIdentifiers)  | shape = (144,) | dtype = int64
  Dataset /processing/behavior/states/label (VectorData) Sleep state. | shape = (144,) | dtype = object
  Dataset /processing/behavior/states/start_time (VectorData) Start time of epoch, in seconds | shape = (144,) | dtype = float32
  Dataset /processing/behavior/states/stop_time (VectorData) Stop time of epoch, in seconds | shape = (144,) | dtype = float32
  Group /processing/ecephys (ProcessingModule) Intermediate data from extracellular electrophysiology recordings, e.g., LFP.
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/LFP (ElectricalSeries) Local field potential signal.
  Dataset /processing/ecephys/LFP/LFP/electrodes (DynamicTableRegion) electrode_table_region | shape = (128,) | dtype = int64
  session_description: This data set is composed of eight bilateral silicon-probe multi-cellular electrophysiological 
  session_start_time: 2013-10-25T00:00:00-04:00
  timestamps_reference_time: 2013-10-25T00:00:00-04:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/cell_type (VectorData) Type of cell this has been classified as. | shape = (137,) | dtype = object
  Dataset /units/id (ElementIdentifiers)  | shape = (137,) | dtype = int64
  Dataset /units/location (VectorData) Brain region where each unit was detected. | shape = (137,) | dtype = object
  Dataset /units/shank_id (VectorData) 0-indexed id of cluster identified from the shank. | shape = (137,) | dtype = int64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (8414607,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (137,) | dtype = uint32


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2021-01-24T11:11:39.567911-05:00']
  Group /general/devices/Device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  experimenter: ['Andres Grosmark']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/bad_electrode (VectorData) Indicator for if the electrode was removed from analysis due to low-amplitude or instabilities. | shape = (128,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/shank_electrode_number (VectorData) 0-indexed channel within a shank. | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (128,) | dtype = float64
  Group /general/extracellular_ephys/shank1 (ElectrodeGroup) shank1 electrodes
  Group /general/extracellular_ephys/shank1/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank10 (ElectrodeGroup) shank10 electrodes
  Group /general/extracellular_ephys/shank10/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank11 (ElectrodeGroup) shank11 electrodes
  Group /general/extracellular_ephys/shank11/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank12 (ElectrodeGroup) shank12 electrodes
  Group /general/extracellular_ephys/shank12/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank13 (ElectrodeGroup) shank13 electrodes
  Group /general/extracellular_ephys/shank13/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank14 (ElectrodeGroup) shank14 electrodes
  Group /general/extracellular_ephys/shank14/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank2 (ElectrodeGroup) shank2 electrodes
  Group /general/extracellular_ephys/shank2/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank3 (ElectrodeGroup) shank3 electrodes
  Group /general/extracellular_ephys/shank3/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank4 (ElectrodeGroup) shank4 electrodes
  Group /general/extracellular_ephys/shank4/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank5 (ElectrodeGroup) shank5 electrodes
  Group /general/extracellular_ephys/shank5/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank6 (ElectrodeGroup) shank6 electrodes
  Group /general/extracellular_ephys/shank6/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank7 (ElectrodeGroup) shank7 electrodes
  Group /general/extracellular_ephys/shank7/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank8 (ElectrodeGroup) shank8 electrodes
  Group /general/extracellular_ephys/shank8/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank9 (ElectrodeGroup) shank9 electrodes
  Group /general/extracellular_ephys/shank9/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  institution: NYU
  lab: Buzsaki
  related_publications: ['Grosmark, A.D., and Buzsáki, G. (2016). Diversity in neural firing dynamics supports both rigid and learned hippocampal sequences. Science 351, 1440–1443.'
   'Chen, Z., Grosmark, A.D., Penagos, H., and Wilson, M.A. (2016). Uncovering representations of sleep-associated hippocampal ensemble spike activity. Sci. Rep. 6, 32193.']
  session_id: Achilles_11012013
  Group /general/subject (Subject) 
  identifier: 884a4f2d-1f32-459f-ac35-2a76757dcf3a
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (3,) | dtype = int64
  Dataset /intervals/epochs/label (VectorData) Name of epoch. | shape = (3,) | dtype = object
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (3,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (3,) | dtype = float64
  Group /processing/behavior (ProcessingModule) Contains behavioral data.
  Group /processing/behavior/CircularMazeLinearizedPosition (Position) 
  Group /processing/behavior/CircularMazeLinearizedPosition/CircularMazeLinearizedTimeSeries (SpatialSeries) Linearized position, defined as starting at the edge of reward area, and increasing clockwise, terminating at the opposing edge of the reward area.
  Group /processing/behavior/CircularMazePosition (Position) 
  Group /processing/behavior/CircularMazePosition/CircularMazeSpatialSeries (SpatialSeries) (x,y) coordinates tracking subject movement through the maze.
  Group /processing/behavior/states (TimeIntervals) Sleep states of animal.
  Dataset /processing/behavior/states/id (ElementIdentifiers)  | shape = (284,) | dtype = int64
  Dataset /processing/behavior/states/label (VectorData) Sleep state. | shape = (284,) | dtype = object
  Dataset /processing/behavior/states/start_time (VectorData) Start time of epoch, in seconds | shape = (284,) | dtype = float32
  Dataset /processing/behavior/states/stop_time (VectorData) Stop time of epoch, in seconds | shape = (284,) | dtype = float32
  Group /processing/ecephys (ProcessingModule) Intermediate data from extracellular electrophysiology recordings, e.g., LFP.
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/LFP (ElectricalSeries) Local field potential signal.
  Dataset /processing/ecephys/LFP/LFP/electrodes (DynamicTableRegion) electrode_table_region | shape = (128,) | dtype = int64
  session_description: This data set is composed of eight bilateral silicon-probe multi-cellular electrophysiological 
  session_start_time: 2013-11-01T00:00:00-04:00
  timestamps_reference_time: 2013-11-01T00:00:00-04:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/cell_type (VectorData) Type of cell this has been classified as. | shape = (104,) | dtype = object
  Dataset /units/id (ElementIdentifiers)  | shape = (104,) | dtype = int64
  Dataset /units/location (VectorData) Brain region where each unit was detected. | shape = (104,) | dtype = object
  Dataset /units/shank_id (VectorData) 0-indexed id of cluster identified from the shank. | shape = (104,) | dtype = int64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (7665373,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (104,) | dtype = uint32


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2021-01-24T12:04:29.442727-05:00']
  Group /general/devices/Device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  experimenter: ['Andres Grosmark']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/bad_electrode (VectorData) Indicator for if the electrode was removed from analysis due to low-amplitude or instabilities. | shape = (128,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/shank_electrode_number (VectorData) 0-indexed channel within a shank. | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (128,) | dtype = float64
  Group /general/extracellular_ephys/shank1 (ElectrodeGroup) shank1 electrodes
  Group /general/extracellular_ephys/shank1/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank10 (ElectrodeGroup) shank10 electrodes
  Group /general/extracellular_ephys/shank10/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank11 (ElectrodeGroup) shank11 electrodes
  Group /general/extracellular_ephys/shank11/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank12 (ElectrodeGroup) shank12 electrodes
  Group /general/extracellular_ephys/shank12/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank13 (ElectrodeGroup) shank13 electrodes
  Group /general/extracellular_ephys/shank13/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank14 (ElectrodeGroup) shank14 electrodes
  Group /general/extracellular_ephys/shank14/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank15 (ElectrodeGroup) shank15 electrodes
  Group /general/extracellular_ephys/shank15/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank16 (ElectrodeGroup) shank16 electrodes
  Group /general/extracellular_ephys/shank16/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank2 (ElectrodeGroup) shank2 electrodes
  Group /general/extracellular_ephys/shank2/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank3 (ElectrodeGroup) shank3 electrodes
  Group /general/extracellular_ephys/shank3/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank4 (ElectrodeGroup) shank4 electrodes
  Group /general/extracellular_ephys/shank4/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank5 (ElectrodeGroup) shank5 electrodes
  Group /general/extracellular_ephys/shank5/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank6 (ElectrodeGroup) shank6 electrodes
  Group /general/extracellular_ephys/shank6/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank7 (ElectrodeGroup) shank7 electrodes
  Group /general/extracellular_ephys/shank7/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank8 (ElectrodeGroup) shank8 electrodes
  Group /general/extracellular_ephys/shank8/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank9 (ElectrodeGroup) shank9 electrodes
  Group /general/extracellular_ephys/shank9/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  institution: NYU
  lab: Buzsaki
  related_publications: ['Grosmark, A.D., and Buzsáki, G. (2016). Diversity in neural firing dynamics supports both rigid and learned hippocampal sequences. Science 351, 1440–1443.'
   'Chen, Z., Grosmark, A.D., Penagos, H., and Wilson, M.A. (2016). Uncovering representations of sleep-associated hippocampal ensemble spike activity. Sci. Rep. 6, 32193.']
  session_id: Buddy_06272013
  Group /general/subject (Subject) 
  identifier: 913d2e79-68ef-4cc5-82ff-5c05b7ca7449
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (3,) | dtype = int64
  Dataset /intervals/epochs/label (VectorData) Name of epoch. | shape = (3,) | dtype = object
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (3,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (3,) | dtype = float64
  Group /processing/behavior (ProcessingModule) Contains behavioral data.
  Group /processing/behavior/1.6mLinearMazeLinearizedPosition (Position) 
  Group /processing/behavior/1.6mLinearMazeLinearizedPosition/1.6mLinearMazeLinearizedTimeSeries (SpatialSeries) Linearized position, defined as starting at the edge of reward area, and increasing clockwise, terminating at the opposing edge of the reward area.
  Group /processing/behavior/1.6mLinearMazePosition (Position) 
  Group /processing/behavior/1.6mLinearMazePosition/1.6mLinearMazeSpatialSeries (SpatialSeries) (x,y) coordinates tracking subject movement through the maze.
  Group /processing/behavior/states (TimeIntervals) Sleep states of animal.
  Dataset /processing/behavior/states/id (ElementIdentifiers)  | shape = (157,) | dtype = int64
  Dataset /processing/behavior/states/label (VectorData) Sleep state. | shape = (157,) | dtype = object
  Dataset /processing/behavior/states/start_time (VectorData) Start time of epoch, in seconds | shape = (157,) | dtype = float32
  Dataset /processing/behavior/states/stop_time (VectorData) Stop time of epoch, in seconds | shape = (157,) | dtype = float32
  Group /processing/ecephys (ProcessingModule) Intermediate data from extracellular electrophysiology recordings, e.g., LFP.
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/LFP (ElectricalSeries) Local field potential signal.
  Dataset /processing/ecephys/LFP/LFP/electrodes (DynamicTableRegion) electrode_table_region | shape = (128,) | dtype = int64
  session_description: This data set is composed of eight bilateral silicon-probe multi-cellular electrophysiological 
  session_start_time: 2013-06-27T00:00:00-04:00
  timestamps_reference_time: 2013-06-27T00:00:00-04:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/cell_type (VectorData) Type of cell this has been classified as. | shape = (68,) | dtype = object
  Dataset /units/id (ElementIdentifiers)  | shape = (68,) | dtype = int64
  Dataset /units/location (VectorData) Brain region where each unit was detected. | shape = (68,) | dtype = object
  Dataset /units/shank_id (VectorData) 0-indexed id of cluster identified from the shank. | shape = (68,) | dtype = int64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (6412255,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (68,) | dtype = uint32


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2021-01-24T12:57:19.828404-05:00']
  Group /general/devices/Device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  experimenter: ['Andres Grosmark']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/bad_electrode (VectorData) Indicator for if the electrode was removed from analysis due to low-amplitude or instabilities. | shape = (128,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/shank_electrode_number (VectorData) 0-indexed channel within a shank. | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (128,) | dtype = float64
  Group /general/extracellular_ephys/shank1 (ElectrodeGroup) shank1 electrodes
  Group /general/extracellular_ephys/shank1/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank10 (ElectrodeGroup) shank10 electrodes
  Group /general/extracellular_ephys/shank10/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank11 (ElectrodeGroup) shank11 electrodes
  Group /general/extracellular_ephys/shank11/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank12 (ElectrodeGroup) shank12 electrodes
  Group /general/extracellular_ephys/shank12/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank13 (ElectrodeGroup) shank13 electrodes
  Group /general/extracellular_ephys/shank13/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank14 (ElectrodeGroup) shank14 electrodes
  Group /general/extracellular_ephys/shank14/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank2 (ElectrodeGroup) shank2 electrodes
  Group /general/extracellular_ephys/shank2/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank3 (ElectrodeGroup) shank3 electrodes
  Group /general/extracellular_ephys/shank3/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank4 (ElectrodeGroup) shank4 electrodes
  Group /general/extracellular_ephys/shank4/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank5 (ElectrodeGroup) shank5 electrodes
  Group /general/extracellular_ephys/shank5/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank6 (ElectrodeGroup) shank6 electrodes
  Group /general/extracellular_ephys/shank6/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank7 (ElectrodeGroup) shank7 electrodes
  Group /general/extracellular_ephys/shank7/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank8 (ElectrodeGroup) shank8 electrodes
  Group /general/extracellular_ephys/shank8/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank9 (ElectrodeGroup) shank9 electrodes
  Group /general/extracellular_ephys/shank9/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  institution: NYU
  lab: Buzsaki
  related_publications: ['Grosmark, A.D., and Buzsáki, G. (2016). Diversity in neural firing dynamics supports both rigid and learned hippocampal sequences. Science 351, 1440–1443.'
   'Chen, Z., Grosmark, A.D., Penagos, H., and Wilson, M.A. (2016). Uncovering representations of sleep-associated hippocampal ensemble spike activity. Sci. Rep. 6, 32193.']
  session_id: Cicero_09172014
  Group /general/subject (Subject) 
  identifier: 0a4af9ab-499b-46d5-a02a-17298403076a
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (3,) | dtype = int64
  Dataset /intervals/epochs/label (VectorData) Name of epoch. | shape = (3,) | dtype = object
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (3,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (3,) | dtype = float64
  Group /processing/behavior (ProcessingModule) Contains behavioral data.
  Group /processing/behavior/2mLinearMazeLinearizedPosition (Position) 
  Group /processing/behavior/2mLinearMazeLinearizedPosition/2mLinearMazeLinearizedTimeSeries (SpatialSeries) Linearized position, defined as starting at the edge of reward area, and increasing clockwise, terminating at the opposing edge of the reward area.
  Group /processing/behavior/2mLinearMazePosition (Position) 
  Group /processing/behavior/2mLinearMazePosition/2mLinearMazeSpatialSeries (SpatialSeries) (x,y) coordinates tracking subject movement through the maze.
  Group /processing/behavior/states (TimeIntervals) Sleep states of animal.
  Dataset /processing/behavior/states/id (ElementIdentifiers)  | shape = (288,) | dtype = int64
  Dataset /processing/behavior/states/label (VectorData) Sleep state. | shape = (288,) | dtype = object
  Dataset /processing/behavior/states/start_time (VectorData) Start time of epoch, in seconds | shape = (288,) | dtype = float32
  Dataset /processing/behavior/states/stop_time (VectorData) Stop time of epoch, in seconds | shape = (288,) | dtype = float32
  Group /processing/ecephys (ProcessingModule) Intermediate data from extracellular electrophysiology recordings, e.g., LFP.
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/LFP (ElectricalSeries) Local field potential signal.
  Dataset /processing/ecephys/LFP/LFP/electrodes (DynamicTableRegion) electrode_table_region | shape = (128,) | dtype = int64
  session_description: This data set is composed of eight bilateral silicon-probe multi-cellular electrophysiological 
  session_start_time: 2014-09-17T00:00:00-04:00
  timestamps_reference_time: 2014-09-17T00:00:00-04:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/cell_type (VectorData) Type of cell this has been classified as. | shape = (72,) | dtype = object
  Dataset /units/id (ElementIdentifiers)  | shape = (72,) | dtype = int64
  Dataset /units/location (VectorData) Brain region where each unit was detected. | shape = (72,) | dtype = object
  Dataset /units/shank_id (VectorData) 0-indexed id of cluster identified from the shank. | shape = (72,) | dtype = int64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (7708448,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (72,) | dtype = uint32


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2021-01-24T13:14:34.626794-05:00']
  Group /general/devices/Device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  experimenter: ['Andres Grosmark']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/bad_electrode (VectorData) Indicator for if the electrode was removed from analysis due to low-amplitude or instabilities. | shape = (128,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/shank_electrode_number (VectorData) 0-indexed channel within a shank. | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (128,) | dtype = float64
  Group /general/extracellular_ephys/shank1 (ElectrodeGroup) shank1 electrodes
  Group /general/extracellular_ephys/shank1/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank10 (ElectrodeGroup) shank10 electrodes
  Group /general/extracellular_ephys/shank10/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank11 (ElectrodeGroup) shank11 electrodes
  Group /general/extracellular_ephys/shank11/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank12 (ElectrodeGroup) shank12 electrodes
  Group /general/extracellular_ephys/shank12/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank13 (ElectrodeGroup) shank13 electrodes
  Group /general/extracellular_ephys/shank13/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank14 (ElectrodeGroup) shank14 electrodes
  Group /general/extracellular_ephys/shank14/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank15 (ElectrodeGroup) shank15 electrodes
  Group /general/extracellular_ephys/shank15/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank16 (ElectrodeGroup) shank16 electrodes
  Group /general/extracellular_ephys/shank16/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank2 (ElectrodeGroup) shank2 electrodes
  Group /general/extracellular_ephys/shank2/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank3 (ElectrodeGroup) shank3 electrodes
  Group /general/extracellular_ephys/shank3/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank4 (ElectrodeGroup) shank4 electrodes
  Group /general/extracellular_ephys/shank4/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank5 (ElectrodeGroup) shank5 electrodes
  Group /general/extracellular_ephys/shank5/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank6 (ElectrodeGroup) shank6 electrodes
  Group /general/extracellular_ephys/shank6/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank7 (ElectrodeGroup) shank7 electrodes
  Group /general/extracellular_ephys/shank7/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank8 (ElectrodeGroup) shank8 electrodes
  Group /general/extracellular_ephys/shank8/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  Group /general/extracellular_ephys/shank9 (ElectrodeGroup) shank9 electrodes
  Group /general/extracellular_ephys/shank9/device (Device) Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the 
  institution: NYU
  lab: Buzsaki
  related_publications: ['Grosmark, A.D., and Buzsáki, G. (2016). Diversity in neural firing dynamics supports both rigid and learned hippocampal sequences. Science 351, 1440–1443.'
   'Chen, Z., Grosmark, A.D., Penagos, H., and Wilson, M.A. (2016). Uncovering representations of sleep-associated hippocampal ensemble spike activity. Sci. Rep. 6, 32193.']
  session_id: Gatsby_08282013
  Group /general/subject (Subject) 
  identifier: 199756d2-e8bc-4414-bd41-6e41c0bee258
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (3,) | dtype = int64
  Dataset /intervals/epochs/label (VectorData) Name of epoch. | shape = (3,) | dtype = object
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (3,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (3,) | dtype = float64
  Group /processing/behavior (ProcessingModule) Contains behavioral data.
  Group /processing/behavior/CircularMazeLinearizedPosition (Position) 
  Group /processing/behavior/CircularMazeLinearizedPosition/CircularMazeLinearizedTimeSeries (SpatialSeries) Linearized position, defined as starting at the edge of reward area, and increasing clockwise, terminating at the opposing edge of the reward area.
  Group /processing/behavior/CircularMazePosition (Position) 
  Group /processing/behavior/CircularMazePosition/CircularMazeSpatialSeries (SpatialSeries) (x,y) coordinates tracking subject movement through the maze.
  Group /processing/behavior/states (TimeIntervals) Sleep states of animal.
  Dataset /processing/behavior/states/id (ElementIdentifiers)  | shape = (270,) | dtype = int64
  Dataset /processing/behavior/states/label (VectorData) Sleep state. | shape = (270,) | dtype = object
  Dataset /processing/behavior/states/start_time (VectorData) Start time of epoch, in seconds | shape = (270,) | dtype = float32
  Dataset /processing/behavior/states/stop_time (VectorData) Stop time of epoch, in seconds | shape = (270,) | dtype = float32
  Group /processing/ecephys (ProcessingModule) Intermediate data from extracellular electrophysiology recordings, e.g., LFP.
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/LFP (ElectricalSeries) Local field potential signal.
  Dataset /processing/ecephys/LFP/LFP/electrodes (DynamicTableRegion) electrode_table_region | shape = (128,) | dtype = int64
  session_description: This data set is composed of eight bilateral silicon-probe multi-cellular electrophysiological 
  session_start_time: 2013-08-28T00:00:00-04:00
  timestamps_reference_time: 2013-08-28T00:00:00-04:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/cell_type (VectorData) Type of cell this has been classified as. | shape = (51,) | dtype = object
  Dataset /units/id (ElementIdentifiers)  | shape = (51,) | dtype = int64
  Dataset /units/location (VectorData) Brain region where each unit was detected. | shape = (51,) | dtype = object
  Dataset /units/shank_id (VectorData) 0-indexed id of cluster identified from the shank. | shape = (51,) | dtype = int64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (5775679,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (51,) | dtype = uint32
