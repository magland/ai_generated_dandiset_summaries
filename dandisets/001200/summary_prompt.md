
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001200/draft
name: Neural Spiking Data in Rats Responding to Optogenetic Stimulation and Transcranial Focused Ultrasound Stimulation in Neural Pathway
contributor: [{'name': 'Gao, Huan', 'email': 'huangao@andrew.cmu.edu', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Ramachandran, Sandhya', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'He, Bin', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Yu, Kai', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Carnegie Mellon University', 'roleName': ['dcite:Affiliation'], 'schemaKey': 'Organization', 'includeInCitation': False}, {'name': 'NIH NS13106', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'includeInCitation': False}, {'name': 'NIH EB029354', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'includeInCitation': False}, {'name': 'NIH NS124564', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'includeInCitation': False}]
description: In these recordings, we stimulate rats that were injected with AAV virus to optogenetically tag for CaMKII or PV to distinguish between excitatory pyramidal neurons and inhibitory interneurons in both somatosensory cortex (S1) and posteromedial complex (POm) of the thalamus. We alternate between stimulating them optogenetically in order to tag the neuronal subtype and testing different PRFs (pulse repetition frequencies), pulse durations and pressure levels of ultrasound stimulation using a 128-element random array ultrasound transducer to stimulate the somatosensory cortex. Electrophysiological recordings were acquired using 32-channel 64-channel NeuroNexus electrodes inserted into S1 and 32-channel NeuroNexus electrodes inserted into POm. Ultrasound stimulation is delivered every 2.5 seconds with a 10% jitter, and each recording has 500 trials. Optogenetic stimulation was delivered at 150mA of 50ms. The tFUS parameters (PRFs, PDs and pressure levels) for each recording can be found in the identifier field. For example, in BH596_3000_200_67_10_S1_POm,  the PRF is 3000Hz, PD is 200us, pressure level is 10V and stimulation target is POm. 

assetsSummary: {'species': [{'name': 'Rattus norvegicus - Norway rat', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10116'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 19257968, 'numberOfFiles': 50, 'numberOfSubjects': 2, 'variableMeasured': ['Units', 'ElectrodeGroup'], 'measurementTechnique': [{'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 001200 has 54 NWB files.
54 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2024-09-30T19:12:47.747000-04:00']
  data_collection: optical parameters {stim_duration:2ms stim_intensity:mA}
  Group /general/devices/array (Device) A1x64-Edge-6mm-22.5-177 & A1x32-Poly3-10mm-50-177-A32
  Group /general/extracellular_ephys/electrodes (DynamicTable) all electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) my description | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) my description | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) my description | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (32,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) my description | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) my description | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) my description | shape = (32,) | dtype = float32
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) my description | shape = (32,) | dtype = float32
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) my description | shape = (32,) | dtype = float64
  Group /general/extracellular_ephys/shank1 (ElectrodeGroup) electrode group for shank1
  Group /general/extracellular_ephys/shank1/device (Device) A1x64-Edge-6mm-22.5-177 & A1x32-Poly3-10mm-50-177-A32
  institution: Carnegie Mellon University
  notes: VirusPV;Recording:S1; stim at:S1
  Group /general/optogenetics/OptogeneticStimulusSite (OptogeneticStimulusSite) 
  Group /general/optogenetics/OptogeneticStimulusSite/device (Device) A1x64-Edge-6mm-22.5-177 & A1x32-Poly3-10mm-50-177-A32
  stimulus: intervals contains each tFUS trial start and end timestamps
  Group /general/subject (Subject) 
  identifier: BH585_50ms_130mA_S1
  Group /intervals/trials (TimeIntervals) each trial start and end timestamps
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (300,) | dtype = int64
  Dataset /intervals/trials/start_time (VectorData) start time of trial | shape = (300,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) end time of each trial | shape = (300,) | dtype = float64
  session_description: Neural Spikes for neural pathways to tFUS
  session_start_time: 2024-09-13T16:35:00.000000-04:00
  timestamps_reference_time: 2024-09-30T19:12:47.347000-04:00
  Group /units (Units) units table
  Dataset /units/celltype_label (VectorData) label 1 = RSU, label 2 = FSU | shape = (8,) | dtype = object
  Dataset /units/id (ElementIdentifiers)  | shape = (8,) | dtype = int64
  Dataset /units/spike_times (VectorData) /units/spike_times | shape = (12495,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) indexes data | shape = (8,) | dtype = uint64
