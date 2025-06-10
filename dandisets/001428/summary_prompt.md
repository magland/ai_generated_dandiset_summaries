
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001428/draft
name: Hippocampal Neural Dynamics and Postoperative Delirium-Like Behavior in Aged Mice
contributor: [{'name': 'National Institutes of Health (NIH)', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': '4 R01 AG 070141-02'}, {'name': 'Guo, Shiqi', 'email': 'SHIQIGUO29@GMAIL.COM', 'schemaKey': 'Person', 'identifier': '0000-0001-6323-9287', 'includeInCitation': True}, {'name': 'Yang, Liuyue', 'schemaKey': 'Person'}, {'name': 'Ding, Weihua', 'schemaKey': 'Person'}, {'name': 'National Institutes if Health (NIH)', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': 'R01 AG082975'}, {'name': 'Shen, Shiqian', 'email': 'sshen2@mgh.harvard.edu', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person'}, {'name': 'National Institutes if Health (NIH)', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': 'R35 GM128692'}]
description: Using a model of POD in older mice, we investigated the effects of anesthesia/surgery on electrophysiological signals and assessed neural dynamics through in vivo calcium imaging. Additionally, we treated older mice with indole 3-propionic acid (IPA) and evaluated its impact on POD-like behavior, as well as on neural activity using electrophysiology and calcium imaging.
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 26074690766, 'numberOfFiles': 6, 'numberOfSubjects': 5, 'variableMeasured': ['ElectrodeGroup', 'ElectricalSeries'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 001428 has 6 NWB files.
6 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeries (ElectricalSeries) Acquisition traces for the ElectricalSeries.
  Dataset /acquisition/ElectricalSeries/electrodes (DynamicTableRegion) electrode_table_region | shape = (384,) | dtype = int32
  file_create_date: ['2025-04-29T15:45:53.420582-04:00']
  Group /general/devices/DeviceEcephys (Device) no description
  experiment_description: all shanks 385-480
  experimenter: ['Guo, Shiqi']
  Group /general/extracellular_ephys/0 (ElectrodeGroup) no description
  Group /general/extracellular_ephys/0/device (Device) no description
  Group /general/extracellular_ephys/1 (ElectrodeGroup) no description
  Group /general/extracellular_ephys/1/device (Device) no description
  Group /general/extracellular_ephys/2 (ElectrodeGroup) no description
  Group /general/extracellular_ephys/2/device (Device) no description
  Group /general/extracellular_ephys/3 (ElectrodeGroup) no description
  Group /general/extracellular_ephys/3/device (Device) no description
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/channel_name (VectorData) unique channel reference | shape = (384,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/gain_to_physical_unit (VectorData) No description. | shape = (384,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (384,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (384,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (384,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/inter_sample_shift (VectorData) Time-delay of each channel sampling in proportion to the per-frame sampling period. | shape = (384,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (384,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/offset_to_physical_unit (VectorData) No description. | shape = (384,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/physical_unit (VectorData) No description. | shape = (384,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/rel_x (VectorData) rel_x | shape = (384,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_y (VectorData) rel_y | shape = (384,) | dtype = float64
  institution: MGH
  lab: Shen-Lab
  session_id: before
  source_script: Created using NWB GUIDE v1.0.6-beta
  Group /general/subject (Subject) 
  identifier: af8fb9ab-567a-4f05-89a6-706bc8e018f9
  session_description: 
  session_start_time: 2024-07-30T21:28:02-04:00
  timestamps_reference_time: 2024-07-30T21:28:02-04:00
