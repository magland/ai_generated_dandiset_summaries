
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000678/0.231004.2146
name: Pupil and movement measurements during mouse auditory and visual discrimination
contributor: [{'name': 'Hulsey, Daniel', 'email': 'hulsey.daniel@gmail.com', 'roleName': ['dcite:Author', 'dcite:Conceptualization', 'dcite:DataCollector', 'dcite:FormalAnalysis', 'dcite:Investigation', 'dcite:Methodology', 'dcite:Researcher', 'dcite:Software', 'dcite:Visualization'], 'schemaKey': 'Person', 'identifier': '0000-0003-3243-6282', 'affiliation': [], 'includeInCitation': True}, {'name': 'Zumwalt, Kevin', 'roleName': ['dcite:Author', 'dcite:DataCollector', 'dcite:Investigation'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Mazzucato, Luca', 'roleName': ['dcite:Author', 'dcite:Conceptualization', 'dcite:FundingAcquisition', 'dcite:Methodology', 'dcite:Software', 'dcite:Supervision'], 'schemaKey': 'Person', 'identifier': '0000-0002-8525-7539', 'affiliation': [], 'includeInCitation': True}, {'name': 'McCormick, David A.', 'roleName': ['dcite:Author', 'dcite:Conceptualization', 'dcite:FundingAcquisition', 'dcite:Resources', 'dcite:Supervision'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Jaramillo, Santiago', 'roleName': ['dcite:Author', 'dcite:Conceptualization', 'dcite:FundingAcquisition', 'dcite:Methodology', 'dcite:Software', 'dcite:Supervision', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0002-6595-8450', 'affiliation': [], 'includeInCitation': True}, {'name': 'National Institute of Neurological Disorders and Stroke', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': 'R01NS118461, R35NS097287 ', 'contactPoint': [], 'includeInCitation': False}, {'name': 'National Science Foundation', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': '2024926', 'contactPoint': [], 'includeInCitation': False}]
description: Pupil diameter, face motion energy, and locomotion speed measures recorded during sensory discrimination behavior of head-fixed mice. Subjects classify the frequency of an auditory tone cloud stimulus, or the angle of a drifting Gabor patch, at right or left lick ports. Data include 391 behavioral sessions from 13 subjects. For more information see the preprint at https://www.biorxiv.org/content/10.1101/2023.03.02.530651v2.
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 8108311416, 'numberOfFiles': 391, 'numberOfSubjects': 13, 'variableMeasured': [], 'measurementTechnique': []}

Dandiset 000678 has 100 NWB files.
25 of these NWB files are of type 1.
75 of these NWB files are of type 2.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/face_energy (TimeSeries) Pixel intensity time differential within face ROI.
  Group /acquisition/licks_left (TimeSeries) Time of each left-port lick.
  Group /acquisition/licks_right (TimeSeries) Time of each right-port lick.
  Group /acquisition/post_hoc_pupil_diameter (TimeSeries) Pixel length of the long axis of the pupil per frame calculated post-hoc.
  Group /acquisition/pupil_area (TimeSeries) The pixel area of the pupil per frame calculated online during behavioral performance.
  Group /acquisition/pupil_diameter (TimeSeries) Pixel length of the long axis of the pupil per frame calculated online during behavioral performance.
  Group /acquisition/reward_left (TimeSeries) Time of each left-port reward.
  Group /acquisition/reward_right (TimeSeries) Time of each right-port reward.
  Group /acquisition/running_speed (TimeSeries) Speed of the animal, estimated from the rotary encoder on the wheel.
  Group /acquisition/whisker_energy (TimeSeries) Pixel intensity time differential within whisker pad ROI.
  file_create_date: ['2023-09-08T17:05:17.819983-07:00']
  experimenter: ['csteven4']
  institution: University of Oregon
  Group /general/metadata (LabMetaData_ext) 
  Group /general/subject (Subject) 
  identifier: BW041_20210830T130549
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/auditory_stim_band (VectorData) Target band of presented tone cloud MAP:{'low_band': 0, 'high_band': 1} | shape = (885,) | dtype = float64
  Dataset /intervals/trials/auditory_stim_difficulty (VectorData) Ratio of tones selected from target frequency band | shape = (885,) | dtype = float64
  Dataset /intervals/trials/auditory_stim_id (VectorData) Auditory stimulus ID MAP:{'left': 0, 'right': 1, 'no stim': 2} | shape = (885,) | dtype = float64
  Dataset /intervals/trials/choice (VectorData) Trial choice MAP:{'left': 0, 'right': 1, 'no_lick': 2} | shape = (885,) | dtype = float64
  Dataset /intervals/trials/cue_ID (VectorData) Odor identity MAP:{'A': 0, 'B': 1} | shape = (885,) | dtype = float64
  Dataset /intervals/trials/cue_duration (VectorData) Duration of odor presentation | shape = (885,) | dtype = float64
  Dataset /intervals/trials/cue_time (VectorData) Odor cue time relative to session start | shape = (885,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (885,) | dtype = int32
  Dataset /intervals/trials/outcome (VectorData) Trial outcome MAP:{'timeout': 0, 'hit': 1, 'miss': 2, 'false_alarm': 4, 'correct_reject': 8, 'incorrect_reject': 16} | shape = (885,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (885,) | dtype = float64
  Dataset /intervals/trials/stimulus_duration (VectorData) Duration of stimulus presentation | shape = (885,) | dtype = float64
  Dataset /intervals/trials/stimulus_time (VectorData) Stimulus time rlative to session start | shape = (885,) | dtype = float64
  Dataset /intervals/trials/stimulus_type (VectorData) Type of stimulus presented MAP:{'target': 0, 'distractor': 1, 'both': 2} | shape = (885,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (885,) | dtype = float64
  Dataset /intervals/trials/target_modality (VectorData) Target sensory modality MAP:{'auditory': 0, 'visual': 1} | shape = (885,) | dtype = float64
  Dataset /intervals/trials/target_port (VectorData) Port rewarded on correct response MAP:{'left': 0, 'right': 1} | shape = (885,) | dtype = float64
  Dataset /intervals/trials/visual_stim_difficulty (VectorData) Delta degrees clockwise or counterclockwise from 45 degrees of drifting grating MAP:{'45': 0, '36': 1, '27': 2, '18': 3, '9': 4} | shape = (885,) | dtype = float64
  Dataset /intervals/trials/visual_stim_id (VectorData) Visual stimulus ID MAP:{'left': 0, 'right': 1, 'no stim': 2} | shape = (885,) | dtype = float64
  Dataset /intervals/trials/visual_stim_oreintation (VectorData) Orientation of gabor patch MAP:{'horizontal': 0, 'vertical': 1} | shape = (885,) | dtype = float64
  session_description: Behavior data. Two-alternative choice visual/auditory discrimination.
  session_start_time: 2021-08-30T13:05:49.532000-07:00
  timestamps_reference_time: 2021-08-30T13:05:49.532000-07:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/face_energy (TimeSeries) Pixel intensity time differential within face ROI.
  Group /acquisition/licks_left (TimeSeries) Time of each left-port lick.
  Group /acquisition/licks_right (TimeSeries) Time of each right-port lick.
  Group /acquisition/post_hoc_pupil_diameter (TimeSeries) Pixel length of the long axis of the pupil per frame calculated post-hoc.
  Group /acquisition/pupil_area (TimeSeries) The pixel area of the pupil per frame calculated online during behavioral performance.
  Group /acquisition/pupil_diameter (TimeSeries) Pixel length of the long axis of the pupil per frame calculated online during behavioral performance.
  Group /acquisition/reward_left (TimeSeries) Time of each left-port reward.
  Group /acquisition/reward_right (TimeSeries) Time of each right-port reward.
  Group /acquisition/running_speed (TimeSeries) Speed of the animal, estimated from the rotary encoder on the wheel.
  Group /acquisition/whisker_energy (TimeSeries) Pixel intensity time differential within whisker pad ROI.
  file_create_date: ['2023-09-08T17:08:18.690183-07:00']
  experimenter: ['csteven4']
  institution: University of Oregon
  Group /general/metadata (LabMetaData_ext) 
  Group /general/subject (Subject) 
  identifier: BW041_20210917T133552
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/auditory_stim_band (VectorData) Target band of presented tone cloud MAP:{'low_band': 0, 'high_band': 1} | shape = (849,) | dtype = float64
  Dataset /intervals/trials/auditory_stim_difficulty (VectorData) Ratio of tones selected from target frequency band | shape = (849,) | dtype = float64
  Dataset /intervals/trials/auditory_stim_id (VectorData) Auditory stimulus ID MAP:{'left': 0, 'right': 1, 'no stim': 2} | shape = (849,) | dtype = float64
  Dataset /intervals/trials/choice (VectorData) Trial choice MAP:{'left': 0, 'right': 1, 'no_lick': 2} | shape = (849,) | dtype = float64
  Dataset /intervals/trials/cue_ID (VectorData) Odor identity MAP:{'A': 0, 'B': 1} | shape = (849,) | dtype = float64
  Dataset /intervals/trials/cue_duration (VectorData) Duration of odor presentation | shape = (849,) | dtype = float64
  Dataset /intervals/trials/cue_time (VectorData) Odor cue time relative to session start | shape = (849,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (849,) | dtype = int32
  Dataset /intervals/trials/outcome (VectorData) Trial outcome MAP:{'timeout': 0, 'hit': 1, 'miss': 2, 'false_alarm': 4, 'correct_reject': 8, 'incorrect_reject': 16} | shape = (849,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (849,) | dtype = float64
  Dataset /intervals/trials/stimulus_duration (VectorData) Duration of stimulus presentation | shape = (849,) | dtype = float64
  Dataset /intervals/trials/stimulus_time (VectorData) Stimulus time rlative to session start | shape = (849,) | dtype = float64
  Dataset /intervals/trials/stimulus_type (VectorData) Type of stimulus presented MAP:{'target': 0, 'distractor': 1, 'both': 2} | shape = (849,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (849,) | dtype = float64
  Dataset /intervals/trials/target_modality (VectorData) Target sensory modality MAP:{'auditory': 0, 'visual': 1} | shape = (849,) | dtype = float64
  Dataset /intervals/trials/target_port (VectorData) Port rewarded on correct response MAP:{'left': 0, 'right': 1} | shape = (849,) | dtype = float64
  Dataset /intervals/trials/visual_gabor_angle (VectorData) degrees clockwise from vertical of stationary gabor patch | shape = (849,) | dtype = float64
  Dataset /intervals/trials/visual_stim_difficulty (VectorData) Delta degrees clockwise or counterclockwise from 45 degrees of drifting grating MAP:{'45': 0, '36': 1, '27': 2, '18': 3, '9': 4} | shape = (849,) | dtype = float64
  Dataset /intervals/trials/visual_stim_id (VectorData) Visual stimulus ID MAP:{'left': 0, 'right': 1, 'no stim': 2} | shape = (849,) | dtype = float64
  Dataset /intervals/trials/visual_stim_oreintation (VectorData) Orientation of gabor patch MAP:{'horizontal': 0, 'vertical': 1} | shape = (849,) | dtype = float64
  session_description: Behavior data. Two-alternative choice visual/auditory discrimination.
  session_start_time: 2021-09-17T13:35:52.471000-07:00
  timestamps_reference_time: 2021-09-17T13:35:52.471000-07:00
