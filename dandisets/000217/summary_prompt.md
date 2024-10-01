
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000217/0.220125.2004
name: Sniff-synchronized, gradient-guided olfactory search by freely moving mice -- Behavioral Dataset
contributor: [{'name': 'Findley, Teresa', 'email': 'tmfindley15@gmail.com', 'roleName': ['dcite:ContactPerson', 'dcite:Author', 'dcite:Researcher'], 'schemaKey': 'Person', 'identifier': '0000-0002-2050-4869', 'affiliation': [{'name': 'University of Oregon', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/0293rh119'}], 'includeInCitation': True}, {'name': 'Wyrick, David G', 'roleName': ['dcite:Author', 'dcite:Researcher'], 'schemaKey': 'Person', 'identifier': '0000-0001-8096-5766', 'affiliation': [{'name': 'University of Oregon', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/0293rh119'}], 'includeInCitation': True}, {'name': 'Cramer, Jennifer L', 'roleName': ['dcite:Researcher', 'dcite:DataCollector', 'dcite:Author'], 'schemaKey': 'Person', 'affiliation': [{'name': 'University of Oregon', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/0293rh119'}], 'includeInCitation': True}, {'name': 'Brown, Morgan A', 'email': 'morganallen@gmail.com', 'roleName': ['dcite:DataCollector', 'dcite:Researcher', 'dcite:Author'], 'schemaKey': 'Person', 'affiliation': [{'name': 'University of Oregon', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/0293rh119'}], 'includeInCitation': True}, {'name': 'Holcomb, Blake', 'roleName': ['dcite:Author', 'dcite:DataCollector'], 'schemaKey': 'Person', 'affiliation': [{'name': 'University of Oregon', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/0293rh119'}], 'includeInCitation': True}, {'name': 'Attey, Robin', 'roleName': ['dcite:Author', 'dcite:DataCollector'], 'schemaKey': 'Person', 'affiliation': [{'name': 'University of Oregon', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/0293rh119'}], 'includeInCitation': True}, {'name': 'Yeh, Dorian', 'roleName': ['dcite:Author', 'dcite:DataCollector'], 'schemaKey': 'Person', 'affiliation': [{'name': 'University of Oregon', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/0293rh119'}], 'includeInCitation': True}, {'name': 'Monasevitch, Eric', 'roleName': ['dcite:Author', 'dcite:DataCollector'], 'schemaKey': 'Person', 'affiliation': [{'name': 'University of Oregon', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/0293rh119'}], 'includeInCitation': True}, {'name': 'Nouboussi, Nelly', 'roleName': ['dcite:Author', 'dcite:DataCollector'], 'schemaKey': 'Person', 'affiliation': [{'name': 'University of Oregon', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/0293rh119'}], 'includeInCitation': True}, {'name': 'Cullen, Isabelle', 'roleName': ['dcite:Author', 'dcite:DataCollector'], 'schemaKey': 'Person', 'affiliation': [{'name': 'University of Oregon', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/0293rh119'}], 'includeInCitation': True}, {'name': 'Songco, Jeremea O', 'roleName': ['dcite:Author', 'dcite:DataCollector'], 'schemaKey': 'Person', 'affiliation': [{'name': 'University of Oregon', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/0293rh119'}], 'includeInCitation': True}, {'name': 'King, Jared F', 'roleName': ['dcite:Author', 'dcite:DataCollector'], 'schemaKey': 'Person', 'affiliation': [{'name': 'University of Oregon', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/0293rh119'}], 'includeInCitation': True}, {'name': 'Ahmadian, Yashar', 'roleName': ['dcite:Author', 'dcite:ProjectLeader', 'dcite:Researcher'], 'schemaKey': 'Person', 'identifier': '0000-0002-5942-0697', 'affiliation': [{'name': 'University of Oregon', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/0293rh119'}, {'name': 'University of Cambridge', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/013meh722'}], 'includeInCitation': True}, {'name': 'Smear, Matt', 'email': 'smear@uoregon.edu', 'roleName': ['dcite:ProjectLeader', 'dcite:ContactPerson', 'dcite:Author', 'dcite:Researcher'], 'schemaKey': 'Person', 'identifier': '0000-0003-4689-388X', 'affiliation': [{'name': 'University of Oregon', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/0293rh119'}], 'includeInCitation': True}]
description: This dataset contains the movement tracking, sniff recording, and trial statistics for the dataset used in the publication: Sniff-synchronized, gradient-guided olfactory search by freely moving mice in eLife (Findley et al. 2021)
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 2152038728, 'numberOfFiles': 1121, 'numberOfSubjects': 25, 'variableMeasured': [], 'measurementTechnique': []}

Dandiset 000217 has 100 NWB files.
87 of these NWB files are of type 1.
13 of these NWB files are of type 2.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2017-12-11T15:16:32-08:00']
  session_id: Session 01
  Group /general/subject (Subject) 
  identifier: 2054_interleaved_01
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/chosen (VectorData) which side of the assay the mouse chose (correct or incorrect) | shape = (124,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (124,) | dtype = int32
  Dataset /intervals/trials/level (VectorData) the level of odor concentration stimulus presented | shape = (124,) | dtype = float64
  Dataset /intervals/trials/side (VectorData) which side of the assay the correct stimulus is presented on | shape = (124,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (124,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (124,) | dtype = float64
  session_description: Experiment type: interleaved, Mouse 2054, Session 01
  session_start_time: 2017-12-11T15:16:32-08:00
  timestamps_reference_time: 2017-12-11T15:16:32-08:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/sniff_signal (TimeSeries) no description
  file_create_date: ['2017-12-12T18:27:00-08:00']
  session_id: Session 02
  Group /general/subject (Subject) 
  identifier: 2054_interleaved_02
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/chosen (VectorData) which side of the assay the mouse chose (correct or incorrect) | shape = (143,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (143,) | dtype = int32
  Dataset /intervals/trials/level (VectorData) the level of odor concentration stimulus presented | shape = (143,) | dtype = float64
  Dataset /intervals/trials/side (VectorData) which side of the assay the correct stimulus is presented on | shape = (143,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (143,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (143,) | dtype = float64
  session_description: Experiment type: interleaved, Mouse 2054, Session 02
  session_start_time: 2017-12-12T18:27:00-08:00
  timestamps_reference_time: 2017-12-12T18:27:00-08:00
