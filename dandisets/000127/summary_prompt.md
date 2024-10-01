
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000127/0.220113.0359
name: Area2_Bump: macaque somatosensory area 2 spiking activity during reaching with perturbations
contributor: [{'name': 'Pei, Felix', 'email': 'felp8484@gmail.com', 'roleName': ['dcite:ContactPerson', 'dcite:Maintainer'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': False}, {'name': 'Chowdhury, Raeed', 'roleName': ['dcite:DataCollector'], 'schemaKey': 'Person', 'identifier': '0000-0002-5934-919X', 'affiliation': [{'name': 'University of Pittsburgh', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/01an3r305'}], 'includeInCitation': True}, {'name': 'Miller, Lee', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0001-8675-7140', 'affiliation': [{'name': 'Northwestern University', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/000e0be47'}], 'includeInCitation': True}]
description: This dataset contains sorted unit spiking times and behavioral data from a macaque performing a reaching task with perturbations. In the experimental task, the subject performed delayed center-out reaches using a manipulandum to control a cursor. On a portion of the trials, the manipulandum applied a bump during the center hold prior to the reach. Neural activity was recorded from an electrode array implanted in somatosensory area 2. Hand position, cursor position, force applied to the manipulandum, length and velocity of various arm muscles, and angle and velocity of various arm joints were all recorded during the experiment. Provided as part of the Neural Latents Benchmark: https://neurallatents.github.io.
assetsSummary: {'species': [{'name': 'Rhesus monkey', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9544'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}, {'name': 'behavioral approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 1823368810, 'numberOfFiles': 2, 'numberOfSubjects': 1, 'variableMeasured': ['ElectrodeGroup', 'Units', 'SpatialSeries', 'ProcessingModule'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000127 has 2 NWB files.
1 of these NWB files are of type 1.
1 of these NWB files are of type 2.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2021-09-01T21:40:43.149091-04:00']
  Group /general/devices/electrode_array (Device) 96-electrode Utah array
  experiment_description: Center out reaching task with perturbations during center hold period before reach
  experimenter: ['Raeed H. Chowdhury']
  Group /general/extracellular_ephys/electrode_group (ElectrodeGroup) Electrodes in an implanted Utah array
  Group /general/extracellular_ephys/electrode_group/device (Device) 96-electrode Utah array
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (96,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (96,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (96,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (96,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (96,) | dtype = float64
  institution: Northwestern University
  keywords: ['somatosensory cortex' 'reaching' 'macaque' 'Neural Latents Benchmark']
  lab: Miller
  related_publications: ['https://doi.org/10.7554/eLife.48198']
  session_id: 20171207
  Group /general/subject (Subject) 
  identifier: c942902c-0b8e-11ec-b9b7-0bfeb2c344ea
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (98,) | dtype = int64
  Dataset /intervals/trials/move_onset_time (VectorData) Time of move onset around bump for passive trials and after go cue for active trials | shape = (98,) | dtype = float64
  Dataset /intervals/trials/split (VectorData) Trial split that the trial belongs to for the Neural Latents Benchmark. Can be "train", "val", "test", or "none" | shape = (98,) | dtype = object
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (98,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (98,) | dtype = float64
  session_description: Data from monkey Han performing center-out active-passive task. This file contains segments of trials from the full session on 2017-12-07 that are to be used for evaluating models for the Neural Latents Benchmark.
  session_start_time: 2017-12-07T17:06:09.727000-05:00
  timestamps_reference_time: 2017-12-07T17:06:09.727000-05:00
  Group /units (Units) data on spiking units
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (49,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex) Index for VectorData 'electrodes' | shape = (49,) | dtype = uint8
  Dataset /units/heldout (VectorData) Whether the unit is held out in the test data (True) or not (False) in the Neural Latents Benchmark | shape = (49,) | dtype = bool
  Dataset /units/id (ElementIdentifiers)  | shape = (49,) | dtype = int64
  Dataset /units/obs_intervals (VectorData) the observation intervals for each unit | shape = (4802, 2) | dtype = float64
  Dataset /units/obs_intervals_index (VectorIndex) Index for VectorData 'obs_intervals' | shape = (49,) | dtype = uint16
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (22263,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (49,) | dtype = uint16


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2021-09-01T21:40:32.929476-04:00']
  Group /general/devices/electrode_array (Device) 96-electrode Utah array
  experiment_description: Center out reaching task with perturbations during center hold period before reach
  experimenter: ['Raeed H. Chowdhury']
  Group /general/extracellular_ephys/electrode_group (ElectrodeGroup) Electrodes in an implanted Utah array
  Group /general/extracellular_ephys/electrode_group/device (Device) 96-electrode Utah array
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (96,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (96,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (96,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (96,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (96,) | dtype = float64
  institution: Northwestern University
  keywords: ['somatosensory cortex' 'reaching' 'macaque' 'Neural Latents Benchmark']
  lab: Miller
  related_publications: ['https://doi.org/10.7554/eLife.48198']
  session_id: 20171207
  Group /general/subject (Subject) 
  identifier: c32b334c-0b8e-11ec-b9b7-0bfeb2c344ea
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/bump_dir (VectorData) Angle (in degrees) of bump direction, if there was one. 0 degrees is directly to the right, and 90 degrees is directly upward | shape = (826,) | dtype = float64
  Dataset /intervals/trials/bump_time (VectorData) Time of bump delivery, if there was one | shape = (826,) | dtype = float64
  Dataset /intervals/trials/cond_dir (VectorData) Direction of bump for passive trials and target direction for active trials, for convenience when filtering trials | shape = (826,) | dtype = float64
  Dataset /intervals/trials/ctr_hold (VectorData) Required hold time on center before reach, in seconds | shape = (826,) | dtype = float64
  Dataset /intervals/trials/ctr_hold_bump (VectorData) Whether there was bump during center hold | shape = (826,) | dtype = bool
  Dataset /intervals/trials/go_cue_time (VectorData) Time of go cue delivery | shape = (826,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (826,) | dtype = int64
  Dataset /intervals/trials/move_onset_time (VectorData) Time of move onset around bump for passive trials and after go cue for active trials | shape = (826,) | dtype = float64
  Dataset /intervals/trials/result (VectorData) Result of the trial, either 'R' (reward), 'A' (abort), 'I' (incomplete) or 'F' (fail) | shape = (826,) | dtype = object
  Dataset /intervals/trials/split (VectorData) Trial split that the trial belongs to for the Neural Latents Benchmark. Can be "train", "val", "test", or "none" | shape = (826,) | dtype = object
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (826,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (826,) | dtype = float64
  Dataset /intervals/trials/target_dir (VectorData) Direction of target, in degrees. 0 degrees is directly to the right, and 90 degrees is directly upward | shape = (826,) | dtype = float64
  Dataset /intervals/trials/target_on_time (VectorData) Time of target presentation | shape = (826,) | dtype = float64
  Group /processing/behavior (ProcessingModule) Processed behavioral data
  Group /processing/behavior/force (TimeSeries) Interface forces and torques between the hand and the manipulandum handle, in Newtons or Newton-meters. First three columns are forces in X, Y, and Z directions, respectively, and last three columns are X, Y, and Z moments, respectively. Sampled at 1 kHz
  Group /processing/behavior/hand_pos (SpatialSeries) Hand position in Cartesian coordinates, in cm. First column is x coordinate, second column is y coordinate. Sampled at 1 kHz, low-pass filtered at 100 Hz cutoff
  Group /processing/behavior/hand_vel (TimeSeries) Hand velocity, in cm/s. First column is x direction, second column is y direction. Sampled at 1 kHz, low-pass filtered at 100 Hz cutoff
  Group /processing/behavior/joint_ang (TimeSeries) Angle of monkey arm joints in degrees, calculated from motion tracking data
  Group /processing/behavior/joint_vel (TimeSeries) Velocity of monkey arm joints in degrees/s, calculated from motion tracking data
  Group /processing/behavior/muscle_len (TimeSeries) Length of various monkey arm muscles in m, calculated from motion tracking data
  Group /processing/behavior/muscle_vel (TimeSeries) Velocity of various monkey arm muscles in m/s, calculated from motion tracking data
  session_description: Data from monkey Han performing center-out active-passive task. This file contains several continuous segments of the full session on 2017-12-07 that can be used for training models for the Neural Latents Benchmark.
  session_start_time: 2017-12-07T17:06:09.727000-05:00
  timestamps_reference_time: 2017-12-07T17:06:09.727000-05:00
  Group /units (Units) data on spiking units
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (65,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex) Index for VectorData 'electrodes' | shape = (65,) | dtype = uint8
  Dataset /units/heldout (VectorData) Whether the unit is held out in the test data (True) or not (False) in the Neural Latents Benchmark | shape = (65,) | dtype = bool
  Dataset /units/id (ElementIdentifiers)  | shape = (65,) | dtype = int64
  Dataset /units/obs_intervals (VectorData) the observation intervals for each unit | shape = (260, 2) | dtype = float64
  Dataset /units/obs_intervals_index (VectorIndex) Index for VectorData 'obs_intervals' | shape = (65,) | dtype = uint16
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (1017465,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (65,) | dtype = uint32
