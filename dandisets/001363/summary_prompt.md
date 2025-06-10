
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001363/draft
name: Neural Spiking Data in the Rat Somatosensory Cortex Using a Flexible Electrode Responding to Transcranial Focused Ultrasound
contributor: [{'name': 'Ramachandran, Sandhya', 'email': 's.ramachandran8@gmail.com', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Gao, Huan', 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Yu, Kai', 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Yeh, Kelly', 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'He, Bin', 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Carnegie Mellon University', 'schemaKey': 'Organization', 'includeInCitation': False}, {'name': 'RF1NS131069', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'includeInCitation': False}, {'name': 'R01 NS124564', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': '', 'includeInCitation': False}]
description: In this study, we investigate the neuronal response to transcranial focused ultrasound stimulation (tFUS) on the somatosensory cortex using a 128-element array transducer and a chronically implanted ultraflexible nanoelectric thread electrode. This flexible electrode allows us to  study higher intensities of tFUS which are impossible with a rigid electrode due to the vibration artifacts that are created. Here we test 5 different levels of in situ ultrasound pressure including 100, 400, 700, 1000, and 1300 kPa. We then tested the effect of varying duty cycle while keeping the pulse repetition frequency (PRF) constant while using the highest peak-peak pressure (1300 kPa), testing duty cycles of 0.6%, 6%, 30%, 60%, and 90% while holding PRF at 1500 Hz. Finally we tested the effect of varying PRF while holding duty cycle constant, testing PRFs of 30, 300, 1500, 3000, and 4500 Hz with a duty cycle of 30%. In each of these, the fundamental frequency of ultrasound was 1500 kHz, and the ultrasound duration was 67 ms, with trials performed every 2 seconds, with a jitter of 10%. Each recording has 505 trials. 
assetsSummary: {'species': [{'name': 'Rattus norvegicus - Norway rat', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10116'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 180622044792, 'numberOfFiles': 55, 'numberOfSubjects': 5, 'variableMeasured': ['ElectrodeGroup', 'ElectricalSeries'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 001363 has 55 NWB files.
55 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeries (ElectricalSeries) no description
  Dataset /acquisition/ElectricalSeries/electrodes (DynamicTableRegion) all electrodes | shape = (32,) | dtype = int64
  file_create_date: ['2025-03-27T13:48:28.847000-04:00' '2025-03-27T13:48:29.304000-04:00']
  Group /general/devices/array (Device) NET probe flexible electrode
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
  Group /general/extracellular_ephys/shank1/device (Device) NET probe flexible electrode
  institution: Carnegie Mellon University
  Group /general/subject (Subject) 
  identifier: BH589_1500_200_67_25V
  Group /intervals/trials (TimeIntervals) tFUS stimulation trial onset and offset
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (500,) | dtype = int64
  Dataset /intervals/trials/start_time (VectorData) start time of trial | shape = (500,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) end of each trial | shape = (500,) | dtype = float64
  session_description: Rat Ultrasound Array Stimulation
  session_start_time: ['2024-08-27T16:04:57.000000-04:00']
  timestamps_reference_time: ['2024-08-27T16:04:57.000000-04:00']
