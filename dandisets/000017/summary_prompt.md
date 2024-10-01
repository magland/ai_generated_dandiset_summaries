
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000017/0.240329.1926
name: Distributed coding of choice, action and engagement across the mouse brain
contributor: [{'name': 'Steinmetz, Nicholas', 'roleName': ['dcite:Author', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0001-7029-2908', 'includeInCitation': True}, {'name': 'Zatka-Haas, Peter', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0001-9054-2599', 'includeInCitation': True}, {'name': 'Carandini, Matteo', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0003-4880-7682', 'includeInCitation': True}, {'name': 'Harris, Kenneth', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-5930-6456', 'includeInCitation': True}, {'name': 'Wang, Renee', 'roleName': ['dcite:DataCurator'], 'schemaKey': 'Person', 'includeInCitation': True}]
description: Data from "Distributed coding of choice, action and engagement across the mouse brain" Steinmetz et. al Nature 2019
assetsSummary: {'species': [{'name': 'House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}, {'name': 'behavioral approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 14682586049, 'numberOfFiles': 39, 'numberOfSubjects': 10, 'variableMeasured': ['ProcessingModule', 'PupilTracking', 'BehavioralEpochs', 'Units', 'BehavioralEvents', 'BehavioralTimeSeries', 'ElectrodeGroup'], 'measurementTechnique': [{'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000017 has 39 NWB files.
23 of these NWB files are of type 1.
15 of these NWB files are of type 2.
1 of these NWB files are of type 3.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/lickPiezo (TimeSeries) Voltage values from a thin-film piezo connected to the lick spout, so that values are proportional to deflection of the spout and licks can be detected as peaks of the signal.
  Group /acquisition/wheel_position (TimeSeries) The position reading of the rotary encoder attached to the rubber wheel that the mouse pushes left and right with his forelimbs.
  file_create_date: ['2019-11-26T13:54:42.972670-08:00']
  Group /general/devices/0 (Device) 
  Group /general/devices/1 (Device) 
  experiment_description: Large-scale Neuropixels recordings across brain regions of mice during a head-fixed visual discrimination task. 
  experimenter: ['Nick Steinmetz']
  Group /general/extracellular_ephys/Probe1 (ElectrodeGroup) Neuropixels Phase3A opt3
  Group /general/extracellular_ephys/Probe1/device (Device) 
  Group /general/extracellular_ephys/Probe2 (ElectrodeGroup) Neuropixels Phase3A opt3
  Group /general/extracellular_ephys/Probe2/device (Device) 
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/axial_angle (VectorData) axial angle of probe (degrees). Zero means that without vertical and horizontal rotations, the probe contacts would be pointing up. Positive means "counterclockwise. | shape = (748,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/ccf_ap (VectorData) The AP position in Allen Institute's Common Coordinate Framework. | shape = (748,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/ccf_dv (VectorData) The DV position in Allen Institute's Common Coordinate Framework. | shape = (748,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/ccf_lr (VectorData) The LR position in Allen Institute's Common Coordinate Framework. | shape = (748,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/distance_advanced (VectorData) How far the probe was moved forward from its entry point. (microns). | shape = (748,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/entry_point_ap (VectorData) anteroposterior position of probe entry point relative to bregma (microns). Positive means anterior | shape = (748,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/entry_point_rl (VectorData) mediolateral position of probe entry point relative to midline (microns). Positive means right | shape = (748,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (748,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (748,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (748,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/horizontal_angle (VectorData) horizontal angle of probe (degrees), after vertical rotation. Zero means anterior. Positive means counterclockwise (i.e. left). | shape = (748,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (748,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (748,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (748,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/site_id (VectorData) The site number, in within-probe numbering, of the channel (in practice for this dataset this always starts at zero and counts up to 383 on each probe so is equivalent to the channel number - but if switches had been used, the site number could have been different than the channel number). | shape = (748,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/site_position (VectorData) The x- and y-position of the site relative to the face of the probe (where the first column is across the face of the probe laterally and the second is the position along the length of the probe; the sites nearest the tip have second column=0). | shape = (748, 2) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/vertical_angle (VectorData) vertical angle of probe (degrees). Zero means horizontal. Positive means pointing down | shape = (748,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (748,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (748,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (748,) | dtype = float64
  institution: University College London
  keywords: ['Neural coding' 'Neuropixels' 'mouse' 'brain-wide' 'vision'
   'visual discrimination' 'electrophysiology']
  lab: The Carandini and Harris Lab
  related_publications: ['DOI 10.1038/s41586-019-1787-x']
  Group /general/subject (Subject) 
  identifier: Cori_2016-12-14
  Group /intervals/spontaneous (TimeIntervals) Intervals of sufficient duration when nothing else is going on (no task or stimulus presentation
  Dataset /intervals/spontaneous/id (ElementIdentifiers)  | shape = (4,) | dtype = int64
  Dataset /intervals/spontaneous/start_time (VectorData) Start time of epoch, in seconds | shape = (4,) | dtype = float64
  Dataset /intervals/spontaneous/stop_time (VectorData) Stop time of epoch, in seconds | shape = (4,) | dtype = float64
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/feedback_time (VectorData) Times are relative to the same time base as every other time in the dataset, not to the start of the trial. | shape = (214,) | dtype = float64
  Dataset /intervals/trials/feedback_type (VectorData) Enumerated type. -1 for negative feedback (white noise burst); +1 for positive feedback (water reward delivery). | shape = (214,) | dtype = int64
  Dataset /intervals/trials/go_cue (VectorData) The 'goCue' is referred to as the 'auditory tone cue' in the manuscript. | shape = (214,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (214,) | dtype = int64
  Dataset /intervals/trials/included (VectorData) Importantly, while this variable gives inclusion criteria according to the definition of disengagement (see manuscript Methods), it does not give inclusion criteria based on the time of response, as used for most analyses in the paper. | shape = (214,) | dtype = bool
  Dataset /intervals/trials/rep_num (VectorData) Trials are repeated if they are "easy" trials (high contrast stimuli with large difference between the two sides, or the blank screen condition) and this keeps track of how many times the current trial's condition has been repeated. | shape = (214,) | dtype = float64
  Dataset /intervals/trials/response_choice (VectorData) Enumerated type. The response registered at the end of the trial, which determines the feedback according to the contrast condition. Note that in a small percentage of cases (~4%, see manuscript Methods) the initial wheel turn was in the opposite direction. -1 for Right choice (i.e. correct when stimuli are on the right); +1 for left choice; 0 for Nogo choice. | shape = (214,) | dtype = float64
  Dataset /intervals/trials/response_time (VectorData) Times are relative to the same time base as every other time in the dataset, not to the start of the trial. | shape = (214,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (214,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (214,) | dtype = float64
  Dataset /intervals/trials/visual_stimulus_left_contrast (VectorData) Proportion contrast. A value of 0.5 means 50% contrast. 0 is a blank screen: no change to any pixel values on that side (completely undetectable). | shape = (214,) | dtype = float64
  Dataset /intervals/trials/visual_stimulus_right_contrast (VectorData) Proportion contrast. A value of 0.5 means 50% contrast. 0 is a blank screen: no change to any pixel values on that side (completely undetectable). | shape = (214,) | dtype = float64
  Dataset /intervals/trials/visual_stimulus_time (VectorData) Times are relative to the same time base as every other time in the dataset, not to the start of the trial. | shape = (214,) | dtype = float64
  Group /processing/behavior (ProcessingModule) behavior module
  Group /processing/behavior/BehavioralEpochs (BehavioralEpochs) 
  Group /processing/behavior/BehavioralEpochs/wheel_moves (IntervalSeries) Detected wheel movements.
  Group /processing/behavior/BehavioralEvents (BehavioralEvents) 
  Group /processing/behavior/BehavioralEvents/lick_times (TimeSeries) Extracted times of licks, from the lickPiezo signal.
  Group /processing/behavior/BehavioralTimeSeries (BehavioralTimeSeries) 
  Group /processing/behavior/BehavioralTimeSeries/face_motion_energy (TimeSeries) Features extracted from the video of the frontal aspect of the subject, including the subject's face and forearms.
  Group /processing/behavior/PupilTracking (PupilTracking) 
  Group /processing/behavior/PupilTracking/eye_area (TimeSeries) Features extracted from the video of the right eye.
  Group /processing/behavior/PupilTracking/eye_xy_positions (TimeSeries) Features extracted from the video of the right eye.
  session_description: Neuropixels recording during visual discrimination in awake mice.
  session_start_time: 2016-12-14T12:00:00+00:00
  Group /stimulus/presentation/passive_beeps (TimeSeries) Auditory tones of the same frequency as the auditory tone cue in the task
  Group /stimulus/presentation/passive_click_times (TimeSeries) Opening of the reward valve, but with a clamp in place such that no water flows. Therefore the auditory sound of the valve is heard, but no water reward is obtained.
  Group /stimulus/presentation/passive_left_contrast (TimeSeries) Gratings of the same size, spatial freq, position, etc as during the discrimination task.
  Group /stimulus/presentation/passive_right_contrast (TimeSeries) Gratings of the same size, spatial freq, position, etc as during the discrimination task.
  Group /stimulus/presentation/passive_white_noise (TimeSeries) The sound that accompanies an incorrect response during the discrimination task.
  Group /stimulus/presentation/receptive_field_mapping_sparse_noise (TimeSeries) White squares shown on the screen with randomized positions and timing - see manuscript Methods.
  timestamps_reference_time: 2016-12-14T12:00:00+00:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/cluster_depths (VectorData) The position of the center of mass of the template of the cluster, relative to the probe. The deepest channel on the probe is depth=0, and the most superficial is depth=3820. Units: µm | shape = (1085, 1) | dtype = float64
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (1085,) | dtype = object
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (54250,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex)  | shape = (1085,) | dtype = int64
  Dataset /units/id (ElementIdentifiers)  | shape = (1085,) | dtype = int64
  Dataset /units/peak_channel (VectorData) The channel number of the location of the peak of the cluster's waveform. | shape = (1085, 1) | dtype = int64
  Dataset /units/phy_annotations (VectorData) 0 = noise (these are already excluded and don't appear in this dataset at all); 1 = MUA (i.e. presumed to contain spikes from multiple neurons; these are not analyzed in any analyses in the paper); 2 = Good (manually labeled); 3 = Unsorted. In this dataset 'Good' was applied in a few but not all datasets to included neurons, so in general the neurons with _phy_annotation>=2 are the ones that should be included. | shape = (1085,) | dtype = int64
  Dataset /units/sampling_rate (VectorData) Sampling rate, in Hz. | shape = (1085,) | dtype = float64
  Dataset /units/spike_amps (VectorData) The peak-to-trough amplitude, obtained from the template and template-scaling amplitude returned by Kilosort (not from the raw data). | shape = (10017476, 1) | dtype = float64
  Dataset /units/spike_amps_index (VectorIndex)  | shape = (1085,) | dtype = int64
  Dataset /units/spike_depths (VectorData) The position of the center of mass of the spike on the probe, determined from the principal component features returned by Kilosort. The deepest channel on the probe is depth=0, and the most superficial is depth=3820. | shape = (10017476, 1) | dtype = float32
  Dataset /units/spike_depths_index (VectorIndex)  | shape = (1085,) | dtype = int64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (10017476,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex)  | shape = (1085,) | dtype = int64
  Dataset /units/waveform_duration (VectorData) The trough-to-peak duration of the waveform on the peak channel. | shape = (1085, 1) | dtype = int64
  Dataset /units/waveform_mean (VectorData) the spike waveform mean for each spike unit | shape = (1085, 82, 50) | dtype = float64


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/lickPiezo (TimeSeries) Voltage values from a thin-film piezo connected to the lick spout, so that values are proportional to deflection of the spout and licks can be detected as peaks of the signal.
  Group /acquisition/wheel_position (TimeSeries) The position reading of the rotary encoder attached to the rubber wheel that the mouse pushes left and right with his forelimbs.
  file_create_date: ['2019-11-26T14:04:23.109455-08:00']
  Group /general/devices/0 (Device) 
  Group /general/devices/1 (Device) 
  Group /general/devices/2 (Device) 
  experiment_description: Large-scale Neuropixels recordings across brain regions of mice during a head-fixed visual discrimination task. 
  experimenter: ['Nick Steinmetz']
  Group /general/extracellular_ephys/Probe1 (ElectrodeGroup) Neuropixels Phase3A opt3
  Group /general/extracellular_ephys/Probe1/device (Device) 
  Group /general/extracellular_ephys/Probe2 (ElectrodeGroup) Neuropixels Phase3A opt3
  Group /general/extracellular_ephys/Probe2/device (Device) 
  Group /general/extracellular_ephys/Probe3 (ElectrodeGroup) Neuropixels Phase3A opt3
  Group /general/extracellular_ephys/Probe3/device (Device) 
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/axial_angle (VectorData) axial angle of probe (degrees). Zero means that without vertical and horizontal rotations, the probe contacts would be pointing up. Positive means "counterclockwise. | shape = (1122,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/ccf_ap (VectorData) The AP position in Allen Institute's Common Coordinate Framework. | shape = (1122,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/ccf_dv (VectorData) The DV position in Allen Institute's Common Coordinate Framework. | shape = (1122,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/ccf_lr (VectorData) The LR position in Allen Institute's Common Coordinate Framework. | shape = (1122,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/distance_advanced (VectorData) How far the probe was moved forward from its entry point. (microns). | shape = (1122,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/entry_point_ap (VectorData) anteroposterior position of probe entry point relative to bregma (microns). Positive means anterior | shape = (1122,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/entry_point_rl (VectorData) mediolateral position of probe entry point relative to midline (microns). Positive means right | shape = (1122,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (1122,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (1122,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (1122,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/horizontal_angle (VectorData) horizontal angle of probe (degrees), after vertical rotation. Zero means anterior. Positive means counterclockwise (i.e. left). | shape = (1122,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (1122,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (1122,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (1122,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/site_id (VectorData) The site number, in within-probe numbering, of the channel (in practice for this dataset this always starts at zero and counts up to 383 on each probe so is equivalent to the channel number - but if switches had been used, the site number could have been different than the channel number). | shape = (1122,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/site_position (VectorData) The x- and y-position of the site relative to the face of the probe (where the first column is across the face of the probe laterally and the second is the position along the length of the probe; the sites nearest the tip have second column=0). | shape = (1122, 2) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/vertical_angle (VectorData) vertical angle of probe (degrees). Zero means horizontal. Positive means pointing down | shape = (1122,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (1122,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (1122,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (1122,) | dtype = float64
  institution: University College London
  keywords: ['Neural coding' 'Neuropixels' 'mouse' 'brain-wide' 'vision'
   'visual discrimination' 'electrophysiology']
  lab: The Carandini and Harris Lab
  related_publications: ['DOI 10.1038/s41586-019-1787-x']
  Group /general/subject (Subject) 
  identifier: Forssmann_2017-11-01
  Group /intervals/spontaneous (TimeIntervals) Intervals of sufficient duration when nothing else is going on (no task or stimulus presentation
  Dataset /intervals/spontaneous/id (ElementIdentifiers)  | shape = (4,) | dtype = int64
  Dataset /intervals/spontaneous/start_time (VectorData) Start time of epoch, in seconds | shape = (4,) | dtype = float64
  Dataset /intervals/spontaneous/stop_time (VectorData) Stop time of epoch, in seconds | shape = (4,) | dtype = float64
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/feedback_time (VectorData) Times are relative to the same time base as every other time in the dataset, not to the start of the trial. | shape = (249,) | dtype = float64
  Dataset /intervals/trials/feedback_type (VectorData) Enumerated type. -1 for negative feedback (white noise burst); +1 for positive feedback (water reward delivery). | shape = (249,) | dtype = int64
  Dataset /intervals/trials/go_cue (VectorData) The 'goCue' is referred to as the 'auditory tone cue' in the manuscript. | shape = (249,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (249,) | dtype = int64
  Dataset /intervals/trials/included (VectorData) Importantly, while this variable gives inclusion criteria according to the definition of disengagement (see manuscript Methods), it does not give inclusion criteria based on the time of response, as used for most analyses in the paper. | shape = (249,) | dtype = bool
  Dataset /intervals/trials/rep_num (VectorData) Trials are repeated if they are "easy" trials (high contrast stimuli with large difference between the two sides, or the blank screen condition) and this keeps track of how many times the current trial's condition has been repeated. | shape = (249,) | dtype = float64
  Dataset /intervals/trials/response_choice (VectorData) Enumerated type. The response registered at the end of the trial, which determines the feedback according to the contrast condition. Note that in a small percentage of cases (~4%, see manuscript Methods) the initial wheel turn was in the opposite direction. -1 for Right choice (i.e. correct when stimuli are on the right); +1 for left choice; 0 for Nogo choice. | shape = (249,) | dtype = float64
  Dataset /intervals/trials/response_time (VectorData) Times are relative to the same time base as every other time in the dataset, not to the start of the trial. | shape = (249,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (249,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (249,) | dtype = float64
  Dataset /intervals/trials/visual_stimulus_left_contrast (VectorData) Proportion contrast. A value of 0.5 means 50% contrast. 0 is a blank screen: no change to any pixel values on that side (completely undetectable). | shape = (249,) | dtype = float64
  Dataset /intervals/trials/visual_stimulus_right_contrast (VectorData) Proportion contrast. A value of 0.5 means 50% contrast. 0 is a blank screen: no change to any pixel values on that side (completely undetectable). | shape = (249,) | dtype = float64
  Dataset /intervals/trials/visual_stimulus_time (VectorData) Times are relative to the same time base as every other time in the dataset, not to the start of the trial. | shape = (249,) | dtype = float64
  Group /processing/behavior (ProcessingModule) behavior module
  Group /processing/behavior/BehavioralEpochs (BehavioralEpochs) 
  Group /processing/behavior/BehavioralEpochs/wheel_moves (IntervalSeries) Detected wheel movements.
  Group /processing/behavior/BehavioralEvents (BehavioralEvents) 
  Group /processing/behavior/BehavioralEvents/lick_times (TimeSeries) Extracted times of licks, from the lickPiezo signal.
  Group /processing/behavior/BehavioralTimeSeries (BehavioralTimeSeries) 
  Group /processing/behavior/BehavioralTimeSeries/face_motion_energy (TimeSeries) Features extracted from the video of the frontal aspect of the subject, including the subject's face and forearms.
  Group /processing/behavior/PupilTracking (PupilTracking) 
  Group /processing/behavior/PupilTracking/eye_area (TimeSeries) Features extracted from the video of the right eye.
  Group /processing/behavior/PupilTracking/eye_xy_positions (TimeSeries) Features extracted from the video of the right eye.
  session_description: Neuropixels recording during visual discrimination in awake mice.
  session_start_time: 2017-11-01T12:00:00+00:00
  Group /stimulus/presentation/passive_beeps (TimeSeries) Auditory tones of the same frequency as the auditory tone cue in the task
  Group /stimulus/presentation/passive_click_times (TimeSeries) Opening of the reward valve, but with a clamp in place such that no water flows. Therefore the auditory sound of the valve is heard, but no water reward is obtained.
  Group /stimulus/presentation/passive_left_contrast (TimeSeries) Gratings of the same size, spatial freq, position, etc as during the discrimination task.
  Group /stimulus/presentation/passive_right_contrast (TimeSeries) Gratings of the same size, spatial freq, position, etc as during the discrimination task.
  Group /stimulus/presentation/passive_white_noise (TimeSeries) The sound that accompanies an incorrect response during the discrimination task.
  Group /stimulus/presentation/receptive_field_mapping_sparse_noise (TimeSeries) White squares shown on the screen with randomized positions and timing - see manuscript Methods.
  timestamps_reference_time: 2017-11-01T12:00:00+00:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/cluster_depths (VectorData) The position of the center of mass of the template of the cluster, relative to the probe. The deepest channel on the probe is depth=0, and the most superficial is depth=3820. Units: µm | shape = (2073, 1) | dtype = float64
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (2073,) | dtype = object
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (103650,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex)  | shape = (2073,) | dtype = int64
  Dataset /units/id (ElementIdentifiers)  | shape = (2073,) | dtype = int64
  Dataset /units/peak_channel (VectorData) The channel number of the location of the peak of the cluster's waveform. | shape = (2073, 1) | dtype = int64
  Dataset /units/phy_annotations (VectorData) 0 = noise (these are already excluded and don't appear in this dataset at all); 1 = MUA (i.e. presumed to contain spikes from multiple neurons; these are not analyzed in any analyses in the paper); 2 = Good (manually labeled); 3 = Unsorted. In this dataset 'Good' was applied in a few but not all datasets to included neurons, so in general the neurons with _phy_annotation>=2 are the ones that should be included. | shape = (2073,) | dtype = int64
  Dataset /units/sampling_rate (VectorData) Sampling rate, in Hz. | shape = (2073,) | dtype = float64
  Dataset /units/spike_amps (VectorData) The peak-to-trough amplitude, obtained from the template and template-scaling amplitude returned by Kilosort (not from the raw data). | shape = (13285502, 1) | dtype = float64
  Dataset /units/spike_amps_index (VectorIndex)  | shape = (2073,) | dtype = int64
  Dataset /units/spike_depths (VectorData) The position of the center of mass of the spike on the probe, determined from the principal component features returned by Kilosort. The deepest channel on the probe is depth=0, and the most superficial is depth=3820. | shape = (13285502, 1) | dtype = float32
  Dataset /units/spike_depths_index (VectorIndex)  | shape = (2073,) | dtype = int64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (13285502,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex)  | shape = (2073,) | dtype = int64
  Dataset /units/waveform_duration (VectorData) The trough-to-peak duration of the waveform on the peak channel. | shape = (2073, 1) | dtype = int64
  Dataset /units/waveform_mean (VectorData) the spike waveform mean for each spike unit | shape = (2073, 82, 50) | dtype = float64


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/lickPiezo (TimeSeries) Voltage values from a thin-film piezo connected to the lick spout, so that values are proportional to deflection of the spout and licks can be detected as peaks of the signal.
  Group /acquisition/wheel_position (TimeSeries) The position reading of the rotary encoder attached to the rubber wheel that the mouse pushes left and right with his forelimbs.
  file_create_date: ['2019-11-26T14:48:09.315049-08:00']
  Group /general/devices/0 (Device) 
  experiment_description: Large-scale Neuropixels recordings across brain regions of mice during a head-fixed visual discrimination task. 
  experimenter: ['Nick Steinmetz']
  Group /general/extracellular_ephys/Probe1 (ElectrodeGroup) Neuropixels Phase3A opt3
  Group /general/extracellular_ephys/Probe1/device (Device) 
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/axial_angle (VectorData) axial angle of probe (degrees). Zero means that without vertical and horizontal rotations, the probe contacts would be pointing up. Positive means "counterclockwise. | shape = (374,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/ccf_ap (VectorData) The AP position in Allen Institute's Common Coordinate Framework. | shape = (374,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/ccf_dv (VectorData) The DV position in Allen Institute's Common Coordinate Framework. | shape = (374,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/ccf_lr (VectorData) The LR position in Allen Institute's Common Coordinate Framework. | shape = (374,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/distance_advanced (VectorData) How far the probe was moved forward from its entry point. (microns). | shape = (374,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/entry_point_ap (VectorData) anteroposterior position of probe entry point relative to bregma (microns). Positive means anterior | shape = (374,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/entry_point_rl (VectorData) mediolateral position of probe entry point relative to midline (microns). Positive means right | shape = (374,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (374,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (374,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (374,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/horizontal_angle (VectorData) horizontal angle of probe (degrees), after vertical rotation. Zero means anterior. Positive means counterclockwise (i.e. left). | shape = (374,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (374,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (374,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (374,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/site_id (VectorData) The site number, in within-probe numbering, of the channel (in practice for this dataset this always starts at zero and counts up to 383 on each probe so is equivalent to the channel number - but if switches had been used, the site number could have been different than the channel number). | shape = (374,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/site_position (VectorData) The x- and y-position of the site relative to the face of the probe (where the first column is across the face of the probe laterally and the second is the position along the length of the probe; the sites nearest the tip have second column=0). | shape = (374, 2) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/vertical_angle (VectorData) vertical angle of probe (degrees). Zero means horizontal. Positive means pointing down | shape = (374,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (374,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (374,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (374,) | dtype = float64
  institution: University College London
  keywords: ['Neural coding' 'Neuropixels' 'mouse' 'brain-wide' 'vision'
   'visual discrimination' 'electrophysiology']
  lab: The Carandini and Harris Lab
  related_publications: ['DOI 10.1038/s41586-019-1787-x']
  Group /general/subject (Subject) 
  identifier: Lederberg_2017-12-10
  Group /intervals/spontaneous (TimeIntervals) Intervals of sufficient duration when nothing else is going on (no task or stimulus presentation
  Dataset /intervals/spontaneous/id (ElementIdentifiers)  | shape = (4,) | dtype = int64
  Dataset /intervals/spontaneous/start_time (VectorData) Start time of epoch, in seconds | shape = (4,) | dtype = float64
  Dataset /intervals/spontaneous/stop_time (VectorData) Stop time of epoch, in seconds | shape = (4,) | dtype = float64
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/feedback_time (VectorData) Times are relative to the same time base as every other time in the dataset, not to the start of the trial. | shape = (224,) | dtype = float64
  Dataset /intervals/trials/feedback_type (VectorData) Enumerated type. -1 for negative feedback (white noise burst); +1 for positive feedback (water reward delivery). | shape = (224,) | dtype = int64
  Dataset /intervals/trials/go_cue (VectorData) The 'goCue' is referred to as the 'auditory tone cue' in the manuscript. | shape = (224,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (224,) | dtype = int64
  Dataset /intervals/trials/included (VectorData) Importantly, while this variable gives inclusion criteria according to the definition of disengagement (see manuscript Methods), it does not give inclusion criteria based on the time of response, as used for most analyses in the paper. | shape = (224,) | dtype = bool
  Dataset /intervals/trials/rep_num (VectorData) Trials are repeated if they are "easy" trials (high contrast stimuli with large difference between the two sides, or the blank screen condition) and this keeps track of how many times the current trial's condition has been repeated. | shape = (224,) | dtype = float64
  Dataset /intervals/trials/response_choice (VectorData) Enumerated type. The response registered at the end of the trial, which determines the feedback according to the contrast condition. Note that in a small percentage of cases (~4%, see manuscript Methods) the initial wheel turn was in the opposite direction. -1 for Right choice (i.e. correct when stimuli are on the right); +1 for left choice; 0 for Nogo choice. | shape = (224,) | dtype = float64
  Dataset /intervals/trials/response_time (VectorData) Times are relative to the same time base as every other time in the dataset, not to the start of the trial. | shape = (224,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (224,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (224,) | dtype = float64
  Dataset /intervals/trials/visual_stimulus_left_contrast (VectorData) Proportion contrast. A value of 0.5 means 50% contrast. 0 is a blank screen: no change to any pixel values on that side (completely undetectable). | shape = (224,) | dtype = float64
  Dataset /intervals/trials/visual_stimulus_right_contrast (VectorData) Proportion contrast. A value of 0.5 means 50% contrast. 0 is a blank screen: no change to any pixel values on that side (completely undetectable). | shape = (224,) | dtype = float64
  Dataset /intervals/trials/visual_stimulus_time (VectorData) Times are relative to the same time base as every other time in the dataset, not to the start of the trial. | shape = (224,) | dtype = float64
  Group /processing/behavior (ProcessingModule) behavior module
  Group /processing/behavior/BehavioralEpochs (BehavioralEpochs) 
  Group /processing/behavior/BehavioralEpochs/wheel_moves (IntervalSeries) Detected wheel movements.
  Group /processing/behavior/BehavioralEvents (BehavioralEvents) 
  Group /processing/behavior/BehavioralEvents/lick_times (TimeSeries) Extracted times of licks, from the lickPiezo signal.
  Group /processing/behavior/BehavioralTimeSeries (BehavioralTimeSeries) 
  Group /processing/behavior/BehavioralTimeSeries/face_motion_energy (TimeSeries) Features extracted from the video of the frontal aspect of the subject, including the subject's face and forearms.
  Group /processing/behavior/PupilTracking (PupilTracking) 
  Group /processing/behavior/PupilTracking/eye_area (TimeSeries) Features extracted from the video of the right eye.
  Group /processing/behavior/PupilTracking/eye_xy_positions (TimeSeries) Features extracted from the video of the right eye.
  session_description: Neuropixels recording during visual discrimination in awake mice.
  session_start_time: 2017-12-10T12:00:00+00:00
  Group /stimulus/presentation/passive_beeps (TimeSeries) Auditory tones of the same frequency as the auditory tone cue in the task
  Group /stimulus/presentation/passive_click_times (TimeSeries) Opening of the reward valve, but with a clamp in place such that no water flows. Therefore the auditory sound of the valve is heard, but no water reward is obtained.
  Group /stimulus/presentation/passive_left_contrast (TimeSeries) Gratings of the same size, spatial freq, position, etc as during the discrimination task.
  Group /stimulus/presentation/passive_right_contrast (TimeSeries) Gratings of the same size, spatial freq, position, etc as during the discrimination task.
  Group /stimulus/presentation/passive_white_noise (TimeSeries) The sound that accompanies an incorrect response during the discrimination task.
  Group /stimulus/presentation/receptive_field_mapping_sparse_noise (TimeSeries) White squares shown on the screen with randomized positions and timing - see manuscript Methods.
  timestamps_reference_time: 2017-12-10T12:00:00+00:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/cluster_depths (VectorData) The position of the center of mass of the template of the cluster, relative to the probe. The deepest channel on the probe is depth=0, and the most superficial is depth=3820. Units: µm | shape = (727, 1) | dtype = float64
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (727,) | dtype = object
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (36350,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex)  | shape = (727,) | dtype = int64
  Dataset /units/id (ElementIdentifiers)  | shape = (727,) | dtype = int64
  Dataset /units/peak_channel (VectorData) The channel number of the location of the peak of the cluster's waveform. | shape = (727, 1) | dtype = int64
  Dataset /units/phy_annotations (VectorData) 0 = noise (these are already excluded and don't appear in this dataset at all); 1 = MUA (i.e. presumed to contain spikes from multiple neurons; these are not analyzed in any analyses in the paper); 2 = Good (manually labeled); 3 = Unsorted. In this dataset 'Good' was applied in a few but not all datasets to included neurons, so in general the neurons with _phy_annotation>=2 are the ones that should be included. | shape = (727,) | dtype = int64
  Dataset /units/sampling_rate (VectorData) Sampling rate, in Hz. | shape = (727,) | dtype = float64
  Dataset /units/spike_amps (VectorData) The peak-to-trough amplitude, obtained from the template and template-scaling amplitude returned by Kilosort (not from the raw data). | shape = (5724792, 1) | dtype = float64
  Dataset /units/spike_amps_index (VectorIndex)  | shape = (727,) | dtype = int64
  Dataset /units/spike_depths (VectorData) The position of the center of mass of the spike on the probe, determined from the principal component features returned by Kilosort. The deepest channel on the probe is depth=0, and the most superficial is depth=3820. | shape = (5724792, 1) | dtype = float32
  Dataset /units/spike_depths_index (VectorIndex)  | shape = (727,) | dtype = int64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (5724792,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex)  | shape = (727,) | dtype = int64
  Dataset /units/waveform_duration (VectorData) The trough-to-peak duration of the waveform on the peak channel. | shape = (727, 1) | dtype = int64
  Dataset /units/waveform_mean (VectorData) the spike waveform mean for each spike unit | shape = (727, 82, 50) | dtype = float64
