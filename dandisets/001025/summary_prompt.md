
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001025/0.240605.1826
name: The impact of voltage on CANCAN focusing of electroporation using four-electrode arrays of varying sizes
contributor: [{'name': 'Silkuniene, Giedre', 'email': 'giedre.silkuniene@gmail.com', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0001-8436-9718', 'affiliation': [], 'includeInCitation': True}, {'name': 'Gudvangen, Emily', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Mangalanathan, Uma', 'schemaKey': 'Person', 'identifier': '0000-0003-0126-5660', 'includeInCitation': True}, {'name': 'Semenov, Iurii', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-0302-1355', 'includeInCitation': True}, {'name': 'Pakhomov, Andrei', 'roleName': ['dcite:Author', 'dcite:ProjectLeader'], 'schemaKey': 'Person', 'identifier': '0000-0003-3816-3860', 'includeInCitation': True}, {'name': 'National Institutes of Health', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': ' NIH 1R21EY034258', 'includeInCitation': False}]
description: The study examines the effect of pulse voltage on CANCAN focusing of electroporation using electrode arrays of different sizes. Adjustments in the amplitude of nanosecond electroporation pulses influenced the intensity of electroporation but did not alter its spatial characteristics across the electrode array. The study was supported in part by NIH R21EY034258
assetsSummary: {'species': [{'name': 'Cricetulus griseus - Cricetulus aureus', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10029'}], 'approach': [], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 10690479132, 'numberOfFiles': 21, 'numberOfSubjects': 19, 'variableMeasured': [], 'measurementTechnique': []}

Dandiset 001025 has 21 NWB files.
21 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ScanningImaging (ImageSeries) Single time point imaging (ScanningImaging) using fluorescence microscopy. Additional metadata: Microscope: Unknown microscope, Detector: Hamamatsu Hamamatsu ORCA-Flash4.0, Objective: Olympus IX3 Nosepiece NA=0.40000000000000002 Mag=10, Channels: FITC, DAPI
  file_create_date: ['2024-06-05T13:57:16.024746-04:00']
  experimenter: ['Iurii Semenov']
  institution: Old Dominion University
  lab: Pakhomov Lab
  session_id: single_time_point
  Group /general/subject (Subject) 
  identifier: 80713518-0920-434d-b41e-384553366a18
  session_description: 02. Experiments were conducted in a 4 electrodes setup. CanCan protocol applied at 4.8kV (first pulse) with the subsequent canceling pulses 12.5% lower than pulses before. Packets were repeated 10 times at 1Hz frequency. Than also at 1Hz frequency protocol was shifted and than electrode 2 was starting electrode with noted amplitude of the first pulse. Protocol finished when all 4 electrodes were active pulse electrodes. Detailed information on pulsing parameters, electrodes and procedures can be found in 10.1016/j.bioelechem.2023.108437.
  session_start_time: 2021-05-20T12:49:16-04:00
  timestamps_reference_time: 2021-05-20T12:49:16-04:00
