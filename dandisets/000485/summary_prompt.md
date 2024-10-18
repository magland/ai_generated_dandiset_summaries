
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000485/0.241014.2127
name: Thermal Plaid Experiments
contributor: [{'name': 'National Institutes of Health (NIH)', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': '5 R01 NS 123887-02'}, {'name': 'Haesemeyer, Martin', 'email': 'martin.haesemeyer@osumc.edu', 'roleName': ['dcite:DataCollector', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'includeInCitation': True}]
description: Larval zebrafish navigating a virtual thermal plaid created by an infrared stimulus laser
assetsSummary: {'species': [{'name': 'Danio rerio - Zebra fish', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_7955'}], 'approach': [{'name': 'behavioral approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 1299698178, 'numberOfFiles': 37, 'numberOfSubjects': 37, 'variableMeasured': ['SpatialSeries', 'Position', 'ProcessingModule', 'CompassDirection'], 'measurementTechnique': [{'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000485 has 37 NWB files.
37 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Overview (Images) Chamber overview at start of experiment
  Dataset /acquisition/Overview/ArenaTrack (RGBAImage) Arena track plotted during tail extraction | shape = (433, 430, 4) | dtype = uint8
  file_create_date: ['2023-04-20T16:46:05.408321-04:00']
  Group /general/devices/LaserTrackingRig_1 (Device) OSU Haesemeyer Lab, Laser Tracking Rig 1 (as in Haesemeyer et al., 2015)
  experiment_description: Experiment name: Plaid_warm_01
  
  Fish name: nachet
  
  Fish DOB: 2/8/2023 12:00:00 AM
  
  Dish center (x, y): (400, 400)
  
  Dish radius: 360
  
  ------
  
  Comment:
  
  From today: Righ heated to 28C. Fish water for fills/refills kept at 28C.
  
  ------
  
  Start date: 2/13/2023
  
  Start Time: 1:21 PM
  
  
  
  Frame rate: 250 Hz
  
  Resolution: 8 px/mm
  
  
  
  
  
  Thermal plaid experiment
  
  Habituation length 600 [s]
  
  Pre gradient length 1200 [s]
  
  Plaid length 1200 [s]
  
  Trough power at sample 50 [mW]
  
  Peak power at sample 1000 [mW]
  
  Plaid period 20 [mm]
  
  Plaid period 160 [px]
  
  Plaid offset X 968 [px]
  
  Plaid offset Y 654 [px]
  
  
  
  --------------
  
  Experiment ended:
  
  2/13/2023 2:11:09 PM
  
  experimenter: ['Martin Haesemeyer']
  institution: THE Ohio State University
  Group /general/subject (Subject) 
  identifier: Plaid_warm_01_nachet
  Group /processing/Experimental information (ProcessingModule) Ongoing experimental variables
  Group /processing/Experimental information/Experiment phase (TimeSeries) Experimental phase
  Group /processing/Recorded behavior data (ProcessingModule) Behavior of fish. Fish type: nachet
  Group /processing/Recorded behavior data/Cumulative tail angle (Position) 
  Group /processing/Recorded behavior data/Cumulative tail angle/Cumulative tail angle (SpatialSeries) Cumulative bend angle of the tail in radians.
  Group /processing/Recorded behavior data/Heading (CompassDirection) 
  Group /processing/Recorded behavior data/Heading/Fish heading (SpatialSeries) Absolute fish heading in radians.
  Group /processing/Recorded behavior data/Position (Position) 
  Group /processing/Recorded behavior data/Position/Chamber position (SpatialSeries) Position of the fish within the swim lane in mm coordinates.
  Dataset /scratch/Experiment type (ScratchData)  | shape = () | dtype = <U25
  Dataset /scratch/Raw Experiment metadata (ScratchData)  | shape = () | dtype = <U649
  session_description: Thermal plaid experiment
  session_start_time: 2023-02-13T13:21:00-05:00
  Group /stimulus/presentation/IR Laser Power at Sample (TimeSeries) 980 nm tracking laser power at sample
  timestamps_reference_time: 2023-02-13T13:21:00-05:00
