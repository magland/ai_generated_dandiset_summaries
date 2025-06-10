
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001413/draft
name: Calcium imaging of motor cortex during arm reaching tasks
contributor: [{'name': 'Galvan, Adriana', 'email': 'agalvan@emory.edu', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}]
description: This dandiset includes calcium imaging data of cortical neurons (SMA & M1) recorded in macaque monkeys during simple arm reaching task performance. 
assetsSummary: {'species': [], 'approach': [], 'schemaKey': 'AssetsSummary', 'dataStandard': [], 'numberOfBytes': 864909510, 'numberOfFiles': 1, 'variableMeasured': [], 'measurementTechnique': []}

Dandiset 001413 has 1 NWB files.
1 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/OnePhotonSeries (OnePhotonSeries) Miniscope imaging data
  Group /acquisition/OnePhotonSeries/imaging_plane (ImagingPlane) 
  Group /acquisition/OnePhotonSeries/imaging_plane/OpticalChannel (OpticalChannel) 
  Group /acquisition/OnePhotonSeries/imaging_plane/device (Device) NVista3
  file_create_date: ['2025-04-14T19:40:22.327883+00:00']
  Group /general/devices/Miniscope (Device) NVista3
  Group /general/optophysiology/ImagingPlane (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane/OpticalChannel (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane/device (Device) NVista3
  Group /general/subject (Subject) 
  identifier: 97b8b793-0cd9-4d05-a836-80a2dd6ee1ec
  Group /processing/ophys (ProcessingModule) Optical physiology data obtained by processing raw calcium imaging data
  Group /processing/ophys/EventAmplitude (RoiResponseSeries) Amplitude of neural events associated with spatial footprints
  Dataset /processing/ophys/EventAmplitude/rois (DynamicTableRegion) ROIs | shape = (14,) | dtype = int64
  Group /processing/ophys/Fluorescence (Fluorescence) 
  Group /processing/ophys/Fluorescence/RoiResponseSeries (RoiResponseSeries) Fluorescence data associated with spatial footprints
  Dataset /processing/ophys/Fluorescence/RoiResponseSeries/rois (DynamicTableRegion) ROIs | shape = (14,) | dtype = int64
  Group /processing/ophys/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation (PlaneSegmentation) Footprints of individual cells obtained by segmenting the field of view
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/id (ElementIdentifiers)  | shape = (14,) | dtype = int64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (14, 318, 198) | dtype = float32
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/OpticalChannel (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/device (Device) NVista3
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/reference_images/OnePhotonSeries (OnePhotonSeries) Miniscope imaging data
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/reference_images/OnePhotonSeries/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/reference_images/OnePhotonSeries/imaging_plane/OpticalChannel (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/reference_images/OnePhotonSeries/imaging_plane/device (Device) NVista3
  session_description: Calcium imaging in SMA during the arm reaching condition
  session_start_time: 2023-03-28T11:18:37.534000+00:00
  timestamps_reference_time: 2023-03-28T11:18:37.534000+00:00
