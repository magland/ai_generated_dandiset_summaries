
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000938/0.240511.1846
name: Visualization and characterization of membrane lesions
contributor: [{'name': 'Silkunas, Mantas', 'schemaKey': 'Person', 'identifier': '0000-0002-4568-9265', 'includeInCitation': True}, {'name': 'Silkuniene, Giedre', 'email': 'giedre.silkuniene@gmail.com', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Pakhomov, Andrei', 'schemaKey': 'Person', 'identifier': '0000-0003-3816-3860', 'includeInCitation': True}, {'name': 'National Institutes of Health', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': 'NIH 15R21EY034803', 'includeInCitation': False}, {'name': 'National Institutes of Health', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': 'NIH 1R21EY034258', 'includeInCitation': False}]
description: In this study, real-time imaging was used to visualize individual electropores and demonstrate their persistence in electroporated cells. HEK 923 cells were cultured on Indium Tin Oxide (ITO)-coated coverslips and loaded with the Cal520 fluorescent indicator for visualization. Real-time imaging was performed in Total Internal Reflection Fluorescent (TIRF) mode. Electrophysiological manipulations were applied using a patch clamp in voltage clamp mode, set in a whole-cell configuration. The protocol included a command voltage of 0 mV interrupted by a -50 mV pulse for 50 ms and a -400 mV pulse for 1 ms at frame 91, returning to -50 mV for 50 ms. Additionally, 0.4 seconds into the second and third stacks, the command voltage was changed from 0 mV to -50 mV for 50 ms. The study was supported in part by NIH 15R21EY034803 and NIH 1R21EY034258.
assetsSummary: {'species': [{'name': 'Homo sapiens - Human', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9606'}], 'approach': [], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 2762531957, 'numberOfFiles': 5, 'numberOfSubjects': 5, 'variableMeasured': [], 'measurementTechnique': []}

Dandiset 000938 has 5 NWB files.
5 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/TIRFImaging (ImageSeries) Recordings: 902 frames in total;	5.65 ms/frame; 1st and 2nd frames are artefacts;	Entire movie recorded in 3 stacks containing 300 frames/stack;	30s delays between stack 1 to 2, and between 2 to 3; Scale: 64.9 x 64.9 nm per pixel; Imaging system: Olympus IX83 inverted microscope (Olympus America, Center Valley, PA);	Total Internal Reflection Fluorescent mode, cellTIRF MITICO unit (Olympus);	100x, 1.5 NA UPLAPO100×OHR objective (Olympus);	Orca Flash 4.0 V.3 sCMOS camera (Hamamatsu, Bridgewater, NJ); 488 nm excitation laser (Coherent, Santa Clara, CA);	Olympus U-RTCE Real-Time Controller and cellSens interface (Olympus)
  file_create_date: ['2024-05-10T13:09:09.705990-04:00']
  experimenter: ['Silkunas, Mantas']
  institution: Old Dominion University
  lab: Pakhomov Lab
  session_id: TIRF-Imaging_Figure5
  Group /general/subject (Subject) 
  identifier: c2ac9e5a-1a2a-446f-82fa-8caed3ec872d
  session_description: Image series: TIRFImaging. Cell_line: HEK-293, Grown on Indium Tin Oxide (ITO) coated coverslip; Cal520 fluorescent indicator. Pulse application:	Patch clamp, voltage clamp mode, whole cell configuration with 0mV command voltage interrupted at by -50mV for 50ms followed by -400mV for 1ms (frame 91) followed by -50mV for 50ms; 0.4s into 2nd  and 3rd stacks, command voltage from 0mV changed to -50mV for 50ms.
  session_start_time: 2024-05-10T13:09:08.867416-04:00
  timestamps_reference_time: 2024-05-10T13:09:08.867416-04:00
