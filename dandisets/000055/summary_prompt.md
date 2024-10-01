
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000055/0.220127.0436
name: AJILE12: Long-term naturalistic human intracranial neural recordings and pose
contributor: [{'name': 'Peterson, Steven M.', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0003-0782-5788', 'affiliation': [{'name': 'University of Washington', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/00cvxb145'}], 'includeInCitation': True}, {'name': 'Singh, Satpreet H.', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0003-1867-4401', 'affiliation': [{'name': 'University of Washington', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/00cvxb145'}], 'includeInCitation': True}, {'name': 'Dichter, Benjamin', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0001-5725-6910', 'affiliation': [{'name': 'CatalystNeuro', 'schemaKey': 'Affiliation'}], 'includeInCitation': True}, {'name': 'Scheid, Micheal', 'roleName': [], 'schemaKey': 'Person', 'affiliation': [{'name': 'CatalystNeuro', 'schemaKey': 'Affiliation'}], 'includeInCitation': True}, {'name': 'Rao, Rajesh P. N.', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0003-0682-8952', 'affiliation': [{'name': 'University of Washington', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/00cvxb145'}], 'includeInCitation': True}, {'name': 'Brunton, Bingni W.', 'email': 'bbrunton@uw.edu', 'roleName': ['dcite:Author', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0002-4831-3466', 'affiliation': [{'name': 'University of Washington', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/00cvxb145'}], 'includeInCitation': True}]
description: Understanding the neural basis of human movement in naturalistic scenarios is critical for expanding neuroscience research beyond constrained laboratory paradigms. The neural correlates of unstructured, spontaneous movements in completely naturalistic settings have rarely been studied, due in large part to a lack of available data. Here, we present our Annotated Joints in Long-term Electrocorticography for 12 human participants (AJILE12) dataset, the largest human neurobehavioral dataset that is publicly available; the dataset was recorded opportunistically during passive clinical epilepsy monitoring. AJILE12 includes synchronized intracranial neural recordings and upper body pose trajectories across 55 semi-continuous days of naturalistic movements, along with relevant metadata, including thousands of wrist movement events and annotated behavioral states. Neural recordings are available at 500 Hz from at least 64 electrodes per participant, for a total of 1280 hours. Pose trajectories at 9 upper-body keypoints, including wrist, elbow, and shoulder joints, were sampled at 30 frames per second and estimated from 118 million video frames. In adherence with the FAIR data principles, we have shared AJILE12 on The Dandi Archive in the Neurodata Without Borders (NWB) data standard and developed a browser-based dashboard to facilitate data exploration and reuse.
assetsSummary: {'species': [{'name': 'Human', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9606'}], 'approach': [{'name': 'behavioral approach', 'schemaKey': 'ApproachType'}, {'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 845869698341, 'numberOfFiles': 55, 'numberOfSubjects': 12, 'variableMeasured': ['Position', 'ProcessingModule', 'ElectricalSeries', 'ElectrodeGroup'], 'measurementTechnique': [{'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000055 has 22 NWB files.
4 of these NWB files are of type 1.
5 of these NWB files are of type 2.
4 of these NWB files are of type 3.
4 of these NWB files are of type 4.
5 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ECGL (TimeSeries) Electrooculography for tracking saccades - left
  Group /acquisition/ECGR (TimeSeries) Electrooculography for tracking saccades - right
  Group /acquisition/EOGL (TimeSeries) Electrooculography for tracking saccades - left
  Group /acquisition/EOGR (TimeSeries) Electrooculography for tracking saccades - right
  Group /acquisition/ElectricalSeries (ElectricalSeries) no description
  Dataset /acquisition/ElectricalSeries/electrodes (DynamicTableRegion) all electrodes | shape = (94,) | dtype = int64
  file_create_date: ['2021-06-09T05:44:48.194751-04:00']
  Group /general/devices/ECG (Device) 
  Group /general/devices/EOG (Device) 
  Group /general/devices/GRID (Device) 
  Group /general/devices/LAT (Device) 
  Group /general/devices/LID (Device) 
  Group /general/devices/LMT (Device) 
  Group /general/devices/LPT (Device) 
  Group /general/devices/LTO (Device) 
  Group /general/extracellular_ephys/ECG (ElectrodeGroup) electrocardiogram
  Group /general/extracellular_ephys/ECG/device (Device) 
  Group /general/extracellular_ephys/EOG (ElectrodeGroup) electrooculogram
  Group /general/extracellular_ephys/EOG/device (Device) 
  Group /general/extracellular_ephys/GRID (ElectrodeGroup) ECoG grid
  Group /general/extracellular_ephys/GRID/device (Device) 
  Group /general/extracellular_ephys/LAT (ElectrodeGroup) left anterior temporal
  Group /general/extracellular_ephys/LAT/device (Device) 
  Group /general/extracellular_ephys/LID (ElectrodeGroup) left insular depth
  Group /general/extracellular_ephys/LID/device (Device) 
  Group /general/extracellular_ephys/LMT (ElectrodeGroup) left medial temporal
  Group /general/extracellular_ephys/LMT/device (Device) 
  Group /general/extracellular_ephys/LPT (ElectrodeGroup) left posterior temporal
  Group /general/extracellular_ephys/LPT/device (Device) 
  Group /general/extracellular_ephys/LTO (ElectrodeGroup) left temporal occipital
  Group /general/extracellular_ephys/LTO/device (Device) 
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (94,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/good (VectorData) good electrodes | shape = (94,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (94,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (94,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/high_freq_R2 (VectorData) R^2 for high frequency band on each electrode | shape = (94,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (94,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (94,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/kurtosis (VectorData) kurtosis of each electrode's data for the entire recording period | shape = (94,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (94,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/low_freq_R2 (VectorData) R^2 for low frequency band on each electrode | shape = (94,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/median_deviation (VectorData) median absolute deviation estimator for standard deviation for each electrode | shape = (94,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/standard_deviation (VectorData) standard deviation of each electrode's data for the entire recording period | shape = (94,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (94,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (94,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (94,) | dtype = float64
  session_id: 3
  Group /general/subject (Subject) 
  identifier: 4c571b6c-1028-476f-b0e1-e34aa27b3206
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (1427,) | dtype = int64
  Dataset /intervals/epochs/labels (VectorData) Coarse behavioral labels | shape = (1427,) | dtype = object
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (1427,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1427,) | dtype = float64
  Group /intervals/reaches (TimeIntervals) Features of each reach
  Dataset /intervals/reaches/Bimanual_class (VectorData) binary feature that classifies each movement event as unimanual (0) or bimanual (1) based on how close in time a ipsilateral wrist movement started relative to each contralateral wrist movement events | shape = (156,) | dtype = float64
  Dataset /intervals/reaches/Bimanual_overlap (VectorData) The amount of ipsilateral and contralateral wrist temporaloverlap as a fraction of the entire contralateral movement duration | shape = (156,) | dtype = float64
  Dataset /intervals/reaches/Bimanual_ratio (VectorData) ratio of ipsilateral wrist reach magnitude to the sum of ipsilateral and contralateral wrist magnitudes; ranges from 0 (unimanual/contralateral move only) to 1 (only ipsilateral arm moving); 0.5 indicates bimanual movement | shape = (156,) | dtype = float64
  Dataset /intervals/reaches/Onset_speed_px_per_sec (VectorData) Onset speed in pixels / second) | shape = (156,) | dtype = float64
  Dataset /intervals/reaches/Reach_angle_degrees (VectorData) Reach angle in degrees | shape = (156,) | dtype = float64
  Dataset /intervals/reaches/Reach_magnitude_px (VectorData) Magnitude of reach in pixels | shape = (156,) | dtype = float64
  Dataset /intervals/reaches/Speech_ratio (VectorData) rough estimation of whether someone is likely to be speaking based on a power ratio of audio data; ranges from 0 (no speech) to 1 (high likelihood of speech)h | shape = (156,) | dtype = float64
  Dataset /intervals/reaches/id (ElementIdentifiers)  | shape = (156,) | dtype = int64
  Dataset /intervals/reaches/start_time (VectorData) Start time of epoch, in seconds | shape = (156,) | dtype = float64
  Dataset /intervals/reaches/stop_time (VectorData) Stop time of epoch, in seconds | shape = (156,) | dtype = float64
  Group /processing/behavior (ProcessingModule) pose data
  Group /processing/behavior/Position (Position) 
  Group /processing/behavior/Position/L_Ear (SpatialSeries) no description
  Group /processing/behavior/Position/L_Elbow (SpatialSeries) no description
  Group /processing/behavior/Position/L_Shoulder (SpatialSeries) no description
  Group /processing/behavior/Position/L_Wrist (SpatialSeries) no description
  Group /processing/behavior/Position/Nose (SpatialSeries) no description
  Group /processing/behavior/Position/R_Ear (SpatialSeries) no description
  Group /processing/behavior/Position/R_Elbow (SpatialSeries) no description
  Group /processing/behavior/Position/R_Shoulder (SpatialSeries) no description
  Group /processing/behavior/Position/R_Wrist (SpatialSeries) no description
  Group /processing/behavior/ReachEvents (Events) r_wrist
  session_description: no description
  session_start_time: 2000-01-02T19:00:00-05:00
  timestamps_reference_time: 2000-01-02T19:00:00-05:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeries (ElectricalSeries) no description
  Dataset /acquisition/ElectricalSeries/electrodes (DynamicTableRegion) all electrodes | shape = (126,) | dtype = int64
  file_create_date: ['2021-06-09T00:35:59.249207-04:00']
  Group /general/devices/Grid (Device) 
  Group /general/devices/LAT (Device) 
  Group /general/devices/LF (Device) 
  Group /general/devices/LID (Device) 
  Group /general/devices/LMT (Device) 
  Group /general/devices/LPT (Device) 
  Group /general/devices/LTO (Device) 
  Group /general/devices/RAT (Device) 
  Group /general/devices/RATD (Device) 
  Group /general/devices/RFD (Device) 
  Group /general/devices/RPT (Device) 
  Group /general/devices/RPTD (Device) 
  Group /general/extracellular_ephys/Grid (ElectrodeGroup) ECoG grid
  Group /general/extracellular_ephys/Grid/device (Device) 
  Group /general/extracellular_ephys/LAT (ElectrodeGroup) left anterior temporal
  Group /general/extracellular_ephys/LAT/device (Device) 
  Group /general/extracellular_ephys/LF (ElectrodeGroup) left frontal
  Group /general/extracellular_ephys/LF/device (Device) 
  Group /general/extracellular_ephys/LID (ElectrodeGroup) left insular depth
  Group /general/extracellular_ephys/LID/device (Device) 
  Group /general/extracellular_ephys/LMT (ElectrodeGroup) left medial temporal
  Group /general/extracellular_ephys/LMT/device (Device) 
  Group /general/extracellular_ephys/LPT (ElectrodeGroup) left posterior temporal
  Group /general/extracellular_ephys/LPT/device (Device) 
  Group /general/extracellular_ephys/LTO (ElectrodeGroup) left temporal occipital
  Group /general/extracellular_ephys/LTO/device (Device) 
  Group /general/extracellular_ephys/RAT (ElectrodeGroup) right anterior temporal
  Group /general/extracellular_ephys/RAT/device (Device) 
  Group /general/extracellular_ephys/RATD (ElectrodeGroup) right anterior temporal depth
  Group /general/extracellular_ephys/RATD/device (Device) 
  Group /general/extracellular_ephys/RFD (ElectrodeGroup) right frontal depth
  Group /general/extracellular_ephys/RFD/device (Device) 
  Group /general/extracellular_ephys/RPT (ElectrodeGroup) right posterior temporal
  Group /general/extracellular_ephys/RPT/device (Device) 
  Group /general/extracellular_ephys/RPTD (ElectrodeGroup) right posterior temporal depth
  Group /general/extracellular_ephys/RPTD/device (Device) 
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (126,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/good (VectorData) good electrodes | shape = (126,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (126,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (126,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/high_freq_R2 (VectorData) R^2 for high frequency band on each electrode | shape = (126,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (126,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (126,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/kurtosis (VectorData) kurtosis of each electrode's data for the entire recording period | shape = (126,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (126,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/low_freq_R2 (VectorData) R^2 for low frequency band on each electrode | shape = (126,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/median_deviation (VectorData) median absolute deviation estimator for standard deviation for each electrode | shape = (126,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/standard_deviation (VectorData) standard deviation of each electrode's data for the entire recording period | shape = (126,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (126,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (126,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (126,) | dtype = float64
  session_id: 3
  Group /general/subject (Subject) 
  identifier: 1d0f5abc-e4cf-4354-aab8-400c11fac72e
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (1425,) | dtype = int64
  Dataset /intervals/epochs/labels (VectorData) Coarse behavioral labels | shape = (1425,) | dtype = object
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (1425,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1425,) | dtype = float64
  Group /intervals/reaches (TimeIntervals) Features of each reach
  Dataset /intervals/reaches/Bimanual_class (VectorData) binary feature that classifies each movement event as unimanual (0) or bimanual (1) based on how close in time a ipsilateral wrist movement started relative to each contralateral wrist movement events | shape = (15,) | dtype = float64
  Dataset /intervals/reaches/Bimanual_overlap (VectorData) The amount of ipsilateral and contralateral wrist temporaloverlap as a fraction of the entire contralateral movement duration | shape = (15,) | dtype = float64
  Dataset /intervals/reaches/Bimanual_ratio (VectorData) ratio of ipsilateral wrist reach magnitude to the sum of ipsilateral and contralateral wrist magnitudes; ranges from 0 (unimanual/contralateral move only) to 1 (only ipsilateral arm moving); 0.5 indicates bimanual movement | shape = (15,) | dtype = float64
  Dataset /intervals/reaches/Onset_speed_px_per_sec (VectorData) Onset speed in pixels / second) | shape = (15,) | dtype = float64
  Dataset /intervals/reaches/Reach_angle_degrees (VectorData) Reach angle in degrees | shape = (15,) | dtype = float64
  Dataset /intervals/reaches/Reach_magnitude_px (VectorData) Magnitude of reach in pixels | shape = (15,) | dtype = float64
  Dataset /intervals/reaches/Speech_ratio (VectorData) rough estimation of whether someone is likely to be speaking based on a power ratio of audio data; ranges from 0 (no speech) to 1 (high likelihood of speech)h | shape = (15,) | dtype = float64
  Dataset /intervals/reaches/id (ElementIdentifiers)  | shape = (15,) | dtype = int64
  Dataset /intervals/reaches/start_time (VectorData) Start time of epoch, in seconds | shape = (15,) | dtype = float64
  Dataset /intervals/reaches/stop_time (VectorData) Stop time of epoch, in seconds | shape = (15,) | dtype = float64
  Group /processing/behavior (ProcessingModule) pose data
  Group /processing/behavior/Position (Position) 
  Group /processing/behavior/Position/L_Ear (SpatialSeries) no description
  Group /processing/behavior/Position/L_Elbow (SpatialSeries) no description
  Group /processing/behavior/Position/L_Shoulder (SpatialSeries) no description
  Group /processing/behavior/Position/L_Wrist (SpatialSeries) no description
  Group /processing/behavior/Position/Nose (SpatialSeries) no description
  Group /processing/behavior/Position/R_Ear (SpatialSeries) no description
  Group /processing/behavior/Position/R_Elbow (SpatialSeries) no description
  Group /processing/behavior/Position/R_Shoulder (SpatialSeries) no description
  Group /processing/behavior/Position/R_Wrist (SpatialSeries) no description
  Group /processing/behavior/ReachEvents (Events) r_wrist
  session_description: no description
  session_start_time: 2000-01-02T19:00:00-05:00
  timestamps_reference_time: 2000-01-02T19:00:00-05:00


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeries (ElectricalSeries) no description
  Dataset /acquisition/ElectricalSeries/electrodes (DynamicTableRegion) all electrodes | shape = (86,) | dtype = int64
  file_create_date: ['2021-06-09T09:24:46.360495-04:00']
  Group /general/devices/GRID (Device) 
  Group /general/devices/RDA (Device) 
  Group /general/devices/RDP (Device) 
  Group /general/devices/RST (Device) 
  Group /general/extracellular_ephys/GRID (ElectrodeGroup) ECoG grid
  Group /general/extracellular_ephys/GRID/device (Device) 
  Group /general/extracellular_ephys/RDA (ElectrodeGroup) right depth anterior
  Group /general/extracellular_ephys/RDA/device (Device) 
  Group /general/extracellular_ephys/RDP (ElectrodeGroup) right depth posterior
  Group /general/extracellular_ephys/RDP/device (Device) 
  Group /general/extracellular_ephys/RST (ElectrodeGroup) right temporal
  Group /general/extracellular_ephys/RST/device (Device) 
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (86,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/good (VectorData) good electrodes | shape = (86,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (86,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (86,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/high_freq_R2 (VectorData) R^2 for high frequency band on each electrode | shape = (86,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (86,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (86,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/kurtosis (VectorData) kurtosis of each electrode's data for the entire recording period | shape = (86,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (86,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/low_freq_R2 (VectorData) R^2 for low frequency band on each electrode | shape = (86,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/median_deviation (VectorData) median absolute deviation estimator for standard deviation for each electrode | shape = (86,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/standard_deviation (VectorData) standard deviation of each electrode's data for the entire recording period | shape = (86,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (86,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (86,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (86,) | dtype = float64
  session_id: 3
  Group /general/subject (Subject) 
  identifier: ccb4f7ee-5d1b-4329-9eb3-204fffa7a691
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (1435,) | dtype = int64
  Dataset /intervals/epochs/labels (VectorData) Coarse behavioral labels | shape = (1435,) | dtype = object
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (1435,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1435,) | dtype = float64
  Group /intervals/reaches (TimeIntervals) Features of each reach
  Dataset /intervals/reaches/Bimanual_class (VectorData) binary feature that classifies each movement event as unimanual (0) or bimanual (1) based on how close in time a ipsilateral wrist movement started relative to each contralateral wrist movement events | shape = (51,) | dtype = float64
  Dataset /intervals/reaches/Bimanual_overlap (VectorData) The amount of ipsilateral and contralateral wrist temporaloverlap as a fraction of the entire contralateral movement duration | shape = (51,) | dtype = float64
  Dataset /intervals/reaches/Bimanual_ratio (VectorData) ratio of ipsilateral wrist reach magnitude to the sum of ipsilateral and contralateral wrist magnitudes; ranges from 0 (unimanual/contralateral move only) to 1 (only ipsilateral arm moving); 0.5 indicates bimanual movement | shape = (51,) | dtype = float64
  Dataset /intervals/reaches/Onset_speed_px_per_sec (VectorData) Onset speed in pixels / second) | shape = (51,) | dtype = float64
  Dataset /intervals/reaches/Reach_angle_degrees (VectorData) Reach angle in degrees | shape = (51,) | dtype = float64
  Dataset /intervals/reaches/Reach_magnitude_px (VectorData) Magnitude of reach in pixels | shape = (51,) | dtype = float64
  Dataset /intervals/reaches/Speech_ratio (VectorData) rough estimation of whether someone is likely to be speaking based on a power ratio of audio data; ranges from 0 (no speech) to 1 (high likelihood of speech)h | shape = (51,) | dtype = float64
  Dataset /intervals/reaches/id (ElementIdentifiers)  | shape = (51,) | dtype = int64
  Dataset /intervals/reaches/start_time (VectorData) Start time of epoch, in seconds | shape = (51,) | dtype = float64
  Dataset /intervals/reaches/stop_time (VectorData) Stop time of epoch, in seconds | shape = (51,) | dtype = float64
  Group /processing/behavior (ProcessingModule) pose data
  Group /processing/behavior/Position (Position) 
  Group /processing/behavior/Position/L_Ear (SpatialSeries) no description
  Group /processing/behavior/Position/L_Elbow (SpatialSeries) no description
  Group /processing/behavior/Position/L_Shoulder (SpatialSeries) no description
  Group /processing/behavior/Position/L_Wrist (SpatialSeries) no description
  Group /processing/behavior/Position/Nose (SpatialSeries) no description
  Group /processing/behavior/Position/R_Ear (SpatialSeries) no description
  Group /processing/behavior/Position/R_Elbow (SpatialSeries) no description
  Group /processing/behavior/Position/R_Shoulder (SpatialSeries) no description
  Group /processing/behavior/Position/R_Wrist (SpatialSeries) no description
  Group /processing/behavior/ReachEvents (Events) l_wrist
  session_description: no description
  session_start_time: 2000-01-02T19:00:00-05:00
  timestamps_reference_time: 2000-01-02T19:00:00-05:00


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeries (ElectricalSeries) no description
  Dataset /acquisition/ElectricalSeries/electrodes (DynamicTableRegion) all electrodes | shape = (96,) | dtype = int64
  file_create_date: ['2021-06-09T07:03:47.857693-04:00']
  Group /general/devices/GRID (Device) 
  Group /general/devices/LAD (Device) 
  Group /general/devices/LAT (Device) 
  Group /general/devices/LMT (Device) 
  Group /general/devices/LPD (Device) 
  Group /general/extracellular_ephys/GRID (ElectrodeGroup) ECoG grid
  Group /general/extracellular_ephys/GRID/device (Device) 
  Group /general/extracellular_ephys/LAD (ElectrodeGroup) left anterior depth
  Group /general/extracellular_ephys/LAD/device (Device) 
  Group /general/extracellular_ephys/LAT (ElectrodeGroup) left anterior temporal
  Group /general/extracellular_ephys/LAT/device (Device) 
  Group /general/extracellular_ephys/LMT (ElectrodeGroup) left medial temporal
  Group /general/extracellular_ephys/LMT/device (Device) 
  Group /general/extracellular_ephys/LPD (ElectrodeGroup) left posterior depth
  Group /general/extracellular_ephys/LPD/device (Device) 
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/good (VectorData) good electrodes | shape = (96,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/high_freq_R2 (VectorData) R^2 for high frequency band on each electrode | shape = (96,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (96,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (96,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/kurtosis (VectorData) kurtosis of each electrode's data for the entire recording period | shape = (96,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/low_freq_R2 (VectorData) R^2 for low frequency band on each electrode | shape = (96,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/median_deviation (VectorData) median absolute deviation estimator for standard deviation for each electrode | shape = (96,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/standard_deviation (VectorData) standard deviation of each electrode's data for the entire recording period | shape = (96,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (96,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (96,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (96,) | dtype = float64
  session_id: 3
  Group /general/subject (Subject) 
  identifier: 279c0b35-bc6d-48a3-9797-07eaeffe0fb9
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (1427,) | dtype = int64
  Dataset /intervals/epochs/labels (VectorData) Coarse behavioral labels | shape = (1427,) | dtype = object
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (1427,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1427,) | dtype = float64
  Group /intervals/reaches (TimeIntervals) Features of each reach
  Dataset /intervals/reaches/Bimanual_class (VectorData) binary feature that classifies each movement event as unimanual (0) or bimanual (1) based on how close in time a ipsilateral wrist movement started relative to each contralateral wrist movement events | shape = (198,) | dtype = float64
  Dataset /intervals/reaches/Bimanual_overlap (VectorData) The amount of ipsilateral and contralateral wrist temporaloverlap as a fraction of the entire contralateral movement duration | shape = (198,) | dtype = float64
  Dataset /intervals/reaches/Bimanual_ratio (VectorData) ratio of ipsilateral wrist reach magnitude to the sum of ipsilateral and contralateral wrist magnitudes; ranges from 0 (unimanual/contralateral move only) to 1 (only ipsilateral arm moving); 0.5 indicates bimanual movement | shape = (198,) | dtype = float64
  Dataset /intervals/reaches/Onset_speed_px_per_sec (VectorData) Onset speed in pixels / second) | shape = (198,) | dtype = float64
  Dataset /intervals/reaches/Reach_angle_degrees (VectorData) Reach angle in degrees | shape = (198,) | dtype = float64
  Dataset /intervals/reaches/Reach_magnitude_px (VectorData) Magnitude of reach in pixels | shape = (198,) | dtype = float64
  Dataset /intervals/reaches/Speech_ratio (VectorData) rough estimation of whether someone is likely to be speaking based on a power ratio of audio data; ranges from 0 (no speech) to 1 (high likelihood of speech)h | shape = (198,) | dtype = float64
  Dataset /intervals/reaches/id (ElementIdentifiers)  | shape = (198,) | dtype = int64
  Dataset /intervals/reaches/start_time (VectorData) Start time of epoch, in seconds | shape = (198,) | dtype = float64
  Dataset /intervals/reaches/stop_time (VectorData) Stop time of epoch, in seconds | shape = (198,) | dtype = float64
  Group /processing/behavior (ProcessingModule) pose data
  Group /processing/behavior/Position (Position) 
  Group /processing/behavior/Position/L_Ear (SpatialSeries) no description
  Group /processing/behavior/Position/L_Elbow (SpatialSeries) no description
  Group /processing/behavior/Position/L_Shoulder (SpatialSeries) no description
  Group /processing/behavior/Position/L_Wrist (SpatialSeries) no description
  Group /processing/behavior/Position/Nose (SpatialSeries) no description
  Group /processing/behavior/Position/R_Ear (SpatialSeries) no description
  Group /processing/behavior/Position/R_Elbow (SpatialSeries) no description
  Group /processing/behavior/Position/R_Shoulder (SpatialSeries) no description
  Group /processing/behavior/Position/R_Wrist (SpatialSeries) no description
  Group /processing/behavior/ReachEvents (Events) r_wrist
  session_description: no description
  session_start_time: 2000-01-02T19:00:00-05:00
  timestamps_reference_time: 2000-01-02T19:00:00-05:00


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeries (ElectricalSeries) no description
  Dataset /acquisition/ElectricalSeries/electrodes (DynamicTableRegion) all electrodes | shape = (126,) | dtype = int64
  file_create_date: ['2021-06-08T23:32:26.074096-04:00']
  Group /general/devices/AHD (Device) 
  Group /general/devices/AID (Device) 
  Group /general/devices/GRID (Device) 
  Group /general/devices/LAT (Device) 
  Group /general/devices/LMT (Device) 
  Group /general/devices/LOF (Device) 
  Group /general/devices/LPT (Device) 
  Group /general/devices/LTP (Device) 
  Group /general/devices/MHD (Device) 
  Group /general/devices/MID (Device) 
  Group /general/devices/PID (Device) 
  Group /general/extracellular_ephys/AHD (ElectrodeGroup) anterior hippocampal depth
  Group /general/extracellular_ephys/AHD/device (Device) 
  Group /general/extracellular_ephys/AID (ElectrodeGroup) anterior insular depth
  Group /general/extracellular_ephys/AID/device (Device) 
  Group /general/extracellular_ephys/GRID (ElectrodeGroup) ECoG grid
  Group /general/extracellular_ephys/GRID/device (Device) 
  Group /general/extracellular_ephys/LAT (ElectrodeGroup) left anterior temporal
  Group /general/extracellular_ephys/LAT/device (Device) 
  Group /general/extracellular_ephys/LMT (ElectrodeGroup) left medial temporal
  Group /general/extracellular_ephys/LMT/device (Device) 
  Group /general/extracellular_ephys/LOF (ElectrodeGroup) left orbitofrontal
  Group /general/extracellular_ephys/LOF/device (Device) 
  Group /general/extracellular_ephys/LPT (ElectrodeGroup) left posterior temporal
  Group /general/extracellular_ephys/LPT/device (Device) 
  Group /general/extracellular_ephys/LTP (ElectrodeGroup) left temporal pole
  Group /general/extracellular_ephys/LTP/device (Device) 
  Group /general/extracellular_ephys/MHD (ElectrodeGroup) medial hippocampal depth
  Group /general/extracellular_ephys/MHD/device (Device) 
  Group /general/extracellular_ephys/MID (ElectrodeGroup) medial insular depth
  Group /general/extracellular_ephys/MID/device (Device) 
  Group /general/extracellular_ephys/PID (ElectrodeGroup) posterior insular depth
  Group /general/extracellular_ephys/PID/device (Device) 
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (126,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/good (VectorData) good electrodes | shape = (126,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (126,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (126,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/high_freq_R2 (VectorData) R^2 for high frequency band on each electrode | shape = (126,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (126,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (126,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/kurtosis (VectorData) kurtosis of each electrode's data for the entire recording period | shape = (126,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (126,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/low_freq_R2 (VectorData) R^2 for low frequency band on each electrode | shape = (126,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/median_deviation (VectorData) median absolute deviation estimator for standard deviation for each electrode | shape = (126,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/standard_deviation (VectorData) standard deviation of each electrode's data for the entire recording period | shape = (126,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (126,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (126,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (126,) | dtype = float64
  session_id: 3
  Group /general/subject (Subject) 
  identifier: 62367237-1ac6-4bb9-80de-ac014d058e91
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (1432,) | dtype = int64
  Dataset /intervals/epochs/labels (VectorData) Coarse behavioral labels | shape = (1432,) | dtype = object
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (1432,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1432,) | dtype = float64
  Group /intervals/reaches (TimeIntervals) Features of each reach
  Dataset /intervals/reaches/Bimanual_class (VectorData) binary feature that classifies each movement event as unimanual (0) or bimanual (1) based on how close in time a ipsilateral wrist movement started relative to each contralateral wrist movement events | shape = (184,) | dtype = float64
  Dataset /intervals/reaches/Bimanual_overlap (VectorData) The amount of ipsilateral and contralateral wrist temporaloverlap as a fraction of the entire contralateral movement duration | shape = (184,) | dtype = float64
  Dataset /intervals/reaches/Bimanual_ratio (VectorData) ratio of ipsilateral wrist reach magnitude to the sum of ipsilateral and contralateral wrist magnitudes; ranges from 0 (unimanual/contralateral move only) to 1 (only ipsilateral arm moving); 0.5 indicates bimanual movement | shape = (184,) | dtype = float64
  Dataset /intervals/reaches/Onset_speed_px_per_sec (VectorData) Onset speed in pixels / second) | shape = (184,) | dtype = float64
  Dataset /intervals/reaches/Reach_angle_degrees (VectorData) Reach angle in degrees | shape = (184,) | dtype = float64
  Dataset /intervals/reaches/Reach_magnitude_px (VectorData) Magnitude of reach in pixels | shape = (184,) | dtype = float64
  Dataset /intervals/reaches/Speech_ratio (VectorData) rough estimation of whether someone is likely to be speaking based on a power ratio of audio data; ranges from 0 (no speech) to 1 (high likelihood of speech)h | shape = (184,) | dtype = float64
  Dataset /intervals/reaches/id (ElementIdentifiers)  | shape = (184,) | dtype = int64
  Dataset /intervals/reaches/start_time (VectorData) Start time of epoch, in seconds | shape = (184,) | dtype = float64
  Dataset /intervals/reaches/stop_time (VectorData) Stop time of epoch, in seconds | shape = (184,) | dtype = float64
  Group /processing/behavior (ProcessingModule) pose data
  Group /processing/behavior/Position (Position) 
  Group /processing/behavior/Position/L_Ear (SpatialSeries) no description
  Group /processing/behavior/Position/L_Elbow (SpatialSeries) no description
  Group /processing/behavior/Position/L_Shoulder (SpatialSeries) no description
  Group /processing/behavior/Position/L_Wrist (SpatialSeries) no description
  Group /processing/behavior/Position/Nose (SpatialSeries) no description
  Group /processing/behavior/Position/R_Ear (SpatialSeries) no description
  Group /processing/behavior/Position/R_Elbow (SpatialSeries) no description
  Group /processing/behavior/Position/R_Shoulder (SpatialSeries) no description
  Group /processing/behavior/Position/R_Wrist (SpatialSeries) no description
  Group /processing/behavior/ReachEvents (Events) r_wrist
  session_description: no description
  session_start_time: 2000-01-02T19:00:00-05:00
  timestamps_reference_time: 2000-01-02T19:00:00-05:00
