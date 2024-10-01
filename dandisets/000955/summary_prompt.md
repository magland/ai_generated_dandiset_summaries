
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000955/draft
name: Neural Spiking Data in Rats Responding to Optogenetic Stimulation and Transcranial Focused Ultrasound Stimulation in the Somatosensory Cortex
contributor: [{'name': 'Ramachandran, Sandhya', 'email': 's.ramachandran8@gmail.com', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Gao, Huan', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Yu, Kai', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'He, Bin', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Carnegie Mellon University', 'roleName': ['dcite:Affiliation'], 'schemaKey': 'Organization', 'includeInCitation': False}, {'name': 'NIH NS124564', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'includeInCitation': False}, {'name': 'NIH EB029354', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'includeInCitation': False}, {'name': 'NIH NS131069', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'includeInCitation': False}]
description: In these recordings, we stimulate rats that were injected with AAV virus to optogenetically tag for CaMKII  to distinguish between excitatory pyramidal neurons and inhibitory interneurons. We alternate between stimulating them optogenetically in order to tag the neuronal subtype and testing different PRFs (pulse repetition frequencies) and pulse durations of ultrasound stimulation using a 128-element random array ultrasound transducer to stimulate the somatosensory cortex. Electrophysiological recordings were acquired using 32-channel NeuroNexus electrodes (Model: A1x32-Poly3-10mm-50-177-A32), surgically inserted into the rat brain. Ultrasound stimulation is delivered every 2.5 seconds with a 10% jitter, and each recording has 500 trials. Optogenetic stimulation was delivered at 120A for 10ms. The PRFs tested were 30 Hz, 300 Hz, 1500 Hz, 3000 Hz, and 4500 Hz, with pulse durations including 4, 40, 200, and 400 microseconds, and a 67 millisecond ultrasound duration. 

File Information: All subjects were male Wistar rats. Ultrasound test files are named in the format SubjectName_PRF_PulseDuration_UltrasoundDuration_Voltage. Optogenetics test files are named in the format SubjectName_opto_Current_Duration_OrderWithinUltrasoundPRFtests .Each file contains spike time data with the time series data for the onset of each trial of ultrasound stimulation or optogenetic stimulation.
assetsSummary: {'species': [{'name': 'Rattus norvegicus - Norway rat', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10116'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 10556448, 'numberOfFiles': 11, 'numberOfSubjects': 1, 'variableMeasured': ['Units', 'ElectrodeGroup'], 'measurementTechnique': [{'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000955 has 11 NWB files.
11 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2024-04-02T23:39:02.000000-04:00' '2024-04-02T23:39:07.440000-04:00']
  Group /general/devices/array (Device) A1x32-Poly3-10mm-50-177-Z32
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
  Group /general/extracellular_ephys/shank1/device (Device) A1x32-Poly3-10mm-50-177-Z32
  institution: Carnegie Mellon University
  Group /general/subject (Subject) 
  identifier: BH549_1500_200_67_5
  Group /intervals/trials (TimeIntervals) tFUS stimulation trial onset and offset
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (500,) | dtype = int64
  Dataset /intervals/trials/start_time (VectorData) start time of trial | shape = (500,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) end of each trial | shape = (500,) | dtype = float64
  session_description: Awake S1 Stimulation by tFUS
  session_start_time: 2024-03-31T13:26:33.000000-04:00
  timestamps_reference_time: 2024-03-31T13:26:33.000000-04:00
  Group /units (Units) units table
  Dataset /units/id (ElementIdentifiers)  | shape = (6,) | dtype = int64
  Dataset /units/spike_times (VectorData) /units/spike_times | shape = (24379,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) indexes data | shape = (6,) | dtype = uint64
