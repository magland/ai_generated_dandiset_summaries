
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000144/draft
name: croat-test
contributor: [{'name': 'Roat, Chris', 'email': 'chris.roat@gmail.com', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}]
description: Testing
assetsSummary: {'species': [], 'approach': [{'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 589064856, 'numberOfFiles': 2, 'numberOfSubjects': 1, 'variableMeasured': ['PlaneSegmentation', 'ProcessingModule', 'TwoPhotonSeries'], 'measurementTechnique': [{'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'two-photon microscopy technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000144 has 2 NWB files.
1 of these NWB files are of type 1.
1 of these NWB files are of type 2.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/MySeries (TwoPhotonSeries) no description
  Group /acquisition/MySeries/imaging_plane (ImagingPlane) 
  Group /acquisition/MySeries/imaging_plane/OpticalChannel (OpticalChannel) 
  Group /acquisition/MySeries/imaging_plane/device (Device) My two-photon microscope
  file_create_date: ['2021-10-08T16:35:17.340183-07:00']
  Group /general/devices/Microscope (Device) My two-photon microscope
  experiment_description: Test of dandi upload.
  experimenter: ['bilbo']
  institution: Stanford University
  lab: Deisseroth
  Group /general/optophysiology/ImagingPlane (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane/OpticalChannel (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane/device (Device) My two-photon microscope
  session_id: 2000-01-01 00:00:00
  Group /general/subject (Subject) 
  identifier: foo-bar
  session_description: my first synthetic recording
  session_start_time: 2021-10-08T16:35:17.340033-07:00
  timestamps_reference_time: 2021-10-08T16:35:17.340033-07:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/TwoPhotonSeries (TwoPhotonSeries) no description
  Group /acquisition/TwoPhotonSeries/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeries/imaging_plane/OpticalChannel (OpticalChannel) 
  Group /acquisition/TwoPhotonSeries/imaging_plane/device (Device) My two-photon microscope
  file_create_date: ['2021-10-08T16:36:58.729459-07:00']
  Group /general/devices/Microscope (Device) My two-photon microscope
  Group /general/optophysiology/ImagingPlane (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane/OpticalChannel (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane/device (Device) My two-photon microscope
  Group /general/subject (Subject) 
  identifier: W
  Group /processing/ophys (ProcessingModule) optical physiology processed data
  Group /processing/ophys/Backgrounds_0 (Images) no description
  Dataset /processing/ophys/Backgrounds_0/Vcorr (GrayscaleImage)  | shape = (512, 512) | dtype = float32
  Dataset /processing/ophys/Backgrounds_0/max_proj (GrayscaleImage)  | shape = (512, 512) | dtype = float32
  Dataset /processing/ophys/Backgrounds_0/meanImg (GrayscaleImage)  | shape = (512, 512) | dtype = float64
  Group /processing/ophys/Deconvolved (Fluorescence) 
  Group /processing/ophys/Deconvolved/Deconvolved (RoiResponseSeries) no description
  Dataset /processing/ophys/Deconvolved/Deconvolved/rois (DynamicTableRegion) all ROIs | shape = (4954,) | dtype = int64
  Group /processing/ophys/Fluorescence (Fluorescence) 
  Group /processing/ophys/Fluorescence/Fluorescence (RoiResponseSeries) no description
  Dataset /processing/ophys/Fluorescence/Fluorescence/rois (DynamicTableRegion) all ROIs | shape = (4954,) | dtype = int64
  Group /processing/ophys/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation (PlaneSegmentation) suite2p output
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/id (ElementIdentifiers)  | shape = (4954,) | dtype = int64
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/OpticalChannel (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/device (Device) My two-photon microscope
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/iscell (VectorData) two columns - iscell & probcell | shape = (4954, 2) | dtype = float64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/pixel_mask (VectorData) Pixel masks for each ROI | shape = (46691,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (4954,) | dtype = uint16
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/reference_images/TwoPhotonSeries (TwoPhotonSeries) no description
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/reference_images/TwoPhotonSeries/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/reference_images/TwoPhotonSeries/imaging_plane/OpticalChannel (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/reference_images/TwoPhotonSeries/imaging_plane/device (Device) My two-photon microscope
  Group /processing/ophys/Neuropil (Fluorescence) 
  Group /processing/ophys/Neuropil/Neuropil (RoiResponseSeries) no description
  Dataset /processing/ophys/Neuropil/Neuropil/rois (DynamicTableRegion) all ROIs | shape = (4954,) | dtype = int64
  session_description: suite2p_proc
  session_start_time: 2021-10-08T16:35:43.593880-07:00
  timestamps_reference_time: 2021-10-08T16:35:43.593880-07:00
