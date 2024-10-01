
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000060/draft
name: Dataset for Finkelstein, Fontolan et al. "Attractor dynamics gate cortical information flow during decision-making"
contributor: [{'name': 'Finkelstein, Arseny', 'email': 'arsenyf@gmail.com', 'roleName': ['dcite:Author', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0003-1480-5670', 'affiliation': [{'name': 'Janelia Research Campus, Howard Hughes Medical Institute', 'schemaKey': 'Affiliation', 'includeInCitation': False}], 'includeInCitation': True}, {'name': 'Svoboda, Karel', 'email': 'svobodak@janelia.hhmi.org', 'roleName': ['dcite:Author', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [{'name': 'Janelia Research Campus, Howard Hughes Medical Institute', 'schemaKey': 'Affiliation', 'includeInCitation': False}], 'includeInCitation': True}]
description: Extracellular electrophysiology recordings in anterior lateral motor cortex and in vibrissal sensory cortex in mice trained to detect optogenetic stimulation of the vibrissal sensory cortex.

The data analysis code for this dataset is available here: 
 https://github.com/arsenyf/FinkelsteinFontolan_2021NN
assetsSummary: {'species': [{'name': 'House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}, {'name': 'behavioral approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 1009087545, 'numberOfFiles': 98, 'numberOfSubjects': 9, 'variableMeasured': ['Units', 'BehavioralEvents'], 'measurementTechnique': [{'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000060 has 44 NWB files.
11 of these NWB files are of type 1.
5 of these NWB files are of type 2.
26 of these NWB files are of type 3.
1 of these NWB files are of type 4.
1 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/LabeledEvents (LabeledEvents) behavioral events of the experimental paradigm
  Group /acquisition/PhotostimEvents (BehavioralEvents) 
  Group /acquisition/PhotostimEvents/photostim_start_times (TimeSeries) Timestamps of the photo-stimulation and the corresponding powers (in mW) being applied
  Group /acquisition/PhotostimEvents/photostim_stop_times (TimeSeries) Timestamps of the photo-stimulation being switched off
  file_create_date: ['2021-04-09T22:47:35.055900-05:00']
  data_collection: good behavior
  Group /general/devices/LaserGem473 (Device) 
  Group /general/devices/janelia2x32_H-129 (Device) 
  experiment_description: Extracellular electrophysiology recordings in anterior lateral motor cortex and in vibrissal sensory cortex in mice trained to detect optogenetic stimulation of the vibrissal sensory cortex
  experimenter: ['ars']
  Group /general/extracellular_ephys/1 (ElectrodeGroup) N/A
  Group /general/extracellular_ephys/1/device (Device) 
  Group /general/extracellular_ephys/2 (ElectrodeGroup) N/A
  Group /general/extracellular_ephys/2/device (Device) 
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (64,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (64,) | dtype = float64
  institution: Janelia Research Campus
  keywords: ['decision-making' 'motor cortex' 'optogenetic stimulation'
   'extracellular electrophysiology' 'attractor']
  Group /general/optogenetics/LaserGem473_1 (OptogeneticStimulusSite) 
  Group /general/optogenetics/LaserGem473_1/device (Device) 
  related_publications: ['https://doi.org/10.1038/s41593-021-00840-6']
  Group /general/subject (Subject) 
  identifier: 353936_session_1
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/early_lick (VectorData)  | shape = (354,) | dtype = object
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (354,) | dtype = int32
  Dataset /intervals/trials/outcome (VectorData)  | shape = (354,) | dtype = object
  Dataset /intervals/trials/photostim_duration (VectorData) total stimulation duration (s) | shape = (354,) | dtype = object
  Dataset /intervals/trials/photostim_onset (VectorData) onset of the stimulation relative to the go-cue (s); None for no-stim trials | shape = (354,) | dtype = object
  Dataset /intervals/trials/photostim_power (VectorData) laser power (mW) | shape = (354,) | dtype = object
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (354,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (354,) | dtype = float64
  Dataset /intervals/trials/task (VectorData) task type | shape = (354,) | dtype = object
  Dataset /intervals/trials/task_protocol (VectorData) task ptotcol | shape = (354,) | dtype = int32
  Dataset /intervals/trials/trial_instruction (VectorData)  | shape = (354,) | dtype = object
  Dataset /intervals/trials/trial_type_name (VectorData) trial-type name | shape = (354,) | dtype = object
  session_description: {"subject_id": 353936, "session": 1, "task": "s1 stim", "task_protocol": 4, "task_description": "S1 photostimulation task (2AFC)"}
  session_start_time: 2017-05-19T00:00:00-05:00
  timestamps_reference_time: 2017-05-19T00:00:00-05:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/cell_type (VectorData) cell type | shape = (41,) | dtype = object
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (41,) | dtype = object
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (41,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex) Index for VectorData 'electrodes' | shape = (41,) | dtype = uint8
  Dataset /units/id (ElementIdentifiers)  | shape = (41,) | dtype = int32
  Dataset /units/obs_intervals (VectorData) the observation intervals for each unit | shape = (14514, 2) | dtype = float64
  Dataset /units/obs_intervals_index (VectorIndex) Index for VectorData 'obs_intervals' | shape = (41,) | dtype = uint16
  Dataset /units/quality (VectorData) unit quality from clustering | shape = (41,) | dtype = object
  Dataset /units/sampling_rate (VectorData) Sampling rate of the raw voltage traces (Hz) | shape = (41,) | dtype = float64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (1678798,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (41,) | dtype = uint32
  Dataset /units/spk_width_ms (VectorData) unit average spike width, in ms | shape = (41,) | dtype = float64
  Dataset /units/unit_ap_location (VectorData) um from ref; anterior is positive; based on manipulator coordinates (or histology) & probe config | shape = (41,) | dtype = float64
  Dataset /units/unit_dv_location (VectorData) um from dura; ventral is positive; based on manipulator coordinates (or histology) & probe config | shape = (41,) | dtype = float64
  Dataset /units/unit_ml_location (VectorData) um from ref; right is positive; based on manipulator coordinates (or histology) & probe config | shape = (41,) | dtype = float64
  Dataset /units/waveform_amplitude (VectorData) unit amplitude (peak) in microvolts | shape = (41,) | dtype = float64
  Dataset /units/waveform_mean (VectorData) the spike waveform mean for each spike unit | shape = (41, 1, 42) | dtype = float64
  Dataset /units/waveform_sd (VectorData) the spike waveform standard deviation for each spike unit | shape = (41, 1, 42) | dtype = float64


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/LabeledEvents (LabeledEvents) behavioral events of the experimental paradigm
  Group /acquisition/PhotostimEvents (BehavioralEvents) 
  Group /acquisition/PhotostimEvents/photostim_start_times (TimeSeries) Timestamps of the photo-stimulation and the corresponding powers (in mW) being applied
  Group /acquisition/PhotostimEvents/photostim_stop_times (TimeSeries) Timestamps of the photo-stimulation being switched off
  file_create_date: ['2021-04-10T00:42:10.360738-05:00']
  data_collection: bad behavior
  Group /general/devices/LaserGem473 (Device) 
  Group /general/devices/janelia2x32_H-254 (Device) 
  experiment_description: Extracellular electrophysiology recordings in anterior lateral motor cortex and in vibrissal sensory cortex in mice trained to detect optogenetic stimulation of the vibrissal sensory cortex
  experimenter: ['ars']
  Group /general/extracellular_ephys/1 (ElectrodeGroup) N/A
  Group /general/extracellular_ephys/1/device (Device) 
  Group /general/extracellular_ephys/2 (ElectrodeGroup) N/A
  Group /general/extracellular_ephys/2/device (Device) 
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (64,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (64,) | dtype = float64
  institution: Janelia Research Campus
  keywords: ['decision-making' 'motor cortex' 'optogenetic stimulation'
   'extracellular electrophysiology' 'attractor']
  Group /general/optogenetics/LaserGem473_1 (OptogeneticStimulusSite) 
  Group /general/optogenetics/LaserGem473_1/device (Device) 
  related_publications: ['https://doi.org/10.1038/s41593-021-00840-6']
  Group /general/subject (Subject) 
  identifier: 365938_session_8
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/early_lick (VectorData)  | shape = (621,) | dtype = object
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (621,) | dtype = int32
  Dataset /intervals/trials/outcome (VectorData)  | shape = (621,) | dtype = object
  Dataset /intervals/trials/photostim_duration (VectorData) total stimulation duration (s) | shape = (621,) | dtype = object
  Dataset /intervals/trials/photostim_onset (VectorData) onset of the stimulation relative to the go-cue (s); None for no-stim trials | shape = (621,) | dtype = object
  Dataset /intervals/trials/photostim_power (VectorData) laser power (mW) | shape = (621,) | dtype = object
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (621,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (621,) | dtype = float64
  Dataset /intervals/trials/task (VectorData) task type | shape = (621,) | dtype = object
  Dataset /intervals/trials/task_protocol (VectorData) task ptotcol | shape = (621,) | dtype = int32
  Dataset /intervals/trials/trial_instruction (VectorData)  | shape = (621,) | dtype = object
  Dataset /intervals/trials/trial_type_name (VectorData) trial-type name | shape = (621,) | dtype = object
  session_description: {"subject_id": 365938, "session": 8, "task": "s1 stim", "task_protocol": 4, "task_description": "S1 photostimulation task (2AFC)"}
  session_start_time: 2017-10-30T00:00:00-05:00
  timestamps_reference_time: 2017-10-30T00:00:00-05:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/cell_type (VectorData) cell type | shape = (19,) | dtype = object
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (19,) | dtype = object
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (19,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex) Index for VectorData 'electrodes' | shape = (19,) | dtype = uint8
  Dataset /units/id (ElementIdentifiers)  | shape = (19,) | dtype = int32
  Dataset /units/obs_intervals (VectorData) the observation intervals for each unit | shape = (11799, 2) | dtype = float64
  Dataset /units/obs_intervals_index (VectorIndex) Index for VectorData 'obs_intervals' | shape = (19,) | dtype = uint16
  Dataset /units/quality (VectorData) unit quality from clustering | shape = (19,) | dtype = object
  Dataset /units/sampling_rate (VectorData) Sampling rate of the raw voltage traces (Hz) | shape = (19,) | dtype = float64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (1191880,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (19,) | dtype = uint32
  Dataset /units/spk_width_ms (VectorData) unit average spike width, in ms | shape = (19,) | dtype = float64
  Dataset /units/unit_ap_location (VectorData) um from ref; anterior is positive; based on manipulator coordinates (or histology) & probe config | shape = (19,) | dtype = float64
  Dataset /units/unit_dv_location (VectorData) um from dura; ventral is positive; based on manipulator coordinates (or histology) & probe config | shape = (19,) | dtype = float64
  Dataset /units/unit_ml_location (VectorData) um from ref; right is positive; based on manipulator coordinates (or histology) & probe config | shape = (19,) | dtype = float64
  Dataset /units/waveform_amplitude (VectorData) unit amplitude (peak) in microvolts | shape = (19,) | dtype = float64
  Dataset /units/waveform_mean (VectorData) the spike waveform mean for each spike unit | shape = (19, 1, 42) | dtype = float64
  Dataset /units/waveform_sd (VectorData) the spike waveform standard deviation for each spike unit | shape = (19, 1, 42) | dtype = float64


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/LabeledEvents (LabeledEvents) behavioral events of the experimental paradigm
  Group /acquisition/PhotostimEvents (BehavioralEvents) 
  Group /acquisition/PhotostimEvents/photostim_start_times (TimeSeries) Timestamps of the photo-stimulation and the corresponding powers (in mW) being applied
  Group /acquisition/PhotostimEvents/photostim_stop_times (TimeSeries) Timestamps of the photo-stimulation being switched off
  file_create_date: ['2021-04-09T22:52:39.310637-05:00']
  data_collection: good behavior
  Group /general/devices/LaserGem473 (Device) 
  Group /general/devices/janelia2x32_H-194 (Device) 
  experiment_description: Extracellular electrophysiology recordings in anterior lateral motor cortex and in vibrissal sensory cortex in mice trained to detect optogenetic stimulation of the vibrissal sensory cortex
  experimenter: ['ars']
  Group /general/extracellular_ephys/1 (ElectrodeGroup) N/A
  Group /general/extracellular_ephys/1/device (Device) 
  Group /general/extracellular_ephys/2 (ElectrodeGroup) N/A
  Group /general/extracellular_ephys/2/device (Device) 
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (64,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (64,) | dtype = float64
  institution: Janelia Research Campus
  keywords: ['decision-making' 'motor cortex' 'optogenetic stimulation'
   'extracellular electrophysiology' 'attractor']
  Group /general/optogenetics/LaserGem473_1 (OptogeneticStimulusSite) 
  Group /general/optogenetics/LaserGem473_1/device (Device) 
  related_publications: ['https://doi.org/10.1038/s41593-021-00840-6']
  Group /general/subject (Subject) 
  identifier: 353936_session_4
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/early_lick (VectorData)  | shape = (569,) | dtype = object
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (569,) | dtype = int32
  Dataset /intervals/trials/outcome (VectorData)  | shape = (569,) | dtype = object
  Dataset /intervals/trials/photostim_duration (VectorData) total stimulation duration (s) | shape = (569,) | dtype = object
  Dataset /intervals/trials/photostim_onset (VectorData) onset of the stimulation relative to the go-cue (s); None for no-stim trials | shape = (569,) | dtype = object
  Dataset /intervals/trials/photostim_power (VectorData) laser power (mW) | shape = (569,) | dtype = object
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (569,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (569,) | dtype = float64
  Dataset /intervals/trials/task (VectorData) task type | shape = (569,) | dtype = object
  Dataset /intervals/trials/task_protocol (VectorData) task ptotcol | shape = (569,) | dtype = int32
  Dataset /intervals/trials/trial_instruction (VectorData)  | shape = (569,) | dtype = object
  Dataset /intervals/trials/trial_type_name (VectorData) trial-type name | shape = (569,) | dtype = object
  session_description: {"subject_id": 353936, "session": 4, "task": "s1 stim", "task_protocol": 4, "task_description": "S1 photostimulation task (2AFC)"}
  session_start_time: 2017-06-10T00:00:00-05:00
  timestamps_reference_time: 2017-06-10T00:00:00-05:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/cell_type (VectorData) cell type | shape = (120,) | dtype = object
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (120,) | dtype = object
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (120,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex) Index for VectorData 'electrodes' | shape = (120,) | dtype = uint8
  Dataset /units/id (ElementIdentifiers)  | shape = (120,) | dtype = int32
  Dataset /units/obs_intervals (VectorData) the observation intervals for each unit | shape = (68280, 2) | dtype = float64
  Dataset /units/obs_intervals_index (VectorIndex) Index for VectorData 'obs_intervals' | shape = (120,) | dtype = uint32
  Dataset /units/quality (VectorData) unit quality from clustering | shape = (120,) | dtype = object
  Dataset /units/sampling_rate (VectorData) Sampling rate of the raw voltage traces (Hz) | shape = (120,) | dtype = float64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (2434313,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (120,) | dtype = uint32
  Dataset /units/spk_width_ms (VectorData) unit average spike width, in ms | shape = (120,) | dtype = float64
  Dataset /units/unit_ap_location (VectorData) um from ref; anterior is positive; based on manipulator coordinates (or histology) & probe config | shape = (120,) | dtype = float64
  Dataset /units/unit_dv_location (VectorData) um from dura; ventral is positive; based on manipulator coordinates (or histology) & probe config | shape = (120,) | dtype = float64
  Dataset /units/unit_ml_location (VectorData) um from ref; right is positive; based on manipulator coordinates (or histology) & probe config | shape = (120,) | dtype = float64
  Dataset /units/waveform_amplitude (VectorData) unit amplitude (peak) in microvolts | shape = (120,) | dtype = float64
  Dataset /units/waveform_mean (VectorData) the spike waveform mean for each spike unit | shape = (120, 1, 42) | dtype = float64
  Dataset /units/waveform_sd (VectorData) the spike waveform standard deviation for each spike unit | shape = (120, 1, 42) | dtype = float64


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/LabeledEvents (LabeledEvents) behavioral events of the experimental paradigm
  Group /acquisition/PhotostimEvents (BehavioralEvents) 
  Group /acquisition/PhotostimEvents/photostim_start_times (TimeSeries) Timestamps of the photo-stimulation and the corresponding powers (in mW) being applied
  Group /acquisition/PhotostimEvents/photostim_stop_times (TimeSeries) Timestamps of the photo-stimulation being switched off
  file_create_date: ['2021-04-09T23:11:54.176486-05:00']
  data_collection: good behavior
  Group /general/devices/LaserGem473 (Device) 
  Group /general/devices/janelia2x32_H-192 (Device) 
  experiment_description: Extracellular electrophysiology recordings in anterior lateral motor cortex and in vibrissal sensory cortex in mice trained to detect optogenetic stimulation of the vibrissal sensory cortex
  experimenter: ['ars']
  Group /general/extracellular_ephys/1 (ElectrodeGroup) N/A
  Group /general/extracellular_ephys/1/device (Device) 
  Group /general/extracellular_ephys/2 (ElectrodeGroup) N/A
  Group /general/extracellular_ephys/2/device (Device) 
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (64,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (64,) | dtype = float64
  institution: Janelia Research Campus
  keywords: ['decision-making' 'motor cortex' 'optogenetic stimulation'
   'extracellular electrophysiology' 'attractor']
  Group /general/optogenetics/LaserGem473_1 (OptogeneticStimulusSite) 
  Group /general/optogenetics/LaserGem473_1/device (Device) 
  related_publications: ['https://doi.org/10.1038/s41593-021-00840-6']
  Group /general/subject (Subject) 
  identifier: 353936_session_6
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/early_lick (VectorData)  | shape = (430,) | dtype = object
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (430,) | dtype = int32
  Dataset /intervals/trials/outcome (VectorData)  | shape = (430,) | dtype = object
  Dataset /intervals/trials/photostim_duration (VectorData) total stimulation duration (s) | shape = (430,) | dtype = object
  Dataset /intervals/trials/photostim_onset (VectorData) onset of the stimulation relative to the go-cue (s); None for no-stim trials | shape = (430,) | dtype = object
  Dataset /intervals/trials/photostim_power (VectorData) laser power (mW) | shape = (430,) | dtype = object
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (430,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (430,) | dtype = float64
  Dataset /intervals/trials/task (VectorData) task type | shape = (430,) | dtype = object
  Dataset /intervals/trials/task_protocol (VectorData) task ptotcol | shape = (430,) | dtype = int32
  Dataset /intervals/trials/trial_instruction (VectorData)  | shape = (430,) | dtype = object
  Dataset /intervals/trials/trial_type_name (VectorData) trial-type name | shape = (430,) | dtype = object
  session_description: {"subject_id": 353936, "session": 6, "task": "s1 stim", "task_protocol": 5, "task_description": "S1 photostimulation task (2AFC)"}
  session_start_time: 2017-06-12T00:00:00-05:00
  timestamps_reference_time: 2017-06-12T00:00:00-05:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/cell_type (VectorData) cell type | shape = (129,) | dtype = object
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (129,) | dtype = object
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (129,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex) Index for VectorData 'electrodes' | shape = (129,) | dtype = uint8
  Dataset /units/id (ElementIdentifiers)  | shape = (129,) | dtype = int32
  Dataset /units/obs_intervals (VectorData) the observation intervals for each unit | shape = (55470, 2) | dtype = float64
  Dataset /units/obs_intervals_index (VectorIndex) Index for VectorData 'obs_intervals' | shape = (129,) | dtype = uint16
  Dataset /units/quality (VectorData) unit quality from clustering | shape = (129,) | dtype = object
  Dataset /units/sampling_rate (VectorData) Sampling rate of the raw voltage traces (Hz) | shape = (129,) | dtype = float64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (1568692,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (129,) | dtype = uint32
  Dataset /units/spk_width_ms (VectorData) unit average spike width, in ms | shape = (129,) | dtype = float64
  Dataset /units/unit_ap_location (VectorData) um from ref; anterior is positive; based on manipulator coordinates (or histology) & probe config | shape = (129,) | dtype = float64
  Dataset /units/unit_dv_location (VectorData) um from dura; ventral is positive; based on manipulator coordinates (or histology) & probe config | shape = (129,) | dtype = float64
  Dataset /units/unit_ml_location (VectorData) um from ref; right is positive; based on manipulator coordinates (or histology) & probe config | shape = (129,) | dtype = float64
  Dataset /units/waveform_amplitude (VectorData) unit amplitude (peak) in microvolts | shape = (129,) | dtype = float64
  Dataset /units/waveform_mean (VectorData) the spike waveform mean for each spike unit | shape = (129, 1, 42) | dtype = float64
  Dataset /units/waveform_sd (VectorData) the spike waveform standard deviation for each spike unit | shape = (129, 1, 42) | dtype = float64


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  Group /acquisition/LabeledEvents (LabeledEvents) behavioral events of the experimental paradigm
  Group /acquisition/PhotostimEvents (BehavioralEvents) 
  Group /acquisition/PhotostimEvents/photostim_start_times (TimeSeries) Timestamps of the photo-stimulation and the corresponding powers (in mW) being applied
  Group /acquisition/PhotostimEvents/photostim_stop_times (TimeSeries) Timestamps of the photo-stimulation being switched off
  file_create_date: ['2021-04-09T23:13:51.761226-05:00']
  data_collection: good behavior
  Group /general/devices/LaserGem473 (Device) 
  Group /general/devices/janelia2x32_I92 (Device) 
  experiment_description: Extracellular electrophysiology recordings in anterior lateral motor cortex and in vibrissal sensory cortex in mice trained to detect optogenetic stimulation of the vibrissal sensory cortex
  experimenter: ['ars']
  Group /general/extracellular_ephys/1 (ElectrodeGroup) N/A
  Group /general/extracellular_ephys/1/device (Device) 
  Group /general/extracellular_ephys/2 (ElectrodeGroup) N/A
  Group /general/extracellular_ephys/2/device (Device) 
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (64,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (64,) | dtype = float64
  institution: Janelia Research Campus
  keywords: ['decision-making' 'motor cortex' 'optogenetic stimulation'
   'extracellular electrophysiology' 'attractor']
  Group /general/optogenetics/LaserGem473_1 (OptogeneticStimulusSite) 
  Group /general/optogenetics/LaserGem473_1/device (Device) 
  related_publications: ['https://doi.org/10.1038/s41593-021-00840-6']
  Group /general/subject (Subject) 
  identifier: 353936_session_7
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/early_lick (VectorData)  | shape = (648,) | dtype = object
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (648,) | dtype = int32
  Dataset /intervals/trials/outcome (VectorData)  | shape = (648,) | dtype = object
  Dataset /intervals/trials/photostim_duration (VectorData) total stimulation duration (s) | shape = (648,) | dtype = object
  Dataset /intervals/trials/photostim_onset (VectorData) onset of the stimulation relative to the go-cue (s); None for no-stim trials | shape = (648,) | dtype = object
  Dataset /intervals/trials/photostim_power (VectorData) laser power (mW) | shape = (648,) | dtype = object
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (648,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (648,) | dtype = float64
  Dataset /intervals/trials/task (VectorData) task type | shape = (648,) | dtype = object
  Dataset /intervals/trials/task_protocol (VectorData) task ptotcol | shape = (648,) | dtype = int32
  Dataset /intervals/trials/trial_instruction (VectorData)  | shape = (648,) | dtype = object
  Dataset /intervals/trials/trial_type_name (VectorData) trial-type name | shape = (648,) | dtype = object
  session_description: {"subject_id": 353936, "session": 7, "task": "s1 stim", "task_protocol": 4, "task_description": "S1 photostimulation task (2AFC)"}
  session_start_time: 2017-06-17T00:00:00-05:00
  timestamps_reference_time: 2017-06-17T00:00:00-05:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/cell_type (VectorData) cell type | shape = (106,) | dtype = object
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (106,) | dtype = object
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (106,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex) Index for VectorData 'electrodes' | shape = (106,) | dtype = uint8
  Dataset /units/id (ElementIdentifiers)  | shape = (106,) | dtype = int32
  Dataset /units/obs_intervals (VectorData) the observation intervals for each unit | shape = (68688, 2) | dtype = float64
  Dataset /units/obs_intervals_index (VectorIndex) Index for VectorData 'obs_intervals' | shape = (106,) | dtype = uint32
  Dataset /units/quality (VectorData) unit quality from clustering | shape = (106,) | dtype = object
  Dataset /units/sampling_rate (VectorData) Sampling rate of the raw voltage traces (Hz) | shape = (106,) | dtype = float64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (4269369,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (106,) | dtype = uint32
  Dataset /units/spk_width_ms (VectorData) unit average spike width, in ms | shape = (106,) | dtype = float64
  Dataset /units/unit_ap_location (VectorData) um from ref; anterior is positive; based on manipulator coordinates (or histology) & probe config | shape = (106,) | dtype = float64
  Dataset /units/unit_dv_location (VectorData) um from dura; ventral is positive; based on manipulator coordinates (or histology) & probe config | shape = (106,) | dtype = float64
  Dataset /units/unit_ml_location (VectorData) um from ref; right is positive; based on manipulator coordinates (or histology) & probe config | shape = (106,) | dtype = float64
  Dataset /units/waveform_amplitude (VectorData) unit amplitude (peak) in microvolts | shape = (106,) | dtype = float64
  Dataset /units/waveform_mean (VectorData) the spike waveform mean for each spike unit | shape = (106, 1, 42) | dtype = float64
  Dataset /units/waveform_sd (VectorData) the spike waveform standard deviation for each spike unit | shape = (106, 1, 42) | dtype = float64
