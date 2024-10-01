
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000338/draft
name: groupweight BMI
contributor: [{'name': 'Zhang, Chenguang', 'email': 'chz95@pitt.edu', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}]
description: This dataset is the group-weight BMI experiment data. 
assetsSummary: {'species': [{'name': 'Macaca mulatta - Rhesus monkey', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9544'}], 'approach': [], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 740232574, 'numberOfFiles': 2, 'numberOfSubjects': 2, 'variableMeasured': [], 'measurementTechnique': []}

Dandiset 000338 has 2 NWB files.
1 of these NWB files are of type 1.
1 of these NWB files are of type 2.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2022-12-02T12:08:48.008354-05:00' '2022-12-02T12:22:38.868505-05:00']
  experiment_description: Two rhesus monkey was doing the grouopweight method brain control experiment and get improved through time.
  experimenter: ['Zhang, Chenguang']
  institution: Beijing Normal University, Beijing, China
  keywords: ['BCI, BMI, BBMI leaning']
  Group /general/subject (Subject) 
  identifier: ident1
  Group /intervals/trials (TimeIntervals) the summary data of all trials
  Dataset /intervals/trials/correct (VectorData) whether the trial is correct 1 or run out of time 0 | shape = (2119,) | dtype = uint8
  Dataset /intervals/trials/cursor_pos (VectorData) The cursor position in the current trial, first row as time and 2nd, 3rd row as x-, and y- position | shape = (1419107, 3) | dtype = float64
  Dataset /intervals/trials/cursor_pos_index (VectorIndex) cursor_position_index | shape = (2119,) | dtype = uint64
  Dataset /intervals/trials/cursor_size (VectorData) the size of the cursor  | shape = (2119,) | dtype = float64
  Dataset /intervals/trials/cursor_vel (VectorData) The cursor velocity in the current trial, first row as time and 2nd, 3rd row as x-, and y- velocity | shape = (2949505, 3) | dtype = float64
  Dataset /intervals/trials/cursor_vel_index (VectorIndex) cursor_velocity_index | shape = (2119,) | dtype = uint64
  Dataset /intervals/trials/duration (VectorData) the duration of current trial | shape = (2119,) | dtype = float64
  Dataset /intervals/trials/fr_freeze (VectorData) The fr_freeze in the current trial, each row is each channel | shape = (1333371, 96) | dtype = float64
  Dataset /intervals/trials/fr_freeze_index (VectorIndex) fr_freeze_index | shape = (2119,) | dtype = uint64
  Dataset /intervals/trials/fr_mov (VectorData) The fr_mov in the current trial, each row is each channel | shape = (1460450, 96) | dtype = float64
  Dataset /intervals/trials/fr_mov_index (VectorIndex) fr_mov_index | shape = (2119,) | dtype = uint64
  Dataset /intervals/trials/freeze_t (VectorData) freeze time of the trial | shape = (2251,) | dtype = float64
  Dataset /intervals/trials/freeze_t_index (VectorIndex) Index into column freeze_t | shape = (2119,) | dtype = uint64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (2119,) | dtype = int64
  Dataset /intervals/trials/monkey (VectorData) the monkey name of the trial | shape = (2119,) | dtype = float64
  Dataset /intervals/trials/rotation (VectorData) rotation of the target relative to the cursor departure position | shape = (2119,) | dtype = float64
  Dataset /intervals/trials/spike_freeze (VectorData) The spike_freeze in the current trial, each row is each channel | shape = (1333371, 96) | dtype = uint8
  Dataset /intervals/trials/spike_freeze_index (VectorIndex) spike_freeze_index | shape = (2119,) | dtype = uint64
  Dataset /intervals/trials/spike_mov (VectorData) The spike_mov in the current trial, each row is each channel | shape = (1460450, 96) | dtype = uint8
  Dataset /intervals/trials/spike_mov_index (VectorIndex) spike_mov_index | shape = (2119,) | dtype = uint64
  Dataset /intervals/trials/ss_num (VectorData) the session number of the trial | shape = (2119,) | dtype = float64
  Dataset /intervals/trials/startEndLength (VectorData) the distance of the target | shape = (2119,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) start times of the current trial | shape = (2119,) | dtype = float64
  Dataset /intervals/trials/states (VectorData) the position of the target | shape = (13002,) | dtype = float64
  Dataset /intervals/trials/states_index (VectorIndex) states_index | shape = (2119,) | dtype = uint64
  Dataset /intervals/trials/states_t (VectorData) the position of the target | shape = (13002,) | dtype = float64
  Dataset /intervals/trials/states_t_index (VectorIndex) states_t_index | shape = (2119,) | dtype = uint64
  Dataset /intervals/trials/stop_time (VectorData) start times of the current trial | shape = (2119,) | dtype = float64
  Dataset /intervals/trials/target (VectorData) the position of the target | shape = (2119,) | dtype = float64
  Dataset /intervals/trials/target_size (VectorData) the size of the target | shape = (2119,) | dtype = float64
  Dataset /intervals/trials/trajecRate (VectorData) the trajectoryLength over the distance | shape = (2119,) | dtype = float64
  Dataset /intervals/trials/trajectoryLength (VectorData) the trajectory length of the target | shape = (2119,) | dtype = float64
  Dataset /intervals/trials/trial_num (VectorData) the trial number of all the trials | shape = (2119,) | dtype = float64
  Dataset /intervals/trials/unfreeze_t (VectorData) unfreeze time of the trial | shape = (2119,) | dtype = float64
  session_description: monkeyT
  session_start_time: 2017-01-01T00:00:00.000000-05:00
  timestamps_reference_time: 2017-01-01T00:00:00.000000-05:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2022-12-02T12:08:48.008354-05:00' '2022-12-02T12:22:51.474777-05:00']
  experiment_description: Two rhesus monkey was doing the grouopweight method brain control experiment and get improved through time.
  experimenter: ['Zhang, Chenguang']
  institution: Beijing Normal University, Beijing, China
  keywords: ['BCI, BMI, BBMI leaning']
  Group /general/subject (Subject) 
  identifier: ident1
  Group /intervals/trials (TimeIntervals) the summary data of all trials
  Dataset /intervals/trials/correct (VectorData) whether the trial is correct 1 or run out of time 0 | shape = (3772,) | dtype = uint8
  Dataset /intervals/trials/cursor_pos (VectorData) The cursor position in the current trial, first row as time and 2nd, 3rd row as x-, and y- position | shape = (2222763, 3) | dtype = float64
  Dataset /intervals/trials/cursor_pos_index (VectorIndex) cursor_position_index | shape = (3772,) | dtype = uint64
  Dataset /intervals/trials/cursor_size (VectorData) the size of the cursor  | shape = (3772,) | dtype = float64
  Dataset /intervals/trials/cursor_vel (VectorData) The cursor velocity in the current trial, first row as time and 2nd, 3rd row as x-, and y- velocity | shape = (2222763, 3) | dtype = float64
  Dataset /intervals/trials/cursor_vel_index (VectorIndex) cursor_velocity_index | shape = (3772,) | dtype = uint64
  Dataset /intervals/trials/duration (VectorData) the duration of current trial | shape = (3772,) | dtype = float64
  Dataset /intervals/trials/fr_freeze (VectorData) The fr_freeze in the current trial, each row is each channel | shape = (3772, 96) | dtype = float64
  Dataset /intervals/trials/fr_freeze_index (VectorIndex) fr_freeze_index | shape = (3772,) | dtype = uint64
  Dataset /intervals/trials/fr_mov (VectorData) The fr_mov in the current trial, each row is each channel | shape = (2220920, 96) | dtype = float64
  Dataset /intervals/trials/fr_mov_index (VectorIndex) fr_mov_index | shape = (3772,) | dtype = uint64
  Dataset /intervals/trials/freeze_t (VectorData) freeze time of the trial | shape = (3772,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (3772,) | dtype = int64
  Dataset /intervals/trials/monkey (VectorData) the monkey name of the trial | shape = (3772,) | dtype = float64
  Dataset /intervals/trials/rotation (VectorData) rotation of the target relative to the cursor departure position | shape = (3772,) | dtype = float64
  Dataset /intervals/trials/spike_freeze (VectorData) The spike_freeze in the current trial, each row is each channel | shape = (3772, 96) | dtype = uint8
  Dataset /intervals/trials/spike_freeze_index (VectorIndex) spike_freeze_index | shape = (3772,) | dtype = uint64
  Dataset /intervals/trials/spike_mov (VectorData) The spike_mov in the current trial, each row is each channel | shape = (2220920, 96) | dtype = uint8
  Dataset /intervals/trials/spike_mov_index (VectorIndex) spike_mov_index | shape = (3772,) | dtype = uint64
  Dataset /intervals/trials/ss_num (VectorData) the session number of the trial | shape = (3772,) | dtype = float64
  Dataset /intervals/trials/startEndLength (VectorData) the distance of the target | shape = (3772,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) start times of the current trial | shape = (3772,) | dtype = float64
  Dataset /intervals/trials/states (VectorData) the position of the target | shape = (17853,) | dtype = float64
  Dataset /intervals/trials/states_index (VectorIndex) states_index | shape = (3772,) | dtype = uint64
  Dataset /intervals/trials/states_t (VectorData) the position of the target | shape = (17853,) | dtype = float64
  Dataset /intervals/trials/states_t_index (VectorIndex) states_t_index | shape = (3772,) | dtype = uint64
  Dataset /intervals/trials/stop_time (VectorData) start times of the current trial | shape = (3772,) | dtype = float64
  Dataset /intervals/trials/target (VectorData) the position of the target | shape = (3772,) | dtype = float64
  Dataset /intervals/trials/target_size (VectorData) the size of the target | shape = (3772,) | dtype = float64
  Dataset /intervals/trials/trajecRate (VectorData) the trajectoryLength over the distance | shape = (3772,) | dtype = float64
  Dataset /intervals/trials/trajectoryLength (VectorData) the trajectory length of the target | shape = (3772,) | dtype = float64
  Dataset /intervals/trials/trial_num (VectorData) the trial number of all the trials | shape = (3772,) | dtype = float64
  Dataset /intervals/trials/unfreeze_t (VectorData) unfreeze time of the trial | shape = (3772,) | dtype = float64
  session_description: monkeyK
  session_start_time: 2016-01-01T00:00:00.000000-05:00
  timestamps_reference_time: 2016-01-01T00:00:00.000000-05:00
