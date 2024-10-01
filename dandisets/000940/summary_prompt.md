
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000940/draft
name: Data for: Hippocampal Theta Phase Precession Supports Memory Formation and Retrieval of Naturalistic Experience in Humans
contributor: [{'name': 'National Institutes of Health (NIH)', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': '5 U01 NS 117839-04'}, {'name': 'Zheng, Jie', 'email': 'zjzheng@ucdavis.edu', 'roleName': ['dcite:Author', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Yebra, Mar', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Schjetnan, Andrea', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Patel, Kramay', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Katz, Chaim', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Kyzar, Michael', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Mosher, Clayton', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Kalia, Suneil', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Chung, Jeffrey', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Reed, Chrystal', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Valiante, Taufik', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Mamelak, Adam', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Kreiman, Gabriel', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'includeInCitation': False}, {'name': 'Rutishauser, Ueli', 'email': 'ueli.rutishauser@cshs.org', 'roleName': ['dcite:Author', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0002-9207-7069', 'includeInCitation': True}]
description: This repository contains the single neuron and local field potential recordings that underly the analysis of the paper: 

Hippocampal Theta Phase Precession Supports Memory Formation and Retrieval of Naturalistic Experience in Humans. Jie Zheng, Mar Yebra, Andrea G.P. Schjetnan, Clayton Mosher, Suneil K. Kalia, Jeffrey M. Chung, Chrystal M. Reed, Taufik A. Valiante, Adam N. Mamelak, Gabriel Kreiman, Ueli Rutishauser. Nature Human Behavior, in press (2024).

Further information will be added upon publication.
assetsSummary: {'species': [{'name': 'Homo sapiens - Human', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9606'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 3596791437, 'numberOfFiles': 21, 'numberOfSubjects': 21, 'variableMeasured': ['ElectrodeGroup', 'ElectricalSeries', 'Units'], 'measurementTechnique': [{'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000940 has 7 NWB files.
1 of these NWB files are of type 1.
1 of these NWB files are of type 2.
1 of these NWB files are of type 3.
2 of these NWB files are of type 4.
2 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/LFPs (ElectricalSeries) These are LFP recordings that have been downsampled to 250 Hz
  Dataset /acquisition/LFPs/electrodes (DynamicTableRegion) single electrodes | shape = (10,) | dtype = int32
  Group /acquisition/events (TimeSeries) The events coorespond to the TTL markers for each trial. For the encoding trials, the TTL markers are the following: 61 = start of the experiment, 1 = stimulus ON, 2 = stimulus OFF, 11 = Fix Cross, 3 = Probe, 4 = Response, 60 = End of Experiment
  Group /acquisition/experiment_ids (TimeSeries) The experiment_ids correspond to the encoding, recognition or time discrimination trials. The encoding trials are demarcated by: 70. The recognition trials are demarcated by: 71. The time discrimination trials are demarcated by: 72
  file_create_date: ['2024-07-19T06:40:24.233532-07:00']
  Group /general/devices/NLX-microwires-177 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-178 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-179 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-180 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-182 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-183 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-184 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-190 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-191 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-192 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  experiment_description: This data contains electrophysiological recordings and behavior from the cognitive boundary task performed in patients with intractable epilepsy implanted with depth electrodes and Behnke-Fried microwires in the human Medical Temporal Lobe (MTL).
  experimenter: ['Kyzar, Michael']
  Group /general/extracellular_ephys/NLX-microwires-177 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-177/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-178 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-178/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-179 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-179/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-180 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-180/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-182 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-182/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-183 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-183/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-184 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-184/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-190 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-190/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-191 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-191/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-192 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-192/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/electrodes (DynamicTable) microwire electrodes table
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) my description | shape = (10,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) my description | shape = (10,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) my description | shape = (10,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (10,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) my description | shape = (10,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/origChannel (VectorData) my description | shape = (10,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) my description | shape = (10,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) my description | shape = (10,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) my description | shape = (10,) | dtype = float64
  institution: Cedars-Sinai Medical Center
  keywords: ['single neuron, human, intracranial']
  lab: Rutishauser
  notes: (1) Experiment variant: 1. (2) The session start time has been set to Jan 1st to avoid disclosure of protected health information (PHI).
  related_publications: ['doi: https://doi.org/10.1101/2023.06.05.543539']
  session_id: 1
  source_script: NWB_CBPP_export_main
  Group /general/subject (Subject) 
  identifier: sub-1_ses-1_P60CS
  Group /intervals/encoding_table (TimeIntervals) intervals for the encoding task
  Dataset /intervals/encoding_table/Clip_name (VectorData) video clip shown during this trial | shape = (90,) | dtype = object
  Dataset /intervals/encoding_table/ExperimentID (VectorData) EXPERIMENT_ID | shape = (90,) | dtype = float64
  Dataset /intervals/encoding_table/boundary1_time (VectorData) time of first boundary (0 if it does not exist; absolute timestamp). For no boundary (NB), this is equal to 4s (same as HB). For hard boundary (HB) clips, this is the time of the HB. For soft boundary (SB) clips, this is the time of the first SB. | shape = (90,) | dtype = float64
  Dataset /intervals/encoding_table/boundary2_time (VectorData) time of second boundary (0 if it does not exist; absolute timestamp). For HB clips, this is the time of first SB boundary. For SB clips, this is second SB boundary in the clip. | shape = (90,) | dtype = float64
  Dataset /intervals/encoding_table/boundary3_time (VectorData) time of third boundary (0 if it does not exist; absolute timestamp). For HB clips, thisis the time of the second SB boundary. For SB clips, this is the third SB boundary of the clip. | shape = (90,) | dtype = float64
  Dataset /intervals/encoding_table/fixcross_time (VectorData) fix cross time. TTL=11 | shape = (90,) | dtype = float64
  Dataset /intervals/encoding_table/id (ElementIdentifiers)  | shape = (90,) | dtype = int64
  Dataset /intervals/encoding_table/start_time (VectorData) start time of video. TTL=1 | shape = (90,) | dtype = float64
  Dataset /intervals/encoding_table/stimCategory (VectorData) 1=no boundary (NB), 2=soft boundary (SB), 3=hard boundary (HB). Note - HB clips can, in addition, also contain SB boundaries. | shape = (90,) | dtype = uint8
  Dataset /intervals/encoding_table/stop_time (VectorData) stop time of video. TTL=2 | shape = (90,) | dtype = float64
  Group /intervals/recognition_table (TimeIntervals) intervals for scene recognition task
  Dataset /intervals/recognition_table/ExperimentID (VectorData) EXPERIMENT_ID | shape = (180,) | dtype = float64
  Dataset /intervals/recognition_table/RT (VectorData) Reaction time | shape = (180,) | dtype = float64
  Dataset /intervals/recognition_table/accuracy (VectorData) correct = 2, incorrect 1, no response = 0 | shape = (180,) | dtype = uint8
  Dataset /intervals/recognition_table/boundary_type (VectorData) 1=no boundary (NB), 2=soft boundary (SB), 3=hard boundary (HB) | shape = (180,) | dtype = uint8
  Dataset /intervals/recognition_table/confidence (VectorData) 3 = high, 2 = medium, 1 = low | shape = (180,) | dtype = uint8
  Dataset /intervals/recognition_table/fixcross_time (VectorData) fix cross onset. TTL=11 | shape = (180,) | dtype = float64
  Dataset /intervals/recognition_table/frameName (VectorData) name of image shown | shape = (180,) | dtype = object
  Dataset /intervals/recognition_table/id (ElementIdentifiers)  | shape = (180,) | dtype = int64
  Dataset /intervals/recognition_table/old_new (VectorData) Response Old = 2, New = 1 | shape = (180,) | dtype = uint8
  Dataset /intervals/recognition_table/resp_value (VectorData) range = 2-7, -1=timeout | shape = (180,) | dtype = uint8
  Dataset /intervals/recognition_table/response_time (VectorData) fix cross onset. TTL=4 | shape = (180,) | dtype = float64
  Dataset /intervals/recognition_table/start_time (VectorData) start time of test frame. TTL=1 | shape = (180,) | dtype = float64
  Dataset /intervals/recognition_table/stimuli_type (VectorData) target (ground truth) = 1, foil = 0 | shape = (180,) | dtype = uint8
  Dataset /intervals/recognition_table/stop_time (VectorData) stop time of test frame. TTL=2 | shape = (180,) | dtype = float64
  Dataset /intervals/recognition_table/trial_num (VectorData) trial nr | shape = (180,) | dtype = uint8
  Group /intervals/timediscrimination_table (TimeIntervals) intervals for time discrimination task
  Dataset /intervals/timediscrimination_table/ExperimentID (VectorData) EXPERIMENT_ID | shape = (180,) | dtype = float64
  Dataset /intervals/timediscrimination_table/RT (VectorData) Reaction time | shape = (180,) | dtype = float64
  Dataset /intervals/timediscrimination_table/accuracy (VectorData) correct = 2, incorrect 1, no response = 0 | shape = (180,) | dtype = float64
  Dataset /intervals/timediscrimination_table/boundary_type (VectorData) 1=no boundary (NB), 2=soft boundary (SB), 3=hard boundary (HB) | shape = (180,) | dtype = uint8
  Dataset /intervals/timediscrimination_table/confidence (VectorData) 3 = high, 2 = medium, 1 = low | shape = (180,) | dtype = float64
  Dataset /intervals/timediscrimination_table/fixcross_time (VectorData) fix cross onset. TTL=11 | shape = (180,) | dtype = float64
  Dataset /intervals/timediscrimination_table/frameName (VectorData) name of image shown | shape = (180,) | dtype = object
  Dataset /intervals/timediscrimination_table/id (ElementIdentifiers)  | shape = (180,) | dtype = int64
  Dataset /intervals/timediscrimination_table/key (VectorData) left = 1, right = 2 | shape = (180,) | dtype = uint8
  Dataset /intervals/timediscrimination_table/leftright (VectorData) Left = 1, Right = 2 | shape = (180,) | dtype = uint8
  Dataset /intervals/timediscrimination_table/resp_value (VectorData) range = 2-7, -1=no response | shape = (180,) | dtype = uint8
  Dataset /intervals/timediscrimination_table/response_time (VectorData) fix cross onset. TTL=4 | shape = (180,) | dtype = float64
  Dataset /intervals/timediscrimination_table/start_time (VectorData) start time of test frame. TTL=1 | shape = (180,) | dtype = float64
  Dataset /intervals/timediscrimination_table/stop_time (VectorData) stop time of test frame. TTL=2 | shape = (180,) | dtype = float64
  Dataset /intervals/timediscrimination_table/trial_num (VectorData) trial nr | shape = (180,) | dtype = uint8
  session_description: CBPP: 1 CBPPID: 1
  session_start_time: 2018-01-01T00:00:00.000000-08:00
  Group /stimulus/presentation/ExternalVideos (OpticalSeries) Please contact authors for clips.
  timestamps_reference_time: 2018-01-01T00:00:00.000000-08:00
  Group /units (Units) units table
  Dataset /units/electrodes (DynamicTableRegion) single electrodes | shape = (43,) | dtype = int32
  Dataset /units/id (ElementIdentifiers)  | shape = (43,) | dtype = int32
  Dataset /units/spike_times (VectorData) Timestamps when spikes occured (seconds) | shape = (603265,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) indexes data | shape = (43,) | dtype = uint64


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/LFPs (ElectricalSeries) These are LFP recordings that have been downsampled to 250 Hz
  Dataset /acquisition/LFPs/electrodes (DynamicTableRegion) single electrodes | shape = (13,) | dtype = int32
  Group /acquisition/events (TimeSeries) The events coorespond to the TTL markers for each trial. For the encoding trials, the TTL markers are the following: 61 = start of the experiment, 1 = stimulus ON, 2 = stimulus OFF, 11 = Fix Cross, 3 = Probe, 4 = Response, 60 = End of Experiment
  Group /acquisition/experiment_ids (TimeSeries) The experiment_ids correspond to the encoding, recognition or time discrimination trials. The encoding trials are demarcated by: 70. The recognition trials are demarcated by: 71. The time discrimination trials are demarcated by: 72
  file_create_date: ['2024-07-19T06:36:51.646056-07:00']
  Group /general/devices/NLX-microwires-137 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-139 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-140 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-141 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-142 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-143 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-217 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-218 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-219 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-220 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-221 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-222 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-223 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  experiment_description: This data contains electrophysiological recordings and behavior from the cognitive boundary task performed in patients with intractable epilepsy implanted with depth electrodes and Behnke-Fried microwires in the human Medical Temporal Lobe (MTL).
  experimenter: ['Kyzar, Michael']
  Group /general/extracellular_ephys/NLX-microwires-137 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-137/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-139 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-139/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-140 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-140/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-141 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-141/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-142 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-142/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-143 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-143/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-217 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-217/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-218 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-218/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-219 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-219/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-220 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-220/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-221 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-221/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-222 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-222/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-223 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-223/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/electrodes (DynamicTable) microwire electrodes table
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) my description | shape = (13,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) my description | shape = (13,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) my description | shape = (13,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (13,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) my description | shape = (13,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/origChannel (VectorData) my description | shape = (13,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) my description | shape = (13,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) my description | shape = (13,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) my description | shape = (13,) | dtype = float64
  institution: Toronto Western Hospital
  keywords: ['single neuron, human, intracranial']
  lab: Rutishauser
  notes: (1) Experiment variant: 1. (2) The session start time has been set to Jan 1st to avoid disclosure of protected health information (PHI).
  related_publications: ['doi: https://doi.org/10.1101/2023.06.05.543539']
  session_id: 1
  source_script: NWB_CBPP_export_main
  Group /general/subject (Subject) 
  identifier: sub-10_ses-1_TWH116
  Group /intervals/encoding_table (TimeIntervals) intervals for the encoding task
  Dataset /intervals/encoding_table/Clip_name (VectorData) video clip shown during this trial | shape = (90,) | dtype = object
  Dataset /intervals/encoding_table/ExperimentID (VectorData) EXPERIMENT_ID | shape = (90,) | dtype = float64
  Dataset /intervals/encoding_table/boundary1_time (VectorData) time of first boundary (0 if it does not exist; absolute timestamp). For no boundary (NB), this is equal to 4s (same as HB). For hard boundary (HB) clips, this is the time of the HB. For soft boundary (SB) clips, this is the time of the first SB. | shape = (90,) | dtype = float64
  Dataset /intervals/encoding_table/boundary2_time (VectorData) time of second boundary (0 if it does not exist; absolute timestamp). For HB clips, this is the time of first SB boundary. For SB clips, this is second SB boundary in the clip. | shape = (90,) | dtype = float64
  Dataset /intervals/encoding_table/boundary3_time (VectorData) time of third boundary (0 if it does not exist; absolute timestamp). For HB clips, thisis the time of the second SB boundary. For SB clips, this is the third SB boundary of the clip. | shape = (90,) | dtype = float64
  Dataset /intervals/encoding_table/fixcross_time (VectorData) fix cross time. TTL=11 | shape = (90,) | dtype = float64
  Dataset /intervals/encoding_table/id (ElementIdentifiers)  | shape = (90,) | dtype = int64
  Dataset /intervals/encoding_table/start_time (VectorData) start time of video. TTL=1 | shape = (90,) | dtype = float64
  Dataset /intervals/encoding_table/stimCategory (VectorData) 1=no boundary (NB), 2=soft boundary (SB), 3=hard boundary (HB). Note - HB clips can, in addition, also contain SB boundaries. | shape = (90,) | dtype = uint8
  Dataset /intervals/encoding_table/stop_time (VectorData) stop time of video. TTL=2 | shape = (90,) | dtype = float64
  Group /intervals/recognition_table (TimeIntervals) intervals for scene recognition task
  Dataset /intervals/recognition_table/ExperimentID (VectorData) EXPERIMENT_ID | shape = (180,) | dtype = float64
  Dataset /intervals/recognition_table/RT (VectorData) Reaction time | shape = (180,) | dtype = float64
  Dataset /intervals/recognition_table/accuracy (VectorData) correct = 2, incorrect 1, no response = 0 | shape = (180,) | dtype = uint8
  Dataset /intervals/recognition_table/boundary_type (VectorData) 1=no boundary (NB), 2=soft boundary (SB), 3=hard boundary (HB) | shape = (180,) | dtype = uint8
  Dataset /intervals/recognition_table/confidence (VectorData) 3 = high, 2 = medium, 1 = low | shape = (180,) | dtype = uint8
  Dataset /intervals/recognition_table/fixcross_time (VectorData) fix cross onset. TTL=11 | shape = (180,) | dtype = float64
  Dataset /intervals/recognition_table/frameName (VectorData) name of image shown | shape = (180,) | dtype = object
  Dataset /intervals/recognition_table/id (ElementIdentifiers)  | shape = (180,) | dtype = int64
  Dataset /intervals/recognition_table/old_new (VectorData) Response Old = 2, New = 1 | shape = (180,) | dtype = uint8
  Dataset /intervals/recognition_table/resp_value (VectorData) range = 2-7, -1=timeout | shape = (180,) | dtype = uint8
  Dataset /intervals/recognition_table/response_time (VectorData) fix cross onset. TTL=4 | shape = (180,) | dtype = float64
  Dataset /intervals/recognition_table/start_time (VectorData) start time of test frame. TTL=1 | shape = (180,) | dtype = float64
  Dataset /intervals/recognition_table/stimuli_type (VectorData) target (ground truth) = 1, foil = 0 | shape = (180,) | dtype = uint8
  Dataset /intervals/recognition_table/stop_time (VectorData) stop time of test frame. TTL=2 | shape = (180,) | dtype = float64
  Dataset /intervals/recognition_table/trial_num (VectorData) trial nr | shape = (180,) | dtype = uint8
  Group /intervals/timediscrimination_table (TimeIntervals) intervals for time discrimination task
  Dataset /intervals/timediscrimination_table/ExperimentID (VectorData) EXPERIMENT_ID | shape = (180,) | dtype = float64
  Dataset /intervals/timediscrimination_table/RT (VectorData) Reaction time | shape = (180,) | dtype = float64
  Dataset /intervals/timediscrimination_table/accuracy (VectorData) correct = 2, incorrect 1, no response = 0 | shape = (180,) | dtype = float64
  Dataset /intervals/timediscrimination_table/boundary_type (VectorData) 1=no boundary (NB), 2=soft boundary (SB), 3=hard boundary (HB) | shape = (180,) | dtype = uint8
  Dataset /intervals/timediscrimination_table/confidence (VectorData) 3 = high, 2 = medium, 1 = low | shape = (180,) | dtype = float64
  Dataset /intervals/timediscrimination_table/fixcross_time (VectorData) fix cross onset. TTL=11 | shape = (180,) | dtype = float64
  Dataset /intervals/timediscrimination_table/frameName (VectorData) name of image shown | shape = (180,) | dtype = object
  Dataset /intervals/timediscrimination_table/id (ElementIdentifiers)  | shape = (180,) | dtype = int64
  Dataset /intervals/timediscrimination_table/key (VectorData) left = 1, right = 2 | shape = (180,) | dtype = uint8
  Dataset /intervals/timediscrimination_table/leftright (VectorData) Left = 1, Right = 2 | shape = (180,) | dtype = uint8
  Dataset /intervals/timediscrimination_table/resp_value (VectorData) range = 2-7, -1=no response | shape = (180,) | dtype = uint8
  Dataset /intervals/timediscrimination_table/response_time (VectorData) fix cross onset. TTL=4 | shape = (180,) | dtype = float64
  Dataset /intervals/timediscrimination_table/start_time (VectorData) start time of test frame. TTL=1 | shape = (180,) | dtype = float64
  Dataset /intervals/timediscrimination_table/stop_time (VectorData) stop time of test frame. TTL=2 | shape = (180,) | dtype = float64
  Dataset /intervals/timediscrimination_table/trial_num (VectorData) trial nr | shape = (180,) | dtype = uint8
  session_description: CBPP: 1 CBPPID: 10
  session_start_time: 2018-01-01T00:00:00.000000-08:00
  Group /stimulus/presentation/ExternalVideos (OpticalSeries) Please contact authors for clips.
  timestamps_reference_time: 2018-01-01T00:00:00.000000-08:00
  Group /units (Units) units table
  Dataset /units/electrodes (DynamicTableRegion) single electrodes | shape = (27,) | dtype = int32
  Dataset /units/id (ElementIdentifiers)  | shape = (27,) | dtype = int32
  Dataset /units/spike_times (VectorData) Timestamps when spikes occured (seconds) | shape = (140083,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) indexes data | shape = (27,) | dtype = uint64


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/LFPs (ElectricalSeries) These are LFP recordings that have been downsampled to 250 Hz
  Dataset /acquisition/LFPs/electrodes (DynamicTableRegion) single electrodes | shape = (11,) | dtype = int32
  Group /acquisition/events (TimeSeries) The events coorespond to the TTL markers for each trial. For the encoding trials, the TTL markers are the following: 61 = start of the experiment, 1 = stimulus ON, 2 = stimulus OFF, 11 = Fix Cross, 3 = Probe, 4 = Response, 60 = End of Experiment
  Group /acquisition/experiment_ids (TimeSeries) The experiment_ids correspond to the encoding, recognition or time discrimination trials. The encoding trials are demarcated by: 70. The recognition trials are demarcated by: 71. The time discrimination trials are demarcated by: 72
  file_create_date: ['2024-07-19T06:36:59.439579-07:00']
  Group /general/devices/NLX-microwires-148 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-149 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-152 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-154 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-157 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-158 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-159 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-160 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-164 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-166 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-167 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  experiment_description: This data contains electrophysiological recordings and behavior from the cognitive boundary task performed in patients with intractable epilepsy implanted with depth electrodes and Behnke-Fried microwires in the human Medical Temporal Lobe (MTL).
  experimenter: ['Kyzar, Michael']
  Group /general/extracellular_ephys/NLX-microwires-148 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-148/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-149 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-149/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-152 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-152/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-154 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-154/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-157 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-157/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-158 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-158/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-159 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-159/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-160 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-160/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-164 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-164/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-166 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-166/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-167 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-167/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/electrodes (DynamicTable) microwire electrodes table
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) my description | shape = (11,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) my description | shape = (11,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) my description | shape = (11,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (11,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) my description | shape = (11,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/origChannel (VectorData) my description | shape = (11,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) my description | shape = (11,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) my description | shape = (11,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) my description | shape = (11,) | dtype = float64
  institution: Toronto Western Hospital
  keywords: ['single neuron, human, intracranial']
  lab: Rutishauser
  notes: (1) Experiment variant: 1. (2) The session start time has been set to Jan 1st to avoid disclosure of protected health information (PHI).
  related_publications: ['doi: https://doi.org/10.1101/2023.06.05.543539']
  session_id: 1
  source_script: NWB_CBPP_export_main
  Group /general/subject (Subject) 
  identifier: sub-11_ses-1_TWH117
  Group /intervals/encoding_table (TimeIntervals) intervals for the encoding task
  Dataset /intervals/encoding_table/Clip_name (VectorData) video clip shown during this trial | shape = (90,) | dtype = object
  Dataset /intervals/encoding_table/ExperimentID (VectorData) EXPERIMENT_ID | shape = (90,) | dtype = float64
  Dataset /intervals/encoding_table/boundary1_time (VectorData) time of first boundary (0 if it does not exist; absolute timestamp). For no boundary (NB), this is equal to 4s (same as HB). For hard boundary (HB) clips, this is the time of the HB. For soft boundary (SB) clips, this is the time of the first SB. | shape = (90,) | dtype = float64
  Dataset /intervals/encoding_table/boundary2_time (VectorData) time of second boundary (0 if it does not exist; absolute timestamp). For HB clips, this is the time of first SB boundary. For SB clips, this is second SB boundary in the clip. | shape = (90,) | dtype = float64
  Dataset /intervals/encoding_table/boundary3_time (VectorData) time of third boundary (0 if it does not exist; absolute timestamp). For HB clips, thisis the time of the second SB boundary. For SB clips, this is the third SB boundary of the clip. | shape = (90,) | dtype = float64
  Dataset /intervals/encoding_table/fixcross_time (VectorData) fix cross time. TTL=11 | shape = (90,) | dtype = float64
  Dataset /intervals/encoding_table/id (ElementIdentifiers)  | shape = (90,) | dtype = int64
  Dataset /intervals/encoding_table/start_time (VectorData) start time of video. TTL=1 | shape = (90,) | dtype = float64
  Dataset /intervals/encoding_table/stimCategory (VectorData) 1=no boundary (NB), 2=soft boundary (SB), 3=hard boundary (HB). Note - HB clips can, in addition, also contain SB boundaries. | shape = (90,) | dtype = uint8
  Dataset /intervals/encoding_table/stop_time (VectorData) stop time of video. TTL=2 | shape = (90,) | dtype = float64
  Group /intervals/recognition_table (TimeIntervals) intervals for scene recognition task
  Dataset /intervals/recognition_table/ExperimentID (VectorData) EXPERIMENT_ID | shape = (180,) | dtype = float64
  Dataset /intervals/recognition_table/RT (VectorData) Reaction time | shape = (180,) | dtype = float64
  Dataset /intervals/recognition_table/accuracy (VectorData) correct = 2, incorrect 1, no response = 0 | shape = (180,) | dtype = uint8
  Dataset /intervals/recognition_table/boundary_type (VectorData) 1=no boundary (NB), 2=soft boundary (SB), 3=hard boundary (HB) | shape = (180,) | dtype = uint8
  Dataset /intervals/recognition_table/confidence (VectorData) 3 = high, 2 = medium, 1 = low | shape = (180,) | dtype = uint8
  Dataset /intervals/recognition_table/fixcross_time (VectorData) fix cross onset. TTL=11 | shape = (180,) | dtype = float64
  Dataset /intervals/recognition_table/frameName (VectorData) name of image shown | shape = (180,) | dtype = object
  Dataset /intervals/recognition_table/id (ElementIdentifiers)  | shape = (180,) | dtype = int64
  Dataset /intervals/recognition_table/old_new (VectorData) Response Old = 2, New = 1 | shape = (180,) | dtype = uint8
  Dataset /intervals/recognition_table/resp_value (VectorData) range = 2-7, -1=timeout | shape = (180,) | dtype = uint8
  Dataset /intervals/recognition_table/response_time (VectorData) fix cross onset. TTL=4 | shape = (180,) | dtype = float64
  Dataset /intervals/recognition_table/start_time (VectorData) start time of test frame. TTL=1 | shape = (180,) | dtype = float64
  Dataset /intervals/recognition_table/stimuli_type (VectorData) target (ground truth) = 1, foil = 0 | shape = (180,) | dtype = uint8
  Dataset /intervals/recognition_table/stop_time (VectorData) stop time of test frame. TTL=2 | shape = (180,) | dtype = float64
  Dataset /intervals/recognition_table/trial_num (VectorData) trial nr | shape = (180,) | dtype = uint8
  Group /intervals/timediscrimination_table (TimeIntervals) intervals for time discrimination task
  Dataset /intervals/timediscrimination_table/ExperimentID (VectorData) EXPERIMENT_ID | shape = (180,) | dtype = float64
  Dataset /intervals/timediscrimination_table/RT (VectorData) Reaction time | shape = (180,) | dtype = float64
  Dataset /intervals/timediscrimination_table/accuracy (VectorData) correct = 2, incorrect 1, no response = 0 | shape = (180,) | dtype = float64
  Dataset /intervals/timediscrimination_table/boundary_type (VectorData) 1=no boundary (NB), 2=soft boundary (SB), 3=hard boundary (HB) | shape = (180,) | dtype = uint8
  Dataset /intervals/timediscrimination_table/confidence (VectorData) 3 = high, 2 = medium, 1 = low | shape = (180,) | dtype = float64
  Dataset /intervals/timediscrimination_table/fixcross_time (VectorData) fix cross onset. TTL=11 | shape = (180,) | dtype = float64
  Dataset /intervals/timediscrimination_table/frameName (VectorData) name of image shown | shape = (180,) | dtype = object
  Dataset /intervals/timediscrimination_table/id (ElementIdentifiers)  | shape = (180,) | dtype = int64
  Dataset /intervals/timediscrimination_table/key (VectorData) left = 1, right = 2 | shape = (180,) | dtype = uint8
  Dataset /intervals/timediscrimination_table/leftright (VectorData) Left = 1, Right = 2 | shape = (180,) | dtype = uint8
  Dataset /intervals/timediscrimination_table/resp_value (VectorData) range = 2-7, -1=no response | shape = (180,) | dtype = uint8
  Dataset /intervals/timediscrimination_table/response_time (VectorData) fix cross onset. TTL=4 | shape = (180,) | dtype = float64
  Dataset /intervals/timediscrimination_table/start_time (VectorData) start time of test frame. TTL=1 | shape = (180,) | dtype = float64
  Dataset /intervals/timediscrimination_table/stop_time (VectorData) stop time of test frame. TTL=2 | shape = (180,) | dtype = float64
  Dataset /intervals/timediscrimination_table/trial_num (VectorData) trial nr | shape = (180,) | dtype = uint8
  session_description: CBPP: 1 CBPPID: 11
  session_start_time: 2018-01-01T00:00:00.000000-08:00
  Group /stimulus/presentation/ExternalVideos (OpticalSeries) Please contact authors for clips.
  timestamps_reference_time: 2018-01-01T00:00:00.000000-08:00
  Group /units (Units) units table
  Dataset /units/electrodes (DynamicTableRegion) single electrodes | shape = (14,) | dtype = int32
  Dataset /units/id (ElementIdentifiers)  | shape = (14,) | dtype = int32
  Dataset /units/spike_times (VectorData) Timestamps when spikes occured (seconds) | shape = (128079,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) indexes data | shape = (14,) | dtype = uint64


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/LFPs (ElectricalSeries) These are LFP recordings that have been downsampled to 250 Hz
  Dataset /acquisition/LFPs/electrodes (DynamicTableRegion) single electrodes | shape = (39,) | dtype = int32
  Group /acquisition/events (TimeSeries) The events coorespond to the TTL markers for each trial. For the encoding trials, the TTL markers are the following: 61 = start of the experiment, 1 = stimulus ON, 2 = stimulus OFF, 11 = Fix Cross, 3 = Probe, 4 = Response, 60 = End of Experiment
  Group /acquisition/experiment_ids (TimeSeries) The experiment_ids correspond to the encoding, recognition or time discrimination trials. The encoding trials are demarcated by: 70. The recognition trials are demarcated by: 71. The time discrimination trials are demarcated by: 72
  file_create_date: ['2024-07-19T06:37:08.239635-07:00']
  Group /general/devices/NLX-microwires-129 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-130 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-131 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-132 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-133 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-134 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-135 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-137 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-138 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-139 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-141 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-142 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-144 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-145 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-146 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-147 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-148 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-149 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-150 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-151 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-152 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-154 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-155 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-156 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-157 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-159 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-160 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-161 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-162 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-164 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-165 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-168 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-169 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-170 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-171 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-173 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-174 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-175 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-176 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  experiment_description: This data contains electrophysiological recordings and behavior from the cognitive boundary task performed in patients with intractable epilepsy implanted with depth electrodes and Behnke-Fried microwires in the human Medical Temporal Lobe (MTL).
  experimenter: ['Kyzar, Michael']
  Group /general/extracellular_ephys/NLX-microwires-129 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-129/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-130 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-130/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-131 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-131/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-132 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-132/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-133 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-133/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-134 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-134/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-135 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-135/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-137 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-137/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-138 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-138/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-139 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-139/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-141 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-141/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-142 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-142/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-144 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-144/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-145 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-145/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-146 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-146/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-147 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-147/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-148 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-148/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-149 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-149/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-150 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-150/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-151 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-151/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-152 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-152/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-154 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-154/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-155 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-155/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-156 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-156/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-157 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-157/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-159 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-159/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-160 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-160/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-161 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-161/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-162 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-162/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-164 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-164/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-165 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-165/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-168 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-168/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-169 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-169/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-170 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-170/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-171 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-171/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-173 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-173/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-174 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-174/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-175 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-175/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-176 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-176/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/electrodes (DynamicTable) microwire electrodes table
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) my description | shape = (39,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) my description | shape = (39,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) my description | shape = (39,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (39,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) my description | shape = (39,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/origChannel (VectorData) my description | shape = (39,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) my description | shape = (39,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) my description | shape = (39,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) my description | shape = (39,) | dtype = float64
  institution: Cedars-Sinai Medical Center
  keywords: ['single neuron, human, intracranial']
  lab: Rutishauser
  notes: (1) Experiment variant: 1. (2) The session start time has been set to Jan 1st to avoid disclosure of protected health information (PHI).
  related_publications: ['doi: https://doi.org/10.1101/2023.06.05.543539']
  session_id: 1
  source_script: NWB_CBPP_export_main
  Group /general/subject (Subject) 
  identifier: sub-12_ses-1_P64CS
  Group /intervals/encoding_table (TimeIntervals) intervals for the encoding task
  Dataset /intervals/encoding_table/Clip_name (VectorData) video clip shown during this trial | shape = (90,) | dtype = object
  Dataset /intervals/encoding_table/ExperimentID (VectorData) EXPERIMENT_ID | shape = (90,) | dtype = float64
  Dataset /intervals/encoding_table/boundary1_time (VectorData) time of first boundary (0 if it does not exist; absolute timestamp). For no boundary (NB), this is equal to 4s (same as HB). For hard boundary (HB) clips, this is the time of the HB. For soft boundary (SB) clips, this is the time of the first SB. | shape = (90,) | dtype = float64
  Dataset /intervals/encoding_table/boundary2_time (VectorData) time of second boundary (0 if it does not exist; absolute timestamp). For HB clips, this is the time of first SB boundary. For SB clips, this is second SB boundary in the clip. | shape = (90,) | dtype = float64
  Dataset /intervals/encoding_table/boundary3_time (VectorData) time of third boundary (0 if it does not exist; absolute timestamp). For HB clips, thisis the time of the second SB boundary. For SB clips, this is the third SB boundary of the clip. | shape = (90,) | dtype = float64
  Dataset /intervals/encoding_table/fixcross_time (VectorData) fix cross time. TTL=11 | shape = (90,) | dtype = float64
  Dataset /intervals/encoding_table/id (ElementIdentifiers)  | shape = (90,) | dtype = int64
  Dataset /intervals/encoding_table/start_time (VectorData) start time of video. TTL=1 | shape = (90,) | dtype = float64
  Dataset /intervals/encoding_table/stimCategory (VectorData) 1=no boundary (NB), 2=soft boundary (SB), 3=hard boundary (HB). Note - HB clips can, in addition, also contain SB boundaries. | shape = (90,) | dtype = uint8
  Dataset /intervals/encoding_table/stop_time (VectorData) stop time of video. TTL=2 | shape = (90,) | dtype = float64
  Group /intervals/recognition_table (TimeIntervals) intervals for scene recognition task
  Dataset /intervals/recognition_table/ExperimentID (VectorData) EXPERIMENT_ID | shape = (180,) | dtype = float64
  Dataset /intervals/recognition_table/RT (VectorData) Reaction time | shape = (180,) | dtype = float64
  Dataset /intervals/recognition_table/accuracy (VectorData) correct = 2, incorrect 1, no response = 0 | shape = (180,) | dtype = uint8
  Dataset /intervals/recognition_table/boundary_type (VectorData) 1=no boundary (NB), 2=soft boundary (SB), 3=hard boundary (HB) | shape = (180,) | dtype = uint8
  Dataset /intervals/recognition_table/confidence (VectorData) 3 = high, 2 = medium, 1 = low | shape = (180,) | dtype = uint8
  Dataset /intervals/recognition_table/fixcross_time (VectorData) fix cross onset. TTL=11 | shape = (180,) | dtype = float64
  Dataset /intervals/recognition_table/frameName (VectorData) name of image shown | shape = (180,) | dtype = object
  Dataset /intervals/recognition_table/id (ElementIdentifiers)  | shape = (180,) | dtype = int64
  Dataset /intervals/recognition_table/old_new (VectorData) Response Old = 2, New = 1 | shape = (180,) | dtype = uint8
  Dataset /intervals/recognition_table/resp_value (VectorData) range = 2-7, -1=timeout | shape = (180,) | dtype = uint8
  Dataset /intervals/recognition_table/response_time (VectorData) fix cross onset. TTL=4 | shape = (180,) | dtype = float64
  Dataset /intervals/recognition_table/start_time (VectorData) start time of test frame. TTL=1 | shape = (180,) | dtype = float64
  Dataset /intervals/recognition_table/stimuli_type (VectorData) target (ground truth) = 1, foil = 0 | shape = (180,) | dtype = uint8
  Dataset /intervals/recognition_table/stop_time (VectorData) stop time of test frame. TTL=2 | shape = (180,) | dtype = float64
  Dataset /intervals/recognition_table/trial_num (VectorData) trial nr | shape = (180,) | dtype = uint8
  Group /intervals/timediscrimination_table (TimeIntervals) intervals for time discrimination task
  Dataset /intervals/timediscrimination_table/ExperimentID (VectorData) EXPERIMENT_ID | shape = (180,) | dtype = float64
  Dataset /intervals/timediscrimination_table/RT (VectorData) Reaction time | shape = (180,) | dtype = float64
  Dataset /intervals/timediscrimination_table/accuracy (VectorData) correct = 2, incorrect 1, no response = 0 | shape = (180,) | dtype = float64
  Dataset /intervals/timediscrimination_table/boundary_type (VectorData) 1=no boundary (NB), 2=soft boundary (SB), 3=hard boundary (HB) | shape = (180,) | dtype = uint8
  Dataset /intervals/timediscrimination_table/confidence (VectorData) 3 = high, 2 = medium, 1 = low | shape = (180,) | dtype = float64
  Dataset /intervals/timediscrimination_table/fixcross_time (VectorData) fix cross onset. TTL=11 | shape = (180,) | dtype = float64
  Dataset /intervals/timediscrimination_table/frameName (VectorData) name of image shown | shape = (180,) | dtype = object
  Dataset /intervals/timediscrimination_table/id (ElementIdentifiers)  | shape = (180,) | dtype = int64
  Dataset /intervals/timediscrimination_table/key (VectorData) left = 1, right = 2 | shape = (180,) | dtype = uint8
  Dataset /intervals/timediscrimination_table/leftright (VectorData) Left = 1, Right = 2 | shape = (180,) | dtype = uint8
  Dataset /intervals/timediscrimination_table/resp_value (VectorData) range = 2-7, -1=no response | shape = (180,) | dtype = uint8
  Dataset /intervals/timediscrimination_table/response_time (VectorData) fix cross onset. TTL=4 | shape = (180,) | dtype = float64
  Dataset /intervals/timediscrimination_table/start_time (VectorData) start time of test frame. TTL=1 | shape = (180,) | dtype = float64
  Dataset /intervals/timediscrimination_table/stop_time (VectorData) stop time of test frame. TTL=2 | shape = (180,) | dtype = float64
  Dataset /intervals/timediscrimination_table/trial_num (VectorData) trial nr | shape = (180,) | dtype = uint8
  session_description: CBPP: 1 CBPPID: 12
  session_start_time: 2018-01-01T00:00:00.000000-08:00
  Group /stimulus/presentation/ExternalVideos (OpticalSeries) Please contact authors for clips.
  timestamps_reference_time: 2018-01-01T00:00:00.000000-08:00
  Group /units (Units) units table
  Dataset /units/electrodes (DynamicTableRegion) single electrodes | shape = (79,) | dtype = int32
  Dataset /units/id (ElementIdentifiers)  | shape = (79,) | dtype = int32
  Dataset /units/spike_times (VectorData) Timestamps when spikes occured (seconds) | shape = (629728,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) indexes data | shape = (79,) | dtype = uint64


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  Group /acquisition/LFPs (ElectricalSeries) These are LFP recordings that have been downsampled to 250 Hz
  Dataset /acquisition/LFPs/electrodes (DynamicTableRegion) single electrodes | shape = (34,) | dtype = int32
  Group /acquisition/events (TimeSeries) The events coorespond to the TTL markers for each trial. For the encoding trials, the TTL markers are the following: 61 = start of the experiment, 1 = stimulus ON, 2 = stimulus OFF, 11 = Fix Cross, 3 = Probe, 4 = Response, 60 = End of Experiment
  Group /acquisition/experiment_ids (TimeSeries) The experiment_ids correspond to the encoding, recognition or time discrimination trials. The encoding trials are demarcated by: 70. The recognition trials are demarcated by: 71. The time discrimination trials are demarcated by: 72
  file_create_date: ['2024-07-19T06:37:24.585039-07:00']
  Group /general/devices/NLX-microwires-145 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-146 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-147 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-148 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-149 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-150 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-151 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-152 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-153 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-154 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-155 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-156 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-157 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-158 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-159 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-160 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-177 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-178 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-179 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-180 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-181 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-182 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-183 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-184 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-185 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-186 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-187 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-188 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-189 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-190 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-191 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-192 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-193 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-194 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  experiment_description: This data contains electrophysiological recordings and behavior from the cognitive boundary task performed in patients with intractable epilepsy implanted with depth electrodes and Behnke-Fried microwires in the human Medical Temporal Lobe (MTL).
  experimenter: ['Kyzar, Michael']
  Group /general/extracellular_ephys/NLX-microwires-145 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-145/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-146 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-146/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-147 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-147/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-148 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-148/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-149 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-149/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-150 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-150/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-151 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-151/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-152 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-152/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-153 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-153/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-154 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-154/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-155 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-155/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-156 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-156/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-157 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-157/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-158 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-158/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-159 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-159/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-160 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-160/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-177 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-177/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-178 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-178/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-179 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-179/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-180 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-180/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-181 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-181/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-182 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-182/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-183 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-183/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-184 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-184/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-185 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-185/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-186 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-186/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-187 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-187/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-188 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-188/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-189 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-189/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-190 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-190/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-191 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-191/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-192 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-192/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-193 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-193/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-194 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-194/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/electrodes (DynamicTable) microwire electrodes table
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) my description | shape = (34,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) my description | shape = (34,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) my description | shape = (34,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (34,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) my description | shape = (34,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/origChannel (VectorData) my description | shape = (34,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) my description | shape = (34,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) my description | shape = (34,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) my description | shape = (34,) | dtype = float64
  institution: Cedars-Sinai Medical Center
  keywords: ['single neuron, human, intracranial']
  lab: Rutishauser
  notes: (1) Experiment variant: 1. (2) The session start time has been set to Jan 1st to avoid disclosure of protected health information (PHI).
  related_publications: ['doi: https://doi.org/10.1101/2023.06.05.543539']
  session_id: 1
  source_script: NWB_CBPP_export_main
  Group /general/subject (Subject) 
  identifier: sub-13_ses-1_P65CS
  Group /intervals/encoding_table (TimeIntervals) intervals for the encoding task
  Dataset /intervals/encoding_table/Clip_name (VectorData) video clip shown during this trial | shape = (90,) | dtype = object
  Dataset /intervals/encoding_table/ExperimentID (VectorData) EXPERIMENT_ID | shape = (90,) | dtype = float64
  Dataset /intervals/encoding_table/boundary1_time (VectorData) time of first boundary (0 if it does not exist; absolute timestamp). For no boundary (NB), this is equal to 4s (same as HB). For hard boundary (HB) clips, this is the time of the HB. For soft boundary (SB) clips, this is the time of the first SB. | shape = (90,) | dtype = float64
  Dataset /intervals/encoding_table/boundary2_time (VectorData) time of second boundary (0 if it does not exist; absolute timestamp). For HB clips, this is the time of first SB boundary. For SB clips, this is second SB boundary in the clip. | shape = (90,) | dtype = float64
  Dataset /intervals/encoding_table/boundary3_time (VectorData) time of third boundary (0 if it does not exist; absolute timestamp). For HB clips, thisis the time of the second SB boundary. For SB clips, this is the third SB boundary of the clip. | shape = (90,) | dtype = float64
  Dataset /intervals/encoding_table/fixcross_time (VectorData) fix cross time. TTL=11 | shape = (90,) | dtype = float64
  Dataset /intervals/encoding_table/id (ElementIdentifiers)  | shape = (90,) | dtype = int64
  Dataset /intervals/encoding_table/start_time (VectorData) start time of video. TTL=1 | shape = (90,) | dtype = float64
  Dataset /intervals/encoding_table/stimCategory (VectorData) 1=no boundary (NB), 2=soft boundary (SB), 3=hard boundary (HB). Note - HB clips can, in addition, also contain SB boundaries. | shape = (90,) | dtype = uint8
  Dataset /intervals/encoding_table/stop_time (VectorData) stop time of video. TTL=2 | shape = (90,) | dtype = float64
  Group /intervals/recognition_table (TimeIntervals) intervals for scene recognition task
  Dataset /intervals/recognition_table/ExperimentID (VectorData) EXPERIMENT_ID | shape = (180,) | dtype = float64
  Dataset /intervals/recognition_table/RT (VectorData) Reaction time | shape = (180,) | dtype = float64
  Dataset /intervals/recognition_table/accuracy (VectorData) correct = 2, incorrect 1, no response = 0 | shape = (180,) | dtype = uint8
  Dataset /intervals/recognition_table/boundary_type (VectorData) 1=no boundary (NB), 2=soft boundary (SB), 3=hard boundary (HB) | shape = (180,) | dtype = uint8
  Dataset /intervals/recognition_table/confidence (VectorData) 3 = high, 2 = medium, 1 = low | shape = (180,) | dtype = uint8
  Dataset /intervals/recognition_table/fixcross_time (VectorData) fix cross onset. TTL=11 | shape = (180,) | dtype = float64
  Dataset /intervals/recognition_table/frameName (VectorData) name of image shown | shape = (180,) | dtype = object
  Dataset /intervals/recognition_table/id (ElementIdentifiers)  | shape = (180,) | dtype = int64
  Dataset /intervals/recognition_table/old_new (VectorData) Response Old = 2, New = 1 | shape = (180,) | dtype = uint8
  Dataset /intervals/recognition_table/resp_value (VectorData) range = 2-7, -1=timeout | shape = (180,) | dtype = uint8
  Dataset /intervals/recognition_table/response_time (VectorData) fix cross onset. TTL=4 | shape = (180,) | dtype = float64
  Dataset /intervals/recognition_table/start_time (VectorData) start time of test frame. TTL=1 | shape = (180,) | dtype = float64
  Dataset /intervals/recognition_table/stimuli_type (VectorData) target (ground truth) = 1, foil = 0 | shape = (180,) | dtype = uint8
  Dataset /intervals/recognition_table/stop_time (VectorData) stop time of test frame. TTL=2 | shape = (180,) | dtype = float64
  Dataset /intervals/recognition_table/trial_num (VectorData) trial nr | shape = (180,) | dtype = uint8
  Group /intervals/timediscrimination_table (TimeIntervals) intervals for time discrimination task
  Dataset /intervals/timediscrimination_table/ExperimentID (VectorData) EXPERIMENT_ID | shape = (180,) | dtype = float64
  Dataset /intervals/timediscrimination_table/RT (VectorData) Reaction time | shape = (180,) | dtype = float64
  Dataset /intervals/timediscrimination_table/accuracy (VectorData) correct = 2, incorrect 1, no response = 0 | shape = (180,) | dtype = float64
  Dataset /intervals/timediscrimination_table/boundary_type (VectorData) 1=no boundary (NB), 2=soft boundary (SB), 3=hard boundary (HB) | shape = (180,) | dtype = uint8
  Dataset /intervals/timediscrimination_table/confidence (VectorData) 3 = high, 2 = medium, 1 = low | shape = (180,) | dtype = float64
  Dataset /intervals/timediscrimination_table/fixcross_time (VectorData) fix cross onset. TTL=11 | shape = (180,) | dtype = float64
  Dataset /intervals/timediscrimination_table/frameName (VectorData) name of image shown | shape = (180,) | dtype = object
  Dataset /intervals/timediscrimination_table/id (ElementIdentifiers)  | shape = (180,) | dtype = int64
  Dataset /intervals/timediscrimination_table/key (VectorData) left = 1, right = 2 | shape = (180,) | dtype = uint8
  Dataset /intervals/timediscrimination_table/leftright (VectorData) Left = 1, Right = 2 | shape = (180,) | dtype = uint8
  Dataset /intervals/timediscrimination_table/resp_value (VectorData) range = 2-7, -1=no response | shape = (180,) | dtype = uint8
  Dataset /intervals/timediscrimination_table/response_time (VectorData) fix cross onset. TTL=4 | shape = (180,) | dtype = float64
  Dataset /intervals/timediscrimination_table/start_time (VectorData) start time of test frame. TTL=1 | shape = (180,) | dtype = float64
  Dataset /intervals/timediscrimination_table/stop_time (VectorData) stop time of test frame. TTL=2 | shape = (180,) | dtype = float64
  Dataset /intervals/timediscrimination_table/trial_num (VectorData) trial nr | shape = (180,) | dtype = uint8
  session_description: CBPP: 1 CBPPID: 13
  session_start_time: 2018-01-01T00:00:00.000000-08:00
  Group /stimulus/presentation/ExternalVideos (OpticalSeries) Please contact authors for clips.
  timestamps_reference_time: 2018-01-01T00:00:00.000000-08:00
  Group /units (Units) units table
  Dataset /units/electrodes (DynamicTableRegion) single electrodes | shape = (121,) | dtype = int32
  Dataset /units/id (ElementIdentifiers)  | shape = (121,) | dtype = int32
  Dataset /units/spike_times (VectorData) Timestamps when spikes occured (seconds) | shape = (413833,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) indexes data | shape = (121,) | dtype = uint64
