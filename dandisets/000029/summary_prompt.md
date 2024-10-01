
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000029/0.231017.1959
name: Test dataset for development purposes
contributor: [{'name': 'Last, First', 'roleName': ['dcite:Author', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0003-3456-2493', 'affiliation': [{'name': 'An Institution', 'roleName': [], 'schemaKey': 'Affiliation', 'contactPoint': [], 'includeInCitation': False}], 'includeInCitation': True}, {'url': 'https://dandiarchive.org', 'name': 'Test Org', 'email': 'michael.vandenburgh@kitware.com', 'roleName': ['dcite:Sponsor'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/000000000', 'contactPoint': [], 'includeInCitation': True}, {}]
description: Should be ignored by regular mojgjhhj.  fjrtalddgdfgdfgs, and not relied upon being static or ever correct.
Должно быть введено на Английском, но почему бы нам не проверить всю эту кухню 
ΔЙקم๗あ
abcdefghi
assetsSummary: {'species': [{'name': 'Macaca mulatta - Rhesus monkey', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9544'}, {'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}, {'name': 'Rattus norvegicus - Norway rat', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10116'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}, {'name': 'behavioral approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 39011902, 'numberOfFiles': 9, 'numberOfSubjects': 5, 'variableMeasured': ['ProcessingModule', 'ElectrodeGroup', 'BehavioralEvents', 'Units'], 'measurementTechnique': [{'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000029 has 5 NWB files.
1 of these NWB files are of type 1.
1 of these NWB files are of type 2.
1 of these NWB files are of type 3.
1 of these NWB files are of type 4.
1 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2018-04-15T12:00:00-04:00']
  Group /general/subject (Subject) 
  identifier: TEST_Subject
  session_description: a file to test writing and reading a Subject
  session_start_time: 1971-01-01T12:00:00+00:00
  timestamps_reference_time: 1971-01-01T12:00:00+00:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/lick_times (BehavioralEvents) 
  Group /acquisition/lick_times/lick_left_times (TimeSeries) no description
  Group /acquisition/lick_times/lick_right_times (TimeSeries) no description
  file_create_date: ['2019-10-07T17:40:41.133533-05:00']
  Group /general/devices/H-129 (Device) 
  experiment_description: Extracellular electrophysiology recordings performed on mouse anterior lateral motor cortex (ALM) in delay response task. Neural activity from two neuron populations, pyramidal track upper and lower, were characterized, in relation to movement execution.
  experimenter: Mike Economo
  Group /general/extracellular_ephys/H-129: 64 (ElectrodeGroup) N/A
  Group /general/extracellular_ephys/H-129: 64/device (Device) 
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (64,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (64,) | dtype = float64
  institution: Janelia Research Campus
  keywords: ['motor planning' 'premotor cortex' 'preparatory activity'
   'extracellular electrophysiology']
  related_publications: doi:10.1038/s41586-018-0642-9
  Group /general/subject (Subject) 
  identifier: anm369962_2017-03-10_1
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/cue_start_time (VectorData) onset of response period | shape = (275,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (275,) | dtype = int32
  Dataset /intervals/trials/is_good (VectorData) good/bad status of trial (bad trials are not analyzed) | shape = (275,) | dtype = int32
  Dataset /intervals/trials/pole_in_time (VectorData) onset of sample period | shape = (275,) | dtype = float64
  Dataset /intervals/trials/pole_out_time (VectorData) onset of the delay period | shape = (275,) | dtype = float64
  Dataset /intervals/trials/response (VectorData)  | shape = (275,) | dtype = object
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (275,) | dtype = float64
  Dataset /intervals/trials/stim_present (VectorData) is this a stim or no-stim trial | shape = (275,) | dtype = int32
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (275,) | dtype = float64
  Dataset /intervals/trials/type (VectorData)  | shape = (275,) | dtype = object
  session_description: 
  session_start_time: 2017-03-10T00:00:00-06:00
  timestamps_reference_time: 2017-03-10T00:00:00-06:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/cell_type (VectorData) cell type (e.g. wide width, narrow width spiking) | shape = (79,) | dtype = object
  Dataset /units/depth (VectorData) depth this unit (um) | shape = (79,) | dtype = float64
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (79,) | dtype = int32
  Dataset /units/electrodes_index (VectorIndex)  | shape = (79,) | dtype = int32
  Dataset /units/id (ElementIdentifiers)  | shape = (79,) | dtype = int32
  Dataset /units/quality (VectorData) quality of the spike sorted unit (e.g. excellent, good, poor, fair, etc.) | shape = (79,) | dtype = object
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (793090,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex)  | shape = (79,) | dtype = int32


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/lick_times (BehavioralEvents) 
  Group /acquisition/lick_times/lick_left_times (TimeSeries) no description
  Group /acquisition/lick_times/lick_right_times (TimeSeries) no description
  file_create_date: ['2019-10-07T17:41:38.493346-05:00']
  Group /general/devices/H-116 (Device) 
  experiment_description: Extracellular electrophysiology recordings performed on mouse anterior lateral motor cortex (ALM) in delay response task. Neural activity from two neuron populations, pyramidal track upper and lower, were characterized, in relation to movement execution.
  experimenter: Mike Economo
  Group /general/extracellular_ephys/H-116: 64 (ElectrodeGroup) N/A
  Group /general/extracellular_ephys/H-116: 64/device (Device) 
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (64,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (64,) | dtype = float64
  institution: Janelia Research Campus
  keywords: ['motor planning' 'premotor cortex' 'preparatory activity'
   'extracellular electrophysiology']
  related_publications: doi:10.1038/s41586-018-0642-9
  Group /general/subject (Subject) 
  identifier: anm369963_2017-02-26_0
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/cue_start_time (VectorData) onset of response period | shape = (295,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (295,) | dtype = int32
  Dataset /intervals/trials/is_good (VectorData) good/bad status of trial (bad trials are not analyzed) | shape = (295,) | dtype = int32
  Dataset /intervals/trials/pole_in_time (VectorData) onset of sample period | shape = (295,) | dtype = float64
  Dataset /intervals/trials/pole_out_time (VectorData) onset of the delay period | shape = (295,) | dtype = float64
  Dataset /intervals/trials/response (VectorData)  | shape = (295,) | dtype = object
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (295,) | dtype = float64
  Dataset /intervals/trials/stim_present (VectorData) is this a stim or no-stim trial | shape = (295,) | dtype = int32
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (295,) | dtype = float64
  Dataset /intervals/trials/type (VectorData)  | shape = (295,) | dtype = object
  session_description: 
  session_start_time: 2017-02-26T00:00:00-06:00
  timestamps_reference_time: 2017-02-26T00:00:00-06:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/cell_type (VectorData) cell type (e.g. wide width, narrow width spiking) | shape = (49,) | dtype = object
  Dataset /units/depth (VectorData) depth this unit (um) | shape = (49,) | dtype = float64
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (49,) | dtype = int32
  Dataset /units/electrodes_index (VectorIndex)  | shape = (49,) | dtype = int32
  Dataset /units/id (ElementIdentifiers)  | shape = (49,) | dtype = int32
  Dataset /units/quality (VectorData) quality of the spike sorted unit (e.g. excellent, good, poor, fair, etc.) | shape = (49,) | dtype = object
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (759789,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex)  | shape = (49,) | dtype = int32


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/lick_times (BehavioralEvents) 
  Group /acquisition/lick_times/lick_left_times (TimeSeries) no description
  Group /acquisition/lick_times/lick_right_times (TimeSeries) no description
  file_create_date: ['2019-10-07T17:42:31.649019-05:00']
  Group /general/devices/H-117 (Device) 
  experiment_description: Extracellular electrophysiology recordings performed on mouse anterior lateral motor cortex (ALM) in delay response task. Neural activity from two neuron populations, pyramidal track upper and lower, were characterized, in relation to movement execution.
  experimenter: Mike Economo
  Group /general/extracellular_ephys/H-117: 64 (ElectrodeGroup) N/A
  Group /general/extracellular_ephys/H-117: 64/device (Device) 
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (64,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (64,) | dtype = float64
  institution: Janelia Research Campus
  keywords: ['motor planning' 'premotor cortex' 'preparatory activity'
   'extracellular electrophysiology']
  related_publications: doi:10.1038/s41586-018-0642-9
  Group /general/subject (Subject) 
  identifier: anm369964_2017-03-20_0
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/cue_start_time (VectorData) onset of response period | shape = (319,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (319,) | dtype = int32
  Dataset /intervals/trials/is_good (VectorData) good/bad status of trial (bad trials are not analyzed) | shape = (319,) | dtype = int32
  Dataset /intervals/trials/pole_in_time (VectorData) onset of sample period | shape = (319,) | dtype = float64
  Dataset /intervals/trials/pole_out_time (VectorData) onset of the delay period | shape = (319,) | dtype = float64
  Dataset /intervals/trials/response (VectorData)  | shape = (319,) | dtype = object
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (319,) | dtype = float64
  Dataset /intervals/trials/stim_present (VectorData) is this a stim or no-stim trial | shape = (319,) | dtype = int32
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (319,) | dtype = float64
  Dataset /intervals/trials/type (VectorData)  | shape = (319,) | dtype = object
  session_description: 
  session_start_time: 2017-03-20T00:00:00-05:00
  timestamps_reference_time: 2017-03-20T00:00:00-05:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/cell_type (VectorData) cell type (e.g. wide width, narrow width spiking) | shape = (55,) | dtype = object
  Dataset /units/depth (VectorData) depth this unit (um) | shape = (55,) | dtype = float64
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (55,) | dtype = int32
  Dataset /units/electrodes_index (VectorIndex)  | shape = (55,) | dtype = int32
  Dataset /units/id (ElementIdentifiers)  | shape = (55,) | dtype = int32
  Dataset /units/quality (VectorData) quality of the spike sorted unit (e.g. excellent, good, poor, fair, etc.) | shape = (55,) | dtype = object
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (918242,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex)  | shape = (55,) | dtype = int32


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2023-01-12T22:14:16.171398-08:00']
  experiment_description: Single unit recordings from chronically implanted microwire                 electrode array in PMd/M1 used for BMI control using Kalman filter decoder. File includes BMI-unit spike counts,                 BMI task parameters, and BMI cursor data used for analysis. TimeSeries are reported at 60 hz, BMI update rate was 10 Hz.                 Raw electrophysiolgy data files are not included
  experimenter: ['Khanna, Preeya']
  institution: UC Berkeley
  keywords: ['BMI control' 'kalman filter' 'chronic electrophysiolgy' 'motor cortex'
   'premotor cortex' 'microwire arrays' 'monkey']
  lab: Carmena lab
  session_id: session8
  Group /general/subject (Subject) 
  identifier: MonkeyG_session8
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (139,) | dtype = int64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (139,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (139,) | dtype = float64
  Group /processing/behavior (ProcessingModule) BMI spike counts and behavior
  Group /processing/behavior/cursor (TimeSeries) 2D cursor position (x, y) 
  Group /processing/behavior/decoder_state (TimeSeries) decoder state (2d-pos, 2d-vel, offset)
  Group /processing/behavior/obs_details (TimeSeries) description of obstacle shape (square, and side length of square in cm, is "na" if no obstacle
  Group /processing/behavior/obstacle_position (TimeSeries) position of obstacle (center of square, is (0,0) if no obstacle)
  Group /processing/behavior/spike_counts (TimeSeries) binned spike counts used for BMI control
  Group /processing/behavior/target_state (TimeSeries) target state (2d-pos, 2d-vel, offset) -- location of target
  Group /processing/behavior/te_num (TimeSeries) task entry number for trials (corresponds to task ID in bmi3d db.sql file
  Group /processing/behavior/teblk_4558_cursor_radius (TimeSeries) cursor radius (cm)
  Group /processing/behavior/teblk_4558_decoder_A (TimeSeries) kalman filter decoder A matrix (cursor dynamics, 5 x 5 )
  Group /processing/behavior/teblk_4558_decoder_C (TimeSeries) kalman filter deocder C matrix (neural encoding of cursor 5 x Nneurons)
  Group /processing/behavior/teblk_4558_decoder_Q (TimeSeries) kalman filter deocder Q matrix (noise of cusror encoding Nneurons x Nneurons)
  Group /processing/behavior/teblk_4558_decoder_W (TimeSeries) kalman filter decoder W matrix (noise of cursor dynamics 5 x 5 )
  Group /processing/behavior/teblk_4558_decoder_ssF (TimeSeries) kalman filter steady state F matrix (cursor dynamics 5 x 5)
  Group /processing/behavior/teblk_4558_decoder_ssKG (TimeSeries) kalman filter steady state K matrix (kalman gain, neural update 5 x Nneurons)
  Group /processing/behavior/teblk_4558_plant_type (TimeSeries) plant type (name of plant corresponding to BMI3D code)
  Group /processing/behavior/teblk_4558_reward time (sec) (TimeSeries) reward time (sec) -- how long juicer was open to deliver rewards
  Group /processing/behavior/teblk_4558_target_radius (TimeSeries) target radius (cm)
  Group /processing/behavior/teblk_4560_cursor_radius (TimeSeries) cursor radius (cm)
  Group /processing/behavior/teblk_4560_decoder_A (TimeSeries) kalman filter decoder A matrix (cursor dynamics, 5 x 5 )
  Group /processing/behavior/teblk_4560_decoder_C (TimeSeries) kalman filter deocder C matrix (neural encoding of cursor 5 x Nneurons)
  Group /processing/behavior/teblk_4560_decoder_Q (TimeSeries) kalman filter deocder Q matrix (noise of cusror encoding Nneurons x Nneurons)
  Group /processing/behavior/teblk_4560_decoder_W (TimeSeries) kalman filter decoder W matrix (noise of cursor dynamics 5 x 5 )
  Group /processing/behavior/teblk_4560_decoder_ssF (TimeSeries) kalman filter steady state F matrix (cursor dynamics 5 x 5)
  Group /processing/behavior/teblk_4560_decoder_ssKG (TimeSeries) kalman filter steady state K matrix (kalman gain, neural update 5 x Nneurons)
  Group /processing/behavior/teblk_4560_plant_type (TimeSeries) plant type (name of plant corresponding to BMI3D code)
  Group /processing/behavior/teblk_4560_reward time (sec) (TimeSeries) reward time (sec) -- how long juicer was open to deliver rewards
  Group /processing/behavior/teblk_4560_target_radius (TimeSeries) target radius (cm)
  Group /processing/behavior/update_bmi (TimeSeries) binary variable where "1" indicates bins which BMI was updated (10 hz, task runs at 60 hz)
  session_description: Monkey performing 2D cursor BMI
  session_start_time: 2016-03-19T00:00:00-07:00
  timestamps_reference_time: 2016-03-19T00:00:00-07:00
