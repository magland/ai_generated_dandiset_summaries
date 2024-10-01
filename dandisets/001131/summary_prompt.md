
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001131/0.240826.1647
name: A line attractor encoding a persistent internal state requires neuropeptide signaling
contributor: [{'name': 'Nair, Aditya', 'email': 'adi.nair@caltech.edu', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'HHMI', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/006w34k90', 'includeInCitation': False}, {'name': 'NIH', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01cwqze88', 'awardNumber': 'RO1MH112593', 'includeInCitation': False}, {'name': 'NIH', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01cwqze88', 'awardNumber': 'RO1MH123612', 'includeInCitation': False}, {'name': 'NIH', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01cwqze88', 'awardNumber': 'RO1NS123916', 'includeInCitation': False}, {'name': 'Agency of Science, Technology and Research, Singapore', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/059yjzn93', 'awardNumber': 'National Science Scholarship', 'includeInCitation': False}]
description: This dataset provides neural and behavioural annotation data from the paper: "A line attractor encoding a persistent internal state requires neuropeptide signaling". Data is stored in the NWB or HDF5 format and contains GCaMP traces, behavioural annotation (timing of behaviour) and other metadata.
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'behavioral approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 23676040, 'numberOfFiles': 2, 'numberOfSubjects': 2, 'variableMeasured': ['ProcessingModule', 'BehavioralEpochs'], 'measurementTechnique': [{'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 001131 has 2 NWB files.
2 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /analysis/rSLDS (DynamicTable) Weight contributed by each cell for a particular latent factor.
  Dataset /analysis/rSLDS/id (ElementIdentifiers)  | shape = (119,) | dtype = int32
  Dataset /analysis/rSLDS/latent factor 1 (VectorData) latent factor 1 | shape = (119,) | dtype = float64
  file_create_date: ['2024-08-26T09:43:34.832026-07:00']
  Group /general/devices/inscopix-miniscope (Device) 1-p miniscope
  experiment_description: imaging experiments.
  experimenter: ['Mountoufaris, George' 'Yang, Bin' 'Nair, Aditya']
  institution: California Institute of Technology
  keywords: ['ophys' 'behavior' 'male']
  lab: David Anderson Lab
  Group /general/subject (Subject) 
  identifier: 8ca648c7-0e00-4168-9268-34c506f703f1
  Group /processing/behavior (ProcessingModule) Processed behavioral data collected at 10.0hz. Timestamps are in seconds
  Group /processing/behavior/BehavioralEpochs (BehavioralEpochs) 
  Group /processing/behavior/BehavioralEpochs/Ch1: sniffing (IntervalSeries) Intervals where sniffing was ocurring.
  Group /processing/ophys (ProcessingModule) Preprocessed calcium imaging data (motion correction + CNMFE).
  Group /processing/ophys/NeuralTrace (TimeSeries) Calcium imaging neural trace in VMHvl.
  session_description: resident-intruder assay
  session_start_time: 2023-02-01T00:00:00-08:00
  timestamps_reference_time: 2023-02-01T00:00:00-08:00
