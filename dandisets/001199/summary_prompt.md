
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001199/draft
name: Neural Pathways Modulation in the Anesthetized Rat Elicited by Trials of Transcranial Focused Ultrasound Stimulation
contributor: [{'name': 'Gao, Huan', 'email': 'huangao@andrew.cmu.edu', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'He, Bin', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Ramachandran, Sandhya', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Yu, Kai', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Carnegie Mellon University', 'roleName': ['dcite:Affiliation'], 'schemaKey': 'Organization', 'includeInCitation': False}, {'name': 'NIH NS124564', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'includeInCitation': False}, {'name': 'NIH EB029354', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'includeInCitation': False}, {'name': 'NIH NS13106', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'includeInCitation': False}]
description: In these recordings, we recorded neuronal activities from cortical-thalamocortical (CTC) pathway, including the somatosensory cortex (S1) and posteromedial complex (POm) of the thalamus responded to different Pulse Repetition Frequencies (PRFs ) or Pulse Durations (PDs) and Pressure Levels of transcranial ultrasound focused stimulation (tFUS) using a 128-element transducer to stimulate either at S1or PoM.  Recordings for S1 are taken using 64-channel Cambridge or Neuronexus electrodes and recordings for POm are taken using 32-channel Nueronexus electrodes. Ultrasound stimulation is delivered every 2.5 seconds and each recording has 500 trials. The Ultrasound Duration (UD) and pressure level used in each recording is 67ms. The PRFs, PDs and pressure levels for each recording can be found in the identifier field. For example, in BH596_3000_200_67_10, the PRF is 3000Hz, PD is 200us and pressure level is 10V. 
assetsSummary: {'species': [{'name': 'Rattus norvegicus - Norway rat', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10116'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 133497360, 'numberOfFiles': 74, 'numberOfSubjects': 3, 'variableMeasured': ['ElectrodeGroup', 'Units'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 001199 has 96 NWB files.
96 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2024-09-30T18:23:32.208000-04:00']
  data_collection: No tFUS
  Group /general/devices/array (Device) A1x64-Edge-6mm-22.5-177 with z-coating
  Group /general/extracellular_ephys/electrodes (DynamicTable) all electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) my description | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) my description | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) my description | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (64,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) my description | shape = (64,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) my description | shape = (64,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) my description | shape = (64,) | dtype = float32
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) my description | shape = (64,) | dtype = float32
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) my description | shape = (64,) | dtype = float64
  Group /general/extracellular_ephys/shank1 (ElectrodeGroup) electrode group for shank1
  Group /general/extracellular_ephys/shank1/device (Device) A1x64-Edge-6mm-22.5-177 with z-coating
  institution: Carnegie Mellon University
  notes: Recording:S1; stim at:S1
  stimulus: intervals contains each tFUS trial start and end timestamps
  Group /general/subject (Subject) 
  identifier: BH590_BASELINE_NZ
  Group /intervals/trials (TimeIntervals) each trial start and end timestamps
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (400,) | dtype = int64
  Dataset /intervals/trials/start_time (VectorData) start time of trial | shape = (400,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) end time of each trial | shape = (400,) | dtype = float64
  session_description: Neural Spikes for neural pathways to tFUS
  session_start_time: 2024-08-16T16:54:00.000000-04:00
  timestamps_reference_time: 2024-09-30T18:23:31.808000-04:00
  Group /units (Units) units table
  Dataset /units/celltype_label (VectorData) label 1 = RSU, label 2 = FSU | shape = (10,) | dtype = float64
  Dataset /units/id (ElementIdentifiers)  | shape = (10,) | dtype = int64
  Dataset /units/spike_times (VectorData) /units/spike_times | shape = (82155,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) indexes data | shape = (10,) | dtype = uint64
