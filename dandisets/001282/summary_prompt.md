
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001282/draft
name: Neuropixels 1.0-NHP insertion datasets
contributor: [{'name': 'Windolf, Charlie', 'email': 'charliexwindolf@gmail.com', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}]
description: These are Neuropixels recordings made in non-human primates during deep probe insertions, collected by Eric Trautmann with guidance from Mike Shadlen and Mark Churchland. They are analyzed in Figure 4 and Supplementary Figure 5 of Windolf et al., "DREDge: robust motion correction for high-density extracellular recordings across species", to appear in Nature Methods. Detailed methodological information about methods used to create these recordings is available in that reference or the preprint (https://www.biorxiv.org/content/10.1101/2023.10.24.563768v1) under Datasets. See also Trautmann et al., "Large-scale brain-wide neural recording in nonhuman primates" (https://www.biorxiv.org/content/10.1101/2023.02.01.526664v1).
assetsSummary: {'species': [{'name': 'Macaca mulatta - Rhesus monkey', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9544'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 59004052857, 'numberOfFiles': 2, 'numberOfSubjects': 1, 'variableMeasured': ['ElectricalSeries', 'ElectrodeGroup'], 'measurementTechnique': [{'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 001282 has 2 NWB files.
2 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeriesAP (ElectricalSeries) Acquisition traces for the ElectricalSeriesAP.
  Dataset /acquisition/ElectricalSeriesAP/electrodes (DynamicTableRegion) electrode_table_region | shape = (384,) | dtype = int64
  Group /acquisition/ElectricalSeriesLF (ElectricalSeries) Acquisition traces for the ElectricalSeriesLF.
  Dataset /acquisition/ElectricalSeriesLF/electrodes (DynamicTableRegion) electrode_table_region | shape = (384,) | dtype = int64
  file_create_date: ['2024-12-30T20:10:55.093150-05:00']
  Group /general/devices/NeuropixelImec0 (Device) {"probe_type": "1030", "probe_type_description": "NP1.0 NHP", "flex_part_number": "NPNH_AFLEX_00", "connected_base_station_part_number": "NP2_HS_30"}
  Group /general/extracellular_ephys/Imec0 (ElectrodeGroup) A group representing probe/shank 'Imec0'.
  Group /general/extracellular_ephys/Imec0/device (Device) {"probe_type": "1030", "probe_type_description": "NP1.0 NHP", "flex_part_number": "NPNH_AFLEX_00", "connected_base_station_part_number": "NP2_HS_30"}
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/channel_name (VectorData) unique channel reference | shape = (768,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/contact_ids (VectorData) The id of the contact on the electrode | shape = (768,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/contact_shapes (VectorData) The shape of the electrode | shape = (768,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (768,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (768,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (768,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/inter_sample_shift (VectorData) no description | shape = (768,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (768,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/rel_x (VectorData) rel_x | shape = (768,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_y (VectorData) rel_y | shape = (768,) | dtype = float64
  source_script: Created using NeuroConv v0.6.6
  Group /general/subject (Subject) 
  identifier: 33392494-a974-4818-ad3d-18417b0af8ac
  session_description: 
  session_start_time: 2022-01-21T13:37:54-05:00
  timestamps_reference_time: 2022-01-21T13:37:54-05:00
