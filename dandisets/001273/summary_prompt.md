
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001273/draft
name: Kinetics of Membrane Charging and Its Dependence on Neuron Shape and Alignment with the Electric Field
contributor: [{'name': 'Silkuniene, Giedre', 'email': 'giedre.silkuniene@gmail.com', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0001-8436-9718', 'affiliation': [], 'includeInCitation': True}, {'name': 'National Institutes of Health', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': '5R21EY034803', 'includeInCitation': False}, {'name': 'Kim, Vitalii ', 'schemaKey': 'Person', 'identifier': '0000-0003-0699-5582', 'includeInCitation': True}, {'name': 'Semenov, Iurii', 'schemaKey': 'Person', 'identifier': '0000-0002-0302-1355', 'includeInCitation': True}, {'name': 'Pakhomov, Andrei', 'schemaKey': 'Person', 'identifier': '0000-0003-3816-3860', 'includeInCitation': True}]
description: This experimental series aimed to visualize and characterize plasma membrane (PM) polarization dynamics in hippocampal neurons exposed to 2 µs electric pulses, focusing on the influence of neuronal shape and position within the applied electric field. Neurons were pre-loaded with FluoVolt potentiometric dye, and pulsed laser strobe microscopy was employed to capture changes in membrane polarization. This study was partially supported by the NIH Brain Initiative (NEI R21EY034803).
assetsSummary: {'species': [{'name': 'Rattus norvegicus - Norway rat', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10116'}], 'approach': [], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 10631548786, 'numberOfFiles': 181, 'numberOfSubjects': 13, 'variableMeasured': [], 'measurementTechnique': []}

Dandiset 001273 has 100 NWB files.
100 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/StrobeImaging (ImageSeries) Optical time-lapse (strobe imaging) recording of plasma membrane (PM) polarization performed at 6 Hz (Image frames were taken at this rate, but the data represent events occurring at a 40 MHz rate). Exposures began 1 µs after the start of the recording. The strobe imaging method utilizes pulsed laser fluorescence microscopy, where a single short-pulse laser flash is delivered at a precise time interval before, during, or after the event (application of electric pulse (EP)). Cells are pre-loaded with a voltage-sensitive FluoVolt dye, which responds to transmembrane potential (TMP) changes within nanoseconds. The camera shutter opens before and closes after the laser flash, capturing one TMP image per event (EP exposure). Multiple EP and laser flash combinations are delivered with programmed time interval increments (+50 ns) or decrements (-50 ns) to capture the time course of TMP during and after EP. The image series represents events lasting 8 µs and containing 160 individual frames.
  file_create_date: ['2025-01-02T15:33:27.185768-05:00']
  experimenter: ['Iurii Semenov']
  institution: Old Dominion University
  lab: Pakhomov Lab
  session_id: PM polarization
  Group /general/subject (Subject) 
  identifier: cdae1469-e223-4df0-9358-e06ef598660b
  session_description: Subject ID: 1_20240117. Stimulation was applied with 2 µs long rectangular pulse at 40,0V amplitude . The recording was performed in a backward manner, starting after pulse application and proceeding in reverse to ensure repeated pulses did not alter the cell's response. Electrode position not specified. Note: For 40V pulse amplitude, the actual measured amplitude was 25V; for 80V, the actual measured was 62V; for 100V, the actual measured was 79V; and for 130V, the actual measured was 102V. Distance between electrodes 1.4 mm, electrode diameter 0.5 mm. Neuron action potentials were visualized using the voltage-sensitive fluorescent dye FluoVolt FITC filter cube. All experiments were performed in standard physiological solution containing (in mM): 140 NaCl, 5.4 KCl, 2 CaCl2, 1.5 MgCl2, 10 D-glucose, and 10 HEPES (pH 7.3, 290-300 mOsm/kg). More method details in the related manuscript.
  session_start_time: 2024-01-17T19:26:21-05:00
  timestamps_reference_time: 2024-01-17T19:26:21-05:00
