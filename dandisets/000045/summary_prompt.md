
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000045/0.211209.1413
name: IBL behavioral data
contributor: [{'url': 'https://internationalbrainlab.com', 'name': 'International Brain Laboratory', 'email': 'ibldata@internationalbrainlab.org', 'roleName': ['dcite:Author', 'dcite:ContactPerson'], 'schemaKey': 'Organization', 'contactPoint': [], 'includeInCitation': True}]
description: This dataset is a result of a multi-institution, cross country collaboration of labs, called International Brain Laboratory conducting standardized experiments on decision-making in mice. In the experiment, mice are shown a visual grating on screen with varying levels of contrast, and they are trained to rotate a wheel to move the on-screen stimulus from either side of their visual field to the center. These NWB files contain datasets corresponding to this wheel movement, camera footage of mice and information about the visual stimulus at every trial. 
Paper: 
Aguillon, V., Angelaki, D., Bayer, H. M., Bonacchi, N., Carandini, M., Cazettes, F., Churchland, A. K., Chapuis, G., Dan, Y., Dewitt, E., Faulkner, M., Hamish, F., Haetzel, L., Hausser, M., Hofer, S., Hu, F., Khanal, A., Krasniak, C., Laranjeira, I., … Zador, A. (2020). A standardized and reproducible method to measure decision-making in mice. BioRxiv, 2020.01.17.909838. https://doi.org/10.1101/2020.01.17.909838
assetsSummary: {'species': [{'name': 'House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'behavioral approach', 'schemaKey': 'ApproachType'}, {'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 97844923040, 'numberOfFiles': 6615, 'numberOfSubjects': 178, 'variableMeasured': ['BehavioralTimeSeries', 'ProcessingModule', 'DecompositionSeries', 'Position', 'ElectrodeGroup'], 'measurementTechnique': [{'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'fourier analysis technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000045 has 69 NWB files.
1 of these NWB files are of type 1.
11 of these NWB files are of type 2.
28 of these NWB files are of type 3.
25 of these NWB files are of type 4.
4 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2020-11-23T11:59:40.040861+05:30']
  Group /general/Ibl_session_data (IblSessionData) 
  Group /general/devices/NeuroPixels probe (Device) NeuroPixels probe
  experiment_description: ibl_neuropixel_brainwide_01
  experimenter: ['Karolina_Socha']
  institution: University College London
  keywords: ['Karolina_Socha' 'cortexlab' 'IBL']
  lab: cortexlab
  notes: 
  protocol: _iblrig_tasks_biasedChoiceWorld6.0.5
  session_id: 4492f579-67eb-4385-99a6-d2c4e679c753
  Group /general/subject (IblSubject) 
  surgery: none
  identifier: 4492f579-67eb-4385-99a6-d2c4e679c753
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/choice (VectorData) which choice was made in choiceworld: -1 (turn CCW), +1 (turn CW), or 0 (nogo) | shape = (974,) | dtype = int64
  Dataset /intervals/trials/contrastLeft (VectorData) contrast of left-side stimulus (0...1) nan if trial is on other side | shape = (974,) | dtype = float64
  Dataset /intervals/trials/contrastRight (VectorData) contrast of right-side stimulus (0...1) nan if trial is on other side | shape = (974,) | dtype = float64
  Dataset /intervals/trials/feedbackType (VectorData) Whether feedback is positive or negative in choiceworld (-1 for negative, +1 for positive) | shape = (974,) | dtype = int64
  Dataset /intervals/trials/feedback_times (VectorData) Time of feedback delivery (reward or not) in choiceworld - in absolute seconds, rather than relative to trial onset | shape = (974,) | dtype = float64
  Dataset /intervals/trials/goCueTrigger_times (VectorData) Time of go cues in choiceworld - in absolute seconds, rather than relative to trial onset NOTE: this is the time the trigger command is sent by Bpod | shape = (974,) | dtype = float64
  Dataset /intervals/trials/goCue_times (VectorData) Time of go cues in choiceworld - in absolute seconds, rather than relative to trial onset | shape = (974,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (974,) | dtype = int32
  Dataset /intervals/trials/included (VectorData) boolean suggesting which trials to include in analysis, chosen at experimenter discretion, e.g. by excluding the block of incorrect trials at the end of the session when the mouse has stopped | shape = (974,) | dtype = bool
  Dataset /intervals/trials/probabilityLeft (VectorData) Probability that the stimulus will be on the left hand side for the current block. The probability of right is 1 minus this | shape = (974,) | dtype = float64
  Dataset /intervals/trials/response_times (VectorData) Time of "response" in choiceworld- in absolute seconds, rather than relative to trial onset. This is when one of the three possible choices is registered in software, will not be the same as when the mouse's movement to generate that response begins. | shape = (974,) | dtype = float64
  Dataset /intervals/trials/rewardVolume (VectorData) volume of reward given each trial in µl | shape = (974,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (974,) | dtype = float64
  Dataset /intervals/trials/stimOn_times (VectorData) Times of stimuli in choiceworld - in absolute seconds, rather than relative to trial onset | shape = (974,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (974,) | dtype = float64
  Group /processing/behavior (ProcessingModule) behavior
  Group /processing/behavior/BehavioralTimeSeries (BehavioralTimeSeries) 
  Group /processing/behavior/BehavioralTimeSeries/position (TimeSeries) Absolute position of wheel.
  session_description: Behavior training/tasks
  session_start_time: 2019-10-29T09:41:55+00:00
  timestamps_reference_time: 2019-10-29T09:41:55+00:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/_iblmic_audioSpectrogram (DecompositionSeries) Audio spectrogram from microphone, power
  Group /acquisition/_iblmic_audioSpectrogram/bands (DynamicTable) spectogram frequencies
  Dataset /acquisition/_iblmic_audioSpectrogram/bands/freq (VectorData) frequency value | shape = (257,) | dtype = float32
  Dataset /acquisition/_iblmic_audioSpectrogram/bands/id (ElementIdentifiers)  | shape = (257,) | dtype = int32
  Group /acquisition/camera_raw (ImageSeries) no description
  file_create_date: ['2020-11-22T19:18:24.273570+05:30']
  Group /general/Ibl_session_data (IblSessionData) 
  Group /general/devices/NeuroPixels probe (Device) NeuroPixels probe
  experiment_description: ibl_neuropixel_brainwide_01
  experimenter: ['Karolina_Socha']
  institution: University College London
  keywords: ['Karolina_Socha' 'cortexlab' 'IBL']
  lab: cortexlab
  notes: 
  protocol: _iblrig_tasks_biasedChoiceWorld6.3.1
  session_id: 00594aec-bb70-4601-862d-63a31ef0e1c0
  Group /general/subject (IblSubject) 
  surgery: none
  identifier: 00594aec-bb70-4601-862d-63a31ef0e1c0
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/choice (VectorData) which choice was made in choiceworld: -1 (turn CCW), +1 (turn CW), or 0 (nogo) | shape = (704,) | dtype = int64
  Dataset /intervals/trials/contrastLeft (VectorData) contrast of left-side stimulus (0...1) nan if trial is on other side | shape = (704,) | dtype = float64
  Dataset /intervals/trials/contrastRight (VectorData) contrast of right-side stimulus (0...1) nan if trial is on other side | shape = (704,) | dtype = float64
  Dataset /intervals/trials/feedbackType (VectorData) Whether feedback is positive or negative in choiceworld (-1 for negative, +1 for positive) | shape = (704,) | dtype = int64
  Dataset /intervals/trials/feedback_times (VectorData) Time of feedback delivery (reward or not) in choiceworld - in absolute seconds, rather than relative to trial onset | shape = (704,) | dtype = float64
  Dataset /intervals/trials/firstMovement_times (VectorData) Movement onset (absolute from session start) extracted from the rotary encoder  | shape = (704,) | dtype = float64
  Dataset /intervals/trials/goCueTrigger_times (VectorData) Time of go cues in choiceworld - in absolute seconds, rather than relative to trial onset NOTE: this is the time the trigger command is sent by Bpod | shape = (704,) | dtype = float64
  Dataset /intervals/trials/goCue_times (VectorData) Time of go cues in choiceworld - in absolute seconds, rather than relative to trial onset | shape = (704,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (704,) | dtype = int32
  Dataset /intervals/trials/included (VectorData) boolean suggesting which trials to include in analysis, chosen at experimenter discretion, e.g. by excluding the block of incorrect trials at the end of the session when the mouse has stopped | shape = (704,) | dtype = bool
  Dataset /intervals/trials/probabilityLeft (VectorData) Probability that the stimulus will be on the left hand side for the current block. The probability of right is 1 minus this | shape = (704,) | dtype = float64
  Dataset /intervals/trials/response_times (VectorData) Time of "response" in choiceworld- in absolute seconds, rather than relative to trial onset. This is when one of the three possible choices is registered in software, will not be the same as when the mouse's movement to generate that response begins. | shape = (704,) | dtype = float64
  Dataset /intervals/trials/rewardVolume (VectorData) volume of reward given each trial in µl | shape = (704,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (704,) | dtype = float64
  Dataset /intervals/trials/stimOn_times (VectorData) Times of stimuli in choiceworld - in absolute seconds, rather than relative to trial onset | shape = (704,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (704,) | dtype = float64
  Group /processing/behavior (ProcessingModule) behavior
  Group /processing/behavior/BehavioralEpochs (TimeIntervals) experimental intervals
  Dataset /processing/behavior/BehavioralEpochs/id (ElementIdentifiers)  | shape = (1311,) | dtype = int32
  Dataset /processing/behavior/BehavioralEpochs/peakAmplitude (VectorData) amplitude of the wheel move | shape = (1311,) | dtype = float64
  Dataset /processing/behavior/BehavioralEpochs/start_time (VectorData) Start time of epoch, in seconds | shape = (1311,) | dtype = float64
  Dataset /processing/behavior/BehavioralEpochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1311,) | dtype = float64
  Group /processing/behavior/BehavioralTimeSeries (BehavioralTimeSeries) 
  Group /processing/behavior/BehavioralTimeSeries/position (TimeSeries) Absolute position of wheel.
  session_description: Behavior training/tasks
  session_start_time: 2020-01-20T11:15:32+00:00
  timestamps_reference_time: 2020-01-20T11:15:32+00:00


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/camera_raw (ImageSeries) no description
  file_create_date: ['2020-11-22T19:11:45.483575+05:30']
  Group /general/Ibl_session_data (IblSessionData) 
  Group /general/devices/NeuroPixels probe (Device) NeuroPixels probe
  experiment_description: ibl_neuropixel_brainwide_01
  experimenter: ['Karolina_Socha']
  institution: University College London
  keywords: ['Karolina_Socha' 'cortexlab' 'IBL']
  lab: cortexlab
  notes: 
  protocol: _iblrig_tasks_trainingChoiceWorld5.2.7
  session_id: 07497983-2229-4cb2-8a45-50cee3fe9089
  Group /general/subject (IblSubject) 
  surgery: none
  identifier: 07497983-2229-4cb2-8a45-50cee3fe9089
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/choice (VectorData) which choice was made in choiceworld: -1 (turn CCW), +1 (turn CW), or 0 (nogo) | shape = (55,) | dtype = int32
  Dataset /intervals/trials/contrastLeft (VectorData) contrast of left-side stimulus (0...1) nan if trial is on other side | shape = (55,) | dtype = float64
  Dataset /intervals/trials/contrastRight (VectorData) contrast of right-side stimulus (0...1) nan if trial is on other side | shape = (55,) | dtype = float64
  Dataset /intervals/trials/feedbackType (VectorData) Whether feedback is positive or negative in choiceworld (-1 for negative, +1 for positive) | shape = (55,) | dtype = int64
  Dataset /intervals/trials/feedback_times (VectorData) Time of feedback delivery (reward or not) in choiceworld - in absolute seconds, rather than relative to trial onset | shape = (55,) | dtype = float64
  Dataset /intervals/trials/firstMovement_times (VectorData) Movement onset (absolute from session start) extracted from the rotary encoder  | shape = (55,) | dtype = float64
  Dataset /intervals/trials/goCueTrigger_times (VectorData) Time of go cues in choiceworld - in absolute seconds, rather than relative to trial onset NOTE: this is the time the trigger command is sent by Bpod | shape = (55,) | dtype = float64
  Dataset /intervals/trials/goCue_times (VectorData) Time of go cues in choiceworld - in absolute seconds, rather than relative to trial onset | shape = (55,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (55,) | dtype = int32
  Dataset /intervals/trials/included (VectorData) boolean suggesting which trials to include in analysis, chosen at experimenter discretion, e.g. by excluding the block of incorrect trials at the end of the session when the mouse has stopped | shape = (55,) | dtype = bool
  Dataset /intervals/trials/probabilityLeft (VectorData) Probability that the stimulus will be on the left hand side for the current block. The probability of right is 1 minus this | shape = (55,) | dtype = float64
  Dataset /intervals/trials/repNum (VectorData) the repetition number of the trial, i.e. how many trials have been repeated on this side (counting from 1) | shape = (55,) | dtype = int32
  Dataset /intervals/trials/response_times (VectorData) Time of "response" in choiceworld- in absolute seconds, rather than relative to trial onset. This is when one of the three possible choices is registered in software, will not be the same as when the mouse's movement to generate that response begins. | shape = (55,) | dtype = float64
  Dataset /intervals/trials/rewardVolume (VectorData) volume of reward given each trial in µl | shape = (55,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (55,) | dtype = float64
  Dataset /intervals/trials/stimOn_times (VectorData) Times of stimuli in choiceworld - in absolute seconds, rather than relative to trial onset | shape = (55,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (55,) | dtype = float64
  Group /processing/behavior (ProcessingModule) behavior
  Group /processing/behavior/BehavioralEpochs (TimeIntervals) experimental intervals
  Dataset /processing/behavior/BehavioralEpochs/id (ElementIdentifiers)  | shape = (388,) | dtype = int32
  Dataset /processing/behavior/BehavioralEpochs/peakAmplitude (VectorData) amplitude of the wheel move | shape = (388,) | dtype = float64
  Dataset /processing/behavior/BehavioralEpochs/start_time (VectorData) Start time of epoch, in seconds | shape = (388,) | dtype = float64
  Dataset /processing/behavior/BehavioralEpochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (388,) | dtype = float64
  Group /processing/behavior/BehavioralTimeSeries (BehavioralTimeSeries) 
  Group /processing/behavior/BehavioralTimeSeries/position (TimeSeries) Absolute position of wheel.
  session_description: Behavior training/tasks
  session_start_time: 2019-08-14T09:37:16+00:00
  timestamps_reference_time: 2019-08-14T09:37:16+00:00


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/camera_raw (ImageSeries) no description
  file_create_date: ['2020-11-22T19:13:49.223313+05:30']
  Group /general/Ibl_session_data (IblSessionData) 
  Group /general/devices/NeuroPixels probe (Device) NeuroPixels probe
  experiment_description: ibl_neuropixel_brainwide_01
  experimenter: ['Karolina_Socha']
  institution: University College London
  keywords: ['Karolina_Socha' 'cortexlab' 'IBL']
  lab: cortexlab
  notes: 
  protocol: _iblrig_tasks_biasedChoiceWorld5.3.0
  session_id: 075dd0a2-48fd-4779-97cc-15ef98110310
  Group /general/subject (IblSubject) 
  surgery: none
  identifier: 075dd0a2-48fd-4779-97cc-15ef98110310
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/choice (VectorData) which choice was made in choiceworld: -1 (turn CCW), +1 (turn CW), or 0 (nogo) | shape = (941,) | dtype = int32
  Dataset /intervals/trials/contrastLeft (VectorData) contrast of left-side stimulus (0...1) nan if trial is on other side | shape = (941,) | dtype = float64
  Dataset /intervals/trials/contrastRight (VectorData) contrast of right-side stimulus (0...1) nan if trial is on other side | shape = (941,) | dtype = float64
  Dataset /intervals/trials/feedbackType (VectorData) Whether feedback is positive or negative in choiceworld (-1 for negative, +1 for positive) | shape = (941,) | dtype = int64
  Dataset /intervals/trials/feedback_times (VectorData) Time of feedback delivery (reward or not) in choiceworld - in absolute seconds, rather than relative to trial onset | shape = (941,) | dtype = float64
  Dataset /intervals/trials/firstMovement_times (VectorData) Movement onset (absolute from session start) extracted from the rotary encoder  | shape = (941,) | dtype = float64
  Dataset /intervals/trials/goCueTrigger_times (VectorData) Time of go cues in choiceworld - in absolute seconds, rather than relative to trial onset NOTE: this is the time the trigger command is sent by Bpod | shape = (941,) | dtype = float64
  Dataset /intervals/trials/goCue_times (VectorData) Time of go cues in choiceworld - in absolute seconds, rather than relative to trial onset | shape = (941,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (941,) | dtype = int32
  Dataset /intervals/trials/included (VectorData) boolean suggesting which trials to include in analysis, chosen at experimenter discretion, e.g. by excluding the block of incorrect trials at the end of the session when the mouse has stopped | shape = (941,) | dtype = bool
  Dataset /intervals/trials/probabilityLeft (VectorData) Probability that the stimulus will be on the left hand side for the current block. The probability of right is 1 minus this | shape = (941,) | dtype = float64
  Dataset /intervals/trials/response_times (VectorData) Time of "response" in choiceworld- in absolute seconds, rather than relative to trial onset. This is when one of the three possible choices is registered in software, will not be the same as when the mouse's movement to generate that response begins. | shape = (941,) | dtype = float64
  Dataset /intervals/trials/rewardVolume (VectorData) volume of reward given each trial in µl | shape = (941,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (941,) | dtype = float64
  Dataset /intervals/trials/stimOn_times (VectorData) Times of stimuli in choiceworld - in absolute seconds, rather than relative to trial onset | shape = (941,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (941,) | dtype = float64
  Group /processing/behavior (ProcessingModule) behavior
  Group /processing/behavior/BehavioralEpochs (TimeIntervals) experimental intervals
  Dataset /processing/behavior/BehavioralEpochs/id (ElementIdentifiers)  | shape = (1679,) | dtype = int32
  Dataset /processing/behavior/BehavioralEpochs/peakAmplitude (VectorData) amplitude of the wheel move | shape = (1679,) | dtype = float64
  Dataset /processing/behavior/BehavioralEpochs/start_time (VectorData) Start time of epoch, in seconds | shape = (1679,) | dtype = float64
  Dataset /processing/behavior/BehavioralEpochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1679,) | dtype = float64
  Group /processing/behavior/BehavioralTimeSeries (BehavioralTimeSeries) 
  Group /processing/behavior/BehavioralTimeSeries/position (TimeSeries) Absolute position of wheel.
  session_description: Behavior training/tasks
  session_start_time: 2019-09-27T09:06:41+00:00
  timestamps_reference_time: 2019-09-27T09:06:41+00:00


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  Group /acquisition/_iblmic_audioSpectrogram (DecompositionSeries) Audio spectrogram from microphone, power
  Group /acquisition/_iblmic_audioSpectrogram/bands (DynamicTable) spectogram frequencies
  Dataset /acquisition/_iblmic_audioSpectrogram/bands/freq (VectorData) frequency value | shape = (257,) | dtype = float32
  Dataset /acquisition/_iblmic_audioSpectrogram/bands/id (ElementIdentifiers)  | shape = (257,) | dtype = int32
  Group /acquisition/camera_raw (ImageSeries) no description
  file_create_date: ['2020-11-22T19:17:27.183111+05:30']
  Group /general/Ibl_session_data (IblSessionData) 
  Group /general/devices/NeuroPixels probe (Device) NeuroPixels probe
  experiment_description: ibl_neuropixel_brainwide_01
  experimenter: ['Karolina_Socha']
  institution: University College London
  keywords: ['Karolina_Socha' 'cortexlab' 'IBL']
  lab: cortexlab
  notes: 
  protocol: _iblrig_tasks_biasedChoiceWorld6.2.4
  session_id: ac41a31e-00f3-4b13-b38b-b19aaf9e9b5f
  Group /general/subject (IblSubject) 
  surgery: none
  identifier: ac41a31e-00f3-4b13-b38b-b19aaf9e9b5f
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/choice (VectorData) which choice was made in choiceworld: -1 (turn CCW), +1 (turn CW), or 0 (nogo) | shape = (864,) | dtype = int64
  Dataset /intervals/trials/contrastLeft (VectorData) contrast of left-side stimulus (0...1) nan if trial is on other side | shape = (864,) | dtype = float64
  Dataset /intervals/trials/contrastRight (VectorData) contrast of right-side stimulus (0...1) nan if trial is on other side | shape = (864,) | dtype = float64
  Dataset /intervals/trials/feedbackType (VectorData) Whether feedback is positive or negative in choiceworld (-1 for negative, +1 for positive) | shape = (864,) | dtype = int64
  Dataset /intervals/trials/feedback_times (VectorData) Time of feedback delivery (reward or not) in choiceworld - in absolute seconds, rather than relative to trial onset | shape = (864,) | dtype = float64
  Dataset /intervals/trials/goCueTrigger_times (VectorData) Time of go cues in choiceworld - in absolute seconds, rather than relative to trial onset NOTE: this is the time the trigger command is sent by Bpod | shape = (864,) | dtype = float64
  Dataset /intervals/trials/goCue_times (VectorData) Time of go cues in choiceworld - in absolute seconds, rather than relative to trial onset | shape = (864,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (864,) | dtype = int32
  Dataset /intervals/trials/included (VectorData) boolean suggesting which trials to include in analysis, chosen at experimenter discretion, e.g. by excluding the block of incorrect trials at the end of the session when the mouse has stopped | shape = (864,) | dtype = bool
  Dataset /intervals/trials/probabilityLeft (VectorData) Probability that the stimulus will be on the left hand side for the current block. The probability of right is 1 minus this | shape = (864,) | dtype = float64
  Dataset /intervals/trials/response_times (VectorData) Time of "response" in choiceworld- in absolute seconds, rather than relative to trial onset. This is when one of the three possible choices is registered in software, will not be the same as when the mouse's movement to generate that response begins. | shape = (864,) | dtype = float64
  Dataset /intervals/trials/rewardVolume (VectorData) volume of reward given each trial in µl | shape = (864,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (864,) | dtype = float64
  Dataset /intervals/trials/stimOn_times (VectorData) Times of stimuli in choiceworld - in absolute seconds, rather than relative to trial onset | shape = (864,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (864,) | dtype = float64
  Group /processing/behavior (ProcessingModule) behavior
  Group /processing/behavior/BehavioralTimeSeries (BehavioralTimeSeries) 
  Group /processing/behavior/BehavioralTimeSeries/position (TimeSeries) Absolute position of wheel.
  session_description: Behavior training/tasks
  session_start_time: 2019-12-10T09:40:43+00:00
  timestamps_reference_time: 2019-12-10T09:40:43+00:00
