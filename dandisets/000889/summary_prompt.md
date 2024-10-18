
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000889/0.241014.2127
name: Thermal Plaid Replay Experiments - steep gradients
contributor: [{'name': 'National Institutes of Health (NIH)', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': '5 R01 NS 123887-03'}, {'name': 'Anderson, Lindsay', 'roleName': ['dcite:DataCollector'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Haesemeyer, Martin', 'email': 'martin.haesemeyer@osumc.edu', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'includeInCitation': True}]
description: Larval zebrafish experiencing the replay of another fish that navigated a virtual thermal plaid created by an infrared stimulus laser in a preheated experimental chamber
assetsSummary: {'species': [{'name': 'Danio rerio - Zebra fish', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_7955'}], 'approach': [{'name': 'behavioral approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 1831507548, 'numberOfFiles': 52, 'numberOfSubjects': 104, 'variableMeasured': ['ProcessingModule', 'SpatialSeries', 'Position', 'CompassDirection'], 'measurementTechnique': [{'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000889 has 52 NWB files.
52 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Overview (Images) Chamber overview at start of experiment
  Dataset /acquisition/Overview/ArenaTrack (RGBAImage) Arena track plotted during tail extraction | shape = (433, 430, 4) | dtype = uint8
  file_create_date: ['2024-02-07T10:15:07.319775-05:00']
  Group /general/devices/LaserTrackingRig_1 (Device) OSU Haesemeyer Lab, Laser Tracking Rig 1 (as in Haesemeyer et al., 2015)
  experiment_description: Experiment name: la_replay_01_0119
  
  Fish name: nac het
  
  Fish DOB: 1/19/2024 12:00:00 AM
  
  Dish center (x, y): (400, 400)
  
  Dish radius: 360
  
  ------
  
  Comment:
  
  ---batch #4; experiment #46---
  
  ------
  
  Start date: 1/25/2024
  
  Start Time: 10:30 AM
  
  
  
  Frame rate: 250 Hz
  
  Resolution: 8 px/mm
  
  
  
  
  
  Replay experiment of: Plaid experiment
  
  -----------------------------------------------------------
  
  Original info file data follows:
  
  	Experiment name: la_plaid_01_0119
  
  	Fish name: nac het
  
  	Fish DOB: 1/19/2024 12:00:00 AM
  
  	Dish center (x, y): (400, 400)
  
  	Dish radius: 360
  
  	------
  
  	Comment:
  
  	---batch #4; experiment #46---
  
  	------
  
  	Start date: 1/25/2024
  
  	Start Time: 9:38 AM
  
  	
  
  	Frame rate: 250 Hz
  
  	Resolution: 8 px/mm
  
  	
  
  	
  
  	Thermal plaid experiment
  
  	Habituation length 600 [s]
  
  	Pre gradient length 1200 [s]
  
  	Plaid length 1200 [s]
  
  	Trough power at sample 500 [mW]
  
  	Peak power at sample 2000 [mW]
  
  	Plaid period 15 [mm]
  
  	Plaid period 120 [px]
  
  	Plaid offset X 26 [px]
  
  	Plaid offset Y 394 [px]
  
  	
  
  	--------------
  
  	Experiment ended:
  
  	1/25/2024 10:28:09 AM
  
  -----------------------------------------------------------
  
  
  
  --------------
  
  Experiment ended:
  
  1/25/2024 11:20:31 AM
  
  experimenter: ['Lindsay Anderson']
  institution: THE Ohio State University
  Group /general/subject (Subject) 
  identifier: la_replay_01_0119_nac het_#2024_1_25
  Group /processing/Experimental information (ProcessingModule) Ongoing experimental variables
  Group /processing/Experimental information/Experiment phase (TimeSeries) Experimental phase
  Group /processing/Recorded behavior data (ProcessingModule) Behavior of fish. Fish type: nac het
  Group /processing/Recorded behavior data/Cumulative tail angle (Position) 
  Group /processing/Recorded behavior data/Cumulative tail angle/Cumulative tail angle (SpatialSeries) Cumulative bend angle of the tail in radians.
  Group /processing/Recorded behavior data/Heading (CompassDirection) 
  Group /processing/Recorded behavior data/Heading/Fish heading (SpatialSeries) Absolute fish heading in radians.
  Group /processing/Recorded behavior data/Position (Position) 
  Group /processing/Recorded behavior data/Position/Chamber position (SpatialSeries) Position of the fish within the swim lane in mm coordinates.
  Dataset /scratch/Experiment type (ScratchData)  | shape = () | dtype = <U39
  Dataset /scratch/Raw Experiment metadata (ScratchData)  | shape = () | dtype = <U1187
  session_description: Thermal plaid replay experiment
  session_start_time: 2024-01-25T10:30:00-05:00
  Group /stimulus/presentation/IR Laser Power at Sample (TimeSeries) 980 nm tracking laser power at sample
  timestamps_reference_time: 2024-01-25T10:30:00-05:00
