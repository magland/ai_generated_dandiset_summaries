
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000448/0.230421.1844
name: Time kinetics of the membrane potential at the cathode- and anode-facing poles of a cell induced by a train of 5 pulses at 833 kHz
contributor: [{'name': 'Silkuniene, Giedre', 'email': 'gsilkuni@odu.edu', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0001-8436-9718', 'affiliation': [], 'includeInCitation': True}, {'name': 'Kim, Vitalii', 'roleName': [], 'schemaKey': 'Person', 'identifier': '0000-0003-0699-5582', 'affiliation': [], 'includeInCitation': True}, {'name': 'Semenov, Iurii', 'roleName': [], 'schemaKey': 'Person', 'identifier': '0000-0002-0302-1355', 'affiliation': [], 'includeInCitation': True}, {'name': 'Pakhomov, Andrei', 'roleName': [], 'schemaKey': 'Person', 'identifier': '0000-0003-3816-3860', 'affiliation': [], 'includeInCitation': True}, {'name': 'National Institutes of Health', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': '1R21EY034258', 'contactPoint': [], 'includeInCitation': False}]
description: Time-lapse recordings for the investigation of the relationship between the electroporation efficiency of nsEP and changes in the transmembrane potential (TMP). A strobe imaging synchronized with nsEP exposure was used.  This allowed studying the nanosecond kinetics of TMP charging and relaxation, which is the primary effect of nsEP that rapidly charges the plasma membrane. The methodology involved pulsed laser fluorescence microscopy with voltage-sensitive FluoVolt dye-loaded cells that respond to TMP changes within nanoseconds. FluoVolt has a high sensitivity of about 10 % deltaF/F per 100 mV. During the imaging, a single short pulse laser flash is delivered at a precise time interval (addition of 25ns in each frame) before, during, or after nsEP exposure. The camera shutter opens in advance of and closes after the laser flash, capturing one TMP image per nsEP exposure. Supported by NIH 1R21EY034258
assetsSummary: {'species': [{'name': 'Cricetulus griseus - Cricetulus aureus', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10029'}], 'approach': [], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 3173065152, 'numberOfFiles': 18, 'numberOfSubjects': 18, 'variableMeasured': [], 'measurementTechnique': []}

Dandiset 000448 has 18 NWB files.
18 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/StrobeImaging (ImageSeries) Strobe Imaging method utilizes pulsed laser fluorescence microscopy where a single short pulse laser flash is delivered at a precise time interval before, during, or after the event (aplication of ns Electric pulse (nsEP)). Cells are loaded with a voltage-sensitive FluoVolt dye, which responds to Transmembrane Membrane Potential (TMP) changes within nanoseconds. The camera shutter opens in advance of and closes after the laser flash, capturing one TMP image per event (nsEP exposure). Multiple nsEP and laser flash combinations are delivered with programmed time interval increments (+25 ns) or decrements (-25 ns), to capture the time course of TMP during and after nsEP.
  file_create_date: ['2023-03-14T15:40:31.929065+00:00']
  experimenter: ['Semenov, Iurii ']
  institution: Old Dominion University
  lab: Pakhomov Lab
  session_id: 08_05_2022_cell09_F
  Group /general/subject (Subject) 
  identifier: f6dd8766-770e-4f7c-9de4-1c461f2eb643
  session_description: Pulse_shape: bipolar, Recording: forward (cell09), Cell_line: CHO, Pulse_duration: 600ns, Number_of_pulses: 5p, Pulse_repetition_rate: 833kHz, Electric_field: 0.3kV/cm, Dye: FluoVolt, Recording_type: strobe imaging
  session_start_time: 2022-08-05T21:36:26+00:00
  timestamps_reference_time: 2022-08-05T21:36:26+00:00
