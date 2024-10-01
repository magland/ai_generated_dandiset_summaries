
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000019/0.220126.2148
name: Human ECoG speaking consonant-vowel syllables
contributor: [{'name': 'Bouchard, Kristofer E.', 'roleName': ['dcite:Author', 'dcite:DataCollector', 'dcite:FormalAnalysis'], 'schemaKey': 'Person', 'identifier': '0000-0002-1974-4603', 'includeInCitation': True}, {'name': 'Chang, Edward F.', 'email': 'Edward.Chang@ucsf.edu', 'roleName': ['dcite:Author', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}]
description: The enclosed data is collected using a high-density 256-channel electrocorticography (ECoG) array implanted in human patients during treatment for epilepsy. The subjects are reading aloud consonant-vowel syllables from a list. The data was collected by Dr. Edward Chang and Dr. Kristofer Bouchard at the University of California, San Francisco, and curated by Dr. Kristofer Bouchard and Dr. Benjamin Dichter.


Data is organized by subject ID, and each file is a continuous recording session in Neurodata Without Borders (NWB) 2.0 format. Voltage traces are included for each of the recorded 256 channels. Microphone signal was recorded at the time but is removed for HIPAA compliance. Detailed hand-marked annotations are provided which mark what syllable was said, and the times of the start, consonant-vowel transition, and end of each syllable. A rest-period time is also included when the subject was silent, which can be used as a baseline. Hand-marked anatomical labels are included for electrodes in the relevant brain regions. All dates have been removed for HIPAA compliance and replaced with Jan 1, 1900.
assetsSummary: {'species': [{'name': 'Human', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9606'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 55585858956, 'numberOfFiles': 31, 'numberOfSubjects': 4, 'variableMeasured': ['ElectrodeGroup', 'ElectricalSeries', 'ProcessingModule', 'Spectrum'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'fourier analysis technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000019 has 24 NWB files.
1 of these NWB files are of type 1.
13 of these NWB files are of type 2.
2 of these NWB files are of type 3.
6 of these NWB files are of type 4.
2 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeries (ElectricalSeries) all Wav data
  Dataset /acquisition/ElectricalSeries/electrodes (DynamicTableRegion) ECoG electrodes on brain | shape = (256,) | dtype = int64
  file_create_date: ['2019-06-19T11:07:43.198581-07:00']
  Group /general/devices/L256Grid (Device) 
  Group /general/extracellular_ephys/L256Grid electrodes (ElectrodeGroup) L256Grid
  Group /general/extracellular_ephys/L256Grid electrodes/device (Device) 
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/bad (VectorData) electrode identified as too noisy | shape = (256,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (256,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (256,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (256,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (256,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (256,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (256,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (256,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (256,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (256,) | dtype = float64
  institution: University of California, San Francisco
  lab: Chang Lab
  session_id: EC2_B1
  Group /general/subject (Subject) 
  identifier: EC2_B1
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /intervals/epochs/label (VectorData) label | shape = (1,) | dtype = object
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (1,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1,) | dtype = float64
  Group /intervals/invalid_times (TimeIntervals) time intervals to be removed from analysis
  Dataset /intervals/invalid_times/id (ElementIdentifiers)  | shape = (6,) | dtype = int64
  Dataset /intervals/invalid_times/start_time (VectorData) Start time of epoch, in seconds | shape = (6,) | dtype = float64
  Dataset /intervals/invalid_times/stop_time (VectorData) Stop time of epoch, in seconds | shape = (6,) | dtype = float64
  Dataset /intervals/invalid_times/tags (VectorData) user-defined tags | shape = (6,) | dtype = object
  Dataset /intervals/invalid_times/tags_index (VectorIndex)  | shape = (6,) | dtype = int64
  Dataset /intervals/invalid_times/timeseries (VectorData) index into a TimeSeries object | shape = (6,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/invalid_times/timeseries_index (VectorIndex)  | shape = (6,) | dtype = int64
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/condition (VectorData) syllable spoken | shape = (387,) | dtype = object
  Dataset /intervals/trials/cv_transition_time (VectorData) time of CV transition in seconds | shape = (387,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (387,) | dtype = int64
  Dataset /intervals/trials/speak (VectorData) if True, subject is speaking. If False, subject is listening | shape = (387,) | dtype = bool
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (387,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (387,) | dtype = float64
  Group /processing/ecephys (ProcessingModule) desc
  Group /processing/ecephys/spectrum (Spectrum) 
  Group /processing/ecephys/spectrum/source_timeseries (ElectricalSeries) all Wav data
  Dataset /processing/ecephys/spectrum/source_timeseries/electrodes (DynamicTableRegion) ECoG electrodes on brain | shape = (256,) | dtype = int64
  session_description: EC2_B1
  session_start_time: 1900-01-01T08:00:00+00:00
  timestamps_reference_time: 1900-01-01T08:00:00+00:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeries (ElectricalSeries) all Wav data
  Dataset /acquisition/ElectricalSeries/electrodes (DynamicTableRegion) ECoG electrodes on brain | shape = (256,) | dtype = int64
  file_create_date: ['2019-06-19T11:18:11.234373-07:00']
  Group /general/devices/L256Grid (Device) 
  Group /general/extracellular_ephys/L256Grid electrodes (ElectrodeGroup) L256Grid
  Group /general/extracellular_ephys/L256Grid electrodes/device (Device) 
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/bad (VectorData) electrode identified as too noisy | shape = (256,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (256,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (256,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (256,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (256,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (256,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (256,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (256,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (256,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (256,) | dtype = float64
  institution: University of California, San Francisco
  lab: Chang Lab
  session_id: EC2_B105
  Group /general/subject (Subject) 
  identifier: EC2_B105
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /intervals/epochs/label (VectorData) label | shape = (1,) | dtype = object
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (1,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1,) | dtype = float64
  Group /intervals/invalid_times (TimeIntervals) time intervals to be removed from analysis
  Dataset /intervals/invalid_times/id (ElementIdentifiers)  | shape = (5,) | dtype = int64
  Dataset /intervals/invalid_times/start_time (VectorData) Start time of epoch, in seconds | shape = (5,) | dtype = float64
  Dataset /intervals/invalid_times/stop_time (VectorData) Stop time of epoch, in seconds | shape = (5,) | dtype = float64
  Dataset /intervals/invalid_times/tags (VectorData) user-defined tags | shape = (5,) | dtype = object
  Dataset /intervals/invalid_times/tags_index (VectorIndex)  | shape = (5,) | dtype = int64
  Dataset /intervals/invalid_times/timeseries (VectorData) index into a TimeSeries object | shape = (5,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/invalid_times/timeseries_index (VectorIndex)  | shape = (5,) | dtype = int64
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/condition (VectorData) syllable spoken | shape = (311,) | dtype = object
  Dataset /intervals/trials/cv_transition_time (VectorData) time of CV transition in seconds | shape = (311,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (311,) | dtype = int64
  Dataset /intervals/trials/speak (VectorData) if True, subject is speaking. If False, subject is listening | shape = (311,) | dtype = bool
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (311,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (311,) | dtype = float64
  session_description: EC2_B105
  session_start_time: 1900-01-01T08:00:00+00:00
  timestamps_reference_time: 1900-01-01T08:00:00+00:00


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeries (ElectricalSeries) all Wav data
  Dataset /acquisition/ElectricalSeries/electrodes (DynamicTableRegion) ECoG electrodes on brain | shape = (256,) | dtype = int64
  file_create_date: ['2019-06-19T12:20:57.567169-07:00']
  Group /general/devices/256Grid (Device) 
  Group /general/extracellular_ephys/256Grid electrodes (ElectrodeGroup) auto_group
  Group /general/extracellular_ephys/256Grid electrodes/device (Device) 
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/bad (VectorData) electrode identified as too noisy | shape = (256,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (256,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (256,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (256,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (256,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (256,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (256,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (256,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (256,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (256,) | dtype = float64
  institution: University of California, San Francisco
  lab: Chang Lab
  session_id: EC9_B15
  Group /general/subject (Subject) 
  identifier: EC9_B15
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /intervals/epochs/label (VectorData) label | shape = (1,) | dtype = object
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (1,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1,) | dtype = float64
  Group /intervals/invalid_times (TimeIntervals) time intervals to be removed from analysis
  Dataset /intervals/invalid_times/id (ElementIdentifiers)  | shape = (25,) | dtype = int64
  Dataset /intervals/invalid_times/start_time (VectorData) Start time of epoch, in seconds | shape = (25,) | dtype = float64
  Dataset /intervals/invalid_times/stop_time (VectorData) Stop time of epoch, in seconds | shape = (25,) | dtype = float64
  Dataset /intervals/invalid_times/tags (VectorData) user-defined tags | shape = (25,) | dtype = object
  Dataset /intervals/invalid_times/tags_index (VectorIndex)  | shape = (25,) | dtype = int64
  Dataset /intervals/invalid_times/timeseries (VectorData) index into a TimeSeries object | shape = (25,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/invalid_times/timeseries_index (VectorIndex)  | shape = (25,) | dtype = int64
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/condition (VectorData) syllable spoken | shape = (70,) | dtype = object
  Dataset /intervals/trials/cv_transition_time (VectorData) time of CV transition in seconds | shape = (70,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (70,) | dtype = int64
  Dataset /intervals/trials/speak (VectorData) if True, subject is speaking. If False, subject is listening | shape = (70,) | dtype = bool
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (70,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (70,) | dtype = float64
  session_description: EC9_B15
  session_start_time: 1900-01-01T08:00:00+00:00
  timestamps_reference_time: 1900-01-01T08:00:00+00:00


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeries (ElectricalSeries) all Wav data
  Dataset /acquisition/ElectricalSeries/electrodes (DynamicTableRegion) ECoG electrodes on brain | shape = (256,) | dtype = int64
  file_create_date: ['2019-06-19T12:23:02.665179-07:00']
  Group /general/devices/auto_device (Device) 
  Group /general/extracellular_ephys/auto_group (ElectrodeGroup) auto_group
  Group /general/extracellular_ephys/auto_group/device (Device) 
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/bad (VectorData) electrode identified as too noisy | shape = (256,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (256,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (256,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (256,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (256,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (256,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (256,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (256,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (256,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (256,) | dtype = float64
  institution: University of California, San Francisco
  lab: Chang Lab
  session_id: EC9_B46
  Group /general/subject (Subject) 
  identifier: EC9_B46
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /intervals/epochs/label (VectorData) label | shape = (1,) | dtype = object
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (1,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1,) | dtype = float64
  Group /intervals/invalid_times (TimeIntervals) time intervals to be removed from analysis
  Dataset /intervals/invalid_times/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /intervals/invalid_times/start_time (VectorData) Start time of epoch, in seconds | shape = (1,) | dtype = float64
  Dataset /intervals/invalid_times/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1,) | dtype = float64
  Dataset /intervals/invalid_times/tags (VectorData) user-defined tags | shape = (1,) | dtype = object
  Dataset /intervals/invalid_times/tags_index (VectorIndex)  | shape = (1,) | dtype = int64
  Dataset /intervals/invalid_times/timeseries (VectorData) index into a TimeSeries object | shape = (1,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/invalid_times/timeseries_index (VectorIndex)  | shape = (1,) | dtype = int64
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/condition (VectorData) syllable spoken | shape = (227,) | dtype = object
  Dataset /intervals/trials/cv_transition_time (VectorData) time of CV transition in seconds | shape = (227,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (227,) | dtype = int64
  Dataset /intervals/trials/speak (VectorData) if True, subject is speaking. If False, subject is listening | shape = (227,) | dtype = bool
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (227,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (227,) | dtype = float64
  session_description: EC9_B46
  session_start_time: 1900-01-01T08:00:00+00:00
  timestamps_reference_time: 1900-01-01T08:00:00+00:00


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeries (ElectricalSeries) all Wav data
  Dataset /acquisition/ElectricalSeries/electrodes (DynamicTableRegion) ECoG electrodes on brain | shape = (256,) | dtype = int64
  file_create_date: ['2019-06-19T12:26:09.660535-07:00']
  Group /general/devices/auto_device (Device) 
  Group /general/extracellular_ephys/auto_group (ElectrodeGroup) auto_group
  Group /general/extracellular_ephys/auto_group/device (Device) 
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/bad (VectorData) electrode identified as too noisy | shape = (256,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (256,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (256,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (256,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (256,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (256,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (256,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (256,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (256,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (256,) | dtype = float64
  institution: University of California, San Francisco
  lab: Chang Lab
  session_id: EC9_B49
  Group /general/subject (Subject) 
  identifier: EC9_B49
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /intervals/epochs/label (VectorData) label | shape = (1,) | dtype = object
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (1,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1,) | dtype = float64
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/condition (VectorData) syllable spoken | shape = (254,) | dtype = object
  Dataset /intervals/trials/cv_transition_time (VectorData) time of CV transition in seconds | shape = (254,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (254,) | dtype = int64
  Dataset /intervals/trials/speak (VectorData) if True, subject is speaking. If False, subject is listening | shape = (254,) | dtype = bool
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (254,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (254,) | dtype = float64
  session_description: EC9_B49
  session_start_time: 1900-01-01T08:00:00+00:00
  timestamps_reference_time: 1900-01-01T08:00:00+00:00
