
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001176/draft
name: Cortical acetylcholine dynamics are predicted by cholinergic axon activity and behavior state
contributor: [{'name': 'National Institutes of Health (NIH)', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': '1 R34 NS 132045-00'}, {'name': 'Reimer, Jacob', 'email': 'reimer@bcm.edu', 'schemaKey': 'Person', 'identifier': '0000-0003-4364-8846', 'includeInCitation': True}, {'name': 'Neyhart, Erin', 'schemaKey': 'Person', 'identifier': '0000-0001-9164-0553', 'includeInCitation': True}]
description: This dataset includes simultaneous in vivo imaging data of acetylcholine (ACh) sensors and GCaMP-expressing axons in the cortex during spontaneous changes in behavioral states in awake animals. It features detailed recordings of ACh activity, axon activity, and pupil size, providing valuable insights into the spatiotemporal properties of cortical ACh release and its correlation with axonal activity.
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}, {'name': 'behavioral approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 924191446, 'numberOfFiles': 132, 'numberOfSubjects': 29, 'variableMeasured': ['ImagingPlane', 'PlaneSegmentation', 'EyeTracking', 'PupilTracking', 'ProcessingModule', 'OpticalChannel', 'SpatialSeries'], 'measurementTechnique': [{'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 001176 has 100 NWB files.
88 of these NWB files are of type 1.
3 of these NWB files are of type 2.
9 of these NWB files are of type 3.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/EyeTracking (EyeTracking) 
  Group /acquisition/EyeTracking/eye_position (SpatialSeries) The x,y position of the pupil.The values are estimated in the relative pixel units.
  Group /acquisition/PupilTracking (PupilTracking) 
  Group /acquisition/PupilTracking/pupil_raw_radius (TimeSeries) radius extracted from the pupil tracking ellipse.The values are estimated in the relative pixel units.
  Group /acquisition/imageMeanIntensity (TimeSeries) Mean intensity per frame for all channels. Quality control purpose
  Group /acquisition/treadmill_velocity (TimeSeries) Cylindrical treadmill rostral-caudal position extracted at 100 Hz and converted into velocity.
  file_create_date: ['2025-01-06T15:58:33.318702-06:00']
  Group /general/devices/Microscope (Device) two-photon random access mesoscope
  experiment_description: scans recording a green ACh sensor (GACh3.0) in Primary motor cortex
  experimenter: ['Neyhart, Erin Iris']
  institution: Baylor College of Medicine
  keywords: ['neuromodulator' 'Acetylcholine' 'Two-photon imaging']
  lab: Reimer, Jacob
  Group /general/optophysiology/ImagingChannel_1 (ImagingPlane) 
  Group /general/optophysiology/ImagingChannel_1/chan2 (OpticalChannel) 
  Group /general/optophysiology/ImagingChannel_1/device (Device) two-photon random access mesoscope
  session_id: 16_1_2_Ach_M1
  Group /general/subject (Subject) 
  identifier: JR_BCM_16_1_2_Ach_M1
  Group /processing/ophys (ProcessingModule) processed 2p data
  Group /processing/ophys/Fluorescence (Fluorescence) 
  Group /processing/ophys/Fluorescence/RoiResponseSeries1 (RoiResponseSeries) The fluorescence traces for field 1
  Dataset /processing/ophys/Fluorescence/RoiResponseSeries1/rois (DynamicTableRegion) all rois in channel 1 | shape = (1,) | dtype = int64
  Group /processing/ophys/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation1 (PlaneSegmentation) The output from chan 1 contains the image masks (weights and mask classification) and the structural ids extracted from the jr-database on 2025-01-06. 
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation1/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation1/image_mask (VectorData) The image masks for each ROI. | shape = (1, 256, 256) | dtype = float32
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation1/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation1/imaging_plane/chan2 (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation1/imaging_plane/device (Device) two-photon random access mesoscope
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation1/mask_type (VectorData) The classification of mask as soma or artifact. | shape = (1,) | dtype = object
  Group /processing/ophys/SummaryImages_chan1 (Images) Correlation and average images for channel 1.
  Dataset /processing/ophys/SummaryImages_chan1/average (GrayscaleImage) average image for the stack  | shape = (256, 256) | dtype = float64
  Dataset /processing/ophys/SummaryImages_chan1/correlation (GrayscaleImage) summary image for the stack using locally spatial correlations | shape = (256, 256) | dtype = float64
  session_description: Two-Photon in-vivo imaging
  session_start_time: 2024-04-29T17:31:15-05:51
  timestamps_reference_time: 2024-04-29T17:31:15-05:51


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/imageMeanIntensity (TimeSeries) Mean intensity per frame for all channels. Quality control purpose
  Group /acquisition/treadmill_velocity (TimeSeries) Cylindrical treadmill rostral-caudal position extracted at 100 Hz and converted into velocity.
  file_create_date: ['2025-01-06T15:59:02.454935-06:00']
  Group /general/devices/Microscope (Device) two-photon random access mesoscope
  experiment_description: scans recording a green ACh sensor (GACh3.0) in Primary motor cortex
  experimenter: ['Neyhart, Erin Iris']
  institution: Baylor College of Medicine
  keywords: ['neuromodulator' 'Acetylcholine' 'Two-photon imaging']
  lab: Reimer, Jacob
  Group /general/optophysiology/ImagingChannel_1 (ImagingPlane) 
  Group /general/optophysiology/ImagingChannel_1/chan2 (OpticalChannel) 
  Group /general/optophysiology/ImagingChannel_1/device (Device) two-photon random access mesoscope
  session_id: 24_3_1_Ach_M1
  Group /general/subject (Subject) 
  identifier: JR_BCM_24_3_1_Ach_M1
  Group /processing/ophys (ProcessingModule) processed 2p data
  Group /processing/ophys/Fluorescence (Fluorescence) 
  Group /processing/ophys/Fluorescence/RoiResponseSeries1 (RoiResponseSeries) The fluorescence traces for field 1
  Dataset /processing/ophys/Fluorescence/RoiResponseSeries1/rois (DynamicTableRegion) all rois in channel 1 | shape = (1,) | dtype = int64
  Group /processing/ophys/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation1 (PlaneSegmentation) The output from chan 1 contains the image masks (weights and mask classification) and the structural ids extracted from the jr-database on 2025-01-06. 
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation1/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation1/image_mask (VectorData) The image masks for each ROI. | shape = (1, 512, 512) | dtype = float32
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation1/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation1/imaging_plane/chan2 (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation1/imaging_plane/device (Device) two-photon random access mesoscope
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation1/mask_type (VectorData) The classification of mask as soma or artifact. | shape = (1,) | dtype = object
  Group /processing/ophys/SummaryImages_chan1 (Images) Correlation and average images for channel 1.
  Dataset /processing/ophys/SummaryImages_chan1/average (GrayscaleImage) average image for the stack  | shape = (512, 512) | dtype = float64
  Dataset /processing/ophys/SummaryImages_chan1/correlation (GrayscaleImage) summary image for the stack using locally spatial correlations | shape = (512, 512) | dtype = float64
  session_description: Two-Photon in-vivo imaging
  session_start_time: 2024-05-24T10:46:37-05:51
  timestamps_reference_time: 2024-05-24T10:46:37-05:51


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/EyeTracking (EyeTracking) 
  Group /acquisition/EyeTracking/eye_position (SpatialSeries) The x,y position of the pupil.The values are estimated in the relative pixel units.
  Group /acquisition/PupilTracking (PupilTracking) 
  Group /acquisition/PupilTracking/pupil_raw_radius (TimeSeries) radius extracted from the pupil tracking ellipse.The values are estimated in the relative pixel units.
  Group /acquisition/imageMeanIntensity (TimeSeries) Mean intensity per frame for all channels. Quality control purpose
  Group /acquisition/treadmill_velocity (TimeSeries) Cylindrical treadmill rostral-caudal position extracted at 100 Hz and converted into velocity.
  file_create_date: ['2025-01-06T17:30:58.445854-06:00']
  Group /general/devices/Microscope (Device) two-photon random access mesoscope
  experiment_description: scans recording a red ACh sensor (rACh1.4) and GCaMP8s-expressing, V1-projecting cholinergic basal forebrain axons in the same ROI
  experimenter: ['Neyhart, Erin Iris']
  institution: Baylor College of Medicine
  keywords: ['neuromodulator' 'Acetylcholine' 'Axon imaging' 'Two-photon imaging']
  lab: Reimer, Jacob
  Group /general/optophysiology/ImagingChannel_1 (ImagingPlane) 
  Group /general/optophysiology/ImagingChannel_1/chan1 (OpticalChannel) 
  Group /general/optophysiology/ImagingChannel_1/device (Device) two-photon random access mesoscope
  Group /general/optophysiology/ImagingChannel_2 (ImagingPlane) 
  Group /general/optophysiology/ImagingChannel_2/chan2 (OpticalChannel) 
  Group /general/optophysiology/ImagingChannel_2/device (Device) two-photon random access mesoscope
  session_id: 26536_1_2
  Group /general/subject (Subject) 
  identifier: JR_BCM_26536_1_2
  Group /processing/ophys (ProcessingModule) processed 2p data
  Group /processing/ophys/Fluorescence (Fluorescence) 
  Group /processing/ophys/Fluorescence/RoiResponseSeries1 (RoiResponseSeries) The fluorescence traces for field 1
  Dataset /processing/ophys/Fluorescence/RoiResponseSeries1/rois (DynamicTableRegion) all rois in channel 1 | shape = (1,) | dtype = int64
  Group /processing/ophys/Fluorescence/RoiResponseSeries2 (RoiResponseSeries) The fluorescence traces for field 2
  Dataset /processing/ophys/Fluorescence/RoiResponseSeries2/rois (DynamicTableRegion) all rois in channel 2 | shape = (1,) | dtype = int64
  Group /processing/ophys/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation1 (PlaneSegmentation) The output from chan 1 contains the image masks (weights and mask classification) and the structural ids extracted from the jr-database on 2025-01-06. 
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation1/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation1/image_mask (VectorData) The image masks for each ROI. | shape = (1, 512, 512) | dtype = float32
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation1/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation1/imaging_plane/chan1 (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation1/imaging_plane/device (Device) two-photon random access mesoscope
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation1/mask_type (VectorData) The classification of mask as soma or artifact. | shape = (1,) | dtype = object
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation2 (PlaneSegmentation) The output from chan 2 contains the image masks (weights and mask classification) and the structural ids extracted from the jr-database on 2025-01-06. 
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation2/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation2/image_mask (VectorData) The image masks for each ROI. | shape = (1, 512, 512) | dtype = float32
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation2/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation2/imaging_plane/chan2 (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation2/imaging_plane/device (Device) two-photon random access mesoscope
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation2/mask_type (VectorData) The classification of mask as soma or artifact. | shape = (1,) | dtype = object
  Group /processing/ophys/SummaryImages_chan1 (Images) Correlation and average images for channel 1.
  Dataset /processing/ophys/SummaryImages_chan1/average (GrayscaleImage) average image for the stack  | shape = (512, 512) | dtype = float64
  Dataset /processing/ophys/SummaryImages_chan1/correlation (GrayscaleImage) summary image for the stack using locally spatial correlations | shape = (512, 512) | dtype = float64
  Group /processing/ophys/SummaryImages_chan2 (Images) Correlation and average images for channel 2.
  Dataset /processing/ophys/SummaryImages_chan2/average (GrayscaleImage) average image for the stack  | shape = (512, 512) | dtype = float64
  Dataset /processing/ophys/SummaryImages_chan2/correlation (GrayscaleImage) summary image for the stack using locally spatial correlations | shape = (512, 512) | dtype = float64
  session_description: Two-Photon imaging
  session_start_time: 2022-05-17T00:01:38-05:51
  timestamps_reference_time: 2022-05-17T00:01:38-05:51
