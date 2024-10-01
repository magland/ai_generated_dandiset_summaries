
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000572/0.230826.0140
name: Activity map of a cortico-cerebellar loop underlying motor planning
contributor: [{'name': 'li, nuo', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'awardNumber': '1 R01 NS 112312-01', 'includeInCitation': False}]
description: Data from "Activity map of a cortico-cerebellar loop underlying motor planning" Jia Zhu, Hana Hasanbegovic, Liu D. Liu, Zhenyu Gao, Nuo Li. Nat Neurosci 2023

An activity map of the cerebellar cortex during a delayed response task in which mice used short-term memory to plan directional licking.

Supported by Robert and Janice McNair Foundation, Whitehall Foundation, Alfred P. Sloan Foundation, Searle Scholars Program, Pew Scholars Program, NIH NS104781, NS112312, NS113110, McKnight Foundation, Simons Collaboration on the Global Brain.

assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}, {'name': 'optogenetic approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 311812040462, 'numberOfFiles': 289, 'numberOfSubjects': 37, 'variableMeasured': ['OptogeneticSeries', 'SpikeEventSeries', 'ElectrodeGroup', 'Units'], 'measurementTechnique': [{'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000572 has 7 NWB files.
1 of these NWB files are of type 1.
3 of these NWB files are of type 2.
1 of these NWB files are of type 3.
1 of these NWB files are of type 4.
1 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /analysis/unit10SS (SpikeEventSeries) single unit10SS with cell type information and approximate depth
  Dataset /analysis/unit10SS/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (33019,) | dtype = int64
  Group /analysis/unit11SS (SpikeEventSeries) single unit11SS with cell type information and approximate depth
  Dataset /analysis/unit11SS/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (1205,) | dtype = int64
  Group /analysis/unit12CS (SpikeEventSeries) single unit12CS with cell type information and approximate depth
  Dataset /analysis/unit12CS/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (4897,) | dtype = int64
  Group /analysis/unit12SS (SpikeEventSeries) single unit12SS with cell type information and approximate depth
  Dataset /analysis/unit12SS/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (345401,) | dtype = int64
  Group /analysis/unit1SS (SpikeEventSeries) single unit1SS with cell type information and approximate depth
  Dataset /analysis/unit1SS/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (36355,) | dtype = int64
  Group /analysis/unit2SS (SpikeEventSeries) single unit2SS with cell type information and approximate depth
  Dataset /analysis/unit2SS/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (27863,) | dtype = int64
  Group /analysis/unit3SS (SpikeEventSeries) single unit3SS with cell type information and approximate depth
  Dataset /analysis/unit3SS/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (3572,) | dtype = int64
  Group /analysis/unit4SS (SpikeEventSeries) single unit4SS with cell type information and approximate depth
  Dataset /analysis/unit4SS/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (6499,) | dtype = int64
  Group /analysis/unit5SS (SpikeEventSeries) single unit5SS with cell type information and approximate depth
  Dataset /analysis/unit5SS/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (1775,) | dtype = int64
  Group /analysis/unit6SS (SpikeEventSeries) single unit6SS with cell type information and approximate depth
  Dataset /analysis/unit6SS/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (8112,) | dtype = int64
  Group /analysis/unit7SS (SpikeEventSeries) single unit7SS with cell type information and approximate depth
  Dataset /analysis/unit7SS/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (5247,) | dtype = int64
  Group /analysis/unit8SS (SpikeEventSeries) single unit8SS with cell type information and approximate depth
  Dataset /analysis/unit8SS/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (23527,) | dtype = int64
  Group /analysis/unit9SS (SpikeEventSeries) single unit9SS with cell type information and approximate depth
  Dataset /analysis/unit9SS/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (23875,) | dtype = int64
  file_create_date: ['2023-08-03T16:05:20.052201-05:00']
  data_collection: extracellularDataType: sorted spike times, spike waveform snipets, spike band voltage traces
  cellType: Identified PC, others
  identificationMethod: SS and CS spike waveforms and cross-correlogram, spike waveforms
  amplifierRolloff: 
  spikeSorting: manual:matclust
  ADunit: 14 bits
  Group /general/devices/Cambridge NeuroTech 64ch H2 probe 2x32 shank1:ch1-32 shank2:ch33-64 (Cambridge NeuroTech) (Device) 
  Group /general/devices/laser-473nm (Utralaser) (Device) 
  experiment_description: experimentType: behavior, extracellular, photostim
  referenceAtlas: Allen Reference Atlas
  task_keyword: detection, discrimination, lick Left lick Right, delay, somatosensory, motor, response, reward
  experimenter: ['Zhu, Jia']
  Group /general/extracellular_ephys/Cambridge NeuroTech 64ch H2 probe 2x32 shank1:ch1-32 shank2:ch33-64 (Cambridge NeuroTech) (ElectrodeGroup) recordingCoordinates: -3           -0.5           1200
  recordingMarker: stereotaxic coordinate from lambda
  recordingType: acute
  penetrationN: 1
  groundCoordinates: [1 -1  1]
  referenceCoordinates: []
  Group /general/extracellular_ephys/Cambridge NeuroTech 64ch H2 probe 2x32 shank1:ch1-32 shank2:ch33-64 (Cambridge NeuroTech)/device (Device) 
  Group /general/extracellular_ephys/electrodes (DynamicTable) Electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (52,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (52,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (52,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (52,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (52,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (52,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (52,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (52,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (52,) | dtype = float64
  institution: Baylor College of Medicine, Houston, TX 77030
  keywords: ['Motor planning' 'Cerebellar cortex' 'Short-term memory']
  lab: Nuo Li
  Group /general/optogenetics/photostim (OptogeneticStimulusSite) 
  Group /general/optogenetics/photostim/device (Device) 
  protocol: IACUC
  related_publications: ['Jia Zhu, Hana Hasanbegović, Liu D. Liu, Zhenyu Gao,  Nuo LiActivity map of a cortico-cerebellar loop underlying motor planning2023, Nature Neuroscience']
  session_id: 20190225
  source_script: batch_convertTrials4jia
  stimulus: photostim
  Group /general/subject (Subject) 
  surgery: Mice were prepared for photoinhibition and electrophysiology with a clear-skull cap and a headpost. The scalp and periosteum over the dorsal surface of the skull were removed. A layer of cyanoacrylate adhesive (Krazy glue, Elmer's Products Inc.) was directly applied to the intact skull. A custom made headpost was placed on the skull with its posterior edge aligned with the suture lambda and cemented in place with clear dental acrylic (Lang Dental Jet Repair Acrylic; 1223-clear). A thin layer of clear dental acrylic was applied over the cyanoacrylate adhesive covering the entire exposed skull, followed by a thin layer of clear nail polish (Electron Microscopy Sciences, 72180).
  identifier: BAYLORNL23_20190225
  Group /intervals/trials (TimeIntervals) trial data and properties
  Dataset /intervals/trials/CueTime (VectorData) Start of Response period (in seconds, relative to trial start time) | shape = (258, 2) | dtype = float64
  Dataset /intervals/trials/ErrL (VectorData) ErrL | shape = (258,) | dtype = bool
  Dataset /intervals/trials/ErrR (VectorData) ErrR | shape = (258,) | dtype = bool
  Dataset /intervals/trials/GoodTrials (VectorData) 0 for trials in which mice are not performing, discard for analyses | shape = (258,) | dtype = bool
  Dataset /intervals/trials/HitL (VectorData) HitL | shape = (258,) | dtype = bool
  Dataset /intervals/trials/HitR (VectorData) HitR | shape = (258,) | dtype = bool
  Dataset /intervals/trials/LickEarly (VectorData) LickEarly | shape = (258,) | dtype = bool
  Dataset /intervals/trials/NoLickL (VectorData) NoLickL | shape = (258,) | dtype = bool
  Dataset /intervals/trials/NoLickR (VectorData) NoLickR | shape = (258,) | dtype = bool
  Dataset /intervals/trials/PhotostimulationType (VectorData) "0"--non-stimulation trials;
  "1"--photoinhibition of left ALM; One light spot (diameter 1 mm); Early Delay (start from the onset of delay epoch); 800ms (200ms ramp);
  "2"--photoinhibition of right ALM; One light spot (diameter 1 mm); Early Delay (start from the onset of delay epoch); 800ms (200ms ramp);
  "3"--photoinhibition of both left and right ALM; Four light spots for each side; Early Delay (start from the onset of delay epoch); 800ms (200ms ramp);
  "NaN and others"--discard (stimulation configuration for other purposes, should not analyze) | shape = (258,) | dtype = float64
  Dataset /intervals/trials/PoleInTime (VectorData) Start of Sample period (in seconds, relative to trial start time) | shape = (258,) | dtype = float64
  Dataset /intervals/trials/PoleOutTime (VectorData) Start of Delay period (in seconds, relative to trial start time) | shape = (258,) | dtype = float64
  Dataset /intervals/trials/StimTrials (VectorData) StimTrials | shape = (258,) | dtype = bool
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (258,) | dtype = int64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds. | shape = (258,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) the end time of each trial | shape = (258,) | dtype = float64
  Dataset /intervals/trials/timeseries (TimeSeriesReferenceVectorData) A group of timeseries | shape = (2606,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/trials/timeseries_index (VectorIndex) Index into Timeseries VectorData | shape = (258,) | dtype = uint64
  session_description: Animal `BAYLORNL23` on Session `20190225`
  session_start_time: 2019-02-25T10:28:22.000000-06:00
  Group /stimulus/presentation/aom_input_trace (TimeSeries) voltage input to AOM
  Group /stimulus/presentation/laser_power (OptogeneticSeries) laser power delivered to tissue (mW)
  Group /stimulus/presentation/laser_power/site (OptogeneticStimulusSite) 
  Group /stimulus/presentation/laser_power/site/device (Device) 
  timestamps_reference_time: 2019-02-25T10:28:22.000000-06:00
  Group /units (Units) Analysed Spike Events
  Dataset /units/id (ElementIdentifiers)  | shape = (13,) | dtype = int64
  Dataset /units/spike_times (VectorData) timestamps of spikes | shape = (521347,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) index into timestamps of spikes | shape = (13,) | dtype = uint64
  Dataset /units/trials (VectorData) A large group of trial IDs for each unit | shape = (521347,) | dtype = float64
  Dataset /units/trials_index (VectorIndex) Index into Trials vector data | shape = (13,) | dtype = uint64


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /analysis/unit10SS (SpikeEventSeries) single unit10SS with cell type information and approximate depth
  Dataset /analysis/unit10SS/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (27433,) | dtype = int64
  Group /analysis/unit11SS (SpikeEventSeries) single unit11SS with cell type information and approximate depth
  Dataset /analysis/unit11SS/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (43296,) | dtype = int64
  Group /analysis/unit12SS (SpikeEventSeries) single unit12SS with cell type information and approximate depth
  Dataset /analysis/unit12SS/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (3222,) | dtype = int64
  Group /analysis/unit13SS (SpikeEventSeries) single unit13SS with cell type information and approximate depth
  Dataset /analysis/unit13SS/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (31256,) | dtype = int64
  Group /analysis/unit1SS (SpikeEventSeries) single unit1SS with cell type information and approximate depth
  Dataset /analysis/unit1SS/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (57320,) | dtype = int64
  Group /analysis/unit2SS (SpikeEventSeries) single unit2SS with cell type information and approximate depth
  Dataset /analysis/unit2SS/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (70383,) | dtype = int64
  Group /analysis/unit3SS (SpikeEventSeries) single unit3SS with cell type information and approximate depth
  Dataset /analysis/unit3SS/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (164961,) | dtype = int64
  Group /analysis/unit4SS (SpikeEventSeries) single unit4SS with cell type information and approximate depth
  Dataset /analysis/unit4SS/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (1550,) | dtype = int64
  Group /analysis/unit5SS (SpikeEventSeries) single unit5SS with cell type information and approximate depth
  Dataset /analysis/unit5SS/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (889,) | dtype = int64
  Group /analysis/unit6SS (SpikeEventSeries) single unit6SS with cell type information and approximate depth
  Dataset /analysis/unit6SS/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (59572,) | dtype = int64
  Group /analysis/unit7SS (SpikeEventSeries) single unit7SS with cell type information and approximate depth
  Dataset /analysis/unit7SS/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (1388,) | dtype = int64
  Group /analysis/unit8SS (SpikeEventSeries) single unit8SS with cell type information and approximate depth
  Dataset /analysis/unit8SS/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (20611,) | dtype = int64
  Group /analysis/unit9SS (SpikeEventSeries) single unit9SS with cell type information and approximate depth
  Dataset /analysis/unit9SS/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (15386,) | dtype = int64
  file_create_date: ['2023-08-03T16:06:16.692809-05:00']
  data_collection: extracellularDataType: sorted spike times, spike waveform snipets, spike band voltage traces
  cellType: Identified PC, others
  identificationMethod: SS and CS spike waveforms and cross-correlogram, spike waveforms
  amplifierRolloff: 
  spikeSorting: manual:matclust
  ADunit: 14 bits
  Group /general/devices/Cambridge NeuroTech 64ch H2 probe 2x32 shank1:ch1-32 shank2:ch33-64 (Cambridge NeuroTech) (Device) 
  Group /general/devices/laser-473nm (Utralaser) (Device) 
  experiment_description: experimentType: behavior, extracellular, photostim
  referenceAtlas: Allen Reference Atlas
  task_keyword: detection, discrimination, lick Left lick Right, delay, somatosensory, motor, response, reward
  experimenter: ['Zhu, Jia']
  Group /general/extracellular_ephys/Cambridge NeuroTech 64ch H2 probe 2x32 shank1:ch1-32 shank2:ch33-64 (Cambridge NeuroTech) (ElectrodeGroup) recordingCoordinates: -3           -0.5           1400
  recordingMarker: stereotaxic coordinate from lambda
  recordingType: acute
  penetrationN: 2
  groundCoordinates: [1 -1  1]
  referenceCoordinates: []
  Group /general/extracellular_ephys/Cambridge NeuroTech 64ch H2 probe 2x32 shank1:ch1-32 shank2:ch33-64 (Cambridge NeuroTech)/device (Device) 
  Group /general/extracellular_ephys/electrodes (DynamicTable) Electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (48,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (48,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (48,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (48,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (48,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (48,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (48,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (48,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (48,) | dtype = float64
  institution: Baylor College of Medicine, Houston, TX 77030
  keywords: ['Motor planning' 'Cerebellar cortex' 'Short-term memory']
  lab: Nuo Li
  Group /general/optogenetics/photostim (OptogeneticStimulusSite) 
  Group /general/optogenetics/photostim/device (Device) 
  protocol: IACUC
  related_publications: ['Jia Zhu, Hana Hasanbegović, Liu D. Liu, Zhenyu Gao,  Nuo LiActivity map of a cortico-cerebellar loop underlying motor planning2023, Nature Neuroscience']
  session_id: 20190226
  source_script: batch_convertTrials4jia
  stimulus: photostim
  Group /general/subject (Subject) 
  surgery: Mice were prepared for photoinhibition and electrophysiology with a clear-skull cap and a headpost. The scalp and periosteum over the dorsal surface of the skull were removed. A layer of cyanoacrylate adhesive (Krazy glue, Elmer's Products Inc.) was directly applied to the intact skull. A custom made headpost was placed on the skull with its posterior edge aligned with the suture lambda and cemented in place with clear dental acrylic (Lang Dental Jet Repair Acrylic; 1223-clear). A thin layer of clear dental acrylic was applied over the cyanoacrylate adhesive covering the entire exposed skull, followed by a thin layer of clear nail polish (Electron Microscopy Sciences, 72180).
  identifier: BAYLORNL23_20190226
  Group /intervals/trials (TimeIntervals) trial data and properties
  Dataset /intervals/trials/CueTime (VectorData) Start of Response period (in seconds, relative to trial start time) | shape = (207, 2) | dtype = float64
  Dataset /intervals/trials/ErrL (VectorData) ErrL | shape = (207,) | dtype = bool
  Dataset /intervals/trials/ErrR (VectorData) ErrR | shape = (207,) | dtype = bool
  Dataset /intervals/trials/GoodTrials (VectorData) 0 for trials in which mice are not performing, discard for analyses | shape = (207,) | dtype = bool
  Dataset /intervals/trials/HitL (VectorData) HitL | shape = (207,) | dtype = bool
  Dataset /intervals/trials/HitR (VectorData) HitR | shape = (207,) | dtype = bool
  Dataset /intervals/trials/LickEarly (VectorData) LickEarly | shape = (207,) | dtype = bool
  Dataset /intervals/trials/NoLickL (VectorData) NoLickL | shape = (207,) | dtype = bool
  Dataset /intervals/trials/NoLickR (VectorData) NoLickR | shape = (207,) | dtype = bool
  Dataset /intervals/trials/PhotostimulationType (VectorData) "0"--non-stimulation trials;
  "1"--photoinhibition of left ALM; One light spot (diameter 1 mm); Early Delay (start from the onset of delay epoch); 800ms (200ms ramp);
  "2"--photoinhibition of right ALM; One light spot (diameter 1 mm); Early Delay (start from the onset of delay epoch); 800ms (200ms ramp);
  "3"--photoinhibition of both left and right ALM; Four light spots for each side; Early Delay (start from the onset of delay epoch); 800ms (200ms ramp);
  "NaN and others"--discard (stimulation configuration for other purposes, should not analyze) | shape = (207,) | dtype = float64
  Dataset /intervals/trials/PoleInTime (VectorData) Start of Sample period (in seconds, relative to trial start time) | shape = (207,) | dtype = float64
  Dataset /intervals/trials/PoleOutTime (VectorData) Start of Delay period (in seconds, relative to trial start time) | shape = (207,) | dtype = float64
  Dataset /intervals/trials/StimTrials (VectorData) StimTrials | shape = (207,) | dtype = bool
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (207,) | dtype = int64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds. | shape = (207,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) the end time of each trial | shape = (207,) | dtype = float64
  Dataset /intervals/trials/timeseries (TimeSeriesReferenceVectorData) A group of timeseries | shape = (2238,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/trials/timeseries_index (VectorIndex) Index into Timeseries VectorData | shape = (207,) | dtype = uint64
  session_description: Animal `BAYLORNL23` on Session `20190226`
  session_start_time: 2019-02-26T10:29:43.000000-06:00
  Group /stimulus/presentation/aom_input_trace (TimeSeries) voltage input to AOM
  Group /stimulus/presentation/laser_power (OptogeneticSeries) laser power delivered to tissue (mW)
  Group /stimulus/presentation/laser_power/site (OptogeneticStimulusSite) 
  Group /stimulus/presentation/laser_power/site/device (Device) 
  timestamps_reference_time: 2019-02-26T10:29:43.000000-06:00
  Group /units (Units) Analysed Spike Events
  Dataset /units/id (ElementIdentifiers)  | shape = (13,) | dtype = int64
  Dataset /units/spike_times (VectorData) timestamps of spikes | shape = (497267,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) index into timestamps of spikes | shape = (13,) | dtype = uint64
  Dataset /units/trials (VectorData) A large group of trial IDs for each unit | shape = (497267,) | dtype = float64
  Dataset /units/trials_index (VectorIndex) Index into Trials vector data | shape = (13,) | dtype = uint64


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /analysis/unit1SS (SpikeEventSeries) single unit1SS with cell type information and approximate depth
  Dataset /analysis/unit1SS/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (94522,) | dtype = int64
  Group /analysis/unit2CS (SpikeEventSeries) single unit2CS with cell type information and approximate depth
  Dataset /analysis/unit2CS/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (4222,) | dtype = int64
  Group /analysis/unit2SS (SpikeEventSeries) single unit2SS with cell type information and approximate depth
  Dataset /analysis/unit2SS/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (356792,) | dtype = int64
  Group /analysis/unit3SS (SpikeEventSeries) single unit3SS with cell type information and approximate depth
  Dataset /analysis/unit3SS/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (4656,) | dtype = int64
  Group /analysis/unit4SS (SpikeEventSeries) single unit4SS with cell type information and approximate depth
  Dataset /analysis/unit4SS/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (22854,) | dtype = int64
  Group /analysis/unit5SS (SpikeEventSeries) single unit5SS with cell type information and approximate depth
  Dataset /analysis/unit5SS/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (113285,) | dtype = int64
  file_create_date: ['2023-08-03T16:07:31.217687-05:00']
  data_collection: extracellularDataType: sorted spike times, spike waveform snipets, spike band voltage traces
  cellType: Identified PC, others
  identificationMethod: SS and CS spike waveforms and cross-correlogram, spike waveforms
  amplifierRolloff: 
  spikeSorting: manual:matclust
  ADunit: 14 bits
  Group /general/devices/Cambridge NeuroTech 64ch H2 probe 2x32 shank1:ch1-32 shank2:ch33-64 (Cambridge NeuroTech) (Device) 
  Group /general/devices/laser-473nm (Utralaser) (Device) 
  experiment_description: experimentType: behavior, extracellular, photostim
  referenceAtlas: Allen Reference Atlas
  task_keyword: detection, discrimination, lick Left lick Right, delay, somatosensory, motor, response, reward
  experimenter: ['Zhu, Jia']
  Group /general/extracellular_ephys/Cambridge NeuroTech 64ch H2 probe 2x32 shank1:ch1-32 shank2:ch33-64 (Cambridge NeuroTech) (ElectrodeGroup) recordingCoordinates: -3           -0.5           1500
  recordingMarker: stereotaxic coordinate from lambda
  recordingType: acute
  penetrationN: 3
  groundCoordinates: [1 -1  1]
  referenceCoordinates: []
  Group /general/extracellular_ephys/Cambridge NeuroTech 64ch H2 probe 2x32 shank1:ch1-32 shank2:ch33-64 (Cambridge NeuroTech)/device (Device) 
  Group /general/extracellular_ephys/electrodes (DynamicTable) Electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (55,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (55,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (55,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (55,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (55,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (55,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (55,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (55,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (55,) | dtype = float64
  institution: Baylor College of Medicine, Houston, TX 77030
  keywords: ['Motor planning' 'Cerebellar cortex' 'Short-term memory']
  lab: Nuo Li
  Group /general/optogenetics/photostim (OptogeneticStimulusSite) 
  Group /general/optogenetics/photostim/device (Device) 
  protocol: IACUC
  related_publications: ['Jia Zhu, Hana Hasanbegović, Liu D. Liu, Zhenyu Gao,  Nuo LiActivity map of a cortico-cerebellar loop underlying motor planning2023, Nature Neuroscience']
  session_id: 20190228
  source_script: batch_convertTrials4jia
  stimulus: photostim
  Group /general/subject (Subject) 
  surgery: Mice were prepared for photoinhibition and electrophysiology with a clear-skull cap and a headpost. The scalp and periosteum over the dorsal surface of the skull were removed. A layer of cyanoacrylate adhesive (Krazy glue, Elmer's Products Inc.) was directly applied to the intact skull. A custom made headpost was placed on the skull with its posterior edge aligned with the suture lambda and cemented in place with clear dental acrylic (Lang Dental Jet Repair Acrylic; 1223-clear). A thin layer of clear dental acrylic was applied over the cyanoacrylate adhesive covering the entire exposed skull, followed by a thin layer of clear nail polish (Electron Microscopy Sciences, 72180).
  identifier: BAYLORNL23_20190228
  Group /intervals/trials (TimeIntervals) trial data and properties
  Dataset /intervals/trials/CueTime (VectorData) Start of Response period (in seconds, relative to trial start time) | shape = (273, 2) | dtype = float64
  Dataset /intervals/trials/ErrL (VectorData) ErrL | shape = (273,) | dtype = bool
  Dataset /intervals/trials/ErrR (VectorData) ErrR | shape = (273,) | dtype = bool
  Dataset /intervals/trials/GoodTrials (VectorData) 0 for trials in which mice are not performing, discard for analyses | shape = (273,) | dtype = bool
  Dataset /intervals/trials/HitL (VectorData) HitL | shape = (273,) | dtype = bool
  Dataset /intervals/trials/HitR (VectorData) HitR | shape = (273,) | dtype = bool
  Dataset /intervals/trials/LickEarly (VectorData) LickEarly | shape = (273,) | dtype = bool
  Dataset /intervals/trials/NoLickL (VectorData) NoLickL | shape = (273,) | dtype = bool
  Dataset /intervals/trials/NoLickR (VectorData) NoLickR | shape = (273,) | dtype = bool
  Dataset /intervals/trials/PhotostimulationType (VectorData) "0"--non-stimulation trials;
  "1"--photoinhibition of left ALM; One light spot (diameter 1 mm); Early Delay (start from the onset of delay epoch); 800ms (200ms ramp);
  "2"--photoinhibition of right ALM; One light spot (diameter 1 mm); Early Delay (start from the onset of delay epoch); 800ms (200ms ramp);
  "3"--photoinhibition of both left and right ALM; Four light spots for each side; Early Delay (start from the onset of delay epoch); 800ms (200ms ramp);
  "NaN and others"--discard (stimulation configuration for other purposes, should not analyze) | shape = (273,) | dtype = float64
  Dataset /intervals/trials/PoleInTime (VectorData) Start of Sample period (in seconds, relative to trial start time) | shape = (273,) | dtype = float64
  Dataset /intervals/trials/PoleOutTime (VectorData) Start of Delay period (in seconds, relative to trial start time) | shape = (273,) | dtype = float64
  Dataset /intervals/trials/StimTrials (VectorData) StimTrials | shape = (273,) | dtype = bool
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (273,) | dtype = int64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds. | shape = (273,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) the end time of each trial | shape = (273,) | dtype = float64
  Dataset /intervals/trials/timeseries (TimeSeriesReferenceVectorData) A group of timeseries | shape = (1514,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/trials/timeseries_index (VectorIndex) Index into Timeseries VectorData | shape = (273,) | dtype = uint64
  session_description: Animal `BAYLORNL23` on Session `20190228`
  session_start_time: 2019-02-28T11:25:06.000000-06:00
  Group /stimulus/presentation/aom_input_trace (TimeSeries) voltage input to AOM
  Group /stimulus/presentation/laser_power (OptogeneticSeries) laser power delivered to tissue (mW)
  Group /stimulus/presentation/laser_power/site (OptogeneticStimulusSite) 
  Group /stimulus/presentation/laser_power/site/device (Device) 
  timestamps_reference_time: 2019-02-28T11:25:06.000000-06:00
  Group /units (Units) Analysed Spike Events
  Dataset /units/id (ElementIdentifiers)  | shape = (6,) | dtype = int64
  Dataset /units/spike_times (VectorData) timestamps of spikes | shape = (596331,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) index into timestamps of spikes | shape = (6,) | dtype = uint64
  Dataset /units/trials (VectorData) A large group of trial IDs for each unit | shape = (596331,) | dtype = float64
  Dataset /units/trials_index (VectorIndex) Index into Trials vector data | shape = (6,) | dtype = uint64


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /analysis/unit10SS (SpikeEventSeries) single unit10SS with cell type information and approximate depth
  Dataset /analysis/unit10SS/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (8490,) | dtype = int64
  Group /analysis/unit11SS (SpikeEventSeries) single unit11SS with cell type information and approximate depth
  Dataset /analysis/unit11SS/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (9020,) | dtype = int64
  Group /analysis/unit12SS (SpikeEventSeries) single unit12SS with cell type information and approximate depth
  Dataset /analysis/unit12SS/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (47067,) | dtype = int64
  Group /analysis/unit13SS (SpikeEventSeries) single unit13SS with cell type information and approximate depth
  Dataset /analysis/unit13SS/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (4795,) | dtype = int64
  Group /analysis/unit14SS (SpikeEventSeries) single unit14SS with cell type information and approximate depth
  Dataset /analysis/unit14SS/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (68414,) | dtype = int64
  Group /analysis/unit15SS (SpikeEventSeries) single unit15SS with cell type information and approximate depth
  Dataset /analysis/unit15SS/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (2134,) | dtype = int64
  Group /analysis/unit16SS (SpikeEventSeries) single unit16SS with cell type information and approximate depth
  Dataset /analysis/unit16SS/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (30472,) | dtype = int64
  Group /analysis/unit17SS (SpikeEventSeries) single unit17SS with cell type information and approximate depth
  Dataset /analysis/unit17SS/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (1469,) | dtype = int64
  Group /analysis/unit1SS (SpikeEventSeries) single unit1SS with cell type information and approximate depth
  Dataset /analysis/unit1SS/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (9054,) | dtype = int64
  Group /analysis/unit2SS (SpikeEventSeries) single unit2SS with cell type information and approximate depth
  Dataset /analysis/unit2SS/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (1289,) | dtype = int64
  Group /analysis/unit3SS (SpikeEventSeries) single unit3SS with cell type information and approximate depth
  Dataset /analysis/unit3SS/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (2068,) | dtype = int64
  Group /analysis/unit4SS (SpikeEventSeries) single unit4SS with cell type information and approximate depth
  Dataset /analysis/unit4SS/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (40718,) | dtype = int64
  Group /analysis/unit5SS (SpikeEventSeries) single unit5SS with cell type information and approximate depth
  Dataset /analysis/unit5SS/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (123991,) | dtype = int64
  Group /analysis/unit6SS (SpikeEventSeries) single unit6SS with cell type information and approximate depth
  Dataset /analysis/unit6SS/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (32575,) | dtype = int64
  Group /analysis/unit7SS (SpikeEventSeries) single unit7SS with cell type information and approximate depth
  Dataset /analysis/unit7SS/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (172558,) | dtype = int64
  Group /analysis/unit8SS (SpikeEventSeries) single unit8SS with cell type information and approximate depth
  Dataset /analysis/unit8SS/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (26558,) | dtype = int64
  Group /analysis/unit9SS (SpikeEventSeries) single unit9SS with cell type information and approximate depth
  Dataset /analysis/unit9SS/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (18058,) | dtype = int64
  file_create_date: ['2023-08-03T16:08:44.038848-05:00']
  data_collection: extracellularDataType: sorted spike times, spike waveform snipets, spike band voltage traces
  cellType: Identified PC, others
  identificationMethod: SS and CS spike waveforms and cross-correlogram, spike waveforms
  amplifierRolloff: 
  spikeSorting: manual:matclust
  ADunit: 14 bits
  Group /general/devices/Cambridge NeuroTech 64ch H2 probe 2x32 shank1:ch1-32 shank2:ch33-64 (Cambridge NeuroTech) (Device) 
  Group /general/devices/laser-473nm (Utralaser) (Device) 
  experiment_description: experimentType: behavior, extracellular, photostim
  referenceAtlas: Allen Reference Atlas
  task_keyword: detection, discrimination, lick Left lick Right, delay, somatosensory, motor, response, reward
  experimenter: ['Zhu, Jia']
  Group /general/extracellular_ephys/Cambridge NeuroTech 64ch H2 probe 2x32 shank1:ch1-32 shank2:ch33-64 (Cambridge NeuroTech) (ElectrodeGroup) recordingCoordinates: -3           -0.5           1700
  recordingMarker: stereotaxic coordinate from lambda
  recordingType: acute
  penetrationN: 4
  groundCoordinates: [1 -1  1]
  referenceCoordinates: []
  Group /general/extracellular_ephys/Cambridge NeuroTech 64ch H2 probe 2x32 shank1:ch1-32 shank2:ch33-64 (Cambridge NeuroTech)/device (Device) 
  Group /general/extracellular_ephys/electrodes (DynamicTable) Electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (59,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (59,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (59,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (59,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (59,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (59,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (59,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (59,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (59,) | dtype = float64
  institution: Baylor College of Medicine, Houston, TX 77030
  keywords: ['Motor planning' 'Cerebellar cortex' 'Short-term memory']
  lab: Nuo Li
  Group /general/optogenetics/photostim (OptogeneticStimulusSite) 
  Group /general/optogenetics/photostim/device (Device) 
  protocol: IACUC
  related_publications: ['Jia Zhu, Hana Hasanbegović, Liu D. Liu, Zhenyu Gao,  Nuo LiActivity map of a cortico-cerebellar loop underlying motor planning2023, Nature Neuroscience']
  session_id: 20190301
  source_script: batch_convertTrials4jia
  stimulus: photostim
  Group /general/subject (Subject) 
  surgery: Mice were prepared for photoinhibition and electrophysiology with a clear-skull cap and a headpost. The scalp and periosteum over the dorsal surface of the skull were removed. A layer of cyanoacrylate adhesive (Krazy glue, Elmer's Products Inc.) was directly applied to the intact skull. A custom made headpost was placed on the skull with its posterior edge aligned with the suture lambda and cemented in place with clear dental acrylic (Lang Dental Jet Repair Acrylic; 1223-clear). A thin layer of clear dental acrylic was applied over the cyanoacrylate adhesive covering the entire exposed skull, followed by a thin layer of clear nail polish (Electron Microscopy Sciences, 72180).
  identifier: BAYLORNL23_20190301
  Group /intervals/trials (TimeIntervals) trial data and properties
  Dataset /intervals/trials/CueTime (VectorData) Start of Response period (in seconds, relative to trial start time) | shape = (259, 2) | dtype = float64
  Dataset /intervals/trials/ErrL (VectorData) ErrL | shape = (259,) | dtype = bool
  Dataset /intervals/trials/ErrR (VectorData) ErrR | shape = (259,) | dtype = bool
  Dataset /intervals/trials/GoodTrials (VectorData) 0 for trials in which mice are not performing, discard for analyses | shape = (259,) | dtype = bool
  Dataset /intervals/trials/HitL (VectorData) HitL | shape = (259,) | dtype = bool
  Dataset /intervals/trials/HitR (VectorData) HitR | shape = (259,) | dtype = bool
  Dataset /intervals/trials/LickEarly (VectorData) LickEarly | shape = (259,) | dtype = bool
  Dataset /intervals/trials/NoLickL (VectorData) NoLickL | shape = (259,) | dtype = bool
  Dataset /intervals/trials/NoLickR (VectorData) NoLickR | shape = (259,) | dtype = bool
  Dataset /intervals/trials/PhotostimulationType (VectorData) "0"--non-stimulation trials;
  "1"--photoinhibition of left ALM; One light spot (diameter 1 mm); Early Delay (start from the onset of delay epoch); 800ms (200ms ramp);
  "2"--photoinhibition of right ALM; One light spot (diameter 1 mm); Early Delay (start from the onset of delay epoch); 800ms (200ms ramp);
  "3"--photoinhibition of both left and right ALM; Four light spots for each side; Early Delay (start from the onset of delay epoch); 800ms (200ms ramp);
  "NaN and others"--discard (stimulation configuration for other purposes, should not analyze) | shape = (259,) | dtype = float64
  Dataset /intervals/trials/PoleInTime (VectorData) Start of Sample period (in seconds, relative to trial start time) | shape = (259,) | dtype = float64
  Dataset /intervals/trials/PoleOutTime (VectorData) Start of Delay period (in seconds, relative to trial start time) | shape = (259,) | dtype = float64
  Dataset /intervals/trials/StimTrials (VectorData) StimTrials | shape = (259,) | dtype = bool
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (259,) | dtype = int64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds. | shape = (259,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) the end time of each trial | shape = (259,) | dtype = float64
  Dataset /intervals/trials/timeseries (TimeSeriesReferenceVectorData) A group of timeseries | shape = (2701,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/trials/timeseries_index (VectorIndex) Index into Timeseries VectorData | shape = (259,) | dtype = uint64
  session_description: Animal `BAYLORNL23` on Session `20190301`
  session_start_time: 2019-03-01T11:43:01.000000-06:00
  Group /stimulus/presentation/aom_input_trace (TimeSeries) voltage input to AOM
  Group /stimulus/presentation/laser_power (OptogeneticSeries) laser power delivered to tissue (mW)
  Group /stimulus/presentation/laser_power/site (OptogeneticStimulusSite) 
  Group /stimulus/presentation/laser_power/site/device (Device) 
  timestamps_reference_time: 2019-03-01T11:43:01.000000-06:00
  Group /units (Units) Analysed Spike Events
  Dataset /units/id (ElementIdentifiers)  | shape = (17,) | dtype = int64
  Dataset /units/spike_times (VectorData) timestamps of spikes | shape = (598730,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) index into timestamps of spikes | shape = (17,) | dtype = uint64
  Dataset /units/trials (VectorData) A large group of trial IDs for each unit | shape = (598730,) | dtype = float64
  Dataset /units/trials_index (VectorIndex) Index into Trials vector data | shape = (17,) | dtype = uint64


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  Group /analysis/unit1SS (SpikeEventSeries) single unit1SS with cell type information and approximate depth
  Dataset /analysis/unit1SS/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (51972,) | dtype = int64
  Group /analysis/unit2SS (SpikeEventSeries) single unit2SS with cell type information and approximate depth
  Dataset /analysis/unit2SS/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (89527,) | dtype = int64
  Group /analysis/unit3SS (SpikeEventSeries) single unit3SS with cell type information and approximate depth
  Dataset /analysis/unit3SS/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (12276,) | dtype = int64
  Group /analysis/unit4SS (SpikeEventSeries) single unit4SS with cell type information and approximate depth
  Dataset /analysis/unit4SS/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (3664,) | dtype = int64
  Group /analysis/unit5SS (SpikeEventSeries) single unit5SS with cell type information and approximate depth
  Dataset /analysis/unit5SS/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (314601,) | dtype = int64
  Group /analysis/unit6SS (SpikeEventSeries) single unit6SS with cell type information and approximate depth
  Dataset /analysis/unit6SS/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (54464,) | dtype = int64
  Group /analysis/unit7SS (SpikeEventSeries) single unit7SS with cell type information and approximate depth
  Dataset /analysis/unit7SS/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (34836,) | dtype = int64
  Group /analysis/unit8CS (SpikeEventSeries) single unit8CS with cell type information and approximate depth
  Dataset /analysis/unit8CS/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (5338,) | dtype = int64
  Group /analysis/unit8SS (SpikeEventSeries) single unit8SS with cell type information and approximate depth
  Dataset /analysis/unit8SS/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (396487,) | dtype = int64
  Group /analysis/unit9SS (SpikeEventSeries) single unit9SS with cell type information and approximate depth
  Dataset /analysis/unit9SS/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (9128,) | dtype = int64
  file_create_date: ['2023-08-03T16:10:24.467549-05:00']
  data_collection: extracellularDataType: sorted spike times, spike waveform snipets, spike band voltage traces
  cellType: Identified PC, others
  identificationMethod: SS and CS spike waveforms and cross-correlogram, spike waveforms
  amplifierRolloff: 
  spikeSorting: manual:matclust
  ADunit: 14 bits
  Group /general/devices/Cambridge NeuroTech 64ch H2 probe 2x32 shank1:ch1-32 shank2:ch33-64 (Cambridge NeuroTech) (Device) 
  Group /general/devices/laser-473nm (Utralaser) (Device) 
  experiment_description: experimentType: behavior, extracellular, photostim
  referenceAtlas: Allen Reference Atlas
  task_keyword: detection, discrimination, lick Left lick Right, delay, somatosensory, motor, response, reward
  experimenter: ['Zhu, Jia']
  Group /general/extracellular_ephys/Cambridge NeuroTech 64ch H2 probe 2x32 shank1:ch1-32 shank2:ch33-64 (Cambridge NeuroTech) (ElectrodeGroup) recordingCoordinates: -2.5             -3           1100
  recordingMarker: stereotaxic coordinate from lambda
  recordingType: acute
  penetrationN: 5
  groundCoordinates: [1 -1  1]
  referenceCoordinates: []
  Group /general/extracellular_ephys/Cambridge NeuroTech 64ch H2 probe 2x32 shank1:ch1-32 shank2:ch33-64 (Cambridge NeuroTech)/device (Device) 
  Group /general/extracellular_ephys/electrodes (DynamicTable) Electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (50,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (50,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (50,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (50,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (50,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (50,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (50,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (50,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (50,) | dtype = float64
  institution: Baylor College of Medicine, Houston, TX 77030
  keywords: ['Motor planning' 'Cerebellar cortex' 'Short-term memory']
  lab: Nuo Li
  Group /general/optogenetics/photostim (OptogeneticStimulusSite) 
  Group /general/optogenetics/photostim/device (Device) 
  protocol: IACUC
  related_publications: ['Jia Zhu, Hana Hasanbegović, Liu D. Liu, Zhenyu Gao,  Nuo LiActivity map of a cortico-cerebellar loop underlying motor planning2023, Nature Neuroscience']
  session_id: 20190318
  source_script: batch_convertTrials4jia
  stimulus: photostim
  Group /general/subject (Subject) 
  surgery: Mice were prepared for photoinhibition and electrophysiology with a clear-skull cap and a headpost. The scalp and periosteum over the dorsal surface of the skull were removed. A layer of cyanoacrylate adhesive (Krazy glue, Elmer's Products Inc.) was directly applied to the intact skull. A custom made headpost was placed on the skull with its posterior edge aligned with the suture lambda and cemented in place with clear dental acrylic (Lang Dental Jet Repair Acrylic; 1223-clear). A thin layer of clear dental acrylic was applied over the cyanoacrylate adhesive covering the entire exposed skull, followed by a thin layer of clear nail polish (Electron Microscopy Sciences, 72180).
  identifier: BAYLORNL23_20190318
  Group /intervals/trials (TimeIntervals) trial data and properties
  Dataset /intervals/trials/CueTime (VectorData) Start of Response period (in seconds, relative to trial start time) | shape = (290, 2) | dtype = float64
  Dataset /intervals/trials/ErrL (VectorData) ErrL | shape = (290,) | dtype = bool
  Dataset /intervals/trials/ErrR (VectorData) ErrR | shape = (290,) | dtype = bool
  Dataset /intervals/trials/GoodTrials (VectorData) 0 for trials in which mice are not performing, discard for analyses | shape = (290,) | dtype = bool
  Dataset /intervals/trials/HitL (VectorData) HitL | shape = (290,) | dtype = bool
  Dataset /intervals/trials/HitR (VectorData) HitR | shape = (290,) | dtype = bool
  Dataset /intervals/trials/LickEarly (VectorData) LickEarly | shape = (290,) | dtype = bool
  Dataset /intervals/trials/NoLickL (VectorData) NoLickL | shape = (290,) | dtype = bool
  Dataset /intervals/trials/NoLickR (VectorData) NoLickR | shape = (290,) | dtype = bool
  Dataset /intervals/trials/PhotostimulationType (VectorData) "0"--non-stimulation trials;
  "1"--photoinhibition of left ALM; One light spot (diameter 1 mm); Early Delay (start from the onset of delay epoch); 800ms (200ms ramp);
  "2"--photoinhibition of right ALM; One light spot (diameter 1 mm); Early Delay (start from the onset of delay epoch); 800ms (200ms ramp);
  "3"--photoinhibition of both left and right ALM; Four light spots for each side; Early Delay (start from the onset of delay epoch); 800ms (200ms ramp);
  "NaN and others"--discard (stimulation configuration for other purposes, should not analyze) | shape = (290,) | dtype = float64
  Dataset /intervals/trials/PoleInTime (VectorData) Start of Sample period (in seconds, relative to trial start time) | shape = (290,) | dtype = float64
  Dataset /intervals/trials/PoleOutTime (VectorData) Start of Delay period (in seconds, relative to trial start time) | shape = (290,) | dtype = float64
  Dataset /intervals/trials/StimTrials (VectorData) StimTrials | shape = (290,) | dtype = bool
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (290,) | dtype = int64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds. | shape = (290,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) the end time of each trial | shape = (290,) | dtype = float64
  Dataset /intervals/trials/timeseries (TimeSeriesReferenceVectorData) A group of timeseries | shape = (2638,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/trials/timeseries_index (VectorIndex) Index into Timeseries VectorData | shape = (290,) | dtype = uint64
  session_description: Animal `BAYLORNL23` on Session `20190318`
  session_start_time: 2019-03-18T10:24:46.000000-05:00
  Group /stimulus/presentation/aom_input_trace (TimeSeries) voltage input to AOM
  Group /stimulus/presentation/laser_power (OptogeneticSeries) laser power delivered to tissue (mW)
  Group /stimulus/presentation/laser_power/site (OptogeneticStimulusSite) 
  Group /stimulus/presentation/laser_power/site/device (Device) 
  timestamps_reference_time: 2019-03-18T10:24:46.000000-05:00
  Group /units (Units) Analysed Spike Events
  Dataset /units/id (ElementIdentifiers)  | shape = (10,) | dtype = int64
  Dataset /units/spike_times (VectorData) timestamps of spikes | shape = (972293,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) index into timestamps of spikes | shape = (10,) | dtype = uint64
  Dataset /units/trials (VectorData) A large group of trial IDs for each unit | shape = (972293,) | dtype = float64
  Dataset /units/trials_index (VectorIndex) Index into Trials vector data | shape = (10,) | dtype = uint64
