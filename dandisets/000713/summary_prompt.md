
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000713/0.240702.1725
name: Allen Institute - Visual Behavior - Neuropixels
contributor: [{'name': 'Morrison, Christopher', 'email': 'chris.morrison@alleninstitute.org', 'roleName': ['dcite:DataCurator'], 'schemaKey': 'Person', 'identifier': '0000-0001-9419-3947', 'affiliation': [{'name': 'Allen Institute', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/03cpe7c52'}], 'includeInCitation': False}, {'name': 'Bennett, Corbett', 'email': 'corbettb@alleninstitute.org', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0009-0001-2847-7754', 'includeInCitation': False}]
description: Data released here is for archival purposes. The recommended route for interacting with these data is through the AllenSDK (https://github.com/AllenInstitute/AllenSDK/) which provides methods for downloading and processing data. Documentation of the AllenSDK can be found here: https://allensdk.readthedocs.io/en/latest/. Full documentation of the Visual Behavior Neuropixels dataset and tutorials can be found here: https://allensdk.readthedocs.io/en/latest/visual_behavior_neuropixels.html 
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 4761056388409, 'numberOfFiles': 4293, 'numberOfSubjects': 81, 'variableMeasured': ['ProcessingModule', 'Units', 'ElectricalSeries', 'LFP'], 'measurementTechnique': [{'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'signal filtering technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000713 has 26 NWB files.
5 of these NWB files are of type 1.
6 of these NWB files are of type 2.
6 of these NWB files are of type 3.
4 of these NWB files are of type 4.
5 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/v_in (TimeSeries) The theoretical maximum voltage that the running wheel encoder will reach prior to "wrapping". This should theoretically be 5V (after crossing 5V goes to 0V, or vice versa). In practice the encoder does not always reach this value before wrapping, which can cause transient spikes in speed at the voltage "wraps".
  Group /acquisition/v_sig (TimeSeries) Voltage signal from the running wheel encoder
  file_create_date: ['2023-11-16T15:08:56.378053+00:00']
  Group /general/devices/BEH.G-Box1 (Device) Allen Brain Observatory - Scientifica 2P Rig
  experiment_description: An associative training session where a mouse is automatically rewarded when a grating stimulus changes orientation. Grating stimuli are  full-field, square-wave static gratings with a spatial frequency of 0.04 cycles per degree, with orientation changes between 0 and 90 degrees, at two spatial phases. Delivered rewards are 5ul in volume, and the session lasts for 15 minutes.
  institution: Allen Institute for Brain Science
  keywords: ['visual' 'behavior' 'task']
  Group /general/metadata (BehaviorMetadata) 
  Group /general/subject (BehaviorSubject) 
  Group /general/task_parameters (BehaviorTaskParameters) 
  identifier: 1010991549
  Group /intervals/grating_presentations (TimeIntervals) Presentation times and stimuli details for 'grating' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/grating_presentations/active (VectorData) No description | shape = (123,) | dtype = bool
  Dataset /intervals/grating_presentations/duration (VectorData) No description | shape = (123,) | dtype = float64
  Dataset /intervals/grating_presentations/end_frame (VectorData) No description | shape = (123,) | dtype = int64
  Dataset /intervals/grating_presentations/flashes_since_change (VectorData) No description | shape = (123,) | dtype = int64
  Dataset /intervals/grating_presentations/id (ElementIdentifiers)  | shape = (123,) | dtype = int64
  Dataset /intervals/grating_presentations/image_index (VectorData) No description | shape = (123,) | dtype = int64
  Dataset /intervals/grating_presentations/image_name (VectorData) No description | shape = (123,) | dtype = object
  Dataset /intervals/grating_presentations/image_set (VectorData) No description | shape = (123,) | dtype = object
  Dataset /intervals/grating_presentations/is_change (VectorData) No description | shape = (123,) | dtype = bool
  Dataset /intervals/grating_presentations/is_image_novel (VectorData) No description | shape = (123,) | dtype = bool
  Dataset /intervals/grating_presentations/is_sham_change (VectorData) No description | shape = (123,) | dtype = bool
  Dataset /intervals/grating_presentations/omitted (VectorData) No description | shape = (123,) | dtype = bool
  Dataset /intervals/grating_presentations/orientation (VectorData) Orientation of stimulus | shape = (123,) | dtype = float64
  Dataset /intervals/grating_presentations/phase (VectorData) Phase of grating stimulus | shape = (123,) | dtype = float64
  Dataset /intervals/grating_presentations/spatial_frequency (VectorData) Spatial frequency of stimulus | shape = (123,) | dtype = float64
  Dataset /intervals/grating_presentations/start_frame (VectorData) No description | shape = (123,) | dtype = int64
  Dataset /intervals/grating_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (123,) | dtype = float64
  Dataset /intervals/grating_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (123,) | dtype = int64
  Dataset /intervals/grating_presentations/stimulus_name (VectorData) Name of stimulus | shape = (123,) | dtype = object
  Dataset /intervals/grating_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (123,) | dtype = float64
  Dataset /intervals/grating_presentations/tags (VectorData) user-defined tags | shape = (123,) | dtype = object
  Dataset /intervals/grating_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (123,) | dtype = uint8
  Dataset /intervals/grating_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (123,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/grating_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (123,) | dtype = uint8
  Dataset /intervals/grating_presentations/trials_id (VectorData) No description | shape = (123,) | dtype = int64
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/aborted (VectorData) NOT IMPLEMENTED: aborted | shape = (122,) | dtype = bool
  Dataset /intervals/trials/auto_rewarded (VectorData) NOT IMPLEMENTED: auto_rewarded | shape = (122,) | dtype = bool
  Dataset /intervals/trials/catch (VectorData) NOT IMPLEMENTED: catch | shape = (122,) | dtype = bool
  Dataset /intervals/trials/change_frame (VectorData) NOT IMPLEMENTED: change_frame | shape = (122,) | dtype = int64
  Dataset /intervals/trials/change_image_name (VectorData) NOT IMPLEMENTED: change_image_name | shape = (122,) | dtype = object
  Dataset /intervals/trials/change_time (VectorData) NOT IMPLEMENTED: change_time | shape = (122,) | dtype = float64
  Dataset /intervals/trials/correct_reject (VectorData) NOT IMPLEMENTED: correct_reject | shape = (122,) | dtype = bool
  Dataset /intervals/trials/false_alarm (VectorData) NOT IMPLEMENTED: false_alarm | shape = (122,) | dtype = bool
  Dataset /intervals/trials/go (VectorData) NOT IMPLEMENTED: go | shape = (122,) | dtype = bool
  Dataset /intervals/trials/hit (VectorData) NOT IMPLEMENTED: hit | shape = (122,) | dtype = bool
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (122,) | dtype = int64
  Dataset /intervals/trials/initial_image_name (VectorData) NOT IMPLEMENTED: initial_image_name | shape = (122,) | dtype = object
  Dataset /intervals/trials/is_change (VectorData) NOT IMPLEMENTED: is_change | shape = (122,) | dtype = bool
  Dataset /intervals/trials/lick_times (VectorData) NOT IMPLEMENTED: lick_times | shape = (738,) | dtype = float64
  Dataset /intervals/trials/lick_times_index (VectorIndex) Index for VectorData 'lick_times' | shape = (122,) | dtype = uint16
  Dataset /intervals/trials/miss (VectorData) NOT IMPLEMENTED: miss | shape = (122,) | dtype = bool
  Dataset /intervals/trials/response_latency (VectorData) NOT IMPLEMENTED: response_latency | shape = (122,) | dtype = float64
  Dataset /intervals/trials/response_time (VectorData) NOT IMPLEMENTED: response_time | shape = (122,) | dtype = float64
  Dataset /intervals/trials/reward_time (VectorData) NOT IMPLEMENTED: reward_time | shape = (122,) | dtype = float64
  Dataset /intervals/trials/reward_volume (VectorData) NOT IMPLEMENTED: reward_volume | shape = (122,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (122,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (122,) | dtype = float64
  Dataset /intervals/trials/trial_length (VectorData) NOT IMPLEMENTED: trial_length | shape = (122,) | dtype = float64
  Group /processing/licking (ProcessingModule) Licking behavior processing module
  Group /processing/licking/licks (TimeSeries) Timestamps and stimulus presentation frame indices for lick events
  Group /processing/rewards (ProcessingModule) Licking behavior processing module
  Group /processing/rewards/autorewarded (TimeSeries) no description
  Group /processing/rewards/volume (TimeSeries) no description
  Group /processing/running (ProcessingModule) Running speed processing module
  Group /processing/running/dx (TimeSeries) Running wheel angular change, computed during data collection
  Group /processing/running/speed (TimeSeries) no description
  Group /processing/running/speed_unfiltered (TimeSeries) no description
  Group /processing/stimulus (ProcessingModule) Stimulus Times processing
  Group /processing/stimulus/timestamps (TimeSeries) no description
  session_description: TRAINING_0_gratings_autorewards_15min
  session_start_time: 2020-02-28T11:11:17.576000+00:00
  Group /stimulus/presentation/grating (IndexSeries) no description
  Group /stimulus/presentation/grating/indexed_timeseries (StimulusTemplate) no description
  Group /stimulus/templates/grating (StimulusTemplate) no description
  timestamps_reference_time: 2020-02-28T11:11:17.576000+00:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/v_in (TimeSeries) The theoretical maximum voltage that the running wheel encoder will reach prior to "wrapping". This should theoretically be 5V (after crossing 5V goes to 0V, or vice versa). In practice the encoder does not always reach this value before wrapping, which can cause transient spikes in speed at the voltage "wraps".
  Group /acquisition/v_sig (TimeSeries) Voltage signal from the running wheel encoder
  file_create_date: ['2023-11-16T15:09:01.757742+00:00']
  Group /general/devices/BEH.B-Box1 (Device) Allen Brain Observatory - Scientifica 2P Rig
  experiment_description: An operant behavior training session where a mouse must lick following a change in stimulus identity to earn rewards. Stimuli consist of  full-field, square-wave static gratings with a spatial frequency of 0.04 cycles per degree. Orientation changes between 0 and 90 degrees occur with no intervening gray period. Delivered rewards are 10ul in volume, and the session lasts 60 minutes
  institution: Allen Institute for Brain Science
  keywords: ['visual' 'behavior' 'task']
  Group /general/metadata (BehaviorMetadata) 
  Group /general/subject (BehaviorSubject) 
  Group /general/task_parameters (BehaviorTaskParameters) 
  identifier: 1012862460
  Group /intervals/grating_presentations (TimeIntervals) Presentation times and stimuli details for 'grating' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/grating_presentations/active (VectorData) No description | shape = (87,) | dtype = bool
  Dataset /intervals/grating_presentations/duration (VectorData) No description | shape = (87,) | dtype = float64
  Dataset /intervals/grating_presentations/end_frame (VectorData) No description | shape = (87,) | dtype = int64
  Dataset /intervals/grating_presentations/flashes_since_change (VectorData) No description | shape = (87,) | dtype = int64
  Dataset /intervals/grating_presentations/id (ElementIdentifiers)  | shape = (87,) | dtype = int64
  Dataset /intervals/grating_presentations/image_index (VectorData) No description | shape = (87,) | dtype = int64
  Dataset /intervals/grating_presentations/image_name (VectorData) No description | shape = (87,) | dtype = object
  Dataset /intervals/grating_presentations/image_set (VectorData) No description | shape = (87,) | dtype = object
  Dataset /intervals/grating_presentations/is_change (VectorData) No description | shape = (87,) | dtype = bool
  Dataset /intervals/grating_presentations/is_image_novel (VectorData) No description | shape = (87,) | dtype = bool
  Dataset /intervals/grating_presentations/is_sham_change (VectorData) No description | shape = (87,) | dtype = bool
  Dataset /intervals/grating_presentations/omitted (VectorData) No description | shape = (87,) | dtype = bool
  Dataset /intervals/grating_presentations/orientation (VectorData) Orientation of stimulus | shape = (87,) | dtype = float64
  Dataset /intervals/grating_presentations/phase (VectorData) Phase of grating stimulus | shape = (87,) | dtype = float64
  Dataset /intervals/grating_presentations/spatial_frequency (VectorData) Spatial frequency of stimulus | shape = (87,) | dtype = float64
  Dataset /intervals/grating_presentations/start_frame (VectorData) No description | shape = (87,) | dtype = int64
  Dataset /intervals/grating_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (87,) | dtype = float64
  Dataset /intervals/grating_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (87,) | dtype = int64
  Dataset /intervals/grating_presentations/stimulus_name (VectorData) Name of stimulus | shape = (87,) | dtype = object
  Dataset /intervals/grating_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (87,) | dtype = float64
  Dataset /intervals/grating_presentations/tags (VectorData) user-defined tags | shape = (87,) | dtype = object
  Dataset /intervals/grating_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (87,) | dtype = uint8
  Dataset /intervals/grating_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (87,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/grating_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (87,) | dtype = uint8
  Dataset /intervals/grating_presentations/trials_id (VectorData) No description | shape = (87,) | dtype = int64
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/aborted (VectorData) NOT IMPLEMENTED: aborted | shape = (1286,) | dtype = bool
  Dataset /intervals/trials/auto_rewarded (VectorData) NOT IMPLEMENTED: auto_rewarded | shape = (1286,) | dtype = bool
  Dataset /intervals/trials/catch (VectorData) NOT IMPLEMENTED: catch | shape = (1286,) | dtype = bool
  Dataset /intervals/trials/change_frame (VectorData) NOT IMPLEMENTED: change_frame | shape = (1286,) | dtype = int64
  Dataset /intervals/trials/change_image_name (VectorData) NOT IMPLEMENTED: change_image_name | shape = (1286,) | dtype = object
  Dataset /intervals/trials/change_time (VectorData) NOT IMPLEMENTED: change_time | shape = (1286,) | dtype = float64
  Dataset /intervals/trials/correct_reject (VectorData) NOT IMPLEMENTED: correct_reject | shape = (1286,) | dtype = bool
  Dataset /intervals/trials/false_alarm (VectorData) NOT IMPLEMENTED: false_alarm | shape = (1286,) | dtype = bool
  Dataset /intervals/trials/go (VectorData) NOT IMPLEMENTED: go | shape = (1286,) | dtype = bool
  Dataset /intervals/trials/hit (VectorData) NOT IMPLEMENTED: hit | shape = (1286,) | dtype = bool
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (1286,) | dtype = int64
  Dataset /intervals/trials/initial_image_name (VectorData) NOT IMPLEMENTED: initial_image_name | shape = (1286,) | dtype = object
  Dataset /intervals/trials/is_change (VectorData) NOT IMPLEMENTED: is_change | shape = (1286,) | dtype = bool
  Dataset /intervals/trials/lick_times (VectorData) NOT IMPLEMENTED: lick_times | shape = (3174,) | dtype = float64
  Dataset /intervals/trials/lick_times_index (VectorIndex) Index for VectorData 'lick_times' | shape = (1286,) | dtype = uint16
  Dataset /intervals/trials/miss (VectorData) NOT IMPLEMENTED: miss | shape = (1286,) | dtype = bool
  Dataset /intervals/trials/response_latency (VectorData) NOT IMPLEMENTED: response_latency | shape = (1286,) | dtype = float64
  Dataset /intervals/trials/response_time (VectorData) NOT IMPLEMENTED: response_time | shape = (1286,) | dtype = float64
  Dataset /intervals/trials/reward_time (VectorData) NOT IMPLEMENTED: reward_time | shape = (1286,) | dtype = float64
  Dataset /intervals/trials/reward_volume (VectorData) NOT IMPLEMENTED: reward_volume | shape = (1286,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (1286,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1286,) | dtype = float64
  Dataset /intervals/trials/trial_length (VectorData) NOT IMPLEMENTED: trial_length | shape = (1286,) | dtype = float64
  Group /processing/licking (ProcessingModule) Licking behavior processing module
  Group /processing/licking/licks (TimeSeries) Timestamps and stimulus presentation frame indices for lick events
  Group /processing/rewards (ProcessingModule) Licking behavior processing module
  Group /processing/rewards/autorewarded (TimeSeries) no description
  Group /processing/rewards/volume (TimeSeries) no description
  Group /processing/running (ProcessingModule) Running speed processing module
  Group /processing/running/dx (TimeSeries) Running wheel angular change, computed during data collection
  Group /processing/running/speed (TimeSeries) no description
  Group /processing/running/speed_unfiltered (TimeSeries) no description
  Group /processing/stimulus (ProcessingModule) Stimulus Times processing
  Group /processing/stimulus/timestamps (TimeSeries) no description
  session_description: TRAINING_1_gratings
  session_start_time: 2020-03-06T12:36:40.378000+00:00
  Group /stimulus/presentation/grating (IndexSeries) no description
  Group /stimulus/presentation/grating/indexed_timeseries (StimulusTemplate) no description
  Group /stimulus/templates/grating (StimulusTemplate) no description
  timestamps_reference_time: 2020-03-06T12:36:40.378000+00:00


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/v_in (TimeSeries) The theoretical maximum voltage that the running wheel encoder will reach prior to "wrapping". This should theoretically be 5V (after crossing 5V goes to 0V, or vice versa). In practice the encoder does not always reach this value before wrapping, which can cause transient spikes in speed at the voltage "wraps".
  Group /acquisition/v_sig (TimeSeries) Voltage signal from the running wheel encoder
  file_create_date: ['2023-11-16T15:09:55.223048+00:00']
  Group /general/devices/BEH.B-Box1 (Device) Allen Brain Observatory - Scientifica 2P Rig
  experiment_description: An operant behavior training session where a mouse must lick following a change in stimulus identity to earn rewards. Stimuli consist of 8 natural scene images, for a total of 64 possible pairwise transitions. Images are shown for 250 ms with a 500 ms intervening gray period. Delivered rewards are 10ul in volume, and the session lasts for 60 minutes
  institution: Allen Institute for Brain Science
  keywords: ['visual' 'behavior' 'task']
  Group /general/metadata (BehaviorMetadata) 
  Group /general/subject (BehaviorSubject) 
  Group /general/task_parameters (BehaviorTaskParameters) 
  identifier: 1014456264
  Group /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations (TimeIntervals) Presentation times and stimuli details for 'Natural_Images_Lum_Matched_set_ophys_G_2019' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/active (VectorData) No description | shape = (4804,) | dtype = bool
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/duration (VectorData) No description | shape = (4804,) | dtype = float64
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/end_frame (VectorData) No description | shape = (4804,) | dtype = int64
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/flashes_since_change (VectorData) No description | shape = (4804,) | dtype = int64
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/id (ElementIdentifiers)  | shape = (4804,) | dtype = int64
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/image_index (VectorData) No description | shape = (4804,) | dtype = int64
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/image_name (VectorData) No description | shape = (4804,) | dtype = object
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/image_set (VectorData) No description | shape = (4804,) | dtype = object
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/is_change (VectorData) No description | shape = (4804,) | dtype = bool
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/is_image_novel (VectorData) No description | shape = (4804,) | dtype = bool
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/is_sham_change (VectorData) No description | shape = (4804,) | dtype = bool
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/omitted (VectorData) No description | shape = (4804,) | dtype = bool
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/start_frame (VectorData) No description | shape = (4804,) | dtype = int64
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (4804,) | dtype = float64
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (4804,) | dtype = int64
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/stimulus_name (VectorData) Name of stimulus | shape = (4804,) | dtype = object
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (4804,) | dtype = float64
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/tags (VectorData) user-defined tags | shape = (4804,) | dtype = object
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (4804,) | dtype = uint16
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (4804,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (4804,) | dtype = uint16
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/trials_id (VectorData) No description | shape = (4804,) | dtype = int64
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/aborted (VectorData) NOT IMPLEMENTED: aborted | shape = (837,) | dtype = bool
  Dataset /intervals/trials/auto_rewarded (VectorData) NOT IMPLEMENTED: auto_rewarded | shape = (837,) | dtype = bool
  Dataset /intervals/trials/catch (VectorData) NOT IMPLEMENTED: catch | shape = (837,) | dtype = bool
  Dataset /intervals/trials/change_frame (VectorData) NOT IMPLEMENTED: change_frame | shape = (837,) | dtype = int64
  Dataset /intervals/trials/change_image_name (VectorData) NOT IMPLEMENTED: change_image_name | shape = (837,) | dtype = object
  Dataset /intervals/trials/change_time (VectorData) NOT IMPLEMENTED: change_time | shape = (837,) | dtype = float64
  Dataset /intervals/trials/correct_reject (VectorData) NOT IMPLEMENTED: correct_reject | shape = (837,) | dtype = bool
  Dataset /intervals/trials/false_alarm (VectorData) NOT IMPLEMENTED: false_alarm | shape = (837,) | dtype = bool
  Dataset /intervals/trials/go (VectorData) NOT IMPLEMENTED: go | shape = (837,) | dtype = bool
  Dataset /intervals/trials/hit (VectorData) NOT IMPLEMENTED: hit | shape = (837,) | dtype = bool
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (837,) | dtype = int64
  Dataset /intervals/trials/initial_image_name (VectorData) NOT IMPLEMENTED: initial_image_name | shape = (837,) | dtype = object
  Dataset /intervals/trials/is_change (VectorData) NOT IMPLEMENTED: is_change | shape = (837,) | dtype = bool
  Dataset /intervals/trials/lick_times (VectorData) NOT IMPLEMENTED: lick_times | shape = (2517,) | dtype = float64
  Dataset /intervals/trials/lick_times_index (VectorIndex) Index for VectorData 'lick_times' | shape = (837,) | dtype = uint16
  Dataset /intervals/trials/miss (VectorData) NOT IMPLEMENTED: miss | shape = (837,) | dtype = bool
  Dataset /intervals/trials/response_latency (VectorData) NOT IMPLEMENTED: response_latency | shape = (837,) | dtype = float64
  Dataset /intervals/trials/response_time (VectorData) NOT IMPLEMENTED: response_time | shape = (837,) | dtype = float64
  Dataset /intervals/trials/reward_time (VectorData) NOT IMPLEMENTED: reward_time | shape = (837,) | dtype = float64
  Dataset /intervals/trials/reward_volume (VectorData) NOT IMPLEMENTED: reward_volume | shape = (837,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (837,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (837,) | dtype = float64
  Dataset /intervals/trials/trial_length (VectorData) NOT IMPLEMENTED: trial_length | shape = (837,) | dtype = float64
  Group /processing/licking (ProcessingModule) Licking behavior processing module
  Group /processing/licking/licks (TimeSeries) Timestamps and stimulus presentation frame indices for lick events
  Group /processing/rewards (ProcessingModule) Licking behavior processing module
  Group /processing/rewards/autorewarded (TimeSeries) no description
  Group /processing/rewards/volume (TimeSeries) no description
  Group /processing/running (ProcessingModule) Running speed processing module
  Group /processing/running/dx (TimeSeries) Running wheel angular change, computed during data collection
  Group /processing/running/speed (TimeSeries) no description
  Group /processing/running/speed_unfiltered (TimeSeries) no description
  Group /processing/stimulus (ProcessingModule) Stimulus Times processing
  Group /processing/stimulus/timestamps (TimeSeries) no description
  session_description: TRAINING_3_images_G_10uL_reward
  session_start_time: 2020-03-16T15:16:25.163000+00:00
  Group /stimulus/presentation/Natural_Images_Lum_Matched_set_ophys_G_2019.05.26 (IndexSeries) no description
  Group /stimulus/presentation/Natural_Images_Lum_Matched_set_ophys_G_2019.05.26/indexed_timeseries (StimulusTemplate) no description
  Group /stimulus/templates/Natural_Images_Lum_Matched_set_ophys_G_2019.05.26 (StimulusTemplate) no description
  timestamps_reference_time: 2020-03-16T15:16:25.163000+00:00


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/v_in (TimeSeries) The theoretical maximum voltage that the running wheel encoder will reach prior to "wrapping". This should theoretically be 5V (after crossing 5V goes to 0V, or vice versa). In practice the encoder does not always reach this value before wrapping, which can cause transient spikes in speed at the voltage "wraps".
  Group /acquisition/v_sig (TimeSeries) Voltage signal from the running wheel encoder
  file_create_date: ['2023-11-16T16:02:20.717023+00:00']
  Group /general/devices/NP.1 (Device) Allen Brain Observatory - Scientifica 2P Rig
  institution: Allen Institute for Brain Science
  keywords: ['visual' 'behavior' 'task']
  Group /general/metadata (BehaviorMetadata) 
  Group /general/subject (BehaviorSubject) 
  Group /general/task_parameters (BehaviorTaskParameters) 
  identifier: 1040882886
  Group /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations (TimeIntervals) Presentation times and stimuli details for 'Natural_Images_Lum_Matched_set_ophys_G_2019' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/active (VectorData) No description | shape = (4803,) | dtype = bool
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/duration (VectorData) No description | shape = (4803,) | dtype = float64
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/end_frame (VectorData) No description | shape = (4803,) | dtype = int64
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/flashes_since_change (VectorData) No description | shape = (4803,) | dtype = int64
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/id (ElementIdentifiers)  | shape = (4803,) | dtype = int64
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/image_index (VectorData) No description | shape = (4803,) | dtype = int64
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/image_name (VectorData) No description | shape = (4803,) | dtype = object
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/image_set (VectorData) No description | shape = (4803,) | dtype = object
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/is_change (VectorData) No description | shape = (4803,) | dtype = bool
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/is_image_novel (VectorData) No description | shape = (4803,) | dtype = bool
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/is_sham_change (VectorData) No description | shape = (4803,) | dtype = bool
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/omitted (VectorData) No description | shape = (4803,) | dtype = bool
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/start_frame (VectorData) No description | shape = (4803,) | dtype = int64
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (4803,) | dtype = float64
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (4803,) | dtype = int64
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/stimulus_name (VectorData) Name of stimulus | shape = (4803,) | dtype = object
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (4803,) | dtype = float64
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/tags (VectorData) user-defined tags | shape = (4803,) | dtype = object
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (4803,) | dtype = uint16
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (4803,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (4803,) | dtype = uint16
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/trials_id (VectorData) No description | shape = (4803,) | dtype = int64
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/aborted (VectorData) NOT IMPLEMENTED: aborted | shape = (712,) | dtype = bool
  Dataset /intervals/trials/auto_rewarded (VectorData) NOT IMPLEMENTED: auto_rewarded | shape = (712,) | dtype = bool
  Dataset /intervals/trials/catch (VectorData) NOT IMPLEMENTED: catch | shape = (712,) | dtype = bool
  Dataset /intervals/trials/change_frame (VectorData) NOT IMPLEMENTED: change_frame | shape = (712,) | dtype = int64
  Dataset /intervals/trials/change_image_name (VectorData) NOT IMPLEMENTED: change_image_name | shape = (712,) | dtype = object
  Dataset /intervals/trials/change_time (VectorData) NOT IMPLEMENTED: change_time | shape = (712,) | dtype = float64
  Dataset /intervals/trials/correct_reject (VectorData) NOT IMPLEMENTED: correct_reject | shape = (712,) | dtype = bool
  Dataset /intervals/trials/false_alarm (VectorData) NOT IMPLEMENTED: false_alarm | shape = (712,) | dtype = bool
  Dataset /intervals/trials/go (VectorData) NOT IMPLEMENTED: go | shape = (712,) | dtype = bool
  Dataset /intervals/trials/hit (VectorData) NOT IMPLEMENTED: hit | shape = (712,) | dtype = bool
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (712,) | dtype = int64
  Dataset /intervals/trials/initial_image_name (VectorData) NOT IMPLEMENTED: initial_image_name | shape = (712,) | dtype = object
  Dataset /intervals/trials/is_change (VectorData) NOT IMPLEMENTED: is_change | shape = (712,) | dtype = bool
  Dataset /intervals/trials/lick_times (VectorData) NOT IMPLEMENTED: lick_times | shape = (786,) | dtype = float64
  Dataset /intervals/trials/lick_times_index (VectorIndex) Index for VectorData 'lick_times' | shape = (712,) | dtype = uint16
  Dataset /intervals/trials/miss (VectorData) NOT IMPLEMENTED: miss | shape = (712,) | dtype = bool
  Dataset /intervals/trials/response_latency (VectorData) NOT IMPLEMENTED: response_latency | shape = (712,) | dtype = float64
  Dataset /intervals/trials/response_time (VectorData) NOT IMPLEMENTED: response_time | shape = (712,) | dtype = float64
  Dataset /intervals/trials/reward_time (VectorData) NOT IMPLEMENTED: reward_time | shape = (712,) | dtype = float64
  Dataset /intervals/trials/reward_volume (VectorData) NOT IMPLEMENTED: reward_volume | shape = (712,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (712,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (712,) | dtype = float64
  Dataset /intervals/trials/trial_length (VectorData) NOT IMPLEMENTED: trial_length | shape = (712,) | dtype = float64
  Group /processing/licking (ProcessingModule) Licking behavior processing module
  Group /processing/licking/licks (TimeSeries) Timestamps and stimulus presentation frame indices for lick events
  Group /processing/rewards (ProcessingModule) Licking behavior processing module
  Group /processing/rewards/autorewarded (TimeSeries) no description
  Group /processing/rewards/volume (TimeSeries) no description
  Group /processing/running (ProcessingModule) Running speed processing module
  Group /processing/running/dx (TimeSeries) Running wheel angular change, computed during data collection
  Group /processing/running/speed (TimeSeries) no description
  Group /processing/running/speed_unfiltered (TimeSeries) no description
  Group /processing/stimulus (ProcessingModule) Stimulus Times processing
  Group /processing/stimulus/timestamps (TimeSeries) no description
  session_description: HABITUATION_5_images_G_handoff_ready_5uL_reward
  session_start_time: 2020-08-04T16:30:32.835000+00:00
  Group /stimulus/presentation/Natural_Images_Lum_Matched_set_ophys_G_2019.05.26 (IndexSeries) no description
  Group /stimulus/presentation/Natural_Images_Lum_Matched_set_ophys_G_2019.05.26/indexed_timeseries (StimulusTemplate) no description
  Group /stimulus/templates/Natural_Images_Lum_Matched_set_ophys_G_2019.05.26 (StimulusTemplate) no description
  timestamps_reference_time: 2020-08-04T16:30:32.835000+00:00


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  Group /acquisition/v_in (TimeSeries) The theoretical maximum voltage that the running wheel encoder will reach prior to "wrapping". This should theoretically be 5V (after crossing 5V goes to 0V, or vice versa). In practice the encoder does not always reach this value before wrapping, which can cause transient spikes in speed at the voltage "wraps".
  Group /acquisition/v_sig (TimeSeries) Voltage signal from the running wheel encoder
  file_create_date: ['2023-11-16T16:06:59.181994+00:00']
  Group /general/devices/NP.0 (Device) Allen Brain Observatory - Scientifica 2P Rig
  institution: Allen Institute for Brain Science
  keywords: ['visual' 'behavior' 'task']
  Group /general/metadata (BehaviorMetadata) 
  Group /general/subject (BehaviorSubject) 
  Group /general/task_parameters (BehaviorTaskParameters) 
  identifier: 1041487615
  Group /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations (TimeIntervals) Presentation times and stimuli details for 'Natural_Images_Lum_Matched_set_ophys_G_2019' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/active (VectorData) No description | shape = (4797,) | dtype = bool
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/duration (VectorData) No description | shape = (4797,) | dtype = float64
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/end_frame (VectorData) No description | shape = (4797,) | dtype = int64
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/flashes_since_change (VectorData) No description | shape = (4797,) | dtype = int64
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/id (ElementIdentifiers)  | shape = (4797,) | dtype = int64
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/image_index (VectorData) No description | shape = (4797,) | dtype = int64
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/image_name (VectorData) No description | shape = (4797,) | dtype = object
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/image_set (VectorData) No description | shape = (4797,) | dtype = object
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/is_change (VectorData) No description | shape = (4797,) | dtype = bool
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/is_image_novel (VectorData) No description | shape = (4797,) | dtype = bool
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/is_sham_change (VectorData) No description | shape = (4797,) | dtype = bool
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/omitted (VectorData) No description | shape = (4797,) | dtype = bool
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/start_frame (VectorData) No description | shape = (4797,) | dtype = int64
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (4797,) | dtype = float64
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (4797,) | dtype = int64
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/stimulus_name (VectorData) Name of stimulus | shape = (4797,) | dtype = object
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (4797,) | dtype = float64
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/tags (VectorData) user-defined tags | shape = (4797,) | dtype = object
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (4797,) | dtype = uint16
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (4797,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (4797,) | dtype = uint16
  Dataset /intervals/Natural_Images_Lum_Matched_set_ophys_G_2019_presentations/trials_id (VectorData) No description | shape = (4797,) | dtype = int64
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/aborted (VectorData) NOT IMPLEMENTED: aborted | shape = (583,) | dtype = bool
  Dataset /intervals/trials/auto_rewarded (VectorData) NOT IMPLEMENTED: auto_rewarded | shape = (583,) | dtype = bool
  Dataset /intervals/trials/catch (VectorData) NOT IMPLEMENTED: catch | shape = (583,) | dtype = bool
  Dataset /intervals/trials/change_frame (VectorData) NOT IMPLEMENTED: change_frame | shape = (583,) | dtype = int64
  Dataset /intervals/trials/change_image_name (VectorData) NOT IMPLEMENTED: change_image_name | shape = (583,) | dtype = object
  Dataset /intervals/trials/change_time (VectorData) NOT IMPLEMENTED: change_time | shape = (583,) | dtype = float64
  Dataset /intervals/trials/correct_reject (VectorData) NOT IMPLEMENTED: correct_reject | shape = (583,) | dtype = bool
  Dataset /intervals/trials/false_alarm (VectorData) NOT IMPLEMENTED: false_alarm | shape = (583,) | dtype = bool
  Dataset /intervals/trials/go (VectorData) NOT IMPLEMENTED: go | shape = (583,) | dtype = bool
  Dataset /intervals/trials/hit (VectorData) NOT IMPLEMENTED: hit | shape = (583,) | dtype = bool
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (583,) | dtype = int64
  Dataset /intervals/trials/initial_image_name (VectorData) NOT IMPLEMENTED: initial_image_name | shape = (583,) | dtype = object
  Dataset /intervals/trials/is_change (VectorData) NOT IMPLEMENTED: is_change | shape = (583,) | dtype = bool
  Dataset /intervals/trials/lick_times (VectorData) NOT IMPLEMENTED: lick_times | shape = (832,) | dtype = float64
  Dataset /intervals/trials/lick_times_index (VectorIndex) Index for VectorData 'lick_times' | shape = (583,) | dtype = uint16
  Dataset /intervals/trials/miss (VectorData) NOT IMPLEMENTED: miss | shape = (583,) | dtype = bool
  Dataset /intervals/trials/response_latency (VectorData) NOT IMPLEMENTED: response_latency | shape = (583,) | dtype = float64
  Dataset /intervals/trials/response_time (VectorData) NOT IMPLEMENTED: response_time | shape = (583,) | dtype = float64
  Dataset /intervals/trials/reward_time (VectorData) NOT IMPLEMENTED: reward_time | shape = (583,) | dtype = float64
  Dataset /intervals/trials/reward_volume (VectorData) NOT IMPLEMENTED: reward_volume | shape = (583,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (583,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (583,) | dtype = float64
  Dataset /intervals/trials/trial_length (VectorData) NOT IMPLEMENTED: trial_length | shape = (583,) | dtype = float64
  Group /processing/licking (ProcessingModule) Licking behavior processing module
  Group /processing/licking/licks (TimeSeries) Timestamps and stimulus presentation frame indices for lick events
  Group /processing/rewards (ProcessingModule) Licking behavior processing module
  Group /processing/rewards/autorewarded (TimeSeries) no description
  Group /processing/rewards/volume (TimeSeries) no description
  Group /processing/running (ProcessingModule) Running speed processing module
  Group /processing/running/dx (TimeSeries) Running wheel angular change, computed during data collection
  Group /processing/running/speed (TimeSeries) no description
  Group /processing/running/speed_unfiltered (TimeSeries) no description
  Group /processing/stimulus (ProcessingModule) Stimulus Times processing
  Group /processing/stimulus/timestamps (TimeSeries) no description
  session_description: HABITUATION_5_images_G_handoff_ready_5uL_reward
  session_start_time: 2020-08-07T11:46:28.205000+00:00
  Group /stimulus/presentation/Natural_Images_Lum_Matched_set_ophys_G_2019.05.26 (IndexSeries) no description
  Group /stimulus/presentation/Natural_Images_Lum_Matched_set_ophys_G_2019.05.26/indexed_timeseries (StimulusTemplate) no description
  Group /stimulus/templates/Natural_Images_Lum_Matched_set_ophys_G_2019.05.26 (StimulusTemplate) no description
  timestamps_reference_time: 2020-08-07T11:46:28.205000+00:00
