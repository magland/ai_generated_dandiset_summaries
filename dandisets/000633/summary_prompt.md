
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000633/0.231013.2226
name: The difference in electroporation patterns produced by a train of single pulses and a train of paired pulses
contributor: [{'name': 'Silkuniene, Giedre', 'email': 'giedre.silkuniene@gmail.com', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0001-8436-9718', 'affiliation': [], 'includeInCitation': True}, {'name': 'Kim, Vitalii', 'roleName': [], 'schemaKey': 'Person', 'identifier': '0000-0003-0699-5582', 'affiliation': [], 'includeInCitation': True}, {'name': 'Semenov, Iurii', 'roleName': [], 'schemaKey': 'Person', 'identifier': '0000-0002-0302-1355', 'affiliation': [], 'includeInCitation': True}, {'name': 'Pakhomov, Andrei', 'roleName': [], 'schemaKey': 'Person', 'identifier': '0000-0003-3816-3860', 'affiliation': [], 'includeInCitation': True}, {'name': 'National Institutes of Health ', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': 'NIH 1R21EY034258', 'contactPoint': [], 'includeInCitation': False}]
description: The difference in electroporation patterns produced by a train of single pulses and a train of paired pulses. Supported by NIH 1R21EY034258
assetsSummary: {'species': [{'name': 'Bos taurus - Cattle', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9913'}], 'approach': [], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 2137420087, 'numberOfFiles': 2, 'numberOfSubjects': 2, 'variableMeasured': [], 'measurementTechnique': []}

Dandiset 000633 has 2 NWB files.
2 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ScaningImaging (ImageSeries) IX83 microscope used; MS-2000 scanning stage; X-Cite 110LED illuminator; ORCA-Flash4 sCMOS camera;CellSens software for automation; Channel 1 ex/em 350/460nm for MemBrite dye; ex/em 480/535nm for YOPRO-1; dark circles indicate electrode footprints; 144 images captured in a 12x12 grid from a six-well plate; 216 additional images with DAPI and FITC filter cubes; all images automatically stitched for a final composite; 10×, 0.38NA objective used for high-resolution imaging.
  file_create_date: ['2023-10-13T18:13:44.633053-04:00']
  experimenter: ['Kim Vitalii']
  institution: Old Dominion University
  lab: Pakhomov Lab
  session_id: Paired-pulse_trains
  Group /general/subject (Subject) 
  identifier: afa01753-d72e-454f-aac4-98987d0cf7f3
  session_description: In this experimental setup, a cell monolayer is subjected to a train of electrical pulses, delivered through a triangular electrode array where two base electrodes are connected to two separate channels. The innovative design ensures that as one channel is energized, the other is automatically grounded, and vice versa. This dynamic allows for the efficient electroporation of the cells with a train of 5 paired-pulses, each consisting of a 600+600 ns duration. The application occurs at a frequency of 833 kHz and an amplitude of 2 kV, ensuring precise and controlled exposure.
  session_start_time: 2022-11-29T19:37:16-05:00
  timestamps_reference_time: 2022-11-29T19:37:16-05:00
