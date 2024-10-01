
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000960/draft
name: Test
contributor: [{'name': 'Zhuang, James', 'email': 'haider-lab@bme.gatech.edu', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}]
description: Testing dataset
assetsSummary: {'schemaKey': 'AssetsSummary', 'numberOfBytes': 0, 'numberOfFiles': 0}

Dandiset 000960 has 1 NWB files.
1 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2024-04-12T17:26:48.621000-04:00' '2024-04-12T17:26:48.827000-04:00'
   '2024-04-12T17:26:49.604000-04:00' '2024-04-12T17:26:50.095000-04:00'
   '2024-04-12T17:26:50.668000-04:00']
  Group /general/devices/Serial Number:  06101 (Device) Neuropixels 1.0 Phase 3B probes
  experimenter: ['James Zhuang']
  Group /general/extracellular_ephys/electrodes (DynamicTable) all electrodes
  Dataset /general/extracellular_ephys/electrodes/electrode_group (VectorData) my description | shape = (383,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) my description | shape = (383,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (383,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) my description | shape = (383,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) my description | shape = (383,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) my description | shape = (383,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) my description | shape = (383,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) my description | shape = (383,) | dtype = float64
  Group /general/extracellular_ephys/group_name (ElectrodeGroup) Electrode group for Probe 1
  Group /general/extracellular_ephys/group_name/device (Device) Neuropixels 1.0 Phase 3B probes
  institution: GATech
  protocol: A100171
  Group /general/subject (Subject) 
  identifier: M231117_1
  Group /intervals/trials (TimeIntervals) Visual stimulus information and timing; 1 grating per trial, but multiple bars per trial so trial & grating are NaN padded to match Probe data dimension
  Dataset /intervals/trials/gratingAzimuth (VectorData) 0 degrees is defined as the center of the binocular monitor,trials with less than 45 degrees means grating appears on binocular monitor, and trials with greater than 45 degrees means is grating appears on binocular monitor | shape = (1183,) | dtype = float64
  Dataset /intervals/trials/gratingContrast (VectorData) Contrast of the grating which ranges from 0 to 1 | shape = (1183,) | dtype = float64
  Dataset /intervals/trials/gratingTargetPhase (VectorData) Phase of the grating is randomized | shape = (1183,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (1183,) | dtype = int64
  Dataset /intervals/trials/probeAzimuth (VectorData) 0 degrees is defined as the center of the binocular monitor,trials with less than 45 degrees means grating appears on binocular monitor, and trials with greater than 45 degrees means is grating appears on binocular monitor | shape = (1183,) | dtype = float64
  Dataset /intervals/trials/probeColor (VectorData) binary; 1 means a flashing black bar, 2 means a flashing white bar | shape = (1183,) | dtype = float64
  Dataset /intervals/trials/probeEndedTime (VectorData) End time was start time 100 ms | shape = (1183,) | dtype = float64
  Dataset /intervals/trials/probeStartedTime (VectorData) Task irrelevant stimuli to probe for attention: 5% contrast flashing black and white bars that occurs for 100ms with an ITI of 300ms | shape = (1183,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start times of grating stimulus, in seconds relative to the start of the recording to sync up with spikeTimes | shape = (1183,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) End time of grating stimulus, in seconds relative to the start of the recording to sync up with spikeTimes | shape = (1183,) | dtype = float64
  Group /processing/ecephys (ProcessingModule) extracellular electrophysiology
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/ElectricalSeries (ElectricalSeries) no description
  Dataset /processing/ecephys/LFP/ElectricalSeries/electrodes (DynamicTableRegion) all electrodes | shape = (383,) | dtype = int64
  Group /processing/motionEnergy (ProcessingModule) contains motion energy data
  Group /processing/motionEnergy/motionEnergy (Position) 
  Group /processing/motionEnergy/motionEnergy/SpatialSeries (SpatialSeries) Tracking of orofacial movements (ME) during behavior at 30 FPS
  Group /processing/pupilArea (ProcessingModule) contains pupil and motion energy data
  Group /processing/pupilArea/pupilArea (Position) 
  Group /processing/pupilArea/pupilArea/SpatialSeries (SpatialSeries) Tracking of pupil area (area) during behavior at 30 FPS
  session_description: Mouse V1 ephys recording & visual spatial detection
  session_start_time: ['2023-12-31T14:55:42.621000-05:00']
  timestamps_reference_time: ['2023-12-31T14:55:42.621000-05:00']
  Group /units (Units) units table
  Dataset /units/AssignedChan (VectorData) Channel # on probe | shape = (34,) | dtype = float64
  Dataset /units/CellType (VectorData) .4ms TPP cutoff for RS vs FS | shape = (34,) | dtype = object
  Dataset /units/ClusterClass (VectorData) SU or MU | shape = (34,) | dtype = object
  Dataset /units/ClusterNum (VectorData) unit # assigned during spike sorting | shape = (34,) | dtype = float64
  Dataset /units/ClusterRecLoc (VectorData) Location of recorded cluster | shape = (34,) | dtype = object
  Dataset /units/Layer (VectorData) Assigned cortical layer for each neuron | shape = (34,) | dtype = object
  Dataset /units/id (ElementIdentifiers)  | shape = (34,) | dtype = int64
  Dataset /units/mean_waveform (VectorData) 3ms duration mean waveform across all channels in uV | shape = (34, 82) | dtype = float64
  Dataset /units/spike_times (VectorData) no description | shape = (691956,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) indexes data | shape = (34,) | dtype = uint64
