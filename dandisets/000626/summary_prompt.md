
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000626/draft
name: Neural Organoid Ephys Trace
contributor: [{'name': 'Blauvelt, Lon', 'email': 'lblauvel@ucsc.edu', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}]
description: Captured originally with a MaxWell BioSystems CMOS-based High-Density Microelectrode Array.
assetsSummary: {'species': [{'name': 'Macaca mulatta - Rhesus monkey', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9544'}], 'approach': [], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 18295752, 'numberOfFiles': 1, 'numberOfSubjects': 1, 'variableMeasured': ['ProcessingModule'], 'measurementTechnique': [{'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000626 has 1 NWB files.
1 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
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
