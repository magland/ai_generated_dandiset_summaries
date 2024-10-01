
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000013/0.220126.2143
name: Low-noise encoding of active touch by layer 4 in the somatosensory cortex
contributor: [{'name': 'Hires, Samuel', 'roleName': ['dcite:Author', 'dcite:ContactPerson', 'dcite:DataCollector', 'dcite:DataManager'], 'schemaKey': 'Person', 'identifier': '0000-0003-3498-0388', 'affiliation': [], 'includeInCitation': True}, {'name': 'Gutnisky, Diego', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-8578-0039', 'affiliation': [], 'includeInCitation': True}, {'name': 'Yu, Jianing', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': "O'Connor, Daniel H", 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Svoboda, Karel', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-6670-7362', 'affiliation': [], 'includeInCitation': True}]
description: Data from "Low-noise encoding of active touch by layer 4 in the somatosensory cortex" Hires, Gutnisky et al. Elife 2015
assetsSummary: {'species': [{'name': 'House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}, {'name': 'behavioral approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 11408735292, 'numberOfFiles': 52, 'numberOfSubjects': 23, 'variableMeasured': ['BehavioralTimeSeries', 'CurrentClampSeries', 'PatchClampSeries'], 'measurementTechnique': [{'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'patch clamp technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'current clamp technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000013 has 5 NWB files.
1 of these NWB files are of type 1.
1 of these NWB files are of type 2.
1 of these NWB files are of type 3.
1 of these NWB files are of type 4.
1 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/CurrentClampSeries (CurrentClampSeries) no description
  Group /acquisition/CurrentClampSeries/electrode (IntracellularElectrode) 
  Group /acquisition/CurrentClampSeries/electrode/device (Device) 
  Group /acquisition/SpikeTrain (PatchClampSeries) The data are either 0 or 1, where 1 represents whether a spike was detected at the corresponding timestamp.
  Group /acquisition/SpikeTrain/electrode (IntracellularElectrode) 
  Group /acquisition/SpikeTrain/electrode/device (Device) 
  Group /acquisition/behavior (BehavioralTimeSeries) 
  Group /acquisition/behavior/amplitude (TimeSeries) the amplitude of the Hilbert Transform of theta_at_base
  Group /acquisition/behavior/beam_break_times (TimeSeries) binary array of lick times (1 = onset of spout contact)
  Group /acquisition/behavior/delta_kappa (TimeSeries) the change in whisker curvature following each touch onset
  Group /acquisition/behavior/distance_to_pole (TimeSeries) (mm) the shortest distance from whisker to the pole
  Group /acquisition/behavior/phase (TimeSeries) the phase of the Hilbert Transform of theta_at_base
  Group /acquisition/behavior/pole_available (TimeSeries) binary array of time when the pole is within reach of the whisker
  Group /acquisition/behavior/set_point (TimeSeries) the amplitude of the Hilbert Transform of theta_at_base
  Group /acquisition/behavior/theta_at_base (TimeSeries) (degree) the angle of the whisker base relative to medialateral axis of the animal
  Group /acquisition/behavior/theta_filt (TimeSeries) theta_at_base filtered with 6-60Hz bandpass
  Group /acquisition/behavior/touch_offset (TimeSeries) binary array of all touch offset times (1 = offset)
  Group /acquisition/behavior/touch_onset (TimeSeries) binary array of all touch onset times (1 = onset)
  file_create_date: ['2020-03-09T15:52:06.002599-05:00']
  Group /general/devices/Borosilicate glass (Device) 
  experiment_description: Intracellular and extracellular electrophysiology recordings performed on mouse barrel cortex in object locating task, where whisker movements and contacts with object were tracked to the milisecond precision.
  experimenter: ['Samuel Andrew Hires']
  institution: Janelia Research Campus
  Group /general/intracellular_ephys/AH0040_AAAA (IntracellularElectrode) 
  Group /general/intracellular_ephys/AH0040_AAAA/device (Device) 
  keywords: ['barrel cortex' 'whiskers' 'extracellular electrophysiology'
   'intracellular electrophysiology']
  related_publications: ['doi:10.7554/eLife.06619']
  Group /general/subject (Subject) 
  identifier: anm101105_2010-06-19_Cell46
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/first_lick_time (VectorData) time of first lick | shape = (117,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (117,) | dtype = int32
  Dataset /intervals/trials/pole_in_time (VectorData) onset of pole moving in | shape = (117,) | dtype = float64
  Dataset /intervals/trials/pole_out_time (VectorData) onset of pole moving out | shape = (117,) | dtype = float64
  Dataset /intervals/trials/pole_position (VectorData) (mm)  the location of the pole along the anteroposterior axis of the animal | shape = (117,) | dtype = float64
  Dataset /intervals/trials/response (VectorData)  | shape = (117,) | dtype = object
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (117,) | dtype = float64
  Dataset /intervals/trials/stim_present (VectorData) is this a stim or no-stim trial | shape = (117,) | dtype = int32
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (117,) | dtype = float64
  Dataset /intervals/trials/type (VectorData)  | shape = (117,) | dtype = object
  session_description: 
  session_start_time: 2010-06-19T00:00:00-05:00
  timestamps_reference_time: 2010-06-19T00:00:00-05:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/CurrentClampSeries (CurrentClampSeries) no description
  Group /acquisition/CurrentClampSeries/electrode (IntracellularElectrode) 
  Group /acquisition/CurrentClampSeries/electrode/device (Device) 
  Group /acquisition/SpikeTrain (PatchClampSeries) The data are either 0 or 1, where 1 represents whether a spike was detected at the corresponding timestamp.
  Group /acquisition/SpikeTrain/electrode (IntracellularElectrode) 
  Group /acquisition/SpikeTrain/electrode/device (Device) 
  Group /acquisition/behavior (BehavioralTimeSeries) 
  Group /acquisition/behavior/amplitude (TimeSeries) the amplitude of the Hilbert Transform of theta_at_base
  Group /acquisition/behavior/beam_break_times (TimeSeries) binary array of lick times (1 = onset of spout contact)
  Group /acquisition/behavior/delta_kappa (TimeSeries) the change in whisker curvature following each touch onset
  Group /acquisition/behavior/distance_to_pole (TimeSeries) (mm) the shortest distance from whisker to the pole
  Group /acquisition/behavior/phase (TimeSeries) the phase of the Hilbert Transform of theta_at_base
  Group /acquisition/behavior/pole_available (TimeSeries) binary array of time when the pole is within reach of the whisker
  Group /acquisition/behavior/set_point (TimeSeries) the amplitude of the Hilbert Transform of theta_at_base
  Group /acquisition/behavior/theta_at_base (TimeSeries) (degree) the angle of the whisker base relative to medialateral axis of the animal
  Group /acquisition/behavior/theta_filt (TimeSeries) theta_at_base filtered with 6-60Hz bandpass
  Group /acquisition/behavior/touch_offset (TimeSeries) binary array of all touch offset times (1 = offset)
  Group /acquisition/behavior/touch_onset (TimeSeries) binary array of all touch onset times (1 = onset)
  file_create_date: ['2020-03-09T15:52:13.375818-05:00']
  Group /general/devices/Borosilicate glass (Device) 
  experiment_description: Intracellular and extracellular electrophysiology recordings performed on mouse barrel cortex in object locating task, where whisker movements and contacts with object were tracked to the milisecond precision.
  experimenter: ['Samuel Andrew Hires']
  institution: Janelia Research Campus
  Group /general/intracellular_ephys/AH0042_AAAA (IntracellularElectrode) 
  Group /general/intracellular_ephys/AH0042_AAAA/device (Device) 
  keywords: ['barrel cortex' 'whiskers' 'extracellular electrophysiology'
   'intracellular electrophysiology']
  related_publications: ['doi:10.7554/eLife.06619']
  Group /general/subject (Subject) 
  identifier: anm101105_2010-06-20_Cell47
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/first_lick_time (VectorData) time of first lick | shape = (143,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (143,) | dtype = int32
  Dataset /intervals/trials/pole_in_time (VectorData) onset of pole moving in | shape = (143,) | dtype = float64
  Dataset /intervals/trials/pole_out_time (VectorData) onset of pole moving out | shape = (143,) | dtype = float64
  Dataset /intervals/trials/pole_position (VectorData) (mm)  the location of the pole along the anteroposterior axis of the animal | shape = (143,) | dtype = float64
  Dataset /intervals/trials/response (VectorData)  | shape = (143,) | dtype = object
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (143,) | dtype = float64
  Dataset /intervals/trials/stim_present (VectorData) is this a stim or no-stim trial | shape = (143,) | dtype = int32
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (143,) | dtype = float64
  Dataset /intervals/trials/type (VectorData)  | shape = (143,) | dtype = object
  session_description: 
  session_start_time: 2010-06-20T00:00:00-05:00
  timestamps_reference_time: 2010-06-20T00:00:00-05:00


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/CurrentClampSeries (CurrentClampSeries) no description
  Group /acquisition/CurrentClampSeries/electrode (IntracellularElectrode) 
  Group /acquisition/CurrentClampSeries/electrode/device (Device) 
  Group /acquisition/SpikeTrain (PatchClampSeries) The data are either 0 or 1, where 1 represents whether a spike was detected at the corresponding timestamp.
  Group /acquisition/SpikeTrain/electrode (IntracellularElectrode) 
  Group /acquisition/SpikeTrain/electrode/device (Device) 
  Group /acquisition/behavior (BehavioralTimeSeries) 
  Group /acquisition/behavior/amplitude (TimeSeries) the amplitude of the Hilbert Transform of theta_at_base
  Group /acquisition/behavior/beam_break_times (TimeSeries) binary array of lick times (1 = onset of spout contact)
  Group /acquisition/behavior/delta_kappa (TimeSeries) the change in whisker curvature following each touch onset
  Group /acquisition/behavior/distance_to_pole (TimeSeries) (mm) the shortest distance from whisker to the pole
  Group /acquisition/behavior/phase (TimeSeries) the phase of the Hilbert Transform of theta_at_base
  Group /acquisition/behavior/pole_available (TimeSeries) binary array of time when the pole is within reach of the whisker
  Group /acquisition/behavior/set_point (TimeSeries) the amplitude of the Hilbert Transform of theta_at_base
  Group /acquisition/behavior/theta_at_base (TimeSeries) (degree) the angle of the whisker base relative to medialateral axis of the animal
  Group /acquisition/behavior/theta_filt (TimeSeries) theta_at_base filtered with 6-60Hz bandpass
  Group /acquisition/behavior/touch_offset (TimeSeries) binary array of all touch offset times (1 = offset)
  Group /acquisition/behavior/touch_onset (TimeSeries) binary array of all touch onset times (1 = onset)
  file_create_date: ['2020-03-09T15:52:21.727965-05:00']
  Group /general/devices/Borosilicate glass (Device) 
  experiment_description: Intracellular and extracellular electrophysiology recordings performed on mouse barrel cortex in object locating task, where whisker movements and contacts with object were tracked to the milisecond precision.
  experimenter: ['Samuel Andrew Hires']
  institution: Janelia Research Campus
  Group /general/intracellular_ephys/AH0044_AAAA (IntracellularElectrode) 
  Group /general/intracellular_ephys/AH0044_AAAA/device (Device) 
  keywords: ['barrel cortex' 'whiskers' 'extracellular electrophysiology'
   'intracellular electrophysiology']
  related_publications: ['doi:10.7554/eLife.06619']
  Group /general/subject (Subject) 
  identifier: anm101105_2010-06-21_Cell48
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/first_lick_time (VectorData) time of first lick | shape = (104,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (104,) | dtype = int32
  Dataset /intervals/trials/pole_in_time (VectorData) onset of pole moving in | shape = (104,) | dtype = float64
  Dataset /intervals/trials/pole_out_time (VectorData) onset of pole moving out | shape = (104,) | dtype = float64
  Dataset /intervals/trials/pole_position (VectorData) (mm)  the location of the pole along the anteroposterior axis of the animal | shape = (104,) | dtype = float64
  Dataset /intervals/trials/response (VectorData)  | shape = (104,) | dtype = object
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (104,) | dtype = float64
  Dataset /intervals/trials/stim_present (VectorData) is this a stim or no-stim trial | shape = (104,) | dtype = int32
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (104,) | dtype = float64
  Dataset /intervals/trials/type (VectorData)  | shape = (104,) | dtype = object
  session_description: 
  session_start_time: 2010-06-21T00:00:00-05:00
  timestamps_reference_time: 2010-06-21T00:00:00-05:00


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/CurrentClampSeries (CurrentClampSeries) no description
  Group /acquisition/CurrentClampSeries/electrode (IntracellularElectrode) 
  Group /acquisition/CurrentClampSeries/electrode/device (Device) 
  Group /acquisition/SpikeTrain (PatchClampSeries) The data are either 0 or 1, where 1 represents whether a spike was detected at the corresponding timestamp.
  Group /acquisition/SpikeTrain/electrode (IntracellularElectrode) 
  Group /acquisition/SpikeTrain/electrode/device (Device) 
  Group /acquisition/behavior (BehavioralTimeSeries) 
  Group /acquisition/behavior/amplitude (TimeSeries) the amplitude of the Hilbert Transform of theta_at_base
  Group /acquisition/behavior/beam_break_times (TimeSeries) binary array of lick times (1 = onset of spout contact)
  Group /acquisition/behavior/delta_kappa (TimeSeries) the change in whisker curvature following each touch onset
  Group /acquisition/behavior/distance_to_pole (TimeSeries) (mm) the shortest distance from whisker to the pole
  Group /acquisition/behavior/phase (TimeSeries) the phase of the Hilbert Transform of theta_at_base
  Group /acquisition/behavior/pole_available (TimeSeries) binary array of time when the pole is within reach of the whisker
  Group /acquisition/behavior/set_point (TimeSeries) the amplitude of the Hilbert Transform of theta_at_base
  Group /acquisition/behavior/theta_at_base (TimeSeries) (degree) the angle of the whisker base relative to medialateral axis of the animal
  Group /acquisition/behavior/theta_filt (TimeSeries) theta_at_base filtered with 6-60Hz bandpass
  Group /acquisition/behavior/touch_offset (TimeSeries) binary array of all touch offset times (1 = offset)
  Group /acquisition/behavior/touch_onset (TimeSeries) binary array of all touch onset times (1 = onset)
  file_create_date: ['2020-03-09T15:52:27.157249-05:00']
  Group /general/devices/Borosilicate glass (Device) 
  experiment_description: Intracellular and extracellular electrophysiology recordings performed on mouse barrel cortex in object locating task, where whisker movements and contacts with object were tracked to the milisecond precision.
  experimenter: ['Samuel Andrew Hires']
  institution: Janelia Research Campus
  Group /general/intracellular_ephys/AH0062_AAAA (IntracellularElectrode) 
  Group /general/intracellular_ephys/AH0062_AAAA/device (Device) 
  keywords: ['barrel cortex' 'whiskers' 'extracellular electrophysiology'
   'intracellular electrophysiology']
  related_publications: ['doi:10.7554/eLife.06619']
  Group /general/subject (Subject) 
  identifier: anm106211_2010-09-25_Cell17
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/first_lick_time (VectorData) time of first lick | shape = (166,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (166,) | dtype = int32
  Dataset /intervals/trials/pole_in_time (VectorData) onset of pole moving in | shape = (166,) | dtype = float64
  Dataset /intervals/trials/pole_out_time (VectorData) onset of pole moving out | shape = (166,) | dtype = float64
  Dataset /intervals/trials/pole_position (VectorData) (mm)  the location of the pole along the anteroposterior axis of the animal | shape = (166,) | dtype = float64
  Dataset /intervals/trials/response (VectorData)  | shape = (166,) | dtype = object
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (166,) | dtype = float64
  Dataset /intervals/trials/stim_present (VectorData) is this a stim or no-stim trial | shape = (166,) | dtype = int32
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (166,) | dtype = float64
  Dataset /intervals/trials/type (VectorData)  | shape = (166,) | dtype = object
  session_description: 
  session_start_time: 2010-09-25T00:00:00-05:00
  timestamps_reference_time: 2010-09-25T00:00:00-05:00


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  Group /acquisition/CurrentClampSeries (CurrentClampSeries) no description
  Group /acquisition/CurrentClampSeries/electrode (IntracellularElectrode) 
  Group /acquisition/CurrentClampSeries/electrode/device (Device) 
  Group /acquisition/SpikeTrain (PatchClampSeries) The data are either 0 or 1, where 1 represents whether a spike was detected at the corresponding timestamp.
  Group /acquisition/SpikeTrain/electrode (IntracellularElectrode) 
  Group /acquisition/SpikeTrain/electrode/device (Device) 
  Group /acquisition/behavior (BehavioralTimeSeries) 
  Group /acquisition/behavior/amplitude (TimeSeries) the amplitude of the Hilbert Transform of theta_at_base
  Group /acquisition/behavior/beam_break_times (TimeSeries) binary array of lick times (1 = onset of spout contact)
  Group /acquisition/behavior/delta_kappa (TimeSeries) the change in whisker curvature following each touch onset
  Group /acquisition/behavior/distance_to_pole (TimeSeries) (mm) the shortest distance from whisker to the pole
  Group /acquisition/behavior/phase (TimeSeries) the phase of the Hilbert Transform of theta_at_base
  Group /acquisition/behavior/pole_available (TimeSeries) binary array of time when the pole is within reach of the whisker
  Group /acquisition/behavior/set_point (TimeSeries) the amplitude of the Hilbert Transform of theta_at_base
  Group /acquisition/behavior/theta_at_base (TimeSeries) (degree) the angle of the whisker base relative to medialateral axis of the animal
  Group /acquisition/behavior/theta_filt (TimeSeries) theta_at_base filtered with 6-60Hz bandpass
  Group /acquisition/behavior/touch_offset (TimeSeries) binary array of all touch offset times (1 = offset)
  Group /acquisition/behavior/touch_onset (TimeSeries) binary array of all touch onset times (1 = onset)
  file_create_date: ['2020-03-09T15:52:35.338878-05:00']
  Group /general/devices/Borosilicate glass (Device) 
  experiment_description: Intracellular and extracellular electrophysiology recordings performed on mouse barrel cortex in object locating task, where whisker movements and contacts with object were tracked to the milisecond precision.
  experimenter: ['Samuel Andrew Hires']
  institution: Janelia Research Campus
  Group /general/intracellular_ephys/AH0048_AAAA (IntracellularElectrode) 
  Group /general/intracellular_ephys/AH0048_AAAA/device (Device) 
  keywords: ['barrel cortex' 'whiskers' 'extracellular electrophysiology'
   'intracellular electrophysiology']
  related_publications: ['doi:10.7554/eLife.06619']
  Group /general/subject (Subject) 
  identifier: anm106213_2010-08-22_Cell49
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/first_lick_time (VectorData) time of first lick | shape = (99,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (99,) | dtype = int32
  Dataset /intervals/trials/pole_in_time (VectorData) onset of pole moving in | shape = (99,) | dtype = float64
  Dataset /intervals/trials/pole_out_time (VectorData) onset of pole moving out | shape = (99,) | dtype = float64
  Dataset /intervals/trials/pole_position (VectorData) (mm)  the location of the pole along the anteroposterior axis of the animal | shape = (99,) | dtype = float64
  Dataset /intervals/trials/response (VectorData)  | shape = (99,) | dtype = object
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (99,) | dtype = float64
  Dataset /intervals/trials/stim_present (VectorData) is this a stim or no-stim trial | shape = (99,) | dtype = int32
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (99,) | dtype = float64
  Dataset /intervals/trials/type (VectorData)  | shape = (99,) | dtype = object
  session_description: 
  session_start_time: 2010-08-22T00:00:00-05:00
  timestamps_reference_time: 2010-08-22T00:00:00-05:00
