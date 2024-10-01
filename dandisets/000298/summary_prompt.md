
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000298/draft
name: Brain_stim_and_FSCV_and_ensemble_recording_anesthetized
contributor: [{'name': 'Cowen, Stephen', 'email': 'scowen@email.arizona.edu', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}]
description: Determine how variability in the inter-pulse timing of electrical brain stimulation affects dopamine release and single-unit activity in the nucleus accumbens.
Working through the process of using NWB and Dandi so initial uploads will be buggy.

Data from grant 1 R01 NS 123424-01
assetsSummary: {'schemaKey': 'AssetsSummary', 'numberOfBytes': 0, 'numberOfFiles': 0}

Dandiset 000298 has 1 NWB files.
1 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/TimeSeries_FSCV (TimeSeries) no description
  Group /acquisition/TimeSeries_LFP (TimeSeries) no description
  Group /acquisition/series1 (TimeSeries) no description
  Group /acquisition/series2 (TimeSeries) no description
  file_create_date: ['2024-06-07T20:28:43.644526-07:00']
  Group /general/devices/FSCV probe (Device) Carbon probe for measuring FSCV
  Group /general/devices/LFP probe (Device) LFP
  Group /general/devices/Neuropixels probe (Device) Neuropixels
  experiment_description: Determine if different forms of inter-stim-pulse variability alters the magnitude of dopamine release
  experimenter: ['Abhi Vishwanath' 'Andrea Hamilton']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering, including the filter name and frequency cutoffs | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the electrode, in ohms | shape = (1,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/label (VectorData) label of electrode | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the position (+x is posterior) | shape = (1,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the position (+y is inferior) | shape = (1,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the position (+z is right) | shape = (1,) | dtype = float64
  Group /general/extracellular_ephys/shank0 (ElectrodeGroup) FSCV probe 0
  Group /general/extracellular_ephys/shank0/device (Device) Carbon probe for measuring FSCV
  institution: University of Arizona
  lab: Cowen/Heien Laboratories
  notes: animal did not go under anesthesia for about 30 min. Weak FSCV evoked release. We had about 10 neurons.
  session_id: 220408_MFB_NAc
  stimulus: Stimulation trains delivered at 300uA to the MFB
  Group /general/subject (Subject) 
  identifier: 220408_MFB_NAc
  Group /intervals/sleep_stages (TimeIntervals) intervals for each sleep stage as determined by EEG
  Dataset /intervals/sleep_stages/confidence (VectorData) confidence in stage (0-1) | shape = (3,) | dtype = float64
  Dataset /intervals/sleep_stages/id (ElementIdentifiers)  | shape = (3,) | dtype = int32
  Dataset /intervals/sleep_stages/stage (VectorData) stage of sleep | shape = (3,) | dtype = int32
  Dataset /intervals/sleep_stages/start_time (VectorData) Start time of epoch, in seconds | shape = (3,) | dtype = float64
  Dataset /intervals/sleep_stages/stop_time (VectorData) Stop time of epoch, in seconds | shape = (3,) | dtype = float64
  session_description: FSCV and single unit anesthetized with MFB stim all LV value
  session_start_time: 2022-04-08T00:00:00-07:00
  timestamps_reference_time: 2022-04-08T00:00:00-07:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/id (ElementIdentifiers)  | shape = (10,) | dtype = int32
  Dataset /units/quality (VectorData) sorting quality | shape = (10,) | dtype = object
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (231,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (10,) | dtype = uint8
  Dataset /units/waveform_mean (VectorData) the spike waveform mean for each spike unit | shape = (10, 5) | dtype = float64
