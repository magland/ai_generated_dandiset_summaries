
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000212/draft
name: Tracking of Drosophila during egg-laying decisions
contributor: [{'name': 'Vijayan, Vikram', 'email': 'vvijayan@rockefeller.edu', 'roleName': ['dcite:ContactPerson', 'dcite:DataCollector', 'dcite:Author', 'dcite:Conceptualization'], 'schemaKey': 'Person', 'identifier': '0000-0003-3948-7568', 'affiliation': [{'name': 'Rockefeller University', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/0420db125'}, {'name': 'Howard Hughes Medical Institute', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/006w34k90'}], 'includeInCitation': True}, {'name': 'Maimon, Gaby', 'email': 'maimon@rockefeller.edu', 'roleName': ['dcite:Author', 'dcite:ContactPerson', 'dcite:Conceptualization', 'dcite:Supervision'], 'schemaKey': 'Person', 'identifier': '0000-0003-1219-5856', 'affiliation': [{'name': 'Rockefeller University', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/0420db125'}, {'name': 'Howard Hughes Medical Institute', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/006w34k90'}], 'includeInCitation': True}, {'name': ' National Institutes of Health', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01s5ya894', 'awardNumber': 'R01NS121904', 'contactPoint': [], 'includeInCitation': False}, {'name': 'Howard Hughes Medical Institute', 'roleName': ['dcite:Affiliation', 'dcite:Funder'], 'schemaKey': 'Organization', 'contactPoint': [], 'includeInCitation': False}, {'name': 'Leon Levy Foundation', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'contactPoint': [], 'includeInCitation': False}, {'name': 'Kavli Neural Systems Institute', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'contactPoint': [], 'includeInCitation': False}, {'name': 'The Rockefeller University', 'roleName': ['dcite:Affiliation'], 'schemaKey': 'Organization', 'contactPoint': [], 'includeInCitation': False}]
description: Dataset on the egg-laying behavior of flies used to understand how flies make egg-laying decisions. Each NWB file contains time series data from an individual fly: the x-y position of the fly, egg-deposition moments of the fly, and sucrose concentration underneath the fly. A variety of fly genotypes and a variety of environments (egg-laying chambers) were used. Data and methods are described in "A rise-to-threshold signal for a relative value deliberation" (https://www.biorxiv.org/content/10.1101/2021.09.23.461548v1) and “An internal expectation guides Drosophila egg-laying decisions” (https://doi.org/10.1126/sciadv.abn3852). Please contact Vikram Vijayan and/or Gaby Maimon for more information including different download options and different raw/processed data formats.
assetsSummary: {'species': [{'name': 'Drosophila melanogaster - Fruit fly', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_7227'}, {'name': 'Drosophila suzukii', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_28584'}], 'approach': [{'name': 'behavioral approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 9004401256, 'numberOfFiles': 1013, 'numberOfSubjects': 1097, 'variableMeasured': ['Position', 'ProcessingModule', 'SpatialSeries'], 'measurementTechnique': [{'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000212 has 100 NWB files.
100 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2022-01-10T18:26:02.206000-05:00']
  experimenter: ['Vikram Vijayan']
  institution: The Rockefeller University / HHMI
  Group /general/subject (Subject) 
  identifier: 0_0_CS
  Group /processing/behavior (ProcessingModule) contains behavioral data
  Group /processing/behavior/Egg (TimeSeries) egg laid or not
  Group /processing/behavior/Island (TimeSeries) island of current substrate
  Group /processing/behavior/Position (Position) 
  Group /processing/behavior/Position/SpatialSeries (SpatialSeries) x and y position in chamber
  Group /processing/behavior/Sucrose_Concentration (TimeSeries) sucrose concentration of current substrate
  session_description: fly in egg laying chamber
  session_start_time: 2021-01-01T01:01:01.000000-05:00
  timestamps_reference_time: 2021-01-01T01:01:01.000000-05:00
