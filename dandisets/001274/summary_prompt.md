
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001274/draft
name: Characterization of Plasma Membrane Polarization in Hippocampal Neurons During Sine Wave and Modulated Sine Wave Stimulation
contributor: [{'name': 'Silkuniene, Giedre', 'email': 'giedre.silkuniene@gmail.com', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0001-8436-9718', 'affiliation': [], 'includeInCitation': True}, {'name': 'Kim, Vitalii', 'schemaKey': 'Person', 'identifier': '0000-0003-0699-5582', 'includeInCitation': True}, {'name': 'Semenov, Iurii ', 'schemaKey': 'Person', 'identifier': '0000-0002-0302-1355', 'includeInCitation': True}, {'name': 'Pakhomov, Andrei', 'roleName': ['dcite:ProjectLeader'], 'schemaKey': 'Person', 'identifier': '0000-0003-3816-3860', 'includeInCitation': True}, {'name': 'National Institutes of Health', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': '5R21EY034803', 'includeInCitation': False}]
description: This experimental series aimed to visualize and characterize plasma membrane (PM) polarization dynamics in hippocampal neurons exposed to 2 kHz sine waves or 2 kHz sine waves modulated at 100 Hz or 154 Hz. Neurons were pre-loaded with FluoVolt potentiometric dye to enable visualization of membrane polarization changes. This study was partially supported by the NIH Brain Initiative (NEI R21EY034803).
assetsSummary: {'species': [{'name': 'Rattus norvegicus - Norway rat', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10116'}], 'approach': [], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 23609898505, 'numberOfFiles': 222, 'numberOfSubjects': 19, 'variableMeasured': [], 'measurementTechnique': []}

Dandiset 001274 has 100 NWB files.
100 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/StrobeImaging (ImageSeries) Optical time-lapse (strobe imaging) recordings of plasma membrane (PM) polarization were performed at 6 Hz (image frames were taken at this rate, but the data represent events occurring at MHz rates). Exposures began 1 µs after the start of recording for single pulse exposures and immediately at the start of the recordings for sine wave exposures. The strobe imaging method utilizes pulsed laser fluorescence microscopy, where a single short-pulse laser flash is delivered at a precise time interval before, during, or after the event (application of an electric pulse (EP)). Cells were pre-loaded with a voltage-sensitive FluoVolt dye, which responds to transmembrane potential changes within nanoseconds.
  file_create_date: ['2025-01-03T15:45:25.501776-05:00']
  experimenter: ['Iurii Semenov']
  institution: Old Dominion University
  lab: Pakhomov Lab
  session_id: PM polarization with sinewaves and modulated sine waves (spindles)
  Group /general/subject (Subject) 
  identifier: 6437aa34-205a-45d3-92a0-2bbdf1e9581f
  session_description: Subject ID: 1_20240522. Stimulation was applied with a single 2 µs long rectangular pulse at 10,0V amplitude . The experiment was performed without tetrodotoxin (vehicle control). The recording was performed in a forward manner, following the sequence of pulse application to mimic the real-time progression of events. Electrode position not specified. Distance between electrodes 0.12 mm, electrode diameter 0.1 mm. Neuron action potentials were visualized using the voltage-sensitive fluorescent dye FluoVolt and a FITC filter cube. All experiments were performed in standard physiological solution containing (in mM): 140 NaCl, 5.4 KCl, 2 CaCl2, 1.5 MgCl2, 10 D-glucose, and 10 HEPES (pH 7.3, 290-300 mOsm/kg). More method details in the related manuscript.
  session_start_time: 2024-05-22T22:12:40-04:00
  timestamps_reference_time: 2024-05-22T22:12:40-04:00
