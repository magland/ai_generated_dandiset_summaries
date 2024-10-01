
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000458/0.230317.0039
name: Simultaneous electroencephalography, extracellular electrophysiology, and cortical electrical stimulation in head-fixed mice
contributor: [{'name': 'Claar, Leslie D', 'email': 'lesliec@alleninstitute.org', 'roleName': ['dcite:ContactPerson', 'dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-4030-9171', 'affiliation': [{'name': 'Allen Institute', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/03cpe7c52'}], 'includeInCitation': True}, {'name': 'Rembado, Irene', 'email': 'irene.rembado@alleninstitute.org', 'roleName': ['dcite:Author', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [{'name': 'Allen Institute', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/03cpe7c52'}], 'includeInCitation': True}, {'name': 'Kuyat, Jacqulyn R', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [{'name': 'Allen Institute', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/03cpe7c52'}], 'includeInCitation': True}, {'name': 'Russo, Simone', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [{'name': 'Allen Institute', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/03cpe7c52'}], 'includeInCitation': True}, {'name': 'Marks, Lydia C', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [{'name': 'Allen Institute', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/03cpe7c52'}], 'includeInCitation': True}, {'name': 'Olsen, Shawn R', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [{'name': 'Allen Institute', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/03cpe7c52'}], 'includeInCitation': True}, {'name': 'Koch, Christof', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [{'name': 'Allen Institute', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/03cpe7c52'}], 'includeInCitation': True}, {'url': 'https://www.tinybluedotfoundation.org/', 'name': 'Tiny Blue Dot Foundation', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'contactPoint': [], 'includeInCitation': False}, {'url': 'https://alleninstitute.org/', 'name': 'Allen Institute', 'roleName': ['dcite:Sponsor', 'dcite:Affiliation'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/03cpe7c52', 'contactPoint': [{'schemaKey': 'ContactPoint'}], 'includeInCitation': False}]
description: In this set of experiments, we recorded neural signals using an electroencephalography (EEG) array and Neuropixels probes while directly electrically stimulating the cortex in awake and anesthetized head-fixed mice. Details of the experiments can be found in the associated manuscript (Claar, Rembado et al., 2023). Briefly, the recordings and stimulation commenced while the mouse was awake, free to rest or move on a rotating disc. After delivering a series of stimuli, anesthesia was induced with isoflurane (5% via inhalation). Once a surgical level of anesthesia was reached, the mouse was maintained unconscious (1-1.5% isoflurane) during the delivery of another series of stimuli. In some subjects another series of stimuli was delivered after the isoflurane was turned off, this epoch/state is referred to as “recovery” in the dataset.

Each session file includes the following data: raw EEG signals from all 30 surface electrodes and the associated electrode information; raw LFP signals from all electrodes on all Neuropixels probes (if used) and the associated electrode information; spike times for all units (spike sorted with Kilosort 2.0) that passed our quality threshold with associated information (brain region, spike waveform duration, etc.); subject’s speed computed from the rotation of the disc for the entire session; epochs marking when isoflurane was induced and when it was maintained; and a trial table containing information about every stimulus delivered throughout the session.

All sessions included an awake and an isoflurane epoch, but not all sessions included a recovery epoch. Some subjects received visual stimulation trials (visual stimuli presented on a screen in the subject’s right field of view) interleaved with the electrical stimulation trials.
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}, {'name': 'behavioral approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 361482309556, 'numberOfFiles': 24, 'numberOfSubjects': 23, 'variableMeasured': ['BehavioralTimeSeries', 'Units', 'ElectricalSeries', 'ElectrodeGroup', 'LFP', 'ProcessingModule'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'signal filtering technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000458 has 24 NWB files.
6 of these NWB files are of type 1.
1 of these NWB files are of type 2.
4 of these NWB files are of type 3.
2 of these NWB files are of type 4.
11 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeriesEEG (ElectricalSeries) voltage measured over time and associated timestamps from EEG array
  Dataset /acquisition/ElectricalSeriesEEG/electrodes (DynamicTableRegion) EEG electrodes | shape = (30,) | dtype = int32
  file_create_date: ['2023-03-15T10:11:43.767364-07:00']
  Group /general/devices/EEG array (Device) H32 Mouse EEG (30-ch)
  experiment_description: in vivo electrophysiology in a head-fixed mouse during cortical electrical microstimulation
  experimenter: ['Claar, Leslie D' 'Rembado, Irene' 'Kuyat, Jacqulyn R' 'Russo, Simone'
   'Marks, Lydia C' 'Olsen, Shawn R' 'Koch, Christof']
  Group /general/extracellular_ephys/EEG array (ElectrodeGroup) 30-ch surface grid
  Group /general/extracellular_ephys/EEG array/device (Device) H32 Mouse EEG (30-ch)
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (30,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (30,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (30,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/is_data_valid (VectorData) True for electrodes/channels with usable data | shape = (30,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (30,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/probe_horizontal_position (VectorData) width-wise position of electrode/channel on device (microns) | shape = (30,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/probe_vertical_position (VectorData) length-wise position of electrode/channel on device (microns) | shape = (30,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/reference (VectorData) Description of the reference electrode and/or reference scheme used for this                         electrode, e.g.,"stainless steel skull screw" or "online common average referencing". | shape = (30,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the position (+x is posterior) | shape = (30,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the position (+y is inferior) | shape = (30,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the position (+z is right) | shape = (30,) | dtype = float64
  institution: Allen Institute
  keywords: ['EEG' 'Neuropixels' 'electrical stimulation' 'brain states'
   'cortico-thalamic interactions']
  related_publications: ['https://doi.org/10.7554/eLife.84630.1']
  session_id: 20200709
  stimulus: single pulse electrical stimuli targeted to MOs (superficial layers)
  Group /general/subject (Subject) 
  identifier: 521885-20200709-v001
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (2,) | dtype = int32
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (2,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (2,) | dtype = float64
  Dataset /intervals/epochs/tags (VectorData) user-defined tags | shape = (2,) | dtype = object
  Dataset /intervals/epochs/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (2,) | dtype = uint8
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/behavioral_epoch (VectorData) behavioral epoch when stimulus was delivered | shape = (360,) | dtype = object
  Dataset /intervals/trials/estim_current (VectorData) electrical stimulation current (μA), if applicable | shape = (360,) | dtype = object
  Dataset /intervals/trials/estim_target_depth (VectorData) electrical stimulation target depth (cortical layer), if applicable | shape = (360,) | dtype = object
  Dataset /intervals/trials/estim_target_region (VectorData) electrical stimulation target region, if applicable | shape = (360,) | dtype = object
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (360,) | dtype = int32
  Dataset /intervals/trials/is_running (VectorData) True if mouse is running during trial, running defined as average speed > 0 cm/s between [-0.5, 0.5] s from stimulus onset | shape = (360,) | dtype = bool
  Dataset /intervals/trials/is_valid (VectorData) True for valid trials, trials are invalid if they have large electrical artifacts or if electrical stimulation was off target | shape = (360,) | dtype = bool
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (360,) | dtype = float64
  Dataset /intervals/trials/stimulus_description (VectorData) more specific description of stimulus type | shape = (360,) | dtype = object
  Dataset /intervals/trials/stimulus_type (VectorData) type of stimulus delivered | shape = (360,) | dtype = object
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (360,) | dtype = float64
  Group /processing/behavior (ProcessingModule) processed behavioral data
  Group /processing/behavior/BehavioralTimeSeries (BehavioralTimeSeries) 
  Group /processing/behavior/BehavioralTimeSeries/running_speed (TimeSeries) running speed data, computed from wheel angular velocity
  session_description: EEG recording during wakefulness and isoflurane anesthesia
  session_start_time: 2020-07-09T14:17:02.725000-07:00
  timestamps_reference_time: 2020-07-09T14:17:02.725000-07:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeriesEEG (ElectricalSeries) voltage measured over time and associated timestamps from EEG array
  Dataset /acquisition/ElectricalSeriesEEG/electrodes (DynamicTableRegion) EEG electrodes | shape = (30,) | dtype = int32
  Group /acquisition/LFPprobeB (LFP) 
  Group /acquisition/LFPprobeB/ElectricalSeriesprobeB (ElectricalSeries) voltage measured over time and associated timestamps from NeuropixelsprobeB
  Dataset /acquisition/LFPprobeB/ElectricalSeriesprobeB/electrodes (DynamicTableRegion) probeB electrodes | shape = (384,) | dtype = int32
  Group /acquisition/LFPprobeC (LFP) 
  Group /acquisition/LFPprobeC/ElectricalSeriesprobeC (ElectricalSeries) voltage measured over time and associated timestamps from NeuropixelsprobeC
  Dataset /acquisition/LFPprobeC/ElectricalSeriesprobeC/electrodes (DynamicTableRegion) probeC electrodes | shape = (384,) | dtype = int32
  file_create_date: ['2023-03-15T10:15:49.719646-07:00']
  Group /general/devices/EEG array (Device) H32 Mouse EEG (30-ch)
  Group /general/devices/probeB (Device) Neuropixels 1.0 probe
  Group /general/devices/probeC (Device) Neuropixels 1.0 probe
  experiment_description: in vivo electrophysiology in a head-fixed mouse during cortical electrical microstimulation
  experimenter: ['Claar, Leslie D' 'Rembado, Irene' 'Kuyat, Jacqulyn R' 'Russo, Simone'
   'Marks, Lydia C' 'Olsen, Shawn R' 'Koch, Christof']
  Group /general/extracellular_ephys/EEG array (ElectrodeGroup) 30-ch surface grid
  Group /general/extracellular_ephys/EEG array/device (Device) H32 Mouse EEG (30-ch)
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (798,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (798,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (798,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/is_data_valid (VectorData) True for electrodes/channels with usable data | shape = (798,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (798,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/probe_horizontal_position (VectorData) width-wise position of electrode/channel on device (microns) | shape = (798,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/probe_vertical_position (VectorData) length-wise position of electrode/channel on device (microns) | shape = (798,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/reference (VectorData) Description of the reference electrode and/or reference scheme used for this                         electrode, e.g.,"stainless steel skull screw" or "online common average referencing". | shape = (798,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the position (+x is posterior) | shape = (798,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the position (+y is inferior) | shape = (798,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the position (+z is right) | shape = (798,) | dtype = float64
  Group /general/extracellular_ephys/probeB (ElectrodeGroup) Neuropixels probe B
  Group /general/extracellular_ephys/probeB/device (Device) Neuropixels 1.0 probe
  Group /general/extracellular_ephys/probeC (ElectrodeGroup) Neuropixels probe C
  Group /general/extracellular_ephys/probeC/device (Device) Neuropixels 1.0 probe
  institution: Allen Institute
  keywords: ['EEG' 'Neuropixels' 'electrical stimulation' 'brain states'
   'cortico-thalamic interactions']
  related_publications: ['https://doi.org/10.7554/eLife.84630.1']
  session_id: 20201023
  stimulus: single pulse electrical stimuli targeted to MOs (deep layers)
  Group /general/subject (Subject) 
  identifier: 546655-20201023-v001
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (2,) | dtype = int32
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (2,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (2,) | dtype = float64
  Dataset /intervals/epochs/tags (VectorData) user-defined tags | shape = (2,) | dtype = object
  Dataset /intervals/epochs/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (2,) | dtype = uint8
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/behavioral_epoch (VectorData) behavioral epoch when stimulus was delivered | shape = (1459,) | dtype = object
  Dataset /intervals/trials/estim_current (VectorData) electrical stimulation current (μA), if applicable | shape = (1459,) | dtype = object
  Dataset /intervals/trials/estim_target_depth (VectorData) electrical stimulation target depth (cortical layer), if applicable | shape = (1459,) | dtype = object
  Dataset /intervals/trials/estim_target_region (VectorData) electrical stimulation target region, if applicable | shape = (1459,) | dtype = object
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (1459,) | dtype = int32
  Dataset /intervals/trials/is_running (VectorData) True if mouse is running during trial, running defined as average speed > 0 cm/s between [-0.5, 0.5] s from stimulus onset | shape = (1459,) | dtype = bool
  Dataset /intervals/trials/is_valid (VectorData) True for valid trials, trials are invalid if they have large electrical artifacts or if electrical stimulation was off target | shape = (1459,) | dtype = bool
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (1459,) | dtype = float64
  Dataset /intervals/trials/stimulus_description (VectorData) more specific description of stimulus type | shape = (1459,) | dtype = object
  Dataset /intervals/trials/stimulus_type (VectorData) type of stimulus delivered | shape = (1459,) | dtype = object
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1459,) | dtype = float64
  Group /processing/behavior (ProcessingModule) processed behavioral data
  Group /processing/behavior/BehavioralTimeSeries (BehavioralTimeSeries) 
  Group /processing/behavior/BehavioralTimeSeries/running_speed (TimeSeries) running speed data, computed from wheel angular velocity
  session_description: EEG and Neuropixels recording during wakefulness and isoflurane anesthesia
  session_start_time: 2020-10-23T11:00:53.462000-07:00
  timestamps_reference_time: 2020-10-23T11:00:53.462000-07:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/amplitude_cutoff (VectorData) an estimate of the fraction of spikes below the spike detection threshold | shape = (265,) | dtype = float64
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (265,) | dtype = object
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (265,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex) Index for VectorData 'electrodes' | shape = (265,) | dtype = uint16
  Dataset /units/id (ElementIdentifiers)  | shape = (265,) | dtype = int32
  Dataset /units/isi_violations (VectorData) an estimate of the relative firing rate of hypothetical neurons generating inter-spike-interval violations | shape = (265,) | dtype = float64
  Dataset /units/location (VectorData) the location of unit within the brain (CCF acronym) | shape = (265,) | dtype = object
  Dataset /units/presence_ratio (VectorData) the fraction of time the unit was present during the experiment (ranges from 0 to 0.99) | shape = (265,) | dtype = float64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (7034400,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (265,) | dtype = uint32
  Dataset /units/waveform_duration (VectorData) the mean duration (s) of detected spiking events | shape = (265,) | dtype = float64
  Dataset /units/waveform_mean (VectorData) the spike waveform mean for each spike unit | shape = (265, 82) | dtype = float64
  Dataset /units/x (VectorData) the x coordinate of the position (CCF, +x is posterior) | shape = (265,) | dtype = float64
  Dataset /units/y (VectorData) the y coordinate of the position (CCF, +y is inferior) | shape = (265,) | dtype = float64
  Dataset /units/z (VectorData) the z coordinate of the position (CCF, +z is right) | shape = (265,) | dtype = float64


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeriesEEG (ElectricalSeries) voltage measured over time and associated timestamps from EEG array
  Dataset /acquisition/ElectricalSeriesEEG/electrodes (DynamicTableRegion) EEG electrodes | shape = (30,) | dtype = int32
  Group /acquisition/LFPprobeB (LFP) 
  Group /acquisition/LFPprobeB/ElectricalSeriesprobeB (ElectricalSeries) voltage measured over time and associated timestamps from NeuropixelsprobeB
  Dataset /acquisition/LFPprobeB/ElectricalSeriesprobeB/electrodes (DynamicTableRegion) probeB electrodes | shape = (384,) | dtype = int32
  Group /acquisition/LFPprobeF (LFP) 
  Group /acquisition/LFPprobeF/ElectricalSeriesprobeF (ElectricalSeries) voltage measured over time and associated timestamps from NeuropixelsprobeF
  Dataset /acquisition/LFPprobeF/ElectricalSeriesprobeF/electrodes (DynamicTableRegion) probeF electrodes | shape = (384,) | dtype = int32
  file_create_date: ['2023-03-15T11:11:55.417065-07:00']
  Group /general/devices/EEG array (Device) H32 Mouse EEG (30-ch)
  Group /general/devices/probeB (Device) Neuropixels 1.0 probe
  Group /general/devices/probeF (Device) Neuropixels 1.0 probe
  experiment_description: in vivo electrophysiology in a head-fixed mouse during cortical electrical microstimulation
  experimenter: ['Claar, Leslie D' 'Rembado, Irene' 'Kuyat, Jacqulyn R' 'Russo, Simone'
   'Marks, Lydia C' 'Olsen, Shawn R' 'Koch, Christof']
  Group /general/extracellular_ephys/EEG array (ElectrodeGroup) 30-ch surface grid
  Group /general/extracellular_ephys/EEG array/device (Device) H32 Mouse EEG (30-ch)
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (798,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (798,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (798,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/is_data_valid (VectorData) True for electrodes/channels with usable data | shape = (798,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (798,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/probe_horizontal_position (VectorData) width-wise position of electrode/channel on device (microns) | shape = (798,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/probe_vertical_position (VectorData) length-wise position of electrode/channel on device (microns) | shape = (798,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/reference (VectorData) Description of the reference electrode and/or reference scheme used for this                         electrode, e.g.,"stainless steel skull screw" or "online common average referencing". | shape = (798,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the position (+x is posterior) | shape = (798,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the position (+y is inferior) | shape = (798,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the position (+z is right) | shape = (798,) | dtype = float64
  Group /general/extracellular_ephys/probeB (ElectrodeGroup) Neuropixels probe B
  Group /general/extracellular_ephys/probeB/device (Device) Neuropixels 1.0 probe
  Group /general/extracellular_ephys/probeF (ElectrodeGroup) Neuropixels probe F
  Group /general/extracellular_ephys/probeF/device (Device) Neuropixels 1.0 probe
  institution: Allen Institute
  keywords: ['EEG' 'Neuropixels' 'electrical stimulation' 'brain states'
   'cortico-thalamic interactions']
  related_publications: ['https://doi.org/10.7554/eLife.84630.1']
  session_id: 20210211
  stimulus: single pulse electrical stimuli targeted to MOs (deep layers)
  Group /general/subject (Subject) 
  identifier: 551397-20210211-v001
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (2,) | dtype = int32
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (2,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (2,) | dtype = float64
  Dataset /intervals/epochs/tags (VectorData) user-defined tags | shape = (2,) | dtype = object
  Dataset /intervals/epochs/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (2,) | dtype = uint8
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/behavioral_epoch (VectorData) behavioral epoch when stimulus was delivered | shape = (1800,) | dtype = object
  Dataset /intervals/trials/estim_current (VectorData) electrical stimulation current (μA), if applicable | shape = (1800,) | dtype = object
  Dataset /intervals/trials/estim_target_depth (VectorData) electrical stimulation target depth (cortical layer), if applicable | shape = (1800,) | dtype = object
  Dataset /intervals/trials/estim_target_region (VectorData) electrical stimulation target region, if applicable | shape = (1800,) | dtype = object
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (1800,) | dtype = int32
  Dataset /intervals/trials/is_running (VectorData) True if mouse is running during trial, running defined as average speed > 0 cm/s between [-0.5, 0.5] s from stimulus onset | shape = (1800,) | dtype = bool
  Dataset /intervals/trials/is_valid (VectorData) True for valid trials, trials are invalid if they have large electrical artifacts or if electrical stimulation was off target | shape = (1800,) | dtype = bool
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (1800,) | dtype = float64
  Dataset /intervals/trials/stimulus_description (VectorData) more specific description of stimulus type | shape = (1800,) | dtype = object
  Dataset /intervals/trials/stimulus_type (VectorData) type of stimulus delivered | shape = (1800,) | dtype = object
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1800,) | dtype = float64
  Group /processing/behavior (ProcessingModule) processed behavioral data
  Group /processing/behavior/BehavioralTimeSeries (BehavioralTimeSeries) 
  Group /processing/behavior/BehavioralTimeSeries/running_speed (TimeSeries) running speed data, computed from wheel angular velocity
  session_description: EEG and Neuropixels recording during wakefulness and isoflurane anesthesia
  session_start_time: 2021-02-11T10:45:18.239000-08:00
  timestamps_reference_time: 2021-02-11T10:45:18.239000-08:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/amplitude_cutoff (VectorData) an estimate of the fraction of spikes below the spike detection threshold | shape = (607,) | dtype = float64
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (607,) | dtype = object
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (607,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex) Index for VectorData 'electrodes' | shape = (607,) | dtype = uint16
  Dataset /units/id (ElementIdentifiers)  | shape = (607,) | dtype = int32
  Dataset /units/isi_violations (VectorData) an estimate of the relative firing rate of hypothetical neurons generating inter-spike-interval violations | shape = (607,) | dtype = float64
  Dataset /units/location (VectorData) the location of unit within the brain (CCF acronym) | shape = (607,) | dtype = object
  Dataset /units/presence_ratio (VectorData) the fraction of time the unit was present during the experiment (ranges from 0 to 0.99) | shape = (607,) | dtype = float64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (30495283,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (607,) | dtype = uint32
  Dataset /units/waveform_duration (VectorData) the mean duration (s) of detected spiking events | shape = (607,) | dtype = float64
  Dataset /units/waveform_mean (VectorData) the spike waveform mean for each spike unit | shape = (607, 82) | dtype = float64
  Dataset /units/x (VectorData) the x coordinate of the position (CCF, +x is posterior) | shape = (607,) | dtype = float64
  Dataset /units/y (VectorData) the y coordinate of the position (CCF, +y is inferior) | shape = (607,) | dtype = float64
  Dataset /units/z (VectorData) the z coordinate of the position (CCF, +z is right) | shape = (607,) | dtype = float64


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeriesEEG (ElectricalSeries) voltage measured over time and associated timestamps from EEG array
  Dataset /acquisition/ElectricalSeriesEEG/electrodes (DynamicTableRegion) EEG electrodes | shape = (30,) | dtype = int32
  Group /acquisition/LFPprobeB (LFP) 
  Group /acquisition/LFPprobeB/ElectricalSeriesprobeB (ElectricalSeries) voltage measured over time and associated timestamps from NeuropixelsprobeB
  Dataset /acquisition/LFPprobeB/ElectricalSeriesprobeB/electrodes (DynamicTableRegion) probeB electrodes | shape = (384,) | dtype = int32
  Group /acquisition/LFPprobeD (LFP) 
  Group /acquisition/LFPprobeD/ElectricalSeriesprobeD (ElectricalSeries) voltage measured over time and associated timestamps from NeuropixelsprobeD
  Dataset /acquisition/LFPprobeD/ElectricalSeriesprobeD/electrodes (DynamicTableRegion) probeD electrodes | shape = (384,) | dtype = int32
  Group /acquisition/LFPprobeF (LFP) 
  Group /acquisition/LFPprobeF/ElectricalSeriesprobeF (ElectricalSeries) voltage measured over time and associated timestamps from NeuropixelsprobeF
  Dataset /acquisition/LFPprobeF/ElectricalSeriesprobeF/electrodes (DynamicTableRegion) probeF electrodes | shape = (384,) | dtype = int32
  file_create_date: ['2023-03-15T11:40:05.364699-07:00']
  Group /general/devices/EEG array (Device) H32 Mouse EEG (30-ch)
  Group /general/devices/probeB (Device) Neuropixels 1.0 probe
  Group /general/devices/probeD (Device) Neuropixels 1.0 probe
  Group /general/devices/probeF (Device) Neuropixels 1.0 probe
  experiment_description: in vivo electrophysiology in a head-fixed mouse during cortical electrical microstimulation
  experimenter: ['Claar, Leslie D' 'Rembado, Irene' 'Kuyat, Jacqulyn R' 'Russo, Simone'
   'Marks, Lydia C' 'Olsen, Shawn R' 'Koch, Christof']
  Group /general/extracellular_ephys/EEG array (ElectrodeGroup) 30-ch surface grid
  Group /general/extracellular_ephys/EEG array/device (Device) H32 Mouse EEG (30-ch)
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (1182,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (1182,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (1182,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/is_data_valid (VectorData) True for electrodes/channels with usable data | shape = (1182,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (1182,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/probe_horizontal_position (VectorData) width-wise position of electrode/channel on device (microns) | shape = (1182,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/probe_vertical_position (VectorData) length-wise position of electrode/channel on device (microns) | shape = (1182,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/reference (VectorData) Description of the reference electrode and/or reference scheme used for this                         electrode, e.g.,"stainless steel skull screw" or "online common average referencing". | shape = (1182,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the position (+x is posterior) | shape = (1182,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the position (+y is inferior) | shape = (1182,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the position (+z is right) | shape = (1182,) | dtype = float64
  Group /general/extracellular_ephys/probeB (ElectrodeGroup) Neuropixels probe B
  Group /general/extracellular_ephys/probeB/device (Device) Neuropixels 1.0 probe
  Group /general/extracellular_ephys/probeD (ElectrodeGroup) Neuropixels probe D
  Group /general/extracellular_ephys/probeD/device (Device) Neuropixels 1.0 probe
  Group /general/extracellular_ephys/probeF (ElectrodeGroup) Neuropixels probe F
  Group /general/extracellular_ephys/probeF/device (Device) Neuropixels 1.0 probe
  institution: Allen Institute
  keywords: ['EEG' 'Neuropixels' 'electrical stimulation' 'brain states'
   'cortico-thalamic interactions']
  related_publications: ['https://doi.org/10.7554/eLife.84630.1']
  session_id: 20210218
  stimulus: single pulse electrical stimuli targeted to MOs (deep layers)
  Group /general/subject (Subject) 
  identifier: 569062-20210218-v001
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (2,) | dtype = int32
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (2,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (2,) | dtype = float64
  Dataset /intervals/epochs/tags (VectorData) user-defined tags | shape = (2,) | dtype = object
  Dataset /intervals/epochs/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (2,) | dtype = uint8
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/behavioral_epoch (VectorData) behavioral epoch when stimulus was delivered | shape = (1440,) | dtype = object
  Dataset /intervals/trials/estim_current (VectorData) electrical stimulation current (μA), if applicable | shape = (1440,) | dtype = object
  Dataset /intervals/trials/estim_target_depth (VectorData) electrical stimulation target depth (cortical layer), if applicable | shape = (1440,) | dtype = object
  Dataset /intervals/trials/estim_target_region (VectorData) electrical stimulation target region, if applicable | shape = (1440,) | dtype = object
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (1440,) | dtype = int32
  Dataset /intervals/trials/is_running (VectorData) True if mouse is running during trial, running defined as average speed > 0 cm/s between [-0.5, 0.5] s from stimulus onset | shape = (1440,) | dtype = bool
  Dataset /intervals/trials/is_valid (VectorData) True for valid trials, trials are invalid if they have large electrical artifacts or if electrical stimulation was off target | shape = (1440,) | dtype = bool
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (1440,) | dtype = float64
  Dataset /intervals/trials/stimulus_description (VectorData) more specific description of stimulus type | shape = (1440,) | dtype = object
  Dataset /intervals/trials/stimulus_type (VectorData) type of stimulus delivered | shape = (1440,) | dtype = object
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1440,) | dtype = float64
  Group /processing/behavior (ProcessingModule) processed behavioral data
  Group /processing/behavior/BehavioralTimeSeries (BehavioralTimeSeries) 
  Group /processing/behavior/BehavioralTimeSeries/running_speed (TimeSeries) running speed data, computed from wheel angular velocity
  session_description: EEG and Neuropixels recording during wakefulness and isoflurane anesthesia
  session_start_time: 2021-02-18T11:17:47.286000-08:00
  timestamps_reference_time: 2021-02-18T11:17:47.286000-08:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/amplitude_cutoff (VectorData) an estimate of the fraction of spikes below the spike detection threshold | shape = (902,) | dtype = float64
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (902,) | dtype = object
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (902,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex) Index for VectorData 'electrodes' | shape = (902,) | dtype = uint16
  Dataset /units/id (ElementIdentifiers)  | shape = (902,) | dtype = int32
  Dataset /units/isi_violations (VectorData) an estimate of the relative firing rate of hypothetical neurons generating inter-spike-interval violations | shape = (902,) | dtype = float64
  Dataset /units/location (VectorData) the location of unit within the brain (CCF acronym) | shape = (902,) | dtype = object
  Dataset /units/presence_ratio (VectorData) the fraction of time the unit was present during the experiment (ranges from 0 to 0.99) | shape = (902,) | dtype = float64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (22684156,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (902,) | dtype = uint32
  Dataset /units/waveform_duration (VectorData) the mean duration (s) of detected spiking events | shape = (902,) | dtype = float64
  Dataset /units/waveform_mean (VectorData) the spike waveform mean for each spike unit | shape = (902, 82) | dtype = float64
  Dataset /units/x (VectorData) the x coordinate of the position (CCF, +x is posterior) | shape = (902,) | dtype = float64
  Dataset /units/y (VectorData) the y coordinate of the position (CCF, +y is inferior) | shape = (902,) | dtype = float64
  Dataset /units/z (VectorData) the z coordinate of the position (CCF, +z is right) | shape = (902,) | dtype = float64


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeriesEEG (ElectricalSeries) voltage measured over time and associated timestamps from EEG array
  Dataset /acquisition/ElectricalSeriesEEG/electrodes (DynamicTableRegion) EEG electrodes | shape = (30,) | dtype = int32
  Group /acquisition/LFPprobeB (LFP) 
  Group /acquisition/LFPprobeB/ElectricalSeriesprobeB (ElectricalSeries) voltage measured over time and associated timestamps from NeuropixelsprobeB
  Dataset /acquisition/LFPprobeB/ElectricalSeriesprobeB/electrodes (DynamicTableRegion) probeB electrodes | shape = (384,) | dtype = int32
  Group /acquisition/LFPprobeC (LFP) 
  Group /acquisition/LFPprobeC/ElectricalSeriesprobeC (ElectricalSeries) voltage measured over time and associated timestamps from NeuropixelsprobeC
  Dataset /acquisition/LFPprobeC/ElectricalSeriesprobeC/electrodes (DynamicTableRegion) probeC electrodes | shape = (384,) | dtype = int32
  Group /acquisition/LFPprobeF (LFP) 
  Group /acquisition/LFPprobeF/ElectricalSeriesprobeF (ElectricalSeries) voltage measured over time and associated timestamps from NeuropixelsprobeF
  Dataset /acquisition/LFPprobeF/ElectricalSeriesprobeF/electrodes (DynamicTableRegion) probeF electrodes | shape = (384,) | dtype = int32
  file_create_date: ['2023-03-15T14:10:53.284341-07:00']
  Group /general/devices/EEG array (Device) H32 Mouse EEG (30-ch)
  Group /general/devices/probeB (Device) Neuropixels 1.0 probe
  Group /general/devices/probeC (Device) Neuropixels 1.0 probe
  Group /general/devices/probeF (Device) Neuropixels 1.0 probe
  experiment_description: in vivo electrophysiology in a head-fixed mouse during cortical electrical microstimulation
  experimenter: ['Claar, Leslie D' 'Rembado, Irene' 'Kuyat, Jacqulyn R' 'Russo, Simone'
   'Marks, Lydia C' 'Olsen, Shawn R' 'Koch, Christof']
  Group /general/extracellular_ephys/EEG array (ElectrodeGroup) 30-ch surface grid
  Group /general/extracellular_ephys/EEG array/device (Device) H32 Mouse EEG (30-ch)
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (1182,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (1182,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (1182,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/is_data_valid (VectorData) True for electrodes/channels with usable data | shape = (1182,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (1182,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/probe_horizontal_position (VectorData) width-wise position of electrode/channel on device (microns) | shape = (1182,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/probe_vertical_position (VectorData) length-wise position of electrode/channel on device (microns) | shape = (1182,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/reference (VectorData) Description of the reference electrode and/or reference scheme used for this                         electrode, e.g.,"stainless steel skull screw" or "online common average referencing". | shape = (1182,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the position (+x is posterior) | shape = (1182,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the position (+y is inferior) | shape = (1182,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the position (+z is right) | shape = (1182,) | dtype = float64
  Group /general/extracellular_ephys/probeB (ElectrodeGroup) Neuropixels probe B
  Group /general/extracellular_ephys/probeB/device (Device) Neuropixels 1.0 probe
  Group /general/extracellular_ephys/probeC (ElectrodeGroup) Neuropixels probe C
  Group /general/extracellular_ephys/probeC/device (Device) Neuropixels 1.0 probe
  Group /general/extracellular_ephys/probeF (ElectrodeGroup) Neuropixels probe F
  Group /general/extracellular_ephys/probeF/device (Device) Neuropixels 1.0 probe
  institution: Allen Institute
  keywords: ['EEG' 'Neuropixels' 'electrical stimulation' 'brain states'
   'cortico-thalamic interactions']
  related_publications: ['https://doi.org/10.7554/eLife.84630.1']
  session_id: 20210408
  stimulus: single pulse electrical stimuli targeted to MOs (deep layers)
  Group /general/subject (Subject) 
  identifier: 569064-20210408-v001
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (2,) | dtype = int32
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (2,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (2,) | dtype = float64
  Dataset /intervals/epochs/tags (VectorData) user-defined tags | shape = (2,) | dtype = object
  Dataset /intervals/epochs/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (2,) | dtype = uint8
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/behavioral_epoch (VectorData) behavioral epoch when stimulus was delivered | shape = (1920,) | dtype = object
  Dataset /intervals/trials/estim_current (VectorData) electrical stimulation current (μA), if applicable | shape = (1920,) | dtype = object
  Dataset /intervals/trials/estim_target_depth (VectorData) electrical stimulation target depth (cortical layer), if applicable | shape = (1920,) | dtype = object
  Dataset /intervals/trials/estim_target_region (VectorData) electrical stimulation target region, if applicable | shape = (1920,) | dtype = object
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (1920,) | dtype = int32
  Dataset /intervals/trials/is_running (VectorData) True if mouse is running during trial, running defined as average speed > 0 cm/s between [-0.5, 0.5] s from stimulus onset | shape = (1920,) | dtype = bool
  Dataset /intervals/trials/is_valid (VectorData) True for valid trials, trials are invalid if they have large electrical artifacts or if electrical stimulation was off target | shape = (1920,) | dtype = bool
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (1920,) | dtype = float64
  Dataset /intervals/trials/stimulus_description (VectorData) more specific description of stimulus type | shape = (1920,) | dtype = object
  Dataset /intervals/trials/stimulus_type (VectorData) type of stimulus delivered | shape = (1920,) | dtype = object
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1920,) | dtype = float64
  Group /processing/behavior (ProcessingModule) processed behavioral data
  Group /processing/behavior/BehavioralTimeSeries (BehavioralTimeSeries) 
  Group /processing/behavior/BehavioralTimeSeries/running_speed (TimeSeries) running speed data, computed from wheel angular velocity
  session_description: EEG and Neuropixels recording during wakefulness and isoflurane anesthesia
  session_start_time: 2021-04-08T10:27:27.251000-07:00
  timestamps_reference_time: 2021-04-08T10:27:27.251000-07:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/amplitude_cutoff (VectorData) an estimate of the fraction of spikes below the spike detection threshold | shape = (481,) | dtype = float64
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (481,) | dtype = object
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (481,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex) Index for VectorData 'electrodes' | shape = (481,) | dtype = uint16
  Dataset /units/id (ElementIdentifiers)  | shape = (481,) | dtype = int32
  Dataset /units/isi_violations (VectorData) an estimate of the relative firing rate of hypothetical neurons generating inter-spike-interval violations | shape = (481,) | dtype = float64
  Dataset /units/location (VectorData) the location of unit within the brain (CCF acronym) | shape = (481,) | dtype = object
  Dataset /units/presence_ratio (VectorData) the fraction of time the unit was present during the experiment (ranges from 0 to 0.99) | shape = (481,) | dtype = float64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (17086406,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (481,) | dtype = uint32
  Dataset /units/waveform_duration (VectorData) the mean duration (s) of detected spiking events | shape = (481,) | dtype = float64
  Dataset /units/waveform_mean (VectorData) the spike waveform mean for each spike unit | shape = (481, 82) | dtype = float64
  Dataset /units/x (VectorData) the x coordinate of the position (CCF, +x is posterior) | shape = (481,) | dtype = float64
  Dataset /units/y (VectorData) the y coordinate of the position (CCF, +y is inferior) | shape = (481,) | dtype = float64
  Dataset /units/z (VectorData) the z coordinate of the position (CCF, +z is right) | shape = (481,) | dtype = float64
