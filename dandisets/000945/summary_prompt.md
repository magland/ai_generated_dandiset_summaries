
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000945/draft
name: Neural Spiking Data in the Awake Rat Somatosensory Cortex Responding to Trials of Transcranial Focused Ultrasound Stimulation
contributor: [{'name': 'Ramachandran, Sandhya', 'email': 's.ramachandran8@gmail.com', 'roleName': ['dcite:ContactPerson', 'dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Gao, Huan', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Yu, Kai', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'He, Bin', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Carnegie Mellon University', 'roleName': ['dcite:Affiliation'], 'schemaKey': 'Organization', 'includeInCitation': False}, {'name': 'NIH NS124564', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'includeInCitation': False}, {'name': 'NIH EB029354', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'includeInCitation': False}, {'name': 'NIH NS131069', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'includeInCitation': False}]
description: In these recordings, we tested different PRFs (pulse repetition frequencies) of ultrasound stimulation using a 128-element random array ultrasound transducer to stimulate the somatosensory cortex of awake head-fixed rats. Chronic electrophysiological recordings were acquired using 32-channel NeuroNexus electrodes (Model: A1x32-Poly3-10mm-50-177-Z32), chronically implanted into the rat brain. Ultrasound stimulation is delivered every 2.5 seconds with a 10% jitter, and each recording has 500 trials. The PRFs tested were 30 Hz, 300 Hz, 1500 Hz, 3000 Hz, and 4500 Hz, each with a 200 microsecond pulse duration and a 67 ms ultrasound duration. Anesthetized files were performed under 2% isoflurane anesthesia for comparison.

File Information
All 10 subjects were male rats, implanted with their chronic electrode at 6 months of age and then recordings taken first at 8-10 months, and then some repeats taken at 12 months. Within each subject's folder are recordings for the different PRFs. Most subjects have 5 recordings within, one for each PRF. Some subjects have duplicate recordings taken a few months after the original ones. A few recordings were not included due to excessive noise in the recordings. Files are named in the format SubjectName_PRF_PulseDuration. Each file contains spike time data with the cell type labels included for each neurons, as well as time series data for the onset of each trial of ultrasound stimulation.
assetsSummary: {'species': [{'name': 'Rattus norvegicus - Norway rat', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10116'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 524086736, 'numberOfFiles': 75, 'numberOfSubjects': 10, 'variableMeasured': ['ElectrodeGroup', 'Units'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000945 has 75 NWB files.
60 of these NWB files are of type 1.
15 of these NWB files are of type 2.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2024-03-29T23:25:55.000000-04:00' '2024-03-29T23:25:55.259000-04:00']
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
  identifier: BH498_3000_200_anes
  Group /intervals/trials (TimeIntervals) tFUS stimulation trial onset and offset
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (500,) | dtype = int64
  Dataset /intervals/trials/start_time (VectorData) start time of trial | shape = (500,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) end of each trial | shape = (500,) | dtype = float64
  session_description: Awake S1 Stimulation by tFUS
  session_start_time: 2024-03-10T14:37:29.000000-04:00
  timestamps_reference_time: 2024-03-10T14:37:29.000000-04:00
  Group /units (Units) units table
  Dataset /units/celltype_label (VectorData) label 1 = RSU, label 2 = FSU | shape = (64,) | dtype = float64
  Dataset /units/id (ElementIdentifiers)  | shape = (64,) | dtype = int64
  Dataset /units/spike_times (VectorData) /units/spike_times | shape = (1200943,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) indexes data | shape = (64,) | dtype = uint64


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2024-09-30T14:26:49.649000-04:00' '2024-09-30T14:26:50.017000-04:00']
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
  identifier: BH498_3000_200_anes
  Group /intervals/trials (TimeIntervals) tFUS stimulation trial onset and offset
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (500,) | dtype = int64
  Dataset /intervals/trials/start_time (VectorData) start time of trial | shape = (500,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) end of each trial | shape = (500,) | dtype = float64
  session_description: Awake Model Anes S1 Stimulation by tFUS
  session_start_time: ['2024-03-10T14:37:29.000000-04:00']
  timestamps_reference_time: ['2024-03-10T14:37:29.000000-04:00']
  Group /units (Units) units table
  Dataset /units/id (ElementIdentifiers)  | shape = (64,) | dtype = int64
  Dataset /units/spike_times (VectorData) /units/spike_times | shape = (1200943,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) indexes data | shape = (64,) | dtype = uint64
