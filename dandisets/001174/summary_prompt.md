
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001174/draft
name: Calcium imaging in SMA and M1 of macaques
contributor: [{'name': 'Galvan, Adriana', 'email': 'agalvan@emory.edu', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}]
description: This dataset contains data used in Martel et al "MICROENDOSCOPIC CALCIUM IMAGING IN SUPPLEMENTARY MOTOR AREA AND PRIMARY MOTOR CORTEX OF RHESUS MACAQUES AT REST AND DURING ARM MOVEMENT"
assetsSummary: {'species': [{'name': 'Macaca mulatta - Rhesus monkey', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9544'}], 'approach': [{'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 60755797884, 'numberOfFiles': 67, 'numberOfSubjects': 4, 'variableMeasured': ['ImagingPlane', 'OpticalChannel', 'ProcessingModule', 'PlaneSegmentation'], 'measurementTechnique': [{'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 001174 has 68 NWB files.
4 of these NWB files are of type 1.
64 of these NWB files are of type 2.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/OnePhotonSeries (OnePhotonSeries) Miniscope imaging data
  Group /acquisition/OnePhotonSeries/imaging_plane (ImagingPlane) 
  Group /acquisition/OnePhotonSeries/imaging_plane/OpticalChannel (OpticalChannel) 
  Group /acquisition/OnePhotonSeries/imaging_plane/device (Device) NVista3
  file_create_date: ['2024-09-05T18:26:06.311163+00:00']
  Group /general/devices/Miniscope (Device) NVista3
  Group /general/optophysiology/ImagingPlane (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane/OpticalChannel (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane/device (Device) NVista3
  Group /general/subject (Subject) 
  identifier: a8487157-9506-4087-837a-05f16a6967bb
  Group /processing/ophys (ProcessingModule) Optical physiology data obtained by processing raw calcium imaging data
  Group /processing/ophys/Fluorescence (Fluorescence) 
  Group /processing/ophys/Fluorescence/RoiResponseSeries (RoiResponseSeries) Fluorescence data associated with spatial footprints
  Dataset /processing/ophys/Fluorescence/RoiResponseSeries/rois (DynamicTableRegion) ROIs | shape = (11,) | dtype = int64
  Group /processing/ophys/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation (PlaneSegmentation) Footprints of individual cells obtained by segmenting the field of view
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/id (ElementIdentifiers)  | shape = (11,) | dtype = int64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (11, 318, 197) | dtype = float32
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/OpticalChannel (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/device (Device) NVista3
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/reference_images/OnePhotonSeries (OnePhotonSeries) Miniscope imaging data
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/reference_images/OnePhotonSeries/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/reference_images/OnePhotonSeries/imaging_plane/OpticalChannel (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/reference_images/OnePhotonSeries/imaging_plane/device (Device) NVista3
  session_description: M1 Spontaneous 
  session_start_time: 2023-03-09T10:45:56.856000+00:00
  timestamps_reference_time: 2023-03-09T10:45:56.856000+00:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2024-09-03T16:27:11.930494+00:00']
  Group /general/devices/Miniscope (Device) NVista3
  Group /general/optophysiology/ImagingPlane (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane/OpticalChannel (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane/device (Device) NVista3
  Group /general/subject (Subject) 
  identifier: d167ac86-a29c-4e65-a291-781cac5eba6e
  Group /processing/ophys (ProcessingModule) Optical physiology data obtained by processing raw calcium imaging data
  Group /processing/ophys/Fluorescence (Fluorescence) 
  Group /processing/ophys/Fluorescence/RoiResponseSeries (RoiResponseSeries) Fluorescence data associated with spatial footprints
  Dataset /processing/ophys/Fluorescence/RoiResponseSeries/rois (DynamicTableRegion) ROIs | shape = (6,) | dtype = int64
  Group /processing/ophys/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation (PlaneSegmentation) Footprints of individual cells obtained by segmenting the field of view
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/id (ElementIdentifiers)  | shape = (6,) | dtype = int64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (6, 318, 198) | dtype = float32
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/OpticalChannel (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/device (Device) NVista3
  session_description: Spontaneous OASIS
  session_start_time: 2024-02-13T11:04:30.267000+00:00
  timestamps_reference_time: 2024-02-13T11:04:30.267000+00:00
