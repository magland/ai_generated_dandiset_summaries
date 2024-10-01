
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000005/0.220126.1853
name: Electrophysiology data from thalamic and cortical neurons during somatosensation
contributor: [{'name': 'Yu, Jianing', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [{'name': 'Janelia Research Campus, Howard Hughes Medical Institute', 'schemaKey': 'Affiliation', 'includeInCitation': False}], 'includeInCitation': True}, {'name': 'Gutnisky, Diego A', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [{'name': 'Janelia Research Campus, Howard Hughes Medical Institute', 'schemaKey': 'Affiliation', 'includeInCitation': False}], 'includeInCitation': True}, {'name': 'Hires, S Andrew', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [{'name': 'Janelia Research Campus, Howard Hughes Medical Institute', 'schemaKey': 'Affiliation', 'includeInCitation': False}], 'includeInCitation': True}, {'name': 'Svoboda, Karel', 'roleName': ['dcite:Author', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0002-6670-7362', 'affiliation': [{'name': 'Janelia Research Campus, Howard Hughes Medical Institute', 'roleName': [], 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/013sk6x84', 'contactPoint': [], 'includeInCitation': False}], 'includeInCitation': True}]
description: intracellular and extracellular electrophysiology recordings performed on mouse barrel cortex and ventral posterolateral nucleus (vpm) in whisker-based object locating task.
assetsSummary: {'species': [{'name': 'House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}, {'name': 'optogenetic approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 46436686324, 'numberOfFiles': 148, 'numberOfSubjects': 55, 'variableMeasured': ['CurrentClampStimulusSeries', 'CurrentClampSeries', 'OptogeneticSeries', 'ElectrodeGroup', 'Units'], 'measurementTechnique': [{'name': 'current clamp technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000005 has 6 NWB files.
2 of these NWB files are of type 1.
1 of these NWB files are of type 2.
1 of these NWB files are of type 3.
1 of these NWB files are of type 4.
1 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/lick_trace (BehavioralTimeSeries) 
  Group /acquisition/lick_trace/lick_trace (TimeSeries) Binary array of the animal's lick trace
  Group /acquisition/principal_whisker_b2 (BehavioralTimeSeries) 
  Group /acquisition/principal_whisker_b2/pole_available (TimeSeries) binary array of time when the pole is within reach of the whisker
  Group /acquisition/principal_whisker_b2/touch_offset (TimeSeries) binary array of all touch offset times (1 = offset)
  Group /acquisition/principal_whisker_b2/touch_onset (TimeSeries) binary array of all touch onset times (1 = onset)
  Group /acquisition/principal_whisker_b2/whisker_angle (TimeSeries) (degree) the angle of the whisker relative to medialateral axis of the animal
  Group /acquisition/principal_whisker_b2/whisker_curvature (TimeSeries) the change in whisker curvature
  Group /acquisition/whisker_b1 (BehavioralTimeSeries) 
  Group /acquisition/whisker_b1/pole_available (TimeSeries) binary array of time when the pole is within reach of the whisker
  Group /acquisition/whisker_b1/touch_offset (TimeSeries) binary array of all touch offset times (1 = offset)
  Group /acquisition/whisker_b1/touch_onset (TimeSeries) binary array of all touch onset times (1 = onset)
  Group /acquisition/whisker_b1/whisker_angle (TimeSeries) (degree) the angle of the whisker relative to medialateral axis of the animal
  Group /acquisition/whisker_b1/whisker_curvature (TimeSeries) the change in whisker curvature
  Group /acquisition/whisker_beta (BehavioralTimeSeries) 
  Group /acquisition/whisker_beta/pole_available (TimeSeries) binary array of time when the pole is within reach of the whisker
  Group /acquisition/whisker_beta/touch_offset (TimeSeries) binary array of all touch offset times (1 = offset)
  Group /acquisition/whisker_beta/touch_onset (TimeSeries) binary array of all touch onset times (1 = onset)
  Group /acquisition/whisker_beta/whisker_angle (TimeSeries) (degree) the angle of the whisker relative to medialateral axis of the animal
  Group /acquisition/whisker_beta/whisker_curvature (TimeSeries) the change in whisker curvature
  file_create_date: ['2020-03-12T12:16:33.462573-05:00']
  Group /general/devices/4x8_Neuronexus_Z50um_X200um (Device) 
  experiment_description: Intracellular and extracellular electrophysiology recordings performed on mouse barrel cortex and ventral posterolateral nucleus (VPM) in whisker-based object locating task.
  experimenter: ['Diego Gutnisky']
  Group /general/extracellular_ephys/4x8_Neuronexus_Z50um_X200um: 32 (ElectrodeGroup) N/A
  Group /general/extracellular_ephys/4x8_Neuronexus_Z50um_X200um: 32/device (Device) 
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (32,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/reference (VectorData) Description of the reference used for this electrode. | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (32,) | dtype = float64
  institution: Janelia Research Campus
  keywords: ['barrel cortex' 'thalamus' 'whiskers' 'extracellular electrophysiology'
   'intracellular electrophysiology' 'optogenetic perturbations']
  related_publications: ['doi:10.1038/nn.4412']
  Group /general/subject (Subject) 
  identifier: anm184389_2013-02-07_ANM184389_20130207
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/first_lick_time (VectorData) time of first lick | shape = (368,) | dtype = float64
  Dataset /intervals/trials/first_touch_time (VectorData) time of first whisker touch | shape = (368,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (368,) | dtype = int32
  Dataset /intervals/trials/photo_stim_mode (VectorData)  | shape = (368,) | dtype = object
  Dataset /intervals/trials/photo_stim_power (VectorData) (mW) stimulation power | shape = (368,) | dtype = object
  Dataset /intervals/trials/pole_in_time (VectorData) onset of pole moving in | shape = (368,) | dtype = float64
  Dataset /intervals/trials/pole_out_time (VectorData) onset of pole moving out | shape = (368,) | dtype = float64
  Dataset /intervals/trials/pole_pos_time (VectorData) time of recorded pole_position | shape = (368,) | dtype = float64
  Dataset /intervals/trials/pole_position (VectorData) (mm)  the location of the pole along the anteroposterior axis of the animal | shape = (368,) | dtype = float64
  Dataset /intervals/trials/response (VectorData)  | shape = (368,) | dtype = object
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (368,) | dtype = float64
  Dataset /intervals/trials/stim_present (VectorData) is this a stim or no-stim trial | shape = (368,) | dtype = int32
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (368,) | dtype = float64
  Dataset /intervals/trials/type (VectorData)  | shape = (368,) | dtype = object
  session_description: Chronic Silicon probe recordings in VPM during active tactile behavior. Each unit has a particular principal whisker (PW). To align touch or whisker movement parameters take into account which whisker parameter is the PW of a given unit or not.
  session_start_time: 2013-02-07T00:00:00-06:00
  timestamps_reference_time: 2013-02-07T00:00:00-06:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/cell_desc (VectorData) description of this unit (e.g. cell type) | shape = (3,) | dtype = object
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (24,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex)  | shape = (3,) | dtype = int32
  Dataset /units/id (ElementIdentifiers)  | shape = (3,) | dtype = int32
  Dataset /units/obs_intervals (VectorData) the observation intervals for each unit | shape = (3, 2) | dtype = float64
  Dataset /units/obs_intervals_index (VectorIndex)  | shape = (3,) | dtype = int32
  Dataset /units/sampling_rate (VectorData) Sampling rate of the raw voltage traces (Hz) | shape = (3,) | dtype = float64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (72321,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex)  | shape = (3,) | dtype = int32
  Dataset /units/waveform_mean (VectorData) the spike waveform mean for each spike unit | shape = (3, 25, 8) | dtype = float32
  Dataset /units/waveform_sd (VectorData) the spike waveform standard deviation for each spike unit | shape = (3, 25, 8) | dtype = float32


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/lick_trace (BehavioralTimeSeries) 
  Group /acquisition/lick_trace/lick_trace (TimeSeries) Binary array of the animal's lick trace
  Group /acquisition/principal_whisker_beta (BehavioralTimeSeries) 
  Group /acquisition/principal_whisker_beta/pole_available (TimeSeries) binary array of time when the pole is within reach of the whisker
  Group /acquisition/principal_whisker_beta/touch_offset (TimeSeries) binary array of all touch offset times (1 = offset)
  Group /acquisition/principal_whisker_beta/touch_onset (TimeSeries) binary array of all touch onset times (1 = onset)
  Group /acquisition/principal_whisker_beta/whisker_angle (TimeSeries) (degree) the angle of the whisker relative to medialateral axis of the animal
  Group /acquisition/principal_whisker_beta/whisker_curvature (TimeSeries) the change in whisker curvature
  Group /acquisition/whisker_b1 (BehavioralTimeSeries) 
  Group /acquisition/whisker_b1/pole_available (TimeSeries) binary array of time when the pole is within reach of the whisker
  Group /acquisition/whisker_b1/touch_offset (TimeSeries) binary array of all touch offset times (1 = offset)
  Group /acquisition/whisker_b1/touch_onset (TimeSeries) binary array of all touch onset times (1 = onset)
  Group /acquisition/whisker_b1/whisker_angle (TimeSeries) (degree) the angle of the whisker relative to medialateral axis of the animal
  Group /acquisition/whisker_b1/whisker_curvature (TimeSeries) the change in whisker curvature
  Group /acquisition/whisker_b2 (BehavioralTimeSeries) 
  Group /acquisition/whisker_b2/pole_available (TimeSeries) binary array of time when the pole is within reach of the whisker
  Group /acquisition/whisker_b2/touch_offset (TimeSeries) binary array of all touch offset times (1 = offset)
  Group /acquisition/whisker_b2/touch_onset (TimeSeries) binary array of all touch onset times (1 = onset)
  Group /acquisition/whisker_b2/whisker_angle (TimeSeries) (degree) the angle of the whisker relative to medialateral axis of the animal
  Group /acquisition/whisker_b2/whisker_curvature (TimeSeries) the change in whisker curvature
  file_create_date: ['2020-03-12T12:16:45.277751-05:00']
  Group /general/devices/4x8_Neuronexus_Z50um_X200um (Device) 
  experiment_description: Intracellular and extracellular electrophysiology recordings performed on mouse barrel cortex and ventral posterolateral nucleus (VPM) in whisker-based object locating task.
  experimenter: ['Diego Gutnisky']
  Group /general/extracellular_ephys/4x8_Neuronexus_Z50um_X200um: 32 (ElectrodeGroup) N/A
  Group /general/extracellular_ephys/4x8_Neuronexus_Z50um_X200um: 32/device (Device) 
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (32,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/reference (VectorData) Description of the reference used for this electrode. | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (32,) | dtype = float64
  institution: Janelia Research Campus
  keywords: ['barrel cortex' 'thalamus' 'whiskers' 'extracellular electrophysiology'
   'intracellular electrophysiology' 'optogenetic perturbations']
  related_publications: ['doi:10.1038/nn.4412']
  Group /general/subject (Subject) 
  identifier: anm184389_2013-02-11_ANM184389_20130211
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/first_lick_time (VectorData) time of first lick | shape = (542,) | dtype = float64
  Dataset /intervals/trials/first_touch_time (VectorData) time of first whisker touch | shape = (542,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (542,) | dtype = int32
  Dataset /intervals/trials/photo_stim_mode (VectorData)  | shape = (542,) | dtype = object
  Dataset /intervals/trials/photo_stim_power (VectorData) (mW) stimulation power | shape = (542,) | dtype = object
  Dataset /intervals/trials/pole_in_time (VectorData) onset of pole moving in | shape = (542,) | dtype = float64
  Dataset /intervals/trials/pole_out_time (VectorData) onset of pole moving out | shape = (542,) | dtype = float64
  Dataset /intervals/trials/pole_pos_time (VectorData) time of recorded pole_position | shape = (542,) | dtype = float64
  Dataset /intervals/trials/pole_position (VectorData) (mm)  the location of the pole along the anteroposterior axis of the animal | shape = (542,) | dtype = float64
  Dataset /intervals/trials/response (VectorData)  | shape = (542,) | dtype = object
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (542,) | dtype = float64
  Dataset /intervals/trials/stim_present (VectorData) is this a stim or no-stim trial | shape = (542,) | dtype = int32
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (542,) | dtype = float64
  Dataset /intervals/trials/type (VectorData)  | shape = (542,) | dtype = object
  session_description: Chronic Silicon probe recordings in VPM during active tactile behavior. Each unit has a particular principal whisker (PW). To align touch or whisker movement parameters take into account which whisker parameter is the PW of a given unit or not.
  session_start_time: 2013-02-11T00:00:00-06:00
  timestamps_reference_time: 2013-02-11T00:00:00-06:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/cell_desc (VectorData) description of this unit (e.g. cell type) | shape = (2,) | dtype = object
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (16,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex)  | shape = (2,) | dtype = int32
  Dataset /units/id (ElementIdentifiers)  | shape = (2,) | dtype = int32
  Dataset /units/obs_intervals (VectorData) the observation intervals for each unit | shape = (2, 2) | dtype = float64
  Dataset /units/obs_intervals_index (VectorIndex)  | shape = (2,) | dtype = int32
  Dataset /units/sampling_rate (VectorData) Sampling rate of the raw voltage traces (Hz) | shape = (2,) | dtype = float64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (33267,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex)  | shape = (2,) | dtype = int32
  Dataset /units/waveform_mean (VectorData) the spike waveform mean for each spike unit | shape = (2, 25, 8) | dtype = float32
  Dataset /units/waveform_sd (VectorData) the spike waveform standard deviation for each spike unit | shape = (2, 25, 8) | dtype = float32


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/lick_trace (BehavioralTimeSeries) 
  Group /acquisition/lick_trace/lick_trace (TimeSeries) Binary array of the animal's lick trace
  Group /acquisition/principal_whisker_b1 (BehavioralTimeSeries) 
  Group /acquisition/principal_whisker_b1/pole_available (TimeSeries) binary array of time when the pole is within reach of the whisker
  Group /acquisition/principal_whisker_b1/touch_offset (TimeSeries) binary array of all touch offset times (1 = offset)
  Group /acquisition/principal_whisker_b1/touch_onset (TimeSeries) binary array of all touch onset times (1 = onset)
  Group /acquisition/principal_whisker_b1/whisker_angle (TimeSeries) (degree) the angle of the whisker relative to medialateral axis of the animal
  Group /acquisition/principal_whisker_b1/whisker_curvature (TimeSeries) the change in whisker curvature
  Group /acquisition/whisker_b2 (BehavioralTimeSeries) 
  Group /acquisition/whisker_b2/pole_available (TimeSeries) binary array of time when the pole is within reach of the whisker
  Group /acquisition/whisker_b2/touch_offset (TimeSeries) binary array of all touch offset times (1 = offset)
  Group /acquisition/whisker_b2/touch_onset (TimeSeries) binary array of all touch onset times (1 = onset)
  Group /acquisition/whisker_b2/whisker_angle (TimeSeries) (degree) the angle of the whisker relative to medialateral axis of the animal
  Group /acquisition/whisker_b2/whisker_curvature (TimeSeries) the change in whisker curvature
  Group /acquisition/whisker_beta (BehavioralTimeSeries) 
  Group /acquisition/whisker_beta/pole_available (TimeSeries) binary array of time when the pole is within reach of the whisker
  Group /acquisition/whisker_beta/touch_offset (TimeSeries) binary array of all touch offset times (1 = offset)
  Group /acquisition/whisker_beta/touch_onset (TimeSeries) binary array of all touch onset times (1 = onset)
  Group /acquisition/whisker_beta/whisker_angle (TimeSeries) (degree) the angle of the whisker relative to medialateral axis of the animal
  Group /acquisition/whisker_beta/whisker_curvature (TimeSeries) the change in whisker curvature
  file_create_date: ['2020-03-12T12:17:12.885147-05:00']
  Group /general/devices/4x8_Neuronexus_Z50um_X200um (Device) 
  experiment_description: Intracellular and extracellular electrophysiology recordings performed on mouse barrel cortex and ventral posterolateral nucleus (VPM) in whisker-based object locating task.
  experimenter: ['Diego Gutnisky']
  Group /general/extracellular_ephys/4x8_Neuronexus_Z50um_X200um: 32 (ElectrodeGroup) N/A
  Group /general/extracellular_ephys/4x8_Neuronexus_Z50um_X200um: 32/device (Device) 
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (32,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/reference (VectorData) Description of the reference used for this electrode. | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (32,) | dtype = float64
  institution: Janelia Research Campus
  keywords: ['barrel cortex' 'thalamus' 'whiskers' 'extracellular electrophysiology'
   'intracellular electrophysiology' 'optogenetic perturbations']
  related_publications: ['doi:10.1038/nn.4412']
  Group /general/subject (Subject) 
  identifier: anm184389_2013-02-13_ANM184389_20130213
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/first_lick_time (VectorData) time of first lick | shape = (348,) | dtype = float64
  Dataset /intervals/trials/first_touch_time (VectorData) time of first whisker touch | shape = (348,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (348,) | dtype = int32
  Dataset /intervals/trials/photo_stim_mode (VectorData)  | shape = (348,) | dtype = object
  Dataset /intervals/trials/photo_stim_power (VectorData) (mW) stimulation power | shape = (348,) | dtype = object
  Dataset /intervals/trials/pole_in_time (VectorData) onset of pole moving in | shape = (348,) | dtype = float64
  Dataset /intervals/trials/pole_out_time (VectorData) onset of pole moving out | shape = (348,) | dtype = float64
  Dataset /intervals/trials/pole_pos_time (VectorData) time of recorded pole_position | shape = (348,) | dtype = float64
  Dataset /intervals/trials/pole_position (VectorData) (mm)  the location of the pole along the anteroposterior axis of the animal | shape = (348,) | dtype = float64
  Dataset /intervals/trials/response (VectorData)  | shape = (348,) | dtype = object
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (348,) | dtype = float64
  Dataset /intervals/trials/stim_present (VectorData) is this a stim or no-stim trial | shape = (348,) | dtype = int32
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (348,) | dtype = float64
  Dataset /intervals/trials/type (VectorData)  | shape = (348,) | dtype = object
  session_description: Chronic Silicon probe recordings in VPM during active tactile behavior. Each unit has a particular principal whisker (PW). To align touch or whisker movement parameters take into account which whisker parameter is the PW of a given unit or not.
  session_start_time: 2013-02-13T00:00:00-06:00
  timestamps_reference_time: 2013-02-13T00:00:00-06:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/cell_desc (VectorData) description of this unit (e.g. cell type) | shape = (5,) | dtype = object
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (40,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex)  | shape = (5,) | dtype = int32
  Dataset /units/id (ElementIdentifiers)  | shape = (5,) | dtype = int32
  Dataset /units/obs_intervals (VectorData) the observation intervals for each unit | shape = (5, 2) | dtype = float64
  Dataset /units/obs_intervals_index (VectorIndex)  | shape = (5,) | dtype = int32
  Dataset /units/sampling_rate (VectorData) Sampling rate of the raw voltage traces (Hz) | shape = (5,) | dtype = float64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (50194,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex)  | shape = (5,) | dtype = int32
  Dataset /units/waveform_mean (VectorData) the spike waveform mean for each spike unit | shape = (5, 25, 8) | dtype = float32
  Dataset /units/waveform_sd (VectorData) the spike waveform standard deviation for each spike unit | shape = (5, 25, 8) | dtype = float32


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/lick_trace (BehavioralTimeSeries) 
  Group /acquisition/lick_trace/lick_trace (TimeSeries) Binary array of the animal's lick trace
  Group /acquisition/principal_whisker_c1 (BehavioralTimeSeries) 
  Group /acquisition/principal_whisker_c1/pole_available (TimeSeries) binary array of time when the pole is within reach of the whisker
  Group /acquisition/principal_whisker_c1/touch_offset (TimeSeries) binary array of all touch offset times (1 = offset)
  Group /acquisition/principal_whisker_c1/touch_onset (TimeSeries) binary array of all touch onset times (1 = onset)
  Group /acquisition/principal_whisker_c1/whisker_angle (TimeSeries) (degree) the angle of the whisker relative to medialateral axis of the animal
  Group /acquisition/principal_whisker_c1/whisker_curvature (TimeSeries) the change in whisker curvature
  Group /acquisition/whisker_c2 (BehavioralTimeSeries) 
  Group /acquisition/whisker_c2/pole_available (TimeSeries) binary array of time when the pole is within reach of the whisker
  Group /acquisition/whisker_c2/touch_offset (TimeSeries) binary array of all touch offset times (1 = offset)
  Group /acquisition/whisker_c2/touch_onset (TimeSeries) binary array of all touch onset times (1 = onset)
  Group /acquisition/whisker_c2/whisker_angle (TimeSeries) (degree) the angle of the whisker relative to medialateral axis of the animal
  Group /acquisition/whisker_c2/whisker_curvature (TimeSeries) the change in whisker curvature
  Group /acquisition/whisker_c3 (BehavioralTimeSeries) 
  Group /acquisition/whisker_c3/pole_available (TimeSeries) binary array of time when the pole is within reach of the whisker
  Group /acquisition/whisker_c3/touch_offset (TimeSeries) binary array of all touch offset times (1 = offset)
  Group /acquisition/whisker_c3/touch_onset (TimeSeries) binary array of all touch onset times (1 = onset)
  Group /acquisition/whisker_c3/whisker_angle (TimeSeries) (degree) the angle of the whisker relative to medialateral axis of the animal
  Group /acquisition/whisker_c3/whisker_curvature (TimeSeries) the change in whisker curvature
  file_create_date: ['2020-03-12T12:17:23.658515-05:00']
  Group /general/devices/4x8_Neuronexus_Z50um_X200um (Device) 
  experiment_description: Intracellular and extracellular electrophysiology recordings performed on mouse barrel cortex and ventral posterolateral nucleus (VPM) in whisker-based object locating task.
  experimenter: ['Diego Gutnisky']
  Group /general/extracellular_ephys/4x8_Neuronexus_Z50um_X200um: 32 (ElectrodeGroup) N/A
  Group /general/extracellular_ephys/4x8_Neuronexus_Z50um_X200um: 32/device (Device) 
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (32,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/reference (VectorData) Description of the reference used for this electrode. | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (32,) | dtype = float64
  institution: Janelia Research Campus
  keywords: ['barrel cortex' 'thalamus' 'whiskers' 'extracellular electrophysiology'
   'intracellular electrophysiology' 'optogenetic perturbations']
  related_publications: ['doi:10.1038/nn.4412']
  Group /general/subject (Subject) 
  identifier: anm186997_2013-03-17_ANM186997_20130317
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/first_lick_time (VectorData) time of first lick | shape = (372,) | dtype = float64
  Dataset /intervals/trials/first_touch_time (VectorData) time of first whisker touch | shape = (372,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (372,) | dtype = int32
  Dataset /intervals/trials/photo_stim_mode (VectorData)  | shape = (372,) | dtype = object
  Dataset /intervals/trials/photo_stim_power (VectorData) (mW) stimulation power | shape = (372,) | dtype = object
  Dataset /intervals/trials/pole_in_time (VectorData) onset of pole moving in | shape = (372,) | dtype = float64
  Dataset /intervals/trials/pole_out_time (VectorData) onset of pole moving out | shape = (372,) | dtype = float64
  Dataset /intervals/trials/pole_pos_time (VectorData) time of recorded pole_position | shape = (372,) | dtype = float64
  Dataset /intervals/trials/pole_position (VectorData) (mm)  the location of the pole along the anteroposterior axis of the animal | shape = (372,) | dtype = float64
  Dataset /intervals/trials/response (VectorData)  | shape = (372,) | dtype = object
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (372,) | dtype = float64
  Dataset /intervals/trials/stim_present (VectorData) is this a stim or no-stim trial | shape = (372,) | dtype = int32
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (372,) | dtype = float64
  Dataset /intervals/trials/type (VectorData)  | shape = (372,) | dtype = object
  session_description: Chronic Silicon probe recordings in VPM during active tactile behavior. Each unit has a particular principal whisker (PW). To align touch or whisker movement parameters take into account which whisker parameter is the PW of a given unit or not.
  session_start_time: 2013-03-17T00:00:00-05:00
  timestamps_reference_time: 2013-03-17T00:00:00-05:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/cell_desc (VectorData) description of this unit (e.g. cell type) | shape = (1,) | dtype = object
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (8,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex)  | shape = (1,) | dtype = int32
  Dataset /units/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Dataset /units/obs_intervals (VectorData) the observation intervals for each unit | shape = (1, 2) | dtype = float64
  Dataset /units/obs_intervals_index (VectorIndex)  | shape = (1,) | dtype = int32
  Dataset /units/sampling_rate (VectorData) Sampling rate of the raw voltage traces (Hz) | shape = (1,) | dtype = float64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (3176,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex)  | shape = (1,) | dtype = int32
  Dataset /units/waveform_mean (VectorData) the spike waveform mean for each spike unit | shape = (1, 25, 8) | dtype = float32
  Dataset /units/waveform_sd (VectorData) the spike waveform standard deviation for each spike unit | shape = (1, 25, 8) | dtype = float32


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  Group /acquisition/lick_trace (BehavioralTimeSeries) 
  Group /acquisition/lick_trace/lick_trace (TimeSeries) Binary array of the animal's lick trace
  Group /acquisition/principal_whisker_c2 (BehavioralTimeSeries) 
  Group /acquisition/principal_whisker_c2/pole_available (TimeSeries) binary array of time when the pole is within reach of the whisker
  Group /acquisition/principal_whisker_c2/touch_offset (TimeSeries) binary array of all touch offset times (1 = offset)
  Group /acquisition/principal_whisker_c2/touch_onset (TimeSeries) binary array of all touch onset times (1 = onset)
  Group /acquisition/principal_whisker_c2/whisker_angle (TimeSeries) (degree) the angle of the whisker relative to medialateral axis of the animal
  Group /acquisition/principal_whisker_c2/whisker_curvature (TimeSeries) the change in whisker curvature
  Group /acquisition/whisker_c1 (BehavioralTimeSeries) 
  Group /acquisition/whisker_c1/pole_available (TimeSeries) binary array of time when the pole is within reach of the whisker
  Group /acquisition/whisker_c1/touch_offset (TimeSeries) binary array of all touch offset times (1 = offset)
  Group /acquisition/whisker_c1/touch_onset (TimeSeries) binary array of all touch onset times (1 = onset)
  Group /acquisition/whisker_c1/whisker_angle (TimeSeries) (degree) the angle of the whisker relative to medialateral axis of the animal
  Group /acquisition/whisker_c1/whisker_curvature (TimeSeries) the change in whisker curvature
  file_create_date: ['2020-03-12T12:17:34.948805-05:00']
  Group /general/devices/4x8_Neuronexus_Z50um_X200um (Device) 
  experiment_description: Intracellular and extracellular electrophysiology recordings performed on mouse barrel cortex and ventral posterolateral nucleus (VPM) in whisker-based object locating task.
  experimenter: ['Diego Gutnisky']
  Group /general/extracellular_ephys/4x8_Neuronexus_Z50um_X200um: 32 (ElectrodeGroup) N/A
  Group /general/extracellular_ephys/4x8_Neuronexus_Z50um_X200um: 32/device (Device) 
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (32,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/reference (VectorData) Description of the reference used for this electrode. | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (32,) | dtype = float64
  institution: Janelia Research Campus
  keywords: ['barrel cortex' 'thalamus' 'whiskers' 'extracellular electrophysiology'
   'intracellular electrophysiology' 'optogenetic perturbations']
  related_publications: ['doi:10.1038/nn.4412']
  Group /general/subject (Subject) 
  identifier: anm186997_2013-03-21_ANM186997_20130321
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/first_lick_time (VectorData) time of first lick | shape = (329,) | dtype = float64
  Dataset /intervals/trials/first_touch_time (VectorData) time of first whisker touch | shape = (329,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (329,) | dtype = int32
  Dataset /intervals/trials/photo_stim_mode (VectorData)  | shape = (329,) | dtype = object
  Dataset /intervals/trials/photo_stim_power (VectorData) (mW) stimulation power | shape = (329,) | dtype = object
  Dataset /intervals/trials/pole_in_time (VectorData) onset of pole moving in | shape = (329,) | dtype = float64
  Dataset /intervals/trials/pole_out_time (VectorData) onset of pole moving out | shape = (329,) | dtype = float64
  Dataset /intervals/trials/pole_pos_time (VectorData) time of recorded pole_position | shape = (329,) | dtype = float64
  Dataset /intervals/trials/pole_position (VectorData) (mm)  the location of the pole along the anteroposterior axis of the animal | shape = (329,) | dtype = float64
  Dataset /intervals/trials/response (VectorData)  | shape = (329,) | dtype = object
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (329,) | dtype = float64
  Dataset /intervals/trials/stim_present (VectorData) is this a stim or no-stim trial | shape = (329,) | dtype = int32
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (329,) | dtype = float64
  Dataset /intervals/trials/type (VectorData)  | shape = (329,) | dtype = object
  session_description: Chronic Silicon probe recordings in VPM during active tactile behavior. Each unit has a particular principal whisker (PW). To align touch or whisker movement parameters take into account which whisker parameter is the PW of a given unit or not.
  session_start_time: 2013-03-21T00:00:00-05:00
  timestamps_reference_time: 2013-03-21T00:00:00-05:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/cell_desc (VectorData) description of this unit (e.g. cell type) | shape = (1,) | dtype = object
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (8,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex)  | shape = (1,) | dtype = int32
  Dataset /units/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Dataset /units/obs_intervals (VectorData) the observation intervals for each unit | shape = (1, 2) | dtype = float64
  Dataset /units/obs_intervals_index (VectorIndex)  | shape = (1,) | dtype = int32
  Dataset /units/sampling_rate (VectorData) Sampling rate of the raw voltage traces (Hz) | shape = (1,) | dtype = float64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (18797,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex)  | shape = (1,) | dtype = int32
  Dataset /units/waveform_mean (VectorData) the spike waveform mean for each spike unit | shape = (1, 25, 8) | dtype = float32
  Dataset /units/waveform_sd (VectorData) the spike waveform standard deviation for each spike unit | shape = (1, 25, 8) | dtype = float32
