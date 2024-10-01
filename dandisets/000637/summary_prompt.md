
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000637/draft
name: Neural Spike Time Response Data in Anesthetized Rats in the Primary Somatosensory Cortex with Phased Ultrasound Array Stimulation
contributor: [{'name': 'Ramachandran, Sandhya', 'email': 's.ramachandran8@gmail.com', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Gao, Huan', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'NIH NS124564', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'contactPoint': [], 'includeInCitation': False}, {'name': 'NIH EB029354', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'contactPoint': [], 'includeInCitation': False}, {'name': 'He, Bin', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Yu, Kai', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Carnegie Mellon University', 'roleName': ['dcite:Affiliation'], 'schemaKey': 'Organization', 'contactPoint': [], 'includeInCitation': False}]
description: In this study, we investigate the neuronal response to transcranial focused ultrasound (tFUS) stimulation on somatosensory cortex by using a 128-element array transducer. Intracranial recordings were performed using a 32-channel Neuronexus multi-electrode array from somatosensory cortex. Wistar rats were anesthetized using isoflurane at 2%. tFUS with different parameters was applied every 2.5s (±10%). Data was recorded using a TDT system and MUA recordings were sorted using the Plexon Offline Sorter to determine the spike times.
This dataset contains spike times of the sorted neural signals and event time for each tFUS trial. In these recordings, we test different pulse repetition frequencies (PRFs) (30Hz, 300Hz, 1500Hz, 3000Hz, and 4500Hz), ultrasound durations (UDs) (100µs, 200µs, and 400µs) of ultrasound stimulation to explore the neuronal response to tFUS. The pulse duration was kept at 67ms. Each recording has 500 trials.

assetsSummary: {'species': [{'name': 'Rattus norvegicus - Norway rat', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10116'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 1163422160, 'numberOfFiles': 292, 'numberOfSubjects': 25, 'variableMeasured': ['Units', 'ElectrodeGroup'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000637 has 100 NWB files.
100 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2023-09-20T14:56:44.883000-04:00']
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
  Group /general/subject (Subject) 
  identifier: BH401_3000_100_67_5V
  Group /intervals/trials (TimeIntervals) trial data and properties
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (230,) | dtype = int64
  Dataset /intervals/trials/start_time (VectorData) start time of trial | shape = (230,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) end of each trial | shape = (230,) | dtype = float64
  session_description: Neural Spikes for S1 tFUS
  session_start_time: 2022-03-01T00:00:00.000000-05:00
  timestamps_reference_time: 2022-03-01T00:00:00.000000-05:00
  Group /units (Units) units table
  Dataset /units/id (ElementIdentifiers)  | shape = (41,) | dtype = int64
  Dataset /units/spike_times (VectorData) /units/spike_times | shape = (262252,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) indexes data | shape = (41,) | dtype = uint64
