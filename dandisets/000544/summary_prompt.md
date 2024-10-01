
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000544/0.230514.1148
name: Test Dataset
contributor: [{'name': 'Bakshi, Kushal', 'email': 'kushal.bakshi@datajoint.com', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}]
description: Test dataset for DataJoint uploads to DANDI
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}, {'name': 'behavioral approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 485784554, 'numberOfFiles': 1, 'numberOfSubjects': 1, 'variableMeasured': ['BehavioralEvents', 'BehavioralTimeSeries', 'Units', 'ElectrodeGroup'], 'measurementTechnique': [{'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000544 has 1 NWB files.
1 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/BehavioralEvents (BehavioralEvents) 
  Group /acquisition/BehavioralEvents/delay_start_times (TimeSeries) Timestamps for event type: delay - Start Time
  Group /acquisition/BehavioralEvents/delay_stop_times (TimeSeries) Timestamps for event type: delay - Stop Time
  Group /acquisition/BehavioralEvents/go_start_times (TimeSeries) Timestamps for event type: go - Start Time
  Group /acquisition/BehavioralEvents/go_stop_times (TimeSeries) Timestamps for event type: go - Stop Time
  Group /acquisition/BehavioralEvents/left_lick_times (TimeSeries) Timestamps for event type: left lick
  Group /acquisition/BehavioralEvents/photostim_start_times (TimeSeries) Timestamps of the photo-stimulation and the corresponding powers (in mW) being applied
  Group /acquisition/BehavioralEvents/photostim_stop_times (TimeSeries) Timestamps of the photo-stimulation being switched off
  Group /acquisition/BehavioralEvents/presample_start_times (TimeSeries) Timestamps for event type: presample - Start Time
  Group /acquisition/BehavioralEvents/presample_stop_times (TimeSeries) Timestamps for event type: presample - Stop Time
  Group /acquisition/BehavioralEvents/right_lick_times (TimeSeries) Timestamps for event type: right lick
  Group /acquisition/BehavioralEvents/sample_start_times (TimeSeries) Timestamps for event type: sample - Start Time
  Group /acquisition/BehavioralEvents/sample_stop_times (TimeSeries) Timestamps for event type: sample - Stop Time
  Group /acquisition/BehavioralEvents/trialend_start_times (TimeSeries) Timestamps for event type: trialend - Start Time
  Group /acquisition/BehavioralEvents/trialend_stop_times (TimeSeries) Timestamps for event type: trialend - Stop Time
  Group /acquisition/BehavioralTimeSeries (BehavioralTimeSeries) 
  Group /acquisition/BehavioralTimeSeries/Camera0_side_JawTracking (TimeSeries) Time series for JawTracking position: ('jaw_x', 'jaw_y', 'jaw_likelihood')
  Group /acquisition/BehavioralTimeSeries/Camera0_side_NoseTracking (TimeSeries) Time series for NoseTracking position: ('nose_x', 'nose_y', 'nose_likelihood')
  Group /acquisition/BehavioralTimeSeries/Camera0_side_TongueTracking (TimeSeries) Time series for TongueTracking position: ('tongue_x', 'tongue_y', 'tongue_likelihood')
  file_create_date: ['2023-02-13T12:22:02.746406-06:00']
  data_collection: 
  Group /general/devices/18005123392 (neuropixels 1.0 - 3B) (Device) neuropixels 1.0 - 3B
  Group /general/devices/18005123682 (neuropixels 1.0 - 3B) (Device) neuropixels 1.0 - 3B
  Group /general/devices/19011111614 (neuropixels 2.0 - SS) (Device) neuropixels 2.0 - SS
  Group /general/devices/19122511894 (neuropixels 2.0 - SS) (Device) neuropixels 2.0 - SS
  Group /general/devices/OBIS470 (Device) 
  experiment_description: high tone vs. low tone
  experimenter: ['susu']
  Group /general/extracellular_ephys/18005123392 1-384 (ElectrodeGroup) {"probe": "18005123392", "probe_type": "neuropixels 1.0 - 3B", "electrode_config_name": "1-384", "subject_id": 484677, "session": 25, "insertion_number": 4, "probe_comment": "", "electrode_config_hash": "4ae1f6ed4687467836d43369e548fe00"}
  Group /general/extracellular_ephys/18005123392 1-384/device (Device) neuropixels 1.0 - 3B
  Group /general/extracellular_ephys/18005123682 1-384 (ElectrodeGroup) {"probe": "18005123682", "probe_type": "neuropixels 1.0 - 3B", "electrode_config_name": "1-384", "subject_id": 484677, "session": 25, "insertion_number": 3, "probe_comment": "", "electrode_config_hash": "4ae1f6ed4687467836d43369e548fe00"}
  Group /general/extracellular_ephys/18005123682 1-384/device (Device) neuropixels 1.0 - 3B
  Group /general/extracellular_ephys/19011111614 1-384 (ElectrodeGroup) {"probe": "19011111614", "probe_type": "neuropixels 2.0 - SS", "electrode_config_name": "1-384", "subject_id": 484677, "session": 25, "insertion_number": 1, "probe_comment": "", "electrode_config_hash": "d762114f2ff79a615ab6d34c71519e72"}
  Group /general/extracellular_ephys/19011111614 1-384/device (Device) neuropixels 2.0 - SS
  Group /general/extracellular_ephys/19122511894 1-384 (ElectrodeGroup) {"probe": "19122511894", "probe_type": "neuropixels 2.0 - SS", "electrode_config_name": "1-384", "subject_id": 484677, "session": 25, "insertion_number": 2, "probe_comment": "", "electrode_config_hash": "d762114f2ff79a615ab6d34c71519e72"}
  Group /general/extracellular_ephys/19122511894 1-384/device (Device) neuropixels 2.0 - SS
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/electrode (VectorData) electrode index, starts at 0 | shape = (1536,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering, including the filter name and frequency cutoffs | shape = (1536,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (1536,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (1536,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (1536,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the electrode, in ohms | shape = (1536,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (1536,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/rel_x (VectorData) the x coordinate within the electrode group | shape = (1536,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_y (VectorData) the y coordinate within the electrode group | shape = (1536,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_z (VectorData) the z coordinate within the electrode group | shape = (1536,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/shank (VectorData) shank index, starts at 0, advance left to right | shape = (1536,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/shank_col (VectorData) column index, starts at 0, advance left to right | shape = (1536,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/shank_row (VectorData) row index, starts at 0, advance tip to tail | shape = (1536,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the position (+x is posterior) | shape = (1536,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the position (+y is inferior) | shape = (1536,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the position (+z is right) | shape = (1536,) | dtype = float64
  institution: Janelia Research Campus
  keywords: ['electrophysiology']
  Group /general/optogenetics/OBIS470_4 (OptogeneticStimulusSite) 
  Group /general/optogenetics/OBIS470_4/device (Device) 
  Group /general/optogenetics/OBIS470_5 (OptogeneticStimulusSite) 
  Group /general/optogenetics/OBIS470_5/device (Device) 
  Group /general/optogenetics/OBIS470_6 (OptogeneticStimulusSite) 
  Group /general/optogenetics/OBIS470_6/device (Device) 
  related_publications: ['']
  Group /general/subject (Subject) 
  identifier: SC067_20210415_161621_s25
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/auto_water (VectorData)  | shape = (520,) | dtype = int32
  Dataset /intervals/trials/early_lick (VectorData)  | shape = (520,) | dtype = object
  Dataset /intervals/trials/free_water (VectorData)  | shape = (520,) | dtype = int32
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (520,) | dtype = int32
  Dataset /intervals/trials/outcome (VectorData)  | shape = (520,) | dtype = object
  Dataset /intervals/trials/photostim_duration (VectorData) calculated attribute | shape = (520,) | dtype = object
  Dataset /intervals/trials/photostim_onset (VectorData) calculated attribute | shape = (520,) | dtype = object
  Dataset /intervals/trials/photostim_power (VectorData) calculated attribute | shape = (520,) | dtype = object
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (520,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (520,) | dtype = float64
  Dataset /intervals/trials/task (VectorData) task type | shape = (520,) | dtype = object
  Dataset /intervals/trials/task_protocol (VectorData) task protocol | shape = (520,) | dtype = int32
  Dataset /intervals/trials/trial (VectorData) trial number (1-based indexing) | shape = (520,) | dtype = int32
  Dataset /intervals/trials/trial_instruction (VectorData)  | shape = (520,) | dtype = object
  Dataset /intervals/trials/trial_uid (VectorData) unique across sessions/animals | shape = (520,) | dtype = int32
  session_description: 
  session_start_time: 2021-04-15T16:16:21-05:00
  timestamps_reference_time: 2021-04-15T16:16:21-05:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/amplitude_cutoff (VectorData) Estimate of miss rate based on amplitude histogram | shape = (1441,) | dtype = float64
  Dataset /units/avg_firing_rate (VectorData) (Hz) | shape = (1441,) | dtype = float64
  Dataset /units/cumulative_drift (VectorData) Cumulative change in spike depth throughout recording | shape = (1441,) | dtype = float64
  Dataset /units/d_prime (VectorData) Classification accuracy based on LDA | shape = (1441,) | dtype = float64
  Dataset /units/drift_metric (VectorData)  | shape = (1441,) | dtype = float64
  Dataset /units/duration (VectorData)  | shape = (1441,) | dtype = float64
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (1441,) | dtype = object
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (1441,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex) Index for VectorData 'electrodes' | shape = (1441,) | dtype = uint16
  Dataset /units/halfwidth (VectorData)  | shape = (1441,) | dtype = float64
  Dataset /units/id (ElementIdentifiers)  | shape = (1441,) | dtype = int32
  Dataset /units/isi_violation (VectorData)  | shape = (1441,) | dtype = float64
  Dataset /units/isolation_distance (VectorData) Distance to nearest cluster in Mahalanobis space | shape = (1441,) | dtype = float64
  Dataset /units/l_ratio (VectorData)  | shape = (1441,) | dtype = float64
  Dataset /units/max_drift (VectorData) Maximum change in spike depth throughout recording | shape = (1441,) | dtype = float64
  Dataset /units/nn_hit_rate (VectorData)  | shape = (1441,) | dtype = float64
  Dataset /units/nn_miss_rate (VectorData)  | shape = (1441,) | dtype = float64
  Dataset /units/obs_intervals (VectorData) the observation intervals for each unit | shape = (749320, 2) | dtype = float64
  Dataset /units/obs_intervals_index (VectorIndex) Index for VectorData 'obs_intervals' | shape = (1441,) | dtype = uint32
  Dataset /units/presence_ratio (VectorData) Fraction of epoch in which spikes are present | shape = (1441,) | dtype = float64
  Dataset /units/pt_ratio (VectorData)  | shape = (1441,) | dtype = float64
  Dataset /units/recovery_slope (VectorData)  | shape = (1441,) | dtype = float64
  Dataset /units/repolarization_slope (VectorData)  | shape = (1441,) | dtype = float64
  Dataset /units/sampling_rate (VectorData) (Hz) | shape = (1441,) | dtype = int32
  Dataset /units/silhouette_score (VectorData) Standard metric for cluster overlap | shape = (1441,) | dtype = float64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (46889816,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (1441,) | dtype = uint32
  Dataset /units/spread (VectorData)  | shape = (1441,) | dtype = float64
  Dataset /units/unit (VectorData)  | shape = (1441,) | dtype = int32
  Dataset /units/unit_amp (VectorData)  | shape = (1441,) | dtype = float64
  Dataset /units/unit_posx (VectorData) (um) estimated x position of the unit relative to probe's tip (0,0) | shape = (1441,) | dtype = float64
  Dataset /units/unit_posy (VectorData) (um) estimated y position of the unit relative to probe's tip (0,0) | shape = (1441,) | dtype = float64
  Dataset /units/unit_quality (VectorData)  | shape = (1441,) | dtype = object
  Dataset /units/unit_snr (VectorData)  | shape = (1441,) | dtype = float64
  Dataset /units/velocity_above (VectorData)  | shape = (1441,) | dtype = float64
  Dataset /units/velocity_below (VectorData)  | shape = (1441,) | dtype = float64
  Dataset /units/waveform_mean (VectorData) the spike waveform mean for each spike unit | shape = (1441, 82) | dtype = float64
  Dataset /units/waveform_sd (VectorData) the spike waveform standard deviation for each spike unit | shape = (1441, 1) | dtype = float64
