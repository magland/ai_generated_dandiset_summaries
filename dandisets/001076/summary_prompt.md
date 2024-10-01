
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001076/draft
name: OMR Robot CaImaging
contributor: [{'name': 'Loring, Matthew', 'email': 'matthew.loring@duke.edu', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}]
description: Recorded calcium imaging data associated with the following manuscript: Embodied Neural Visuomotor Circuits in Neuromechanical Simulations and a Zebrafish Robot 
assetsSummary: {'species': [{'name': 'Danio rerio - Zebra fish', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_7955'}], 'approach': [{'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 624332749, 'numberOfFiles': 44, 'numberOfSubjects': 1, 'variableMeasured': ['ProcessingModule', 'PlaneSegmentation', 'OpticalChannel', 'ImagingPlane'], 'measurementTechnique': [{'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 001076 has 48 NWB files.
48 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2024-06-27T10:14:47.882866-04:00']
  Group /general/devices/Microscope (Device) 
  Group /general/optophysiology/ImagingPlane (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane/OpticalChannel (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane/device (Device) 
  Group /general/subject (Subject) 
  identifier: 6a2a0909-3049-45d5-ba2c-dfccfee6da82
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (100,) | dtype = int32
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (100,) | dtype = float64
  Dataset /intervals/trials/stim (VectorData) the visual stimuli during the trial | shape = (100,) | dtype = object
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (100,) | dtype = float64
  Group /processing/ophys (ProcessingModule) No description.
  Group /processing/ophys/Fluorescence (Fluorescence) 
  Group /processing/ophys/Fluorescence/Deconvolved (RoiResponseSeries) description of deconvolved traces
  Dataset /processing/ophys/Fluorescence/Deconvolved/rois (DynamicTableRegion) The ROIs for ImagingPlane. | shape = (968,) | dtype = int32
  Group /processing/ophys/Fluorescence/Neuropil (RoiResponseSeries) description of neuropil traces
  Dataset /processing/ophys/Fluorescence/Neuropil/rois (DynamicTableRegion) The ROIs for ImagingPlane. | shape = (968,) | dtype = int32
  Group /processing/ophys/Fluorescence/RoiResponseSeries (RoiResponseSeries) Array of raw fluorescence traces.
  Dataset /processing/ophys/Fluorescence/RoiResponseSeries/rois (DynamicTableRegion) The ROIs for ImagingPlane. | shape = (968,) | dtype = int32
  Group /processing/ophys/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation (PlaneSegmentation) Segmented ROIs
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/Accepted (VectorData) 1 if ROI was accepted or 0 if rejected as a cell during segmentation operation. | shape = (968,) | dtype = int32
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/ROICentroids (VectorData) The x, y, (z) centroids of each ROI. | shape = (968, 2) | dtype = int32
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/Rejected (VectorData) 1 if ROI was rejected or 0 if accepted as a cell during segmentation operation. | shape = (968,) | dtype = int32
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/id (ElementIdentifiers)  | shape = (968,) | dtype = int32
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/image_mask (VectorData) Image masks for each ROI. | shape = (968, 270, 292) | dtype = float64
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/OpticalChannel (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/device (Device) 
  Group /processing/ophys/SegmentationImages (Images) The summary images of the segmentation.
  Dataset /processing/ophys/SegmentationImages/correlation (GrayscaleImage) The correlation image. | shape = (270, 292) | dtype = float64
  Dataset /processing/ophys/SegmentationImages/mean (GrayscaleImage)  | shape = (270, 292) | dtype = float64
  session_description: no description
  session_start_time: 2023-01-23T19:00:57.808286-05:00
  timestamps_reference_time: 2023-01-23T19:00:57.808286-05:00
