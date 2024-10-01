
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000010/0.220126.1905
name: A motor cortex circuit for motor planning and movement
contributor: [{'name': 'Li, Nuo', 'roleName': ['dcite:Author', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0002-6613-5018', 'includeInCitation': True}, {'name': 'Chen, Tsai-Wen', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-3407-8223', 'includeInCitation': True}, {'name': 'Guo, Zengcai V.', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-4140-7961', 'includeInCitation': True}, {'name': 'Gerfen, Charles R.', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0001-9008-4882', 'includeInCitation': True}, {'name': 'Svoboda, Karel', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-6670-7362', 'includeInCitation': True}]
description: Data from "A motor cortex circuit for motor planning and movement" Li et al. Nature 2015
assetsSummary: {'species': [{'name': 'House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}, {'name': 'behavioral approach', 'schemaKey': 'ApproachType'}, {'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 40006570644, 'numberOfFiles': 158, 'numberOfSubjects': 23, 'variableMeasured': ['BehavioralTimeSeries', 'Units', 'ElectrodeGroup', 'BehavioralEvents', 'PlaneSegmentation'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000010 has 60 NWB files.
9 of these NWB files are of type 1.
33 of these NWB files are of type 2.
9 of these NWB files are of type 3.
6 of these NWB files are of type 4.
3 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/BehavioralEvents (BehavioralEvents) 
  Group /acquisition/BehavioralEvents/delay (TimeSeries) no description
  Group /acquisition/BehavioralEvents/go (TimeSeries) no description
  Group /acquisition/BehavioralEvents/sample (TimeSeries) no description
  Group /acquisition/BehavioralTimeSeries (BehavioralTimeSeries) 
  Group /acquisition/BehavioralTimeSeries/lick_trace (TimeSeries) Time-series of the animal's tongue movement when licking
  file_create_date: ['2020-02-20T15:26:47.689417-06:00']
  Group /general/devices/A4x8-5mm-100-200-177 (Device) 
  Group /general/devices/LaserGem473 (Device) 
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
  keywords: ['motor planning' 'preparatory activity' 'whiskers'
   'optogenetic perturbations' 'extracellular electrophysiology']
  Group /general/optogenetics/left ALM (OptogeneticStimulusSite) 
  Group /general/optogenetics/left ALM/device (Device) 
  Group /general/optogenetics/left PONS (OptogeneticStimulusSite) 
  Group /general/optogenetics/left PONS/device (Device) 
  related_publications: ['doi:10.1038/nature14178']
  Group /general/subject (Subject) 
  virus: [{"injection_id": "1", "virus": "Addgene41015", "injection_date": "2013-05-23", "injection_volume": "30.0", "brain_area": "M2", "hemisphere": "left", "virus_source": "Janelia core", "virus_lot_number": "", "virus_titer": "None"}, {"injection_id": "2", "virus": "Addgene41015", "injection_date": "2013-05-23", "injection_volume": "30.0", "brain_area": "M2", "hemisphere": "left", "virus_source": "Janelia core", "virus_lot_number": "", "virus_titer": "None"}]
  identifier: ANM210861_2013-07-01_1
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/early_lick (VectorData) varchar(32) # | shape = (423,) | dtype = object
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (423,) | dtype = int32
  Dataset /intervals/trials/outcome (VectorData) varchar(32) # | shape = (423,) | dtype = object
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (423,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (423,) | dtype = float64
  Dataset /intervals/trials/task (VectorData) varchar(12) # task type | shape = (423,) | dtype = object
  Dataset /intervals/trials/task_protocol (VectorData) tinyint # task protocol | shape = (423,) | dtype = int32
  Dataset /intervals/trials/trial_instruction (VectorData) varchar(16) # | shape = (423,) | dtype = object
  session_description: 
  session_start_time: 2013-07-01T00:00:00-05:00
  timestamps_reference_time: 2013-07-01T00:00:00-05:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/cell_type (VectorData) cell type (e.g. fast spiking or pyramidal) | shape = (27,) | dtype = object
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (27,) | dtype = object
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (27,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex)  | shape = (27,) | dtype = int32
  Dataset /units/id (ElementIdentifiers)  | shape = (27,) | dtype = int32
  Dataset /units/obs_intervals (VectorData) the observation intervals for each unit | shape = (10989, 2) | dtype = float64
  Dataset /units/obs_intervals_index (VectorIndex)  | shape = (27,) | dtype = int32
  Dataset /units/posx (VectorData) estimated x position of the unit relative to probe (0,0) (um) | shape = (27,) | dtype = float64
  Dataset /units/posy (VectorData) estimated y position of the unit relative to probe (0,0) (um) | shape = (27,) | dtype = float64
  Dataset /units/quality (VectorData) unit quality from clustering | shape = (27,) | dtype = object
  Dataset /units/sampling_rate (VectorData) Sampling rate of the raw voltage traces (Hz) | shape = (27,) | dtype = float64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (146791,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex)  | shape = (27,) | dtype = int32
  Dataset /units/waveform_mean (VectorData) the spike waveform mean for each spike unit | shape = (27, 29) | dtype = float64
  Dataset /units/waveform_sd (VectorData) the spike waveform standard deviation for each spike unit | shape = (27, 29) | dtype = float64


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/BehavioralEvents (BehavioralEvents) 
  Group /acquisition/BehavioralEvents/delay (TimeSeries) no description
  Group /acquisition/BehavioralEvents/go (TimeSeries) no description
  Group /acquisition/BehavioralEvents/photostim_start_time (TimeSeries) no description
  Group /acquisition/BehavioralEvents/photostim_stop_time (TimeSeries) no description
  Group /acquisition/BehavioralEvents/sample (TimeSeries) no description
  Group /acquisition/BehavioralTimeSeries (BehavioralTimeSeries) 
  Group /acquisition/BehavioralTimeSeries/lick_trace (TimeSeries) Time-series of the animal's tongue movement when licking
  file_create_date: ['2020-02-20T15:40:00.648240-06:00']
  Group /general/devices/A4x8-5mm-100-200-177 (Device) 
  Group /general/devices/LaserGem473 (Device) 
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
  keywords: ['motor planning' 'preparatory activity' 'whiskers'
   'optogenetic perturbations' 'extracellular electrophysiology']
  Group /general/optogenetics/left ALM (OptogeneticStimulusSite) 
  Group /general/optogenetics/left ALM/device (Device) 
  Group /general/optogenetics/left PONS (OptogeneticStimulusSite) 
  Group /general/optogenetics/left PONS/device (Device) 
  related_publications: ['doi:10.1038/nature14178']
  Group /general/subject (Subject) 
  virus: [{"injection_id": "1", "virus": "Addgene41015", "injection_date": "2013-07-17", "injection_volume": "100.0", "brain_area": "M2", "hemisphere": "left", "virus_source": "Janelia core", "virus_lot_number": "", "virus_titer": "None"}, {"injection_id": "2", "virus": "Addgene41015", "injection_date": "2013-07-17", "injection_volume": "100.0", "brain_area": "M2", "hemisphere": "left", "virus_source": "Janelia core", "virus_lot_number": "", "virus_titer": "None"}]
  identifier: ANM219030_2013-08-29_1
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/early_lick (VectorData) varchar(32) # | shape = (308,) | dtype = object
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (308,) | dtype = int32
  Dataset /intervals/trials/outcome (VectorData) varchar(32) # | shape = (308,) | dtype = object
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (308,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (308,) | dtype = float64
  Dataset /intervals/trials/task (VectorData) varchar(12) # task type | shape = (308,) | dtype = object
  Dataset /intervals/trials/task_protocol (VectorData) tinyint # task protocol | shape = (308,) | dtype = int32
  Dataset /intervals/trials/trial_instruction (VectorData) varchar(16) # | shape = (308,) | dtype = object
  session_description: 
  session_start_time: 2013-08-29T00:00:00-05:00
  Group /stimulus/presentation/left PONS_aom_input_trace (OptogeneticSeries) no description
  Group /stimulus/presentation/left PONS_aom_input_trace/site (OptogeneticStimulusSite) 
  Group /stimulus/presentation/left PONS_aom_input_trace/site/device (Device) 
  Group /stimulus/presentation/left PONS_laser_power (OptogeneticSeries) no description
  Group /stimulus/presentation/left PONS_laser_power/site (OptogeneticStimulusSite) 
  Group /stimulus/presentation/left PONS_laser_power/site/device (Device) 
  timestamps_reference_time: 2013-08-29T00:00:00-05:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/cell_type (VectorData) cell type (e.g. fast spiking or pyramidal) | shape = (20,) | dtype = object
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (20,) | dtype = object
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (20,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex)  | shape = (20,) | dtype = int32
  Dataset /units/id (ElementIdentifiers)  | shape = (20,) | dtype = int32
  Dataset /units/obs_intervals (VectorData) the observation intervals for each unit | shape = (5440, 2) | dtype = float64
  Dataset /units/obs_intervals_index (VectorIndex)  | shape = (20,) | dtype = int32
  Dataset /units/posx (VectorData) estimated x position of the unit relative to probe (0,0) (um) | shape = (20,) | dtype = float64
  Dataset /units/posy (VectorData) estimated y position of the unit relative to probe (0,0) (um) | shape = (20,) | dtype = float64
  Dataset /units/quality (VectorData) unit quality from clustering | shape = (20,) | dtype = object
  Dataset /units/sampling_rate (VectorData) Sampling rate of the raw voltage traces (Hz) | shape = (20,) | dtype = float64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (132322,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex)  | shape = (20,) | dtype = int32
  Dataset /units/waveform_mean (VectorData) the spike waveform mean for each spike unit | shape = (20, 29) | dtype = float64
  Dataset /units/waveform_sd (VectorData) the spike waveform standard deviation for each spike unit | shape = (20, 29) | dtype = float64


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
  file_create_date: ['2020-02-20T15:27:59.363357-06:00']
  Group /general/devices/A4x8-5mm-100-200-177 (Device) 
  Group /general/devices/LaserGem473 (Device) 
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
  keywords: ['motor planning' 'preparatory activity' 'whiskers'
   'optogenetic perturbations' 'extracellular electrophysiology']
  Group /general/optogenetics/bilateral ALM (OptogeneticStimulusSite) 
  Group /general/optogenetics/bilateral ALM/device (Device) 
  Group /general/optogenetics/left PONS (OptogeneticStimulusSite) 
  Group /general/optogenetics/left PONS/device (Device) 
  related_publications: ['doi:10.1038/nature14178']
  Group /general/subject (Subject) 
  virus: [{"injection_id": "1", "virus": "Addgene41015", "injection_date": "2013-07-14", "injection_volume": "100.0", "brain_area": "M2", "hemisphere": "left", "virus_source": "Janelia core", "virus_lot_number": "", "virus_titer": "None"}, {"injection_id": "2", "virus": "Addgene41015", "injection_date": "2013-07-14", "injection_volume": "100.0", "brain_area": "M2", "hemisphere": "left", "virus_source": "Janelia core", "virus_lot_number": "", "virus_titer": "None"}]
  identifier: ANM214427_2013-08-05_1
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/early_lick (VectorData) varchar(32) # | shape = (320,) | dtype = object
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (320,) | dtype = int32
  Dataset /intervals/trials/outcome (VectorData) varchar(32) # | shape = (320,) | dtype = object
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (320,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (320,) | dtype = float64
  Dataset /intervals/trials/task (VectorData) varchar(12) # task type | shape = (320,) | dtype = object
  Dataset /intervals/trials/task_protocol (VectorData) tinyint # task protocol | shape = (320,) | dtype = int32
  Dataset /intervals/trials/trial_instruction (VectorData) varchar(16) # | shape = (320,) | dtype = object
  session_description: 
  session_start_time: 2013-08-05T00:00:00-05:00
  Group /stimulus/presentation/bilateral ALM_aom_input_trace (OptogeneticSeries) no description
  Group /stimulus/presentation/bilateral ALM_aom_input_trace/site (OptogeneticStimulusSite) 
  Group /stimulus/presentation/bilateral ALM_aom_input_trace/site/device (Device) 
  Group /stimulus/presentation/bilateral ALM_laser_power (OptogeneticSeries) no description
  Group /stimulus/presentation/bilateral ALM_laser_power/site (OptogeneticStimulusSite) 
  Group /stimulus/presentation/bilateral ALM_laser_power/site/device (Device) 
  Group /stimulus/presentation/left PONS_aom_input_trace (OptogeneticSeries) no description
  Group /stimulus/presentation/left PONS_aom_input_trace/site (OptogeneticStimulusSite) 
  Group /stimulus/presentation/left PONS_aom_input_trace/site/device (Device) 
  Group /stimulus/presentation/left PONS_laser_power (OptogeneticSeries) no description
  Group /stimulus/presentation/left PONS_laser_power/site (OptogeneticStimulusSite) 
  Group /stimulus/presentation/left PONS_laser_power/site/device (Device) 
  timestamps_reference_time: 2013-08-05T00:00:00-05:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/cell_type (VectorData) cell type (e.g. fast spiking or pyramidal) | shape = (12,) | dtype = object
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (12,) | dtype = object
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (12,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex)  | shape = (12,) | dtype = int32
  Dataset /units/id (ElementIdentifiers)  | shape = (12,) | dtype = int32
  Dataset /units/obs_intervals (VectorData) the observation intervals for each unit | shape = (3720, 2) | dtype = float64
  Dataset /units/obs_intervals_index (VectorIndex)  | shape = (12,) | dtype = int32
  Dataset /units/posx (VectorData) estimated x position of the unit relative to probe (0,0) (um) | shape = (12,) | dtype = float64
  Dataset /units/posy (VectorData) estimated y position of the unit relative to probe (0,0) (um) | shape = (12,) | dtype = float64
  Dataset /units/quality (VectorData) unit quality from clustering | shape = (12,) | dtype = object
  Dataset /units/sampling_rate (VectorData) Sampling rate of the raw voltage traces (Hz) | shape = (12,) | dtype = float64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (58726,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex)  | shape = (12,) | dtype = int32
  Dataset /units/waveform_mean (VectorData) the spike waveform mean for each spike unit | shape = (12, 29) | dtype = float64
  Dataset /units/waveform_sd (VectorData) the spike waveform standard deviation for each spike unit | shape = (12, 29) | dtype = float64


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/images (Images) Structural images of a scanning
  Dataset /acquisition/images/Beads PT (RGBImage)  | shape = (512, 512, 3) | dtype = float64
  Dataset /acquisition/images/CTB-647 IT (RGBImage)  | shape = (512, 512, 3) | dtype = float64
  Dataset /acquisition/images/GCaMP at 940nm (GrayscaleImage)  | shape = (512, 512) | dtype = float32
  file_create_date: ['2020-01-16T23:32:26.303868+00:00']
  Group /general/devices/two-photon microscope with Thorlabs resonant galvo scannner (Device) 
  experiment_description: Two-photon experiment recorded in ALM
  experimenter: ['Tsai-Wen Chen']
  institution: Janelia Research Campus
  keywords: ['motor planning' 'motor movement' 'anterior lateral cortex' 'ALM'
   'Two-photon imaging']
  Group /general/optophysiology/ImagingPlane (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane/device (Device) 
  Group /general/optophysiology/ImagingPlane/green (OpticalChannel) 
  related_publications: ['https://doi.org/10.1038/nature14178']
  Group /general/subject (Subject) 
  virus: [{"injection_id": "1", "virus": "AV-1-PV2824", "injection_date": "2013-08-20", "injection_volume": "6.0", "virus_dilution": "None", "brain_location_name": "left_alm", "ml_location": "2500.0", "ap_location": "-1500.0", "dv_location": "210.0", "virus_source": "UPenn", "virus_lot_number": "", "virus_titer": "None"}, {"injection_id": "2", "virus": "AV-1-PV2824", "injection_date": "2013-08-20", "injection_volume": "6.0", "virus_dilution": "None", "brain_location_name": "left_alm", "ml_location": "2500.0", "ap_location": "-1500.0", "dv_location": "370.0", "virus_source": "UPenn", "virus_lot_number": "", "virus_titer": "None"}, {"injection_id": "3", "virus": "AV-1-PV2824", "injection_date": "2013-08-20", "injection_volume": "6.0", "virus_dilution": "None", "brain_location_name": "left_alm", "ml_location": "2500.0", "ap_location": "-1500.0", "dv_location": "530.0", "virus_source": "UPenn", "virus_lot_number": "", "virus_titer": "None"}]
  identifier: 217951_2013-10-09_11
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/early_lick (VectorData) varchar(32) # | shape = (124,) | dtype = bool
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (124,) | dtype = int64
  Dataset /intervals/trials/outcome (VectorData) varchar(32) # | shape = (124,) | dtype = object
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (124,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (124,) | dtype = float64
  Dataset /intervals/trials/task (VectorData) varchar(12) # task type | shape = (124,) | dtype = object
  Dataset /intervals/trials/task_protocol (VectorData) tinyint # task protocol | shape = (124,) | dtype = int64
  Dataset /intervals/trials/trial_instruction (VectorData) varchar(16) # | shape = (124,) | dtype = object
  Group /processing/behavior (ProcessingModule) Time of behavioral events in this session
  Group /processing/behavior/BehavioralEvents (BehavioralEvents) 
  Group /processing/behavior/BehavioralEvents/delay (TimeSeries) Time stamps of the beginning of the delay period on each trial.
  Group /processing/behavior/BehavioralEvents/go (TimeSeries) Time stamps of the go cue signal on each trial.
  Group /processing/behavior/BehavioralEvents/sample (TimeSeries) Time stamps of the beginning of the sampling period on each trial.
  Group /processing/ophys (ProcessingModule) Processing result of imaging
  Group /processing/ophys/Fluorescence (Fluorescence) 
  Group /processing/ophys/Fluorescence/NeuropilResponseSeries (RoiResponseSeries) average fluorescence of the neuropil surrounding the roi
  Dataset /processing/ophys/Fluorescence/NeuropilResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (104,) | dtype = int64
  Group /processing/ophys/Fluorescence/RoiResponseSeries (RoiResponseSeries) average fluorescence of roi
  Dataset /processing/ophys/Fluorescence/RoiResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (104,) | dtype = int64
  Group /processing/ophys/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation (PlaneSegmentation) output from segmenting the current imaging plane
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/cell_type (VectorData) PT, IT, or unknown | shape = (104,) | dtype = object
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/id (ElementIdentifiers)  | shape = (104,) | dtype = int64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (104, 512, 512) | dtype = bool
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/device (Device) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/green (OpticalChannel) 
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/included (VectorData) whether to include this roi into later analyses | shape = (104,) | dtype = bool
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/neuropil_mask (VectorData) mask of neurophil surrounding this roi | shape = (104, 512, 512) | dtype = bool
  session_description: Imaging session
  session_start_time: 2013-10-09T00:00:00+00:00
  timestamps_reference_time: 2013-10-09T00:00:00+00:00


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  Group /acquisition/BehavioralEvents (BehavioralEvents) 
  Group /acquisition/BehavioralEvents/delay (TimeSeries) no description
  Group /acquisition/BehavioralEvents/go (TimeSeries) no description
  Group /acquisition/BehavioralEvents/photostim_start_time (TimeSeries) no description
  Group /acquisition/BehavioralEvents/photostim_stop_time (TimeSeries) no description
  Group /acquisition/BehavioralEvents/sample (TimeSeries) no description
  Group /acquisition/BehavioralTimeSeries (BehavioralTimeSeries) 
  Group /acquisition/BehavioralTimeSeries/lick_trace (TimeSeries) Time-series of the animal's tongue movement when licking
  file_create_date: ['2020-02-20T15:28:19.438200-06:00']
  Group /general/devices/A4x8-5mm-100-200-177 (Device) 
  Group /general/devices/LaserGem473 (Device) 
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
  keywords: ['motor planning' 'preparatory activity' 'whiskers'
   'optogenetic perturbations' 'extracellular electrophysiology']
  Group /general/optogenetics/bilateral ALM (OptogeneticStimulusSite) 
  Group /general/optogenetics/bilateral ALM/device (Device) 
  Group /general/optogenetics/left PONS (OptogeneticStimulusSite) 
  Group /general/optogenetics/left PONS/device (Device) 
  related_publications: ['doi:10.1038/nature14178']
  Group /general/subject (Subject) 
  virus: [{"injection_id": "1", "virus": "Addgene41015", "injection_date": "2013-07-14", "injection_volume": "100.0", "brain_area": "M2", "hemisphere": "left", "virus_source": "Janelia core", "virus_lot_number": "", "virus_titer": "None"}, {"injection_id": "2", "virus": "Addgene41015", "injection_date": "2013-07-14", "injection_volume": "100.0", "brain_area": "M2", "hemisphere": "left", "virus_source": "Janelia core", "virus_lot_number": "", "virus_titer": "None"}]
  identifier: ANM214427_2013-08-07_3
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/early_lick (VectorData) varchar(32) # | shape = (550,) | dtype = object
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (550,) | dtype = int32
  Dataset /intervals/trials/outcome (VectorData) varchar(32) # | shape = (550,) | dtype = object
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (550,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (550,) | dtype = float64
  Dataset /intervals/trials/task (VectorData) varchar(12) # task type | shape = (550,) | dtype = object
  Dataset /intervals/trials/task_protocol (VectorData) tinyint # task protocol | shape = (550,) | dtype = int32
  Dataset /intervals/trials/trial_instruction (VectorData) varchar(16) # | shape = (550,) | dtype = object
  session_description: 
  session_start_time: 2013-08-07T00:00:00-05:00
  Group /stimulus/presentation/bilateral ALM_aom_input_trace (OptogeneticSeries) no description
  Group /stimulus/presentation/bilateral ALM_aom_input_trace/site (OptogeneticStimulusSite) 
  Group /stimulus/presentation/bilateral ALM_aom_input_trace/site/device (Device) 
  Group /stimulus/presentation/bilateral ALM_laser_power (OptogeneticSeries) no description
  Group /stimulus/presentation/bilateral ALM_laser_power/site (OptogeneticStimulusSite) 
  Group /stimulus/presentation/bilateral ALM_laser_power/site/device (Device) 
  timestamps_reference_time: 2013-08-07T00:00:00-05:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/cell_type (VectorData) cell type (e.g. fast spiking or pyramidal) | shape = (5,) | dtype = object
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (5,) | dtype = object
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (5,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex)  | shape = (5,) | dtype = int32
  Dataset /units/id (ElementIdentifiers)  | shape = (5,) | dtype = int32
  Dataset /units/obs_intervals (VectorData) the observation intervals for each unit | shape = (2135, 2) | dtype = float64
  Dataset /units/obs_intervals_index (VectorIndex)  | shape = (5,) | dtype = int32
  Dataset /units/posx (VectorData) estimated x position of the unit relative to probe (0,0) (um) | shape = (5,) | dtype = float64
  Dataset /units/posy (VectorData) estimated y position of the unit relative to probe (0,0) (um) | shape = (5,) | dtype = float64
  Dataset /units/quality (VectorData) unit quality from clustering | shape = (5,) | dtype = object
  Dataset /units/sampling_rate (VectorData) Sampling rate of the raw voltage traces (Hz) | shape = (5,) | dtype = float64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (21028,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex)  | shape = (5,) | dtype = int32
  Dataset /units/waveform_mean (VectorData) the spike waveform mean for each spike unit | shape = (5, 29) | dtype = float64
  Dataset /units/waveform_sd (VectorData) the spike waveform standard deviation for each spike unit | shape = (5, 29) | dtype = float64
