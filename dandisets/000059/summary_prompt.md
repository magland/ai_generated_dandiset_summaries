
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000059/0.230907.2101
name: Cooling of Medial Septum Reveals Theta Phase Lag Coordination of Hippocampal Cell Assemblies
contributor: [{'name': 'Petersen, Peter', 'roleName': ['dcite:Author', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0002-2092-4791', 'affiliation': [], 'includeInCitation': True}, {'name': 'Buzsáki, György', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-3100-4800', 'affiliation': [], 'includeInCitation': True}, {'name': 'Baker, Cody', 'roleName': ['dcite:DataCurator'], 'schemaKey': 'Person', 'identifier': '0000-0002-0829-4790', 'affiliation': [], 'includeInCitation': False}, {'url': 'http://www.nsf.gov/', 'name': 'National Science Foundation', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/021nxhr62', 'awardNumber': 'NeuroNex 1707316', 'contactPoint': [], 'includeInCitation': False}, {'name': 'Lundbeck Foundation', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/03hz8wd80', 'contactPoint': [], 'includeInCitation': False}, {'url': 'http://www.nih.gov/', 'name': 'National Institutes of Health', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01cwqze88', 'awardNumber': 'MH122391, MH54671, MH107396, U19 NS107616, U19 NS104590', 'contactPoint': [], 'includeInCitation': False}]
description: Hippocampal theta oscillations coordinate neuronal firing to support memory and spatial navigation. The medial septum (MS) is critical in theta generation by two possible mechanisms: either a unitary “pacemaker” timing signal is imposed on the hippocampal system, or it may assist in organizing target subcircuits within the phase space of theta oscillations. We used temperature manipulation of the MS to test these models. Cooling of the MS reduced both theta frequency and power and was associated with an enhanced incidence of errors in a spatial navigation task, but it did not affect spatial correlates of neurons. MS cooling decreased theta frequency oscillations of place cells and reduced distance-time compression but preserved distance-phase compression of place field sequences within the theta cycle. Thus, the septum is critical for sustaining precise theta phase coordination of cell assemblies in the hippocampal system, a mechanism needed for spatial memory.
assetsSummary: {'species': [{'name': 'Rattus norvegicus - Norway rat', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10116'}], 'approach': [{'name': 'behavioral approach', 'schemaKey': 'ApproachType'}, {'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 2935390229648, 'numberOfFiles': 100, 'numberOfSubjects': 5, 'variableMeasured': ['ProcessingModule', 'Position', 'ElectrodeGroup', 'SpatialSeries', 'Units', 'LFP', 'ElectricalSeries'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'signal filtering technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000059 has 20 NWB files.
6 of these NWB files are of type 1.
9 of these NWB files are of type 2.
3 of these NWB files are of type 3.
1 of these NWB files are of type 4.
1 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2021-02-17T08:28:36.635240-05:00']
  Group /general/devices/Device (Device) The five rats were implanted with multi-shank 64-site silicon probes bilaterally in the CA1 pyramidal layer of the dorsal hippocampus.
  experimenter: ['Peter Petersen']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (64,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/shank_electrode_number (VectorData) 0-indexed channel within a shank. | shape = (64,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/theta_reference (VectorData) Channel used as theta reference. | shape = (64,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (64,) | dtype = float64
  Group /general/extracellular_ephys/shank1 (ElectrodeGroup) shank1 electrodes
  Group /general/extracellular_ephys/shank1/device (Device) The five rats were implanted with multi-shank 64-site silicon probes bilaterally in the CA1 pyramidal layer of the dorsal hippocampus.
  Group /general/extracellular_ephys/shank2 (ElectrodeGroup) shank2 electrodes
  Group /general/extracellular_ephys/shank2/device (Device) The five rats were implanted with multi-shank 64-site silicon probes bilaterally in the CA1 pyramidal layer of the dorsal hippocampus.
  Group /general/extracellular_ephys/shank3 (ElectrodeGroup) shank3 electrodes
  Group /general/extracellular_ephys/shank3/device (Device) The five rats were implanted with multi-shank 64-site silicon probes bilaterally in the CA1 pyramidal layer of the dorsal hippocampus.
  Group /general/extracellular_ephys/shank4 (ElectrodeGroup) shank4 electrodes
  Group /general/extracellular_ephys/shank4/device (Device) The five rats were implanted with multi-shank 64-site silicon probes bilaterally in the CA1 pyramidal layer of the dorsal hippocampus.
  Group /general/extracellular_ephys/shank5 (ElectrodeGroup) shank5 electrodes
  Group /general/extracellular_ephys/shank5/device (Device) The five rats were implanted with multi-shank 64-site silicon probes bilaterally in the CA1 pyramidal layer of the dorsal hippocampus.
  Group /general/extracellular_ephys/shank6 (ElectrodeGroup) shank6 electrodes
  Group /general/extracellular_ephys/shank6/device (Device) The five rats were implanted with multi-shank 64-site silicon probes bilaterally in the CA1 pyramidal layer of the dorsal hippocampus.
  Group /general/extracellular_ephys/shank7 (ElectrodeGroup) shank7 electrodes
  Group /general/extracellular_ephys/shank7/device (Device) The five rats were implanted with multi-shank 64-site silicon probes bilaterally in the CA1 pyramidal layer of the dorsal hippocampus.
  institution: NYU
  lab: Buzsaki
  related_publications: ['Cooling of Medial Septum Reveals Theta Phase Lag Coordination of Hippocampal Cell Assemblies.Petersen P, Buzsaki G, Neuron. 2020']
  session_id: Peter_MS10_170307_154746_concat
  Group /general/subject (Subject) 
  identifier: 5ad7ea46-dfe0-4bb9-9db9-ae8432b3a0f1
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/condition (VectorData) Whether the maze condition was left or right. | shape = (37,) | dtype = object
  Dataset /intervals/trials/cooling state (VectorData) The labeled cooling state of the subject during the trial. | shape = (37,) | dtype = object
  Dataset /intervals/trials/error (VectorData) Whether the subject made a mistake. | shape = (37,) | dtype = bool
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (37,) | dtype = int32
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (37,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (37,) | dtype = float64
  Group /processing/behavior (ProcessingModule) Contains processed behavioral data.
  Group /processing/behavior/Acceleration (TimeSeries) Instantaneous acceleration of subject through the maze.
  Group /processing/behavior/SubjectPosition (Position) 
  Group /processing/behavior/SubjectPosition/SpatialSeries (SpatialSeries) (x,y,z) coordinates tracking subject movement through the maze.
  Group /processing/behavior/SubjectSpeed (TimeSeries) Instantaneous speed of subject through the maze.
  Group /processing/behavior/Temperature (TimeSeries) Internal brain temperature throughout the session.
  session_description: Petersen et al. demonstrate that cooling of the medial septum slows theta oscillation and increases choice errors without affecting spatial features of pyramidal neurons. Cooling affects distance-time, but not distance-theta phase, compression. The findings reveal that cell assemblies are organized by theta phase and not by external (clock) time.
  session_start_time: 2017-03-07T15:47:46-05:00
  timestamps_reference_time: 2017-03-07T15:47:46-05:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/amplitudes (VectorData) no description | shape = (2101575,) | dtype = float64
  Dataset /units/amplitudes_index (VectorIndex) Index for VectorData 'amplitudes' | shape = (409,) | dtype = uint64
  Dataset /units/id (ElementIdentifiers)  | shape = (409,) | dtype = int64
  Dataset /units/pc_features (VectorData) no description | shape = (2101575, 3, 12) | dtype = float32
  Dataset /units/pc_features_index (VectorIndex) Index for VectorData 'pc_features' | shape = (409,) | dtype = uint64
  Dataset /units/quality (VectorData) Quality of the unit as defined by phy (good, mua, noise). | shape = (409,) | dtype = object
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (2101575,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (409,) | dtype = uint32


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeries (ElectricalSeries) Raw acquisition traces.
  Dataset /acquisition/ElectricalSeries/electrodes (DynamicTableRegion) electrode_table_region | shape = (64,) | dtype = int64
  file_create_date: ['2021-02-17T08:28:36.635240-05:00']
  Group /general/devices/Device (Device) The five rats were implanted with multi-shank 64-site silicon probes bilaterally in the CA1 pyramidal layer of the dorsal hippocampus.
  experimenter: ['Peter Petersen']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (64,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/shank_electrode_number (VectorData) 0-indexed channel within a shank. | shape = (64,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/theta_reference (VectorData) Channel used as theta reference. | shape = (64,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (64,) | dtype = float64
  Group /general/extracellular_ephys/shank1 (ElectrodeGroup) shank1 electrodes
  Group /general/extracellular_ephys/shank1/device (Device) The five rats were implanted with multi-shank 64-site silicon probes bilaterally in the CA1 pyramidal layer of the dorsal hippocampus.
  Group /general/extracellular_ephys/shank2 (ElectrodeGroup) shank2 electrodes
  Group /general/extracellular_ephys/shank2/device (Device) The five rats were implanted with multi-shank 64-site silicon probes bilaterally in the CA1 pyramidal layer of the dorsal hippocampus.
  Group /general/extracellular_ephys/shank3 (ElectrodeGroup) shank3 electrodes
  Group /general/extracellular_ephys/shank3/device (Device) The five rats were implanted with multi-shank 64-site silicon probes bilaterally in the CA1 pyramidal layer of the dorsal hippocampus.
  Group /general/extracellular_ephys/shank4 (ElectrodeGroup) shank4 electrodes
  Group /general/extracellular_ephys/shank4/device (Device) The five rats were implanted with multi-shank 64-site silicon probes bilaterally in the CA1 pyramidal layer of the dorsal hippocampus.
  Group /general/extracellular_ephys/shank5 (ElectrodeGroup) shank5 electrodes
  Group /general/extracellular_ephys/shank5/device (Device) The five rats were implanted with multi-shank 64-site silicon probes bilaterally in the CA1 pyramidal layer of the dorsal hippocampus.
  Group /general/extracellular_ephys/shank6 (ElectrodeGroup) shank6 electrodes
  Group /general/extracellular_ephys/shank6/device (Device) The five rats were implanted with multi-shank 64-site silicon probes bilaterally in the CA1 pyramidal layer of the dorsal hippocampus.
  Group /general/extracellular_ephys/shank7 (ElectrodeGroup) shank7 electrodes
  Group /general/extracellular_ephys/shank7/device (Device) The five rats were implanted with multi-shank 64-site silicon probes bilaterally in the CA1 pyramidal layer of the dorsal hippocampus.
  institution: NYU
  lab: Buzsaki
  related_publications: ['Cooling of Medial Septum Reveals Theta Phase Lag Coordination of Hippocampal Cell Assemblies.Petersen P, Buzsaki G, Neuron. 2020']
  session_id: Peter_MS10_170307_154746_concat
  Group /general/subject (Subject) 
  identifier: df03d979-f4a7-4d8a-a530-ad8cedcb4bc6
  Group /processing/ecephys (ProcessingModule) Intermediate data from extracellular electrophysiology recordings, e.g., LFP.
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/LFP (ElectricalSeries) Local field potential signal.
  Dataset /processing/ecephys/LFP/LFP/electrodes (DynamicTableRegion) electrode_table_region | shape = (64,) | dtype = int64
  session_description: Petersen et al. demonstrate that cooling of the medial septum slows theta oscillation and increases choice errors without affecting spatial features of pyramidal neurons. Cooling affects distance-time, but not distance-theta phase, compression. The findings reveal that cell assemblies are organized by theta phase and not by external (clock) time.
  session_start_time: 2017-03-07T15:47:46-05:00
  timestamps_reference_time: 2017-03-07T15:47:46-05:00


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2021-02-17T10:14:10.070398-05:00']
  Group /general/devices/Device (Device) The five rats were implanted with multi-shank 64-site silicon probes bilaterally in the CA1 pyramidal layer of the dorsal hippocampus.
  experimenter: ['Peter Petersen']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (64,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/shank_electrode_number (VectorData) 0-indexed channel within a shank. | shape = (64,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/theta_reference (VectorData) Channel used as theta reference. | shape = (64,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (64,) | dtype = float64
  Group /general/extracellular_ephys/shank1 (ElectrodeGroup) shank1 electrodes
  Group /general/extracellular_ephys/shank1/device (Device) The five rats were implanted with multi-shank 64-site silicon probes bilaterally in the CA1 pyramidal layer of the dorsal hippocampus.
  Group /general/extracellular_ephys/shank2 (ElectrodeGroup) shank2 electrodes
  Group /general/extracellular_ephys/shank2/device (Device) The five rats were implanted with multi-shank 64-site silicon probes bilaterally in the CA1 pyramidal layer of the dorsal hippocampus.
  Group /general/extracellular_ephys/shank3 (ElectrodeGroup) shank3 electrodes
  Group /general/extracellular_ephys/shank3/device (Device) The five rats were implanted with multi-shank 64-site silicon probes bilaterally in the CA1 pyramidal layer of the dorsal hippocampus.
  Group /general/extracellular_ephys/shank4 (ElectrodeGroup) shank4 electrodes
  Group /general/extracellular_ephys/shank4/device (Device) The five rats were implanted with multi-shank 64-site silicon probes bilaterally in the CA1 pyramidal layer of the dorsal hippocampus.
  Group /general/extracellular_ephys/shank5 (ElectrodeGroup) shank5 electrodes
  Group /general/extracellular_ephys/shank5/device (Device) The five rats were implanted with multi-shank 64-site silicon probes bilaterally in the CA1 pyramidal layer of the dorsal hippocampus.
  Group /general/extracellular_ephys/shank6 (ElectrodeGroup) shank6 electrodes
  Group /general/extracellular_ephys/shank6/device (Device) The five rats were implanted with multi-shank 64-site silicon probes bilaterally in the CA1 pyramidal layer of the dorsal hippocampus.
  Group /general/extracellular_ephys/shank7 (ElectrodeGroup) shank7 electrodes
  Group /general/extracellular_ephys/shank7/device (Device) The five rats were implanted with multi-shank 64-site silicon probes bilaterally in the CA1 pyramidal layer of the dorsal hippocampus.
  institution: NYU
  lab: Buzsaki
  related_publications: ['Cooling of Medial Septum Reveals Theta Phase Lag Coordination of Hippocampal Cell Assemblies.Petersen P, Buzsaki G, Neuron. 2020']
  session_id: Peter_MS10_170311_180956_concat
  Group /general/subject (Subject) 
  identifier: f4edd41f-b260-4d0c-9bea-9d5049c7ddf6
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/condition (VectorData) Whether the maze condition was left or right. | shape = (130,) | dtype = object
  Dataset /intervals/trials/cooling state (VectorData) The labeled cooling state of the subject during the trial. | shape = (130,) | dtype = object
  Dataset /intervals/trials/error (VectorData) Whether the subject made a mistake. | shape = (130,) | dtype = bool
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (130,) | dtype = int32
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (130,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (130,) | dtype = float64
  Group /processing/behavior (ProcessingModule) Contains processed behavioral data.
  Group /processing/behavior/Acceleration (TimeSeries) Instantaneous acceleration of subject through the maze.
  Group /processing/behavior/SubjectPosition (Position) 
  Group /processing/behavior/SubjectPosition/SpatialSeries (SpatialSeries) (x,y,z) coordinates tracking subject movement through the maze.
  Group /processing/behavior/SubjectSpeed (TimeSeries) Instantaneous speed of subject through the maze.
  Group /processing/behavior/Temperature (TimeSeries) Internal brain temperature throughout the session.
  session_description: Petersen et al. demonstrate that cooling of the medial septum slows theta oscillation and increases choice errors without affecting spatial features of pyramidal neurons. Cooling affects distance-time, but not distance-theta phase, compression. The findings reveal that cell assemblies are organized by theta phase and not by external (clock) time.
  session_start_time: 2017-03-11T18:09:56-05:00
  timestamps_reference_time: 2017-03-11T18:09:56-05:00


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2021-02-17T13:56:22.998400-05:00']
  Group /general/devices/Device (Device) The five rats were implanted with multi-shank 64-site silicon probes bilaterally in the CA1 pyramidal layer of the dorsal hippocampus.
  experimenter: ['Peter Petersen']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (47,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (47,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (47,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (47,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (47,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (47,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/shank_electrode_number (VectorData) 0-indexed channel within a shank. | shape = (47,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/theta_reference (VectorData) Channel used as theta reference. | shape = (47,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (47,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (47,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (47,) | dtype = float64
  Group /general/extracellular_ephys/shank1 (ElectrodeGroup) shank1 electrodes
  Group /general/extracellular_ephys/shank1/device (Device) The five rats were implanted with multi-shank 64-site silicon probes bilaterally in the CA1 pyramidal layer of the dorsal hippocampus.
  Group /general/extracellular_ephys/shank2 (ElectrodeGroup) shank2 electrodes
  Group /general/extracellular_ephys/shank2/device (Device) The five rats were implanted with multi-shank 64-site silicon probes bilaterally in the CA1 pyramidal layer of the dorsal hippocampus.
  Group /general/extracellular_ephys/shank3 (ElectrodeGroup) shank3 electrodes
  Group /general/extracellular_ephys/shank3/device (Device) The five rats were implanted with multi-shank 64-site silicon probes bilaterally in the CA1 pyramidal layer of the dorsal hippocampus.
  Group /general/extracellular_ephys/shank4 (ElectrodeGroup) shank4 electrodes
  Group /general/extracellular_ephys/shank4/device (Device) The five rats were implanted with multi-shank 64-site silicon probes bilaterally in the CA1 pyramidal layer of the dorsal hippocampus.
  Group /general/extracellular_ephys/shank5 (ElectrodeGroup) shank5 electrodes
  Group /general/extracellular_ephys/shank5/device (Device) The five rats were implanted with multi-shank 64-site silicon probes bilaterally in the CA1 pyramidal layer of the dorsal hippocampus.
  Group /general/extracellular_ephys/shank6 (ElectrodeGroup) shank6 electrodes
  Group /general/extracellular_ephys/shank6/device (Device) The five rats were implanted with multi-shank 64-site silicon probes bilaterally in the CA1 pyramidal layer of the dorsal hippocampus.
  institution: NYU
  lab: Buzsaki
  related_publications: ['Cooling of Medial Septum Reveals Theta Phase Lag Coordination of Hippocampal Cell Assemblies.Petersen P, Buzsaki G, Neuron. 2020']
  session_id: Peter_MS10_170314_163038
  Group /general/subject (Subject) 
  identifier: 94f425cc-e68b-4d69-af52-21aeab8c1680
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/condition (VectorData) Whether the maze condition was left or right. | shape = (142,) | dtype = object
  Dataset /intervals/trials/cooling state (VectorData) The labeled cooling state of the subject during the trial. | shape = (142,) | dtype = object
  Dataset /intervals/trials/error (VectorData) Whether the subject made a mistake. | shape = (142,) | dtype = bool
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (142,) | dtype = int64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (142,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (142,) | dtype = float64
  Group /processing/behavior (ProcessingModule) Contains processed behavioral data.
  Group /processing/behavior/Acceleration (TimeSeries) Instantaneous acceleration of subject through the maze.
  Group /processing/behavior/SubjectPosition (Position) 
  Group /processing/behavior/SubjectPosition/SpatialSeries (SpatialSeries) (x,y,z) coordinates tracking subject movement through the maze.
  Group /processing/behavior/SubjectSpeed (TimeSeries) Instantaneous speed of subject through the maze.
  Group /processing/behavior/Temperature (TimeSeries) Internal brain temperature throughout the session.
  session_description: Petersen et al. demonstrate that cooling of the medial septum slows theta oscillation and increases choice errors without affecting spatial features of pyramidal neurons. Cooling affects distance-time, but not distance-theta phase, compression. The findings reveal that cell assemblies are organized by theta phase and not by external (clock) time.
  session_start_time: 2017-03-14T16:30:38-04:00
  timestamps_reference_time: 2017-03-14T16:30:38-04:00


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeries (ElectricalSeries) Raw acquisition traces.
  Dataset /acquisition/ElectricalSeries/electrodes (DynamicTableRegion) electrode_table_region | shape = (47,) | dtype = int64
  file_create_date: ['2021-02-17T13:56:22.998400-05:00']
  Group /general/devices/Device (Device) The five rats were implanted with multi-shank 64-site silicon probes bilaterally in the CA1 pyramidal layer of the dorsal hippocampus.
  experimenter: ['Peter Petersen']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (47,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (47,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (47,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (47,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (47,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (47,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/shank_electrode_number (VectorData) 0-indexed channel within a shank. | shape = (47,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/theta_reference (VectorData) Channel used as theta reference. | shape = (47,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (47,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (47,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (47,) | dtype = float64
  Group /general/extracellular_ephys/shank1 (ElectrodeGroup) shank1 electrodes
  Group /general/extracellular_ephys/shank1/device (Device) The five rats were implanted with multi-shank 64-site silicon probes bilaterally in the CA1 pyramidal layer of the dorsal hippocampus.
  Group /general/extracellular_ephys/shank2 (ElectrodeGroup) shank2 electrodes
  Group /general/extracellular_ephys/shank2/device (Device) The five rats were implanted with multi-shank 64-site silicon probes bilaterally in the CA1 pyramidal layer of the dorsal hippocampus.
  Group /general/extracellular_ephys/shank3 (ElectrodeGroup) shank3 electrodes
  Group /general/extracellular_ephys/shank3/device (Device) The five rats were implanted with multi-shank 64-site silicon probes bilaterally in the CA1 pyramidal layer of the dorsal hippocampus.
  Group /general/extracellular_ephys/shank4 (ElectrodeGroup) shank4 electrodes
  Group /general/extracellular_ephys/shank4/device (Device) The five rats were implanted with multi-shank 64-site silicon probes bilaterally in the CA1 pyramidal layer of the dorsal hippocampus.
  Group /general/extracellular_ephys/shank5 (ElectrodeGroup) shank5 electrodes
  Group /general/extracellular_ephys/shank5/device (Device) The five rats were implanted with multi-shank 64-site silicon probes bilaterally in the CA1 pyramidal layer of the dorsal hippocampus.
  Group /general/extracellular_ephys/shank6 (ElectrodeGroup) shank6 electrodes
  Group /general/extracellular_ephys/shank6/device (Device) The five rats were implanted with multi-shank 64-site silicon probes bilaterally in the CA1 pyramidal layer of the dorsal hippocampus.
  institution: NYU
  lab: Buzsaki
  related_publications: ['Cooling of Medial Septum Reveals Theta Phase Lag Coordination of Hippocampal Cell Assemblies.Petersen P, Buzsaki G, Neuron. 2020']
  session_id: Peter_MS10_170314_163038
  Group /general/subject (Subject) 
  identifier: 8af6f754-096c-4426-b324-458d6ec81c66
  Group /processing/ecephys (ProcessingModule) Intermediate data from extracellular electrophysiology recordings, e.g., LFP.
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/LFP (ElectricalSeries) Local field potential signal.
  Dataset /processing/ecephys/LFP/LFP/electrodes (DynamicTableRegion) electrode_table_region | shape = (47,) | dtype = int64
  session_description: Petersen et al. demonstrate that cooling of the medial septum slows theta oscillation and increases choice errors without affecting spatial features of pyramidal neurons. Cooling affects distance-time, but not distance-theta phase, compression. The findings reveal that cell assemblies are organized by theta phase and not by external (clock) time.
  session_start_time: 2017-03-14T16:30:38-04:00
  timestamps_reference_time: 2017-03-14T16:30:38-04:00
