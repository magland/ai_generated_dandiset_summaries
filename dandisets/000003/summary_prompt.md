
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000003/0.230629.1955
name: Physiological Properties and Behavioral Correlates of Hippocampal Granule Cells and Mossy Cells
contributor: [{'name': 'Senzai, Yuta', 'roleName': ['dcite:Author', 'dcite:ContactPerson', 'dcite:DataCollector', 'dcite:FormalAnalysis'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Fernandez-Ruiz, Antonio', 'roleName': ['dcite:Author', 'dcite:FormalAnalysis'], 'schemaKey': 'Person', 'identifier': '0000-0001-8481-0796', 'affiliation': [], 'includeInCitation': True}, {'name': 'Buzsáki, György', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-3100-4800', 'affiliation': [{'name': 'New York University Langone Medical Center', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/005dvqh91'}], 'includeInCitation': True}, {'url': 'https://www.nih.gov/', 'name': 'National Institutes of Health', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01cwqze88', 'awardNumber': 'NIHMH54671, MH107396, NS090583', 'contactPoint': [], 'includeInCitation': False}, {'url': 'http://hnf.jp/', 'name': 'Nakajima Foundation', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/000k40t10', 'contactPoint': [], 'includeInCitation': False}, {'url': 'http://www.nsf.gov/', 'name': 'National Science Foundation', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/021nxhr62', 'awardNumber': 'PIRE', 'contactPoint': [], 'includeInCitation': False}, {'url': 'https://www.simonsfoundation.org', 'name': 'Simons Foundation', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01cmst727', 'contactPoint': [], 'includeInCitation': False}]
description: Data from "Physiological Properties and Behavioral Correlates of Hippocampal Granule Cells and Mossy Cells" Senzai, Buzsaki, Neuron 2017. Electrophysiology recordings of hippocampus during theta maze exploration.
assetsSummary: {'species': [{'name': 'House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}, {'name': 'behavioral approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 2559248010229, 'numberOfFiles': 101, 'numberOfSubjects': 16, 'variableMeasured': ['DecompositionSeries', 'LFP', 'Units', 'Position', 'ElectricalSeries'], 'measurementTechnique': [{'name': 'signal filtering technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'fourier analysis technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000003 has 5 NWB files.
1 of these NWB files are of type 1.
1 of these NWB files are of type 2.
1 of these NWB files are of type 3.
1 of these NWB files are of type 4.
1 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/position_sensor0 (SpatialSeries) raw sensor data from sensor 0
  Group /acquisition/position_sensor1 (SpatialSeries) raw sensor data from sensor 1
  file_create_date: ['2021-01-16T20:24:13.973543-05:00']
  Group /general/devices/Device (Device) YutaMouse20-140321.xml
  Group /general/devices/Implant (Device) Silicon electrodes on Intan probe.
  experimenter: ['Yuta Senzai']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (65,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (65,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (65,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (65,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (65,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (65,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/shank_electrode_number (VectorData) 0-indexed channel within a shank. | shape = (65,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/theta_reference (VectorData) This electrode was used to calculate LFP canonical bands. | shape = (65,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (65,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (65,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (65,) | dtype = float64
  Group /general/extracellular_ephys/shank1 (ElectrodeGroup) shank1 electrodes
  Group /general/extracellular_ephys/shank1/device (Device) Silicon electrodes on Intan probe.
  Group /general/extracellular_ephys/shank2 (ElectrodeGroup) shank2 electrodes
  Group /general/extracellular_ephys/shank2/device (Device) Silicon electrodes on Intan probe.
  Group /general/extracellular_ephys/shank3 (ElectrodeGroup) shank3 electrodes
  Group /general/extracellular_ephys/shank3/device (Device) Silicon electrodes on Intan probe.
  Group /general/extracellular_ephys/shank4 (ElectrodeGroup) shank4 electrodes
  Group /general/extracellular_ephys/shank4/device (Device) Silicon electrodes on Intan probe.
  Group /general/extracellular_ephys/shank5 (ElectrodeGroup) shank5 electrodes
  Group /general/extracellular_ephys/shank5/device (Device) Silicon electrodes on Intan probe.
  Group /general/extracellular_ephys/shank6 (ElectrodeGroup) shank6 electrodes
  Group /general/extracellular_ephys/shank6/device (Device) Silicon electrodes on Intan probe.
  Group /general/extracellular_ephys/shank7 (ElectrodeGroup) shank7 electrodes
  Group /general/extracellular_ephys/shank7/device (Device) Silicon electrodes on Intan probe.
  Group /general/extracellular_ephys/shank8 (ElectrodeGroup) shank8 electrodes
  Group /general/extracellular_ephys/shank8/device (Device) Silicon electrodes on Intan probe.
  institution: NYU
  lab: Buzsaki
  related_publications: ['DOI:10.1016/j.neuron.2016.12.011']
  session_id: YutaMouse20-140321
  Group /general/subject (Subject) 
  identifier: 23647bce-e14c-4498-a45d-8b5dcd572360
  Group /processing/behavior (ProcessingModule) Contains behavioral data.
  Group /processing/behavior/states (TimeIntervals) sleep states of animal
  Dataset /processing/behavior/states/id (ElementIdentifiers)  | shape = (21,) | dtype = int64
  Dataset /processing/behavior/states/label (VectorData) sleep state | shape = (21,) | dtype = object
  Dataset /processing/behavior/states/start_time (VectorData) Start time of epoch, in seconds | shape = (21,) | dtype = float32
  Dataset /processing/behavior/states/stop_time (VectorData) Stop time of epoch, in seconds | shape = (21,) | dtype = float32
  Group /processing/ecephys (ProcessingModule) Intermediate data from extracellular electrophysiology recordings, e.g., LFP.
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/LFP (ElectricalSeries) Local field potential signal.
  Dataset /processing/ecephys/LFP/LFP/electrodes (DynamicTableRegion) electrode_table_region | shape = (65,) | dtype = int64
  Group /processing/ecephys/LFPDecompositionSeries (DecompositionSeries) Theta and Gamma phase for reference LFP
  Group /processing/ecephys/LFPDecompositionSeries/bands (DynamicTable) data about the frequency bands that the signal was decomposed into
  Dataset /processing/ecephys/LFPDecompositionSeries/bands/band_limits (VectorData) low and high frequencies of bandpass filter in Hz | shape = (2, 2) | dtype = int64
  Dataset /processing/ecephys/LFPDecompositionSeries/bands/band_name (VectorData) the name of the frequency band (recommended: 'alpha', 'beta', 'gamma', 'delta', 'high gamma' | shape = (2,) | dtype = object
  Dataset /processing/ecephys/LFPDecompositionSeries/bands/id (ElementIdentifiers)  | shape = (2,) | dtype = int64
  Group /processing/ecephys/LFPDecompositionSeries/source_timeseries (ElectricalSeries) Local field potential signal.
  Dataset /processing/ecephys/LFPDecompositionSeries/source_timeseries/electrodes (DynamicTableRegion) electrode_table_region | shape = (65,) | dtype = int64
  session_description: Mouse in open exploration and theta maze.
  session_start_time: 2014-03-21T00:00:00-04:00
  Group /stimulus/presentation/DS1.ch4 (AnnotationSeries) no description
  Group /stimulus/presentation/DS2.ch4 (AnnotationSeries) no description
  Group /stimulus/presentation/MS_PulseStim (AnnotationSeries) no description
  Group /stimulus/presentation/MS_PulseStim_briefLD (AnnotationSeries) no description
  Group /stimulus/presentation/MS_PulseStim_briefLaser (AnnotationSeries) no description
  Group /stimulus/presentation/PeakStim5V (AnnotationSeries) no description
  Group /stimulus/presentation/PulseStim_10ms (AnnotationSeries) no description
  Group /stimulus/presentation/PulseStim_1sec (AnnotationSeries) no description
  Group /stimulus/presentation/PulseStim_1sec_weak (AnnotationSeries) no description
  Group /stimulus/presentation/Ripple (AnnotationSeries) no description
  Group /stimulus/presentation/StimDuringRun_5V_End (AnnotationSeries) no description
  Group /stimulus/presentation/StimDuringRun_5V_Start (AnnotationSeries) no description
  Group /stimulus/presentation/StimDuringRun_End (AnnotationSeries) no description
  Group /stimulus/presentation/StimDuringRun_Start (AnnotationSeries) no description
  Group /stimulus/presentation/TroughStim5V (AnnotationSeries) no description
  timestamps_reference_time: 2014-03-21T00:00:00-04:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/cell_type (VectorData) Name of cell type. | shape = (22,) | dtype = object
  Dataset /units/global_id (VectorData) Global id for cell for entire experiment. | shape = (22,) | dtype = uint16
  Dataset /units/id (ElementIdentifiers)  | shape = (22,) | dtype = int64
  Dataset /units/shank_id (VectorData) 0-indexed id of cluster of shank. | shape = (22,) | dtype = int64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (2759455,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (22,) | dtype = uint32
  Dataset /units/waveforms (VectorData) Individual waveforms for each spike. If the dataset is three-dimensional, the third dimension shows the response from different electrodes that all observe this unit simultaneously. In this case, the `electrodes` column of this Units table should be used to indicate which electrodes are associated with this unit, and the electrodes dimension here should be in the same order as the electrodes referenced in the `electrodes` column of this table. | shape = (27594550, 32) | dtype = float64
  Dataset /units/waveforms_index (VectorIndex) Index for VectorData 'waveforms' | shape = (2759455,) | dtype = uint32
  Dataset /units/waveforms_index_index (VectorIndex) Index for VectorData 'waveforms_index' | shape = (22,) | dtype = uint32


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/position_sensor0 (SpatialSeries) raw sensor data from sensor 0
  Group /acquisition/position_sensor1 (SpatialSeries) raw sensor data from sensor 1
  file_create_date: ['2021-01-16T20:36:26.711506-05:00']
  Group /general/devices/Device (Device) YutaMouse20-140324.xml
  Group /general/devices/Implant (Device) Silicon electrodes on Intan probe.
  experimenter: ['Yuta Senzai']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (65,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (65,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (65,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (65,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (65,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (65,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/shank_electrode_number (VectorData) 0-indexed channel within a shank. | shape = (65,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/theta_reference (VectorData) This electrode was used to calculate LFP canonical bands. | shape = (65,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (65,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (65,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (65,) | dtype = float64
  Group /general/extracellular_ephys/shank1 (ElectrodeGroup) shank1 electrodes
  Group /general/extracellular_ephys/shank1/device (Device) Silicon electrodes on Intan probe.
  Group /general/extracellular_ephys/shank2 (ElectrodeGroup) shank2 electrodes
  Group /general/extracellular_ephys/shank2/device (Device) Silicon electrodes on Intan probe.
  Group /general/extracellular_ephys/shank3 (ElectrodeGroup) shank3 electrodes
  Group /general/extracellular_ephys/shank3/device (Device) Silicon electrodes on Intan probe.
  Group /general/extracellular_ephys/shank4 (ElectrodeGroup) shank4 electrodes
  Group /general/extracellular_ephys/shank4/device (Device) Silicon electrodes on Intan probe.
  Group /general/extracellular_ephys/shank5 (ElectrodeGroup) shank5 electrodes
  Group /general/extracellular_ephys/shank5/device (Device) Silicon electrodes on Intan probe.
  Group /general/extracellular_ephys/shank6 (ElectrodeGroup) shank6 electrodes
  Group /general/extracellular_ephys/shank6/device (Device) Silicon electrodes on Intan probe.
  Group /general/extracellular_ephys/shank7 (ElectrodeGroup) shank7 electrodes
  Group /general/extracellular_ephys/shank7/device (Device) Silicon electrodes on Intan probe.
  Group /general/extracellular_ephys/shank8 (ElectrodeGroup) shank8 electrodes
  Group /general/extracellular_ephys/shank8/device (Device) Silicon electrodes on Intan probe.
  institution: NYU
  lab: Buzsaki
  related_publications: ['DOI:10.1016/j.neuron.2016.12.011']
  session_id: YutaMouse20-140324
  Group /general/subject (Subject) 
  identifier: c54bfca8-ce87-4ffa-ad85-a736b115e01c
  Group /processing/behavior (ProcessingModule) Contains behavioral data.
  Group /processing/behavior/states (TimeIntervals) sleep states of animal
  Dataset /processing/behavior/states/id (ElementIdentifiers)  | shape = (36,) | dtype = int64
  Dataset /processing/behavior/states/label (VectorData) sleep state | shape = (36,) | dtype = object
  Dataset /processing/behavior/states/start_time (VectorData) Start time of epoch, in seconds | shape = (36,) | dtype = float32
  Dataset /processing/behavior/states/stop_time (VectorData) Stop time of epoch, in seconds | shape = (36,) | dtype = float32
  Group /processing/ecephys (ProcessingModule) Intermediate data from extracellular electrophysiology recordings, e.g., LFP.
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/LFP (ElectricalSeries) Local field potential signal.
  Dataset /processing/ecephys/LFP/LFP/electrodes (DynamicTableRegion) electrode_table_region | shape = (65,) | dtype = int64
  Group /processing/ecephys/LFPDecompositionSeries (DecompositionSeries) Theta and Gamma phase for reference LFP
  Group /processing/ecephys/LFPDecompositionSeries/bands (DynamicTable) data about the frequency bands that the signal was decomposed into
  Dataset /processing/ecephys/LFPDecompositionSeries/bands/band_limits (VectorData) low and high frequencies of bandpass filter in Hz | shape = (2, 2) | dtype = int64
  Dataset /processing/ecephys/LFPDecompositionSeries/bands/band_name (VectorData) the name of the frequency band (recommended: 'alpha', 'beta', 'gamma', 'delta', 'high gamma' | shape = (2,) | dtype = object
  Dataset /processing/ecephys/LFPDecompositionSeries/bands/id (ElementIdentifiers)  | shape = (2,) | dtype = int64
  Group /processing/ecephys/LFPDecompositionSeries/source_timeseries (ElectricalSeries) Local field potential signal.
  Dataset /processing/ecephys/LFPDecompositionSeries/source_timeseries/electrodes (DynamicTableRegion) electrode_table_region | shape = (65,) | dtype = int64
  session_description: Mouse in open exploration and theta maze.
  session_start_time: 2014-03-24T00:00:00-04:00
  Group /stimulus/presentation/DS1.ch59 (AnnotationSeries) no description
  Group /stimulus/presentation/DS2.ch59 (AnnotationSeries) no description
  Group /stimulus/presentation/MS_PulseStim (AnnotationSeries) no description
  Group /stimulus/presentation/MS_PulseStim_briefLD (AnnotationSeries) no description
  Group /stimulus/presentation/MS_PulseStim_briefLaser (AnnotationSeries) no description
  Group /stimulus/presentation/PeakStim (AnnotationSeries) no description
  Group /stimulus/presentation/PulseStim_10ms (AnnotationSeries) no description
  Group /stimulus/presentation/PulseStim_1sec (AnnotationSeries) no description
  Group /stimulus/presentation/PulseStim_1sec2 (AnnotationSeries) no description
  Group /stimulus/presentation/PulseStim_1sec_weak (AnnotationSeries) no description
  Group /stimulus/presentation/Ripple (AnnotationSeries) no description
  Group /stimulus/presentation/StimDuringRun_5V_End (AnnotationSeries) no description
  Group /stimulus/presentation/StimDuringRun_5V_Start (AnnotationSeries) no description
  Group /stimulus/presentation/StimDuringRun_End (AnnotationSeries) no description
  Group /stimulus/presentation/StimDuringRun_Start (AnnotationSeries) no description
  Group /stimulus/presentation/TroughStim (AnnotationSeries) no description
  timestamps_reference_time: 2014-03-24T00:00:00-04:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/cell_type (VectorData) Name of cell type. | shape = (42,) | dtype = object
  Dataset /units/global_id (VectorData) Global id for cell for entire experiment. | shape = (42,) | dtype = float64
  Dataset /units/id (ElementIdentifiers)  | shape = (42,) | dtype = int64
  Dataset /units/shank_id (VectorData) 0-indexed id of cluster of shank. | shape = (42,) | dtype = int64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (4079097,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (42,) | dtype = uint32
  Dataset /units/waveforms (VectorData) Individual waveforms for each spike. If the dataset is three-dimensional, the third dimension shows the response from different electrodes that all observe this unit simultaneously. In this case, the `electrodes` column of this Units table should be used to indicate which electrodes are associated with this unit, and the electrodes dimension here should be in the same order as the electrodes referenced in the `electrodes` column of this table. | shape = (40790970, 32) | dtype = float64
  Dataset /units/waveforms_index (VectorIndex) Index for VectorData 'waveforms' | shape = (4079097,) | dtype = uint32
  Dataset /units/waveforms_index_index (VectorIndex) Index for VectorData 'waveforms_index' | shape = (42,) | dtype = uint32


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/position_sensor0 (SpatialSeries) raw sensor data from sensor 0
  Group /acquisition/position_sensor1 (SpatialSeries) raw sensor data from sensor 1
  file_create_date: ['2021-01-16T20:50:56.836886-05:00']
  Group /general/devices/Device (Device) YutaMouse20-140325.xml
  Group /general/devices/Implant (Device) Silicon electrodes on Intan probe.
  experimenter: ['Yuta Senzai']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (65,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (65,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (65,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (65,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (65,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (65,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/shank_electrode_number (VectorData) 0-indexed channel within a shank. | shape = (65,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/theta_reference (VectorData) This electrode was used to calculate LFP canonical bands. | shape = (65,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (65,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (65,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (65,) | dtype = float64
  Group /general/extracellular_ephys/shank1 (ElectrodeGroup) shank1 electrodes
  Group /general/extracellular_ephys/shank1/device (Device) Silicon electrodes on Intan probe.
  Group /general/extracellular_ephys/shank2 (ElectrodeGroup) shank2 electrodes
  Group /general/extracellular_ephys/shank2/device (Device) Silicon electrodes on Intan probe.
  Group /general/extracellular_ephys/shank3 (ElectrodeGroup) shank3 electrodes
  Group /general/extracellular_ephys/shank3/device (Device) Silicon electrodes on Intan probe.
  Group /general/extracellular_ephys/shank4 (ElectrodeGroup) shank4 electrodes
  Group /general/extracellular_ephys/shank4/device (Device) Silicon electrodes on Intan probe.
  Group /general/extracellular_ephys/shank5 (ElectrodeGroup) shank5 electrodes
  Group /general/extracellular_ephys/shank5/device (Device) Silicon electrodes on Intan probe.
  Group /general/extracellular_ephys/shank6 (ElectrodeGroup) shank6 electrodes
  Group /general/extracellular_ephys/shank6/device (Device) Silicon electrodes on Intan probe.
  Group /general/extracellular_ephys/shank7 (ElectrodeGroup) shank7 electrodes
  Group /general/extracellular_ephys/shank7/device (Device) Silicon electrodes on Intan probe.
  Group /general/extracellular_ephys/shank8 (ElectrodeGroup) shank8 electrodes
  Group /general/extracellular_ephys/shank8/device (Device) Silicon electrodes on Intan probe.
  institution: NYU
  lab: Buzsaki
  related_publications: ['DOI:10.1016/j.neuron.2016.12.011']
  session_id: YutaMouse20-140325
  Group /general/subject (Subject) 
  identifier: cd572d08-795b-4806-bff6-d973b824ab8f
  Group /processing/behavior (ProcessingModule) Contains behavioral data.
  Group /processing/behavior/states (TimeIntervals) sleep states of animal
  Dataset /processing/behavior/states/id (ElementIdentifiers)  | shape = (33,) | dtype = int64
  Dataset /processing/behavior/states/label (VectorData) sleep state | shape = (33,) | dtype = object
  Dataset /processing/behavior/states/start_time (VectorData) Start time of epoch, in seconds | shape = (33,) | dtype = float32
  Dataset /processing/behavior/states/stop_time (VectorData) Stop time of epoch, in seconds | shape = (33,) | dtype = float32
  Group /processing/ecephys (ProcessingModule) Intermediate data from extracellular electrophysiology recordings, e.g., LFP.
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/LFP (ElectricalSeries) Local field potential signal.
  Dataset /processing/ecephys/LFP/LFP/electrodes (DynamicTableRegion) electrode_table_region | shape = (65,) | dtype = int64
  Group /processing/ecephys/LFPDecompositionSeries (DecompositionSeries) Theta and Gamma phase for reference LFP
  Group /processing/ecephys/LFPDecompositionSeries/bands (DynamicTable) data about the frequency bands that the signal was decomposed into
  Dataset /processing/ecephys/LFPDecompositionSeries/bands/band_limits (VectorData) low and high frequencies of bandpass filter in Hz | shape = (2, 2) | dtype = int64
  Dataset /processing/ecephys/LFPDecompositionSeries/bands/band_name (VectorData) the name of the frequency band (recommended: 'alpha', 'beta', 'gamma', 'delta', 'high gamma' | shape = (2,) | dtype = object
  Dataset /processing/ecephys/LFPDecompositionSeries/bands/id (ElementIdentifiers)  | shape = (2,) | dtype = int64
  Group /processing/ecephys/LFPDecompositionSeries/source_timeseries (ElectricalSeries) Local field potential signal.
  Dataset /processing/ecephys/LFPDecompositionSeries/source_timeseries/electrodes (DynamicTableRegion) electrode_table_region | shape = (65,) | dtype = int64
  session_description: Mouse in open exploration and theta maze.
  session_start_time: 2014-03-25T00:00:00-04:00
  Group /stimulus/presentation/DS1.ch11 (AnnotationSeries) no description
  Group /stimulus/presentation/DS1.ch33 (AnnotationSeries) no description
  Group /stimulus/presentation/DS2.ch11 (AnnotationSeries) no description
  Group /stimulus/presentation/DS2.ch33 (AnnotationSeries) no description
  Group /stimulus/presentation/MS_PulseStim (AnnotationSeries) no description
  Group /stimulus/presentation/MS_PulseStim_briefLD (AnnotationSeries) no description
  Group /stimulus/presentation/MS_PulseStim_briefLaser (AnnotationSeries) no description
  Group /stimulus/presentation/PeakStim5V (AnnotationSeries) no description
  Group /stimulus/presentation/PulseStim_10ms (AnnotationSeries) no description
  Group /stimulus/presentation/PulseStim_1sec (AnnotationSeries) no description
  Group /stimulus/presentation/PulseStim_1sec_weak (AnnotationSeries) no description
  Group /stimulus/presentation/Ripple (AnnotationSeries) no description
  Group /stimulus/presentation/StimDuringRun_5V_End (AnnotationSeries) no description
  Group /stimulus/presentation/StimDuringRun_5V_Start (AnnotationSeries) no description
  Group /stimulus/presentation/StimDuringRun_End (AnnotationSeries) no description
  Group /stimulus/presentation/StimDuringRun_Start (AnnotationSeries) no description
  Group /stimulus/presentation/TroughStim5V (AnnotationSeries) no description
  timestamps_reference_time: 2014-03-25T00:00:00-04:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/cell_type (VectorData) Name of cell type. | shape = (36,) | dtype = object
  Dataset /units/global_id (VectorData) Global id for cell for entire experiment. | shape = (36,) | dtype = float64
  Dataset /units/id (ElementIdentifiers)  | shape = (36,) | dtype = int64
  Dataset /units/shank_id (VectorData) 0-indexed id of cluster of shank. | shape = (36,) | dtype = int64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (4980587,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (36,) | dtype = uint32
  Dataset /units/waveforms (VectorData) Individual waveforms for each spike. If the dataset is three-dimensional, the third dimension shows the response from different electrodes that all observe this unit simultaneously. In this case, the `electrodes` column of this Units table should be used to indicate which electrodes are associated with this unit, and the electrodes dimension here should be in the same order as the electrodes referenced in the `electrodes` column of this table. | shape = (49805870, 32) | dtype = float64
  Dataset /units/waveforms_index (VectorIndex) Index for VectorData 'waveforms' | shape = (4980587,) | dtype = uint32
  Dataset /units/waveforms_index_index (VectorIndex) Index for VectorData 'waveforms_index' | shape = (36,) | dtype = uint32


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/position_sensor0 (SpatialSeries) raw sensor data from sensor 0
  Group /acquisition/position_sensor1 (SpatialSeries) raw sensor data from sensor 1
  file_create_date: ['2021-01-16T21:07:05.240171-05:00']
  Group /general/devices/Device (Device) YutaMouse20-140327.xml
  Group /general/devices/Implant (Device) Silicon electrodes on Intan probe.
  experimenter: ['Yuta Senzai']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (65,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (65,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (65,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (65,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (65,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (65,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/shank_electrode_number (VectorData) 0-indexed channel within a shank. | shape = (65,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/theta_reference (VectorData) This electrode was used to calculate LFP canonical bands. | shape = (65,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (65,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (65,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (65,) | dtype = float64
  Group /general/extracellular_ephys/shank1 (ElectrodeGroup) shank1 electrodes
  Group /general/extracellular_ephys/shank1/device (Device) Silicon electrodes on Intan probe.
  Group /general/extracellular_ephys/shank2 (ElectrodeGroup) shank2 electrodes
  Group /general/extracellular_ephys/shank2/device (Device) Silicon electrodes on Intan probe.
  Group /general/extracellular_ephys/shank3 (ElectrodeGroup) shank3 electrodes
  Group /general/extracellular_ephys/shank3/device (Device) Silicon electrodes on Intan probe.
  Group /general/extracellular_ephys/shank4 (ElectrodeGroup) shank4 electrodes
  Group /general/extracellular_ephys/shank4/device (Device) Silicon electrodes on Intan probe.
  Group /general/extracellular_ephys/shank5 (ElectrodeGroup) shank5 electrodes
  Group /general/extracellular_ephys/shank5/device (Device) Silicon electrodes on Intan probe.
  Group /general/extracellular_ephys/shank6 (ElectrodeGroup) shank6 electrodes
  Group /general/extracellular_ephys/shank6/device (Device) Silicon electrodes on Intan probe.
  Group /general/extracellular_ephys/shank7 (ElectrodeGroup) shank7 electrodes
  Group /general/extracellular_ephys/shank7/device (Device) Silicon electrodes on Intan probe.
  Group /general/extracellular_ephys/shank8 (ElectrodeGroup) shank8 electrodes
  Group /general/extracellular_ephys/shank8/device (Device) Silicon electrodes on Intan probe.
  institution: NYU
  lab: Buzsaki
  related_publications: ['DOI:10.1016/j.neuron.2016.12.011']
  session_id: YutaMouse20-140327
  Group /general/subject (Subject) 
  identifier: fd889571-df95-4fb0-9139-64836eb98e3e
  Group /processing/behavior (ProcessingModule) Contains behavioral data.
  Group /processing/behavior/states (TimeIntervals) sleep states of animal
  Dataset /processing/behavior/states/id (ElementIdentifiers)  | shape = (28,) | dtype = int64
  Dataset /processing/behavior/states/label (VectorData) sleep state | shape = (28,) | dtype = object
  Dataset /processing/behavior/states/start_time (VectorData) Start time of epoch, in seconds | shape = (28,) | dtype = float32
  Dataset /processing/behavior/states/stop_time (VectorData) Stop time of epoch, in seconds | shape = (28,) | dtype = float32
  Group /processing/ecephys (ProcessingModule) Intermediate data from extracellular electrophysiology recordings, e.g., LFP.
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/LFP (ElectricalSeries) Local field potential signal.
  Dataset /processing/ecephys/LFP/LFP/electrodes (DynamicTableRegion) electrode_table_region | shape = (65,) | dtype = int64
  Group /processing/ecephys/LFPDecompositionSeries (DecompositionSeries) Theta and Gamma phase for reference LFP
  Group /processing/ecephys/LFPDecompositionSeries/bands (DynamicTable) data about the frequency bands that the signal was decomposed into
  Dataset /processing/ecephys/LFPDecompositionSeries/bands/band_limits (VectorData) low and high frequencies of bandpass filter in Hz | shape = (2, 2) | dtype = int64
  Dataset /processing/ecephys/LFPDecompositionSeries/bands/band_name (VectorData) the name of the frequency band (recommended: 'alpha', 'beta', 'gamma', 'delta', 'high gamma' | shape = (2,) | dtype = object
  Dataset /processing/ecephys/LFPDecompositionSeries/bands/id (ElementIdentifiers)  | shape = (2,) | dtype = int64
  Group /processing/ecephys/LFPDecompositionSeries/source_timeseries (ElectricalSeries) Local field potential signal.
  Dataset /processing/ecephys/LFPDecompositionSeries/source_timeseries/electrodes (DynamicTableRegion) electrode_table_region | shape = (65,) | dtype = int64
  session_description: Mouse in open exploration and theta maze.
  session_start_time: 2014-03-27T00:00:00-04:00
  Group /stimulus/presentation/DS1.ch54 (AnnotationSeries) no description
  Group /stimulus/presentation/DS2.ch54 (AnnotationSeries) no description
  Group /stimulus/presentation/MS_PulseStim (AnnotationSeries) no description
  Group /stimulus/presentation/MS_PulseStim_briefLD (AnnotationSeries) no description
  Group /stimulus/presentation/MS_PulseStim_briefLaser (AnnotationSeries) no description
  Group /stimulus/presentation/PeakStim5V (AnnotationSeries) no description
  Group /stimulus/presentation/PulseStim_10ms (AnnotationSeries) no description
  Group /stimulus/presentation/PulseStim_1sec (AnnotationSeries) no description
  Group /stimulus/presentation/Ripple (AnnotationSeries) no description
  Group /stimulus/presentation/StimDuringRun_5V_End (AnnotationSeries) no description
  Group /stimulus/presentation/StimDuringRun_5V_Start (AnnotationSeries) no description
  Group /stimulus/presentation/StimDuringRun_End (AnnotationSeries) no description
  Group /stimulus/presentation/StimDuringRun_Start (AnnotationSeries) no description
  Group /stimulus/presentation/TroughStim5V (AnnotationSeries) no description
  timestamps_reference_time: 2014-03-27T00:00:00-04:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/cell_type (VectorData) Name of cell type. | shape = (14,) | dtype = object
  Dataset /units/global_id (VectorData) Global id for cell for entire experiment. | shape = (14,) | dtype = float64
  Dataset /units/id (ElementIdentifiers)  | shape = (14,) | dtype = int64
  Dataset /units/shank_id (VectorData) 0-indexed id of cluster of shank. | shape = (14,) | dtype = int64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (1649623,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (14,) | dtype = uint32
  Dataset /units/waveforms (VectorData) Individual waveforms for each spike. If the dataset is three-dimensional, the third dimension shows the response from different electrodes that all observe this unit simultaneously. In this case, the `electrodes` column of this Units table should be used to indicate which electrodes are associated with this unit, and the electrodes dimension here should be in the same order as the electrodes referenced in the `electrodes` column of this table. | shape = (16340212, 32) | dtype = float64
  Dataset /units/waveforms_index (VectorIndex) Index for VectorData 'waveforms' | shape = (1649623,) | dtype = uint32
  Dataset /units/waveforms_index_index (VectorIndex) Index for VectorData 'waveforms_index' | shape = (14,) | dtype = uint32


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  Group /acquisition/position_sensor0 (SpatialSeries) raw sensor data from sensor 0
  Group /acquisition/position_sensor1 (SpatialSeries) raw sensor data from sensor 1
  file_create_date: ['2021-01-16T21:19:26.824517-05:00']
  Group /general/devices/Device (Device) YutaMouse20-140328.xml
  Group /general/devices/Implant (Device) Silicon electrodes on Intan probe.
  experimenter: ['Yuta Senzai']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (65,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (65,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (65,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (65,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (65,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (65,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/shank_electrode_number (VectorData) 0-indexed channel within a shank. | shape = (65,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/theta_reference (VectorData) This electrode was used to calculate LFP canonical bands. | shape = (65,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (65,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (65,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (65,) | dtype = float64
  Group /general/extracellular_ephys/shank1 (ElectrodeGroup) shank1 electrodes
  Group /general/extracellular_ephys/shank1/device (Device) Silicon electrodes on Intan probe.
  Group /general/extracellular_ephys/shank2 (ElectrodeGroup) shank2 electrodes
  Group /general/extracellular_ephys/shank2/device (Device) Silicon electrodes on Intan probe.
  Group /general/extracellular_ephys/shank3 (ElectrodeGroup) shank3 electrodes
  Group /general/extracellular_ephys/shank3/device (Device) Silicon electrodes on Intan probe.
  Group /general/extracellular_ephys/shank4 (ElectrodeGroup) shank4 electrodes
  Group /general/extracellular_ephys/shank4/device (Device) Silicon electrodes on Intan probe.
  Group /general/extracellular_ephys/shank5 (ElectrodeGroup) shank5 electrodes
  Group /general/extracellular_ephys/shank5/device (Device) Silicon electrodes on Intan probe.
  Group /general/extracellular_ephys/shank6 (ElectrodeGroup) shank6 electrodes
  Group /general/extracellular_ephys/shank6/device (Device) Silicon electrodes on Intan probe.
  Group /general/extracellular_ephys/shank7 (ElectrodeGroup) shank7 electrodes
  Group /general/extracellular_ephys/shank7/device (Device) Silicon electrodes on Intan probe.
  Group /general/extracellular_ephys/shank8 (ElectrodeGroup) shank8 electrodes
  Group /general/extracellular_ephys/shank8/device (Device) Silicon electrodes on Intan probe.
  institution: NYU
  lab: Buzsaki
  related_publications: ['DOI:10.1016/j.neuron.2016.12.011']
  session_id: YutaMouse20-140328
  Group /general/subject (Subject) 
  identifier: 0d184950-8d6f-4d1d-820c-7394a7f487bb
  Group /processing/behavior (ProcessingModule) Contains behavioral data.
  Group /processing/behavior/states (TimeIntervals) sleep states of animal
  Dataset /processing/behavior/states/id (ElementIdentifiers)  | shape = (22,) | dtype = int64
  Dataset /processing/behavior/states/label (VectorData) sleep state | shape = (22,) | dtype = object
  Dataset /processing/behavior/states/start_time (VectorData) Start time of epoch, in seconds | shape = (22,) | dtype = float32
  Dataset /processing/behavior/states/stop_time (VectorData) Stop time of epoch, in seconds | shape = (22,) | dtype = float32
  Group /processing/ecephys (ProcessingModule) Intermediate data from extracellular electrophysiology recordings, e.g., LFP.
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/LFP (ElectricalSeries) Local field potential signal.
  Dataset /processing/ecephys/LFP/LFP/electrodes (DynamicTableRegion) electrode_table_region | shape = (65,) | dtype = int64
  Group /processing/ecephys/LFPDecompositionSeries (DecompositionSeries) Theta and Gamma phase for reference LFP
  Group /processing/ecephys/LFPDecompositionSeries/bands (DynamicTable) data about the frequency bands that the signal was decomposed into
  Dataset /processing/ecephys/LFPDecompositionSeries/bands/band_limits (VectorData) low and high frequencies of bandpass filter in Hz | shape = (2, 2) | dtype = int64
  Dataset /processing/ecephys/LFPDecompositionSeries/bands/band_name (VectorData) the name of the frequency band (recommended: 'alpha', 'beta', 'gamma', 'delta', 'high gamma' | shape = (2,) | dtype = object
  Dataset /processing/ecephys/LFPDecompositionSeries/bands/id (ElementIdentifiers)  | shape = (2,) | dtype = int64
  Group /processing/ecephys/LFPDecompositionSeries/source_timeseries (ElectricalSeries) Local field potential signal.
  Dataset /processing/ecephys/LFPDecompositionSeries/source_timeseries/electrodes (DynamicTableRegion) electrode_table_region | shape = (65,) | dtype = int64
  session_description: Mouse in open exploration and theta maze.
  session_start_time: 2014-03-28T00:00:00-04:00
  Group /stimulus/presentation/DS1.ch59 (AnnotationSeries) no description
  Group /stimulus/presentation/DS2.ch59 (AnnotationSeries) no description
  Group /stimulus/presentation/MS_PulseStim (AnnotationSeries) no description
  Group /stimulus/presentation/MS_PulseStim_briefLD (AnnotationSeries) no description
  Group /stimulus/presentation/MS_PulseStim_briefLaser (AnnotationSeries) no description
  Group /stimulus/presentation/PeakStim5V (AnnotationSeries) no description
  Group /stimulus/presentation/PulseStim_10ms (AnnotationSeries) no description
  Group /stimulus/presentation/PulseStim_1sec (AnnotationSeries) no description
  Group /stimulus/presentation/Ripple (AnnotationSeries) no description
  Group /stimulus/presentation/StimDuringRun_5V_End (AnnotationSeries) no description
  Group /stimulus/presentation/StimDuringRun_5V_Start (AnnotationSeries) no description
  Group /stimulus/presentation/StimDuringRun_End (AnnotationSeries) no description
  Group /stimulus/presentation/StimDuringRun_Start (AnnotationSeries) no description
  Group /stimulus/presentation/TroughStim5V (AnnotationSeries) no description
  timestamps_reference_time: 2014-03-28T00:00:00-04:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/cell_type (VectorData) Name of cell type. | shape = (22,) | dtype = object
  Dataset /units/global_id (VectorData) Global id for cell for entire experiment. | shape = (22,) | dtype = float64
  Dataset /units/id (ElementIdentifiers)  | shape = (22,) | dtype = int64
  Dataset /units/shank_id (VectorData) 0-indexed id of cluster of shank. | shape = (22,) | dtype = int64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (5442106,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (22,) | dtype = uint32
  Dataset /units/waveforms (VectorData) Individual waveforms for each spike. If the dataset is three-dimensional, the third dimension shows the response from different electrodes that all observe this unit simultaneously. In this case, the `electrodes` column of this Units table should be used to indicate which electrodes are associated with this unit, and the electrodes dimension here should be in the same order as the electrodes referenced in the `electrodes` column of this table. | shape = (54421060, 32) | dtype = float64
  Dataset /units/waveforms_index (VectorIndex) Index for VectorData 'waveforms' | shape = (5442106,) | dtype = uint32
  Dataset /units/waveforms_index_index (VectorIndex) Index for VectorData 'waveforms_index' | shape = (22,) | dtype = uint32
