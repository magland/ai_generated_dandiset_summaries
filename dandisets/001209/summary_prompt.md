
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001209/draft
name: FALCON Benchmark M1-B: primary motor cortex recordings in primate during reach-to-grasp task
contributor: [{'name': 'Karpowicz, Brianna', 'email': 'brianna.karpowicz@emory.edu', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': False}, {'name': 'Rouse, Adam G', 'roleName': ['dcite:DataCollector'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Schieber, Marc H', 'roleName': ['dcite:DataCollector'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'NIH NINDS', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'includeInCitation': False}]
description: This dataset contains multiunit spiking times and behavioral data from a macaque performing a reach-to-grasp task. The experimental task was a center-out reaching task with four different objects in eight possible positions. Neural activity was recorded from electrode arrays implanted in primary motor cortex (M1). Electromyographical (EMG) activity was simultaneously recorded from upper limb muscles. Provided as part of the FALCON Benchmark: https://snel-repo.github.io/falcon/ 

The datafile contains the following data in the acquisition fields: `preprocessed_emg` containing iEMG recordings from 16 muscles and `eval_mask` indicating within-trial periods used for evaluating performance in the FALCON Benchmark. Each datafile also includes spike times in the `units` field, and trial metadata for each reach and grasp (`gocue_time`, `move_onset_time`, `contact_time`, `reward_time`, `result`, `number`, `tgt_loc`, `tgt_obj`, `obj_id`, `condition_id`) in the `trials` field.

As part of the FALCON challenge, dataset files are released in three ways. The `held-in-calib` data includes many trials of data intended for calibration of decoders in the FALCON challenge. The `held-in-minival` data is a small subset of the `held-in-calib` data intended for FALCON models to validate submission format. Lastly, `held-out-calib` data are separate sessions of data from `held-in-calib`, but have much fewer trials, intended to be used for few-shot recalibration. Please bear in mind these factors if making use of this dataset for purposes outside of the FALCON Benchmark. Each dataset split is considered one "subject" by the DANDI repository; only data from one monkey is included.

Data from an additional monkey is available here: https://dandiarchive.org/dandiset/000941
assetsSummary: {'species': [{'name': 'Macaca mulatta - Rhesus monkey', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9544'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}, {'name': 'behavioral approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 233554359, 'numberOfFiles': 12, 'numberOfSubjects': 3, 'variableMeasured': ['BehavioralTimeSeries', 'Units', 'ElectrodeGroup'], 'measurementTechnique': [{'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 001209 has 12 NWB files.
12 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/eval_mask (TimeSeries) Timesteps to KEEP covariates (for training, eval).
  Group /acquisition/preprocessed_emg (BehavioralTimeSeries) 
  Group /acquisition/preprocessed_emg/APL (TimeSeries) no description
  Group /acquisition/preprocessed_emg/BCPs (TimeSeries) no description
  Group /acquisition/preprocessed_emg/DLTa (TimeSeries) no description
  Group /acquisition/preprocessed_emg/DLTp (TimeSeries) no description
  Group /acquisition/preprocessed_emg/ECRB (TimeSeries) no description
  Group /acquisition/preprocessed_emg/ECU (TimeSeries) no description
  Group /acquisition/preprocessed_emg/EDC (TimeSeries) no description
  Group /acquisition/preprocessed_emg/FCR (TimeSeries) no description
  Group /acquisition/preprocessed_emg/FCU (TimeSeries) no description
  Group /acquisition/preprocessed_emg/FDI (TimeSeries) no description
  Group /acquisition/preprocessed_emg/FDPr (TimeSeries) no description
  Group /acquisition/preprocessed_emg/FDPu (TimeSeries) no description
  Group /acquisition/preprocessed_emg/Hypoth (TimeSeries) no description
  Group /acquisition/preprocessed_emg/PECmaj (TimeSeries) no description
  Group /acquisition/preprocessed_emg/TCPlat (TimeSeries) no description
  Group /acquisition/preprocessed_emg/Thenar (TimeSeries) no description
  file_create_date: ['2024-10-18T13:36:34.240539-04:00']
  Group /general/devices/floating microelectrode_array (Device) 16-electrode array
  experiment_description: reach-to-grasp center out
  experimenter: ['Dr. Adam Rouse']
  Group /general/extracellular_ephys/E_electrode_group (ElectrodeGroup) Electrodes in an implanted FMA array labeled E
  Group /general/extracellular_ephys/E_electrode_group/device (Device) 16-electrode array
  Group /general/extracellular_ephys/F_electrode_group (ElectrodeGroup) Electrodes in an implanted FMA array labeled F
  Group /general/extracellular_ephys/F_electrode_group/device (Device) 16-electrode array
  Group /general/extracellular_ephys/G_electrode_group (ElectrodeGroup) Electrodes in an implanted FMA array labeled G
  Group /general/extracellular_ephys/G_electrode_group/device (Device) 16-electrode array
  Group /general/extracellular_ephys/H_electrode_group (ElectrodeGroup) Electrodes in an implanted FMA array labeled H
  Group /general/extracellular_ephys/H_electrode_group/device (Device) 16-electrode array
  Group /general/extracellular_ephys/I_electrode_group (ElectrodeGroup) Electrodes in an implanted FMA array labeled I
  Group /general/extracellular_ephys/I_electrode_group/device (Device) 16-electrode array
  Group /general/extracellular_ephys/J_electrode_group (ElectrodeGroup) Electrodes in an implanted FMA array labeled J
  Group /general/extracellular_ephys/J_electrode_group/device (Device) 16-electrode array
  Group /general/extracellular_ephys/Z_electrode_group (ElectrodeGroup) Electrodes not labelled as belonging to any other group
  Group /general/extracellular_ephys/Z_electrode_group/device (Device) 16-electrode array
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering, including the filter name and frequency cutoffs | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (64,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the electrode, in ohms | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the position (+x is posterior) | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the position (+y is inferior) | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the position (+z is right) | shape = (64,) | dtype = float64
  institution: University of Kansas
  lab: Rouse
  Group /general/subject (Subject) 
  identifier: X_20121206_held_in_calib
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/condition_id (VectorData) generic integer id across all loc/obj conditions | shape = (395,) | dtype = int64
  Dataset /intervals/trials/contact_time (VectorData) timing of contact onset | shape = (395,) | dtype = float64
  Dataset /intervals/trials/gocue_time (VectorData) timing of go cue | shape = (395,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (395,) | dtype = int64
  Dataset /intervals/trials/move_onset_time (VectorData) timing of move onset | shape = (395,) | dtype = float64
  Dataset /intervals/trials/number (VectorData) trial number in rouse dataset | shape = (395,) | dtype = uint16
  Dataset /intervals/trials/obj_id (VectorData) integer id for each object | shape = (395,) | dtype = int64
  Dataset /intervals/trials/result (VectorData) outcome of trial (success/failure/abort) | shape = (395,) | dtype = object
  Dataset /intervals/trials/reward_time (VectorData) timing of reward | shape = (395,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (395,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (395,) | dtype = float64
  Dataset /intervals/trials/tgt_loc (VectorData) location of target (angle) | shape = (395,) | dtype = float64
  Dataset /intervals/trials/tgt_obj (VectorData) object to grasp at target | shape = (395,) | dtype = object
  session_description: monkey performing reach-to-grasp task
  session_start_time: 2012-12-06T00:00:00-06:00
  timestamps_reference_time: 2012-12-06T00:00:00-06:00
  Group /units (Units) Sampled at 30 kHz with anti-alias
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (64,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex) Index for VectorData 'electrodes' | shape = (64,) | dtype = uint8
  Dataset /units/id (ElementIdentifiers)  | shape = (64,) | dtype = int64
  Dataset /units/obs_intervals (VectorData) the observation intervals for each unit | shape = (64, 2) | dtype = float64
  Dataset /units/obs_intervals_index (VectorIndex) Index for VectorData 'obs_intervals' | shape = (64,) | dtype = uint8
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (1398145,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (64,) | dtype = uint32
