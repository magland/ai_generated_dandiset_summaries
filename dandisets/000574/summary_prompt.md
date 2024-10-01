
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000574/0.231010.1809
name: Dataset of human medial temporal lobe neurons, scalp and intracranial EEG during a verbal working memory task
contributor: [{'name': 'Boran, Ece', 'roleName': [], 'schemaKey': 'Person', 'identifier': '0000-0002-0395-7575', 'affiliation': [{'name': 'Klinik für Neurochirurgie, UniversitätsSpital und Universität Zürich, 8091 Zürich, Switzerland', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/01462r250'}], 'includeInCitation': True}, {'name': 'Fedele, Tommaso', 'email': 'fedele.tm@gmail.com', 'roleName': [], 'schemaKey': 'Person', 'identifier': '0000-0001-7574-8062', 'affiliation': [{'name': 'Klinik für Neurochirurgie, UniversitätsSpital und Universität Zürich, 8091 Zürich, Switzerland.', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/01462r250'}, {'name': 'Zentrum für Neurowissenschaften Zürich, ETH Zürich, Zürich, Switzerland.', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/05a28rw58'}, {'name': 'Institute for Cognitive Neuroscience, National Research University Higher School of Economics, Russian Federation.', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/055f7t516'}], 'includeInCitation': True}, {'name': 'Hilfiker, Peter', 'roleName': [], 'schemaKey': 'Person', 'identifier': '0000-0001-7729-4754', 'affiliation': [], 'includeInCitation': True}, {'name': 'Stieglitz, Lennart', 'roleName': [], 'schemaKey': 'Person', 'identifier': '0000-0002-3744-5105', 'affiliation': [{'name': 'Klinik für Neurochirurgie, UniversitätsSpital und Universität Zürich, 8091 Zürich, Switzerland.', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/01462r250'}], 'includeInCitation': True}, {'name': 'Grunwald, Thomas', 'roleName': [], 'schemaKey': 'Person', 'affiliation': [{'name': 'Schweizerisches Epilepsie-Zentrum, 8008 Zürich, Switzerland.', 'schemaKey': 'Affiliation'}, {'name': 'Klinik für Neurologie, UniversitätsSpital Zürich, 8091 Zürich, Switzerland.', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/01462r250'}], 'includeInCitation': True}, {'url': 'https://www.hohenheim.ch', 'name': 'Hohenheim, Jan', 'email': 'jan@hohenheim.ch', 'roleName': ['dcite:ContactPerson', 'dcite:DataCurator'], 'schemaKey': 'Person', 'identifier': '0000-0001-9436-8348', 'affiliation': [{'name': 'Institute of Neuroinformatics, University of Zurich', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/02crff812'}, {'name': 'Institute of Neuroinformatics, ETH Zurich', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/05a28rw58'}], 'includeInCitation': True}, {'name': 'Sarnthein, Johannes', 'email': 'Johannes.Sarnthein@usz.ch', 'roleName': ['dcite:ContactPerson', 'dcite:Author', 'dcite:Conceptualization'], 'schemaKey': 'Person', 'identifier': '0000-0001-9141-381X', 'affiliation': [{'name': 'Klinik für Neurochirurgie, UniversitätsSpital und Universität Zürich, 8091 Zürich, Switzerland.', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/01462r250'}, {'name': 'Zentrum für Neurowissenschaften Zürich, ETH Zürich, Zürich, Switzerland.', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/05a28rw58'}], 'includeInCitation': True}, {'url': 'http://www.snf.ch/en', 'name': ' Swiss National Science Foundation', 'email': 'projects.ls@snf.ch', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/00yjd3n13', 'awardNumber': '204651', 'contactPoint': [], 'includeInCitation': False}, {'url': 'https://www.kavlifoundation.org/', 'name': ' The Kavli Foundation', 'email': 'communications@kavlifoundation.org', 'roleName': ['dcite:Sponsor'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/00kztt736', 'awardNumber': '2586', 'contactPoint': [], 'includeInCitation': False}]
description: We present an electrophysiological dataset recorded from nine subjects during a verbal working memory task. Subjects were epilepsy patients undergoing intracranial monitoring for localization of epileptic seizures. Subjects performed a modified Sternberg task in which the encoding of memory items, maintenance, and recall were temporally separated. The dataset includes simultaneously recorded scalp EEG with the 10-20 system, intracranial EEG (iEEG) recorded with depth electrodes, waveforms and spike times of 1526 units recorded in the medial temporal lobe, and the MNI coordinates and anatomical labels of all intracranial electrodes. Subject characteristics and information on sessions (set size, match/mismatch, correct/incorrect, response, response time for each trial) are also provided. This dataset enables the investigation of working memory by providing simultaneous scalp EEG and iEEG recordings, which can be used for connectivity analysis, alongside hard to obtain unit recordings from humans.
assetsSummary: {'species': [{'name': 'Homo sapiens - Human', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9606'}], 'approach': [{'name': 'behavioral approach', 'schemaKey': 'ApproachType'}, {'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 138887036866, 'numberOfFiles': 45, 'numberOfSubjects': 9, 'variableMeasured': ['Units', 'LFP', 'ElectrodeGroup', 'ElectricalSeries', 'ProcessingModule', 'BehavioralEvents'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'signal filtering technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000574 has 45 NWB files.
38 of these NWB files are of type 1.
7 of these NWB files are of type 2.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ecephys.eeg (ElectricalSeries) Scalp EEG data. Recorded at
  Dataset /acquisition/ecephys.eeg/electrodes (DynamicTableRegion) eeg electrodes | shape = (19,) | dtype = int32
  Group /acquisition/ecephys.ieeg (ElectricalSeries) iEEG data
  Dataset /acquisition/ecephys.ieeg/electrodes (DynamicTableRegion) ieeg electrodes | shape = (48,) | dtype = int32
  file_create_date: ['2023-10-09T22:09:55.869508+02:00']
  Group /general/devices/ATLAS Neurophysiology System (Device) iEEG recording system
  Group /general/devices/NicoletOne EEG System (Device) EEG recording system
  experiment_description: Task Name: Sternberg
  Task Description: The task is a modified Sternberg task in which the encoding of memory items, maintenance, and recall were temporally separated. Each trial starts with a fixation period ([-6, -5] s), followed by the stimulus ([-5, -3] s). The stimulus consists of a set of eight consonants at the center of the screen. The middle four, six, or eight letters are the memory items,which determine the set size for the trial (4, 6, or 8, respectively). The outer positions are filled with “X,” which is never a memory item. After the stimulus, the letters disappear from the screen, and the maintenance interval starts ([-3, 0] s).A fixation square is shown throughout fixation, encoding, and maintenance. After maintenance, a probe letter is presented. The subjects respond with a button press to indicate whether the probe was part of the stimulus.The subjects are instructed to respond as rapidly as possible without making errors. The hand used for the response is counterbalanced across subjects within the clinical constraints. After the response, the probe is turned off, and the subjects receive acoustic feedback regarding whether their response was correct or incorrect. Before initiating the next trial, the subjects were encouraged to blink and relax. The subjects perform 50 trials in one session, which last approximately 10 min. Trials with different set sizes are presented in a random order,with the single exception that a trial with an incorrect response is always followed by a trial with a set size of 4.
  Task URL: http://www.neurobs.com/ex_files/expt_view?id=266
  experimenter: ['Boran, Ece']
  Group /general/extracellular_ephys/eeg (ElectrodeGroup) EEG electrodes on scalp
  Group /general/extracellular_ephys/eeg/device (Device) EEG recording system
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering, including the filter name and frequency cutoffs | shape = (67,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (67,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (67,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (67,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/is_inside_soz (VectorData) Indicates whether the electrode is inside the seizure onset zone (SOZ) | shape = (67,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/label (VectorData) Channel label referenced by other data arrays | shape = (67,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (67,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/reference (VectorData) Description of the reference electrode and/or reference scheme used for this                         electrode, e.g.,"stainless steel skull screw" or "online common average referencing". | shape = (67,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the position (+x is posterior) | shape = (67,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the position (+y is inferior) | shape = (67,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the position (+z is right) | shape = (67,) | dtype = float64
  Group /general/extracellular_ephys/ieeg (ElectrodeGroup) iEEG electrodes
  Group /general/extracellular_ephys/ieeg/device (Device) iEEG recording system
  institution: Universitätsspital Zürich, 8091 Zurich, Switzerland
  keywords: ['Neuroscience' 'Electrophysiology' 'Human' 'Awake'
   'Local field potential' 'Neuronal action potential' 'Spikes'
   'Medial temporal lobe' 'Hippocampus' 'Entorhinal cortex' 'Amygdala'
   'Scalp EEG' 'Intracranial EEG' 'Cognitive task' 'Verbal working memory'
   'Epilepsy']
  lab: Schweizerische Epilepsie-Zentrum, 8008 Zurich, Switzerland
  related_publications: ['doi: 10.1126/sciadv.aav3687']
  Group /general/subject (Subject) 
  identifier: Human_MTL_units_scalp_EEG_and_iEEG_verbal_WM_subject01_session01
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (200,) | dtype = int32
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (200,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (200,) | dtype = float64
  Dataset /intervals/epochs/tags (VectorData) user-defined tags | shape = (200,) | dtype = object
  Dataset /intervals/epochs/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (200,) | dtype = uint8
  Dataset /intervals/epochs/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (800,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/epochs/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (200,) | dtype = uint16
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/artifact (VectorData) Whether the trial data was visually marked as an artifact by the experimenter | shape = (50,) | dtype = bool
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (50,) | dtype = int32
  Dataset /intervals/trials/probe_letter (VectorData) The letter presented to the participant during the retrieval period | shape = (50,) | dtype = object
  Dataset /intervals/trials/set_letters (VectorData) Letters shown during encoding period. Note that this information is currently not part of the dataset, so all entries are "not available" | shape = (50,) | dtype = object
  Dataset /intervals/trials/set_size (VectorData) Number of letters shown during encoding period (4, 6, or 8 letters) | shape = (50,) | dtype = int32
  Dataset /intervals/trials/solution (VectorData) The solution to the question "Was the letter at hand present in the encoding set?" | shape = (50,) | dtype = bool
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (50,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (50,) | dtype = float64
  Dataset /intervals/trials/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (200,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/trials/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (50,) | dtype = uint8
  Group /processing/behavior (ProcessingModule) Data for all trials in this session.
  Group /processing/behavior/BehavioralEvents.response (BehavioralEvents) 
  Group /processing/behavior/BehavioralEvents.response/response (TimeSeries) The participant's answer to the question "Was the letter at hand present in the encoding set?"
  Group /processing/ecephys (ProcessingModule) processed extracellular electrophysiology data
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/ecephys.lfp (ElectricalSeries) LFP data
  Dataset /processing/ecephys/LFP/ecephys.lfp/electrodes (DynamicTableRegion) ieeg electrodes | shape = (32,) | dtype = int32
  session_description: Running experiment as described in the the experiment description
  session_start_time: 2016-12-14T17:13:00+01:00
  timestamps_reference_time: 2016-12-14T17:13:00+01:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (37,) | dtype = object
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (37,) | dtype = int32
  Dataset /units/electrodes_index (VectorIndex) Index for VectorData 'electrodes' | shape = (37,) | dtype = uint8
  Dataset /units/id (ElementIdentifiers)  | shape = (37,) | dtype = int32
  Dataset /units/obs_intervals (VectorData) the observation intervals for each unit | shape = (1850, 2) | dtype = float64
  Dataset /units/obs_intervals_index (VectorIndex) Index for VectorData 'obs_intervals' | shape = (37,) | dtype = uint16
  Dataset /units/offset (VectorData) The offset in seconds of the first waveform voltage relative to the spike event | shape = (37,) | dtype = float64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (42527,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (37,) | dtype = uint16
  Dataset /units/waveform_mean (VectorData) the spike waveform mean for each spike unit | shape = (37, 64) | dtype = float64
  Dataset /units/waveform_sd (VectorData) the spike waveform standard deviation for each spike unit | shape = (37, 64) | dtype = float64


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ecephys.eeg (ElectricalSeries) Scalp EEG data. Recorded at
  Dataset /acquisition/ecephys.eeg/electrodes (DynamicTableRegion) eeg electrodes | shape = (19,) | dtype = int32
  Group /acquisition/ecephys.ieeg (ElectricalSeries) iEEG data
  Dataset /acquisition/ecephys.ieeg/electrodes (DynamicTableRegion) ieeg electrodes | shape = (48,) | dtype = int32
  file_create_date: ['2023-10-09T22:16:00.249690+02:00']
  Group /general/devices/ATLAS Neurophysiology System (Device) iEEG recording system
  Group /general/devices/NicoletOne EEG System (Device) EEG recording system
  experiment_description: Task Name: Sternberg
  Task Description: The task is a modified Sternberg task in which the encoding of memory items, maintenance, and recall were temporally separated. Each trial starts with a fixation period ([-6, -5] s), followed by the stimulus ([-5, -3] s). The stimulus consists of a set of eight consonants at the center of the screen. The middle four, six, or eight letters are the memory items,which determine the set size for the trial (4, 6, or 8, respectively). The outer positions are filled with “X,” which is never a memory item. After the stimulus, the letters disappear from the screen, and the maintenance interval starts ([-3, 0] s).A fixation square is shown throughout fixation, encoding, and maintenance. After maintenance, a probe letter is presented. The subjects respond with a button press to indicate whether the probe was part of the stimulus.The subjects are instructed to respond as rapidly as possible without making errors. The hand used for the response is counterbalanced across subjects within the clinical constraints. After the response, the probe is turned off, and the subjects receive acoustic feedback regarding whether their response was correct or incorrect. Before initiating the next trial, the subjects were encouraged to blink and relax. The subjects perform 50 trials in one session, which last approximately 10 min. Trials with different set sizes are presented in a random order,with the single exception that a trial with an incorrect response is always followed by a trial with a set size of 4.
  Task URL: http://www.neurobs.com/ex_files/expt_view?id=266
  experimenter: ['Boran, Ece']
  Group /general/extracellular_ephys/eeg (ElectrodeGroup) EEG electrodes on scalp
  Group /general/extracellular_ephys/eeg/device (Device) EEG recording system
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering, including the filter name and frequency cutoffs | shape = (67,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (67,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (67,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (67,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/is_inside_soz (VectorData) Indicates whether the electrode is inside the seizure onset zone (SOZ) | shape = (67,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/label (VectorData) Channel label referenced by other data arrays | shape = (67,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (67,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/reference (VectorData) Description of the reference electrode and/or reference scheme used for this                         electrode, e.g.,"stainless steel skull screw" or "online common average referencing". | shape = (67,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the position (+x is posterior) | shape = (67,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the position (+y is inferior) | shape = (67,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the position (+z is right) | shape = (67,) | dtype = float64
  Group /general/extracellular_ephys/ieeg (ElectrodeGroup) iEEG electrodes
  Group /general/extracellular_ephys/ieeg/device (Device) iEEG recording system
  institution: Universitätsspital Zürich, 8091 Zurich, Switzerland
  keywords: ['Neuroscience' 'Electrophysiology' 'Human' 'Awake'
   'Local field potential' 'Neuronal action potential' 'Spikes'
   'Medial temporal lobe' 'Hippocampus' 'Entorhinal cortex' 'Amygdala'
   'Scalp EEG' 'Intracranial EEG' 'Cognitive task' 'Verbal working memory'
   'Epilepsy']
  lab: Schweizerische Epilepsie-Zentrum, 8008 Zurich, Switzerland
  related_publications: ['doi: 10.1126/sciadv.aav3687']
  Group /general/subject (Subject) 
  identifier: Human_MTL_units_scalp_EEG_and_iEEG_verbal_WM_subject01_session03
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/artifact (VectorData) Whether the trial data was visually marked as an artifact by the experimenter | shape = (50,) | dtype = bool
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (50,) | dtype = int32
  Dataset /intervals/trials/probe_letter (VectorData) The letter presented to the participant during the retrieval period | shape = (50,) | dtype = object
  Dataset /intervals/trials/set_letters (VectorData) Letters shown during encoding period. Note that this information is currently not part of the dataset, so all entries are "not available" | shape = (50,) | dtype = object
  Dataset /intervals/trials/set_size (VectorData) Number of letters shown during encoding period (4, 6, or 8 letters) | shape = (50,) | dtype = int32
  Dataset /intervals/trials/solution (VectorData) The solution to the question "Was the letter at hand present in the encoding set?" | shape = (50,) | dtype = bool
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (50,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (50,) | dtype = float64
  Dataset /intervals/trials/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (200,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/trials/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (50,) | dtype = uint8
  Group /processing/behavior (ProcessingModule) Data for all trials in this session.
  Group /processing/behavior/BehavioralEvents.response (BehavioralEvents) 
  Group /processing/behavior/BehavioralEvents.response/response (TimeSeries) The participant's answer to the question "Was the letter at hand present in the encoding set?"
  Group /processing/ecephys (ProcessingModule) processed extracellular electrophysiology data
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/ecephys.lfp (ElectricalSeries) LFP data
  Dataset /processing/ecephys/LFP/ecephys.lfp/electrodes (DynamicTableRegion) ieeg electrodes | shape = (32,) | dtype = int32
  session_description: Running experiment as described in the the experiment description
  session_start_time: 2016-12-17T12:14:00+01:00
  timestamps_reference_time: 2016-12-17T12:14:00+01:00
