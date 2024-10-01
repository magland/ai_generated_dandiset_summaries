
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000004/0.220126.1852
name: A NWB-based dataset and processing pipeline of human single-neuron activity during a declarative memory task
contributor: [{'name': 'Chandravadia, Nand', 'email': 'nandc10@gmail.com', 'roleName': ['dcite:Author', 'dcite:ContactPerson', 'dcite:DataCurator', 'dcite:DataManager', 'dcite:FormalAnalysis', 'dcite:Investigation', 'dcite:Maintainer', 'dcite:Methodology', 'dcite:ProjectLeader', 'dcite:ProjectManager', 'dcite:ProjectMember', 'dcite:Researcher', 'dcite:Software', 'dcite:Validation', 'dcite:Visualization'], 'schemaKey': 'Person', 'identifier': '0000-0003-0161-4007', 'affiliation': [{'name': 'Department of Neurosurgery, Cedars-Sinai Medical Center, Los Angeles, CA, USA', 'schemaKey': 'Affiliation', 'includeInCitation': False}], 'includeInCitation': True}, {'name': 'Liang, Dehua', 'email': 'liang134@mail.chapman.edu', 'roleName': ['dcite:Author', 'dcite:Methodology', 'dcite:ProjectMember', 'dcite:Software', 'dcite:Validation'], 'schemaKey': 'Person', 'affiliation': [{'name': 'Institute for Interdisciplinary Brain and Behavioral Sciences, Crean College of Health and Behavioral Sciences, Schmid College of Science and Technology, Chapman University, Orange, CA, USA', 'schemaKey': 'Affiliation', 'includeInCitation': False}], 'includeInCitation': True}, {'name': 'Schjetnan, Andrea Gomez Palacio', 'email': 'Andrea.Schjetan@uhnresearch.ca', 'roleName': ['dcite:Author', 'dcite:DataCollector', 'dcite:ProjectMember', 'dcite:Validation'], 'schemaKey': 'Person', 'identifier': '0000-0002-4319-7689', 'affiliation': [{'name': 'Krembil Brain Institute, Toronto Western Hospital, Toronto, Canada', 'schemaKey': 'Affiliation', 'includeInCitation': False}], 'includeInCitation': True}, {'name': 'Carlson, April', 'email': 'april.carlson@tufts.edu', 'roleName': ['dcite:Author', 'dcite:DataCurator', 'dcite:ProjectMember', 'dcite:Validation'], 'schemaKey': 'Person', 'identifier': '0000-0002-9207-7069', 'affiliation': [{'name': 'Department of Neurosurgery, Cedars-Sinai Medical Center, Los Angeles, CA, USA', 'schemaKey': 'Affiliation', 'includeInCitation': False}], 'includeInCitation': True}, {'name': 'Faraut, Mailys', 'email': 'mailyscm.faraut@gmail.com', 'roleName': ['dcite:Author', 'dcite:DataCollector', 'dcite:ProjectMember', 'dcite:Validation'], 'schemaKey': 'Person', 'affiliation': [{'name': 'Department of Neurosurgery, Cedars-Sinai Medical Center, Los Angeles, CA, USA', 'schemaKey': 'Affiliation', 'includeInCitation': False}], 'includeInCitation': True}, {'name': 'Chung, Jeffrey M.', 'email': 'Jeffrey.Chung@cshs.org', 'roleName': ['dcite:Author', 'dcite:ProjectMember', 'dcite:Validation'], 'schemaKey': 'Person', 'affiliation': [{'name': 'Department of Neurology, Cedars-Sinai Medical Center, Los Angeles, CA, USA', 'schemaKey': 'Affiliation', 'includeInCitation': False}], 'includeInCitation': True}, {'name': 'Reed, Chrystal M.', 'email': 'Chrystal.Reed@csmc.edu', 'roleName': ['dcite:Author', 'dcite:ProjectMember', 'dcite:Validation'], 'schemaKey': 'Person', 'affiliation': [{'name': 'Department of Neurology, Cedars-Sinai Medical Center, Los Angeles, CA, USA', 'schemaKey': 'Affiliation', 'includeInCitation': False}], 'includeInCitation': True}, {'name': 'Dichter, Ben', 'email': 'ben.dichter@gmail.com', 'roleName': ['dcite:Author', 'dcite:Software', 'dcite:ProjectMember', 'dcite:Validation'], 'schemaKey': 'Person', 'affiliation': [{'name': 'Biological Systems & Engineering Division, Lawrence Berkeley National Laboratory, Berkeley, CA, USA', 'schemaKey': 'Affiliation', 'includeInCitation': False}, {'name': 'Department of Neurosurgery, Stanford University, Stanford, CA, USA', 'schemaKey': 'Affiliation', 'includeInCitation': False}], 'includeInCitation': True}, {'name': 'Maoz, Uri', 'email': 'maoz.uri@gmail.com', 'roleName': ['dcite:Author', 'dcite:Conceptualization', 'dcite:ProjectMember', 'dcite:Validation'], 'schemaKey': 'Person', 'affiliation': [{'name': 'Institute for Interdisciplinary Brain and Behavioral Sciences, Crean College of Health and Behavioral Sciences, Schmid College of Science and Technology, Chapman University, Orange, CA, USA', 'schemaKey': 'Affiliation', 'includeInCitation': False}, {'name': 'Division of Biology and Biological Engineering, California Institute of Technology, Pasadena, CA, USA', 'schemaKey': 'Affiliation', 'includeInCitation': False}], 'includeInCitation': True}, {'name': 'Kalia, Suneil K.', 'email': 'suneil.kalia@uhn.ca', 'roleName': ['dcite:Author', 'dcite:ProjectMember', 'dcite:Validation'], 'schemaKey': 'Person', 'affiliation': [{'name': 'Division of Neurosurgery, Department of Surgery, University of Toronto, Toronto, Canada', 'schemaKey': 'Affiliation', 'includeInCitation': False}, {'name': 'Krembil Brain Institute, Toronto Western Hospital, Toronto, Canada', 'schemaKey': 'Affiliation', 'includeInCitation': False}], 'includeInCitation': True}, {'name': 'Valiante, Taufik A.', 'email': 'Taufik.Valiante@uhn.ca', 'roleName': ['dcite:Author', 'dcite:ProjectMember', 'dcite:Validation'], 'schemaKey': 'Person', 'affiliation': [{'name': 'Krembil Brain Institute, Toronto Western Hospital, Toronto, Canada', 'schemaKey': 'Affiliation', 'includeInCitation': False}, {'name': 'Division of Neurosurgery, Department of Surgery, University of Toronto, Toronto, Canada', 'schemaKey': 'Affiliation', 'includeInCitation': False}], 'includeInCitation': True}, {'name': 'Mamelak, Adam N.', 'email': 'Adam.Mamelak@cshs.org', 'roleName': ['dcite:Author', 'dcite:ProjectMember', 'dcite:Validation'], 'schemaKey': 'Person', 'affiliation': [{'name': 'Department of Neurosurgery, Cedars-Sinai Medical Center, Los Angeles, CA, USA', 'schemaKey': 'Affiliation', 'includeInCitation': False}], 'includeInCitation': True}, {'name': 'Rutishauser, Ueli', 'email': 'Ueli.Rutishauser@cshs.org', 'roleName': ['dcite:Author', 'dcite:Conceptualization', 'dcite:FundingAcquisition', 'dcite:ProjectMember', 'dcite:Resources', 'dcite:Software', 'dcite:Supervision', 'dcite:Validation'], 'schemaKey': 'Person', 'identifier': '0000-0002-9207-7069', 'affiliation': [{'name': 'Department of Neurosurgery, Cedars-Sinai Medical Center, Los Angeles, CA, USA', 'schemaKey': 'Affiliation', 'includeInCitation': False}, {'name': 'Department of Neurology, Cedars-Sinai Medical Center, Los Angeles, CA, USA', 'schemaKey': 'Affiliation', 'includeInCitation': False}, {'name': 'Division of Biology and Biological Engineering, California Institute of Technology, Pasadena, CA, USA', 'schemaKey': 'Affiliation', 'includeInCitation': False}, {'name': 'Computational and Neural Systems Program, California Institute of Technology, Pasadena, CA, USA', 'schemaKey': 'Affiliation', 'includeInCitation': False}, {'name': 'Center for Neural Science and Medicine, Department of Biomedical Science, Cedars-Sinai Medical Center, Los Angeles, CA, USA', 'schemaKey': 'Affiliation', 'includeInCitation': False}], 'includeInCitation': True}, {'name': 'National Institute of Neurological Disorders and Stroke', 'roleName': ['dcite:Sponsor'], 'schemaKey': 'Organization', 'awardNumber': 'U01NS103792', 'contactPoint': [], 'includeInCitation': False}, {'name': 'National Science Foundation', 'roleName': ['dcite:Sponsor'], 'schemaKey': 'Organization', 'awardNumber': '1554105', 'contactPoint': [], 'includeInCitation': False}, {'name': 'National Institute of Mental Health', 'roleName': ['dcite:Sponsor'], 'schemaKey': 'Organization', 'awardNumber': 'R01MH110831', 'contactPoint': [], 'includeInCitation': False}, {'name': 'McKnight Endowment for Neuroscience', 'roleName': ['dcite:Sponsor'], 'schemaKey': 'Organization', 'contactPoint': [], 'includeInCitation': False}, {'name': 'NARSAD Young Investigator grant from the Brain & Behavior Research Foundation', 'roleName': ['dcite:Sponsor'], 'schemaKey': 'Organization', 'contactPoint': [], 'includeInCitation': False}, {'name': 'Kavli Foundation', 'roleName': ['dcite:Sponsor'], 'schemaKey': 'Organization', 'contactPoint': [], 'includeInCitation': False}, {'name': 'BRAIN initiative', 'roleName': ['dcite:Sponsor'], 'schemaKey': 'Organization', 'awardNumber': 'U19NS104590', 'contactPoint': [], 'includeInCitation': False}]
description: A challenge for data sharing in systems neuroscience is the multitude of different data formats used. Neurodata Without Borders: Neurophysiology 2.0 (NWB:N) has emerged as a standardized data format for the storage of cellular-level data together with meta-data, stimulus information, and behavior. A key next step to facilitate NWB:N adoption is to provide easy to use processing pipelines to import/export data from/to NWB:N. Here, we present a NWB-formatted dataset of 1863 single neurons recorded from the medial temporal lobes of 59 human subjects undergoing intracranial monitoring while they performed a recognition memory task. We provide code to analyze and export/import stimuli, behavior, and electrophysiological recordings to/from NWB in both MATLAB and Python. The data files are NWB:N compliant, which affords interoperability between programming languages and operating systems. This combined data and code release is a case study for how to utilize NWB:N for human single-neuron recordings and enables easy re-use of this hard-to-obtain data for both teaching and research on the mechanisms of human memory.
assetsSummary: {'species': [{'name': 'Human', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9606'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 6197474020, 'numberOfFiles': 87, 'numberOfSubjects': 59, 'variableMeasured': ['Units', 'ElectrodeGroup'], 'measurementTechnique': [{'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000004 has 5 NWB files.
1 of these NWB files are of type 1.
1 of these NWB files are of type 2.
1 of these NWB files are of type 3.
1 of these NWB files are of type 4.
1 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/events (AnnotationSeries)  The events coorespond to the TTL markers for each trial. For the learning trials, the TTL markers 
              are the following: 55 = start of the experiment, 1 = stimulus ON, 2 = stimulus OFF, 3 = Question Screen Onset [“Is this an animal?”], 
              20 = Yes (21 = NO) during learning, 6 = End of Delay after Response, 66 = End of Experiment. For the recognition trials, 
              the TTL markers are the following: 55 = start of experiment, 1 = stimulus ON, 2 = stimulus OFF, 3 = Question Screen Onset [“Have you seen this image before?”], 
              31:36 = Confidence (Yes vs. No) response [31 (new, confident), 32 (new, probably), 33 (new, guess), 34 (old, guess), 
              35 (old, probably), 36 (old, confident)], 66 = End of Experiment
  Group /acquisition/experiment_ids (TimeSeries) The experiment_ids coorespond to the encoding (i.e., learning) or recogniton trials. The learning trials are demarcated by: 80. The recognition trials are demarcated by: 81. 
  file_create_date: ['2020-05-26T19:08:23.826535-07:00']
  data_collection: learning: 80, recognition: 81
  Group /general/devices/Neuralynx-cheetah (Device) 
  experiment_description: The data contained within this file describes a new/old recogntion task performed in patients with intractable epilepsy implanted with depth electrodes and Behnke-Fried microwires in the human Medical Temporal Lobe (MTL).
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-1 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-1/device (Device) 
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-13 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-13/device (Device) 
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-14 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-14/device (Device) 
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-15 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-15/device (Device) 
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-16 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-16/device (Device) 
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-17 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-17/device (Device) 
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-18 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-18/device (Device) 
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-19 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-19/device (Device) 
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-2 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-2/device (Device) 
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-20 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-20/device (Device) 
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-22 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-22/device (Device) 
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-23 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-23/device (Device) 
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-24 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-24/device (Device) 
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-3 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-3/device (Device) 
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-4 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-4/device (Device) 
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-5 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-5/device (Device) 
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-6 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-6/device (Device) 
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-8 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-8/device (Device) 
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (18,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (18,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (18,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (18,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (18,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (18,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/origChannel (VectorData) The original channel ID for the channel | shape = (18,) | dtype = uint16
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (18,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (18,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (18,) | dtype = float64
  institution: Hunigton Memorial Hospital
  keywords: ['Intracranial Recordings' 'Intractable Epilepsy' 'Single-Unit Recordings'
   'Cognitive Neuroscience' 'Learning' 'Memory' 'Neurosurgery']
  lab: Rutishauser
  related_publications: ['Faraut et al. 2018, Scientific Data; Rutishauser et al. 2015, Nat Neurosci;']
  Group /general/subject (Subject) 
  identifier: H10_7
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/category_name (VectorData) The Category Name of the Stimulus | shape = (200,) | dtype = object
  Dataset /intervals/trials/delay1_time (VectorData) The Time when Delay1 is Off | shape = (200,) | dtype = float64
  Dataset /intervals/trials/delay2_time (VectorData) The Time when Delay2 is Off | shape = (200,) | dtype = float64
  Dataset /intervals/trials/external_image_file (VectorData) The File Path to the Stimulus | shape = (200,) | dtype = object
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (200,) | dtype = int32
  Dataset /intervals/trials/new_old_labels_recog (VectorData) The Ground truth Labels for New or Old Stimulus. 0 == Old Stimuli 
                              (presented during the learning phase), 1 = New Stimuli (not seen )'during learning phase | shape = (200,) | dtype = object
  Dataset /intervals/trials/response_time (VectorData) The Response Time for each Stimulus | shape = (200,) | dtype = float64
  Dataset /intervals/trials/response_value (VectorData) The Response for Each Stimulus | shape = (200,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (200,) | dtype = float64
  Dataset /intervals/trials/stimCategory (VectorData) The Category ID of the Stimulus | shape = (200,) | dtype = uint8
  Dataset /intervals/trials/stim_off_time (VectorData) The Time when the Stimulus is Off | shape = (200,) | dtype = float64
  Dataset /intervals/trials/stim_on_time (VectorData) The Time when the Stimulus is Shown | shape = (200,) | dtype = float64
  Dataset /intervals/trials/stim_phase (VectorData) Learning/Recognition Phase During the Trial | shape = (200,) | dtype = object
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (200,) | dtype = float64
  session_description: New/Old recognition task for ID: 7. 
  session_start_time: 2006-09-01T00:00:00-07:00
  Group /stimulus/presentation/StimulusPresentation (OpticalSeries) no description
  timestamps_reference_time: 2006-09-01T00:00:00-07:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/IsolationDist (VectorData) IsolDist | shape = (38,) | dtype = float64
  Dataset /units/SNR (VectorData) SNR | shape = (38,) | dtype = float64
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (38,) | dtype = int32
  Dataset /units/electrodes_index (VectorIndex)  | shape = (38,) | dtype = int32
  Dataset /units/id (ElementIdentifiers)  | shape = (38,) | dtype = int32
  Dataset /units/origClusterID (VectorData) The original cluster id | shape = (38,) | dtype = int32
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (97804,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex)  | shape = (38,) | dtype = int32
  Dataset /units/waveform_mean_encoding (VectorData) The mean waveform for encoding phase. | shape = (38, 256) | dtype = float64
  Dataset /units/waveform_mean_recognition (VectorData) The mean waveform for the recognition phase. | shape = (38, 256) | dtype = float64
  Dataset /units/waveform_mean_sampling_rate (VectorData) The Sampling Rate of Waveform | shape = (38, 1) | dtype = float64


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/events (AnnotationSeries)  The events coorespond to the TTL markers for each trial. For the learning trials, the TTL markers 
              are the following: 55 = start of the experiment, 1 = stimulus ON, 2 = stimulus OFF, 3 = Question Screen Onset [“Is this an animal?”], 
              20 = Yes (21 = NO) during learning, 6 = End of Delay after Response, 66 = End of Experiment. For the recognition trials, 
              the TTL markers are the following: 55 = start of experiment, 1 = stimulus ON, 2 = stimulus OFF, 3 = Question Screen Onset [“Have you seen this image before?”], 
              31:36 = Confidence (Yes vs. No) response [31 (new, confident), 32 (new, probably), 33 (new, guess), 34 (old, guess), 
              35 (old, probably), 36 (old, confident)], 66 = End of Experiment
  Group /acquisition/experiment_ids (TimeSeries) The experiment_ids coorespond to the encoding (i.e., learning) or recogniton trials. The learning trials are demarcated by: 80. The recognition trials are demarcated by: 81. 
  file_create_date: ['2020-05-26T19:08:31.224415-07:00']
  data_collection: learning: 80, recognition: 81
  Group /general/devices/Neuralynx-cheetah (Device) 
  experiment_description: The data contained within this file describes a new/old recogntion task performed in patients with intractable epilepsy implanted with depth electrodes and Behnke-Fried microwires in the human Medical Temporal Lobe (MTL).
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-19 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-19/device (Device) 
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-2 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-2/device (Device) 
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-21 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-21/device (Device) 
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-22 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-22/device (Device) 
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-3 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-3/device (Device) 
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-4 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-4/device (Device) 
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-6 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-6/device (Device) 
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-7 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-7/device (Device) 
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-8 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-8/device (Device) 
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (9,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (9,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (9,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (9,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (9,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (9,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/origChannel (VectorData) The original channel ID for the channel | shape = (9,) | dtype = uint16
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (9,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (9,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (9,) | dtype = float64
  institution: Hunigton Memorial Hospital
  keywords: ['Intracranial Recordings' 'Intractable Epilepsy' 'Single-Unit Recordings'
   'Cognitive Neuroscience' 'Learning' 'Memory' 'Neurosurgery']
  lab: Rutishauser
  related_publications: ['Faraut et al. 2018, Scientific Data; Rutishauser et al. 2015, Nat Neurosci;']
  Group /general/subject (Subject) 
  identifier: H11_9
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/category_name (VectorData) The Category Name of the Stimulus | shape = (200,) | dtype = object
  Dataset /intervals/trials/delay1_time (VectorData) The Time when Delay1 is Off | shape = (200,) | dtype = float64
  Dataset /intervals/trials/delay2_time (VectorData) The Time when Delay2 is Off | shape = (200,) | dtype = float64
  Dataset /intervals/trials/external_image_file (VectorData) The File Path to the Stimulus | shape = (200,) | dtype = object
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (200,) | dtype = int32
  Dataset /intervals/trials/new_old_labels_recog (VectorData) The Ground truth Labels for New or Old Stimulus. 0 == Old Stimuli 
                              (presented during the learning phase), 1 = New Stimuli (not seen )'during learning phase | shape = (200,) | dtype = object
  Dataset /intervals/trials/response_time (VectorData) The Response Time for each Stimulus | shape = (200,) | dtype = float64
  Dataset /intervals/trials/response_value (VectorData) The Response for Each Stimulus | shape = (200,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (200,) | dtype = float64
  Dataset /intervals/trials/stimCategory (VectorData) The Category ID of the Stimulus | shape = (200,) | dtype = uint8
  Dataset /intervals/trials/stim_off_time (VectorData) The Time when the Stimulus is Off | shape = (200,) | dtype = float64
  Dataset /intervals/trials/stim_on_time (VectorData) The Time when the Stimulus is Shown | shape = (200,) | dtype = float64
  Dataset /intervals/trials/stim_phase (VectorData) Learning/Recognition Phase During the Trial | shape = (200,) | dtype = object
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (200,) | dtype = float64
  session_description: New/Old recognition task for ID: 9. 
  session_start_time: 2006-11-01T00:00:00-07:00
  Group /stimulus/presentation/StimulusPresentation (OpticalSeries) no description
  timestamps_reference_time: 2006-11-01T00:00:00-07:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/IsolationDist (VectorData) IsolDist | shape = (25,) | dtype = float64
  Dataset /units/SNR (VectorData) SNR | shape = (25,) | dtype = float64
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (25,) | dtype = int32
  Dataset /units/electrodes_index (VectorIndex)  | shape = (25,) | dtype = int32
  Dataset /units/id (ElementIdentifiers)  | shape = (25,) | dtype = int32
  Dataset /units/origClusterID (VectorData) The original cluster id | shape = (25,) | dtype = int32
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (40835,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex)  | shape = (25,) | dtype = int32
  Dataset /units/waveform_mean_encoding (VectorData) The mean waveform for encoding phase. | shape = (25, 256) | dtype = float64
  Dataset /units/waveform_mean_recognition (VectorData) The mean waveform for the recognition phase. | shape = (25, 256) | dtype = float64
  Dataset /units/waveform_mean_sampling_rate (VectorData) The Sampling Rate of Waveform | shape = (25, 1) | dtype = float64


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/events (AnnotationSeries)  The events coorespond to the TTL markers for each trial. For the learning trials, the TTL markers 
              are the following: 55 = start of the experiment, 1 = stimulus ON, 2 = stimulus OFF, 3 = Question Screen Onset [“Is this an animal?”], 
              20 = Yes (21 = NO) during learning, 6 = End of Delay after Response, 66 = End of Experiment. For the recognition trials, 
              the TTL markers are the following: 55 = start of experiment, 1 = stimulus ON, 2 = stimulus OFF, 3 = Question Screen Onset [“Have you seen this image before?”], 
              31:36 = Confidence (Yes vs. No) response [31 (new, confident), 32 (new, probably), 33 (new, guess), 34 (old, guess), 
              35 (old, probably), 36 (old, confident)], 66 = End of Experiment
  Group /acquisition/experiment_ids (TimeSeries) The experiment_ids coorespond to the encoding (i.e., learning) or recogniton trials. The learning trials are demarcated by: 83. The recognition trials are demarcated by: 84. 
  file_create_date: ['2020-05-26T19:08:36.250776-07:00']
  data_collection: learning: 83, recognition: 84
  Group /general/devices/Neuralynx-cheetah (Device) 
  experiment_description: The data contained within this file describes a new/old recogntion task performed in patients with intractable epilepsy implanted with depth electrodes and Behnke-Fried microwires in the human Medical Temporal Lobe (MTL).
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-11 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-11/device (Device) 
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-12 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-12/device (Device) 
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-13 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-13/device (Device) 
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-15 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-15/device (Device) 
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-3 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-3/device (Device) 
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-4 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-4/device (Device) 
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-5 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-5/device (Device) 
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-6 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-6/device (Device) 
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-7 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-7/device (Device) 
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (9,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (9,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (9,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (9,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (9,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (9,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/origChannel (VectorData) The original channel ID for the channel | shape = (9,) | dtype = uint16
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (9,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (9,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (9,) | dtype = float64
  institution: Hunigton Memorial Hospital
  keywords: ['Intracranial Recordings' 'Intractable Epilepsy' 'Single-Unit Recordings'
   'Cognitive Neuroscience' 'Learning' 'Memory' 'Neurosurgery']
  lab: Rutishauser
  related_publications: ['Faraut et al. 2018, Scientific Data; Rutishauser et al. 2015, Nat Neurosci;']
  Group /general/subject (Subject) 
  identifier: H14_17
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/category_name (VectorData) The Category Name of the Stimulus | shape = (200,) | dtype = object
  Dataset /intervals/trials/delay1_time (VectorData) The Time when Delay1 is Off | shape = (200,) | dtype = float64
  Dataset /intervals/trials/delay2_time (VectorData) The Time when Delay2 is Off | shape = (200,) | dtype = float64
  Dataset /intervals/trials/external_image_file (VectorData) The File Path to the Stimulus | shape = (200,) | dtype = object
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (200,) | dtype = int32
  Dataset /intervals/trials/new_old_labels_recog (VectorData) The Ground truth Labels for New or Old Stimulus. 0 == Old Stimuli 
                              (presented during the learning phase), 1 = New Stimuli (not seen )'during learning phase | shape = (200,) | dtype = object
  Dataset /intervals/trials/response_time (VectorData) The Response Time for each Stimulus | shape = (200,) | dtype = float64
  Dataset /intervals/trials/response_value (VectorData) The Response for Each Stimulus | shape = (200,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (200,) | dtype = float64
  Dataset /intervals/trials/stimCategory (VectorData) The Category ID of the Stimulus | shape = (200,) | dtype = uint8
  Dataset /intervals/trials/stim_off_time (VectorData) The Time when the Stimulus is Off | shape = (200,) | dtype = float64
  Dataset /intervals/trials/stim_on_time (VectorData) The Time when the Stimulus is Shown | shape = (200,) | dtype = float64
  Dataset /intervals/trials/stim_phase (VectorData) Learning/Recognition Phase During the Trial | shape = (200,) | dtype = object
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (200,) | dtype = float64
  session_description: New/Old recognition task for ID: 17. 
  session_start_time: 2007-06-01T00:00:00-07:00
  Group /stimulus/presentation/StimulusPresentation (OpticalSeries) no description
  timestamps_reference_time: 2007-06-01T00:00:00-07:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/IsolationDist (VectorData) IsolDist | shape = (23,) | dtype = float64
  Dataset /units/SNR (VectorData) SNR | shape = (23,) | dtype = float64
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (23,) | dtype = int32
  Dataset /units/electrodes_index (VectorIndex)  | shape = (23,) | dtype = int32
  Dataset /units/id (ElementIdentifiers)  | shape = (23,) | dtype = int32
  Dataset /units/origClusterID (VectorData) The original cluster id | shape = (23,) | dtype = int32
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (111625,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex)  | shape = (23,) | dtype = int32
  Dataset /units/waveform_mean_encoding (VectorData) The mean waveform for encoding phase. | shape = (23, 256) | dtype = float64
  Dataset /units/waveform_mean_recognition (VectorData) The mean waveform for the recognition phase. | shape = (23, 256) | dtype = float64
  Dataset /units/waveform_mean_sampling_rate (VectorData) The Sampling Rate of Waveform | shape = (23, 1) | dtype = float64


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/events (AnnotationSeries)  The events coorespond to the TTL markers for each trial. For the learning trials, the TTL markers 
              are the following: 55 = start of the experiment, 1 = stimulus ON, 2 = stimulus OFF, 3 = Question Screen Onset [“Is this an animal?”], 
              20 = Yes (21 = NO) during learning, 6 = End of Delay after Response, 66 = End of Experiment. For the recognition trials, 
              the TTL markers are the following: 55 = start of experiment, 1 = stimulus ON, 2 = stimulus OFF, 3 = Question Screen Onset [“Have you seen this image before?”], 
              31:36 = Confidence (Yes vs. No) response [31 (new, confident), 32 (new, probably), 33 (new, guess), 34 (old, guess), 
              35 (old, probably), 36 (old, confident)], 66 = End of Experiment
  Group /acquisition/experiment_ids (TimeSeries) The experiment_ids coorespond to the encoding (i.e., learning) or recogniton trials. The learning trials are demarcated by: 80. The recognition trials are demarcated by: 81. 
  file_create_date: ['2020-05-26T19:08:43.867295-07:00']
  data_collection: learning: 80, recognition: 81
  Group /general/devices/Neuralynx-cheetah (Device) 
  experiment_description: The data contained within this file describes a new/old recogntion task performed in patients with intractable epilepsy implanted with depth electrodes and Behnke-Fried microwires in the human Medical Temporal Lobe (MTL).
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-1 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-1/device (Device) 
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-10 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-10/device (Device) 
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-11 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-11/device (Device) 
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-13 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-13/device (Device) 
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-15 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-15/device (Device) 
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-3 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-3/device (Device) 
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-4 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-4/device (Device) 
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-5 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-5/device (Device) 
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-6 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-6/device (Device) 
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-7 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-7/device (Device) 
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (10,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (10,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (10,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (10,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (10,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (10,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/origChannel (VectorData) The original channel ID for the channel | shape = (10,) | dtype = uint16
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (10,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (10,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (10,) | dtype = float64
  institution: Hunigton Memorial Hospital
  keywords: ['Intracranial Recordings' 'Intractable Epilepsy' 'Single-Unit Recordings'
   'Cognitive Neuroscience' 'Learning' 'Memory' 'Neurosurgery']
  lab: Rutishauser
  related_publications: ['Faraut et al. 2018, Scientific Data; Rutishauser et al. 2015, Nat Neurosci;']
  Group /general/subject (Subject) 
  identifier: H14_18
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/category_name (VectorData) The Category Name of the Stimulus | shape = (150,) | dtype = object
  Dataset /intervals/trials/delay1_time (VectorData) The Time when Delay1 is Off | shape = (150,) | dtype = float64
  Dataset /intervals/trials/delay2_time (VectorData) The Time when Delay2 is Off | shape = (150,) | dtype = float64
  Dataset /intervals/trials/external_image_file (VectorData) The File Path to the Stimulus | shape = (150,) | dtype = object
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (150,) | dtype = int32
  Dataset /intervals/trials/new_old_labels_recog (VectorData) The Ground truth Labels for New or Old Stimulus. 0 == Old Stimuli 
                              (presented during the learning phase), 1 = New Stimuli (not seen )'during learning phase | shape = (150,) | dtype = object
  Dataset /intervals/trials/response_time (VectorData) The Response Time for each Stimulus | shape = (150,) | dtype = float64
  Dataset /intervals/trials/response_value (VectorData) The Response for Each Stimulus | shape = (150,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (150,) | dtype = float64
  Dataset /intervals/trials/stimCategory (VectorData) The Category ID of the Stimulus | shape = (150,) | dtype = uint8
  Dataset /intervals/trials/stim_off_time (VectorData) The Time when the Stimulus is Off | shape = (150,) | dtype = float64
  Dataset /intervals/trials/stim_on_time (VectorData) The Time when the Stimulus is Shown | shape = (150,) | dtype = float64
  Dataset /intervals/trials/stim_phase (VectorData) Learning/Recognition Phase During the Trial | shape = (150,) | dtype = object
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (150,) | dtype = float64
  session_description: New/Old recognition task for ID: 18. 
  session_start_time: 2007-06-01T00:00:00-07:00
  Group /stimulus/presentation/StimulusPresentation (OpticalSeries) no description
  timestamps_reference_time: 2007-06-01T00:00:00-07:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/IsolationDist (VectorData) IsolDist | shape = (33,) | dtype = float64
  Dataset /units/SNR (VectorData) SNR | shape = (33,) | dtype = float64
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (33,) | dtype = int32
  Dataset /units/electrodes_index (VectorIndex)  | shape = (33,) | dtype = int32
  Dataset /units/id (ElementIdentifiers)  | shape = (33,) | dtype = int32
  Dataset /units/origClusterID (VectorData) The original cluster id | shape = (33,) | dtype = int32
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (118870,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex)  | shape = (33,) | dtype = int32
  Dataset /units/waveform_mean_encoding (VectorData) The mean waveform for encoding phase. | shape = (33, 256) | dtype = float64
  Dataset /units/waveform_mean_recognition (VectorData) The mean waveform for the recognition phase. | shape = (33, 256) | dtype = float64
  Dataset /units/waveform_mean_sampling_rate (VectorData) The Sampling Rate of Waveform | shape = (33, 1) | dtype = float64


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  Group /acquisition/events (AnnotationSeries)  The events coorespond to the TTL markers for each trial. For the learning trials, the TTL markers 
              are the following: 55 = start of the experiment, 1 = stimulus ON, 2 = stimulus OFF, 3 = Question Screen Onset [“Is this an animal?”], 
              20 = Yes (21 = NO) during learning, 6 = End of Delay after Response, 66 = End of Experiment. For the recognition trials, 
              the TTL markers are the following: 55 = start of experiment, 1 = stimulus ON, 2 = stimulus OFF, 3 = Question Screen Onset [“Have you seen this image before?”], 
              31:36 = Confidence (Yes vs. No) response [31 (new, confident), 32 (new, probably), 33 (new, guess), 34 (old, guess), 
              35 (old, probably), 36 (old, confident)], 66 = End of Experiment
  Group /acquisition/experiment_ids (TimeSeries) The experiment_ids coorespond to the encoding (i.e., learning) or recogniton trials. The learning trials are demarcated by: 83. The recognition trials are demarcated by: 84. 
  file_create_date: ['2020-05-26T19:08:53.143469-07:00']
  data_collection: learning: 83, recognition: 84
  Group /general/devices/Neuralynx-cheetah (Device) 
  experiment_description: The data contained within this file describes a new/old recogntion task performed in patients with intractable epilepsy implanted with depth electrodes and Behnke-Fried microwires in the human Medical Temporal Lobe (MTL).
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-17 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-17/device (Device) 
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-18 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-18/device (Device) 
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-19 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-19/device (Device) 
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-20 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-20/device (Device) 
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-21 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-21/device (Device) 
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-22 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-22/device (Device) 
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-29 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-cheetah-microwires-29/device (Device) 
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (7,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (7,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (7,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (7,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (7,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (7,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/origChannel (VectorData) The original channel ID for the channel | shape = (7,) | dtype = uint16
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (7,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (7,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (7,) | dtype = float64
  institution: Hunigton Memorial Hospital
  keywords: ['Intracranial Recordings' 'Intractable Epilepsy' 'Single-Unit Recordings'
   'Cognitive Neuroscience' 'Learning' 'Memory' 'Neurosurgery']
  lab: Rutishauser
  related_publications: ['Faraut et al. 2018, Scientific Data; Rutishauser et al. 2015, Nat Neurosci;']
  Group /general/subject (Subject) 
  identifier: H15_21
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/category_name (VectorData) The Category Name of the Stimulus | shape = (150,) | dtype = object
  Dataset /intervals/trials/delay1_time (VectorData) The Time when Delay1 is Off | shape = (150,) | dtype = float64
  Dataset /intervals/trials/delay2_time (VectorData) The Time when Delay2 is Off | shape = (150,) | dtype = float64
  Dataset /intervals/trials/external_image_file (VectorData) The File Path to the Stimulus | shape = (150,) | dtype = object
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (150,) | dtype = int32
  Dataset /intervals/trials/new_old_labels_recog (VectorData) The Ground truth Labels for New or Old Stimulus. 0 == Old Stimuli 
                              (presented during the learning phase), 1 = New Stimuli (not seen )'during learning phase | shape = (150,) | dtype = object
  Dataset /intervals/trials/response_time (VectorData) The Response Time for each Stimulus | shape = (150,) | dtype = float64
  Dataset /intervals/trials/response_value (VectorData) The Response for Each Stimulus | shape = (150,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (150,) | dtype = float64
  Dataset /intervals/trials/stimCategory (VectorData) The Category ID of the Stimulus | shape = (150,) | dtype = uint8
  Dataset /intervals/trials/stim_off_time (VectorData) The Time when the Stimulus is Off | shape = (150,) | dtype = float64
  Dataset /intervals/trials/stim_on_time (VectorData) The Time when the Stimulus is Shown | shape = (150,) | dtype = float64
  Dataset /intervals/trials/stim_phase (VectorData) Learning/Recognition Phase During the Trial | shape = (150,) | dtype = object
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (150,) | dtype = float64
  session_description: New/Old recognition task for ID: 21. 
  session_start_time: 2007-09-01T00:00:00-07:00
  Group /stimulus/presentation/StimulusPresentation (OpticalSeries) no description
  timestamps_reference_time: 2007-09-01T00:00:00-07:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/IsolationDist (VectorData) IsolDist | shape = (14,) | dtype = float64
  Dataset /units/SNR (VectorData) SNR | shape = (14,) | dtype = float64
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (14,) | dtype = int32
  Dataset /units/electrodes_index (VectorIndex)  | shape = (14,) | dtype = int32
  Dataset /units/id (ElementIdentifiers)  | shape = (14,) | dtype = int32
  Dataset /units/origClusterID (VectorData) The original cluster id | shape = (14,) | dtype = int32
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (104841,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex)  | shape = (14,) | dtype = int32
  Dataset /units/waveform_mean_encoding (VectorData) The mean waveform for encoding phase. | shape = (14, 256) | dtype = float64
  Dataset /units/waveform_mean_recognition (VectorData) The mean waveform for the recognition phase. | shape = (14, 256) | dtype = float64
  Dataset /units/waveform_mean_sampling_rate (VectorData) The Sampling Rate of Waveform | shape = (14, 1) | dtype = float64
