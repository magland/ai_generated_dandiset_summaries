
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000339/draft
name: Local Field Potential Recordings in the Primary Somatosensory Cortex before and after Transcranial Focused Ultrasound Stimulation in Rats
contributor: [{'name': 'Ramachandran, Sandhya', 'email': 's.ramachandran8@gmail.com', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Carnegie Mellon University', 'roleName': ['dcite:Affiliation'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/05x2bcf33', 'contactPoint': [], 'includeInCitation': True}, {'name': 'Niu, Xiaodan', 'email': 'xiaodann@andrew.cmu.edu', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [{'name': 'Carnegie Mellon University', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/05x2bcf33'}], 'includeInCitation': True}, {'name': 'Yu, Kai', 'email': 'yukai@cmu.edu', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [{'name': 'Carnegie Mellon University', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/05x2bcf33'}], 'includeInCitation': True}, {'name': 'He, Bin', 'email': 'bhe1@andrew.cmu.edu', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [{'name': 'Carnegie Mellon University', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/05x2bcf33'}], 'includeInCitation': True}, {'name': 'NIH MH114233', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'contactPoint': [], 'includeInCitation': False}, {'name': 'NIH NS124564 ', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'contactPoint': [], 'includeInCitation': False}]
description: In this study, we investigate how transcranial focused ultrasound (tFUS) modulates neural interaction and response to peripheral electrical stimulation at hindlimb through intracranial multi-electrode recordings in the rat somatosensory cortex. Recordings were performed using a 32-channel NeuroNexus® multi-electrode array. Rats were anesthetized using isoflurane at 2%. Recordings were taken while delivering peripheral electrical stimulation once every 5 seconds to analyze the neural response in the rat S1HL region, before ultrasound for 30 minutes and then afterwards for an hour, in order to determine how the ultrasound modulated the electrical stimulation induced local field potential (LFP) waveforms. We delivered ultrasound for 5 minutes in a pulsed pattern at 5 levels of sonication repetition frequencies (SRF) (10 Hz, 50 Hz, 75 Hz, 100 Hz, and 125 Hz) to induce frequency dependent plasticity in a manner similar to that is found following tetanic electrical stimulation. We investigated whether delivering tFUS that alters connectivity/correlation between the targeted neurons may alter collective responses manifested in the modulated LFP waveforms. The applied fundamental frequency of ultrasound was 0.5 MHz, the pulse repetition frequency (PRF) was 3 kHz, and the total duty cycle was 36%. This dataset contains LFP recordings, with 32 channels for each datafile.
In each subject, recordings are provided with "pre" and "post" tFUS for two different frequencies (SRF), and most contain recordings during the delivery of ultrasound and during rest periods between sessions of different ultrasound parameters. For example, a single subject may include "100Hz_pre", "100Hz_post", "50Hz_pre", "50Hz_post", which are the pre and post tFUS recordings for the two used parameters, and then "50Hz" and "100Hz", which are the recordings taken during stimulation, and "rest1" and "rest2", which are the rest periods between sessions. These names are preceded by a label such as "BH280", which is the animal subject label. Ultrasound is delivered in a continuous paradigm, with pulses delivered at the stimulation repetition frequency continuously throughout the 5 minutes of stimulation. During the "pre" and "post" recordings, the peripheral electrical stimulation is delivered once every 5 seconds approximately. Electrical stimulation event trigger is not included in the dataset as it was not recorded due to using a separate system to deliver the electrical stimulation. We were using threshold detection on a channel of LFP recordings in order to detect the electrical stimulation events, in which events can be recognized by the quick rising of voltage. One could also approximate it by detecting the first event, and then add periods of 5 seconds to generate the rest of the trigger times.
More details about the experimental details can be found in our paper published by Journal of Neural Engineering (DOI: 10.1088/1741-2552/ac889f).
assetsSummary: {'species': [{'name': 'Rattus norvegicus - Norway rat', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10116'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 64243853984, 'numberOfFiles': 66, 'numberOfSubjects': 30, 'variableMeasured': ['ProcessingModule', 'ElectricalSeries', 'LFP', 'ElectrodeGroup'], 'measurementTechnique': [{'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'signal filtering technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000339 has 66 NWB files.
66 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2023-03-22T21:47:41.000000-07:00' '2023-03-22T21:47:43.109000-07:00']
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
  identifier: BH243_50Hz_pre
  Group /processing/ecephys (ProcessingModule) extracellular electrophysiology
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/ElectricalSeries (ElectricalSeries) no description
  Dataset /processing/ecephys/LFP/ElectricalSeries/electrodes (DynamicTableRegion) all electrodes | shape = (32,) | dtype = int64
  session_description: Rat SEP induction
  session_start_time: 2021-04-14T17:00:02.000000-07:00
  timestamps_reference_time: 2021-04-14T17:00:02.000000-07:00
