
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001272/draft
name: The Use of Di8-ANEPPS to Evaluate Neuronal Sensitivity to Unmodulated Sine Waves
contributor: [{'name': 'Silkuniene, Giedre', 'email': 'giedre.silkuniene@gmail.com', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0001-8436-9718', 'affiliation': [], 'includeInCitation': True}, {'name': 'Kim, Vitalii', 'schemaKey': 'Person', 'identifier': '0000-0003-0699-5582', 'includeInCitation': True}, {'name': 'Semenov, Iurii', 'schemaKey': 'Person', 'identifier': '0000-0002-0302-1355', 'includeInCitation': True}, {'name': 'Pakhomov, Andrei', 'roleName': ['dcite:ProjectLeader'], 'schemaKey': 'Person', 'identifier': '0000-0003-3816-3860', 'includeInCitation': True}, {'name': 'National Institutes of Health', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': '5R21EY034803', 'includeInCitation': False}]
description: Experiments were conducted using the potentiometric dye Di8-ANEPPS, which detects voltage through an electrochromic mechanism, differing from the photo-induced electron transfer mechanism. The goal was to ensure that action potentials recorded with FluoVolt (published in other DANDIsets) were not influenced by the dye when applying intense sinewaves. Control experiments were performed using Di8-ANEPPS, chosen for its distinct molecular structure and voltage detection method. This study was partially supported by the NIH Brain Initiative (NEI R21EY034803).
assetsSummary: {'species': [{'name': 'Rattus norvegicus - Norway rat', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10116'}], 'approach': [], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 44171195, 'numberOfFiles': 65, 'numberOfSubjects': 3, 'variableMeasured': [], 'measurementTechnique': []}

Dandiset 001272 has 65 NWB files.
65 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/TimeLapseImaging (ImageSeries) Subject ID: 2_20240806. Stimulation was applied with a 250ms-long sine wave at 2kHz with 5.5V amplitude. The experiment was performed without tetrodotoxin (vehicle control). Note: Actual amplitude measured on the oscilloscope may be smaller due to calibration factors. For the employed electrode configuration, 1V translates to 36 V/cm at the location of neurons. Neuron action potentials were visualized using the voltage-sensitive fluorescent dye Di-8-ANEPPS, using TRITC filter cube. All experiments were performed in standard physiological solution containing (in mM): 140 NaCl, 5.4 KCl, 2 CaCl2, 1.5 MgCl2, 10 D-glucose, and 10 HEPES (pH 7.3, 290-300 mOsm/kg). More method details in the related manuscript
  file_create_date: ['2024-12-18T15:24:51.054729-05:00']
  experimenter: ['Iurii Semenov']
  institution: Old Dominion University
  lab: Pakhomov Lab
  session_id: Di-8-ANEPPS instead of FluoVolt
  Group /general/subject (Subject) 
  identifier: 36d40609-4d23-415c-aeb4-e0005fe54ad9
  session_description: Subject ID: 2_20240806. Stimulation was applied with a 250ms-long sine wave at 2kHz with 5.5V amplitude. The experiment was performed without tetrodotoxin (vehicle control). Note: Actual amplitude measured on the oscilloscope may be smaller due to calibration factors. For the employed electrode configuration, 1V translates to 36 V/cm at the location of neurons. Neuron action potentials were visualized using the voltage-sensitive fluorescent dye Di-8-ANEPPS, using TRITC filter cube. All experiments were performed in standard physiological solution containing (in mM): 140 NaCl, 5.4 KCl, 2 CaCl2, 1.5 MgCl2, 10 D-glucose, and 10 HEPES (pH 7.3, 290-300 mOsm/kg). More method details in the related manuscript
  session_start_time: 2024-08-06T20:22:10-04:00
  timestamps_reference_time: 2024-08-06T20:22:10-04:00
