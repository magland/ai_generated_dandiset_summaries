
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000575/0.231010.1811
name: Dataset of human medial temporal lobe neurons during a visual working memory task
contributor: [{'name': 'Boran, Ece', 'roleName': [], 'schemaKey': 'Person', 'identifier': '0000-0002-0395-7575', 'affiliation': [{'name': 'Department of Neurosurgery, University Hospital Zurich (USZ), University of Zurich, Zurich 8091, Switzerland', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/01462r250'}], 'includeInCitation': True}, {'name': 'Hilfiker, Peter', 'roleName': [], 'schemaKey': 'Person', 'identifier': '0000-0001-7729-4754', 'affiliation': [], 'includeInCitation': True}, {'name': 'Stieglitz, Lennart ', 'roleName': [], 'schemaKey': 'Person', 'identifier': '0000-0002-3744-5105', 'affiliation': [{'name': 'Department of Neurosurgery, University Hospital Zurich (USZ), University of Zurich, Zurich 8091, Switzerland', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/01462r250'}], 'includeInCitation': True}, {'name': 'Hohenheim, Jan', 'email': 'jan@hohenheim.ch', 'roleName': ['dcite:ContactPerson', 'dcite:DataManager'], 'schemaKey': 'Person', 'identifier': '0000-0001-9436-8348', 'affiliation': [], 'includeInCitation': True}, {'name': 'Klaver, Peter', 'email': 'peter.klaver@hfh.ch', 'roleName': ['dcite:Author', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0002-6541-9975', 'affiliation': [{'name': 'University of Teacher Education in Special Needs, Zurich 8050, Switzerland', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/00w9q2c06'}, {'name': 'Institute of Psychology, University of Zurich, Zurich 8050, Switzerland', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/02crff812'}, {'name': 'School of Psychology, University of Surrey, Guildford GU2 7XH, UK', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/00ks66431'}], 'includeInCitation': True}, {'name': 'Sarnthein, Johannes ', 'email': 'johannes.sarnthein@usz.ch', 'roleName': ['dcite:Author', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0001-9141-381X', 'affiliation': [{'name': 'Department of Neurosurgery, University Hospital Zurich (USZ), University of Zurich, Zurich 8091, Switzerland.', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/01462r250'}, {'name': 'Neuroscience Center Zurich, ETH Zurich, Zurich 8057, Switzerland', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/01462r250'}], 'includeInCitation': True}, {'url': 'http://www.snf.ch/en', 'name': ' Swiss National Science Foundation', 'email': 'projects.ls@snf.ch', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/00yjd3n13', 'awardNumber': '204651', 'contactPoint': [], 'includeInCitation': False}, {'url': 'https://www.kavlifoundation.org/', 'name': ' The Kavli Foundation', 'email': 'communications@kavlifoundation.org', 'roleName': ['dcite:Sponsor'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/00kztt736', 'awardNumber': '2586', 'contactPoint': [], 'includeInCitation': False}]
description: We present an electrophysiological dataset recorded from thirteen subjects during a visual working memory task. Subjects were epilepsy patients undergoing intracranial monitoring for localization of epileptic seizures. Here, we recorded single neuron firing in 13 epilepsy patients (7 male) while they performed a visual working memory task. The task is a change detection task designed to examine the visual working memory of subjects. In each trial, arrays of colored squares were presented and had to be memorized. The number of squares determined the set size: 1, 2, 4 or 6. There was a total 192 trials per session. Each trial started with a warning signal (0.4 s) that was a red fixation dot. The fixation dot was then changed to black (0.4 – 0.5 s, jittered). A memory array (encoding period, 0.8 s) was followed by a delay (retention interval, 0.9 s). After the delay, a test array was shown (2 s) followed by a jittered inter-trial interval of 1.3 to 2.3 s. The participants indicated by button press (“Same” or “Different”, forced choice) whether the test array differed from the memory array. If the arrays differed, only one square changed in colour, but all squares remained on the same location. The fixation dot was visible on the screen during the whole trial period. Eight different colours were used for the memory and test array (yellow, red, green, blue, magenta, cyan, grey, black). Before starting the sessions, participants conducted trial runs in a practice session to learn the task. In this session we verified if participants were colour-blind and could discriminate all colours. Practice sessions were repeated until the participant understood the task and was able to follow the pace of the trials.
assetsSummary: {'species': [{'name': 'Homo sapiens - Human', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9606'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}, {'name': 'behavioral approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 50794717628, 'numberOfFiles': 18, 'numberOfSubjects': 13, 'variableMeasured': ['Units', 'BehavioralEvents', 'ElectrodeGroup', 'ProcessingModule', 'LFP', 'ElectricalSeries'], 'measurementTechnique': [{'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'signal filtering technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000575 has 18 NWB files.
13 of these NWB files are of type 1.
5 of these NWB files are of type 2.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2023-10-09T22:11:54.109115+02:00']
  Group /general/devices/ATLAS Neurophysiology System (Device) iEEG recording system
  experiment_description: Task Name: Klaver
  Task Description: The task is a change detection task designed to examine the visual working memory of subjects. In each trial, arrays of colored squares were presented and had to be memorized. The number of squares determined the set size: 1, 2, 4 or 6. There was a total 192 trials per session. Each trial started with a warning signal (0.4 s) that was a red fixation dot. The fixation dot was then changed to black (0.4 – 0.5 s, jittered). A memory array (encoding period, 0.8 s) was followed by a delay (retention interval, 0.9 s). After the delay, a test array was shown (2 s) followed by a jittered inter-trial interval of 1.3 to 2.3 s. The participants indicated by button press (“Same” or “Different”, forced choice) whether the test array differed from the memory array. If the arrays differed, only one square changed in colour, but all squares remained on the same location. The fixation dot was visible on the screen during the whole trial period. Eight different colours were used for the memory and test array (yellow, red, green, blue, magenta, cyan, grey, black). Before starting the sessions, participants conducted trial runs in a practice session to learn the task. In this session we verified if participants were colour-blind and could discriminate all colours. Practice sessions were repeated until the participant understood the task and was able to follow the pace of the trials.
  Task URL: https://www.neurobs.com/ex_files/expt_view?id=285&tree_item_url=klaver12.exp&item_id=klaver12.exp
  experimenter: ['Boran, Ece']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering, including the filter name and frequency cutoffs | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (64,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/is_inside_soz (VectorData) Indicates whether the electrode is inside the seizure onset zone (SOZ) | shape = (64,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/label (VectorData) Channel label referenced by other data arrays | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/reference (VectorData) Description of the reference electrode and/or reference scheme used for this                         electrode, e.g.,"stainless steel skull screw" or "online common average referencing". | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the position (+x is posterior) | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the position (+y is inferior) | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the position (+z is right) | shape = (64,) | dtype = float64
  Group /general/extracellular_ephys/ieeg (ElectrodeGroup) iEEG electrodes
  Group /general/extracellular_ephys/ieeg/device (Device) iEEG recording system
  institution: Universitätsspital Zürich, 8091 Zurich, Switzerland
  keywords: ['Visual' 'Spatial' 'Neural decoding' 'Hippocampus' 'Entorhinal cortex']
  lab: Schweizerische Epilepsie-Zentrum, 8008 Zurich, Switzerland
  related_publications: ['https://doi.org/10.1016/j.neuroimage.2022.119123']
  Group /general/subject (Subject) 
  identifier: Human_MTL_units_visual_WM_subject01_session01
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (756,) | dtype = int32
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (756,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (756,) | dtype = float64
  Dataset /intervals/epochs/tags (VectorData) user-defined tags | shape = (756,) | dtype = object
  Dataset /intervals/epochs/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (756,) | dtype = uint16
  Dataset /intervals/epochs/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (756,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/epochs/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (756,) | dtype = uint16
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (189,) | dtype = int32
  Dataset /intervals/trials/set_size (VectorData) Number of colored squares in array presented during encoding period. Either 1, 2, 4, or 6. | shape = (189,) | dtype = int32
  Dataset /intervals/trials/solution (VectorData) The correct answer to the question "Was the array presented during the test the same as the one presented during the encoding period?" | shape = (189,) | dtype = bool
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (189,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (189,) | dtype = float64
  Dataset /intervals/trials/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (189,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/trials/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (189,) | dtype = uint8
  Group /processing/behavior (ProcessingModule) Data for all trials in this session.
  Group /processing/behavior/BehavioralEvents.response (BehavioralEvents) 
  Group /processing/behavior/BehavioralEvents.response/response (TimeSeries) The participant's answer to the question "Was the array presented during the test the same as the one presented during the encoding period?"
  Group /processing/ecephys (ProcessingModule) processed extracellular electrophysiology data
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/ecephys.lfp (ElectricalSeries) LFP data
  Dataset /processing/ecephys/LFP/ecephys.lfp/electrodes (DynamicTableRegion) ieeg electrodes | shape = (64,) | dtype = int32
  session_description: Running experiment as described in the the experiment description
  session_start_time: 2014-08-27T19:38:00+02:00
  timestamps_reference_time: 2014-08-27T19:38:00+02:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (33,) | dtype = object
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (33,) | dtype = int32
  Dataset /units/electrodes_index (VectorIndex) Index for VectorData 'electrodes' | shape = (33,) | dtype = uint8
  Dataset /units/id (ElementIdentifiers)  | shape = (33,) | dtype = int32
  Dataset /units/obs_intervals (VectorData) the observation intervals for each unit | shape = (6237, 2) | dtype = float64
  Dataset /units/obs_intervals_index (VectorIndex) Index for VectorData 'obs_intervals' | shape = (33,) | dtype = uint16
  Dataset /units/offset (VectorData) The offset in seconds of the first waveform voltage relative to the spike event | shape = (33,) | dtype = float64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (55038,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (33,) | dtype = uint16
  Dataset /units/waveform_mean (VectorData) the spike waveform mean for each spike unit | shape = (33, 64) | dtype = float64
  Dataset /units/waveform_sd (VectorData) the spike waveform standard deviation for each spike unit | shape = (33, 64) | dtype = float64


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2023-10-09T22:16:04.214541+02:00']
  Group /general/devices/ATLAS Neurophysiology System (Device) iEEG recording system
  experiment_description: Task Name: Klaver
  Task Description: The task is a change detection task designed to examine the visual working memory of subjects. In each trial, arrays of colored squares were presented and had to be memorized. The number of squares determined the set size: 1, 2, 4 or 6. There was a total 192 trials per session. Each trial started with a warning signal (0.4 s) that was a red fixation dot. The fixation dot was then changed to black (0.4 – 0.5 s, jittered). A memory array (encoding period, 0.8 s) was followed by a delay (retention interval, 0.9 s). After the delay, a test array was shown (2 s) followed by a jittered inter-trial interval of 1.3 to 2.3 s. The participants indicated by button press (“Same” or “Different”, forced choice) whether the test array differed from the memory array. If the arrays differed, only one square changed in colour, but all squares remained on the same location. The fixation dot was visible on the screen during the whole trial period. Eight different colours were used for the memory and test array (yellow, red, green, blue, magenta, cyan, grey, black). Before starting the sessions, participants conducted trial runs in a practice session to learn the task. In this session we verified if participants were colour-blind and could discriminate all colours. Practice sessions were repeated until the participant understood the task and was able to follow the pace of the trials.
  Task URL: https://www.neurobs.com/ex_files/expt_view?id=285&tree_item_url=klaver12.exp&item_id=klaver12.exp
  experimenter: ['Boran, Ece']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering, including the filter name and frequency cutoffs | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (32,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/is_inside_soz (VectorData) Indicates whether the electrode is inside the seizure onset zone (SOZ) | shape = (32,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/label (VectorData) Channel label referenced by other data arrays | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/reference (VectorData) Description of the reference electrode and/or reference scheme used for this                         electrode, e.g.,"stainless steel skull screw" or "online common average referencing". | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the position (+x is posterior) | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the position (+y is inferior) | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the position (+z is right) | shape = (32,) | dtype = float64
  Group /general/extracellular_ephys/ieeg (ElectrodeGroup) iEEG electrodes
  Group /general/extracellular_ephys/ieeg/device (Device) iEEG recording system
  institution: Universitätsspital Zürich, 8091 Zurich, Switzerland
  keywords: ['Visual' 'Spatial' 'Neural decoding' 'Hippocampus' 'Entorhinal cortex']
  lab: Schweizerische Epilepsie-Zentrum, 8008 Zurich, Switzerland
  related_publications: ['https://doi.org/10.1016/j.neuroimage.2022.119123']
  Group /general/subject (Subject) 
  identifier: Human_MTL_units_visual_WM_subject02_session01
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (768,) | dtype = int32
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (768,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (768,) | dtype = float64
  Dataset /intervals/epochs/tags (VectorData) user-defined tags | shape = (768,) | dtype = object
  Dataset /intervals/epochs/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (768,) | dtype = uint16
  Dataset /intervals/epochs/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (768,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/epochs/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (768,) | dtype = uint16
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (192,) | dtype = int32
  Dataset /intervals/trials/set_size (VectorData) Number of colored squares in array presented during encoding period. Either 1, 2, 4, or 6. | shape = (192,) | dtype = int32
  Dataset /intervals/trials/solution (VectorData) The correct answer to the question "Was the array presented during the test the same as the one presented during the encoding period?" | shape = (192,) | dtype = bool
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (192,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (192,) | dtype = float64
  Dataset /intervals/trials/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (192,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/trials/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (192,) | dtype = uint8
  Group /processing/behavior (ProcessingModule) Data for all trials in this session.
  Group /processing/behavior/BehavioralEvents.response (BehavioralEvents) 
  Group /processing/behavior/BehavioralEvents.response/response (TimeSeries) The participant's answer to the question "Was the array presented during the test the same as the one presented during the encoding period?"
  session_description: Running experiment as described in the the experiment description
  session_start_time: 2017-10-11T15:21:00+02:00
  timestamps_reference_time: 2017-10-11T15:21:00+02:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (36,) | dtype = object
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (36,) | dtype = int32
  Dataset /units/electrodes_index (VectorIndex) Index for VectorData 'electrodes' | shape = (36,) | dtype = uint8
  Dataset /units/id (ElementIdentifiers)  | shape = (36,) | dtype = int32
  Dataset /units/obs_intervals (VectorData) the observation intervals for each unit | shape = (6912, 2) | dtype = float64
  Dataset /units/obs_intervals_index (VectorIndex) Index for VectorData 'obs_intervals' | shape = (36,) | dtype = uint16
  Dataset /units/offset (VectorData) The offset in seconds of the first waveform voltage relative to the spike event | shape = (36,) | dtype = float64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (45296,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (36,) | dtype = uint16
  Dataset /units/waveform_mean (VectorData) the spike waveform mean for each spike unit | shape = (36, 64) | dtype = float64
  Dataset /units/waveform_sd (VectorData) the spike waveform standard deviation for each spike unit | shape = (36, 64) | dtype = float64
