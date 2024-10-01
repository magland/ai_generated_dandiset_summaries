
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000213/0.220127.1738
name: Transformation of a Spatial Map across the Hippocampal-Lateral Septal Circuit
contributor: [{'name': 'Tingley, David', 'roleName': ['dcite:ContactPerson', 'dcite:Author', 'dcite:DataCollector'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Buzsáki, Gyórgy', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'url': 'https://www.nih.gov/', 'name': 'National Institutes of Health', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01cwqze88', 'awardNumber': ' MH54671, MH107396, and NS 090583', 'contactPoint': [], 'includeInCitation': False}, {'url': 'https://www.nsf.gov/', 'name': 'National Science Foundation', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/021nxhr62', 'awardNumber': 'NSF PIRE grant (#1545858)', 'contactPoint': [], 'includeInCitation': False}, {'url': 'http://www.thesimonsfoundation.ca/', 'name': 'Simons Foundation', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01cmst727', 'awardNumber': '351109', 'contactPoint': [], 'includeInCitation': False}]
description: The hippocampus constructs a map of the environment. How this “cognitive map” is utilized by other brain regions to guide behavior remains unexplored. To examine how neuronal firing patterns in the hippocampus are transmitted and transformed, we recorded neurons in its principal subcortical target, the lateral septum (LS). We observed that LS neurons carry reliable spatial information in the phase of action potentials, relative to hippocampal theta oscillations, while the firing rates of LS neurons remained uninformative. Furthermore, this spatial phase code had an anatomical microstructure within the LS and was bound to the hippocampal spatial code by synchronous gamma frequency cell assemblies. Using a data-driven model, we show that rate-independent spatial tuning arises through the dynamic weighting of CA1 and CA3 cell assemblies. Our findings demonstrate that transformation of the hippocampal spatial map depends on higher-order theta-dependent neuronal sequences.
assetsSummary: {'species': [{'name': 'Rattus norvegicus - Norway rat', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10116'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}, {'name': 'behavioral approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 1527009268863, 'numberOfFiles': 67, 'numberOfSubjects': 5, 'variableMeasured': ['Position', 'CompassDirection', 'ElectricalSeries', 'LFP', 'Units', 'SpatialSeries'], 'measurementTechnique': [{'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'signal filtering technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000213 has 24 NWB files.
11 of these NWB files are of type 1.
1 of these NWB files are of type 2.
1 of these NWB files are of type 3.
1 of these NWB files are of type 4.
10 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeries_raw (ElectricalSeries) Raw acquisition traces.
  Dataset /acquisition/ElectricalSeries_raw/electrodes (DynamicTableRegion) electrode_table_region | shape = (128,) | dtype = int64
  file_create_date: ['2022-01-16T09:33:25.529802+00:00']
  Group /general/devices/Neuronexus probe (4 x 1) (Device) according to author thse are reference sites a few millimeters dorsal from the restrecorded from an older neuronexus probe
  Group /general/devices/Neuronexus probe (5 x 12) (Device) A 5 (shanks) x 12 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/devices/Neuronexus probe (6 x 10) (Device) A 6 (shanks) x 10 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  experimenter: ['David Tingley']
  Group /general/extracellular_ephys/Group1 (ElectrodeGroup) Group1 electrodes.
  Group /general/extracellular_ephys/Group1/device (Device) A 5 (shanks) x 12 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group10 (ElectrodeGroup) Group10 electrodes.
  Group /general/extracellular_ephys/Group10/device (Device) A 6 (shanks) x 10 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group11 (ElectrodeGroup) Group11 electrodes.
  Group /general/extracellular_ephys/Group11/device (Device) A 6 (shanks) x 10 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group12 (ElectrodeGroup) Group12 electrodes.
  Group /general/extracellular_ephys/Group12/device (Device) A 6 (shanks) x 10 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group13 (ElectrodeGroup) Group13 electrodes.
  Group /general/extracellular_ephys/Group13/device (Device) according to author thse are reference sites a few millimeters dorsal from the restrecorded from an older neuronexus probe
  Group /general/extracellular_ephys/Group2 (ElectrodeGroup) Group2 electrodes.
  Group /general/extracellular_ephys/Group2/device (Device) A 5 (shanks) x 12 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group3 (ElectrodeGroup) Group3 electrodes.
  Group /general/extracellular_ephys/Group3/device (Device) A 5 (shanks) x 12 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group4 (ElectrodeGroup) Group4 electrodes.
  Group /general/extracellular_ephys/Group4/device (Device) A 5 (shanks) x 12 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group5 (ElectrodeGroup) Group5 electrodes.
  Group /general/extracellular_ephys/Group5/device (Device) A 5 (shanks) x 12 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group6 (ElectrodeGroup) Group6 electrodes.
  Group /general/extracellular_ephys/Group6/device (Device) according to author thse are reference sites a few millimeters dorsal from the restrecorded from an older neuronexus probe
  Group /general/extracellular_ephys/Group7 (ElectrodeGroup) Group7 electrodes.
  Group /general/extracellular_ephys/Group7/device (Device) A 6 (shanks) x 10 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group8 (ElectrodeGroup) Group8 electrodes.
  Group /general/extracellular_ephys/Group8/device (Device) A 6 (shanks) x 10 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group9 (ElectrodeGroup) Group9 electrodes.
  Group /general/extracellular_ephys/Group9/device (Device) A 6 (shanks) x 10 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/shank_electrode_number (VectorData) 0-indexed channel within a shank. | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (128,) | dtype = float64
  institution: NYU
  lab: Buzsaki
  related_publications: ['Tingley, David, and György Buzsáki. "Transformation of a spatial map across the hippocampal-lateral septal circuit." Neuron 98.6 (2018) 1229-1242.']
  session_id: DT2_rPPC_rCCG_3324um_1000um_20160217_160217_103121
  Group /general/subject (Subject) 
  identifier: b6fd3759-3c09-4481-aab0-673f36566c40
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (3,) | dtype = int64
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (3,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (3,) | dtype = float64
  Dataset /intervals/epochs/tags (VectorData) user-defined tags | shape = (3,) | dtype = object
  Dataset /intervals/epochs/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (3,) | dtype = uint8
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/direction (VectorData) direction of the trial | shape = (69,) | dtype = object
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (69,) | dtype = int64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (69,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (69,) | dtype = float64
  Dataset /intervals/trials/trial_type (VectorData) type of trial | shape = (69,) | dtype = object
  Group /processing/behavior (ProcessingModule) Contains behavioral data concerning position.
  Group /processing/behavior/wheel_alternation_task (Position) 
  Group /processing/behavior/wheel_alternation_task/position (SpatialSeries) (x,y,z) coordinates tracking subject movement.
  Group /processing/ecephys (ProcessingModule) Intermediate data from extracellular electrophysiology recordings, e.g., LFP.
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/ElectricalSeries_lfp (ElectricalSeries) Local field potential signal.
  Dataset /processing/ecephys/LFP/ElectricalSeries_lfp/electrodes (DynamicTableRegion) electrode_table_region | shape = (128,) | dtype = int64
  Group /processing/ecephys/sleep_states (TimeIntervals) Sleep state of the animal.
  Dataset /processing/ecephys/sleep_states/id (ElementIdentifiers)  | shape = (169,) | dtype = int64
  Dataset /processing/ecephys/sleep_states/label (VectorData) Sleep state. | shape = (169,) | dtype = object
  Dataset /processing/ecephys/sleep_states/start_time (VectorData) Start time of epoch, in seconds | shape = (169,) | dtype = float64
  Dataset /processing/ecephys/sleep_states/stop_time (VectorData) Stop time of epoch, in seconds | shape = (169,) | dtype = float64
  session_description: The hippocampus constructs a map of the environment. How this “cognitive map” is utilized by other brain regions to guide behavior remains unexplored. To examine how neuronal firing patterns in the hippocampus are transmitted and transformed, we recorded neurons in its principal subcortical target, the lateral septum (LS). We observed that LS neurons carry reliable spatial information in the phase of action potentials, relative to hippocampal theta oscillations, while the firing rates of LS neurons remained uninformative. Furthermore, this spatial phase code had an anatomical microstructure within the LS and was bound to the hippocampal spatial code by synchronous gamma frequency cell assemblies. Using a data-driven model, we show that rate-independent spatial tuning arises through the dynamic weighting of CA1 and CA3 cell assemblies. Our findings demonstrate that transformation of the hippocampal spatial map depends on higher-order theta-dependent neuronal sequences.
  session_start_time: 2016-02-17T10:31:21-05:00
  timestamps_reference_time: 2016-02-17T10:31:21-05:00
  Group /units (Units) Autogenerated by nwb_conversion_tools.
  Dataset /units/clu_id (VectorData) 0-indexed id of cluster identified from the shank. | shape = (56,) | dtype = int64
  Dataset /units/group_id (VectorData) The electrode group ID that each unit was identified by. | shape = (56,) | dtype = object
  Dataset /units/id (ElementIdentifiers)  | shape = (56,) | dtype = int64
  Dataset /units/location (VectorData) Brain region where each unit was detected. | shape = (56,) | dtype = object
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (1517627,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (56,) | dtype = uint32


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2022-01-16T09:41:58.128152+00:00']
  Group /general/devices/Cambridge prob (1 x 64) (Device) Silicon probe from Cambridge Neurotech. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with20 kHz rate.
  Group /general/devices/Neuronexus probe (4 x 1) (Device) according to author thse are reference sites a few millimeters dorsal from the restrecorded from an older neuronexus probe
  Group /general/devices/Neuronexus probe (5 x 12) (Device) A 5 (shanks) x 12 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  experimenter: ['David Tingley']
  Group /general/extracellular_ephys/Group1 (ElectrodeGroup) Group1 electrodes.
  Group /general/extracellular_ephys/Group1/device (Device) A 5 (shanks) x 12 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group2 (ElectrodeGroup) Group2 electrodes.
  Group /general/extracellular_ephys/Group2/device (Device) A 5 (shanks) x 12 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group3 (ElectrodeGroup) Group3 electrodes.
  Group /general/extracellular_ephys/Group3/device (Device) A 5 (shanks) x 12 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group4 (ElectrodeGroup) Group4 electrodes.
  Group /general/extracellular_ephys/Group4/device (Device) A 5 (shanks) x 12 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group5 (ElectrodeGroup) Group5 electrodes.
  Group /general/extracellular_ephys/Group5/device (Device) A 5 (shanks) x 12 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group6 (ElectrodeGroup) Group6 electrodes.
  Group /general/extracellular_ephys/Group6/device (Device) according to author thse are reference sites a few millimeters dorsal from the restrecorded from an older neuronexus probe
  Group /general/extracellular_ephys/Group7 (ElectrodeGroup) Group7 electrodes.
  Group /general/extracellular_ephys/Group7/device (Device) Silicon probe from Cambridge Neurotech. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with20 kHz rate.
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/shank_electrode_number (VectorData) 0-indexed channel within a shank. | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (128,) | dtype = float64
  institution: NYU
  lab: Buzsaki
  related_publications: ['Tingley, David, and György Buzsáki. "Transformation of a spatial map across the hippocampal-lateral septal circuit." Neuron 98.6 (2018) 1229-1242.']
  session_id: 20170324_576um_144um_170324_123932
  Group /general/subject (Subject) 
  identifier: fd6020df-839b-4496-b9d9-534e21aa955b
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (3,) | dtype = int64
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (3,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (3,) | dtype = float64
  Dataset /intervals/epochs/tags (VectorData) user-defined tags | shape = (3,) | dtype = object
  Dataset /intervals/epochs/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (3,) | dtype = uint8
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/direction (VectorData) direction of the trial | shape = (121,) | dtype = object
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (121,) | dtype = int64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (121,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (121,) | dtype = float64
  Dataset /intervals/trials/trial_type (VectorData) type of trial | shape = (121,) | dtype = object
  Group /processing/behavior (ProcessingModule) Contains behavioral data concerning position.
  Group /processing/behavior/allocentric_frame_tracking (CompassDirection) 
  Group /processing/behavior/allocentric_frame_tracking/orientation (SpatialSeries) (x, y, z, w) orientation coordinates, orientation type: quaternion
  Group /processing/behavior/wheel_alternation_task (Position) 
  Group /processing/behavior/wheel_alternation_task/error_per_marker (SpatialSeries) Estimated error for marker tracking from optitrack system.
  Group /processing/behavior/wheel_alternation_task/position (SpatialSeries) (x,y,z) coordinates tracking subject movement.
  Group /processing/ecephys (ProcessingModule) Intermediate data from extracellular electrophysiology recordings, e.g., LFP.
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/ElectricalSeries_lfp (ElectricalSeries) Local field potential signal.
  Dataset /processing/ecephys/LFP/ElectricalSeries_lfp/electrodes (DynamicTableRegion) electrode_table_region | shape = (128,) | dtype = int64
  Group /processing/ecephys/sleep_states (TimeIntervals) Sleep state of the animal.
  Dataset /processing/ecephys/sleep_states/id (ElementIdentifiers)  | shape = (49,) | dtype = int64
  Dataset /processing/ecephys/sleep_states/label (VectorData) Sleep state. | shape = (49,) | dtype = object
  Dataset /processing/ecephys/sleep_states/start_time (VectorData) Start time of epoch, in seconds | shape = (49,) | dtype = float64
  Dataset /processing/ecephys/sleep_states/stop_time (VectorData) Stop time of epoch, in seconds | shape = (49,) | dtype = float64
  session_description: The hippocampus constructs a map of the environment. How this “cognitive map” is utilized by other brain regions to guide behavior remains unexplored. To examine how neuronal firing patterns in the hippocampus are transmitted and transformed, we recorded neurons in its principal subcortical target, the lateral septum (LS). We observed that LS neurons carry reliable spatial information in the phase of action potentials, relative to hippocampal theta oscillations, while the firing rates of LS neurons remained uninformative. Furthermore, this spatial phase code had an anatomical microstructure within the LS and was bound to the hippocampal spatial code by synchronous gamma frequency cell assemblies. Using a data-driven model, we show that rate-independent spatial tuning arises through the dynamic weighting of CA1 and CA3 cell assemblies. Our findings demonstrate that transformation of the hippocampal spatial map depends on higher-order theta-dependent neuronal sequences.
  session_start_time: 2017-03-24T12:39:32-04:00
  timestamps_reference_time: 2017-03-24T12:39:32-04:00


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2022-01-16T09:33:28.009621+00:00']
  Group /general/devices/Cambridge prob (1 x 64) (Device) Silicon probe from Cambridge Neurotech. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with20 kHz rate.
  Group /general/devices/Neuronexus probe (4 x 1) (Device) according to author thse are reference sites a few millimeters dorsal from the restrecorded from an older neuronexus probe
  Group /general/devices/Neuronexus probe (5 x 12) (Device) A 5 (shanks) x 12 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  experimenter: ['David Tingley']
  Group /general/extracellular_ephys/Group1 (ElectrodeGroup) Group1 electrodes.
  Group /general/extracellular_ephys/Group1/device (Device) A 5 (shanks) x 12 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group2 (ElectrodeGroup) Group2 electrodes.
  Group /general/extracellular_ephys/Group2/device (Device) A 5 (shanks) x 12 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group3 (ElectrodeGroup) Group3 electrodes.
  Group /general/extracellular_ephys/Group3/device (Device) A 5 (shanks) x 12 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group4 (ElectrodeGroup) Group4 electrodes.
  Group /general/extracellular_ephys/Group4/device (Device) A 5 (shanks) x 12 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group5 (ElectrodeGroup) Group5 electrodes.
  Group /general/extracellular_ephys/Group5/device (Device) A 5 (shanks) x 12 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group6 (ElectrodeGroup) Group6 electrodes.
  Group /general/extracellular_ephys/Group6/device (Device) according to author thse are reference sites a few millimeters dorsal from the restrecorded from an older neuronexus probe
  Group /general/extracellular_ephys/Group7 (ElectrodeGroup) Group7 electrodes.
  Group /general/extracellular_ephys/Group7/device (Device) Silicon probe from Cambridge Neurotech. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with20 kHz rate.
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/shank_electrode_number (VectorData) 0-indexed channel within a shank. | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (128,) | dtype = float64
  institution: NYU
  lab: Buzsaki
  related_publications: ['Tingley, David, and György Buzsáki. "Transformation of a spatial map across the hippocampal-lateral septal circuit." Neuron 98.6 (2018) 1229-1242.']
  session_id: 20170401_864um_936um_merge
  Group /general/subject (Subject) 
  identifier: cea539b5-cdc2-463a-b9c7-b32a48f9969d
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (3,) | dtype = int64
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (3,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (3,) | dtype = float64
  Dataset /intervals/epochs/tags (VectorData) user-defined tags | shape = (3,) | dtype = object
  Dataset /intervals/epochs/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (3,) | dtype = uint8
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (81,) | dtype = int64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (81,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (81,) | dtype = float64
  Group /processing/behavior (ProcessingModule) Contains behavioral data concerning position.
  Group /processing/behavior/allocentric_frame_tracking (CompassDirection) 
  Group /processing/behavior/allocentric_frame_tracking/orientation (SpatialSeries) (x, y, z, w) orientation coordinates, orientation type: quaternion
  Group /processing/behavior/linear_task (Position) 
  Group /processing/behavior/linear_task/error_per_marker (SpatialSeries) Estimated error for marker tracking from optitrack system.
  Group /processing/behavior/linear_task/position (SpatialSeries) (x,y,z) coordinates tracking subject movement.
  Group /processing/ecephys (ProcessingModule) Intermediate data from extracellular electrophysiology recordings, e.g., LFP.
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/ElectricalSeries_lfp (ElectricalSeries) Local field potential signal.
  Dataset /processing/ecephys/LFP/ElectricalSeries_lfp/electrodes (DynamicTableRegion) electrode_table_region | shape = (128,) | dtype = int64
  Group /processing/ecephys/sleep_states (TimeIntervals) Sleep state of the animal.
  Dataset /processing/ecephys/sleep_states/id (ElementIdentifiers)  | shape = (71,) | dtype = int64
  Dataset /processing/ecephys/sleep_states/label (VectorData) Sleep state. | shape = (71,) | dtype = object
  Dataset /processing/ecephys/sleep_states/start_time (VectorData) Start time of epoch, in seconds | shape = (71,) | dtype = float64
  Dataset /processing/ecephys/sleep_states/stop_time (VectorData) Stop time of epoch, in seconds | shape = (71,) | dtype = float64
  session_description: The hippocampus constructs a map of the environment. How this “cognitive map” is utilized by other brain regions to guide behavior remains unexplored. To examine how neuronal firing patterns in the hippocampus are transmitted and transformed, we recorded neurons in its principal subcortical target, the lateral septum (LS). We observed that LS neurons carry reliable spatial information in the phase of action potentials, relative to hippocampal theta oscillations, while the firing rates of LS neurons remained uninformative. Furthermore, this spatial phase code had an anatomical microstructure within the LS and was bound to the hippocampal spatial code by synchronous gamma frequency cell assemblies. Using a data-driven model, we show that rate-independent spatial tuning arises through the dynamic weighting of CA1 and CA3 cell assemblies. Our findings demonstrate that transformation of the hippocampal spatial map depends on higher-order theta-dependent neuronal sequences.
  session_start_time: 2017-04-01T00:00:00-04:00
  timestamps_reference_time: 2017-04-01T00:00:00-04:00
  Group /units (Units) Autogenerated by nwb_conversion_tools.
  Dataset /units/clu_id (VectorData) 0-indexed id of cluster identified from the shank. | shape = (47,) | dtype = int64
  Dataset /units/group_id (VectorData) The electrode group ID that each unit was identified by. | shape = (47,) | dtype = object
  Dataset /units/id (ElementIdentifiers)  | shape = (47,) | dtype = int64
  Dataset /units/location (VectorData) Brain region where each unit was detected. | shape = (47,) | dtype = object
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (1566927,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (47,) | dtype = uint32


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2022-01-16T09:42:42.556213+00:00']
  Group /general/devices/Cambridge prob (1 x 64) (Device) Silicon probe from Cambridge Neurotech. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with20 kHz rate.
  Group /general/devices/Neuronexus probe (4 x 1) (Device) according to author thse are reference sites a few millimeters dorsal from the restrecorded from an older neuronexus probe
  Group /general/devices/Neuronexus probe (5 x 12) (Device) A 5 (shanks) x 12 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  experimenter: ['David Tingley']
  Group /general/extracellular_ephys/Group1 (ElectrodeGroup) Group1 electrodes.
  Group /general/extracellular_ephys/Group1/device (Device) A 5 (shanks) x 12 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group2 (ElectrodeGroup) Group2 electrodes.
  Group /general/extracellular_ephys/Group2/device (Device) A 5 (shanks) x 12 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group3 (ElectrodeGroup) Group3 electrodes.
  Group /general/extracellular_ephys/Group3/device (Device) A 5 (shanks) x 12 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group4 (ElectrodeGroup) Group4 electrodes.
  Group /general/extracellular_ephys/Group4/device (Device) A 5 (shanks) x 12 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group5 (ElectrodeGroup) Group5 electrodes.
  Group /general/extracellular_ephys/Group5/device (Device) A 5 (shanks) x 12 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group6 (ElectrodeGroup) Group6 electrodes.
  Group /general/extracellular_ephys/Group6/device (Device) according to author thse are reference sites a few millimeters dorsal from the restrecorded from an older neuronexus probe
  Group /general/extracellular_ephys/Group7 (ElectrodeGroup) Group7 electrodes.
  Group /general/extracellular_ephys/Group7/device (Device) Silicon probe from Cambridge Neurotech. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with20 kHz rate.
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/shank_electrode_number (VectorData) 0-indexed channel within a shank. | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (128,) | dtype = float64
  institution: NYU
  lab: Buzsaki
  related_publications: ['Tingley, David, and György Buzsáki. "Transformation of a spatial map across the hippocampal-lateral septal circuit." Neuron 98.6 (2018) 1229-1242.']
  session_id: 20170412_1440um_1170um_170412_103153
  Group /general/subject (Subject) 
  identifier: f697403b-75f3-4304-a673-f3448a1983a1
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (3,) | dtype = int64
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (3,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (3,) | dtype = float64
  Dataset /intervals/epochs/tags (VectorData) user-defined tags | shape = (3,) | dtype = object
  Dataset /intervals/epochs/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (3,) | dtype = uint8
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/direction (VectorData) direction of the trial | shape = (76,) | dtype = object
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (76,) | dtype = int64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (76,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (76,) | dtype = float64
  Dataset /intervals/trials/trial_type (VectorData) type of trial | shape = (76,) | dtype = object
  Group /processing/behavior (ProcessingModule) Contains behavioral data concerning position.
  Group /processing/behavior/allocentric_frame_tracking (CompassDirection) 
  Group /processing/behavior/allocentric_frame_tracking/orientation (SpatialSeries) (x, y, z, w) orientation coordinates, orientation type: quaternion
  Group /processing/behavior/both_alternation_task (Position) 
  Group /processing/behavior/both_alternation_task/error_per_marker (SpatialSeries) Estimated error for marker tracking from optitrack system.
  Group /processing/behavior/both_alternation_task/position (SpatialSeries) (x,y,z) coordinates tracking subject movement.
  Group /processing/ecephys (ProcessingModule) Intermediate data from extracellular electrophysiology recordings, e.g., LFP.
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/ElectricalSeries_lfp (ElectricalSeries) Local field potential signal.
  Dataset /processing/ecephys/LFP/ElectricalSeries_lfp/electrodes (DynamicTableRegion) electrode_table_region | shape = (128,) | dtype = int64
  Group /processing/ecephys/sleep_states (TimeIntervals) Sleep state of the animal.
  Dataset /processing/ecephys/sleep_states/id (ElementIdentifiers)  | shape = (206,) | dtype = int64
  Dataset /processing/ecephys/sleep_states/label (VectorData) Sleep state. | shape = (206,) | dtype = object
  Dataset /processing/ecephys/sleep_states/start_time (VectorData) Start time of epoch, in seconds | shape = (206,) | dtype = float64
  Dataset /processing/ecephys/sleep_states/stop_time (VectorData) Stop time of epoch, in seconds | shape = (206,) | dtype = float64
  session_description: The hippocampus constructs a map of the environment. How this “cognitive map” is utilized by other brain regions to guide behavior remains unexplored. To examine how neuronal firing patterns in the hippocampus are transmitted and transformed, we recorded neurons in its principal subcortical target, the lateral septum (LS). We observed that LS neurons carry reliable spatial information in the phase of action potentials, relative to hippocampal theta oscillations, while the firing rates of LS neurons remained uninformative. Furthermore, this spatial phase code had an anatomical microstructure within the LS and was bound to the hippocampal spatial code by synchronous gamma frequency cell assemblies. Using a data-driven model, we show that rate-independent spatial tuning arises through the dynamic weighting of CA1 and CA3 cell assemblies. Our findings demonstrate that transformation of the hippocampal spatial map depends on higher-order theta-dependent neuronal sequences.
  session_start_time: 2017-04-12T10:31:53-04:00
  timestamps_reference_time: 2017-04-12T10:31:53-04:00
  Group /units (Units) Autogenerated by nwb_conversion_tools.
  Dataset /units/clu_id (VectorData) 0-indexed id of cluster identified from the shank. | shape = (223,) | dtype = int64
  Dataset /units/group_id (VectorData) The electrode group ID that each unit was identified by. | shape = (223,) | dtype = object
  Dataset /units/id (ElementIdentifiers)  | shape = (223,) | dtype = int64
  Dataset /units/location (VectorData) Brain region where each unit was detected. | shape = (223,) | dtype = object
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (3362374,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (223,) | dtype = uint32


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2022-01-16T09:33:22.653083+00:00']
  Group /general/devices/Neuronexus probe (4 x 1) (Device) according to author thse are reference sites a few millimeters dorsal from the restrecorded from an older neuronexus probe
  Group /general/devices/Neuronexus probe (4 x 8) (Device) A 4 (shanks) x 8 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/devices/Neuronexus probe (5 x 12) (Device) A 5 (shanks) x 12 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  experimenter: ['David Tingley']
  Group /general/extracellular_ephys/Group1 (ElectrodeGroup) Group1 electrodes.
  Group /general/extracellular_ephys/Group1/device (Device) A 4 (shanks) x 8 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group10 (ElectrodeGroup) Group10 electrodes.
  Group /general/extracellular_ephys/Group10/device (Device) according to author thse are reference sites a few millimeters dorsal from the restrecorded from an older neuronexus probe
  Group /general/extracellular_ephys/Group2 (ElectrodeGroup) Group2 electrodes.
  Group /general/extracellular_ephys/Group2/device (Device) A 4 (shanks) x 8 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group3 (ElectrodeGroup) Group3 electrodes.
  Group /general/extracellular_ephys/Group3/device (Device) A 4 (shanks) x 8 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group4 (ElectrodeGroup) Group4 electrodes.
  Group /general/extracellular_ephys/Group4/device (Device) A 4 (shanks) x 8 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group5 (ElectrodeGroup) Group5 electrodes.
  Group /general/extracellular_ephys/Group5/device (Device) A 5 (shanks) x 12 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group6 (ElectrodeGroup) Group6 electrodes.
  Group /general/extracellular_ephys/Group6/device (Device) A 5 (shanks) x 12 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group7 (ElectrodeGroup) Group7 electrodes.
  Group /general/extracellular_ephys/Group7/device (Device) A 5 (shanks) x 12 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group8 (ElectrodeGroup) Group8 electrodes.
  Group /general/extracellular_ephys/Group8/device (Device) A 5 (shanks) x 12 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group9 (ElectrodeGroup) Group9 electrodes.
  Group /general/extracellular_ephys/Group9/device (Device) A 5 (shanks) x 12 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (96,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (96,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/shank_electrode_number (VectorData) 0-indexed channel within a shank. | shape = (96,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (96,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (96,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (96,) | dtype = float64
  institution: NYU
  lab: Buzsaki
  related_publications: ['Tingley, David, and György Buzsáki. "Transformation of a spatial map across the hippocampal-lateral septal circuit." Neuron 98.6 (2018) 1229-1242.']
  session_id: 20170125_0um_0um_merge
  Group /general/subject (Subject) 
  identifier: db86c595-e223-4908-b24c-e7d056e72293
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (3,) | dtype = int64
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (3,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (3,) | dtype = float64
  Dataset /intervals/epochs/tags (VectorData) user-defined tags | shape = (3,) | dtype = object
  Dataset /intervals/epochs/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (3,) | dtype = uint8
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/direction (VectorData) direction of the trial | shape = (17,) | dtype = object
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (17,) | dtype = int64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (17,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (17,) | dtype = float64
  Dataset /intervals/trials/trial_type (VectorData) type of trial | shape = (17,) | dtype = object
  Group /processing/behavior (ProcessingModule) Contains behavioral data concerning position.
  Group /processing/behavior/allocentric_frame_tracking (CompassDirection) 
  Group /processing/behavior/allocentric_frame_tracking/orientation (SpatialSeries) (x, y, z, w) orientation coordinates, orientation type: quaternion
  Group /processing/behavior/central_alternation_task (Position) 
  Group /processing/behavior/central_alternation_task/error_per_marker (SpatialSeries) Estimated error for marker tracking from optitrack system.
  Group /processing/behavior/central_alternation_task/position (SpatialSeries) (x,y,z) coordinates tracking subject movement.
  Group /processing/ecephys (ProcessingModule) Intermediate data from extracellular electrophysiology recordings, e.g., LFP.
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/ElectricalSeries_lfp (ElectricalSeries) Local field potential signal.
  Dataset /processing/ecephys/LFP/ElectricalSeries_lfp/electrodes (DynamicTableRegion) electrode_table_region | shape = (96,) | dtype = int64
  session_description: The hippocampus constructs a map of the environment. How this “cognitive map” is utilized by other brain regions to guide behavior remains unexplored. To examine how neuronal firing patterns in the hippocampus are transmitted and transformed, we recorded neurons in its principal subcortical target, the lateral septum (LS). We observed that LS neurons carry reliable spatial information in the phase of action potentials, relative to hippocampal theta oscillations, while the firing rates of LS neurons remained uninformative. Furthermore, this spatial phase code had an anatomical microstructure within the LS and was bound to the hippocampal spatial code by synchronous gamma frequency cell assemblies. Using a data-driven model, we show that rate-independent spatial tuning arises through the dynamic weighting of CA1 and CA3 cell assemblies. Our findings demonstrate that transformation of the hippocampal spatial map depends on higher-order theta-dependent neuronal sequences.
  session_start_time: 2017-01-25T00:00:00-05:00
  timestamps_reference_time: 2017-01-25T00:00:00-05:00
  Group /units (Units) Autogenerated by nwb_conversion_tools.
  Dataset /units/clu_id (VectorData) 0-indexed id of cluster identified from the shank. | shape = (28,) | dtype = int64
  Dataset /units/group_id (VectorData) The electrode group ID that each unit was identified by. | shape = (28,) | dtype = object
  Dataset /units/id (ElementIdentifiers)  | shape = (28,) | dtype = int64
  Dataset /units/location (VectorData) Brain region where each unit was detected. | shape = (28,) | dtype = object
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (339665,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (28,) | dtype = uint32
