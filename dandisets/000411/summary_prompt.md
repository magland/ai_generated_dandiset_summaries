
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000411/draft
name: test
contributor: [{'name': 'Li, Chenyang', 'email': 'cyli@ion.ac.cn', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}]
description: It is a test to use DANDI archive, like hello world. I will not upload any neural data in this set.
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 232080, 'numberOfFiles': 1, 'numberOfSubjects': 1, 'variableMeasured': ['ElectricalSeries', 'ElectrodeGroup'], 'measurementTechnique': [{'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000411 has 1 NWB files.
1 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeries (ElectricalSeries) no description
  Dataset /acquisition/ElectricalSeries/electrodes (DynamicTableRegion) all electrodes | shape = (50,) | dtype = int64
  file_create_date: ['2023-02-14T16:52:51.460144+08:00']
  Group /general/devices/array (Device) the best array
  experiment_description: I went on an adventure with thirteen dwarves to reclaim vast treasures.
  experimenter: ['Dr. Bilbo Baggins']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (50,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (50,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (50,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/label (VectorData) label of electrode | shape = (50,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (50,) | dtype = object
  Group /general/extracellular_ephys/shank0 (ElectrodeGroup) electrode group for shank 0
  Group /general/extracellular_ephys/shank0/device (Device) the best array
  Group /general/extracellular_ephys/shank1 (ElectrodeGroup) electrode group for shank 1
  Group /general/extracellular_ephys/shank1/device (Device) the best array
  Group /general/extracellular_ephys/shank2 (ElectrodeGroup) electrode group for shank 2
  Group /general/extracellular_ephys/shank2/device (Device) the best array
  Group /general/extracellular_ephys/shank3 (ElectrodeGroup) electrode group for shank 3
  Group /general/extracellular_ephys/shank3/device (Device) the best array
  Group /general/extracellular_ephys/shank4 (ElectrodeGroup) electrode group for shank 4
  Group /general/extracellular_ephys/shank4/device (Device) the best array
  institution: University of Middle Earth at the Shire
  lab: Bag End Laboratory
  session_id: LONELYMTN
  Group /general/subject (Subject) 
  identifier: EXAMPLE_ID
  session_description: my first synthetic recording
  session_start_time: 2023-02-14T16:52:51.459986+08:00
  timestamps_reference_time: 2023-02-14T16:52:51.459986+08:00
