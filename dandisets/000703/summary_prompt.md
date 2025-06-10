
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000703/draft
name: Constant temperature behavior 28C
contributor: [{'name': 'National Institutes of Health (NIH)', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': '5 R01 NS 123887-03'}, {'name': 'Balakrishnan, Kaarthik A', 'email': 'balakrishnan.64@buckeyemail.osu.edu', 'roleName': ['dcite:DataCollector'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Haesemeyer, Martin', 'email': 'haesemeyer.1@osu.edu', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0003-2704-3601', 'includeInCitation': True}]
description: Fish swimming behavior in light at constant 28C
assetsSummary: {'species': [{'name': 'Danio rerio - Zebra fish', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_7955'}], 'approach': [{'name': 'behavioral approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 207725605, 'numberOfFiles': 22, 'numberOfSubjects': 24, 'variableMeasured': ['Position', 'ProcessingModule', 'CompassDirection', 'SpatialSeries', 'BehavioralTimeSeries'], 'measurementTechnique': [{'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000703 has 22 NWB files.
22 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2023-11-10T11:50:53.533207-05:00']
  Group /general/devices/GradientChamber_1 (Device) OSU Haesemeyer Lab, Gradient Behavior Chamber 1
  experiment_description: Experiment name: Temp_pref_F28_B28_6dpf_01
  
  Fish name: unsorted_nac
  
  Fish DOB: 9/7/2023 12:00:00 AM
  
  Dish center (x, y): (550, 732)
  
  Dish radius: 360
  
  ------
  
  Comment:
  
  
  
  ------
  
  Start date: 9/13/2023
  
  Start Time: 11:22 AM
  
  
  
  Frame rate: 100 Hz
  
  Resolution: 7 px/mm
  
  
  
  
  
  Trial ID: 
  
  
  
  EV Front Temp: 240
  
  EV Back Temp: -22
  
  EV LPS Lane: R
  
  
  
  --------------
  
  Experiment ended:
  
  9/13/2023 11:52:34 AM
  
  experimenter: ['Kaarthik Balakrishnan']
  institution: THE Ohio State University
  Group /general/subject (Subject) 
  identifier: Temp_pref_F28_B28_6dpf_01_unsorted_nac (2)
  Group /processing/wt:nacre: behavior left lane (ProcessingModule) Behavior of fish in left lane of gradient chamber. Fish type: wt:nacre
  Group /processing/wt:nacre: behavior left lane/Heading (CompassDirection) 
  Group /processing/wt:nacre: behavior left lane/Heading/Fish heading (SpatialSeries) Absolute fish heading in radians.
  Group /processing/wt:nacre: behavior left lane/Position (Position) 
  Group /processing/wt:nacre: behavior left lane/Position/Chamber position (SpatialSeries) Position of the fish within the swim lane in mm coordinates.
  Group /processing/wt:nacre: behavior left lane/Temperature (BehavioralTimeSeries) 
  Group /processing/wt:nacre: behavior left lane/Temperature/Temperatures (TimeSeries) Temperature at fish position.
  Group /processing/wt:nacre: behavior right lane (ProcessingModule) Behavior of fish in right lane of gradient chamber. Fish type: wt:nacre
  Group /processing/wt:nacre: behavior right lane/Heading (CompassDirection) 
  Group /processing/wt:nacre: behavior right lane/Heading/Fish heading (SpatialSeries) Absolute fish heading in radians.
  Group /processing/wt:nacre: behavior right lane/Position (Position) 
  Group /processing/wt:nacre: behavior right lane/Position/Chamber position (SpatialSeries) Position of the fish within the swim lane in mm coordinates.
  Group /processing/wt:nacre: behavior right lane/Temperature (BehavioralTimeSeries) 
  Group /processing/wt:nacre: behavior right lane/Temperature/Temperatures (TimeSeries) Temperature at fish position.
  Dataset /scratch/Back Temperature (ScratchData)  | shape = () | dtype = float64
  Dataset /scratch/Front Temperature (ScratchData)  | shape = () | dtype = float64
  Dataset /scratch/Left fish (ScratchData)  | shape = () | dtype = <U8
  Dataset /scratch/Raw Experiment metadata (ScratchData)  | shape = () | dtype = <U399
  Dataset /scratch/Right fish (ScratchData)  | shape = () | dtype = <U8
  session_description: Uniform temperature gradient
  session_start_time: 2023-09-13T11:22:00-04:00
  timestamps_reference_time: 2023-09-13T11:22:00-04:00
