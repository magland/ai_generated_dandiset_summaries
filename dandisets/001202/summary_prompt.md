
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001202/draft
name: Neural Spike Time Response recorded by NET Probe Soft Electrode in the Primary Somatosensory Cortex with Phased Ultrasound Array Stimulation
contributor: [{'name': 'Gao, Huan', 'email': 'huangao@andrew.cmu.edu', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'He, Bin', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Yu, Kai', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Ramachandran, Sandhya', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Carnegie Mellon University', 'roleName': ['dcite:Affiliation'], 'schemaKey': 'Organization', 'includeInCitation': False}, {'name': 'NIH NS13106', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'includeInCitation': False}, {'name': 'NIH NS124564', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'includeInCitation': False}, {'name': 'NIH EB029354', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'includeInCitation': False}]
description: In this study, we investigate the neuronal response to transcranial focused ultrasound (tFUS) stimulation on somatosensory cortex by using a 128-element array transducer. Intracranial recordings were performed using a 32-channel Soft NET Probe, which is compatible with tFUS. The electrode was chronically implanted  and can be repeatedly used. Wistar rats were anesthetized using isoflurane at 2% during recording session. tFUS with different parameters was applied every 2.5s (±10%). This dataset contains spike times of the sorted neural signals and event time for each tFUS trial. In these recordings, we test different pulse repetition frequencies (PRFs)  and pressure levels of ultrasound stimulation to explore the neuronal response to tFUS. The pulse duration was kept at 67ms. Each recording has 500 trials. We also compare two setup of the transducer, one is with a collimator and the other one is without the collimator, to explore the better setup for chronic recording and tFUS modulation.
assetsSummary: {'schemaKey': 'AssetsSummary', 'numberOfBytes': 0, 'numberOfFiles': 0}

Dandiset 001202 has 13 NWB files.
13 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2024-09-30T21:42:40.414000-04:00']
  data_collection: No tFUS
  Group /general/devices/array (Device) A1x64-Edge-6mm-22.5-177 without z-coating
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
  Group /general/extracellular_ephys/shank1/device (Device) A1x64-Edge-6mm-22.5-177 without z-coating
  institution: Carnegie Mellon University
  notes: Recording:S1; collimator:with collimator
  stimulus: intervals contains each tFUS trial start and end timestamps
  Group /general/subject (Subject) 
  identifier: BH560_baseline
  Group /intervals/trials (TimeIntervals) each trial start and end timestamps
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (321,) | dtype = int64
  Dataset /intervals/trials/start_time (VectorData) start time of trial | shape = (321,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) end time of each trial | shape = (321,) | dtype = float64
  session_description: Neural Spikes for neural pathways to tFUS
  session_start_time: 2024-06-21T18:25:00.000000-04:00
  timestamps_reference_time: 2024-09-30T21:42:40.012000-04:00
  Group /units (Units) units table
  Dataset /units/celltype_label (VectorData) label 1 = RSU, label 2 = FSU | shape = (2,) | dtype = float64
  Dataset /units/id (ElementIdentifiers)  | shape = (2,) | dtype = int64
  Dataset /units/spike_times (VectorData) /units/spike_times | shape = (23972,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) indexes data | shape = (2,) | dtype = uint64
