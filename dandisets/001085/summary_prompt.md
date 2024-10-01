
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001085/draft
name: test
contributor: [{'name': 'Shelton, Andrew', 'email': 'andrew.shelton@alleninstitute.org', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}]
description: Dataset to test nwb file upload
assetsSummary: {'schemaKey': 'AssetsSummary', 'numberOfBytes': 0, 'numberOfFiles': 0}

Dandiset 001085 has 1 NWB files.
1 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2024-07-02T09:57:28.911695-07:00']
  Group /general/devices/Neuropixels Probe (Device) Extracellular electrophysiology probe
  experiment_description: Optotagging experiment in a VIP-Cre;Ai32 mouse. This is the first recording in this series on this day for this mouse.
  experimenter: ['Andrew Shelton']
  Group /general/extracellular_ephys/ProbeA Electrode Group (ElectrodeGroup) Electrode group for ProbeA
  Group /general/extracellular_ephys/ProbeA Electrode Group/device (Device) Extracellular electrophysiology probe
  Group /general/extracellular_ephys/ProbeC Electrode Group (ElectrodeGroup) Electrode group for ProbeC
  Group /general/extracellular_ephys/ProbeC Electrode Group/device (Device) Extracellular electrophysiology probe
  Group /general/extracellular_ephys/ProbeE Electrode Group (ElectrodeGroup) Electrode group for ProbeE
  Group /general/extracellular_ephys/ProbeE Electrode Group/device (Device) Extracellular electrophysiology probe
  Group /general/extracellular_ephys/ProbeF Electrode Group (ElectrodeGroup) Electrode group for ProbeF
  Group /general/extracellular_ephys/ProbeF Electrode Group/device (Device) Extracellular electrophysiology probe
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering, including the filter name and frequency cutoffs | shape = (1536,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (1536,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (1536,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (1536,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the electrode, in ohms | shape = (1536,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (1536,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the position (+x is posterior) | shape = (1536,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the position (+y is inferior) | shape = (1536,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the position (+z is right) | shape = (1536,) | dtype = float64
  institution: Allen Institute
  lab: Neural Dynamics
  protocol: 2104
  session_id: 2021-02-09_546513_1
  Group /general/subject (Subject) 
  identifier: 2021-02-09_546513_1
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (600,) | dtype = int32
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (600,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (600,) | dtype = float64
  Dataset /intervals/trials/trial_conditions (VectorData) Conditions of optogenetic stimulation | shape = (600,) | dtype = float64
  Dataset /intervals/trials/trial_levels (VectorData) Levels of optogenetic stimulation | shape = (600,) | dtype = float64
  Group /processing/10ms_pulse_psth (ProcessingModule) 10ms pulse PSTH per unit
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_0 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_1 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_10 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_11 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_12 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_13 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_14 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_15 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_16 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_17 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_18 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_19 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_2 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_20 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_21 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_22 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_23 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_24 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_25 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_26 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_27 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_28 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_29 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_3 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_30 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_31 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_32 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_33 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_34 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_35 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_36 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_37 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_38 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_39 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_4 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_40 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_41 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_42 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_43 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_44 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_45 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_46 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_47 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_48 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_49 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_5 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_50 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_51 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_52 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_53 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_54 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_55 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_56 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_57 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_58 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_59 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_6 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_60 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_61 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_62 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_63 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_7 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_8 (TimeSeries) no description
  Group /processing/10ms_pulse_psth/10ms_pulse_psth_9 (TimeSeries) no description
  Group /processing/1s_cosine_psth (ProcessingModule) 1s cosine PSTH per unit
  Group /processing/1s_cosine_psth/1s_cosine_psth_0 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_1 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_10 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_11 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_12 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_13 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_14 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_15 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_16 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_17 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_18 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_19 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_2 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_20 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_21 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_22 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_23 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_24 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_25 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_26 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_27 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_28 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_29 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_3 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_30 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_31 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_32 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_33 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_34 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_35 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_36 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_37 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_38 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_39 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_4 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_40 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_41 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_42 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_43 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_44 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_45 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_46 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_47 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_48 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_49 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_5 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_50 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_51 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_52 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_53 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_54 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_55 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_56 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_57 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_58 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_59 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_6 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_60 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_61 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_62 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_63 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_7 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_8 (TimeSeries) no description
  Group /processing/1s_cosine_psth/1s_cosine_psth_9 (TimeSeries) no description
  Group /processing/spike_times (ProcessingModule) Spike times per unit
  Group /processing/spike_times/spike_times_0 (TimeSeries) no description
  Group /processing/spike_times/spike_times_1 (TimeSeries) no description
  Group /processing/spike_times/spike_times_10 (TimeSeries) no description
  Group /processing/spike_times/spike_times_11 (TimeSeries) no description
  Group /processing/spike_times/spike_times_12 (TimeSeries) no description
  Group /processing/spike_times/spike_times_13 (TimeSeries) no description
  Group /processing/spike_times/spike_times_14 (TimeSeries) no description
  Group /processing/spike_times/spike_times_15 (TimeSeries) no description
  Group /processing/spike_times/spike_times_16 (TimeSeries) no description
  Group /processing/spike_times/spike_times_17 (TimeSeries) no description
  Group /processing/spike_times/spike_times_18 (TimeSeries) no description
  Group /processing/spike_times/spike_times_19 (TimeSeries) no description
  Group /processing/spike_times/spike_times_2 (TimeSeries) no description
  Group /processing/spike_times/spike_times_20 (TimeSeries) no description
  Group /processing/spike_times/spike_times_21 (TimeSeries) no description
  Group /processing/spike_times/spike_times_22 (TimeSeries) no description
  Group /processing/spike_times/spike_times_23 (TimeSeries) no description
  Group /processing/spike_times/spike_times_24 (TimeSeries) no description
  Group /processing/spike_times/spike_times_25 (TimeSeries) no description
  Group /processing/spike_times/spike_times_26 (TimeSeries) no description
  Group /processing/spike_times/spike_times_27 (TimeSeries) no description
  Group /processing/spike_times/spike_times_28 (TimeSeries) no description
  Group /processing/spike_times/spike_times_29 (TimeSeries) no description
  Group /processing/spike_times/spike_times_3 (TimeSeries) no description
  Group /processing/spike_times/spike_times_30 (TimeSeries) no description
  Group /processing/spike_times/spike_times_31 (TimeSeries) no description
  Group /processing/spike_times/spike_times_32 (TimeSeries) no description
  Group /processing/spike_times/spike_times_33 (TimeSeries) no description
  Group /processing/spike_times/spike_times_34 (TimeSeries) no description
  Group /processing/spike_times/spike_times_35 (TimeSeries) no description
  Group /processing/spike_times/spike_times_36 (TimeSeries) no description
  Group /processing/spike_times/spike_times_37 (TimeSeries) no description
  Group /processing/spike_times/spike_times_38 (TimeSeries) no description
  Group /processing/spike_times/spike_times_39 (TimeSeries) no description
  Group /processing/spike_times/spike_times_4 (TimeSeries) no description
  Group /processing/spike_times/spike_times_40 (TimeSeries) no description
  Group /processing/spike_times/spike_times_41 (TimeSeries) no description
  Group /processing/spike_times/spike_times_42 (TimeSeries) no description
  Group /processing/spike_times/spike_times_43 (TimeSeries) no description
  Group /processing/spike_times/spike_times_44 (TimeSeries) no description
  Group /processing/spike_times/spike_times_45 (TimeSeries) no description
  Group /processing/spike_times/spike_times_46 (TimeSeries) no description
  Group /processing/spike_times/spike_times_47 (TimeSeries) no description
  Group /processing/spike_times/spike_times_48 (TimeSeries) no description
  Group /processing/spike_times/spike_times_49 (TimeSeries) no description
  Group /processing/spike_times/spike_times_5 (TimeSeries) no description
  Group /processing/spike_times/spike_times_50 (TimeSeries) no description
  Group /processing/spike_times/spike_times_51 (TimeSeries) no description
  Group /processing/spike_times/spike_times_52 (TimeSeries) no description
  Group /processing/spike_times/spike_times_53 (TimeSeries) no description
  Group /processing/spike_times/spike_times_54 (TimeSeries) no description
  Group /processing/spike_times/spike_times_55 (TimeSeries) no description
  Group /processing/spike_times/spike_times_56 (TimeSeries) no description
  Group /processing/spike_times/spike_times_57 (TimeSeries) no description
  Group /processing/spike_times/spike_times_58 (TimeSeries) no description
  Group /processing/spike_times/spike_times_59 (TimeSeries) no description
  Group /processing/spike_times/spike_times_6 (TimeSeries) no description
  Group /processing/spike_times/spike_times_60 (TimeSeries) no description
  Group /processing/spike_times/spike_times_61 (TimeSeries) no description
  Group /processing/spike_times/spike_times_62 (TimeSeries) no description
  Group /processing/spike_times/spike_times_63 (TimeSeries) no description
  Group /processing/spike_times/spike_times_7 (TimeSeries) no description
  Group /processing/spike_times/spike_times_8 (TimeSeries) no description
  Group /processing/spike_times/spike_times_9 (TimeSeries) no description
  Group /processing/waveforms (ProcessingModule) Waveforms per unit
  Group /processing/waveforms/waveform_0 (TimeSeries) no description
  Group /processing/waveforms/waveform_1 (TimeSeries) no description
  Group /processing/waveforms/waveform_10 (TimeSeries) no description
  Group /processing/waveforms/waveform_11 (TimeSeries) no description
  Group /processing/waveforms/waveform_12 (TimeSeries) no description
  Group /processing/waveforms/waveform_13 (TimeSeries) no description
  Group /processing/waveforms/waveform_14 (TimeSeries) no description
  Group /processing/waveforms/waveform_15 (TimeSeries) no description
  Group /processing/waveforms/waveform_16 (TimeSeries) no description
  Group /processing/waveforms/waveform_17 (TimeSeries) no description
  Group /processing/waveforms/waveform_18 (TimeSeries) no description
  Group /processing/waveforms/waveform_19 (TimeSeries) no description
  Group /processing/waveforms/waveform_2 (TimeSeries) no description
  Group /processing/waveforms/waveform_20 (TimeSeries) no description
  Group /processing/waveforms/waveform_21 (TimeSeries) no description
  Group /processing/waveforms/waveform_22 (TimeSeries) no description
  Group /processing/waveforms/waveform_23 (TimeSeries) no description
  Group /processing/waveforms/waveform_24 (TimeSeries) no description
  Group /processing/waveforms/waveform_25 (TimeSeries) no description
  Group /processing/waveforms/waveform_26 (TimeSeries) no description
  Group /processing/waveforms/waveform_27 (TimeSeries) no description
  Group /processing/waveforms/waveform_28 (TimeSeries) no description
  Group /processing/waveforms/waveform_29 (TimeSeries) no description
  Group /processing/waveforms/waveform_3 (TimeSeries) no description
  Group /processing/waveforms/waveform_30 (TimeSeries) no description
  Group /processing/waveforms/waveform_31 (TimeSeries) no description
  Group /processing/waveforms/waveform_32 (TimeSeries) no description
  Group /processing/waveforms/waveform_33 (TimeSeries) no description
  Group /processing/waveforms/waveform_34 (TimeSeries) no description
  Group /processing/waveforms/waveform_35 (TimeSeries) no description
  Group /processing/waveforms/waveform_36 (TimeSeries) no description
  Group /processing/waveforms/waveform_37 (TimeSeries) no description
  Group /processing/waveforms/waveform_38 (TimeSeries) no description
  Group /processing/waveforms/waveform_39 (TimeSeries) no description
  Group /processing/waveforms/waveform_4 (TimeSeries) no description
  Group /processing/waveforms/waveform_40 (TimeSeries) no description
  Group /processing/waveforms/waveform_41 (TimeSeries) no description
  Group /processing/waveforms/waveform_42 (TimeSeries) no description
  Group /processing/waveforms/waveform_43 (TimeSeries) no description
  Group /processing/waveforms/waveform_44 (TimeSeries) no description
  Group /processing/waveforms/waveform_45 (TimeSeries) no description
  Group /processing/waveforms/waveform_46 (TimeSeries) no description
  Group /processing/waveforms/waveform_47 (TimeSeries) no description
  Group /processing/waveforms/waveform_48 (TimeSeries) no description
  Group /processing/waveforms/waveform_49 (TimeSeries) no description
  Group /processing/waveforms/waveform_5 (TimeSeries) no description
  Group /processing/waveforms/waveform_50 (TimeSeries) no description
  Group /processing/waveforms/waveform_51 (TimeSeries) no description
  Group /processing/waveforms/waveform_52 (TimeSeries) no description
  Group /processing/waveforms/waveform_53 (TimeSeries) no description
  Group /processing/waveforms/waveform_54 (TimeSeries) no description
  Group /processing/waveforms/waveform_55 (TimeSeries) no description
  Group /processing/waveforms/waveform_56 (TimeSeries) no description
  Group /processing/waveforms/waveform_57 (TimeSeries) no description
  Group /processing/waveforms/waveform_58 (TimeSeries) no description
  Group /processing/waveforms/waveform_59 (TimeSeries) no description
  Group /processing/waveforms/waveform_6 (TimeSeries) no description
  Group /processing/waveforms/waveform_60 (TimeSeries) no description
  Group /processing/waveforms/waveform_61 (TimeSeries) no description
  Group /processing/waveforms/waveform_62 (TimeSeries) no description
  Group /processing/waveforms/waveform_63 (TimeSeries) no description
  Group /processing/waveforms/waveform_7 (TimeSeries) no description
  Group /processing/waveforms/waveform_8 (TimeSeries) no description
  Group /processing/waveforms/waveform_9 (TimeSeries) no description
  session_description: Optotagging experiment in a VIP-Cre;Ai32 mouse. This is the first recording in this series on this day for this mouse.
  session_start_time: 2021-02-09T00:00:00+00:00
  timestamps_reference_time: 2021-02-09T00:00:00+00:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/PTR (VectorData) Column PTR from units data | shape = (64,) | dtype = float64
  Dataset /units/amp (VectorData) Column amp from units data | shape = (64,) | dtype = float64
  Dataset /units/avg_ISI (VectorData) Column avg_ISI from units data | shape = (64,) | dtype = float64
  Dataset /units/baseline_FR (VectorData) Column baseline_FR from units data | shape = (64,) | dtype = float64
  Dataset /units/ct (VectorData) Column ct from units data | shape = (64,) | dtype = object
  Dataset /units/dur (VectorData) Column dur from units data | shape = (64,) | dtype = float64
  Dataset /units/footprint (VectorData) Column footprint from units data | shape = (64,) | dtype = int32
  Dataset /units/genotype (VectorData) Column genotype from units data | shape = (64,) | dtype = object
  Dataset /units/id (ElementIdentifiers)  | shape = (64,) | dtype = int32
  Dataset /units/mouseID (VectorData) Column mouseID from units data | shape = (64,) | dtype = object
  Dataset /units/optotagged (VectorData) Column optotagged from units data | shape = (64,) | dtype = int32
  Dataset /units/prePTR (VectorData) Column prePTR from units data | shape = (64,) | dtype = float64
  Dataset /units/probe (VectorData) Column probe from units data | shape = (64,) | dtype = object
  Dataset /units/recording (VectorData) Column recording from units data | shape = (64,) | dtype = object
  Dataset /units/recording_date (VectorData) Column recording_date from units data | shape = (64,) | dtype = object
  Dataset /units/recov_slope (VectorData) Column recov_slope from units data | shape = (64,) | dtype = float64
  Dataset /units/repol_slope (VectorData) Column repol_slope from units data | shape = (64,) | dtype = float64
  Dataset /units/sessionID (VectorData) Column sessionID from units data | shape = (64,) | dtype = object
  Dataset /units/unitID (VectorData) Column unitID from units data | shape = (64,) | dtype = object
