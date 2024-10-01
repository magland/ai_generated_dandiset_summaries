
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000638/draft
name: Hippocampus and Entorhinal Cortex Dual Region Silicon Probe recording
contributor: [{'name': 'Yu Feng', 'email': 'susieyufeng@gmail.com', 'roleName': ['dcite:Author', 'dcite:ContactPerson', 'dcite:DataCollector', 'dcite:DataManager', 'dcite:FormalAnalysis', 'dcite:Methodology', 'dcite:ProjectLeader', 'dcite:ProjectManager'], 'schemaKey': 'Organization', 'includeInCitation': True}, {'name': 'Zhe Dong', 'email': 'phil.zhe.dong@gmail.com', 'roleName': ['dcite:FormalAnalysis'], 'schemaKey': 'Organization', 'includeInCitation': False}, {'name': 'Tristan Shuman', 'email': 'tristan.shuman@mssm.edu', 'roleName': ['dcite:ContactPerson', 'dcite:FundingAcquisition'], 'schemaKey': 'Organization', 'includeInCitation': False}]
description: Acute hippocampus and entorhinal cortex dual region silicon probe recording in head-fixed animals, both control and epileptic, running in virtual reality. Data was collected at either 3 weeks or 8 weeks after pilocarpine treatment. 
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}, {'name': 'behavioral approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 1199530787667, 'numberOfFiles': 33, 'numberOfSubjects': 33, 'variableMeasured': ['ElectrodeGroup', 'LFP', 'ProcessingModule', 'SpatialSeries', 'Units', 'ElectricalSeries', 'Position', 'BehavioralTimeSeries', 'BehavioralEpochs'], 'measurementTechnique': [{'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'signal filtering technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000638 has 19 NWB files.
3 of these NWB files are of type 1.
8 of these NWB files are of type 2.
4 of these NWB files are of type 3.
3 of these NWB files are of type 4.
1 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/shank3 (ElectricalSeries) no description
  Dataset /acquisition/shank3/electrodes (DynamicTableRegion) table region for shank3 | shape = (64,) | dtype = int32
  Group /acquisition/shank7 (ElectricalSeries) no description
  Dataset /acquisition/shank7/electrodes (DynamicTableRegion) table region for shank7 | shape = (64,) | dtype = int32
  file_create_date: ['2023-09-10T00:08:36.547318-04:00']
  Group /general/devices/Masmanidis Probe (Device) UCLA Masmanidis Lab 256 Channel Silicon Probe (https://masmanidislab.neurobio.ucla.edu/technology.html)
  experiment_description: MEC, HPC dual-region silicon probe recording in head-fixed mouse running in VR
  experimenter: ['Susie Feng']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (512,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (512,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (512,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/isBadChannel (VectorData) whether the electrode is bad and excluded in analysis. | shape = (512,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/isMaster (VectorData) whether the electrode belong to the best representative shank for either HPC or MEC | shape = (512,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (512,) | dtype = object
  Group /general/extracellular_ephys/shank1 (ElectrodeGroup) electrode group for shank 1
  Group /general/extracellular_ephys/shank1/device (Device) UCLA Masmanidis Lab 256 Channel Silicon Probe (https://masmanidislab.neurobio.ucla.edu/technology.html)
  Group /general/extracellular_ephys/shank2 (ElectrodeGroup) electrode group for shank 2
  Group /general/extracellular_ephys/shank2/device (Device) UCLA Masmanidis Lab 256 Channel Silicon Probe (https://masmanidislab.neurobio.ucla.edu/technology.html)
  Group /general/extracellular_ephys/shank3 (ElectrodeGroup) electrode group for shank 3
  Group /general/extracellular_ephys/shank3/device (Device) UCLA Masmanidis Lab 256 Channel Silicon Probe (https://masmanidislab.neurobio.ucla.edu/technology.html)
  Group /general/extracellular_ephys/shank4 (ElectrodeGroup) electrode group for shank 4
  Group /general/extracellular_ephys/shank4/device (Device) UCLA Masmanidis Lab 256 Channel Silicon Probe (https://masmanidislab.neurobio.ucla.edu/technology.html)
  Group /general/extracellular_ephys/shank5 (ElectrodeGroup) electrode group for shank 5
  Group /general/extracellular_ephys/shank5/device (Device) UCLA Masmanidis Lab 256 Channel Silicon Probe (https://masmanidislab.neurobio.ucla.edu/technology.html)
  Group /general/extracellular_ephys/shank6 (ElectrodeGroup) electrode group for shank 6
  Group /general/extracellular_ephys/shank6/device (Device) UCLA Masmanidis Lab 256 Channel Silicon Probe (https://masmanidislab.neurobio.ucla.edu/technology.html)
  Group /general/extracellular_ephys/shank7 (ElectrodeGroup) electrode group for shank 7
  Group /general/extracellular_ephys/shank7/device (Device) UCLA Masmanidis Lab 256 Channel Silicon Probe (https://masmanidislab.neurobio.ucla.edu/technology.html)
  Group /general/extracellular_ephys/shank8 (ElectrodeGroup) electrode group for shank 8
  Group /general/extracellular_ephys/shank8/device (Device) UCLA Masmanidis Lab 256 Channel Silicon Probe (https://masmanidislab.neurobio.ucla.edu/technology.html)
  institution: Icahn School of Medicine at Mount Sinai
  lab: Tristan Shuman Laboratory
  related_publications: ['N/A']
  session_id: TS110-3
  Group /general/subject (Subject) 
  identifier: TS110-3
  Group /processing/behavior (ProcessingModule) Raw and processed behavioral data
  Group /processing/behavior/lick (BehavioralTimeSeries) 
  Group /processing/behavior/lick/lick (TimeSeries) Voltage output from lick sensor, a value of 5.0 indicate a lick
  Group /processing/behavior/position (Position) 
  Group /processing/behavior/position/position (SpatialSeries) no description
  Group /processing/behavior/reward (BehavioralTimeSeries) 
  Group /processing/behavior/reward/reward (TimeSeries) Driving voltage of water delievery valve, a value above 0.02 indicate a reward delivery
  Group /processing/behavior/speed (BehavioralTimeSeries) 
  Group /processing/behavior/speed/speed (TimeSeries) Output from VR track
  Group /processing/theta (ProcessingModule) Filtered out 60Hz then filtered through 5-12Hz (theta band) of raw data
  Group /processing/theta/shank3 (LFP) 
  Group /processing/theta/shank3/shank3 (ElectricalSeries) no description
  Dataset /processing/theta/shank3/shank3/electrodes (DynamicTableRegion) table region for shank3 | shape = (64,) | dtype = int32
  Group /processing/theta/shank7 (LFP) 
  Group /processing/theta/shank7/shank7 (ElectricalSeries) no description
  Dataset /processing/theta/shank7/shank7/electrodes (DynamicTableRegion) table region for shank7 | shape = (64,) | dtype = int32
  session_description: head fixed mouse running in VR
  session_start_time: 2020-07-11T00:00:00-04:00
  timestamps_reference_time: 2020-07-11T00:00:00-04:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (28,) | dtype = object
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (28,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex) Index for VectorData 'electrodes' | shape = (28,) | dtype = uint8
  Dataset /units/id (ElementIdentifiers)  | shape = (28,) | dtype = int32
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (1485654,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (28,) | dtype = uint32
  Dataset /units/unit_type (VectorData) specify whether unit is classified as excitatory or inhibitory or unclassified | shape = (28,) | dtype = object


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/shank3 (ElectricalSeries) no description
  Dataset /acquisition/shank3/electrodes (DynamicTableRegion) table region for shank3 | shape = (64,) | dtype = int32
  Group /acquisition/shank6 (ElectricalSeries) no description
  Dataset /acquisition/shank6/electrodes (DynamicTableRegion) table region for shank6 | shape = (64,) | dtype = int32
  file_create_date: ['2023-09-10T01:13:49.132759-04:00']
  Group /general/devices/Masmanidis Probe (Device) UCLA Masmanidis Lab 256 Channel Silicon Probe (https://masmanidislab.neurobio.ucla.edu/technology.html)
  experiment_description: MEC, HPC dual-region silicon probe recording in head-fixed mouse running in VR
  experimenter: ['Susie Feng']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (512,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (512,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (512,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/isBadChannel (VectorData) whether the electrode is bad and excluded in analysis. | shape = (512,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/isMaster (VectorData) whether the electrode belong to the best representative shank for either HPC or MEC | shape = (512,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (512,) | dtype = object
  Group /general/extracellular_ephys/shank1 (ElectrodeGroup) electrode group for shank 1
  Group /general/extracellular_ephys/shank1/device (Device) UCLA Masmanidis Lab 256 Channel Silicon Probe (https://masmanidislab.neurobio.ucla.edu/technology.html)
  Group /general/extracellular_ephys/shank2 (ElectrodeGroup) electrode group for shank 2
  Group /general/extracellular_ephys/shank2/device (Device) UCLA Masmanidis Lab 256 Channel Silicon Probe (https://masmanidislab.neurobio.ucla.edu/technology.html)
  Group /general/extracellular_ephys/shank3 (ElectrodeGroup) electrode group for shank 3
  Group /general/extracellular_ephys/shank3/device (Device) UCLA Masmanidis Lab 256 Channel Silicon Probe (https://masmanidislab.neurobio.ucla.edu/technology.html)
  Group /general/extracellular_ephys/shank4 (ElectrodeGroup) electrode group for shank 4
  Group /general/extracellular_ephys/shank4/device (Device) UCLA Masmanidis Lab 256 Channel Silicon Probe (https://masmanidislab.neurobio.ucla.edu/technology.html)
  Group /general/extracellular_ephys/shank5 (ElectrodeGroup) electrode group for shank 5
  Group /general/extracellular_ephys/shank5/device (Device) UCLA Masmanidis Lab 256 Channel Silicon Probe (https://masmanidislab.neurobio.ucla.edu/technology.html)
  Group /general/extracellular_ephys/shank6 (ElectrodeGroup) electrode group for shank 6
  Group /general/extracellular_ephys/shank6/device (Device) UCLA Masmanidis Lab 256 Channel Silicon Probe (https://masmanidislab.neurobio.ucla.edu/technology.html)
  Group /general/extracellular_ephys/shank7 (ElectrodeGroup) electrode group for shank 7
  Group /general/extracellular_ephys/shank7/device (Device) UCLA Masmanidis Lab 256 Channel Silicon Probe (https://masmanidislab.neurobio.ucla.edu/technology.html)
  Group /general/extracellular_ephys/shank8 (ElectrodeGroup) electrode group for shank 8
  Group /general/extracellular_ephys/shank8/device (Device) UCLA Masmanidis Lab 256 Channel Silicon Probe (https://masmanidislab.neurobio.ucla.edu/technology.html)
  institution: Icahn School of Medicine at Mount Sinai
  lab: Tristan Shuman Laboratory
  related_publications: ['N/A']
  session_id: TS111-1
  Group /general/subject (Subject) 
  identifier: TS111-1
  Group /processing/behavior (ProcessingModule) Raw and processed behavioral data
  Group /processing/behavior/lick (BehavioralTimeSeries) 
  Group /processing/behavior/lick/lick (TimeSeries) Voltage output from lick sensor, a value of 5.0 indicate a lick
  Group /processing/behavior/position (Position) 
  Group /processing/behavior/position/position (SpatialSeries) no description
  Group /processing/behavior/reward (BehavioralTimeSeries) 
  Group /processing/behavior/reward/reward (TimeSeries) Driving voltage of water delievery valve, a value above 0.02 indicate a reward delivery
  Group /processing/behavior/speed (BehavioralTimeSeries) 
  Group /processing/behavior/speed/speed (TimeSeries) Output from VR track
  Group /processing/theta (ProcessingModule) Filtered out 60Hz then filtered through 5-12Hz (theta band) of raw data
  Group /processing/theta/shank3 (LFP) 
  Group /processing/theta/shank3/shank3 (ElectricalSeries) no description
  Dataset /processing/theta/shank3/shank3/electrodes (DynamicTableRegion) table region for shank3 | shape = (64,) | dtype = int32
  Group /processing/theta/shank6 (LFP) 
  Group /processing/theta/shank6/shank6 (ElectricalSeries) no description
  Dataset /processing/theta/shank6/shank6/electrodes (DynamicTableRegion) table region for shank6 | shape = (64,) | dtype = int32
  session_description: head fixed mouse running in VR
  session_start_time: 2020-08-15T00:00:00-04:00
  timestamps_reference_time: 2020-08-15T00:00:00-04:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (135,) | dtype = object
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (135,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex) Index for VectorData 'electrodes' | shape = (135,) | dtype = uint8
  Dataset /units/id (ElementIdentifiers)  | shape = (135,) | dtype = int32
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (2838447,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (135,) | dtype = uint32
  Dataset /units/unit_type (VectorData) specify whether unit is classified as excitatory or inhibitory or unclassified | shape = (135,) | dtype = object


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/shank3 (ElectricalSeries) no description
  Dataset /acquisition/shank3/electrodes (DynamicTableRegion) table region for shank3 | shape = (64,) | dtype = int32
  Group /acquisition/shank6 (ElectricalSeries) no description
  Dataset /acquisition/shank6/electrodes (DynamicTableRegion) table region for shank6 | shape = (64,) | dtype = int32
  file_create_date: ['2023-09-10T01:22:19.860506-04:00']
  Group /general/devices/Masmanidis Probe (Device) UCLA Masmanidis Lab 256 Channel Silicon Probe (https://masmanidislab.neurobio.ucla.edu/technology.html)
  experiment_description: MEC, HPC dual-region silicon probe recording in head-fixed mouse running in VR
  experimenter: ['Susie Feng']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (512,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (512,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (512,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/isBadChannel (VectorData) whether the electrode is bad and excluded in analysis. | shape = (512,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/isMaster (VectorData) whether the electrode belong to the best representative shank for either HPC or MEC | shape = (512,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (512,) | dtype = object
  Group /general/extracellular_ephys/shank1 (ElectrodeGroup) electrode group for shank 1
  Group /general/extracellular_ephys/shank1/device (Device) UCLA Masmanidis Lab 256 Channel Silicon Probe (https://masmanidislab.neurobio.ucla.edu/technology.html)
  Group /general/extracellular_ephys/shank2 (ElectrodeGroup) electrode group for shank 2
  Group /general/extracellular_ephys/shank2/device (Device) UCLA Masmanidis Lab 256 Channel Silicon Probe (https://masmanidislab.neurobio.ucla.edu/technology.html)
  Group /general/extracellular_ephys/shank3 (ElectrodeGroup) electrode group for shank 3
  Group /general/extracellular_ephys/shank3/device (Device) UCLA Masmanidis Lab 256 Channel Silicon Probe (https://masmanidislab.neurobio.ucla.edu/technology.html)
  Group /general/extracellular_ephys/shank4 (ElectrodeGroup) electrode group for shank 4
  Group /general/extracellular_ephys/shank4/device (Device) UCLA Masmanidis Lab 256 Channel Silicon Probe (https://masmanidislab.neurobio.ucla.edu/technology.html)
  Group /general/extracellular_ephys/shank5 (ElectrodeGroup) electrode group for shank 5
  Group /general/extracellular_ephys/shank5/device (Device) UCLA Masmanidis Lab 256 Channel Silicon Probe (https://masmanidislab.neurobio.ucla.edu/technology.html)
  Group /general/extracellular_ephys/shank6 (ElectrodeGroup) electrode group for shank 6
  Group /general/extracellular_ephys/shank6/device (Device) UCLA Masmanidis Lab 256 Channel Silicon Probe (https://masmanidislab.neurobio.ucla.edu/technology.html)
  Group /general/extracellular_ephys/shank7 (ElectrodeGroup) electrode group for shank 7
  Group /general/extracellular_ephys/shank7/device (Device) UCLA Masmanidis Lab 256 Channel Silicon Probe (https://masmanidislab.neurobio.ucla.edu/technology.html)
  Group /general/extracellular_ephys/shank8 (ElectrodeGroup) electrode group for shank 8
  Group /general/extracellular_ephys/shank8/device (Device) UCLA Masmanidis Lab 256 Channel Silicon Probe (https://masmanidislab.neurobio.ucla.edu/technology.html)
  institution: Icahn School of Medicine at Mount Sinai
  lab: Tristan Shuman Laboratory
  related_publications: ['N/A']
  session_id: TS111-2
  Group /general/subject (Subject) 
  identifier: TS111-2
  Group /processing/behavior (ProcessingModule) Raw and processed behavioral data
  Group /processing/behavior/BehavioralEpochs (BehavioralEpochs) 
  Group /processing/behavior/BehavioralEpochs/seizure (IntervalSeries) Intervals when the mouse was seizing
  Group /processing/behavior/lick (BehavioralTimeSeries) 
  Group /processing/behavior/lick/lick (TimeSeries) Voltage output from lick sensor, a value of 5.0 indicate a lick
  Group /processing/behavior/position (Position) 
  Group /processing/behavior/position/position (SpatialSeries) no description
  Group /processing/behavior/reward (BehavioralTimeSeries) 
  Group /processing/behavior/reward/reward (TimeSeries) Driving voltage of water delievery valve, a value above 0.02 indicate a reward delivery
  Group /processing/behavior/speed (BehavioralTimeSeries) 
  Group /processing/behavior/speed/speed (TimeSeries) Output from VR track
  Group /processing/theta (ProcessingModule) Filtered out 60Hz then filtered through 5-12Hz (theta band) of raw data
  Group /processing/theta/shank3 (LFP) 
  Group /processing/theta/shank3/shank3 (ElectricalSeries) no description
  Dataset /processing/theta/shank3/shank3/electrodes (DynamicTableRegion) table region for shank3 | shape = (64,) | dtype = int32
  Group /processing/theta/shank6 (LFP) 
  Group /processing/theta/shank6/shank6 (ElectricalSeries) no description
  Dataset /processing/theta/shank6/shank6/electrodes (DynamicTableRegion) table region for shank6 | shape = (64,) | dtype = int32
  session_description: head fixed mouse running in VR
  session_start_time: 2020-08-17T00:00:00-04:00
  timestamps_reference_time: 2020-08-17T00:00:00-04:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (31,) | dtype = object
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (31,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex) Index for VectorData 'electrodes' | shape = (31,) | dtype = uint8
  Dataset /units/id (ElementIdentifiers)  | shape = (31,) | dtype = int32
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (664061,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (31,) | dtype = uint32
  Dataset /units/unit_type (VectorData) specify whether unit is classified as excitatory or inhibitory or unclassified | shape = (31,) | dtype = object


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/shank3 (ElectricalSeries) no description
  Dataset /acquisition/shank3/electrodes (DynamicTableRegion) table region for shank3 | shape = (64,) | dtype = int32
  Group /acquisition/shank5 (ElectricalSeries) no description
  Dataset /acquisition/shank5/electrodes (DynamicTableRegion) table region for shank5 | shape = (64,) | dtype = int32
  file_create_date: ['2023-09-10T00:14:03.542066-04:00']
  Group /general/devices/Masmanidis Probe (Device) UCLA Masmanidis Lab 256 Channel Silicon Probe (https://masmanidislab.neurobio.ucla.edu/technology.html)
  experiment_description: MEC, HPC dual-region silicon probe recording in head-fixed mouse running in VR
  experimenter: ['Susie Feng']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (512,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (512,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (512,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/isBadChannel (VectorData) whether the electrode is bad and excluded in analysis. | shape = (512,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/isMaster (VectorData) whether the electrode belong to the best representative shank for either HPC or MEC | shape = (512,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (512,) | dtype = object
  Group /general/extracellular_ephys/shank1 (ElectrodeGroup) electrode group for shank 1
  Group /general/extracellular_ephys/shank1/device (Device) UCLA Masmanidis Lab 256 Channel Silicon Probe (https://masmanidislab.neurobio.ucla.edu/technology.html)
  Group /general/extracellular_ephys/shank2 (ElectrodeGroup) electrode group for shank 2
  Group /general/extracellular_ephys/shank2/device (Device) UCLA Masmanidis Lab 256 Channel Silicon Probe (https://masmanidislab.neurobio.ucla.edu/technology.html)
  Group /general/extracellular_ephys/shank3 (ElectrodeGroup) electrode group for shank 3
  Group /general/extracellular_ephys/shank3/device (Device) UCLA Masmanidis Lab 256 Channel Silicon Probe (https://masmanidislab.neurobio.ucla.edu/technology.html)
  Group /general/extracellular_ephys/shank4 (ElectrodeGroup) electrode group for shank 4
  Group /general/extracellular_ephys/shank4/device (Device) UCLA Masmanidis Lab 256 Channel Silicon Probe (https://masmanidislab.neurobio.ucla.edu/technology.html)
  Group /general/extracellular_ephys/shank5 (ElectrodeGroup) electrode group for shank 5
  Group /general/extracellular_ephys/shank5/device (Device) UCLA Masmanidis Lab 256 Channel Silicon Probe (https://masmanidislab.neurobio.ucla.edu/technology.html)
  Group /general/extracellular_ephys/shank6 (ElectrodeGroup) electrode group for shank 6
  Group /general/extracellular_ephys/shank6/device (Device) UCLA Masmanidis Lab 256 Channel Silicon Probe (https://masmanidislab.neurobio.ucla.edu/technology.html)
  Group /general/extracellular_ephys/shank7 (ElectrodeGroup) electrode group for shank 7
  Group /general/extracellular_ephys/shank7/device (Device) UCLA Masmanidis Lab 256 Channel Silicon Probe (https://masmanidislab.neurobio.ucla.edu/technology.html)
  Group /general/extracellular_ephys/shank8 (ElectrodeGroup) electrode group for shank 8
  Group /general/extracellular_ephys/shank8/device (Device) UCLA Masmanidis Lab 256 Channel Silicon Probe (https://masmanidislab.neurobio.ucla.edu/technology.html)
  institution: Icahn School of Medicine at Mount Sinai
  lab: Tristan Shuman Laboratory
  related_publications: ['N/A']
  session_id: TS112-0
  Group /general/subject (Subject) 
  identifier: TS112-0
  Group /processing/behavior (ProcessingModule) Raw and processed behavioral data
  Group /processing/behavior/BehavioralEpochs (BehavioralEpochs) 
  Group /processing/behavior/BehavioralEpochs/seizure (IntervalSeries) Intervals when the mouse was seizing
  Group /processing/behavior/lick (BehavioralTimeSeries) 
  Group /processing/behavior/lick/lick (TimeSeries) Voltage output from lick sensor, a value of 5.0 indicate a lick
  Group /processing/behavior/position (Position) 
  Group /processing/behavior/position/position (SpatialSeries) no description
  Group /processing/behavior/reward (BehavioralTimeSeries) 
  Group /processing/behavior/reward/reward (TimeSeries) Driving voltage of water delievery valve, a value above 0.02 indicate a reward delivery
  Group /processing/behavior/speed (BehavioralTimeSeries) 
  Group /processing/behavior/speed/speed (TimeSeries) Output from VR track
  Group /processing/theta (ProcessingModule) Filtered out 60Hz then filtered through 5-12Hz (theta band) of raw data
  Group /processing/theta/shank3 (LFP) 
  Group /processing/theta/shank3/shank3 (ElectricalSeries) no description
  Dataset /processing/theta/shank3/shank3/electrodes (DynamicTableRegion) table region for shank3 | shape = (64,) | dtype = int32
  Group /processing/theta/shank5 (LFP) 
  Group /processing/theta/shank5/shank5 (ElectricalSeries) no description
  Dataset /processing/theta/shank5/shank5/electrodes (DynamicTableRegion) table region for shank5 | shape = (64,) | dtype = int32
  session_description: head fixed mouse running in VR
  session_start_time: 2020-07-22T00:00:00-04:00
  timestamps_reference_time: 2020-07-22T00:00:00-04:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (190,) | dtype = object
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (190,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex) Index for VectorData 'electrodes' | shape = (190,) | dtype = uint8
  Dataset /units/id (ElementIdentifiers)  | shape = (190,) | dtype = int32
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (2883292,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (190,) | dtype = uint32
  Dataset /units/unit_type (VectorData) specify whether unit is classified as excitatory or inhibitory or unclassified | shape = (190,) | dtype = object


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  Group /acquisition/shank3 (ElectricalSeries) no description
  Dataset /acquisition/shank3/electrodes (DynamicTableRegion) table region for shank3 | shape = (64,) | dtype = int32
  file_create_date: ['2023-09-10T00:20:35.547196-04:00']
  Group /general/devices/Masmanidis Probe (Device) UCLA Masmanidis Lab 256 Channel Silicon Probe (https://masmanidislab.neurobio.ucla.edu/technology.html)
  experiment_description: MEC, HPC dual-region silicon probe recording in head-fixed mouse running in VR
  experimenter: ['Susie Feng']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (512,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (512,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (512,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/isBadChannel (VectorData) whether the electrode is bad and excluded in analysis. | shape = (512,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/isMaster (VectorData) whether the electrode belong to the best representative shank for either HPC or MEC | shape = (512,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (512,) | dtype = object
  Group /general/extracellular_ephys/shank1 (ElectrodeGroup) electrode group for shank 1
  Group /general/extracellular_ephys/shank1/device (Device) UCLA Masmanidis Lab 256 Channel Silicon Probe (https://masmanidislab.neurobio.ucla.edu/technology.html)
  Group /general/extracellular_ephys/shank2 (ElectrodeGroup) electrode group for shank 2
  Group /general/extracellular_ephys/shank2/device (Device) UCLA Masmanidis Lab 256 Channel Silicon Probe (https://masmanidislab.neurobio.ucla.edu/technology.html)
  Group /general/extracellular_ephys/shank3 (ElectrodeGroup) electrode group for shank 3
  Group /general/extracellular_ephys/shank3/device (Device) UCLA Masmanidis Lab 256 Channel Silicon Probe (https://masmanidislab.neurobio.ucla.edu/technology.html)
  Group /general/extracellular_ephys/shank4 (ElectrodeGroup) electrode group for shank 4
  Group /general/extracellular_ephys/shank4/device (Device) UCLA Masmanidis Lab 256 Channel Silicon Probe (https://masmanidislab.neurobio.ucla.edu/technology.html)
  Group /general/extracellular_ephys/shank5 (ElectrodeGroup) electrode group for shank 5
  Group /general/extracellular_ephys/shank5/device (Device) UCLA Masmanidis Lab 256 Channel Silicon Probe (https://masmanidislab.neurobio.ucla.edu/technology.html)
  Group /general/extracellular_ephys/shank6 (ElectrodeGroup) electrode group for shank 6
  Group /general/extracellular_ephys/shank6/device (Device) UCLA Masmanidis Lab 256 Channel Silicon Probe (https://masmanidislab.neurobio.ucla.edu/technology.html)
  Group /general/extracellular_ephys/shank7 (ElectrodeGroup) electrode group for shank 7
  Group /general/extracellular_ephys/shank7/device (Device) UCLA Masmanidis Lab 256 Channel Silicon Probe (https://masmanidislab.neurobio.ucla.edu/technology.html)
  Group /general/extracellular_ephys/shank8 (ElectrodeGroup) electrode group for shank 8
  Group /general/extracellular_ephys/shank8/device (Device) UCLA Masmanidis Lab 256 Channel Silicon Probe (https://masmanidislab.neurobio.ucla.edu/technology.html)
  institution: Icahn School of Medicine at Mount Sinai
  lab: Tristan Shuman Laboratory
  related_publications: ['N/A']
  session_id: TS112-1
  Group /general/subject (Subject) 
  identifier: TS112-1
  Group /processing/behavior (ProcessingModule) Raw and processed behavioral data
  Group /processing/behavior/BehavioralEpochs (BehavioralEpochs) 
  Group /processing/behavior/BehavioralEpochs/seizure (IntervalSeries) Intervals when the mouse was seizing
  Group /processing/behavior/lick (BehavioralTimeSeries) 
  Group /processing/behavior/lick/lick (TimeSeries) Voltage output from lick sensor, a value of 5.0 indicate a lick
  Group /processing/behavior/position (Position) 
  Group /processing/behavior/position/position (SpatialSeries) no description
  Group /processing/behavior/reward (BehavioralTimeSeries) 
  Group /processing/behavior/reward/reward (TimeSeries) Driving voltage of water delievery valve, a value above 0.02 indicate a reward delivery
  Group /processing/behavior/speed (BehavioralTimeSeries) 
  Group /processing/behavior/speed/speed (TimeSeries) Output from VR track
  Group /processing/theta (ProcessingModule) Filtered out 60Hz then filtered through 5-12Hz (theta band) of raw data
  Group /processing/theta/shank3 (LFP) 
  Group /processing/theta/shank3/shank3 (ElectricalSeries) no description
  Dataset /processing/theta/shank3/shank3/electrodes (DynamicTableRegion) table region for shank3 | shape = (64,) | dtype = int32
  session_description: head fixed mouse running in VR
  session_start_time: 2020-07-28T00:00:00-04:00
  timestamps_reference_time: 2020-07-28T00:00:00-04:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (27,) | dtype = object
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (27,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex) Index for VectorData 'electrodes' | shape = (27,) | dtype = uint8
  Dataset /units/id (ElementIdentifiers)  | shape = (27,) | dtype = int32
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (537719,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (27,) | dtype = uint32
  Dataset /units/unit_type (VectorData) specify whether unit is classified as excitatory or inhibitory or unclassified | shape = (27,) | dtype = object
