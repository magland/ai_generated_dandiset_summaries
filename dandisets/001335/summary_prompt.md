
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001335/draft
name: Neuropixels Recordings from Hippocampus of head-fixed mice during odor presentation
contributor: [{'name': 'Mohapatra, Manish', 'email': 'manishofyore@gmail.com', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Halchenko, Yaroslav', 'email': 'debian@onerussian.com', 'roleName': ['dcite:Software', 'dcite:Validation'], 'schemaKey': 'Person', 'includeInCitation': True}]
description: Head-fixed wild type mice were presented with various odor sequences, as neural activity was recorded from hippocampus using Neuropixels probes.
assetsSummary: {'schemaKey': 'AssetsSummary', 'numberOfBytes': 0, 'numberOfFiles': 0}

Dandiset 001335 has 1 NWB files.
1 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2025-02-14T10:53:25.648683-05:00']
  Group /general/devices/imec0 (Device) 4-shank NPX2.0 
  Group /general/devices/imec1 (Device) 4-shank NPX2.0 
  experiment_description: Head-fixed mouse presented with odor sequences
  experimenter: ['Mohapatra, Manish']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/depth (VectorData) Location of the electrode on the probe | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/hemisphere (VectorData) Location of the electrode on the probe | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (64,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/label (VectorData) Identifier for the channel on the probe | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (64,) | dtype = object
  Group /general/extracellular_ephys/imec0.shank0 (ElectrodeGroup) electrode group for shank 0 on imec0
  Group /general/extracellular_ephys/imec0.shank0/device (Device) 4-shank NPX2.0 
  Group /general/extracellular_ephys/imec0.shank1 (ElectrodeGroup) electrode group for shank 1 on imec0
  Group /general/extracellular_ephys/imec0.shank1/device (Device) 4-shank NPX2.0 
  Group /general/extracellular_ephys/imec0.shank2 (ElectrodeGroup) electrode group for shank 2 on imec0
  Group /general/extracellular_ephys/imec0.shank2/device (Device) 4-shank NPX2.0 
  Group /general/extracellular_ephys/imec0.shank3 (ElectrodeGroup) electrode group for shank 3 on imec0
  Group /general/extracellular_ephys/imec0.shank3/device (Device) 4-shank NPX2.0 
  Group /general/extracellular_ephys/imec1.shank0 (ElectrodeGroup) electrode group for shank 0 on imec1
  Group /general/extracellular_ephys/imec1.shank0/device (Device) 4-shank NPX2.0 
  Group /general/extracellular_ephys/imec1.shank1 (ElectrodeGroup) electrode group for shank 1 on imec1
  Group /general/extracellular_ephys/imec1.shank1/device (Device) 4-shank NPX2.0 
  Group /general/extracellular_ephys/imec1.shank2 (ElectrodeGroup) electrode group for shank 2 on imec1
  Group /general/extracellular_ephys/imec1.shank2/device (Device) 4-shank NPX2.0 
  Group /general/extracellular_ephys/imec1.shank3 (ElectrodeGroup) electrode group for shank 3 on imec1
  Group /general/extracellular_ephys/imec1.shank3/device (Device) 4-shank NPX2.0 
  institution: Dartmouth College
  keywords: ['ecephys' 'neuropixels' 'odor-sequences' 'hippocampus']
  lab: vandermeerlab
  Group /general/subject (Subject) 
  identifier: M541-2024-08-31
  Group /intervals/Block 1 (TimeIntervals) Interval when Block 1 odors were being presented
  Dataset /intervals/Block 1/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /intervals/Block 1/start_time (VectorData) Start time of epoch, in seconds | shape = (1,) | dtype = float64
  Dataset /intervals/Block 1/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1,) | dtype = float64
  Group /intervals/Block 2 (TimeIntervals) Interval when Block 2 odors were being presented
  Dataset /intervals/Block 2/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /intervals/Block 2/start_time (VectorData) Start time of epoch, in seconds | shape = (1,) | dtype = float64
  Dataset /intervals/Block 2/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1,) | dtype = float64
  Group /intervals/Block 3 (TimeIntervals) Interval when Block 3 odors were being presented
  Dataset /intervals/Block 3/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /intervals/Block 3/start_time (VectorData) Start time of epoch, in seconds | shape = (1,) | dtype = float64
  Dataset /intervals/Block 3/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1,) | dtype = float64
  Group /intervals/Odor A ON (TimeIntervals) Intervals when Odor A was being presented
  Dataset /intervals/Odor A ON/id (ElementIdentifiers)  | shape = (101,) | dtype = int64
  Dataset /intervals/Odor A ON/start_time (VectorData) Start time of epoch, in seconds | shape = (101,) | dtype = float64
  Dataset /intervals/Odor A ON/stop_time (VectorData) Stop time of epoch, in seconds | shape = (101,) | dtype = float64
  Group /intervals/Odor B ON (TimeIntervals) Intervals when Odor B was being presented
  Dataset /intervals/Odor B ON/id (ElementIdentifiers)  | shape = (101,) | dtype = int64
  Dataset /intervals/Odor B ON/start_time (VectorData) Start time of epoch, in seconds | shape = (101,) | dtype = float64
  Dataset /intervals/Odor B ON/stop_time (VectorData) Stop time of epoch, in seconds | shape = (101,) | dtype = float64
  Group /intervals/Odor C ON (TimeIntervals) Intervals when Odor C was being presented
  Dataset /intervals/Odor C ON/id (ElementIdentifiers)  | shape = (101,) | dtype = int64
  Dataset /intervals/Odor C ON/start_time (VectorData) Start time of epoch, in seconds | shape = (101,) | dtype = float64
  Dataset /intervals/Odor C ON/stop_time (VectorData) Stop time of epoch, in seconds | shape = (101,) | dtype = float64
  Group /intervals/Odor D ON (TimeIntervals) Intervals when Odor D was being presented
  Dataset /intervals/Odor D ON/id (ElementIdentifiers)  | shape = (101,) | dtype = int64
  Dataset /intervals/Odor D ON/start_time (VectorData) Start time of epoch, in seconds | shape = (101,) | dtype = float64
  Dataset /intervals/Odor D ON/stop_time (VectorData) Stop time of epoch, in seconds | shape = (101,) | dtype = float64
  Group /intervals/Odor E ON (TimeIntervals) Intervals when Odor E was being presented
  Dataset /intervals/Odor E ON/id (ElementIdentifiers)  | shape = (101,) | dtype = int64
  Dataset /intervals/Odor E ON/start_time (VectorData) Start time of epoch, in seconds | shape = (101,) | dtype = float64
  Dataset /intervals/Odor E ON/stop_time (VectorData) Stop time of epoch, in seconds | shape = (101,) | dtype = float64
  Group /intervals/Odor F ON (TimeIntervals) Intervals when Odor F was being presented
  Dataset /intervals/Odor F ON/id (ElementIdentifiers)  | shape = (101,) | dtype = int64
  Dataset /intervals/Odor F ON/start_time (VectorData) Start time of epoch, in seconds | shape = (101,) | dtype = float64
  Dataset /intervals/Odor F ON/stop_time (VectorData) Stop time of epoch, in seconds | shape = (101,) | dtype = float64
  Group /processing/ecephys (ProcessingModule) LFP data obtained from rawdata
  Group /processing/ecephys/LFP (ElectricalSeries) Raw data subsampled  2500 Hz and bandpass filtered in the range 1-400 Hz
  Dataset /processing/ecephys/LFP/electrodes (DynamicTableRegion) LFP electrodes | shape = (64,) | dtype = int64
  session_description: Block 1:UE (ABC), Block 2:SE (DEF), Block3:Localizer
  session_start_time: 2025-02-14T10:53:25.647928-05:00
  timestamps_reference_time: 2025-02-14T10:53:25.647928-05:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/depth (VectorData) Depth of the unit from the surface of the brain | shape = (283,) | dtype = float64
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (283,) | dtype = object
  Dataset /units/global_id (VectorData) ID to uniquely identify the unit | shape = (283,) | dtype = object
  Dataset /units/hemisphere (VectorData) Hemisphere of the brain where the unit was recorded | shape = (283,) | dtype = object
  Dataset /units/id (ElementIdentifiers)  | shape = (283,) | dtype = int64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (5260124,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (283,) | dtype = uint32
  Dataset /units/waveform_mean (VectorData) the spike waveform mean for each spike unit | shape = (283, 90) | dtype = float32
