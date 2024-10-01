
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000711/0.231121.1730
name: Allen Institute - Visual Behavior - Optical Physiology
contributor: [{'url': 'http://alleninstitute.org/', 'name': 'Allen Institute for Brain Science', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/00dcv1019', 'contactPoint': [], 'includeInCitation': True}, {'name': 'Olsen, Shawn', 'email': 'shawno@alleninstitute.org', 'roleName': ['dcite:Conceptualization', 'dcite:ProjectLeader', 'dcite:Supervision', 'dcite:Resources'], 'schemaKey': 'Person', 'identifier': '0000-0002-9568-7057', 'affiliation': [{'name': 'Allen Institute', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/03cpe7c52'}], 'includeInCitation': True}, {'name': 'Morrison, Christopher', 'email': 'chris.morrison@alleninstitute.org', 'roleName': ['dcite:DataCurator'], 'schemaKey': 'Person', 'identifier': '0000-0001-9419-3947', 'affiliation': [{'name': 'Allen Institute', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/03cpe7c52'}], 'includeInCitation': False}, {'name': 'Garrett, Marina', 'email': 'marinag@alleninstitute.org', 'roleName': ['dcite:Conceptualization', 'dcite:ProjectLeader', 'dcite:Validation', 'dcite:DataCurator', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0002-5271-2291', 'affiliation': [{'name': 'Allen Institute', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/03cpe7c52'}], 'includeInCitation': True}, {'name': 'Groblewski, Peter', 'email': 'peterg@alleninstitute.org', 'roleName': ['dcite:Conceptualization', 'dcite:ProjectLeader', 'dcite:Supervision', 'dcite:ProjectAdministration'], 'schemaKey': 'Person', 'identifier': '0000-0002-6529-1414', 'affiliation': [{'name': 'Allen Institute', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/03cpe7c52'}], 'includeInCitation': True}]
description: The Visual Behavior Ophys dataset was generated using in vivo 2-photon calcium imaging (also called optical physiology, or “ophys”) to measure the activity of genetically identified neurons in the visual cortex of mice performing a go/no-go visual change detection task. Population of neurons were recorded over multiple days with varying sensory and behavioral contexts, including familiar and novel stimuli, and passive exposure sessions. This dataset can be used to evaluate the influence of experience, expectation, and task engagement on neural coding and dynamics in excitatory, Vip inhibitory, and Sst inhibitory cell populations. 

The full ophys dataset includes neural and behavioral measurements from 107 well-trained mice during 703 in vivo 2-photon imaging sessions from 326 unique fields of view, resulting in a total of 50,476 cortical neurons recorded. The full behavioral training history of all imaged mice is also provided as part of the dataset, allowing investigation into task learning, behavioral strategy, and inter-animal variability. There are a total of 4,782 behavior sessions available for analysis.

Full documentation of the Visual Behavior Ophys dataset and tutorials can be found here: https://allensdk.readthedocs.io/en/latest/visual_behavior_optical_physiology.html

The recommended route for interacting with these data is through the AllenSDK (https://github.com/AllenInstitute/AllenSDK/) which provides methods for downloading and processing data. Documentation of the AllenSDK can be found here: https://allensdk.readthedocs.io/en/latest/. 

There are several metadata summary tables that are available as "related resources" associated with this DANDI-set. You can also use the AllenSDK to download these tables. See this notebook (https://allensdk.readthedocs.io/en/latest/_static/examples/nb/visual_behavior_ophys_data_access.html) for information on downloading the metadata and the associated NWB files.

Publicly available pre-prints using this dataset include: 

Stimulus novelty uncovers coding diversity in visual cortical circuits
https://doi.org/10.1101/2023.02.14.528085 

Behavioral strategy shapes activation of the Vip-Sst disinhibitory circuit in visual cortex
https://doi.org/10.1101/2023.04.28.538575 

Familiarity modulated synapses model visual cortical circuit novelty responses
https://doi.org/10.1101/2023.08.16.553635 
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 1508058148534, 'numberOfFiles': 6015, 'numberOfSubjects': 107, 'variableMeasured': ['ProcessingModule', 'ImagingPlane', 'PlaneSegmentation', 'OpticalChannel'], 'measurementTechnique': [{'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000711 has 40 NWB files.
9 of these NWB files are of type 1.
6 of these NWB files are of type 2.
5 of these NWB files are of type 3.
4 of these NWB files are of type 4.
16 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/v_in (TimeSeries) The theoretical maximum voltage that the running wheel encoder will reach prior to "wrapping". This should theoretically be 5V (after crossing 5V goes to 0V, or vice versa). In practice the encoder does not always reach this value before wrapping, which can cause transient spikes in speed at the voltage "wraps".
  Group /acquisition/v_sig (TimeSeries) Voltage signal from the running wheel encoder
  file_create_date: ['2023-09-15T13:06:17.199802+00:00']
  Group /general/devices/BEH.F-Box1 (Device) Allen Brain Observatory - Scientifica 2P Rig
  experiment_description: An associative training session where a mouse is automatically rewarded when a grating stimulus changes orientation. Grating stimuli are  full-field, square-wave static gratings with a spatial frequency of 0.04 cycles per degree, with orientation changes between 0 and 90 degrees, at two spatial phases. Delivered rewards are 5ul in volume, and the session lasts for 15 minutes.
  institution: Allen Institute for Brain Science
  keywords: ['visual' 'behavior' 'task']
  Group /general/metadata (BehaviorMetadata) 
  Group /general/subject (BehaviorSubject) 
  Group /general/task_parameters (BehaviorTaskParameters) 
  identifier: 742008131
  Group /intervals/grating_presentations (TimeIntervals) Presentation times and stimuli details for 'grating' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/grating_presentations/active (VectorData) No description | shape = (110,) | dtype = bool
  Dataset /intervals/grating_presentations/duration (VectorData) No description | shape = (110,) | dtype = float64
  Dataset /intervals/grating_presentations/end_frame (VectorData) No description | shape = (110,) | dtype = int64
  Dataset /intervals/grating_presentations/flashes_since_change (VectorData) No description | shape = (110,) | dtype = int64
  Dataset /intervals/grating_presentations/id (ElementIdentifiers)  | shape = (110,) | dtype = int64
  Dataset /intervals/grating_presentations/image_index (VectorData) No description | shape = (110,) | dtype = int64
  Dataset /intervals/grating_presentations/image_name (VectorData) No description | shape = (110,) | dtype = object
  Dataset /intervals/grating_presentations/image_set (VectorData) No description | shape = (110,) | dtype = object
  Dataset /intervals/grating_presentations/is_change (VectorData) No description | shape = (110,) | dtype = bool
  Dataset /intervals/grating_presentations/is_image_novel (VectorData) No description | shape = (110,) | dtype = bool
  Dataset /intervals/grating_presentations/is_sham_change (VectorData) No description | shape = (110,) | dtype = bool
  Dataset /intervals/grating_presentations/omitted (VectorData) No description | shape = (110,) | dtype = bool
  Dataset /intervals/grating_presentations/orientation (VectorData) Orientation of stimulus | shape = (110,) | dtype = float64
  Dataset /intervals/grating_presentations/phase (VectorData) Phase of grating stimulus | shape = (110,) | dtype = float64
  Dataset /intervals/grating_presentations/spatial_frequency (VectorData) Spatial frequency of stimulus | shape = (110,) | dtype = float64
  Dataset /intervals/grating_presentations/start_frame (VectorData) No description | shape = (110,) | dtype = int64
  Dataset /intervals/grating_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (110,) | dtype = float64
  Dataset /intervals/grating_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (110,) | dtype = int64
  Dataset /intervals/grating_presentations/stimulus_block_name (VectorData) No description | shape = (110,) | dtype = object
  Dataset /intervals/grating_presentations/stimulus_name (VectorData) Name of stimulus | shape = (110,) | dtype = object
  Dataset /intervals/grating_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (110,) | dtype = float64
  Dataset /intervals/grating_presentations/tags (VectorData) user-defined tags | shape = (110,) | dtype = object
  Dataset /intervals/grating_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (110,) | dtype = uint8
  Dataset /intervals/grating_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (110,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/grating_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (110,) | dtype = uint8
  Dataset /intervals/grating_presentations/trials_id (VectorData) No description | shape = (110,) | dtype = int64
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/aborted (VectorData) NOT IMPLEMENTED: aborted | shape = (109,) | dtype = bool
  Dataset /intervals/trials/auto_rewarded (VectorData) NOT IMPLEMENTED: auto_rewarded | shape = (109,) | dtype = bool
  Dataset /intervals/trials/catch (VectorData) NOT IMPLEMENTED: catch | shape = (109,) | dtype = bool
  Dataset /intervals/trials/change_frame (VectorData) NOT IMPLEMENTED: change_frame | shape = (109,) | dtype = int64
  Dataset /intervals/trials/change_image_name (VectorData) NOT IMPLEMENTED: change_image_name | shape = (109,) | dtype = object
  Dataset /intervals/trials/change_time (VectorData) NOT IMPLEMENTED: change_time | shape = (109,) | dtype = float64
  Dataset /intervals/trials/correct_reject (VectorData) NOT IMPLEMENTED: correct_reject | shape = (109,) | dtype = bool
  Dataset /intervals/trials/false_alarm (VectorData) NOT IMPLEMENTED: false_alarm | shape = (109,) | dtype = bool
  Dataset /intervals/trials/go (VectorData) NOT IMPLEMENTED: go | shape = (109,) | dtype = bool
  Dataset /intervals/trials/hit (VectorData) NOT IMPLEMENTED: hit | shape = (109,) | dtype = bool
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (109,) | dtype = int64
  Dataset /intervals/trials/initial_image_name (VectorData) NOT IMPLEMENTED: initial_image_name | shape = (109,) | dtype = object
  Dataset /intervals/trials/is_change (VectorData) NOT IMPLEMENTED: is_change | shape = (109,) | dtype = bool
  Dataset /intervals/trials/lick_times (VectorData) NOT IMPLEMENTED: lick_times | shape = (1900,) | dtype = float64
  Dataset /intervals/trials/lick_times_index (VectorIndex) Index for VectorData 'lick_times' | shape = (109,) | dtype = uint16
  Dataset /intervals/trials/miss (VectorData) NOT IMPLEMENTED: miss | shape = (109,) | dtype = bool
  Dataset /intervals/trials/response_latency (VectorData) NOT IMPLEMENTED: response_latency | shape = (109,) | dtype = float64
  Dataset /intervals/trials/response_time (VectorData) NOT IMPLEMENTED: response_time | shape = (109,) | dtype = float64
  Dataset /intervals/trials/reward_time (VectorData) NOT IMPLEMENTED: reward_time | shape = (109,) | dtype = float64
  Dataset /intervals/trials/reward_volume (VectorData) NOT IMPLEMENTED: reward_volume | shape = (109,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (109,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (109,) | dtype = float64
  Dataset /intervals/trials/trial_length (VectorData) NOT IMPLEMENTED: trial_length | shape = (109,) | dtype = float64
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
  session_start_time: 2018-08-24T14:51:25.667000+00:00
  Group /stimulus/presentation/grating (IndexSeries) no description
  Group /stimulus/presentation/grating/indexed_timeseries (StimulusTemplate) no description
  Group /stimulus/templates/grating (StimulusTemplate) no description
  timestamps_reference_time: 2018-08-24T14:51:25.667000+00:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/v_in (TimeSeries) The theoretical maximum voltage that the running wheel encoder will reach prior to "wrapping". This should theoretically be 5V (after crossing 5V goes to 0V, or vice versa). In practice the encoder does not always reach this value before wrapping, which can cause transient spikes in speed at the voltage "wraps".
  Group /acquisition/v_sig (TimeSeries) Voltage signal from the running wheel encoder
  file_create_date: ['2023-09-15T13:08:00.443449+00:00']
  Group /general/devices/BEH.F-Box1 (Device) Allen Brain Observatory - Scientifica 2P Rig
  experiment_description: An operant behavior training session where a mouse must lick following a change in stimulus identity to earn rewards. Stimuli consist of 8 natural scene images, for a total of 64 possible pairwise transitions. Images are shown for 250 ms with a 500 ms intervening gray period. Delivered rewards are 10ul in volume, and the session lasts for 60 minutes
  institution: Allen Institute for Brain Science
  keywords: ['visual' 'behavior' 'task']
  Group /general/metadata (BehaviorMetadata) 
  Group /general/subject (BehaviorSubject) 
  Group /general/task_parameters (BehaviorTaskParameters) 
  identifier: 746928360
  Group /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations (TimeIntervals) Presentation times and stimuli details for 'Natural_Images_Lum_Matched_set_training_2017' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/active (VectorData) No description | shape = (4799,) | dtype = bool
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/duration (VectorData) No description | shape = (4799,) | dtype = float64
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/end_frame (VectorData) No description | shape = (4799,) | dtype = int64
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/flashes_since_change (VectorData) No description | shape = (4799,) | dtype = int64
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/id (ElementIdentifiers)  | shape = (4799,) | dtype = int64
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/image_index (VectorData) No description | shape = (4799,) | dtype = int64
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/image_name (VectorData) No description | shape = (4799,) | dtype = object
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/image_set (VectorData) No description | shape = (4799,) | dtype = object
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/is_change (VectorData) No description | shape = (4799,) | dtype = bool
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/is_image_novel (VectorData) No description | shape = (4799,) | dtype = bool
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/is_sham_change (VectorData) No description | shape = (4799,) | dtype = bool
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/omitted (VectorData) No description | shape = (4799,) | dtype = bool
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/start_frame (VectorData) No description | shape = (4799,) | dtype = int64
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (4799,) | dtype = float64
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (4799,) | dtype = int64
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/stimulus_block_name (VectorData) No description | shape = (4799,) | dtype = object
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/stimulus_name (VectorData) Name of stimulus | shape = (4799,) | dtype = object
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (4799,) | dtype = float64
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/tags (VectorData) user-defined tags | shape = (4799,) | dtype = object
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (4799,) | dtype = uint16
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (4799,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (4799,) | dtype = uint16
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/trials_id (VectorData) No description | shape = (4799,) | dtype = int64
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/aborted (VectorData) NOT IMPLEMENTED: aborted | shape = (721,) | dtype = bool
  Dataset /intervals/trials/auto_rewarded (VectorData) NOT IMPLEMENTED: auto_rewarded | shape = (721,) | dtype = bool
  Dataset /intervals/trials/catch (VectorData) NOT IMPLEMENTED: catch | shape = (721,) | dtype = bool
  Dataset /intervals/trials/change_frame (VectorData) NOT IMPLEMENTED: change_frame | shape = (721,) | dtype = int64
  Dataset /intervals/trials/change_image_name (VectorData) NOT IMPLEMENTED: change_image_name | shape = (721,) | dtype = object
  Dataset /intervals/trials/change_time (VectorData) NOT IMPLEMENTED: change_time | shape = (721,) | dtype = float64
  Dataset /intervals/trials/correct_reject (VectorData) NOT IMPLEMENTED: correct_reject | shape = (721,) | dtype = bool
  Dataset /intervals/trials/false_alarm (VectorData) NOT IMPLEMENTED: false_alarm | shape = (721,) | dtype = bool
  Dataset /intervals/trials/go (VectorData) NOT IMPLEMENTED: go | shape = (721,) | dtype = bool
  Dataset /intervals/trials/hit (VectorData) NOT IMPLEMENTED: hit | shape = (721,) | dtype = bool
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (721,) | dtype = int64
  Dataset /intervals/trials/initial_image_name (VectorData) NOT IMPLEMENTED: initial_image_name | shape = (721,) | dtype = object
  Dataset /intervals/trials/is_change (VectorData) NOT IMPLEMENTED: is_change | shape = (721,) | dtype = bool
  Dataset /intervals/trials/lick_times (VectorData) NOT IMPLEMENTED: lick_times | shape = (1764,) | dtype = float64
  Dataset /intervals/trials/lick_times_index (VectorIndex) Index for VectorData 'lick_times' | shape = (721,) | dtype = uint16
  Dataset /intervals/trials/miss (VectorData) NOT IMPLEMENTED: miss | shape = (721,) | dtype = bool
  Dataset /intervals/trials/response_latency (VectorData) NOT IMPLEMENTED: response_latency | shape = (721,) | dtype = float64
  Dataset /intervals/trials/response_time (VectorData) NOT IMPLEMENTED: response_time | shape = (721,) | dtype = float64
  Dataset /intervals/trials/reward_time (VectorData) NOT IMPLEMENTED: reward_time | shape = (721,) | dtype = float64
  Dataset /intervals/trials/reward_volume (VectorData) NOT IMPLEMENTED: reward_volume | shape = (721,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (721,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (721,) | dtype = float64
  Dataset /intervals/trials/trial_length (VectorData) NOT IMPLEMENTED: trial_length | shape = (721,) | dtype = float64
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
  session_description: TRAINING_3_images_A_10uL_reward
  session_start_time: 2018-09-07T13:25:12.176000+00:00
  Group /stimulus/presentation/Natural_Images_Lum_Matched_set_training_2017.07.14 (IndexSeries) no description
  Group /stimulus/presentation/Natural_Images_Lum_Matched_set_training_2017.07.14/indexed_timeseries (StimulusTemplate) no description
  Group /stimulus/templates/Natural_Images_Lum_Matched_set_training_2017.07.14 (StimulusTemplate) no description
  timestamps_reference_time: 2018-09-07T13:25:12.176000+00:00


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/v_in (TimeSeries) The theoretical maximum voltage that the running wheel encoder will reach prior to "wrapping". This should theoretically be 5V (after crossing 5V goes to 0V, or vice versa). In practice the encoder does not always reach this value before wrapping, which can cause transient spikes in speed at the voltage "wraps".
  Group /acquisition/v_sig (TimeSeries) Voltage signal from the running wheel encoder
  file_create_date: ['2023-09-15T13:08:34.395691+00:00']
  Group /general/devices/BEH.D-Box5 (Device) Allen Brain Observatory - Scientifica 2P Rig
  experiment_description: An operant behavior training session where a mouse must lick a spout following a change in stimulus identity to earn rewards. Stimuli consist of 8 natural scene images, for a total of 64 possible pairwise transitions. Images are shown for 250 ms with a 500 ms intervening gray period. Delivered rewards are 7ul in volume, and the session lasts for 60 minutes
  institution: Allen Institute for Brain Science
  keywords: ['visual' 'behavior' 'task']
  Group /general/metadata (BehaviorMetadata) 
  Group /general/subject (BehaviorSubject) 
  Group /general/task_parameters (BehaviorTaskParameters) 
  identifier: 754509820
  Group /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations (TimeIntervals) Presentation times and stimuli details for 'Natural_Images_Lum_Matched_set_training_2017' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/active (VectorData) No description | shape = (4786,) | dtype = bool
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/duration (VectorData) No description | shape = (4786,) | dtype = float64
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/end_frame (VectorData) No description | shape = (4786,) | dtype = int64
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/flashes_since_change (VectorData) No description | shape = (4786,) | dtype = int64
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/id (ElementIdentifiers)  | shape = (4786,) | dtype = int64
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/image_index (VectorData) No description | shape = (4786,) | dtype = int64
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/image_name (VectorData) No description | shape = (4786,) | dtype = object
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/image_set (VectorData) No description | shape = (4786,) | dtype = object
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/is_change (VectorData) No description | shape = (4786,) | dtype = bool
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/is_image_novel (VectorData) No description | shape = (4786,) | dtype = bool
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/is_sham_change (VectorData) No description | shape = (4786,) | dtype = bool
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/omitted (VectorData) No description | shape = (4786,) | dtype = bool
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/start_frame (VectorData) No description | shape = (4786,) | dtype = int64
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (4786,) | dtype = float64
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (4786,) | dtype = int64
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/stimulus_block_name (VectorData) No description | shape = (4786,) | dtype = object
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/stimulus_name (VectorData) Name of stimulus | shape = (4786,) | dtype = object
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (4786,) | dtype = float64
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/tags (VectorData) user-defined tags | shape = (4786,) | dtype = object
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (4786,) | dtype = uint16
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (4786,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (4786,) | dtype = uint16
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/trials_id (VectorData) No description | shape = (4786,) | dtype = int64
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/aborted (VectorData) NOT IMPLEMENTED: aborted | shape = (666,) | dtype = bool
  Dataset /intervals/trials/auto_rewarded (VectorData) NOT IMPLEMENTED: auto_rewarded | shape = (666,) | dtype = bool
  Dataset /intervals/trials/catch (VectorData) NOT IMPLEMENTED: catch | shape = (666,) | dtype = bool
  Dataset /intervals/trials/change_frame (VectorData) NOT IMPLEMENTED: change_frame | shape = (666,) | dtype = int64
  Dataset /intervals/trials/change_image_name (VectorData) NOT IMPLEMENTED: change_image_name | shape = (666,) | dtype = object
  Dataset /intervals/trials/change_time (VectorData) NOT IMPLEMENTED: change_time | shape = (666,) | dtype = float64
  Dataset /intervals/trials/correct_reject (VectorData) NOT IMPLEMENTED: correct_reject | shape = (666,) | dtype = bool
  Dataset /intervals/trials/false_alarm (VectorData) NOT IMPLEMENTED: false_alarm | shape = (666,) | dtype = bool
  Dataset /intervals/trials/go (VectorData) NOT IMPLEMENTED: go | shape = (666,) | dtype = bool
  Dataset /intervals/trials/hit (VectorData) NOT IMPLEMENTED: hit | shape = (666,) | dtype = bool
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (666,) | dtype = int64
  Dataset /intervals/trials/initial_image_name (VectorData) NOT IMPLEMENTED: initial_image_name | shape = (666,) | dtype = object
  Dataset /intervals/trials/is_change (VectorData) NOT IMPLEMENTED: is_change | shape = (666,) | dtype = bool
  Dataset /intervals/trials/lick_times (VectorData) NOT IMPLEMENTED: lick_times | shape = (2239,) | dtype = float64
  Dataset /intervals/trials/lick_times_index (VectorIndex) Index for VectorData 'lick_times' | shape = (666,) | dtype = uint16
  Dataset /intervals/trials/miss (VectorData) NOT IMPLEMENTED: miss | shape = (666,) | dtype = bool
  Dataset /intervals/trials/response_latency (VectorData) NOT IMPLEMENTED: response_latency | shape = (666,) | dtype = float64
  Dataset /intervals/trials/response_time (VectorData) NOT IMPLEMENTED: response_time | shape = (666,) | dtype = float64
  Dataset /intervals/trials/reward_time (VectorData) NOT IMPLEMENTED: reward_time | shape = (666,) | dtype = float64
  Dataset /intervals/trials/reward_volume (VectorData) NOT IMPLEMENTED: reward_volume | shape = (666,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (666,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (666,) | dtype = float64
  Dataset /intervals/trials/trial_length (VectorData) NOT IMPLEMENTED: trial_length | shape = (666,) | dtype = float64
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
  session_description: TRAINING_4_images_A_handoff_ready
  session_start_time: 2018-09-17T14:01:55.092000+00:00
  Group /stimulus/presentation/Natural_Images_Lum_Matched_set_training_2017.07.14 (IndexSeries) no description
  Group /stimulus/presentation/Natural_Images_Lum_Matched_set_training_2017.07.14/indexed_timeseries (StimulusTemplate) no description
  Group /stimulus/templates/Natural_Images_Lum_Matched_set_training_2017.07.14 (StimulusTemplate) no description
  timestamps_reference_time: 2018-09-17T14:01:55.092000+00:00


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/v_in (TimeSeries) The theoretical maximum voltage that the running wheel encoder will reach prior to "wrapping". This should theoretically be 5V (after crossing 5V goes to 0V, or vice versa). In practice the encoder does not always reach this value before wrapping, which can cause transient spikes in speed at the voltage "wraps".
  Group /acquisition/v_sig (TimeSeries) Voltage signal from the running wheel encoder
  file_create_date: ['2023-09-15T13:09:48.140047+00:00']
  Group /general/devices/BEH.D-Box4 (Device) Allen Brain Observatory - Scientifica 2P Rig
  experiment_description: An operant behavior training session where a mouse must lick a spout following a change in stimulus identity to earn rewards. Stimuli consist of 8 natural scene images, for a total of 64 possible pairwise transitions. Images are shown for 250 ms with a 500 ms intervening gray period. Delivered rewards are 7ul in volume, and the session lasts for 60 minutes
  institution: Allen Institute for Brain Science
  keywords: ['visual' 'behavior' 'task']
  Group /general/metadata (BehaviorMetadata) 
  Group /general/subject (BehaviorSubject) 
  Group /general/task_parameters (BehaviorTaskParameters) 
  identifier: 757431083
  Group /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations (TimeIntervals) Presentation times and stimuli details for 'Natural_Images_Lum_Matched_set_training_2017' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/active (VectorData) No description | shape = (4787,) | dtype = bool
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/duration (VectorData) No description | shape = (4787,) | dtype = float64
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/end_frame (VectorData) No description | shape = (4787,) | dtype = int64
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/flashes_since_change (VectorData) No description | shape = (4787,) | dtype = int64
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/id (ElementIdentifiers)  | shape = (4787,) | dtype = int64
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/image_index (VectorData) No description | shape = (4787,) | dtype = int64
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/image_name (VectorData) No description | shape = (4787,) | dtype = object
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/image_set (VectorData) No description | shape = (4787,) | dtype = object
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/is_change (VectorData) No description | shape = (4787,) | dtype = bool
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/is_image_novel (VectorData) No description | shape = (4787,) | dtype = bool
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/is_sham_change (VectorData) No description | shape = (4787,) | dtype = bool
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/omitted (VectorData) No description | shape = (4787,) | dtype = bool
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/start_frame (VectorData) No description | shape = (4787,) | dtype = int64
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (4787,) | dtype = float64
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (4787,) | dtype = int64
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/stimulus_block_name (VectorData) No description | shape = (4787,) | dtype = object
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/stimulus_name (VectorData) Name of stimulus | shape = (4787,) | dtype = object
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (4787,) | dtype = float64
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/tags (VectorData) user-defined tags | shape = (4787,) | dtype = object
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (4787,) | dtype = uint16
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (4787,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (4787,) | dtype = uint16
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/trials_id (VectorData) No description | shape = (4787,) | dtype = int64
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/aborted (VectorData) NOT IMPLEMENTED: aborted | shape = (1307,) | dtype = bool
  Dataset /intervals/trials/auto_rewarded (VectorData) NOT IMPLEMENTED: auto_rewarded | shape = (1307,) | dtype = bool
  Dataset /intervals/trials/catch (VectorData) NOT IMPLEMENTED: catch | shape = (1307,) | dtype = bool
  Dataset /intervals/trials/change_frame (VectorData) NOT IMPLEMENTED: change_frame | shape = (1307,) | dtype = int64
  Dataset /intervals/trials/change_image_name (VectorData) NOT IMPLEMENTED: change_image_name | shape = (1307,) | dtype = object
  Dataset /intervals/trials/change_time (VectorData) NOT IMPLEMENTED: change_time | shape = (1307,) | dtype = float64
  Dataset /intervals/trials/correct_reject (VectorData) NOT IMPLEMENTED: correct_reject | shape = (1307,) | dtype = bool
  Dataset /intervals/trials/false_alarm (VectorData) NOT IMPLEMENTED: false_alarm | shape = (1307,) | dtype = bool
  Dataset /intervals/trials/go (VectorData) NOT IMPLEMENTED: go | shape = (1307,) | dtype = bool
  Dataset /intervals/trials/hit (VectorData) NOT IMPLEMENTED: hit | shape = (1307,) | dtype = bool
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (1307,) | dtype = int64
  Dataset /intervals/trials/initial_image_name (VectorData) NOT IMPLEMENTED: initial_image_name | shape = (1307,) | dtype = object
  Dataset /intervals/trials/is_change (VectorData) NOT IMPLEMENTED: is_change | shape = (1307,) | dtype = bool
  Dataset /intervals/trials/lick_times (VectorData) NOT IMPLEMENTED: lick_times | shape = (3285,) | dtype = float64
  Dataset /intervals/trials/lick_times_index (VectorIndex) Index for VectorData 'lick_times' | shape = (1307,) | dtype = uint16
  Dataset /intervals/trials/miss (VectorData) NOT IMPLEMENTED: miss | shape = (1307,) | dtype = bool
  Dataset /intervals/trials/response_latency (VectorData) NOT IMPLEMENTED: response_latency | shape = (1307,) | dtype = float64
  Dataset /intervals/trials/response_time (VectorData) NOT IMPLEMENTED: response_time | shape = (1307,) | dtype = float64
  Dataset /intervals/trials/reward_time (VectorData) NOT IMPLEMENTED: reward_time | shape = (1307,) | dtype = float64
  Dataset /intervals/trials/reward_volume (VectorData) NOT IMPLEMENTED: reward_volume | shape = (1307,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (1307,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1307,) | dtype = float64
  Dataset /intervals/trials/trial_length (VectorData) NOT IMPLEMENTED: trial_length | shape = (1307,) | dtype = float64
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
  session_description: TRAINING_4_images_A_handoff_lapsed
  session_start_time: 2018-09-24T13:25:42.270000+00:00
  Group /stimulus/presentation/Natural_Images_Lum_Matched_set_training_2017.07.14 (IndexSeries) no description
  Group /stimulus/presentation/Natural_Images_Lum_Matched_set_training_2017.07.14/indexed_timeseries (StimulusTemplate) no description
  Group /stimulus/templates/Natural_Images_Lum_Matched_set_training_2017.07.14 (StimulusTemplate) no description
  timestamps_reference_time: 2018-09-24T13:25:42.270000+00:00


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  Group /acquisition/v_in (TimeSeries) The theoretical maximum voltage that the running wheel encoder will reach prior to "wrapping". This should theoretically be 5V (after crossing 5V goes to 0V, or vice versa). In practice the encoder does not always reach this value before wrapping, which can cause transient spikes in speed at the voltage "wraps".
  Group /acquisition/v_sig (TimeSeries) Voltage signal from the running wheel encoder
  file_create_date: ['2023-09-15T13:09:59.885081+00:00']
  Group /general/devices/BEH.D-Box1 (Device) Allen Brain Observatory - Scientifica 2P Rig
  experiment_description: An operant behavior training session where a mouse must lick a spout following a change in stimulus identity to earn rewards. Stimuli consist of 8 natural scene images, for a total of 64 possible pairwise transitions. Images are shown for 250 ms with a 500 ms intervening gray period. Delivered rewards are 7ul in volume, and the session lasts for 60 minutes
  institution: Allen Institute for Brain Science
  keywords: ['visual' 'behavior' 'task']
  Group /general/metadata (BehaviorMetadata) 
  Group /general/subject (BehaviorSubject) 
  Group /general/task_parameters (BehaviorTaskParameters) 
  identifier: 759756829
  Group /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations (TimeIntervals) Presentation times and stimuli details for 'Natural_Images_Lum_Matched_set_training_2017' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/active (VectorData) No description | shape = (4790,) | dtype = bool
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/duration (VectorData) No description | shape = (4790,) | dtype = float64
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/end_frame (VectorData) No description | shape = (4790,) | dtype = int64
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/flashes_since_change (VectorData) No description | shape = (4790,) | dtype = int64
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/id (ElementIdentifiers)  | shape = (4790,) | dtype = int64
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/image_index (VectorData) No description | shape = (4790,) | dtype = int64
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/image_name (VectorData) No description | shape = (4790,) | dtype = object
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/image_set (VectorData) No description | shape = (4790,) | dtype = object
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/is_change (VectorData) No description | shape = (4790,) | dtype = bool
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/is_image_novel (VectorData) No description | shape = (4790,) | dtype = bool
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/is_sham_change (VectorData) No description | shape = (4790,) | dtype = bool
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/omitted (VectorData) No description | shape = (4790,) | dtype = bool
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/start_frame (VectorData) No description | shape = (4790,) | dtype = int64
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (4790,) | dtype = float64
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (4790,) | dtype = int64
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/stimulus_block_name (VectorData) No description | shape = (4790,) | dtype = object
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/stimulus_name (VectorData) Name of stimulus | shape = (4790,) | dtype = object
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (4790,) | dtype = float64
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/tags (VectorData) user-defined tags | shape = (4790,) | dtype = object
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (4790,) | dtype = uint16
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (4790,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (4790,) | dtype = uint16
  Dataset /intervals/Natural_Images_Lum_Matched_set_training_2017_presentations/trials_id (VectorData) No description | shape = (4790,) | dtype = int64
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/aborted (VectorData) NOT IMPLEMENTED: aborted | shape = (1291,) | dtype = bool
  Dataset /intervals/trials/auto_rewarded (VectorData) NOT IMPLEMENTED: auto_rewarded | shape = (1291,) | dtype = bool
  Dataset /intervals/trials/catch (VectorData) NOT IMPLEMENTED: catch | shape = (1291,) | dtype = bool
  Dataset /intervals/trials/change_frame (VectorData) NOT IMPLEMENTED: change_frame | shape = (1291,) | dtype = int64
  Dataset /intervals/trials/change_image_name (VectorData) NOT IMPLEMENTED: change_image_name | shape = (1291,) | dtype = object
  Dataset /intervals/trials/change_time (VectorData) NOT IMPLEMENTED: change_time | shape = (1291,) | dtype = float64
  Dataset /intervals/trials/correct_reject (VectorData) NOT IMPLEMENTED: correct_reject | shape = (1291,) | dtype = bool
  Dataset /intervals/trials/false_alarm (VectorData) NOT IMPLEMENTED: false_alarm | shape = (1291,) | dtype = bool
  Dataset /intervals/trials/go (VectorData) NOT IMPLEMENTED: go | shape = (1291,) | dtype = bool
  Dataset /intervals/trials/hit (VectorData) NOT IMPLEMENTED: hit | shape = (1291,) | dtype = bool
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (1291,) | dtype = int64
  Dataset /intervals/trials/initial_image_name (VectorData) NOT IMPLEMENTED: initial_image_name | shape = (1291,) | dtype = object
  Dataset /intervals/trials/is_change (VectorData) NOT IMPLEMENTED: is_change | shape = (1291,) | dtype = bool
  Dataset /intervals/trials/lick_times (VectorData) NOT IMPLEMENTED: lick_times | shape = (2227,) | dtype = float64
  Dataset /intervals/trials/lick_times_index (VectorIndex) Index for VectorData 'lick_times' | shape = (1291,) | dtype = uint16
  Dataset /intervals/trials/miss (VectorData) NOT IMPLEMENTED: miss | shape = (1291,) | dtype = bool
  Dataset /intervals/trials/response_latency (VectorData) NOT IMPLEMENTED: response_latency | shape = (1291,) | dtype = float64
  Dataset /intervals/trials/response_time (VectorData) NOT IMPLEMENTED: response_time | shape = (1291,) | dtype = float64
  Dataset /intervals/trials/reward_time (VectorData) NOT IMPLEMENTED: reward_time | shape = (1291,) | dtype = float64
  Dataset /intervals/trials/reward_volume (VectorData) NOT IMPLEMENTED: reward_volume | shape = (1291,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (1291,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1291,) | dtype = float64
  Dataset /intervals/trials/trial_length (VectorData) NOT IMPLEMENTED: trial_length | shape = (1291,) | dtype = float64
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
  session_description: TRAINING_4_images_A_handoff_lapsed
  session_start_time: 2018-10-01T14:25:12.779000+00:00
  Group /stimulus/presentation/Natural_Images_Lum_Matched_set_training_2017.07.14 (IndexSeries) no description
  Group /stimulus/presentation/Natural_Images_Lum_Matched_set_training_2017.07.14/indexed_timeseries (StimulusTemplate) no description
  Group /stimulus/templates/Natural_Images_Lum_Matched_set_training_2017.07.14 (StimulusTemplate) no description
  timestamps_reference_time: 2018-10-01T14:25:12.779000+00:00
