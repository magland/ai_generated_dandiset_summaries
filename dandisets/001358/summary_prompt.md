
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001358/draft
name: Neural correlates of crowding in macaque area V4
contributor: [{'name': 'Kim, Taekjun', 'email': 'taekjunkim1223@gmail.com', 'roleName': ['dcite:ContactPerson', 'dcite:Author', 'dcite:Researcher', 'dcite:Investigation', 'dcite:FormalAnalysis'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Pasupathy, Anitha', 'email': 'pasupat@uw.edu', 'roleName': ['dcite:Author', 'dcite:ProjectLeader', 'dcite:FundingAcquisition', 'dcite:Supervision', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'National Eye Institute', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': 'R01 EY018839, R01 EY029601, P30 EY01730', 'includeInCitation': False}, {'name': 'National Institute of Health', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': 'P51 OD010425', 'includeInCitation': False}]
description: We studied the responses of 147 V4 neurons in two awake, fixating macaque monkeys (66 in Monkey 1, 81 in Monkey 2) to examine how their responses and selectivity to an isolated shape are modified by the presence of surrounding clutter stimuli.

More detailed information associated with this dataset is described in https://doi.org/10.1523/JNEUROSCI.2260-23.2024 
assetsSummary: {'species': [{'name': 'Macaca mulatta - Rhesus monkey', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9544'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 71586840, 'numberOfFiles': 131, 'numberOfSubjects': 2, 'variableMeasured': ['Units', 'ElectrodeGroup'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 001358 has 100 NWB files.
100 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2025-03-12T09:09:09.182850-07:00']
  Group /general/devices/Tungsten (Device) single electrode
  experimenter: ['Kim, Taekjun']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/label (VectorData) label of electrode | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (1,) | dtype = object
  Group /general/extracellular_ephys/probe0 (ElectrodeGroup) electrode group for probe 0
  Group /general/extracellular_ephys/probe0/device (Device) single electrode
  institution: University of Washington
  lab: Pasupathy Lab
  session_id: s060_J210421
  Group /general/subject (Subject) 
  identifier: s060_J210421
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/cond_ID (VectorData) crowding condition ID (0-21) | shape = (1130,) | dtype = int64
  Dataset /intervals/trials/cond_Name (VectorData) crowding condition name | shape = (1130,) | dtype = object
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (1130,) | dtype = int64
  Dataset /intervals/trials/pdOff (VectorData) stimulus offset time | shape = (1130,) | dtype = float64
  Dataset /intervals/trials/pdOn (VectorData) stimulus onset time | shape = (1130,) | dtype = float64
  Dataset /intervals/trials/rep_num (VectorData) rep_num | shape = (1130,) | dtype = int64
  Dataset /intervals/trials/ses_ID (VectorData) session ID | shape = (1130,) | dtype = object
  Dataset /intervals/trials/ses_Name (VectorData) session Name | shape = (1130,) | dtype = object
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (1130,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1130,) | dtype = float64
  Dataset /intervals/trials/target_rot (VectorData) target_rotation (deg) | shape = (1130,) | dtype = float64
  session_description: V4 crowding experiment
  session_start_time: 2021-04-21T10:30:00-07:00
  timestamps_reference_time: 2021-04-21T10:30:00-07:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/best_ch (VectorData) unit ID | shape = (1,) | dtype = int64
  Dataset /units/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /units/is_sua (VectorData) unit ID | shape = (1,) | dtype = bool
  Dataset /units/probe_num (VectorData) unit ID | shape = (1,) | dtype = int64
  Dataset /units/ses_ID (VectorData) session ID | shape = (1,) | dtype = object
  Dataset /units/ses_Name (VectorData) session Name | shape = (1,) | dtype = object
  Dataset /units/spike_times (VectorData) spike_times | shape = (42583,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (1,) | dtype = uint16
  Dataset /units/unit_ID (VectorData) unit ID | shape = (1,) | dtype = int64
