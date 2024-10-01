
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000946/draft
name: Neural Pathways Modulation in the Anesthetized Rat Elicited by Trials of Transcranial Focused Ultrasound Stimulation
contributor: [{'name': 'Gao, Huan', 'email': 'huangao@andrew.cmu.edu', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Ramachandran, Sandhya', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'He, Bin', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Yu Kai', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'NIH NS124564', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'includeInCitation': False}, {'name': 'NIH EB029354', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'includeInCitation': False}, {'name': 'Carnegie Mellon University', 'roleName': ['dcite:Affiliation'], 'schemaKey': 'Organization', 'includeInCitation': False}, {'name': 'NIH NS13106', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'includeInCitation': False}]
description: In these recordings, we recorded neuronal activities from cortical-thalamocortical (CTC) pathway, including the somatosensory cortex (S1), motor cortex (M1) and posteromedial complex (PoM) of the thalamus responded to different PRFs (pulse repetition frequencies) or Pulse Durations (PDs) of transcranial ultrasound focused stimulation (tFUS) using a 128-element transducer to stimulate either at S1, M1 or PoM. Also, we tested the neural responses of the auditory cortex (AC) with tFUS targeting at S1. Recordings for each target are taken using 32-channel Neuronexus electrodes. Ultrasound stimulation is delivered every 2.5 seconds and each recording has 500 trials. The ultrasound duration and pressure level used in each recording is 67ms and ~90kPa. The PRFs and PDs for each recording can be found in the identifier field. For example, in BH494_1500_200_67_5, the PRF is 1500Hz and PD is 200us.
Each recording contains two areas (64-channel). The spike time tiling coefficient (STTC) of neurons cross-area and within-area is included in the folders named with STTC.
assetsSummary: {'species': [{'name': 'Rattus norvegicus - Norway rat', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10116'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 64576397240, 'numberOfFiles': 1875, 'numberOfSubjects': 37, 'variableMeasured': ['Units', 'ElectrodeGroup'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000946 has 100 NWB files.
98 of these NWB files are of type 1.
2 of these NWB files are of type 2.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2024-04-04T22:52:49.466000-04:00']
  data_collection: tFUS parameters {PRF:1500Hz PD:200us UD:67ms}
  Group /general/devices/array (Device) A1x32-Poly3-10mm-50-177-A32
  Group /general/extracellular_ephys/electrodes (DynamicTable) all electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) my description | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) my description | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) my description | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (32,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) my description | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) my description | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) my description | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) my description | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) my description | shape = (32,) | dtype = float64
  Group /general/extracellular_ephys/shank1 (ElectrodeGroup) electrode group for shank1
  Group /general/extracellular_ephys/shank1/device (Device) A1x32-Poly3-10mm-50-177-A32
  institution: Carnegie Mellon University
  notes: Recording:M1; stim at:M1
  stimulus: intervals contains each tFUS trial start and end timestamps
  Group /general/subject (Subject) 
  identifier: BH494_1500_200_67_5_MOTOR
  Group /intervals/trials (TimeIntervals) each trial start and end timestamps
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (500,) | dtype = int64
  Dataset /intervals/trials/start_time (VectorData) start time of trial | shape = (500,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) end time of each trial | shape = (500,) | dtype = float64
  session_description: Neural Spikes for neural pathways to tFUS
  session_start_time: ['2023-08-21T13:40:17.000000-04:00']
  timestamps_reference_time: ['2024-04-04T22:52:49.042000-04:00']
  Group /units (Units) units table
  Dataset /units/celltype_label (VectorData) label 1 = RSU, label 2 = FSU | shape = (19,) | dtype = float64
  Dataset /units/id (ElementIdentifiers)  | shape = (19,) | dtype = int64
  Dataset /units/spike_times (VectorData) /units/spike_times | shape = (359781,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) indexes data | shape = (19,) | dtype = uint64


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2024-03-30T18:13:03.335000-04:00']
  Group /general/devices/array (Device) A1x32-Poly3-10mm-50-177-A32
  Group /general/extracellular_ephys/electrodes (DynamicTable) all electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) my description | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) my description | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) my description | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (32,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) my description | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) my description | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) my description | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) my description | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) my description | shape = (32,) | dtype = float64
  Group /general/extracellular_ephys/shank1 (ElectrodeGroup) electrode group for shank1
  Group /general/extracellular_ephys/shank1/device (Device) A1x32-Poly3-10mm-50-177-A32
  institution: Carnegie Mellon University
  notes: recording:S1;stimulation:S1
  Group /general/subject (Subject) 
  identifier: BH494_1500_200_67_5
  Group /intervals/trials (TimeIntervals) trial data and properties
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (500,) | dtype = int64
  Dataset /intervals/trials/start_time (VectorData) start time of trial | shape = (500,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) end of each trial | shape = (500,) | dtype = float64
  session_description: Neural Spikes for neural pathways to tFUS
  session_start_time: ['2023-08-17T13:28:00.000000-04:00']
  timestamps_reference_time: ['2024-03-30T18:13:02.965000-04:00']
  Group /units (Units) units table
  Dataset /units/id (ElementIdentifiers)  | shape = (35,) | dtype = int64
  Dataset /units/spike_times (VectorData) /units/spike_times | shape = (762562,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) indexes data | shape = (35,) | dtype = uint64
