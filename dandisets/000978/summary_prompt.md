
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000978/0.240511.0307
name: Single Day W-Track Learning
contributor: [{'name': 'Shin, Justin', 'email': 'jdshin@brandeis.edu', 'roleName': ['dcite:ContactPerson', 'dcite:DataCollector', 'dcite:DataCurator', 'dcite:Investigation', 'dcite:Methodology'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Jadhav, Shantanu', 'roleName': ['dcite:Supervision', 'dcite:Funder', 'dcite:Author'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'National Institute of Mental Health', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': 'R01MH112661 ', 'includeInCitation': False}]
description: This dataset contains data from 8 animals (male Long Evans rats) learning a W-Track alternation task in a single day over 8 behavioral sessions (interleaved with sleep - 17 total epochs). Data includes position information (including velocity), spike times for dorsal CA1 and prefrontal single units, and local field potential.
assetsSummary: {'species': [{'name': 'Rattus norvegicus - Norway rat', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10116'}], 'approach': [{'name': 'behavioral approach', 'schemaKey': 'ApproachType'}, {'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 322981345984, 'numberOfFiles': 9, 'numberOfSubjects': 8, 'variableMeasured': ['SpatialSeries', 'LFP', 'Position', 'ProcessingModule', 'ElectrodeGroup', 'Units', 'ElectricalSeries'], 'measurementTechnique': [{'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'signal filtering technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000978 has 9 NWB files.
2 of these NWB files are of type 1.
1 of these NWB files are of type 2.
2 of these NWB files are of type 3.
4 of these NWB files are of type 4.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeries (ElectricalSeries) no description
  Dataset /acquisition/ElectricalSeries/electrodes (DynamicTableRegion) all electrodes - one channel per tetrode | shape = (128,) | dtype = int64
  file_create_date: ['2024-05-04T05:10:03.724000-04:00']
  Group /general/devices/array (Device) 64 Tetrode microdrive array
  experiment_description: Microdrive tetrode recordings in behaving rats
  experimenter: ['Shin, Justin D']
  Group /general/extracellular_ephys/Tetrode1 (ElectrodeGroup) electrode group for tetrode1
  Group /general/extracellular_ephys/Tetrode1/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode10 (ElectrodeGroup) electrode group for tetrode10
  Group /general/extracellular_ephys/Tetrode10/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode11 (ElectrodeGroup) electrode group for tetrode11
  Group /general/extracellular_ephys/Tetrode11/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode12 (ElectrodeGroup) electrode group for tetrode12
  Group /general/extracellular_ephys/Tetrode12/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode13 (ElectrodeGroup) electrode group for tetrode13
  Group /general/extracellular_ephys/Tetrode13/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode14 (ElectrodeGroup) electrode group for tetrode14
  Group /general/extracellular_ephys/Tetrode14/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode15 (ElectrodeGroup) electrode group for tetrode15
  Group /general/extracellular_ephys/Tetrode15/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode16 (ElectrodeGroup) electrode group for tetrode16
  Group /general/extracellular_ephys/Tetrode16/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode17 (ElectrodeGroup) electrode group for tetrode17
  Group /general/extracellular_ephys/Tetrode17/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode18 (ElectrodeGroup) electrode group for tetrode18
  Group /general/extracellular_ephys/Tetrode18/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode19 (ElectrodeGroup) electrode group for tetrode19
  Group /general/extracellular_ephys/Tetrode19/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode2 (ElectrodeGroup) electrode group for tetrode2
  Group /general/extracellular_ephys/Tetrode2/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode20 (ElectrodeGroup) electrode group for tetrode20
  Group /general/extracellular_ephys/Tetrode20/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode21 (ElectrodeGroup) electrode group for tetrode21
  Group /general/extracellular_ephys/Tetrode21/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode22 (ElectrodeGroup) electrode group for tetrode22
  Group /general/extracellular_ephys/Tetrode22/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode23 (ElectrodeGroup) electrode group for tetrode23
  Group /general/extracellular_ephys/Tetrode23/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode24 (ElectrodeGroup) electrode group for tetrode24
  Group /general/extracellular_ephys/Tetrode24/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode25 (ElectrodeGroup) electrode group for tetrode25
  Group /general/extracellular_ephys/Tetrode25/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode26 (ElectrodeGroup) electrode group for tetrode26
  Group /general/extracellular_ephys/Tetrode26/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode27 (ElectrodeGroup) electrode group for tetrode27
  Group /general/extracellular_ephys/Tetrode27/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode28 (ElectrodeGroup) electrode group for tetrode28
  Group /general/extracellular_ephys/Tetrode28/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode29 (ElectrodeGroup) electrode group for tetrode29
  Group /general/extracellular_ephys/Tetrode29/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode3 (ElectrodeGroup) electrode group for tetrode3
  Group /general/extracellular_ephys/Tetrode3/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode30 (ElectrodeGroup) electrode group for tetrode30
  Group /general/extracellular_ephys/Tetrode30/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode31 (ElectrodeGroup) electrode group for tetrode31
  Group /general/extracellular_ephys/Tetrode31/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode32 (ElectrodeGroup) electrode group for tetrode32
  Group /general/extracellular_ephys/Tetrode32/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode33 (ElectrodeGroup) electrode group for tetrode33
  Group /general/extracellular_ephys/Tetrode33/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode34 (ElectrodeGroup) electrode group for tetrode34
  Group /general/extracellular_ephys/Tetrode34/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode35 (ElectrodeGroup) electrode group for tetrode35
  Group /general/extracellular_ephys/Tetrode35/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode36 (ElectrodeGroup) electrode group for tetrode36
  Group /general/extracellular_ephys/Tetrode36/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode37 (ElectrodeGroup) electrode group for tetrode37
  Group /general/extracellular_ephys/Tetrode37/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode38 (ElectrodeGroup) electrode group for tetrode38
  Group /general/extracellular_ephys/Tetrode38/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode39 (ElectrodeGroup) electrode group for tetrode39
  Group /general/extracellular_ephys/Tetrode39/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode4 (ElectrodeGroup) electrode group for tetrode4
  Group /general/extracellular_ephys/Tetrode4/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode40 (ElectrodeGroup) electrode group for tetrode40
  Group /general/extracellular_ephys/Tetrode40/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode41 (ElectrodeGroup) electrode group for tetrode41
  Group /general/extracellular_ephys/Tetrode41/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode42 (ElectrodeGroup) electrode group for tetrode42
  Group /general/extracellular_ephys/Tetrode42/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode43 (ElectrodeGroup) electrode group for tetrode43
  Group /general/extracellular_ephys/Tetrode43/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode44 (ElectrodeGroup) electrode group for tetrode44
  Group /general/extracellular_ephys/Tetrode44/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode45 (ElectrodeGroup) electrode group for tetrode45
  Group /general/extracellular_ephys/Tetrode45/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode46 (ElectrodeGroup) electrode group for tetrode46
  Group /general/extracellular_ephys/Tetrode46/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode47 (ElectrodeGroup) electrode group for tetrode47
  Group /general/extracellular_ephys/Tetrode47/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode48 (ElectrodeGroup) electrode group for tetrode48
  Group /general/extracellular_ephys/Tetrode48/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode49 (ElectrodeGroup) electrode group for tetrode49
  Group /general/extracellular_ephys/Tetrode49/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode5 (ElectrodeGroup) electrode group for tetrode5
  Group /general/extracellular_ephys/Tetrode5/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode50 (ElectrodeGroup) electrode group for tetrode50
  Group /general/extracellular_ephys/Tetrode50/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode51 (ElectrodeGroup) electrode group for tetrode51
  Group /general/extracellular_ephys/Tetrode51/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode52 (ElectrodeGroup) electrode group for tetrode52
  Group /general/extracellular_ephys/Tetrode52/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode53 (ElectrodeGroup) electrode group for tetrode53
  Group /general/extracellular_ephys/Tetrode53/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode54 (ElectrodeGroup) electrode group for tetrode54
  Group /general/extracellular_ephys/Tetrode54/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode55 (ElectrodeGroup) electrode group for tetrode55
  Group /general/extracellular_ephys/Tetrode55/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode56 (ElectrodeGroup) electrode group for tetrode56
  Group /general/extracellular_ephys/Tetrode56/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode57 (ElectrodeGroup) electrode group for tetrode57
  Group /general/extracellular_ephys/Tetrode57/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode58 (ElectrodeGroup) electrode group for tetrode58
  Group /general/extracellular_ephys/Tetrode58/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode59 (ElectrodeGroup) electrode group for tetrode59
  Group /general/extracellular_ephys/Tetrode59/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode6 (ElectrodeGroup) electrode group for tetrode6
  Group /general/extracellular_ephys/Tetrode6/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode60 (ElectrodeGroup) electrode group for tetrode60
  Group /general/extracellular_ephys/Tetrode60/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode61 (ElectrodeGroup) electrode group for tetrode61
  Group /general/extracellular_ephys/Tetrode61/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode62 (ElectrodeGroup) electrode group for tetrode62
  Group /general/extracellular_ephys/Tetrode62/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode63 (ElectrodeGroup) electrode group for tetrode63
  Group /general/extracellular_ephys/Tetrode63/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode64 (ElectrodeGroup) electrode group for tetrode64
  Group /general/extracellular_ephys/Tetrode64/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode7 (ElectrodeGroup) electrode group for tetrode7
  Group /general/extracellular_ephys/Tetrode7/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode8 (ElectrodeGroup) electrode group for tetrode8
  Group /general/extracellular_ephys/Tetrode8/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode9 (ElectrodeGroup) electrode group for tetrode9
  Group /general/extracellular_ephys/Tetrode9/device (Device) 64 Tetrode microdrive array
  Group /general/extracellular_ephys/electrodes (DynamicTable) all electrodes
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) my description | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) my description | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/label (VectorData) my description | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) my description | shape = (128,) | dtype = object
  institution: Brandeis University
  keywords: ['Hippocampus' 'Prefrontal cortex' 'Spatial memory' 'Working memory'
   'Sleep' 'Learning']
  lab: Jadhav Lab
  session_id: 01
  Group /general/subject (Subject) 
  identifier: ZT2_01
  Group /intervals/epoch intervals (TimeIntervals) Start and end times of all epochs
  Dataset /intervals/epoch intervals/id (ElementIdentifiers)  | shape = (8,) | dtype = int64
  Dataset /intervals/epoch intervals/start_time (VectorData) AUTOGENERATED description for column `start_time` | shape = (8,) | dtype = float64
  Dataset /intervals/epoch intervals/stop_time (VectorData) AUTOGENERATED description for column `stop_time` | shape = (8,) | dtype = float64
  Group /intervals/trials (TimeIntervals) trial data and properties
  Dataset /intervals/trials/correct (VectorData) correct or incorrect | shape = (119,) | dtype = float64
  Dataset /intervals/trials/end_well (VectorData) well ID at trajectory end (Well-1 Center; Well-2 Left; Well-3 Right) | shape = (119,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (119,) | dtype = int64
  Dataset /intervals/trials/start_time (VectorData) start time of trajectory in seconds | shape = (119,) | dtype = float64
  Dataset /intervals/trials/start_well (VectorData) well ID at trajectory start (Well-1 Center; Well-2 Left; Well-3 Right) | shape = (119,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) end of each trajectory in seconds | shape = (119,) | dtype = float64
  Dataset /intervals/trials/trajectory_type (VectorData) Inbound = 1; Outbound = 0 | shape = (119,) | dtype = float64
  Group /processing/behavior (ProcessingModule) contains behavioral data
  Group /processing/behavior/Position (Position) 
  Group /processing/behavior/Position/SpatialSeries (SpatialSeries) no description
  Group /processing/ecephys (ProcessingModule) extracellular electrophysiology
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/ElectricalSeries (ElectricalSeries) no description
  Dataset /processing/ecephys/LFP/ElectricalSeries/electrodes (DynamicTableRegion) all electrodes - one channel per tetrode | shape = (128,) | dtype = int64
  session_description: Single Day WTrack Learning Experiment
  session_start_time: 2024-05-03T10:44:17.908000-04:00
  timestamps_reference_time: 2024-05-03T10:44:17.908000-04:00
  Group /units (Units) units table
  Dataset /units/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (240,) | dtype = int64
  Dataset /units/id (ElementIdentifiers)  | shape = (240,) | dtype = int64
  Dataset /units/spike_times (VectorData) no description | shape = (6742394,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) indexes data | shape = (240,) | dtype = uint64


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeries (ElectricalSeries) no description
  Dataset /acquisition/ElectricalSeries/electrodes (DynamicTableRegion) all electrodes - one channel per tetrode | shape = (60,) | dtype = int64
  file_create_date: ['2024-05-01T16:00:12.629000-04:00']
  Group /general/devices/array (Device) 30 Tetrode microdrive array
  experiment_description: Microdrive tetrode recordings in behaving rats
  experimenter: ['Shin, Justin D']
  Group /general/extracellular_ephys/Tetrode1 (ElectrodeGroup) electrode group for tetrode1
  Group /general/extracellular_ephys/Tetrode1/device (Device) 30 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode10 (ElectrodeGroup) electrode group for tetrode10
  Group /general/extracellular_ephys/Tetrode10/device (Device) 30 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode11 (ElectrodeGroup) electrode group for tetrode11
  Group /general/extracellular_ephys/Tetrode11/device (Device) 30 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode12 (ElectrodeGroup) electrode group for tetrode12
  Group /general/extracellular_ephys/Tetrode12/device (Device) 30 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode13 (ElectrodeGroup) electrode group for tetrode13
  Group /general/extracellular_ephys/Tetrode13/device (Device) 30 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode14 (ElectrodeGroup) electrode group for tetrode14
  Group /general/extracellular_ephys/Tetrode14/device (Device) 30 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode15 (ElectrodeGroup) electrode group for tetrode15
  Group /general/extracellular_ephys/Tetrode15/device (Device) 30 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode16 (ElectrodeGroup) electrode group for tetrode16
  Group /general/extracellular_ephys/Tetrode16/device (Device) 30 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode17 (ElectrodeGroup) electrode group for tetrode17
  Group /general/extracellular_ephys/Tetrode17/device (Device) 30 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode18 (ElectrodeGroup) electrode group for tetrode18
  Group /general/extracellular_ephys/Tetrode18/device (Device) 30 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode19 (ElectrodeGroup) electrode group for tetrode19
  Group /general/extracellular_ephys/Tetrode19/device (Device) 30 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode2 (ElectrodeGroup) electrode group for tetrode2
  Group /general/extracellular_ephys/Tetrode2/device (Device) 30 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode20 (ElectrodeGroup) electrode group for tetrode20
  Group /general/extracellular_ephys/Tetrode20/device (Device) 30 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode21 (ElectrodeGroup) electrode group for tetrode21
  Group /general/extracellular_ephys/Tetrode21/device (Device) 30 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode22 (ElectrodeGroup) electrode group for tetrode22
  Group /general/extracellular_ephys/Tetrode22/device (Device) 30 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode23 (ElectrodeGroup) electrode group for tetrode23
  Group /general/extracellular_ephys/Tetrode23/device (Device) 30 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode24 (ElectrodeGroup) electrode group for tetrode24
  Group /general/extracellular_ephys/Tetrode24/device (Device) 30 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode25 (ElectrodeGroup) electrode group for tetrode25
  Group /general/extracellular_ephys/Tetrode25/device (Device) 30 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode26 (ElectrodeGroup) electrode group for tetrode26
  Group /general/extracellular_ephys/Tetrode26/device (Device) 30 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode27 (ElectrodeGroup) electrode group for tetrode27
  Group /general/extracellular_ephys/Tetrode27/device (Device) 30 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode28 (ElectrodeGroup) electrode group for tetrode28
  Group /general/extracellular_ephys/Tetrode28/device (Device) 30 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode29 (ElectrodeGroup) electrode group for tetrode29
  Group /general/extracellular_ephys/Tetrode29/device (Device) 30 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode3 (ElectrodeGroup) electrode group for tetrode3
  Group /general/extracellular_ephys/Tetrode3/device (Device) 30 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode30 (ElectrodeGroup) electrode group for tetrode30
  Group /general/extracellular_ephys/Tetrode30/device (Device) 30 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode4 (ElectrodeGroup) electrode group for tetrode4
  Group /general/extracellular_ephys/Tetrode4/device (Device) 30 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode5 (ElectrodeGroup) electrode group for tetrode5
  Group /general/extracellular_ephys/Tetrode5/device (Device) 30 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode6 (ElectrodeGroup) electrode group for tetrode6
  Group /general/extracellular_ephys/Tetrode6/device (Device) 30 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode7 (ElectrodeGroup) electrode group for tetrode7
  Group /general/extracellular_ephys/Tetrode7/device (Device) 30 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode8 (ElectrodeGroup) electrode group for tetrode8
  Group /general/extracellular_ephys/Tetrode8/device (Device) 30 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode9 (ElectrodeGroup) electrode group for tetrode9
  Group /general/extracellular_ephys/Tetrode9/device (Device) 30 Tetrode microdrive array
  Group /general/extracellular_ephys/electrodes (DynamicTable) all electrodes
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) my description | shape = (60,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) my description | shape = (60,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (60,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/label (VectorData) my description | shape = (60,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) my description | shape = (60,) | dtype = object
  institution: Brandeis University
  keywords: ['Hippocampus' 'Prefrontal cortex' 'Spatial memory' 'Working memory'
   'Sleep' 'Learning']
  lab: Jadhav Lab
  session_id: 01
  Group /general/subject (Subject) 
  identifier: ER1_01
  Group /intervals/epoch intervals (TimeIntervals) Start and end times of all epochs
  Dataset /intervals/epoch intervals/id (ElementIdentifiers)  | shape = (17,) | dtype = int64
  Dataset /intervals/epoch intervals/start_time (VectorData) AUTOGENERATED description for column `start_time` | shape = (17,) | dtype = float64
  Dataset /intervals/epoch intervals/stop_time (VectorData) AUTOGENERATED description for column `stop_time` | shape = (17,) | dtype = float64
  Group /intervals/trials (TimeIntervals) trial data and properties
  Dataset /intervals/trials/correct (VectorData) correct or incorrect | shape = (362,) | dtype = float64
  Dataset /intervals/trials/end_well (VectorData) well ID at trajectory end (Well-1 Center; Well-2 Left; Well-3 Right) | shape = (362,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (362,) | dtype = int64
  Dataset /intervals/trials/start_time (VectorData) start time of trajectory in seconds | shape = (362,) | dtype = float64
  Dataset /intervals/trials/start_well (VectorData) well ID at trajectory start (Well-1 Center; Well-2 Left; Well-3 Right) | shape = (362,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) end of each trajectory in seconds | shape = (362,) | dtype = float64
  Dataset /intervals/trials/trajectory_type (VectorData) Inbound = 1; Outbound = 0 | shape = (362,) | dtype = float64
  Group /processing/behavior (ProcessingModule) contains behavioral data
  Group /processing/behavior/Position (Position) 
  Group /processing/behavior/Position/SpatialSeries (SpatialSeries) no description
  Group /processing/ecephys (ProcessingModule) extracellular electrophysiology
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/ElectricalSeries (ElectricalSeries) no description
  Dataset /processing/ecephys/LFP/ElectricalSeries/electrodes (DynamicTableRegion) all electrodes - one channel per tetrode | shape = (60,) | dtype = int64
  session_description: Single Day WTrack Learning Experiment
  session_start_time: 2024-05-01T15:19:04.423000-04:00
  timestamps_reference_time: 2024-05-01T15:19:04.423000-04:00
  Group /units (Units) units table
  Dataset /units/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (122,) | dtype = int64
  Dataset /units/id (ElementIdentifiers)  | shape = (122,) | dtype = int64
  Dataset /units/spike_times (VectorData) no description | shape = (2466821,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) indexes data | shape = (122,) | dtype = uint64


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeries (ElectricalSeries) no description
  Dataset /acquisition/ElectricalSeries/electrodes (DynamicTableRegion) all electrodes - one channel per tetrode | shape = (62,) | dtype = int64
  file_create_date: ['2024-05-01T19:54:17.714000-04:00']
  Group /general/devices/array (Device) 31 Tetrode microdrive array
  experiment_description: Microdrive tetrode recordings in behaving rats
  experimenter: ['Shin, Justin D']
  Group /general/extracellular_ephys/Tetrode1 (ElectrodeGroup) electrode group for tetrode1
  Group /general/extracellular_ephys/Tetrode1/device (Device) 31 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode10 (ElectrodeGroup) electrode group for tetrode10
  Group /general/extracellular_ephys/Tetrode10/device (Device) 31 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode11 (ElectrodeGroup) electrode group for tetrode11
  Group /general/extracellular_ephys/Tetrode11/device (Device) 31 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode12 (ElectrodeGroup) electrode group for tetrode12
  Group /general/extracellular_ephys/Tetrode12/device (Device) 31 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode13 (ElectrodeGroup) electrode group for tetrode13
  Group /general/extracellular_ephys/Tetrode13/device (Device) 31 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode14 (ElectrodeGroup) electrode group for tetrode14
  Group /general/extracellular_ephys/Tetrode14/device (Device) 31 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode15 (ElectrodeGroup) electrode group for tetrode15
  Group /general/extracellular_ephys/Tetrode15/device (Device) 31 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode16 (ElectrodeGroup) electrode group for tetrode16
  Group /general/extracellular_ephys/Tetrode16/device (Device) 31 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode17 (ElectrodeGroup) electrode group for tetrode17
  Group /general/extracellular_ephys/Tetrode17/device (Device) 31 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode18 (ElectrodeGroup) electrode group for tetrode18
  Group /general/extracellular_ephys/Tetrode18/device (Device) 31 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode19 (ElectrodeGroup) electrode group for tetrode19
  Group /general/extracellular_ephys/Tetrode19/device (Device) 31 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode2 (ElectrodeGroup) electrode group for tetrode2
  Group /general/extracellular_ephys/Tetrode2/device (Device) 31 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode20 (ElectrodeGroup) electrode group for tetrode20
  Group /general/extracellular_ephys/Tetrode20/device (Device) 31 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode21 (ElectrodeGroup) electrode group for tetrode21
  Group /general/extracellular_ephys/Tetrode21/device (Device) 31 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode22 (ElectrodeGroup) electrode group for tetrode22
  Group /general/extracellular_ephys/Tetrode22/device (Device) 31 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode23 (ElectrodeGroup) electrode group for tetrode23
  Group /general/extracellular_ephys/Tetrode23/device (Device) 31 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode24 (ElectrodeGroup) electrode group for tetrode24
  Group /general/extracellular_ephys/Tetrode24/device (Device) 31 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode25 (ElectrodeGroup) electrode group for tetrode25
  Group /general/extracellular_ephys/Tetrode25/device (Device) 31 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode26 (ElectrodeGroup) electrode group for tetrode26
  Group /general/extracellular_ephys/Tetrode26/device (Device) 31 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode27 (ElectrodeGroup) electrode group for tetrode27
  Group /general/extracellular_ephys/Tetrode27/device (Device) 31 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode28 (ElectrodeGroup) electrode group for tetrode28
  Group /general/extracellular_ephys/Tetrode28/device (Device) 31 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode29 (ElectrodeGroup) electrode group for tetrode29
  Group /general/extracellular_ephys/Tetrode29/device (Device) 31 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode3 (ElectrodeGroup) electrode group for tetrode3
  Group /general/extracellular_ephys/Tetrode3/device (Device) 31 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode30 (ElectrodeGroup) electrode group for tetrode30
  Group /general/extracellular_ephys/Tetrode30/device (Device) 31 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode31 (ElectrodeGroup) electrode group for tetrode31
  Group /general/extracellular_ephys/Tetrode31/device (Device) 31 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode4 (ElectrodeGroup) electrode group for tetrode4
  Group /general/extracellular_ephys/Tetrode4/device (Device) 31 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode5 (ElectrodeGroup) electrode group for tetrode5
  Group /general/extracellular_ephys/Tetrode5/device (Device) 31 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode6 (ElectrodeGroup) electrode group for tetrode6
  Group /general/extracellular_ephys/Tetrode6/device (Device) 31 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode7 (ElectrodeGroup) electrode group for tetrode7
  Group /general/extracellular_ephys/Tetrode7/device (Device) 31 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode8 (ElectrodeGroup) electrode group for tetrode8
  Group /general/extracellular_ephys/Tetrode8/device (Device) 31 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode9 (ElectrodeGroup) electrode group for tetrode9
  Group /general/extracellular_ephys/Tetrode9/device (Device) 31 Tetrode microdrive array
  Group /general/extracellular_ephys/electrodes (DynamicTable) all electrodes
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) my description | shape = (62,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) my description | shape = (62,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (62,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/label (VectorData) my description | shape = (62,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) my description | shape = (62,) | dtype = object
  institution: Brandeis University
  keywords: ['Hippocampus' 'Prefrontal cortex' 'Spatial memory' 'Working memory'
   'Sleep' 'Learning']
  lab: Jadhav Lab
  session_id: 01
  Group /general/subject (Subject) 
  identifier: JS14_01
  Group /intervals/epoch intervals (TimeIntervals) Start and end times of all epochs
  Dataset /intervals/epoch intervals/id (ElementIdentifiers)  | shape = (17,) | dtype = int64
  Dataset /intervals/epoch intervals/start_time (VectorData) AUTOGENERATED description for column `start_time` | shape = (17,) | dtype = float64
  Dataset /intervals/epoch intervals/stop_time (VectorData) AUTOGENERATED description for column `stop_time` | shape = (17,) | dtype = float64
  Group /intervals/trials (TimeIntervals) trial data and properties
  Dataset /intervals/trials/correct (VectorData) correct or incorrect | shape = (298,) | dtype = float64
  Dataset /intervals/trials/end_well (VectorData) well ID at trajectory end (Well-1 Center; Well-2 Left; Well-3 Right) | shape = (298,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (298,) | dtype = int64
  Dataset /intervals/trials/start_time (VectorData) start time of trajectory in seconds | shape = (298,) | dtype = float64
  Dataset /intervals/trials/start_well (VectorData) well ID at trajectory start (Well-1 Center; Well-2 Left; Well-3 Right) | shape = (298,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) end of each trajectory in seconds | shape = (298,) | dtype = float64
  Dataset /intervals/trials/trajectory_type (VectorData) Inbound = 1; Outbound = 0 | shape = (298,) | dtype = float64
  Group /processing/behavior (ProcessingModule) contains behavioral data
  Group /processing/behavior/Position (Position) 
  Group /processing/behavior/Position/SpatialSeries (SpatialSeries) no description
  Group /processing/ecephys (ProcessingModule) extracellular electrophysiology
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/ElectricalSeries (ElectricalSeries) no description
  Dataset /processing/ecephys/LFP/ElectricalSeries/electrodes (DynamicTableRegion) all electrodes - one channel per tetrode | shape = (62,) | dtype = int64
  session_description: Single Day WTrack Learning Experiment
  session_start_time: 2024-05-01T19:33:28.919000-04:00
  timestamps_reference_time: 2024-05-01T19:33:28.919000-04:00
  Group /units (Units) units table
  Dataset /units/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (72,) | dtype = int64
  Dataset /units/id (ElementIdentifiers)  | shape = (72,) | dtype = int64
  Dataset /units/spike_times (VectorData) no description | shape = (1836621,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) indexes data | shape = (72,) | dtype = uint64


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeries (ElectricalSeries) no description
  Dataset /acquisition/ElectricalSeries/electrodes (DynamicTableRegion) all electrodes - one channel per tetrode | shape = (64,) | dtype = int64
  file_create_date: ['2024-05-01T18:07:34.484000-04:00']
  Group /general/devices/array (Device) 32 Tetrode microdrive array
  experiment_description: Microdrive tetrode recordings in behaving rats
  experimenter: ['Shin, Justin D']
  Group /general/extracellular_ephys/Tetrode1 (ElectrodeGroup) electrode group for tetrode1
  Group /general/extracellular_ephys/Tetrode1/device (Device) 32 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode10 (ElectrodeGroup) electrode group for tetrode10
  Group /general/extracellular_ephys/Tetrode10/device (Device) 32 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode11 (ElectrodeGroup) electrode group for tetrode11
  Group /general/extracellular_ephys/Tetrode11/device (Device) 32 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode12 (ElectrodeGroup) electrode group for tetrode12
  Group /general/extracellular_ephys/Tetrode12/device (Device) 32 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode13 (ElectrodeGroup) electrode group for tetrode13
  Group /general/extracellular_ephys/Tetrode13/device (Device) 32 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode14 (ElectrodeGroup) electrode group for tetrode14
  Group /general/extracellular_ephys/Tetrode14/device (Device) 32 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode15 (ElectrodeGroup) electrode group for tetrode15
  Group /general/extracellular_ephys/Tetrode15/device (Device) 32 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode16 (ElectrodeGroup) electrode group for tetrode16
  Group /general/extracellular_ephys/Tetrode16/device (Device) 32 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode17 (ElectrodeGroup) electrode group for tetrode17
  Group /general/extracellular_ephys/Tetrode17/device (Device) 32 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode18 (ElectrodeGroup) electrode group for tetrode18
  Group /general/extracellular_ephys/Tetrode18/device (Device) 32 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode19 (ElectrodeGroup) electrode group for tetrode19
  Group /general/extracellular_ephys/Tetrode19/device (Device) 32 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode2 (ElectrodeGroup) electrode group for tetrode2
  Group /general/extracellular_ephys/Tetrode2/device (Device) 32 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode20 (ElectrodeGroup) electrode group for tetrode20
  Group /general/extracellular_ephys/Tetrode20/device (Device) 32 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode21 (ElectrodeGroup) electrode group for tetrode21
  Group /general/extracellular_ephys/Tetrode21/device (Device) 32 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode22 (ElectrodeGroup) electrode group for tetrode22
  Group /general/extracellular_ephys/Tetrode22/device (Device) 32 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode23 (ElectrodeGroup) electrode group for tetrode23
  Group /general/extracellular_ephys/Tetrode23/device (Device) 32 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode24 (ElectrodeGroup) electrode group for tetrode24
  Group /general/extracellular_ephys/Tetrode24/device (Device) 32 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode25 (ElectrodeGroup) electrode group for tetrode25
  Group /general/extracellular_ephys/Tetrode25/device (Device) 32 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode26 (ElectrodeGroup) electrode group for tetrode26
  Group /general/extracellular_ephys/Tetrode26/device (Device) 32 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode27 (ElectrodeGroup) electrode group for tetrode27
  Group /general/extracellular_ephys/Tetrode27/device (Device) 32 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode28 (ElectrodeGroup) electrode group for tetrode28
  Group /general/extracellular_ephys/Tetrode28/device (Device) 32 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode29 (ElectrodeGroup) electrode group for tetrode29
  Group /general/extracellular_ephys/Tetrode29/device (Device) 32 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode3 (ElectrodeGroup) electrode group for tetrode3
  Group /general/extracellular_ephys/Tetrode3/device (Device) 32 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode30 (ElectrodeGroup) electrode group for tetrode30
  Group /general/extracellular_ephys/Tetrode30/device (Device) 32 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode31 (ElectrodeGroup) electrode group for tetrode31
  Group /general/extracellular_ephys/Tetrode31/device (Device) 32 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode32 (ElectrodeGroup) electrode group for tetrode32
  Group /general/extracellular_ephys/Tetrode32/device (Device) 32 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode4 (ElectrodeGroup) electrode group for tetrode4
  Group /general/extracellular_ephys/Tetrode4/device (Device) 32 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode5 (ElectrodeGroup) electrode group for tetrode5
  Group /general/extracellular_ephys/Tetrode5/device (Device) 32 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode6 (ElectrodeGroup) electrode group for tetrode6
  Group /general/extracellular_ephys/Tetrode6/device (Device) 32 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode7 (ElectrodeGroup) electrode group for tetrode7
  Group /general/extracellular_ephys/Tetrode7/device (Device) 32 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode8 (ElectrodeGroup) electrode group for tetrode8
  Group /general/extracellular_ephys/Tetrode8/device (Device) 32 Tetrode microdrive array
  Group /general/extracellular_ephys/Tetrode9 (ElectrodeGroup) electrode group for tetrode9
  Group /general/extracellular_ephys/Tetrode9/device (Device) 32 Tetrode microdrive array
  Group /general/extracellular_ephys/electrodes (DynamicTable) all electrodes
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) my description | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) my description | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (64,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/label (VectorData) my description | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) my description | shape = (64,) | dtype = object
  institution: Brandeis University
  keywords: ['Hippocampus' 'Prefrontal cortex' 'Spatial memory' 'Working memory'
   'Sleep' 'Learning']
  lab: Jadhav Lab
  session_id: 01
  Group /general/subject (Subject) 
  identifier: JS17_01
  Group /intervals/epoch intervals (TimeIntervals) Start and end times of all epochs
  Dataset /intervals/epoch intervals/id (ElementIdentifiers)  | shape = (17,) | dtype = int64
  Dataset /intervals/epoch intervals/start_time (VectorData) AUTOGENERATED description for column `start_time` | shape = (17,) | dtype = float64
  Dataset /intervals/epoch intervals/stop_time (VectorData) AUTOGENERATED description for column `stop_time` | shape = (17,) | dtype = float64
  Group /intervals/trials (TimeIntervals) trial data and properties
  Dataset /intervals/trials/correct (VectorData) correct or incorrect | shape = (366,) | dtype = float64
  Dataset /intervals/trials/end_well (VectorData) well ID at trajectory end (Well-1 Center; Well-2 Left; Well-3 Right) | shape = (366,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (366,) | dtype = int64
  Dataset /intervals/trials/start_time (VectorData) start time of trajectory in seconds | shape = (366,) | dtype = float64
  Dataset /intervals/trials/start_well (VectorData) well ID at trajectory start (Well-1 Center; Well-2 Left; Well-3 Right) | shape = (366,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) end of each trajectory in seconds | shape = (366,) | dtype = float64
  Dataset /intervals/trials/trajectory_type (VectorData) Inbound = 1; Outbound = 0 | shape = (366,) | dtype = float64
  Group /processing/behavior (ProcessingModule) contains behavioral data
  Group /processing/behavior/Position (Position) 
  Group /processing/behavior/Position/SpatialSeries (SpatialSeries) no description
  Group /processing/ecephys (ProcessingModule) extracellular electrophysiology
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/ElectricalSeries (ElectricalSeries) no description
  Dataset /processing/ecephys/LFP/ElectricalSeries/electrodes (DynamicTableRegion) all electrodes - one channel per tetrode | shape = (64,) | dtype = int64
  session_description: Single Day WTrack Learning Experiment
  session_start_time: 2024-05-01T16:09:19.707000-04:00
  timestamps_reference_time: 2024-05-01T16:09:19.707000-04:00
  Group /units (Units) units table
  Dataset /units/electrodes (DynamicTableRegion) Electrodes involved with these spike events | shape = (78,) | dtype = int64
  Dataset /units/id (ElementIdentifiers)  | shape = (78,) | dtype = int64
  Dataset /units/spike_times (VectorData) no description | shape = (4423118,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) indexes data | shape = (78,) | dtype = uint64
