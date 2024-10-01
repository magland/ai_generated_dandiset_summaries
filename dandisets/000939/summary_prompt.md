
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000939/0.240528.1542
name: Large-scale recordings of head-direction cells in mouse postsubiculum
contributor: [{'name': 'Duszkiewicz, Adrian', 'email': 'a.j.duszkiewicz@gmail.com', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Skromne Carrasco, Sofia', 'email': 'sofia.skromnecarrasco@mail.mcgill.ca', 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Peyrache, Adrien', 'email': 'adrien.peyrache@mcgill.ca', 'roleName': [], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Wellcome Trust', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/029chgv08', 'includeInCitation': False}, {'name': 'McGill University', 'roleName': [], 'schemaKey': 'Organization', 'includeInCitation': False}, {'name': 'University of Edinburgh', 'schemaKey': 'Organization', 'includeInCitation': False}]
description: 64-channel linear probe recordings from mouse postsubiculum (dorsal presubiculum) - a region in which most excitatory cells are narrowly tuned to the animal's head-direction.  Dataset includes one recording session per mouse (N = 31 mice, 42 - 185 units per recording). All sessions include a square open field exploration epoch and two sleep epochs. Some sessions additionally include a triangular open field epoch or an optogenetic stimulation epoch. 

Each NWB file contains: timestamps of detected units, mean waveforms, LFP,  animal position and head-direction,  sleep scoring (REM/NREM), accelerometer data. 

Metadata: https://docs.google.com/spreadsheets/d/1eGVMXkzyo25IOJHTyiNYFGhNO_7H4ZscUFfCBi31fYU/edit?usp=sharing

Data used in Duszkiewicz et al, 2024 (DOI: 10.1038/s41593-024-01588-5). Collected by Adrian J. Duszkiewicz and Sofia Skromne Carrasco in Peyrache lab. Additional adjustment of motion tracking data by Miao Wang, Sirota lab. 

Original version of the dataset used in the article (including ADN recordings) and code to reproduce figures can be found in Matlab format at:
https://doi.org/10.6084/m9.figshare.24921252

assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'behavioral approach', 'schemaKey': 'ApproachType'}, {'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}, {'name': 'optogenetic approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 54772596116, 'numberOfFiles': 31, 'numberOfSubjects': 31, 'variableMeasured': ['CompassDirection', 'ProcessingModule', 'SpatialSeries', 'ElectricalSeries', 'Position', 'LFP', 'OptogeneticSeries', 'Units', 'ElectrodeGroup'], 'measurementTechnique': [{'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'signal filtering technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000939 has 31 NWB files.
5 of these NWB files are of type 1.
20 of these NWB files are of type 2.
1 of these NWB files are of type 3.
1 of these NWB files are of type 4.
4 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2024-05-27T19:20:00.054703+01:00']
  Group /general/devices/Cambridge Neurotech H5 probe (Device) 64-channel linear array, 12.5 um channel spacing, implanted vertically, across cortical layers. Channels sorted top to bottom of shank.
  Group /general/devices/Mono fiberoptic cannula (Device) MFC_200/240-0.22 implanted bilaterally above ADN in the anterior thalamus
  experiment_description: high-density recordings in mouse postsubiculum during exploration and sleep
  experimenter: ['Duszkiewicz, Adrian J.']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering, including the filter name and frequency cutoffs | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (64,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/is_faulty (VectorData) Boolean column to indicate faulty electrodes | shape = (64,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/label (VectorData) label of electrode | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the position (+x is posterior) | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the position (+y is inferior) | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the position (+z is right) | shape = (64,) | dtype = float64
  Group /general/extracellular_ephys/shank0 (ElectrodeGroup) electrode group for shank0
  Group /general/extracellular_ephys/shank0/device (Device) 64-channel linear array, 12.5 um channel spacing, implanted vertically, across cortical layers. Channels sorted top to bottom of shank.
  institution: McGill University
  keywords: ['head-direction' 'postsubiculum' 'extracellular' 'freely-moving'
   'electrophysiology']
  lab: Peyrache Lab
  Group /general/optogenetics/ADN (OptogeneticStimulusSite) 
  Group /general/optogenetics/ADN/device (Device) MFC_200/240-0.22 implanted bilaterally above ADN in the anterior thalamus
  related_publications: ['doi: 10.1038/s41593-024-01588-5']
  session_id: 190807
  Group /general/subject (Subject) 
  virus: Bilateral AAV9-emCBA-Flex-GFP virus injection into thalamic reticular nucleus (400 ul/side)
  identifier: A1808
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (4,) | dtype = int64
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (4,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (4,) | dtype = float64
  Dataset /intervals/epochs/tags (VectorData) user-defined tags | shape = (4,) | dtype = object
  Dataset /intervals/epochs/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (4,) | dtype = uint8
  Group /intervals/nrem (TimeIntervals) experimental intervals
  Dataset /intervals/nrem/id (ElementIdentifiers)  | shape = (67,) | dtype = int64
  Dataset /intervals/nrem/start_time (VectorData) Start time of epoch, in seconds | shape = (67,) | dtype = float32
  Dataset /intervals/nrem/stop_time (VectorData) Stop time of epoch, in seconds | shape = (67,) | dtype = float32
  Dataset /intervals/nrem/tags (VectorData) user-defined tags | shape = (124,) | dtype = object
  Dataset /intervals/nrem/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (67,) | dtype = uint8
  Group /intervals/rem (TimeIntervals) experimental intervals
  Dataset /intervals/rem/id (ElementIdentifiers)  | shape = (2,) | dtype = int64
  Dataset /intervals/rem/start_time (VectorData) Start time of epoch, in seconds | shape = (2,) | dtype = float32
  Dataset /intervals/rem/stop_time (VectorData) Stop time of epoch, in seconds | shape = (2,) | dtype = float32
  Dataset /intervals/rem/tags (VectorData) user-defined tags | shape = (2,) | dtype = object
  Dataset /intervals/rem/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (2,) | dtype = uint8
  Group /processing/behavior (ProcessingModule) Tracking data acquired by Optitrack Motive 2.0
  Group /processing/behavior/CompassDirection (CompassDirection) 
  Group /processing/behavior/CompassDirection/head-direction (SpatialSeries) Horizontal angle of the head (yaw)
  Group /processing/behavior/Position (Position) 
  Group /processing/behavior/Position/position (SpatialSeries) (x,y) position in the open field
  Group /processing/behavior/accelerometer (TimeSeries) Accelerometer data from the Intan RHD headstage
  Group /processing/ecephys (ProcessingModule) Processed electrophysiological signals
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/LFP (ElectricalSeries) Local field potential (low-pass filtered at 625 Hz)
  Dataset /processing/ecephys/LFP/LFP/electrodes (DynamicTableRegion) all electrodes | shape = (64,) | dtype = int64
  Group /processing/ecephys/pseudoEMG (TimeSeries) Pseudo EMG from correlated high-frequency LFP
  Group /processing/ogen (ProcessingModule) Optogenetic stimulation data
  Group /processing/ogen/optogenetic_stim (OptogeneticSeries) optogenetic stimulation
  Group /processing/ogen/optogenetic_stim/site (OptogeneticStimulusSite) 
  Group /processing/ogen/optogenetic_stim/site/device (Device) MFC_200/240-0.22 implanted bilaterally above ADN in the anterior thalamus
  session_description: Open field and sleep recording
  session_start_time: 2019-08-07T00:00:00-04:00
  timestamps_reference_time: 2019-08-07T00:00:00-04:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (101,) | dtype = object
  Dataset /units/electrode_index (VectorData) electrode with the highest waveform amplitude | shape = (101,) | dtype = int64
  Dataset /units/id (ElementIdentifiers)  | shape = (101,) | dtype = int64
  Dataset /units/is_excitatory (VectorData) Putative excitatory cells | shape = (101,) | dtype = uint8
  Dataset /units/is_fast_spiking (VectorData) Putative fast-spiking interneurons | shape = (101,) | dtype = uint8
  Dataset /units/is_head_direction (VectorData) Head-direction tuned units | shape = (101,) | dtype = uint8
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (5649530,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (101,) | dtype = uint32
  Dataset /units/trough_to_peak (VectorData) Trough-to-peak duration of waveform (ms) | shape = (101,) | dtype = float64
  Dataset /units/waveform_mean (VectorData) the spike waveform mean for each spike unit | shape = (101, 40, 64) | dtype = float64


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2024-05-27T19:40:49.131542+01:00']
  Group /general/devices/Cambridge Neurotech H5 probe (Device) 64-channel linear array, 12.5 um channel spacing, implanted at 20deg angle, approximately parallel to cortical layers. Channels sorted top to bottom of shank. 
  experiment_description: high-density recordings in mouse postsubiculum during exploration and sleep
  experimenter: ['Duszkiewicz, Adrian J.']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering, including the filter name and frequency cutoffs | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (64,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/is_faulty (VectorData) Boolean column to indicate faulty electrodes | shape = (64,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/label (VectorData) label of electrode | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the position (+x is posterior) | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the position (+y is inferior) | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the position (+z is right) | shape = (64,) | dtype = float64
  Group /general/extracellular_ephys/shank0 (ElectrodeGroup) electrode group for shank0
  Group /general/extracellular_ephys/shank0/device (Device) 64-channel linear array, 12.5 um channel spacing, implanted at 20deg angle, approximately parallel to cortical layers. Channels sorted top to bottom of shank. 
  institution: McGill University
  keywords: ['head-direction' 'postsubiculum' 'extracellular' 'freely-moving'
   'electrophysiology']
  lab: Peyrache Lab
  related_publications: ['doi: 10.1038/s41593-024-01588-5']
  session_id: 191119
  Group /general/subject (Subject) 
  virus: nan
  identifier: A3701
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (4,) | dtype = int64
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (4,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (4,) | dtype = float64
  Dataset /intervals/epochs/tags (VectorData) user-defined tags | shape = (4,) | dtype = object
  Dataset /intervals/epochs/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (4,) | dtype = uint8
  Group /intervals/nrem (TimeIntervals) experimental intervals
  Dataset /intervals/nrem/id (ElementIdentifiers)  | shape = (85,) | dtype = int64
  Dataset /intervals/nrem/start_time (VectorData) Start time of epoch, in seconds | shape = (85,) | dtype = float32
  Dataset /intervals/nrem/stop_time (VectorData) Stop time of epoch, in seconds | shape = (85,) | dtype = float32
  Dataset /intervals/nrem/tags (VectorData) user-defined tags | shape = (160,) | dtype = object
  Dataset /intervals/nrem/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (85,) | dtype = uint8
  Group /intervals/rem (TimeIntervals) experimental intervals
  Dataset /intervals/rem/id (ElementIdentifiers)  | shape = (7,) | dtype = int64
  Dataset /intervals/rem/start_time (VectorData) Start time of epoch, in seconds | shape = (7,) | dtype = float32
  Dataset /intervals/rem/stop_time (VectorData) Stop time of epoch, in seconds | shape = (7,) | dtype = float32
  Dataset /intervals/rem/tags (VectorData) user-defined tags | shape = (7,) | dtype = object
  Dataset /intervals/rem/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (7,) | dtype = uint8
  Group /processing/behavior (ProcessingModule) Tracking data acquired by Optitrack Motive 2.0
  Group /processing/behavior/CompassDirection (CompassDirection) 
  Group /processing/behavior/CompassDirection/head-direction (SpatialSeries) Horizontal angle of the head (yaw)
  Group /processing/behavior/Position (Position) 
  Group /processing/behavior/Position/position (SpatialSeries) (x,y) position in the open field
  Group /processing/behavior/accelerometer (TimeSeries) Accelerometer data from the Intan RHD headstage
  Group /processing/ecephys (ProcessingModule) Processed electrophysiological signals
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/LFP (ElectricalSeries) Local field potential (low-pass filtered at 625 Hz)
  Dataset /processing/ecephys/LFP/LFP/electrodes (DynamicTableRegion) all electrodes | shape = (64,) | dtype = int64
  Group /processing/ecephys/pseudoEMG (TimeSeries) Pseudo EMG from correlated high-frequency LFP
  session_description: Open field and sleep recording
  session_start_time: 2019-11-19T00:00:00-05:00
  timestamps_reference_time: 2019-11-19T00:00:00-05:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (102,) | dtype = object
  Dataset /units/electrode_index (VectorData) electrode with the highest waveform amplitude | shape = (102,) | dtype = int64
  Dataset /units/id (ElementIdentifiers)  | shape = (102,) | dtype = int64
  Dataset /units/is_excitatory (VectorData) Putative excitatory cells | shape = (102,) | dtype = uint8
  Dataset /units/is_fast_spiking (VectorData) Putative fast-spiking interneurons | shape = (102,) | dtype = uint8
  Dataset /units/is_head_direction (VectorData) Head-direction tuned units | shape = (102,) | dtype = uint8
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (6043225,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (102,) | dtype = uint32
  Dataset /units/trough_to_peak (VectorData) Trough-to-peak duration of waveform (ms) | shape = (102,) | dtype = float64
  Dataset /units/waveform_mean (VectorData) the spike waveform mean for each spike unit | shape = (102, 40, 64) | dtype = float64


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2024-05-27T20:44:26.764705+01:00']
  Group /general/devices/Cambridge Neurotech H5 probe (Device) 64-channel linear array, 12.5 um channel spacing, implanted at 20deg angle, approximately parallel to cortical layers. Channels sorted top to bottom of shank. 
  experiment_description: high-density recordings in mouse postsubiculum during exploration and sleep
  experimenter: ['Duszkiewicz, Adrian J.']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering, including the filter name and frequency cutoffs | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (64,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/is_faulty (VectorData) Boolean column to indicate faulty electrodes | shape = (64,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/label (VectorData) label of electrode | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the position (+x is posterior) | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the position (+y is inferior) | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the position (+z is right) | shape = (64,) | dtype = float64
  Group /general/extracellular_ephys/shank0 (ElectrodeGroup) electrode group for shank0
  Group /general/extracellular_ephys/shank0/device (Device) 64-channel linear array, 12.5 um channel spacing, implanted at 20deg angle, approximately parallel to cortical layers. Channels sorted top to bottom of shank. 
  institution: McGill University
  keywords: ['head-direction' 'postsubiculum' 'extracellular' 'freely-moving'
   'electrophysiology']
  lab: Peyrache Lab
  related_publications: ['doi: 10.1038/s41593-024-01588-5']
  session_id: 210309b
  Group /general/subject (Subject) 
  virus: nan
  identifier: A3728
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (4,) | dtype = int64
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (4,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (4,) | dtype = float64
  Dataset /intervals/epochs/tags (VectorData) user-defined tags | shape = (4,) | dtype = object
  Dataset /intervals/epochs/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (4,) | dtype = uint8
  Group /intervals/nrem (TimeIntervals) experimental intervals
  Dataset /intervals/nrem/id (ElementIdentifiers)  | shape = (5,) | dtype = int64
  Dataset /intervals/nrem/start_time (VectorData) Start time of epoch, in seconds | shape = (5,) | dtype = float32
  Dataset /intervals/nrem/stop_time (VectorData) Stop time of epoch, in seconds | shape = (5,) | dtype = float32
  Dataset /intervals/nrem/tags (VectorData) user-defined tags | shape = (5,) | dtype = object
  Dataset /intervals/nrem/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (5,) | dtype = uint8
  Group /processing/behavior (ProcessingModule) Tracking data acquired by Optitrack Motive 2.0
  Group /processing/behavior/CompassDirection (CompassDirection) 
  Group /processing/behavior/CompassDirection/head-direction (SpatialSeries) Horizontal angle of the head (yaw)
  Group /processing/behavior/Position (Position) 
  Group /processing/behavior/Position/position (SpatialSeries) (x,y) position in the open field
  Group /processing/ecephys (ProcessingModule) Processed electrophysiological signals
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/LFP (ElectricalSeries) Local field potential (low-pass filtered at 625 Hz)
  Dataset /processing/ecephys/LFP/LFP/electrodes (DynamicTableRegion) all electrodes | shape = (64,) | dtype = int64
  Group /processing/ecephys/pseudoEMG (TimeSeries) Pseudo EMG from correlated high-frequency LFP
  session_description: Open field and sleep recording
  session_start_time: 2021-03-09T00:00:00-05:00
  timestamps_reference_time: 2021-03-09T00:00:00-05:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (42,) | dtype = object
  Dataset /units/electrode_index (VectorData) electrode with the highest waveform amplitude | shape = (42,) | dtype = int64
  Dataset /units/id (ElementIdentifiers)  | shape = (42,) | dtype = int64
  Dataset /units/is_excitatory (VectorData) Putative excitatory cells | shape = (42,) | dtype = uint8
  Dataset /units/is_fast_spiking (VectorData) Putative fast-spiking interneurons | shape = (42,) | dtype = uint8
  Dataset /units/is_head_direction (VectorData) Head-direction tuned units | shape = (42,) | dtype = uint8
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (2408872,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (42,) | dtype = uint32
  Dataset /units/trough_to_peak (VectorData) Trough-to-peak duration of waveform (ms) | shape = (42,) | dtype = float64
  Dataset /units/waveform_mean (VectorData) the spike waveform mean for each spike unit | shape = (42, 40, 64) | dtype = float64


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2024-05-27T20:47:16.698403+01:00']
  Group /general/devices/Cambridge Neurotech H5 probe (Device) 64-channel linear array, 12.5 um channel spacing, implanted at 20deg angle, approximately parallel to cortical layers. Channels sorted top to bottom of shank. 
  experiment_description: high-density recordings in mouse postsubiculum during exploration and sleep
  experimenter: ['Duszkiewicz, Adrian J.']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering, including the filter name and frequency cutoffs | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (64,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/is_faulty (VectorData) Boolean column to indicate faulty electrodes | shape = (64,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/label (VectorData) label of electrode | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the position (+x is posterior) | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the position (+y is inferior) | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the position (+z is right) | shape = (64,) | dtype = float64
  Group /general/extracellular_ephys/shank0 (ElectrodeGroup) electrode group for shank0
  Group /general/extracellular_ephys/shank0/device (Device) 64-channel linear array, 12.5 um channel spacing, implanted at 20deg angle, approximately parallel to cortical layers. Channels sorted top to bottom of shank. 
  institution: McGill University
  keywords: ['head-direction' 'postsubiculum' 'extracellular' 'freely-moving'
   'electrophysiology']
  lab: Peyrache Lab
  related_publications: ['doi: 10.1038/s41593-024-01588-5']
  session_id: 210323b
  Group /general/subject (Subject) 
  virus: nan
  identifier: A3730
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (4,) | dtype = int64
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (4,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (4,) | dtype = float64
  Dataset /intervals/epochs/tags (VectorData) user-defined tags | shape = (4,) | dtype = object
  Dataset /intervals/epochs/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (4,) | dtype = uint8
  Group /intervals/nrem (TimeIntervals) experimental intervals
  Dataset /intervals/nrem/id (ElementIdentifiers)  | shape = (12,) | dtype = int64
  Dataset /intervals/nrem/start_time (VectorData) Start time of epoch, in seconds | shape = (12,) | dtype = float32
  Dataset /intervals/nrem/stop_time (VectorData) Stop time of epoch, in seconds | shape = (12,) | dtype = float32
  Dataset /intervals/nrem/tags (VectorData) user-defined tags | shape = (14,) | dtype = object
  Dataset /intervals/nrem/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (12,) | dtype = uint8
  Group /intervals/rem (TimeIntervals) experimental intervals
  Dataset /intervals/rem/id (ElementIdentifiers)  | shape = (3,) | dtype = int64
  Dataset /intervals/rem/start_time (VectorData) Start time of epoch, in seconds | shape = (3,) | dtype = float32
  Dataset /intervals/rem/stop_time (VectorData) Stop time of epoch, in seconds | shape = (3,) | dtype = float32
  Dataset /intervals/rem/tags (VectorData) user-defined tags | shape = (3,) | dtype = object
  Dataset /intervals/rem/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (3,) | dtype = uint8
  Group /processing/behavior (ProcessingModule) Tracking data acquired by Optitrack Motive 2.0
  Group /processing/behavior/CompassDirection (CompassDirection) 
  Group /processing/behavior/CompassDirection/head-direction (SpatialSeries) Horizontal angle of the head (yaw)
  Group /processing/behavior/Position (Position) 
  Group /processing/behavior/Position/position (SpatialSeries) (x,y) position in the open field
  Group /processing/ecephys (ProcessingModule) Processed electrophysiological signals
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/LFP (ElectricalSeries) Local field potential (low-pass filtered at 625 Hz)
  Dataset /processing/ecephys/LFP/LFP/electrodes (DynamicTableRegion) all electrodes | shape = (64,) | dtype = int64
  Group /processing/ecephys/pseudoEMG (TimeSeries) Pseudo EMG from correlated high-frequency LFP
  session_description: Open field and sleep recording
  session_start_time: 2021-03-23T00:00:00-04:00
  timestamps_reference_time: 2021-03-23T00:00:00-04:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (77,) | dtype = object
  Dataset /units/electrode_index (VectorData) electrode with the highest waveform amplitude | shape = (77,) | dtype = int64
  Dataset /units/id (ElementIdentifiers)  | shape = (77,) | dtype = int64
  Dataset /units/is_excitatory (VectorData) Putative excitatory cells | shape = (77,) | dtype = uint8
  Dataset /units/is_fast_spiking (VectorData) Putative fast-spiking interneurons | shape = (77,) | dtype = uint8
  Dataset /units/is_head_direction (VectorData) Head-direction tuned units | shape = (77,) | dtype = uint8
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (5473776,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (77,) | dtype = uint32
  Dataset /units/trough_to_peak (VectorData) Trough-to-peak duration of waveform (ms) | shape = (77,) | dtype = float64
  Dataset /units/waveform_mean (VectorData) the spike waveform mean for each spike unit | shape = (77, 40, 64) | dtype = float64


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2024-05-27T21:08:58.840559+01:00']
  Group /general/devices/Cambridge Neurotech H5 probe (Device) 64-channel linear array, 12.5 um channel spacing, implanted vertically, across cortical layers. Channels sorted top to bottom of shank.
  Group /general/devices/Mono fiberoptic cannula (Device) MFC_200/240-0.22 implanted unilaterally above left PoSub
  experiment_description: high-density recordings in mouse postsubiculum during exploration and sleep
  experimenter: ['Duszkiewicz, Adrian J.']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering, including the filter name and frequency cutoffs | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (64,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/is_faulty (VectorData) Boolean column to indicate faulty electrodes | shape = (64,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/label (VectorData) label of electrode | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the position (+x is posterior) | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the position (+y is inferior) | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the position (+z is right) | shape = (64,) | dtype = float64
  Group /general/extracellular_ephys/shank0 (ElectrodeGroup) electrode group for shank0
  Group /general/extracellular_ephys/shank0/device (Device) 64-channel linear array, 12.5 um channel spacing, implanted vertically, across cortical layers. Channels sorted top to bottom of shank.
  institution: McGill University
  keywords: ['head-direction' 'postsubiculum' 'extracellular' 'freely-moving'
   'electrophysiology']
  lab: Peyrache Lab
  Group /general/optogenetics/PoSub (OptogeneticStimulusSite) 
  Group /general/optogenetics/PoSub/device (Device) MFC_200/240-0.22 implanted unilaterally above left PoSub
  related_publications: ['doi: 10.1038/s41593-024-01588-5']
  session_id: 210407
  Group /general/subject (Subject) 
  virus: Unilateral AAV2/8-CAG-Flex-ArchT-eGFP virus injection into left PoSub (150 ul)
  identifier: A6211
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (4,) | dtype = int64
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (4,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (4,) | dtype = float64
  Dataset /intervals/epochs/tags (VectorData) user-defined tags | shape = (4,) | dtype = object
  Dataset /intervals/epochs/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (4,) | dtype = uint8
  Group /intervals/nrem (TimeIntervals) experimental intervals
  Dataset /intervals/nrem/id (ElementIdentifiers)  | shape = (20,) | dtype = int64
  Dataset /intervals/nrem/start_time (VectorData) Start time of epoch, in seconds | shape = (20,) | dtype = float32
  Dataset /intervals/nrem/stop_time (VectorData) Stop time of epoch, in seconds | shape = (20,) | dtype = float32
  Dataset /intervals/nrem/tags (VectorData) user-defined tags | shape = (30,) | dtype = object
  Dataset /intervals/nrem/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (20,) | dtype = uint8
  Group /intervals/rem (TimeIntervals) experimental intervals
  Dataset /intervals/rem/id (ElementIdentifiers)  | shape = (4,) | dtype = int64
  Dataset /intervals/rem/start_time (VectorData) Start time of epoch, in seconds | shape = (4,) | dtype = float32
  Dataset /intervals/rem/stop_time (VectorData) Stop time of epoch, in seconds | shape = (4,) | dtype = float32
  Dataset /intervals/rem/tags (VectorData) user-defined tags | shape = (4,) | dtype = object
  Dataset /intervals/rem/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (4,) | dtype = uint8
  Group /processing/behavior (ProcessingModule) Tracking data acquired by Optitrack Motive 2.0
  Group /processing/behavior/CompassDirection (CompassDirection) 
  Group /processing/behavior/CompassDirection/head-direction (SpatialSeries) Horizontal angle of the head (yaw)
  Group /processing/behavior/Position (Position) 
  Group /processing/behavior/Position/position (SpatialSeries) (x,y) position in the open field
  Group /processing/behavior/accelerometer (TimeSeries) Accelerometer data from the Intan RHD headstage
  Group /processing/ecephys (ProcessingModule) Processed electrophysiological signals
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/LFP (ElectricalSeries) Local field potential (low-pass filtered at 625 Hz)
  Dataset /processing/ecephys/LFP/LFP/electrodes (DynamicTableRegion) all electrodes | shape = (64,) | dtype = int64
  Group /processing/ecephys/pseudoEMG (TimeSeries) Pseudo EMG from correlated high-frequency LFP
  Group /processing/ogen (ProcessingModule) Optogenetic stimulation data
  Group /processing/ogen/optogenetic_stim (OptogeneticSeries) optogenetic stimulation
  Group /processing/ogen/optogenetic_stim/site (OptogeneticStimulusSite) 
  Group /processing/ogen/optogenetic_stim/site/device (Device) MFC_200/240-0.22 implanted unilaterally above left PoSub
  session_description: Open field and sleep recording
  session_start_time: 2021-04-07T00:00:00-04:00
  timestamps_reference_time: 2021-04-07T00:00:00-04:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (61,) | dtype = object
  Dataset /units/electrode_index (VectorData) electrode with the highest waveform amplitude | shape = (61,) | dtype = int64
  Dataset /units/id (ElementIdentifiers)  | shape = (61,) | dtype = int64
  Dataset /units/is_excitatory (VectorData) Putative excitatory cells | shape = (61,) | dtype = uint8
  Dataset /units/is_fast_spiking (VectorData) Putative fast-spiking interneurons | shape = (61,) | dtype = uint8
  Dataset /units/is_head_direction (VectorData) Head-direction tuned units | shape = (61,) | dtype = uint8
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (4658843,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (61,) | dtype = uint32
  Dataset /units/trough_to_peak (VectorData) Trough-to-peak duration of waveform (ms) | shape = (61,) | dtype = float64
  Dataset /units/waveform_mean (VectorData) the spike waveform mean for each spike unit | shape = (61, 40, 64) | dtype = float64
