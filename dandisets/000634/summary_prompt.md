
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000634/0.231005.1820
name: Cell Membrane Charging by Co- and Counter-Directional ns electrical pulses (nsEP)
contributor: [{'name': 'Silkuniene, Giedre', 'email': 'giedre.silkuniene@gmail.com', 'roleName': ['dcite:ContactPerson', 'dcite:DataCurator'], 'schemaKey': 'Person', 'identifier': '0000-0001-8436-9718', 'affiliation': [], 'includeInCitation': True}, {'name': 'Kim, Vitalii', 'roleName': [], 'schemaKey': 'Person', 'identifier': '0000-0003-0699-5582', 'affiliation': [], 'includeInCitation': True}, {'name': 'Semenov, Iurii', 'roleName': [], 'schemaKey': 'Person', 'identifier': '0000-0002-0302-1355', 'affiliation': [], 'includeInCitation': True}, {'name': 'Pakhomov, Andrei', 'roleName': [], 'schemaKey': 'Person', 'identifier': '0000-0003-3816-3860', 'affiliation': [], 'includeInCitation': True}, {'name': 'National Institutes of Health ', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': 'NIH 1R21EY034258', 'contactPoint': [], 'includeInCitation': False}]
description: Strobe photography, used at nanosecond resolution, captures the dynamic process of cell membrane charging and relaxation kinetics in cells treated with FluoVolt dye and exposed to electric pulses. This study uses a triangular electrode array where 300 ns pulses are applied alternately at a frequency of 1.67 MHz. The precise coordination of electric pulses and laser flashes, adjusted in 50 ns steps, allows for the detailed imaging of the cell's response. The electric field induces enhanced fluorescence at the cathode-facing side of the FluoVolt-loaded CHO cells and suppressed fluorescence at the anode-facing side. This research method provides a comprehensive and reliable examination of the cell membrane's behavior under electrical stimulation without causing damage, ensuring consistent observations to understand cellular responses to varying electrical stimuli. Supported by NIH 1R21EY034258
assetsSummary: {'species': [{'name': 'Cricetulus griseus - Cricetulus aureus', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10029'}], 'approach': [], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 1035526841, 'numberOfFiles': 10, 'numberOfSubjects': 10, 'variableMeasured': [], 'measurementTechnique': []}

Dandiset 000634 has 10 NWB files.
10 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/StrobeImaging (ImageSeries) Strobe Imaging method utilizes pulsed laser fluorescence microscopy where a single short pulse laser flash is delivered at a precise time interval before, during, or after the event (aplication of ns Electric pulse (nsEP)). Cells are loaded with a voltage-sensitive FluoVolt dye, which responds to Transmembrane Membrane Potential (TMP) changes within nanoseconds. The camera shutter opens in advance of and closes after the laser flash, capturing one TMP image per event (nsEP exposure). Multiple nsEP and laser flash combinations are delivered with programmed time interval increments (+50 ns) or decrements (-50 ns), to capture the time course of TMP during and after nsEP. Image series represents events of 11µs that contains 220 individual frames. 
  file_create_date: ['2023-10-05T12:29:17.814127-04:00']
  experimenter: ['Semenov, Iurii ']
  institution: Old Dominion University
  lab: Pakhomov Lab
  session_id: StrobeImaging_Figure5
  Group /general/subject (Subject) 
  identifier: a71ec7e1-e97e-4464-9439-357ad86e5850
  session_description: Cell_line: CHO, Pulse_duration: 300ns, Pulse_repetition_rate: 1.67MHz, Electric_field: 0.15kV/cm, number of pulses: 24, Elecrtode array: triangular, Pulses applied alternately to base electrodes E1 and E2, and inactive electrode became groud; Dye: FluoVolt, Recording_type: strobe imaging
  session_start_time: 2022-09-09T19:50:14-04:00
  timestamps_reference_time: 2022-09-09T19:50:14-04:00
