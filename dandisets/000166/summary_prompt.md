
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000166/0.220116.2037
name: Layer-Specific Physiological Features and Interlaminar Interactions in the Primary Visual Cortex of the Mouse
contributor: [{'name': 'Senzai, Yuta', 'roleName': ['dcite:ContactPerson', 'dcite:Author', 'dcite:DataCollector', 'dcite:FormalAnalysis'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Fernandez-Ruiz, Antonio', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Buzsáki, György', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'url': 'http://hnf.jp/', 'name': 'Heiwa Nakajima Foundation', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/000k40t10', 'contactPoint': [], 'includeInCitation': False}, {'url': 'http://www.nih.gov/', 'name': 'National Institutes of Health', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01cwqze88', 'awardNumber': 'MH54671,  MH107396, NS090583', 'contactPoint': [], 'includeInCitation': False}, {'url': 'http://www.nsf.gov/', 'name': 'National Science Foundation', 'email': 'info@nsf.gov', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/021nxhr62', 'awardNumber': '1545858, 1707316', 'contactPoint': [], 'includeInCitation': False}, {'url': 'http://www.wellcome.ac.uk/', 'name': 'Wellcome Trust', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/029chgv08', 'contactPoint': [], 'includeInCitation': False}]
description: The relationship between mesoscopic local field potentials (LFPs) and single-neuron firing in the multi-layered neocortex is poorly understood. Simultaneous recordings from all layers in the primary visual cortex (V1) of the behaving mouse revealed functionally defined layers in V1. The depth of maximum spike power and sink-source distributions of LFPs provided consistent laminar landmarks across animals. Coherence of gamma oscillations (30-100 Hz) and spike-LFP coupling identified six physiological layers and further sublayers. Firing rates, burstiness, and other electrophysiological features of neurons displayed unique layer and brain state dependence. Spike transmission strength from layer 2/3 cells to layer 5 pyramidal cells and interneurons was stronger during waking compared with non-REM sleep but stronger during non-REM sleep among deep-layer excitatory neurons. A subset of deep-layer neurons was active exclusively in the DOWN state of non-REM sleep. These results bridge mesoscopic LFPs and single-neuron interactions with laminar structure in V1.
assetsSummary: {'species': [{'name': 'House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 787191910918, 'numberOfFiles': 19, 'numberOfSubjects': 19, 'variableMeasured': ['ElectrodeGroup', 'Units', 'LFP'], 'measurementTechnique': [{'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'signal filtering technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000166 has 19 NWB files.
3 of these NWB files are of type 1.
1 of these NWB files are of type 2.
2 of these NWB files are of type 3.
12 of these NWB files are of type 4.
1 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeries (ElectricalSeries) Raw acquisition traces.
  Dataset /acquisition/ElectricalSeries/electrodes (DynamicTableRegion) electrode_table_region | shape = (64,) | dtype = int64
  file_create_date: ['2021-11-07T16:28:07.926605+00:00']
  Group /general/devices/Device_ecephys (Device) Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  experiment_description: The relationship between mesoscopic local field potentials (LFPs) and single-neuron firing in the multi-layered neocortex is poorly understood. Simultaneous recordings from all layers in the primary visual cortex (V1) of the behaving mouse revealed functionally defined layers in V1. The depth of maximum spike power and sink-source distributions of LFPs provided consistent laminar landmarks across animals. Coherence of gamma oscillations (30–100 Hz) and spike-LFP coupling identified six physiological layers and further sublayers. Firing rates, burstiness, and other electrophysiological features of neurons displayed unique layer and brain state dependence. Spike transmission strength from layer 2/3 cells to layer 5 pyramidal cells and interneurons was stronger during waking compared with non-REM sleep but stronger during non-REM sleep among deep-layer excitatory neurons. A subset of deep-layer neurons was active exclusively in the DOWN state of non-REM sleep. These results bridge mesoscopic LFPs and single-neuron interactions with laminar structure in V1.
  experimenter: ['Yuta Senzai']
  Group /general/extracellular_ephys/Group1 (ElectrodeGroup) Group1 electrodes.
  Group /general/extracellular_ephys/Group1/device (Device) Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/gain (VectorData) gain | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (64,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/offset (VectorData) offset | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_x (VectorData) the x coordinate within the electrode group | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_y (VectorData) the y coordinate within the electrode group | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/shank_electrode_number (VectorData) 0-indexed channel within a shank. | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (64,) | dtype = float64
  institution: NYU
  lab: Buzsaki
  related_publications: ['Senzai, Y., Fernandez-Ruiz, A., & Buzsáki, G. (2019). Layer-specific physiological features and interlaminar interactions in the primary visual cortex of the mouse. Neuron, 101(3), 500-513.']
  session_id: YMV01_170818
  Group /general/subject (Subject) 
  identifier: 4956f7b1-8370-4dfa-8630-7ae66759aebd
  Group /processing/Neural states (ProcessingModule) Contains behavioral data concerning classified states.
  Group /processing/Neural states/Sleep states (TimeIntervals) Sleep state of the animal.
  Dataset /processing/Neural states/Sleep states/id (ElementIdentifiers)  | shape = (30,) | dtype = int64
  Dataset /processing/Neural states/Sleep states/label (VectorData) Sleep state. | shape = (30,) | dtype = object
  Dataset /processing/Neural states/Sleep states/start_time (VectorData) Start time of epoch, in seconds | shape = (30,) | dtype = float64
  Dataset /processing/Neural states/Sleep states/stop_time (VectorData) Stop time of epoch, in seconds | shape = (30,) | dtype = float64
  Group /processing/Neural states/Up-Down states (TimeIntervals) Up and down states classified by LFP.
  Dataset /processing/Neural states/Up-Down states/id (ElementIdentifiers)  | shape = (3018,) | dtype = int64
  Dataset /processing/Neural states/Up-Down states/label (VectorData) state. | shape = (3018,) | dtype = object
  Dataset /processing/Neural states/Up-Down states/start_time (VectorData) Start time of epoch, in seconds | shape = (3018,) | dtype = float64
  Dataset /processing/Neural states/Up-Down states/stop_time (VectorData) Stop time of epoch, in seconds | shape = (3018,) | dtype = float64
  Group /processing/ecephys (ProcessingModule) Intermediate data from extracellular electrophysiology recordings, e.g., LFP.
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/LFP (ElectricalSeries) Local field potential signal.
  Dataset /processing/ecephys/LFP/LFP/electrodes (DynamicTableRegion) electrode_table_region | shape = (64,) | dtype = int64
  session_description: The relationship between mesoscopic local field potentials (LFPs) and single-neuron firing in the multi-layered neocortex is poorly understood. Simultaneous recordings from all layers in the primary visual cortex (V1) of the behaving mouse revealed functionally defined layers in V1. The depth of maximum spike power and sink-source distributions of LFPs provided consistent laminar landmarks across animals. Coherence of gamma oscillations (30–100 Hz) and spike-LFP coupling identified six physiological layers and further sublayers. Firing rates, burstiness, and other electrophysiological features of neurons displayed unique layer and brain state dependence. Spike transmission strength from layer 2/3 cells to layer 5 pyramidal cells and interneurons was stronger during waking compared with non-REM sleep but stronger during non-REM sleep among deep-layer excitatory neurons. A subset of deep-layer neurons was active exclusively in the DOWN state of non-REM sleep. These results bridge mesoscopic LFPs and single-neuron interactions with laminar structure in V1. Subjects were between 3 and 8 months of age.
  session_start_time: 2017-08-18T00:00:00-04:00
  timestamps_reference_time: 2017-08-18T00:00:00-04:00
  Group /units (Units) Autogenerated by nwb_conversion_tools.
  Dataset /units/ab_ratio (VectorData) AB ratio for the unit. | shape = (53,) | dtype = float64
  Dataset /units/amplitudes (VectorData) no description | shape = (1319077,) | dtype = float64
  Dataset /units/amplitudes_index (VectorIndex) Index for VectorData 'amplitudes' | shape = (53,) | dtype = uint32
  Dataset /units/brain_region (VectorData) Assigned brain region where the unit is located. | shape = (53,) | dtype = object
  Dataset /units/cell_type (VectorData) Classification of the cell type. | shape = (53,) | dtype = object
  Dataset /units/coefficient_of_variation (VectorData) Coefficient of variation for the unit activity. | shape = (53,) | dtype = float64
  Dataset /units/firing_rate (VectorData) Average firing rate of the unit. | shape = (53,) | dtype = float64
  Dataset /units/id (ElementIdentifiers)  | shape = (53,) | dtype = int64
  Dataset /units/max_channel (DynamicTableRegion) Channel that observed the maximum waveform amplitude for the unit. | shape = (53,) | dtype = int32
  Dataset /units/pc_features (VectorData) no description | shape = (1319077, 3, 12) | dtype = float32
  Dataset /units/pc_features_index (VectorIndex) Index for VectorData 'pc_features' | shape = (53,) | dtype = uint32
  Dataset /units/peak_voltage (VectorData) Magnitude of peak voltage for the unit. | shape = (53,) | dtype = float64
  Dataset /units/polarity (VectorData) Polarity of the unit. | shape = (53,) | dtype = float64
  Dataset /units/quality (VectorData) Quality of the unit as defined by phy (good, mua, noise). | shape = (53,) | dtype = object
  Dataset /units/refractory_period_violation (VectorData) Score for the violation of the refractory period. | shape = (53,) | dtype = float64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (1319077,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (53,) | dtype = uint32
  Dataset /units/synaptic_effect (VectorData) Classification of the synaptic effect (excitatory or inhibitory). Unknown if undetermined. | shape = (53,) | dtype = object
  Dataset /units/theta_modulation_index (VectorData) Index of theta modulation. | shape = (53,) | dtype = float64


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeries (ElectricalSeries) Raw acquisition traces.
  Dataset /acquisition/ElectricalSeries/electrodes (DynamicTableRegion) electrode_table_region | shape = (64,) | dtype = int64
  file_create_date: ['2021-11-07T16:28:36.827925+00:00']
  Group /general/devices/Device_ecephys (Device) Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  experiment_description: The relationship between mesoscopic local field potentials (LFPs) and single-neuron firing in the multi-layered neocortex is poorly understood. Simultaneous recordings from all layers in the primary visual cortex (V1) of the behaving mouse revealed functionally defined layers in V1. The depth of maximum spike power and sink-source distributions of LFPs provided consistent laminar landmarks across animals. Coherence of gamma oscillations (30–100 Hz) and spike-LFP coupling identified six physiological layers and further sublayers. Firing rates, burstiness, and other electrophysiological features of neurons displayed unique layer and brain state dependence. Spike transmission strength from layer 2/3 cells to layer 5 pyramidal cells and interneurons was stronger during waking compared with non-REM sleep but stronger during non-REM sleep among deep-layer excitatory neurons. A subset of deep-layer neurons was active exclusively in the DOWN state of non-REM sleep. These results bridge mesoscopic LFPs and single-neuron interactions with laminar structure in V1.
  experimenter: ['Yuta Senzai']
  Group /general/extracellular_ephys/Group1 (ElectrodeGroup) Group1 electrodes.
  Group /general/extracellular_ephys/Group1/device (Device) Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/gain (VectorData) gain | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (64,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/offset (VectorData) offset | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_x (VectorData) the x coordinate within the electrode group | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_y (VectorData) the y coordinate within the electrode group | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/shank_electrode_number (VectorData) 0-indexed channel within a shank. | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (64,) | dtype = float64
  institution: NYU
  lab: Buzsaki
  related_publications: ['Senzai, Y., Fernandez-Ruiz, A., & Buzsáki, G. (2019). Layer-specific physiological features and interlaminar interactions in the primary visual cortex of the mouse. Neuron, 101(3), 500-513.']
  session_id: YMV03_170818
  Group /general/subject (Subject) 
  identifier: 494cb7b4-6097-4b2f-bcc7-253344048ab0
  Group /processing/Neural states (ProcessingModule) Contains behavioral data concerning classified states.
  Group /processing/Neural states/Sleep states (TimeIntervals) Sleep state of the animal.
  Dataset /processing/Neural states/Sleep states/id (ElementIdentifiers)  | shape = (69,) | dtype = int64
  Dataset /processing/Neural states/Sleep states/label (VectorData) Sleep state. | shape = (69,) | dtype = object
  Dataset /processing/Neural states/Sleep states/start_time (VectorData) Start time of epoch, in seconds | shape = (69,) | dtype = float64
  Dataset /processing/Neural states/Sleep states/stop_time (VectorData) Stop time of epoch, in seconds | shape = (69,) | dtype = float64
  Group /processing/Neural states/Up-Down states (TimeIntervals) Up and down states classified by LFP.
  Dataset /processing/Neural states/Up-Down states/id (ElementIdentifiers)  | shape = (11860,) | dtype = int64
  Dataset /processing/Neural states/Up-Down states/label (VectorData) state. | shape = (11860,) | dtype = object
  Dataset /processing/Neural states/Up-Down states/start_time (VectorData) Start time of epoch, in seconds | shape = (11860,) | dtype = float64
  Dataset /processing/Neural states/Up-Down states/stop_time (VectorData) Stop time of epoch, in seconds | shape = (11860,) | dtype = float64
  Group /processing/ecephys (ProcessingModule) Intermediate data from extracellular electrophysiology recordings, e.g., LFP.
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/LFP (ElectricalSeries) Local field potential signal.
  Dataset /processing/ecephys/LFP/LFP/electrodes (DynamicTableRegion) electrode_table_region | shape = (64,) | dtype = int64
  session_description: The relationship between mesoscopic local field potentials (LFPs) and single-neuron firing in the multi-layered neocortex is poorly understood. Simultaneous recordings from all layers in the primary visual cortex (V1) of the behaving mouse revealed functionally defined layers in V1. The depth of maximum spike power and sink-source distributions of LFPs provided consistent laminar landmarks across animals. Coherence of gamma oscillations (30–100 Hz) and spike-LFP coupling identified six physiological layers and further sublayers. Firing rates, burstiness, and other electrophysiological features of neurons displayed unique layer and brain state dependence. Spike transmission strength from layer 2/3 cells to layer 5 pyramidal cells and interneurons was stronger during waking compared with non-REM sleep but stronger during non-REM sleep among deep-layer excitatory neurons. A subset of deep-layer neurons was active exclusively in the DOWN state of non-REM sleep. These results bridge mesoscopic LFPs and single-neuron interactions with laminar structure in V1. Subjects were between 3 and 8 months of age.
  session_start_time: 2017-08-18T00:00:00-04:00
  timestamps_reference_time: 2017-08-18T00:00:00-04:00
  Group /units (Units) Autogenerated by nwb_conversion_tools.
  Dataset /units/amplitudes (VectorData) no description | shape = (3597835,) | dtype = float64
  Dataset /units/amplitudes_index (VectorIndex) Index for VectorData 'amplitudes' | shape = (116,) | dtype = uint32
  Dataset /units/id (ElementIdentifiers)  | shape = (116,) | dtype = int64
  Dataset /units/pc_features (VectorData) no description | shape = (3597835, 3, 12) | dtype = float32
  Dataset /units/pc_features_index (VectorIndex) Index for VectorData 'pc_features' | shape = (116,) | dtype = uint32
  Dataset /units/quality (VectorData) Quality of the unit as defined by phy (good, mua, noise). | shape = (116,) | dtype = object
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (3597835,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (116,) | dtype = uint32


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeries (ElectricalSeries) Raw acquisition traces.
  Dataset /acquisition/ElectricalSeries/electrodes (DynamicTableRegion) electrode_table_region | shape = (64,) | dtype = int64
  file_create_date: ['2021-11-07T16:28:57.811093+00:00']
  Group /general/devices/Device_ecephys (Device) Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  experiment_description: The relationship between mesoscopic local field potentials (LFPs) and single-neuron firing in the multi-layered neocortex is poorly understood. Simultaneous recordings from all layers in the primary visual cortex (V1) of the behaving mouse revealed functionally defined layers in V1. The depth of maximum spike power and sink-source distributions of LFPs provided consistent laminar landmarks across animals. Coherence of gamma oscillations (30–100 Hz) and spike-LFP coupling identified six physiological layers and further sublayers. Firing rates, burstiness, and other electrophysiological features of neurons displayed unique layer and brain state dependence. Spike transmission strength from layer 2/3 cells to layer 5 pyramidal cells and interneurons was stronger during waking compared with non-REM sleep but stronger during non-REM sleep among deep-layer excitatory neurons. A subset of deep-layer neurons was active exclusively in the DOWN state of non-REM sleep. These results bridge mesoscopic LFPs and single-neuron interactions with laminar structure in V1.
  experimenter: ['Yuta Senzai']
  Group /general/extracellular_ephys/Group1 (ElectrodeGroup) Group1 electrodes.
  Group /general/extracellular_ephys/Group1/device (Device) Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/gain (VectorData) gain | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (64,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/offset (VectorData) offset | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_x (VectorData) the x coordinate within the electrode group | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_y (VectorData) the y coordinate within the electrode group | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/shank_electrode_number (VectorData) 0-indexed channel within a shank. | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (64,) | dtype = float64
  institution: NYU
  lab: Buzsaki
  related_publications: ['Senzai, Y., Fernandez-Ruiz, A., & Buzsáki, G. (2019). Layer-specific physiological features and interlaminar interactions in the primary visual cortex of the mouse. Neuron, 101(3), 500-513.']
  session_id: YMV05_170912
  Group /general/subject (Subject) 
  identifier: ce6b60aa-19c4-4301-910f-f5b6b1f5a3df
  Group /processing/Neural states (ProcessingModule) Contains behavioral data concerning classified states.
  Group /processing/Neural states/Laser diode (TimeIntervals) Laser pulses for optogenetics.
  Dataset /processing/Neural states/Laser diode/amplitude (VectorData) Amplitude of the laser pulse. | shape = (1488, 1) | dtype = float64
  Dataset /processing/Neural states/Laser diode/id (ElementIdentifiers)  | shape = (1488,) | dtype = int64
  Dataset /processing/Neural states/Laser diode/start_time (VectorData) Start time of epoch, in seconds | shape = (1488,) | dtype = float64
  Dataset /processing/Neural states/Laser diode/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1488,) | dtype = float64
  Group /processing/Neural states/Sleep states (TimeIntervals) Sleep state of the animal.
  Dataset /processing/Neural states/Sleep states/id (ElementIdentifiers)  | shape = (35,) | dtype = int64
  Dataset /processing/Neural states/Sleep states/label (VectorData) Sleep state. | shape = (35,) | dtype = object
  Dataset /processing/Neural states/Sleep states/start_time (VectorData) Start time of epoch, in seconds | shape = (35,) | dtype = float64
  Dataset /processing/Neural states/Sleep states/stop_time (VectorData) Stop time of epoch, in seconds | shape = (35,) | dtype = float64
  Group /processing/Neural states/Up-Down states (TimeIntervals) Up and down states classified by LFP.
  Dataset /processing/Neural states/Up-Down states/id (ElementIdentifiers)  | shape = (4896,) | dtype = int64
  Dataset /processing/Neural states/Up-Down states/label (VectorData) state. | shape = (4896,) | dtype = object
  Dataset /processing/Neural states/Up-Down states/start_time (VectorData) Start time of epoch, in seconds | shape = (4896,) | dtype = float64
  Dataset /processing/Neural states/Up-Down states/stop_time (VectorData) Stop time of epoch, in seconds | shape = (4896,) | dtype = float64
  Group /processing/Neural states/Visual laser (TimeIntervals) Laser pulses for subject stimulation.
  Dataset /processing/Neural states/Visual laser/amplitude (VectorData) Amplitude of the laser pulse. | shape = (1988, 1) | dtype = float64
  Dataset /processing/Neural states/Visual laser/id (ElementIdentifiers)  | shape = (1988,) | dtype = int64
  Dataset /processing/Neural states/Visual laser/start_time (VectorData) Start time of epoch, in seconds | shape = (1988,) | dtype = float64
  Dataset /processing/Neural states/Visual laser/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1988,) | dtype = float64
  Group /processing/ecephys (ProcessingModule) Intermediate data from extracellular electrophysiology recordings, e.g., LFP.
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/LFP (ElectricalSeries) Local field potential signal.
  Dataset /processing/ecephys/LFP/LFP/electrodes (DynamicTableRegion) electrode_table_region | shape = (64,) | dtype = int64
  session_description: The relationship between mesoscopic local field potentials (LFPs) and single-neuron firing in the multi-layered neocortex is poorly understood. Simultaneous recordings from all layers in the primary visual cortex (V1) of the behaving mouse revealed functionally defined layers in V1. The depth of maximum spike power and sink-source distributions of LFPs provided consistent laminar landmarks across animals. Coherence of gamma oscillations (30–100 Hz) and spike-LFP coupling identified six physiological layers and further sublayers. Firing rates, burstiness, and other electrophysiological features of neurons displayed unique layer and brain state dependence. Spike transmission strength from layer 2/3 cells to layer 5 pyramidal cells and interneurons was stronger during waking compared with non-REM sleep but stronger during non-REM sleep among deep-layer excitatory neurons. A subset of deep-layer neurons was active exclusively in the DOWN state of non-REM sleep. These results bridge mesoscopic LFPs and single-neuron interactions with laminar structure in V1. Subjects were between 3 and 8 months of age.
  session_start_time: 2017-09-12T00:00:00-04:00
  timestamps_reference_time: 2017-09-12T00:00:00-04:00
  Group /units (Units) Autogenerated by nwb_conversion_tools.
  Dataset /units/ab_ratio (VectorData) AB ratio for the unit. | shape = (72,) | dtype = float64
  Dataset /units/amplitudes (VectorData) no description | shape = (4388284,) | dtype = float64
  Dataset /units/amplitudes_index (VectorIndex) Index for VectorData 'amplitudes' | shape = (72,) | dtype = uint32
  Dataset /units/brain_region (VectorData) Assigned brain region where the unit is located. | shape = (72,) | dtype = object
  Dataset /units/cell_type (VectorData) Classification of the cell type. | shape = (72,) | dtype = object
  Dataset /units/coefficient_of_variation (VectorData) Coefficient of variation for the unit activity. | shape = (72,) | dtype = float64
  Dataset /units/firing_rate (VectorData) Average firing rate of the unit. | shape = (72,) | dtype = float64
  Dataset /units/id (ElementIdentifiers)  | shape = (72,) | dtype = int64
  Dataset /units/max_channel (DynamicTableRegion) Channel that observed the maximum waveform amplitude for the unit. | shape = (72,) | dtype = int32
  Dataset /units/pc_features (VectorData) no description | shape = (4388284, 3, 12) | dtype = float32
  Dataset /units/pc_features_index (VectorIndex) Index for VectorData 'pc_features' | shape = (72,) | dtype = uint32
  Dataset /units/peak_voltage (VectorData) Magnitude of peak voltage for the unit. | shape = (72,) | dtype = float64
  Dataset /units/polarity (VectorData) Polarity of the unit. | shape = (72,) | dtype = float64
  Dataset /units/quality (VectorData) Quality of the unit as defined by phy (good, mua, noise). | shape = (72,) | dtype = object
  Dataset /units/refractory_period_violation (VectorData) Score for the violation of the refractory period. | shape = (72,) | dtype = float64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (4388284,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (72,) | dtype = uint32
  Dataset /units/synaptic_effect (VectorData) Classification of the synaptic effect (excitatory or inhibitory). Unknown if undetermined. | shape = (72,) | dtype = object
  Dataset /units/theta_modulation_index (VectorData) Index of theta modulation. | shape = (72,) | dtype = float64


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeries (ElectricalSeries) Raw acquisition traces.
  Dataset /acquisition/ElectricalSeries/electrodes (DynamicTableRegion) electrode_table_region | shape = (64,) | dtype = int64
  file_create_date: ['2021-11-07T16:28:47.604104+00:00']
  Group /general/devices/Device_ecephys (Device) Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  experiment_description: The relationship between mesoscopic local field potentials (LFPs) and single-neuron firing in the multi-layered neocortex is poorly understood. Simultaneous recordings from all layers in the primary visual cortex (V1) of the behaving mouse revealed functionally defined layers in V1. The depth of maximum spike power and sink-source distributions of LFPs provided consistent laminar landmarks across animals. Coherence of gamma oscillations (30–100 Hz) and spike-LFP coupling identified six physiological layers and further sublayers. Firing rates, burstiness, and other electrophysiological features of neurons displayed unique layer and brain state dependence. Spike transmission strength from layer 2/3 cells to layer 5 pyramidal cells and interneurons was stronger during waking compared with non-REM sleep but stronger during non-REM sleep among deep-layer excitatory neurons. A subset of deep-layer neurons was active exclusively in the DOWN state of non-REM sleep. These results bridge mesoscopic LFPs and single-neuron interactions with laminar structure in V1.
  experimenter: ['Yuta Senzai']
  Group /general/extracellular_ephys/Group1 (ElectrodeGroup) Group1 electrodes.
  Group /general/extracellular_ephys/Group1/device (Device) Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/gain (VectorData) gain | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (64,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/offset (VectorData) offset | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_x (VectorData) the x coordinate within the electrode group | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_y (VectorData) the y coordinate within the electrode group | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/shank_electrode_number (VectorData) 0-indexed channel within a shank. | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (64,) | dtype = float64
  institution: NYU
  lab: Buzsaki
  related_publications: ['Senzai, Y., Fernandez-Ruiz, A., & Buzsáki, G. (2019). Layer-specific physiological features and interlaminar interactions in the primary visual cortex of the mouse. Neuron, 101(3), 500-513.']
  session_id: YMV06_170913
  Group /general/subject (Subject) 
  identifier: 32a8df91-60f0-4c73-8258-7aa770c89837
  Group /processing/Neural states (ProcessingModule) Contains behavioral data concerning classified states.
  Group /processing/Neural states/Laser diode (TimeIntervals) Laser pulses for optogenetics.
  Dataset /processing/Neural states/Laser diode/amplitude (VectorData) Amplitude of the laser pulse. | shape = (1488, 1) | dtype = float64
  Dataset /processing/Neural states/Laser diode/id (ElementIdentifiers)  | shape = (1488,) | dtype = int64
  Dataset /processing/Neural states/Laser diode/start_time (VectorData) Start time of epoch, in seconds | shape = (1488,) | dtype = float64
  Dataset /processing/Neural states/Laser diode/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1488,) | dtype = float64
  Group /processing/Neural states/Sleep states (TimeIntervals) Sleep state of the animal.
  Dataset /processing/Neural states/Sleep states/id (ElementIdentifiers)  | shape = (63,) | dtype = int64
  Dataset /processing/Neural states/Sleep states/label (VectorData) Sleep state. | shape = (63,) | dtype = object
  Dataset /processing/Neural states/Sleep states/start_time (VectorData) Start time of epoch, in seconds | shape = (63,) | dtype = float64
  Dataset /processing/Neural states/Sleep states/stop_time (VectorData) Stop time of epoch, in seconds | shape = (63,) | dtype = float64
  Group /processing/Neural states/Up-Down states (TimeIntervals) Up and down states classified by LFP.
  Dataset /processing/Neural states/Up-Down states/id (ElementIdentifiers)  | shape = (21993,) | dtype = int64
  Dataset /processing/Neural states/Up-Down states/label (VectorData) state. | shape = (21993,) | dtype = object
  Dataset /processing/Neural states/Up-Down states/start_time (VectorData) Start time of epoch, in seconds | shape = (21993,) | dtype = float64
  Dataset /processing/Neural states/Up-Down states/stop_time (VectorData) Stop time of epoch, in seconds | shape = (21993,) | dtype = float64
  Group /processing/ecephys (ProcessingModule) Intermediate data from extracellular electrophysiology recordings, e.g., LFP.
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/LFP (ElectricalSeries) Local field potential signal.
  Dataset /processing/ecephys/LFP/LFP/electrodes (DynamicTableRegion) electrode_table_region | shape = (64,) | dtype = int64
  session_description: The relationship between mesoscopic local field potentials (LFPs) and single-neuron firing in the multi-layered neocortex is poorly understood. Simultaneous recordings from all layers in the primary visual cortex (V1) of the behaving mouse revealed functionally defined layers in V1. The depth of maximum spike power and sink-source distributions of LFPs provided consistent laminar landmarks across animals. Coherence of gamma oscillations (30–100 Hz) and spike-LFP coupling identified six physiological layers and further sublayers. Firing rates, burstiness, and other electrophysiological features of neurons displayed unique layer and brain state dependence. Spike transmission strength from layer 2/3 cells to layer 5 pyramidal cells and interneurons was stronger during waking compared with non-REM sleep but stronger during non-REM sleep among deep-layer excitatory neurons. A subset of deep-layer neurons was active exclusively in the DOWN state of non-REM sleep. These results bridge mesoscopic LFPs and single-neuron interactions with laminar structure in V1. Subjects were between 3 and 8 months of age.
  session_start_time: 2017-09-13T00:00:00-04:00
  timestamps_reference_time: 2017-09-13T00:00:00-04:00
  Group /units (Units) Autogenerated by nwb_conversion_tools.
  Dataset /units/ab_ratio (VectorData) AB ratio for the unit. | shape = (73,) | dtype = float64
  Dataset /units/amplitudes (VectorData) no description | shape = (3869645,) | dtype = float64
  Dataset /units/amplitudes_index (VectorIndex) Index for VectorData 'amplitudes' | shape = (73,) | dtype = uint32
  Dataset /units/brain_region (VectorData) Assigned brain region where the unit is located. | shape = (73,) | dtype = object
  Dataset /units/cell_type (VectorData) Classification of the cell type. | shape = (73,) | dtype = object
  Dataset /units/coefficient_of_variation (VectorData) Coefficient of variation for the unit activity. | shape = (73,) | dtype = float64
  Dataset /units/firing_rate (VectorData) Average firing rate of the unit. | shape = (73,) | dtype = float64
  Dataset /units/id (ElementIdentifiers)  | shape = (73,) | dtype = int64
  Dataset /units/max_channel (DynamicTableRegion) Channel that observed the maximum waveform amplitude for the unit. | shape = (73,) | dtype = int32
  Dataset /units/pc_features (VectorData) no description | shape = (3869645, 3, 12) | dtype = float32
  Dataset /units/pc_features_index (VectorIndex) Index for VectorData 'pc_features' | shape = (73,) | dtype = uint32
  Dataset /units/peak_voltage (VectorData) Magnitude of peak voltage for the unit. | shape = (73,) | dtype = float64
  Dataset /units/polarity (VectorData) Polarity of the unit. | shape = (73,) | dtype = float64
  Dataset /units/quality (VectorData) Quality of the unit as defined by phy (good, mua, noise). | shape = (73,) | dtype = object
  Dataset /units/refractory_period_violation (VectorData) Score for the violation of the refractory period. | shape = (73,) | dtype = float64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (3869645,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (73,) | dtype = uint32
  Dataset /units/synaptic_effect (VectorData) Classification of the synaptic effect (excitatory or inhibitory). Unknown if undetermined. | shape = (73,) | dtype = object
  Dataset /units/theta_modulation_index (VectorData) Index of theta modulation. | shape = (73,) | dtype = float64


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeries (ElectricalSeries) Raw acquisition traces.
  Dataset /acquisition/ElectricalSeries/electrodes (DynamicTableRegion) electrode_table_region | shape = (64,) | dtype = int64
  file_create_date: ['2021-11-07T16:29:18.773714+00:00']
  Group /general/devices/Device_ecephys (Device) Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  experiment_description: The relationship between mesoscopic local field potentials (LFPs) and single-neuron firing in the multi-layered neocortex is poorly understood. Simultaneous recordings from all layers in the primary visual cortex (V1) of the behaving mouse revealed functionally defined layers in V1. The depth of maximum spike power and sink-source distributions of LFPs provided consistent laminar landmarks across animals. Coherence of gamma oscillations (30–100 Hz) and spike-LFP coupling identified six physiological layers and further sublayers. Firing rates, burstiness, and other electrophysiological features of neurons displayed unique layer and brain state dependence. Spike transmission strength from layer 2/3 cells to layer 5 pyramidal cells and interneurons was stronger during waking compared with non-REM sleep but stronger during non-REM sleep among deep-layer excitatory neurons. A subset of deep-layer neurons was active exclusively in the DOWN state of non-REM sleep. These results bridge mesoscopic LFPs and single-neuron interactions with laminar structure in V1.
  experimenter: ['Yuta Senzai']
  Group /general/extracellular_ephys/Group1 (ElectrodeGroup) Group1 electrodes.
  Group /general/extracellular_ephys/Group1/device (Device) Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/gain (VectorData) gain | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (64,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/offset (VectorData) offset | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_x (VectorData) the x coordinate within the electrode group | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_y (VectorData) the y coordinate within the electrode group | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/shank_electrode_number (VectorData) 0-indexed channel within a shank. | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (64,) | dtype = float64
  institution: NYU
  lab: Buzsaki
  related_publications: ['Senzai, Y., Fernandez-Ruiz, A., & Buzsáki, G. (2019). Layer-specific physiological features and interlaminar interactions in the primary visual cortex of the mouse. Neuron, 101(3), 500-513.']
  session_id: YMV19_180209
  Group /general/subject (Subject) 
  identifier: 1263acff-c4b9-4609-b13e-7fd03dfc01f0
  Group /processing/Neural states (ProcessingModule) Contains behavioral data concerning classified states.
  Group /processing/Neural states/Laser diode (TimeIntervals) Laser pulses for optogenetics.
  Dataset /processing/Neural states/Laser diode/amplitude (VectorData) Amplitude of the laser pulse. | shape = (1488, 1) | dtype = float64
  Dataset /processing/Neural states/Laser diode/id (ElementIdentifiers)  | shape = (1488,) | dtype = int64
  Dataset /processing/Neural states/Laser diode/start_time (VectorData) Start time of epoch, in seconds | shape = (1488,) | dtype = float64
  Dataset /processing/Neural states/Laser diode/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1488,) | dtype = float64
  Group /processing/Neural states/Up-Down states (TimeIntervals) Up and down states classified by LFP.
  Dataset /processing/Neural states/Up-Down states/id (ElementIdentifiers)  | shape = (27637,) | dtype = int64
  Dataset /processing/Neural states/Up-Down states/label (VectorData) state. | shape = (27637,) | dtype = object
  Dataset /processing/Neural states/Up-Down states/start_time (VectorData) Start time of epoch, in seconds | shape = (27637,) | dtype = float64
  Dataset /processing/Neural states/Up-Down states/stop_time (VectorData) Stop time of epoch, in seconds | shape = (27637,) | dtype = float64
  Group /processing/ecephys (ProcessingModule) Intermediate data from extracellular electrophysiology recordings, e.g., LFP.
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/LFP (ElectricalSeries) Local field potential signal.
  Dataset /processing/ecephys/LFP/LFP/electrodes (DynamicTableRegion) electrode_table_region | shape = (64,) | dtype = int64
  session_description: The relationship between mesoscopic local field potentials (LFPs) and single-neuron firing in the multi-layered neocortex is poorly understood. Simultaneous recordings from all layers in the primary visual cortex (V1) of the behaving mouse revealed functionally defined layers in V1. The depth of maximum spike power and sink-source distributions of LFPs provided consistent laminar landmarks across animals. Coherence of gamma oscillations (30–100 Hz) and spike-LFP coupling identified six physiological layers and further sublayers. Firing rates, burstiness, and other electrophysiological features of neurons displayed unique layer and brain state dependence. Spike transmission strength from layer 2/3 cells to layer 5 pyramidal cells and interneurons was stronger during waking compared with non-REM sleep but stronger during non-REM sleep among deep-layer excitatory neurons. A subset of deep-layer neurons was active exclusively in the DOWN state of non-REM sleep. These results bridge mesoscopic LFPs and single-neuron interactions with laminar structure in V1. Subjects were between 3 and 8 months of age.
  session_start_time: 2018-02-09T00:00:00-05:00
  timestamps_reference_time: 2018-02-09T00:00:00-05:00
  Group /units (Units) Autogenerated by nwb_conversion_tools.
  Dataset /units/ab_ratio (VectorData) AB ratio for the unit. | shape = (64,) | dtype = float64
  Dataset /units/amplitudes (VectorData) no description | shape = (6488223,) | dtype = float64
  Dataset /units/amplitudes_index (VectorIndex) Index for VectorData 'amplitudes' | shape = (64,) | dtype = uint32
  Dataset /units/brain_region (VectorData) Assigned brain region where the unit is located. | shape = (64,) | dtype = object
  Dataset /units/cell_type (VectorData) Classification of the cell type. | shape = (64,) | dtype = object
  Dataset /units/coefficient_of_variation (VectorData) Coefficient of variation for the unit activity. | shape = (64,) | dtype = float64
  Dataset /units/firing_rate (VectorData) Average firing rate of the unit. | shape = (64,) | dtype = float64
  Dataset /units/id (ElementIdentifiers)  | shape = (64,) | dtype = int64
  Dataset /units/max_channel (DynamicTableRegion) Channel that observed the maximum waveform amplitude for the unit. | shape = (64,) | dtype = int32
  Dataset /units/pc_features (VectorData) no description | shape = (6488223, 3, 12) | dtype = float32
  Dataset /units/pc_features_index (VectorIndex) Index for VectorData 'pc_features' | shape = (64,) | dtype = uint32
  Dataset /units/peak_voltage (VectorData) Magnitude of peak voltage for the unit. | shape = (64,) | dtype = float64
  Dataset /units/polarity (VectorData) Polarity of the unit. | shape = (64,) | dtype = float64
  Dataset /units/quality (VectorData) Quality of the unit as defined by phy (good, mua, noise). | shape = (64,) | dtype = object
  Dataset /units/refractory_period_violation (VectorData) Score for the violation of the refractory period. | shape = (64,) | dtype = float64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (6488223,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (64,) | dtype = uint32
  Dataset /units/synaptic_effect (VectorData) Classification of the synaptic effect (excitatory or inhibitory). Unknown if undetermined. | shape = (64,) | dtype = object
  Dataset /units/theta_modulation_index (VectorData) Index of theta modulation. | shape = (64,) | dtype = float64
