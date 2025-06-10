
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001470/draft
name: Neuropixels recordings from hippocampus of head-fixed mice during odor presentation (Raw - BIDS)
contributor: [{'name': 'Baker, Cody', 'email': 'cody.c.baker.phd@gmail.com', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}]
description: BEP32-compliant version of 001335 (https://dandiarchive.org/dandiset/001335/draft)
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Brain Imaging Data Structure (BIDS)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_016124'}, {'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 1723168, 'numberOfFiles': 8, 'numberOfSubjects': 1, 'variableMeasured': ['ElectricalSeries', 'ElectrodeGroup'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 001470 has 1 NWB files.
1 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeriesAPImec0 (ElectricalSeries) Acquisition traces for the ElectricalSeriesAPImec0.
  Dataset /acquisition/ElectricalSeriesAPImec0/electrodes (DynamicTableRegion) electrode_table_region | shape = (384,) | dtype = int64
  Group /acquisition/ElectricalSeriesAPImec1 (ElectricalSeries) Acquisition traces for the ElectricalSeriesAPImec1.
  Dataset /acquisition/ElectricalSeriesAPImec1/electrodes (DynamicTableRegion) electrode_table_region | shape = (384,) | dtype = int64
  Group /acquisition/EventsNIDQDigitalChannelXD0 (LabeledEvents) On and Off Events from channel XD0
  Group /acquisition/EventsNIDQDigitalChannelXD2 (LabeledEvents) On and Off Events from channel XD2
  Group /acquisition/EventsNIDQDigitalChannelXD3 (LabeledEvents) On and Off Events from channel XD3
  Group /acquisition/TimeSeriesNIDQ (TimeSeries) Analog data from the NIDQ board. Channels are ['XA0' 'XA1' 'XA2' 'XA3' 'XA4' 'XA5' 'XA6' 'XA7'] in that order.
  file_create_date: ['2025-06-05T14:59:37.373812-04:00']
  Group /general/devices/NIDQBoard (Device) A NIDQ board used in conjunction with SpikeGLX.
  Group /general/devices/NeuropixelsImec0 (Device) {"probe_type": "2013", "probe_type_description": "Neuropixels 2.0 - Four Shank", "flex_part_number": "NPM_FLEX_01", "connected_base_station_part_number": "NP2_QBSC_00"}
  Group /general/devices/NeuropixelsImec1 (Device) {"probe_type": "2013", "probe_type_description": "Neuropixels 2.0 - Four Shank", "flex_part_number": "NPM_FLEX_01", "connected_base_station_part_number": "NP2_QBSC_00"}
  Group /general/extracellular_ephys/NeuropixelsImec0Shank0 (ElectrodeGroup) A group representing probe/shank 'NeuropixelsImec0Shank0'.
  Group /general/extracellular_ephys/NeuropixelsImec0Shank0/device (Device) {"probe_type": "2013", "probe_type_description": "Neuropixels 2.0 - Four Shank", "flex_part_number": "NPM_FLEX_01", "connected_base_station_part_number": "NP2_QBSC_00"}
  Group /general/extracellular_ephys/NeuropixelsImec0Shank1 (ElectrodeGroup) A group representing probe/shank 'NeuropixelsImec0Shank1'.
  Group /general/extracellular_ephys/NeuropixelsImec0Shank1/device (Device) {"probe_type": "2013", "probe_type_description": "Neuropixels 2.0 - Four Shank", "flex_part_number": "NPM_FLEX_01", "connected_base_station_part_number": "NP2_QBSC_00"}
  Group /general/extracellular_ephys/NeuropixelsImec0Shank2 (ElectrodeGroup) A group representing probe/shank 'NeuropixelsImec0Shank2'.
  Group /general/extracellular_ephys/NeuropixelsImec0Shank2/device (Device) {"probe_type": "2013", "probe_type_description": "Neuropixels 2.0 - Four Shank", "flex_part_number": "NPM_FLEX_01", "connected_base_station_part_number": "NP2_QBSC_00"}
  Group /general/extracellular_ephys/NeuropixelsImec0Shank3 (ElectrodeGroup) A group representing probe/shank 'NeuropixelsImec0Shank3'.
  Group /general/extracellular_ephys/NeuropixelsImec0Shank3/device (Device) {"probe_type": "2013", "probe_type_description": "Neuropixels 2.0 - Four Shank", "flex_part_number": "NPM_FLEX_01", "connected_base_station_part_number": "NP2_QBSC_00"}
  Group /general/extracellular_ephys/NeuropixelsImec1Shank0 (ElectrodeGroup) A group representing probe/shank 'NeuropixelsImec1Shank0'.
  Group /general/extracellular_ephys/NeuropixelsImec1Shank0/device (Device) {"probe_type": "2013", "probe_type_description": "Neuropixels 2.0 - Four Shank", "flex_part_number": "NPM_FLEX_01", "connected_base_station_part_number": "NP2_QBSC_00"}
  Group /general/extracellular_ephys/NeuropixelsImec1Shank1 (ElectrodeGroup) A group representing probe/shank 'NeuropixelsImec1Shank1'.
  Group /general/extracellular_ephys/NeuropixelsImec1Shank1/device (Device) {"probe_type": "2013", "probe_type_description": "Neuropixels 2.0 - Four Shank", "flex_part_number": "NPM_FLEX_01", "connected_base_station_part_number": "NP2_QBSC_00"}
  Group /general/extracellular_ephys/NeuropixelsImec1Shank2 (ElectrodeGroup) A group representing probe/shank 'NeuropixelsImec1Shank2'.
  Group /general/extracellular_ephys/NeuropixelsImec1Shank2/device (Device) {"probe_type": "2013", "probe_type_description": "Neuropixels 2.0 - Four Shank", "flex_part_number": "NPM_FLEX_01", "connected_base_station_part_number": "NP2_QBSC_00"}
  Group /general/extracellular_ephys/NeuropixelsImec1Shank3 (ElectrodeGroup) A group representing probe/shank 'NeuropixelsImec1Shank3'.
  Group /general/extracellular_ephys/NeuropixelsImec1Shank3/device (Device) {"probe_type": "2013", "probe_type_description": "Neuropixels 2.0 - Four Shank", "flex_part_number": "NPM_FLEX_01", "connected_base_station_part_number": "NP2_QBSC_00"}
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/channel_name (VectorData) unique channel reference | shape = (768,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/contact_ids (VectorData) The id of the contact on the electrode | shape = (768,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/contact_shapes (VectorData) The shape of the electrode | shape = (768,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/gain_to_physical_unit (VectorData) no description | shape = (768,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (768,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (768,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (768,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/inter_sample_shift (VectorData) Array of relative phase shifts for each channel, with values ranging from 0 to 1, representing the fractional delay within the sampling period due to sequential ADC. | shape = (768,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (768,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/offset_to_physical_unit (VectorData) no description | shape = (768,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/physical_unit (VectorData) no description | shape = (768,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/rel_x (VectorData) rel_x | shape = (768,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_y (VectorData) rel_y | shape = (768,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/shank_ids (VectorData) The shank id of the electrode | shape = (768,) | dtype = object
  session_id: M54120240831
  source_script: Created using NeuroConv v0.7.4
  Group /general/subject (Subject) 
  identifier: 6a64a4be-36b6-4f75-a534-3d32a42f81f3
  session_description: 
  session_start_time: 2024-08-31T18:02:46-04:00
  timestamps_reference_time: 2024-08-31T18:02:46-04:00
