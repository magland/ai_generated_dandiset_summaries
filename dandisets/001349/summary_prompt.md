
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001349/0.250604.1510
name: From Initial Formation to Developmental Refinement: GABAergic Inputs Shape Neuronal Subnetworks in the Primary Somatosensory Cortex
contributor: [{'name': 'Huang, Jui-Yen', 'email': 'juiyhuan@iu.edu', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}]
description: The calcium imaging data were obtained through two-photon awake imaging of the somatosensory cortex in developing mice from P11 to P21. Simultaneously, behavioral video recordings were collected from the experimental setup. The two modalities were synchronized using an LED signal at the start and end of the two-photon imaging experiment. Imaging data analysis was performed using Python or MATLAB, utilizing standard toolboxes, open-access toolboxes, and custom-written code.
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 10498307134, 'numberOfFiles': 422, 'numberOfSubjects': 32, 'variableMeasured': ['ProcessingModule', 'ImagingPlane', 'PlaneSegmentation', 'OpticalChannel'], 'measurementTechnique': [{'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 001349 has 100 NWB files.
100 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2025-05-14T23:45:17.928064+00:00']
  data_collection: Two-photon calcium imaging
  Group /general/devices/Nikon A1 plus (Device) Two photon microscope
  experiment_description: Mouse behavior and neural imaging
  experimenter: ['Edna']
  institution: Indiana University Bloomington
  keywords: ['calcium imaging' 'behavior' 'pose estimation']
  Group /general/optophysiology/ImagingPlane_1_chn1 (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane_1_chn1/OpticalChannel1 (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane_1_chn1/device (Device) Two photon microscope
  related_publications: ['']
  session_id: 0
  Group /general/subject (Subject) 
  identifier: C57-C2-1-AL_0
  Group /processing/ophys (ProcessingModule) optical physiology processed data
  Group /processing/ophys/Fluorescence (Fluorescence) 
  Group /processing/ophys/Fluorescence/ca_events_chn0 (RoiResponseSeries) Ca_Events
  Dataset /processing/ophys/Fluorescence/ca_events_chn0/rois (DynamicTableRegion) All ROIs from database. | shape = (197,) | dtype = int32
  Group /processing/ophys/Fluorescence/dff_chn0 (RoiResponseSeries) Dff
  Dataset /processing/ophys/Fluorescence/dff_chn0/rois (DynamicTableRegion) All ROIs from database. | shape = (197,) | dtype = int32
  Group /processing/ophys/Fluorescence/f_corrected_chn0 (RoiResponseSeries) F_Corrected
  Dataset /processing/ophys/Fluorescence/f_corrected_chn0/rois (DynamicTableRegion) All ROIs from database. | shape = (197,) | dtype = int32
  Group /processing/ophys/Fluorescence/fluorescence_chn0 (RoiResponseSeries) Fluorescence
  Dataset /processing/ophys/Fluorescence/fluorescence_chn0/rois (DynamicTableRegion) All ROIs from database. | shape = (197,) | dtype = int32
  Group /processing/ophys/Fluorescence/neuropil_fluorescence_chn0 (RoiResponseSeries) Neuropil_Fluorescence
  Dataset /processing/ophys/Fluorescence/neuropil_fluorescence_chn0/rois (DynamicTableRegion) All ROIs from database. | shape = (197,) | dtype = int32
  Group /processing/ophys/Fluorescence/z_score_chn0 (RoiResponseSeries) Z_Score
  Dataset /processing/ophys/Fluorescence/z_score_chn0/rois (DynamicTableRegion) All ROIs from database. | shape = (197,) | dtype = int32
  Group /processing/ophys/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation_1 (PlaneSegmentation) output from segmenting
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_1/id (ElementIdentifiers)  | shape = (197,) | dtype = int32
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation_1/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation_1/imaging_plane/OpticalChannel1 (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation_1/imaging_plane/device (Device) Two photon microscope
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_1/pixel_mask (VectorData) Pixel masks for each ROI | shape = (32447,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_1/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (197,) | dtype = uint16
  session_description: CNOInjection: Neg; P15CNO: Neg
  session_start_time: 2022-03-12T00:00:00-06:00
  timestamps_reference_time: 2022-03-12T00:00:00-06:00
