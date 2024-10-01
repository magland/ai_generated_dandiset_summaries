
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000041/0.210812.1515
name: Network Homeostasis and State Dynamics of Neocortical Sleep
contributor: [{'name': 'Watson, Brendon O.', 'roleName': ['dcite:Author', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Levenstein, Daniel', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Greene, J. Palmer', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Gelinas, Jennifer N.', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Buzsáki, György', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-3100-4800', 'affiliation': [], 'includeInCitation': True}]
description: Data was recorded using silicon probe electrodes in the frontal cortices of male Long Evans rats between 4-7 months of age. The design was to have no specific behavior, task or stimulus, rather the animal was left alone in it’s home cage (which it lives in at all
times). Data includes both local field potentials (LFP) and spikes. 11 total animals, 27 recording sessions, 1360 total units recorded, 1121 units considered stable, 995 putative excitatory units and 126 putative inhibitory units. Only recordings including a “WAKE-SLEEP” episode wherein at least 7 minutes of wake are followed by 20 minutes of sleep. On average 2 such WAKE-SLEEP episodes per recording session. 
assetsSummary: {'species': [{'name': 'Brown rat', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10116'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 154863459017, 'numberOfFiles': 22, 'numberOfSubjects': 10, 'variableMeasured': ['Units', 'LFP', 'ElectricalSeries'], 'measurementTechnique': [{'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'signal filtering technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000041 has 9 NWB files.
2 of these NWB files are of type 1.
1 of these NWB files are of type 2.
2 of these NWB files are of type 3.
3 of these NWB files are of type 4.
1 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2020-10-03T13:47:04.119233-04:00']
  Group /general/devices/implant (Device) silicon probe electrodes; see BWRat17_121712.xml or BWRat17_121712.sessionInfo.mat for more information
  experimenter: ['Brendon Watson']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (66,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (66,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (66,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (66,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (66,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (66,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/rel_x (VectorData) the x coordinate within the electrode group | shape = (66,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_y (VectorData) the y coordinate within the electrode group | shape = (66,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/shank_electrode_number (VectorData) 0-indexed channel within a shank | shape = (66,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/spindle_reference (VectorData) this electrode was used to calculate slow-wave sleep | shape = (66,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/theta_reference (VectorData) this electrode was used to calculate theta canonical bands | shape = (66,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/up_reference (VectorData) this electrode was used to calculate UP-states | shape = (66,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (66,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (66,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (66,) | dtype = float64
  Group /general/extracellular_ephys/shank1 (ElectrodeGroup) shank1 electrodes
  Group /general/extracellular_ephys/shank1/device (Device) silicon probe electrodes; see BWRat17_121712.xml or BWRat17_121712.sessionInfo.mat for more information
  Group /general/extracellular_ephys/shank2 (ElectrodeGroup) shank2 electrodes
  Group /general/extracellular_ephys/shank2/device (Device) silicon probe electrodes; see BWRat17_121712.xml or BWRat17_121712.sessionInfo.mat for more information
  Group /general/extracellular_ephys/shank3 (ElectrodeGroup) shank3 electrodes
  Group /general/extracellular_ephys/shank3/device (Device) silicon probe electrodes; see BWRat17_121712.xml or BWRat17_121712.sessionInfo.mat for more information
  Group /general/extracellular_ephys/shank4 (ElectrodeGroup) shank4 electrodes
  Group /general/extracellular_ephys/shank4/device (Device) silicon probe electrodes; see BWRat17_121712.xml or BWRat17_121712.sessionInfo.mat for more information
  Group /general/extracellular_ephys/shank5 (ElectrodeGroup) shank5 electrodes
  Group /general/extracellular_ephys/shank5/device (Device) silicon probe electrodes; see BWRat17_121712.xml or BWRat17_121712.sessionInfo.mat for more information
  Group /general/extracellular_ephys/shank6 (ElectrodeGroup) shank6 electrodes
  Group /general/extracellular_ephys/shank6/device (Device) silicon probe electrodes; see BWRat17_121712.xml or BWRat17_121712.sessionInfo.mat for more information
  Group /general/extracellular_ephys/shank7 (ElectrodeGroup) shank7 electrodes
  Group /general/extracellular_ephys/shank7/device (Device) silicon probe electrodes; see BWRat17_121712.xml or BWRat17_121712.sessionInfo.mat for more information
  Group /general/extracellular_ephys/shank8 (ElectrodeGroup) shank8 electrodes
  Group /general/extracellular_ephys/shank8/device (Device) silicon probe electrodes; see BWRat17_121712.xml or BWRat17_121712.sessionInfo.mat for more information
  Group /general/extracellular_ephys/shank9 (ElectrodeGroup) shank9 electrodes
  Group /general/extracellular_ephys/shank9/device (Device) silicon probe electrodes; see BWRat17_121712.xml or BWRat17_121712.sessionInfo.mat for more information
  institution: NYU
  lab: Buzsaki
  related_publications: ['Network Homeostasis and State Dynamics of Neocortical SleepWatson BO, Levenstein D, Greene JP, Gelinas JN, Buzsáki G.Neuron. 2016 Apr 27. pii: S0896-6273(16)30056-3.doi: 10.1016/j.neuron.2016.03.036']
  session_id: BWRat17_121712
  Group /general/subject (Subject) 
  identifier: BWRat17_121712
  Group /processing/behavior (ProcessingModule) contains behavioral data
  Group /processing/behavior/states (TimeIntervals) Sleep states of animal.
  Dataset /processing/behavior/states/id (ElementIdentifiers)  | shape = (33,) | dtype = int32
  Dataset /processing/behavior/states/label (VectorData) Sleep state. | shape = (33,) | dtype = object
  Dataset /processing/behavior/states/start_time (VectorData) Start time of epoch, in seconds | shape = (33,) | dtype = float32
  Dataset /processing/behavior/states/stop_time (VectorData) Stop time of epoch, in seconds | shape = (33,) | dtype = float32
  Group /processing/ecephys (ProcessingModule) intermediate data from extracellular electrophysiology recordings, e.g., LFP
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/lfp (ElectricalSeries) lfp signal for all shank electrodes
  Dataset /processing/ecephys/LFP/lfp/electrodes (DynamicTableRegion) electrode table reference | shape = (66,) | dtype = int32
  Group /processing/ecephys/SpikeWaveforms1 (SpikeEventSeries) no description
  Dataset /processing/ecephys/SpikeWaveforms1/electrodes (DynamicTableRegion) shank1 region | shape = (8,) | dtype = int64
  Group /processing/ecephys/SpikeWaveforms2 (SpikeEventSeries) no description
  Dataset /processing/ecephys/SpikeWaveforms2/electrodes (DynamicTableRegion) shank2 region | shape = (8,) | dtype = int64
  Group /processing/ecephys/SpikeWaveforms3 (SpikeEventSeries) no description
  Dataset /processing/ecephys/SpikeWaveforms3/electrodes (DynamicTableRegion) shank3 region | shape = (8,) | dtype = int64
  Group /processing/ecephys/SpikeWaveforms4 (SpikeEventSeries) no description
  Dataset /processing/ecephys/SpikeWaveforms4/electrodes (DynamicTableRegion) shank4 region | shape = (8,) | dtype = int64
  Group /processing/ecephys/SpikeWaveforms5 (SpikeEventSeries) no description
  Dataset /processing/ecephys/SpikeWaveforms5/electrodes (DynamicTableRegion) shank5 region | shape = (7,) | dtype = int64
  Group /processing/ecephys/SpikeWaveforms6 (SpikeEventSeries) no description
  Dataset /processing/ecephys/SpikeWaveforms6/electrodes (DynamicTableRegion) shank6 region | shape = (7,) | dtype = int64
  Group /processing/ecephys/SpikeWaveforms7 (SpikeEventSeries) no description
  Dataset /processing/ecephys/SpikeWaveforms7/electrodes (DynamicTableRegion) shank7 region | shape = (8,) | dtype = int64
  Group /processing/ecephys/SpikeWaveforms8 (SpikeEventSeries) no description
  Dataset /processing/ecephys/SpikeWaveforms8/electrodes (DynamicTableRegion) shank8 region | shape = (8,) | dtype = int64
  Group /processing/ecephys/SpikeWaveforms9 (SpikeEventSeries) no description
  Dataset /processing/ecephys/SpikeWaveforms9/electrodes (DynamicTableRegion) shank9 region | shape = (4,) | dtype = int64
  Group /processing/ecephys/SpindleDecompositionSeries (DecompositionSeries) Theta and Gamma phase for spindle-reference LFP
  Group /processing/ecephys/SpindleDecompositionSeries/bands (DynamicTable) data about the frequency bands that the signal was decomposed into
  Dataset /processing/ecephys/SpindleDecompositionSeries/bands/band_limits (VectorData) low and high frequencies of bandpass filter in Hz | shape = (2, 2) | dtype = int32
  Dataset /processing/ecephys/SpindleDecompositionSeries/bands/band_name (VectorData) the name of the frequency band (recommended: 'alpha', 'beta', 'gamma', 'delta', 'high gamma' | shape = (2,) | dtype = object
  Dataset /processing/ecephys/SpindleDecompositionSeries/bands/id (ElementIdentifiers)  | shape = (2,) | dtype = int32
  Group /processing/ecephys/SpindleDecompositionSeries/source_timeseries (ElectricalSeries) lfp signal for all shank electrodes
  Dataset /processing/ecephys/SpindleDecompositionSeries/source_timeseries/electrodes (DynamicTableRegion) electrode table reference | shape = (66,) | dtype = int32
  Group /processing/ecephys/ThetaDecompositionSeries (DecompositionSeries) Theta and Gamma phase for theta-reference LFP
  Group /processing/ecephys/ThetaDecompositionSeries/bands (DynamicTable) data about the frequency bands that the signal was decomposed into
  Dataset /processing/ecephys/ThetaDecompositionSeries/bands/band_limits (VectorData) low and high frequencies of bandpass filter in Hz | shape = (2, 2) | dtype = int32
  Dataset /processing/ecephys/ThetaDecompositionSeries/bands/band_name (VectorData) the name of the frequency band (recommended: 'alpha', 'beta', 'gamma', 'delta', 'high gamma' | shape = (2,) | dtype = object
  Dataset /processing/ecephys/ThetaDecompositionSeries/bands/id (ElementIdentifiers)  | shape = (2,) | dtype = int32
  Group /processing/ecephys/ThetaDecompositionSeries/source_timeseries (ElectricalSeries) lfp signal for all shank electrodes
  Dataset /processing/ecephys/ThetaDecompositionSeries/source_timeseries/electrodes (DynamicTableRegion) electrode table reference | shape = (66,) | dtype = int32
  Group /processing/ecephys/UPDecompositionSeries (DecompositionSeries) Theta and Gamma phase for up-reference LFP
  Group /processing/ecephys/UPDecompositionSeries/bands (DynamicTable) data about the frequency bands that the signal was decomposed into
  Dataset /processing/ecephys/UPDecompositionSeries/bands/band_limits (VectorData) low and high frequencies of bandpass filter in Hz | shape = (2, 2) | dtype = int32
  Dataset /processing/ecephys/UPDecompositionSeries/bands/band_name (VectorData) the name of the frequency band (recommended: 'alpha', 'beta', 'gamma', 'delta', 'high gamma' | shape = (2,) | dtype = object
  Dataset /processing/ecephys/UPDecompositionSeries/bands/id (ElementIdentifiers)  | shape = (2,) | dtype = int32
  Group /processing/ecephys/UPDecompositionSeries/source_timeseries (ElectricalSeries) lfp signal for all shank electrodes
  Dataset /processing/ecephys/UPDecompositionSeries/source_timeseries/electrodes (DynamicTableRegion) electrode table reference | shape = (66,) | dtype = int32
  session_description: Data was recorded using silicon probe electrodes in the frontal cortices of male Long Evans rats between 4-7 months of age. The design was to have no specific behavior, task or stimulus, rather the animal was left alone in it’s home cage (which it lives in at all times).
  session_start_time: 2012-12-17T00:00:00-05:00
  timestamps_reference_time: 2012-12-17T00:00:00-05:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/cell_type (VectorData) name of cell type | shape = (50,) | dtype = object
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (50,) | dtype = object
  Dataset /units/global_id (VectorData) global id for cell for entire experiment | shape = (50,) | dtype = int32
  Dataset /units/id (ElementIdentifiers)  | shape = (50,) | dtype = int32
  Dataset /units/region (VectorData) brain region where unit was detected | shape = (50,) | dtype = object
  Dataset /units/shank_id (VectorData) 0-indexed id of cluster from shank | shape = (50,) | dtype = int32
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (345203,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex)  | shape = (50,) | dtype = int32


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2020-10-03T13:51:38.612596-04:00']
  Group /general/devices/implant (Device) silicon probe electrodes; see BWRat18_020513.xml or BWRat18_020513.sessionInfo.mat for more information
  experimenter: ['Brendon Watson']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (128,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/rel_x (VectorData) the x coordinate within the electrode group | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_y (VectorData) the y coordinate within the electrode group | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/shank_electrode_number (VectorData) 0-indexed channel within a shank | shape = (128,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/spindle_reference (VectorData) this electrode was used to calculate slow-wave sleep | shape = (128,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/theta_reference (VectorData) this electrode was used to calculate theta canonical bands | shape = (128,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/up_reference (VectorData) this electrode was used to calculate UP-states | shape = (128,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (128,) | dtype = float64
  Group /general/extracellular_ephys/shank1 (ElectrodeGroup) shank1 electrodes
  Group /general/extracellular_ephys/shank1/device (Device) silicon probe electrodes; see BWRat18_020513.xml or BWRat18_020513.sessionInfo.mat for more information
  Group /general/extracellular_ephys/shank10 (ElectrodeGroup) shank10 electrodes
  Group /general/extracellular_ephys/shank10/device (Device) silicon probe electrodes; see BWRat18_020513.xml or BWRat18_020513.sessionInfo.mat for more information
  Group /general/extracellular_ephys/shank11 (ElectrodeGroup) shank11 electrodes
  Group /general/extracellular_ephys/shank11/device (Device) silicon probe electrodes; see BWRat18_020513.xml or BWRat18_020513.sessionInfo.mat for more information
  Group /general/extracellular_ephys/shank12 (ElectrodeGroup) shank12 electrodes
  Group /general/extracellular_ephys/shank12/device (Device) silicon probe electrodes; see BWRat18_020513.xml or BWRat18_020513.sessionInfo.mat for more information
  Group /general/extracellular_ephys/shank13 (ElectrodeGroup) shank13 electrodes
  Group /general/extracellular_ephys/shank13/device (Device) silicon probe electrodes; see BWRat18_020513.xml or BWRat18_020513.sessionInfo.mat for more information
  Group /general/extracellular_ephys/shank14 (ElectrodeGroup) shank14 electrodes
  Group /general/extracellular_ephys/shank14/device (Device) silicon probe electrodes; see BWRat18_020513.xml or BWRat18_020513.sessionInfo.mat for more information
  Group /general/extracellular_ephys/shank15 (ElectrodeGroup) shank15 electrodes
  Group /general/extracellular_ephys/shank15/device (Device) silicon probe electrodes; see BWRat18_020513.xml or BWRat18_020513.sessionInfo.mat for more information
  Group /general/extracellular_ephys/shank16 (ElectrodeGroup) shank16 electrodes
  Group /general/extracellular_ephys/shank16/device (Device) silicon probe electrodes; see BWRat18_020513.xml or BWRat18_020513.sessionInfo.mat for more information
  Group /general/extracellular_ephys/shank2 (ElectrodeGroup) shank2 electrodes
  Group /general/extracellular_ephys/shank2/device (Device) silicon probe electrodes; see BWRat18_020513.xml or BWRat18_020513.sessionInfo.mat for more information
  Group /general/extracellular_ephys/shank3 (ElectrodeGroup) shank3 electrodes
  Group /general/extracellular_ephys/shank3/device (Device) silicon probe electrodes; see BWRat18_020513.xml or BWRat18_020513.sessionInfo.mat for more information
  Group /general/extracellular_ephys/shank4 (ElectrodeGroup) shank4 electrodes
  Group /general/extracellular_ephys/shank4/device (Device) silicon probe electrodes; see BWRat18_020513.xml or BWRat18_020513.sessionInfo.mat for more information
  Group /general/extracellular_ephys/shank5 (ElectrodeGroup) shank5 electrodes
  Group /general/extracellular_ephys/shank5/device (Device) silicon probe electrodes; see BWRat18_020513.xml or BWRat18_020513.sessionInfo.mat for more information
  Group /general/extracellular_ephys/shank6 (ElectrodeGroup) shank6 electrodes
  Group /general/extracellular_ephys/shank6/device (Device) silicon probe electrodes; see BWRat18_020513.xml or BWRat18_020513.sessionInfo.mat for more information
  Group /general/extracellular_ephys/shank7 (ElectrodeGroup) shank7 electrodes
  Group /general/extracellular_ephys/shank7/device (Device) silicon probe electrodes; see BWRat18_020513.xml or BWRat18_020513.sessionInfo.mat for more information
  Group /general/extracellular_ephys/shank8 (ElectrodeGroup) shank8 electrodes
  Group /general/extracellular_ephys/shank8/device (Device) silicon probe electrodes; see BWRat18_020513.xml or BWRat18_020513.sessionInfo.mat for more information
  Group /general/extracellular_ephys/shank9 (ElectrodeGroup) shank9 electrodes
  Group /general/extracellular_ephys/shank9/device (Device) silicon probe electrodes; see BWRat18_020513.xml or BWRat18_020513.sessionInfo.mat for more information
  institution: NYU
  lab: Buzsaki
  related_publications: ['Network Homeostasis and State Dynamics of Neocortical SleepWatson BO, Levenstein D, Greene JP, Gelinas JN, Buzsáki G.Neuron. 2016 Apr 27. pii: S0896-6273(16)30056-3.doi: 10.1016/j.neuron.2016.03.036']
  session_id: BWRat18_020513
  Group /general/subject (Subject) 
  identifier: BWRat18_020513
  Group /processing/behavior (ProcessingModule) contains behavioral data
  Group /processing/behavior/states (TimeIntervals) Sleep states of animal.
  Dataset /processing/behavior/states/id (ElementIdentifiers)  | shape = (53,) | dtype = int32
  Dataset /processing/behavior/states/label (VectorData) Sleep state. | shape = (53,) | dtype = object
  Dataset /processing/behavior/states/start_time (VectorData) Start time of epoch, in seconds | shape = (53,) | dtype = float32
  Dataset /processing/behavior/states/stop_time (VectorData) Stop time of epoch, in seconds | shape = (53,) | dtype = float32
  Group /processing/ecephys (ProcessingModule) intermediate data from extracellular electrophysiology recordings, e.g., LFP
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/lfp (ElectricalSeries) lfp signal for all shank electrodes
  Dataset /processing/ecephys/LFP/lfp/electrodes (DynamicTableRegion) electrode table reference | shape = (128,) | dtype = int32
  Group /processing/ecephys/SpikeWaveforms1 (SpikeEventSeries) no description
  Dataset /processing/ecephys/SpikeWaveforms1/electrodes (DynamicTableRegion) shank1 region | shape = (8,) | dtype = int64
  Group /processing/ecephys/SpikeWaveforms10 (SpikeEventSeries) no description
  Dataset /processing/ecephys/SpikeWaveforms10/electrodes (DynamicTableRegion) shank10 region | shape = (8,) | dtype = int64
  Group /processing/ecephys/SpikeWaveforms11 (SpikeEventSeries) no description
  Dataset /processing/ecephys/SpikeWaveforms11/electrodes (DynamicTableRegion) shank11 region | shape = (8,) | dtype = int64
  Group /processing/ecephys/SpikeWaveforms12 (SpikeEventSeries) no description
  Dataset /processing/ecephys/SpikeWaveforms12/electrodes (DynamicTableRegion) shank12 region | shape = (8,) | dtype = int64
  Group /processing/ecephys/SpikeWaveforms13 (SpikeEventSeries) no description
  Dataset /processing/ecephys/SpikeWaveforms13/electrodes (DynamicTableRegion) shank13 region | shape = (8,) | dtype = int64
  Group /processing/ecephys/SpikeWaveforms14 (SpikeEventSeries) no description
  Dataset /processing/ecephys/SpikeWaveforms14/electrodes (DynamicTableRegion) shank14 region | shape = (8,) | dtype = int64
  Group /processing/ecephys/SpikeWaveforms15 (SpikeEventSeries) no description
  Dataset /processing/ecephys/SpikeWaveforms15/electrodes (DynamicTableRegion) shank15 region | shape = (8,) | dtype = int64
  Group /processing/ecephys/SpikeWaveforms16 (SpikeEventSeries) no description
  Dataset /processing/ecephys/SpikeWaveforms16/electrodes (DynamicTableRegion) shank16 region | shape = (8,) | dtype = int64
  Group /processing/ecephys/SpikeWaveforms2 (SpikeEventSeries) no description
  Dataset /processing/ecephys/SpikeWaveforms2/electrodes (DynamicTableRegion) shank2 region | shape = (8,) | dtype = int64
  Group /processing/ecephys/SpikeWaveforms3 (SpikeEventSeries) no description
  Dataset /processing/ecephys/SpikeWaveforms3/electrodes (DynamicTableRegion) shank3 region | shape = (8,) | dtype = int64
  Group /processing/ecephys/SpikeWaveforms4 (SpikeEventSeries) no description
  Dataset /processing/ecephys/SpikeWaveforms4/electrodes (DynamicTableRegion) shank4 region | shape = (8,) | dtype = int64
  Group /processing/ecephys/SpikeWaveforms5 (SpikeEventSeries) no description
  Dataset /processing/ecephys/SpikeWaveforms5/electrodes (DynamicTableRegion) shank5 region | shape = (8,) | dtype = int64
  Group /processing/ecephys/SpikeWaveforms6 (SpikeEventSeries) no description
  Dataset /processing/ecephys/SpikeWaveforms6/electrodes (DynamicTableRegion) shank6 region | shape = (8,) | dtype = int64
  Group /processing/ecephys/SpikeWaveforms7 (SpikeEventSeries) no description
  Dataset /processing/ecephys/SpikeWaveforms7/electrodes (DynamicTableRegion) shank7 region | shape = (8,) | dtype = int64
  Group /processing/ecephys/SpikeWaveforms8 (SpikeEventSeries) no description
  Dataset /processing/ecephys/SpikeWaveforms8/electrodes (DynamicTableRegion) shank8 region | shape = (8,) | dtype = int64
  Group /processing/ecephys/SpikeWaveforms9 (SpikeEventSeries) no description
  Dataset /processing/ecephys/SpikeWaveforms9/electrodes (DynamicTableRegion) shank9 region | shape = (8,) | dtype = int64
  Group /processing/ecephys/SpindleDecompositionSeries (DecompositionSeries) Theta and Gamma phase for spindle-reference LFP
  Group /processing/ecephys/SpindleDecompositionSeries/bands (DynamicTable) data about the frequency bands that the signal was decomposed into
  Dataset /processing/ecephys/SpindleDecompositionSeries/bands/band_limits (VectorData) low and high frequencies of bandpass filter in Hz | shape = (2, 2) | dtype = int32
  Dataset /processing/ecephys/SpindleDecompositionSeries/bands/band_name (VectorData) the name of the frequency band (recommended: 'alpha', 'beta', 'gamma', 'delta', 'high gamma' | shape = (2,) | dtype = object
  Dataset /processing/ecephys/SpindleDecompositionSeries/bands/id (ElementIdentifiers)  | shape = (2,) | dtype = int32
  Group /processing/ecephys/SpindleDecompositionSeries/source_timeseries (ElectricalSeries) lfp signal for all shank electrodes
  Dataset /processing/ecephys/SpindleDecompositionSeries/source_timeseries/electrodes (DynamicTableRegion) electrode table reference | shape = (128,) | dtype = int32
  Group /processing/ecephys/ThetaDecompositionSeries (DecompositionSeries) Theta and Gamma phase for theta-reference LFP
  Group /processing/ecephys/ThetaDecompositionSeries/bands (DynamicTable) data about the frequency bands that the signal was decomposed into
  Dataset /processing/ecephys/ThetaDecompositionSeries/bands/band_limits (VectorData) low and high frequencies of bandpass filter in Hz | shape = (2, 2) | dtype = int32
  Dataset /processing/ecephys/ThetaDecompositionSeries/bands/band_name (VectorData) the name of the frequency band (recommended: 'alpha', 'beta', 'gamma', 'delta', 'high gamma' | shape = (2,) | dtype = object
  Dataset /processing/ecephys/ThetaDecompositionSeries/bands/id (ElementIdentifiers)  | shape = (2,) | dtype = int32
  Group /processing/ecephys/ThetaDecompositionSeries/source_timeseries (ElectricalSeries) lfp signal for all shank electrodes
  Dataset /processing/ecephys/ThetaDecompositionSeries/source_timeseries/electrodes (DynamicTableRegion) electrode table reference | shape = (128,) | dtype = int32
  Group /processing/ecephys/UPDecompositionSeries (DecompositionSeries) Theta and Gamma phase for up-reference LFP
  Group /processing/ecephys/UPDecompositionSeries/bands (DynamicTable) data about the frequency bands that the signal was decomposed into
  Dataset /processing/ecephys/UPDecompositionSeries/bands/band_limits (VectorData) low and high frequencies of bandpass filter in Hz | shape = (2, 2) | dtype = int32
  Dataset /processing/ecephys/UPDecompositionSeries/bands/band_name (VectorData) the name of the frequency band (recommended: 'alpha', 'beta', 'gamma', 'delta', 'high gamma' | shape = (2,) | dtype = object
  Dataset /processing/ecephys/UPDecompositionSeries/bands/id (ElementIdentifiers)  | shape = (2,) | dtype = int32
  Group /processing/ecephys/UPDecompositionSeries/source_timeseries (ElectricalSeries) lfp signal for all shank electrodes
  Dataset /processing/ecephys/UPDecompositionSeries/source_timeseries/electrodes (DynamicTableRegion) electrode table reference | shape = (128,) | dtype = int32
  session_description: Data was recorded using silicon probe electrodes in the frontal cortices of male Long Evans rats between 4-7 months of age. The design was to have no specific behavior, task or stimulus, rather the animal was left alone in it’s home cage (which it lives in at all times).
  session_start_time: 2013-02-05T00:00:00-05:00
  timestamps_reference_time: 2013-02-05T00:00:00-05:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/cell_type (VectorData) name of cell type | shape = (40,) | dtype = object
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (40,) | dtype = object
  Dataset /units/global_id (VectorData) global id for cell for entire experiment | shape = (40,) | dtype = int32
  Dataset /units/id (ElementIdentifiers)  | shape = (40,) | dtype = int32
  Dataset /units/region (VectorData) brain region where unit was detected | shape = (40,) | dtype = object
  Dataset /units/shank_id (VectorData) 0-indexed id of cluster from shank | shape = (40,) | dtype = int32
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (222046,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex)  | shape = (40,) | dtype = int32


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2020-10-03T13:58:40.595278-04:00']
  Group /general/devices/implant (Device) silicon probe electrodes; see BWRat19_032413.xml or BWRat19_032413.sessionInfo.mat for more information
  experimenter: ['Brendon Watson']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (135,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (135,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (135,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (135,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (135,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (135,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/rel_x (VectorData) the x coordinate within the electrode group | shape = (135,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_y (VectorData) the y coordinate within the electrode group | shape = (135,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/shank_electrode_number (VectorData) 0-indexed channel within a shank | shape = (135,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/spindle_reference (VectorData) this electrode was used to calculate slow-wave sleep | shape = (135,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/theta_reference (VectorData) this electrode was used to calculate theta canonical bands | shape = (135,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/up_reference (VectorData) this electrode was used to calculate UP-states | shape = (135,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (135,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (135,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (135,) | dtype = float64
  Group /general/extracellular_ephys/shank1 (ElectrodeGroup) shank1 electrodes
  Group /general/extracellular_ephys/shank1/device (Device) silicon probe electrodes; see BWRat19_032413.xml or BWRat19_032413.sessionInfo.mat for more information
  Group /general/extracellular_ephys/shank10 (ElectrodeGroup) shank10 electrodes
  Group /general/extracellular_ephys/shank10/device (Device) silicon probe electrodes; see BWRat19_032413.xml or BWRat19_032413.sessionInfo.mat for more information
  Group /general/extracellular_ephys/shank11 (ElectrodeGroup) shank11 electrodes
  Group /general/extracellular_ephys/shank11/device (Device) silicon probe electrodes; see BWRat19_032413.xml or BWRat19_032413.sessionInfo.mat for more information
  Group /general/extracellular_ephys/shank12 (ElectrodeGroup) shank12 electrodes
  Group /general/extracellular_ephys/shank12/device (Device) silicon probe electrodes; see BWRat19_032413.xml or BWRat19_032413.sessionInfo.mat for more information
  Group /general/extracellular_ephys/shank13 (ElectrodeGroup) shank13 electrodes
  Group /general/extracellular_ephys/shank13/device (Device) silicon probe electrodes; see BWRat19_032413.xml or BWRat19_032413.sessionInfo.mat for more information
  Group /general/extracellular_ephys/shank14 (ElectrodeGroup) shank14 electrodes
  Group /general/extracellular_ephys/shank14/device (Device) silicon probe electrodes; see BWRat19_032413.xml or BWRat19_032413.sessionInfo.mat for more information
  Group /general/extracellular_ephys/shank15 (ElectrodeGroup) shank15 electrodes
  Group /general/extracellular_ephys/shank15/device (Device) silicon probe electrodes; see BWRat19_032413.xml or BWRat19_032413.sessionInfo.mat for more information
  Group /general/extracellular_ephys/shank2 (ElectrodeGroup) shank2 electrodes
  Group /general/extracellular_ephys/shank2/device (Device) silicon probe electrodes; see BWRat19_032413.xml or BWRat19_032413.sessionInfo.mat for more information
  Group /general/extracellular_ephys/shank3 (ElectrodeGroup) shank3 electrodes
  Group /general/extracellular_ephys/shank3/device (Device) silicon probe electrodes; see BWRat19_032413.xml or BWRat19_032413.sessionInfo.mat for more information
  Group /general/extracellular_ephys/shank4 (ElectrodeGroup) shank4 electrodes
  Group /general/extracellular_ephys/shank4/device (Device) silicon probe electrodes; see BWRat19_032413.xml or BWRat19_032413.sessionInfo.mat for more information
  Group /general/extracellular_ephys/shank5 (ElectrodeGroup) shank5 electrodes
  Group /general/extracellular_ephys/shank5/device (Device) silicon probe electrodes; see BWRat19_032413.xml or BWRat19_032413.sessionInfo.mat for more information
  Group /general/extracellular_ephys/shank6 (ElectrodeGroup) shank6 electrodes
  Group /general/extracellular_ephys/shank6/device (Device) silicon probe electrodes; see BWRat19_032413.xml or BWRat19_032413.sessionInfo.mat for more information
  Group /general/extracellular_ephys/shank7 (ElectrodeGroup) shank7 electrodes
  Group /general/extracellular_ephys/shank7/device (Device) silicon probe electrodes; see BWRat19_032413.xml or BWRat19_032413.sessionInfo.mat for more information
  Group /general/extracellular_ephys/shank8 (ElectrodeGroup) shank8 electrodes
  Group /general/extracellular_ephys/shank8/device (Device) silicon probe electrodes; see BWRat19_032413.xml or BWRat19_032413.sessionInfo.mat for more information
  Group /general/extracellular_ephys/shank9 (ElectrodeGroup) shank9 electrodes
  Group /general/extracellular_ephys/shank9/device (Device) silicon probe electrodes; see BWRat19_032413.xml or BWRat19_032413.sessionInfo.mat for more information
  institution: NYU
  lab: Buzsaki
  related_publications: ['Network Homeostasis and State Dynamics of Neocortical SleepWatson BO, Levenstein D, Greene JP, Gelinas JN, Buzsáki G.Neuron. 2016 Apr 27. pii: S0896-6273(16)30056-3.doi: 10.1016/j.neuron.2016.03.036']
  session_id: BWRat19_032413
  Group /general/subject (Subject) 
  identifier: BWRat19_032413
  Group /processing/behavior (ProcessingModule) contains behavioral data
  Group /processing/behavior/states (TimeIntervals) Sleep states of animal.
  Dataset /processing/behavior/states/id (ElementIdentifiers)  | shape = (34,) | dtype = int32
  Dataset /processing/behavior/states/label (VectorData) Sleep state. | shape = (34,) | dtype = object
  Dataset /processing/behavior/states/start_time (VectorData) Start time of epoch, in seconds | shape = (34,) | dtype = float32
  Dataset /processing/behavior/states/stop_time (VectorData) Stop time of epoch, in seconds | shape = (34,) | dtype = float32
  Group /processing/ecephys (ProcessingModule) intermediate data from extracellular electrophysiology recordings, e.g., LFP
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/lfp (ElectricalSeries) lfp signal for all shank electrodes
  Dataset /processing/ecephys/LFP/lfp/electrodes (DynamicTableRegion) electrode table reference | shape = (135,) | dtype = int32
  Group /processing/ecephys/SpikeWaveforms1 (SpikeEventSeries) no description
  Dataset /processing/ecephys/SpikeWaveforms1/electrodes (DynamicTableRegion) shank1 region | shape = (10,) | dtype = int64
  Group /processing/ecephys/SpikeWaveforms10 (SpikeEventSeries) no description
  Dataset /processing/ecephys/SpikeWaveforms10/electrodes (DynamicTableRegion) shank10 region | shape = (8,) | dtype = int64
  Group /processing/ecephys/SpikeWaveforms11 (SpikeEventSeries) no description
  Dataset /processing/ecephys/SpikeWaveforms11/electrodes (DynamicTableRegion) shank11 region | shape = (8,) | dtype = int64
  Group /processing/ecephys/SpikeWaveforms12 (SpikeEventSeries) no description
  Dataset /processing/ecephys/SpikeWaveforms12/electrodes (DynamicTableRegion) shank12 region | shape = (8,) | dtype = int64
  Group /processing/ecephys/SpikeWaveforms13 (SpikeEventSeries) no description
  Dataset /processing/ecephys/SpikeWaveforms13/electrodes (DynamicTableRegion) shank13 region | shape = (8,) | dtype = int64
  Group /processing/ecephys/SpikeWaveforms14 (SpikeEventSeries) no description
  Dataset /processing/ecephys/SpikeWaveforms14/electrodes (DynamicTableRegion) shank14 region | shape = (8,) | dtype = int64
  Group /processing/ecephys/SpikeWaveforms15 (SpikeEventSeries) no description
  Dataset /processing/ecephys/SpikeWaveforms15/electrodes (DynamicTableRegion) shank15 region | shape = (7,) | dtype = int64
  Group /processing/ecephys/SpikeWaveforms2 (SpikeEventSeries) no description
  Dataset /processing/ecephys/SpikeWaveforms2/electrodes (DynamicTableRegion) shank2 region | shape = (10,) | dtype = int64
  Group /processing/ecephys/SpikeWaveforms3 (SpikeEventSeries) no description
  Dataset /processing/ecephys/SpikeWaveforms3/electrodes (DynamicTableRegion) shank3 region | shape = (10,) | dtype = int64
  Group /processing/ecephys/SpikeWaveforms4 (SpikeEventSeries) no description
  Dataset /processing/ecephys/SpikeWaveforms4/electrodes (DynamicTableRegion) shank4 region | shape = (14,) | dtype = int64
  Group /processing/ecephys/SpikeWaveforms5 (SpikeEventSeries) no description
  Dataset /processing/ecephys/SpikeWaveforms5/electrodes (DynamicTableRegion) shank5 region | shape = (10,) | dtype = int64
  Group /processing/ecephys/SpikeWaveforms6 (SpikeEventSeries) no description
  Dataset /processing/ecephys/SpikeWaveforms6/electrodes (DynamicTableRegion) shank6 region | shape = (10,) | dtype = int64
  Group /processing/ecephys/SpikeWaveforms7 (SpikeEventSeries) no description
  Dataset /processing/ecephys/SpikeWaveforms7/electrodes (DynamicTableRegion) shank7 region | shape = (8,) | dtype = int64
  Group /processing/ecephys/SpikeWaveforms8 (SpikeEventSeries) no description
  Dataset /processing/ecephys/SpikeWaveforms8/electrodes (DynamicTableRegion) shank8 region | shape = (8,) | dtype = int64
  Group /processing/ecephys/SpikeWaveforms9 (SpikeEventSeries) no description
  Dataset /processing/ecephys/SpikeWaveforms9/electrodes (DynamicTableRegion) shank9 region | shape = (8,) | dtype = int64
  Group /processing/ecephys/SpindleDecompositionSeries (DecompositionSeries) Theta and Gamma phase for spindle-reference LFP
  Group /processing/ecephys/SpindleDecompositionSeries/bands (DynamicTable) data about the frequency bands that the signal was decomposed into
  Dataset /processing/ecephys/SpindleDecompositionSeries/bands/band_limits (VectorData) low and high frequencies of bandpass filter in Hz | shape = (2, 2) | dtype = int32
  Dataset /processing/ecephys/SpindleDecompositionSeries/bands/band_name (VectorData) the name of the frequency band (recommended: 'alpha', 'beta', 'gamma', 'delta', 'high gamma' | shape = (2,) | dtype = object
  Dataset /processing/ecephys/SpindleDecompositionSeries/bands/id (ElementIdentifiers)  | shape = (2,) | dtype = int32
  Group /processing/ecephys/SpindleDecompositionSeries/source_timeseries (ElectricalSeries) lfp signal for all shank electrodes
  Dataset /processing/ecephys/SpindleDecompositionSeries/source_timeseries/electrodes (DynamicTableRegion) electrode table reference | shape = (135,) | dtype = int32
  Group /processing/ecephys/ThetaDecompositionSeries (DecompositionSeries) Theta and Gamma phase for theta-reference LFP
  Group /processing/ecephys/ThetaDecompositionSeries/bands (DynamicTable) data about the frequency bands that the signal was decomposed into
  Dataset /processing/ecephys/ThetaDecompositionSeries/bands/band_limits (VectorData) low and high frequencies of bandpass filter in Hz | shape = (2, 2) | dtype = int32
  Dataset /processing/ecephys/ThetaDecompositionSeries/bands/band_name (VectorData) the name of the frequency band (recommended: 'alpha', 'beta', 'gamma', 'delta', 'high gamma' | shape = (2,) | dtype = object
  Dataset /processing/ecephys/ThetaDecompositionSeries/bands/id (ElementIdentifiers)  | shape = (2,) | dtype = int32
  Group /processing/ecephys/ThetaDecompositionSeries/source_timeseries (ElectricalSeries) lfp signal for all shank electrodes
  Dataset /processing/ecephys/ThetaDecompositionSeries/source_timeseries/electrodes (DynamicTableRegion) electrode table reference | shape = (135,) | dtype = int32
  Group /processing/ecephys/UPDecompositionSeries (DecompositionSeries) Theta and Gamma phase for up-reference LFP
  Group /processing/ecephys/UPDecompositionSeries/bands (DynamicTable) data about the frequency bands that the signal was decomposed into
  Dataset /processing/ecephys/UPDecompositionSeries/bands/band_limits (VectorData) low and high frequencies of bandpass filter in Hz | shape = (2, 2) | dtype = int32
  Dataset /processing/ecephys/UPDecompositionSeries/bands/band_name (VectorData) the name of the frequency band (recommended: 'alpha', 'beta', 'gamma', 'delta', 'high gamma' | shape = (2,) | dtype = object
  Dataset /processing/ecephys/UPDecompositionSeries/bands/id (ElementIdentifiers)  | shape = (2,) | dtype = int32
  Group /processing/ecephys/UPDecompositionSeries/source_timeseries (ElectricalSeries) lfp signal for all shank electrodes
  Dataset /processing/ecephys/UPDecompositionSeries/source_timeseries/electrodes (DynamicTableRegion) electrode table reference | shape = (135,) | dtype = int32
  session_description: Data was recorded using silicon probe electrodes in the frontal cortices of male Long Evans rats between 4-7 months of age. The design was to have no specific behavior, task or stimulus, rather the animal was left alone in it’s home cage (which it lives in at all times).
  session_start_time: 2013-03-24T00:00:00-04:00
  timestamps_reference_time: 2013-03-24T00:00:00-04:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/cell_type (VectorData) name of cell type | shape = (49,) | dtype = object
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (49,) | dtype = object
  Dataset /units/global_id (VectorData) global id for cell for entire experiment | shape = (49,) | dtype = int32
  Dataset /units/id (ElementIdentifiers)  | shape = (49,) | dtype = int32
  Dataset /units/region (VectorData) brain region where unit was detected | shape = (49,) | dtype = object
  Dataset /units/shank_id (VectorData) 0-indexed id of cluster from shank | shape = (49,) | dtype = int32
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (683978,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex)  | shape = (49,) | dtype = int32


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2020-10-03T14:04:34.817444-04:00']
  Group /general/devices/implant (Device) silicon probe electrodes; see BWRat20_101013.xml or BWRat20_101013.sessionInfo.mat for more information
  experimenter: ['Brendon Watson']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (64,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/rel_x (VectorData) the x coordinate within the electrode group | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_y (VectorData) the y coordinate within the electrode group | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/shank_electrode_number (VectorData) 0-indexed channel within a shank | shape = (64,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/spindle_reference (VectorData) this electrode was used to calculate slow-wave sleep | shape = (64,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/theta_reference (VectorData) this electrode was used to calculate theta canonical bands | shape = (64,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/up_reference (VectorData) this electrode was used to calculate UP-states | shape = (64,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (64,) | dtype = float64
  Group /general/extracellular_ephys/shank1 (ElectrodeGroup) shank1 electrodes
  Group /general/extracellular_ephys/shank1/device (Device) silicon probe electrodes; see BWRat20_101013.xml or BWRat20_101013.sessionInfo.mat for more information
  Group /general/extracellular_ephys/shank2 (ElectrodeGroup) shank2 electrodes
  Group /general/extracellular_ephys/shank2/device (Device) silicon probe electrodes; see BWRat20_101013.xml or BWRat20_101013.sessionInfo.mat for more information
  Group /general/extracellular_ephys/shank3 (ElectrodeGroup) shank3 electrodes
  Group /general/extracellular_ephys/shank3/device (Device) silicon probe electrodes; see BWRat20_101013.xml or BWRat20_101013.sessionInfo.mat for more information
  Group /general/extracellular_ephys/shank4 (ElectrodeGroup) shank4 electrodes
  Group /general/extracellular_ephys/shank4/device (Device) silicon probe electrodes; see BWRat20_101013.xml or BWRat20_101013.sessionInfo.mat for more information
  Group /general/extracellular_ephys/shank5 (ElectrodeGroup) shank5 electrodes
  Group /general/extracellular_ephys/shank5/device (Device) silicon probe electrodes; see BWRat20_101013.xml or BWRat20_101013.sessionInfo.mat for more information
  Group /general/extracellular_ephys/shank6 (ElectrodeGroup) shank6 electrodes
  Group /general/extracellular_ephys/shank6/device (Device) silicon probe electrodes; see BWRat20_101013.xml or BWRat20_101013.sessionInfo.mat for more information
  Group /general/extracellular_ephys/shank7 (ElectrodeGroup) shank7 electrodes
  Group /general/extracellular_ephys/shank7/device (Device) silicon probe electrodes; see BWRat20_101013.xml or BWRat20_101013.sessionInfo.mat for more information
  Group /general/extracellular_ephys/shank8 (ElectrodeGroup) shank8 electrodes
  Group /general/extracellular_ephys/shank8/device (Device) silicon probe electrodes; see BWRat20_101013.xml or BWRat20_101013.sessionInfo.mat for more information
  institution: NYU
  lab: Buzsaki
  related_publications: ['Network Homeostasis and State Dynamics of Neocortical SleepWatson BO, Levenstein D, Greene JP, Gelinas JN, Buzsáki G.Neuron. 2016 Apr 27. pii: S0896-6273(16)30056-3.doi: 10.1016/j.neuron.2016.03.036']
  session_id: BWRat20_101013
  Group /general/subject (Subject) 
  identifier: BWRat20_101013
  Group /processing/behavior (ProcessingModule) contains behavioral data
  Group /processing/behavior/states (TimeIntervals) Sleep states of animal.
  Dataset /processing/behavior/states/id (ElementIdentifiers)  | shape = (62,) | dtype = int32
  Dataset /processing/behavior/states/label (VectorData) Sleep state. | shape = (62,) | dtype = object
  Dataset /processing/behavior/states/start_time (VectorData) Start time of epoch, in seconds | shape = (62,) | dtype = float32
  Dataset /processing/behavior/states/stop_time (VectorData) Stop time of epoch, in seconds | shape = (62,) | dtype = float32
  Group /processing/ecephys (ProcessingModule) intermediate data from extracellular electrophysiology recordings, e.g., LFP
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/lfp (ElectricalSeries) lfp signal for all shank electrodes
  Dataset /processing/ecephys/LFP/lfp/electrodes (DynamicTableRegion) electrode table reference | shape = (64,) | dtype = int32
  Group /processing/ecephys/SpikeWaveforms1 (SpikeEventSeries) no description
  Dataset /processing/ecephys/SpikeWaveforms1/electrodes (DynamicTableRegion) shank1 region | shape = (8,) | dtype = int64
  Group /processing/ecephys/SpikeWaveforms2 (SpikeEventSeries) no description
  Dataset /processing/ecephys/SpikeWaveforms2/electrodes (DynamicTableRegion) shank2 region | shape = (8,) | dtype = int64
  Group /processing/ecephys/SpikeWaveforms3 (SpikeEventSeries) no description
  Dataset /processing/ecephys/SpikeWaveforms3/electrodes (DynamicTableRegion) shank3 region | shape = (8,) | dtype = int64
  Group /processing/ecephys/SpikeWaveforms4 (SpikeEventSeries) no description
  Dataset /processing/ecephys/SpikeWaveforms4/electrodes (DynamicTableRegion) shank4 region | shape = (8,) | dtype = int64
  Group /processing/ecephys/SpikeWaveforms5 (SpikeEventSeries) no description
  Dataset /processing/ecephys/SpikeWaveforms5/electrodes (DynamicTableRegion) shank5 region | shape = (8,) | dtype = int64
  Group /processing/ecephys/SpikeWaveforms6 (SpikeEventSeries) no description
  Dataset /processing/ecephys/SpikeWaveforms6/electrodes (DynamicTableRegion) shank6 region | shape = (8,) | dtype = int64
  Group /processing/ecephys/SpikeWaveforms7 (SpikeEventSeries) no description
  Dataset /processing/ecephys/SpikeWaveforms7/electrodes (DynamicTableRegion) shank7 region | shape = (8,) | dtype = int64
  Group /processing/ecephys/SpikeWaveforms8 (SpikeEventSeries) no description
  Dataset /processing/ecephys/SpikeWaveforms8/electrodes (DynamicTableRegion) shank8 region | shape = (8,) | dtype = int64
  Group /processing/ecephys/SpindleDecompositionSeries (DecompositionSeries) Theta and Gamma phase for spindle-reference LFP
  Group /processing/ecephys/SpindleDecompositionSeries/bands (DynamicTable) data about the frequency bands that the signal was decomposed into
  Dataset /processing/ecephys/SpindleDecompositionSeries/bands/band_limits (VectorData) low and high frequencies of bandpass filter in Hz | shape = (2, 2) | dtype = int32
  Dataset /processing/ecephys/SpindleDecompositionSeries/bands/band_name (VectorData) the name of the frequency band (recommended: 'alpha', 'beta', 'gamma', 'delta', 'high gamma' | shape = (2,) | dtype = object
  Dataset /processing/ecephys/SpindleDecompositionSeries/bands/id (ElementIdentifiers)  | shape = (2,) | dtype = int32
  Group /processing/ecephys/SpindleDecompositionSeries/source_timeseries (ElectricalSeries) lfp signal for all shank electrodes
  Dataset /processing/ecephys/SpindleDecompositionSeries/source_timeseries/electrodes (DynamicTableRegion) electrode table reference | shape = (64,) | dtype = int32
  Group /processing/ecephys/ThetaDecompositionSeries (DecompositionSeries) Theta and Gamma phase for theta-reference LFP
  Group /processing/ecephys/ThetaDecompositionSeries/bands (DynamicTable) data about the frequency bands that the signal was decomposed into
  Dataset /processing/ecephys/ThetaDecompositionSeries/bands/band_limits (VectorData) low and high frequencies of bandpass filter in Hz | shape = (2, 2) | dtype = int32
  Dataset /processing/ecephys/ThetaDecompositionSeries/bands/band_name (VectorData) the name of the frequency band (recommended: 'alpha', 'beta', 'gamma', 'delta', 'high gamma' | shape = (2,) | dtype = object
  Dataset /processing/ecephys/ThetaDecompositionSeries/bands/id (ElementIdentifiers)  | shape = (2,) | dtype = int32
  Group /processing/ecephys/ThetaDecompositionSeries/source_timeseries (ElectricalSeries) lfp signal for all shank electrodes
  Dataset /processing/ecephys/ThetaDecompositionSeries/source_timeseries/electrodes (DynamicTableRegion) electrode table reference | shape = (64,) | dtype = int32
  Group /processing/ecephys/UPDecompositionSeries (DecompositionSeries) Theta and Gamma phase for up-reference LFP
  Group /processing/ecephys/UPDecompositionSeries/bands (DynamicTable) data about the frequency bands that the signal was decomposed into
  Dataset /processing/ecephys/UPDecompositionSeries/bands/band_limits (VectorData) low and high frequencies of bandpass filter in Hz | shape = (2, 2) | dtype = int32
  Dataset /processing/ecephys/UPDecompositionSeries/bands/band_name (VectorData) the name of the frequency band (recommended: 'alpha', 'beta', 'gamma', 'delta', 'high gamma' | shape = (2,) | dtype = object
  Dataset /processing/ecephys/UPDecompositionSeries/bands/id (ElementIdentifiers)  | shape = (2,) | dtype = int32
  Group /processing/ecephys/UPDecompositionSeries/source_timeseries (ElectricalSeries) lfp signal for all shank electrodes
  Dataset /processing/ecephys/UPDecompositionSeries/source_timeseries/electrodes (DynamicTableRegion) electrode table reference | shape = (64,) | dtype = int32
  session_description: Data was recorded using silicon probe electrodes in the frontal cortices of male Long Evans rats between 4-7 months of age. The design was to have no specific behavior, task or stimulus, rather the animal was left alone in it’s home cage (which it lives in at all times).
  session_start_time: 2013-10-10T00:00:00-04:00
  timestamps_reference_time: 2013-10-10T00:00:00-04:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/cell_type (VectorData) name of cell type | shape = (18,) | dtype = object
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (18,) | dtype = object
  Dataset /units/global_id (VectorData) global id for cell for entire experiment | shape = (18,) | dtype = int32
  Dataset /units/id (ElementIdentifiers)  | shape = (18,) | dtype = int32
  Dataset /units/region (VectorData) brain region where unit was detected | shape = (18,) | dtype = object
  Dataset /units/shank_id (VectorData) 0-indexed id of cluster from shank | shape = (18,) | dtype = int32
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (947036,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex)  | shape = (18,) | dtype = int32


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2020-10-03T17:08:59.702940-04:00']
  Group /general/devices/implant (Device) silicon probe electrodes; see BWRat21_121113.xml or BWRat21_121113.sessionInfo.mat for more information
  experimenter: ['Brendon Watson']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (58,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (58,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (58,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (58,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (58,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (58,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/rel_x (VectorData) the x coordinate within the electrode group | shape = (58,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_y (VectorData) the y coordinate within the electrode group | shape = (58,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/shank_electrode_number (VectorData) 0-indexed channel within a shank | shape = (58,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/spindle_reference (VectorData) this electrode was used to calculate slow-wave sleep | shape = (58,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/up_reference (VectorData) this electrode was used to calculate UP-states | shape = (58,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (58,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (58,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (58,) | dtype = float64
  Group /general/extracellular_ephys/shank1 (ElectrodeGroup) shank1 electrodes
  Group /general/extracellular_ephys/shank1/device (Device) silicon probe electrodes; see BWRat21_121113.xml or BWRat21_121113.sessionInfo.mat for more information
  Group /general/extracellular_ephys/shank2 (ElectrodeGroup) shank2 electrodes
  Group /general/extracellular_ephys/shank2/device (Device) silicon probe electrodes; see BWRat21_121113.xml or BWRat21_121113.sessionInfo.mat for more information
  Group /general/extracellular_ephys/shank3 (ElectrodeGroup) shank3 electrodes
  Group /general/extracellular_ephys/shank3/device (Device) silicon probe electrodes; see BWRat21_121113.xml or BWRat21_121113.sessionInfo.mat for more information
  Group /general/extracellular_ephys/shank4 (ElectrodeGroup) shank4 electrodes
  Group /general/extracellular_ephys/shank4/device (Device) silicon probe electrodes; see BWRat21_121113.xml or BWRat21_121113.sessionInfo.mat for more information
  Group /general/extracellular_ephys/shank5 (ElectrodeGroup) shank5 electrodes
  Group /general/extracellular_ephys/shank5/device (Device) silicon probe electrodes; see BWRat21_121113.xml or BWRat21_121113.sessionInfo.mat for more information
  Group /general/extracellular_ephys/shank6 (ElectrodeGroup) shank6 electrodes
  Group /general/extracellular_ephys/shank6/device (Device) silicon probe electrodes; see BWRat21_121113.xml or BWRat21_121113.sessionInfo.mat for more information
  Group /general/extracellular_ephys/shank7 (ElectrodeGroup) shank7 electrodes
  Group /general/extracellular_ephys/shank7/device (Device) silicon probe electrodes; see BWRat21_121113.xml or BWRat21_121113.sessionInfo.mat for more information
  institution: NYU
  lab: Buzsaki
  related_publications: ['Network Homeostasis and State Dynamics of Neocortical SleepWatson BO, Levenstein D, Greene JP, Gelinas JN, Buzsáki G.Neuron. 2016 Apr 27. pii: S0896-6273(16)30056-3.doi: 10.1016/j.neuron.2016.03.036']
  session_id: BWRat21_121113
  Group /general/subject (Subject) 
  identifier: BWRat21_121113
  Group /processing/behavior (ProcessingModule) contains behavioral data
  Group /processing/behavior/states (TimeIntervals) Sleep states of animal.
  Dataset /processing/behavior/states/id (ElementIdentifiers)  | shape = (213,) | dtype = int32
  Dataset /processing/behavior/states/label (VectorData) Sleep state. | shape = (213,) | dtype = object
  Dataset /processing/behavior/states/start_time (VectorData) Start time of epoch, in seconds | shape = (213,) | dtype = float32
  Dataset /processing/behavior/states/stop_time (VectorData) Stop time of epoch, in seconds | shape = (213,) | dtype = float32
  Group /processing/ecephys (ProcessingModule) intermediate data from extracellular electrophysiology recordings, e.g., LFP
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/lfp (ElectricalSeries) lfp signal for all shank electrodes
  Dataset /processing/ecephys/LFP/lfp/electrodes (DynamicTableRegion) electrode table reference | shape = (58,) | dtype = int32
  Group /processing/ecephys/SpikeWaveforms1 (SpikeEventSeries) no description
  Dataset /processing/ecephys/SpikeWaveforms1/electrodes (DynamicTableRegion) shank1 region | shape = (8,) | dtype = int64
  Group /processing/ecephys/SpikeWaveforms2 (SpikeEventSeries) no description
  Dataset /processing/ecephys/SpikeWaveforms2/electrodes (DynamicTableRegion) shank2 region | shape = (8,) | dtype = int64
  Group /processing/ecephys/SpikeWaveforms3 (SpikeEventSeries) no description
  Dataset /processing/ecephys/SpikeWaveforms3/electrodes (DynamicTableRegion) shank3 region | shape = (8,) | dtype = int64
  Group /processing/ecephys/SpikeWaveforms4 (SpikeEventSeries) no description
  Dataset /processing/ecephys/SpikeWaveforms4/electrodes (DynamicTableRegion) shank4 region | shape = (8,) | dtype = int64
  Group /processing/ecephys/SpikeWaveforms5 (SpikeEventSeries) no description
  Dataset /processing/ecephys/SpikeWaveforms5/electrodes (DynamicTableRegion) shank5 region | shape = (8,) | dtype = int64
  Group /processing/ecephys/SpikeWaveforms6 (SpikeEventSeries) no description
  Dataset /processing/ecephys/SpikeWaveforms6/electrodes (DynamicTableRegion) shank6 region | shape = (8,) | dtype = int64
  Group /processing/ecephys/SpikeWaveforms7 (SpikeEventSeries) no description
  Dataset /processing/ecephys/SpikeWaveforms7/electrodes (DynamicTableRegion) shank7 region | shape = (10,) | dtype = int64
  Group /processing/ecephys/SpindleDecompositionSeries (DecompositionSeries) Theta and Gamma phase for spindle-reference LFP
  Group /processing/ecephys/SpindleDecompositionSeries/bands (DynamicTable) data about the frequency bands that the signal was decomposed into
  Dataset /processing/ecephys/SpindleDecompositionSeries/bands/band_limits (VectorData) low and high frequencies of bandpass filter in Hz | shape = (2, 2) | dtype = int32
  Dataset /processing/ecephys/SpindleDecompositionSeries/bands/band_name (VectorData) the name of the frequency band (recommended: 'alpha', 'beta', 'gamma', 'delta', 'high gamma' | shape = (2,) | dtype = object
  Dataset /processing/ecephys/SpindleDecompositionSeries/bands/id (ElementIdentifiers)  | shape = (2,) | dtype = int32
  Group /processing/ecephys/SpindleDecompositionSeries/source_timeseries (ElectricalSeries) lfp signal for all shank electrodes
  Dataset /processing/ecephys/SpindleDecompositionSeries/source_timeseries/electrodes (DynamicTableRegion) electrode table reference | shape = (58,) | dtype = int32
  Group /processing/ecephys/UPDecompositionSeries (DecompositionSeries) Theta and Gamma phase for up-reference LFP
  Group /processing/ecephys/UPDecompositionSeries/bands (DynamicTable) data about the frequency bands that the signal was decomposed into
  Dataset /processing/ecephys/UPDecompositionSeries/bands/band_limits (VectorData) low and high frequencies of bandpass filter in Hz | shape = (2, 2) | dtype = int32
  Dataset /processing/ecephys/UPDecompositionSeries/bands/band_name (VectorData) the name of the frequency band (recommended: 'alpha', 'beta', 'gamma', 'delta', 'high gamma' | shape = (2,) | dtype = object
  Dataset /processing/ecephys/UPDecompositionSeries/bands/id (ElementIdentifiers)  | shape = (2,) | dtype = int32
  Group /processing/ecephys/UPDecompositionSeries/source_timeseries (ElectricalSeries) lfp signal for all shank electrodes
  Dataset /processing/ecephys/UPDecompositionSeries/source_timeseries/electrodes (DynamicTableRegion) electrode table reference | shape = (58,) | dtype = int32
  session_description: Data was recorded using silicon probe electrodes in the frontal cortices of male Long Evans rats between 4-7 months of age. The design was to have no specific behavior, task or stimulus, rather the animal was left alone in it’s home cage (which it lives in at all times).
  session_start_time: 2013-12-11T00:00:00-05:00
  timestamps_reference_time: 2013-12-11T00:00:00-05:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/cell_type (VectorData) name of cell type | shape = (32,) | dtype = object
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (32,) | dtype = object
  Dataset /units/global_id (VectorData) global id for cell for entire experiment | shape = (32,) | dtype = int32
  Dataset /units/id (ElementIdentifiers)  | shape = (32,) | dtype = int32
  Dataset /units/region (VectorData) brain region where unit was detected | shape = (32,) | dtype = object
  Dataset /units/shank_id (VectorData) 0-indexed id of cluster from shank | shape = (32,) | dtype = int32
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (976450,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex)  | shape = (32,) | dtype = int32
