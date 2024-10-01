
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000351/draft
name: Jeong et al (2022) Mesolimbic dopamine release conveys causal associations
contributor: [{'name': 'Jeong, Huijeong', 'email': 'huijeong.jeong@ucsf.edu', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0003-1219-4191', 'affiliation': [{'name': 'University of California, San Francisco', 'schemaKey': 'Affiliation'}], 'includeInCitation': True}, {'name': 'Taylor, Annie', 'email': 'Annie.Taylor@ucsf.edu', 'roleName': [], 'schemaKey': 'Person', 'affiliation': [{'name': 'University of California, San Francisco', 'schemaKey': 'Affiliation'}], 'includeInCitation': True}, {'name': 'Floeder, Joseph R ', 'email': 'Joey.Floeder@ucsf.edu', 'roleName': [], 'schemaKey': 'Person', 'affiliation': [{'name': 'University of California, San Francisco', 'schemaKey': 'Affiliation'}], 'includeInCitation': True}, {'name': 'Lohmann, Martin', 'email': 'martin.lohmann@alleninstitute.org', 'roleName': [], 'schemaKey': 'Person', 'affiliation': [{'name': 'Allen Institute for Brain Science', 'schemaKey': 'Affiliation'}], 'includeInCitation': True}, {'name': 'Mihalas, Stefan', 'email': 'stefan.mihalas@gmail.com', 'roleName': [], 'schemaKey': 'Person', 'affiliation': [{'name': 'Allen Institute for Brain Science', 'schemaKey': 'Affiliation'}], 'includeInCitation': True}, {'name': 'Wu, Brenda', 'email': 'Brenda.Wu@ucsf.edu', 'roleName': [], 'schemaKey': 'Person', 'affiliation': [{'name': 'University of California, San Francisco', 'schemaKey': 'Affiliation'}], 'includeInCitation': True}, {'name': 'Zhou, Mingkang', 'email': 'Mingkang.Zhou@ucsf.edu', 'roleName': [], 'schemaKey': 'Person', 'affiliation': [{'name': 'University of California, San Francisco', 'schemaKey': 'Affiliation'}], 'includeInCitation': True}, {'name': 'Burke, Dennis A', 'email': 'Dennis.Burke@ucsf.edu', 'roleName': [], 'schemaKey': 'Person', 'affiliation': [{'name': 'University of California, San Francisco', 'schemaKey': 'Affiliation'}], 'includeInCitation': True}, {'name': 'K Namboodiri, Vijay Mohan', 'email': 'vijaymohan.knamboodiri@ucsf.edu', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0002-6674-610X', 'affiliation': [{'name': 'University of California, San Francisco', 'schemaKey': 'Affiliation'}], 'includeInCitation': True}, {'name': 'National Institute of Mental Health', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': 'R00MH118422, R01MH129582', 'contactPoint': [], 'includeInCitation': False}, {'name': 'Scott Alan Myers Endowed Professorship', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'contactPoint': [], 'includeInCitation': False}]
description: This dataset includes fiber photometry (NAcc) and behavioral data from Jeong et al., 2022: "Mesolimbic dopamine release conveys causal associations". Animals names and session numbers used for each figure can be found from 'Subject and session information' in Related resource.
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 98548166664, 'numberOfFiles': 428, 'numberOfSubjects': 28, 'variableMeasured': ['ProcessingModule'], 'measurementTechnique': [{'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000351 has 100 NWB files.
36 of these NWB files are of type 1.
64 of these NWB files are of type 2.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/eventidx_table (AnnotatedEventsTable) event index table
  Dataset /acquisition/eventidx_table/event_description (VectorData) Description for each event type. | shape = (4,) | dtype = object
  Dataset /acquisition/eventidx_table/event_index (VectorData) Index for each event type. | shape = (4,) | dtype = int32
  Dataset /acquisition/eventidx_table/id (ElementIdentifiers)  | shape = (4,) | dtype = int32
  Group /acquisition/eventlog (Eventlog) 
  file_create_date: ['2022-11-04T18:36:14.172929-07:00']
  institution: University of California, San Francisco
  lab: Namboodiri lab
  session_id: Day1_30
  Group /general/subject (Subject) 
  identifier: photometry-NAcc-dLight1.3b-DB_longITI_C1_F1
  session_description: DB_longITI_C1_F1
  session_start_time: 2022-04-02T13:48:29-07:00
  timestamps_reference_time: 2022-04-02T13:48:29-07:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/eventidx_table (AnnotatedEventsTable) event index table
  Dataset /acquisition/eventidx_table/event_description (VectorData) Description for each event type. | shape = (4,) | dtype = object
  Dataset /acquisition/eventidx_table/event_index (VectorData) Index for each event type. | shape = (4,) | dtype = int32
  Dataset /acquisition/eventidx_table/id (ElementIdentifiers)  | shape = (4,) | dtype = int32
  Group /acquisition/eventlog (Eventlog) 
  Group /acquisition/photometry (FiberPhotometrySeries) no description
  file_create_date: ['2022-11-04T16:53:14.243005-07:00']
  institution: University of California, San Francisco
  lab: Namboodiri lab
  session_id: Day1
  Group /general/subject (Subject) 
  identifier: photometry-NAcc-dLight1.3b-HJ_FP_F1
  Group /processing/photometry (ProcessingModule) photometry
  Group /processing/photometry/dff (DffSeries) calculated dff and timestamps aligned to behavior timestamps
  session_description: RandomRewards
  session_start_time: 2021-09-06T15:47:23-07:00
  timestamps_reference_time: 2021-09-06T15:47:23-07:00
