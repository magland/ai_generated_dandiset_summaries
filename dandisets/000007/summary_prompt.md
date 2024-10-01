
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000007/0.220126.1903
name: A cortico-cerebellar loop for motor planning
contributor: [{'name': 'Gao, Zhenyu', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Davis, Courtney', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Thomas, Alyse M.', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-6070-4769', 'affiliation': [], 'includeInCitation': True}, {'name': 'Economo, Michael N.', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0001-9893-1505', 'affiliation': [], 'includeInCitation': True}, {'name': 'Abrego, Amada M.', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0003-0311-5244', 'affiliation': [], 'includeInCitation': True}, {'name': 'Svoboda, Karel', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Zeeuw, Chris I. De', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0001-5628-8187', 'affiliation': [], 'includeInCitation': True}, {'name': 'Li, Nuo', 'roleName': ['dcite:Author', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0002-6613-5018', 'affiliation': [], 'includeInCitation': True}]
description: Extracellular recording in ALM
assetsSummary: {'species': [{'name': 'House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 199439472, 'numberOfFiles': 54, 'numberOfSubjects': 13, 'variableMeasured': ['Units', 'ElectrodeGroup'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000007 has 54 NWB files.
21 of these NWB files are of type 1.
20 of these NWB files are of type 2.
13 of these NWB files are of type 3.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2020-03-24T23:06:01.996372+00:00']
  Group /general/devices/NN 32ch A4x8-5mm-100-200-177 (Device) 
  Group /general/devices/fiber (Device) 
  experiment_description: Extracelluar recording in ALM
  experimenter: ['Nuo Li']
  Group /general/extracellular_ephys/NN 32ch A4x8-5mm-100-200-177_g1 (ElectrodeGroup) N/A
  Group /general/extracellular_ephys/NN 32ch A4x8-5mm-100-200-177_g1/device (Device) 
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (64,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (64,) | dtype = float64
  institution: Janelia Research Campus
  keywords: ['motor planning' 'anterior lateral cortex' 'ALM'
   'Extracellular recording' 'optogenetics']
  Group /general/optogenetics/Fastigial (OptogeneticStimulusSite) 
  Group /general/optogenetics/Fastigial/device (Device) 
  related_publications: ['https://www.nature.com/articles/s41586-018-0633-x']
  Group /general/subject (Subject) 
  virus: [{"virus": "AAV2-hSyn-hChR2(H134R)-EYFP", "brain_location": "Fastigial", "hemisphere": "right", "injection_date": "2017-04-05", "injection_volume": "150.0", "injection_coordinate_ap": "-2.5", "injection_coordinate_ml": "0.8", "injection_coordinate_dv": "2.4", "coordinate_ref": "lambda", "virus_source": "UNC", "virus_lot_number": ""}]
  identifier: BAYLORCD6_2017-06-10 13:57:20
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/cue_time (VectorData) float # in secs, the end of the delay period, relative to the start of the trials | shape = (307,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (307,) | dtype = int64
  Dataset /intervals/trials/lick_early (VectorData) tinyint # whether the animal licks early | shape = (307,) | dtype = int64
  Dataset /intervals/trials/photo_stim_id (VectorData) varchar(8) # | shape = (307,) | dtype = object
  Dataset /intervals/trials/pole_in_time (VectorData) float # in secs, the start of the sample period for each trial, relative to the trial start | shape = (307,) | dtype = float64
  Dataset /intervals/trials/pole_out_time (VectorData) float # in secs, the end of the sample period and start of the delay period, relative to the trial start | shape = (307,) | dtype = float64
  Dataset /intervals/trials/response (VectorData) enum('HitR','HitL','ErrR','ErrL','NoLickR','NoLickL','NoLickNoResponse') # subject response to the stimulus | shape = (307,) | dtype = object
  Dataset /intervals/trials/session_directory (VectorData) varchar(256) # | shape = (307,) | dtype = object
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (307,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (307,) | dtype = float64
  session_description: 
  session_start_time: 2017-06-10T13:57:20+00:00
  timestamps_reference_time: 2017-06-10T13:57:20+00:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/cell_type (VectorData) cell type (e.g. fast spiking or pyramidal) | shape = (64,) | dtype = object
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (64,) | dtype = object
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (64,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex)  | shape = (64,) | dtype = int64
  Dataset /units/id (ElementIdentifiers)  | shape = (64,) | dtype = int64
  Dataset /units/obs_intervals (VectorData) the observation intervals for each unit | shape = (64, 2) | dtype = float64
  Dataset /units/obs_intervals_index (VectorIndex)  | shape = (64,) | dtype = int64
  Dataset /units/sampling_rate (VectorData) sampling rate of the waveform, Hz | shape = (64,) | dtype = int64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (827948,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex)  | shape = (64,) | dtype = int64
  Dataset /units/waveform_mean (VectorData) the spike waveform mean for each spike unit | shape = (64, 30) | dtype = float64
  Dataset /units/waveform_sd (VectorData) the spike waveform standard deviation for each spike unit | shape = (64, 30) | dtype = float64


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2020-03-24T23:04:49.249151+00:00']
  Group /general/devices/Cambridge NeuroTech 64ch H2 probe (Device) 
  Group /general/devices/fiber (Device) 
  experiment_description: Extracelluar recording in ALM
  experimenter: ['Nuo Li']
  Group /general/extracellular_ephys/Cambridge NeuroTech 64ch H2 probe_g1 (ElectrodeGroup) N/A
  Group /general/extracellular_ephys/Cambridge NeuroTech 64ch H2 probe_g1/device (Device) 
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (64,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (64,) | dtype = float64
  institution: Janelia Research Campus
  keywords: ['motor planning' 'anterior lateral cortex' 'ALM'
   'Extracellular recording' 'optogenetics']
  Group /general/optogenetics/Fastigial (OptogeneticStimulusSite) 
  Group /general/optogenetics/Fastigial/device (Device) 
  related_publications: ['https://www.nature.com/articles/s41586-018-0633-x']
  Group /general/subject (Subject) 
  virus: []
  identifier: BAYLORCD12_2018-01-25 19:16:01
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/cue_time (VectorData) float # in secs, the end of the delay period, relative to the start of the trials | shape = (273,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (273,) | dtype = int64
  Dataset /intervals/trials/lick_early (VectorData) tinyint # whether the animal licks early | shape = (273,) | dtype = int64
  Dataset /intervals/trials/photo_stim_id (VectorData) varchar(8) # | shape = (273,) | dtype = object
  Dataset /intervals/trials/pole_in_time (VectorData) float # in secs, the start of the sample period for each trial, relative to the trial start | shape = (273,) | dtype = float64
  Dataset /intervals/trials/pole_out_time (VectorData) float # in secs, the end of the sample period and start of the delay period, relative to the trial start | shape = (273,) | dtype = float64
  Dataset /intervals/trials/response (VectorData) enum('HitR','HitL','ErrR','ErrL','NoLickR','NoLickL','NoLickNoResponse') # subject response to the stimulus | shape = (273,) | dtype = object
  Dataset /intervals/trials/session_directory (VectorData) varchar(256) # | shape = (273,) | dtype = object
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (273,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (273,) | dtype = float64
  session_description: 
  session_start_time: 2018-01-25T19:16:01+00:00
  timestamps_reference_time: 2018-01-25T19:16:01+00:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/cell_type (VectorData) cell type (e.g. fast spiking or pyramidal) | shape = (20,) | dtype = object
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (20,) | dtype = object
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (20,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex)  | shape = (20,) | dtype = int64
  Dataset /units/id (ElementIdentifiers)  | shape = (20,) | dtype = int64
  Dataset /units/obs_intervals (VectorData) the observation intervals for each unit | shape = (20, 2) | dtype = float64
  Dataset /units/obs_intervals_index (VectorIndex)  | shape = (20,) | dtype = int64
  Dataset /units/sampling_rate (VectorData) sampling rate of the waveform, Hz | shape = (20,) | dtype = int64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (148525,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex)  | shape = (20,) | dtype = int64
  Dataset /units/waveform_mean (VectorData) the spike waveform mean for each spike unit | shape = (20, 30) | dtype = float64
  Dataset /units/waveform_sd (VectorData) the spike waveform standard deviation for each spike unit | shape = (20, 30) | dtype = float64


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2020-03-24T23:07:27.379340+00:00']
  Group /general/devices/NN 32ch A4x8-5mm-100-200-177 (Device) 
  Group /general/devices/fiber (Device) 
  experiment_description: Extracelluar recording in ALM
  experimenter: ['Nuo Li']
  Group /general/extracellular_ephys/NN 32ch A4x8-5mm-100-200-177_g1 (ElectrodeGroup) N/A
  Group /general/extracellular_ephys/NN 32ch A4x8-5mm-100-200-177_g1/device (Device) 
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (64,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (64,) | dtype = float64
  institution: Janelia Research Campus
  keywords: ['motor planning' 'anterior lateral cortex' 'ALM'
   'Extracellular recording' 'optogenetics']
  Group /general/optogenetics/Dentate (OptogeneticStimulusSite) 
  Group /general/optogenetics/Dentate/device (Device) 
  related_publications: ['https://www.nature.com/articles/s41586-018-0633-x']
  Group /general/subject (Subject) 
  virus: [{"virus": "AAV2-hSyn-hChR2(H134R)-EYFP", "brain_location": "Dentate", "hemisphere": "right", "injection_date": "2017-04-03", "injection_volume": "150.0", "injection_coordinate_ap": "-2.3", "injection_coordinate_ml": "2.5", "injection_coordinate_dv": "2.4", "coordinate_ref": "lambda", "virus_source": "UNC", "virus_lot_number": ""}]
  identifier: BAYLORNL12_2017-06-10 12:25:30
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/cue_time (VectorData) float # in secs, the end of the delay period, relative to the start of the trials | shape = (368,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (368,) | dtype = int64
  Dataset /intervals/trials/lick_early (VectorData) tinyint # whether the animal licks early | shape = (368,) | dtype = int64
  Dataset /intervals/trials/photo_stim_id (VectorData) varchar(8) # | shape = (368,) | dtype = object
  Dataset /intervals/trials/pole_in_time (VectorData) float # in secs, the start of the sample period for each trial, relative to the trial start | shape = (368,) | dtype = float64
  Dataset /intervals/trials/pole_out_time (VectorData) float # in secs, the end of the sample period and start of the delay period, relative to the trial start | shape = (368,) | dtype = float64
  Dataset /intervals/trials/response (VectorData) enum('HitR','HitL','ErrR','ErrL','NoLickR','NoLickL','NoLickNoResponse') # subject response to the stimulus | shape = (368,) | dtype = object
  Dataset /intervals/trials/session_directory (VectorData) varchar(256) # | shape = (368,) | dtype = object
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (368,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (368,) | dtype = float64
  session_description: 
  session_start_time: 2017-06-10T12:25:30+00:00
  timestamps_reference_time: 2017-06-10T12:25:30+00:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/cell_type (VectorData) cell type (e.g. fast spiking or pyramidal) | shape = (63,) | dtype = object
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (63,) | dtype = object
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (63,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex)  | shape = (63,) | dtype = int64
  Dataset /units/id (ElementIdentifiers)  | shape = (63,) | dtype = int64
  Dataset /units/obs_intervals (VectorData) the observation intervals for each unit | shape = (63, 2) | dtype = float64
  Dataset /units/obs_intervals_index (VectorIndex)  | shape = (63,) | dtype = int64
  Dataset /units/sampling_rate (VectorData) sampling rate of the waveform, Hz | shape = (63,) | dtype = int64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (829541,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex)  | shape = (63,) | dtype = int64
  Dataset /units/waveform_mean (VectorData) the spike waveform mean for each spike unit | shape = (63, 30) | dtype = float64
  Dataset /units/waveform_sd (VectorData) the spike waveform standard deviation for each spike unit | shape = (63, 30) | dtype = float64
