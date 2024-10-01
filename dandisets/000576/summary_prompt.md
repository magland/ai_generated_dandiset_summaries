
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000576/0.231010.1811
name: Dataset of neurons and intracranial EEG from human amygdala during aversive dynamic visual stimulation
contributor: [{'name': 'Fedele, Tommaso', 'email': 'fedele.tm@gmail.com', 'roleName': ['dcite:Author', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0001-7574-8062', 'affiliation': [{'name': 'National Research University Higher School of Economics, Moscow, Russian Federation', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/055f7t516'}], 'includeInCitation': True}, {'name': 'Hilfiker, Peter ', 'roleName': [], 'schemaKey': 'Person', 'identifier': '0000-0001-7729-4754', 'affiliation': [], 'includeInCitation': True}, {'name': 'Grunwald, Thomas ', 'roleName': [], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Stieglitz, Lennart ', 'roleName': [], 'schemaKey': 'Person', 'identifier': '0000-0002-3744-5105', 'affiliation': [{'name': 'Klinik für Neurochirurgie, UniversitätsSpital Zürich und Universität Zürich, Zurich, Switzerland', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/01462r250'}], 'includeInCitation': True}, {'name': 'Jokeit, Hennric', 'roleName': [], 'schemaKey': 'Person', 'identifier': '0000-0001-6969-9639', 'affiliation': [{'name': 'Zentrum für Neurowissenschaften Zürich, Switzerland', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/01462r250'}], 'includeInCitation': True}, {'url': 'https://www.hohenheim.ch', 'name': 'Hohenheim, Jan', 'email': 'jan@hohenheim.ch', 'roleName': ['dcite:ContactPerson', 'dcite:DataManager'], 'schemaKey': 'Person', 'identifier': '0000-0001-9436-8348', 'affiliation': [{'name': 'Institute of Neuroinformatics, University of Zurich & ETH Zurich', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/02crff812'}, {'name': 'Institute of Neuroinformatics, University of Zurich & ETH Zurich', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/05a28rw58'}], 'includeInCitation': True}, {'name': 'Sarnthein, Johannes ', 'email': 'johannes.sarnthein@usz.ch', 'roleName': ['dcite:Author', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0001-9141-381X', 'affiliation': [{'name': 'Klinik für Neurochirurgie, UniversitätsSpital Zürich und Universität Zürich, Zurich, Switzerland', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/01462r250'}, {'name': 'Zentrum für Neurowissenschaften Zürich, Switzerland', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/01462r250'}], 'includeInCitation': True}, {'url': 'http://www.snf.ch/en', 'name': ' Swiss National Science Foundation', 'email': 'projects.ls@snf.ch', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/00yjd3n13', 'awardNumber': '204651', 'contactPoint': [], 'includeInCitation': False}, {'url': 'https://www.kavlifoundation.org/', 'name': ' The Kavli Foundation', 'email': 'communications@kavlifoundation.org', 'roleName': ['dcite:Sponsor'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/00kztt736', 'awardNumber': '2586', 'contactPoint': [], 'includeInCitation': False}]
description: We present an electrophysiological dataset collected from the amygdalae of nine subjects attending a visual dynamic stimulation of emotional aversive content. The subjects were patients affected by epilepsy who underwent preoperative invasive monitoring in the mesial temporal lobe. Subjects were presented with dynamic visual sequences of fearful faces (aversive condition), interleaved with sequences of neutral landscapes (neutral condition).

We provide simultaneous recordings of intracranial EEG (iEEG) and neuronal spike times and waveforms, and metadata related to the task, subjects, sessions and electrodes in the NIX standard. We technically validated this dataset and provide here the spike sorting quality metrics and the spectra of iEEG signals.
This dataset allows the investigation of amygdalar response to dynamic aversive stimuli at multiple spatial scales, from the macroscopic EEG to the neuronal firing in the human brain.
assetsSummary: {'species': [{'name': 'Homo sapiens - Human', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9606'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 2191651090, 'numberOfFiles': 27, 'numberOfSubjects': 9, 'variableMeasured': ['ProcessingModule', 'LFP', 'Units', 'ElectricalSeries', 'ElectrodeGroup'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'signal filtering technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000576 has 17 NWB files.
5 of these NWB files are of type 1.
5 of these NWB files are of type 2.
3 of these NWB files are of type 3.
3 of these NWB files are of type 4.
1 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ImageSeries (ImageSeries) Videos of aversive and neutral stimuli.
  Group /acquisition/ecephys.ieeg (ElectricalSeries) iEEG data
  Dataset /acquisition/ecephys.ieeg/electrodes (DynamicTableRegion) ieeg electrodes | shape = (2,) | dtype = int32
  file_create_date: ['2023-10-09T22:11:25.174495+02:00']
  Group /general/devices/ATLAS Neurophysiology System (Device) iEEG recording system
  experiment_description: Task Name: Jokeit
  Task Description: We used a paradigm comprising of a series of dynamic videos, which has been already validated in previous clinical investigations (Schacher et al., 2006). The videos were all silent and consisted of dynamic fearful faces and dynamic neutral landscapes, presented in an alternating order, in a block design. The paradigm included eight blocks of 75 short video clips (2–3 s) of fearful faces (aversive condition) and nine blocks of 72 short video clips (2–3 s) of neutral landscapes (neutral condition). Each block lasted 24 s in total, and contained short video clips without any intermission between consecutive videos. Video clips of fearful faces were extracted from thriller and horror movies and contained faces of actors showing fear, without being violent or aggressive. Video clips of neutral landscapes were chosen as a control condition, and were matched to the duration of the fearful faces videos (2–3 s). They included domestic landscapes which are posited to have a low emotional content and visual properties comparable to the emotional videos (Schacher et al., 2006). All videos were only included once. A panel of psychologists had evaluated the stimuli to ensure that they are suitable for the patients and that they do not include any episodes of violence or aggression (Schacher et al., 2006). In particular, we started with a set of 120 videos of fearful faces and reduced that to 72, by excluding videos where: (a) the actor’s face was not continuously visible (b) fear was not clearly recognized on the actor’s face (c) no other emotion was displayed (e.g. anger/surprise) and (d) the display of fear was intense. During electrophysiological recordings the videos were presented to the patients via a laptop screen, while during the fMRI scan they were presented through a tilted overhead mirror. In both cases, patients were instructed to pay attention to the videos and focus on the eyes of the actors during the clips containing faces. For the electrophysiological recordings, blocks were separated by a repeated baseline of 2 s taken from a neutral condition.
  Task URL: http://www.neurobs.com/ex_files/expt_view?id=283
  experimenter: ['Fedele, Tommaso']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering, including the filter name and frequency cutoffs | shape = (2,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (2,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (2,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (2,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/is_inside_soz (VectorData) Indicates whether the electrode is inside the seizure onset zone (SOZ) | shape = (2,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/label (VectorData) Channel label referenced by other data arrays | shape = (2,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (2,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/reference (VectorData) Description of the reference electrode and/or reference scheme used for this                         electrode, e.g.,"stainless steel skull screw" or "online common average referencing". | shape = (2,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the position (+x is posterior) | shape = (2,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the position (+y is inferior) | shape = (2,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the position (+z is right) | shape = (2,) | dtype = float64
  Group /general/extracellular_ephys/ieeg (ElectrodeGroup) iEEG electrodes
  Group /general/extracellular_ephys/ieeg/device (Device) iEEG recording system
  institution: Universitätsspital Zürich, 8091 Zurich, Switzerland
  keywords: ['Neuroscience' 'Electrophysiology' 'Human' 'Awake'
   'Local field potential' 'Neuronal action potential' 'Spikes' 'Amygdala'
   'Intracranial EEG' 'Cognitive task' 'Dynamic visual stimuli'
   'Aversive stimuli' 'Epilepsy']
  lab: Schweizerische Epilepsie-Zentrum, 8008 Zurich, Switzerland
  related_publications: ['doi: 10.1016/j.neuroimage.2020.116705']
  Group /general/subject (Subject) 
  identifier: Human_Amygdala_MUA_sEEG_FearVideo_subject01_session01
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/condition (VectorData) Kind of videos presented in trial block. Either "Aversive", i.e. fearful faces, or "Neutral", i.e. neutral landscapes | shape = (17,) | dtype = object
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (17,) | dtype = int32
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (17,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (17,) | dtype = float64
  Dataset /intervals/trials/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (17,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/trials/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (17,) | dtype = uint8
  session_description: Running experiment as described in the the experiment description
  session_start_time: 2014-08-28T13:27:00+02:00
  timestamps_reference_time: 2014-08-28T13:27:00+02:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (4,) | dtype = object
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (4,) | dtype = int32
  Dataset /units/electrodes_index (VectorIndex) Index for VectorData 'electrodes' | shape = (4,) | dtype = uint8
  Dataset /units/id (ElementIdentifiers)  | shape = (4,) | dtype = int32
  Dataset /units/obs_intervals (VectorData) the observation intervals for each unit | shape = (68, 2) | dtype = float64
  Dataset /units/obs_intervals_index (VectorIndex) Index for VectorData 'obs_intervals' | shape = (4,) | dtype = uint8
  Dataset /units/offset (VectorData) The offset in seconds of the first waveform voltage relative to the spike event | shape = (4,) | dtype = float64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (2792,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (4,) | dtype = uint16
  Dataset /units/waveform_mean (VectorData) the spike waveform mean for each spike unit | shape = (4, 64) | dtype = float64
  Dataset /units/waveform_sd (VectorData) the spike waveform standard deviation for each spike unit | shape = (4, 64) | dtype = float64


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2023-07-07T14:21:15.004902+02:00']
  Group /general/devices/ATLAS Neurophysiology System (Device) iEEG recording system
  experiment_description: Task Name: Jokeit
  Task Description: We used a paradigm comprising of a series of dynamic videos, which has been already validated in previous clinical investigations (Schacher et al., 2006). The videos were all silent and consisted of dynamic fearful faces and dynamic neutral landscapes, presented in an alternating order, in a block design. The paradigm included eight blocks of 75 short video clips (2–3 s) of fearful faces (aversive condition) and nine blocks of 72 short video clips (2–3 s) of neutral landscapes (neutral condition). Each block lasted 24 s in total, and contained short video clips without any intermission between consecutive videos. Video clips of fearful faces were extracted from thriller and horror movies and contained faces of actors showing fear, without being violent or aggressive. Video clips of neutral landscapes were chosen as a control condition, and were matched to the duration of the fearful faces videos (2–3 s). They included domestic landscapes which are posited to have a low emotional content and visual properties comparable to the emotional videos (Schacher et al., 2006). All videos were only included once. A panel of psychologists had evaluated the stimuli to ensure that they are suitable for the patients and that they do not include any episodes of violence or aggression (Schacher et al., 2006). In particular, we started with a set of 120 videos of fearful faces and reduced that to 72, by excluding videos where: (a) the actor’s face was not continuously visible (b) fear was not clearly recognized on the actor’s face (c) no other emotion was displayed (e.g. anger/surprise) and (d) the display of fear was intense. During electrophysiological recordings the videos were presented to the patients via a laptop screen, while during the fMRI scan they were presented through a tilted overhead mirror. In both cases, patients were instructed to pay attention to the videos and focus on the eyes of the actors during the clips containing faces. For the electrophysiological recordings, blocks were separated by a repeated baseline of 2 s taken from a neutral condition.
  Task URL: http://www.neurobs.com/ex_files/expt_view?id=283
  experimenter: ['Fedele, Tommaso']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering, including the filter name and frequency cutoffs | shape = (2,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (2,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (2,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (2,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/is_inside_soz (VectorData) Indicates whether the electrode is inside the seizure onset zone (SOZ) | shape = (2,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/label (VectorData) Channel label referenced by other data arrays | shape = (2,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (2,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/reference (VectorData) Description of the reference electrode and/or reference scheme used for this                         electrode, e.g.,"stainless steel skull screw" or "online common average referencing". | shape = (2,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the position (+x is posterior) | shape = (2,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the position (+y is inferior) | shape = (2,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the position (+z is right) | shape = (2,) | dtype = float64
  Group /general/extracellular_ephys/ieeg (ElectrodeGroup) iEEG electrodes
  Group /general/extracellular_ephys/ieeg/device (Device) iEEG recording system
  institution: Universitätsspital Zürich, 8091 Zurich, Switzerland
  keywords: ['Neuroscience' 'Electrophysiology' 'Human' 'Awake'
   'Local field potential' 'Neuronal action potential' 'Spikes' 'Amygdala'
   'Intracranial EEG' 'Cognitive task' 'Dynamic visual stimuli'
   'Aversive stimuli' 'Epilepsy']
  lab: Schweizerische Epilepsie-Zentrum, 8008 Zurich, Switzerland
  related_publications: ['doi: 10.1016/j.neuroimage.2020.116705']
  Group /general/subject (Subject) 
  identifier: Human_Amygdala_MUA_sEEG_FearVideo_subject01_session01
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/condition (VectorData) Kind of videos presented in trial block. Either "Aversive", i.e. fearful faces, or "Neutral", i.e. neutral landscapes | shape = (17,) | dtype = object
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (17,) | dtype = int32
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (17,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (17,) | dtype = float64
  Dataset /intervals/trials/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (17,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/trials/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (17,) | dtype = uint8
  Group /processing/ecephys (ProcessingModule) processed extracellular electrophysiology data
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/ecephys.ieeg (ElectricalSeries) iEEG data
  Dataset /processing/ecephys/LFP/ecephys.ieeg/electrodes (DynamicTableRegion) ieeg electrodes | shape = (2,) | dtype = int32
  session_description: Running experiment as described in the the experiment description
  session_start_time: 2014-08-28T13:27:00+02:00
  timestamps_reference_time: 2014-08-28T13:27:00+02:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/electrode_group (VectorData) the electrode group that each spike unit came from | shape = (4,) | dtype = object
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (4,) | dtype = int32
  Dataset /units/electrodes_index (VectorIndex) Index for VectorData 'electrodes' | shape = (4,) | dtype = uint8
  Dataset /units/id (ElementIdentifiers)  | shape = (4,) | dtype = int32
  Dataset /units/obs_intervals (VectorData) the observation intervals for each unit | shape = (68, 2) | dtype = float64
  Dataset /units/obs_intervals_index (VectorIndex) Index for VectorData 'obs_intervals' | shape = (4,) | dtype = uint8
  Dataset /units/offset (VectorData) The offset in seconds of the first waveform voltage relative to the spike event | shape = (4,) | dtype = float64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (2792,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (4,) | dtype = uint16
  Dataset /units/waveform_mean (VectorData) the spike waveform mean for each spike unit | shape = (4, 64) | dtype = float64
  Dataset /units/waveform_sd (VectorData) the spike waveform standard deviation for each spike unit | shape = (4, 64) | dtype = float64


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ImageSeries (ImageSeries) Videos of aversive and neutral stimuli.
  Group /acquisition/ecephys.ieeg (ElectricalSeries) iEEG data
  Dataset /acquisition/ecephys.ieeg/electrodes (DynamicTableRegion) ieeg electrodes | shape = (1,) | dtype = int32
  file_create_date: ['2023-10-09T22:11:34.804220+02:00']
  Group /general/devices/ATLAS Neurophysiology System (Device) iEEG recording system
  experiment_description: Task Name: Jokeit
  Task Description: We used a paradigm comprising of a series of dynamic videos, which has been already validated in previous clinical investigations (Schacher et al., 2006). The videos were all silent and consisted of dynamic fearful faces and dynamic neutral landscapes, presented in an alternating order, in a block design. The paradigm included eight blocks of 75 short video clips (2–3 s) of fearful faces (aversive condition) and nine blocks of 72 short video clips (2–3 s) of neutral landscapes (neutral condition). Each block lasted 24 s in total, and contained short video clips without any intermission between consecutive videos. Video clips of fearful faces were extracted from thriller and horror movies and contained faces of actors showing fear, without being violent or aggressive. Video clips of neutral landscapes were chosen as a control condition, and were matched to the duration of the fearful faces videos (2–3 s). They included domestic landscapes which are posited to have a low emotional content and visual properties comparable to the emotional videos (Schacher et al., 2006). All videos were only included once. A panel of psychologists had evaluated the stimuli to ensure that they are suitable for the patients and that they do not include any episodes of violence or aggression (Schacher et al., 2006). In particular, we started with a set of 120 videos of fearful faces and reduced that to 72, by excluding videos where: (a) the actor’s face was not continuously visible (b) fear was not clearly recognized on the actor’s face (c) no other emotion was displayed (e.g. anger/surprise) and (d) the display of fear was intense. During electrophysiological recordings the videos were presented to the patients via a laptop screen, while during the fMRI scan they were presented through a tilted overhead mirror. In both cases, patients were instructed to pay attention to the videos and focus on the eyes of the actors during the clips containing faces. For the electrophysiological recordings, blocks were separated by a repeated baseline of 2 s taken from a neutral condition.
  Task URL: http://www.neurobs.com/ex_files/expt_view?id=283
  experimenter: ['Fedele, Tommaso']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering, including the filter name and frequency cutoffs | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/is_inside_soz (VectorData) Indicates whether the electrode is inside the seizure onset zone (SOZ) | shape = (1,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/label (VectorData) Channel label referenced by other data arrays | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/reference (VectorData) Description of the reference electrode and/or reference scheme used for this                         electrode, e.g.,"stainless steel skull screw" or "online common average referencing". | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the position (+x is posterior) | shape = (1,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the position (+y is inferior) | shape = (1,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the position (+z is right) | shape = (1,) | dtype = float64
  Group /general/extracellular_ephys/ieeg (ElectrodeGroup) iEEG electrodes
  Group /general/extracellular_ephys/ieeg/device (Device) iEEG recording system
  institution: Universitätsspital Zürich, 8091 Zurich, Switzerland
  keywords: ['Neuroscience' 'Electrophysiology' 'Human' 'Awake'
   'Local field potential' 'Neuronal action potential' 'Spikes' 'Amygdala'
   'Intracranial EEG' 'Cognitive task' 'Dynamic visual stimuli'
   'Aversive stimuli' 'Epilepsy']
  lab: Schweizerische Epilepsie-Zentrum, 8008 Zurich, Switzerland
  related_publications: ['doi: 10.1016/j.neuroimage.2020.116705']
  Group /general/subject (Subject) 
  identifier: Human_Amygdala_MUA_sEEG_FearVideo_subject05_session01
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/condition (VectorData) Kind of videos presented in trial block. Either "Aversive", i.e. fearful faces, or "Neutral", i.e. neutral landscapes | shape = (17,) | dtype = object
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (17,) | dtype = int32
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (17,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (17,) | dtype = float64
  Dataset /intervals/trials/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (17,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/trials/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (17,) | dtype = uint8
  session_description: Running experiment as described in the the experiment description
  session_start_time: 2012-12-07T17:35:00+01:00
  timestamps_reference_time: 2012-12-07T17:35:00+01:00


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2023-07-07T14:21:26.300745+02:00']
  Group /general/devices/ATLAS Neurophysiology System (Device) iEEG recording system
  experiment_description: Task Name: Jokeit
  Task Description: We used a paradigm comprising of a series of dynamic videos, which has been already validated in previous clinical investigations (Schacher et al., 2006). The videos were all silent and consisted of dynamic fearful faces and dynamic neutral landscapes, presented in an alternating order, in a block design. The paradigm included eight blocks of 75 short video clips (2–3 s) of fearful faces (aversive condition) and nine blocks of 72 short video clips (2–3 s) of neutral landscapes (neutral condition). Each block lasted 24 s in total, and contained short video clips without any intermission between consecutive videos. Video clips of fearful faces were extracted from thriller and horror movies and contained faces of actors showing fear, without being violent or aggressive. Video clips of neutral landscapes were chosen as a control condition, and were matched to the duration of the fearful faces videos (2–3 s). They included domestic landscapes which are posited to have a low emotional content and visual properties comparable to the emotional videos (Schacher et al., 2006). All videos were only included once. A panel of psychologists had evaluated the stimuli to ensure that they are suitable for the patients and that they do not include any episodes of violence or aggression (Schacher et al., 2006). In particular, we started with a set of 120 videos of fearful faces and reduced that to 72, by excluding videos where: (a) the actor’s face was not continuously visible (b) fear was not clearly recognized on the actor’s face (c) no other emotion was displayed (e.g. anger/surprise) and (d) the display of fear was intense. During electrophysiological recordings the videos were presented to the patients via a laptop screen, while during the fMRI scan they were presented through a tilted overhead mirror. In both cases, patients were instructed to pay attention to the videos and focus on the eyes of the actors during the clips containing faces. For the electrophysiological recordings, blocks were separated by a repeated baseline of 2 s taken from a neutral condition.
  Task URL: http://www.neurobs.com/ex_files/expt_view?id=283
  experimenter: ['Fedele, Tommaso']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering, including the filter name and frequency cutoffs | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/is_inside_soz (VectorData) Indicates whether the electrode is inside the seizure onset zone (SOZ) | shape = (1,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/label (VectorData) Channel label referenced by other data arrays | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/reference (VectorData) Description of the reference electrode and/or reference scheme used for this                         electrode, e.g.,"stainless steel skull screw" or "online common average referencing". | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the position (+x is posterior) | shape = (1,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the position (+y is inferior) | shape = (1,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the position (+z is right) | shape = (1,) | dtype = float64
  Group /general/extracellular_ephys/ieeg (ElectrodeGroup) iEEG electrodes
  Group /general/extracellular_ephys/ieeg/device (Device) iEEG recording system
  institution: Universitätsspital Zürich, 8091 Zurich, Switzerland
  keywords: ['Neuroscience' 'Electrophysiology' 'Human' 'Awake'
   'Local field potential' 'Neuronal action potential' 'Spikes' 'Amygdala'
   'Intracranial EEG' 'Cognitive task' 'Dynamic visual stimuli'
   'Aversive stimuli' 'Epilepsy']
  lab: Schweizerische Epilepsie-Zentrum, 8008 Zurich, Switzerland
  related_publications: ['doi: 10.1016/j.neuroimage.2020.116705']
  Group /general/subject (Subject) 
  identifier: Human_Amygdala_MUA_sEEG_FearVideo_subject05_session01
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/condition (VectorData) Kind of videos presented in trial block. Either "Aversive", i.e. fearful faces, or "Neutral", i.e. neutral landscapes | shape = (17,) | dtype = object
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (17,) | dtype = int32
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (17,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (17,) | dtype = float64
  Dataset /intervals/trials/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (17,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/trials/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (17,) | dtype = uint8
  Group /processing/ecephys (ProcessingModule) processed extracellular electrophysiology data
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/ecephys.ieeg (ElectricalSeries) iEEG data
  Dataset /processing/ecephys/LFP/ecephys.ieeg/electrodes (DynamicTableRegion) ieeg electrodes | shape = (1,) | dtype = int32
  session_description: Running experiment as described in the the experiment description
  session_start_time: 2012-12-07T17:35:00+01:00
  timestamps_reference_time: 2012-12-07T17:35:00+01:00


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ImageSeries (ImageSeries) Videos of aversive and neutral stimuli.
  Group /acquisition/ecephys.ieeg (ElectricalSeries) iEEG data
  Dataset /acquisition/ecephys.ieeg/electrodes (DynamicTableRegion) ieeg electrodes | shape = (2,) | dtype = int32
  file_create_date: ['2023-10-09T22:11:36.172331+02:00']
  Group /general/devices/ATLAS Neurophysiology System (Device) iEEG recording system
  experiment_description: Task Name: Jokeit
  Task Description: We used a paradigm comprising of a series of dynamic videos, which has been already validated in previous clinical investigations (Schacher et al., 2006). The videos were all silent and consisted of dynamic fearful faces and dynamic neutral landscapes, presented in an alternating order, in a block design. The paradigm included eight blocks of 75 short video clips (2–3 s) of fearful faces (aversive condition) and nine blocks of 72 short video clips (2–3 s) of neutral landscapes (neutral condition). Each block lasted 24 s in total, and contained short video clips without any intermission between consecutive videos. Video clips of fearful faces were extracted from thriller and horror movies and contained faces of actors showing fear, without being violent or aggressive. Video clips of neutral landscapes were chosen as a control condition, and were matched to the duration of the fearful faces videos (2–3 s). They included domestic landscapes which are posited to have a low emotional content and visual properties comparable to the emotional videos (Schacher et al., 2006). All videos were only included once. A panel of psychologists had evaluated the stimuli to ensure that they are suitable for the patients and that they do not include any episodes of violence or aggression (Schacher et al., 2006). In particular, we started with a set of 120 videos of fearful faces and reduced that to 72, by excluding videos where: (a) the actor’s face was not continuously visible (b) fear was not clearly recognized on the actor’s face (c) no other emotion was displayed (e.g. anger/surprise) and (d) the display of fear was intense. During electrophysiological recordings the videos were presented to the patients via a laptop screen, while during the fMRI scan they were presented through a tilted overhead mirror. In both cases, patients were instructed to pay attention to the videos and focus on the eyes of the actors during the clips containing faces. For the electrophysiological recordings, blocks were separated by a repeated baseline of 2 s taken from a neutral condition.
  Task URL: http://www.neurobs.com/ex_files/expt_view?id=283
  experimenter: ['Fedele, Tommaso']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering, including the filter name and frequency cutoffs | shape = (2,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (2,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (2,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (2,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/is_inside_soz (VectorData) Indicates whether the electrode is inside the seizure onset zone (SOZ) | shape = (2,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/label (VectorData) Channel label referenced by other data arrays | shape = (2,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (2,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/reference (VectorData) Description of the reference electrode and/or reference scheme used for this                         electrode, e.g.,"stainless steel skull screw" or "online common average referencing". | shape = (2,) | dtype = object
  Group /general/extracellular_ephys/ieeg (ElectrodeGroup) iEEG electrodes
  Group /general/extracellular_ephys/ieeg/device (Device) iEEG recording system
  institution: Universitätsspital Zürich, 8091 Zurich, Switzerland
  keywords: ['Neuroscience' 'Electrophysiology' 'Human' 'Awake'
   'Local field potential' 'Neuronal action potential' 'Spikes' 'Amygdala'
   'Intracranial EEG' 'Cognitive task' 'Dynamic visual stimuli'
   'Aversive stimuli' 'Epilepsy']
  lab: Schweizerische Epilepsie-Zentrum, 8008 Zurich, Switzerland
  related_publications: ['doi: 10.1016/j.neuroimage.2020.116705']
  Group /general/subject (Subject) 
  identifier: Human_Amygdala_MUA_sEEG_FearVideo_subject06_session01
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/condition (VectorData) Kind of videos presented in trial block. Either "Aversive", i.e. fearful faces, or "Neutral", i.e. neutral landscapes | shape = (17,) | dtype = object
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (17,) | dtype = int32
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (17,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (17,) | dtype = float64
  Dataset /intervals/trials/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (17,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/trials/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (17,) | dtype = uint8
  session_description: Running experiment as described in the the experiment description
  session_start_time: 2013-12-09T11:36:00+01:00
  timestamps_reference_time: 2013-12-09T11:36:00+01:00
