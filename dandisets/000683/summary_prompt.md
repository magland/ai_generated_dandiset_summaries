
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000683/draft
name: Element Calcium Imaging Data Upload
contributor: [{'name': 'Bakshi, Kushal', 'email': 'kushal.bakshi@datajoint.com', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}]
description: Direct upload of data from DataJoint's calcium imaging pipeline (element-calcium-imaging)
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 31732204, 'numberOfFiles': 1, 'numberOfSubjects': 1, 'variableMeasured': ['PlaneSegmentation', 'OpticalChannel', 'ProcessingModule', 'ImagingPlane'], 'measurementTechnique': [{'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000683 has 1 NWB files.
1 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2023-10-11T14:19:16.612221-05:00']
  Group /general/devices/ScannerA (Device) Two photon microscope
  Group /general/optophysiology/ImagingPlane1 (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane1/OpticalChannel1 (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane1/device (Device) Two photon microscope
  session_id: subject1_0
  Group /general/subject (Subject) 
  identifier: ba3d9b83-db23-4d4b-9ef8-9ec588b1f6f3
  Group /processing/ophys (ProcessingModule) optical physiology processed data
  Group /processing/ophys/Fluorescence (Fluorescence) 
  Group /processing/ophys/Fluorescence/Fluorescence_0 (RoiResponseSeries) no description
  Dataset /processing/ophys/Fluorescence/Fluorescence_0/rois (DynamicTableRegion) All ROIs from database. | shape = (1276,) | dtype = int32
  Group /processing/ophys/Fluorescence/Neuropil_0 (RoiResponseSeries) no description
  Dataset /processing/ophys/Fluorescence/Neuropil_0/rois (DynamicTableRegion) All ROIs from database. | shape = (1276,) | dtype = int32
  Group /processing/ophys/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation (PlaneSegmentation) output from segmenting
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/id (ElementIdentifiers)  | shape = (1276,) | dtype = int32
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/OpticalChannel1 (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/device (Device) Two photon microscope
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/pixel_mask (VectorData) Pixel masks for each ROI | shape = (73701,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1276,) | dtype = uint32
  session_description: Test DataJoint session.
  session_start_time: 2023-09-06T05:00:00+00:00
  timestamps_reference_time: 2023-09-06T05:00:00+00:00
