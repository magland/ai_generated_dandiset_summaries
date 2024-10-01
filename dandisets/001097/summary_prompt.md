
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001097/0.240814.1849
name: Encoding of female mating dynamics by a hypothalamic line attractor
contributor: [{'url': 'https://adinair.people.caltech.edu/', 'name': 'Nair, Aditya', 'email': 'adi.nair@caltech.edu', 'roleName': ['dcite:Author', 'dcite:Conceptualization', 'dcite:ContactPerson', 'dcite:DataCollector', 'dcite:DataManager', 'dcite:FormalAnalysis'], 'schemaKey': 'Person', 'identifier': '0000-0001-5242-5527', 'includeInCitation': True}, {'name': 'HHMI', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/006w34k90', 'includeInCitation': False}, {'name': 'NIH', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01cwqze88', 'awardNumber': 'RO1MH112593', 'includeInCitation': False}, {'name': 'NIH', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01cwqze88', 'awardNumber': 'RO1MH123612', 'includeInCitation': False}, {'name': 'NIH', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01cwqze88', 'awardNumber': 'RO1NS123916', 'includeInCitation': False}, {'name': 'Agency of Science, Technology and Research, Singapore', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/059yjzn93', 'awardNumber': 'National Science Scholarship', 'includeInCitation': False}]
description: This dataset provides neural and behavioural annotation data from the paper: "Encoding of female mating dynamics by a hypothalamic line attractor". Data is stored in the NWB format and contains GCaMP traces, behavioural annotation (timing of behaviour), low-dimensional latent factors from dynamical models and other metadata.
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'behavioral approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 15616440, 'numberOfFiles': 2, 'numberOfSubjects': 2, 'variableMeasured': ['BehavioralEpochs', 'ProcessingModule'], 'measurementTechnique': [{'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 001097 has 2 NWB files.
1 of these NWB files are of type 1.
1 of these NWB files are of type 2.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /analysis/rSLDS (DynamicTable) Weight contributed by each cell for a particular latent factor.
  Dataset /analysis/rSLDS/id (ElementIdentifiers)  | shape = (176,) | dtype = int32
  Dataset /analysis/rSLDS/latent factor 1 (VectorData) latent factor 1 | shape = (176,) | dtype = float64
  Dataset /analysis/rSLDS/latent factor 2 (VectorData) latent factor 2 | shape = (176,) | dtype = float64
  file_create_date: ['2024-08-14T09:48:42.166190-07:00']
  Group /general/devices/inscopix-miniscope (Device) 1-p miniscope
  experiment_description: longitudinal imaging experiments.
  experimenter: ['Liu, Mengyu' 'Nair, Aditya']
  institution: California Institute of Technology
  keywords: ['ophys' 'behavior' 'female']
  lab: David Anderson Lab
  Group /general/subject (Subject) 
  identifier: fa3bf243-7626-4712-be6a-576c219ca625
  Group /processing/behavior (ProcessingModule) Processed behavioral data collected at 30.0hz. Timestamps are in seconds
  Group /processing/behavior/BehavioralEpochs (BehavioralEpochs) 
  Group /processing/behavior/BehavioralEpochs/Ch1: into_male_cage (IntervalSeries) Intervals where into_male_cage was ocurring.
  Group /processing/behavior/BehavioralEpochs/Ch1: intromission (IntervalSeries) Intervals where intromission was ocurring.
  Group /processing/behavior/BehavioralEpochs/Ch1: male_sniff (IntervalSeries) Intervals where male_sniff was ocurring.
  Group /processing/behavior/BehavioralEpochs/Ch1: mount (IntervalSeries) Intervals where mount was ocurring.
  Group /processing/behavior/BehavioralEpochs/Ch2: approach (IntervalSeries) Intervals where approach was ocurring.
  Group /processing/behavior/BehavioralEpochs/Ch2: check_genital (IntervalSeries) Intervals where check_genital was ocurring.
  Group /processing/behavior/BehavioralEpochs/Ch2: dart (IntervalSeries) Intervals where dart was ocurring.
  Group /processing/behavior/BehavioralEpochs/Ch2: into_male_cage (IntervalSeries) Intervals where into_male_cage was ocurring.
  Group /processing/behavior/BehavioralEpochs/Ch2: lordose (IntervalSeries) Intervals where lordose was ocurring.
  Group /processing/behavior/BehavioralEpochs/Ch2: sniff (IntervalSeries) Intervals where sniff was ocurring.
  Group /processing/behavior/BehavioralEpochs/Ch2: stay (IntervalSeries) Intervals where stay was ocurring.
  Group /processing/behavior/BehavioralEpochs/Ch2: top_up (IntervalSeries) Intervals where top_up was ocurring.
  Group /processing/behavior/BehavioralEpochs/Ch2: turn (IntervalSeries) Intervals where turn was ocurring.
  Group /processing/behavior/BehavioralEpochs/Ch2: wiggle (IntervalSeries) Intervals where wiggle was ocurring.
  Group /processing/ophys (ProcessingModule) Preprocessed calcium imaging data (motion correction + CNMFE).
  Group /processing/ophys/NeuralTrace (TimeSeries) Calcium imaging neural trace in VMHvl.
  session_description: resident-intruder assay
  session_start_time: 2022-09-30T00:00:00-07:00
  timestamps_reference_time: 2022-09-30T00:00:00-07:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /analysis/rSLDS (DynamicTable) Weight contributed by each cell for a particular latent factor.
  Dataset /analysis/rSLDS/id (ElementIdentifiers)  | shape = (72,) | dtype = int32
  Dataset /analysis/rSLDS/latent factor 1 (VectorData) latent factor 1 | shape = (72,) | dtype = float64
  Dataset /analysis/rSLDS/latent factor 2 (VectorData) latent factor 2 | shape = (72,) | dtype = float64
  file_create_date: ['2024-08-14T09:48:43.350771-07:00']
  Group /general/devices/inscopix-miniscope (Device) 1-p miniscope
  experiment_description: longitudinal imaging experiments.
  experimenter: ['Liu, Mengyu' 'Nair, Aditya']
  institution: California Institute of Technology
  keywords: ['ophys' 'behavior' 'female']
  lab: David Anderson Lab
  Group /general/subject (Subject) 
  identifier: b0ec5f05-0b30-4018-ac05-f6359064affe
  Group /processing/behavior (ProcessingModule) Processed behavioral data collected at 30.0hz. Timestamps are in seconds
  Group /processing/behavior/BehavioralEpochs (BehavioralEpochs) 
  Group /processing/behavior/BehavioralEpochs/Ch1: into_male_cage (IntervalSeries) Intervals where into_male_cage was ocurring.
  Group /processing/behavior/BehavioralEpochs/Ch1: intromission (IntervalSeries) Intervals where intromission was ocurring.
  Group /processing/behavior/BehavioralEpochs/Ch1: male_sniff (IntervalSeries) Intervals where male_sniff was ocurring.
  Group /processing/behavior/BehavioralEpochs/Ch1: mount (IntervalSeries) Intervals where mount was ocurring.
  Group /processing/behavior/BehavioralEpochs/Ch2: approach (IntervalSeries) Intervals where approach was ocurring.
  Group /processing/behavior/BehavioralEpochs/Ch2: dart (IntervalSeries) Intervals where dart was ocurring.
  Group /processing/behavior/BehavioralEpochs/Ch2: into_male_cage (IntervalSeries) Intervals where into_male_cage was ocurring.
  Group /processing/behavior/BehavioralEpochs/Ch2: kick (IntervalSeries) Intervals where kick was ocurring.
  Group /processing/behavior/BehavioralEpochs/Ch2: lordose (IntervalSeries) Intervals where lordose was ocurring.
  Group /processing/behavior/BehavioralEpochs/Ch2: sniff (IntervalSeries) Intervals where sniff was ocurring.
  Group /processing/behavior/BehavioralEpochs/Ch2: stay (IntervalSeries) Intervals where stay was ocurring.
  Group /processing/behavior/BehavioralEpochs/Ch2: top_up (IntervalSeries) Intervals where top_up was ocurring.
  Group /processing/behavior/BehavioralEpochs/Ch2: turn (IntervalSeries) Intervals where turn was ocurring.
  Group /processing/ophys (ProcessingModule) Preprocessed calcium imaging data (motion correction + CNMFE).
  Group /processing/ophys/NeuralTrace (TimeSeries) Calcium imaging neural trace in VMHvl.
  session_description: resident-intruder assay
  session_start_time: 2022-09-30T00:00:00-07:00
  timestamps_reference_time: 2022-09-30T00:00:00-07:00
