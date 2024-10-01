
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000953/draft
name: FALCON Benchmark M2: primary motor cortex recordings in primate during finger movement
contributor: [{'name': 'Samuel R Nason-Tomaszewski', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-7127-0986', 'includeInCitation': True}, {'name': 'Matthew J. Mender', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-9671-7051', 'includeInCitation': True}, {'name': 'Cynthia Chestek', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-9671-7051', 'includeInCitation': True}, {'name': 'Joel Ye', 'email': 'joelye9@gmail.com', 'roleName': ['dcite:DataCurator'], 'schemaKey': 'Person', 'identifier': '0000-0002-1149-6035', 'includeInCitation': False}]
description: This dataset contains multiunit spiking times and behavioral data from a macaque in a finger movement task. The experimental task was to move two finger groups according to targets cued on a screen. Neural activity was recorded from electrode arrays implanted in primary motor cortex (M1). Finger positions as recorded by the manipulandum state, and normalized between full flexion and full extension, are provided. 

This dataset is part of the FALCON benchmark: https://snel-repo.github.io/falcon. The datafile contains the following data in the acquisition fields: 2D kinematics (`finger_vel`) and metadata for FALCON evaluation (`eval_mask`). The datafile also contains multi-unit spiking activity in the `units` field.

As part of the FALCON challenge, dataset files are released in three ways. The held-in-calib data includes many trials of data intended for calibration of decoders in the FALCON challenge. The held-in-minival data is a small subset of the held-in-calib data intended for FALCON models to validate submission format. Lastly, held-out-calib data are separate sessions of data from held-in-calib, but have much fewer trials, intended to be used for few-shot recalibration. Please bear in mind these factors if making use of this dataset for purposes outside of the FALCON Benchmark. Each dataset split is considered one "subject" by the DANDI repository; only data from one monkey is included.
assetsSummary: {'species': [{'name': 'Macaca mulatta - Rhesus monkey', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9544'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}, {'name': 'behavioral approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 22404212, 'numberOfFiles': 20, 'numberOfSubjects': 3, 'variableMeasured': ['Units', 'ElectrodeGroup', 'BehavioralTimeSeries'], 'measurementTechnique': [{'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000953 has 20 NWB files.
20 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/eval_mask (TimeSeries) Timesteps to keep covariates (for training, eval).
  Group /acquisition/finger_pos (BehavioralTimeSeries) 
  Group /acquisition/finger_pos/index (TimeSeries) no description
  Group /acquisition/finger_pos/mrs (TimeSeries) no description
  Group /acquisition/finger_vel (BehavioralTimeSeries) 
  Group /acquisition/finger_vel/index (TimeSeries) no description
  Group /acquisition/finger_vel/mrs (TimeSeries) no description
  file_create_date: ['2024-04-17T11:49:17.196303-04:00']
  Group /general/devices/Blackrock Utah Array (Device) 2x64-channel array, 96 active
  experiment_description: Two finger group movement in NHP. Behavior provided in 20ms bins, observation interval at trial ends may include a bit of neural data from partial bin.
  experimenter: ['Samuel R. Nason-Tomaszewski and Matthew J. Mender']
  Group /general/extracellular_ephys/M1_array (ElectrodeGroup) Hand area 2x64-channel array (96 active channels in recording system)
  Group /general/extracellular_ephys/M1_array/device (Device) 2x64-channel array, 96 active
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering, including the filter name and frequency cutoffs | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (96,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the electrode, in ohms | shape = (96,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the position (+x is posterior) | shape = (96,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the position (+y is inferior) | shape = (96,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the position (+z is right) | shape = (96,) | dtype = float64
  institution: University of Michigan
  lab: Chestek Lab
  session_id: 2020-10-19_Run1
  Group /general/subject (Subject) 
  identifier: MonkeyN_10-19-13:00_held_in
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (337,) | dtype = int64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (337,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (337,) | dtype = float64
  Dataset /intervals/trials/tgt_loc (VectorData) location of target (0-1 AU) | shape = (337, 2) | dtype = float32
  Dataset /intervals/trials/trial_num (VectorData) trial number as in experiment | shape = (337,) | dtype = int64
  session_description: M2 data
  session_start_time: 2020-10-19T13:00:00-04:00
  timestamps_reference_time: 2020-10-19T13:00:00-04:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (96,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex) Index for VectorData 'electrodes' | shape = (96,) | dtype = uint8
  Dataset /units/id (ElementIdentifiers)  | shape = (96,) | dtype = int64
  Dataset /units/obs_intervals (VectorData) the observation intervals for each unit | shape = (96, 2) | dtype = float64
  Dataset /units/obs_intervals_index (VectorIndex) Index for VectorData 'obs_intervals' | shape = (96,) | dtype = uint8
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (202939,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (96,) | dtype = uint32
