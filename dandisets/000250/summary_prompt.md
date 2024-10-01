
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000250/draft
name: High-resolution tracking of Drosophila during egg-laying
contributor: [{'name': 'National Institutes of Health (NIH)', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': '1 R01 NS 121904-01'}, {'name': 'Vijayan, Vikram', 'email': 'vvijayan@rockefeller.edu', 'roleName': ['dcite:ContactPerson', 'dcite:DataCollector', 'dcite:Author', 'dcite:Conceptualization'], 'schemaKey': 'Person', 'identifier': '0000-0003-3948-7568', 'affiliation': [{'name': 'Rockefeller University', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/0420db125'}, {'name': 'Howard Hughes Medical Institute', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/006w34k90'}], 'includeInCitation': True}, {'name': 'Maimon, Gaby', 'email': 'maimon@rockefeller.edu', 'roleName': ['dcite:Author', 'dcite:Conceptualization', 'dcite:ContactPerson', 'dcite:Supervision'], 'schemaKey': 'Person', 'identifier': '0000-0003-1219-5856', 'affiliation': [{'name': 'Rockefeller University', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/0420db125'}, {'name': 'Howard Hughes Medical Institute', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/006w34k90'}], 'includeInCitation': True}, {'name': 'Howard Hughes Medical Institute', 'roleName': ['dcite:Affiliation', 'dcite:Funder'], 'schemaKey': 'Organization', 'contactPoint': [], 'includeInCitation': False}, {'name': 'The Rockefeller University', 'roleName': ['dcite:Affiliation'], 'schemaKey': 'Organization', 'contactPoint': [], 'includeInCitation': False}, {'name': 'Kavli Neural Systems Institute', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'contactPoint': [], 'includeInCitation': False}, {'name': 'Leon Levy Foundation', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'contactPoint': [], 'includeInCitation': False}]
description: Dataset on the egg-laying behavior of flies used to understand the egg-laying behavioral sequence. Each NWB file contains time series data from an individual fly: the x-y position of the fly, the body length of the fly, egg-deposition moments of the fly, and other behavioral annotations related to egg laying. Data and methods are described in "A rise-to-threshold signal for a relative value deliberation" (https://www.biorxiv.org/content/10.1101/2021.09.23.461548v1). Please contact Vikram Vijayan and/or Gaby Maimon for more information including different download options and different raw/processed data formats.
assetsSummary: {'species': [{'name': 'Drosophila melanogaster - Fruit fly', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_7227'}], 'approach': [{'name': 'behavioral approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 100324608, 'numberOfFiles': 3, 'numberOfSubjects': 3, 'variableMeasured': ['ProcessingModule', 'SpatialSeries', 'Position'], 'measurementTechnique': [{'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000250 has 3 NWB files.
3 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2022-05-19T15:29:06.068000-04:00']
  experimenter: ['Vikram Vijayan']
  institution: The Rockefeller University / HHMI
  Group /general/subject (Subject) 
  identifier: Canton S (CS) fly in circular sloped ceiling chamber
  Group /processing/behavior (ProcessingModule) contains behavioral data
  Group /processing/behavior/Abdomen Bend Complete (TimeSeries) abdomen bend to lay egg complete
  Group /processing/behavior/Egg Deposition (TimeSeries) egg deposition moments
  Group /processing/behavior/Neck to Tip Length (TimeSeries) Neck to Tip Length
  Group /processing/behavior/Ovulation Start (TimeSeries) ovulation start
  Group /processing/behavior/Position (Position) 
  Group /processing/behavior/Position/SpatialSeries (SpatialSeries) x and y position in chamber
  Group /processing/behavior/Seach Start (TimeSeries) search start
  Group /processing/behavior/Sucrose_Concentration (TimeSeries) sucrose concentration of current substrate
  session_description: fly in egg laying chamber
  session_start_time: 2021-01-01T01:01:01.000000-05:00
  timestamps_reference_time: 2021-01-01T01:01:01.000000-05:00
