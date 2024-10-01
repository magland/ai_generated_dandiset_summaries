
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000147/0.221122.2256
name: PPC_Finger: human posterior parietal cortex recordings during attempted finger movements
contributor: [{'name': 'Guan, Charles', 'email': 'cguan@caltech.edu', 'roleName': ['dcite:ContactPerson', 'dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-8040-8844', 'affiliation': [{'name': 'California Institute of Technology', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/05dxps055'}], 'includeInCitation': True}, {'name': 'Aflalo, Tyson', 'email': 'taflalo@caltech.edu', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-0101-2455', 'affiliation': [{'name': 'California Institute of Technology', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/05dxps055'}], 'includeInCitation': True}, {'name': 'Zhang, Carey', 'email': 'carey.zhang@gmail.com', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0001-9867-4510', 'affiliation': [{'name': 'California Institute of Technology', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/05dxps055'}], 'includeInCitation': True}, {'url': 'https://www.vis.caltech.edu/', 'name': 'Andersen, Richard', 'email': 'richard.andersen@vis.caltech.edu', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-7947-0472', 'affiliation': [{'name': 'California Institute of Technology', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/05dxps055'}], 'includeInCitation': True}]
description: This dataset contains neural activity and trial information from a tetraplegic human participant performing a brain-computer interface (BCI) finger press task. Neural activity was recorded from a 96-channel Utah array (Blackrock) implanted in the left posterior parietal cortex (PPC) at the junction of the postcentral and intraparietal sulci (PC-IP). On each trial, a finger cue, at a pseudorandom location on a screen, was selected. The participant immediately looked at the cue and pressed the cued finger until decoder feedback was shown (1.5 seconds after the cue).

This dataset includes sorted unit spiking times, finger cue, in-session classified finger, cue location, and trial timing.
assetsSummary: {'species': [{'name': 'Homo sapiens - Human', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9606'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 77665528, 'numberOfFiles': 10, 'numberOfSubjects': 1, 'variableMeasured': ['Units', 'ElectrodeGroup'], 'measurementTechnique': [{'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000147 has 10 NWB files.
10 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2022-02-11T09:11:12.614907-08:00']
  Group /general/devices/NSP1 (Device) Neuroport Recording System with Utah array
  experiment_description: Intracortical recordings during a brain-computer interface finger movement task
  experimenter: ['Tyson Aflalo' 'Carey Zhang']
  Group /general/extracellular_ephys/PPC (ElectrodeGroup) Utah array
  Group /general/extracellular_ephys/PPC/device (Device) Neuroport Recording System with Utah array
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (96,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (96,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (96,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (96,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (96,) | dtype = float64
  institution: California Institute of Technology
  lab: Andersen Lab
  session_id: 2018-09-10
  Group /general/subject (Subject) 
  identifier: sub-P1_ses-20180910T102421
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/Run (VectorData) run-block index (within session) | shape = (8,) | dtype = int64
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (8,) | dtype = int64
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (8,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (8,) | dtype = float64
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/Run (VectorData) no description | shape = (384,) | dtype = int64
  Dataset /intervals/trials/TrialNumber (VectorData) no description | shape = (384,) | dtype = uint64
  Dataset /intervals/trials/cue_location (VectorData) screen location (index) where text cue was displayed | shape = (384,) | dtype = uint8
  Dataset /intervals/trials/finger (VectorData) the finger cued during the trial | shape = (384,) | dtype = object
  Dataset /intervals/trials/finger_pred (VectorData) the finger predicted by the decoder during the trial | shape = (384,) | dtype = object
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (384,) | dtype = int64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (384,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (384,) | dtype = float64
  session_description: individual-finger press, main task
  session_start_time: 2018-09-10T10:24:21-07:00
  timestamps_reference_time: 2018-09-10T10:24:21-07:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (100,) | dtype = object
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (100,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex) Index for VectorData 'electrodes' | shape = (100,) | dtype = uint8
  Dataset /units/id (ElementIdentifiers)  | shape = (100,) | dtype = int64
  Dataset /units/obs_intervals (VectorData) the observation intervals for each unit | shape = (800, 2) | dtype = float64
  Dataset /units/obs_intervals_index (VectorIndex) Index for VectorData 'obs_intervals' | shape = (100,) | dtype = uint16
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (1286010,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (100,) | dtype = uint32
