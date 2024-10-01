
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001030/0.240520.1924
name: High-frequency (2 kHz) sine wave  stimulation of individual hippocampal neurons: the effect of electric field
contributor: [{'name': 'Silkuniene, Giedre', 'email': 'giedre.silkuniene@gmail.com', 'roleName': ['dcite:ContactPerson', 'dcite:DataCurator'], 'schemaKey': 'Person', 'identifier': '0000-0001-8436-9718', 'affiliation': [], 'includeInCitation': True}, {'name': 'Kim, Vitalii', 'roleName': ['dcite:DataCollector', 'dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0003-0699-5582', 'includeInCitation': True}, {'name': 'Pakhomov, Andrei', 'roleName': ['dcite:ProjectLeader'], 'schemaKey': 'Person', 'identifier': '0000-0003-3816-3860', 'includeInCitation': True}, {'name': 'National Institutes of Health', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': '5R21EY034803', 'includeInCitation': False}]
description: 2 kHz stimulation of hippocampal neurons under different amplitudes (measured as one polarity, V; peak-to-peak would be two-fold larger). Sine wave amplitude was gradually increased during the initial 0.25 s, then stayed constant at the voltage indicated in session descriptions. Sine wave stimulation begins at 25 ms and lasts 2 s. For the employed electrode configuration, 1V translates into 36 V/cm. Neuron action potentials were visualized using the voltage-sensitive fluorescent dye, FluoVolt. The study was supported in part by NIH 15R21EY034803.
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 51968333, 'numberOfFiles': 17, 'numberOfSubjects': 34, 'variableMeasured': [], 'measurementTechnique': []}

Dandiset 001030 has 17 NWB files.
17 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/TimeLapseImaging (ImageSeries) TimeLapseImaging method utilizes fluorescence microscopy.Cells are loaded with a voltage-sensitive FluoVolt dye, which responds to Transmembrane Membrane Potential (TMP)changes within nanoseconds and that alowes Optical recording of induced action potentials.Images (16 x16 pixel) are recorded at 3134.8 frames/s
  file_create_date: ['2024-05-20T13:03:58.696824-04:00']
  experimenter: ['Vitalii, Kim']
  institution: Old Dominion University
  lab: Pakhomov Lab
  session_id: 2kHz_stimulation_1,0V
  Group /general/subject (Subject) 
  identifier: 668225e4-3f17-4413-826a-8ebc30c7c384
  session_description: 2 kHz stimulation of hippocampal neurons under 1.0V amplitude (measured as one polarity, V; peak-to-peak would be two-fold larger). Sine wave amplitude is gradually increased during the initial 0.25 s, then stays constant at the indicated voltage. Sine wave stimulation begins at 25 ms and lasts 2 s. For the employed electrode configuration, 1V translates into 36 V/cm. All experiments were performed in a low-conductance physiological solution containing (in mM): 140 NaGluconate, 5.4 KCl, 2 CaCl2, 1.5 MgCl2, 10 D-glucose, and 10 HEPES (pH 7.3, 290-300 mOsm/kg, 0.8 S/m).
  session_start_time: 2024-03-21T22:18:08-04:00
  timestamps_reference_time: 2024-03-21T22:18:08-04:00
