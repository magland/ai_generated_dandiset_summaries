
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000011/0.220126.1907
name: Robust neuronal dynamics in premotor cortex during motor planning
contributor: [{'name': 'Li, Nuo', 'roleName': ['dcite:Author', 'dcite:DataCollector'], 'schemaKey': 'Person', 'identifier': '0000-0002-6613-5018', 'affiliation': [{'name': 'Janelia Research Campus, Howard Hughes Medical Institute', 'schemaKey': 'Affiliation', 'includeInCitation': False}], 'includeInCitation': True}, {'name': 'Daie, Kayvon', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [{'name': 'Janelia Research Campus, Howard Hughes Medical Institute', 'schemaKey': 'Affiliation', 'includeInCitation': False}], 'includeInCitation': True}, {'name': 'Svoboda, Karel', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [{'name': 'Janelia Research Campus, Howard Hughes Medical Institute', 'schemaKey': 'Affiliation', 'includeInCitation': False}], 'includeInCitation': True}, {'name': 'Druckmann, Shaul', 'roleName': ['dcite:Author', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0003-0068-3377', 'affiliation': [{'name': 'Janelia Research Campus, Howard Hughes Medical Institute', 'roleName': [], 'schemaKey': 'Affiliation', 'contactPoint': [], 'includeInCitation': False}], 'includeInCitation': True}]
description: Data from "Robust neuronal dynamics in premotor cortex during motor planning" Nature 2016
assetsSummary: {'species': [{'name': 'House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}, {'name': 'behavioral approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 32435325542, 'numberOfFiles': 92, 'numberOfSubjects': 19, 'variableMeasured': ['BehavioralEvents', 'ElectrodeGroup', 'Units', 'BehavioralTimeSeries'], 'measurementTechnique': [{'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000011 has 45 NWB files.
3 of these NWB files are of type 1.
1 of these NWB files are of type 2.
17 of these NWB files are of type 3.
19 of these NWB files are of type 4.
5 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/BehavioralEvents (BehavioralEvents) 
  Group /acquisition/BehavioralEvents/delay (TimeSeries) no description
  Group /acquisition/BehavioralEvents/go (TimeSeries) no description
  Group /acquisition/BehavioralEvents/sample (TimeSeries) no description
  Group /acquisition/BehavioralTimeSeries (BehavioralTimeSeries) 
  Group /acquisition/BehavioralTimeSeries/lick_trace (TimeSeries) Time-series of the animal's tongue movement when licking
  file_create_date: ['2020-02-20T15:28:02.794325-06:00']
  Group /general/devices/A4x8-5mm-100-200-177 (Device) 
  Group /general/devices/LaserCoboltMambo100 (Device) 
  experiment_description: Extracellular electrophysiology recordings with optogenetic perturbations performed on anterior lateral region of the mouse cortex during object location discrimination task
  experimenter: ['Nuo Li']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (32,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (32,) | dtype = float64
  Group /general/extracellular_ephys/silicon32_g0 (ElectrodeGroup) N/A
  Group /general/extracellular_ephys/silicon32_g0/device (Device) 
  institution: Janelia Research Campus
  keywords: ['motor planning' 'premotor cortex' 'whiskers' 'optogenetic perturbations'
   'extracellular electrophysiology']
  Group /general/optogenetics/left ALM (OptogeneticStimulusSite) 
  Group /general/optogenetics/left ALM/device (Device) 
  related_publications: ['doi:10.1038/nature17643']
  Group /general/subject (Subject) 
  virus: []
  identifier: ANM255200_2014-09-10_2
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/early_lick (VectorData) varchar(32) # | shape = (288,) | dtype = object
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (288,) | dtype = int32
  Dataset /intervals/trials/outcome (VectorData) varchar(32) # | shape = (288,) | dtype = object
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (288,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (288,) | dtype = float64
  Dataset /intervals/trials/task (VectorData) varchar(12) # task type | shape = (288,) | dtype = object
  Dataset /intervals/trials/task_protocol (VectorData) tinyint # task protocol | shape = (288,) | dtype = int32
  Dataset /intervals/trials/trial_instruction (VectorData) varchar(16) # | shape = (288,) | dtype = object
  session_description: 
  session_start_time: 2014-09-10T00:00:00-05:00
  timestamps_reference_time: 2014-09-10T00:00:00-05:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/cell_type (VectorData) cell type (e.g. fast spiking or pyramidal) | shape = (15,) | dtype = object
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (15,) | dtype = object
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (15,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex)  | shape = (15,) | dtype = int32
  Dataset /units/id (ElementIdentifiers)  | shape = (15,) | dtype = int32
  Dataset /units/obs_intervals (VectorData) the observation intervals for each unit | shape = (3810, 2) | dtype = float64
  Dataset /units/obs_intervals_index (VectorIndex)  | shape = (15,) | dtype = int32
  Dataset /units/posx (VectorData) estimated x position of the unit relative to probe (0,0) (um) | shape = (15,) | dtype = float64
  Dataset /units/posy (VectorData) estimated y position of the unit relative to probe (0,0) (um) | shape = (15,) | dtype = float64
  Dataset /units/quality (VectorData) unit quality from clustering | shape = (15,) | dtype = object
  Dataset /units/sampling_rate (VectorData) Sampling rate of the raw voltage traces (Hz) | shape = (15,) | dtype = float64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (117243,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex)  | shape = (15,) | dtype = int32
  Dataset /units/waveform_mean (VectorData) the spike waveform mean for each spike unit | shape = (15, 29) | dtype = float64
  Dataset /units/waveform_sd (VectorData) the spike waveform standard deviation for each spike unit | shape = (15, 29) | dtype = float64


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/BehavioralEvents (BehavioralEvents) 
  file_create_date: ['2020-02-20T15:28:01.342325-06:00']
  experiment_description: Extracellular electrophysiology recordings with optogenetic perturbations performed on anterior lateral region of the mouse cortex during object location discrimination task
  experimenter: ['Nuo Li']
  institution: Janelia Research Campus
  keywords: ['motor planning' 'premotor cortex' 'whiskers' 'optogenetic perturbations'
   'extracellular electrophysiology']
  related_publications: ['doi:10.1038/nature17643']
  Group /general/subject (Subject) 
  virus: []
  identifier: ANM255200_2014-09-10_1
  session_description: 
  session_start_time: 2014-09-10T00:00:00-05:00
  timestamps_reference_time: 2014-09-10T00:00:00-05:00


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/BehavioralEvents (BehavioralEvents) 
  Group /acquisition/BehavioralEvents/delay (TimeSeries) no description
  Group /acquisition/BehavioralEvents/go (TimeSeries) no description
  Group /acquisition/BehavioralEvents/photostim_start_time (TimeSeries) no description
  Group /acquisition/BehavioralEvents/photostim_stop_time (TimeSeries) no description
  Group /acquisition/BehavioralEvents/sample (TimeSeries) no description
  Group /acquisition/BehavioralTimeSeries (BehavioralTimeSeries) 
  Group /acquisition/BehavioralTimeSeries/lick_trace (TimeSeries) Time-series of the animal's tongue movement when licking
  file_create_date: ['2020-02-20T15:28:36.809932-06:00']
  Group /general/devices/A4x8-5mm-100-200-177 (Device) 
  Group /general/devices/LaserCoboltMambo100 (Device) 
  experiment_description: Extracellular electrophysiology recordings with optogenetic perturbations performed on anterior lateral region of the mouse cortex during object location discrimination task
  experimenter: ['Nuo Li']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (32,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (32,) | dtype = float64
  Group /general/extracellular_ephys/silicon32_g0 (ElectrodeGroup) N/A
  Group /general/extracellular_ephys/silicon32_g0/device (Device) 
  institution: Janelia Research Campus
  keywords: ['motor planning' 'premotor cortex' 'whiskers' 'optogenetic perturbations'
   'extracellular electrophysiology']
  Group /general/optogenetics/left ALM (OptogeneticStimulusSite) 
  Group /general/optogenetics/left ALM/device (Device) 
  related_publications: ['doi:10.1038/nature17643']
  Group /general/subject (Subject) 
  virus: []
  identifier: ANM255200_2014-09-13_5
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/early_lick (VectorData) varchar(32) # | shape = (413,) | dtype = object
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (413,) | dtype = int32
  Dataset /intervals/trials/outcome (VectorData) varchar(32) # | shape = (413,) | dtype = object
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (413,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (413,) | dtype = float64
  Dataset /intervals/trials/task (VectorData) varchar(12) # task type | shape = (413,) | dtype = object
  Dataset /intervals/trials/task_protocol (VectorData) tinyint # task protocol | shape = (413,) | dtype = int32
  Dataset /intervals/trials/trial_instruction (VectorData) varchar(16) # | shape = (413,) | dtype = object
  session_description: 
  session_start_time: 2014-09-13T00:00:00-05:00
  Group /stimulus/presentation/left ALM_aom_input_trace (OptogeneticSeries) no description
  Group /stimulus/presentation/left ALM_aom_input_trace/site (OptogeneticStimulusSite) 
  Group /stimulus/presentation/left ALM_aom_input_trace/site/device (Device) 
  Group /stimulus/presentation/left ALM_laser_power (OptogeneticSeries) no description
  Group /stimulus/presentation/left ALM_laser_power/site (OptogeneticStimulusSite) 
  Group /stimulus/presentation/left ALM_laser_power/site/device (Device) 
  timestamps_reference_time: 2014-09-13T00:00:00-05:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/cell_type (VectorData) cell type (e.g. fast spiking or pyramidal) | shape = (11,) | dtype = object
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (11,) | dtype = object
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (11,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex)  | shape = (11,) | dtype = int32
  Dataset /units/id (ElementIdentifiers)  | shape = (11,) | dtype = int32
  Dataset /units/obs_intervals (VectorData) the observation intervals for each unit | shape = (4224, 2) | dtype = float64
  Dataset /units/obs_intervals_index (VectorIndex)  | shape = (11,) | dtype = int32
  Dataset /units/posx (VectorData) estimated x position of the unit relative to probe (0,0) (um) | shape = (11,) | dtype = float64
  Dataset /units/posy (VectorData) estimated y position of the unit relative to probe (0,0) (um) | shape = (11,) | dtype = float64
  Dataset /units/quality (VectorData) unit quality from clustering | shape = (11,) | dtype = object
  Dataset /units/sampling_rate (VectorData) Sampling rate of the raw voltage traces (Hz) | shape = (11,) | dtype = float64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (48295,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex)  | shape = (11,) | dtype = int32
  Dataset /units/waveform_mean (VectorData) the spike waveform mean for each spike unit | shape = (11, 29) | dtype = float64
  Dataset /units/waveform_sd (VectorData) the spike waveform standard deviation for each spike unit | shape = (11, 29) | dtype = float64


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/BehavioralEvents (BehavioralEvents) 
  Group /acquisition/BehavioralEvents/delay (TimeSeries) no description
  Group /acquisition/BehavioralEvents/go (TimeSeries) no description
  Group /acquisition/BehavioralEvents/photostim_start_time (TimeSeries) no description
  Group /acquisition/BehavioralEvents/photostim_stop_time (TimeSeries) no description
  Group /acquisition/BehavioralEvents/sample (TimeSeries) no description
  Group /acquisition/BehavioralTimeSeries (BehavioralTimeSeries) 
  Group /acquisition/BehavioralTimeSeries/lick_trace (TimeSeries) Time-series of the animal's tongue movement when licking
  file_create_date: ['2020-02-20T15:31:03.516016-06:00']
  Group /general/devices/A4x8-5mm-100-200-177 (Device) 
  Group /general/devices/LaserCoboltMambo100 (Device) 
  experiment_description: Extracellular electrophysiology recordings with optogenetic perturbations performed on anterior lateral region of the mouse cortex during object location discrimination task
  experimenter: ['Nuo Li']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (32,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (32,) | dtype = float64
  Group /general/extracellular_ephys/silicon32_g0 (ElectrodeGroup) N/A
  Group /general/extracellular_ephys/silicon32_g0/device (Device) 
  institution: Janelia Research Campus
  keywords: ['motor planning' 'premotor cortex' 'whiskers' 'optogenetic perturbations'
   'extracellular electrophysiology']
  Group /general/optogenetics/bilateral ALM (OptogeneticStimulusSite) 
  Group /general/optogenetics/bilateral ALM/device (Device) 
  Group /general/optogenetics/left ALM (OptogeneticStimulusSite) 
  Group /general/optogenetics/left ALM/device (Device) 
  Group /general/optogenetics/right ALM (OptogeneticStimulusSite) 
  Group /general/optogenetics/right ALM/device (Device) 
  related_publications: ['doi:10.1038/nature17643']
  Group /general/subject (Subject) 
  virus: []
  identifier: ANM255201_2014-11-21_2
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/early_lick (VectorData) varchar(32) # | shape = (270,) | dtype = object
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (270,) | dtype = int32
  Dataset /intervals/trials/outcome (VectorData) varchar(32) # | shape = (270,) | dtype = object
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (270,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (270,) | dtype = float64
  Dataset /intervals/trials/task (VectorData) varchar(12) # task type | shape = (270,) | dtype = object
  Dataset /intervals/trials/task_protocol (VectorData) tinyint # task protocol | shape = (270,) | dtype = int32
  Dataset /intervals/trials/trial_instruction (VectorData) varchar(16) # | shape = (270,) | dtype = object
  session_description: 
  session_start_time: 2014-11-21T00:00:00-06:00
  Group /stimulus/presentation/bilateral ALM_aom_input_trace (OptogeneticSeries) no description
  Group /stimulus/presentation/bilateral ALM_aom_input_trace/site (OptogeneticStimulusSite) 
  Group /stimulus/presentation/bilateral ALM_aom_input_trace/site/device (Device) 
  Group /stimulus/presentation/bilateral ALM_laser_power (OptogeneticSeries) no description
  Group /stimulus/presentation/bilateral ALM_laser_power/site (OptogeneticStimulusSite) 
  Group /stimulus/presentation/bilateral ALM_laser_power/site/device (Device) 
  Group /stimulus/presentation/left ALM_aom_input_trace (OptogeneticSeries) no description
  Group /stimulus/presentation/left ALM_aom_input_trace/site (OptogeneticStimulusSite) 
  Group /stimulus/presentation/left ALM_aom_input_trace/site/device (Device) 
  Group /stimulus/presentation/left ALM_laser_power (OptogeneticSeries) no description
  Group /stimulus/presentation/left ALM_laser_power/site (OptogeneticStimulusSite) 
  Group /stimulus/presentation/left ALM_laser_power/site/device (Device) 
  Group /stimulus/presentation/right ALM_aom_input_trace (OptogeneticSeries) no description
  Group /stimulus/presentation/right ALM_aom_input_trace/site (OptogeneticStimulusSite) 
  Group /stimulus/presentation/right ALM_aom_input_trace/site/device (Device) 
  Group /stimulus/presentation/right ALM_laser_power (OptogeneticSeries) no description
  Group /stimulus/presentation/right ALM_laser_power/site (OptogeneticStimulusSite) 
  Group /stimulus/presentation/right ALM_laser_power/site/device (Device) 
  timestamps_reference_time: 2014-11-21T00:00:00-06:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/cell_type (VectorData) cell type (e.g. fast spiking or pyramidal) | shape = (17,) | dtype = object
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (17,) | dtype = object
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (17,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex)  | shape = (17,) | dtype = int32
  Dataset /units/id (ElementIdentifiers)  | shape = (17,) | dtype = int32
  Dataset /units/obs_intervals (VectorData) the observation intervals for each unit | shape = (4182, 2) | dtype = float64
  Dataset /units/obs_intervals_index (VectorIndex)  | shape = (17,) | dtype = int32
  Dataset /units/posx (VectorData) estimated x position of the unit relative to probe (0,0) (um) | shape = (17,) | dtype = float64
  Dataset /units/posy (VectorData) estimated y position of the unit relative to probe (0,0) (um) | shape = (17,) | dtype = float64
  Dataset /units/quality (VectorData) unit quality from clustering | shape = (17,) | dtype = object
  Dataset /units/sampling_rate (VectorData) Sampling rate of the raw voltage traces (Hz) | shape = (17,) | dtype = float64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (101613,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex)  | shape = (17,) | dtype = int32
  Dataset /units/waveform_mean (VectorData) the spike waveform mean for each spike unit | shape = (17, 29) | dtype = float64
  Dataset /units/waveform_sd (VectorData) the spike waveform standard deviation for each spike unit | shape = (17, 29) | dtype = float64


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  Group /acquisition/BehavioralEvents (BehavioralEvents) 
  Group /acquisition/BehavioralEvents/delay (TimeSeries) no description
  Group /acquisition/BehavioralEvents/go (TimeSeries) no description
  Group /acquisition/BehavioralEvents/sample (TimeSeries) no description
  Group /acquisition/BehavioralTimeSeries (BehavioralTimeSeries) 
  Group /acquisition/BehavioralTimeSeries/lick_trace (TimeSeries) Time-series of the animal's tongue movement when licking
  file_create_date: ['2020-02-20T16:15:39.013017-06:00']
  Group /general/devices/A4x8-5mm-100-200-177 (Device) 
  Group /general/devices/LaserCoboltMambo100 (Device) 
  experiment_description: Extracellular electrophysiology recordings with optogenetic perturbations performed on anterior lateral region of the mouse cortex during object location discrimination task
  experimenter: ['Nuo Li']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (32,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (32,) | dtype = float64
  Group /general/extracellular_ephys/silicon32_g0 (ElectrodeGroup) N/A
  Group /general/extracellular_ephys/silicon32_g0/device (Device) 
  institution: Janelia Research Campus
  keywords: ['motor planning' 'premotor cortex' 'whiskers' 'optogenetic perturbations'
   'extracellular electrophysiology']
  Group /general/optogenetics/bilateral ALM (OptogeneticStimulusSite) 
  Group /general/optogenetics/bilateral ALM/device (Device) 
  Group /general/optogenetics/left ALM (OptogeneticStimulusSite) 
  Group /general/optogenetics/left ALM/device (Device) 
  Group /general/optogenetics/right ALM (OptogeneticStimulusSite) 
  Group /general/optogenetics/right ALM/device (Device) 
  related_publications: ['doi:10.1038/nature17643']
  Group /general/subject (Subject) 
  virus: []
  identifier: ANM297634_2015-09-07_1
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/early_lick (VectorData) varchar(32) # | shape = (344,) | dtype = object
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (344,) | dtype = int32
  Dataset /intervals/trials/outcome (VectorData) varchar(32) # | shape = (344,) | dtype = object
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (344,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (344,) | dtype = float64
  Dataset /intervals/trials/task (VectorData) varchar(12) # task type | shape = (344,) | dtype = object
  Dataset /intervals/trials/task_protocol (VectorData) tinyint # task protocol | shape = (344,) | dtype = int32
  Dataset /intervals/trials/trial_instruction (VectorData) varchar(16) # | shape = (344,) | dtype = object
  session_description: 
  session_start_time: 2015-09-07T00:00:00-05:00
  timestamps_reference_time: 2015-09-07T00:00:00-05:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/cell_type (VectorData) cell type (e.g. fast spiking or pyramidal) | shape = (22,) | dtype = object
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (22,) | dtype = object
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (22,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex)  | shape = (22,) | dtype = int32
  Dataset /units/id (ElementIdentifiers)  | shape = (22,) | dtype = int32
  Dataset /units/obs_intervals (VectorData) the observation intervals for each unit | shape = (4730, 2) | dtype = float64
  Dataset /units/obs_intervals_index (VectorIndex)  | shape = (22,) | dtype = int32
  Dataset /units/posx (VectorData) estimated x position of the unit relative to probe (0,0) (um) | shape = (22,) | dtype = float64
  Dataset /units/posy (VectorData) estimated y position of the unit relative to probe (0,0) (um) | shape = (22,) | dtype = float64
  Dataset /units/quality (VectorData) unit quality from clustering | shape = (22,) | dtype = object
  Dataset /units/sampling_rate (VectorData) Sampling rate of the raw voltage traces (Hz) | shape = (22,) | dtype = float64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (69886,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex)  | shape = (22,) | dtype = int32
  Dataset /units/waveform_mean (VectorData) the spike waveform mean for each spike unit | shape = (22, 37) | dtype = float64
  Dataset /units/waveform_sd (VectorData) the spike waveform standard deviation for each spike unit | shape = (22, 37) | dtype = float64
