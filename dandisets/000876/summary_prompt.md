
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000876/draft
name: MVMNDA
contributor: [{'name': 'Christian, Horea', 'email': 'chr@chymera.eu', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}]
description: Neuropixels SpikeGLX data for olfaction.
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}, {'name': 'Brain Imaging Data Structure (BIDS)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_016124'}], 'numberOfBytes': 18609018147, 'numberOfFiles': 26, 'numberOfSubjects': 1, 'variableMeasured': ['ElectricalSeries', 'ElectrodeGroup'], 'measurementTechnique': [{'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000876 has 1 NWB files.
1 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeriesAP (ElectricalSeries) Acquisition traces for the ElectricalSeriesAP.
  Dataset /acquisition/ElectricalSeriesAP/electrodes (DynamicTableRegion) electrode_table_region | shape = (384,) | dtype = int64
  Group /acquisition/ElectricalSeriesNIDQ (ElectricalSeries) Raw acquisition traces from the NIDQ (.nidq.bin) channels.
  Dataset /acquisition/ElectricalSeriesNIDQ/electrodes (DynamicTableRegion) electrode_table_region | shape = (9,) | dtype = int64
  file_create_date: ['2024-01-25T13:50:11.291743-05:00']
  Group /general/devices/Neuropixel-Imec (Device) {"probe_type": "0", "probe_type_description": "NP1.0", "flex_part_number": "NP2_FLEX_0", "connected_base_station_part_number": "NP2_QBSC_00"}
  Group /general/extracellular_ephys/NIDQChannelGroup (ElectrodeGroup) A group representing the NIDQ channels.
  Group /general/extracellular_ephys/NIDQChannelGroup/device (Device) {"probe_type": "0", "probe_type_description": "NP1.0", "flex_part_number": "NP2_FLEX_0", "connected_base_station_part_number": "NP2_QBSC_00"}
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/channel_name (VectorData) no description | shape = (393,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/contact_shapes (VectorData) The shape of the electrode | shape = (393,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/gain_to_uV (VectorData) no description | shape = (393,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (393,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (393,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (393,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/inter_sample_shift (VectorData) no description | shape = (393,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (393,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/offset_to_uV (VectorData) no description | shape = (393,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_x (VectorData) rel_x | shape = (393,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_y (VectorData) rel_y | shape = (393,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/shank_electrode_number (VectorData) 0-indexed channel within a shank. | shape = (393,) | dtype = float64
  Group /general/extracellular_ephys/s0 (ElectrodeGroup) a group representing shank s0
  Group /general/extracellular_ephys/s0/device (Device) {"probe_type": "0", "probe_type_description": "NP1.0", "flex_part_number": "NP2_FLEX_0", "connected_base_station_part_number": "NP2_QBSC_00"}
  Group /general/subject (Subject) 
  identifier: 44d63174-bf02-4b21-9263-9e585a845377
  session_description: Auto-generated by neuroconv
  session_start_time: 2023-11-20T11:40:21-05:00
  timestamps_reference_time: 2023-11-20T11:40:21-05:00
