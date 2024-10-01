
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000688/draft
name: Long-term recordings of motor and premotor cortical spiking activity during reaching in monkeys
contributor: [{'url': 'https://ma.ttperi.ch/', 'name': 'Perich, Matthew G.', 'email': 'matthew.perich@umontreal.ca', 'roleName': ['dcite:ContactPerson', 'dcite:DataCollector', 'dcite:DataManager', 'dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0001-9800-2386', 'affiliation': [], 'includeInCitation': True}, {'name': 'Miller, Lee E.', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0001-8675-7140', 'affiliation': [], 'includeInCitation': True}, {'url': 'https://www.mehai.dev/', 'name': 'Azabou, Mehdi', 'email': 'mehdiazabou@gmail.com', 'roleName': [], 'schemaKey': 'Person', 'identifier': '0000-0001-8778-9507', 'affiliation': [], 'includeInCitation': True}, {'name': 'Dyer, Eva L.', 'email': 'evadyer@gatech.edu', 'roleName': [], 'schemaKey': 'Person', 'identifier': '0000-0002-6962-524X', 'affiliation': [], 'includeInCitation': True}]
description: This dataset contains electrophysiology and behavioral data from three macaques performing either a center-out task or a continuous random target acquisition task. Neural activity was recorded from chronically-implanted electrode arrays in the primary motor cortex (M1) or dorsal premotor cortex (PMd) of four rhesus macaque monkeys. A subset of sessions includes recordings from both regions simultaneously. The data contains spiking activity—manually spike sorted in three subjects, and threshold crossings in the fourth subject—obtained from up to 192 electrodes per session, cursor position and velocity, and other task related metadata.
assetsSummary: {'species': [{'name': 'Macaca fascicularis - Cynomolgus monkeys', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9541'}, {'name': 'Macaca mulatta - Rhesus monkey', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9544'}], 'approach': [{'name': 'behavioral approach', 'schemaKey': 'ApproachType'}, {'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 12238349474, 'numberOfFiles': 103, 'numberOfSubjects': 4, 'variableMeasured': ['ProcessingModule', 'SpatialSeries', 'Units', 'Position', 'ElectrodeGroup', 'BehavioralTimeSeries'], 'measurementTechnique': [{'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000688 has 100 NWB files.
35 of these NWB files are of type 1.
44 of these NWB files are of type 2.
15 of these NWB files are of type 3.
6 of these NWB files are of type 4.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2024-02-04T23:26:41.152674-05:00']
  Group /general/devices/electrode_array_M1 (Device) 96-electrode Utah array in M1
  Group /general/devices/electrode_array_PMd (Device) 96-electrode Utah array in PMd
  experiment_description: Center-out delayed reaching task
  experimenter: ['Perich, Matthew G.']
  Group /general/extracellular_ephys/electrode_group_M1 (ElectrodeGroup) 96-electrode Utah array in M1
  Group /general/extracellular_ephys/electrode_group_M1/device (Device) 96-electrode Utah array in M1
  Group /general/extracellular_ephys/electrode_group_PMd (ElectrodeGroup) 96-electrode Utah array in PMd
  Group /general/extracellular_ephys/electrode_group_PMd/device (Device) 96-electrode Utah array in PMd
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/bank (VectorData) bank of the electrode | shape = (192,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering, including the filter name and frequency cutoffs | shape = (192,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (192,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (192,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (192,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/label (VectorData) label of the electrode | shape = (192,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (192,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/pin (VectorData) pin of the electrode | shape = (192,) | dtype = int64
  institution: Northwestern University
  keywords: ['motor cortex' 'reaching' 'neural data' 'spike sorting']
  lab: Miller
  related_publications: ['doi: 10.1016/j.neuron.2018.09.030' 'doi: 10.48550/arXiv.2310.16046'
   'doi: 10.1007/s00221-017-4997-1' 'doi: DOI:10.1038/s41593-019-0555-4'
   'doi: 10.1038/s41467-018-04062-6']
  session_id: sub-C_ses-CO-20160909
  Group /general/subject (Subject) 
  identifier: 8186ea8f-5602-435b-8109-0aa0157a1e22
  Group /intervals/trials (TimeIntervals) Delayed center-out reaching trial.
  Dataset /intervals/trials/go_cue_time (VectorData) time when the go cue is given | shape = (335,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (335,) | dtype = int64
  Dataset /intervals/trials/result (VectorData) trial outcome, R: reward, A: abort, F: fail, I: incomplete | shape = (335,) | dtype = object
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (335,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (335,) | dtype = float64
  Dataset /intervals/trials/target_corners (VectorData) target corners | shape = (335, 4) | dtype = float64
  Dataset /intervals/trials/target_dir (VectorData) target direction | shape = (335,) | dtype = float64
  Dataset /intervals/trials/target_id (VectorData) target id | shape = (335,) | dtype = float64
  Dataset /intervals/trials/target_on_time (VectorData) time when the target is shown | shape = (335,) | dtype = float64
  Group /processing/behavior (ProcessingModule) Processed Behavioral data
  Group /processing/behavior/Acceleration (BehavioralTimeSeries) 
  Group /processing/behavior/Acceleration/cursor_acc (TimeSeries) Cursor acceleration (ax, ay).
  Group /processing/behavior/Position (Position) 
  Group /processing/behavior/Position/cursor_pos (SpatialSeries) Cursor position (x, y) on the screen.
  Group /processing/behavior/Velocity (BehavioralTimeSeries) 
  Group /processing/behavior/Velocity/cursor_vel (TimeSeries) Cursor velocity (vx, vy).
  session_description: Monkey C performing center-out reaching task. Warning: This session with Monkey
  session_start_time: 2016-09-09T18:02:43.173000-04:00
  timestamps_reference_time: 2016-09-09T18:02:43.173000-04:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (246,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex) Index for VectorData 'electrodes' | shape = (246,) | dtype = uint8
  Dataset /units/id (ElementIdentifiers)  | shape = (246,) | dtype = int64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (1886568,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (246,) | dtype = uint32
  Dataset /units/waveforms (VectorData) Individual waveforms for each spike. If the dataset is three-dimensional, the third dimension shows the response from different electrodes that all observe this unit simultaneously. In this case, the `electrodes` column of this Units table should be used to indicate which electrodes are associated with this unit, and the electrodes dimension here should be in the same order as the electrodes referenced in the `electrodes` column of this table. | shape = (90555264, 1) | dtype = int16
  Dataset /units/waveforms_index (VectorIndex) Index for VectorData 'waveforms' | shape = (1886568,) | dtype = uint32
  Dataset /units/waveforms_index_index (VectorIndex) Index for VectorData 'waveforms_index' | shape = (246,) | dtype = uint32


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2024-02-04T22:38:43.497397-05:00']
  Group /general/devices/electrode_array_M1 (Device) 96-electrode Utah array in M1
  experiment_description: Center-out delayed reaching task
  experimenter: ['Perich, Matthew G.']
  Group /general/extracellular_ephys/electrode_group_M1 (ElectrodeGroup) 96-electrode Utah array in M1
  Group /general/extracellular_ephys/electrode_group_M1/device (Device) 96-electrode Utah array in M1
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/bank (VectorData) bank of the electrode | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering, including the filter name and frequency cutoffs | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (96,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/label (VectorData) label of the electrode | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/pin (VectorData) pin of the electrode | shape = (96,) | dtype = int64
  institution: Northwestern University
  keywords: ['motor cortex' 'reaching' 'neural data' 'spike sorting']
  lab: Miller
  related_publications: ['doi: 10.1016/j.neuron.2018.09.030' 'doi: 10.48550/arXiv.2310.16046'
   'doi: 10.1007/s00221-017-4997-1' 'doi: DOI:10.1038/s41593-019-0555-4'
   'doi: 10.1038/s41467-018-04062-6']
  session_id: sub-C_ses-CO-20131003
  Group /general/subject (Subject) 
  identifier: 0fb6a9f9-ef4a-4f07-a7bf-c853843694eb
  Group /intervals/trials (TimeIntervals) Delayed center-out reaching trial.
  Dataset /intervals/trials/go_cue_time (VectorData) time when the go cue is given | shape = (193,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (193,) | dtype = int64
  Dataset /intervals/trials/result (VectorData) trial outcome, R: reward, A: abort, F: fail, I: incomplete | shape = (193,) | dtype = object
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (193,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (193,) | dtype = float64
  Dataset /intervals/trials/target_corners (VectorData) target corners | shape = (193, 4) | dtype = float64
  Dataset /intervals/trials/target_dir (VectorData) target direction | shape = (193,) | dtype = float64
  Dataset /intervals/trials/target_id (VectorData) target id | shape = (193,) | dtype = float64
  Dataset /intervals/trials/target_on_time (VectorData) time when the target is shown | shape = (193,) | dtype = float64
  Group /processing/behavior (ProcessingModule) Processed Behavioral data
  Group /processing/behavior/Acceleration (BehavioralTimeSeries) 
  Group /processing/behavior/Acceleration/cursor_acc (TimeSeries) Cursor acceleration (ax, ay).
  Group /processing/behavior/Position (Position) 
  Group /processing/behavior/Position/cursor_pos (SpatialSeries) Cursor position (x, y) on the screen.
  Group /processing/behavior/Velocity (BehavioralTimeSeries) 
  Group /processing/behavior/Velocity/cursor_vel (TimeSeries) Cursor velocity (vx, vy).
  session_description: Monkey C performing center-out reaching task.
  session_start_time: 2013-10-03T12:39:08.680000-04:00
  timestamps_reference_time: 2013-10-03T12:39:08.680000-04:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (71,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex) Index for VectorData 'electrodes' | shape = (71,) | dtype = uint8
  Dataset /units/id (ElementIdentifiers)  | shape = (71,) | dtype = int64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (319409,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (71,) | dtype = uint32
  Dataset /units/waveforms (VectorData) Individual waveforms for each spike. If the dataset is three-dimensional, the third dimension shows the response from different electrodes that all observe this unit simultaneously. In this case, the `electrodes` column of this Units table should be used to indicate which electrodes are associated with this unit, and the electrodes dimension here should be in the same order as the electrodes referenced in the `electrodes` column of this table. | shape = (15331632, 1) | dtype = int16
  Dataset /units/waveforms_index (VectorIndex) Index for VectorData 'waveforms' | shape = (319409,) | dtype = uint32
  Dataset /units/waveforms_index_index (VectorIndex) Index for VectorData 'waveforms_index' | shape = (71,) | dtype = uint32


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2024-02-04T23:26:24.427385-05:00']
  Group /general/devices/electrode_array_M1 (Device) 96-electrode Utah array in M1
  experiment_description: Random target reaching task
  experimenter: ['Perich, Matthew G.']
  Group /general/extracellular_ephys/electrode_group_M1 (ElectrodeGroup) 96-electrode Utah array in M1
  Group /general/extracellular_ephys/electrode_group_M1/device (Device) 96-electrode Utah array in M1
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/bank (VectorData) bank of the electrode | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering, including the filter name and frequency cutoffs | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (96,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/label (VectorData) label of the electrode | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/pin (VectorData) pin of the electrode | shape = (96,) | dtype = int64
  institution: Northwestern University
  keywords: ['motor cortex' 'reaching' 'neural data' 'spike sorting']
  lab: Miller
  related_publications: ['doi: 10.1016/j.neuron.2018.09.030' 'doi: 10.48550/arXiv.2310.16046'
   'doi: 10.1007/s00221-017-4997-1' 'doi: DOI:10.1038/s41593-019-0555-4'
   'doi: 10.1038/s41467-018-04062-6']
  session_id: sub-C_ses-RT-20131009
  Group /general/subject (Subject) 
  identifier: 262f9a05-976b-4b50-88b4-f494ba06c70d
  Group /intervals/trials (TimeIntervals) experimental trials.
  Dataset /intervals/trials/go_cue_time_array (VectorData) time when the go cue is given | shape = (187, 4) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (187,) | dtype = int64
  Dataset /intervals/trials/num_attempted (VectorData) number of attempted targets | shape = (187,) | dtype = float64
  Dataset /intervals/trials/num_targets (VectorData) number of targets | shape = (187,) | dtype = uint8
  Dataset /intervals/trials/result (VectorData) trial outcome, R: reward, A: abort, F: fail, I: incomplete | shape = (187,) | dtype = object
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (187,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (187,) | dtype = float64
  Dataset /intervals/trials/target_dir (VectorData) target direction | shape = (187,) | dtype = float64
  Dataset /intervals/trials/target_id (VectorData) target id | shape = (187, 4) | dtype = float64
  Dataset /intervals/trials/target_size (VectorData) target size | shape = (187,) | dtype = float64
  Group /processing/behavior (ProcessingModule) Processed Behavioral data
  Group /processing/behavior/Acceleration (BehavioralTimeSeries) 
  Group /processing/behavior/Acceleration/cursor_acc (TimeSeries) Cursor acceleration (ax, ay).
  Group /processing/behavior/Position (Position) 
  Group /processing/behavior/Position/cursor_pos (SpatialSeries) Cursor position (x, y) on the screen.
  Group /processing/behavior/Velocity (BehavioralTimeSeries) 
  Group /processing/behavior/Velocity/cursor_vel (TimeSeries) Cursor velocity (vx, vy).
  session_description: Monkey C performing random target reaching task.
  session_start_time: 2013-10-09T13:02:29.468000-04:00
  timestamps_reference_time: 2013-10-09T13:02:29.468000-04:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (74,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex) Index for VectorData 'electrodes' | shape = (74,) | dtype = uint8
  Dataset /units/id (ElementIdentifiers)  | shape = (74,) | dtype = int64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (604037,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (74,) | dtype = uint32
  Dataset /units/waveforms (VectorData) Individual waveforms for each spike. If the dataset is three-dimensional, the third dimension shows the response from different electrodes that all observe this unit simultaneously. In this case, the `electrodes` column of this Units table should be used to indicate which electrodes are associated with this unit, and the electrodes dimension here should be in the same order as the electrodes referenced in the `electrodes` column of this table. | shape = (28993776, 1) | dtype = int16
  Dataset /units/waveforms_index (VectorIndex) Index for VectorData 'waveforms' | shape = (604037,) | dtype = uint32
  Dataset /units/waveforms_index_index (VectorIndex) Index for VectorData 'waveforms_index' | shape = (74,) | dtype = uint32


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2024-02-04T22:24:46.103627-05:00']
  Group /general/devices/electrode_array_M1 (Device) 96-electrode Utah array in M1
  Group /general/devices/electrode_array_PMd (Device) 96-electrode Utah array in PMd
  experiment_description: Random target reaching task
  experimenter: ['Perich, Matthew G.']
  Group /general/extracellular_ephys/electrode_group_M1 (ElectrodeGroup) 96-electrode Utah array in M1
  Group /general/extracellular_ephys/electrode_group_M1/device (Device) 96-electrode Utah array in M1
  Group /general/extracellular_ephys/electrode_group_PMd (ElectrodeGroup) 96-electrode Utah array in PMd
  Group /general/extracellular_ephys/electrode_group_PMd/device (Device) 96-electrode Utah array in PMd
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/bank (VectorData) bank of the electrode | shape = (192,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering, including the filter name and frequency cutoffs | shape = (192,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (192,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (192,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (192,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/label (VectorData) label of the electrode | shape = (192,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (192,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/pin (VectorData) pin of the electrode | shape = (192,) | dtype = int64
  institution: Northwestern University
  keywords: ['motor cortex' 'reaching' 'neural data' 'spike sorting']
  lab: Miller
  related_publications: ['doi: 10.1016/j.neuron.2018.09.030' 'doi: 10.48550/arXiv.2310.16046'
   'doi: 10.1007/s00221-017-4997-1' 'doi: DOI:10.1038/s41593-019-0555-4'
   'doi: 10.1038/s41467-018-04062-6']
  session_id: sub-M_ses-RT-20140114
  Group /general/subject (Subject) 
  identifier: aa332c7c-4ebb-4bd0-94f7-46d1410038d7
  Group /intervals/trials (TimeIntervals) experimental trials.
  Dataset /intervals/trials/go_cue_time_array (VectorData) time when the go cue is given | shape = (252, 4) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (252,) | dtype = int64
  Dataset /intervals/trials/num_attempted (VectorData) number of attempted targets | shape = (252,) | dtype = float64
  Dataset /intervals/trials/num_targets (VectorData) number of targets | shape = (252,) | dtype = uint8
  Dataset /intervals/trials/result (VectorData) trial outcome, R: reward, A: abort, F: fail, I: incomplete | shape = (252,) | dtype = object
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (252,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (252,) | dtype = float64
  Dataset /intervals/trials/target_dir (VectorData) target direction | shape = (252,) | dtype = float64
  Dataset /intervals/trials/target_id (VectorData) target id | shape = (252, 4) | dtype = float64
  Dataset /intervals/trials/target_size (VectorData) target size | shape = (252,) | dtype = float64
  Group /processing/behavior (ProcessingModule) Processed Behavioral data
  Group /processing/behavior/Acceleration (BehavioralTimeSeries) 
  Group /processing/behavior/Acceleration/cursor_acc (TimeSeries) Cursor acceleration (ax, ay).
  Group /processing/behavior/Position (Position) 
  Group /processing/behavior/Position/cursor_pos (SpatialSeries) Cursor position (x, y) on the screen.
  Group /processing/behavior/Velocity (BehavioralTimeSeries) 
  Group /processing/behavior/Velocity/cursor_vel (TimeSeries) Cursor velocity (vx, vy).
  session_description: Monkey M performing random target reaching task.
  session_start_time: 2014-01-14T13:11:23.561000-05:00
  timestamps_reference_time: 2014-01-14T13:11:23.561000-05:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (165,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex) Index for VectorData 'electrodes' | shape = (165,) | dtype = uint8
  Dataset /units/id (ElementIdentifiers)  | shape = (165,) | dtype = int64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (1068112,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (165,) | dtype = uint32
  Dataset /units/waveforms (VectorData) Individual waveforms for each spike. If the dataset is three-dimensional, the third dimension shows the response from different electrodes that all observe this unit simultaneously. In this case, the `electrodes` column of this Units table should be used to indicate which electrodes are associated with this unit, and the electrodes dimension here should be in the same order as the electrodes referenced in the `electrodes` column of this table. | shape = (51269376, 1) | dtype = int16
  Dataset /units/waveforms_index (VectorIndex) Index for VectorData 'waveforms' | shape = (1068112,) | dtype = uint32
  Dataset /units/waveforms_index_index (VectorIndex) Index for VectorData 'waveforms_index' | shape = (165,) | dtype = uint32
