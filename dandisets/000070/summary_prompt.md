
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000070/draft
name: Neural population dynamics during reaching
contributor: [{'url': 'https://pubmed.ncbi.nlm.nih.gov/?cmd=search&term=Mark+M.+Churchland', 'name': 'Churchland, Mark', 'email': 'mc3502@columbia.edu', 'roleName': ['dcite:Author', 'dcite:DataCollector', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0001-9123-6526', 'affiliation': [{'name': 'Department of Electrical Engineering, Stanford University, Stanford, 94305, California, USA', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/00f54p054'}, {'name': 'Department of Neuroscience, Kavli Institute for Brain Science, David Mahoney Center, Columbia University Medical Center, New York, 10032, New York, USA', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/00hj8s172'}], 'includeInCitation': True}, {'url': 'https://pubmed.ncbi.nlm.nih.gov/?term=Cunningham+JP&cauthor_id=30877963', 'name': 'Cunningham, John P.', 'email': 'jpc2181@columbia.edu', 'roleName': ['dcite:Author', 'dcite:DataCollector'], 'schemaKey': 'Person', 'affiliation': [{'name': 'Department of Biomedical Engineering, Washington University in St Louis, St Louis, 63130, Missouri, USA', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/01yc7t268'}], 'includeInCitation': True}, {'url': 'https://pubmed.ncbi.nlm.nih.gov/?cmd=search&term=Matthew+T.+Kaufman', 'name': 'Kaufman, Matthew T.', 'email': 'mattkaufman@uchicago.edu', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-8072-023X', 'affiliation': [{'name': 'Department of Electrical Engineering, Stanford University, Stanford, 94305, California, USA', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/00f54p054'}], 'includeInCitation': True}, {'url': 'https://pubmed.ncbi.nlm.nih.gov/?cmd=search&term=Justin+D.+Foster', 'name': 'Foster, Justin D.', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [{'name': 'Department of Electrical Engineering, Stanford University, Stanford, 94305, California, USA', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/00f54p054'}], 'includeInCitation': True}, {'name': 'Nuyujukian, Paul', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [{'name': 'Department of Bioengineering, Stanford University, Stanford, 94705, California, USA', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/00f54p054'}], 'includeInCitation': True}, {'name': 'Ryu, Stephen I.', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [{'name': 'Department of Electrical Engineering, Stanford University, Stanford, 94305, California, USA', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/00f54p054'}], 'includeInCitation': True}, {'url': 'https://pubmed.ncbi.nlm.nih.gov/?cmd=search&term=Krishna+V.+Shenoy', 'name': 'Shenoy, Krishna V.', 'email': 'shenoy@stanford.edu', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0003-1534-9240', 'affiliation': [{'name': 'Department of Electrical Engineering, Stanford University, Stanford, 94305, California, USA', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/00f54p054'}], 'includeInCitation': True}, {'name': 'Sharda, Saksham', 'email': 'saksham20.sharda@gmail.com', 'roleName': ['dcite:Maintainer', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': False}, {'url': 'https://www.simonsfoundation.org/', 'name': 'Simons Foundation', 'roleName': ['dcite:Funder', 'dcite:Sponsor'], 'schemaKey': 'Organization', 'awardNumber': 'https://www.simonsfoundation.org/collaborations/global-brain/data-sharing-initiatives/', 'contactPoint': [], 'includeInCitation': False}]
description: Monkeys recordings of Motor Cortex (M1) and dorsal Premotor Cortex (PMd) using two 96 channel high density Utah Arrays (Blackrock Microsystems) while performing reaching tasks with right hand.
assetsSummary: {'species': [{'name': 'Rhesus monkey', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9544'}], 'approach': [{'name': 'behavioral approach', 'schemaKey': 'ApproachType'}, {'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 45909708322, 'numberOfFiles': 9, 'numberOfSubjects': 2, 'variableMeasured': ['Position', 'Units'], 'measurementTechnique': [{'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000070 has 9 NWB files.
4 of these NWB files are of type 1.
2 of these NWB files are of type 2.
1 of these NWB files are of type 3.
1 of these NWB files are of type 4.
1 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2021-08-11T02:59:54.008857-04:00']
  Group /general/devices/Utah Array(M1) (Device) 96 channel utah array
  Group /general/devices/Utah Array(PMd) (Device) 96 channel utah array
  experiment_description: 
  experimenter: ['Matthew T. Kaufman' 'Mark M. Churchland']
  Group /general/extracellular_ephys/1 (ElectrodeGroup) array corresponding to device implanted at PMd
  Group /general/extracellular_ephys/1/device (Device) 96 channel utah array
  Group /general/extracellular_ephys/2 (ElectrodeGroup) array corresponding to device implanted at M1
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
  related_publications: ['10.1038/nature11129 10.1152/jn.00892.2011 10.1038/nn.3643 10.1038/nn.4042 10.1146/annurev-neuro-062111-150509 10.7554/eLife.0467710.1523/ENEURO.0085-16.2016 10.1038/s41592-018-0109-9']
  Group /general/subject (Subject) 
  identifier: 94563eca-e111-4c9e-8cad-3f01345163f7
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/barrier_info (VectorData) (x,y,halfwidth,halfheight) | shape = (8313, 4) | dtype = float64
  Dataset /intervals/trials/barrier_info_index (VectorIndex) Index for VectorData 'barrier_info' | shape = (1588,) | dtype = uint16
  Dataset /intervals/trials/correct_reach (VectorData) tells you the result of our algorithm for determining whether this reach looked like the other reaches for this condition. To get it, we correlated the hand velocity for every pair of trials with that condition, accepted the reach with the most high correlations as prototypical, then marked as “consistent” only reaches that had a high enough correlation with the prototypical reach. | shape = (1588,) | dtype = uint8
  Dataset /intervals/trials/discard_trial (VectorData) flag that will usually be 0, but is set to 1 if there was a photo box problem (meaning RT can't be calculated accurately) or we had a hand tracking error during the movement. In general, throw those trials away. | shape = (1588,) | dtype = uint8
  Dataset /intervals/trials/frame_details (VectorData) (frameLeft,right,bottom,top, width) :tell where the frame (outer rectangle of barriers) were. For those, the values are inner edges | shape = (7940, 1, 1) | dtype = int16
  Dataset /intervals/trials/frame_details_index (VectorIndex) Index for VectorData 'frame_details' | shape = (1588,) | dtype = uint16
  Dataset /intervals/trials/go_cue_time (VectorData) time of go cue | shape = (1588,) | dtype = float64
  Dataset /intervals/trials/hit_target_position (VectorData) x,y position on screen of the target hit | shape = (1588, 2) | dtype = int16
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (1588,) | dtype = int64
  Dataset /intervals/trials/maze_condition (VectorData) The set of 27 (or 108) mazes included was composed of 3 (or 12) “subsets”. Each subset contained 3 related mazes. Each maze had 3 “versions”: the 3-target with barrier, the 1-target with barriers, and the 1-target with no barriers. These 3 versions shared the same target positions. The 3-target and 1-target versions also shared the same barrier positions. In the 3-target version, exactly one target was accessible  | shape = (1588,) | dtype = uint8
  Dataset /intervals/trials/maze_num_barriers (VectorData) number of barriers presented | shape = (1588,) | dtype = uint8
  Dataset /intervals/trials/maze_num_targets (VectorData) number of targets presented | shape = (1588,) | dtype = uint8
  Dataset /intervals/trials/move_begins_time (VectorData) movement onset time | shape = (1588,) | dtype = float64
  Dataset /intervals/trials/move_ends_time (VectorData) movement stop time | shape = (1588,) | dtype = float64
  Dataset /intervals/trials/novel_maze (VectorData) novel maze | shape = (1588,) | dtype = uint8
  Dataset /intervals/trials/proto_trial (VectorData) whether that trial was used as the prototype trial for figuring out which trials were consistent | shape = (1588,) | dtype = uint8
  Dataset /intervals/trials/reaction_time (VectorData) reaction time | shape = (1588,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (1588,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1588,) | dtype = float64
  Dataset /intervals/trials/target_positions (VectorData) x,y position on screen of all targets presented | shape = (2790, 2) | dtype = uint8
  Dataset /intervals/trials/target_positions_index (VectorIndex) Index for VectorData 'target_positions' | shape = (1588,) | dtype = uint16
  Dataset /intervals/trials/target_presentation_time (VectorData) time of target presentation | shape = (1588,) | dtype = float64
  Dataset /intervals/trials/target_size (VectorData) half width of the targets | shape = (1588,) | dtype = uint8
  Dataset /intervals/trials/task_success (VectorData) indicates whether the monkey was successful on this trial | shape = (1588,) | dtype = uint8
  Dataset /intervals/trials/timeseries (VectorData) index into a TimeSeries object | shape = (4764,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/trials/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (1588,) | dtype = uint16
  Dataset /intervals/trials/trial_type (VectorData) trial type | shape = (1588,) | dtype = uint8
  Dataset /intervals/trials/trial_version (VectorData) should be 0 for a truly random maze (two random barriers). For a degenerate maze (real maze with some barriers randomly removed) trialVersion is >10 | shape = (1588,) | dtype = uint8
  Group /processing/behavior (ProcessingModule) contains monkey movement data
  Group /processing/behavior/Position (Position) 
  Group /processing/behavior/Position/Cursor (SpatialSeries) no description
  Group /processing/behavior/Position/Eye (SpatialSeries) no description
  Group /processing/behavior/Position/Hand (SpatialSeries) no description
  Group /processing/ecephys (ProcessingModule) Intermediate data from extracellular electrophysiology recordings, e.g., LFP.
  Group /processing/ecephys/Processed (FilteredEphys) 
  Group /processing/ecephys/Processed/A001 (ElectricalSeries) LFP signal for array A, segment 1data for both arrays A,B in the same segment should be, but is not of the same time lengthand cannot be synced due to lack of time stamps. Ignore the starting times.
  Dataset /processing/ecephys/Processed/A001/electrodes (DynamicTableRegion) electrode_table_region | shape = (96,) | dtype = int64
  Group /processing/ecephys/Processed/A002 (ElectricalSeries) LFP signal for array A, segment 2data for both arrays A,B in the same segment should be, but is not of the same time lengthand cannot be synced due to lack of time stamps. Ignore the starting times.
  Dataset /processing/ecephys/Processed/A002/electrodes (DynamicTableRegion) electrode_table_region | shape = (96,) | dtype = int64
  Group /processing/ecephys/Processed/B001 (ElectricalSeries) LFP signal for array B, segment 1data for both arrays A,B in the same segment should be, but is not of the same time lengthand cannot be synced due to lack of time stamps. Ignore the starting times.
  Dataset /processing/ecephys/Processed/B001/electrodes (DynamicTableRegion) electrode_table_region | shape = (96,) | dtype = int64
  Group /processing/ecephys/Processed/B002 (ElectricalSeries) LFP signal for array B, segment 2data for both arrays A,B in the same segment should be, but is not of the same time lengthand cannot be synced due to lack of time stamps. Ignore the starting times.
  Dataset /processing/ecephys/Processed/B002/electrodes (DynamicTableRegion) electrode_table_region | shape = (96,) | dtype = int64
  session_description: 
  session_start_time: 2009-09-12T00:00:00-07:00
  timestamps_reference_time: 2009-09-12T00:00:00-07:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (192,) | dtype = object
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (192,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex) Index for VectorData 'electrodes' | shape = (192,) | dtype = uint8
  Dataset /units/id (ElementIdentifiers)  | shape = (192,) | dtype = int64
  Dataset /units/obs_intervals (VectorData) the observation intervals for each unit | shape = (304896, 2) | dtype = float64
  Dataset /units/obs_intervals_index (VectorIndex) Index for VectorData 'obs_intervals' | shape = (192,) | dtype = uint32
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (44869604,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (192,) | dtype = uint32


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2021-08-11T03:21:05.275820-04:00']
  Group /general/devices/Utah Array(M1) (Device) 96 channel utah array
  Group /general/devices/Utah Array(PMd) (Device) 96 channel utah array
  experiment_description: 
  experimenter: ['Matthew T. Kaufman' 'Mark M. Churchland']
  Group /general/extracellular_ephys/1 (ElectrodeGroup) array corresponding to device implanted at PMd
  Group /general/extracellular_ephys/1/device (Device) 96 channel utah array
  Group /general/extracellular_ephys/2 (ElectrodeGroup) array corresponding to device implanted at M1
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
  related_publications: ['10.1038/nature11129 10.1152/jn.00892.2011 10.1038/nn.3643 10.1038/nn.4042 10.1146/annurev-neuro-062111-150509 10.7554/eLife.0467710.1523/ENEURO.0085-16.2016 10.1038/s41592-018-0109-9']
  Group /general/subject (Subject) 
  identifier: 0e900362-7a87-4b21-9756-2dc69f287c7d
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/barrier_info (VectorData) (x,y,halfwidth,halfheight) | shape = (18503, 4) | dtype = float64
  Dataset /intervals/trials/barrier_info_index (VectorIndex) Index for VectorData 'barrier_info' | shape = (3038,) | dtype = uint16
  Dataset /intervals/trials/correct_reach (VectorData) tells you the result of our algorithm for determining whether this reach looked like the other reaches for this condition. To get it, we correlated the hand velocity for every pair of trials with that condition, accepted the reach with the most high correlations as prototypical, then marked as “consistent” only reaches that had a high enough correlation with the prototypical reach. | shape = (3038,) | dtype = uint8
  Dataset /intervals/trials/discard_trial (VectorData) flag that will usually be 0, but is set to 1 if there was a photo box problem (meaning RT can't be calculated accurately) or we had a hand tracking error during the movement. In general, throw those trials away. | shape = (3038,) | dtype = uint8
  Dataset /intervals/trials/frame_details (VectorData) (frameLeft,right,bottom,top, width) :tell where the frame (outer rectangle of barriers) were. For those, the values are inner edges | shape = (15190, 1, 1) | dtype = int16
  Dataset /intervals/trials/frame_details_index (VectorIndex) Index for VectorData 'frame_details' | shape = (3038,) | dtype = uint16
  Dataset /intervals/trials/go_cue_time (VectorData) time of go cue | shape = (3038,) | dtype = float64
  Dataset /intervals/trials/hit_target_position (VectorData) x,y position on screen of the target hit | shape = (3038, 2) | dtype = int16
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (3038,) | dtype = int64
  Dataset /intervals/trials/maze_condition (VectorData) The set of 27 (or 108) mazes included was composed of 3 (or 12) “subsets”. Each subset contained 3 related mazes. Each maze had 3 “versions”: the 3-target with barrier, the 1-target with barriers, and the 1-target with no barriers. These 3 versions shared the same target positions. The 3-target and 1-target versions also shared the same barrier positions. In the 3-target version, exactly one target was accessible  | shape = (3038,) | dtype = uint8
  Dataset /intervals/trials/maze_num_barriers (VectorData) number of barriers presented | shape = (3038,) | dtype = uint8
  Dataset /intervals/trials/maze_num_targets (VectorData) number of targets presented | shape = (3038,) | dtype = uint8
  Dataset /intervals/trials/move_begins_time (VectorData) movement onset time | shape = (3038,) | dtype = float64
  Dataset /intervals/trials/move_ends_time (VectorData) movement stop time | shape = (3038,) | dtype = float64
  Dataset /intervals/trials/novel_maze (VectorData) novel maze | shape = (3038,) | dtype = uint8
  Dataset /intervals/trials/proto_trial (VectorData) whether that trial was used as the prototype trial for figuring out which trials were consistent | shape = (3038,) | dtype = uint8
  Dataset /intervals/trials/reaction_time (VectorData) reaction time | shape = (3038,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (3038,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (3038,) | dtype = float64
  Dataset /intervals/trials/target_positions (VectorData) x,y position on screen of all targets presented | shape = (5326, 2) | dtype = uint8
  Dataset /intervals/trials/target_positions_index (VectorIndex) Index for VectorData 'target_positions' | shape = (3038,) | dtype = uint16
  Dataset /intervals/trials/target_presentation_time (VectorData) time of target presentation | shape = (3038,) | dtype = float64
  Dataset /intervals/trials/target_size (VectorData) half width of the targets | shape = (3038,) | dtype = uint8
  Dataset /intervals/trials/task_success (VectorData) indicates whether the monkey was successful on this trial | shape = (3038,) | dtype = uint8
  Dataset /intervals/trials/timeseries (VectorData) index into a TimeSeries object | shape = (9114,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/trials/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (3038,) | dtype = uint16
  Dataset /intervals/trials/trial_type (VectorData) trial type | shape = (3038,) | dtype = uint8
  Dataset /intervals/trials/trial_version (VectorData) should be 0 for a truly random maze (two random barriers). For a degenerate maze (real maze with some barriers randomly removed) trialVersion is >10 | shape = (3038,) | dtype = uint8
  Group /processing/behavior (ProcessingModule) contains monkey movement data
  Group /processing/behavior/Position (Position) 
  Group /processing/behavior/Position/Cursor (SpatialSeries) no description
  Group /processing/behavior/Position/Eye (SpatialSeries) no description
  Group /processing/behavior/Position/Hand (SpatialSeries) no description
  Group /processing/ecephys (ProcessingModule) Intermediate data from extracellular electrophysiology recordings, e.g., LFP.
  Group /processing/ecephys/Processed (FilteredEphys) 
  Group /processing/ecephys/Processed/A001 (ElectricalSeries) LFP signal for array A, segment 1data for both arrays A,B in the same segment should be, but is not of the same time lengthand cannot be synced due to lack of time stamps. Ignore the starting times.
  Dataset /processing/ecephys/Processed/A001/electrodes (DynamicTableRegion) electrode_table_region | shape = (96,) | dtype = int64
  Group /processing/ecephys/Processed/A002 (ElectricalSeries) LFP signal for array A, segment 2data for both arrays A,B in the same segment should be, but is not of the same time lengthand cannot be synced due to lack of time stamps. Ignore the starting times.
  Dataset /processing/ecephys/Processed/A002/electrodes (DynamicTableRegion) electrode_table_region | shape = (96,) | dtype = int64
  Group /processing/ecephys/Processed/A003 (ElectricalSeries) LFP signal for array A, segment 3data for both arrays A,B in the same segment should be, but is not of the same time lengthand cannot be synced due to lack of time stamps. Ignore the starting times.
  Dataset /processing/ecephys/Processed/A003/electrodes (DynamicTableRegion) electrode_table_region | shape = (96,) | dtype = int64
  Group /processing/ecephys/Processed/B001 (ElectricalSeries) LFP signal for array B, segment 1data for both arrays A,B in the same segment should be, but is not of the same time lengthand cannot be synced due to lack of time stamps. Ignore the starting times.
  Dataset /processing/ecephys/Processed/B001/electrodes (DynamicTableRegion) electrode_table_region | shape = (96,) | dtype = int64
  Group /processing/ecephys/Processed/B002 (ElectricalSeries) LFP signal for array B, segment 2data for both arrays A,B in the same segment should be, but is not of the same time lengthand cannot be synced due to lack of time stamps. Ignore the starting times.
  Dataset /processing/ecephys/Processed/B002/electrodes (DynamicTableRegion) electrode_table_region | shape = (96,) | dtype = int64
  Group /processing/ecephys/Processed/B003 (ElectricalSeries) LFP signal for array B, segment 3data for both arrays A,B in the same segment should be, but is not of the same time lengthand cannot be synced due to lack of time stamps. Ignore the starting times.
  Dataset /processing/ecephys/Processed/B003/electrodes (DynamicTableRegion) electrode_table_region | shape = (96,) | dtype = int64
  session_description: 
  session_start_time: 2009-08-12T00:00:00-07:00
  timestamps_reference_time: 2009-08-12T00:00:00-07:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (192,) | dtype = object
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (192,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex) Index for VectorData 'electrodes' | shape = (192,) | dtype = uint8
  Dataset /units/id (ElementIdentifiers)  | shape = (192,) | dtype = int64
  Dataset /units/obs_intervals (VectorData) the observation intervals for each unit | shape = (583296, 2) | dtype = float64
  Dataset /units/obs_intervals_index (VectorIndex) Index for VectorData 'obs_intervals' | shape = (192,) | dtype = uint32
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (89773340,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (192,) | dtype = uint32


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2021-08-11T03:21:49.834892-04:00']
  Group /general/devices/Utah Array(M1) (Device) 96 channel utah array
  Group /general/devices/Utah Array(PMd) (Device) 96 channel utah array
  experiment_description: 
  experimenter: ['Matthew T. Kaufman' 'Mark M. Churchland']
  Group /general/extracellular_ephys/1 (ElectrodeGroup) array corresponding to device implanted at PMd
  Group /general/extracellular_ephys/1/device (Device) 96 channel utah array
  Group /general/extracellular_ephys/2 (ElectrodeGroup) array corresponding to device implanted at M1
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
  related_publications: ['10.1038/nature11129 10.1152/jn.00892.2011 10.1038/nn.3643 10.1038/nn.4042 10.1146/annurev-neuro-062111-150509 10.7554/eLife.0467710.1523/ENEURO.0085-16.2016 10.1038/s41592-018-0109-9']
  Group /general/subject (Subject) 
  identifier: 893a11c1-73d4-4e09-8e25-a5d6fb4b814a
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/barrier_info (VectorData) (x,y,halfwidth,halfheight) | shape = (17964, 4) | dtype = float64
  Dataset /intervals/trials/barrier_info_index (VectorIndex) Index for VectorData 'barrier_info' | shape = (2911,) | dtype = uint16
  Dataset /intervals/trials/correct_reach (VectorData) tells you the result of our algorithm for determining whether this reach looked like the other reaches for this condition. To get it, we correlated the hand velocity for every pair of trials with that condition, accepted the reach with the most high correlations as prototypical, then marked as “consistent” only reaches that had a high enough correlation with the prototypical reach. | shape = (2911,) | dtype = uint8
  Dataset /intervals/trials/discard_trial (VectorData) flag that will usually be 0, but is set to 1 if there was a photo box problem (meaning RT can't be calculated accurately) or we had a hand tracking error during the movement. In general, throw those trials away. | shape = (2911,) | dtype = uint8
  Dataset /intervals/trials/frame_details (VectorData) (frameLeft,right,bottom,top, width) :tell where the frame (outer rectangle of barriers) were. For those, the values are inner edges | shape = (14555, 1, 1) | dtype = int16
  Dataset /intervals/trials/frame_details_index (VectorIndex) Index for VectorData 'frame_details' | shape = (2911,) | dtype = uint16
  Dataset /intervals/trials/go_cue_time (VectorData) time of go cue | shape = (2911,) | dtype = float64
  Dataset /intervals/trials/hit_target_position (VectorData) x,y position on screen of the target hit | shape = (2911, 2) | dtype = int16
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (2911,) | dtype = int64
  Dataset /intervals/trials/maze_condition (VectorData) The set of 27 (or 108) mazes included was composed of 3 (or 12) “subsets”. Each subset contained 3 related mazes. Each maze had 3 “versions”: the 3-target with barrier, the 1-target with barriers, and the 1-target with no barriers. These 3 versions shared the same target positions. The 3-target and 1-target versions also shared the same barrier positions. In the 3-target version, exactly one target was accessible  | shape = (2911,) | dtype = uint8
  Dataset /intervals/trials/maze_num_barriers (VectorData) number of barriers presented | shape = (2911,) | dtype = uint8
  Dataset /intervals/trials/maze_num_targets (VectorData) number of targets presented | shape = (2911,) | dtype = uint8
  Dataset /intervals/trials/move_begins_time (VectorData) movement onset time | shape = (2911,) | dtype = float64
  Dataset /intervals/trials/move_ends_time (VectorData) movement stop time | shape = (2911,) | dtype = float64
  Dataset /intervals/trials/novel_maze (VectorData) novel maze | shape = (2911,) | dtype = uint8
  Dataset /intervals/trials/proto_trial (VectorData) whether that trial was used as the prototype trial for figuring out which trials were consistent | shape = (2911,) | dtype = uint8
  Dataset /intervals/trials/reaction_time (VectorData) reaction time | shape = (2911,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (2911,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (2911,) | dtype = float64
  Dataset /intervals/trials/target_positions (VectorData) x,y position on screen of all targets presented | shape = (4825, 2) | dtype = int16
  Dataset /intervals/trials/target_positions_index (VectorIndex) Index for VectorData 'target_positions' | shape = (2911,) | dtype = uint16
  Dataset /intervals/trials/target_presentation_time (VectorData) time of target presentation | shape = (2911,) | dtype = float64
  Dataset /intervals/trials/target_size (VectorData) half width of the targets | shape = (2911,) | dtype = uint8
  Dataset /intervals/trials/task_success (VectorData) indicates whether the monkey was successful on this trial | shape = (2911,) | dtype = uint8
  Dataset /intervals/trials/timeseries (VectorData) index into a TimeSeries object | shape = (8733,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/trials/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (2911,) | dtype = uint16
  Dataset /intervals/trials/trial_type (VectorData) trial type | shape = (2911,) | dtype = uint8
  Dataset /intervals/trials/trial_version (VectorData) should be 0 for a truly random maze (two random barriers). For a degenerate maze (real maze with some barriers randomly removed) trialVersion is >10 | shape = (2911,) | dtype = uint8
  Group /processing/behavior (ProcessingModule) contains monkey movement data
  Group /processing/behavior/Position (Position) 
  Group /processing/behavior/Position/Cursor (SpatialSeries) no description
  Group /processing/behavior/Position/Eye (SpatialSeries) no description
  Group /processing/behavior/Position/Hand (SpatialSeries) no description
  Group /processing/ecephys (ProcessingModule) Intermediate data from extracellular electrophysiology recordings, e.g., LFP.
  Group /processing/ecephys/Processed (FilteredEphys) 
  Group /processing/ecephys/Processed/A001 (ElectricalSeries) LFP signal for array A, segment 1data for both arrays A,B in the same segment should be, but is not of the same time lengthand cannot be synced due to lack of time stamps. Ignore the starting times.
  Dataset /processing/ecephys/Processed/A001/electrodes (DynamicTableRegion) electrode_table_region | shape = (96,) | dtype = int64
  Group /processing/ecephys/Processed/A002 (ElectricalSeries) LFP signal for array A, segment 2data for both arrays A,B in the same segment should be, but is not of the same time lengthand cannot be synced due to lack of time stamps. Ignore the starting times.
  Dataset /processing/ecephys/Processed/A002/electrodes (DynamicTableRegion) electrode_table_region | shape = (96,) | dtype = int64
  Group /processing/ecephys/Processed/A003 (ElectricalSeries) LFP signal for array A, segment 3data for both arrays A,B in the same segment should be, but is not of the same time lengthand cannot be synced due to lack of time stamps. Ignore the starting times.
  Dataset /processing/ecephys/Processed/A003/electrodes (DynamicTableRegion) electrode_table_region | shape = (96,) | dtype = int64
  Group /processing/ecephys/Processed/A004 (ElectricalSeries) LFP signal for array A, segment 4data for both arrays A,B in the same segment should be, but is not of the same time lengthand cannot be synced due to lack of time stamps. Ignore the starting times.
  Dataset /processing/ecephys/Processed/A004/electrodes (DynamicTableRegion) electrode_table_region | shape = (96,) | dtype = int64
  Group /processing/ecephys/Processed/B001 (ElectricalSeries) LFP signal for array B, segment 1data for both arrays A,B in the same segment should be, but is not of the same time lengthand cannot be synced due to lack of time stamps. Ignore the starting times.
  Dataset /processing/ecephys/Processed/B001/electrodes (DynamicTableRegion) electrode_table_region | shape = (96,) | dtype = int64
  Group /processing/ecephys/Processed/B002 (ElectricalSeries) LFP signal for array B, segment 2data for both arrays A,B in the same segment should be, but is not of the same time lengthand cannot be synced due to lack of time stamps. Ignore the starting times.
  Dataset /processing/ecephys/Processed/B002/electrodes (DynamicTableRegion) electrode_table_region | shape = (96,) | dtype = int64
  Group /processing/ecephys/Processed/B003 (ElectricalSeries) LFP signal for array B, segment 3data for both arrays A,B in the same segment should be, but is not of the same time lengthand cannot be synced due to lack of time stamps. Ignore the starting times.
  Dataset /processing/ecephys/Processed/B003/electrodes (DynamicTableRegion) electrode_table_region | shape = (96,) | dtype = int64
  Group /processing/ecephys/Processed/B004 (ElectricalSeries) LFP signal for array B, segment 4data for both arrays A,B in the same segment should be, but is not of the same time lengthand cannot be synced due to lack of time stamps. Ignore the starting times.
  Dataset /processing/ecephys/Processed/B004/electrodes (DynamicTableRegion) electrode_table_region | shape = (96,) | dtype = int64
  session_description: 
  session_start_time: 2009-09-10T00:00:00-07:00
  timestamps_reference_time: 2009-09-10T00:00:00-07:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (192,) | dtype = object
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (192,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex) Index for VectorData 'electrodes' | shape = (192,) | dtype = uint8
  Dataset /units/id (ElementIdentifiers)  | shape = (192,) | dtype = int64
  Dataset /units/obs_intervals (VectorData) the observation intervals for each unit | shape = (558912, 2) | dtype = float64
  Dataset /units/obs_intervals_index (VectorIndex) Index for VectorData 'obs_intervals' | shape = (192,) | dtype = uint32
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (94386885,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (192,) | dtype = uint32


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2021-08-22T08:34:16.495896-04:00']
  Group /general/devices/Utah Array(M1) (Device) 96 channel utah array
  Group /general/devices/Utah Array(PMd) (Device) 96 channel utah array
  experiment_description: 
  experimenter: ['Matthew T. Kaufman' 'Mark M. Churchland']
  Group /general/extracellular_ephys/1 (ElectrodeGroup) array corresponding to device implanted at PMd
  Group /general/extracellular_ephys/1/device (Device) 96 channel utah array
  Group /general/extracellular_ephys/2 (ElectrodeGroup) array corresponding to device implanted at M1
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
  related_publications: ['10.1038/nature11129 10.1152/jn.00892.2011 10.1038/nn.3643 10.1038/nn.4042 10.1146/annurev-neuro-062111-150509 10.7554/eLife.0467710.1523/ENEURO.0085-16.2016 10.1038/s41592-018-0109-9']
  Group /general/subject (Subject) 
  identifier: 45ef4b33-f931-4118-8458-fc1a86b6db9f
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/barrier_info (VectorData) (x,y,halfwidth,halfheight) | shape = (16176, 4) | dtype = float64
  Dataset /intervals/trials/barrier_info_index (VectorIndex) Index for VectorData 'barrier_info' | shape = (4044,) | dtype = uint16
  Dataset /intervals/trials/discard_trial (VectorData) flag that will usually be 0, but is set to 1 if there was a photo box problem (meaning RT can't be calculated accurately) or we had a hand tracking error during the movement. In general, throw those trials away. | shape = (4044,) | dtype = uint8
  Dataset /intervals/trials/frame_details (VectorData) (frameLeft,right,bottom,top, width) :tell where the frame (outer rectangle of barriers) were. For those, the values are inner edges | shape = (20220, 1, 1) | dtype = int16
  Dataset /intervals/trials/frame_details_index (VectorIndex) Index for VectorData 'frame_details' | shape = (4044,) | dtype = uint16
  Dataset /intervals/trials/go_cue_time (VectorData) time of go cue | shape = (4044,) | dtype = float64
  Dataset /intervals/trials/hit_target_position (VectorData) x,y position on screen of the target hit | shape = (4044, 2) | dtype = int16
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (4044,) | dtype = int64
  Dataset /intervals/trials/maze_num_barriers (VectorData) number of barriers presented | shape = (4044,) | dtype = uint8
  Dataset /intervals/trials/maze_num_targets (VectorData) number of targets presented | shape = (4044,) | dtype = uint8
  Dataset /intervals/trials/move_begins_time (VectorData) movement onset time | shape = (4044,) | dtype = float64
  Dataset /intervals/trials/move_ends_time (VectorData) movement stop time | shape = (4044,) | dtype = float64
  Dataset /intervals/trials/reaction_time (VectorData) reaction time | shape = (4044,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (4044,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (4044,) | dtype = float64
  Dataset /intervals/trials/target_positions (VectorData) x,y position on screen of all targets presented | shape = (8088, 2) | dtype = int16
  Dataset /intervals/trials/target_positions_index (VectorIndex) Index for VectorData 'target_positions' | shape = (4044,) | dtype = uint16
  Dataset /intervals/trials/target_presentation_time (VectorData) time of target presentation | shape = (4044,) | dtype = float64
  Dataset /intervals/trials/target_size (VectorData) half width of the targets | shape = (4044,) | dtype = uint8
  Dataset /intervals/trials/task_success (VectorData) indicates whether the monkey was successful on this trial | shape = (4044,) | dtype = uint8
  Dataset /intervals/trials/timeseries (VectorData) index into a TimeSeries object | shape = (12132,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/trials/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (4044,) | dtype = uint16
  Dataset /intervals/trials/trial_type (VectorData) trial type | shape = (4044,) | dtype = uint8
  Group /processing/behavior (ProcessingModule) contains monkey movement data
  Group /processing/behavior/Position (Position) 
  Group /processing/behavior/Position/Cursor (SpatialSeries) no description
  Group /processing/behavior/Position/Eye (SpatialSeries) no description
  Group /processing/behavior/Position/Hand (SpatialSeries) no description
  Group /processing/ecephys (ProcessingModule) Intermediate data from extracellular electrophysiology recordings, e.g., LFP.
  Group /processing/ecephys/Processed (FilteredEphys) 
  Group /processing/ecephys/Processed/A001 (ElectricalSeries) LFP signal for array A, segment 1data for both arrays A,B in the same segment should be, but is not of the same time lengthand cannot be synced due to lack of time stamps. Ignore the starting times.
  Dataset /processing/ecephys/Processed/A001/electrodes (DynamicTableRegion) electrode_table_region | shape = (96,) | dtype = int64
  Group /processing/ecephys/Processed/A002 (ElectricalSeries) LFP signal for array A, segment 2data for both arrays A,B in the same segment should be, but is not of the same time lengthand cannot be synced due to lack of time stamps. Ignore the starting times.
  Dataset /processing/ecephys/Processed/A002/electrodes (DynamicTableRegion) electrode_table_region | shape = (96,) | dtype = int64
  Group /processing/ecephys/Processed/A003 (ElectricalSeries) LFP signal for array A, segment 3data for both arrays A,B in the same segment should be, but is not of the same time lengthand cannot be synced due to lack of time stamps. Ignore the starting times.
  Dataset /processing/ecephys/Processed/A003/electrodes (DynamicTableRegion) electrode_table_region | shape = (96,) | dtype = int64
  Group /processing/ecephys/Processed/B001 (ElectricalSeries) LFP signal for array B, segment 1data for both arrays A,B in the same segment should be, but is not of the same time lengthand cannot be synced due to lack of time stamps. Ignore the starting times.
  Dataset /processing/ecephys/Processed/B001/electrodes (DynamicTableRegion) electrode_table_region | shape = (96,) | dtype = int64
  Group /processing/ecephys/Processed/B002 (ElectricalSeries) LFP signal for array B, segment 2data for both arrays A,B in the same segment should be, but is not of the same time lengthand cannot be synced due to lack of time stamps. Ignore the starting times.
  Dataset /processing/ecephys/Processed/B002/electrodes (DynamicTableRegion) electrode_table_region | shape = (96,) | dtype = int64
  Group /processing/ecephys/Processed/B003 (ElectricalSeries) LFP signal for array B, segment 3data for both arrays A,B in the same segment should be, but is not of the same time lengthand cannot be synced due to lack of time stamps. Ignore the starting times.
  Dataset /processing/ecephys/Processed/B003/electrodes (DynamicTableRegion) electrode_table_region | shape = (96,) | dtype = int64
  session_description: 
  session_start_time: 2009-09-20T00:00:00-07:00
  timestamps_reference_time: 2009-09-20T00:00:00-07:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (192,) | dtype = object
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (192,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex) Index for VectorData 'electrodes' | shape = (192,) | dtype = uint8
  Dataset /units/id (ElementIdentifiers)  | shape = (192,) | dtype = int64
  Dataset /units/obs_intervals (VectorData) the observation intervals for each unit | shape = (776448, 2) | dtype = float64
  Dataset /units/obs_intervals_index (VectorIndex) Index for VectorData 'obs_intervals' | shape = (192,) | dtype = uint32
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (81387912,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (192,) | dtype = uint32


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2021-08-22T09:23:06.760073-04:00']
  Group /general/devices/Utah Array(M1) (Device) 96 channel utah array
  Group /general/devices/Utah Array(PMd) (Device) 96 channel utah array
  experiment_description: 
  experimenter: ['Mark M. Churchland' 'Matthew T. Kaufman']
  Group /general/extracellular_ephys/1 (ElectrodeGroup) array corresponding to device implanted at PMd
  Group /general/extracellular_ephys/1/device (Device) 96 channel utah array
  Group /general/extracellular_ephys/2 (ElectrodeGroup) array corresponding to device implanted at M1
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
  related_publications: ['10.1038/nature11129 10.1152/jn.00892.2011 10.1038/nn.3643 10.1038/nn.4042 10.1146/annurev-neuro-062111-150509 10.7554/eLife.0467710.1523/ENEURO.0085-16.2016 10.1038/s41592-018-0109-9']
  Group /general/subject (Subject) 
  identifier: e0f29217-4d4d-4753-97d5-91f5abe7e02f
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/barrier_info (VectorData) (x,y,halfwidth,halfheight) | shape = (10448, 4) | dtype = float64
  Dataset /intervals/trials/barrier_info_index (VectorIndex) Index for VectorData 'barrier_info' | shape = (2612,) | dtype = uint16
  Dataset /intervals/trials/discard_trial (VectorData) flag that will usually be 0, but is set to 1 if there was a photo box problem (meaning RT can't be calculated accurately) or we had a hand tracking error during the movement. In general, throw those trials away. | shape = (2612,) | dtype = uint8
  Dataset /intervals/trials/frame_details (VectorData) (frameLeft,right,bottom,top, width) :tell where the frame (outer rectangle of barriers) were. For those, the values are inner edges | shape = (13060, 1, 1) | dtype = int16
  Dataset /intervals/trials/frame_details_index (VectorIndex) Index for VectorData 'frame_details' | shape = (2612,) | dtype = uint16
  Dataset /intervals/trials/go_cue_time (VectorData) time of go cue | shape = (2612,) | dtype = float64
  Dataset /intervals/trials/hit_target_position (VectorData) x,y position on screen of the target hit | shape = (2612, 2) | dtype = int16
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (2612,) | dtype = int64
  Dataset /intervals/trials/maze_num_barriers (VectorData) number of barriers presented | shape = (2612,) | dtype = uint8
  Dataset /intervals/trials/maze_num_targets (VectorData) number of targets presented | shape = (2612,) | dtype = uint8
  Dataset /intervals/trials/move_begins_time (VectorData) movement onset time | shape = (2612,) | dtype = float64
  Dataset /intervals/trials/move_ends_time (VectorData) movement stop time | shape = (2612,) | dtype = float64
  Dataset /intervals/trials/reaction_time (VectorData) reaction time | shape = (2612,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (2612,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (2612,) | dtype = float64
  Dataset /intervals/trials/target_positions (VectorData) x,y position on screen of all targets presented | shape = (5224, 2) | dtype = int16
  Dataset /intervals/trials/target_positions_index (VectorIndex) Index for VectorData 'target_positions' | shape = (2612,) | dtype = uint16
  Dataset /intervals/trials/target_presentation_time (VectorData) time of target presentation | shape = (2612,) | dtype = float64
  Dataset /intervals/trials/target_size (VectorData) half width of the targets | shape = (2612,) | dtype = uint8
  Dataset /intervals/trials/task_success (VectorData) indicates whether the monkey was successful on this trial | shape = (2612,) | dtype = uint8
  Dataset /intervals/trials/timeseries (VectorData) index into a TimeSeries object | shape = (7836,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/trials/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (2612,) | dtype = uint16
  Dataset /intervals/trials/trial_type (VectorData) trial type | shape = (2612,) | dtype = uint8
  Group /processing/behavior (ProcessingModule) contains monkey movement data
  Group /processing/behavior/Position (Position) 
  Group /processing/behavior/Position/Cursor (SpatialSeries) no description
  Group /processing/behavior/Position/Eye (SpatialSeries) no description
  Group /processing/behavior/Position/Hand (SpatialSeries) no description
  Group /processing/ecephys (ProcessingModule) Intermediate data from extracellular electrophysiology recordings, e.g., LFP.
  Group /processing/ecephys/Processed (FilteredEphys) 
  Group /processing/ecephys/Processed/A001 (ElectricalSeries) LFP signal for array A, segment 1data for both arrays A,B in the same segment should be, but is not of the same time lengthand cannot be synced due to lack of time stamps. Ignore the starting times.
  Dataset /processing/ecephys/Processed/A001/electrodes (DynamicTableRegion) electrode_table_region | shape = (96,) | dtype = int64
  Group /processing/ecephys/Processed/A002 (ElectricalSeries) LFP signal for array A, segment 2data for both arrays A,B in the same segment should be, but is not of the same time lengthand cannot be synced due to lack of time stamps. Ignore the starting times.
  Dataset /processing/ecephys/Processed/A002/electrodes (DynamicTableRegion) electrode_table_region | shape = (96,) | dtype = int64
  Group /processing/ecephys/Processed/B001 (ElectricalSeries) LFP signal for array B, segment 1data for both arrays A,B in the same segment should be, but is not of the same time lengthand cannot be synced due to lack of time stamps. Ignore the starting times.
  Dataset /processing/ecephys/Processed/B001/electrodes (DynamicTableRegion) electrode_table_region | shape = (96,) | dtype = int64
  Group /processing/ecephys/Processed/B002 (ElectricalSeries) LFP signal for array B, segment 2data for both arrays A,B in the same segment should be, but is not of the same time lengthand cannot be synced due to lack of time stamps. Ignore the starting times.
  Dataset /processing/ecephys/Processed/B002/electrodes (DynamicTableRegion) electrode_table_region | shape = (96,) | dtype = int64
  session_description: 
  session_start_time: 2009-09-22T00:00:00-07:00
  timestamps_reference_time: 2009-09-22T00:00:00-07:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (192,) | dtype = object
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (192,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex) Index for VectorData 'electrodes' | shape = (192,) | dtype = uint8
  Dataset /units/id (ElementIdentifiers)  | shape = (192,) | dtype = int64
  Dataset /units/obs_intervals (VectorData) the observation intervals for each unit | shape = (501504, 2) | dtype = float64
  Dataset /units/obs_intervals_index (VectorIndex) Index for VectorData 'obs_intervals' | shape = (192,) | dtype = uint32
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (66829586,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (192,) | dtype = uint32
