
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000875/0.240515.1925
name: Influence of unipolar pulse packet quantity on centering the electroporation effect within a quadrupole electrode array.
contributor: [{'name': 'Silkuniene, Giedre', 'email': 'giedre.silkuniene@gmail.com', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Pakhomov, Andrei', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0003-3816-3860', 'affiliation': [], 'includeInCitation': True}, {'name': 'Gudvangen, Emily', 'roleName': [], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Mangalanathan, Uma', 'roleName': [], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Semenov, Iurii', 'roleName': ['dcite:Researcher'], 'schemaKey': 'Person', 'identifier': '0000-0002-0302-1355', 'affiliation': [], 'includeInCitation': True}, {'name': 'National Institutes of Health ', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': 'NIH 1R21EY034258', 'contactPoint': [], 'includeInCitation': False}]
description: This data provides images of Yo-Pro uptake when different numbers of nanosecond electric pulse packets were applied in a four-electrode array. Increasing the total number of applied packets from 4 to 20 and 40 significantly enhanced the electroporative effect across the electrode array. The peak of electroporation at the center was clearly distinguishable for all tested treatments. The study was supported in part by NIH R21EY034258
assetsSummary: {'species': [{'name': 'Bos taurus - Cattle', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9913'}], 'approach': [], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 3607438018, 'numberOfFiles': 9, 'numberOfSubjects': 18, 'variableMeasured': [], 'measurementTechnique': []}

Dandiset 000875 has 9 NWB files.
9 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ScanningImaging (ImageSeries) IX83 microscope used; MS-2000 scanning stage; X-Cite 110LED illuminator; ORCA-Flash4 sCMOS camera;CellSens software for automation; ex/em 480/535nm for detecting electroporation using 1uM YOPRO-1; dark circles indicate electrode footprints; 144 images captured in a 12x12 grid from a six-well plate; all images automatically stitched for a final composite; 10×, 0.38NA objective used for high-resolution imaging.
  file_create_date: ['2024-01-24T18:12:54.343500-05:00']
  experimenter: ['Iurii Semenov']
  institution: Old Dominion University
  lab: Pakhomov Lab
  session_id: 10p_x4_600ns_200ms_3,2kV_YP
  Group /general/subject (Subject) 
  identifier: c5e34ed4-4464-4883-870e-c1378fa0ec9e
  session_description: Electric pulses were delivered through a quadrupole array of blunt, hollow, stainless-steel needle electrodes. This procedure involved administering packets of 15 pulses, each 600 nanoseconds long. The protocol began with a single 3.2 kV pulse directed from electrode e1. Subsequent pulses were applied in pairs to diagonal electrodes, with each new pair having an amplitude 12.5% lower than the previous pair. Following the completion of the packet sequence from the e1 electrode, the identical sequence was then sequentially executed from electrodes e2, e3, and e4, thus completing one cycle. A total of 10 cycles were conducted in this manner. The alternation of packets and cycles was performed at a frequency of 1Hz.
  session_start_time: 2021-02-16T13:39:45-05:00
  timestamps_reference_time: 2021-02-16T13:39:45-05:00
