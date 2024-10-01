
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001132/draft
name: Multimodal evaluation of network activity and optogenetic  interventions in human hippocampal slices
contributor: [{'name': 'National Institutes of Health (NIH)', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': '5 RM1 HG 011543-03', 'includeInCitation': False}, {'name': 'Andrews, John P.', 'email': 'John.Andrews@ucsf.edu', 'roleName': ['dcite:Researcher', 'dcite:Author', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0002-8025-1525', 'includeInCitation': True}, {'name': 'Geng, Jinghui', 'email': 'jgeng2@ucsc.edu', 'roleName': ['dcite:Author', 'dcite:Researcher'], 'schemaKey': 'Person', 'identifier': '0000-0002-3431-9568', 'includeInCitation': True}, {'name': 'Voitiuk, Kateryna', 'email': 'kvoitiuk@ucsc.edu', 'roleName': ['dcite:Author', 'dcite:Researcher'], 'schemaKey': 'Person', 'identifier': '0000-0002-6392-5188', 'awardNumber': 'T32HG012344', 'includeInCitation': True}, {'name': 'Nowakowski, Tomasz J.', 'email': 'tomasz.nowakowski@ucsf.edu', 'roleName': ['dcite:Author', 'dcite:ContactPerson', 'dcite:FundingAcquisition', 'dcite:Investigation', 'dcite:Supervision'], 'schemaKey': 'Person', 'identifier': '0000-0003-2345-4964', 'awardNumber': 'R01NS123263', 'includeInCitation': False}, {'name': 'Teodorescu, Mircea', 'email': 'mteodore@ucsc.edu', 'roleName': ['dcite:Author', 'dcite:ContactPerson', 'dcite:Investigation', 'dcite:FundingAcquisition', 'dcite:Supervision'], 'schemaKey': 'Person', 'includeInCitation': False}, {'name': 'Chang, Edward F.', 'email': 'edward.chang@ucsf.edu', 'roleName': ['dcite:Author', 'dcite:ContactPerson', 'dcite:Investigation', 'dcite:FundingAcquisition', 'dcite:Supervision'], 'schemaKey': 'Person', 'includeInCitation': False}, {'name': 'National Institute of Neurological Disorders and Stroke, National Institutes of Health', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': '5R25NS070680-13', 'includeInCitation': False}, {'name': 'NIH Brain Initiative', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': 'UF1MH130700', 'includeInCitation': False}, {'name': 'NSF', 'schemaKey': 'Organization', 'awardNumber': '2034037', 'includeInCitation': False}]
description: Data accompanying manuscript by Andrews, Geng, Voitiuk, et al. 2024.
assetsSummary: {'species': [{'name': 'Homo sapiens - Human', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9606'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 192373252150, 'numberOfFiles': 69, 'numberOfSubjects': 69, 'variableMeasured': ['ElectricalSeries', 'ElectrodeGroup'], 'measurementTechnique': [{'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 001132 has 69 NWB files.
69 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeries (ElectricalSeries) Acquisition traces for the ElectricalSeries.
  Dataset /acquisition/ElectricalSeries/electrodes (DynamicTableRegion) electrode_table_region | shape = (887,) | dtype = int64
  file_create_date: ['2024-09-28T23:54:27.137409+00:00']
  Group /general/devices/DeviceEcephys (Device) Recorded using Maxwell version '20160704'.
  experiment_description: Multimodal evaluation of network activity and optogenetic interventions in human hippocampal slices
  Group /general/extracellular_ephys/0 (ElectrodeGroup) no description
  Group /general/extracellular_ephys/0/device (Device) Recorded using Maxwell version '20160704'.
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/channel_name (VectorData) unique channel reference | shape = (887,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/electrode (VectorData) no description | shape = (887,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (887,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (887,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (887,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (887,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/rel_x (VectorData) rel_x | shape = (887,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_y (VectorData) rel_y | shape = (887,) | dtype = float64
  institution: UCSF, UCSC
  lab: NOW Lab, UCSF
  source_script: Created using NeuroConv v0.6.4
  Group /general/subject (Subject) 
  identifier: 6d3d933a-5203-4b2a-a23e-6095bdfeea43
  session_description: 
  session_start_time: 2024-09-28T16:54:27.120889-07:00
  timestamps_reference_time: 2024-09-28T16:54:27.120889-07:00
