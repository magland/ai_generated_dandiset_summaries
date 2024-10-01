
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001037/0.240816.1841
name: Causal evidence of a line attractor encoding an affective state
contributor: [{'url': 'https://adinair.people.caltech.edu/', 'name': 'Nair, Aditya', 'email': 'adi.nair@caltech.edu', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0001-5242-5527', 'affiliation': [], 'includeInCitation': True}, {'name': 'HHMI', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/006w34k90', 'includeInCitation': False}, {'name': 'NIH', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01cwqze88', 'awardNumber': 'RO1MH112593', 'includeInCitation': False}, {'name': 'NIH', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01cwqze88', 'awardNumber': 'RO1MH123612', 'includeInCitation': False}, {'name': 'NIH', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01cwqze88', 'awardNumber': 'RO1NS123916', 'includeInCitation': False}, {'name': 'Agency of Science, Technology and Research, Singapore', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/059yjzn93', 'awardNumber': 'National Science Scholarship', 'includeInCitation': False}]
description: This dataset provides neural and behavioural annotation data from the paper: "Causal evidence of a line attractor encoding an affective state". Data is stored in the NWB format and contains GCaMP traces, behavioural annotation (timing of behaviour), low-dimensional latent factors from dynamical models and other metadata.
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'behavioral approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 4589844, 'numberOfFiles': 2, 'numberOfSubjects': 2, 'variableMeasured': ['BehavioralEpochs', 'ProcessingModule'], 'measurementTechnique': [{'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 001037 has 2 NWB files.
1 of these NWB files are of type 1.
1 of these NWB files are of type 2.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /analysis/rSLDS (DynamicTable) Weight contributed by each cell for a particular latent factor.
  Dataset /analysis/rSLDS/id (ElementIdentifiers)  | shape = (65,) | dtype = int32
  Dataset /analysis/rSLDS/latent factor 1 (VectorData) latent factor 1 | shape = (65,) | dtype = float64
  Dataset /analysis/rSLDS/latent factor 2 (VectorData) latent factor 2 | shape = (65,) | dtype = float64
  file_create_date: ['2024-08-14T16:14:21.385476-07:00']
  Group /general/devices/2p-microscope (Device) 2-p microscope
  experiment_description: observation of aggression.
  experimenter: ['Vinograd, Amit' 'Nair, Aditya']
  institution: California Institute of Technology
  keywords: ['ophys' 'behavior' 'male']
  lab: David Anderson Lab
  Group /general/subject (Subject) 
  identifier: 810c75fc-cd56-4f2c-8b8b-fe82ed6c9709
  Group /processing/behavior (ProcessingModule) Processed behavioral data collected at 10.0hz. Timestamps are in seconds
  Group /processing/behavior/BehavioralEpochs (BehavioralEpochs) 
  Group /processing/behavior/BehavioralEpochs/Ch1: Balc in cage (IntervalSeries) Intervals where Balc in cage was ocurring.
  Group /processing/ophys (ProcessingModule) Preprocessed calcium imaging data (motion correction + CNMFE).
  Group /processing/ophys/NeuralTrace (TimeSeries) Calcium imaging neural trace in VMHvl.
  session_description: observation of resident-intruder assay
  session_start_time: 2023-03-23T00:00:00-07:00
  timestamps_reference_time: 2023-03-23T00:00:00-07:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /analysis/rSLDS (DynamicTable) Weight contributed by each cell for a particular latent factor.
  Dataset /analysis/rSLDS/id (ElementIdentifiers)  | shape = (56,) | dtype = int32
  Dataset /analysis/rSLDS/latent factor 1 (VectorData) latent factor 1 | shape = (56,) | dtype = float64
  Dataset /analysis/rSLDS/latent factor 2 (VectorData) latent factor 2 | shape = (56,) | dtype = float64
  file_create_date: ['2024-08-14T16:20:08.246082-07:00']
  Group /general/devices/inscopix-miniscope (Device) 1-p miniscope
  experiment_description: imaging experiments.
  experimenter: ['Vinograd, Amit' 'Nair, Aditya']
  institution: California Institute of Technology
  keywords: ['ophys' 'behavior' 'male']
  lab: David Anderson Lab
  Group /general/subject (Subject) 
  identifier: 66979a2a-b4a8-442c-a874-0f57d8cd0aa2
  Group /processing/behavior (ProcessingModule) Processed behavioral data collected at 10.0hz. Timestamps are in seconds
  Group /processing/behavior/BehavioralEpochs (BehavioralEpochs) 
  Group /processing/behavior/BehavioralEpochs/Ch1: attack (IntervalSeries) Intervals where attack was ocurring.
  Group /processing/ophys (ProcessingModule) Preprocessed calcium imaging data (motion correction + CNMFE).
  Group /processing/ophys/NeuralTrace (TimeSeries) Calcium imaging neural trace in VMHvl.
  session_description: resident-intruder assay
  session_start_time: 2023-05-17T00:00:00-07:00
  timestamps_reference_time: 2023-05-17T00:00:00-07:00
