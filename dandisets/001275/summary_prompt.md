
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001275/draft
name: Mental navigation primate PPC Neupane_Fiete_Jazayeri
contributor: [{'name': 'Neupane, Sujaya', 'email': 'sujayanyaupane@gmail.com', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}]
description: This dataset contains neurophysiology data collected from two primates during a mental navigation task associated with a previously published study (https://doi.org/10.1038/s41586-024-07557-z). Data from the entorhinal cortex is open-sourced here: https://doi.org/10.48324/dandi.000897/0.240605.1710
assetsSummary: {'species': [{'name': 'Macaca mulatta - Rhesus monkey', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9544'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}, {'name': 'behavioral approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 2530041730, 'numberOfFiles': 5, 'numberOfSubjects': 1, 'variableMeasured': ['Units', 'ElectrodeGroup', 'ProcessingModule', 'SpatialSeries'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 001275 has 10 NWB files.
5 of these NWB files are of type 1.
5 of these NWB files are of type 2.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2024-12-04T21:22:10.015690-05:00']
  Group /general/devices/Neuropixel-Imec (Device) {"probe_type": "0", "probe_type_description": "NP1.0", "flex_part_number": "NP2_FLEX_0", "connected_base_station_part_number": "NP2_QBSC_00"}
  experimenter: ['Neupane, Sujaya']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/channel_name (VectorData) no description | shape = (768,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/contact_shapes (VectorData) The shape of the electrode | shape = (768,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/gain_to_uV (VectorData) no description | shape = (768,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (768,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (768,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (768,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/inter_sample_shift (VectorData) no description | shape = (768,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (768,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/offset_to_uV (VectorData) no description | shape = (768,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_x (VectorData) rel_x | shape = (768,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_y (VectorData) rel_y | shape = (768,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/shank_electrode_number (VectorData) 0-indexed channel within a shank. | shape = (768,) | dtype = float64
  Group /general/extracellular_ephys/s0 (ElectrodeGroup) a group representing shank s0
  Group /general/extracellular_ephys/s0/device (Device) {"probe_type": "0", "probe_type_description": "NP1.0", "flex_part_number": "NP2_FLEX_0", "connected_base_station_part_number": "NP2_QBSC_00"}
  institution: MIT
  lab: Jazayeri, Fiete
  session_id: 03122021
  Group /general/subject (Subject) 
  identifier: 16889466-93e9-4999-afc8-f8cae7bf2295
  Group /intervals/trials (TimeIntervals) data about each trial
  Dataset /intervals/trials/attempt (VectorData) # of attempts to perform the trial | shape = (3178,) | dtype = float64
  Dataset /intervals/trials/curr (VectorData) Start landmark | shape = (3178,) | dtype = float64
  Dataset /intervals/trials/delay (VectorData) .4-1.4s delay for go cue. Drawn from an exponential distribution | shape = (3178,) | dtype = float64
  Dataset /intervals/trials/gocuettl (VectorData) Time of go cue. | shape = (3178,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (3178,) | dtype = int64
  Dataset /intervals/trials/joy1offttl (VectorData) Time of joystick release | shape = (3178,) | dtype = float64
  Dataset /intervals/trials/joy1onttl (VectorData) Time of joystick press | shape = (3178,) | dtype = float64
  Dataset /intervals/trials/numrepeat (VectorData) # of times the same condition was repeated, sometimes implemented to prevent deliberate aborts | shape = (3178,) | dtype = float64
  Dataset /intervals/trials/rt (VectorData) Response time = joystick press time - go cue time | shape = (3178,) | dtype = float64
  Dataset /intervals/trials/seqq (VectorData) which sequence: 1,2,3 or 4 | shape = (3178,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (3178,) | dtype = float64
  Dataset /intervals/trials/stim1onttl (VectorData) Time of stimulus onset | shape = (3178,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (3178,) | dtype = float64
  Dataset /intervals/trials/succ (VectorData) binary: successful trial or not | shape = (3178,) | dtype = float64
  Dataset /intervals/trials/ta (VectorData) Actual vector (seconds) | shape = (3178,) | dtype = float64
  Dataset /intervals/trials/target (VectorData) Target landmark | shape = (3178,) | dtype = float64
  Dataset /intervals/trials/tp (VectorData) Produced vector (seconds) | shape = (3178,) | dtype = float64
  Dataset /intervals/trials/trial_type (VectorData) 1=linear map visible (NTS), 2=centre visible, periphery occluded, 3=fully occluded (MNAV) | shape = (3178,) | dtype = float64
  Dataset /intervals/trials/validtrials_mm (VectorData) binary: trial labeled as valid or lapse based on Gaussian Mixture Model fit to tp distrbutions | shape = (3178,) | dtype = float64
  Group /processing/behavior (ProcessingModule) Contains behavior, audio, and reward data from experiment.
  Group /processing/behavior/eye_position (SpatialSeries) Eye position data recorded by EyeLink camera
  Group /processing/behavior/hand_position (SpatialSeries) Hand position data recorded by joystick potentiometer
  Group /processing/ecephys (ProcessingModule) Intermediate data from extracellular electrophysiology recordings, e.g., LFP.
  Group /processing/ecephys/units (Units) Autogenerated by neuroconv.
  Dataset /processing/ecephys/units/Amplitude (VectorData) No description. | shape = (480,) | dtype = float64
  Dataset /processing/ecephys/units/ContamPct (VectorData) No description. | shape = (480,) | dtype = float64
  Dataset /processing/ecephys/units/KSLabel (VectorData) No description. | shape = (480,) | dtype = object
  Dataset /processing/ecephys/units/KSLabel_repeat (VectorData) No description. | shape = (480,) | dtype = object
  Dataset /processing/ecephys/units/id (ElementIdentifiers)  | shape = (480,) | dtype = int64
  Dataset /processing/ecephys/units/original_cluster_id (VectorData) No description. | shape = (480,) | dtype = float64
  Dataset /processing/ecephys/units/spike_times (VectorData) the spike times for each unit | shape = (8443704,) | dtype = float64
  Dataset /processing/ecephys/units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (480,) | dtype = uint32
  Dataset /processing/ecephys/units/unit_name (VectorData) Unique reference for each unit. | shape = (480,) | dtype = object
  session_description: Data from macaque performing mental navigation task. Subject is presented with a start and a target landmark, sampled from a linear map of 6 landmarks on a screen. After a delay, the subject is then cued with a go signal to navigate from start to target landmark with a joystick. Subject should respond by deflecting the joystick in the right direction and holding it until the subject thinks it has arrived at the target landmark. The visual drift or intervening landmarks are all occluded from view making the task a purely mental navigation.
  session_start_time: 2021-03-12T00:00:00-05:00
  timestamps_reference_time: 2021-03-12T00:00:00-05:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeriesAP (ElectricalSeries) Acquisition traces for the ElectricalSeriesAP.
  Dataset /acquisition/ElectricalSeriesAP/electrodes (DynamicTableRegion) electrode_table_region | shape = (384,) | dtype = int64
  Group /acquisition/ElectricalSeriesLF (ElectricalSeries) Acquisition traces for the ElectricalSeriesLF.
  Dataset /acquisition/ElectricalSeriesLF/electrodes (DynamicTableRegion) electrode_table_region | shape = (384,) | dtype = int64
  file_create_date: ['2024-12-04T21:23:08.634708-05:00']
  Group /general/devices/Neuropixel-Imec (Device) {"probe_type": "0", "probe_type_description": "NP1.0", "flex_part_number": "NP2_FLEX_0", "connected_base_station_part_number": "NP2_QBSC_00"}
  experimenter: ['Neupane, Sujaya']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/channel_name (VectorData) no description | shape = (768,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/contact_shapes (VectorData) The shape of the electrode | shape = (768,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/gain_to_uV (VectorData) no description | shape = (768,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (768,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (768,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (768,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/inter_sample_shift (VectorData) no description | shape = (768,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (768,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/offset_to_uV (VectorData) no description | shape = (768,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_x (VectorData) rel_x | shape = (768,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_y (VectorData) rel_y | shape = (768,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/shank_electrode_number (VectorData) 0-indexed channel within a shank. | shape = (768,) | dtype = float64
  Group /general/extracellular_ephys/s0 (ElectrodeGroup) a group representing shank s0
  Group /general/extracellular_ephys/s0/device (Device) {"probe_type": "0", "probe_type_description": "NP1.0", "flex_part_number": "NP2_FLEX_0", "connected_base_station_part_number": "NP2_QBSC_00"}
  institution: MIT
  lab: Jazayeri, Fiete
  session_id: 03122021
  Group /general/subject (Subject) 
  identifier: 95b35ace-5cd6-437b-8633-c885a72db1c5
  session_description: Data from macaque performing mental navigation task. Subject is presented with a start and a target landmark, sampled from a linear map of 6 landmarks on a screen. After a delay, the subject is then cued with a go signal to navigate from start to target landmark with a joystick. Subject should respond by deflecting the joystick in the right direction and holding it until the subject thinks it has arrived at the target landmark. The visual drift or intervening landmarks are all occluded from view making the task a purely mental navigation.
  session_start_time: 2021-03-12T00:00:00-05:00
  timestamps_reference_time: 2021-03-12T00:00:00-05:00
