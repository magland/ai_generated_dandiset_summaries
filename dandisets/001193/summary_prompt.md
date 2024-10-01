
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001193/0.240921.1006
name: Data for: Distinct spatiotemporal patterns of syntactic and semantic processing in human inferior frontal gyrus
contributor: [{'name': 'Shao, TongZe', 'email': 'shaoxydd8888@gmail.com', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}]
description: This dataset comprises high-gamma brain activity recordings (70-150 Hz) obtained through electrocorticography (ECoG) from human subjects. It focuses on neural responses during syntactic and semantic processing tasks, specifically within the inferior frontal gyrus. The data is formatted in the Neurodata Without Borders (NWB) standard, facilitating ease of use and integration within the neuroscience community. This dataset supports the findings published in the article "Distinct spatiotemporal patterns of syntactic and semantic processing in human inferior frontal gyrus," accessible via DOI: 10.1038/s41562-022-01334-6.
assetsSummary: {'species': [{'name': 'Homo sapiens - Human', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9606'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 1365465792, 'numberOfFiles': 40, 'numberOfSubjects': 10, 'variableMeasured': ['ElectrodeGroup', 'ElectricalSeries'], 'measurementTechnique': [{'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 001193 has 40 NWB files.
40 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ECoG (ElectricalSeries) High gamma data
  Dataset /acquisition/ECoG/electrodes (DynamicTableRegion) All ECoG electrodes | shape = (256,) | dtype = int64
  file_create_date: ['2024-09-21T17:34:42.043703+08:00']
  Group /general/devices/Device_1 (Device) manufactured by PMT
  Group /general/devices/Device_2 (Device) manufactured by PMT
  experiment_description: _
  experimenter: ['Yanming, Zhu']
  Group /general/extracellular_ephys/Grid_1 (ElectrodeGroup) ECoG Grid 1
  Group /general/extracellular_ephys/Grid_1/device (Device) manufactured by PMT
  Group /general/extracellular_ephys/Grid_2 (ElectrodeGroup) ECoG Grid 2
  Group /general/extracellular_ephys/Grid_2/device (Device) manufactured by PMT
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering, including the filter name and frequency cutoffs | shape = (256,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (256,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (256,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (256,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (256,) | dtype = object
  institution: Fudan University
  keywords: []
  lab: The Brain Function Laboratory of Neurosurgical Institute of Fudan University
  related_publications: ['doi:10.1038/s41562-022-01334-6']
  Group /general/subject (Subject) 
  identifier: TC12_block4
  session_description: High gamma data session
  session_start_time: 2019-05-28T00:00:00+08:00
  timestamps_reference_time: 2019-05-28T00:00:00+08:00
