
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000167/0.230720.2001
name: Two photon calcium imaging of mice piriform cortex under passive odor presentation
contributor: [{'name': 'Daste, Simon', 'email': 'simon_daste@brown.edu', 'roleName': ['dcite:Author', 'dcite:DataCollector', 'dcite:Researcher', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0001-5139-2743', 'affiliation': [], 'includeInCitation': True}, {'name': 'Pierré, Andrea', 'email': 'andrea_pierre@brown.edu', 'roleName': ['dcite:Software', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0003-4501-5428', 'affiliation': [], 'includeInCitation': True}, {'name': 'Pham, Tuan', 'email': 'tuanhpham@brown.edu', 'roleName': ['dcite:ContactPerson', 'dcite:Software'], 'schemaKey': 'Person', 'identifier': '0000-0001-6891-3760', 'affiliation': [], 'includeInCitation': True}]
description: Two-photon calcium imaging of mouse piriform cortex pyramidal population, under head-fixed condition and passive odor stimulus delivery. There were 10 different odors used (8 trials each), delivered at 10-second for each of the 30-second trial. Imaging was preprocessed with Suite2p. The data was collected by Simon Daste in the Fleischmann lab at Brown University. Showcase notebook available at: https://gitlab.com/fleischmann-lab/datasets/daste-odor-set-2021-11
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 1218408045, 'numberOfFiles': 6, 'numberOfSubjects': 5, 'variableMeasured': ['PlaneSegmentation', 'ProcessingModule', 'ImagingPlane', 'OpticalChannel'], 'measurementTechnique': [{'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000167 has 5 NWB files.
4 of these NWB files are of type 1.
1 of these NWB files are of type 2.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/flow (TimeSeries) no description
  Group /acquisition/wheel (TimeSeries) no description
  file_create_date: ['2023-06-21T17:11:01.133785-04:00']
  Group /general/devices/Microscope (Device) Ultima Investigator
  experiment_description: Two-photon calcium imaging of mouse piriform cortex pyramidal neurons, under head-fixed condition and passive odor stimulus delivery.
  
  There were 10 different odors used (8 trials each), delivered at 10-second for each of the 30-second trial.
  
  Note: we recorded the `wheel` position data in `acquisition`, however the unit was actually not `radian`. This was not inspected for quality. Please ignore the `flow` data in `acquisition`.
  
  experimenter: ['Daste, Simon']
  institution: Brown University
  lab: Fleischmann Lab
  Group /general/optophysiology/ImagingPlane (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane/OpticalChannel (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane/device (Device) Ultima Investigator
  Group /general/subject (Subject) 
  identifier: f566aeaf1dd71f1e1f1c5475343adc47
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (80,) | dtype = int64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (80,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (80,) | dtype = float64
  Group /processing/ophys (ProcessingModule) optical physiology processed data from suite2p
  Group /processing/ophys/Backgrounds_0 (Images) no description
  Dataset /processing/ophys/Backgrounds_0/Vcorr (GrayscaleImage)  | shape = (512, 512) | dtype = float32
  Dataset /processing/ophys/Backgrounds_0/max_proj (GrayscaleImage)  | shape = (512, 512) | dtype = float32
  Dataset /processing/ophys/Backgrounds_0/meanImg (GrayscaleImage)  | shape = (512, 512) | dtype = float64
  Group /processing/ophys/Backgrounds_1 (Images) no description
  Dataset /processing/ophys/Backgrounds_1/Vcorr (GrayscaleImage)  | shape = (512, 512) | dtype = float32
  Dataset /processing/ophys/Backgrounds_1/max_proj (GrayscaleImage)  | shape = (512, 512) | dtype = float32
  Dataset /processing/ophys/Backgrounds_1/meanImg (GrayscaleImage)  | shape = (512, 512) | dtype = float64
  Group /processing/ophys/Backgrounds_2 (Images) no description
  Dataset /processing/ophys/Backgrounds_2/Vcorr (GrayscaleImage)  | shape = (512, 512) | dtype = float32
  Dataset /processing/ophys/Backgrounds_2/max_proj (GrayscaleImage)  | shape = (512, 512) | dtype = float32
  Dataset /processing/ophys/Backgrounds_2/meanImg (GrayscaleImage)  | shape = (512, 512) | dtype = float64
  Group /processing/ophys/Deconvolved (Fluorescence) 
  Group /processing/ophys/Deconvolved/Plane_0 (RoiResponseSeries) no description
  Dataset /processing/ophys/Deconvolved/Plane_0/rois (DynamicTableRegion) ROIs for plane_0 | shape = (273,) | dtype = int64
  Group /processing/ophys/Deconvolved/Plane_1 (RoiResponseSeries) no description
  Dataset /processing/ophys/Deconvolved/Plane_1/rois (DynamicTableRegion) ROIs for plane_1 | shape = (314,) | dtype = int64
  Group /processing/ophys/Deconvolved/Plane_2 (RoiResponseSeries) no description
  Dataset /processing/ophys/Deconvolved/Plane_2/rois (DynamicTableRegion) ROIs for plane_2 | shape = (286,) | dtype = int64
  Group /processing/ophys/Fluorescence (Fluorescence) 
  Group /processing/ophys/Fluorescence/Plane_0 (RoiResponseSeries) no description
  Dataset /processing/ophys/Fluorescence/Plane_0/rois (DynamicTableRegion) ROIs for plane_0 | shape = (273,) | dtype = int64
  Group /processing/ophys/Fluorescence/Plane_1 (RoiResponseSeries) no description
  Dataset /processing/ophys/Fluorescence/Plane_1/rois (DynamicTableRegion) ROIs for plane_1 | shape = (314,) | dtype = int64
  Group /processing/ophys/Fluorescence/Plane_2 (RoiResponseSeries) no description
  Dataset /processing/ophys/Fluorescence/Plane_2/rois (DynamicTableRegion) ROIs for plane_2 | shape = (286,) | dtype = int64
  Group /processing/ophys/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation (PlaneSegmentation) suite2p output
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/id (ElementIdentifiers)  | shape = (873,) | dtype = int64
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/OpticalChannel (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/device (Device) Ultima Investigator
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/iscell (VectorData) two columns - iscell & probcell | shape = (873, 2) | dtype = float64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/voxel_mask (VectorData) Voxel masks for each ROI | shape = (363969,) | dtype = [('x', '<u4'), ('y', '<u4'), ('z', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/voxel_mask_index (VectorIndex) Index for VectorData 'voxel_mask' | shape = (873,) | dtype = uint32
  Group /processing/ophys/Neuropil (Fluorescence) 
  Group /processing/ophys/Neuropil/Plane_0 (RoiResponseSeries) no description
  Dataset /processing/ophys/Neuropil/Plane_0/rois (DynamicTableRegion) ROIs for plane_0 | shape = (273,) | dtype = int64
  Group /processing/ophys/Neuropil/Plane_1 (RoiResponseSeries) no description
  Dataset /processing/ophys/Neuropil/Plane_1/rois (DynamicTableRegion) ROIs for plane_1 | shape = (314,) | dtype = int64
  Group /processing/ophys/Neuropil/Plane_2 (RoiResponseSeries) no description
  Dataset /processing/ophys/Neuropil/Plane_2/rois (DynamicTableRegion) ROIs for plane_2 | shape = (286,) | dtype = int64
  session_description: 2P-PCx-passive-odor
  session_start_time: 2020-02-12T16:06:55.893024-05:00
  Group /stimulus/presentation/odor (TimeSeries) no description
  timestamps_reference_time: 2020-02-12T16:06:55.893024-05:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ExternalVideoFiles (ImageSeries) Demo video of registration motion corrected
  Group /acquisition/flow (TimeSeries) no description
  Group /acquisition/wheel (TimeSeries) no description
  file_create_date: ['2023-06-24T23:16:57.648943-04:00']
  Group /general/devices/Microscope (Device) Ultima Investigator
  experiment_description: Two-photon calcium imaging of mouse piriform cortex pyramidal neurons, under head-fixed condition and passive odor stimulus delivery.
  
  There were 10 different odors used (8 trials each), delivered at 10-second for each of the 30-second trial.
  
  Note: we recorded the `wheel` position data in `acquisition`, however the unit was actually not `radian`. This was not inspected for quality. Please ignore the `flow` data in `acquisition`.
  
  experimenter: ['Daste, Simon']
  institution: Brown University
  lab: Fleischmann Lab
  Group /general/optophysiology/ImagingPlane (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane/OpticalChannel (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane/device (Device) Ultima Investigator
  Group /general/subject (Subject) 
  identifier: f7eea1853100375e7ac926bd0709865d
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (80,) | dtype = int64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (80,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (80,) | dtype = float64
  Group /processing/ophys (ProcessingModule) optical physiology processed data from suite2p
  Group /processing/ophys/Backgrounds_0 (Images) no description
  Dataset /processing/ophys/Backgrounds_0/Vcorr (GrayscaleImage)  | shape = (512, 512) | dtype = float32
  Dataset /processing/ophys/Backgrounds_0/max_proj (GrayscaleImage)  | shape = (512, 512) | dtype = float32
  Dataset /processing/ophys/Backgrounds_0/meanImg (GrayscaleImage)  | shape = (512, 512) | dtype = float64
  Group /processing/ophys/Backgrounds_1 (Images) no description
  Dataset /processing/ophys/Backgrounds_1/Vcorr (GrayscaleImage)  | shape = (512, 512) | dtype = float32
  Dataset /processing/ophys/Backgrounds_1/max_proj (GrayscaleImage)  | shape = (512, 512) | dtype = float32
  Dataset /processing/ophys/Backgrounds_1/meanImg (GrayscaleImage)  | shape = (512, 512) | dtype = float64
  Group /processing/ophys/Backgrounds_2 (Images) no description
  Dataset /processing/ophys/Backgrounds_2/Vcorr (GrayscaleImage)  | shape = (512, 512) | dtype = float32
  Dataset /processing/ophys/Backgrounds_2/max_proj (GrayscaleImage)  | shape = (512, 512) | dtype = float32
  Dataset /processing/ophys/Backgrounds_2/meanImg (GrayscaleImage)  | shape = (512, 512) | dtype = float64
  Group /processing/ophys/Deconvolved (Fluorescence) 
  Group /processing/ophys/Deconvolved/Plane_0 (RoiResponseSeries) no description
  Dataset /processing/ophys/Deconvolved/Plane_0/rois (DynamicTableRegion) ROIs for plane_0 | shape = (96,) | dtype = int64
  Group /processing/ophys/Deconvolved/Plane_1 (RoiResponseSeries) no description
  Dataset /processing/ophys/Deconvolved/Plane_1/rois (DynamicTableRegion) ROIs for plane_1 | shape = (232,) | dtype = int64
  Group /processing/ophys/Deconvolved/Plane_2 (RoiResponseSeries) no description
  Dataset /processing/ophys/Deconvolved/Plane_2/rois (DynamicTableRegion) ROIs for plane_2 | shape = (203,) | dtype = int64
  Group /processing/ophys/Fluorescence (Fluorescence) 
  Group /processing/ophys/Fluorescence/Plane_0 (RoiResponseSeries) no description
  Dataset /processing/ophys/Fluorescence/Plane_0/rois (DynamicTableRegion) ROIs for plane_0 | shape = (96,) | dtype = int64
  Group /processing/ophys/Fluorescence/Plane_1 (RoiResponseSeries) no description
  Dataset /processing/ophys/Fluorescence/Plane_1/rois (DynamicTableRegion) ROIs for plane_1 | shape = (232,) | dtype = int64
  Group /processing/ophys/Fluorescence/Plane_2 (RoiResponseSeries) no description
  Dataset /processing/ophys/Fluorescence/Plane_2/rois (DynamicTableRegion) ROIs for plane_2 | shape = (203,) | dtype = int64
  Group /processing/ophys/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation (PlaneSegmentation) suite2p output
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/id (ElementIdentifiers)  | shape = (531,) | dtype = int64
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/OpticalChannel (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/device (Device) Ultima Investigator
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/iscell (VectorData) two columns - iscell & probcell | shape = (531, 2) | dtype = float64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/voxel_mask (VectorData) Voxel masks for each ROI | shape = (198322,) | dtype = [('x', '<u4'), ('y', '<u4'), ('z', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/voxel_mask_index (VectorIndex) Index for VectorData 'voxel_mask' | shape = (531,) | dtype = uint32
  Group /processing/ophys/Neuropil (Fluorescence) 
  Group /processing/ophys/Neuropil/Plane_0 (RoiResponseSeries) no description
  Dataset /processing/ophys/Neuropil/Plane_0/rois (DynamicTableRegion) ROIs for plane_0 | shape = (96,) | dtype = int64
  Group /processing/ophys/Neuropil/Plane_1 (RoiResponseSeries) no description
  Dataset /processing/ophys/Neuropil/Plane_1/rois (DynamicTableRegion) ROIs for plane_1 | shape = (232,) | dtype = int64
  Group /processing/ophys/Neuropil/Plane_2 (RoiResponseSeries) no description
  Dataset /processing/ophys/Neuropil/Plane_2/rois (DynamicTableRegion) ROIs for plane_2 | shape = (203,) | dtype = int64
  session_description: 2P-PCx-passive-odor
  session_start_time: 2020-01-24T16:15:14.714664-05:00
  Group /stimulus/presentation/odor (TimeSeries) no description
  timestamps_reference_time: 2020-01-24T16:15:14.714664-05:00
