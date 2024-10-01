
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001027/0.240605.1859
name: CANCAN focusing of electroporation in a quadrupole array by different pulsing protocols
contributor: [{'name': 'Silkuniene, Giedre', 'email': 'giedre.silkuniene@gmail.com', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0001-8436-9718', 'affiliation': [], 'includeInCitation': True}, {'name': 'Gudvangen, Emily', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Mangalanathan, Uma', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0003-0126-5660', 'includeInCitation': True}, {'name': 'Semenov, Iurii', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-0302-1355', 'includeInCitation': True}, {'name': 'Pakhomov, Andrei', 'roleName': ['dcite:Author', 'dcite:ProjectLeader'], 'schemaKey': 'Person', 'identifier': '0000-0003-3816-3860', 'includeInCitation': True}, {'name': 'National Institutes of Health', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': '1R21EY034258', 'includeInCitation': False}]
description: Protocols were applied once, starting from each of the electrodes, to a total of four protocols delivered. The 1st pulse amplitude in all protocols was 4 kV. Electroporation of the cells was evaluated using 1 uM YoPro-1 cell impermeable fluorescent dye. The study was supported in part by R21EY034258 from the National Eye Institute to A.G.P
assetsSummary: {'species': [{'name': 'Cricetulus griseus - Cricetulus aureus', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10029'}], 'approach': [], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 3667103151, 'numberOfFiles': 10, 'numberOfSubjects': 10, 'variableMeasured': [], 'measurementTechnique': []}

Dandiset 001027 has 10 NWB files.
10 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ScanningImaging (ImageSeries) Single time point imaging (ScanningImaging) using fluorescence microscopy. Additional metadata: Microscope: Unknown microscope, Detector: Hamamatsu Hamamatsu ORCA-Flash4.0, Objective: Olympus IX3 Nosepiece NA=0.40000000000000002 Mag=10, Channels: FITC
  file_create_date: ['2024-06-05T14:51:19.354922-04:00']
  experimenter: ['Iurii Semenov']
  institution: Old Dominion University
  lab: Pakhomov Lab
  session_id: single_time_point
  Group /general/subject (Subject) 
  identifier: 1bc47a6a-b71d-4a22-994a-d937a58b38bc
  session_description: 03. Experiments were conducted in a 4 electrodes setup. CanCan protocol applied at 4.0kV (first pulse) with the subsequent canceling pulses 12.5% lower than pulses before. Packets were repeated 1 times at 1Hz frequency. Than also at 1Hz frequency protocol was shifted and than electrode 2 was starting electrode with noted amplitude of the first pulse. Protocol finished when all 4 electrodes were active pulse electrodes. Protocol3 had 8 phases of pulses, 600ns pulse duration, canceling pulses delivered with 5us delays before another set of pulses. Detailed information on pulsing parameters, electrodes and procedures can be found in 10.1016/j.bioelechem.2023.108437.
  session_start_time: 2021-03-17T11:40:56-04:00
  timestamps_reference_time: 2021-03-17T11:40:56-04:00
