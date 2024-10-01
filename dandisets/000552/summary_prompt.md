
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000552/0.230630.2304
name: Preconfigured dynamics in the hippocampus are guided by embryonic birthdate and rate of neurogenesis
contributor: [{'name': 'Huszár, Roman', 'email': 'rh2618@nyu.edu', 'roleName': ['dcite:Author', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0002-8426-8308', 'affiliation': [{'name': 'New York University Langone Medical Center', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/005dvqh91'}], 'includeInCitation': True}, {'name': 'Zhang, Yunchang', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [{'name': 'New York University Langone Medical Center', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/005dvqh91'}], 'includeInCitation': True}, {'name': 'Blockus, Heike', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0001-5274-2805', 'affiliation': [], 'includeInCitation': True}, {'name': 'Buzsáki, György', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-3100-4800', 'affiliation': [{'name': 'New York University Langone Medical Center', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/005dvqh91'}], 'includeInCitation': True}, {'url': 'http://www.nih.gov/', 'name': 'National Institutes of Health', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01cwqze88', 'awardNumber': 'U19NS104590-01, MH122391', 'contactPoint': [], 'includeInCitation': False}, {'name': 'Flynn, Garrett', 'email': 'garrett.flynn@catalystneuro.com', 'roleName': ['dcite:DataCurator'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': False}]
description: The incorporation of novel information into the hippocampal network is likely be constrained by its innate architecture and internally generated activity patterns. However, the origin, organization, and consequences of such patterns remain poorly understood. Here, we show that hippocampal network dynamics are affected by sequential neurogenesis. We birthdated CA1 pyramidal neurons with in-utero electroporation over 4 embryonic days encompassing the peak of hippocampal neurogenesis, and compared their functional features in freely moving, adult mice. Neurons of the same birthdate displayed distinct connectivity, coactivity across brain states, and assembly dynamics. Same birthdate hippocampal neurons were topographically organized, in that anatomically clustered (<500µm) neurons exhibited overlapping spatial representations. Overall, the wiring and functional features of CA1 pyramidal neurons reflected a combination of birthdate and the rate of neurogenesis. These observations demonstrate that sequential neurogenesis in embryonic development shapes the preconfigured forms of adult network dynamics.
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}, {'name': 'behavioral approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 1545387836482, 'numberOfFiles': 117, 'numberOfSubjects': 17, 'variableMeasured': ['ElectricalSeries', 'ProcessingModule', 'ElectrodeGroup', 'LFP', 'SpatialSeries', 'Position', 'Units'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'signal filtering technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000552 has 93 NWB files.
20 of these NWB files are of type 1.
1 of these NWB files are of type 2.
34 of these NWB files are of type 3.
5 of these NWB files are of type 4.
33 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2023-06-30T22:27:47.109359+00:00']
  Group /general/devices/Device (Device) Ecephys probe. Automatically generated.
  experiment_description: Preconfigured dynamics in the hippocampus are guided by embryonic birthdate and rate of neurogenesis
  experimenter: ['Huszár, Roman' 'Zhang, Yunchang' 'Blockus, Heike' 'Buzsáki, György']
  Group /general/extracellular_ephys/Group 1 (ElectrodeGroup) no description
  Group /general/extracellular_ephys/Group 1/device (Device) Ecephys probe. Automatically generated.
  Group /general/extracellular_ephys/Group 2 (ElectrodeGroup) no description
  Group /general/extracellular_ephys/Group 2/device (Device) Ecephys probe. Automatically generated.
  Group /general/extracellular_ephys/Group 3 (ElectrodeGroup) no description
  Group /general/extracellular_ephys/Group 3/device (Device) Ecephys probe. Automatically generated.
  Group /general/extracellular_ephys/Group 4 (ElectrodeGroup) no description
  Group /general/extracellular_ephys/Group 4/device (Device) Ecephys probe. Automatically generated.
  Group /general/extracellular_ephys/Group 5 (ElectrodeGroup) no description
  Group /general/extracellular_ephys/Group 5/device (Device) Ecephys probe. Automatically generated.
  Group /general/extracellular_ephys/Group 6 (ElectrodeGroup) no description
  Group /general/extracellular_ephys/Group 6/device (Device) Ecephys probe. Automatically generated.
  Group /general/extracellular_ephys/Group 7 (ElectrodeGroup) no description
  Group /general/extracellular_ephys/Group 7/device (Device) Ecephys probe. Automatically generated.
  Group /general/extracellular_ephys/Group 8 (ElectrodeGroup) no description
  Group /general/extracellular_ephys/Group 8/device (Device) Ecephys probe. Automatically generated.
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/channel_name (VectorData) unique channel reference | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/rel_x (VectorData) rel_x | shape = (128,) | dtype = float32
  Dataset /general/extracellular_ephys/electrodes/rel_y (VectorData) rel_y | shape = (128,) | dtype = float32
  institution: Princeton
  keywords: ['Development of the nervous system' 'Hippocampus' 'Neural circuits']
  lab: Buzsaki
  related_publications: ['https://doi.org/10.1038/s41593-022-01138-x']
  session_id: e13_16f1_210302
  Group /general/subject (Subject) 
  identifier: 58c232ba-f0ba-4812-9919-6e7e1e5f8b64
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (3,) | dtype = int64
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (3,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (3,) | dtype = float64
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/expected_arm (VectorData) A string representing the expected arm of the trial | shape = (22,) | dtype = object
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (22,) | dtype = int64
  Dataset /intervals/trials/is_familiar_maze (VectorData) A boolean representing whether the maze is familiar or novel | shape = (22,) | dtype = bool
  Dataset /intervals/trials/recordings (VectorData) An integer value representing which recording this trial belongs to | shape = (22,) | dtype = uint8
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (22,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (22,) | dtype = float64
  Dataset /intervals/trials/visited_arm (VectorData) A string representing the visited arm of the trial | shape = (22,) | dtype = object
  Dataset /intervals/trials/visited_matched_expected (VectorData) A boolean (or NaN) representing whether the expected and visited arm of the trial matches | shape = (22,) | dtype = float64
  Group /processing/behavior (ProcessingModule) The behavior of the subject for the following recordings: a, l, t, e, r, n, a, t, i, o, n
  Group /processing/behavior/LinearizedPosition (Position) 
  Group /processing/behavior/LinearizedPosition/LinearizedSpatialSeries (SpatialSeries) Linearization of the (x,y) coordinates tracking subject movement.
  Group /processing/behavior/RewardEventsEightMazeTrack (LabeledEvents) Rewards in a figure-eight maze
  Group /processing/behavior/SleepStates (TimeIntervals) Sleep state of the animal.
  Dataset /processing/behavior/SleepStates/id (ElementIdentifiers)  | shape = (30,) | dtype = int64
  Dataset /processing/behavior/SleepStates/label (VectorData) Sleep state. | shape = (30,) | dtype = object
  Dataset /processing/behavior/SleepStates/start_time (VectorData) Start time of epoch, in seconds | shape = (30,) | dtype = float64
  Dataset /processing/behavior/SleepStates/stop_time (VectorData) Stop time of epoch, in seconds | shape = (30,) | dtype = float64
  Group /processing/behavior/SubjectPosition (Position) 
  Group /processing/behavior/SubjectPosition/SpatialSeries (SpatialSeries) (x,y) coordinates tracking subject movement.
  Group /processing/ecephys (ProcessingModule) No description.
  Group /processing/ecephys/Ripples (TimeIntervals) Ripples and their metrics
  Dataset /processing/ecephys/Ripples/id (ElementIdentifiers)  | shape = (5798,) | dtype = int64
  Dataset /processing/ecephys/Ripples/peak_amplitudes (VectorData) Peak amplitude of the ripple. | shape = (5798,) | dtype = float64
  Dataset /processing/ecephys/Ripples/peak_frequencies (VectorData) Peak frequency of the ripple. | shape = (5798,) | dtype = float64
  Dataset /processing/ecephys/Ripples/peak_normed_power (VectorData) Normed power of the peak. | shape = (5798,) | dtype = float64
  Dataset /processing/ecephys/Ripples/peaks (VectorData) Peak of the ripple. | shape = (5798,) | dtype = float64
  Dataset /processing/ecephys/Ripples/ripple_amplitudes (VectorData) Amplitude of each point on the ripple. | shape = (5798, 461) | dtype = float64
  Dataset /processing/ecephys/Ripples/ripple_amplitudes_index (VectorIndex) Index for VectorData 'ripple_amplitudes' | shape = (5798,) | dtype = uint16
  Dataset /processing/ecephys/Ripples/ripple_durations (VectorData) Duration of the ripple event. | shape = (5798,) | dtype = float64
  Dataset /processing/ecephys/Ripples/ripple_frequencies (VectorData) Frequency of each point on the ripple. | shape = (5798, 461) | dtype = float64
  Dataset /processing/ecephys/Ripples/ripple_frequencies_index (VectorIndex) Index for VectorData 'ripple_frequencies' | shape = (5798,) | dtype = uint16
  Dataset /processing/ecephys/Ripples/ripple_phases (VectorData) Phase of each point on the ripple. | shape = (5798, 461) | dtype = float64
  Dataset /processing/ecephys/Ripples/ripple_phases_index (VectorIndex) Index for VectorData 'ripple_phases' | shape = (5798,) | dtype = uint16
  Dataset /processing/ecephys/Ripples/ripple_raw (VectorData) Extracted ripple data. | shape = (5798, 461) | dtype = float64
  Dataset /processing/ecephys/Ripples/ripple_raw_index (VectorIndex) Index for VectorData 'ripple_raw' | shape = (5798,) | dtype = uint16
  Dataset /processing/ecephys/Ripples/start_time (VectorData) Start time of epoch, in seconds | shape = (5798,) | dtype = float64
  Dataset /processing/ecephys/Ripples/stop_time (VectorData) Stop time of epoch, in seconds | shape = (5798,) | dtype = float64
  session_description: The incorporation of new information into the hippocampal network is likely to be constrained by its innate architecture and internally generated activity patterns. However, the origin, organization and consequences of such patterns remain poorly understood. In the present study we show that hippocampal network dynamics are affected by sequential neurogenesis. We birthdated CA1 pyramidal neurons with in utero electroporation over 4 embryonic days, encompassing the peak of hippocampal neurogenesis, and compared their functional features in freely moving adult mice. Neurons of the same birthdate displayed distinct connectivity, coactivity across brain states and assembly dynamics. Same-birthdate neurons exhibited overlapping spatial representations, which were maintained across different environments. Overall, the wiring and functional features of CA1 pyramidal neurons reflected a combination of birthdate and the rate of neurogenesis. These observations demonstrate that sequential neurogenesis during embryonic development shapes the preconfigured forms of adult network dynamics.
  session_start_time: 2021-03-02T00:00:00-05:00
  timestamps_reference_time: 2021-03-02T00:00:00-05:00
  Group /units (Units) Autogenerated by neuroconv.
  Dataset /units/clu_id (VectorData) 0-indexed id of cluster identified from the shank. | shape = (135,) | dtype = float64
  Dataset /units/group_id (VectorData) The electrode group ID that each unit was identified by. | shape = (135,) | dtype = object
  Dataset /units/id (ElementIdentifiers)  | shape = (135,) | dtype = int64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (8046943,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (135,) | dtype = uint32
  Dataset /units/unit_name (VectorData) Unique reference for each unit. | shape = (135,) | dtype = object


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2023-06-30T10:11:51.718834+00:00']
  Group /general/devices/DeviceEcephys (Device) no description
  Group /general/extracellular_ephys/Group 1 (ElectrodeGroup) no description
  Group /general/extracellular_ephys/Group 1/device (Device) no description
  Group /general/extracellular_ephys/Group 2 (ElectrodeGroup) no description
  Group /general/extracellular_ephys/Group 2/device (Device) no description
  Group /general/extracellular_ephys/Group 3 (ElectrodeGroup) no description
  Group /general/extracellular_ephys/Group 3/device (Device) no description
  Group /general/extracellular_ephys/Group 4 (ElectrodeGroup) no description
  Group /general/extracellular_ephys/Group 4/device (Device) no description
  Group /general/extracellular_ephys/Group 5 (ElectrodeGroup) no description
  Group /general/extracellular_ephys/Group 5/device (Device) no description
  Group /general/extracellular_ephys/Group 6 (ElectrodeGroup) no description
  Group /general/extracellular_ephys/Group 6/device (Device) no description
  Group /general/extracellular_ephys/Group 7 (ElectrodeGroup) no description
  Group /general/extracellular_ephys/Group 7/device (Device) no description
  Group /general/extracellular_ephys/Group 8 (ElectrodeGroup) no description
  Group /general/extracellular_ephys/Group 8/device (Device) no description
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/channel_name (VectorData) unique channel reference | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/gain_to_uV (VectorData) no description | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/rel_x (VectorData) rel_x | shape = (128,) | dtype = float32
  Dataset /general/extracellular_ephys/electrodes/rel_y (VectorData) rel_y | shape = (128,) | dtype = float32
  session_id: e15_13f1_220117_raw
  Group /general/subject (Subject) 
  identifier: 7b130345-e062-4f25-8011-b6aa6f8f8d39
  Group /processing/ecephys (ProcessingModule) Intermediate data from extracellular electrophysiology recordings, e.g., LFP.
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/ElectricalSeriesLFP (ElectricalSeries) Acquisition traces for the ElectricalSeriesLFP.
  Dataset /processing/ecephys/LFP/ElectricalSeriesLFP/electrodes (DynamicTableRegion) electrode_table_region | shape = (128,) | dtype = int64
  session_description: NWB files containing only the raw data for the corresponding session IDs in this DANDI set.
  session_start_time: 2011-08-18T00:00:00-04:00
  timestamps_reference_time: 2011-08-18T00:00:00-04:00


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2023-06-30T22:27:15.516742+00:00']
  experiment_description: Preconfigured dynamics in the hippocampus are guided by embryonic birthdate and rate of neurogenesis
  experimenter: ['Huszár, Roman' 'Zhang, Yunchang' 'Blockus, Heike' 'Buzsáki, György']
  institution: Princeton
  keywords: ['Development of the nervous system' 'Hippocampus' 'Neural circuits']
  lab: Buzsaki
  related_publications: ['https://doi.org/10.1038/s41593-022-01138-x']
  session_id: e13_1f1_200228
  Group /general/subject (Subject) 
  identifier: 439a3d96-63a7-4a96-8ef6-b133a3b4175f
  Group /processing/behavior (ProcessingModule) No description.
  Group /processing/behavior/SleepStates (TimeIntervals) Sleep state of the animal.
  Dataset /processing/behavior/SleepStates/id (ElementIdentifiers)  | shape = (116,) | dtype = int64
  Dataset /processing/behavior/SleepStates/label (VectorData) Sleep state. | shape = (116,) | dtype = object
  Dataset /processing/behavior/SleepStates/start_time (VectorData) Start time of epoch, in seconds | shape = (116,) | dtype = float64
  Dataset /processing/behavior/SleepStates/stop_time (VectorData) Stop time of epoch, in seconds | shape = (116,) | dtype = float64
  Group /processing/ecephys (ProcessingModule) No description.
  Group /processing/ecephys/Ripples (TimeIntervals) Ripples and their metrics
  Dataset /processing/ecephys/Ripples/id (ElementIdentifiers)  | shape = (5827,) | dtype = int64
  Dataset /processing/ecephys/Ripples/peak_amplitudes (VectorData) Peak amplitude of the ripple. | shape = (5827,) | dtype = float64
  Dataset /processing/ecephys/Ripples/peak_frequencies (VectorData) Peak frequency of the ripple. | shape = (5827,) | dtype = float64
  Dataset /processing/ecephys/Ripples/peak_normed_power (VectorData) Normed power of the peak. | shape = (5827,) | dtype = float64
  Dataset /processing/ecephys/Ripples/peaks (VectorData) Peak of the ripple. | shape = (5827,) | dtype = float64
  Dataset /processing/ecephys/Ripples/ripple_amplitudes (VectorData) Amplitude of each point on the ripple. | shape = (5827, 489) | dtype = float64
  Dataset /processing/ecephys/Ripples/ripple_amplitudes_index (VectorIndex) Index for VectorData 'ripple_amplitudes' | shape = (5827,) | dtype = uint16
  Dataset /processing/ecephys/Ripples/ripple_durations (VectorData) Duration of the ripple event. | shape = (5827,) | dtype = float64
  Dataset /processing/ecephys/Ripples/ripple_frequencies (VectorData) Frequency of each point on the ripple. | shape = (5827, 489) | dtype = float64
  Dataset /processing/ecephys/Ripples/ripple_frequencies_index (VectorIndex) Index for VectorData 'ripple_frequencies' | shape = (5827,) | dtype = uint16
  Dataset /processing/ecephys/Ripples/ripple_phases (VectorData) Phase of each point on the ripple. | shape = (5827, 489) | dtype = float64
  Dataset /processing/ecephys/Ripples/ripple_phases_index (VectorIndex) Index for VectorData 'ripple_phases' | shape = (5827,) | dtype = uint16
  Dataset /processing/ecephys/Ripples/ripple_raw (VectorData) Extracted ripple data. | shape = (5827, 489) | dtype = float64
  Dataset /processing/ecephys/Ripples/ripple_raw_index (VectorIndex) Index for VectorData 'ripple_raw' | shape = (5827,) | dtype = uint16
  Dataset /processing/ecephys/Ripples/start_time (VectorData) Start time of epoch, in seconds | shape = (5827,) | dtype = float64
  Dataset /processing/ecephys/Ripples/stop_time (VectorData) Stop time of epoch, in seconds | shape = (5827,) | dtype = float64
  session_description: The incorporation of new information into the hippocampal network is likely to be constrained by its innate architecture and internally generated activity patterns. However, the origin, organization and consequences of such patterns remain poorly understood. In the present study we show that hippocampal network dynamics are affected by sequential neurogenesis. We birthdated CA1 pyramidal neurons with in utero electroporation over 4 embryonic days, encompassing the peak of hippocampal neurogenesis, and compared their functional features in freely moving adult mice. Neurons of the same birthdate displayed distinct connectivity, coactivity across brain states and assembly dynamics. Same-birthdate neurons exhibited overlapping spatial representations, which were maintained across different environments. Overall, the wiring and functional features of CA1 pyramidal neurons reflected a combination of birthdate and the rate of neurogenesis. These observations demonstrate that sequential neurogenesis during embryonic development shapes the preconfigured forms of adult network dynamics.
  session_start_time: 2020-02-28T00:00:00-05:00
  timestamps_reference_time: 2020-02-28T00:00:00-05:00


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2023-06-30T22:27:01.951514+00:00']
  experiment_description: Preconfigured dynamics in the hippocampus are guided by embryonic birthdate and rate of neurogenesis
  experimenter: ['Huszár, Roman' 'Zhang, Yunchang' 'Blockus, Heike' 'Buzsáki, György']
  institution: Princeton
  keywords: ['Development of the nervous system' 'Hippocampus' 'Neural circuits']
  lab: Buzsaki
  related_publications: ['https://doi.org/10.1038/s41593-022-01138-x']
  session_id: e13_1f1_200229
  Group /general/subject (Subject) 
  identifier: e2d74b22-22c9-4a69-b762-fabfa912cb9f
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (1,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1,) | dtype = float64
  Group /processing/behavior (ProcessingModule) No description.
  Group /processing/behavior/SleepStates (TimeIntervals) Sleep state of the animal.
  Dataset /processing/behavior/SleepStates/id (ElementIdentifiers)  | shape = (90,) | dtype = int64
  Dataset /processing/behavior/SleepStates/label (VectorData) Sleep state. | shape = (90,) | dtype = object
  Dataset /processing/behavior/SleepStates/start_time (VectorData) Start time of epoch, in seconds | shape = (90,) | dtype = float64
  Dataset /processing/behavior/SleepStates/stop_time (VectorData) Stop time of epoch, in seconds | shape = (90,) | dtype = float64
  Group /processing/ecephys (ProcessingModule) No description.
  Group /processing/ecephys/Ripples (TimeIntervals) Ripples and their metrics
  Dataset /processing/ecephys/Ripples/id (ElementIdentifiers)  | shape = (3904,) | dtype = int64
  Dataset /processing/ecephys/Ripples/peak_amplitudes (VectorData) Peak amplitude of the ripple. | shape = (3904,) | dtype = float64
  Dataset /processing/ecephys/Ripples/peak_frequencies (VectorData) Peak frequency of the ripple. | shape = (3904,) | dtype = float64
  Dataset /processing/ecephys/Ripples/peak_normed_power (VectorData) Normed power of the peak. | shape = (3904,) | dtype = float64
  Dataset /processing/ecephys/Ripples/peaks (VectorData) Peak of the ripple. | shape = (3904,) | dtype = float64
  Dataset /processing/ecephys/Ripples/ripple_amplitudes (VectorData) Amplitude of each point on the ripple. | shape = (3904, 461) | dtype = float64
  Dataset /processing/ecephys/Ripples/ripple_amplitudes_index (VectorIndex) Index for VectorData 'ripple_amplitudes' | shape = (3904,) | dtype = uint16
  Dataset /processing/ecephys/Ripples/ripple_durations (VectorData) Duration of the ripple event. | shape = (3904,) | dtype = float64
  Dataset /processing/ecephys/Ripples/ripple_frequencies (VectorData) Frequency of each point on the ripple. | shape = (3904, 461) | dtype = float64
  Dataset /processing/ecephys/Ripples/ripple_frequencies_index (VectorIndex) Index for VectorData 'ripple_frequencies' | shape = (3904,) | dtype = uint16
  Dataset /processing/ecephys/Ripples/ripple_phases (VectorData) Phase of each point on the ripple. | shape = (3904, 461) | dtype = float64
  Dataset /processing/ecephys/Ripples/ripple_phases_index (VectorIndex) Index for VectorData 'ripple_phases' | shape = (3904,) | dtype = uint16
  Dataset /processing/ecephys/Ripples/ripple_raw (VectorData) Extracted ripple data. | shape = (3904, 461) | dtype = float64
  Dataset /processing/ecephys/Ripples/ripple_raw_index (VectorIndex) Index for VectorData 'ripple_raw' | shape = (3904,) | dtype = uint16
  Dataset /processing/ecephys/Ripples/start_time (VectorData) Start time of epoch, in seconds | shape = (3904,) | dtype = float64
  Dataset /processing/ecephys/Ripples/stop_time (VectorData) Stop time of epoch, in seconds | shape = (3904,) | dtype = float64
  session_description: The incorporation of new information into the hippocampal network is likely to be constrained by its innate architecture and internally generated activity patterns. However, the origin, organization and consequences of such patterns remain poorly understood. In the present study we show that hippocampal network dynamics are affected by sequential neurogenesis. We birthdated CA1 pyramidal neurons with in utero electroporation over 4 embryonic days, encompassing the peak of hippocampal neurogenesis, and compared their functional features in freely moving adult mice. Neurons of the same birthdate displayed distinct connectivity, coactivity across brain states and assembly dynamics. Same-birthdate neurons exhibited overlapping spatial representations, which were maintained across different environments. Overall, the wiring and functional features of CA1 pyramidal neurons reflected a combination of birthdate and the rate of neurogenesis. These observations demonstrate that sequential neurogenesis during embryonic development shapes the preconfigured forms of adult network dynamics.
  session_start_time: 2020-02-29T00:00:00-05:00
  timestamps_reference_time: 2020-02-29T00:00:00-05:00


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2023-06-30T22:27:27.438844+00:00']
  Group /general/devices/Device (Device) Ecephys probe. Automatically generated.
  experiment_description: Preconfigured dynamics in the hippocampus are guided by embryonic birthdate and rate of neurogenesis
  experimenter: ['Huszár, Roman' 'Zhang, Yunchang' 'Blockus, Heike' 'Buzsáki, György']
  Group /general/extracellular_ephys/Group 1 (ElectrodeGroup) no description
  Group /general/extracellular_ephys/Group 1/device (Device) Ecephys probe. Automatically generated.
  Group /general/extracellular_ephys/Group 2 (ElectrodeGroup) no description
  Group /general/extracellular_ephys/Group 2/device (Device) Ecephys probe. Automatically generated.
  Group /general/extracellular_ephys/Group 3 (ElectrodeGroup) no description
  Group /general/extracellular_ephys/Group 3/device (Device) Ecephys probe. Automatically generated.
  Group /general/extracellular_ephys/Group 4 (ElectrodeGroup) no description
  Group /general/extracellular_ephys/Group 4/device (Device) Ecephys probe. Automatically generated.
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/channel_name (VectorData) unique channel reference | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (64,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/rel_x (VectorData) rel_x | shape = (64,) | dtype = float32
  Dataset /general/extracellular_ephys/electrodes/rel_y (VectorData) rel_y | shape = (64,) | dtype = float32
  institution: Princeton
  keywords: ['Development of the nervous system' 'Hippocampus' 'Neural circuits']
  lab: Buzsaki
  related_publications: ['https://doi.org/10.1038/s41593-022-01138-x']
  session_id: e14_2m3_201017
  Group /general/subject (Subject) 
  identifier: 36d773e1-ed2a-4db7-8bfd-a2afc73684e4
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (1,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1,) | dtype = float64
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/expected_arm (VectorData) A string representing the expected arm of the trial | shape = (27,) | dtype = object
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (27,) | dtype = int64
  Dataset /intervals/trials/is_familiar_maze (VectorData) A boolean representing whether the maze is familiar or novel | shape = (27,) | dtype = bool
  Dataset /intervals/trials/recordings (VectorData) An integer value representing which recording this trial belongs to | shape = (27,) | dtype = uint8
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (27,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (27,) | dtype = float64
  Dataset /intervals/trials/visited_arm (VectorData) A string representing the visited arm of the trial | shape = (27,) | dtype = object
  Dataset /intervals/trials/visited_matched_expected (VectorData) A boolean (or NaN) representing whether the expected and visited arm of the trial matches | shape = (27,) | dtype = float64
  Group /processing/behavior (ProcessingModule) The behavior of the subject for the following recordings: a, l, t, e, r, n, a, t, i, o, n
  Group /processing/behavior/LinearizedPosition (Position) 
  Group /processing/behavior/LinearizedPosition/LinearizedSpatialSeries (SpatialSeries) Linearization of the (x,y) coordinates tracking subject movement.
  Group /processing/behavior/RewardEventsEightMazeTrack (LabeledEvents) Rewards in a figure-eight maze
  Group /processing/behavior/SleepStates (TimeIntervals) Sleep state of the animal.
  Dataset /processing/behavior/SleepStates/id (ElementIdentifiers)  | shape = (70,) | dtype = int64
  Dataset /processing/behavior/SleepStates/label (VectorData) Sleep state. | shape = (70,) | dtype = object
  Dataset /processing/behavior/SleepStates/start_time (VectorData) Start time of epoch, in seconds | shape = (70,) | dtype = float64
  Dataset /processing/behavior/SleepStates/stop_time (VectorData) Stop time of epoch, in seconds | shape = (70,) | dtype = float64
  Group /processing/behavior/SubjectPosition (Position) 
  Group /processing/behavior/SubjectPosition/SpatialSeries (SpatialSeries) (x,y) coordinates tracking subject movement.
  Group /processing/ecephys (ProcessingModule) No description.
  Group /processing/ecephys/Ripples (TimeIntervals) Ripples and their metrics
  Dataset /processing/ecephys/Ripples/id (ElementIdentifiers)  | shape = (5469,) | dtype = int64
  Dataset /processing/ecephys/Ripples/peak_amplitudes (VectorData) Peak amplitude of the ripple. | shape = (5469,) | dtype = float64
  Dataset /processing/ecephys/Ripples/peak_frequencies (VectorData) Peak frequency of the ripple. | shape = (5469,) | dtype = float64
  Dataset /processing/ecephys/Ripples/peak_normed_power (VectorData) Normed power of the peak. | shape = (5469,) | dtype = float64
  Dataset /processing/ecephys/Ripples/peaks (VectorData) Peak of the ripple. | shape = (5469,) | dtype = float64
  Dataset /processing/ecephys/Ripples/ripple_amplitudes (VectorData) Amplitude of each point on the ripple. | shape = (5469, 399) | dtype = float64
  Dataset /processing/ecephys/Ripples/ripple_amplitudes_index (VectorIndex) Index for VectorData 'ripple_amplitudes' | shape = (5469,) | dtype = uint16
  Dataset /processing/ecephys/Ripples/ripple_durations (VectorData) Duration of the ripple event. | shape = (5469,) | dtype = float64
  Dataset /processing/ecephys/Ripples/ripple_frequencies (VectorData) Frequency of each point on the ripple. | shape = (5469, 399) | dtype = float64
  Dataset /processing/ecephys/Ripples/ripple_frequencies_index (VectorIndex) Index for VectorData 'ripple_frequencies' | shape = (5469,) | dtype = uint16
  Dataset /processing/ecephys/Ripples/ripple_phases (VectorData) Phase of each point on the ripple. | shape = (5469, 399) | dtype = float64
  Dataset /processing/ecephys/Ripples/ripple_phases_index (VectorIndex) Index for VectorData 'ripple_phases' | shape = (5469,) | dtype = uint16
  Dataset /processing/ecephys/Ripples/ripple_raw (VectorData) Extracted ripple data. | shape = (5469, 399) | dtype = float64
  Dataset /processing/ecephys/Ripples/ripple_raw_index (VectorIndex) Index for VectorData 'ripple_raw' | shape = (5469,) | dtype = uint16
  Dataset /processing/ecephys/Ripples/start_time (VectorData) Start time of epoch, in seconds | shape = (5469,) | dtype = float64
  Dataset /processing/ecephys/Ripples/stop_time (VectorData) Stop time of epoch, in seconds | shape = (5469,) | dtype = float64
  session_description: The incorporation of new information into the hippocampal network is likely to be constrained by its innate architecture and internally generated activity patterns. However, the origin, organization and consequences of such patterns remain poorly understood. In the present study we show that hippocampal network dynamics are affected by sequential neurogenesis. We birthdated CA1 pyramidal neurons with in utero electroporation over 4 embryonic days, encompassing the peak of hippocampal neurogenesis, and compared their functional features in freely moving adult mice. Neurons of the same birthdate displayed distinct connectivity, coactivity across brain states and assembly dynamics. Same-birthdate neurons exhibited overlapping spatial representations, which were maintained across different environments. Overall, the wiring and functional features of CA1 pyramidal neurons reflected a combination of birthdate and the rate of neurogenesis. These observations demonstrate that sequential neurogenesis during embryonic development shapes the preconfigured forms of adult network dynamics.
  session_start_time: 2020-10-17T00:00:00-04:00
  timestamps_reference_time: 2020-10-17T00:00:00-04:00
  Group /units (Units) Autogenerated by neuroconv.
  Dataset /units/clu_id (VectorData) 0-indexed id of cluster identified from the shank. | shape = (34,) | dtype = float64
  Dataset /units/group_id (VectorData) The electrode group ID that each unit was identified by. | shape = (34,) | dtype = object
  Dataset /units/id (ElementIdentifiers)  | shape = (34,) | dtype = int64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (1921664,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (34,) | dtype = uint32
  Dataset /units/unit_name (VectorData) Unique reference for each unit. | shape = (34,) | dtype = object
