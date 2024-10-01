
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000897/0.240605.1710
name: Neupane_Fiete_Jazayeri_Mental navigation_NHP_EntorhinalCortex
contributor: [{'name': 'Neupane, Sujaya', 'email': 'sujayanyaupane@gmail.com', 'roleName': ['dcite:Author', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0002-0052-3122', 'includeInCitation': True}, {'name': 'Fiete, Ila', 'email': 'fiete@mit.edu', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0003-4738-2539', 'includeInCitation': True}, {'name': 'Jazayeri, Mehrdad', 'email': 'mjaz@mit.edu', 'roleName': ['dcite:Author', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0002-9764-6961', 'includeInCitation': True}, {'name': 'National Institute of Mental Health', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/05xj56w78', 'awardNumber': 'NIMH-MH129046', 'includeInCitation': False}, {'name': 'Natural Science and Engineering Council of Canada', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01h531d29', 'awardNumber': 'NSERC PDF-516867-2018', 'includeInCitation': False}]
description: The dataset contains electrophysiology data recorded from the entorhinal cortex of two NHPs performing a mental navigation task. The recording probes used were V-probe with 32 channels or 64 channels, manufactured by Plexon Inc. 
assetsSummary: {'species': [{'name': 'Macaca mulatta - Rhesus monkey', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9544'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}, {'name': 'behavioral approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 361973386790, 'numberOfFiles': 30, 'numberOfSubjects': 2, 'variableMeasured': ['Units', 'ElectrodeGroup', 'SpatialSeries', 'ProcessingModule', 'ElectricalSeries'], 'measurementTechnique': [{'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000897 has 30 NWB files.
4 of these NWB files are of type 1.
15 of these NWB files are of type 2.
1 of these NWB files are of type 3.
1 of these NWB files are of type 4.
9 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2024-04-12T17:41:23.552357-04:00']
  Group /general/devices/vprobe0 (Device) 64-channel Plexon V-Probe
  experimenter: ['Neupane, Sujaya']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/channel_name (VectorData) unique channel reference | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/gain_to_uV (VectorData) no description | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (32,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/offset_to_uV (VectorData) no description | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_x (VectorData) rel_x | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_y (VectorData) rel_y | shape = (32,) | dtype = float64
  Group /general/extracellular_ephys/vprobe0 (ElectrodeGroup) A group representing electrodes on vprobe0
  Group /general/extracellular_ephys/vprobe0/device (Device) 64-channel Plexon V-Probe
  institution: MIT
  lab: Jazayeri, Fiete
  session_id: 08152019
  Group /general/subject (Subject) 
  identifier: 88089ef9-ef9e-4115-917b-a94253a668a6
  Group /intervals/trials (TimeIntervals) data about each trial
  Dataset /intervals/trials/attempt (VectorData) # of attempts to perform the trial | shape = (2078,) | dtype = float64
  Dataset /intervals/trials/curr (VectorData) Start landmark | shape = (2078,) | dtype = float64
  Dataset /intervals/trials/delay (VectorData) .4-1.4s delay for go cue. Drawn from an exponential distribution | shape = (2078,) | dtype = float64
  Dataset /intervals/trials/gocuettl (VectorData) Time of go cue. | shape = (2078,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (2078,) | dtype = int64
  Dataset /intervals/trials/joy1offttl (VectorData) Time of joystick release | shape = (2078,) | dtype = float64
  Dataset /intervals/trials/joy1onttl (VectorData) Time of joystick press | shape = (2078,) | dtype = float64
  Dataset /intervals/trials/numrepeat (VectorData) # of times the same condition was repeated, sometimes implemented to prevent deliberate aborts | shape = (2078,) | dtype = float64
  Dataset /intervals/trials/rt (VectorData) Response time = joystick press time - go cue time | shape = (2078,) | dtype = float64
  Dataset /intervals/trials/seqq (VectorData) which sequence: 1,2,3 or 4 | shape = (2078,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (2078,) | dtype = float64
  Dataset /intervals/trials/stim1onttl (VectorData) Time of stimulus onset | shape = (2078,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (2078,) | dtype = float64
  Dataset /intervals/trials/succ (VectorData) binary: successful trial or not | shape = (2078,) | dtype = float64
  Dataset /intervals/trials/ta (VectorData) Actual vector (seconds) | shape = (2078,) | dtype = float64
  Dataset /intervals/trials/target (VectorData) Target landmark | shape = (2078,) | dtype = float64
  Dataset /intervals/trials/tp (VectorData) Produced vector (seconds) | shape = (2078,) | dtype = float64
  Dataset /intervals/trials/trial_type (VectorData) 1=linear map visible (NTS), 2=centre visible, periphery occluded, 3=fully occluded (MNAV) | shape = (2078,) | dtype = float64
  Dataset /intervals/trials/validtrials_mm (VectorData) binary: trial labeled as valid or lapse based on Gaussian Mixture Model fit to tp distrbutions | shape = (2078,) | dtype = float64
  Group /processing/behavior (ProcessingModule) Contains behavior, audio, and reward data from experiment.
  Group /processing/behavior/eye_position (SpatialSeries) Eye position data recorded by EyeLink camera
  Group /processing/behavior/hand_position (SpatialSeries) Hand position data recorded by joystick potentiometer
  Group /processing/ecephys (ProcessingModule) Intermediate data from extracellular electrophysiology recordings, e.g., LFP.
  Group /processing/ecephys/units (Units) Autogenerated by neuroconv.
  Dataset /processing/ecephys/units/amp (VectorData) No description. | shape = (59,) | dtype = float64
  Dataset /processing/ecephys/units/ch (VectorData) No description. | shape = (59,) | dtype = float64
  Dataset /processing/ecephys/units/depth (VectorData) No description. | shape = (59,) | dtype = float64
  Dataset /processing/ecephys/units/fr (VectorData) No description. | shape = (59,) | dtype = float64
  Dataset /processing/ecephys/units/id (ElementIdentifiers)  | shape = (59,) | dtype = int64
  Dataset /processing/ecephys/units/n_spikes (VectorData) No description. | shape = (59,) | dtype = float64
  Dataset /processing/ecephys/units/original_cluster_id (VectorData) No description. | shape = (59,) | dtype = float64
  Dataset /processing/ecephys/units/quality (VectorData) Quality of the unit as defined by phy (good, mua, noise). | shape = (59,) | dtype = object
  Dataset /processing/ecephys/units/sh (VectorData) No description. | shape = (59,) | dtype = float64
  Dataset /processing/ecephys/units/spike_times (VectorData) the spike times for each unit | shape = (4289692,) | dtype = float64
  Dataset /processing/ecephys/units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (59,) | dtype = uint32
  Dataset /processing/ecephys/units/unit_name (VectorData) Unique reference for each unit. | shape = (59,) | dtype = object
  session_description: Data from macaque performing mental navigation task. Subject is presented with a start and a target landmark, sampled from a linear map of 6 landmarks on a screen. After a delay, the subject is then cued with a go signal to navigate from start to target landmark with a joystick. Subject should respond by deflecting the joystick in the right direction and holding it until the subject thinks it has arrived at the target landmark. The visual drift or intervening landmarks are all occluded from view making the task a purely mental navigation.
  session_start_time: 2019-08-15T00:00:00-04:00
  timestamps_reference_time: 2019-08-15T00:00:00-04:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeriesVP0 (ElectricalSeries) Acquisition traces for the ElectricalSeriesVP0.
  Dataset /acquisition/ElectricalSeriesVP0/electrodes (DynamicTableRegion) electrode_table_region | shape = (32,) | dtype = int64
  file_create_date: ['2024-04-12T17:41:52.078489-04:00']
  Group /general/devices/vprobe0 (Device) 64-channel Plexon V-Probe
  experimenter: ['Neupane, Sujaya']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/channel_name (VectorData) unique channel reference | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/gain_to_uV (VectorData) no description | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (32,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/offset_to_uV (VectorData) no description | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_x (VectorData) rel_x | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_y (VectorData) rel_y | shape = (32,) | dtype = float64
  Group /general/extracellular_ephys/vprobe0 (ElectrodeGroup) A group representing electrodes on vprobe0
  Group /general/extracellular_ephys/vprobe0/device (Device) 64-channel Plexon V-Probe
  institution: MIT
  lab: Jazayeri, Fiete
  session_id: 08152019
  Group /general/subject (Subject) 
  identifier: 293b67c2-4dea-432e-af19-d5e1b3a50aff
  session_description: Data from macaque performing mental navigation task. Subject is presented with a start and a target landmark, sampled from a linear map of 6 landmarks on a screen. After a delay, the subject is then cued with a go signal to navigate from start to target landmark with a joystick. Subject should respond by deflecting the joystick in the right direction and holding it until the subject thinks it has arrived at the target landmark. The visual drift or intervening landmarks are all occluded from view making the task a purely mental navigation.
  session_start_time: 2019-08-15T00:00:00-04:00
  timestamps_reference_time: 2019-08-15T00:00:00-04:00


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2024-03-07T18:01:26.383739-05:00']
  Group /general/devices/vprobe0 (Device) 64-channel Plexon V-Probe
  experimenter: ['Neupane, Sujaya']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/channel_name (VectorData) unique channel reference | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/gain_to_uV (VectorData) no description | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (32,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/offset_to_uV (VectorData) no description | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_x (VectorData) rel_x | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_y (VectorData) rel_y | shape = (32,) | dtype = float64
  Group /general/extracellular_ephys/vprobe0 (ElectrodeGroup) A group representing electrodes on vprobe0
  Group /general/extracellular_ephys/vprobe0/device (Device) 64-channel Plexon V-Probe
  institution: MIT
  lab: Jazayeri, Fiete
  session_id: 08292019
  Group /general/subject (Subject) 
  identifier: 05764f93-afa4-4fa9-90a6-0ecf52fbe172
  Group /intervals/trials (TimeIntervals) data about each trial
  Dataset /intervals/trials/attempt (VectorData) # of attempts to perform the trial | shape = (2434,) | dtype = float64
  Dataset /intervals/trials/curr (VectorData) Start landmark | shape = (2434,) | dtype = float64
  Dataset /intervals/trials/delay (VectorData) .4-1.4s delay for go cue. Drawn from an exponential distribution | shape = (2434,) | dtype = float64
  Dataset /intervals/trials/gocuettl (VectorData) Time of go cue. | shape = (2434,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (2434,) | dtype = int64
  Dataset /intervals/trials/joy1offttl (VectorData) Time of joystick release | shape = (2434,) | dtype = float64
  Dataset /intervals/trials/joy1onttl (VectorData) Time of joystick press | shape = (2434,) | dtype = float64
  Dataset /intervals/trials/numrepeat (VectorData) # of times the same condition was repeated, sometimes implemented to prevent deliberate aborts | shape = (2434,) | dtype = float64
  Dataset /intervals/trials/rt (VectorData) Response time = joystick press time - go cue time | shape = (2434,) | dtype = float64
  Dataset /intervals/trials/seqq (VectorData) which sequence: 1,2,3 or 4 | shape = (2434,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (2434,) | dtype = float64
  Dataset /intervals/trials/stim1onttl (VectorData) Time of stimulus onset | shape = (2434,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (2434,) | dtype = float64
  Dataset /intervals/trials/succ (VectorData) binary: successful trial or not | shape = (2434,) | dtype = float64
  Dataset /intervals/trials/ta (VectorData) Actual vector (seconds) | shape = (2434,) | dtype = float64
  Dataset /intervals/trials/target (VectorData) Target landmark | shape = (2434,) | dtype = float64
  Dataset /intervals/trials/tp (VectorData) Produced vector (seconds) | shape = (2434,) | dtype = float64
  Dataset /intervals/trials/trial_type (VectorData) 1=linear map visible (NTS), 2=centre visible, periphery occluded, 3=fully occluded (MNAV) | shape = (2434,) | dtype = float64
  Dataset /intervals/trials/validtrials_mm (VectorData) binary: trial labeled as valid or lapse based on Gaussian Mixture Model fit to tp distrbutions | shape = (2434,) | dtype = float64
  Group /processing/behavior (ProcessingModule) Contains behavior, audio, and reward data from experiment.
  Group /processing/behavior/eye_position (SpatialSeries) Eye position data recorded by EyeLink camera
  Group /processing/behavior/hand_position (SpatialSeries) Hand position data recorded by joystick potentiometer
  Group /processing/ecephys (ProcessingModule) Intermediate data from extracellular electrophysiology recordings, e.g., LFP.
  Group /processing/ecephys/units (Units) Autogenerated by neuroconv.
  Dataset /processing/ecephys/units/Amplitude (VectorData) No description. | shape = (95,) | dtype = float64
  Dataset /processing/ecephys/units/ContamPct (VectorData) No description. | shape = (95,) | dtype = float64
  Dataset /processing/ecephys/units/KSLabel (VectorData) No description. | shape = (95,) | dtype = object
  Dataset /processing/ecephys/units/amp (VectorData) No description. | shape = (95,) | dtype = float64
  Dataset /processing/ecephys/units/ch (VectorData) No description. | shape = (95,) | dtype = float64
  Dataset /processing/ecephys/units/depth (VectorData) No description. | shape = (95,) | dtype = float64
  Dataset /processing/ecephys/units/fr (VectorData) No description. | shape = (95,) | dtype = float64
  Dataset /processing/ecephys/units/id (ElementIdentifiers)  | shape = (95,) | dtype = int64
  Dataset /processing/ecephys/units/n_spikes (VectorData) No description. | shape = (95,) | dtype = float64
  Dataset /processing/ecephys/units/original_cluster_id (VectorData) No description. | shape = (95,) | dtype = float64
  Dataset /processing/ecephys/units/quality (VectorData) Quality of the unit as defined by phy (good, mua, noise). | shape = (95,) | dtype = object
  Dataset /processing/ecephys/units/sh (VectorData) No description. | shape = (95,) | dtype = float64
  Dataset /processing/ecephys/units/spike_times (VectorData) the spike times for each unit | shape = (6256417,) | dtype = float64
  Dataset /processing/ecephys/units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (95,) | dtype = uint32
  Dataset /processing/ecephys/units/unit_name (VectorData) Unique reference for each unit. | shape = (95,) | dtype = object
  session_description: Data from macaque performing mental navigation task. Subject is presented with a start and a target landmark, sampled from a linear map of 6 landmarks on a screen. After a delay, the subject is then cued with a go signal to navigate from start to target landmark with a joystick. Subject should respond by deflecting the joystick in the right direction and holding it until the subject thinks it has arrived at the target landmark. The visual drift or intervening landmarks are all occluded from view making the task a purely mental navigation.
  session_start_time: 2019-08-29T00:00:00-04:00
  timestamps_reference_time: 2019-08-29T00:00:00-04:00


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2024-04-13T11:40:39.372805-04:00']
  Group /general/devices/vprobe0 (Device) 64-channel Plexon V-Probe
  experimenter: ['Neupane, Sujaya']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/channel_name (VectorData) unique channel reference | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/gain_to_uV (VectorData) no description | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (32,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/offset_to_uV (VectorData) no description | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_x (VectorData) rel_x | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_y (VectorData) rel_y | shape = (32,) | dtype = float64
  Group /general/extracellular_ephys/vprobe0 (ElectrodeGroup) A group representing electrodes on vprobe0
  Group /general/extracellular_ephys/vprobe0/device (Device) 64-channel Plexon V-Probe
  institution: MIT
  lab: Jazayeri, Fiete
  session_id: 09172019
  Group /general/subject (Subject) 
  identifier: 57967824-ccc6-463a-881e-5397b8c8ff03
  Group /intervals/trials (TimeIntervals) data about each trial
  Dataset /intervals/trials/attempt (VectorData) # of attempts to perform the trial | shape = (2257,) | dtype = float64
  Dataset /intervals/trials/curr (VectorData) Start landmark | shape = (2257,) | dtype = float64
  Dataset /intervals/trials/delay (VectorData) .4-1.4s delay for go cue. Drawn from an exponential distribution | shape = (2257,) | dtype = float64
  Dataset /intervals/trials/gocuettl (VectorData) Time of go cue. | shape = (2257,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (2257,) | dtype = int64
  Dataset /intervals/trials/joy1offttl (VectorData) Time of joystick release | shape = (2257,) | dtype = float64
  Dataset /intervals/trials/joy1onttl (VectorData) Time of joystick press | shape = (2257,) | dtype = float64
  Dataset /intervals/trials/numrepeat (VectorData) # of times the same condition was repeated, sometimes implemented to prevent deliberate aborts | shape = (2257,) | dtype = float64
  Dataset /intervals/trials/rt (VectorData) Response time = joystick press time - go cue time | shape = (2257,) | dtype = float64
  Dataset /intervals/trials/seqq (VectorData) which sequence: 1,2,3 or 4 | shape = (2257,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (2257,) | dtype = float64
  Dataset /intervals/trials/stim1onttl (VectorData) Time of stimulus onset | shape = (2257,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (2257,) | dtype = float64
  Dataset /intervals/trials/succ (VectorData) binary: successful trial or not | shape = (2257,) | dtype = float64
  Dataset /intervals/trials/ta (VectorData) Actual vector (seconds) | shape = (2257,) | dtype = float64
  Dataset /intervals/trials/target (VectorData) Target landmark | shape = (2257,) | dtype = float64
  Dataset /intervals/trials/tp (VectorData) Produced vector (seconds) | shape = (2257,) | dtype = float64
  Dataset /intervals/trials/trial_type (VectorData) 1=linear map visible (NTS), 2=centre visible, periphery occluded, 3=fully occluded (MNAV) | shape = (2257,) | dtype = float64
  Dataset /intervals/trials/validtrials_mm (VectorData) binary: trial labeled as valid or lapse based on Gaussian Mixture Model fit to tp distrbutions | shape = (2257,) | dtype = float64
  Group /processing/behavior (ProcessingModule) Contains behavior, audio, and reward data from experiment.
  Group /processing/behavior/eye_position (SpatialSeries) Eye position data recorded by EyeLink camera
  Group /processing/behavior/hand_position (SpatialSeries) Hand position data recorded by joystick potentiometer
  Group /processing/ecephys (ProcessingModule) Intermediate data from extracellular electrophysiology recordings, e.g., LFP.
  Group /processing/ecephys/units (Units) Autogenerated by neuroconv.
  Dataset /processing/ecephys/units/id (ElementIdentifiers)  | shape = (64,) | dtype = int64
  Dataset /processing/ecephys/units/original_cluster_id (VectorData) No description. | shape = (64,) | dtype = float64
  Dataset /processing/ecephys/units/quality (VectorData) Quality of the unit as defined by phy (good, mua, noise). | shape = (64,) | dtype = object
  Dataset /processing/ecephys/units/spike_times (VectorData) the spike times for each unit | shape = (2386730,) | dtype = float64
  Dataset /processing/ecephys/units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (64,) | dtype = uint32
  Dataset /processing/ecephys/units/unit_name (VectorData) Unique reference for each unit. | shape = (64,) | dtype = object
  session_description: Data from macaque performing mental navigation task. Subject is presented with a start and a target landmark, sampled from a linear map of 6 landmarks on a screen. After a delay, the subject is then cued with a go signal to navigate from start to target landmark with a joystick. Subject should respond by deflecting the joystick in the right direction and holding it until the subject thinks it has arrived at the target landmark. The visual drift or intervening landmarks are all occluded from view making the task a purely mental navigation.
  session_start_time: 2019-09-17T00:00:00-04:00
  timestamps_reference_time: 2019-09-17T00:00:00-04:00


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2024-04-24T16:33:40.006602-04:00']
  Group /general/devices/vprobe0 (Device) 64-channel Plexon V-Probe
  experimenter: ['Neupane, Sujaya']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/channel_name (VectorData) unique channel reference | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/gain_to_uV (VectorData) no description | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (32,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/offset_to_uV (VectorData) no description | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_x (VectorData) rel_x | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_y (VectorData) rel_y | shape = (32,) | dtype = float64
  Group /general/extracellular_ephys/vprobe0 (ElectrodeGroup) A group representing electrodes on vprobe0
  Group /general/extracellular_ephys/vprobe0/device (Device) 64-channel Plexon V-Probe
  institution: MIT
  lab: Jazayeri, Fiete
  session_id: 04122021
  Group /general/subject (Subject) 
  identifier: b761b606-0a28-44d8-b7a8-1e4b7f4ae62b
  Group /intervals/trials (TimeIntervals) data about each trial
  Dataset /intervals/trials/attempt (VectorData) # of attempts to perform the trial | shape = (3254,) | dtype = float64
  Dataset /intervals/trials/curr (VectorData) Start landmark | shape = (3254,) | dtype = float64
  Dataset /intervals/trials/delay (VectorData) .4-1.4s delay for go cue. Drawn from an exponential distribution | shape = (3254,) | dtype = float64
  Dataset /intervals/trials/gocuettl (VectorData) Time of go cue. | shape = (3254,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (3254,) | dtype = int64
  Dataset /intervals/trials/joy1offttl (VectorData) Time of joystick release | shape = (3254,) | dtype = float64
  Dataset /intervals/trials/joy1onttl (VectorData) Time of joystick press | shape = (3254,) | dtype = float64
  Dataset /intervals/trials/numrepeat (VectorData) # of times the same condition was repeated, sometimes implemented to prevent deliberate aborts | shape = (3254,) | dtype = float64
  Dataset /intervals/trials/rt (VectorData) Response time = joystick press time - go cue time | shape = (3254,) | dtype = float64
  Dataset /intervals/trials/seqq (VectorData) which sequence: 1,2,3 or 4 | shape = (3254,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (3254,) | dtype = float64
  Dataset /intervals/trials/stim1onttl (VectorData) Time of stimulus onset | shape = (3254,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (3254,) | dtype = float64
  Dataset /intervals/trials/succ (VectorData) binary: successful trial or not | shape = (3254,) | dtype = float64
  Dataset /intervals/trials/ta (VectorData) Actual vector (seconds) | shape = (3254,) | dtype = float64
  Dataset /intervals/trials/target (VectorData) Target landmark | shape = (3254,) | dtype = float64
  Dataset /intervals/trials/tp (VectorData) Produced vector (seconds) | shape = (3254,) | dtype = float64
  Dataset /intervals/trials/trial_type (VectorData) 1=linear map visible (NTS), 2=centre visible, periphery occluded, 3=fully occluded (MNAV) | shape = (3254,) | dtype = float64
  Dataset /intervals/trials/validtrials_mm (VectorData) binary: trial labeled as valid or lapse based on Gaussian Mixture Model fit to tp distrbutions | shape = (3254,) | dtype = float64
  Group /processing/behavior (ProcessingModule) Contains behavior, audio, and reward data from experiment.
  Group /processing/behavior/eye_position (SpatialSeries) Eye position data recorded by EyeLink camera
  Group /processing/behavior/hand_position (SpatialSeries) Hand position data recorded by joystick potentiometer
  Group /processing/ecephys (ProcessingModule) Intermediate data from extracellular electrophysiology recordings, e.g., LFP.
  Group /processing/ecephys/units (Units) Autogenerated by neuroconv.
  Dataset /processing/ecephys/units/Amplitude (VectorData) No description. | shape = (98,) | dtype = float64
  Dataset /processing/ecephys/units/ContamPct (VectorData) No description. | shape = (98,) | dtype = float64
  Dataset /processing/ecephys/units/KSLabel (VectorData) No description. | shape = (98,) | dtype = object
  Dataset /processing/ecephys/units/KSLabel_repeat (VectorData) No description. | shape = (98,) | dtype = object
  Dataset /processing/ecephys/units/id (ElementIdentifiers)  | shape = (98,) | dtype = int64
  Dataset /processing/ecephys/units/original_cluster_id (VectorData) No description. | shape = (98,) | dtype = float64
  Dataset /processing/ecephys/units/spike_times (VectorData) the spike times for each unit | shape = (4476273,) | dtype = float64
  Dataset /processing/ecephys/units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (98,) | dtype = uint32
  Dataset /processing/ecephys/units/unit_name (VectorData) Unique reference for each unit. | shape = (98,) | dtype = object
  session_description: Data from macaque performing mental navigation task. Subject is presented with a start and a target landmark, sampled from a linear map of 6 landmarks on a screen. After a delay, the subject is then cued with a go signal to navigate from start to target landmark with a joystick. Subject should respond by deflecting the joystick in the right direction and holding it until the subject thinks it has arrived at the target landmark. The visual drift or intervening landmarks are all occluded from view making the task a purely mental navigation.
  session_start_time: 2021-04-12T00:00:00-04:00
  timestamps_reference_time: 2021-04-12T00:00:00-04:00
