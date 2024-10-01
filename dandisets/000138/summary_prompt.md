
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000138/0.220113.0407
name: MC_Maze_Large: macaque primary motor and dorsal premotor cortex spiking activity during delayed reaching
contributor: [{'name': 'Pei, Felix', 'email': 'felp8484@gmail.com', 'roleName': ['dcite:ContactPerson', 'dcite:Maintainer'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': False}, {'name': 'Churchland, Mark', 'roleName': ['dcite:Author', 'dcite:DataCollector'], 'schemaKey': 'Person', 'identifier': '0000-0001-9123-6526', 'affiliation': [{'name': 'Stanford University', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/00f54p054'}, {'name': 'Columbia University', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/00hj8s172'}], 'includeInCitation': True}, {'name': 'Kaufman, Matthew', 'roleName': ['dcite:Author', 'dcite:DataCollector'], 'schemaKey': 'Person', 'identifier': '0000-0002-8072-023X', 'affiliation': [{'name': 'Stanford University', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/00f54p054'}, {'name': 'University of Chicago', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/024mw5h28'}], 'includeInCitation': True}]
description: This dataset contains sorted unit spiking times and behavioral data from a macaque performing a delayed reaching task. The experimental task was a center-out reaching task with obstructing barriers forming a maze, resulting in a variety of straight and curved reaches. Neural activity was recorded from electrode arrays implanted in the motor cortex (M1) and dorsal premotor cortex (PMd). Cursor position, hand position, and eye position were also recorded during the experiment, and hand velocity was calculated offline from hand position. The provided data has been limited to 500 train trials and 100 test trials. Provided as part of the Neural Latents Benchmark: https://neurallatents.github.io.
assetsSummary: {'species': [{'name': 'Rhesus monkey', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9544'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 149392888, 'numberOfFiles': 2, 'numberOfSubjects': 1, 'variableMeasured': ['Units', 'ProcessingModule'], 'measurementTechnique': [{'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000138 has 2 NWB files.
1 of these NWB files are of type 1.
1 of these NWB files are of type 2.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2021-09-01T22:26:51.523004-04:00']
  Group /general/devices/electrode_array_M1 (Device) 96-electrode Utah array in M1
  Group /general/devices/electrode_array_PMd (Device) 96-electrode Utah array in PMd
  experiment_description: Center-out delayed reaching task with maze barriers
  experimenter: ['Mark M. Churchland' 'Matthew T. Kaufman']
  Group /general/extracellular_ephys/electrode_group_M1 (ElectrodeGroup) Electrodes in an implanted Utah array in M1
  Group /general/extracellular_ephys/electrode_group_M1/device (Device) 96-electrode Utah array in M1
  Group /general/extracellular_ephys/electrode_group_PMd (ElectrodeGroup) Electrodes in implanted Utah Array in PMd
  Group /general/extracellular_ephys/electrode_group_PMd/device (Device) 96-electrode Utah array in PMd
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (192,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (192,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (192,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (192,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (192,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (192,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (192,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (192,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (192,) | dtype = float64
  institution: Stanford University
  keywords: ['motor cortex' 'premotor cortex' 'reaching' 'macaque'
   'Neural Latents Benchmark']
  lab: Shenoy
  related_publications: ['https://doi.org/10.1016/j.neuron.2010.09.015']
  session_id: large
  Group /general/subject (Subject) 
  identifier: 3b56e14e-0b95-11ec-a513-5fc582312949
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (100,) | dtype = int64
  Dataset /intervals/trials/move_onset_time (VectorData) Time of movement onset, calculated offline using a robust algorithm | shape = (100,) | dtype = float64
  Dataset /intervals/trials/split (VectorData) Trial split that the trial belongs to for the Neural Latents Benchmark. Can be "train", "val", "test", or "none" | shape = (100,) | dtype = object
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (100,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (100,) | dtype = float64
  session_description: Data from monkey Jenkins performing center-out delayed reaching task. This file contains segments of trials from the full session on 2009-10-06 that are to be used for evaluating models for the Neural Latents Benchmark.
  session_start_time: 2009-10-06T00:00:00-07:00
  timestamps_reference_time: 2009-10-06T00:00:00-07:00
  Group /units (Units) data on spiking units
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (122,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex) Index for VectorData 'electrodes' | shape = (122,) | dtype = uint8
  Dataset /units/heldout (VectorData) Whether the unit is held out in the test data (True) or not (False) in the Neural Latents Benchmark | shape = (122,) | dtype = bool
  Dataset /units/id (ElementIdentifiers)  | shape = (122,) | dtype = int64
  Dataset /units/obs_intervals (VectorData) the observation intervals for each unit | shape = (12200, 2) | dtype = float64
  Dataset /units/obs_intervals_index (VectorIndex) Index for VectorData 'obs_intervals' | shape = (122,) | dtype = uint16
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (44027,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (122,) | dtype = uint16


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2021-09-01T22:26:43.507718-04:00']
  Group /general/devices/electrode_array_M1 (Device) 96-electrode Utah array in M1
  Group /general/devices/electrode_array_PMd (Device) 96-electrode Utah array in PMd
  experiment_description: Center-out delayed reaching task with maze barriers.
  experimenter: ['Mark M. Churchland' 'Matthew T. Kaufman']
  Group /general/extracellular_ephys/electrode_group_M1 (ElectrodeGroup) Electrodes in an implanted Utah array in M1
  Group /general/extracellular_ephys/electrode_group_M1/device (Device) 96-electrode Utah array in M1
  Group /general/extracellular_ephys/electrode_group_PMd (ElectrodeGroup) Electrodes in implanted Utah Array in PMd
  Group /general/extracellular_ephys/electrode_group_PMd/device (Device) 96-electrode Utah array in PMd
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (192,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (192,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (192,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (192,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (192,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (192,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (192,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (192,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (192,) | dtype = float64
  institution: Stanford University
  keywords: ['motor cortex' 'premotor cortex' 'reaching' 'macaque'
   'Neural Latents Benchmark']
  lab: Shenoy
  related_publications: ['https://doi.org/10.1016/j.neuron.2010.09.015']
  session_id: large
  Group /general/subject (Subject) 
  identifier: 368fc9f0-0b95-11ec-a513-5fc582312949
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/active_target (VectorData) Which target is reachable and was hit. Value is the index of the target in target_pos list | shape = (500,) | dtype = int64
  Dataset /intervals/trials/barrier_pos (VectorData) Array with rows containing barrier location information. The first two values are the x and y coordinates of the center of the barrier, and the last two are half the width and height of the barrier, respectively | shape = (2569, 4) | dtype = int64
  Dataset /intervals/trials/barrier_pos_index (VectorIndex) Index for VectorData 'barrier_pos' | shape = (500,) | dtype = uint16
  Dataset /intervals/trials/delay (VectorData) Delay between target presentation and go cue, in ms | shape = (500,) | dtype = int64
  Dataset /intervals/trials/go_cue_time (VectorData) Time of go cue delivery, as detected by the photobox | shape = (500,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (500,) | dtype = int64
  Dataset /intervals/trials/maze_id (VectorData) A unique identifier for each maze, lumping all 3 `trial_version`s. `trial_type` is not unique across datasets, but `maze_id` is | shape = (500,) | dtype = int64
  Dataset /intervals/trials/move_onset_time (VectorData) Time of movement onset, calculated offline using a robust algorithm | shape = (500,) | dtype = float64
  Dataset /intervals/trials/num_barriers (VectorData) The number of barriers for the trial | shape = (500,) | dtype = int64
  Dataset /intervals/trials/num_targets (VectorData) The number of targets for the trial | shape = (500,) | dtype = int64
  Dataset /intervals/trials/rt (VectorData) Delay between go cue and movement onset | shape = (500,) | dtype = int64
  Dataset /intervals/trials/split (VectorData) Trial split that the trial belongs to for the Neural Latents Benchmark. Can be "train", "val", "test", or "none" | shape = (500,) | dtype = object
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (500,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (500,) | dtype = float64
  Dataset /intervals/trials/success (VectorData) If the monkey was successful on the trial. In these benchmark files, all unsuccessful trials have been removed | shape = (500,) | dtype = bool
  Dataset /intervals/trials/target_on_time (VectorData) Time of target presentation, as detected by the photobox | shape = (500,) | dtype = float64
  Dataset /intervals/trials/target_pos (VectorData) Array with rows containing x and y coordinates of target location, respectively, for each target | shape = (840, 2) | dtype = int16
  Dataset /intervals/trials/target_pos_index (VectorIndex) Index for VectorData 'target_pos' | shape = (500,) | dtype = uint16
  Dataset /intervals/trials/trial_type (VectorData) A number representing the maze configuration that was used for the trial | shape = (500,) | dtype = int64
  Dataset /intervals/trials/trial_version (VectorData) A number 0-2 indicating which variant of the maze is presented. 0 is 1-target no-barrier, 1 is 1-target with barriers, 2 is 3-target with barriers | shape = (500,) | dtype = int64
  Group /processing/behavior (ProcessingModule) Processed behavioral data
  Group /processing/behavior/cursor_pos (SpatialSeries) Cursor position in mm. First column x, second column y
  Group /processing/behavior/eye_pos (SpatialSeries) Monkey eye position in mm. First column x, second column y
  Group /processing/behavior/hand_pos (SpatialSeries) Monkey hand position in mm. First column x, second column y
  Group /processing/behavior/hand_vel (TimeSeries) Monkey hand velocity in mm/s, calculated from monkey hand position. First column x, second column y
  session_description: Data from monkey Jenkins performing center-out delayed reaching task. This file contains trials from the full session on 2009-10-06 that can be used for training models for the Neural Latents Benchmark.
  session_start_time: 2009-10-06T00:00:00-07:00
  timestamps_reference_time: 2009-10-06T00:00:00-07:00
  Group /units (Units) data on spiking units
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (162,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex) Index for VectorData 'electrodes' | shape = (162,) | dtype = uint8
  Dataset /units/heldout (VectorData) Whether the unit is held out in the test data (True) or not (False) in the Neural Latents Benchmark | shape = (162,) | dtype = bool
  Dataset /units/id (ElementIdentifiers)  | shape = (162,) | dtype = int64
  Dataset /units/obs_intervals (VectorData) the observation intervals for each unit | shape = (81000, 2) | dtype = float64
  Dataset /units/obs_intervals_index (VectorIndex) Index for VectorData 'obs_intervals' | shape = (162,) | dtype = uint32
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (916892,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (162,) | dtype = uint32
