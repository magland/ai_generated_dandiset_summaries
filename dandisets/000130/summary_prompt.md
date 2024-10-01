
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000130/0.220113.0407
name: DMFC_RSG: macaque dorsomedial frontal cortex spiking activity during time interval reproduction task
contributor: [{'name': 'Pei, Felix', 'email': 'felp8484@gmail.com', 'roleName': ['dcite:ContactPerson', 'dcite:Maintainer'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': False}, {'name': 'Sohn, Hansem', 'roleName': ['dcite:Author', 'dcite:DataCollector'], 'schemaKey': 'Person', 'identifier': '0000-0001-8593-7473', 'affiliation': [{'name': 'Massachusetts Institute of Technology', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/042nb2s44'}], 'includeInCitation': True}, {'name': 'Jazayeri, Mehrdad', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-9764-6961', 'affiliation': [{'name': 'Massachusetts Institute of Technology', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/042nb2s44'}], 'includeInCitation': True}]
description: This dataset contains sorted unit spiking times from a macaque performing a time-interval reproduction task. In the experimental task, the monkey was presented with two stimuli separated by a specific interval of time. The monkey then attempted to time their response such that the interval between the second stimulus and their response matched the interval separating the two stimuli. Neural activity was recorded from neural probes implanted in the dorsomedial frontal cortex. Provided as part of the Neural Latents Benchmark: https://neurallatents.github.io.
assetsSummary: {'species': [{'name': 'Rhesus monkey', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9544'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 15673496, 'numberOfFiles': 2, 'numberOfSubjects': 1, 'variableMeasured': ['Units'], 'measurementTechnique': [{'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000130 has 2 NWB files.
1 of these NWB files are of type 1.
1 of these NWB files are of type 2.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2021-10-29T22:31:56.620865-04:00']
  Group /general/devices/electrode_probe_1 (Device) Linear probe with 24 recording channels
  Group /general/devices/electrode_probe_2 (Device) Linear probe with 24 recording channels
  Group /general/devices/electrode_probe_3 (Device) Linear probe with 24 recording channels
  experiment_description: Cognitive timing task in which subject attempts to reproduce interval between two cues
  experimenter: ['Hansem Sohn']
  Group /general/extracellular_ephys/electrode_group_1 (ElectrodeGroup) Electrodes on a neural probe
  Group /general/extracellular_ephys/electrode_group_1/device (Device) Linear probe with 24 recording channels
  Group /general/extracellular_ephys/electrode_group_2 (ElectrodeGroup) Electrodes on a neural probe
  Group /general/extracellular_ephys/electrode_group_2/device (Device) Linear probe with 24 recording channels
  Group /general/extracellular_ephys/electrode_group_3 (ElectrodeGroup) Electrodes on a neural probe
  Group /general/extracellular_ephys/electrode_group_3/device (Device) Linear probe with 24 recording channels
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (72,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (72,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (72,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (72,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (72,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (72,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (72,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (72,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (72,) | dtype = float64
  institution: Massachusetts Institute of Technology
  keywords: ['frontal cortex' 'cognitive' 'macaque' 'Neural Latents Benchmark']
  lab: Jazayeri
  related_publications: ['http://dx.doi.org/10.1016/j.neuron.2019.06.012']
  session_id: 20161211
  Group /general/subject (Subject) 
  identifier: 8d26aa92-3929-11ec-8077-43176b153428
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/go_time (VectorData) Time of monkey response, either with an eye saccade or joystick movement | shape = (283,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (283,) | dtype = int64
  Dataset /intervals/trials/split (VectorData) Trial split that the trial belongs to for the Neural Latents Benchmark. Can be "train", "val", "test", or "none" | shape = (283,) | dtype = object
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (283,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (283,) | dtype = float64
  session_description: Data from monkey Haydn performing ready-set-go time interval reproduction task. This file contains segments of trials from the full session on 2016-12-11 that are to be used for evaluating models for the Neural Latents Benchmark.
  session_start_time: 2016-12-11T00:00:00-05:00
  timestamps_reference_time: 2016-12-11T00:00:00-05:00
  Group /units (Units) data on spiking units
  Dataset /units/heldout (VectorData) Whether the unit is held out in the test data (True) or not (False) in the Neural Latents Benchmark | shape = (40,) | dtype = bool
  Dataset /units/id (ElementIdentifiers)  | shape = (40,) | dtype = int32
  Dataset /units/obs_intervals (VectorData) the observation intervals for each unit | shape = (11320, 2) | dtype = float64
  Dataset /units/obs_intervals_index (VectorIndex) Index for VectorData 'obs_intervals' | shape = (40,) | dtype = uint16
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (140799,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (40,) | dtype = uint32


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2021-10-29T22:31:50.351047-04:00']
  Group /general/devices/electrode_probe_1 (Device) Linear probe with 24 recording channels
  Group /general/devices/electrode_probe_2 (Device) Linear probe with 24 recording channels
  Group /general/devices/electrode_probe_3 (Device) Linear probe with 24 recording channels
  experiment_description: Cognitive timing task in which subject attempts to reproduce interval between two cues
  experimenter: ['Hansem Sohn']
  Group /general/extracellular_ephys/electrode_group_1 (ElectrodeGroup) Electrodes on a neural probe
  Group /general/extracellular_ephys/electrode_group_1/device (Device) Linear probe with 24 recording channels
  Group /general/extracellular_ephys/electrode_group_2 (ElectrodeGroup) Electrodes on a neural probe
  Group /general/extracellular_ephys/electrode_group_2/device (Device) Linear probe with 24 recording channels
  Group /general/extracellular_ephys/electrode_group_3 (ElectrodeGroup) Electrodes on a neural probe
  Group /general/extracellular_ephys/electrode_group_3/device (Device) Linear probe with 24 recording channels
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (72,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (72,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (72,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (72,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (72,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (72,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (72,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (72,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (72,) | dtype = float64
  institution: Massachusetts Institute of Technology
  keywords: ['frontal cortex' 'cognitive' 'macaque' 'Neural Latents Benchmark']
  lab: Jazayeri
  related_publications: ['http://dx.doi.org/10.1016/j.neuron.2019.06.012']
  session_id: 20161211
  Group /general/subject (Subject) 
  identifier: 8969f328-3929-11ec-8077-43176b153428
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/bad_time (VectorData) Time of trial failure, if the trial was unsuccessful | shape = (1160,) | dtype = float64
  Dataset /intervals/trials/fix_on_time (VectorData) Time when the fixation cue on the display turns on | shape = (1160,) | dtype = float64
  Dataset /intervals/trials/fix_time (VectorData) Time when the animal fixates on the fixation cue | shape = (1160,) | dtype = float64
  Dataset /intervals/trials/fix_time_dur (VectorData) Time between animal fixation and target onset, in ms | shape = (1160,) | dtype = float64
  Dataset /intervals/trials/go_time (VectorData) Time of monkey response, either with an eye saccade or joystick movement | shape = (1160,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (1160,) | dtype = int64
  Dataset /intervals/trials/is_eye (VectorData) Whether motion to target was with hand (False) or eye (True) | shape = (1160,) | dtype = bool
  Dataset /intervals/trials/is_outlier (VectorData) Whether a trial's tp is considered an outlier using probabilistic mixture model | shape = (1160,) | dtype = bool
  Dataset /intervals/trials/is_short (VectorData) Whether short prior (True) or long prior (False) | shape = (1160,) | dtype = bool
  Dataset /intervals/trials/iti (VectorData) Inter-trial interval, in ms. Equal to 500 for trials sampled from short prior and 1220 for trials sampled from long prior | shape = (1160,) | dtype = float64
  Dataset /intervals/trials/ready_time (VectorData) Time of ready cue delivery | shape = (1160,) | dtype = float64
  Dataset /intervals/trials/reward_dur (VectorData) Duration of reward, in ms | shape = (1160,) | dtype = float64
  Dataset /intervals/trials/reward_time (VectorData) Time of monkey reward, if there was one | shape = (1160,) | dtype = float64
  Dataset /intervals/trials/set_time (VectorData) Time of set cue presentation | shape = (1160,) | dtype = float64
  Dataset /intervals/trials/split (VectorData) Trial split that the trial belongs to for the Neural Latents Benchmark. Can be "train", "val", "test", or "none" | shape = (1160,) | dtype = object
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (1160,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1160,) | dtype = float64
  Dataset /intervals/trials/target_acq_time (VectorData) Time of target acquisition | shape = (1160,) | dtype = float64
  Dataset /intervals/trials/target_on_time (VectorData) Time of target presentation | shape = (1160,) | dtype = float64
  Dataset /intervals/trials/target_time_dur (VectorData) Time between target onset and ready, in ms | shape = (1160,) | dtype = float64
  Dataset /intervals/trials/theta (VectorData) Whether the target was on the right (0) or left (180) | shape = (1160,) | dtype = float64
  Dataset /intervals/trials/tp (VectorData) Time between set stimulus and monkey go response, in ms | shape = (1160,) | dtype = float64
  Dataset /intervals/trials/ts (VectorData) Time between ready and set stimuli, in ms | shape = (1160,) | dtype = float64
  session_description: Data from monkey Haydn performing ready-set-go time interval reproduction task. This file contains continuous segments of the full session on 2016-12-11 that can be used for training models for the Neural Latents Benchmark.
  session_start_time: 2016-12-11T00:00:00-05:00
  timestamps_reference_time: 2016-12-11T00:00:00-05:00
  Group /units (Units) data on spiking units
  Dataset /units/heldout (VectorData) Whether the unit is held out in the test data (True) or not (False) in the Neural Latents Benchmark | shape = (54,) | dtype = bool
  Dataset /units/id (ElementIdentifiers)  | shape = (54,) | dtype = int32
  Dataset /units/obs_intervals (VectorData) the observation intervals for each unit | shape = (324, 2) | dtype = float64
  Dataset /units/obs_intervals_index (VectorIndex) Index for VectorData 'obs_intervals' | shape = (54,) | dtype = uint16
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (1706196,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (54,) | dtype = uint32
