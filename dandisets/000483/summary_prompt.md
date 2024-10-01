
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000483/0.230421.2321
name: Dataset for "Coregistration of heading to visual cues in retrosplenial cortex"
contributor: [{'name': 'Sit, Kevin', 'email': 'sit@ucsb.edu', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0003-0210-9010', 'affiliation': [], 'includeInCitation': True}, {'name': 'Goard, Michael', 'email': 'michael.goard@lifesci.ucsb.edu', 'roleName': ['dcite:Author', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0002-5366-8501', 'affiliation': [], 'includeInCitation': True}, {'name': ' National Institutes of Health', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01cwqze88', 'awardNumber': '1RF1NS121919', 'contactPoint': [], 'includeInCitation': False}]
description: These are all the accompanying data for the following publication:
Sit, K.K., Goard, M.J. Coregistration of heading to visual cues in retrosplenial cortex. Nat Commun 14, 1992 (2023). https://doi.org/10.1038/s41467-023-37704-5
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}, {'name': 'behavioral approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 695653683544, 'numberOfFiles': 128, 'numberOfSubjects': 20, 'variableMeasured': ['CompassDirection', 'OpticalChannel', 'PlaneSegmentation', 'SpatialSeries', 'ImagingPlane', 'Position', 'ProcessingModule', 'TwoPhotonSeries'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'two-photon microscopy technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000483 has 7 NWB files.
2 of these NWB files are of type 1.
2 of these NWB files are of type 2.
1 of these NWB files are of type 3.
1 of these NWB files are of type 4.
1 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/SKKS080-SingleCue-001: two-photon-series (TwoPhotonSeries) two photon image stack
  Group /acquisition/SKKS080-SingleCue-001: two-photon-series/device (Device) Investigator Ultima
  Group /acquisition/SKKS080-SingleCue-001: two-photon-series/imaging_plane (ImagingPlane) 
  Group /acquisition/SKKS080-SingleCue-001: two-photon-series/imaging_plane/GCaMP6s (OpticalChannel) 
  Group /acquisition/SKKS080-SingleCue-001: two-photon-series/imaging_plane/device (Device) Investigator Ultima
  file_create_date: ['2023-04-20T22:52:13.661840-07:00']
  Group /general/devices/two-photon (Device) Investigator Ultima
  experimenter: ['KKS']
  institution: UC Santa Barbara
  keywords: ['201119_KKS_SKKS080_SingleCueNeurotar_SKKS080-SingleCue-001'
   'SKKS080-SingleCue-001' '201119_KKS_SKKS080_SingleCueNeurotar' '201119'
   'KKS' 'SKKS080' '201119']
  lab: Goard lab
  Group /general/optophysiology/imgplane (ImagingPlane) 
  Group /general/optophysiology/imgplane/GCaMP6s (OpticalChannel) 
  Group /general/optophysiology/imgplane/device (Device) Investigator Ultima
  related_publications: ['https://doi.org/10.1038/s41467-023-37704-5']
  Group /general/subject (Subject) 
  identifier: 201119_KKS_SKKS080_SingleCueNeurotar_SKKS080-SingleCue-001
  Group /processing/neurotar-data (ProcessingModule) processed data from neurotar
  Group /processing/neurotar-data/floating cage orientation (CompassDirection) 
  Group /processing/neurotar-data/floating cage orientation/heading-spatial-series (SpatialSeries) no description
  Group /processing/neurotar-data/location in floating cage (Position) 
  Group /processing/neurotar-data/location in floating cage/position-spatial-series (SpatialSeries) no description
  Group /processing/ophys (ProcessingModule) processed optical physiology data
  Group /processing/ophys/Fluorescence (Fluorescence) 
  Group /processing/ophys/Fluorescence/raw-fluorescence (RoiResponseSeries) no description
  Dataset /processing/ophys/Fluorescence/raw-fluorescence/rois (DynamicTableRegion) rois | shape = (293,) | dtype = int64
  Group /processing/ophys/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/ImageSegmentation/cell-rois (PlaneSegmentation) pixel masks defining rois (putative cells)
  Dataset /processing/ophys/ImageSegmentation/cell-rois/id (ElementIdentifiers)  | shape = (293,) | dtype = int64
  Group /processing/ophys/ImageSegmentation/cell-rois/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/cell-rois/imaging_plane/GCaMP6s (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/cell-rois/imaging_plane/device (Device) Investigator Ultima
  Dataset /processing/ophys/ImageSegmentation/cell-rois/pixel_mask (VectorData) Pixel masks for each ROI | shape = (39045,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/ImageSegmentation/cell-rois/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (293,) | dtype = uint16
  session_description: floating air cage experiment
  session_start_time: 2020-11-19T15:52:30.489407-08:00
  timestamps_reference_time: 2020-11-19T15:52:30.489407-08:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/SKKS080-SingleCue-002: two-photon-series (TwoPhotonSeries) two photon image stack
  Group /acquisition/SKKS080-SingleCue-002: two-photon-series/device (Device) Investigator Ultima
  Group /acquisition/SKKS080-SingleCue-002: two-photon-series/imaging_plane (ImagingPlane) 
  Group /acquisition/SKKS080-SingleCue-002: two-photon-series/imaging_plane/GCaMP6s (OpticalChannel) 
  Group /acquisition/SKKS080-SingleCue-002: two-photon-series/imaging_plane/device (Device) Investigator Ultima
  file_create_date: ['2023-04-20T22:55:38.609647-07:00']
  Group /general/devices/two-photon (Device) Investigator Ultima
  experimenter: ['KKS']
  institution: UC Santa Barbara
  keywords: ['201119_KKS_SKKS080_SingleCueNeurotar_SKKS080-SingleCue-002'
   'SKKS080-SingleCue-002' '201119_KKS_SKKS080_SingleCueNeurotar' '201119'
   'KKS' 'SKKS080' '201119']
  lab: Goard lab
  Group /general/optophysiology/imgplane (ImagingPlane) 
  Group /general/optophysiology/imgplane/GCaMP6s (OpticalChannel) 
  Group /general/optophysiology/imgplane/device (Device) Investigator Ultima
  related_publications: ['https://doi.org/10.1038/s41467-023-37704-5']
  Group /general/subject (Subject) 
  identifier: 201119_KKS_SKKS080_SingleCueNeurotar_SKKS080-SingleCue-002
  Group /processing/neurotar-data (ProcessingModule) processed data from neurotar
  Group /processing/neurotar-data/floating cage orientation (CompassDirection) 
  Group /processing/neurotar-data/floating cage orientation/heading-spatial-series (SpatialSeries) no description
  Group /processing/neurotar-data/location in floating cage (Position) 
  Group /processing/neurotar-data/location in floating cage/position-spatial-series (SpatialSeries) no description
  Group /processing/ophys (ProcessingModule) processed optical physiology data
  Group /processing/ophys/Fluorescence (Fluorescence) 
  Group /processing/ophys/Fluorescence/raw-fluorescence (RoiResponseSeries) no description
  Dataset /processing/ophys/Fluorescence/raw-fluorescence/rois (DynamicTableRegion) rois | shape = (285,) | dtype = int64
  Group /processing/ophys/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/ImageSegmentation/cell-rois (PlaneSegmentation) pixel masks defining rois (putative cells)
  Dataset /processing/ophys/ImageSegmentation/cell-rois/id (ElementIdentifiers)  | shape = (285,) | dtype = int64
  Group /processing/ophys/ImageSegmentation/cell-rois/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/cell-rois/imaging_plane/GCaMP6s (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/cell-rois/imaging_plane/device (Device) Investigator Ultima
  Dataset /processing/ophys/ImageSegmentation/cell-rois/pixel_mask (VectorData) Pixel masks for each ROI | shape = (39352,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/ImageSegmentation/cell-rois/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (285,) | dtype = uint16
  session_description: floating air cage experiment
  session_start_time: 2020-11-19T15:57:43.195173-08:00
  timestamps_reference_time: 2020-11-19T15:57:43.195173-08:00


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/SKKS080-SingleCue-003: two-photon-series (TwoPhotonSeries) two photon image stack
  Group /acquisition/SKKS080-SingleCue-003: two-photon-series/device (Device) Investigator Ultima
  Group /acquisition/SKKS080-SingleCue-003: two-photon-series/imaging_plane (ImagingPlane) 
  Group /acquisition/SKKS080-SingleCue-003: two-photon-series/imaging_plane/GCaMP6s (OpticalChannel) 
  Group /acquisition/SKKS080-SingleCue-003: two-photon-series/imaging_plane/device (Device) Investigator Ultima
  file_create_date: ['2023-04-20T22:57:17.372647-07:00']
  Group /general/devices/two-photon (Device) Investigator Ultima
  experimenter: ['KKS']
  institution: UC Santa Barbara
  keywords: ['201119_KKS_SKKS080_SingleCueNeurotar_SKKS080-SingleCue-003'
   'SKKS080-SingleCue-003' '201119_KKS_SKKS080_SingleCueNeurotar' '201119'
   'KKS' 'SKKS080' '201119']
  lab: Goard lab
  Group /general/optophysiology/imgplane (ImagingPlane) 
  Group /general/optophysiology/imgplane/GCaMP6s (OpticalChannel) 
  Group /general/optophysiology/imgplane/device (Device) Investigator Ultima
  related_publications: ['https://doi.org/10.1038/s41467-023-37704-5']
  Group /general/subject (Subject) 
  identifier: 201119_KKS_SKKS080_SingleCueNeurotar_SKKS080-SingleCue-003
  Group /processing/neurotar-data (ProcessingModule) processed data from neurotar
  Group /processing/neurotar-data/floating cage orientation (CompassDirection) 
  Group /processing/neurotar-data/floating cage orientation/heading-spatial-series (SpatialSeries) no description
  Group /processing/neurotar-data/location in floating cage (Position) 
  Group /processing/neurotar-data/location in floating cage/position-spatial-series (SpatialSeries) no description
  Group /processing/ophys (ProcessingModule) processed optical physiology data
  Group /processing/ophys/Fluorescence (Fluorescence) 
  Group /processing/ophys/Fluorescence/raw-fluorescence (RoiResponseSeries) no description
  Dataset /processing/ophys/Fluorescence/raw-fluorescence/rois (DynamicTableRegion) rois | shape = (313,) | dtype = int64
  Group /processing/ophys/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/ImageSegmentation/cell-rois (PlaneSegmentation) pixel masks defining rois (putative cells)
  Dataset /processing/ophys/ImageSegmentation/cell-rois/id (ElementIdentifiers)  | shape = (313,) | dtype = int64
  Group /processing/ophys/ImageSegmentation/cell-rois/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/cell-rois/imaging_plane/GCaMP6s (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/cell-rois/imaging_plane/device (Device) Investigator Ultima
  Dataset /processing/ophys/ImageSegmentation/cell-rois/pixel_mask (VectorData) Pixel masks for each ROI | shape = (42913,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/ImageSegmentation/cell-rois/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (313,) | dtype = uint16
  session_description: floating air cage experiment
  session_start_time: 2020-11-19T16:03:16.758496-08:00
  timestamps_reference_time: 2020-11-19T16:03:16.758496-08:00


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/SKKS080-SingleCue-004: two-photon-series (TwoPhotonSeries) two photon image stack
  Group /acquisition/SKKS080-SingleCue-004: two-photon-series/device (Device) Investigator Ultima
  Group /acquisition/SKKS080-SingleCue-004: two-photon-series/imaging_plane (ImagingPlane) 
  Group /acquisition/SKKS080-SingleCue-004: two-photon-series/imaging_plane/GCaMP6s (OpticalChannel) 
  Group /acquisition/SKKS080-SingleCue-004: two-photon-series/imaging_plane/device (Device) Investigator Ultima
  file_create_date: ['2023-04-20T22:58:57.645665-07:00']
  Group /general/devices/two-photon (Device) Investigator Ultima
  experimenter: ['KKS']
  institution: UC Santa Barbara
  keywords: ['201119_KKS_SKKS080_SingleCueNeurotar_SKKS080-SingleCue-004'
   'SKKS080-SingleCue-004' '201119_KKS_SKKS080_SingleCueNeurotar' '201119'
   'KKS' 'SKKS080' '201119']
  lab: Goard lab
  Group /general/optophysiology/imgplane (ImagingPlane) 
  Group /general/optophysiology/imgplane/GCaMP6s (OpticalChannel) 
  Group /general/optophysiology/imgplane/device (Device) Investigator Ultima
  related_publications: ['https://doi.org/10.1038/s41467-023-37704-5']
  Group /general/subject (Subject) 
  identifier: 201119_KKS_SKKS080_SingleCueNeurotar_SKKS080-SingleCue-004
  Group /processing/neurotar-data (ProcessingModule) processed data from neurotar
  Group /processing/neurotar-data/floating cage orientation (CompassDirection) 
  Group /processing/neurotar-data/floating cage orientation/heading-spatial-series (SpatialSeries) no description
  Group /processing/neurotar-data/location in floating cage (Position) 
  Group /processing/neurotar-data/location in floating cage/position-spatial-series (SpatialSeries) no description
  Group /processing/ophys (ProcessingModule) processed optical physiology data
  Group /processing/ophys/Fluorescence (Fluorescence) 
  Group /processing/ophys/Fluorescence/raw-fluorescence (RoiResponseSeries) no description
  Dataset /processing/ophys/Fluorescence/raw-fluorescence/rois (DynamicTableRegion) rois | shape = (398,) | dtype = int64
  Group /processing/ophys/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/ImageSegmentation/cell-rois (PlaneSegmentation) pixel masks defining rois (putative cells)
  Dataset /processing/ophys/ImageSegmentation/cell-rois/id (ElementIdentifiers)  | shape = (398,) | dtype = int64
  Group /processing/ophys/ImageSegmentation/cell-rois/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/cell-rois/imaging_plane/GCaMP6s (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/cell-rois/imaging_plane/device (Device) Investigator Ultima
  Dataset /processing/ophys/ImageSegmentation/cell-rois/pixel_mask (VectorData) Pixel masks for each ROI | shape = (49646,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/ImageSegmentation/cell-rois/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (398,) | dtype = uint16
  session_description: floating air cage experiment
  session_start_time: 2020-11-19T16:12:24.477757-08:00
  timestamps_reference_time: 2020-11-19T16:12:24.477757-08:00


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  Group /acquisition/SKKS080-DualCue-003: two-photon-series (TwoPhotonSeries) two photon image stack
  Group /acquisition/SKKS080-DualCue-003: two-photon-series/device (Device) Investigator Ultima
  Group /acquisition/SKKS080-DualCue-003: two-photon-series/imaging_plane (ImagingPlane) 
  Group /acquisition/SKKS080-DualCue-003: two-photon-series/imaging_plane/GCaMP6s (OpticalChannel) 
  Group /acquisition/SKKS080-DualCue-003: two-photon-series/imaging_plane/device (Device) Investigator Ultima
  file_create_date: ['2023-04-20T15:19:08.697810-07:00']
  Group /general/devices/two-photon (Device) Investigator Ultima
  experimenter: ['KKS']
  institution: UC Santa Barbara
  keywords: ['201123_KKS_SKKS080_NeurotarFlipFlop_SKKS080-DualCue-003'
   'SKKS080-DualCue-003' '201123_KKS_SKKS080_NeurotarFlipFlop' '201123'
   'KKS' 'SKKS080' '201123']
  lab: Goard lab
  Group /general/optophysiology/imgplane (ImagingPlane) 
  Group /general/optophysiology/imgplane/GCaMP6s (OpticalChannel) 
  Group /general/optophysiology/imgplane/device (Device) Investigator Ultima
  related_publications: ['https://doi.org/10.1038/s41467-023-37704-5']
  Group /general/subject (Subject) 
  identifier: 201123_KKS_SKKS080_NeurotarFlipFlop_SKKS080-DualCue-003
  Group /processing/neurotar-data (ProcessingModule) processed data from neurotar
  Group /processing/neurotar-data/floating cage orientation (CompassDirection) 
  Group /processing/neurotar-data/floating cage orientation/heading-spatial-series (SpatialSeries) no description
  Group /processing/neurotar-data/location in floating cage (Position) 
  Group /processing/neurotar-data/location in floating cage/position-spatial-series (SpatialSeries) no description
  Group /processing/ophys (ProcessingModule) processed optical physiology data
  Group /processing/ophys/Fluorescence (Fluorescence) 
  Group /processing/ophys/Fluorescence/raw-fluorescence (RoiResponseSeries) no description
  Dataset /processing/ophys/Fluorescence/raw-fluorescence/rois (DynamicTableRegion) rois | shape = (112,) | dtype = int64
  Group /processing/ophys/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/ImageSegmentation/cell-rois (PlaneSegmentation) pixel masks defining rois (putative cells)
  Dataset /processing/ophys/ImageSegmentation/cell-rois/id (ElementIdentifiers)  | shape = (112,) | dtype = int64
  Group /processing/ophys/ImageSegmentation/cell-rois/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/cell-rois/imaging_plane/GCaMP6s (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/cell-rois/imaging_plane/device (Device) Investigator Ultima
  Dataset /processing/ophys/ImageSegmentation/cell-rois/pixel_mask (VectorData) Pixel masks for each ROI | shape = (14634,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/ImageSegmentation/cell-rois/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (112,) | dtype = uint16
  session_description: floating air cage experiment
  session_start_time: 2020-11-23T13:35:53.300172-08:00
  timestamps_reference_time: 2020-11-23T13:35:53.300172-08:00
