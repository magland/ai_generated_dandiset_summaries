
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000489/0.230518.1811
name: The impact of the second phase amplitude (% to the first phase) on the electroporation efficiency (measured as YP emission)
contributor: [{'name': 'Silkuniene, Giedre', 'email': 'giedre.silkuniene@gmail.com', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0001-8436-9718', 'affiliation': [], 'includeInCitation': True}, {'name': 'Kim, Vitalii', 'roleName': [], 'schemaKey': 'Person', 'identifier': '0000-0003-0699-5582', 'affiliation': [], 'includeInCitation': True}, {'name': 'Semenov, Iurii', 'roleName': [], 'schemaKey': 'Person', 'identifier': '0000-0002-0302-1355', 'affiliation': [], 'includeInCitation': True}, {'name': 'Pakhomov, Andrei', 'roleName': [], 'schemaKey': 'Person', 'identifier': '0000-0003-3816-3860', 'affiliation': [], 'includeInCitation': True}, {'name': 'National Institutes of Health', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': '1R21EY034258', 'contactPoint': [], 'includeInCitation': False}]
description: Cells were electroporated by a train of 5 unipolar 600 ns pulses (0 percent) or bipolar 600 + 600 ns pulses (25, 50, 75, 100 percent) at 1 Hz. 25, 50, 75, and 100% represent the second pulse's amplitude in relation to the first pulse's amplitude. 0% represents a unipolar pulse, where no second pulse was applied. The electrodes were two parallel stainless-steel cylinders, 1.5 mm in diameter and 3 mm apart. Supported by NIH 1R21EY034258
assetsSummary: {'species': [{'name': 'Bos taurus - Cattle', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9913'}], 'approach': [], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 18594422294, 'numberOfFiles': 18, 'numberOfSubjects': 18, 'variableMeasured': [], 'measurementTechnique': []}

Dandiset 000489 has 5 NWB files.
1 of these NWB files are of type 1.
1 of these NWB files are of type 2.
1 of these NWB files are of type 3.
1 of these NWB files are of type 4.
1 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Channel1 and Channel2 (ImageSeries) ex/em 350/460 nm and ex/em 480/535nm
  file_create_date: ['2023-05-17T16:10:06.318233-04:00']
  experimenter: ['Kim Vitalii']
  institution: Old Dominion University
  lab: Pakhomov Lab
  session_id: BPAE_staining
  Group /general/subject (Subject) 
  identifier: ed13a968-7640-4a00-9026-dc5a4a5732d7
  session_description: Sample images of a cell monolayer. Electroporated cells are visualized by YOPRO-1 staining (Channel 2) and all cells are labeled with MemBrite dye (Channel 1). Dark circles with no electroporated cells are the footprints of electrodes.
  session_start_time: 2021-09-01T19:13:29-04:00
  timestamps_reference_time: 2021-09-01T19:13:29-04:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Fig2_0_03 (ImageSeries) Channel1 ex/em 350/460nm and ex/em 480/535nm. All cells labeled with MemBrite dye (Channel 1), permeabilized cells visualized by membrane-impermeable fluorescence dye YOPRO-1, Dark circles with no electroporated cells are the footprints of electrodes. An image was obtained by scanning a whole well from a six-well plate, and a total of 144 images (12x12 grid) were captured. These images were then automatically stitched together to create a composite image.
  file_create_date: ['2023-05-18T11:32:06.239396-04:00']
  experimenter: ['Kim Vitalii']
  institution: Old Dominion University
  lab: Pakhomov Lab
  session_id: BPAE_bipolar_0 percent
  Group /general/subject (Subject) 
  identifier: ad676920-0838-40c5-bf59-8dff79b1a3f1
  session_description: Cells were electroporated by a train of 5 unipolar 600 ns pulses (no second pulse(0%)) at 1 Hz.The electrodes were two parallel stainless-steel cylinders, 1.5 mm in diameter and 3 mm apart
  session_start_time: 2021-07-29T13:00:26-04:00
  timestamps_reference_time: 2021-07-29T13:00:26-04:00


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Fig2_0_06 (ImageSeries) Channel1 ex/em 350/460nm and ex/em 480/535nm. All cells labeled with MemBrite dye (Channel 1), permeabilized cells visualized by membrane-impermeable fluorescence dye YOPRO-1, Dark circles with no electroporated cells are the footprints of electrodes. An image was obtained by scanning a whole well from a six-well plate, and a total of 144 images (12x12 grid) were captured. These images were then automatically stitched together to create a composite image.
  file_create_date: ['2023-05-18T11:33:16.392490-04:00']
  experimenter: ['Kim Vitalii']
  institution: Old Dominion University
  lab: Pakhomov Lab
  session_id: BPAE_bipolar_0 percent
  Group /general/subject (Subject) 
  identifier: 92f9fc3a-b0fc-4340-912e-9bc60c5fb40c
  session_description: Cells were electroporated by a train of 5 unipolar 600 ns pulses (no second pulse(0%)) at 1 Hz.The electrodes were two parallel stainless-steel cylinders, 1.5 mm in diameter and 3 mm apart
  session_start_time: 2021-07-29T13:46:16-04:00
  timestamps_reference_time: 2021-07-29T13:46:16-04:00


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Fig2_0_07 (ImageSeries) Channel1 ex/em 350/460nm and ex/em 480/535nm. All cells labeled with MemBrite dye (Channel 1), permeabilized cells visualized by membrane-impermeable fluorescence dye YOPRO-1, Dark circles with no electroporated cells are the footprints of electrodes. An image was obtained by scanning a whole well from a six-well plate, and a total of 144 images (12x12 grid) were captured. These images were then automatically stitched together to create a composite image.
  file_create_date: ['2023-05-18T11:34:30.938736-04:00']
  experimenter: ['Kim Vitalii']
  institution: Old Dominion University
  lab: Pakhomov Lab
  session_id: BPAE_bipolar_0 percent
  Group /general/subject (Subject) 
  identifier: 50344de6-40b2-49e1-9743-ab5aa5983a0e
  session_description: Cells were electroporated by a train of 5 unipolar 600 ns pulses (no second pulse(0%)) at 1 Hz.The electrodes were two parallel stainless-steel cylinders, 1.5 mm in diameter and 3 mm apart
  session_start_time: 2021-07-29T14:00:53-04:00
  timestamps_reference_time: 2021-07-29T14:00:53-04:00


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Fig2_100_03 (ImageSeries) Channel1 ex/em 350/460nm and ex/em 480/535nm. All cells labeled with MemBrite dye (Channel 1), permeabilized cells visualized by membrane-impermeable fluorescence dye YOPRO-1, Dark circles with no electroporated cells are the footprints of electrodes. An image was obtained by scanning a whole well from a six-well plate, and a total of 144 images (12x12 grid) were captured. These images were then automatically stitched together to create a composite image.
  file_create_date: ['2023-05-18T13:54:24.127683-04:00']
  experimenter: ['Kim Vitalii']
  institution: Old Dominion University
  lab: Pakhomov Lab
  session_id: BPAE_bipolar_100 percent
  Group /general/subject (Subject) 
  identifier: cf4c43cf-a163-4797-aa1d-67c710ad2ffb
  session_description: Cells were electroporated by a train of 5 bipolar 600+600 ns pulses (second pulse amplitude 100% in comparison to the first pulse amplitude) at 1 Hz.The electrodes were two parallel stainless-steel cylinders, 1.5 mm in diameter and 3 mm apart
  session_start_time: 2021-08-24T15:18:08-04:00
  timestamps_reference_time: 2021-08-24T15:18:08-04:00
