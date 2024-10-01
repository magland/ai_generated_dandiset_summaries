
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000469/0.240123.1806
name: Dataset of human-single neuron activity during a Sternberg working memory task.
contributor: [{'name': 'Kyzar, Michael', 'email': 'kyzarnexus@gmail.com', 'roleName': ['dcite:ContactPerson', 'dcite:Author', 'dcite:DataCurator', 'dcite:DataManager', 'dcite:FormalAnalysis', 'dcite:Investigation', 'dcite:Maintainer', 'dcite:Methodology', 'dcite:ProjectLeader', 'dcite:ProjectManager', 'dcite:ProjectMember', 'dcite:Researcher', 'dcite:Software', 'dcite:Validation', 'dcite:Visualization'], 'schemaKey': 'Person', 'identifier': '0009-0004-4392-9933', 'affiliation': [{'name': 'Department of Neurosurgery, Cedars-Sinai Medical Center, Los Angeles, CA, USA', 'schemaKey': 'Affiliation'}], 'includeInCitation': True}, {'name': 'Kaminski, Jan', 'roleName': [], 'schemaKey': 'Person', 'identifier': '0000-0002-8663-7314', 'affiliation': [], 'includeInCitation': True}, {'name': 'Brzezicka, Aneta', 'roleName': ['dcite:Author', 'dcite:DataCollector'], 'schemaKey': 'Person', 'identifier': '0000-0003-1950-4180', 'affiliation': [], 'includeInCitation': True}, {'name': 'Reed, Chrystal M.', 'roleName': [], 'schemaKey': 'Person', 'identifier': '0000-0002-7157-3645', 'affiliation': [], 'includeInCitation': True}, {'name': 'Chung, Jeffrey M. ', 'roleName': [], 'schemaKey': 'Person', 'identifier': '0000-0002-4989-0994', 'affiliation': [], 'includeInCitation': True}, {'name': 'Mamelak, Adam M.', 'roleName': [], 'schemaKey': 'Person', 'identifier': '0000-0002-4245-6431', 'affiliation': [], 'includeInCitation': True}, {'name': 'Rutishauser, Ueli', 'email': 'Ueli.Rutishauser@cshs.org', 'roleName': ['dcite:Author', 'dcite:Conceptualization', 'dcite:ProjectMember', 'dcite:FundingAcquisition', 'dcite:Resources', 'dcite:Software', 'dcite:Supervision', 'dcite:Validation', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0002-9207-7069', 'affiliation': [{'name': 'Department of Neurosurgery, Cedars-Sinai Medical Center, Los Angeles, CA, USA', 'schemaKey': 'Affiliation'}, {'name': 'Department of Neurology, Cedars-Sinai Medical Center, Los Angeles, CA, USA', 'schemaKey': 'Affiliation'}, {'name': 'Division of Biology and Biological Engineering, California Institute of Technology, Pasadena, CA, USA', 'schemaKey': 'Affiliation'}, {'name': 'Computational and Neural Systems Program, California Institute of Technology, Pasadena, CA, USA', 'schemaKey': 'Affiliation'}, {'name': 'Center for Neural Science and Medicine, Department of Biomedical Science, Cedars-Sinai Medical Center, Los Angeles, CA, USA', 'schemaKey': 'Affiliation'}], 'awardNumber': '', 'includeInCitation': True}, {'name': 'National Institute of Mental Health', 'roleName': ['dcite:Sponsor'], 'schemaKey': 'Organization', 'awardNumber': 'R01MH110831', 'contactPoint': [], 'includeInCitation': False}, {'name': 'Sullivan, Shannon', 'roleName': ['dcite:DataCollector', 'dcite:Validation'], 'schemaKey': 'Person', 'identifier': '0000-0002-1137-8987', 'affiliation': [], 'includeInCitation': False}, {'name': 'National Insitute of Neurological Disorders and Stroke', 'roleName': ['dcite:Sponsor'], 'schemaKey': 'Organization', 'awardNumber': 'U01NS117839, U01NS098961', 'contactPoint': [], 'includeInCitation': False}]
description: We present a dataset of 1809 single neurons recorded from the human medial temporal lobe (amygdala and hippocampus) and medial frontal lobe (anterior cingulate cortex, pre-supplementary motor area, ventral medial prefrontal cortex) across 41 sessions from 21 patients that underwent intracranial monitoring for epileptic activity. Subjects first performed a screening task (907 neurons), based on which we identified images for which highly selective cells were present in the medial temporal lobe. Subjects then performed a working memory task (902 neurons), in which they were sequentially presented with 1-3 images, and following a maintenance period, were asked if a probe was identical to one of the currently maintained images. This Neural data without borders (NWB) formatted dataset includes spike times, extracellular spike waveforms, stimuli presented, behavior, electrode locations, and subject demographics. As validation, we replicate previous findings on the existence of concept cells and their persistent activity during working memory maintenance. This dataset provides a substantial amount of rare human single neuron recordings together with behavior, thereby enabling investigation of the neural mechanisms of working memory at the single-neuron level.

This code accompanies the following data descriptor: 
* Kyzar M, Kamiński J, Brzezicka A, Reed CM, Chung JM, Mamelak AN, Rutishauser U. Dataset of human-single neuron activity during a Sternberg working memory task. Sci Data. 2024 Jan 18;11(1):89. doi: 10.1038/s41597-024-02943-8. PMID: 38238342; PMCID: PMC10796636.
  [Link to Paper](https://pubmed.ncbi.nlm.nih.gov/38238342/)
* Sample code to access and analyze this dataset has been provided: https://github.com/rutishauserlab/workingmem-release-NWB

assetsSummary: {'species': [{'name': 'Homo sapiens - Human', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9606'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 9788560252, 'numberOfFiles': 41, 'numberOfSubjects': 21, 'variableMeasured': ['Units', 'ElectrodeGroup'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000469 has 5 NWB files.
1 of these NWB files are of type 1.
1 of these NWB files are of type 2.
1 of these NWB files are of type 3.
1 of these NWB files are of type 4.
1 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/events (TimeSeries) The events coorespond to the TTL markers for each trial. The TTL markers are the following: 61 = Start of Experiment, 1 = Start Picture Presentation, 3 = End Picture Presentation, 4 = Subject Response, 60 = End of Experiment 
  file_create_date: ['2023-06-23T00:00:00.000000-07:00' '2023-06-23T10:53:51.689795-07:00']
  Group /general/devices/NLX-microwires-31 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-33 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-34 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-35 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-36 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-37 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-38 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-39 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-40 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-42 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-43 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-44 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-45 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-50 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-51 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-54 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-56 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-60 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  experiment_description: This data contains electrophysiological recordings and behavior from the Sternberg task performed in patients with intractable epilepsy implanted with depth electrodes and Behnke-Fried microwires in the human medial temporal lobe and medial frontal cortex.
  experimenter: ['Kyzar, Michael']
  Group /general/extracellular_ephys/NLX-microwires-31 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-31/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-33 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-33/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-34 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-34/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-35 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-35/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-36 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-36/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-37 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-37/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-38 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-38/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-39 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-39/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-40 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-40/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-42 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-42/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-43 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-43/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-44 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-44/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-45 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-45/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-50 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-50/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-51 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-51/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-54 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-54/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-56 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-56/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-60 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-60/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/electrodes (DynamicTable) microwire electrodes table
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) my description | shape = (18,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) my description | shape = (18,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) my description | shape = (18,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (18,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) my description | shape = (18,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/origChannel (VectorData) my description | shape = (18,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) my description | shape = (18,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) my description | shape = (18,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) my description | shape = (18,) | dtype = float64
  institution: Cedars-Sinai Medical Center
  keywords: ['single neuron, human, intracranial, persistent activity, working memory']
  lab: Rutishauser
  notes: The session start time has been set to Jan 1st of the recording year to avoid disclosure of protected health information (PHI).
  related_publications: ['doi: 10.1038/nn.4509, 10.1016/j.neuron.2020.01.032']
  session_id: 1
  source_script: SC_NWB_export_main.m
  Group /general/subject (Subject) 
  identifier: SCID_1_P42CS
  Group /intervals/trials (TimeIntervals) Intervals for the Sternberg Screening Task
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (378,) | dtype = int32
  Dataset /intervals/trials/start_time (VectorData) Trial start times | shape = (378,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Trial stop times. | shape = (378,) | dtype = float64
  session_description: SCID: 1
  session_start_time: 2016-01-01T00:00:00.000000-08:00
  Group /stimulus/presentation/StimulusPresentation (IndexSeries) Presentation order of the stimulus. Indexes 'StimulusTemplates'.
  Group /stimulus/presentation/StimulusPresentation/indexed_images (Images) A collection of images presented to the subject
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_1 (RGBImage) image_1 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_11 (RGBImage) image_11 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_12 (RGBImage) image_12 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_13 (RGBImage) image_13 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_14 (RGBImage) image_14 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_15 (RGBImage) image_15 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_16 (RGBImage) image_16 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_17 (RGBImage) image_17 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_18 (RGBImage) image_18 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_19 (RGBImage) image_19 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_2 (RGBImage) image_2 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_21 (RGBImage) image_21 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_22 (RGBImage) image_22 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_23 (RGBImage) image_23 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_24 (RGBImage) image_24 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_25 (RGBImage) image_25 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_26 (RGBImage) image_26 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_27 (RGBImage) image_27 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_28 (RGBImage) image_28 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_29 (RGBImage) image_29 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_3 (RGBImage) image_3 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_31 (RGBImage) image_31 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_32 (RGBImage) image_32 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_33 (RGBImage) image_33 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_34 (RGBImage) image_34 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_35 (RGBImage) image_35 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_36 (RGBImage) image_36 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_37 (RGBImage) image_37 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_38 (RGBImage) image_38 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_39 (RGBImage) image_39 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_4 (RGBImage) image_4 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_41 (RGBImage) image_41 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_42 (RGBImage) image_42 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_43 (RGBImage) image_43 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_44 (RGBImage) image_44 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_45 (RGBImage) image_45 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_46 (RGBImage) image_46 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_47 (RGBImage) image_47 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_48 (RGBImage) image_48 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_49 (RGBImage) image_49 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_5 (RGBImage) image_5 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_51 (RGBImage) image_51 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_52 (RGBImage) image_52 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_53 (RGBImage) image_53 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_54 (RGBImage) image_54 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_55 (RGBImage) image_55 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_56 (RGBImage) image_56 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_57 (RGBImage) image_57 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_58 (RGBImage) image_58 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_59 (RGBImage) image_59 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_6 (RGBImage) image_6 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_61 (RGBImage) image_61 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_62 (RGBImage) image_62 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_63 (RGBImage) image_63 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_64 (RGBImage) image_64 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_65 (RGBImage) image_65 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_66 (RGBImage) image_66 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_67 (RGBImage) image_67 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_68 (RGBImage) image_68 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_69 (RGBImage) image_69 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_7 (RGBImage) image_7 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_8 (RGBImage) image_8 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_9 (RGBImage) image_9 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/order_of_images (ImageReferences)  | shape = (63,) | dtype = object
  Group /stimulus/templates/StimulusTemplates (Images) A collection of images presented to the subject
  Dataset /stimulus/templates/StimulusTemplates/image_1 (RGBImage) image_1 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_11 (RGBImage) image_11 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_12 (RGBImage) image_12 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_13 (RGBImage) image_13 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_14 (RGBImage) image_14 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_15 (RGBImage) image_15 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_16 (RGBImage) image_16 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_17 (RGBImage) image_17 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_18 (RGBImage) image_18 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_19 (RGBImage) image_19 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_2 (RGBImage) image_2 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_21 (RGBImage) image_21 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_22 (RGBImage) image_22 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_23 (RGBImage) image_23 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_24 (RGBImage) image_24 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_25 (RGBImage) image_25 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_26 (RGBImage) image_26 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_27 (RGBImage) image_27 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_28 (RGBImage) image_28 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_29 (RGBImage) image_29 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_3 (RGBImage) image_3 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_31 (RGBImage) image_31 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_32 (RGBImage) image_32 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_33 (RGBImage) image_33 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_34 (RGBImage) image_34 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_35 (RGBImage) image_35 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_36 (RGBImage) image_36 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_37 (RGBImage) image_37 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_38 (RGBImage) image_38 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_39 (RGBImage) image_39 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_4 (RGBImage) image_4 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_41 (RGBImage) image_41 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_42 (RGBImage) image_42 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_43 (RGBImage) image_43 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_44 (RGBImage) image_44 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_45 (RGBImage) image_45 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_46 (RGBImage) image_46 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_47 (RGBImage) image_47 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_48 (RGBImage) image_48 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_49 (RGBImage) image_49 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_5 (RGBImage) image_5 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_51 (RGBImage) image_51 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_52 (RGBImage) image_52 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_53 (RGBImage) image_53 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_54 (RGBImage) image_54 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_55 (RGBImage) image_55 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_56 (RGBImage) image_56 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_57 (RGBImage) image_57 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_58 (RGBImage) image_58 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_59 (RGBImage) image_59 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_6 (RGBImage) image_6 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_61 (RGBImage) image_61 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_62 (RGBImage) image_62 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_63 (RGBImage) image_63 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_64 (RGBImage) image_64 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_65 (RGBImage) image_65 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_66 (RGBImage) image_66 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_67 (RGBImage) image_67 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_68 (RGBImage) image_68 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_69 (RGBImage) image_69 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_7 (RGBImage) image_7 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_8 (RGBImage) image_8 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_9 (RGBImage) image_9 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/order_of_images (ImageReferences)  | shape = (63,) | dtype = object
  timestamps_reference_time: 2016-01-01T00:00:00.000000-08:00
  Group /units (Units) units table
  Dataset /units/clusterID_orig (VectorData) Cluster IDs of units, which referneces the cluster ID used in the native dataset. Used for cross-referencing validating the exported dataset | shape = (40,) | dtype = int32
  Dataset /units/electrodes (DynamicTableRegion) single electrodes | shape = (40,) | dtype = int32
  Dataset /units/id (ElementIdentifiers)  | shape = (40,) | dtype = int32
  Dataset /units/spike_times (VectorData) Timestamps when spikes occured (seconds) | shape = (86613,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) indexes data | shape = (40,) | dtype = uint64
  Dataset /units/waveform_mean (VectorData) Mean waveform for each unit. | shape = (40, 256) | dtype = float64
  Dataset /units/waveform_sd (VectorData) Standard deviation for all waveform means at each timestamp. | shape = (40, 256) | dtype = float64
  Dataset /units/waveforms (VectorData) Array of Nx256 waveforms across all clusters. | shape = (86613, 256) | dtype = float64
  Dataset /units/waveforms_index (VectorIndex) indexes data | shape = (40,) | dtype = uint64
  Dataset /units/waveforms_index_index (VectorIndex) indexes indexes | shape = (40,) | dtype = uint64
  Dataset /units/waveforms_isolation_distance (VectorData) Cluster Isolation distance, computed using all waveforms in the cluster. | shape = (40,) | dtype = float64
  Dataset /units/waveforms_mean_proj_dist (VectorData) Cluster Isolation distance, computed using all waveforms in the cluster. | shape = (40,) | dtype = float64
  Dataset /units/waveforms_mean_snr (VectorData) Mean Signal-to-Noise Ratio (SNR) across all samples of the mean waveform. | shape = (40,) | dtype = float64
  Dataset /units/waveforms_peak_snr (VectorData) Signal-to-Noise Ratio (SNR) of the mean signal amplitude. | shape = (40,) | dtype = float64


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/events (TimeSeries) The events coorespond to the TTL markers for each trial. The TTL markers are the following: 61 = Start of Experiment, 11 = Fixation Cross, 1 = Picture #1 Shown, 2 = Picture #2 Shown, 3 = Picture #3 Shown, 5 = Transition between each picture presentation, 6 = End of Encoding Sequence / Start of Maintenance Period, 7 = Probe Stimulus, 8 = Subject Response, 60 = End of Experiment 
  file_create_date: ['2023-06-23T00:00:00.000000-07:00' '2023-06-23T10:17:28.436826-07:00']
  Group /general/devices/NLX-microwires-33 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-34 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-35 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-36 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-37 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-38 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-39 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-41 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-42 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-43 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-44 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-45 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-46 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-47 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-48 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-49 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-51 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-52 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-54 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-56 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-60 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-62 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  experiment_description: This data contains electrophysiological recordings and behavior from the Sternberg task performed in patients with intractable epilepsy implanted with depth electrodes and Behnke-Fried microwires in the human medial temporal lobe and medial frontal cortex.
  experimenter: ['Kyzar, Michael']
  Group /general/extracellular_ephys/NLX-microwires-33 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-33/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-34 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-34/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-35 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-35/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-36 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-36/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-37 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-37/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-38 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-38/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-39 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-39/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-41 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-41/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-42 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-42/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-43 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-43/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-44 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-44/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-45 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-45/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-46 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-46/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-47 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-47/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-48 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-48/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-49 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-49/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-51 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-51/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-52 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-52/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-54 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-54/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-56 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-56/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-60 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-60/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-62 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-62/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/electrodes (DynamicTable) microwire electrodes table
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) my description | shape = (22,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) my description | shape = (22,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) my description | shape = (22,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (22,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) my description | shape = (22,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/origChannel (VectorData) my description | shape = (22,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) my description | shape = (22,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) my description | shape = (22,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) my description | shape = (22,) | dtype = float64
  institution: Cedars-Sinai Medical Center
  keywords: ['single neuron, human, intracranial, persistent activity, working memory']
  lab: Rutishauser
  notes: The session start time has been set to Jan 1st of the recording year to avoid disclosure of protected health information (PHI).
  related_publications: ['doi: 10.1038/nn.4509, 10.1016/j.neuron.2020.01.032']
  session_id: 2
  source_script: SB_NWB_export_main.m
  Group /general/subject (Subject) 
  identifier: SBID_1_P42CS
  Group /intervals/trials (TimeIntervals) Intervals for the Sternberg Task
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (135,) | dtype = int32
  Dataset /intervals/trials/loads (VectorData) Encoding loads for each trial | shape = (135,) | dtype = uint8
  Dataset /intervals/trials/loadsEnc1_PicIDs (VectorData) Picture ID for Enc1 loads. | shape = (135,) | dtype = uint8
  Dataset /intervals/trials/loadsEnc2_PicIDs (VectorData) Picture ID for Enc2 loads. | shape = (135,) | dtype = uint8
  Dataset /intervals/trials/loadsEnc3_PicIDs (VectorData) Picture ID for Enc1 loads. | shape = (135,) | dtype = uint8
  Dataset /intervals/trials/loadsProbe_PicIDs (VectorData) Picture ID for Probe loads. | shape = (135,) | dtype = uint8
  Dataset /intervals/trials/probe_in_out (VectorData) Whether the probe image was held (1) or not held (0) in memory. | shape = (135,) | dtype = uint8
  Dataset /intervals/trials/response_accuracy (VectorData) Whether the subject response was correct (1) or incorrect (0). | shape = (135,) | dtype = uint8
  Dataset /intervals/trials/start_time (VectorData) Trial start times | shape = (135,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Trial stop times | shape = (135,) | dtype = float64
  Dataset /intervals/trials/timestamps_Encoding1 (VectorData) Start times of picture #1 presentation | shape = (135,) | dtype = float64
  Dataset /intervals/trials/timestamps_Encoding1_end (VectorData) End times of picture #1 presentation | shape = (135,) | dtype = float64
  Dataset /intervals/trials/timestamps_Encoding2 (VectorData) Start times of picture #2 presentation | shape = (135,) | dtype = float64
  Dataset /intervals/trials/timestamps_Encoding2_end (VectorData) End times of picture #2 presentation | shape = (135,) | dtype = float64
  Dataset /intervals/trials/timestamps_Encoding3 (VectorData) Start times of picture #3 presentation | shape = (135,) | dtype = float64
  Dataset /intervals/trials/timestamps_Encoding3_end (VectorData) End times of picture #3 presentation | shape = (135,) | dtype = float64
  Dataset /intervals/trials/timestamps_FixationCross (VectorData) Start times of fixation cross | shape = (135,) | dtype = float64
  Dataset /intervals/trials/timestamps_Maintenance (VectorData) Start times of maintenance periods | shape = (135,) | dtype = float64
  Dataset /intervals/trials/timestamps_Probe (VectorData) Start times of probe onset | shape = (135,) | dtype = float64
  Dataset /intervals/trials/timestamps_Response (VectorData) Time stamps of button press | shape = (135,) | dtype = float64
  session_description: SBID: 1
  session_start_time: 2016-01-01T00:00:00.000000-08:00
  Group /stimulus/presentation/StimulusPresentation (IndexSeries) Presentation order of the stimulus. Indexes 'StimulusTemplates'.
  Group /stimulus/presentation/StimulusPresentation/indexed_images (Images) A collection of images presented to the subject
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_22 (RGBImage) image_22 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_44 (RGBImage) image_44 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_53 (RGBImage) image_53 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_61 (RGBImage) image_61 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_62 (RGBImage) image_62 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_999 (RGBImage) image_999 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/order_of_images (ImageReferences)  | shape = (6,) | dtype = object
  Group /stimulus/templates/StimulusTemplates (Images) A collection of images presented to the subject
  Dataset /stimulus/templates/StimulusTemplates/image_22 (RGBImage) image_22 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_44 (RGBImage) image_44 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_53 (RGBImage) image_53 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_61 (RGBImage) image_61 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_62 (RGBImage) image_62 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_999 (RGBImage) image_999 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/order_of_images (ImageReferences)  | shape = (6,) | dtype = object
  timestamps_reference_time: 2016-01-01T00:00:00.000000-08:00
  Group /units (Units) units table
  Dataset /units/clusterID_orig (VectorData) Cluster IDs of units, which referneces the cluster ID used in the native dataset. Used for cross-referencing validating the exported dataset | shape = (40,) | dtype = float64
  Dataset /units/electrodes (DynamicTableRegion) single electrodes | shape = (40,) | dtype = int32
  Dataset /units/id (ElementIdentifiers)  | shape = (40,) | dtype = int32
  Dataset /units/spike_times (VectorData) Timestamps when spikes occured (seconds) | shape = (106650,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) indexes data | shape = (40,) | dtype = uint64
  Dataset /units/waveform_mean (VectorData) Mean waveform for each unit. | shape = (40, 256) | dtype = float64
  Dataset /units/waveform_sd (VectorData) Standard deviation for all waveform means at each timestamp. | shape = (40, 256) | dtype = float64
  Dataset /units/waveforms (VectorData) Array of Nx256 waveforms across all clusters. | shape = (106650, 256) | dtype = float64
  Dataset /units/waveforms_index (VectorIndex) indexes data | shape = (40,) | dtype = uint64
  Dataset /units/waveforms_index_index (VectorIndex) indexes indexes | shape = (40,) | dtype = uint64
  Dataset /units/waveforms_isolation_distance (VectorData) Cluster Isolation distance, computed using all waveforms in the cluster. | shape = (40,) | dtype = float64
  Dataset /units/waveforms_mean_proj_dist (VectorData) Cluster Isolation distance, computed using all waveforms in the cluster. | shape = (40,) | dtype = float64
  Dataset /units/waveforms_mean_snr (VectorData) Mean Signal-to-Noise Ratio (SNR) across all samples of the mean waveform. | shape = (40,) | dtype = float64
  Dataset /units/waveforms_peak_snr (VectorData) Signal-to-Noise Ratio (SNR) of the mean signal amplitude. | shape = (40,) | dtype = float64


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/events (TimeSeries) The events coorespond to the TTL markers for each trial. The TTL markers are the following: 61 = Start of Experiment, 1 = Start Picture Presentation, 3 = End Picture Presentation, 4 = Subject Response, 60 = End of Experiment 
  file_create_date: ['2023-06-23T00:00:00.000000-07:00' '2023-06-23T11:09:12.670072-07:00']
  Group /general/devices/NLX-microwires-1 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-10 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-11 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-12 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-13 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-14 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-15 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-16 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-17 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-18 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-19 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-2 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-20 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-21 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-22 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-23 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-24 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-25 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-26 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-27 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-28 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-29 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-3 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-30 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-31 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-32 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-33 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-34 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-35 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-36 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-37 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-38 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-39 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-4 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-40 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-5 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-6 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-7 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-8 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  experiment_description: This data contains electrophysiological recordings and behavior from the Sternberg task performed in patients with intractable epilepsy implanted with depth electrodes and Behnke-Fried microwires in the human medial temporal lobe and medial frontal cortex.
  experimenter: ['Kyzar, Michael']
  Group /general/extracellular_ephys/NLX-microwires-1 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-1/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-10 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-10/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-11 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-11/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-12 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-12/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-13 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-13/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-14 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-14/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-15 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-15/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-16 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-16/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-17 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-17/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-18 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-18/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-19 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-19/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-2 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-2/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-20 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-20/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-21 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-21/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-22 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-22/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-23 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-23/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-24 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-24/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-25 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-25/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-26 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-26/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-27 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-27/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-28 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-28/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-29 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-29/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-3 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-3/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-30 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-30/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-31 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-31/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-32 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-32/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-33 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-33/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-34 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-34/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-35 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-35/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-36 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-36/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-37 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-37/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-38 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-38/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-39 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-39/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-4 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-4/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-40 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-40/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-5 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-5/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-6 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-6/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-7 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-7/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-8 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-8/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/electrodes (DynamicTable) microwire electrodes table
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) my description | shape = (39,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) my description | shape = (39,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) my description | shape = (39,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (39,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) my description | shape = (39,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/origChannel (VectorData) my description | shape = (39,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) my description | shape = (39,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) my description | shape = (39,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) my description | shape = (39,) | dtype = float64
  institution: Cedars-Sinai Medical Center
  keywords: ['single neuron, human, intracranial, persistent activity, working memory']
  lab: Rutishauser
  notes: The session start time has been set to Jan 1st of the recording year to avoid disclosure of protected health information (PHI).
  related_publications: ['doi: 10.1038/nn.4509, 10.1016/j.neuron.2020.01.032']
  session_id: 1
  source_script: SC_NWB_export_main.m
  Group /general/subject (Subject) 
  identifier: SCID_10_P35CS
  Group /intervals/trials (TimeIntervals) Intervals for the Sternberg Screening Task
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (378,) | dtype = int32
  Dataset /intervals/trials/start_time (VectorData) Trial start times | shape = (378,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Trial stop times. | shape = (378,) | dtype = float64
  session_description: SCID: 10
  session_start_time: 2014-01-01T00:00:00.000000-08:00
  Group /stimulus/presentation/StimulusPresentation (IndexSeries) Presentation order of the stimulus. Indexes 'StimulusTemplates'.
  Group /stimulus/presentation/StimulusPresentation/indexed_images (Images) A collection of images presented to the subject
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_1 (RGBImage) image_1 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_11 (RGBImage) image_11 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_12 (RGBImage) image_12 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_13 (RGBImage) image_13 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_14 (RGBImage) image_14 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_15 (RGBImage) image_15 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_16 (RGBImage) image_16 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_17 (RGBImage) image_17 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_18 (RGBImage) image_18 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_19 (RGBImage) image_19 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_2 (RGBImage) image_2 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_21 (RGBImage) image_21 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_22 (RGBImage) image_22 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_23 (RGBImage) image_23 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_24 (RGBImage) image_24 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_25 (RGBImage) image_25 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_26 (RGBImage) image_26 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_27 (RGBImage) image_27 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_28 (RGBImage) image_28 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_29 (RGBImage) image_29 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_3 (RGBImage) image_3 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_31 (RGBImage) image_31 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_32 (RGBImage) image_32 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_33 (RGBImage) image_33 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_34 (RGBImage) image_34 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_35 (RGBImage) image_35 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_36 (RGBImage) image_36 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_37 (RGBImage) image_37 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_38 (RGBImage) image_38 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_39 (RGBImage) image_39 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_4 (RGBImage) image_4 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_41 (RGBImage) image_41 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_42 (RGBImage) image_42 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_43 (RGBImage) image_43 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_44 (RGBImage) image_44 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_45 (RGBImage) image_45 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_46 (RGBImage) image_46 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_47 (RGBImage) image_47 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_48 (RGBImage) image_48 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_49 (RGBImage) image_49 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_5 (RGBImage) image_5 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_51 (RGBImage) image_51 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_52 (RGBImage) image_52 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_53 (RGBImage) image_53 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_54 (RGBImage) image_54 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_55 (RGBImage) image_55 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_56 (RGBImage) image_56 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_57 (RGBImage) image_57 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_58 (RGBImage) image_58 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_59 (RGBImage) image_59 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_6 (RGBImage) image_6 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_61 (RGBImage) image_61 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_62 (RGBImage) image_62 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_63 (RGBImage) image_63 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_64 (RGBImage) image_64 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_65 (RGBImage) image_65 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_66 (RGBImage) image_66 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_67 (RGBImage) image_67 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_68 (RGBImage) image_68 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_69 (RGBImage) image_69 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_7 (RGBImage) image_7 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_8 (RGBImage) image_8 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_9 (RGBImage) image_9 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/order_of_images (ImageReferences)  | shape = (63,) | dtype = object
  Group /stimulus/templates/StimulusTemplates (Images) A collection of images presented to the subject
  Dataset /stimulus/templates/StimulusTemplates/image_1 (RGBImage) image_1 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_11 (RGBImage) image_11 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_12 (RGBImage) image_12 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_13 (RGBImage) image_13 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_14 (RGBImage) image_14 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_15 (RGBImage) image_15 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_16 (RGBImage) image_16 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_17 (RGBImage) image_17 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_18 (RGBImage) image_18 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_19 (RGBImage) image_19 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_2 (RGBImage) image_2 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_21 (RGBImage) image_21 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_22 (RGBImage) image_22 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_23 (RGBImage) image_23 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_24 (RGBImage) image_24 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_25 (RGBImage) image_25 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_26 (RGBImage) image_26 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_27 (RGBImage) image_27 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_28 (RGBImage) image_28 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_29 (RGBImage) image_29 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_3 (RGBImage) image_3 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_31 (RGBImage) image_31 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_32 (RGBImage) image_32 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_33 (RGBImage) image_33 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_34 (RGBImage) image_34 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_35 (RGBImage) image_35 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_36 (RGBImage) image_36 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_37 (RGBImage) image_37 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_38 (RGBImage) image_38 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_39 (RGBImage) image_39 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_4 (RGBImage) image_4 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_41 (RGBImage) image_41 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_42 (RGBImage) image_42 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_43 (RGBImage) image_43 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_44 (RGBImage) image_44 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_45 (RGBImage) image_45 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_46 (RGBImage) image_46 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_47 (RGBImage) image_47 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_48 (RGBImage) image_48 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_49 (RGBImage) image_49 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_5 (RGBImage) image_5 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_51 (RGBImage) image_51 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_52 (RGBImage) image_52 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_53 (RGBImage) image_53 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_54 (RGBImage) image_54 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_55 (RGBImage) image_55 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_56 (RGBImage) image_56 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_57 (RGBImage) image_57 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_58 (RGBImage) image_58 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_59 (RGBImage) image_59 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_6 (RGBImage) image_6 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_61 (RGBImage) image_61 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_62 (RGBImage) image_62 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_63 (RGBImage) image_63 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_64 (RGBImage) image_64 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_65 (RGBImage) image_65 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_66 (RGBImage) image_66 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_67 (RGBImage) image_67 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_68 (RGBImage) image_68 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_69 (RGBImage) image_69 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_7 (RGBImage) image_7 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_8 (RGBImage) image_8 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_9 (RGBImage) image_9 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/order_of_images (ImageReferences)  | shape = (63,) | dtype = object
  timestamps_reference_time: 2014-01-01T00:00:00.000000-08:00
  Group /units (Units) units table
  Dataset /units/clusterID_orig (VectorData) Cluster IDs of units, which referneces the cluster ID used in the native dataset. Used for cross-referencing validating the exported dataset | shape = (74,) | dtype = int32
  Dataset /units/electrodes (DynamicTableRegion) single electrodes | shape = (74,) | dtype = int32
  Dataset /units/id (ElementIdentifiers)  | shape = (74,) | dtype = int32
  Dataset /units/spike_times (VectorData) Timestamps when spikes occured (seconds) | shape = (163314,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) indexes data | shape = (74,) | dtype = uint64
  Dataset /units/waveform_mean (VectorData) Mean waveform for each unit. | shape = (74, 256) | dtype = float64
  Dataset /units/waveform_sd (VectorData) Standard deviation for all waveform means at each timestamp. | shape = (74, 256) | dtype = float64
  Dataset /units/waveforms (VectorData) Array of Nx256 waveforms across all clusters. | shape = (163314, 256) | dtype = float64
  Dataset /units/waveforms_index (VectorIndex) indexes data | shape = (74,) | dtype = uint64
  Dataset /units/waveforms_index_index (VectorIndex) indexes indexes | shape = (74,) | dtype = uint64
  Dataset /units/waveforms_isolation_distance (VectorData) Cluster Isolation distance, computed using all waveforms in the cluster. | shape = (74,) | dtype = float64
  Dataset /units/waveforms_mean_proj_dist (VectorData) Cluster Isolation distance, computed using all waveforms in the cluster. | shape = (74,) | dtype = float64
  Dataset /units/waveforms_mean_snr (VectorData) Mean Signal-to-Noise Ratio (SNR) across all samples of the mean waveform. | shape = (74,) | dtype = float64
  Dataset /units/waveforms_peak_snr (VectorData) Signal-to-Noise Ratio (SNR) of the mean signal amplitude. | shape = (74,) | dtype = float64


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/events (TimeSeries) The events coorespond to the TTL markers for each trial. The TTL markers are the following: 61 = Start of Experiment, 11 = Fixation Cross, 1 = Picture #1 Shown, 2 = Picture #2 Shown, 3 = Picture #3 Shown, 5 = Transition between each picture presentation, 6 = End of Encoding Sequence / Start of Maintenance Period, 7 = Probe Stimulus, 8 = Subject Response, 60 = End of Experiment 
  file_create_date: ['2023-06-23T00:00:00.000000-07:00' '2023-06-23T10:40:31.291986-07:00']
  Group /general/devices/NLX-microwires-25 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-26 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-30 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-33 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-37 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-38 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-39 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-49 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-50 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-51 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-52 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-53 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-54 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-55 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-56 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  experiment_description: This data contains electrophysiological recordings and behavior from the Sternberg task performed in patients with intractable epilepsy implanted with depth electrodes and Behnke-Fried microwires in the human medial temporal lobe and medial frontal cortex.
  experimenter: ['Kyzar, Michael']
  Group /general/extracellular_ephys/NLX-microwires-25 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-25/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-26 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-26/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-30 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-30/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-33 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-33/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-37 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-37/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-38 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-38/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-39 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-39/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-49 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-49/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-50 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-50/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-51 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-51/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-52 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-52/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-53 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-53/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-54 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-54/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-55 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-55/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-56 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-56/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/electrodes (DynamicTable) microwire electrodes table
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) my description | shape = (15,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) my description | shape = (15,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) my description | shape = (15,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (15,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) my description | shape = (15,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/origChannel (VectorData) my description | shape = (15,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) my description | shape = (15,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) my description | shape = (15,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) my description | shape = (15,) | dtype = float64
  institution: Cedars-Sinai Medical Center
  keywords: ['single neuron, human, intracranial, persistent activity, working memory']
  lab: Rutishauser
  notes: The session start time has been set to Jan 1st of the recording year to avoid disclosure of protected health information (PHI).
  related_publications: ['doi: 10.1038/nn.4509, 10.1016/j.neuron.2020.01.032']
  session_id: 2
  source_script: SB_NWB_export_main.m
  Group /general/subject (Subject) 
  identifier: SBID_10_P35CS
  Group /intervals/trials (TimeIntervals) Intervals for the Sternberg Task
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (135,) | dtype = int32
  Dataset /intervals/trials/loads (VectorData) Encoding loads for each trial | shape = (135,) | dtype = uint8
  Dataset /intervals/trials/loadsEnc1_PicIDs (VectorData) Picture ID for Enc1 loads. | shape = (135,) | dtype = uint8
  Dataset /intervals/trials/loadsEnc2_PicIDs (VectorData) Picture ID for Enc2 loads. | shape = (135,) | dtype = uint8
  Dataset /intervals/trials/loadsEnc3_PicIDs (VectorData) Picture ID for Enc1 loads. | shape = (135,) | dtype = uint8
  Dataset /intervals/trials/loadsProbe_PicIDs (VectorData) Picture ID for Probe loads. | shape = (135,) | dtype = uint8
  Dataset /intervals/trials/probe_in_out (VectorData) Whether the probe image was held (1) or not held (0) in memory. | shape = (135,) | dtype = uint8
  Dataset /intervals/trials/response_accuracy (VectorData) Whether the subject response was correct (1) or incorrect (0). | shape = (135,) | dtype = uint8
  Dataset /intervals/trials/start_time (VectorData) Trial start times | shape = (135,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Trial stop times | shape = (135,) | dtype = float64
  Dataset /intervals/trials/timestamps_Encoding1 (VectorData) Start times of picture #1 presentation | shape = (135,) | dtype = float64
  Dataset /intervals/trials/timestamps_Encoding1_end (VectorData) End times of picture #1 presentation | shape = (135,) | dtype = float64
  Dataset /intervals/trials/timestamps_Encoding2 (VectorData) Start times of picture #2 presentation | shape = (135,) | dtype = float64
  Dataset /intervals/trials/timestamps_Encoding2_end (VectorData) End times of picture #2 presentation | shape = (135,) | dtype = float64
  Dataset /intervals/trials/timestamps_Encoding3 (VectorData) Start times of picture #3 presentation | shape = (135,) | dtype = float64
  Dataset /intervals/trials/timestamps_Encoding3_end (VectorData) End times of picture #3 presentation | shape = (135,) | dtype = float64
  Dataset /intervals/trials/timestamps_FixationCross (VectorData) Start times of fixation cross | shape = (135,) | dtype = float64
  Dataset /intervals/trials/timestamps_Maintenance (VectorData) Start times of maintenance periods | shape = (135,) | dtype = float64
  Dataset /intervals/trials/timestamps_Probe (VectorData) Start times of probe onset | shape = (135,) | dtype = float64
  Dataset /intervals/trials/timestamps_Response (VectorData) Time stamps of button press | shape = (135,) | dtype = float64
  session_description: SBID: 10
  session_start_time: 2014-01-01T00:00:00.000000-08:00
  Group /stimulus/presentation/StimulusPresentation (IndexSeries) Presentation order of the stimulus. Indexes 'StimulusTemplates'.
  Group /stimulus/presentation/StimulusPresentation/indexed_images (Images) A collection of images presented to the subject
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_36 (RGBImage) image_36 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_42 (RGBImage) image_42 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_44 (RGBImage) image_44 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_67 (RGBImage) image_67 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_8 (RGBImage) image_8 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_999 (RGBImage) image_999 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/order_of_images (ImageReferences)  | shape = (6,) | dtype = object
  Group /stimulus/templates/StimulusTemplates (Images) A collection of images presented to the subject
  Dataset /stimulus/templates/StimulusTemplates/image_36 (RGBImage) image_36 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_42 (RGBImage) image_42 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_44 (RGBImage) image_44 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_67 (RGBImage) image_67 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_8 (RGBImage) image_8 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_999 (RGBImage) image_999 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/order_of_images (ImageReferences)  | shape = (6,) | dtype = object
  timestamps_reference_time: 2014-01-01T00:00:00.000000-08:00
  Group /units (Units) units table
  Dataset /units/clusterID_orig (VectorData) Cluster IDs of units, which referneces the cluster ID used in the native dataset. Used for cross-referencing validating the exported dataset | shape = (28,) | dtype = float64
  Dataset /units/electrodes (DynamicTableRegion) single electrodes | shape = (28,) | dtype = int32
  Dataset /units/id (ElementIdentifiers)  | shape = (28,) | dtype = int32
  Dataset /units/spike_times (VectorData) Timestamps when spikes occured (seconds) | shape = (127202,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) indexes data | shape = (28,) | dtype = uint64
  Dataset /units/waveform_mean (VectorData) Mean waveform for each unit. | shape = (28, 256) | dtype = float64
  Dataset /units/waveform_sd (VectorData) Standard deviation for all waveform means at each timestamp. | shape = (28, 256) | dtype = float64
  Dataset /units/waveforms (VectorData) Array of Nx256 waveforms across all clusters. | shape = (127202, 256) | dtype = float64
  Dataset /units/waveforms_index (VectorIndex) indexes data | shape = (28,) | dtype = uint64
  Dataset /units/waveforms_index_index (VectorIndex) indexes indexes | shape = (28,) | dtype = uint64
  Dataset /units/waveforms_isolation_distance (VectorData) Cluster Isolation distance, computed using all waveforms in the cluster. | shape = (28,) | dtype = float64
  Dataset /units/waveforms_mean_proj_dist (VectorData) Cluster Isolation distance, computed using all waveforms in the cluster. | shape = (28,) | dtype = float64
  Dataset /units/waveforms_mean_snr (VectorData) Mean Signal-to-Noise Ratio (SNR) across all samples of the mean waveform. | shape = (28,) | dtype = float64
  Dataset /units/waveforms_peak_snr (VectorData) Signal-to-Noise Ratio (SNR) of the mean signal amplitude. | shape = (28,) | dtype = float64


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  Group /acquisition/events (TimeSeries) The events coorespond to the TTL markers for each trial. The TTL markers are the following: 61 = Start of Experiment, 1 = Start Picture Presentation, 3 = End Picture Presentation, 4 = Subject Response, 60 = End of Experiment 
  file_create_date: ['2023-06-23T00:00:00.000000-07:00' '2023-06-23T11:15:01.521913-07:00']
  Group /general/devices/NLX-microwires-10 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-11 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-12 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-13 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-14 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-15 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-16 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-17 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-18 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-19 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-20 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-21 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-22 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-23 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-24 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-29 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-3 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-30 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-32 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-33 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-34 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-36 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-39 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-4 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-40 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-41 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-42 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-46 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-5 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-50 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-51 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-52 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-55 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-57 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-58 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-59 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-6 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-60 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-61 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-62 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-63 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-64 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-7 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-8 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-9 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  experiment_description: This data contains electrophysiological recordings and behavior from the Sternberg task performed in patients with intractable epilepsy implanted with depth electrodes and Behnke-Fried microwires in the human medial temporal lobe and medial frontal cortex.
  experimenter: ['Kyzar, Michael']
  Group /general/extracellular_ephys/NLX-microwires-10 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-10/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-11 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-11/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-12 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-12/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-13 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-13/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-14 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-14/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-15 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-15/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-16 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-16/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-17 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-17/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-18 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-18/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-19 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-19/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-20 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-20/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-21 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-21/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-22 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-22/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-23 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-23/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-24 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-24/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-29 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-29/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-3 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-3/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-30 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-30/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-32 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-32/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-33 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-33/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-34 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-34/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-36 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-36/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-39 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-39/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-4 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-4/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-40 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-40/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-41 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-41/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-42 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-42/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-46 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-46/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-5 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-5/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-50 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-50/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-51 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-51/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-52 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-52/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-55 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-55/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-57 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-57/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-58 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-58/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-59 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-59/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-6 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-6/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-60 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-60/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-61 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-61/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-62 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-62/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-63 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-63/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-64 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-64/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-7 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-7/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-8 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-8/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-9 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-9/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/electrodes (DynamicTable) microwire electrodes table
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) my description | shape = (45,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) my description | shape = (45,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) my description | shape = (45,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (45,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) my description | shape = (45,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/origChannel (VectorData) my description | shape = (45,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) my description | shape = (45,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) my description | shape = (45,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) my description | shape = (45,) | dtype = float64
  institution: Cedars-Sinai Medical Center
  keywords: ['single neuron, human, intracranial, persistent activity, working memory']
  lab: Rutishauser
  notes: The session start time has been set to Jan 1st of the recording year to avoid disclosure of protected health information (PHI).
  related_publications: ['doi: 10.1038/nn.4509, 10.1016/j.neuron.2020.01.032']
  session_id: 1
  source_script: SC_NWB_export_main.m
  Group /general/subject (Subject) 
  identifier: SCID_11_P36CS
  Group /intervals/trials (TimeIntervals) Intervals for the Sternberg Screening Task
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (378,) | dtype = int32
  Dataset /intervals/trials/start_time (VectorData) Trial start times | shape = (378,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Trial stop times. Due to a damagaged events file for this subject, The stop time has been set to the start time of the next trial. | shape = (378,) | dtype = float64
  session_description: SCID: 11
  session_start_time: 2015-01-01T00:00:00.000000-08:00
  Group /stimulus/presentation/StimulusPresentation (IndexSeries) Presentation order of the stimulus. Indexes 'StimulusTemplates'.
  Group /stimulus/presentation/StimulusPresentation/indexed_images (Images) A collection of images presented to the subject
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_1 (RGBImage) image_1 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_11 (RGBImage) image_11 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_12 (RGBImage) image_12 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_13 (RGBImage) image_13 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_14 (RGBImage) image_14 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_15 (RGBImage) image_15 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_16 (RGBImage) image_16 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_17 (RGBImage) image_17 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_18 (RGBImage) image_18 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_19 (RGBImage) image_19 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_2 (RGBImage) image_2 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_21 (RGBImage) image_21 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_22 (RGBImage) image_22 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_23 (RGBImage) image_23 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_24 (RGBImage) image_24 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_25 (RGBImage) image_25 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_26 (RGBImage) image_26 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_27 (RGBImage) image_27 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_28 (RGBImage) image_28 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_29 (RGBImage) image_29 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_3 (RGBImage) image_3 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_31 (RGBImage) image_31 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_32 (RGBImage) image_32 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_33 (RGBImage) image_33 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_34 (RGBImage) image_34 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_35 (RGBImage) image_35 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_36 (RGBImage) image_36 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_37 (RGBImage) image_37 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_38 (RGBImage) image_38 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_39 (RGBImage) image_39 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_4 (RGBImage) image_4 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_41 (RGBImage) image_41 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_42 (RGBImage) image_42 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_43 (RGBImage) image_43 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_44 (RGBImage) image_44 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_45 (RGBImage) image_45 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_46 (RGBImage) image_46 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_47 (RGBImage) image_47 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_48 (RGBImage) image_48 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_49 (RGBImage) image_49 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_5 (RGBImage) image_5 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_51 (RGBImage) image_51 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_52 (RGBImage) image_52 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_53 (RGBImage) image_53 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_54 (RGBImage) image_54 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_55 (RGBImage) image_55 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_56 (RGBImage) image_56 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_57 (RGBImage) image_57 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_58 (RGBImage) image_58 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_59 (RGBImage) image_59 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_6 (RGBImage) image_6 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_61 (RGBImage) image_61 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_62 (RGBImage) image_62 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_63 (RGBImage) image_63 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_64 (RGBImage) image_64 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_65 (RGBImage) image_65 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_66 (RGBImage) image_66 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_67 (RGBImage) image_67 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_68 (RGBImage) image_68 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_69 (RGBImage) image_69 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_7 (RGBImage) image_7 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_8 (RGBImage) image_8 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/image_9 (RGBImage) image_9 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/presentation/StimulusPresentation/indexed_images/order_of_images (ImageReferences)  | shape = (63,) | dtype = object
  Group /stimulus/templates/StimulusTemplates (Images) A collection of images presented to the subject
  Dataset /stimulus/templates/StimulusTemplates/image_1 (RGBImage) image_1 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_11 (RGBImage) image_11 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_12 (RGBImage) image_12 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_13 (RGBImage) image_13 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_14 (RGBImage) image_14 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_15 (RGBImage) image_15 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_16 (RGBImage) image_16 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_17 (RGBImage) image_17 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_18 (RGBImage) image_18 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_19 (RGBImage) image_19 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_2 (RGBImage) image_2 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_21 (RGBImage) image_21 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_22 (RGBImage) image_22 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_23 (RGBImage) image_23 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_24 (RGBImage) image_24 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_25 (RGBImage) image_25 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_26 (RGBImage) image_26 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_27 (RGBImage) image_27 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_28 (RGBImage) image_28 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_29 (RGBImage) image_29 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_3 (RGBImage) image_3 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_31 (RGBImage) image_31 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_32 (RGBImage) image_32 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_33 (RGBImage) image_33 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_34 (RGBImage) image_34 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_35 (RGBImage) image_35 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_36 (RGBImage) image_36 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_37 (RGBImage) image_37 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_38 (RGBImage) image_38 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_39 (RGBImage) image_39 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_4 (RGBImage) image_4 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_41 (RGBImage) image_41 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_42 (RGBImage) image_42 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_43 (RGBImage) image_43 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_44 (RGBImage) image_44 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_45 (RGBImage) image_45 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_46 (RGBImage) image_46 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_47 (RGBImage) image_47 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_48 (RGBImage) image_48 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_49 (RGBImage) image_49 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_5 (RGBImage) image_5 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_51 (RGBImage) image_51 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_52 (RGBImage) image_52 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_53 (RGBImage) image_53 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_54 (RGBImage) image_54 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_55 (RGBImage) image_55 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_56 (RGBImage) image_56 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_57 (RGBImage) image_57 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_58 (RGBImage) image_58 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_59 (RGBImage) image_59 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_6 (RGBImage) image_6 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_61 (RGBImage) image_61 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_62 (RGBImage) image_62 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_63 (RGBImage) image_63 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_64 (RGBImage) image_64 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_65 (RGBImage) image_65 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_66 (RGBImage) image_66 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_67 (RGBImage) image_67 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_68 (RGBImage) image_68 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_69 (RGBImage) image_69 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_7 (RGBImage) image_7 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_8 (RGBImage) image_8 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/image_9 (RGBImage) image_9 | shape = (400, 300, 3) | dtype = uint8
  Dataset /stimulus/templates/StimulusTemplates/order_of_images (ImageReferences)  | shape = (63,) | dtype = object
  timestamps_reference_time: 2015-01-01T00:00:00.000000-08:00
  Group /units (Units) units table
  Dataset /units/clusterID_orig (VectorData) Cluster IDs of units, which referneces the cluster ID used in the native dataset. Used for cross-referencing validating the exported dataset | shape = (94,) | dtype = int32
  Dataset /units/electrodes (DynamicTableRegion) single electrodes | shape = (94,) | dtype = int32
  Dataset /units/id (ElementIdentifiers)  | shape = (94,) | dtype = int32
  Dataset /units/spike_times (VectorData) Timestamps when spikes occured (seconds) | shape = (242961,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) indexes data | shape = (94,) | dtype = uint64
  Dataset /units/waveform_mean (VectorData) Mean waveform for each unit. | shape = (94, 256) | dtype = float64
  Dataset /units/waveform_sd (VectorData) Standard deviation for all waveform means at each timestamp. | shape = (94, 256) | dtype = float64
  Dataset /units/waveforms (VectorData) Array of Nx256 waveforms across all clusters. | shape = (242961, 256) | dtype = float64
  Dataset /units/waveforms_index (VectorIndex) indexes data | shape = (94,) | dtype = uint64
  Dataset /units/waveforms_index_index (VectorIndex) indexes indexes | shape = (94,) | dtype = uint64
  Dataset /units/waveforms_isolation_distance (VectorData) Cluster Isolation distance, computed using all waveforms in the cluster. | shape = (94,) | dtype = float64
  Dataset /units/waveforms_mean_proj_dist (VectorData) Cluster Isolation distance, computed using all waveforms in the cluster. | shape = (94,) | dtype = float64
  Dataset /units/waveforms_mean_snr (VectorData) Mean Signal-to-Noise Ratio (SNR) across all samples of the mean waveform. | shape = (94,) | dtype = float64
  Dataset /units/waveforms_peak_snr (VectorData) Signal-to-Noise Ratio (SNR) of the mean signal amplitude. | shape = (94,) | dtype = float64
