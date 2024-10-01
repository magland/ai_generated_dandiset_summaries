
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000006/0.220126.1855
name: Mouse anterior lateral motor cortex (ALM) in delay response task
contributor: [{'name': 'Economo, Michael N.', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Svoboda, Karel', 'roleName': ['dcite:Author', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0002-6670-7362', 'affiliation': [], 'includeInCitation': True}]
description: Extracellular electrophysiology recordings performed on mouse anterior lateral motor cortex (ALM) in delay response task. Neural activity from two neuron populations, pyramidal track upper and lower, were characterized, in relation to movement execution. Some files, as originally (re)distributed from e.g. http://datasets.datalad.org/?dir=/labs/svoboda/Economo_2018 were found to be broken and would not be able available among reorganized files under sub-* directories.
assetsSummary: {'species': [{'name': 'House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}, {'name': 'behavioral approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 139600500, 'numberOfFiles': 53, 'numberOfSubjects': 12, 'variableMeasured': ['Units', 'ElectrodeGroup', 'BehavioralEvents'], 'measurementTechnique': [{'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000006 has 38 NWB files.
15 of these NWB files are of type 1.
6 of these NWB files are of type 2.
9 of these NWB files are of type 3.
2 of these NWB files are of type 4.
6 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/lick_times (BehavioralEvents) 
  Group /acquisition/lick_times/lick_left_times (TimeSeries) no description
  Group /acquisition/lick_times/lick_right_times (TimeSeries) no description
  file_create_date: ['2019-10-07T17:40:36.567483-05:00']
  Group /general/devices/H-129 (Device) 
  experiment_description: Extracellular electrophysiology recordings performed on mouse anterior lateral motor cortex (ALM) in delay response task. Neural activity from two neuron populations, pyramidal track upper and lower, were characterized, in relation to movement execution.
  experimenter: Mike Economo
  Group /general/extracellular_ephys/H-129: 64 (ElectrodeGroup) N/A
  Group /general/extracellular_ephys/H-129: 64/device (Device) 
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (64,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (64,) | dtype = float64
  institution: Janelia Research Campus
  keywords: ['motor planning' 'premotor cortex' 'preparatory activity'
   'extracellular electrophysiology']
  related_publications: doi:10.1038/s41586-018-0642-9
  Group /general/subject (Subject) 
  identifier: anm369962_2017-03-09_0
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/cue_start_time (VectorData) onset of response period | shape = (274,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (274,) | dtype = int32
  Dataset /intervals/trials/is_good (VectorData) good/bad status of trial (bad trials are not analyzed) | shape = (274,) | dtype = int32
  Dataset /intervals/trials/pole_in_time (VectorData) onset of sample period | shape = (274,) | dtype = float64
  Dataset /intervals/trials/pole_out_time (VectorData) onset of the delay period | shape = (274,) | dtype = float64
  Dataset /intervals/trials/response (VectorData)  | shape = (274,) | dtype = object
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (274,) | dtype = float64
  Dataset /intervals/trials/stim_present (VectorData) is this a stim or no-stim trial | shape = (274,) | dtype = int32
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (274,) | dtype = float64
  Dataset /intervals/trials/type (VectorData)  | shape = (274,) | dtype = object
  session_description: 
  session_start_time: 2017-03-09T00:00:00-06:00
  timestamps_reference_time: 2017-03-09T00:00:00-06:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/cell_type (VectorData) cell type (e.g. wide width, narrow width spiking) | shape = (3,) | dtype = object
  Dataset /units/depth (VectorData) depth this unit (um) | shape = (3,) | dtype = float64
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (3,) | dtype = int32
  Dataset /units/electrodes_index (VectorIndex)  | shape = (3,) | dtype = int32
  Dataset /units/id (ElementIdentifiers)  | shape = (3,) | dtype = int32
  Dataset /units/quality (VectorData) quality of the spike sorted unit (e.g. excellent, good, poor, fair, etc.) | shape = (3,) | dtype = object
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (62896,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex)  | shape = (3,) | dtype = int32


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/lick_times (BehavioralEvents) 
  Group /acquisition/lick_times/lick_left_times (TimeSeries) no description
  Group /acquisition/lick_times/lick_right_times (TimeSeries) no description
  file_create_date: ['2019-10-07T17:40:50.335488-05:00']
  Group /general/devices/H-193 (Device) 
  experiment_description: Extracellular electrophysiology recordings performed on mouse anterior lateral motor cortex (ALM) in delay response task. Neural activity from two neuron populations, pyramidal track upper and lower, were characterized, in relation to movement execution.
  experimenter: Mike Economo
  Group /general/extracellular_ephys/H-193: 64 (ElectrodeGroup) N/A
  Group /general/extracellular_ephys/H-193: 64/device (Device) 
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (64,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (64,) | dtype = float64
  institution: Janelia Research Campus
  keywords: ['motor planning' 'premotor cortex' 'preparatory activity'
   'extracellular electrophysiology']
  related_publications: doi:10.1038/s41586-018-0642-9
  Group /general/subject (Subject) 
  identifier: anm369962_2017-03-13_0
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/cue_start_time (VectorData) onset of response period | shape = (354,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (354,) | dtype = int32
  Dataset /intervals/trials/is_good (VectorData) good/bad status of trial (bad trials are not analyzed) | shape = (354,) | dtype = int32
  Dataset /intervals/trials/pole_in_time (VectorData) onset of sample period | shape = (354,) | dtype = float64
  Dataset /intervals/trials/pole_out_time (VectorData) onset of the delay period | shape = (354,) | dtype = float64
  Dataset /intervals/trials/response (VectorData)  | shape = (354,) | dtype = object
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (354,) | dtype = float64
  Dataset /intervals/trials/stim_present (VectorData) is this a stim or no-stim trial | shape = (354,) | dtype = int32
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (354,) | dtype = float64
  Dataset /intervals/trials/type (VectorData)  | shape = (354,) | dtype = object
  session_description: 
  session_start_time: 2017-03-13T00:00:00-05:00
  timestamps_reference_time: 2017-03-13T00:00:00-05:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/cell_type (VectorData) cell type (e.g. wide width, narrow width spiking) | shape = (71,) | dtype = object
  Dataset /units/depth (VectorData) depth this unit (um) | shape = (71,) | dtype = float64
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (71,) | dtype = int32
  Dataset /units/electrodes_index (VectorIndex)  | shape = (71,) | dtype = int32
  Dataset /units/id (ElementIdentifiers)  | shape = (71,) | dtype = int32
  Dataset /units/quality (VectorData) quality of the spike sorted unit (e.g. excellent, good, poor, fair, etc.) | shape = (71,) | dtype = object
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (1392414,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex)  | shape = (71,) | dtype = int32


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/lick_times (BehavioralEvents) 
  Group /acquisition/lick_times/lick_left_times (TimeSeries) no description
  Group /acquisition/lick_times/lick_right_times (TimeSeries) no description
  file_create_date: ['2019-10-07T17:41:38.493346-05:00']
  Group /general/devices/H-116 (Device) 
  experiment_description: Extracellular electrophysiology recordings performed on mouse anterior lateral motor cortex (ALM) in delay response task. Neural activity from two neuron populations, pyramidal track upper and lower, were characterized, in relation to movement execution.
  experimenter: Mike Economo
  Group /general/extracellular_ephys/H-116: 64 (ElectrodeGroup) N/A
  Group /general/extracellular_ephys/H-116: 64/device (Device) 
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (64,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (64,) | dtype = float64
  institution: Janelia Research Campus
  keywords: ['motor planning' 'premotor cortex' 'preparatory activity'
   'extracellular electrophysiology']
  related_publications: doi:10.1038/s41586-018-0642-9
  Group /general/subject (Subject) 
  identifier: anm369963_2017-02-26_0
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/cue_start_time (VectorData) onset of response period | shape = (295,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (295,) | dtype = int32
  Dataset /intervals/trials/is_good (VectorData) good/bad status of trial (bad trials are not analyzed) | shape = (295,) | dtype = int32
  Dataset /intervals/trials/pole_in_time (VectorData) onset of sample period | shape = (295,) | dtype = float64
  Dataset /intervals/trials/pole_out_time (VectorData) onset of the delay period | shape = (295,) | dtype = float64
  Dataset /intervals/trials/response (VectorData)  | shape = (295,) | dtype = object
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (295,) | dtype = float64
  Dataset /intervals/trials/stim_present (VectorData) is this a stim or no-stim trial | shape = (295,) | dtype = int32
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (295,) | dtype = float64
  Dataset /intervals/trials/type (VectorData)  | shape = (295,) | dtype = object
  session_description: 
  session_start_time: 2017-02-26T00:00:00-06:00
  timestamps_reference_time: 2017-02-26T00:00:00-06:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/cell_type (VectorData) cell type (e.g. wide width, narrow width spiking) | shape = (49,) | dtype = object
  Dataset /units/depth (VectorData) depth this unit (um) | shape = (49,) | dtype = float64
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (49,) | dtype = int32
  Dataset /units/electrodes_index (VectorIndex)  | shape = (49,) | dtype = int32
  Dataset /units/id (ElementIdentifiers)  | shape = (49,) | dtype = int32
  Dataset /units/quality (VectorData) quality of the spike sorted unit (e.g. excellent, good, poor, fair, etc.) | shape = (49,) | dtype = object
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (759789,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex)  | shape = (49,) | dtype = int32


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/lick_times (BehavioralEvents) 
  Group /acquisition/lick_times/lick_left_times (TimeSeries) no description
  Group /acquisition/lick_times/lick_right_times (TimeSeries) no description
  file_create_date: ['2019-10-07T17:46:20.909672-05:00']
  Group /general/devices/H- (Device) 
  experiment_description: Extracellular electrophysiology recordings performed on mouse anterior lateral motor cortex (ALM) in delay response task. Neural activity from two neuron populations, pyramidal track upper and lower, were characterized, in relation to movement execution.
  experimenter: Mike Economo
  Group /general/extracellular_ephys/H-: 64 (ElectrodeGroup) N/A
  Group /general/extracellular_ephys/H-: 64/device (Device) 
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (64,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (64,) | dtype = float64
  institution: Janelia Research Campus
  keywords: ['motor planning' 'premotor cortex' 'preparatory activity'
   'extracellular electrophysiology']
  related_publications: doi:10.1038/s41586-018-0642-9
  Group /general/subject (Subject) 
  identifier: anm372906_2017-06-08_0
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/cue_start_time (VectorData) onset of response period | shape = (306,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (306,) | dtype = int32
  Dataset /intervals/trials/is_good (VectorData) good/bad status of trial (bad trials are not analyzed) | shape = (306,) | dtype = int32
  Dataset /intervals/trials/pole_in_time (VectorData) onset of sample period | shape = (306,) | dtype = float64
  Dataset /intervals/trials/pole_out_time (VectorData) onset of the delay period | shape = (306,) | dtype = float64
  Dataset /intervals/trials/response (VectorData)  | shape = (306,) | dtype = object
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (306,) | dtype = float64
  Dataset /intervals/trials/stim_present (VectorData) is this a stim or no-stim trial | shape = (306,) | dtype = int32
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (306,) | dtype = float64
  Dataset /intervals/trials/type (VectorData)  | shape = (306,) | dtype = object
  session_description: 
  session_start_time: 2017-06-08T00:00:00-05:00
  timestamps_reference_time: 2017-06-08T00:00:00-05:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/cell_type (VectorData) cell type (e.g. wide width, narrow width spiking) | shape = (57,) | dtype = object
  Dataset /units/depth (VectorData) depth this unit (um) | shape = (57,) | dtype = float64
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (57,) | dtype = int32
  Dataset /units/electrodes_index (VectorIndex)  | shape = (57,) | dtype = int32
  Dataset /units/id (ElementIdentifiers)  | shape = (57,) | dtype = int32
  Dataset /units/quality (VectorData) quality of the spike sorted unit (e.g. excellent, good, poor, fair, etc.) | shape = (57,) | dtype = object
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (824884,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex)  | shape = (57,) | dtype = int32


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  Group /acquisition/lick_times (BehavioralEvents) 
  Group /acquisition/lick_times/lick_left_times (TimeSeries) no description
  Group /acquisition/lick_times/lick_right_times (TimeSeries) no description
  file_create_date: ['2019-10-07T17:42:31.649019-05:00']
  Group /general/devices/H-117 (Device) 
  experiment_description: Extracellular electrophysiology recordings performed on mouse anterior lateral motor cortex (ALM) in delay response task. Neural activity from two neuron populations, pyramidal track upper and lower, were characterized, in relation to movement execution.
  experimenter: Mike Economo
  Group /general/extracellular_ephys/H-117: 64 (ElectrodeGroup) N/A
  Group /general/extracellular_ephys/H-117: 64/device (Device) 
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (64,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (64,) | dtype = float64
  institution: Janelia Research Campus
  keywords: ['motor planning' 'premotor cortex' 'preparatory activity'
   'extracellular electrophysiology']
  related_publications: doi:10.1038/s41586-018-0642-9
  Group /general/subject (Subject) 
  identifier: anm369964_2017-03-20_0
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/cue_start_time (VectorData) onset of response period | shape = (319,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (319,) | dtype = int32
  Dataset /intervals/trials/is_good (VectorData) good/bad status of trial (bad trials are not analyzed) | shape = (319,) | dtype = int32
  Dataset /intervals/trials/pole_in_time (VectorData) onset of sample period | shape = (319,) | dtype = float64
  Dataset /intervals/trials/pole_out_time (VectorData) onset of the delay period | shape = (319,) | dtype = float64
  Dataset /intervals/trials/response (VectorData)  | shape = (319,) | dtype = object
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (319,) | dtype = float64
  Dataset /intervals/trials/stim_present (VectorData) is this a stim or no-stim trial | shape = (319,) | dtype = int32
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (319,) | dtype = float64
  Dataset /intervals/trials/type (VectorData)  | shape = (319,) | dtype = object
  session_description: 
  session_start_time: 2017-03-20T00:00:00-05:00
  timestamps_reference_time: 2017-03-20T00:00:00-05:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/cell_type (VectorData) cell type (e.g. wide width, narrow width spiking) | shape = (55,) | dtype = object
  Dataset /units/depth (VectorData) depth this unit (um) | shape = (55,) | dtype = float64
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (55,) | dtype = int32
  Dataset /units/electrodes_index (VectorIndex)  | shape = (55,) | dtype = int32
  Dataset /units/id (ElementIdentifiers)  | shape = (55,) | dtype = int32
  Dataset /units/quality (VectorData) quality of the spike sorted unit (e.g. excellent, good, poor, fair, etc.) | shape = (55,) | dtype = object
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (918242,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex)  | shape = (55,) | dtype = int32
