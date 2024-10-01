
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000034/0.211030.0713
name: SpikeInterface, a unified framework for spike sorting
contributor: [{'name': 'Buccino, Alessio', 'email': 'alessiop.buccino@gmail.com', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0003-3661-527X', 'affiliation': [], 'awardNumber': 'ETH Zurich Postdoctoral Fellowship 19–2 FEL-17', 'includeInCitation': True}, {'name': 'Hurwitz, Cole', 'roleName': [], 'schemaKey': 'Person', 'identifier': '0000-0002-2023-1653', 'affiliation': [], 'awardNumber': 'Thouron Award and by the Institute for Adaptive and Neural Computation, University of Edinburgh', 'includeInCitation': True}, {'name': 'Garcia, Samuel', 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Magland, Jeremy', 'schemaKey': 'Person', 'identifier': '0000-0002-5286-4375', 'includeInCitation': True}, {'name': 'Siegle, Joshua', 'schemaKey': 'Person', 'identifier': '0000-0002-7736-4844', 'includeInCitation': True}, {'name': 'Hurwitz, Roger', 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Hennig, Matthias H.', 'roleName': [], 'schemaKey': 'Person', 'identifier': '0000-0001-7270-5817', 'affiliation': [], 'awardNumber': 'Wellcome Trust grant 214431/Z/18/Z', 'includeInCitation': True}]
description: SpikeInterface is a Python framework designed to make the analysis of extracellular electrophysiology data more accessible and standardized. The SpikeInterface documentation can be found at https://spikeinterface.readthedocs.io/en/latest/.

This dataset contains all recordings analysed in the paper: "SpikeInterface, a unified framework for spike sorting." Alessio P. Buccino, Cole L. Hurwitz, Samuel Garcia, Jeremy Magland, Joshua H. Siegle, Roger Hurwitz, Matthias H. Hennig, eLife - doi: https://doi.org/10.7554/eLife.61834; 
assetsSummary: {'species': [{'name': 'House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 74351014076, 'numberOfFiles': 6, 'numberOfSubjects': 4, 'variableMeasured': ['ElectrodeGroup', 'Units', 'ElectricalSeries'], 'measurementTechnique': [{'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000034 has 6 NWB files.
1 of these NWB files are of type 1.
3 of these NWB files are of type 2.
2 of these NWB files are of type 3.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeries (ElectricalSeries) acquisition_description
  Dataset /acquisition/ElectricalSeries/electrodes (DynamicTableRegion) electrode_table_region | shape = (384,) | dtype = int64
  file_create_date: ['2020-07-27T09:46:20.620378+01:00']
  Group /general/devices/Device (Device) 
  Group /general/extracellular_ephys/0 (ElectrodeGroup) electrode_group_description
  Group /general/extracellular_ephys/0/device (Device) 
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (384,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (384,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (384,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (384,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (384,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (384,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/rel_x (VectorData) the x coordinate within the electrode group | shape = (384,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_y (VectorData) the y coordinate within the electrode group | shape = (384,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (384,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (384,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (384,) | dtype = float64
  Group /general/subject (Subject) 
  identifier: 8f43bf0f-edb0-45cc-93eb-9acad8f2a84c
  session_description: no description
  session_start_time: 2020-07-27T09:46:20.619184+01:00
  timestamps_reference_time: 2020-07-27T09:46:20.619184+01:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/id (ElementIdentifiers)  | shape = (250,) | dtype = int64
  Dataset /units/soma_location (VectorData) no description | shape = (250, 3) | dtype = float64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (1026644,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex)  | shape = (250,) | dtype = int64


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeries (ElectricalSeries) acquisition_description
  Dataset /acquisition/ElectricalSeries/electrodes (DynamicTableRegion) electrode_table_region | shape = (1024,) | dtype = int64
  file_create_date: ['2020-08-07T09:42:57.478934+01:00']
  Group /general/devices/Device (Device) 
  Group /general/extracellular_ephys/0 (ElectrodeGroup) electrode_group_description
  Group /general/extracellular_ephys/0/device (Device) 
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (1024,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (1024,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (1024,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (1024,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (1024,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (1024,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/rel_x (VectorData) the x coordinate within the electrode group | shape = (1024,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_y (VectorData) the y coordinate within the electrode group | shape = (1024,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (1024,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (1024,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (1024,) | dtype = float64
  Group /general/subject (Subject) 
  identifier: 57e10c71-c0d2-488a-a34d-13d6dcaf7af1
  session_description: no description
  session_start_time: 2020-08-07T09:42:57.434275+01:00
  timestamps_reference_time: 2020-08-07T09:42:57.434275+01:00


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2020-08-24T15:55:42.004673+02:00']
  Group /general/subject (Subject) 
  identifier: 2bddd311-a20a-4f69-aa12-14bcf21bca46
  session_description: No description
  session_start_time: 2020-08-24T15:55:42.004284+02:00
  timestamps_reference_time: 2020-08-24T15:55:42.004284+02:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/id (ElementIdentifiers)  | shape = (258,) | dtype = int32
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (1190752,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (258,) | dtype = uint32
