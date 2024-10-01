
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001052/0.240610.1814
name: Acute Random and FixedBurst stim in MFB and mPFC using Neuropixels in NAc
contributor: [{'name': 'Cowen, Stephen', 'email': 'scowen@email.arizona.edu', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'BRAIN Initiative', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/05h1kgg64', 'awardNumber': 'NS123424-01', 'includeInCitation': True}]
description: Anesthetized rats - recording effects of stim on NAc ensemble activity 
Funded by BRAIN Initiative NS123424-01
assetsSummary: {'species': [{'name': 'Rattus norvegicus - Norway rat', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10116'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 19510736, 'numberOfFiles': 12, 'numberOfSubjects': 12, 'variableMeasured': ['Units'], 'measurementTechnique': [{'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 001052 has 12 NWB files.
12 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2022-10-04T00:00:00.000000-07:00' '2024-06-10T10:45:43.160395-07:00']
  experimenter: ['Schmoe, Joe, L' 'Schmoe, Jane, B']
  institution: University of Arizona
  lab: Cowen and Heien labs
  session_id: Rat406_PFC
  stimulus: electrical stim
  Group /general/subject (Subject) 
  identifier: Rat406_PFC
  session_description: Acute Rat406 Regular stim in PFC using Neuropixels
  
  session_start_time: ['2022-10-04T00:00:00.000000-07:00']
  timestamps_reference_time: ['2022-10-04T00:00:00.000000-07:00']
  Group /units (Units) units table uSec
  Dataset /units/id (ElementIdentifiers)  | shape = (8,) | dtype = int64
  Dataset /units/spike_times (VectorData) no description | shape = (30051,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) indexes data | shape = (8,) | dtype = uint64
