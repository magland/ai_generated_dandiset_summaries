
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001171/0.240917.1434
name: Data for: Whisker deprivation triggers a distinct form of cortical homeostatic plasticity that is impaired in the Fmr1 KO
contributor: [{'name': 'Lakhani, Alishah', 'email': 'lakhanialishah@gmail.com', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}]
description: This dataset contains all the raw data files for the paper: Whisker deprivation triggers a distinct form of cortical homeostatic plasticity that is impaired in the Fmr1 KO
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 911493615448, 'numberOfFiles': 63, 'numberOfSubjects': 62, 'variableMeasured': ['ElectrodeGroup'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 001171 has 63 NWB files.
63 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/time_series (TimeSeries) no description
  file_create_date: ['2024-09-05T14:47:14.593000-04:00']
  Group /general/devices/array (Device) Cambridge NeuroTech H3
  experimenter: Lakhani, Alishah
  Group /general/extracellular_ephys/electrodes (DynamicTable) all electrodes
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) my description | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (64,) | dtype = int8
  Dataset /general/extracellular_ephys/electrodes/label (VectorData) my description | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) my description | shape = (64,) | dtype = object
  Group /general/extracellular_ephys/shank (ElectrodeGroup) electrode group
  Group /general/extracellular_ephys/shank/device (Device) Cambridge NeuroTech H3
  institution: Emory University
  Group /general/subject (Subject) 
  identifier: mouse221005
  Group /intervals/trials (TimeIntervals) whisker stimulations information
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (2375,) | dtype = int16
  Dataset /intervals/trials/start_time (VectorData) start time | shape = (2375,) | dtype = float32
  Dataset /intervals/trials/stop_time (VectorData) stop time | shape = (2375,) | dtype = float32
  Dataset /intervals/trials/velocity (VectorData) velocity (0-0.6 units = 0-800 deg/sec) | shape = (2375,) | dtype = float32
  Dataset /intervals/trials/whisker_stimulated (VectorData) whisker stimulated | shape = (2375,) | dtype = float32
  session_description: extracellular electrophysiology 
  session_start_time: 2022-10-05T01:01:01.000000-04:00
  timestamps_reference_time: 2022-10-05T01:01:01.000000-04:00
