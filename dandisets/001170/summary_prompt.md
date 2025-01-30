
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001170/draft
name: Mesoscale Two-Photon Calcium Imaging of Population Level Odor Responses from the Mouse Olfactory Bulb
contributor: [{'name': 'National Institutes of Health (NIH)', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': '1 UF1 NS 111692-01'}, {'name': 'Pfaffinger, Paul', 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Hanson, Elizabeth', 'email': 'mosse@ohsu.edu', 'schemaKey': 'Person', 'identifier': '0000-0002-5150-8926', 'includeInCitation': True}, {'name': 'Pirhayatifard, Delaram', 'email': 'dp43@rice.edu', 'schemaKey': 'Person', 'includeInCitation': True}, {'url': 'https://www.bcm.edu/research/labs/jacob-reimer', 'name': 'Reimer, Jacob', 'email': 'reimer@bcm.edu', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0003-4364-8846', 'includeInCitation': True}, {'name': 'Hu, Ming', 'email': 'ming.hu@bcm.edu', 'schemaKey': 'Person', 'includeInCitation': True}, {'url': 'https://ankitlab.co/', 'name': 'Patel, Ankit ', 'email': 'ankitp@bcm.edu', 'schemaKey': 'Person', 'identifier': '0000-0001-9678-496X', 'includeInCitation': False}, {'url': 'https://facultyprofiles.cshl.edu/saket.navlakha', 'name': 'Navlakha, Saket', 'email': 'navlakha@cshl.edu', 'schemaKey': 'Person', 'identifier': '0000-0002-5505-9718', 'includeInCitation': True}, {'name': 'Arenkiel, Benjamin', 'email': 'arenkiel@bcm.edu', 'schemaKey': 'Person', 'identifier': '0000-0001-9047-2420', 'includeInCitation': True}]
description: This study explores odor-evoked activity representation in the olfactory bulb (OB) and how odor responses enable odor discrimination. Contrary to some previously cited theories that suggest a sparse representation, we hypothesize a more dense representation during odor presentation. A key question is how odors are reliably encoded in OB activity patterns, and how these patterns contribute to early odor processing. To address this problem, we recorded population level odor responses from the mouse OB with mesoscale two photon calcium imaging and applied machine learning techniques to suggest a model in which sparse coding is largely sufficient for olfaction, but redundant information may make odor coding more robust across different variables.
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'behavioral approach', 'schemaKey': 'ApproachType'}, {'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 352083757265, 'numberOfFiles': 12, 'numberOfSubjects': 8, 'variableMeasured': ['SpatialSeries', 'ProcessingModule', 'PlaneSegmentation', 'OpticalChannel', 'TwoPhotonSeries', 'ImagingPlane'], 'measurementTechnique': [{'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'two-photon microscopy technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 001170 has 12 NWB files.
1 of these NWB files are of type 1.
10 of these NWB files are of type 2.
1 of these NWB files are of type 3.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/respiration (TimeSeries) respiration rate from Respiration table
  Group /acquisition/treadmill_position (SpatialSeries) treadmill position from Treadmill table
  Group /acquisition/two_photon_series_FOV1_channel1 (TwoPhotonSeries) FOV1 refers to the left part of the original ScanImage acquisition. To maximize frame rates in each imaging session, fields of view were defined for acquisition that included a single plane visualizing only the dorsal surface of bilateral OBs (1800 um long x ~600um wide fields of view that were tiled to cover a total field of view that was 1800-2500 um wide). Images were acquired continuously throughout experiments (during odor presentations, intertrial, and inter-block intervals), with 5um/pixel resolution at the fastest possible frame rate allowed by the imaging parameters (15-18 Hz).
  Group /acquisition/two_photon_series_FOV1_channel1/imaging_plane (ImagingPlane) 
  Group /acquisition/two_photon_series_FOV1_channel1/imaging_plane/channel_1 (OpticalChannel) 
  Group /acquisition/two_photon_series_FOV1_channel1/imaging_plane/device (Device) Janelia 2P-RAM mesoscope.
  Group /acquisition/two_photon_series_FOV2_channel1 (TwoPhotonSeries) FOV2 refers to the central part of the original ScanImage acquisition. To maximize frame rates in each imaging session, fields of view were defined for acquisition that included a single plane visualizing only the dorsal surface of bilateral OBs (1800 um long x ~600um wide fields of view that were tiled to cover a total field of view that was 1800-2500 um wide). Images were acquired continuously throughout experiments (during odor presentations, intertrial, and inter-block intervals), with 5um/pixel resolution at the fastest possible frame rate allowed by the imaging parameters (15-18 Hz).
  Group /acquisition/two_photon_series_FOV2_channel1/imaging_plane (ImagingPlane) 
  Group /acquisition/two_photon_series_FOV2_channel1/imaging_plane/channel_1 (OpticalChannel) 
  Group /acquisition/two_photon_series_FOV2_channel1/imaging_plane/device (Device) Janelia 2P-RAM mesoscope.
  Group /acquisition/two_photon_series_FOV3_channel1 (TwoPhotonSeries) FOV3 refers to the right part of the original ScanImage acquisition. To maximize frame rates in each imaging session, fields of view were defined for acquisition that included a single plane visualizing only the dorsal surface of bilateral OBs (1800 um long x ~600um wide fields of view that were tiled to cover a total field of view that was 1800-2500 um wide). Images were acquired continuously throughout experiments (during odor presentations, intertrial, and inter-block intervals), with 5um/pixel resolution at the fastest possible frame rate allowed by the imaging parameters (15-18 Hz).
  Group /acquisition/two_photon_series_FOV3_channel1/imaging_plane (ImagingPlane) 
  Group /acquisition/two_photon_series_FOV3_channel1/imaging_plane/channel_1 (OpticalChannel) 
  Group /acquisition/two_photon_series_FOV3_channel1/imaging_plane/device (Device) Janelia 2P-RAM mesoscope.
  file_create_date: ['2024-08-06T22:13:45.595172+02:00']
  Group /general/devices/two_photon_microscope (Device) Janelia 2P-RAM mesoscope.
  experiment_description: Awake mice were head fixed on a running wheel and presented with odors. A meso-scale two-photon microscope was used to image glomerular activity in the olfactory bulb.
  experimenter: ['Pirhayatifard, Delaram' 'Hanson, Elizabeth' 'Pfaffinger, Paul'
   'Arenkiel, Benjamin' 'Reimer, Jacob']
  institution: Baylor College of Medicine
  keywords: ['odor-evoked activity' 'olfactory bulb' 'two photon calcium imaging']
  lab: Reimer-Arenkiel
  Group /general/optophysiology/imaging_plane_channel1 (ImagingPlane) 
  Group /general/optophysiology/imaging_plane_channel1/channel_1 (OpticalChannel) 
  Group /general/optophysiology/imaging_plane_channel1/device (Device) Janelia 2P-RAM mesoscope.
  related_publications: ['https://doi.org/10.1101/2023.04.24.538157'
   'https://icml-compbio.github.io/2023/papers/WCBICML2023_paper122.pdf']
  session_id: 3
  Group /general/subject (Subject) 
  identifier: 59466e92-2d2d-46ec-8d7a-fd2daa6c961f
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/concentration (VectorData) the concentration of the odorant | shape = (241,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (241,) | dtype = int32
  Dataset /intervals/trials/odorant (VectorData) the name of the odorant | shape = (241,) | dtype = object
  Dataset /intervals/trials/solution_date (VectorData) the date the odorant solution was made | shape = (241,) | dtype = object
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (241,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (241,) | dtype = float64
  Group /processing/behavior (ProcessingModule) behavioral data processing
  Group /processing/behavior/treadmill_velocity (TimeSeries) treadmill velocity from Treadmill table
  Group /processing/ophys (ProcessingModule) ophys data processing
  Group /processing/ophys/average_images (Images) Average image of from SummaryImages.Average table.
  Dataset /processing/ophys/average_images/average_image_FOV1_channel1 (GrayscaleImage) Average image of FOV1 Channel 1. | shape = (502, 120) | dtype = float64
  Dataset /processing/ophys/average_images/average_image_FOV2_channel1 (GrayscaleImage) Average image of FOV2 Channel 1. | shape = (502, 120) | dtype = float64
  Dataset /processing/ophys/average_images/average_image_FOV3_channel1 (GrayscaleImage) Average image of FOV3 Channel 1. | shape = (420, 120) | dtype = float64
  Group /processing/ophys/correlation_images (Images) Correlation image from SummaryImages.Correlation table.
  Dataset /processing/ophys/correlation_images/correlation_image_FOV1_channel1 (GrayscaleImage) Correlation image of FOV1 Channel 1 | shape = (502, 120) | dtype = float64
  Dataset /processing/ophys/correlation_images/correlation_image_FOV2_channel1 (GrayscaleImage) Correlation image of FOV2 Channel 1 | shape = (502, 120) | dtype = float64
  Dataset /processing/ophys/correlation_images/correlation_image_FOV3_channel1 (GrayscaleImage) Correlation image of FOV3 Channel 1 | shape = (420, 120) | dtype = float64
  Group /processing/ophys/fluorescence (Fluorescence) 
  Group /processing/ophys/fluorescence/fluorescence_FOV1_channel1 (RoiResponseSeries) Fluorescence traces from FOV1 Channel1
  Dataset /processing/ophys/fluorescence/fluorescence_FOV1_channel1/rois (DynamicTableRegion) all ROIs | shape = (182,) | dtype = int32
  Group /processing/ophys/fluorescence/fluorescence_FOV2_channel1 (RoiResponseSeries) Fluorescence traces from FOV2 Channel1
  Dataset /processing/ophys/fluorescence/fluorescence_FOV2_channel1/rois (DynamicTableRegion) all ROIs | shape = (237,) | dtype = int32
  Group /processing/ophys/fluorescence/fluorescence_FOV3_channel1 (RoiResponseSeries) Fluorescence traces from FOV3 Channel1
  Dataset /processing/ophys/fluorescence/fluorescence_FOV3_channel1/rois (DynamicTableRegion) all ROIs | shape = (140,) | dtype = int32
  Group /processing/ophys/image_segmentation (ImageSegmentation) 
  Group /processing/ophys/image_segmentation/plane_segmentation_FOV1_channel1 (PlaneSegmentation) Output from segmenting FOV1 Channel 1.
  Dataset /processing/ophys/image_segmentation/plane_segmentation_FOV1_channel1/id (ElementIdentifiers)  | shape = (182,) | dtype = int32
  Group /processing/ophys/image_segmentation/plane_segmentation_FOV1_channel1/imaging_plane (ImagingPlane) 
  Group /processing/ophys/image_segmentation/plane_segmentation_FOV1_channel1/imaging_plane/channel_1 (OpticalChannel) 
  Group /processing/ophys/image_segmentation/plane_segmentation_FOV1_channel1/imaging_plane/device (Device) Janelia 2P-RAM mesoscope.
  Dataset /processing/ophys/image_segmentation/plane_segmentation_FOV1_channel1/pixel_mask (VectorData) Pixel masks for each ROI | shape = (29634,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/image_segmentation/plane_segmentation_FOV1_channel1/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (182,) | dtype = uint16
  Group /processing/ophys/image_segmentation/plane_segmentation_FOV2_channel1 (PlaneSegmentation) Output from segmenting FOV2 Channel 1.
  Dataset /processing/ophys/image_segmentation/plane_segmentation_FOV2_channel1/id (ElementIdentifiers)  | shape = (237,) | dtype = int32
  Group /processing/ophys/image_segmentation/plane_segmentation_FOV2_channel1/imaging_plane (ImagingPlane) 
  Group /processing/ophys/image_segmentation/plane_segmentation_FOV2_channel1/imaging_plane/channel_1 (OpticalChannel) 
  Group /processing/ophys/image_segmentation/plane_segmentation_FOV2_channel1/imaging_plane/device (Device) Janelia 2P-RAM mesoscope.
  Dataset /processing/ophys/image_segmentation/plane_segmentation_FOV2_channel1/pixel_mask (VectorData) Pixel masks for each ROI | shape = (28158,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/image_segmentation/plane_segmentation_FOV2_channel1/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (237,) | dtype = uint16
  Group /processing/ophys/image_segmentation/plane_segmentation_FOV3_channel1 (PlaneSegmentation) Output from segmenting FOV3 Channel 1.
  Dataset /processing/ophys/image_segmentation/plane_segmentation_FOV3_channel1/id (ElementIdentifiers)  | shape = (140,) | dtype = int32
  Group /processing/ophys/image_segmentation/plane_segmentation_FOV3_channel1/imaging_plane (ImagingPlane) 
  Group /processing/ophys/image_segmentation/plane_segmentation_FOV3_channel1/imaging_plane/channel_1 (OpticalChannel) 
  Group /processing/ophys/image_segmentation/plane_segmentation_FOV3_channel1/imaging_plane/device (Device) Janelia 2P-RAM mesoscope.
  Dataset /processing/ophys/image_segmentation/plane_segmentation_FOV3_channel1/pixel_mask (VectorData) Pixel masks for each ROI | shape = (18154,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/image_segmentation/plane_segmentation_FOV3_channel1/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (140,) | dtype = uint16
  session_description: In this study, we explore odor-evoked activity representation in the olfactory bulb (OB) and how odor responses enable odor discrimination. Contrary to some previously cited theories that suggest a sparse representation, we hypothesize a more dense representation during odor presentation. A key question is how odors are reliably encoded in OB activity patterns, and how these patterns contribute to early odor processing. To address this problem, we recorded population level odor responses from the mouse OB with mesoscale two photon calcium imaging and applied machine learning techniques to suggest a model in which sparse coding is largely sufficient for olfaction, but redundant information may make odor coding more robust across different variables.
  session_start_time: 2021-03-22T00:00:00-05:00
  timestamps_reference_time: 2021-03-22T00:00:00-05:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/treadmill_position (SpatialSeries) treadmill position from Treadmill table
  Group /acquisition/two_photon_series_FOV1_channel1 (TwoPhotonSeries) FOV1 refers to the left part of the original ScanImage acquisition. To maximize frame rates in each imaging session, fields of view were defined for acquisition that included a single plane visualizing only the dorsal surface of bilateral OBs (1800 um long x ~600um wide fields of view that were tiled to cover a total field of view that was 1800-2500 um wide). Images were acquired continuously throughout experiments (during odor presentations, intertrial, and inter-block intervals), with 5um/pixel resolution at the fastest possible frame rate allowed by the imaging parameters (15-18 Hz).
  Group /acquisition/two_photon_series_FOV1_channel1/imaging_plane (ImagingPlane) 
  Group /acquisition/two_photon_series_FOV1_channel1/imaging_plane/channel_1 (OpticalChannel) 
  Group /acquisition/two_photon_series_FOV1_channel1/imaging_plane/device (Device) Janelia 2P-RAM mesoscope.
  Group /acquisition/two_photon_series_FOV2_channel1 (TwoPhotonSeries) FOV2 refers to the central part of the original ScanImage acquisition. To maximize frame rates in each imaging session, fields of view were defined for acquisition that included a single plane visualizing only the dorsal surface of bilateral OBs (1800 um long x ~600um wide fields of view that were tiled to cover a total field of view that was 1800-2500 um wide). Images were acquired continuously throughout experiments (during odor presentations, intertrial, and inter-block intervals), with 5um/pixel resolution at the fastest possible frame rate allowed by the imaging parameters (15-18 Hz).
  Group /acquisition/two_photon_series_FOV2_channel1/imaging_plane (ImagingPlane) 
  Group /acquisition/two_photon_series_FOV2_channel1/imaging_plane/channel_1 (OpticalChannel) 
  Group /acquisition/two_photon_series_FOV2_channel1/imaging_plane/device (Device) Janelia 2P-RAM mesoscope.
  Group /acquisition/two_photon_series_FOV3_channel1 (TwoPhotonSeries) FOV3 refers to the right part of the original ScanImage acquisition. To maximize frame rates in each imaging session, fields of view were defined for acquisition that included a single plane visualizing only the dorsal surface of bilateral OBs (1800 um long x ~600um wide fields of view that were tiled to cover a total field of view that was 1800-2500 um wide). Images were acquired continuously throughout experiments (during odor presentations, intertrial, and inter-block intervals), with 5um/pixel resolution at the fastest possible frame rate allowed by the imaging parameters (15-18 Hz).
  Group /acquisition/two_photon_series_FOV3_channel1/imaging_plane (ImagingPlane) 
  Group /acquisition/two_photon_series_FOV3_channel1/imaging_plane/channel_1 (OpticalChannel) 
  Group /acquisition/two_photon_series_FOV3_channel1/imaging_plane/device (Device) Janelia 2P-RAM mesoscope.
  file_create_date: ['2024-08-06T22:34:04.410597+02:00']
  Group /general/devices/two_photon_microscope (Device) Janelia 2P-RAM mesoscope.
  experiment_description: Awake mice were head fixed on a running wheel and presented with odors. A meso-scale two-photon microscope was used to image glomerular activity in the olfactory bulb.
  experimenter: ['Pirhayatifard, Delaram' 'Hanson, Elizabeth' 'Pfaffinger, Paul'
   'Arenkiel, Benjamin' 'Reimer, Jacob']
  institution: Baylor College of Medicine
  keywords: ['odor-evoked activity' 'olfactory bulb' 'two photon calcium imaging']
  lab: Reimer-Arenkiel
  Group /general/optophysiology/imaging_plane_channel1 (ImagingPlane) 
  Group /general/optophysiology/imaging_plane_channel1/channel_1 (OpticalChannel) 
  Group /general/optophysiology/imaging_plane_channel1/device (Device) Janelia 2P-RAM mesoscope.
  related_publications: ['https://doi.org/10.1101/2023.04.24.538157'
   'https://icml-compbio.github.io/2023/papers/WCBICML2023_paper122.pdf']
  session_id: 1
  Group /general/subject (Subject) 
  identifier: aa9c10a8-a5de-4360-a2e4-64f8571e473b
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/concentration (VectorData) the concentration of the odorant | shape = (480,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (480,) | dtype = int32
  Dataset /intervals/trials/odorant (VectorData) the name of the odorant | shape = (480,) | dtype = object
  Dataset /intervals/trials/solution_date (VectorData) the date the odorant solution was made | shape = (480,) | dtype = object
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (480,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (480,) | dtype = float64
  Group /processing/behavior (ProcessingModule) behavioral data processing
  Group /processing/behavior/treadmill_velocity (TimeSeries) treadmill velocity from Treadmill table
  Group /processing/ophys (ProcessingModule) ophys data processing
  Group /processing/ophys/average_images (Images) Average image of from SummaryImages.Average table.
  Dataset /processing/ophys/average_images/average_image_FOV1_channel1 (GrayscaleImage) Average image of FOV1 Channel 1. | shape = (502, 120) | dtype = float64
  Dataset /processing/ophys/average_images/average_image_FOV2_channel1 (GrayscaleImage) Average image of FOV2 Channel 1. | shape = (502, 120) | dtype = float64
  Dataset /processing/ophys/average_images/average_image_FOV3_channel1 (GrayscaleImage) Average image of FOV3 Channel 1. | shape = (440, 120) | dtype = float64
  Group /processing/ophys/correlation_images (Images) Correlation image from SummaryImages.Correlation table.
  Dataset /processing/ophys/correlation_images/correlation_image_FOV1_channel1 (GrayscaleImage) Correlation image of FOV1 Channel 1 | shape = (502, 120) | dtype = float64
  Dataset /processing/ophys/correlation_images/correlation_image_FOV2_channel1 (GrayscaleImage) Correlation image of FOV2 Channel 1 | shape = (502, 120) | dtype = float64
  Dataset /processing/ophys/correlation_images/correlation_image_FOV3_channel1 (GrayscaleImage) Correlation image of FOV3 Channel 1 | shape = (440, 120) | dtype = float64
  Group /processing/ophys/fluorescence (Fluorescence) 
  Group /processing/ophys/fluorescence/fluorescence_FOV1_channel1 (RoiResponseSeries) Fluorescence traces from FOV1 Channel1
  Dataset /processing/ophys/fluorescence/fluorescence_FOV1_channel1/rois (DynamicTableRegion) all ROIs | shape = (105,) | dtype = int32
  Group /processing/ophys/fluorescence/fluorescence_FOV2_channel1 (RoiResponseSeries) Fluorescence traces from FOV2 Channel1
  Dataset /processing/ophys/fluorescence/fluorescence_FOV2_channel1/rois (DynamicTableRegion) all ROIs | shape = (142,) | dtype = int32
  Group /processing/ophys/fluorescence/fluorescence_FOV3_channel1 (RoiResponseSeries) Fluorescence traces from FOV3 Channel1
  Dataset /processing/ophys/fluorescence/fluorescence_FOV3_channel1/rois (DynamicTableRegion) all ROIs | shape = (78,) | dtype = int32
  Group /processing/ophys/image_segmentation (ImageSegmentation) 
  Group /processing/ophys/image_segmentation/plane_segmentation_FOV1_channel1 (PlaneSegmentation) Output from segmenting FOV1 Channel 1.
  Dataset /processing/ophys/image_segmentation/plane_segmentation_FOV1_channel1/id (ElementIdentifiers)  | shape = (105,) | dtype = int32
  Group /processing/ophys/image_segmentation/plane_segmentation_FOV1_channel1/imaging_plane (ImagingPlane) 
  Group /processing/ophys/image_segmentation/plane_segmentation_FOV1_channel1/imaging_plane/channel_1 (OpticalChannel) 
  Group /processing/ophys/image_segmentation/plane_segmentation_FOV1_channel1/imaging_plane/device (Device) Janelia 2P-RAM mesoscope.
  Dataset /processing/ophys/image_segmentation/plane_segmentation_FOV1_channel1/pixel_mask (VectorData) Pixel masks for each ROI | shape = (23360,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/image_segmentation/plane_segmentation_FOV1_channel1/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (105,) | dtype = uint16
  Group /processing/ophys/image_segmentation/plane_segmentation_FOV2_channel1 (PlaneSegmentation) Output from segmenting FOV2 Channel 1.
  Dataset /processing/ophys/image_segmentation/plane_segmentation_FOV2_channel1/id (ElementIdentifiers)  | shape = (142,) | dtype = int32
  Group /processing/ophys/image_segmentation/plane_segmentation_FOV2_channel1/imaging_plane (ImagingPlane) 
  Group /processing/ophys/image_segmentation/plane_segmentation_FOV2_channel1/imaging_plane/channel_1 (OpticalChannel) 
  Group /processing/ophys/image_segmentation/plane_segmentation_FOV2_channel1/imaging_plane/device (Device) Janelia 2P-RAM mesoscope.
  Dataset /processing/ophys/image_segmentation/plane_segmentation_FOV2_channel1/pixel_mask (VectorData) Pixel masks for each ROI | shape = (27541,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/image_segmentation/plane_segmentation_FOV2_channel1/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (142,) | dtype = uint16
  Group /processing/ophys/image_segmentation/plane_segmentation_FOV3_channel1 (PlaneSegmentation) Output from segmenting FOV3 Channel 1.
  Dataset /processing/ophys/image_segmentation/plane_segmentation_FOV3_channel1/id (ElementIdentifiers)  | shape = (78,) | dtype = int32
  Group /processing/ophys/image_segmentation/plane_segmentation_FOV3_channel1/imaging_plane (ImagingPlane) 
  Group /processing/ophys/image_segmentation/plane_segmentation_FOV3_channel1/imaging_plane/channel_1 (OpticalChannel) 
  Group /processing/ophys/image_segmentation/plane_segmentation_FOV3_channel1/imaging_plane/device (Device) Janelia 2P-RAM mesoscope.
  Dataset /processing/ophys/image_segmentation/plane_segmentation_FOV3_channel1/pixel_mask (VectorData) Pixel masks for each ROI | shape = (11149,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/image_segmentation/plane_segmentation_FOV3_channel1/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (78,) | dtype = uint16
  session_description: In this study, we explore odor-evoked activity representation in the olfactory bulb (OB) and how odor responses enable odor discrimination. Contrary to some previously cited theories that suggest a sparse representation, we hypothesize a more dense representation during odor presentation. A key question is how odors are reliably encoded in OB activity patterns, and how these patterns contribute to early odor processing. To address this problem, we recorded population level odor responses from the mouse OB with mesoscale two photon calcium imaging and applied machine learning techniques to suggest a model in which sparse coding is largely sufficient for olfaction, but redundant information may make odor coding more robust across different variables.
  session_start_time: 2021-03-16T00:00:00-05:00
  timestamps_reference_time: 2021-03-16T00:00:00-05:00


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/treadmill_position (SpatialSeries) treadmill position from Treadmill table
  Group /acquisition/two_photon_series_FOV1_channel1 (TwoPhotonSeries) FOV1 refers to the left part of the original ScanImage acquisition. To maximize frame rates in each imaging session, fields of view were defined for acquisition that included a single plane visualizing only the dorsal surface of bilateral OBs (1800 um long x ~600um wide fields of view that were tiled to cover a total field of view that was 1800-2500 um wide). Images were acquired continuously throughout experiments (during odor presentations, intertrial, and inter-block intervals), with 5um/pixel resolution at the fastest possible frame rate allowed by the imaging parameters (15-18 Hz).
  Group /acquisition/two_photon_series_FOV1_channel1/imaging_plane (ImagingPlane) 
  Group /acquisition/two_photon_series_FOV1_channel1/imaging_plane/channel_1 (OpticalChannel) 
  Group /acquisition/two_photon_series_FOV1_channel1/imaging_plane/device (Device) Janelia 2P-RAM mesoscope.
  Group /acquisition/two_photon_series_FOV2_channel1 (TwoPhotonSeries) FOV2 refers to the central part of the original ScanImage acquisition. To maximize frame rates in each imaging session, fields of view were defined for acquisition that included a single plane visualizing only the dorsal surface of bilateral OBs (1800 um long x ~600um wide fields of view that were tiled to cover a total field of view that was 1800-2500 um wide). Images were acquired continuously throughout experiments (during odor presentations, intertrial, and inter-block intervals), with 5um/pixel resolution at the fastest possible frame rate allowed by the imaging parameters (15-18 Hz).
  Group /acquisition/two_photon_series_FOV2_channel1/imaging_plane (ImagingPlane) 
  Group /acquisition/two_photon_series_FOV2_channel1/imaging_plane/channel_1 (OpticalChannel) 
  Group /acquisition/two_photon_series_FOV2_channel1/imaging_plane/device (Device) Janelia 2P-RAM mesoscope.
  Group /acquisition/two_photon_series_FOV3_channel1 (TwoPhotonSeries) FOV3 refers to the right part of the original ScanImage acquisition. To maximize frame rates in each imaging session, fields of view were defined for acquisition that included a single plane visualizing only the dorsal surface of bilateral OBs (1800 um long x ~600um wide fields of view that were tiled to cover a total field of view that was 1800-2500 um wide). Images were acquired continuously throughout experiments (during odor presentations, intertrial, and inter-block intervals), with 5um/pixel resolution at the fastest possible frame rate allowed by the imaging parameters (15-18 Hz).
  Group /acquisition/two_photon_series_FOV3_channel1/imaging_plane (ImagingPlane) 
  Group /acquisition/two_photon_series_FOV3_channel1/imaging_plane/channel_1 (OpticalChannel) 
  Group /acquisition/two_photon_series_FOV3_channel1/imaging_plane/device (Device) Janelia 2P-RAM mesoscope.
  file_create_date: ['2024-08-14T11:17:18.056842+02:00']
  Group /general/devices/two_photon_microscope (Device) Janelia 2P-RAM mesoscope.
  experiment_description: Awake mice were head fixed on a running wheel and presented with odors. A meso-scale two-photon microscope was used to image glomerular activity in the olfactory bulb.
  experimenter: ['Pirhayatifard, Delaram' 'Hanson, Elizabeth' 'Pfaffinger, Paul'
   'Arenkiel, Benjamin' 'Reimer, Jacob']
  institution: Baylor College of Medicine
  keywords: ['odor-evoked activity' 'olfactory bulb' 'two photon calcium imaging']
  lab: Reimer-Arenkiel
  Group /general/optophysiology/imaging_plane_channel1 (ImagingPlane) 
  Group /general/optophysiology/imaging_plane_channel1/channel_1 (OpticalChannel) 
  Group /general/optophysiology/imaging_plane_channel1/device (Device) Janelia 2P-RAM mesoscope.
  related_publications: ['https://doi.org/10.1101/2023.04.24.538157'
   'https://icml-compbio.github.io/2023/papers/WCBICML2023_paper122.pdf']
  session_id: 1
  Group /general/subject (Subject) 
  identifier: 0a6677b4-1466-49e2-aea4-6a2a53a0962c
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/concentration (VectorData) the concentration of the odorant | shape = (480,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (480,) | dtype = int32
  Dataset /intervals/trials/odorant (VectorData) the name of the odorant | shape = (480,) | dtype = object
  Dataset /intervals/trials/solution_date (VectorData) the date the odorant solution was made | shape = (480,) | dtype = object
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (480,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (480,) | dtype = float64
  Group /processing/behavior (ProcessingModule) behavioral data processing
  Group /processing/behavior/treadmill_velocity (TimeSeries) treadmill velocity from Treadmill table
  Group /processing/ophys (ProcessingModule) ophys data processing
  Group /processing/ophys/average_images (Images) Average image of from SummaryImages.Average table.
  Dataset /processing/ophys/average_images/average_image_FOV1_channel1 (GrayscaleImage) Average image of FOV1 Channel 1. | shape = (540, 120) | dtype = float64
  Dataset /processing/ophys/average_images/average_image_FOV1_channel2 (GrayscaleImage) Average image of FOV1 Channel 2. | shape = (540, 120) | dtype = float64
  Dataset /processing/ophys/average_images/average_image_FOV2_channel1 (GrayscaleImage) Average image of FOV2 Channel 1. | shape = (520, 120) | dtype = float64
  Dataset /processing/ophys/average_images/average_image_FOV2_channel2 (GrayscaleImage) Average image of FOV2 Channel 2. | shape = (520, 120) | dtype = float64
  Dataset /processing/ophys/average_images/average_image_FOV3_channel1 (GrayscaleImage) Average image of FOV3 Channel 1. | shape = (480, 120) | dtype = float64
  Dataset /processing/ophys/average_images/average_image_FOV3_channel2 (GrayscaleImage) Average image of FOV3 Channel 2. | shape = (480, 120) | dtype = float64
  Group /processing/ophys/correlation_images (Images) Correlation image from SummaryImages.Correlation table.
  Dataset /processing/ophys/correlation_images/correlation_image_FOV1_channel1 (GrayscaleImage) Correlation image of FOV1 Channel 1 | shape = (540, 120) | dtype = float64
  Dataset /processing/ophys/correlation_images/correlation_image_FOV1_channel2 (GrayscaleImage) Correlation image of FOV1 Channel 2 | shape = (540, 120) | dtype = float64
  Dataset /processing/ophys/correlation_images/correlation_image_FOV2_channel1 (GrayscaleImage) Correlation image of FOV2 Channel 1 | shape = (520, 120) | dtype = float64
  Dataset /processing/ophys/correlation_images/correlation_image_FOV2_channel2 (GrayscaleImage) Correlation image of FOV2 Channel 2 | shape = (520, 120) | dtype = float64
  Dataset /processing/ophys/correlation_images/correlation_image_FOV3_channel1 (GrayscaleImage) Correlation image of FOV3 Channel 1 | shape = (480, 120) | dtype = float64
  Dataset /processing/ophys/correlation_images/correlation_image_FOV3_channel2 (GrayscaleImage) Correlation image of FOV3 Channel 2 | shape = (480, 120) | dtype = float64
  Group /processing/ophys/fluorescence (Fluorescence) 
  Group /processing/ophys/fluorescence/fluorescence_FOV1_channel1 (RoiResponseSeries) Fluorescence traces from FOV1 Channel1
  Dataset /processing/ophys/fluorescence/fluorescence_FOV1_channel1/rois (DynamicTableRegion) all ROIs | shape = (143,) | dtype = int32
  Group /processing/ophys/fluorescence/fluorescence_FOV2_channel1 (RoiResponseSeries) Fluorescence traces from FOV2 Channel1
  Dataset /processing/ophys/fluorescence/fluorescence_FOV2_channel1/rois (DynamicTableRegion) all ROIs | shape = (91,) | dtype = int32
  Group /processing/ophys/fluorescence/fluorescence_FOV3_channel1 (RoiResponseSeries) Fluorescence traces from FOV3 Channel1
  Dataset /processing/ophys/fluorescence/fluorescence_FOV3_channel1/rois (DynamicTableRegion) all ROIs | shape = (169,) | dtype = int32
  Group /processing/ophys/image_segmentation (ImageSegmentation) 
  Group /processing/ophys/image_segmentation/plane_segmentation_FOV1_channel1 (PlaneSegmentation) Output from segmenting FOV1 Channel 1.
  Dataset /processing/ophys/image_segmentation/plane_segmentation_FOV1_channel1/id (ElementIdentifiers)  | shape = (143,) | dtype = int32
  Group /processing/ophys/image_segmentation/plane_segmentation_FOV1_channel1/imaging_plane (ImagingPlane) 
  Group /processing/ophys/image_segmentation/plane_segmentation_FOV1_channel1/imaging_plane/channel_1 (OpticalChannel) 
  Group /processing/ophys/image_segmentation/plane_segmentation_FOV1_channel1/imaging_plane/device (Device) Janelia 2P-RAM mesoscope.
  Dataset /processing/ophys/image_segmentation/plane_segmentation_FOV1_channel1/pixel_mask (VectorData) Pixel masks for each ROI | shape = (15398,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/image_segmentation/plane_segmentation_FOV1_channel1/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (143,) | dtype = uint16
  Group /processing/ophys/image_segmentation/plane_segmentation_FOV2_channel1 (PlaneSegmentation) Output from segmenting FOV2 Channel 1.
  Dataset /processing/ophys/image_segmentation/plane_segmentation_FOV2_channel1/id (ElementIdentifiers)  | shape = (91,) | dtype = int32
  Group /processing/ophys/image_segmentation/plane_segmentation_FOV2_channel1/imaging_plane (ImagingPlane) 
  Group /processing/ophys/image_segmentation/plane_segmentation_FOV2_channel1/imaging_plane/channel_1 (OpticalChannel) 
  Group /processing/ophys/image_segmentation/plane_segmentation_FOV2_channel1/imaging_plane/device (Device) Janelia 2P-RAM mesoscope.
  Dataset /processing/ophys/image_segmentation/plane_segmentation_FOV2_channel1/pixel_mask (VectorData) Pixel masks for each ROI | shape = (15831,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/image_segmentation/plane_segmentation_FOV2_channel1/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (91,) | dtype = uint16
  Group /processing/ophys/image_segmentation/plane_segmentation_FOV3_channel1 (PlaneSegmentation) Output from segmenting FOV3 Channel 1.
  Dataset /processing/ophys/image_segmentation/plane_segmentation_FOV3_channel1/id (ElementIdentifiers)  | shape = (169,) | dtype = int32
  Group /processing/ophys/image_segmentation/plane_segmentation_FOV3_channel1/imaging_plane (ImagingPlane) 
  Group /processing/ophys/image_segmentation/plane_segmentation_FOV3_channel1/imaging_plane/channel_1 (OpticalChannel) 
  Group /processing/ophys/image_segmentation/plane_segmentation_FOV3_channel1/imaging_plane/device (Device) Janelia 2P-RAM mesoscope.
  Dataset /processing/ophys/image_segmentation/plane_segmentation_FOV3_channel1/pixel_mask (VectorData) Pixel masks for each ROI | shape = (19269,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/image_segmentation/plane_segmentation_FOV3_channel1/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (169,) | dtype = uint16
  session_description: In this study, we explore odor-evoked activity representation in the olfactory bulb (OB) and how odor responses enable odor discrimination. Contrary to some previously cited theories that suggest a sparse representation, we hypothesize a more dense representation during odor presentation. A key question is how odors are reliably encoded in OB activity patterns, and how these patterns contribute to early odor processing. To address this problem, we recorded population level odor responses from the mouse OB with mesoscale two photon calcium imaging and applied machine learning techniques to suggest a model in which sparse coding is largely sufficient for olfaction, but redundant information may make odor coding more robust across different variables.
  session_start_time: 2020-07-31T00:00:00-05:00
  timestamps_reference_time: 2020-07-31T00:00:00-05:00
