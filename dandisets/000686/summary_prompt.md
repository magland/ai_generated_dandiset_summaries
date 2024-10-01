
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000686/0.240515.1909
name: Focusing electroporation to the center of a quadrupole electrode array by interference of unipolar pulses (NextGeneration-CANCAN)
contributor: [{'name': 'Silkuniene, Giedre', 'email': 'giedre.silkuniene@gmail.com', 'roleName': ['dcite:ContactPerson', 'dcite:Author', 'dcite:DataCurator', 'dcite:DataManager', 'dcite:FormalAnalysis'], 'schemaKey': 'Person', 'identifier': '0000-0001-8436-9718', 'affiliation': [], 'includeInCitation': True}, {'name': 'Pakhomov, Andrei', 'roleName': ['dcite:Author', 'dcite:ProjectLeader'], 'schemaKey': 'Person', 'identifier': '0000-0003-3816-3860', 'affiliation': [], 'includeInCitation': True}, {'name': 'Gudvangen, Emily', 'roleName': [], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Mangalanathan, Uma', 'roleName': [], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Semenov, Iurii', 'roleName': [], 'schemaKey': 'Person', 'identifier': '0000-0002-0302-1355', 'affiliation': [], 'includeInCitation': True}, {'name': 'National Institutes of Health ', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': 'NIH 1R21EY034258', 'contactPoint': [], 'includeInCitation': False}]
description: These experimental trials demonstrate the feasibility of achieving remote targeting in electroporation by utilizing sequences of unipolar nanosecond electric pulses (nsEP), with the rotation of these packets further enhancing the process. Electroporation of the cells was evaluated using 1 uM YoPro-1 cell impermeable fluorescent dye. The study was supported in part by R21EY034258 from the National Eye Institute to A.G.P
assetsSummary: {'species': [{'name': 'Bos taurus - Cattle', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9913'}], 'approach': [], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 11736585692, 'numberOfFiles': 18, 'numberOfSubjects': 36, 'variableMeasured': [], 'measurementTechnique': []}

Dandiset 000686 has 18 NWB files.
18 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ScanningImaging (ImageSeries) IX83 microscope used; MS-2000 scanning stage; X-Cite 110LED illuminator; ORCA-Flash4 sCMOS camera;CellSens software for automation; ex/em 480/535nm for detecting electroporation using 1uM YOPRO-1; dark circles indicate electrode footprints; 144 images captured in a 12x12 grid from a six-well plate; all images automatically stitched for a final composite; 10×, 0.38NA objective used for high-resolution imaging.
  file_create_date: ['2024-01-19T14:42:34.675213-05:00']
  experimenter: ['Iurii Semenov']
  institution: Old Dominion University
  lab: Pakhomov Lab
  session_id: 1p x 10cycles CanCan 600ns 200ms 6.4kV
  Group /general/subject (Subject) 
  identifier: 8cb770ee-1750-43ab-8565-94523e70cb34
  session_description: In the CanCan treated group, electric pulses were delivered through a quadrupole array of blunt, hollow, stainless-steel needle electrodes. This procedure involved administering packets of 15 pulses, each 600 nanoseconds long. The protocol began with a single 6.4 kV pulse directed to electrode e1. Subsequent pulses were applied in pairs to diagonal electrodes, with each new pair having an amplitude 12.5% lower than the previous pair. Following the completion of the packet sequence from the e1 electrode, the identical sequence was then sequentially executed from electrodes e2, e3, and e4, thus completing one cycle. A total of 10 cycles were conducted in this manner. The alternation of packets and cycles was performed at a frequency of 1Hz.
  session_start_time: 2021-08-06T15:04:58-04:00
  timestamps_reference_time: 2021-08-06T15:04:58-04:00
