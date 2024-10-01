
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000632/0.231012.1930
name: Electroporation efficiency of co-directional and cross-directional paired pulses
contributor: [{'name': 'Silkuniene, Giedre', 'email': 'giedre.silkuniene@gmail.com', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0001-8436-9718', 'affiliation': [], 'includeInCitation': True}, {'name': 'Kim, Vitalii', 'roleName': [], 'schemaKey': 'Person', 'identifier': '0000-0003-0699-5582', 'affiliation': [], 'includeInCitation': True}, {'name': 'Semenov, Iurii', 'roleName': [], 'schemaKey': 'Person', 'identifier': '0000-0002-0302-1355', 'affiliation': [], 'includeInCitation': True}, {'name': 'Pakhomov, Andrei', 'roleName': [], 'schemaKey': 'Person', 'identifier': '0000-0003-3816-3860', 'affiliation': [], 'includeInCitation': True}, {'name': 'National Institutes of Health ', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': 'NIH 1R21EY034258', 'contactPoint': [], 'includeInCitation': False}]
description: The efficiency of electroporation was evaluated in an experiment involving co-directional and cross-directional paired pulses using a triangular electrode array. BPAE cell monolayers were exposed to trains of four paired pulses, each consisting of 600 + 600 ns, at two distinct frequencies: 1 Hz and 770 kHz, with an amplitude of 10 kV/cm. In one scenario, the electric field direction remained consistent throughout each pair (co-directional). In another, the field direction was altered by 90° (cross-directional). The electroporation efficiency was quantified through the cells’ uptake of YoPro-1 dye, serving as a measure of the permeabilization of the cell membranes under varying electric field orientations and frequencies. Supported by NIH 1R21EY034258

assetsSummary: {'species': [{'name': 'Bos taurus - Cattle', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9913'}], 'approach': [], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 42744120707, 'numberOfFiles': 24, 'numberOfSubjects': 24, 'variableMeasured': [], 'measurementTechnique': []}

Dandiset 000632 has 24 NWB files.
24 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ScaningImaging (ImageSeries) IX83 microscope used; MS-2000 scanning stage; X-Cite 110LED illuminator; ORCA-Flash4 sCMOS camera;CellSens software for automation; Channel 1 ex/em 350/460nm for MemBrite dye; ex/em 480/535nm for YOPRO-1; dark circles indicate electrode footprints; 144 images captured in a 12x12 grid from a six-well plate; 216 additional images with DAPI and FITC filter cubes; all images automatically stitched for a final composite; 10×, 0.38NA objective used for high-resolution imaging.
  file_create_date: ['2023-10-12T13:55:14.519643-04:00']
  experimenter: ['Kim Vitalii']
  institution: Old Dominion University
  lab: Pakhomov Lab
  session_id: Cross-directional_1Hz
  Group /general/subject (Subject) 
  identifier: 724dc441-fd49-4267-9b7f-81e5b7e87b31
  session_description: Cells were electroporated by 4 cross-directional paired-pulse (600 + 600 ns) trains, trains were applied at frequency of 1 Hz, amplitude 10 kV/cm. The stainless-steel electrodes were aranged in triangular array; The electric field direction was changed by 90° in each pair.
  session_start_time: 2022-12-04T16:09:58-05:00
  timestamps_reference_time: 2022-12-04T16:09:58-05:00
