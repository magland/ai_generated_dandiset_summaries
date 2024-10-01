
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001069/0.240621.2139
name: SN recording during Temporal lobe seizures
contributor: [{'name': 'Devergnas, Annaelle', 'email': 'adeverg@emory.edu', 'roleName': ['dcite:DataCollector', 'dcite:Author', 'dcite:ProjectLeader', 'dcite:Conceptualization', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [{'name': 'Emory Primate Center', 'schemaKey': 'Affiliation'}], 'awardNumber': '', 'includeInCitation': True}]
description: This data set contains the electrophysiological recordings from 2 NHPs during temporal lobe seizures induced by penicillin injection into the hippocampus. 
assetsSummary: {'species': [{'name': 'Macaca mulatta - Rhesus monkey', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9544'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 1360390639, 'numberOfFiles': 10, 'numberOfSubjects': 2, 'variableMeasured': ['ElectricalSeries', 'ElectrodeGroup'], 'measurementTechnique': [{'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 001069 has 10 NWB files.
10 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeries (ElectricalSeries) Acquisition traces for the ElectricalSeries.
  Dataset /acquisition/ElectricalSeries/electrodes (DynamicTableRegion) electrode_table_region | shape = (35,) | dtype = int32
  file_create_date: ['2024-06-21T16:56:02.330917-04:00']
  Group /general/devices/DeviceEcephys (Device) no description
  Group /general/extracellular_ephys/ElectrodeGroup (ElectrodeGroup) no description
  Group /general/extracellular_ephys/ElectrodeGroup/device (Device) no description
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/channel_name (VectorData) The name of this channel. | shape = (35,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (35,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (35,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (35,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (35,) | dtype = object
  session_id: 2021_05_19_001
  source_script: Created using NWB GUIDE v1.0.0
  Group /general/subject (Subject) 
  identifier: 7a813ffa-7bad-418e-a7fe-3989e76c9333
  session_description: 
  session_start_time: 2021-05-19T13:07:55.340000-04:00
  timestamps_reference_time: 2021-05-19T13:07:55.340000-04:00
