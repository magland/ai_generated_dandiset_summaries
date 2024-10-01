
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000399/draft
name: All-optical physiology resolves a synaptic basis for behavioral time scale plasticity
contributor: [{'name': 'Fan, Linlin', 'email': 'dlinfan@gmail.com', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}]
description: Data included in Fan (2022) Cell
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 86582248, 'numberOfFiles': 105, 'numberOfSubjects': 19, 'variableMeasured': ['ElectricalSeries', 'ElectrodeGroup'], 'measurementTechnique': [{'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000399 has 100 NWB files.
100 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeries (ElectricalSeries) no description
  Dataset /acquisition/ElectricalSeries/electrodes (DynamicTableRegion) all electrodes | shape = (1,) | dtype = int64
  file_create_date: ['2023-06-13T23:16:00.496000-07:00']
  Group /general/devices/Probe0 (Device) Custom-designed microscope for optical ephys
  experiment_description: mouse in vr
  experimenter: ['Fan, Linlin']
  Group /general/extracellular_ephys/Probe0 (ElectrodeGroup) electrode group for Probe0
  Group /general/extracellular_ephys/Probe0/device (Device) Custom-designed microscope for optical ephys
  Group /general/extracellular_ephys/electrodes (DynamicTable) all probes
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) my description | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) my description | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) my description | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) my description | shape = (1,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) my description | shape = (1,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) my description | shape = (1,) | dtype = float64
  institution: Stanford University
  keywords: ['optical electrophysiology' 'hippocampus']
  lab: Deisseroth
  related_publications: ['doi:10.1016/j.cell.2022.12.035']
  Group /general/subject (Subject) 
  identifier: 1-24
  session_description: mouse in vr
  session_start_time: 2021-09-02T00:00:00.000000-07:00
  timestamps_reference_time: 2021-09-02T00:00:00.000000-07:00
