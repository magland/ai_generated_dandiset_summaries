
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001062/draft
name: Marmoset electrophysiology and kinematics during prey capture (monkey MG)
contributor: [{'name': 'Moore, Dalton', 'email': 'daltonm@uchicago.edu', 'roleName': ['dcite:ContactPerson', 'dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0003-0187-2364', 'affiliation': [{'name': 'University of Chicago', 'schemaKey': 'Affiliation'}], 'includeInCitation': True}, {'name': 'Walker, Jeffrey', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0001-7192-9800', 'includeInCitation': True}, {'name': 'MacLean, Jason', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-8021-8063', 'includeInCitation': True}, {'name': 'Hatsopoulos, Nicholas', 'email': 'nicho@uchicago.edu', 'roleName': ['dcite:Author', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0002-4913-6051', 'includeInCitation': True}]
description: Electrophysiology recorded from a 96-channel Utah array implanted in primary motor and somotasensory cortex of the common marmoset. The file also contains kinematics of the hand, elbow, wrist, and head as the marmoset engaged in a naturalistic prey capture task with live moths. This is the processed version of the data, which contains spike-sorted electrophysiology and quantified kinematics (processed by DeepLabCut and Anipose). 
assetsSummary: {'species': [{'name': 'Callithrix jacchus - Common marmoset', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9483'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 278740648, 'numberOfFiles': 1, 'numberOfSubjects': 1, 'variableMeasured': ['ProcessingModule', 'ElectrodeGroup', 'Units'], 'measurementTechnique': [{'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 001062 has 1 NWB files.
1 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2024-06-13T14:23:47.733901-05:00']
  Group /general/devices/Cerebus AnalogIn (Device) analog inputs on Cerebus
  Group /general/devices/Utah Array (M1 target) (Device) 96 channel utah array
  experimenter: ['Moore, Dalton']
  Group /general/extracellular_ephys/MG_array_1 (ElectrodeGroup) array implanted in left forelimb sensorimotor cortex
  Group /general/extracellular_ephys/MG_array_1/device (Device) 96 channel utah array
  Group /general/extracellular_ephys/ainp (ElectrodeGroup) analog inputs from cameras and touchscreen, with ainp1 thru ainp3 corresponding to apparatus cams, enclosure cams, and touchscreen, respectively
  Group /general/extracellular_ephys/ainp/device (Device) analog inputs on Cerebus
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/brain_region (VectorData) no description | shape = (99,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/channel_name (VectorData) unique channel reference | shape = (99,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/electrode_label (VectorData) no description | shape = (99,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) no description | shape = (99,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (99,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (99,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (99,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) no description | shape = (99,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (99,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) no description | shape = (99,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) no description | shape = (99,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) no description | shape = (99,) | dtype = float64
  institution: University of Chicago
  keywords: ['moths' 'free']
  lab: Hatsopoulos Lab
  notes: MG moths and spontaneous behavior
  
  Decently dynamic moths, good engagement for first 20 minutes of session
  Additional engagment with mixture of moarshmallows, foraging mix, and moths later in session
  
  3:14 PM 4/16/2023
  Began dispensing moths
  
  3:54 PM 4/16/2023
  Good moths session so far. Estimate ~35-50 good reaches, probably 25-30 episodes. Giving MG a break.
  
  4:33 PM 4/16/2023
  Resume dispensing moths 
  
  4:43 PM 4/16/2023
  switched to marshmallows in oatmeal
  
  5:18 PM 4/16/2023
  Session over
  protocol: IACUC 72339
  related_publications: ['doi: https://doi.org/10.21203/rs.3.rs-3750312']
  source_script: Created using NeuroConv v0.4.10
  Group /general/subject (Subject) 
  identifier: MG20230416_1505_mothsAndFree-002
  Group /intervals/neural_dropout (TimeIntervals) intervals of dropout in neural signal, computed in 0.100000 sec bins
  Dataset /intervals/neural_dropout/drop_duration (VectorData) duration of dropout in seconds | shape = (279,) | dtype = float64
  Dataset /intervals/neural_dropout/id (ElementIdentifiers)  | shape = (279,) | dtype = int64
  Dataset /intervals/neural_dropout/start_time (VectorData) Start time of epoch, in seconds | shape = (279,) | dtype = float64
  Dataset /intervals/neural_dropout/stop_time (VectorData) Stop time of epoch, in seconds | shape = (279,) | dtype = float64
  Group /intervals/reaching_segments_moths (TimeIntervals) reaching segments identified in kinematics tracked by DLC+anipose
  Dataset /intervals/reaching_segments_moths/id (ElementIdentifiers)  | shape = (56,) | dtype = int64
  Dataset /intervals/reaching_segments_moths/kinematics_module (VectorData) string identifier for linked kinematics module. E.g. nwb.processing[kinematics_module].data_interfaces[video_event] | shape = (56,) | dtype = object
  Dataset /intervals/reaching_segments_moths/peak_extension_idxs (VectorData) index of maximum extension (or 'peak' of reach) within video event | shape = (56,) | dtype = object
  Dataset /intervals/reaching_segments_moths/peak_extension_times (VectorData) time of maximum extension (or 'peak' of reach) | shape = (56,) | dtype = object
  Dataset /intervals/reaching_segments_moths/start_idx (VectorData) index of reach start within video event | shape = (56,) | dtype = int64
  Dataset /intervals/reaching_segments_moths/start_time (VectorData) Start time of epoch, in seconds | shape = (56,) | dtype = float64
  Dataset /intervals/reaching_segments_moths/stop_idx (VectorData) index of reach stop within video event | shape = (56,) | dtype = int64
  Dataset /intervals/reaching_segments_moths/stop_time (VectorData) Stop time of epoch, in seconds | shape = (56,) | dtype = float64
  Dataset /intervals/reaching_segments_moths/video_event (VectorData) string identifier for video event in linked kinematics module. E.g. nwb.processing[kinematics_module].data_interfaces[video_event] | shape = (56,) | dtype = object
  Group /intervals/video_events_free (TimeIntervals) metadata for behavior/video events associated with kinematics
  Dataset /intervals/video_events_free/analog_signals_cut_at_end (VectorData) The number of analog signals (if any) that occurred after the end of video recording session. If they existed, they were cut during processing. | shape = (1,) | dtype = float64
  Dataset /intervals/video_events_free/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /intervals/video_events_free/start_time (VectorData) Start time of epoch, in seconds | shape = (1,) | dtype = float64
  Dataset /intervals/video_events_free/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1,) | dtype = float64
  Dataset /intervals/video_events_free/video_session (VectorData) video session number of recorded video files | shape = (1,) | dtype = int64
  Group /intervals/video_events_moths (TimeIntervals) metadata for behavior/video events associated with kinematics
  Dataset /intervals/video_events_moths/analog_signals_cut_at_end (VectorData) The number of analog signals (if any) that occurred after the end of video recording session. If they existed, they were cut during processing. | shape = (54,) | dtype = float64
  Dataset /intervals/video_events_moths/id (ElementIdentifiers)  | shape = (54,) | dtype = int64
  Dataset /intervals/video_events_moths/start_time (VectorData) Start time of epoch, in seconds | shape = (54,) | dtype = float64
  Dataset /intervals/video_events_moths/stop_time (VectorData) Stop time of epoch, in seconds | shape = (54,) | dtype = float64
  Dataset /intervals/video_events_moths/video_session (VectorData) video session number of recorded video files | shape = (54,) | dtype = int64
  Group /processing/dropped_frames_free (ProcessingModule) Record of dropped frames. The dropped frames have been replaced by copies of the previous good frame. Pose estimation may not be effected if most of the cameras captured that frame or if the drop is brief. Use the boolean mask vectors stored here as needed.
  Group /processing/dropped_frames_moths (ProcessingModule) Record of dropped frames. The dropped frames have been replaced by copies of the previous good frame. Pose estimation may not be effected if most of the cameras captured that frame or if the drop is brief. Use the boolean mask vectors stored here as needed.
  Group /processing/ecephys (ProcessingModule) Intermediate data from extracellular electrophysiology recordings, e.g., LFP.
  Group /processing/goal_directed_kinematics (ProcessingModule) prey capture kinematics - moths
  Group /processing/goal_directed_kinematics/moths_s_1_e_001_position (PoseEstimation) 
  Group /processing/goal_directed_kinematics/moths_s_1_e_001_position/l-elbow (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_001_position/l-head-corner (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_001_position/l-head-front (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_001_position/l-head-under-tab (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_001_position/l-shoulder (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_001_position/l-wrist (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_001_position/origin (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_001_position/r-elbow (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_001_position/r-head-corner (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_001_position/r-head-front (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_001_position/r-head-under-tab (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_001_position/r-shoulder (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_001_position/r-wrist (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_001_position/x (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_001_position/y (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_002_position (PoseEstimation) 
  Group /processing/goal_directed_kinematics/moths_s_1_e_002_position/l-elbow (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_002_position/l-head-corner (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_002_position/l-head-front (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_002_position/l-head-under-tab (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_002_position/l-shoulder (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_002_position/l-wrist (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_002_position/origin (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_002_position/r-elbow (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_002_position/r-head-corner (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_002_position/r-head-front (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_002_position/r-head-under-tab (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_002_position/r-shoulder (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_002_position/r-wrist (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_002_position/x (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_002_position/y (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_003_position (PoseEstimation) 
  Group /processing/goal_directed_kinematics/moths_s_1_e_003_position/l-elbow (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_003_position/l-head-corner (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_003_position/l-head-front (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_003_position/l-head-under-tab (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_003_position/l-shoulder (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_003_position/l-wrist (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_003_position/origin (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_003_position/r-elbow (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_003_position/r-head-corner (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_003_position/r-head-front (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_003_position/r-head-under-tab (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_003_position/r-shoulder (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_003_position/r-wrist (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_003_position/x (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_003_position/y (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_008_position (PoseEstimation) 
  Group /processing/goal_directed_kinematics/moths_s_1_e_008_position/l-elbow (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_008_position/l-head-corner (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_008_position/l-head-front (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_008_position/l-head-under-tab (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_008_position/l-shoulder (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_008_position/l-wrist (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_008_position/origin (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_008_position/r-elbow (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_008_position/r-head-corner (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_008_position/r-head-front (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_008_position/r-head-under-tab (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_008_position/r-shoulder (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_008_position/r-wrist (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_008_position/x (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_008_position/y (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_017_position (PoseEstimation) 
  Group /processing/goal_directed_kinematics/moths_s_1_e_017_position/l-elbow (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_017_position/l-head-corner (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_017_position/l-head-front (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_017_position/l-head-under-tab (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_017_position/l-shoulder (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_017_position/l-wrist (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_017_position/origin (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_017_position/r-elbow (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_017_position/r-head-corner (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_017_position/r-head-front (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_017_position/r-head-under-tab (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_017_position/r-shoulder (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_017_position/r-wrist (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_017_position/x (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_017_position/y (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_020_position (PoseEstimation) 
  Group /processing/goal_directed_kinematics/moths_s_1_e_020_position/l-elbow (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_020_position/l-head-corner (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_020_position/l-head-front (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_020_position/l-head-under-tab (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_020_position/l-shoulder (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_020_position/l-wrist (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_020_position/origin (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_020_position/r-elbow (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_020_position/r-head-corner (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_020_position/r-head-front (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_020_position/r-head-under-tab (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_020_position/r-shoulder (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_020_position/r-wrist (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_020_position/x (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_020_position/y (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_025_position (PoseEstimation) 
  Group /processing/goal_directed_kinematics/moths_s_1_e_025_position/l-elbow (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_025_position/l-head-corner (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_025_position/l-head-front (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_025_position/l-head-under-tab (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_025_position/l-shoulder (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_025_position/l-wrist (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_025_position/origin (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_025_position/r-elbow (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_025_position/r-head-corner (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_025_position/r-head-front (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_025_position/r-head-under-tab (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_025_position/r-shoulder (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_025_position/r-wrist (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_025_position/x (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_025_position/y (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_029_position (PoseEstimation) 
  Group /processing/goal_directed_kinematics/moths_s_1_e_029_position/l-elbow (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_029_position/l-head-corner (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_029_position/l-head-front (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_029_position/l-head-under-tab (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_029_position/l-shoulder (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_029_position/l-wrist (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_029_position/origin (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_029_position/r-elbow (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_029_position/r-head-corner (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_029_position/r-head-front (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_029_position/r-head-under-tab (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_029_position/r-shoulder (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_029_position/r-wrist (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_029_position/x (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_029_position/y (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_030_position (PoseEstimation) 
  Group /processing/goal_directed_kinematics/moths_s_1_e_030_position/l-elbow (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_030_position/l-head-corner (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_030_position/l-head-front (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_030_position/l-head-under-tab (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_030_position/l-shoulder (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_030_position/l-wrist (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_030_position/origin (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_030_position/r-elbow (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_030_position/r-head-corner (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_030_position/r-head-front (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_030_position/r-head-under-tab (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_030_position/r-shoulder (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_030_position/r-wrist (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_030_position/x (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_030_position/y (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_033_position (PoseEstimation) 
  Group /processing/goal_directed_kinematics/moths_s_1_e_033_position/l-elbow (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_033_position/l-head-corner (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_033_position/l-head-front (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_033_position/l-head-under-tab (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_033_position/l-shoulder (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_033_position/l-wrist (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_033_position/origin (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_033_position/r-elbow (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_033_position/r-head-corner (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_033_position/r-head-front (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_033_position/r-head-under-tab (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_033_position/r-shoulder (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_033_position/r-wrist (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_033_position/x (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_033_position/y (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_039_position (PoseEstimation) 
  Group /processing/goal_directed_kinematics/moths_s_1_e_039_position/l-elbow (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_039_position/l-head-corner (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_039_position/l-head-front (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_039_position/l-head-under-tab (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_039_position/l-shoulder (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_039_position/l-wrist (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_039_position/origin (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_039_position/r-elbow (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_039_position/r-head-corner (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_039_position/r-head-front (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_039_position/r-head-under-tab (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_039_position/r-shoulder (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_039_position/r-wrist (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_039_position/x (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_039_position/y (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_040_position (PoseEstimation) 
  Group /processing/goal_directed_kinematics/moths_s_1_e_040_position/l-elbow (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_040_position/l-head-corner (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_040_position/l-head-front (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_040_position/l-head-under-tab (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_040_position/l-shoulder (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_040_position/l-wrist (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_040_position/origin (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_040_position/r-elbow (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_040_position/r-head-corner (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_040_position/r-head-front (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_040_position/r-head-under-tab (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_040_position/r-shoulder (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_040_position/r-wrist (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_040_position/x (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_040_position/y (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_043_position (PoseEstimation) 
  Group /processing/goal_directed_kinematics/moths_s_1_e_043_position/l-elbow (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_043_position/l-head-corner (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_043_position/l-head-front (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_043_position/l-head-under-tab (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_043_position/l-shoulder (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_043_position/l-wrist (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_043_position/origin (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_043_position/r-elbow (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_043_position/r-head-corner (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_043_position/r-head-front (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_043_position/r-head-under-tab (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_043_position/r-shoulder (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_043_position/r-wrist (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_043_position/x (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_043_position/y (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_044_position (PoseEstimation) 
  Group /processing/goal_directed_kinematics/moths_s_1_e_044_position/l-elbow (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_044_position/l-head-corner (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_044_position/l-head-front (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_044_position/l-head-under-tab (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_044_position/l-shoulder (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_044_position/l-wrist (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_044_position/origin (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_044_position/r-elbow (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_044_position/r-head-corner (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_044_position/r-head-front (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_044_position/r-head-under-tab (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_044_position/r-shoulder (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_044_position/r-wrist (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_044_position/x (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_044_position/y (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_045_position (PoseEstimation) 
  Group /processing/goal_directed_kinematics/moths_s_1_e_045_position/l-elbow (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_045_position/l-head-corner (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_045_position/l-head-front (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_045_position/l-head-under-tab (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_045_position/l-shoulder (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_045_position/l-wrist (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_045_position/origin (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_045_position/r-elbow (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_045_position/r-head-corner (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_045_position/r-head-front (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_045_position/r-head-under-tab (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_045_position/r-shoulder (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_045_position/r-wrist (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_045_position/x (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_045_position/y (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_052_position (PoseEstimation) 
  Group /processing/goal_directed_kinematics/moths_s_1_e_052_position/l-elbow (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_052_position/l-head-corner (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_052_position/l-head-front (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_052_position/l-head-under-tab (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_052_position/l-shoulder (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_052_position/l-wrist (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_052_position/origin (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_052_position/r-elbow (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_052_position/r-head-corner (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_052_position/r-head-front (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_052_position/r-head-under-tab (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_052_position/r-shoulder (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_052_position/r-wrist (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_052_position/x (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/goal_directed_kinematics/moths_s_1_e_052_position/y (PoseEstimationSeries) 3D pose tracked by DLC+Anipose. Dimensions of data are [time, x/y/z]
  Group /processing/video_event_timestamps_free (ProcessingModule) set of timeseries holding timestamps for each behavior/video event for experiment = free. 
                      Videos are located at /project/nicho/data/marmosets/kinematics_videos/moths/HMMG/2023_04_16.
                      This first few elements of the path may need to be changed to the new storage location for the "data" directory.
  Group /processing/video_event_timestamps_free/free_s_1_e_001_timestamps (TimeSeries) empty time series holding analog signal timestamps for video frames/DLC pose estimation that will be associated with PoseEstimationSeries data
  Group /processing/video_event_timestamps_moths (ProcessingModule) set of timeseries holding timestamps for each behavior/video event for experiment = moths. 
                      Videos are located at /project/nicho/data/marmosets/kinematics_videos/free/HMMG/2023_04_16.
                      This first few elements of the path may need to be changed to the new storage location for the "data" directory.
  Group /processing/video_event_timestamps_moths/moths_s_1_e_001_timestamps (TimeSeries) empty time series holding analog signal timestamps for video frames/DLC pose estimation that will be associated with PoseEstimationSeries data
  Group /processing/video_event_timestamps_moths/moths_s_1_e_002_timestamps (TimeSeries) empty time series holding analog signal timestamps for video frames/DLC pose estimation that will be associated with PoseEstimationSeries data
  Group /processing/video_event_timestamps_moths/moths_s_1_e_003_timestamps (TimeSeries) empty time series holding analog signal timestamps for video frames/DLC pose estimation that will be associated with PoseEstimationSeries data
  Group /processing/video_event_timestamps_moths/moths_s_1_e_004_timestamps (TimeSeries) empty time series holding analog signal timestamps for video frames/DLC pose estimation that will be associated with PoseEstimationSeries data
  Group /processing/video_event_timestamps_moths/moths_s_1_e_005_timestamps (TimeSeries) empty time series holding analog signal timestamps for video frames/DLC pose estimation that will be associated with PoseEstimationSeries data
  Group /processing/video_event_timestamps_moths/moths_s_1_e_006_timestamps (TimeSeries) empty time series holding analog signal timestamps for video frames/DLC pose estimation that will be associated with PoseEstimationSeries data
  Group /processing/video_event_timestamps_moths/moths_s_1_e_007_timestamps (TimeSeries) empty time series holding analog signal timestamps for video frames/DLC pose estimation that will be associated with PoseEstimationSeries data
  Group /processing/video_event_timestamps_moths/moths_s_1_e_008_timestamps (TimeSeries) empty time series holding analog signal timestamps for video frames/DLC pose estimation that will be associated with PoseEstimationSeries data
  Group /processing/video_event_timestamps_moths/moths_s_1_e_009_timestamps (TimeSeries) empty time series holding analog signal timestamps for video frames/DLC pose estimation that will be associated with PoseEstimationSeries data
  Group /processing/video_event_timestamps_moths/moths_s_1_e_010_timestamps (TimeSeries) empty time series holding analog signal timestamps for video frames/DLC pose estimation that will be associated with PoseEstimationSeries data
  Group /processing/video_event_timestamps_moths/moths_s_1_e_011_timestamps (TimeSeries) empty time series holding analog signal timestamps for video frames/DLC pose estimation that will be associated with PoseEstimationSeries data
  Group /processing/video_event_timestamps_moths/moths_s_1_e_012_timestamps (TimeSeries) empty time series holding analog signal timestamps for video frames/DLC pose estimation that will be associated with PoseEstimationSeries data
  Group /processing/video_event_timestamps_moths/moths_s_1_e_013_timestamps (TimeSeries) empty time series holding analog signal timestamps for video frames/DLC pose estimation that will be associated with PoseEstimationSeries data
  Group /processing/video_event_timestamps_moths/moths_s_1_e_014_timestamps (TimeSeries) empty time series holding analog signal timestamps for video frames/DLC pose estimation that will be associated with PoseEstimationSeries data
  Group /processing/video_event_timestamps_moths/moths_s_1_e_015_timestamps (TimeSeries) empty time series holding analog signal timestamps for video frames/DLC pose estimation that will be associated with PoseEstimationSeries data
  Group /processing/video_event_timestamps_moths/moths_s_1_e_016_timestamps (TimeSeries) empty time series holding analog signal timestamps for video frames/DLC pose estimation that will be associated with PoseEstimationSeries data
  Group /processing/video_event_timestamps_moths/moths_s_1_e_017_timestamps (TimeSeries) empty time series holding analog signal timestamps for video frames/DLC pose estimation that will be associated with PoseEstimationSeries data
  Group /processing/video_event_timestamps_moths/moths_s_1_e_018_timestamps (TimeSeries) empty time series holding analog signal timestamps for video frames/DLC pose estimation that will be associated with PoseEstimationSeries data
  Group /processing/video_event_timestamps_moths/moths_s_1_e_019_timestamps (TimeSeries) empty time series holding analog signal timestamps for video frames/DLC pose estimation that will be associated with PoseEstimationSeries data
  Group /processing/video_event_timestamps_moths/moths_s_1_e_020_timestamps (TimeSeries) empty time series holding analog signal timestamps for video frames/DLC pose estimation that will be associated with PoseEstimationSeries data
  Group /processing/video_event_timestamps_moths/moths_s_1_e_021_timestamps (TimeSeries) empty time series holding analog signal timestamps for video frames/DLC pose estimation that will be associated with PoseEstimationSeries data
  Group /processing/video_event_timestamps_moths/moths_s_1_e_022_timestamps (TimeSeries) empty time series holding analog signal timestamps for video frames/DLC pose estimation that will be associated with PoseEstimationSeries data
  Group /processing/video_event_timestamps_moths/moths_s_1_e_023_timestamps (TimeSeries) empty time series holding analog signal timestamps for video frames/DLC pose estimation that will be associated with PoseEstimationSeries data
  Group /processing/video_event_timestamps_moths/moths_s_1_e_024_timestamps (TimeSeries) empty time series holding analog signal timestamps for video frames/DLC pose estimation that will be associated with PoseEstimationSeries data
  Group /processing/video_event_timestamps_moths/moths_s_1_e_025_timestamps (TimeSeries) empty time series holding analog signal timestamps for video frames/DLC pose estimation that will be associated with PoseEstimationSeries data
  Group /processing/video_event_timestamps_moths/moths_s_1_e_026_timestamps (TimeSeries) empty time series holding analog signal timestamps for video frames/DLC pose estimation that will be associated with PoseEstimationSeries data
  Group /processing/video_event_timestamps_moths/moths_s_1_e_027_timestamps (TimeSeries) empty time series holding analog signal timestamps for video frames/DLC pose estimation that will be associated with PoseEstimationSeries data
  Group /processing/video_event_timestamps_moths/moths_s_1_e_028_timestamps (TimeSeries) empty time series holding analog signal timestamps for video frames/DLC pose estimation that will be associated with PoseEstimationSeries data
  Group /processing/video_event_timestamps_moths/moths_s_1_e_029_timestamps (TimeSeries) empty time series holding analog signal timestamps for video frames/DLC pose estimation that will be associated with PoseEstimationSeries data
  Group /processing/video_event_timestamps_moths/moths_s_1_e_030_timestamps (TimeSeries) empty time series holding analog signal timestamps for video frames/DLC pose estimation that will be associated with PoseEstimationSeries data
  Group /processing/video_event_timestamps_moths/moths_s_1_e_031_timestamps (TimeSeries) empty time series holding analog signal timestamps for video frames/DLC pose estimation that will be associated with PoseEstimationSeries data
  Group /processing/video_event_timestamps_moths/moths_s_1_e_032_timestamps (TimeSeries) empty time series holding analog signal timestamps for video frames/DLC pose estimation that will be associated with PoseEstimationSeries data
  Group /processing/video_event_timestamps_moths/moths_s_1_e_033_timestamps (TimeSeries) empty time series holding analog signal timestamps for video frames/DLC pose estimation that will be associated with PoseEstimationSeries data
  Group /processing/video_event_timestamps_moths/moths_s_1_e_034_timestamps (TimeSeries) empty time series holding analog signal timestamps for video frames/DLC pose estimation that will be associated with PoseEstimationSeries data
  Group /processing/video_event_timestamps_moths/moths_s_1_e_035_timestamps (TimeSeries) empty time series holding analog signal timestamps for video frames/DLC pose estimation that will be associated with PoseEstimationSeries data
  Group /processing/video_event_timestamps_moths/moths_s_1_e_036_timestamps (TimeSeries) empty time series holding analog signal timestamps for video frames/DLC pose estimation that will be associated with PoseEstimationSeries data
  Group /processing/video_event_timestamps_moths/moths_s_1_e_037_timestamps (TimeSeries) empty time series holding analog signal timestamps for video frames/DLC pose estimation that will be associated with PoseEstimationSeries data
  Group /processing/video_event_timestamps_moths/moths_s_1_e_038_timestamps (TimeSeries) empty time series holding analog signal timestamps for video frames/DLC pose estimation that will be associated with PoseEstimationSeries data
  Group /processing/video_event_timestamps_moths/moths_s_1_e_039_timestamps (TimeSeries) empty time series holding analog signal timestamps for video frames/DLC pose estimation that will be associated with PoseEstimationSeries data
  Group /processing/video_event_timestamps_moths/moths_s_1_e_040_timestamps (TimeSeries) empty time series holding analog signal timestamps for video frames/DLC pose estimation that will be associated with PoseEstimationSeries data
  Group /processing/video_event_timestamps_moths/moths_s_1_e_041_timestamps (TimeSeries) empty time series holding analog signal timestamps for video frames/DLC pose estimation that will be associated with PoseEstimationSeries data
  Group /processing/video_event_timestamps_moths/moths_s_1_e_042_timestamps (TimeSeries) empty time series holding analog signal timestamps for video frames/DLC pose estimation that will be associated with PoseEstimationSeries data
  Group /processing/video_event_timestamps_moths/moths_s_1_e_043_timestamps (TimeSeries) empty time series holding analog signal timestamps for video frames/DLC pose estimation that will be associated with PoseEstimationSeries data
  Group /processing/video_event_timestamps_moths/moths_s_1_e_044_timestamps (TimeSeries) empty time series holding analog signal timestamps for video frames/DLC pose estimation that will be associated with PoseEstimationSeries data
  Group /processing/video_event_timestamps_moths/moths_s_1_e_045_timestamps (TimeSeries) empty time series holding analog signal timestamps for video frames/DLC pose estimation that will be associated with PoseEstimationSeries data
  Group /processing/video_event_timestamps_moths/moths_s_1_e_046_timestamps (TimeSeries) empty time series holding analog signal timestamps for video frames/DLC pose estimation that will be associated with PoseEstimationSeries data
  Group /processing/video_event_timestamps_moths/moths_s_1_e_047_timestamps (TimeSeries) empty time series holding analog signal timestamps for video frames/DLC pose estimation that will be associated with PoseEstimationSeries data
  Group /processing/video_event_timestamps_moths/moths_s_1_e_048_timestamps (TimeSeries) empty time series holding analog signal timestamps for video frames/DLC pose estimation that will be associated with PoseEstimationSeries data
  Group /processing/video_event_timestamps_moths/moths_s_1_e_049_timestamps (TimeSeries) empty time series holding analog signal timestamps for video frames/DLC pose estimation that will be associated with PoseEstimationSeries data
  Group /processing/video_event_timestamps_moths/moths_s_1_e_050_timestamps (TimeSeries) empty time series holding analog signal timestamps for video frames/DLC pose estimation that will be associated with PoseEstimationSeries data
  Group /processing/video_event_timestamps_moths/moths_s_1_e_051_timestamps (TimeSeries) empty time series holding analog signal timestamps for video frames/DLC pose estimation that will be associated with PoseEstimationSeries data
  Group /processing/video_event_timestamps_moths/moths_s_1_e_052_timestamps (TimeSeries) empty time series holding analog signal timestamps for video frames/DLC pose estimation that will be associated with PoseEstimationSeries data
  Group /processing/video_event_timestamps_moths/moths_s_1_e_053_timestamps (TimeSeries) empty time series holding analog signal timestamps for video frames/DLC pose estimation that will be associated with PoseEstimationSeries data
  Group /processing/video_event_timestamps_moths/moths_s_1_e_054_timestamps (TimeSeries) empty time series holding analog signal timestamps for video frames/DLC pose estimation that will be associated with PoseEstimationSeries data
  session_description: MG moths and spontaneous behavior
  session_start_time: 2023-04-16T20:08:16-05:00
  timestamps_reference_time: 2023-04-16T20:08:16-05:00
  Group /units (Units) Autogenerated by neuroconv.
  Dataset /units/amp (VectorData) No description. | shape = (81,) | dtype = float64
  Dataset /units/channel_index (VectorData) No description. | shape = (81,) | dtype = float64
  Dataset /units/electrode_label (VectorData) No description. | shape = (81,) | dtype = object
  Dataset /units/fr (VectorData) No description. | shape = (81,) | dtype = float64
  Dataset /units/id (ElementIdentifiers)  | shape = (81,) | dtype = int64
  Dataset /units/isi_violations (VectorData) No description. | shape = (81,) | dtype = float64
  Dataset /units/n_spikes (VectorData) No description. | shape = (81,) | dtype = float64
  Dataset /units/original_cluster_id (VectorData) No description. | shape = (81,) | dtype = float64
  Dataset /units/quality (VectorData) Quality of the unit as defined by phy (good, mua, noise). | shape = (81,) | dtype = object
  Dataset /units/snr (VectorData) The signal-to-noise ratio of the unit. | shape = (81,) | dtype = float64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (18818429,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (81,) | dtype = uint32
  Dataset /units/unit_name (VectorData) Unique reference for each unit. | shape = (81,) | dtype = object
  Dataset /units/x (VectorData) No description. | shape = (81,) | dtype = float64
  Dataset /units/y (VectorData) No description. | shape = (81,) | dtype = float64
  Dataset /units/z (VectorData) No description. | shape = (81,) | dtype = float64
