
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000207/0.230530.1822
name: Data for: Neurons detect cognitive boundaries to structure episodic memories in humans (Zheng et al., 2022, Nat Neuro in press)
contributor: [{'name': 'Zheng, Jie', 'email': 'jie.zheng@childrens.harvard.edu', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-9086-3760', 'affiliation': [{'name': 'Harvard Medical School', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/03vek6s52'}], 'includeInCitation': True}, {'name': 'Schjetnan, Andrea', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Yebra, Mar', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Gomes, Bernard', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Mosher, Clayton', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Kalia, Suneil', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Valiante, Taufik', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Mamelak, Adam', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Kreiman, Gabriel', 'email': 'gabriel.kreiman@childrens.harvard.edu', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0003-3505-8475', 'affiliation': [], 'includeInCitation': True}, {'url': 'https://www.rutishauserlab.org', 'name': 'Rutishauser, Ueli', 'email': 'urut@caltech.edu', 'roleName': ['dcite:ContactPerson', 'dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-9207-7069', 'affiliation': [{'name': 'Cedars-Sinai', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/02pammg90'}, {'name': 'Caltech', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/05dxps055'}], 'includeInCitation': True}, {'name': 'National Institutes of Health', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01cwqze88', 'awardNumber': 'U01NS103792, U01NS117839 ', 'contactPoint': [], 'includeInCitation': False}]
description: This dataset contains human single-neuron data recorded from the medial temporal lobe (MTL) during a set of experiments to explore the role of neurons that respond to cognitive boundaries. This dataset accompanies the paper cited below. Example code on how to plot this data can be found at https://github.com/rutishauserlab/cogboundary-zheng .

Reference (to be updated upon publication):  Cognitive boundary signals in the human medial temporal lobe shape episodic memory representation. Jie Zheng, Andrea Gómez Palacio Schjetnan, Mar Yebra, Clayton Mosher, Suneil Kalia, Taufik A. Valiante, Adam N. Mamelak, Gabriel Kreiman, Ueli Rutishauser. bioRxiv 2021.01.16.426538.  [Nat Neuro, in press, 2022]
assetsSummary: {'species': [{'name': 'Homo sapiens - Human', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9606'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 50310106, 'numberOfFiles': 19, 'numberOfSubjects': 19, 'variableMeasured': ['ElectrodeGroup', 'Units'], 'measurementTechnique': [{'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000207 has 5 NWB files.
1 of these NWB files are of type 1.
1 of these NWB files are of type 2.
1 of these NWB files are of type 3.
1 of these NWB files are of type 4.
1 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/events (TimeSeries) The events coorespond to the TTL markers for each trial. For the encoding trials, the TTL markers are the following: 61 = start of the experiment, 1 = stimulus ON, 2 = stimulus OFF, 11 = Fix Cross, 3 = Probe, 4 = Response, 60 = End of Experiment
  Group /acquisition/experiment_ids (TimeSeries) The experiment_ids correspond to the encoding, recognition or time discrimination trials. The encoding trials are demarcated by: 70. The recognition trials are demarcated by: 71. The time discrimination trials are demarcated by: 72
  file_create_date: ['2023-05-30T10:28:08.611663-04:00']
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
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (10,) | dtype = int8
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) my description | shape = (10,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) my description | shape = (10,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/origChannel (VectorData) my description | shape = (10,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) my description | shape = (10,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) my description | shape = (10,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) my description | shape = (10,) | dtype = float64
  lab: Rutishauser
  related_publications: ['Cognitive boundary signals in the human medial temporal lobe shape episodic memory representation. Jie Zheng, Andrea Gomez Palacio Schjetnan, Mar Yebra, Clayton Mosher, Suneil Kalia, Taufik A. Valiante, Adam N. Mamelak, Gabriel Kreiman, Ueli Rutishauser. Nat Neurosci, 2022 (in press)']
  session_id: 1
  source_script: CB_NWB_export_main.m
  Group /general/subject (Subject) 
  identifier: P60CS_CBID1
  Group /intervals/encoding_table (TimeIntervals) intervals for the encoding task
  Dataset /intervals/encoding_table/Clip_name (VectorData) video clip shown during this trial | shape = (90,) | dtype = object
  Dataset /intervals/encoding_table/ExperimentID (VectorData) EXPERIMENT_ID | shape = (90,) | dtype = float64
  Dataset /intervals/encoding_table/boundary1_time (VectorData) time of first boundary (0 if it does not exist; absolute timestamp). For no boundary (NB), this is equal to 4s (same as HB). For hard boundary (HB) clips, this is the time of the HB. For soft boundary (SB) clips, this is the time of the first SB. | shape = (90,) | dtype = float64
  Dataset /intervals/encoding_table/boundary2_time (VectorData) time of second boundary (0 if it does not exist; absolute timestamp). For HB clips, this is the time of first SB boundary. For SB clips, this is second SB boundary in the clip. | shape = (90,) | dtype = float64
  Dataset /intervals/encoding_table/boundary3_time (VectorData) time of third boundary (0 if it does not exist; absolute timestamp). For HB clips, thisis the time of the second SB boundary. For SB clips, this is the third SB boundary of the clip. | shape = (90,) | dtype = float64
  Dataset /intervals/encoding_table/fixcross_time (VectorData) fix cross time. TTL=11 | shape = (90,) | dtype = float64
  Dataset /intervals/encoding_table/id (ElementIdentifiers)  | shape = (90,) | dtype = int8
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
  Dataset /intervals/recognition_table/id (ElementIdentifiers)  | shape = (180,) | dtype = int16
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
  Dataset /intervals/timediscrimination_table/id (ElementIdentifiers)  | shape = (180,) | dtype = int16
  Dataset /intervals/timediscrimination_table/key (VectorData) left = 1, right = 2 | shape = (180,) | dtype = uint8
  Dataset /intervals/timediscrimination_table/leftright (VectorData) Left = 1, Right = 2 | shape = (180,) | dtype = uint8
  Dataset /intervals/timediscrimination_table/resp_value (VectorData) range = 2-7, -1=no response | shape = (180,) | dtype = uint8
  Dataset /intervals/timediscrimination_table/response_time (VectorData) fix cross onset. TTL=4 | shape = (180,) | dtype = float64
  Dataset /intervals/timediscrimination_table/start_time (VectorData) start time of test frame. TTL=1 | shape = (180,) | dtype = float64
  Dataset /intervals/timediscrimination_table/stop_time (VectorData) stop time of test frame. TTL=2 | shape = (180,) | dtype = float64
  Dataset /intervals/timediscrimination_table/trial_num (VectorData) trial nr | shape = (180,) | dtype = uint8
  session_description: CB: 1 CBID: 1
  session_start_time: 1900-01-01T00:00:00.000000-05:00
  timestamps_reference_time: 1900-01-01T00:00:00.000000-05:00
  Group /units (Units) units table
  Dataset /units/electrodes (DynamicTableRegion) single electrodes | shape = (43,) | dtype = int8
  Dataset /units/id (ElementIdentifiers)  | shape = (43,) | dtype = int64
  Dataset /units/spike_times (VectorData) no description | shape = (603265,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) indexes data | shape = (43,) | dtype = uint32


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/events (TimeSeries) The events coorespond to the TTL markers for each trial. For the encoding trials, the TTL markers are the following: 61 = start of the experiment, 1 = stimulus ON, 2 = stimulus OFF, 11 = Fix Cross, 3 = Probe, 4 = Response, 60 = End of Experiment
  Group /acquisition/experiment_ids (TimeSeries) The experiment_ids correspond to the encoding, recognition or time discrimination trials. The encoding trials are demarcated by: 70. The recognition trials are demarcated by: 71. The time discrimination trials are demarcated by: 72
  file_create_date: ['2023-05-30T10:28:16.606539-04:00']
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
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (13,) | dtype = int8
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) my description | shape = (13,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) my description | shape = (13,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/origChannel (VectorData) my description | shape = (13,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) my description | shape = (13,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) my description | shape = (13,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) my description | shape = (13,) | dtype = float64
  lab: Rutishauser
  related_publications: ['Cognitive boundary signals in the human medial temporal lobe shape episodic memory representation. Jie Zheng, Andrea Gomez Palacio Schjetnan, Mar Yebra, Clayton Mosher, Suneil Kalia, Taufik A. Valiante, Adam N. Mamelak, Gabriel Kreiman, Ueli Rutishauser. Nat Neurosci, 2022 (in press)']
  session_id: 10
  source_script: CB_NWB_export_main.m
  Group /general/subject (Subject) 
  identifier: TWH116_CBID10
  Group /intervals/encoding_table (TimeIntervals) intervals for the encoding task
  Dataset /intervals/encoding_table/Clip_name (VectorData) video clip shown during this trial | shape = (90,) | dtype = object
  Dataset /intervals/encoding_table/ExperimentID (VectorData) EXPERIMENT_ID | shape = (90,) | dtype = float64
  Dataset /intervals/encoding_table/boundary1_time (VectorData) time of first boundary (0 if it does not exist; absolute timestamp). For no boundary (NB), this is equal to 4s (same as HB). For hard boundary (HB) clips, this is the time of the HB. For soft boundary (SB) clips, this is the time of the first SB. | shape = (90,) | dtype = float64
  Dataset /intervals/encoding_table/boundary2_time (VectorData) time of second boundary (0 if it does not exist; absolute timestamp). For HB clips, this is the time of first SB boundary. For SB clips, this is second SB boundary in the clip. | shape = (90,) | dtype = float64
  Dataset /intervals/encoding_table/boundary3_time (VectorData) time of third boundary (0 if it does not exist; absolute timestamp). For HB clips, thisis the time of the second SB boundary. For SB clips, this is the third SB boundary of the clip. | shape = (90,) | dtype = float64
  Dataset /intervals/encoding_table/fixcross_time (VectorData) fix cross time. TTL=11 | shape = (90,) | dtype = float64
  Dataset /intervals/encoding_table/id (ElementIdentifiers)  | shape = (90,) | dtype = int8
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
  Dataset /intervals/recognition_table/id (ElementIdentifiers)  | shape = (180,) | dtype = int16
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
  Dataset /intervals/timediscrimination_table/id (ElementIdentifiers)  | shape = (180,) | dtype = int16
  Dataset /intervals/timediscrimination_table/key (VectorData) left = 1, right = 2 | shape = (180,) | dtype = uint8
  Dataset /intervals/timediscrimination_table/leftright (VectorData) Left = 1, Right = 2 | shape = (180,) | dtype = uint8
  Dataset /intervals/timediscrimination_table/resp_value (VectorData) range = 2-7, -1=no response | shape = (180,) | dtype = uint8
  Dataset /intervals/timediscrimination_table/response_time (VectorData) fix cross onset. TTL=4 | shape = (180,) | dtype = float64
  Dataset /intervals/timediscrimination_table/start_time (VectorData) start time of test frame. TTL=1 | shape = (180,) | dtype = float64
  Dataset /intervals/timediscrimination_table/stop_time (VectorData) stop time of test frame. TTL=2 | shape = (180,) | dtype = float64
  Dataset /intervals/timediscrimination_table/trial_num (VectorData) trial nr | shape = (180,) | dtype = uint8
  session_description: CB: 1 CBID: 10
  session_start_time: 1900-01-01T00:00:00.000000-05:00
  timestamps_reference_time: 1900-01-01T00:00:00.000000-05:00
  Group /units (Units) units table
  Dataset /units/electrodes (DynamicTableRegion) single electrodes | shape = (27,) | dtype = int8
  Dataset /units/id (ElementIdentifiers)  | shape = (27,) | dtype = int64
  Dataset /units/spike_times (VectorData) no description | shape = (140083,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) indexes data | shape = (27,) | dtype = uint32


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/events (TimeSeries) The events coorespond to the TTL markers for each trial. For the encoding trials, the TTL markers are the following: 61 = start of the experiment, 1 = stimulus ON, 2 = stimulus OFF, 11 = Fix Cross, 3 = Probe, 4 = Response, 60 = End of Experiment
  Group /acquisition/experiment_ids (TimeSeries) The experiment_ids correspond to the encoding, recognition or time discrimination trials. The encoding trials are demarcated by: 70. The recognition trials are demarcated by: 71. The time discrimination trials are demarcated by: 72
  file_create_date: ['2023-05-30T10:28:17.303244-04:00']
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
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (11,) | dtype = int8
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) my description | shape = (11,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) my description | shape = (11,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/origChannel (VectorData) my description | shape = (11,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) my description | shape = (11,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) my description | shape = (11,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) my description | shape = (11,) | dtype = float64
  lab: Rutishauser
  related_publications: ['Cognitive boundary signals in the human medial temporal lobe shape episodic memory representation. Jie Zheng, Andrea Gomez Palacio Schjetnan, Mar Yebra, Clayton Mosher, Suneil Kalia, Taufik A. Valiante, Adam N. Mamelak, Gabriel Kreiman, Ueli Rutishauser. Nat Neurosci, 2022 (in press)']
  session_id: 11
  source_script: CB_NWB_export_main.m
  Group /general/subject (Subject) 
  identifier: TWH117_CBID11
  Group /intervals/encoding_table (TimeIntervals) intervals for the encoding task
  Dataset /intervals/encoding_table/Clip_name (VectorData) video clip shown during this trial | shape = (90,) | dtype = object
  Dataset /intervals/encoding_table/ExperimentID (VectorData) EXPERIMENT_ID | shape = (90,) | dtype = float64
  Dataset /intervals/encoding_table/boundary1_time (VectorData) time of first boundary (0 if it does not exist; absolute timestamp). For no boundary (NB), this is equal to 4s (same as HB). For hard boundary (HB) clips, this is the time of the HB. For soft boundary (SB) clips, this is the time of the first SB. | shape = (90,) | dtype = float64
  Dataset /intervals/encoding_table/boundary2_time (VectorData) time of second boundary (0 if it does not exist; absolute timestamp). For HB clips, this is the time of first SB boundary. For SB clips, this is second SB boundary in the clip. | shape = (90,) | dtype = float64
  Dataset /intervals/encoding_table/boundary3_time (VectorData) time of third boundary (0 if it does not exist; absolute timestamp). For HB clips, thisis the time of the second SB boundary. For SB clips, this is the third SB boundary of the clip. | shape = (90,) | dtype = float64
  Dataset /intervals/encoding_table/fixcross_time (VectorData) fix cross time. TTL=11 | shape = (90,) | dtype = float64
  Dataset /intervals/encoding_table/id (ElementIdentifiers)  | shape = (90,) | dtype = int8
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
  Dataset /intervals/recognition_table/id (ElementIdentifiers)  | shape = (180,) | dtype = int16
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
  Dataset /intervals/timediscrimination_table/id (ElementIdentifiers)  | shape = (180,) | dtype = int16
  Dataset /intervals/timediscrimination_table/key (VectorData) left = 1, right = 2 | shape = (180,) | dtype = uint8
  Dataset /intervals/timediscrimination_table/leftright (VectorData) Left = 1, Right = 2 | shape = (180,) | dtype = uint8
  Dataset /intervals/timediscrimination_table/resp_value (VectorData) range = 2-7, -1=no response | shape = (180,) | dtype = uint8
  Dataset /intervals/timediscrimination_table/response_time (VectorData) fix cross onset. TTL=4 | shape = (180,) | dtype = float64
  Dataset /intervals/timediscrimination_table/start_time (VectorData) start time of test frame. TTL=1 | shape = (180,) | dtype = float64
  Dataset /intervals/timediscrimination_table/stop_time (VectorData) stop time of test frame. TTL=2 | shape = (180,) | dtype = float64
  Dataset /intervals/timediscrimination_table/trial_num (VectorData) trial nr | shape = (180,) | dtype = uint8
  session_description: CB: 1 CBID: 11
  session_start_time: 1900-01-01T00:00:00.000000-05:00
  timestamps_reference_time: 1900-01-01T00:00:00.000000-05:00
  Group /units (Units) units table
  Dataset /units/electrodes (DynamicTableRegion) single electrodes | shape = (14,) | dtype = int8
  Dataset /units/id (ElementIdentifiers)  | shape = (14,) | dtype = int64
  Dataset /units/spike_times (VectorData) no description | shape = (128079,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) indexes data | shape = (14,) | dtype = uint32


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/events (TimeSeries) The events coorespond to the TTL markers for each trial. For the encoding trials, the TTL markers are the following: 61 = start of the experiment, 1 = stimulus ON, 2 = stimulus OFF, 11 = Fix Cross, 3 = Probe, 4 = Response, 60 = End of Experiment
  Group /acquisition/experiment_ids (TimeSeries) The experiment_ids correspond to the encoding, recognition or time discrimination trials. The encoding trials are demarcated by: 70. The recognition trials are demarcated by: 71. The time discrimination trials are demarcated by: 72
  file_create_date: ['2023-05-30T10:28:18.011549-04:00']
  Group /general/devices/NLX-microwires-145 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-146 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-147 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-148 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-150 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-151 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-152 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-154 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-155 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-156 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-157 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-159 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-160 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  experiment_description: This data contains electrophysiological recordings and behavior from the cognitive boundary task performed in patients with intractable epilepsy implanted with depth electrodes and Behnke-Fried microwires in the human Medical Temporal Lobe (MTL).
  Group /general/extracellular_ephys/NLX-microwires-145 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-145/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-146 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-146/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-147 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-147/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-148 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-148/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
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
  Group /general/extracellular_ephys/electrodes (DynamicTable) microwire electrodes table
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) my description | shape = (13,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) my description | shape = (13,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) my description | shape = (13,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (13,) | dtype = int8
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) my description | shape = (13,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) my description | shape = (13,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/origChannel (VectorData) my description | shape = (13,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) my description | shape = (13,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) my description | shape = (13,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) my description | shape = (13,) | dtype = float64
  lab: Rutishauser
  related_publications: ['Cognitive boundary signals in the human medial temporal lobe shape episodic memory representation. Jie Zheng, Andrea Gomez Palacio Schjetnan, Mar Yebra, Clayton Mosher, Suneil Kalia, Taufik A. Valiante, Adam N. Mamelak, Gabriel Kreiman, Ueli Rutishauser. Nat Neurosci, 2022 (in press)']
  session_id: 12
  source_script: CB_NWB_export_main.m
  Group /general/subject (Subject) 
  identifier: P64CS_CBID12
  Group /intervals/encoding_table (TimeIntervals) intervals for the encoding task
  Dataset /intervals/encoding_table/Clip_name (VectorData) video clip shown during this trial | shape = (90,) | dtype = object
  Dataset /intervals/encoding_table/ExperimentID (VectorData) EXPERIMENT_ID | shape = (90,) | dtype = float64
  Dataset /intervals/encoding_table/boundary1_time (VectorData) time of first boundary (0 if it does not exist; absolute timestamp). For no boundary (NB), this is equal to 4s (same as HB). For hard boundary (HB) clips, this is the time of the HB. For soft boundary (SB) clips, this is the time of the first SB. | shape = (90,) | dtype = float64
  Dataset /intervals/encoding_table/boundary2_time (VectorData) time of second boundary (0 if it does not exist; absolute timestamp). For HB clips, this is the time of first SB boundary. For SB clips, this is second SB boundary in the clip. | shape = (90,) | dtype = float64
  Dataset /intervals/encoding_table/boundary3_time (VectorData) time of third boundary (0 if it does not exist; absolute timestamp). For HB clips, thisis the time of the second SB boundary. For SB clips, this is the third SB boundary of the clip. | shape = (90,) | dtype = float64
  Dataset /intervals/encoding_table/fixcross_time (VectorData) fix cross time. TTL=11 | shape = (90,) | dtype = float64
  Dataset /intervals/encoding_table/id (ElementIdentifiers)  | shape = (90,) | dtype = int8
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
  Dataset /intervals/recognition_table/id (ElementIdentifiers)  | shape = (180,) | dtype = int16
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
  Dataset /intervals/timediscrimination_table/id (ElementIdentifiers)  | shape = (180,) | dtype = int16
  Dataset /intervals/timediscrimination_table/key (VectorData) left = 1, right = 2 | shape = (180,) | dtype = uint8
  Dataset /intervals/timediscrimination_table/leftright (VectorData) Left = 1, Right = 2 | shape = (180,) | dtype = uint8
  Dataset /intervals/timediscrimination_table/resp_value (VectorData) range = 2-7, -1=no response | shape = (180,) | dtype = uint8
  Dataset /intervals/timediscrimination_table/response_time (VectorData) fix cross onset. TTL=4 | shape = (180,) | dtype = float64
  Dataset /intervals/timediscrimination_table/start_time (VectorData) start time of test frame. TTL=1 | shape = (180,) | dtype = float64
  Dataset /intervals/timediscrimination_table/stop_time (VectorData) stop time of test frame. TTL=2 | shape = (180,) | dtype = float64
  Dataset /intervals/timediscrimination_table/trial_num (VectorData) trial nr | shape = (180,) | dtype = uint8
  session_description: CB: 1 CBID: 12
  session_start_time: 1900-01-01T00:00:00.000000-05:00
  timestamps_reference_time: 1900-01-01T00:00:00.000000-05:00
  Group /units (Units) units table
  Dataset /units/electrodes (DynamicTableRegion) single electrodes | shape = (28,) | dtype = int8
  Dataset /units/id (ElementIdentifiers)  | shape = (28,) | dtype = int64
  Dataset /units/spike_times (VectorData) no description | shape = (266463,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) indexes data | shape = (28,) | dtype = uint32


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  Group /acquisition/events (TimeSeries) The events coorespond to the TTL markers for each trial. For the encoding trials, the TTL markers are the following: 61 = start of the experiment, 1 = stimulus ON, 2 = stimulus OFF, 11 = Fix Cross, 3 = Probe, 4 = Response, 60 = End of Experiment
  Group /acquisition/experiment_ids (TimeSeries) The experiment_ids correspond to the encoding, recognition or time discrimination trials. The encoding trials are demarcated by: 70. The recognition trials are demarcated by: 71. The time discrimination trials are demarcated by: 72
  file_create_date: ['2023-05-30T10:28:18.727869-04:00']
  Group /general/devices/NLX-microwires-145 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-146 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-148 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-149 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-150 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-151 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-152 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-154 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-156 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-157 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-158 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-159 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-178 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-180 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-181 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-182 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-183 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-184 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-186 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-190 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-191 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/devices/NLX-microwires-192 (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  experiment_description: This data contains electrophysiological recordings and behavior from the cognitive boundary task performed in patients with intractable epilepsy implanted with depth electrodes and Behnke-Fried microwires in the human Medical Temporal Lobe (MTL).
  Group /general/extracellular_ephys/NLX-microwires-145 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-145/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-146 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-146/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
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
  Group /general/extracellular_ephys/NLX-microwires-156 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-156/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-157 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-157/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-158 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-158/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-159 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-159/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-178 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-178/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
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
  Group /general/extracellular_ephys/NLX-microwires-186 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-186/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-190 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-190/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-191 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-191/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/NLX-microwires-192 (ElectrodeGroup) Microwire
  Group /general/extracellular_ephys/NLX-microwires-192/device (Device) Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electrode has 8 microwires.
  Group /general/extracellular_ephys/electrodes (DynamicTable) microwire electrodes table
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) my description | shape = (22,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) my description | shape = (22,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) my description | shape = (22,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (22,) | dtype = int8
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) my description | shape = (22,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) my description | shape = (22,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/origChannel (VectorData) my description | shape = (22,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) my description | shape = (22,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) my description | shape = (22,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) my description | shape = (22,) | dtype = float64
  lab: Rutishauser
  related_publications: ['Cognitive boundary signals in the human medial temporal lobe shape episodic memory representation. Jie Zheng, Andrea Gomez Palacio Schjetnan, Mar Yebra, Clayton Mosher, Suneil Kalia, Taufik A. Valiante, Adam N. Mamelak, Gabriel Kreiman, Ueli Rutishauser. Nat Neurosci, 2022 (in press)']
  session_id: 13
  source_script: CB_NWB_export_main.m
  Group /general/subject (Subject) 
  identifier: P65CS_CBID13
  Group /intervals/encoding_table (TimeIntervals) intervals for the encoding task
  Dataset /intervals/encoding_table/Clip_name (VectorData) video clip shown during this trial | shape = (90,) | dtype = object
  Dataset /intervals/encoding_table/ExperimentID (VectorData) EXPERIMENT_ID | shape = (90,) | dtype = float64
  Dataset /intervals/encoding_table/boundary1_time (VectorData) time of first boundary (0 if it does not exist; absolute timestamp). For no boundary (NB), this is equal to 4s (same as HB). For hard boundary (HB) clips, this is the time of the HB. For soft boundary (SB) clips, this is the time of the first SB. | shape = (90,) | dtype = float64
  Dataset /intervals/encoding_table/boundary2_time (VectorData) time of second boundary (0 if it does not exist; absolute timestamp). For HB clips, this is the time of first SB boundary. For SB clips, this is second SB boundary in the clip. | shape = (90,) | dtype = float64
  Dataset /intervals/encoding_table/boundary3_time (VectorData) time of third boundary (0 if it does not exist; absolute timestamp). For HB clips, thisis the time of the second SB boundary. For SB clips, this is the third SB boundary of the clip. | shape = (90,) | dtype = float64
  Dataset /intervals/encoding_table/fixcross_time (VectorData) fix cross time. TTL=11 | shape = (90,) | dtype = float64
  Dataset /intervals/encoding_table/id (ElementIdentifiers)  | shape = (90,) | dtype = int8
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
  Dataset /intervals/recognition_table/id (ElementIdentifiers)  | shape = (180,) | dtype = int16
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
  Dataset /intervals/timediscrimination_table/id (ElementIdentifiers)  | shape = (180,) | dtype = int16
  Dataset /intervals/timediscrimination_table/key (VectorData) left = 1, right = 2 | shape = (180,) | dtype = uint8
  Dataset /intervals/timediscrimination_table/leftright (VectorData) Left = 1, Right = 2 | shape = (180,) | dtype = uint8
  Dataset /intervals/timediscrimination_table/resp_value (VectorData) range = 2-7, -1=no response | shape = (180,) | dtype = uint8
  Dataset /intervals/timediscrimination_table/response_time (VectorData) fix cross onset. TTL=4 | shape = (180,) | dtype = float64
  Dataset /intervals/timediscrimination_table/start_time (VectorData) start time of test frame. TTL=1 | shape = (180,) | dtype = float64
  Dataset /intervals/timediscrimination_table/stop_time (VectorData) stop time of test frame. TTL=2 | shape = (180,) | dtype = float64
  Dataset /intervals/timediscrimination_table/trial_num (VectorData) trial nr | shape = (180,) | dtype = uint8
  session_description: CB: 1 CBID: 13
  session_start_time: 1900-01-01T00:00:00.000000-05:00
  timestamps_reference_time: 1900-01-01T00:00:00.000000-05:00
  Group /units (Units) units table
  Dataset /units/electrodes (DynamicTableRegion) single electrodes | shape = (48,) | dtype = int8
  Dataset /units/id (ElementIdentifiers)  | shape = (48,) | dtype = int64
  Dataset /units/spike_times (VectorData) no description | shape = (229005,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) indexes data | shape = (48,) | dtype = uint32
