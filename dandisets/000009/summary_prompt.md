
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000009/0.220126.1903
name: Maintenance of persistent activity in a frontal thalamocortical loop
contributor: [{'name': 'Guo, Zengcai', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-4140-7961', 'includeInCitation': True}, {'name': 'Inagaki, Hidehiko', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0003-4580-2763', 'includeInCitation': True}, {'name': 'Daie, Kayvon', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Druckmann, Shaul', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0003-0068-3377', 'includeInCitation': True}, {'name': 'Gerfen, Charles R.', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0001-9008-4882', 'includeInCitation': True}, {'name': 'Svoboda, Karel', 'roleName': ['dcite:Author', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0002-6670-7362', 'includeInCitation': True}]
description: We recorded spikes from the ALM and thalamus during tactile discrimination  with a delayed directional response. Here we show that, similar to ALM  neurons, thalamic neurons exhibited selective persistent delay activity  that predicted movement direction. Unilateral photoinhibition of delay  activity in the ALM or thalamus produced contralesional neglect.  Photoinhibition of the thalamus caused a short-latency and near-complete  collapse of ALM activity. Similarly, photoinhibition of the ALM diminished  thalamic activity. Our results show that the thalamus is a circuit hub in  motor preparation and suggest that persistent activity requires reciprocal  excitation across multiple brain areas.
assetsSummary: {'species': [{'name': 'House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}, {'name': 'behavioral approach', 'schemaKey': 'ApproachType'}, {'name': 'optogenetic approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 12919706852, 'numberOfFiles': 173, 'numberOfSubjects': 31, 'variableMeasured': ['Units', 'ElectrodeGroup', 'ProcessingModule', 'BehavioralTimeSeries', 'CurrentClampStimulusSeries', 'OptogeneticSeries'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'current clamp technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000009 has 100 NWB files.
21 of these NWB files are of type 1.
66 of these NWB files are of type 2.
13 of these NWB files are of type 3.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2019-10-07T15:08:04.665804-05:00']
  Group /general/devices/ADunit (Device) 
  experiment_description: 
  experimenter: ['Zengcai Guo']
  Group /general/extracellular_ephys/ADunit: 32 (ElectrodeGroup) N/A
  Group /general/extracellular_ephys/ADunit: 32/device (Device) 
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
  institution: Janelia Research Campus
  keywords: ['anterior lateral motor cortex' 'thalamus' 'persistent activity'
   'optogenetic perturbations' 'extracellular electrophysiology'
   'intracellular electrophysiology']
  related_publications: ['doi:10.1038/nature22324']
  Group /general/subject (Subject) 
  identifier: anm00229327_2017-06-27_09-34-38
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/cue_end_time (VectorData) offset of auditory cue | shape = (320,) | dtype = float64
  Dataset /intervals/trials/cue_start_time (VectorData) onset of auditory cue | shape = (320,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (320,) | dtype = int32
  Dataset /intervals/trials/is_good (VectorData) is this a good or bad trial | shape = (320,) | dtype = int32
  Dataset /intervals/trials/photo_loc_galvo_x (VectorData) (mm) photostim coordinates field | shape = (320,) | dtype = float64
  Dataset /intervals/trials/photo_loc_galvo_y (VectorData) (mm) photostim coordinates field | shape = (320,) | dtype = float64
  Dataset /intervals/trials/photo_loc_galvo_z (VectorData) (mm) photostim coordinates field | shape = (320,) | dtype = float64
  Dataset /intervals/trials/photo_stim_period (VectorData)  | shape = (320,) | dtype = object
  Dataset /intervals/trials/photo_stim_power (VectorData) (mW) stimulation power | shape = (320,) | dtype = float64
  Dataset /intervals/trials/photo_stim_type (VectorData)  | shape = (320,) | dtype = object
  Dataset /intervals/trials/pole_in_time (VectorData) onset of pole moving in | shape = (320,) | dtype = float64
  Dataset /intervals/trials/pole_out_time (VectorData) onset of pole moving out | shape = (320,) | dtype = float64
  Dataset /intervals/trials/response (VectorData)  | shape = (320,) | dtype = object
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (320,) | dtype = float64
  Dataset /intervals/trials/stim_present (VectorData) is this a stim or no-stim trial | shape = (320,) | dtype = int32
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (320,) | dtype = float64
  Dataset /intervals/trials/type (VectorData)  | shape = (320,) | dtype = object
  session_description: Extracellular ephys recording of mouse doing discrimination task(lick left/right), with optogenetic stimulation plus pole and auditory stimulus
  session_start_time: 2017-06-27T09:34:38-05:00
  timestamps_reference_time: 2017-06-27T09:34:38-05:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/cell_type (VectorData) cell type (e.g. wide width, narrow width spiking) | shape = (8,) | dtype = object
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (8,) | dtype = int32
  Dataset /units/electrodes_index (VectorIndex)  | shape = (8,) | dtype = int32
  Dataset /units/id (ElementIdentifiers)  | shape = (8,) | dtype = int32
  Dataset /units/sampling_rate (VectorData) Sampling rate of the raw voltage traces (Hz) | shape = (8,) | dtype = int32
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (149434,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex)  | shape = (8,) | dtype = int32
  Dataset /units/unit_x (VectorData) x-coordinate of this unit (mm) | shape = (8,) | dtype = float64
  Dataset /units/unit_y (VectorData) y-coordinate of this unit (mm) | shape = (8,) | dtype = float64
  Dataset /units/unit_z (VectorData) z-coordinate of this unit (mm) | shape = (8,) | dtype = float64
  Dataset /units/waveform_mean (VectorData) the spike waveform mean for each spike unit | shape = (8, 29) | dtype = float32
  Dataset /units/waveform_sd (VectorData) the spike waveform standard deviation for each spike unit | shape = (8, 29) | dtype = float32


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2019-10-07T15:09:20.486688-05:00']
  Group /general/devices/ADunit (Device) 
  Group /general/devices/laser (Device) 
  experiment_description: 
  experimenter: ['Zengcai Guo']
  Group /general/extracellular_ephys/ADunit: 32 (ElectrodeGroup) N/A
  Group /general/extracellular_ephys/ADunit: 32/device (Device) 
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
  institution: Janelia Research Campus
  keywords: ['anterior lateral motor cortex' 'thalamus' 'persistent activity'
   'optogenetic perturbations' 'extracellular electrophysiology'
   'intracellular electrophysiology']
  Group /general/optogenetics/left-ALM (OptogeneticStimulusSite) 
  Group /general/optogenetics/left-ALM/device (Device) 
  related_publications: ['doi:10.1038/nature22324']
  Group /general/subject (Subject) 
  identifier: anm00234218_2017-06-27_09-35-21
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/cue_end_time (VectorData) offset of auditory cue | shape = (445,) | dtype = float64
  Dataset /intervals/trials/cue_start_time (VectorData) onset of auditory cue | shape = (445,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (445,) | dtype = int32
  Dataset /intervals/trials/is_good (VectorData) is this a good or bad trial | shape = (445,) | dtype = int32
  Dataset /intervals/trials/photo_loc_galvo_x (VectorData) (mm) photostim coordinates field | shape = (445,) | dtype = float64
  Dataset /intervals/trials/photo_loc_galvo_y (VectorData) (mm) photostim coordinates field | shape = (445,) | dtype = float64
  Dataset /intervals/trials/photo_loc_galvo_z (VectorData) (mm) photostim coordinates field | shape = (445,) | dtype = float64
  Dataset /intervals/trials/photo_stim_period (VectorData)  | shape = (445,) | dtype = object
  Dataset /intervals/trials/photo_stim_power (VectorData) (mW) stimulation power | shape = (445,) | dtype = float64
  Dataset /intervals/trials/photo_stim_type (VectorData)  | shape = (445,) | dtype = object
  Dataset /intervals/trials/pole_in_time (VectorData) onset of pole moving in | shape = (445,) | dtype = float64
  Dataset /intervals/trials/pole_out_time (VectorData) onset of pole moving out | shape = (445,) | dtype = float64
  Dataset /intervals/trials/response (VectorData)  | shape = (445,) | dtype = object
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (445,) | dtype = float64
  Dataset /intervals/trials/stim_present (VectorData) is this a stim or no-stim trial | shape = (445,) | dtype = int32
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (445,) | dtype = float64
  Dataset /intervals/trials/type (VectorData)  | shape = (445,) | dtype = object
  session_description: Extracellular ephys recording of mouse doing discrimination task(lick left/right), with optogenetic stimulation plus pole and auditory stimulus
  session_start_time: 2017-06-27T09:35:21-05:00
  timestamps_reference_time: 2017-06-27T09:35:21-05:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/cell_type (VectorData) cell type (e.g. wide width, narrow width spiking) | shape = (10,) | dtype = object
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (10,) | dtype = int32
  Dataset /units/electrodes_index (VectorIndex)  | shape = (10,) | dtype = int32
  Dataset /units/id (ElementIdentifiers)  | shape = (10,) | dtype = int32
  Dataset /units/sampling_rate (VectorData) Sampling rate of the raw voltage traces (Hz) | shape = (10,) | dtype = int32
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (145655,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex)  | shape = (10,) | dtype = int32
  Dataset /units/unit_x (VectorData) x-coordinate of this unit (mm) | shape = (10,) | dtype = float64
  Dataset /units/unit_y (VectorData) y-coordinate of this unit (mm) | shape = (10,) | dtype = float64
  Dataset /units/unit_z (VectorData) z-coordinate of this unit (mm) | shape = (10,) | dtype = float64
  Dataset /units/waveform_mean (VectorData) the spike waveform mean for each spike unit | shape = (10, 29) | dtype = float32
  Dataset /units/waveform_sd (VectorData) the spike waveform standard deviation for each spike unit | shape = (10, 29) | dtype = float32


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2019-10-07T15:17:41.314079-05:00']
  Group /general/devices/ADunit (Device) 
  Group /general/devices/laser (Device) 
  experiment_description: 
  experimenter: ['Zengcai Guo']
  Group /general/extracellular_ephys/ADunit: 32 (ElectrodeGroup) N/A
  Group /general/extracellular_ephys/ADunit: 32/device (Device) 
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
  institution: Janelia Research Campus
  keywords: ['anterior lateral motor cortex' 'thalamus' 'persistent activity'
   'optogenetic perturbations' 'extracellular electrophysiology'
   'intracellular electrophysiology']
  Group /general/optogenetics/left-Thalamus (OptogeneticStimulusSite) 
  Group /general/optogenetics/left-Thalamus/device (Device) 
  related_publications: ['doi:10.1038/nature22324']
  Group /general/subject (Subject) 
  identifier: anm00264942_2017-06-27_09-40-01
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/cue_end_time (VectorData) offset of auditory cue | shape = (242,) | dtype = float64
  Dataset /intervals/trials/cue_start_time (VectorData) onset of auditory cue | shape = (242,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (242,) | dtype = int32
  Dataset /intervals/trials/is_good (VectorData) is this a good or bad trial | shape = (242,) | dtype = int32
  Dataset /intervals/trials/photo_loc_galvo_x (VectorData) (mm) photostim coordinates field | shape = (242,) | dtype = float64
  Dataset /intervals/trials/photo_loc_galvo_y (VectorData) (mm) photostim coordinates field | shape = (242,) | dtype = float64
  Dataset /intervals/trials/photo_loc_galvo_z (VectorData) (mm) photostim coordinates field | shape = (242,) | dtype = float64
  Dataset /intervals/trials/photo_stim_period (VectorData)  | shape = (242,) | dtype = object
  Dataset /intervals/trials/photo_stim_power (VectorData) (mW) stimulation power | shape = (242,) | dtype = float64
  Dataset /intervals/trials/photo_stim_type (VectorData)  | shape = (242,) | dtype = object
  Dataset /intervals/trials/pole_in_time (VectorData) onset of pole moving in | shape = (242,) | dtype = float64
  Dataset /intervals/trials/pole_out_time (VectorData) onset of pole moving out | shape = (242,) | dtype = float64
  Dataset /intervals/trials/response (VectorData)  | shape = (242,) | dtype = object
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (242,) | dtype = float64
  Dataset /intervals/trials/stim_present (VectorData) is this a stim or no-stim trial | shape = (242,) | dtype = int32
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (242,) | dtype = float64
  Dataset /intervals/trials/type (VectorData)  | shape = (242,) | dtype = object
  session_description: Extracellular ephys recording of mouse doing discrimination task(lick left/right), with optogenetic stimulation plus pole and auditory stimulus
  session_start_time: 2017-06-27T09:40:01-05:00
  timestamps_reference_time: 2017-06-27T09:40:01-05:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/cell_type (VectorData) cell type (e.g. wide width, narrow width spiking) | shape = (22,) | dtype = object
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (22,) | dtype = int32
  Dataset /units/electrodes_index (VectorIndex)  | shape = (22,) | dtype = int32
  Dataset /units/id (ElementIdentifiers)  | shape = (22,) | dtype = int32
  Dataset /units/sampling_rate (VectorData) Sampling rate of the raw voltage traces (Hz) | shape = (22,) | dtype = int32
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (91105,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex)  | shape = (22,) | dtype = int32
  Dataset /units/unit_x (VectorData) x-coordinate of this unit (mm) | shape = (22,) | dtype = float64
  Dataset /units/unit_y (VectorData) y-coordinate of this unit (mm) | shape = (22,) | dtype = float64
  Dataset /units/unit_z (VectorData) z-coordinate of this unit (mm) | shape = (22,) | dtype = float64
  Dataset /units/waveform_mean (VectorData) the spike waveform mean for each spike unit | shape = (22, 38) | dtype = float32
  Dataset /units/waveform_sd (VectorData) the spike waveform standard deviation for each spike unit | shape = (22, 38) | dtype = float32
