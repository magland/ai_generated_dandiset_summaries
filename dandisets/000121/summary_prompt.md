
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000121/0.220124.2156
name: Structure and variability of delay activity in premotor cortex
contributor: [{'name': 'Sharda, Saksham', 'email': 'saksham20.sharda@gmail.com', 'roleName': ['dcite:Software'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': False}, {'url': 'http://orcid.org/0000-0003-2186-5567', 'name': 'Even-Chen, Nir', 'email': ' nirec@stanford.edu', 'roleName': ['dcite:Author', 'dcite:Conceptualization', 'dcite:DataCurator', 'dcite:FormalAnalysis', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0003-2186-5567', 'affiliation': [{'name': 'Department of Electrical Engineering, Stanford University, Stanford, CA, United States of America', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/00f54p054'}], 'includeInCitation': True}, {'url': 'http://orcid.org/0000-0003-2753-7150', 'name': 'Sheffer, Blue', 'email': 'bsheffer@stanford.edu', 'roleName': ['dcite:Author', 'dcite:Conceptualization', 'dcite:DataCurator', 'dcite:FormalAnalysis'], 'schemaKey': 'Person', 'identifier': '0000-0003-2753-7150', 'affiliation': [{'name': 'Department of Computer Science, Stanford University, Stanford, CA, United States of America', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/03mtd9a03'}], 'includeInCitation': True}, {'name': 'Vyas, Saurabh', 'email': 'smvyas@stanford.edu', 'roleName': ['dcite:DataCurator', 'dcite:Author'], 'schemaKey': 'Person', 'affiliation': [{'name': 'Department of Bioengineering, Stanford University, Stanford, CA, United States of America', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/03mtd9a03'}], 'includeInCitation': True}, {'url': 'http://orcid.org/0000-0002-4607-7447', 'name': 'Ryu, Stephen', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-4607-7447', 'affiliation': [{'name': 'Department of Neurosurgery, Palo Alto Medical Foundation, Palo Alto, CA, United States of America', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/03mtd9a03'}], 'includeInCitation': True}, {'url': 'https://orcid.org/0000-0003-1534-9240', 'name': 'Shenoy, Krishna', 'email': 'shenoy@stanford.edu', 'roleName': ['dcite:Author', 'dcite:Conceptualization', 'dcite:DataCurator', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0003-1534-9240', 'affiliation': [{'name': 'Stanford University', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/03mtd9a03'}], 'includeInCitation': True}, {'url': 'https://www.simonsfoundation.org/', 'name': 'Simons Foundation', 'roleName': ['dcite:Funder', 'dcite:Sponsor'], 'schemaKey': 'Organization', 'awardNumber': 'https://www.simonsfoundation.org/collaborations/global-brain/data-sharing-initiatives/', 'contactPoint': [], 'includeInCitation': False}]
description: Extracellular physiology data of monkeys implanted with 96 channel Blackrock Utah arrays in the Motor cortex and Premotor cortex. Each file contains a sessions worth of data for one monkey (total 2) performing 1 of the four cursor movement task designs. The data contains hand, eye and cursor position data, LFP, sorted spikes and other task related trialized data.
assetsSummary: {'species': [{'name': 'Rhesus monkey', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9544'}], 'approach': [{'name': 'behavioral approach', 'schemaKey': 'ApproachType'}, {'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 187534957634, 'numberOfFiles': 15, 'numberOfSubjects': 2, 'variableMeasured': ['Units', 'LFP', 'Position'], 'measurementTechnique': [{'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'signal filtering technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000121 has 12 NWB files.
3 of these NWB files are of type 1.
1 of these NWB files are of type 2.
1 of these NWB files are of type 3.
6 of these NWB files are of type 4.
1 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2021-08-04T04:05:04.737853-04:00']
  Group /general/devices/Utah Array(M1) (Device) 96 channel utah array
  Group /general/devices/Utah Array(PMd) (Device) 96 channel utah array
  experiment_description: center out task for Monkeys
  experimenter: ['Nir Even-Chen' 'Blue Scheffer']
  Group /general/extracellular_ephys/1 (ElectrodeGroup) array corresponding to device implanted at M1
  Group /general/extracellular_ephys/1/device (Device) 96 channel utah array
  Group /general/extracellular_ephys/2 (ElectrodeGroup) array corresponding to device implanted at PMd
  Group /general/extracellular_ephys/2/device (Device) 96 channel utah array
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (192,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/gain (VectorData) gain | shape = (192,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (192,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (192,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (192,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (192,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (192,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/offset (VectorData) offset | shape = (192,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (192,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (192,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (192,) | dtype = float64
  institution: Stanford University
  related_publications: ['10.1371/journal.pcbi.1006808']
  Group /general/subject (Subject) 
  identifier: 14a9706a-617d-482c-bcbe-e0105356eebb
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/barrier_points (VectorData) barrier points location | shape = (20556,) | dtype = float64
  Dataset /intervals/trials/barrier_points_index (VectorIndex) Index for VectorData 'barrier_points' | shape = (3426,) | dtype = uint16
  Dataset /intervals/trials/fail_time (VectorData) time limit to target reach failure | shape = (3426,) | dtype = float64
  Dataset /intervals/trials/go_cue_time (VectorData) time when the go cue was given | shape = (3426,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (3426,) | dtype = int64
  Dataset /intervals/trials/is_successful (VectorData) if monkey started before the mandatory delay period after target shown | shape = (3426,) | dtype = uint8
  Dataset /intervals/trials/reach_time (VectorData) max time to reach the target | shape = (3426,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (3426,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (3426,) | dtype = float64
  Dataset /intervals/trials/target_acquire_time (VectorData) time when target was acquired by monkey | shape = (3806,) | dtype = float64
  Dataset /intervals/trials/target_acquire_time_index (VectorIndex) Index for VectorData 'target_acquire_time' | shape = (3426,) | dtype = uint16
  Dataset /intervals/trials/target_held_time (VectorData) time until which target was held by monkey | shape = (3426,) | dtype = float64
  Dataset /intervals/trials/target_hold_time (VectorData) min time required to have successfully acquired the target | shape = (3426,) | dtype = float64
  Dataset /intervals/trials/target_pos (VectorData) position of target on screen | shape = (10278,) | dtype = float64
  Dataset /intervals/trials/target_pos_index (VectorIndex) Index for VectorData 'target_pos' | shape = (3426,) | dtype = uint16
  Dataset /intervals/trials/target_shown_time (VectorData) time when target was shown but before the go cue was given | shape = (3426,) | dtype = float64
  Dataset /intervals/trials/target_size (VectorData) target size | shape = (10278,) | dtype = float64
  Dataset /intervals/trials/target_size_index (VectorIndex) Index for VectorData 'target_size' | shape = (3426,) | dtype = uint16
  Dataset /intervals/trials/task_id (VectorData) which target configuration | shape = (3426,) | dtype = float64
  Dataset /intervals/trials/timeseries (VectorData) index into a TimeSeries object | shape = (13704,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/trials/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (3426,) | dtype = uint16
  Dataset /intervals/trials/version_id (VectorData) which target version | shape = (3426,) | dtype = float64
  Group /processing/behavior (ProcessingModule) contains monkey movement data
  Group /processing/behavior/Position (Position) 
  Group /processing/behavior/Position/Cursor (SpatialSeries) cursor pos on screen in x,y
  Group /processing/behavior/Position/DecodePos (SpatialSeries) decoded pos in x,y
  Group /processing/behavior/Position/Eye (SpatialSeries) pos of eye in x,y
  Group /processing/behavior/Position/Hand (SpatialSeries) hand pos in x,y,z
  Group /processing/ecephys (ProcessingModule) Intermediate data from extracellular electrophysiology recordings, e.g., LFP.
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/M1_1 (ElectricalSeries) LFP signal for array M1_1, segment 1data for both arrays A,B in the same segment should be, but is not of the same time lengthand cannot be synced due to lack of time stamps. Ignore the starting times.
  Dataset /processing/ecephys/LFP/M1_1/electrodes (DynamicTableRegion) electrode_table_region | shape = (96,) | dtype = int64
  Group /processing/ecephys/LFP/M1_2 (ElectricalSeries) LFP signal for array M1_2, segment 2data for both arrays A,B in the same segment should be, but is not of the same time lengthand cannot be synced due to lack of time stamps. Ignore the starting times.
  Dataset /processing/ecephys/LFP/M1_2/electrodes (DynamicTableRegion) electrode_table_region | shape = (96,) | dtype = int64
  Group /processing/ecephys/LFP/PMd_1 (ElectricalSeries) LFP signal for array PMd_1, segment 1data for both arrays A,B in the same segment should be, but is not of the same time lengthand cannot be synced due to lack of time stamps. Ignore the starting times.
  Dataset /processing/ecephys/LFP/PMd_1/electrodes (DynamicTableRegion) electrode_table_region | shape = (96,) | dtype = int64
  Group /processing/ecephys/LFP/PMd_2 (ElectricalSeries) LFP signal for array PMd_2, segment 2data for both arrays A,B in the same segment should be, but is not of the same time lengthand cannot be synced due to lack of time stamps. Ignore the starting times.
  Dataset /processing/ecephys/LFP/PMd_2/electrodes (DynamicTableRegion) electrode_table_region | shape = (96,) | dtype = int64
  Group /processing/ecephys/LFP/PMd_3 (ElectricalSeries) LFP signal for array PMd_3, segment 3data for both arrays A,B in the same segment should be, but is not of the same time lengthand cannot be synced due to lack of time stamps. Ignore the starting times.
  Dataset /processing/ecephys/LFP/PMd_3/electrodes (DynamicTableRegion) electrode_table_region | shape = (96,) | dtype = int64
  session_description: no description
  session_start_time: 2015-10-01T15:03:07.683995-04:00
  Group /stimulus/presentation/juice_reward (TimeSeries) 1 is when reward was presented
  timestamps_reference_time: 2015-10-01T15:03:07.683995-04:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (192,) | dtype = object
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (192,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex) Index for VectorData 'electrodes' | shape = (192,) | dtype = uint8
  Dataset /units/id (ElementIdentifiers)  | shape = (192,) | dtype = int64
  Dataset /units/obs_intervals (VectorData) the observation intervals for each unit | shape = (192, 2) | dtype = float64
  Dataset /units/obs_intervals_index (VectorIndex) Index for VectorData 'obs_intervals' | shape = (192,) | dtype = uint8
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (13599424,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (192,) | dtype = uint32


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2021-08-04T03:18:59.854867-04:00']
  Group /general/devices/Utah Array(M1) (Device) 96 channel utah array
  Group /general/devices/Utah Array(PMd) (Device) 96 channel utah array
  experiment_description: center out task for Monkeys
  experimenter: ['Nir Even-Chen' 'Blue Scheffer']
  Group /general/extracellular_ephys/1 (ElectrodeGroup) array corresponding to device implanted at M1
  Group /general/extracellular_ephys/1/device (Device) 96 channel utah array
  Group /general/extracellular_ephys/2 (ElectrodeGroup) array corresponding to device implanted at PMd
  Group /general/extracellular_ephys/2/device (Device) 96 channel utah array
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (192,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/gain (VectorData) gain | shape = (192,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (192,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (192,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (192,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (192,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (192,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/offset (VectorData) offset | shape = (192,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (192,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (192,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (192,) | dtype = float64
  institution: Stanford University
  related_publications: ['10.1371/journal.pcbi.1006808']
  Group /general/subject (Subject) 
  identifier: df55236e-c59d-4cd3-97bc-ea4495627236
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/barrier_points (VectorData) barrier points location | shape = (15924,) | dtype = float64
  Dataset /intervals/trials/barrier_points_index (VectorIndex) Index for VectorData 'barrier_points' | shape = (2654,) | dtype = uint16
  Dataset /intervals/trials/fail_time (VectorData) time limit to target reach failure | shape = (2654,) | dtype = float64
  Dataset /intervals/trials/go_cue_time (VectorData) time when the go cue was given | shape = (2654,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (2654,) | dtype = int64
  Dataset /intervals/trials/is_successful (VectorData) if monkey started before the mandatory delay period after target shown | shape = (2654,) | dtype = uint8
  Dataset /intervals/trials/reach_time (VectorData) max time to reach the target | shape = (2654,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (2654,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (2654,) | dtype = float64
  Dataset /intervals/trials/target_acquire_time (VectorData) time when target was acquired by monkey | shape = (2795,) | dtype = float64
  Dataset /intervals/trials/target_acquire_time_index (VectorIndex) Index for VectorData 'target_acquire_time' | shape = (2654,) | dtype = uint16
  Dataset /intervals/trials/target_held_time (VectorData) time until which target was held by monkey | shape = (2654,) | dtype = float64
  Dataset /intervals/trials/target_hold_time (VectorData) min time required to have successfully acquired the target | shape = (2654,) | dtype = float64
  Dataset /intervals/trials/target_pos (VectorData) position of target on screen | shape = (7962,) | dtype = float64
  Dataset /intervals/trials/target_pos_index (VectorIndex) Index for VectorData 'target_pos' | shape = (2654,) | dtype = uint16
  Dataset /intervals/trials/target_shown_time (VectorData) time when target was shown but before the go cue was given | shape = (2654,) | dtype = float64
  Dataset /intervals/trials/target_size (VectorData) target size | shape = (7962,) | dtype = float64
  Dataset /intervals/trials/target_size_index (VectorIndex) Index for VectorData 'target_size' | shape = (2654,) | dtype = uint16
  Dataset /intervals/trials/task_id (VectorData) which target configuration | shape = (2654,) | dtype = float64
  Dataset /intervals/trials/timeseries (VectorData) index into a TimeSeries object | shape = (10616,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/trials/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (2654,) | dtype = uint16
  Dataset /intervals/trials/version_id (VectorData) which target version | shape = (2654,) | dtype = float64
  Group /processing/behavior (ProcessingModule) contains monkey movement data
  Group /processing/behavior/Position (Position) 
  Group /processing/behavior/Position/Cursor (SpatialSeries) cursor pos on screen in x,y
  Group /processing/behavior/Position/DecodePos (SpatialSeries) decoded pos in x,y
  Group /processing/behavior/Position/Eye (SpatialSeries) pos of eye in x,y
  Group /processing/behavior/Position/Hand (SpatialSeries) hand pos in x,y,z
  Group /processing/ecephys (ProcessingModule) Intermediate data from extracellular electrophysiology recordings, e.g., LFP.
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/M1_1 (ElectricalSeries) LFP signal for array M1_1, segment 1data for both arrays A,B in the same segment should be, but is not of the same time lengthand cannot be synced due to lack of time stamps. Ignore the starting times.
  Dataset /processing/ecephys/LFP/M1_1/electrodes (DynamicTableRegion) electrode_table_region | shape = (96,) | dtype = int64
  Group /processing/ecephys/LFP/M1_2 (ElectricalSeries) LFP signal for array M1_2, segment 2data for both arrays A,B in the same segment should be, but is not of the same time lengthand cannot be synced due to lack of time stamps. Ignore the starting times.
  Dataset /processing/ecephys/LFP/M1_2/electrodes (DynamicTableRegion) electrode_table_region | shape = (96,) | dtype = int64
  Group /processing/ecephys/LFP/PMd_1 (ElectricalSeries) LFP signal for array PMd_1, segment 1data for both arrays A,B in the same segment should be, but is not of the same time lengthand cannot be synced due to lack of time stamps. Ignore the starting times.
  Dataset /processing/ecephys/LFP/PMd_1/electrodes (DynamicTableRegion) electrode_table_region | shape = (96,) | dtype = int64
  Group /processing/ecephys/LFP/PMd_2 (ElectricalSeries) LFP signal for array PMd_2, segment 2data for both arrays A,B in the same segment should be, but is not of the same time lengthand cannot be synced due to lack of time stamps. Ignore the starting times.
  Dataset /processing/ecephys/LFP/PMd_2/electrodes (DynamicTableRegion) electrode_table_region | shape = (96,) | dtype = int64
  session_description: no description
  session_start_time: 2015-10-15T15:14:24.578996-04:00
  Group /stimulus/presentation/juice_reward (TimeSeries) 1 is when reward was presented
  timestamps_reference_time: 2015-10-15T15:14:24.578996-04:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (192,) | dtype = object
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (192,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex) Index for VectorData 'electrodes' | shape = (192,) | dtype = uint8
  Dataset /units/id (ElementIdentifiers)  | shape = (192,) | dtype = int64
  Dataset /units/obs_intervals (VectorData) the observation intervals for each unit | shape = (192, 2) | dtype = float64
  Dataset /units/obs_intervals_index (VectorIndex) Index for VectorData 'obs_intervals' | shape = (192,) | dtype = uint8
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (10179478,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (192,) | dtype = uint32


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2021-08-04T03:23:28.478727-04:00']
  Group /general/devices/Utah Array(M1) (Device) 96 channel utah array
  Group /general/devices/Utah Array(PMd) (Device) 96 channel utah array
  experiment_description: center out task for Monkeys
  experimenter: ['Nir Even-Chen' 'Blue Scheffer']
  Group /general/extracellular_ephys/1 (ElectrodeGroup) array corresponding to device implanted at M1
  Group /general/extracellular_ephys/1/device (Device) 96 channel utah array
  Group /general/extracellular_ephys/2 (ElectrodeGroup) array corresponding to device implanted at PMd
  Group /general/extracellular_ephys/2/device (Device) 96 channel utah array
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (192,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/gain (VectorData) gain | shape = (192,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (192,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (192,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (192,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (192,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (192,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/offset (VectorData) offset | shape = (192,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (192,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (192,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (192,) | dtype = float64
  institution: Stanford University
  related_publications: ['10.1371/journal.pcbi.1006808']
  Group /general/subject (Subject) 
  identifier: 28d10649-f935-4ada-9a1d-0e38375fac60
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/barrier_points (VectorData) barrier points location | shape = (42120,) | dtype = float64
  Dataset /intervals/trials/barrier_points_index (VectorIndex) Index for VectorData 'barrier_points' | shape = (7020,) | dtype = uint16
  Dataset /intervals/trials/fail_time (VectorData) time limit to target reach failure | shape = (7020,) | dtype = float64
  Dataset /intervals/trials/go_cue_time (VectorData) time when the go cue was given | shape = (7020,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (7020,) | dtype = int64
  Dataset /intervals/trials/is_successful (VectorData) if monkey started before the mandatory delay period after target shown | shape = (7020,) | dtype = uint8
  Dataset /intervals/trials/reach_time (VectorData) max time to reach the target | shape = (7020,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (7020,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (7020,) | dtype = float64
  Dataset /intervals/trials/target_acquire_time (VectorData) time when target was acquired by monkey | shape = (7864,) | dtype = float64
  Dataset /intervals/trials/target_acquire_time_index (VectorIndex) Index for VectorData 'target_acquire_time' | shape = (7020,) | dtype = uint16
  Dataset /intervals/trials/target_held_time (VectorData) time until which target was held by monkey | shape = (7020,) | dtype = float64
  Dataset /intervals/trials/target_hold_time (VectorData) min time required to have successfully acquired the target | shape = (7020,) | dtype = float64
  Dataset /intervals/trials/target_pos (VectorData) position of target on screen | shape = (21060,) | dtype = float64
  Dataset /intervals/trials/target_pos_index (VectorIndex) Index for VectorData 'target_pos' | shape = (7020,) | dtype = uint16
  Dataset /intervals/trials/target_shown_time (VectorData) time when target was shown but before the go cue was given | shape = (7020,) | dtype = float64
  Dataset /intervals/trials/target_size (VectorData) target size | shape = (21060,) | dtype = float64
  Dataset /intervals/trials/target_size_index (VectorIndex) Index for VectorData 'target_size' | shape = (7020,) | dtype = uint16
  Dataset /intervals/trials/task_id (VectorData) which target configuration | shape = (7020,) | dtype = float64
  Dataset /intervals/trials/timeseries (VectorData) index into a TimeSeries object | shape = (28080,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/trials/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (7020,) | dtype = uint16
  Dataset /intervals/trials/version_id (VectorData) which target version | shape = (7020,) | dtype = float64
  Group /processing/behavior (ProcessingModule) contains monkey movement data
  Group /processing/behavior/Position (Position) 
  Group /processing/behavior/Position/Cursor (SpatialSeries) cursor pos on screen in x,y
  Group /processing/behavior/Position/DecodePos (SpatialSeries) decoded pos in x,y
  Group /processing/behavior/Position/Eye (SpatialSeries) pos of eye in x,y
  Group /processing/behavior/Position/Hand (SpatialSeries) hand pos in x,y,z
  Group /processing/ecephys (ProcessingModule) Intermediate data from extracellular electrophysiology recordings, e.g., LFP.
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/M1_1 (ElectricalSeries) LFP signal for array M1_1, segment 1data for both arrays A,B in the same segment should be, but is not of the same time lengthand cannot be synced due to lack of time stamps. Ignore the starting times.
  Dataset /processing/ecephys/LFP/M1_1/electrodes (DynamicTableRegion) electrode_table_region | shape = (96,) | dtype = int64
  Group /processing/ecephys/LFP/M1_2 (ElectricalSeries) LFP signal for array M1_2, segment 2data for both arrays A,B in the same segment should be, but is not of the same time lengthand cannot be synced due to lack of time stamps. Ignore the starting times.
  Dataset /processing/ecephys/LFP/M1_2/electrodes (DynamicTableRegion) electrode_table_region | shape = (96,) | dtype = int64
  Group /processing/ecephys/LFP/M1_3 (ElectricalSeries) LFP signal for array M1_3, segment 3data for both arrays A,B in the same segment should be, but is not of the same time lengthand cannot be synced due to lack of time stamps. Ignore the starting times.
  Dataset /processing/ecephys/LFP/M1_3/electrodes (DynamicTableRegion) electrode_table_region | shape = (96,) | dtype = int64
  Group /processing/ecephys/LFP/PMd_1 (ElectricalSeries) LFP signal for array PMd_1, segment 1data for both arrays A,B in the same segment should be, but is not of the same time lengthand cannot be synced due to lack of time stamps. Ignore the starting times.
  Dataset /processing/ecephys/LFP/PMd_1/electrodes (DynamicTableRegion) electrode_table_region | shape = (96,) | dtype = int64
  Group /processing/ecephys/LFP/PMd_2 (ElectricalSeries) LFP signal for array PMd_2, segment 2data for both arrays A,B in the same segment should be, but is not of the same time lengthand cannot be synced due to lack of time stamps. Ignore the starting times.
  Dataset /processing/ecephys/LFP/PMd_2/electrodes (DynamicTableRegion) electrode_table_region | shape = (96,) | dtype = int64
  Group /processing/ecephys/LFP/PMd_3 (ElectricalSeries) LFP signal for array PMd_3, segment 3data for both arrays A,B in the same segment should be, but is not of the same time lengthand cannot be synced due to lack of time stamps. Ignore the starting times.
  Dataset /processing/ecephys/LFP/PMd_3/electrodes (DynamicTableRegion) electrode_table_region | shape = (96,) | dtype = int64
  Group /processing/ecephys/LFP/PMd_4 (ElectricalSeries) LFP signal for array PMd_4, segment 4data for both arrays A,B in the same segment should be, but is not of the same time lengthand cannot be synced due to lack of time stamps. Ignore the starting times.
  Dataset /processing/ecephys/LFP/PMd_4/electrodes (DynamicTableRegion) electrode_table_region | shape = (96,) | dtype = int64
  session_description: no description
  session_start_time: 2016-01-28T16:07:49.965995-05:00
  Group /stimulus/presentation/juice_reward (TimeSeries) 1 is when reward was presented
  timestamps_reference_time: 2016-01-28T16:07:49.965995-05:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (192,) | dtype = object
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (192,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex) Index for VectorData 'electrodes' | shape = (192,) | dtype = uint8
  Dataset /units/id (ElementIdentifiers)  | shape = (192,) | dtype = int64
  Dataset /units/obs_intervals (VectorData) the observation intervals for each unit | shape = (192, 2) | dtype = float64
  Dataset /units/obs_intervals_index (VectorIndex) Index for VectorData 'obs_intervals' | shape = (192,) | dtype = uint8
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (26284827,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (192,) | dtype = uint32


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2021-07-30T02:06:33.901167-04:00']
  Group /general/devices/Utah Array(M1) (Device) 96 channel utah array
  Group /general/devices/Utah Array(PMd) (Device) 96 channel utah array
  experiment_description: center out task for Monkeys
  experimenter: ['Blue Scheffer' 'Nir Even-Chen']
  Group /general/extracellular_ephys/1 (ElectrodeGroup) array corresponding to device implanted at M1
  Group /general/extracellular_ephys/1/device (Device) 96 channel utah array
  Group /general/extracellular_ephys/2 (ElectrodeGroup) array corresponding to device implanted at PMd
  Group /general/extracellular_ephys/2/device (Device) 96 channel utah array
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (192,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/gain (VectorData) gain | shape = (192,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (192,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (192,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (192,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (192,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (192,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/offset (VectorData) offset | shape = (192,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (192,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (192,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (192,) | dtype = float64
  institution: Stanford University
  related_publications: ['10.1371/journal.pcbi.1006808']
  Group /general/subject (Subject) 
  identifier: 5625b799-5a44-4cd1-a329-efe90833780e
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/barrier_points (VectorData) barrier points location | shape = (31998,) | dtype = float64
  Dataset /intervals/trials/barrier_points_index (VectorIndex) Index for VectorData 'barrier_points' | shape = (5333,) | dtype = uint16
  Dataset /intervals/trials/fail_time (VectorData) time limit to target reach failure | shape = (5333,) | dtype = float64
  Dataset /intervals/trials/go_cue_time (VectorData) time when the go cue was given | shape = (5333,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (5333,) | dtype = int64
  Dataset /intervals/trials/is_successful (VectorData) if monkey started before the mandatory delay period after target shown | shape = (5333,) | dtype = uint8
  Dataset /intervals/trials/reach_time (VectorData) max time to reach the target | shape = (5333,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (5333,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (5333,) | dtype = float64
  Dataset /intervals/trials/target_acquire_time (VectorData) time when target was acquired by monkey | shape = (6282,) | dtype = float64
  Dataset /intervals/trials/target_acquire_time_index (VectorIndex) Index for VectorData 'target_acquire_time' | shape = (5333,) | dtype = uint16
  Dataset /intervals/trials/target_held_time (VectorData) time until which target was held by monkey | shape = (5333,) | dtype = float64
  Dataset /intervals/trials/target_hold_time (VectorData) min time required to have successfully acquired the target | shape = (5333,) | dtype = float64
  Dataset /intervals/trials/target_pos (VectorData) position of target on screen | shape = (15999,) | dtype = float64
  Dataset /intervals/trials/target_pos_index (VectorIndex) Index for VectorData 'target_pos' | shape = (5333,) | dtype = uint16
  Dataset /intervals/trials/target_shown_time (VectorData) time when target was shown but before the go cue was given | shape = (5333,) | dtype = float64
  Dataset /intervals/trials/target_size (VectorData) target size | shape = (15999,) | dtype = float64
  Dataset /intervals/trials/target_size_index (VectorIndex) Index for VectorData 'target_size' | shape = (5333,) | dtype = uint16
  Dataset /intervals/trials/task_id (VectorData) which target configuration | shape = (5333,) | dtype = float64
  Dataset /intervals/trials/timeseries (VectorData) index into a TimeSeries object | shape = (21332,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/trials/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (5333,) | dtype = uint16
  Dataset /intervals/trials/version_id (VectorData) which target version | shape = (5333,) | dtype = float64
  Group /processing/behavior (ProcessingModule) contains monkey movement data
  Group /processing/behavior/Position (Position) 
  Group /processing/behavior/Position/Cursor (SpatialSeries) cursor pos on screen in x,y
  Group /processing/behavior/Position/DecodePos (SpatialSeries) decoded pos in x,y
  Group /processing/behavior/Position/Eye (SpatialSeries) pos of eye in x,y
  Group /processing/behavior/Position/Hand (SpatialSeries) hand pos in x,y,z
  Group /processing/ecephys (ProcessingModule) Intermediate data from extracellular electrophysiology recordings, e.g., LFP.
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/M1_1 (ElectricalSeries) LFP signal for array M1_1, segment 1data for both arrays A,B in the same segment should be, but is not of the same time lengthand cannot be synced due to lack of time stamps. Ignore the starting times.
  Dataset /processing/ecephys/LFP/M1_1/electrodes (DynamicTableRegion) electrode_table_region | shape = (96,) | dtype = int64
  Group /processing/ecephys/LFP/PMd_1 (ElectricalSeries) LFP signal for array PMd_1, segment 1data for both arrays A,B in the same segment should be, but is not of the same time lengthand cannot be synced due to lack of time stamps. Ignore the starting times.
  Dataset /processing/ecephys/LFP/PMd_1/electrodes (DynamicTableRegion) electrode_table_region | shape = (96,) | dtype = int64
  session_description: no description
  session_start_time: 2017-01-15T12:53:33.811003-05:00
  Group /stimulus/presentation/juice_reward (TimeSeries) 1 is when reward was presented
  timestamps_reference_time: 2017-01-15T12:53:33.811003-05:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (192,) | dtype = object
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (192,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex) Index for VectorData 'electrodes' | shape = (192,) | dtype = uint8
  Dataset /units/id (ElementIdentifiers)  | shape = (192,) | dtype = int64
  Dataset /units/obs_intervals (VectorData) the observation intervals for each unit | shape = (192, 2) | dtype = float64
  Dataset /units/obs_intervals_index (VectorIndex) Index for VectorData 'obs_intervals' | shape = (192,) | dtype = uint8
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (15989234,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (192,) | dtype = uint32


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2021-08-02T03:47:31.488379-04:00']
  Group /general/devices/Utah Array(M1) (Device) 96 channel utah array
  Group /general/devices/Utah Array(PMd) (Device) 96 channel utah array
  experiment_description: center out task for Monkeys
  experimenter: ['Blue Scheffer' 'Nir Even-Chen']
  Group /general/extracellular_ephys/1 (ElectrodeGroup) array corresponding to device implanted at M1
  Group /general/extracellular_ephys/1/device (Device) 96 channel utah array
  Group /general/extracellular_ephys/2 (ElectrodeGroup) array corresponding to device implanted at PMd
  Group /general/extracellular_ephys/2/device (Device) 96 channel utah array
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (192,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/gain (VectorData) gain | shape = (192,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (192,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (192,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (192,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (192,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (192,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/offset (VectorData) offset | shape = (192,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (192,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (192,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (192,) | dtype = float64
  institution: Stanford University
  related_publications: ['10.1371/journal.pcbi.1006808']
  Group /general/subject (Subject) 
  identifier: 06f1c03a-c6aa-45a4-86e8-1a71175af294
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/barrier_points (VectorData) barrier points location | shape = (32388,) | dtype = float64
  Dataset /intervals/trials/barrier_points_index (VectorIndex) Index for VectorData 'barrier_points' | shape = (5398,) | dtype = uint16
  Dataset /intervals/trials/fail_time (VectorData) time limit to target reach failure | shape = (5398,) | dtype = float64
  Dataset /intervals/trials/go_cue_time (VectorData) time when the go cue was given | shape = (5398,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (5398,) | dtype = int64
  Dataset /intervals/trials/is_successful (VectorData) if monkey started before the mandatory delay period after target shown | shape = (5398,) | dtype = uint8
  Dataset /intervals/trials/reach_time (VectorData) max time to reach the target | shape = (5398,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (5398,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (5398,) | dtype = float64
  Dataset /intervals/trials/target_acquire_time (VectorData) time when target was acquired by monkey | shape = (6322,) | dtype = float64
  Dataset /intervals/trials/target_acquire_time_index (VectorIndex) Index for VectorData 'target_acquire_time' | shape = (5398,) | dtype = uint16
  Dataset /intervals/trials/target_held_time (VectorData) time until which target was held by monkey | shape = (5398,) | dtype = float64
  Dataset /intervals/trials/target_hold_time (VectorData) min time required to have successfully acquired the target | shape = (5398,) | dtype = float64
  Dataset /intervals/trials/target_pos (VectorData) position of target on screen | shape = (16194,) | dtype = float64
  Dataset /intervals/trials/target_pos_index (VectorIndex) Index for VectorData 'target_pos' | shape = (5398,) | dtype = uint16
  Dataset /intervals/trials/target_shown_time (VectorData) time when target was shown but before the go cue was given | shape = (5398,) | dtype = float64
  Dataset /intervals/trials/target_size (VectorData) target size | shape = (16194,) | dtype = float64
  Dataset /intervals/trials/target_size_index (VectorIndex) Index for VectorData 'target_size' | shape = (5398,) | dtype = uint16
  Dataset /intervals/trials/task_id (VectorData) which target configuration | shape = (5398,) | dtype = float64
  Dataset /intervals/trials/timeseries (VectorData) index into a TimeSeries object | shape = (21592,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/trials/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (5398,) | dtype = uint16
  Dataset /intervals/trials/version_id (VectorData) which target version | shape = (5398,) | dtype = float64
  Group /processing/behavior (ProcessingModule) contains monkey movement data
  Group /processing/behavior/Position (Position) 
  Group /processing/behavior/Position/Cursor (SpatialSeries) cursor pos on screen in x,y
  Group /processing/behavior/Position/DecodePos (SpatialSeries) decoded pos in x,y
  Group /processing/behavior/Position/Eye (SpatialSeries) pos of eye in x,y
  Group /processing/behavior/Position/Hand (SpatialSeries) hand pos in x,y,z
  Group /processing/ecephys (ProcessingModule) Intermediate data from extracellular electrophysiology recordings, e.g., LFP.
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/M1_3 (ElectricalSeries) LFP signal for array M1_3, segment 3data for both arrays A,B in the same segment should be, but is not of the same time lengthand cannot be synced due to lack of time stamps. Ignore the starting times.
  Dataset /processing/ecephys/LFP/M1_3/electrodes (DynamicTableRegion) electrode_table_region | shape = (96,) | dtype = int64
  Group /processing/ecephys/LFP/PMd_3 (ElectricalSeries) LFP signal for array PMd_3, segment 3data for both arrays A,B in the same segment should be, but is not of the same time lengthand cannot be synced due to lack of time stamps. Ignore the starting times.
  Dataset /processing/ecephys/LFP/PMd_3/electrodes (DynamicTableRegion) electrode_table_region | shape = (96,) | dtype = int64
  session_description: no description
  session_start_time: 2017-01-17T10:46:43.492998-05:00
  Group /stimulus/presentation/juice_reward (TimeSeries) 1 is when reward was presented
  timestamps_reference_time: 2017-01-17T10:46:43.492998-05:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (192,) | dtype = object
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (192,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex) Index for VectorData 'electrodes' | shape = (192,) | dtype = uint8
  Dataset /units/id (ElementIdentifiers)  | shape = (192,) | dtype = int64
  Dataset /units/obs_intervals (VectorData) the observation intervals for each unit | shape = (192, 2) | dtype = float64
  Dataset /units/obs_intervals_index (VectorIndex) Index for VectorData 'obs_intervals' | shape = (192,) | dtype = uint8
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (10588960,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (192,) | dtype = uint32
