
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001182/0.240827.1656
name: Stimulus-specific hypothalamic encoding of a persistent defensive state
contributor: [{'name': 'Nair, Aditya', 'email': 'adi.nair@caltech.edu', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'HHMI', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/006w34k90', 'includeInCitation': False}, {'name': 'NIH', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01cwqze88', 'awardNumber': 'MH112593.', 'includeInCitation': False}, {'name': 'NIH', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01cwqze88', 'awardNumber': 'MH117264', 'includeInCitation': False}, {'name': 'Kennedy, Ann', 'email': 'ann.kennedy@northwestern.edu', 'roleName': ['dcite:Author', 'dcite:DataManager', 'dcite:DataCurator', 'dcite:FormalAnalysis', 'dcite:Investigation'], 'schemaKey': 'Person', 'includeInCitation': True}]
description: This dataset provides neural and behavioural annotation data from the paper: "Stimulus-specific hypothalamic encoding of a persistent defensive state". Data is stored in the NWB format and contains GCaMP traces, behavioural annotation (timing of behaviour) and other metadata.


assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'behavioral approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 87598800, 'numberOfFiles': 15, 'numberOfSubjects': 15, 'variableMeasured': ['BehavioralEpochs', 'ProcessingModule'], 'measurementTechnique': [{'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 001182 has 15 NWB files.
15 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2024-08-27T09:32:11.697002-07:00']
  Group /general/devices/inscopix-miniscope (Device) 1-p miniscope
  experiment_description: imaging experiments.
  experimenter: ['Kunwar, Prabhat' 'Li, Lingyun']
  institution: California Institute of Technology
  keywords: ['ophys' 'behavior' 'male']
  lab: David Anderson Lab
  Group /general/subject (Subject) 
  identifier: 970bd4bb-a8db-465f-b078-aae65f111a7f
  Group /processing/behavior (ProcessingModule) Processed behavioral data collected at 11.0hz. Timestamps are in seconds
  Group /processing/behavior/BehavioralEpochs (BehavioralEpochs) 
  Group /processing/behavior/BehavioralEpochs/Ch1: baseline (IntervalSeries) Intervals where baseline was ocurring.
  Group /processing/ophys (ProcessingModule) Preprocessed calcium imaging data (motion correction + CNMFE).
  Group /processing/ophys/NeuralTrace (TimeSeries) Calcium imaging neural trace in VMHvl.
  session_description: defensive_behavior_assay
  session_start_time: 2020-09-16T00:00:00-07:00
  timestamps_reference_time: 2020-09-16T00:00:00-07:00
