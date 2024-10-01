
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000540/0.230515.0530
name: Dataset for: A change in behavioral state switches the pattern of motor output that underlies rhythmic head and orofacial movements
contributor: [{'name': 'Liao, Song-Mao', 'email': 'soliao@ucsd.edu', 'roleName': ['dcite:Author', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'awardNumber': 'GSSA', 'includeInCitation': True}, {'url': 'https://neurophysics.ucsd.edu/', 'name': 'Kleinfeld, David', 'email': 'dk@physics.ucsd.edu', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Rinehart, Duane', 'email': 'drinehart@physics.ucsd.edu', 'roleName': ['dcite:Software'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'url': 'https://ucsd.edu/', 'name': 'University of California San Diego', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/0168r3w48', 'awardNumber': 'R01 NS058668; U01 NS090595; U19 NS107466', 'contactPoint': [], 'includeInCitation': True}]
description: Recorded multi-modal data (videography, respiration, electromyogram, wearable sensor signals, and human annotation) from rats performing naturalistic foraging and rearing behaviors in an open arena. Dataset for S.-M. Liao and D. Kleinfeld, Current Biology (2023). A change in behavioral state switches the pattern of motor output that underlies rhythmic head and orofacial movements. Dataset uploaded by the Kleinfeld Laboratory at University of California San Diego. Code can be found on https://rhythm-n-rodents.github.io/software/.
assetsSummary: {'species': [{'name': 'Rattus norvegicus - Norway rat', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10116'}], 'approach': [{'name': 'behavioral approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 1003937347960, 'numberOfFiles': 990, 'numberOfSubjects': 33, 'variableMeasured': ['BehavioralTimeSeries', 'ProcessingModule'], 'measurementTechnique': [{'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000540 has 100 NWB files.
100 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ImageSeries (ImageSeries) Rat forages in open arena
  file_create_date: ['2023-05-12T10:38:37.721501-07:00']
  Group /general/devices/LabChart-BNO055-Basler (Device) LabChart-BNO055-Basler
  experimenter: ['Liao, Song-Mao']
  institution: UC San Diego
  keywords: ['Researchers: Liao, Song-Mao']
  notes: Annotation,frame_start,frame_end|Video Boundary,201,3681 | Unusable Behavior,1625,1633 | Unusable Behavior,1917,2100 | Unusable Behavior,2155,2160 | Unusable Behavior,2543,2574 | 
  pharmacology: NA
  stimulus: epoch_start,epoch_end,epoch_status,pellet_loc_X,pellet_loc_Y,pellet_loc_status|288,355,0,320,265,0 | 512,1404,0,144,105,0 | 1467,2401,0,213,290,0 | 2442,2668,0,131,308,0 | 2759,3251,0,299,106,0 | 3326,3445,0,236,178,0 | 
  Group /general/subject (Subject) 
  identifier: nan
  Group /processing/behavioral_booleans (ProcessingModule) Annotated masks for pre-defined behaviors (usable, head-torso, both)
  Group /processing/behavioral_booleans/analysis (BehavioralTimeSeries) 
  Group /processing/behavioral_booleans/analysis/analysis (TimeSeries) Annotated masks for pre-defined behaviors (usable, head-torso, both)
  Group /processing/data_36columns (ProcessingModule) nan|nan|nan|nan
  Group /processing/data_36columns/data_36columns (BehavioralTimeSeries) 
  Group /processing/data_36columns/data_36columns/data_36columns (TimeSeries) nan|nan|nan|nan
  Group /processing/raw_labchart_data (ProcessingModule) breathing|torso|head
  Group /processing/raw_labchart_data/raw_labchart_data (BehavioralTimeSeries) 
  Group /processing/raw_labchart_data/raw_labchart_data/raw_labchart_data (TimeSeries) breathing|torso|head
  Group /processing/raw_sensor_data (ProcessingModule) Torso angles (Y, P, R) = (1, 2, 3) columns | Head angles (Y, P, R) = first 3 columns of the second half columns
  Group /processing/raw_sensor_data/raw_sensor_data (BehavioralTimeSeries) 
  Group /processing/raw_sensor_data/raw_sensor_data/raw_sensor_data (TimeSeries) Torso angles (Y, P, R) = (1, 2, 3) columns | Head angles (Y, P, R) = first 3 columns of the second half columns
  Group /processing/signal_percentiles (ProcessingModule) Percentiles of the 36-data signals.
  Group /processing/signal_percentiles/processing (BehavioralTimeSeries) 
  Group /processing/signal_percentiles/processing/processing (TimeSeries) Percentiles of the 36-data signals.
  Group /processing/torso_dlc (ProcessingModule) torso_tracking
  Group /processing/torso_dlc/torso_dlc (BehavioralTimeSeries) 
  Group /processing/torso_dlc/torso_dlc/torso_dlc (TimeSeries) torso_tracking
  session_description: Rat forages in open arena
  session_start_time: 2018-07-06T00:00:00-07:00
  timestamps_reference_time: 2018-07-06T00:00:00-07:00
