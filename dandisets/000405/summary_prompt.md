
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000405/draft
name: Gonzalez & Giocomo (2022) Parahippocampal neurons encode task-relevant information for goal-directed navigation
contributor: [{'name': 'Gonzalez, Alex', 'email': 'alexgb2010@gmail.com', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}]
description: Data used in the Gonzalez & Giocomo (2022) manuscript. This contains session electrophysiological data and accompanying event metadata/time-series necessary to generate figures in the manuscript. Github link contains metadata files that contain information for each session, including if it is an open-field foraging session or a Tree-Maze session, and how many units were collected in it. Additional metadata includes unit matching across session and a detailed behavioral performance table.

Pre-print DOI: 
https://doi.org/10.1101/2022.12.15.520660

Github:
https://github.com/alexgonzl/TMA

assetsSummary: {'species': [{'name': 'Rattus norvegicus - Norway rat', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10116'}], 'approach': [], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 3877487528, 'numberOfFiles': 276, 'numberOfSubjects': 5, 'variableMeasured': [], 'measurementTechnique': []}

Dandiset 000405 has 100 NWB files.
49 of these NWB files are of type 1.
51 of these NWB files are of type 2.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/firing_rates (TimeSeries) no description
  Group /acquisition/track_data (TimeSeries) columns=x,y,hd,sp,ha
  Group /acquisition/unit_table (DynamicTable) 
  Dataset /acquisition/unit_table/cl_name (VectorData) no description | shape = (14,) | dtype = object
  Dataset /acquisition/unit_table/id (ElementIdentifiers)  | shape = (14,) | dtype = int64
  Dataset /acquisition/unit_table/unit_type (VectorData) no description | shape = (14,) | dtype = object
  Dataset /acquisition/unit_table/uuid (VectorData) no description | shape = (14,) | dtype = int64
  file_create_date: ['2023-01-17T10:27:07.707715-08:00']
  experimenter: ['Gonzalez, Alex']
  institution: Stanford
  lab: Giocomo
  session_id: Li_OF_052818
  Group /general/subject (Subject) 
  identifier: s0_se1
  session_description: OF
  session_start_time: 0018-05-28T00:00:00-08:00
  timestamps_reference_time: 0018-05-28T00:00:00-08:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/event_table (DynamicTable) 
  Dataset /acquisition/event_table/dur (VectorData) no description | shape = (1024,) | dtype = int64
  Dataset /acquisition/event_table/event (VectorData) no description | shape = (1024,) | dtype = object
  Dataset /acquisition/event_table/id (ElementIdentifiers)  | shape = (1024,) | dtype = int64
  Dataset /acquisition/event_table/out_bound (VectorData) no description | shape = (1024,) | dtype = int64
  Dataset /acquisition/event_table/t0 (VectorData) no description | shape = (1024,) | dtype = int64
  Dataset /acquisition/event_table/tE (VectorData) no description | shape = (1024,) | dtype = int64
  Dataset /acquisition/event_table/trial_num (VectorData) no description | shape = (1024,) | dtype = int64
  Group /acquisition/firing_rates (TimeSeries) no description
  Group /acquisition/track_data (TimeSeries) columns=x,y,hd
  Group /acquisition/trial_table (DynamicTable) 
  Dataset /acquisition/trial_table/correct (VectorData) no description | shape = (61,) | dtype = float64
  Dataset /acquisition/trial_table/cue (VectorData) no description | shape = (61,) | dtype = object
  Dataset /acquisition/trial_table/dec (VectorData) no description | shape = (61,) | dtype = object
  Dataset /acquisition/trial_table/dur (VectorData) no description | shape = (61,) | dtype = int64
  Dataset /acquisition/trial_table/goal (VectorData) no description | shape = (61,) | dtype = float64
  Dataset /acquisition/trial_table/grw (VectorData) no description | shape = (61,) | dtype = int64
  Dataset /acquisition/trial_table/id (ElementIdentifiers)  | shape = (61,) | dtype = int64
  Dataset /acquisition/trial_table/long (VectorData) no description | shape = (61,) | dtype = float64
  Dataset /acquisition/trial_table/sw (VectorData) no description | shape = (61,) | dtype = int64
  Dataset /acquisition/trial_table/t0 (VectorData) no description | shape = (61,) | dtype = int64
  Dataset /acquisition/trial_table/tD (VectorData) no description | shape = (61,) | dtype = int64
  Dataset /acquisition/trial_table/tE (VectorData) no description | shape = (61,) | dtype = int64
  Dataset /acquisition/trial_table/tE_1 (VectorData) no description | shape = (61,) | dtype = int64
  Dataset /acquisition/trial_table/tE_2 (VectorData) no description | shape = (61,) | dtype = int64
  Dataset /acquisition/trial_table/tR (VectorData) no description | shape = (61,) | dtype = int64
  Dataset /acquisition/trial_table/vsw (VectorData) no description | shape = (61,) | dtype = int64
  Group /acquisition/unit_table (DynamicTable) 
  Dataset /acquisition/unit_table/cl_name (VectorData) no description | shape = (2,) | dtype = object
  Dataset /acquisition/unit_table/id (ElementIdentifiers)  | shape = (2,) | dtype = int64
  Dataset /acquisition/unit_table/unit_type (VectorData) no description | shape = (2,) | dtype = object
  Dataset /acquisition/unit_table/uuid (VectorData) no description | shape = (2,) | dtype = int64
  file_create_date: ['2023-01-17T10:27:06.512576-08:00']
  experimenter: ['Gonzalez, Alex']
  institution: Stanford
  lab: Giocomo
  session_id: Li_T3g_052818
  Group /general/subject (Subject) 
  identifier: s0_se0
  session_description: T3g
  session_start_time: 0018-05-28T00:00:00-08:00
  timestamps_reference_time: 0018-05-28T00:00:00-08:00
