
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001339/draft
name: Fixed hot/cold stim trigeminal ganglion
contributor: [{'name': 'National Institutes of Health (NIH)', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': '5 R01 NS 123887-04'}, {'name': 'Balakrishnan, Kaarthik A', 'roleName': ['dcite:DataCollector'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Haesemeyer, Martin', 'email': 'haesemeyer.1@osu.edu', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0003-2704-3601', 'includeInCitation': True}]
description: 2-photon calcium imaging in Trigeminal ganglion / lateral hypothalamus using hot/cold flow stimuli
assetsSummary: {'schemaKey': 'AssetsSummary', 'numberOfBytes': 0, 'numberOfFiles': 0}

Dandiset 001339 has 5 NWB files.
1 of these NWB files are of type 1.
1 of these NWB files are of type 2.
1 of these NWB files are of type 3.
1 of these NWB files are of type 4.
1 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/240514_Fish42_GCaMP_vglut_TG_5dpf_FlowExperiment_warner_temp_stim_Z_0_0.tif (TwoPhotonSeries) Raw acquisition photon counts
  Group /acquisition/240514_Fish42_GCaMP_vglut_TG_5dpf_FlowExperiment_warner_temp_stim_Z_0_0.tif/imaging_plane (ImagingPlane) 
  Group /acquisition/240514_Fish42_GCaMP_vglut_TG_5dpf_FlowExperiment_warner_temp_stim_Z_0_0.tif/imaging_plane/Ch0 (OpticalChannel) 
  Group /acquisition/240514_Fish42_GCaMP_vglut_TG_5dpf_FlowExperiment_warner_temp_stim_Z_0_0.tif/imaging_plane/device (Device) OSU Haesemeyer Lab, 2-Photon 1
  file_create_date: ['2025-02-19T17:58:35.881349-05:00']
  Group /general/devices/OSU_2P_1 (Device) OSU Haesemeyer Lab, 2-Photon 1
  Group /general/optophysiology/ImagingPlane (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane/Ch0 (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane/device (Device) OSU Haesemeyer Lab, 2-Photon 1
  Group /general/subject (Subject) 
  identifier: D:/HaesemeyerLab/Two Photon/NewTG_Experiments/240514\240514_Fish42_GCaMP_vglut_TG_5dpf_FlowExperiment_warner_temp_stim_Z_0_0
  Group /processing/ophys (ProcessingModule) optical physiology processed data
  Group /processing/ophys/Backgrounds_0 (Images) no description
  Dataset /processing/ophys/Backgrounds_0/Vcorr (GrayscaleImage)  | shape = (512, 512) | dtype = float32
  Dataset /processing/ophys/Backgrounds_0/max_proj (GrayscaleImage)  | shape = (512, 512) | dtype = float32
  Dataset /processing/ophys/Backgrounds_0/meanImg (GrayscaleImage)  | shape = (512, 512) | dtype = float32
  Group /processing/ophys/Deconvolved (Fluorescence) 
  Group /processing/ophys/Deconvolved/plane0 (RoiResponseSeries) no description
  Dataset /processing/ophys/Deconvolved/plane0/rois (DynamicTableRegion) ROIs for plane0 | shape = (76,) | dtype = int32
  Group /processing/ophys/Fluorescence (Fluorescence) 
  Group /processing/ophys/Fluorescence/plane0 (RoiResponseSeries) no description
  Dataset /processing/ophys/Fluorescence/plane0/rois (DynamicTableRegion) ROIs for plane0 | shape = (76,) | dtype = int32
  Group /processing/ophys/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation (PlaneSegmentation) suite2p output
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/id (ElementIdentifiers)  | shape = (76,) | dtype = int32
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/Ch0 (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/device (Device) OSU Haesemeyer Lab, 2-Photon 1
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/iscell (VectorData) two columns - iscell & probcell | shape = (76, 2) | dtype = float64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/pixel_mask (VectorData) Pixel masks for each ROI | shape = (14934,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (76,) | dtype = uint16
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/reference_images/240514_Fish42_GCaMP_vglut_TG_5dpf_FlowExperiment_warner_temp_stim_Z_0_0.tif (TwoPhotonSeries) Raw acquisition photon counts
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/reference_images/240514_Fish42_GCaMP_vglut_TG_5dpf_FlowExperiment_warner_temp_stim_Z_0_0.tif/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/reference_images/240514_Fish42_GCaMP_vglut_TG_5dpf_FlowExperiment_warner_temp_stim_Z_0_0.tif/imaging_plane/Ch0 (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/reference_images/240514_Fish42_GCaMP_vglut_TG_5dpf_FlowExperiment_warner_temp_stim_Z_0_0.tif/imaging_plane/device (Device) OSU Haesemeyer Lab, 2-Photon 1
  Group /processing/ophys/Neuropil (Fluorescence) 
  Group /processing/ophys/Neuropil/plane0 (RoiResponseSeries) no description
  Dataset /processing/ophys/Neuropil/plane0/rois (DynamicTableRegion) ROIs for plane0 | shape = (76,) | dtype = int32
  session_description: suite2p_proc
  session_start_time: 2025-02-04T15:50:20.363998-05:00
  Group /stimulus/presentation/240514_Fish42_GCaMP_vglut_TG_5dpf_FlowExperiment_warner_temp_stim_Z_0_0 (TimeSeries) Temperature stimulus
  timestamps_reference_time: 2025-02-04T15:50:20.363998-05:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/240514_Fish42_GCaMP_vglut_TG_5dpf_FlowExperiment_warner_temp_stim_Z_1_0.tif (TwoPhotonSeries) Raw acquisition photon counts
  Group /acquisition/240514_Fish42_GCaMP_vglut_TG_5dpf_FlowExperiment_warner_temp_stim_Z_1_0.tif/imaging_plane (ImagingPlane) 
  Group /acquisition/240514_Fish42_GCaMP_vglut_TG_5dpf_FlowExperiment_warner_temp_stim_Z_1_0.tif/imaging_plane/Ch0 (OpticalChannel) 
  Group /acquisition/240514_Fish42_GCaMP_vglut_TG_5dpf_FlowExperiment_warner_temp_stim_Z_1_0.tif/imaging_plane/device (Device) OSU Haesemeyer Lab, 2-Photon 1
  file_create_date: ['2025-02-19T17:58:46.484683-05:00']
  Group /general/devices/OSU_2P_1 (Device) OSU Haesemeyer Lab, 2-Photon 1
  Group /general/optophysiology/ImagingPlane (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane/Ch0 (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane/device (Device) OSU Haesemeyer Lab, 2-Photon 1
  Group /general/subject (Subject) 
  identifier: D:/HaesemeyerLab/Two Photon/NewTG_Experiments/240514\240514_Fish42_GCaMP_vglut_TG_5dpf_FlowExperiment_warner_temp_stim_Z_1_0
  Group /processing/ophys (ProcessingModule) optical physiology processed data
  Group /processing/ophys/Backgrounds_0 (Images) no description
  Dataset /processing/ophys/Backgrounds_0/Vcorr (GrayscaleImage)  | shape = (512, 512) | dtype = float32
  Dataset /processing/ophys/Backgrounds_0/max_proj (GrayscaleImage)  | shape = (512, 512) | dtype = float32
  Dataset /processing/ophys/Backgrounds_0/meanImg (GrayscaleImage)  | shape = (512, 512) | dtype = float32
  Group /processing/ophys/Deconvolved (Fluorescence) 
  Group /processing/ophys/Deconvolved/plane0 (RoiResponseSeries) no description
  Dataset /processing/ophys/Deconvolved/plane0/rois (DynamicTableRegion) ROIs for plane0 | shape = (84,) | dtype = int32
  Group /processing/ophys/Fluorescence (Fluorescence) 
  Group /processing/ophys/Fluorescence/plane0 (RoiResponseSeries) no description
  Dataset /processing/ophys/Fluorescence/plane0/rois (DynamicTableRegion) ROIs for plane0 | shape = (84,) | dtype = int32
  Group /processing/ophys/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation (PlaneSegmentation) suite2p output
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/id (ElementIdentifiers)  | shape = (84,) | dtype = int32
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/Ch0 (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/device (Device) OSU Haesemeyer Lab, 2-Photon 1
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/iscell (VectorData) two columns - iscell & probcell | shape = (84, 2) | dtype = float64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/pixel_mask (VectorData) Pixel masks for each ROI | shape = (15296,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (84,) | dtype = uint16
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/reference_images/240514_Fish42_GCaMP_vglut_TG_5dpf_FlowExperiment_warner_temp_stim_Z_1_0.tif (TwoPhotonSeries) Raw acquisition photon counts
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/reference_images/240514_Fish42_GCaMP_vglut_TG_5dpf_FlowExperiment_warner_temp_stim_Z_1_0.tif/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/reference_images/240514_Fish42_GCaMP_vglut_TG_5dpf_FlowExperiment_warner_temp_stim_Z_1_0.tif/imaging_plane/Ch0 (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/reference_images/240514_Fish42_GCaMP_vglut_TG_5dpf_FlowExperiment_warner_temp_stim_Z_1_0.tif/imaging_plane/device (Device) OSU Haesemeyer Lab, 2-Photon 1
  Group /processing/ophys/Neuropil (Fluorescence) 
  Group /processing/ophys/Neuropil/plane0 (RoiResponseSeries) no description
  Dataset /processing/ophys/Neuropil/plane0/rois (DynamicTableRegion) ROIs for plane0 | shape = (84,) | dtype = int32
  session_description: suite2p_proc
  session_start_time: 2025-02-04T15:42:45.666163-05:00
  Group /stimulus/presentation/240514_Fish42_GCaMP_vglut_TG_5dpf_FlowExperiment_warner_temp_stim_Z_1_0 (TimeSeries) Temperature stimulus
  timestamps_reference_time: 2025-02-04T15:42:45.666163-05:00


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/240514_Fish42_GCaMP_vglut_TG_5dpf_FlowExperiment_warner_temp_stim_Z_2_0.tif (TwoPhotonSeries) Raw acquisition photon counts
  Group /acquisition/240514_Fish42_GCaMP_vglut_TG_5dpf_FlowExperiment_warner_temp_stim_Z_2_0.tif/imaging_plane (ImagingPlane) 
  Group /acquisition/240514_Fish42_GCaMP_vglut_TG_5dpf_FlowExperiment_warner_temp_stim_Z_2_0.tif/imaging_plane/Ch0 (OpticalChannel) 
  Group /acquisition/240514_Fish42_GCaMP_vglut_TG_5dpf_FlowExperiment_warner_temp_stim_Z_2_0.tif/imaging_plane/device (Device) OSU Haesemeyer Lab, 2-Photon 1
  file_create_date: ['2025-02-19T17:58:57.754484-05:00']
  Group /general/devices/OSU_2P_1 (Device) OSU Haesemeyer Lab, 2-Photon 1
  Group /general/optophysiology/ImagingPlane (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane/Ch0 (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane/device (Device) OSU Haesemeyer Lab, 2-Photon 1
  Group /general/subject (Subject) 
  identifier: D:/HaesemeyerLab/Two Photon/NewTG_Experiments/240514\240514_Fish42_GCaMP_vglut_TG_5dpf_FlowExperiment_warner_temp_stim_Z_2_0
  Group /processing/ophys (ProcessingModule) optical physiology processed data
  Group /processing/ophys/Backgrounds_0 (Images) no description
  Dataset /processing/ophys/Backgrounds_0/Vcorr (GrayscaleImage)  | shape = (512, 512) | dtype = float32
  Dataset /processing/ophys/Backgrounds_0/max_proj (GrayscaleImage)  | shape = (512, 512) | dtype = float32
  Dataset /processing/ophys/Backgrounds_0/meanImg (GrayscaleImage)  | shape = (512, 512) | dtype = float32
  Group /processing/ophys/Deconvolved (Fluorescence) 
  Group /processing/ophys/Deconvolved/plane0 (RoiResponseSeries) no description
  Dataset /processing/ophys/Deconvolved/plane0/rois (DynamicTableRegion) ROIs for plane0 | shape = (69,) | dtype = int32
  Group /processing/ophys/Fluorescence (Fluorescence) 
  Group /processing/ophys/Fluorescence/plane0 (RoiResponseSeries) no description
  Dataset /processing/ophys/Fluorescence/plane0/rois (DynamicTableRegion) ROIs for plane0 | shape = (69,) | dtype = int32
  Group /processing/ophys/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation (PlaneSegmentation) suite2p output
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/id (ElementIdentifiers)  | shape = (69,) | dtype = int32
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/Ch0 (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/device (Device) OSU Haesemeyer Lab, 2-Photon 1
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/iscell (VectorData) two columns - iscell & probcell | shape = (69, 2) | dtype = float64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/pixel_mask (VectorData) Pixel masks for each ROI | shape = (13347,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (69,) | dtype = uint16
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/reference_images/240514_Fish42_GCaMP_vglut_TG_5dpf_FlowExperiment_warner_temp_stim_Z_2_0.tif (TwoPhotonSeries) Raw acquisition photon counts
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/reference_images/240514_Fish42_GCaMP_vglut_TG_5dpf_FlowExperiment_warner_temp_stim_Z_2_0.tif/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/reference_images/240514_Fish42_GCaMP_vglut_TG_5dpf_FlowExperiment_warner_temp_stim_Z_2_0.tif/imaging_plane/Ch0 (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/reference_images/240514_Fish42_GCaMP_vglut_TG_5dpf_FlowExperiment_warner_temp_stim_Z_2_0.tif/imaging_plane/device (Device) OSU Haesemeyer Lab, 2-Photon 1
  Group /processing/ophys/Neuropil (Fluorescence) 
  Group /processing/ophys/Neuropil/plane0 (RoiResponseSeries) no description
  Dataset /processing/ophys/Neuropil/plane0/rois (DynamicTableRegion) ROIs for plane0 | shape = (69,) | dtype = int32
  session_description: suite2p_proc
  session_start_time: 2025-02-04T15:46:26.699669-05:00
  Group /stimulus/presentation/240514_Fish42_GCaMP_vglut_TG_5dpf_FlowExperiment_warner_temp_stim_Z_2_0 (TimeSeries) Temperature stimulus
  timestamps_reference_time: 2025-02-04T15:46:26.699669-05:00


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/240514_Fish42_GCaMP_vglut_TG_5dpf_FlowExperiment_warner_temp_stim_Z_3_0.tif (TwoPhotonSeries) Raw acquisition photon counts
  Group /acquisition/240514_Fish42_GCaMP_vglut_TG_5dpf_FlowExperiment_warner_temp_stim_Z_3_0.tif/imaging_plane (ImagingPlane) 
  Group /acquisition/240514_Fish42_GCaMP_vglut_TG_5dpf_FlowExperiment_warner_temp_stim_Z_3_0.tif/imaging_plane/Ch0 (OpticalChannel) 
  Group /acquisition/240514_Fish42_GCaMP_vglut_TG_5dpf_FlowExperiment_warner_temp_stim_Z_3_0.tif/imaging_plane/device (Device) OSU Haesemeyer Lab, 2-Photon 1
  file_create_date: ['2025-02-19T17:59:08.665438-05:00']
  Group /general/devices/OSU_2P_1 (Device) OSU Haesemeyer Lab, 2-Photon 1
  Group /general/optophysiology/ImagingPlane (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane/Ch0 (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane/device (Device) OSU Haesemeyer Lab, 2-Photon 1
  Group /general/subject (Subject) 
  identifier: D:/HaesemeyerLab/Two Photon/NewTG_Experiments/240514\240514_Fish42_GCaMP_vglut_TG_5dpf_FlowExperiment_warner_temp_stim_Z_3_0
  Group /processing/ophys (ProcessingModule) optical physiology processed data
  Group /processing/ophys/Backgrounds_0 (Images) no description
  Dataset /processing/ophys/Backgrounds_0/Vcorr (GrayscaleImage)  | shape = (512, 512) | dtype = float32
  Dataset /processing/ophys/Backgrounds_0/max_proj (GrayscaleImage)  | shape = (512, 512) | dtype = float32
  Dataset /processing/ophys/Backgrounds_0/meanImg (GrayscaleImage)  | shape = (512, 512) | dtype = float32
  Group /processing/ophys/Deconvolved (Fluorescence) 
  Group /processing/ophys/Deconvolved/plane0 (RoiResponseSeries) no description
  Dataset /processing/ophys/Deconvolved/plane0/rois (DynamicTableRegion) ROIs for plane0 | shape = (58,) | dtype = int32
  Group /processing/ophys/Fluorescence (Fluorescence) 
  Group /processing/ophys/Fluorescence/plane0 (RoiResponseSeries) no description
  Dataset /processing/ophys/Fluorescence/plane0/rois (DynamicTableRegion) ROIs for plane0 | shape = (58,) | dtype = int32
  Group /processing/ophys/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation (PlaneSegmentation) suite2p output
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/id (ElementIdentifiers)  | shape = (58,) | dtype = int32
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/Ch0 (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/device (Device) OSU Haesemeyer Lab, 2-Photon 1
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/iscell (VectorData) two columns - iscell & probcell | shape = (58, 2) | dtype = float64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/pixel_mask (VectorData) Pixel masks for each ROI | shape = (9792,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (58,) | dtype = uint16
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/reference_images/240514_Fish42_GCaMP_vglut_TG_5dpf_FlowExperiment_warner_temp_stim_Z_3_0.tif (TwoPhotonSeries) Raw acquisition photon counts
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/reference_images/240514_Fish42_GCaMP_vglut_TG_5dpf_FlowExperiment_warner_temp_stim_Z_3_0.tif/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/reference_images/240514_Fish42_GCaMP_vglut_TG_5dpf_FlowExperiment_warner_temp_stim_Z_3_0.tif/imaging_plane/Ch0 (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/reference_images/240514_Fish42_GCaMP_vglut_TG_5dpf_FlowExperiment_warner_temp_stim_Z_3_0.tif/imaging_plane/device (Device) OSU Haesemeyer Lab, 2-Photon 1
  Group /processing/ophys/Neuropil (Fluorescence) 
  Group /processing/ophys/Neuropil/plane0 (RoiResponseSeries) no description
  Dataset /processing/ophys/Neuropil/plane0/rois (DynamicTableRegion) ROIs for plane0 | shape = (58,) | dtype = int32
  session_description: suite2p_proc
  session_start_time: 2025-02-04T15:54:16.811702-05:00
  Group /stimulus/presentation/240514_Fish42_GCaMP_vglut_TG_5dpf_FlowExperiment_warner_temp_stim_Z_3_0 (TimeSeries) Temperature stimulus
  timestamps_reference_time: 2025-02-04T15:54:16.811702-05:00


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  Group /acquisition/240514_Fish42_GCaMP_vglut_TG_5dpf_FlowExperiment_warner_temp_stim_Z_4_0.tif (TwoPhotonSeries) Raw acquisition photon counts
  Group /acquisition/240514_Fish42_GCaMP_vglut_TG_5dpf_FlowExperiment_warner_temp_stim_Z_4_0.tif/imaging_plane (ImagingPlane) 
  Group /acquisition/240514_Fish42_GCaMP_vglut_TG_5dpf_FlowExperiment_warner_temp_stim_Z_4_0.tif/imaging_plane/Ch0 (OpticalChannel) 
  Group /acquisition/240514_Fish42_GCaMP_vglut_TG_5dpf_FlowExperiment_warner_temp_stim_Z_4_0.tif/imaging_plane/device (Device) OSU Haesemeyer Lab, 2-Photon 1
  file_create_date: ['2025-02-19T17:59:19.150552-05:00']
  Group /general/devices/OSU_2P_1 (Device) OSU Haesemeyer Lab, 2-Photon 1
  Group /general/optophysiology/ImagingPlane (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane/Ch0 (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane/device (Device) OSU Haesemeyer Lab, 2-Photon 1
  Group /general/subject (Subject) 
  identifier: D:/HaesemeyerLab/Two Photon/NewTG_Experiments/240514\240514_Fish42_GCaMP_vglut_TG_5dpf_FlowExperiment_warner_temp_stim_Z_4_0
  Group /processing/ophys (ProcessingModule) optical physiology processed data
  Group /processing/ophys/Backgrounds_0 (Images) no description
  Dataset /processing/ophys/Backgrounds_0/Vcorr (GrayscaleImage)  | shape = (512, 512) | dtype = float32
  Dataset /processing/ophys/Backgrounds_0/max_proj (GrayscaleImage)  | shape = (512, 512) | dtype = float32
  Dataset /processing/ophys/Backgrounds_0/meanImg (GrayscaleImage)  | shape = (512, 512) | dtype = float32
  Group /processing/ophys/Deconvolved (Fluorescence) 
  Group /processing/ophys/Deconvolved/plane0 (RoiResponseSeries) no description
  Dataset /processing/ophys/Deconvolved/plane0/rois (DynamicTableRegion) ROIs for plane0 | shape = (60,) | dtype = int32
  Group /processing/ophys/Fluorescence (Fluorescence) 
  Group /processing/ophys/Fluorescence/plane0 (RoiResponseSeries) no description
  Dataset /processing/ophys/Fluorescence/plane0/rois (DynamicTableRegion) ROIs for plane0 | shape = (60,) | dtype = int32
  Group /processing/ophys/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation (PlaneSegmentation) suite2p output
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/id (ElementIdentifiers)  | shape = (60,) | dtype = int32
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/Ch0 (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/device (Device) OSU Haesemeyer Lab, 2-Photon 1
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/iscell (VectorData) two columns - iscell & probcell | shape = (60, 2) | dtype = float64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/pixel_mask (VectorData) Pixel masks for each ROI | shape = (9238,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (60,) | dtype = uint16
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/reference_images/240514_Fish42_GCaMP_vglut_TG_5dpf_FlowExperiment_warner_temp_stim_Z_4_0.tif (TwoPhotonSeries) Raw acquisition photon counts
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/reference_images/240514_Fish42_GCaMP_vglut_TG_5dpf_FlowExperiment_warner_temp_stim_Z_4_0.tif/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/reference_images/240514_Fish42_GCaMP_vglut_TG_5dpf_FlowExperiment_warner_temp_stim_Z_4_0.tif/imaging_plane/Ch0 (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/reference_images/240514_Fish42_GCaMP_vglut_TG_5dpf_FlowExperiment_warner_temp_stim_Z_4_0.tif/imaging_plane/device (Device) OSU Haesemeyer Lab, 2-Photon 1
  Group /processing/ophys/Neuropil (Fluorescence) 
  Group /processing/ophys/Neuropil/plane0 (RoiResponseSeries) no description
  Dataset /processing/ophys/Neuropil/plane0/rois (DynamicTableRegion) ROIs for plane0 | shape = (60,) | dtype = int32
  session_description: suite2p_proc
  session_start_time: 2025-02-04T15:58:20.893263-05:00
  Group /stimulus/presentation/240514_Fish42_GCaMP_vglut_TG_5dpf_FlowExperiment_warner_temp_stim_Z_4_0 (TimeSeries) Temperature stimulus
  timestamps_reference_time: 2025-02-04T15:58:20.893263-05:00
