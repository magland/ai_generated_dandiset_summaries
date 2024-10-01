
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000548/0.230519.1825
name: Effect of the number of pulses on electroporation by unipolar and 50 % bipolar pulses
contributor: [{'name': 'Silkuniene, Giedre', 'email': 'giedre.silkuniene@gmail.com', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0001-8436-9718', 'affiliation': [], 'includeInCitation': True}, {'name': 'National Institutes of Health', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': 'R21EY034258', 'contactPoint': [], 'includeInCitation': False}, {'name': 'Kim, Vitalii', 'roleName': [], 'schemaKey': 'Person', 'identifier': '0000-0003-0699-5582', 'affiliation': [], 'includeInCitation': True}, {'name': 'Semenov, Iurii', 'roleName': [], 'schemaKey': 'Person', 'identifier': '0000-0002-0302-1355', 'affiliation': [], 'includeInCitation': True}, {'name': 'Pakhomov, Andrei    ', 'roleName': [], 'schemaKey': 'Person', 'identifier': '0000-0003-3816-3860', 'affiliation': [], 'includeInCitation': True}]
description: Trains of 5, 10, or 15 pulses all at 1 Hz. Cells were electroporated by a train of 5, 10, or 15 unipolar 600 ns pulses (0 percent) or bipolar 600 + 600 ns pulses (50 percent) at 1 Hz. 50% represents the second pulse's amplitude in relation to the first pulse's amplitude. 0% represents a unipolar pulse, where no second pulse was applied. The electrodes were two parallel stainless-steel cylinders, 1.5 mm in diameter and 3 mm apart. Supported by NIH 1R21EY034258
assetsSummary: {'species': [{'name': 'Bos taurus - Cattle', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9913'}], 'approach': [], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 19823052053, 'numberOfFiles': 19, 'numberOfSubjects': 19, 'variableMeasured': [], 'measurementTechnique': []}

Dandiset 000548 has 5 NWB files.
1 of these NWB files are of type 1.
1 of these NWB files are of type 2.
1 of these NWB files are of type 3.
1 of these NWB files are of type 4.
1 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Fig3_Bi10_08 (ImageSeries) Channel1 ex/em 350/460nm and ex/em 480/535nm. All cells labeled with MemBrite dye (Channel 1), permeabilized cells visualized by membrane-impermeable fluorescence dye YOPRO-1, Dark circles with no electroporated cells are the footprints of electrodes. An image was obtained by scanning a whole well from a six-well plate, and a total of 144 images (12x12 grid) were captured. These images were then automatically stitched together to create a composite image.
  file_create_date: ['2023-05-19T12:59:05.865115-04:00']
  experimenter: ['Kim Vitalii']
  institution: Old Dominion University
  lab: Pakhomov Lab
  session_id: BPAE_bipolar_10pulses
  Group /general/subject (Subject) 
  identifier: 95f5231f-f1dc-43ed-8c05-2105e827a2d5
  session_description: Cells were electroporated by a train of 10 600+600 ns bipolar pulses (amplitude of the second phase was 50% the first phase's amplitude) at 1 Hz.The electrodes were two parallel stainless-steel cylinders, 1.5 mm in diameter and 3 mm apart
  session_start_time: 2021-07-26T19:20:40-04:00
  timestamps_reference_time: 2021-07-26T19:20:40-04:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Fig3_Bi15_07 (ImageSeries) Channel1 ex/em 350/460nm and ex/em 480/535nm. All cells labeled with MemBrite dye (Channel 1), permeabilized cells visualized by membrane-impermeable fluorescence dye YOPRO-1, Dark circles with no electroporated cells are the footprints of electrodes. An image was obtained by scanning a whole well from a six-well plate, and a total of 144 images (12x12 grid) were captured. These images were then automatically stitched together to create a composite image.
  file_create_date: ['2023-05-19T13:01:01.840278-04:00']
  experimenter: ['Kim Vitalii']
  institution: Old Dominion University
  lab: Pakhomov Lab
  session_id: BPAE_bipolar_15pulses
  Group /general/subject (Subject) 
  identifier: c56c330e-ab44-4ddd-96c0-e7f08260ee8b
  session_description: Cells were electroporated by a train of 15 600+600 ns bipolar pulses (amplitude of the second phase was 50% the first phase's amplitude) at 1 Hz.The electrodes were two parallel stainless-steel cylinders, 1.5 mm in diameter and 3 mm apart
  session_start_time: 2021-07-26T19:04:45-04:00
  timestamps_reference_time: 2021-07-26T19:04:45-04:00


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Fig3_Bi15_09 (ImageSeries) Channel1 ex/em 350/460nm and ex/em 480/535nm. All cells labeled with MemBrite dye (Channel 1), permeabilized cells visualized by membrane-impermeable fluorescence dye YOPRO-1, Dark circles with no electroporated cells are the footprints of electrodes. An image was obtained by scanning a whole well from a six-well plate, and a total of 144 images (12x12 grid) were captured. These images were then automatically stitched together to create a composite image.
  file_create_date: ['2023-05-19T13:02:12.358167-04:00']
  experimenter: ['Kim Vitalii']
  institution: Old Dominion University
  lab: Pakhomov Lab
  session_id: BPAE_bipolar_15pulses
  Group /general/subject (Subject) 
  identifier: 6a6774c9-efad-4650-8680-9d9dc6d5eae3
  session_description: Cells were electroporated by a train of 15 600+600 ns bipolar pulses (amplitude of the second phase was 50% the first phase's amplitude) at 1 Hz.The electrodes were two parallel stainless-steel cylinders, 1.5 mm in diameter and 3 mm apart
  session_start_time: 2021-07-26T19:37:45-04:00
  timestamps_reference_time: 2021-07-26T19:37:45-04:00


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Fig3_Bi15_13 (ImageSeries) Channel1 ex/em 350/460nm and ex/em 480/535nm. All cells labeled with MemBrite dye (Channel 1), permeabilized cells visualized by membrane-impermeable fluorescence dye YOPRO-1, Dark circles with no electroporated cells are the footprints of electrodes. An image was obtained by scanning a whole well from a six-well plate, and a total of 144 images (12x12 grid) were captured. These images were then automatically stitched together to create a composite image.
  file_create_date: ['2023-05-19T13:03:21.348362-04:00']
  experimenter: ['Kim Vitalii']
  institution: Old Dominion University
  lab: Pakhomov Lab
  session_id: BPAE_bipolar_15pulses
  Group /general/subject (Subject) 
  identifier: cffc325f-3c27-4d3d-b97b-5b1247dc4b21
  session_description: Cells were electroporated by a train of 15 600+600 ns bipolar pulses (amplitude of the second phase was 50% the first phase's amplitude) at 1 Hz.The electrodes were two parallel stainless-steel cylinders, 1.5 mm in diameter and 3 mm apart
  session_start_time: 2021-07-26T20:36:23-04:00
  timestamps_reference_time: 2021-07-26T20:36:23-04:00


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Fig3_Bi5_06 (ImageSeries) Channel1 ex/em 350/460nm and ex/em 480/535nm. All cells labeled with MemBrite dye (Channel 1), permeabilized cells visualized by membrane-impermeable fluorescence dye YOPRO-1, Dark circles with no electroporated cells are the footprints of electrodes. An image was obtained by scanning a whole well from a six-well plate, and a total of 144 images (12x12 grid) were captured. These images were then automatically stitched together to create a composite image.
  file_create_date: ['2023-05-19T12:46:29.222586-04:00']
  experimenter: ['Kim Vitalii']
  institution: Old Dominion University
  lab: Pakhomov Lab
  session_id: BPAE_bipolar_5pulses
  Group /general/subject (Subject) 
  identifier: e12a6f08-0da2-46ac-8034-a66896351d75
  session_description: Cells were electroporated by a train of 5 600+600 ns bipolar pulses (second phase was 50% the first phase's amplitude) at 1 Hz.The electrodes were two parallel stainless-steel cylinders, 1.5 mm in diameter and 3 mm apart
  session_start_time: 2021-07-26T18:52:17-04:00
  timestamps_reference_time: 2021-07-26T18:52:17-04:00
