
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000252/0.230408.2207
name: Finger_RL: human intracortical recordings during attempted finger movements of right and left hands
contributor: [{'name': 'Guan, Charles', 'email': 'cguan@caltech.edu', 'roleName': ['dcite:ContactPerson', 'dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-8040-8844', 'affiliation': [{'name': 'California Institute of Technology', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/05dxps055'}], 'includeInCitation': True}, {'name': 'Aflalo, Tyson', 'email': 'taflalo@caltech.edu', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-0101-2455', 'affiliation': [{'name': 'California Institute of Technology', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/05dxps055'}], 'includeInCitation': True}, {'name': 'Kadlec, Kelly', 'email': 'kkadlec@caltech.edu', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-8765-7253', 'affiliation': [{'name': 'California Institute of Technology', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/05dxps055'}], 'includeInCitation': True}, {'name': 'Gamez, Jorge', 'email': 'jgamez@caltech.edu', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [{'name': 'California Institute of Technology', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/05dxps055'}], 'includeInCitation': True}, {'url': 'https://www.nei.nih.gov/', 'name': 'NIH National Eye Institute', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/03wkg3b53', 'awardNumber': 'UG1EY032039, R01EY015545', 'contactPoint': [], 'includeInCitation': False}, {'name': 'T&C Chen Brain-Machine Interface Center', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'contactPoint': [], 'includeInCitation': False}]
description: This dataset contains single-neuron recordings from two tetraplegic human participants as they attempted individual finger movements. One participant had an electrode array implanted in the left posterior parietal cortex (PPC) at the junction of the postcentral and intraparietal sulci (PC-IP). The other participant had one electrode array implanted in the hand knob of the left motor cortex (MC) and one electrode array implanted in the superior parietal lobule (SPL) of the left PPC.
assetsSummary: {'species': [{'name': 'Homo sapiens - Human', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9606'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 38128728, 'numberOfFiles': 12, 'numberOfSubjects': 2, 'variableMeasured': ['ElectrodeGroup', 'Units'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000252 has 12 NWB files.
2 of these NWB files are of type 1.
10 of these NWB files are of type 2.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2023-04-08T14:38:29.962369-07:00']
  Group /general/devices/NSP1 (Device) Neuroport Recording System with Utah array
  Group /general/devices/NSP2 (Device) Neuroport Recording System with Utah array
  experiment_description: Intracortical recordings during contralateral/ipsilateral finger movement
  experimenter: ['Tyson Aflalo']
  Group /general/extracellular_ephys/MC (ElectrodeGroup) Utah array in motor cortex (MC)
  Group /general/extracellular_ephys/MC/device (Device) Neuroport Recording System with Utah array
  Group /general/extracellular_ephys/PPC (ElectrodeGroup) Utah array in posterior parietal cortex (PPC)
  Group /general/extracellular_ephys/PPC/device (Device) Neuroport Recording System with Utah array
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering, including the filter name and frequency cutoffs | shape = (191,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (191,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (191,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (191,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the electrode, in ohms | shape = (191,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (191,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the position (+x is posterior) | shape = (191,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the position (+y is inferior) | shape = (191,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the position (+z is right) | shape = (191,) | dtype = float64
  institution: California Institute of Technology
  lab: Andersen Lab
  session_id: 2019-02-12
  Group /general/subject (Subject) 
  identifier: sub-N1_ses-20190212T141736
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/Run (VectorData) run-block index (within session) | shape = (2,) | dtype = int64
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (2,) | dtype = int64
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (2,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (2,) | dtype = float64
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/Run (VectorData) no description | shape = (100,) | dtype = int64
  Dataset /intervals/trials/TrialNumber (VectorData) no description | shape = (100,) | dtype = uint64
  Dataset /intervals/trials/cue_off_time (VectorData) no description | shape = (100,) | dtype = float64
  Dataset /intervals/trials/cue_on_time (VectorData) no description | shape = (100,) | dtype = float64
  Dataset /intervals/trials/finger (VectorData) finger movement cued by text | shape = (100,) | dtype = object
  Dataset /intervals/trials/finger_type (VectorData) finger-type, ignoring left/right | shape = (100,) | dtype = object
  Dataset /intervals/trials/go_on_time (VectorData) no description | shape = (100,) | dtype = float64
  Dataset /intervals/trials/hand (VectorData) left or right hand for finger movement | shape = (100,) | dtype = object
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (100,) | dtype = int64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (100,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (100,) | dtype = float64
  session_description: ten-finger press task, with delay
  session_start_time: 2019-02-12T14:17:36-08:00
  timestamps_reference_time: 2019-02-12T14:17:36-08:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (298,) | dtype = object
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (298,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex) Index for VectorData 'electrodes' | shape = (298,) | dtype = uint16
  Dataset /units/id (ElementIdentifiers)  | shape = (298,) | dtype = int64
  Dataset /units/obs_intervals (VectorData) the observation intervals for each unit | shape = (596, 2) | dtype = float64
  Dataset /units/obs_intervals_index (VectorIndex) Index for VectorData 'obs_intervals' | shape = (298,) | dtype = uint16
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (1506328,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (298,) | dtype = uint32


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2023-04-08T14:43:22.513200-07:00']
  Group /general/devices/NSP1 (Device) Neuroport Recording System with Utah array
  experiment_description: Intracortical recordings during contralateral/ipsilateral finger movement
  experimenter: ['Tyson Aflalo']
  Group /general/extracellular_ephys/PPC (ElectrodeGroup) Utah array in posterior parietal cortex (PPC)
  Group /general/extracellular_ephys/PPC/device (Device) Neuroport Recording System with Utah array
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering, including the filter name and frequency cutoffs | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (96,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the electrode, in ohms | shape = (96,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the position (+x is posterior) | shape = (96,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the position (+y is inferior) | shape = (96,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the position (+z is right) | shape = (96,) | dtype = float64
  institution: California Institute of Technology
  lab: Andersen Lab
  session_id: 2015-08-12
  Group /general/subject (Subject) 
  identifier: sub-P1_ses-20150812T110754
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/Run (VectorData) run-block index (within session) | shape = (2,) | dtype = int64
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (2,) | dtype = int64
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (2,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (2,) | dtype = float64
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/Run (VectorData) no description | shape = (100,) | dtype = int64
  Dataset /intervals/trials/TrialNumber (VectorData) no description | shape = (100,) | dtype = uint64
  Dataset /intervals/trials/cue_off_time (VectorData) no description | shape = (100,) | dtype = float64
  Dataset /intervals/trials/cue_on_time (VectorData) no description | shape = (100,) | dtype = float64
  Dataset /intervals/trials/finger (VectorData) finger movement cued by text | shape = (100,) | dtype = object
  Dataset /intervals/trials/finger_type (VectorData) finger-type, ignoring left/right | shape = (100,) | dtype = object
  Dataset /intervals/trials/go_on_time (VectorData) no description | shape = (100,) | dtype = float64
  Dataset /intervals/trials/hand (VectorData) left or right hand for finger movement | shape = (100,) | dtype = object
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (100,) | dtype = int64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (100,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (100,) | dtype = float64
  session_description: ten-finger press task, with delay
  session_start_time: 2015-08-12T11:07:54-07:00
  timestamps_reference_time: 2015-08-12T11:07:54-07:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (112,) | dtype = object
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (112,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex) Index for VectorData 'electrodes' | shape = (112,) | dtype = uint8
  Dataset /units/id (ElementIdentifiers)  | shape = (112,) | dtype = int64
  Dataset /units/obs_intervals (VectorData) the observation intervals for each unit | shape = (224, 2) | dtype = float64
  Dataset /units/obs_intervals_index (VectorIndex) Index for VectorData 'obs_intervals' | shape = (112,) | dtype = uint8
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (199276,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (112,) | dtype = uint32
