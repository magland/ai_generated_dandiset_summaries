
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001347/0.250528.0702
name: Brain-wide human electrophysiology during aversive stimuli and ketamine
contributor: [{'name': 'National Institutes of Health (NIH)', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': '1 P50 DA 042012-01A1'}, {'name': 'Liu, Tony X', 'email': 'txliu@stanford.edu', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0001-9334-8492', 'includeInCitation': True}, {'name': 'Kauvar, Isaac', 'email': 'ikauvar@stanford.edu', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0002-1336-0721', 'includeInCitation': True}, {'name': 'Richman, Ethan', 'email': 'erichamc@gmail.com', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0001-8471-266X', 'includeInCitation': True}]
description: Brain-wide human electrophysiology associated with Kauvar*, Richman*, Liu* et al Science (2025). 

Regarding data folders, subjects with prefix "SD" indicate iEEG human participants, "h" indicate non-iEEG eyepuff human participants, and "m" indicate mice. Notably, "H" and "mouse" folders include cross-participant aggregated data. 
assetsSummary: {'species': [{'name': 'Homo sapiens - Human', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9606'}, {'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}, {'name': 'behavioral approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 16035455232, 'numberOfFiles': 207, 'numberOfSubjects': 173, 'variableMeasured': ['LFP', 'ElectricalSeries', 'ProcessingModule', 'ElectrodeGroup', 'BehavioralTimeSeries'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'signal filtering technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 001347 has 5 NWB files.
1 of these NWB files are of type 1.
1 of these NWB files are of type 2.
1 of these NWB files are of type 3.
1 of these NWB files are of type 4.
1 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2025-02-23T19:13:27.945390-05:00']
  experiment_description: regional and Yeo-network ketamine change in response to eyepuff, with key clusters
  experimenter: ['Kauvar, Isaac' 'Richman, Ethan' 'Liu, Tony']
  institution: Stanford University
  keywords: ['emotion' 'brain-wide' 'airpuff']
  lab: Karl Deisseroth Lab
  Group /general/subject (Subject) 
  identifier: kauvar-richman-liu-fig3
  Dataset /scratch/ACC_change (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/ACC_contour (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/AG_change (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/AG_contour (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/AMY_change (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/AMY_contour (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/BG_change (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/BG_contour (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/CS_change (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/CS_contour (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/Default_change (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/Default_contour (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/Dorsal Attention_change (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/Dorsal Attention_contour (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/FG_change (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/FG_contour (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/FO_change (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/FO_contour (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/Frontoparietal_change (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/Frontoparietal_contour (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/HIPP_change (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/HIPP_contour (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/IFG_change (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/IFG_contour (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/INS_change (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/INS_contour (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/ITG_change (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/ITG_contour (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/Limbic_change (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/Limbic_contour (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/MCC_change (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/MCC_contour (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/MFC_change (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/MFC_contour (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/MFG_change (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/MFG_contour (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/MOG_change (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/MOG_contour (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/MOT_change (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/MOT_contour (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/MSFG_change (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/MSFG_contour (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/MTG_change (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/MTG_contour (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/OP_change (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/OP_contour (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/ORB_change (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/ORB_contour (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/PHG_change (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/PHG_contour (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/PMC_change (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/PMC_contour (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/PRECG_change (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/PRECG_contour (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/SMG_change (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/SMG_contour (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/SPL_change (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/SPL_contour (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/SS_change (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/SS_contour (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/STG_change (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/STG_contour (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/STS_change (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/STS_contour (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/Somatomotor_change (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/Somatomotor_contour (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/THAL ANT_change (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/THAL ANT_contour (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/THAL MID_change (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/THAL MID_contour (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/THAL POS_change (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/THAL POS_contour (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/TP_change (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/TP_contour (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/VMPFC_change (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/VMPFC_contour (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/Ventral Attention_change (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/Ventral Attention_contour (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/Visual_change (ScratchData)  | shape = (65, 40) | dtype = float64
  Dataset /scratch/Visual_contour (ScratchData)  | shape = (65, 40) | dtype = float64
  Group /scratch/freq_hz (DynamicTable) Labels for the frequency dimension
  Dataset /scratch/freq_hz/frequency (VectorData) Frequency value | shape = (65,) | dtype = float64
  Dataset /scratch/freq_hz/id (ElementIdentifiers)  | shape = (65,) | dtype = int64
  Dataset /scratch/freq_hz/index (VectorData) Index in the matrix | shape = (65,) | dtype = int64
  Group /scratch/time_sec (DynamicTable) Labels for the time dimension
  Dataset /scratch/time_sec/id (ElementIdentifiers)  | shape = (40,) | dtype = int64
  Dataset /scratch/time_sec/index (VectorData) Index in the matrix | shape = (40,) | dtype = int64
  Dataset /scratch/time_sec/time (VectorData) Time point | shape = (40,) | dtype = float64
  session_description: Permutation-clustered ketamine change in regional SEEG spectral response to eyepuff. See `data` and `description` attributes of ScratchData objects for change spectrograms and contours.
  session_start_time: 2000-01-01T12:00:00-08:00
  timestamps_reference_time: 2000-01-01T12:00:00-08:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2025-02-23T19:24:14.786158-05:00']
  experiment_description: NMF factorization of bipolar electrode response to eyepuff
  experimenter: ['Kauvar, Isaac' 'Richman, Ethan' 'Liu, Tony']
  institution: Stanford University
  keywords: ['emotion' 'brain-wide' 'airpuff']
  lab: Karl Deisseroth Lab
  Group /general/subject (Subject) 
  identifier: kauvar-richman-liu-fig2G
  Dataset /scratch/factor_0 (ScratchData)  | shape = (65, 28) | dtype = float64
  Dataset /scratch/factor_1 (ScratchData)  | shape = (65, 28) | dtype = float64
  Dataset /scratch/factor_2 (ScratchData)  | shape = (65, 28) | dtype = float64
  Dataset /scratch/factor_3 (ScratchData)  | shape = (65, 28) | dtype = float64
  Dataset /scratch/factor_4 (ScratchData)  | shape = (65, 28) | dtype = float64
  Dataset /scratch/factor_5 (ScratchData)  | shape = (65, 28) | dtype = float64
  Group /scratch/freq_hz (DynamicTable) Labels for the frequency dimension
  Dataset /scratch/freq_hz/frequency (VectorData) Frequency value | shape = (65,) | dtype = float64
  Dataset /scratch/freq_hz/id (ElementIdentifiers)  | shape = (65,) | dtype = int64
  Dataset /scratch/freq_hz/index (VectorData) Index in the matrix | shape = (65,) | dtype = int64
  Group /scratch/time_sec (DynamicTable) Labels for the time dimension
  Dataset /scratch/time_sec/id (ElementIdentifiers)  | shape = (28,) | dtype = int64
  Dataset /scratch/time_sec/index (VectorData) Index in the matrix | shape = (28,) | dtype = int64
  Dataset /scratch/time_sec/time (VectorData) Time point | shape = (28,) | dtype = float64
  session_description: NMF factors of multichannel SEEG spectral response to eyepuff
  session_start_time: 2000-01-01T12:00:00-08:00
  timestamps_reference_time: 2000-01-01T12:00:00-08:00


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2025-02-23T19:24:15.077880-05:00']
  experiment_description: NMF loadings of bipolar electrode response to eyepuff
  experimenter: ['Kauvar, Isaac' 'Richman, Ethan' 'Liu, Tony']
  institution: Stanford University
  keywords: ['emotion' 'brain-wide' 'airpuff']
  lab: Karl Deisseroth Lab
  Group /general/subject (Subject) 
  identifier: kauvar-richman-liu-fig2HIJ
  Group /scratch/channel (DynamicTable) Labels for the channels, format [region]_[patient]_[bipolar_electrode]
  Dataset /scratch/channel/channel (VectorData) Channel name | shape = (458,) | dtype = object
  Dataset /scratch/channel/id (ElementIdentifiers)  | shape = (458,) | dtype = int64
  Dataset /scratch/channel/index (VectorData) Index in the matrix | shape = (458,) | dtype = int64
  Dataset /scratch/channel_loading_mtx_inf (ScratchData)  | shape = (458, 6) | dtype = float64
  Dataset /scratch/channel_loading_mtx_post (ScratchData)  | shape = (458, 6) | dtype = float64
  Dataset /scratch/channel_loading_mtx_pre (ScratchData)  | shape = (458, 6) | dtype = float64
  Group /scratch/yeo (DynamicTable) Labels for the Yeo networks
  Dataset /scratch/yeo/id (ElementIdentifiers)  | shape = (6,) | dtype = int64
  Dataset /scratch/yeo/index (VectorData) Index in the matrix | shape = (6,) | dtype = int64
  Dataset /scratch/yeo/yeo_network (VectorData) Yeo network | shape = (6,) | dtype = object
  Dataset /scratch/yeo_loading_mtx_inf_minus_pre (ScratchData)  | shape = (6, 6) | dtype = float64
  Dataset /scratch/yeo_loading_mtx_pre (ScratchData)  | shape = (6, 6) | dtype = float64
  session_description: NMF loadings of multichannel SEEG spectral response to eyepuff
  session_start_time: 2000-01-01T12:00:00-08:00
  timestamps_reference_time: 2000-01-01T12:00:00-08:00


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2025-02-23T19:24:15.532819-05:00']
  experiment_description: Multitaper spectrograms of bipolar electrode response to eyepuff
  experimenter: ['Kauvar, Isaac' 'Richman, Ethan' 'Liu, Tony']
  institution: Stanford University
  keywords: ['emotion' 'brain-wide' 'airpuff']
  lab: Karl Deisseroth Lab
  Group /general/subject (Subject) 
  identifier: kauvar-richman-liu-processed_data
  Group /scratch/channel (DynamicTable) Labels for the channels, format [region]_[patient]_[bipolar_electrode]
  Dataset /scratch/channel/channel (VectorData) Channel name | shape = (458,) | dtype = object
  Dataset /scratch/channel/id (ElementIdentifiers)  | shape = (458,) | dtype = int64
  Dataset /scratch/channel/index (VectorData) Index in the matrix | shape = (458,) | dtype = int64
  Group /scratch/freq_hz (DynamicTable) Labels for the frequency dimension
  Dataset /scratch/freq_hz/frequency (VectorData) Frequency value | shape = (65,) | dtype = float64
  Dataset /scratch/freq_hz/id (ElementIdentifiers)  | shape = (65,) | dtype = int64
  Dataset /scratch/freq_hz/index (VectorData) Index in the matrix | shape = (65,) | dtype = int64
  Dataset /scratch/puff_sgram_inf_test_trials (ScratchData)  | shape = (458, 65, 28) | dtype = float64
  Dataset /scratch/puff_sgram_inf_train_trials (ScratchData)  | shape = (458, 65, 28) | dtype = float64
  Dataset /scratch/puff_sgram_post_test_trials (ScratchData)  | shape = (458, 65, 28) | dtype = float64
  Dataset /scratch/puff_sgram_post_train_trials (ScratchData)  | shape = (458, 65, 28) | dtype = float64
  Dataset /scratch/puff_sgram_pre_test_trials (ScratchData)  | shape = (458, 65, 28) | dtype = float64
  Dataset /scratch/puff_sgram_pre_train_trials (ScratchData)  | shape = (458, 65, 28) | dtype = float64
  Group /scratch/time_sec (DynamicTable) Labels for the time dimension
  Dataset /scratch/time_sec/id (ElementIdentifiers)  | shape = (28,) | dtype = int64
  Dataset /scratch/time_sec/index (VectorData) Index in the matrix | shape = (28,) | dtype = int64
  Dataset /scratch/time_sec/time (VectorData) Time point | shape = (28,) | dtype = float64
  session_description: Per-channel spectrograms of SEEG spectral response to eyepuff
  session_start_time: 2000-01-01T12:00:00-08:00
  timestamps_reference_time: 2000-01-01T12:00:00-08:00


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2025-02-28T23:30:12.831906-08:00']
  experiment_description: Multitaper spectrograms of bipolar electrode response to eyepuff
  experimenter: ['Kauvar, Isaac' 'Richman, Ethan' 'Liu, Tony']
  institution: Stanford University
  keywords: ['emotion' 'brain-wide' 'airpuff']
  lab: Karl Deisseroth Lab
  Group /general/subject (Subject) 
  identifier: kauvar-richman-liu-single_trial_data
  Group /scratch/channel (DynamicTable) Labels for the channels, format [region]_[patient]_[bipolar_electrode]
  Dataset /scratch/channel/channel (VectorData) Channel name | shape = (795,) | dtype = object
  Dataset /scratch/channel/id (ElementIdentifiers)  | shape = (795,) | dtype = int64
  Dataset /scratch/channel/index (VectorData) Index in the matrix | shape = (795,) | dtype = int64
  Group /scratch/freq_hz (DynamicTable) Labels for the frequency dimension
  Dataset /scratch/freq_hz/frequency (VectorData) Frequency value | shape = (65,) | dtype = float64
  Dataset /scratch/freq_hz/id (ElementIdentifiers)  | shape = (65,) | dtype = int64
  Dataset /scratch/freq_hz/index (VectorData) Index in the matrix | shape = (65,) | dtype = int64
  Dataset /scratch/puff_sgram_control (ScratchData)  | shape = (795, 39, 65, 80) | dtype = float64
  Dataset /scratch/puff_sgram_infusion (ScratchData)  | shape = (795, 39, 65, 80) | dtype = float64
  Dataset /scratch/puff_sgram_postinfusion (ScratchData)  | shape = (795, 39, 65, 80) | dtype = float64
  Dataset /scratch/puff_sgram_preinfusion (ScratchData)  | shape = (795, 39, 65, 80) | dtype = float64
  Group /scratch/time_sec (DynamicTable) Labels for the time dimension
  Dataset /scratch/time_sec/id (ElementIdentifiers)  | shape = (80,) | dtype = int64
  Dataset /scratch/time_sec/index (VectorData) Index in the matrix | shape = (80,) | dtype = int64
  Dataset /scratch/time_sec/time (VectorData) Time point | shape = (80,) | dtype = float64
  session_description: Per-channel, per-trial spectrograms of SEEG spectral response to eyepuff
  session_start_time: 2000-01-01T12:00:00-08:00
  timestamps_reference_time: 2000-01-01T12:00:00-08:00
