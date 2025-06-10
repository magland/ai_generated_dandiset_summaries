
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001361/0.250609.2249
name: A flexible hippocampal population code for experience relative to reward
contributor: [{'name': 'National Institutes of Health (NIH)', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': '1 K99 MH 135993-01'}, {'name': 'Sosa, Marielena', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0003-0762-1128', 'includeInCitation': True}, {'name': 'Plitt, Mark H.', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-7154-6292', 'includeInCitation': True}, {'name': 'Giocomo, Lisa M.', 'email': 'giocomo@stanford.edu', 'roleName': ['dcite:Author', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0003-0416-2528', 'includeInCitation': True}]
description: 2-photon imaging and behavioral data from hippocampal area CA1 during virtual reality navigation in mice. Included in Sosa, Plitt, & Giocomo, "A flexible hippocampal population code for experience relative to reward," Nature Neuroscience.

To reinforce rewarding behaviors, events leading up to and following rewards must be remembered. Hippocampal place cell activity spans spatial and non-spatial episodes, but whether hippocampal activity encodes entire sequences of events relative to reward is unknown. To test this, we performed two-photon imaging of hippocampal CA1 as mice navigated virtual environments with changing hidden reward locations. When the reward moved, a subpopulation of neurons updated their firing fields to the same relative position with respect to reward, constructing behavioral timescale sequences spanning the entire task. Over learning, this reward-relative representation became more robust as additional neurons were recruited, and changes in reward-relative firing often preceded behavioral adaptations following reward relocation. Concurrently, the spatial environment code was maintained through a parallel, dynamic subpopulation rather than through dedicated cell classes. These findings reveal how hippocampal ensembles flexibly encode multiple aspects of experience while amplifying behaviorally relevant information.
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}, {'name': 'behavioral approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 92560251500, 'numberOfFiles': 152, 'numberOfSubjects': 11, 'variableMeasured': ['TwoPhotonSeries', 'PlaneSegmentation', 'BehavioralTimeSeries', 'ProcessingModule', 'ImagingPlane', 'OpticalChannel'], 'measurementTechnique': [{'name': 'two-photon microscopy technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 001361 has 100 NWB files.
72 of these NWB files are of type 1.
28 of these NWB files are of type 2.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/TwoPhotonSeries (TwoPhotonSeries) no description
  Group /acquisition/TwoPhotonSeries/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeries/imaging_plane/OpticalChannel (OpticalChannel) 
  Group /acquisition/TwoPhotonSeries/imaging_plane/device (Device) My two-photon microscope
  file_create_date: ['2025-03-12T23:45:29.830157-07:00']
  Group /general/devices/Microscope (Device) My two-photon microscope
  experimenter: ['Mari Sosa']
  Group /general/optophysiology/ImagingPlane (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane/OpticalChannel (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane/device (Device) My two-photon microscope
  session_id: 03
  Group /general/subject (Subject) 
  identifier: /data/InVivoDA/GCAMP11/23_02_2023/Env1_LocationB_to_A
  Group /processing/behavior (ProcessingModule) behavior data
  Group /processing/behavior/BehavioralTimeSeries (BehavioralTimeSeries) 
  Group /processing/behavior/BehavioralTimeSeries/Reward (TimeSeries) reward delivery
  Group /processing/behavior/BehavioralTimeSeries/autoreward (TimeSeries) whether trial was automatically rewarded if the subject failed to lick
  Group /processing/behavior/BehavioralTimeSeries/environment (TimeSeries) Virtual reality environment
  Group /processing/behavior/BehavioralTimeSeries/lick (TimeSeries) lick detection by capacitive sensor, cumulative per imaging frame
  Group /processing/behavior/BehavioralTimeSeries/position (TimeSeries) Position in a virtual linear track
  Group /processing/behavior/BehavioralTimeSeries/reward_zone (TimeSeries) reward zone entry (binary)
  Group /processing/behavior/BehavioralTimeSeries/scanning (TimeSeries) whether scanning occurred to collect ophys data
  Group /processing/behavior/BehavioralTimeSeries/speed (TimeSeries) the speed of the subject measured over time
  Group /processing/behavior/BehavioralTimeSeries/teleport (TimeSeries) end of a trial, i.e. entry into the intertrial interval
  Group /processing/behavior/BehavioralTimeSeries/trial number (TimeSeries) trial number, where each trial is a lap of the track
  Group /processing/behavior/BehavioralTimeSeries/trial_start (TimeSeries) start of a trial, i.e. entry to the linear track
  Group /processing/ophys (ProcessingModule) optical physiology processed data
  Group /processing/ophys/Backgrounds_0 (Images) no description
  Dataset /processing/ophys/Backgrounds_0/Vcorr (GrayscaleImage)  | shape = (512, 796) | dtype = float32
  Dataset /processing/ophys/Backgrounds_0/max_proj (GrayscaleImage)  | shape = (512, 796) | dtype = float32
  Dataset /processing/ophys/Backgrounds_0/meanImg (GrayscaleImage)  | shape = (512, 796) | dtype = float64
  Group /processing/ophys/Deconvolved (Fluorescence) 
  Group /processing/ophys/Deconvolved/plane0 (RoiResponseSeries) no description
  Dataset /processing/ophys/Deconvolved/plane0/rois (DynamicTableRegion) ROIs for plane0 | shape = (349,) | dtype = int64
  Group /processing/ophys/Fluorescence (Fluorescence) 
  Group /processing/ophys/Fluorescence/plane0 (RoiResponseSeries) no description
  Dataset /processing/ophys/Fluorescence/plane0/rois (DynamicTableRegion) ROIs for plane0 | shape = (349,) | dtype = int64
  Group /processing/ophys/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation (PlaneSegmentation) suite2p output
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/id (ElementIdentifiers)  | shape = (349,) | dtype = int64
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/OpticalChannel (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/device (Device) My two-photon microscope
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/iscell (VectorData) two columns - iscell & probcell | shape = (349, 2) | dtype = float64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/pixel_mask (VectorData) Pixel masks for each ROI | shape = (27649,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (349,) | dtype = uint16
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/planeIdx (VectorData) rec plane for each roi | shape = (349,) | dtype = int64
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/reference_images/TwoPhotonSeries (TwoPhotonSeries) no description
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/reference_images/TwoPhotonSeries/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/reference_images/TwoPhotonSeries/imaging_plane/OpticalChannel (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/reference_images/TwoPhotonSeries/imaging_plane/device (Device) My two-photon microscope
  Group /processing/ophys/Neuropil (Fluorescence) 
  Group /processing/ophys/Neuropil/plane0 (RoiResponseSeries) no description
  Dataset /processing/ophys/Neuropil/plane0/rois (DynamicTableRegion) ROIs for plane0 | shape = (349,) | dtype = int64
  session_description: processed suite2p data
  session_start_time: 2023-02-23T00:00:00-08:00
  timestamps_reference_time: 2023-02-23T00:00:00-08:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/TwoPhotonSeries (TwoPhotonSeries) no description
  Group /acquisition/TwoPhotonSeries/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeries/imaging_plane/OpticalChannel (OpticalChannel) 
  Group /acquisition/TwoPhotonSeries/imaging_plane/device (Device) My two-photon microscope
  file_create_date: ['2025-03-12T23:58:09.371171-07:00']
  Group /general/devices/Microscope (Device) My two-photon microscope
  experimenter: ['Mari Sosa']
  Group /general/optophysiology/ImagingPlane (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane/OpticalChannel (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane/device (Device) My two-photon microscope
  session_id: 01
  Group /general/subject (Subject) 
  identifier: /data/InVivoDA/GCAMP17/26_03_2024/Env2_LocationB
  Group /processing/behavior (ProcessingModule) behavior data
  Group /processing/behavior/BehavioralTimeSeries (BehavioralTimeSeries) 
  Group /processing/behavior/BehavioralTimeSeries/Reward (TimeSeries) reward delivery
  Group /processing/behavior/BehavioralTimeSeries/autoreward (TimeSeries) whether trial was automatically rewarded if the subject failed to lick
  Group /processing/behavior/BehavioralTimeSeries/environment (TimeSeries) Virtual reality environment
  Group /processing/behavior/BehavioralTimeSeries/lick (TimeSeries) lick detection by capacitive sensor, cumulative per imaging frame
  Group /processing/behavior/BehavioralTimeSeries/position (TimeSeries) Position in a virtual linear track
  Group /processing/behavior/BehavioralTimeSeries/reward_zone (TimeSeries) reward zone entry (binary)
  Group /processing/behavior/BehavioralTimeSeries/scanning (TimeSeries) whether scanning occurred to collect ophys data
  Group /processing/behavior/BehavioralTimeSeries/speed (TimeSeries) the speed of the subject measured over time
  Group /processing/behavior/BehavioralTimeSeries/teleport (TimeSeries) end of a trial, i.e. entry into the intertrial interval
  Group /processing/behavior/BehavioralTimeSeries/trial number (TimeSeries) trial number, where each trial is a lap of the track
  Group /processing/behavior/BehavioralTimeSeries/trial_start (TimeSeries) start of a trial, i.e. entry to the linear track
  Group /processing/ophys (ProcessingModule) optical physiology processed data
  Group /processing/ophys/Backgrounds_0 (Images) no description
  Dataset /processing/ophys/Backgrounds_0/Vcorr (GrayscaleImage)  | shape = (512, 796) | dtype = float32
  Dataset /processing/ophys/Backgrounds_0/max_proj (GrayscaleImage)  | shape = (512, 796) | dtype = float32
  Dataset /processing/ophys/Backgrounds_0/meanImg (GrayscaleImage)  | shape = (512, 796) | dtype = float64
  Group /processing/ophys/Backgrounds_1 (Images) no description
  Dataset /processing/ophys/Backgrounds_1/Vcorr (GrayscaleImage)  | shape = (512, 796) | dtype = float32
  Dataset /processing/ophys/Backgrounds_1/max_proj (GrayscaleImage)  | shape = (512, 796) | dtype = float32
  Dataset /processing/ophys/Backgrounds_1/meanImg (GrayscaleImage)  | shape = (512, 796) | dtype = float64
  Group /processing/ophys/Deconvolved (Fluorescence) 
  Group /processing/ophys/Deconvolved/plane0 (RoiResponseSeries) no description
  Dataset /processing/ophys/Deconvolved/plane0/rois (DynamicTableRegion) ROIs for plane0 | shape = (936,) | dtype = int64
  Group /processing/ophys/Deconvolved/plane1 (RoiResponseSeries) no description
  Dataset /processing/ophys/Deconvolved/plane1/rois (DynamicTableRegion) ROIs for plane1 | shape = (1226,) | dtype = int64
  Group /processing/ophys/Fluorescence (Fluorescence) 
  Group /processing/ophys/Fluorescence/plane0 (RoiResponseSeries) no description
  Dataset /processing/ophys/Fluorescence/plane0/rois (DynamicTableRegion) ROIs for plane0 | shape = (936,) | dtype = int64
  Group /processing/ophys/Fluorescence/plane1 (RoiResponseSeries) no description
  Dataset /processing/ophys/Fluorescence/plane1/rois (DynamicTableRegion) ROIs for plane1 | shape = (1226,) | dtype = int64
  Group /processing/ophys/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation (PlaneSegmentation) suite2p output
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/id (ElementIdentifiers)  | shape = (2162,) | dtype = int64
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/OpticalChannel (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/device (Device) My two-photon microscope
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/iscell (VectorData) two columns - iscell & probcell | shape = (2162, 2) | dtype = float64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/planeIdx (VectorData) rec plane for each roi | shape = (2162,) | dtype = int64
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/reference_images/TwoPhotonSeries (TwoPhotonSeries) no description
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/reference_images/TwoPhotonSeries/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/reference_images/TwoPhotonSeries/imaging_plane/OpticalChannel (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/reference_images/TwoPhotonSeries/imaging_plane/device (Device) My two-photon microscope
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/voxel_mask (VectorData) Voxel masks for each ROI | shape = (162519,) | dtype = [('x', '<u4'), ('y', '<u4'), ('z', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/voxel_mask_index (VectorIndex) Index for VectorData 'voxel_mask' | shape = (2162,) | dtype = uint32
  Group /processing/ophys/Neuropil (Fluorescence) 
  Group /processing/ophys/Neuropil/plane0 (RoiResponseSeries) no description
  Dataset /processing/ophys/Neuropil/plane0/rois (DynamicTableRegion) ROIs for plane0 | shape = (936,) | dtype = int64
  Group /processing/ophys/Neuropil/plane1 (RoiResponseSeries) no description
  Dataset /processing/ophys/Neuropil/plane1/rois (DynamicTableRegion) ROIs for plane1 | shape = (1226,) | dtype = int64
  session_description: processed suite2p data
  session_start_time: 2024-03-26T00:00:00-07:00
  timestamps_reference_time: 2024-03-26T00:00:00-07:00
