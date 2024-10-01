
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001031/0.240520.1924
name: High-frequency (100 kHz) rectangular bipolar pulses stimulation of individual hippocampal neurons: the effect of electric field
contributor: [{'name': 'Silkuniene, Giedre', 'email': 'giedre.silkuniene@gmail.com', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0001-8436-9718', 'affiliation': [], 'includeInCitation': True}, {'name': 'Kim, Vitalii', 'schemaKey': 'Person', 'identifier': '0000-0003-0699-5582', 'includeInCitation': True}, {'name': 'Pakhomov, Andrei', 'roleName': ['dcite:ProjectLeader'], 'schemaKey': 'Person', 'identifier': '0000-0003-3816-3860', 'includeInCitation': True}, {'name': 'National Institutes of Health', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': '5R21EY034803', 'includeInCitation': False}]
description: This dataset includes recordings of hippocampal neurons stimulated at 100 kHz under various amplitudes (measured as one polarity, V; the peak-to-peak value would be double this amount). Rectangular bipolar pulses were applied continuously for 2 seconds, beginning at 25 ms, with a 50% duty cycle. The pulse amplitude was constant at the indicated voltage. For the electrode configuration used, 1V corresponds to 36 V/cm. Neuron action potentials were visualized using the voltage-sensitive fluorescent dye, FluoVolt. This study was partially supported by NIH grant 15R21EY034803.
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 4305334, 'numberOfFiles': 10, 'numberOfSubjects': 20, 'variableMeasured': [], 'measurementTechnique': []}

Dandiset 001031 has 10 NWB files.
10 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/TimeLapseImaging (ImageSeries) TimeLapseImaging method utilizes fluorescence microscopy.Cells are loaded with a voltage-sensitive FluoVolt dye, which responds to Transmembrane Membrane Potential (TMP)changes within nanoseconds and that alowes Optical recording of induced action potentials.Images (16 x16 pixel) are recorded at 3134.8 frames/s
  file_create_date: ['2024-05-20T13:54:09.149171-04:00']
  experimenter: ['Vitalii, Kim']
  institution: Old Dominion University
  lab: Pakhomov Lab
  session_id: 100kHz_stimulation_4,0V
  Group /general/subject (Subject) 
  identifier: 4b03acbc-cd8c-4987-91a2-f64e6a996a4b
  session_description: 100 kHz stimulation of hippocampal neurons under 4.0V amplitude (measured as one polarity, V; peak-to-peak would be two-fold larger). Rectangular bipolar pulses were applied continuously for 2 seconds, beginning at 25 ms, with a 50% duty cycle. The pulse amplitude was constant at the indicated voltage. For the employed electrode configuration, 1V translates into 36 V/cm. Neuron action potentials were visualized using the voltage-sensitive fluorescent dye, FluoVolt. All experiments were performed in a low-conductance physiological solution containing (in mM): 140 NaGluconate, 5.4 KCl, 2 CaCl2, 1.5 MgCl2, 10 D-glucose, and 10 HEPES (pH 7.3, 290-300 mOsm/kg, 0.8 S/m).
  session_start_time: 2024-02-22T18:18:47-05:00
  timestamps_reference_time: 2024-02-22T18:18:47-05:00
