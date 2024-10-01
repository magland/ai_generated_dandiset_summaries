
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000625/0.231114.0019
name: Molecularly Identified CA1 Interneuron Dynamics
contributor: [{'name': 'Zakka, George', 'email': 'gz2333@columbia.edu', 'roleName': ['dcite:DataCurator', 'dcite:DataManager', 'dcite:Maintainer', 'dcite:ProjectMember', 'dcite:Researcher', 'dcite:Software', 'dcite:Resources', 'dcite:Supervision', 'dcite:Affiliation'], 'schemaKey': 'Person', 'affiliation': [{'name': 'Columbia University', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/00hj8s172'}], 'includeInCitation': False}, {'url': 'http://www.columbia.edu/~tcg2117/', 'name': 'Geiller, Tristan', 'email': 'tristan.geiller@gmail.com', 'roleName': ['dcite:ContactPerson', 'dcite:Author', 'dcite:DataCollector'], 'schemaKey': 'Person', 'affiliation': [{'name': 'Columbia University', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/00hj8s172'}], 'awardNumber': '', 'includeInCitation': True}, {'url': 'https://www.nimh.nih.gov/index.shtml', 'name': 'National Institute of Mental Health', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/04xeg9z08', 'awardNumber': '1R01MH100631', 'contactPoint': [], 'includeInCitation': False}, {'url': 'http://www.ninds.nih.gov/', 'name': 'National Institute of Neurological Disorders and Stroke', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01s5ya894', 'awardNumber': '1U19NS104590', 'contactPoint': [], 'includeInCitation': False}, {'url': 'http://www.ninds.nih.gov/', 'name': 'National Institute of Neurological Disorders and Stroke', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01s5ya894', 'awardNumber': '1R01NS094668', 'contactPoint': [], 'includeInCitation': False}]
description: This dataset was collected to examine the dynamics of mouse interneurons whose subtypes were molecularly identified. 231 ROIs were observed over 3 separate imaging sessions. For each session you will find the following:
- Raw images (individual cropped ROIs)
- DfOverF traces
- Fluorescence traces
- Subtype of each ROI (some are undetermined)
- Timing of water rewards
- Time-stamped position of subject


Data was collected by Tristan Geiller at the Losonczy Lab using two photon calcium imaging and head-fixed mice running on a voluntary treadmill.
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'behavioral approach', 'schemaKey': 'ApproachType'}, {'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 74904128, 'numberOfFiles': 3, 'numberOfSubjects': 1, 'variableMeasured': ['BehavioralEpochs', 'ProcessingModule', 'SpatialSeries', 'TwoPhotonSeries', 'Position', 'ImagingPlane', 'OpticalChannel', 'PlaneSegmentation'], 'measurementTechnique': [{'name': 'two-photon microscopy technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000625 has 3 NWB files.
3 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Position (Position) 
  Group /acquisition/Position/SpatialSeries (SpatialSeries) 1D position on a treadmill belt
  Group /acquisition/TwoPhotonSeries2 (TwoPhotonSeries) no description
  Group /acquisition/TwoPhotonSeries2/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeries2/imaging_plane/Green (OpticalChannel) 
  Group /acquisition/TwoPhotonSeries2/imaging_plane/device (Device) Losonczy lab Femto3D-Atlas
  file_create_date: ['2023-11-13T18:16:46.969234+00:00']
  Group /general/devices/JLG-L7-041 (Device) Losonczy lab Femto3D-Atlas
  experiment_description: Head-fixed mouse running on a treadmill belt during 4 random foraging sessions,                         the objective being to label the most numerous interneuron subtypes.
  experimenter: ['Geiller, Tristan']
  institution: Columbia University
  keywords: ['2-photon calcium imaging' 'Interneuron' 'Hippocampus' 'CA1' 'Head-fixed'
   'Mouse']
  lab: Losonczy Lab
  Group /general/optophysiology/CA1 (ImagingPlane) 
  Group /general/optophysiology/CA1/Green (OpticalChannel) 
  Group /general/optophysiology/CA1/device (Device) Losonczy lab Femto3D-Atlas
  session_id: 21322
  Group /general/subject (Subject) 
  identifier: 38ec22cf-6173-4696-b870-50195a006a7b
  Group /processing/behavior (ProcessingModule) raw behavioral data
  Group /processing/behavior/BehavioralEpochs (BehavioralEpochs) 
  Group /processing/behavior/BehavioralEpochs/reward (IntervalSeries) no description
  Group /processing/behavior/BehavioralEpochs/water (IntervalSeries) no description
  Group /processing/ophys (ProcessingModule) optical physiology processed data
  Group /processing/ophys/Cell_Subtypes (DynamicTable) Specifies the ROI cell's subtype where subtype may be ['PVBC', 'SOM', 'NOTHING', 'BISTR', 'NGFF', 'CCK', 'AAC', 'AAC (RIGHT CELL)']
  Dataset /processing/ophys/Cell_Subtypes/id (ElementIdentifiers)  | shape = (232,) | dtype = int64
  Dataset /processing/ophys/Cell_Subtypes/subtype (VectorData) Recording location in Middle Earth | shape = (232,) | dtype = object
  Group /processing/ophys/DfOverF (DfOverF) 
  Group /processing/ophys/DfOverF/RoiResponseSeries (RoiResponseSeries) no description
  Dataset /processing/ophys/DfOverF/RoiResponseSeries/rois (DynamicTableRegion) All 231 ROIs | shape = (231,) | dtype = int64
  Group /processing/ophys/Fluorescence (Fluorescence) 
  Group /processing/ophys/Fluorescence/RoiResponseSeries (RoiResponseSeries) no description
  Dataset /processing/ophys/Fluorescence/RoiResponseSeries/rois (DynamicTableRegion) All 231 ROIs | shape = (231,) | dtype = int64
  Group /processing/ophys/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/ImageSegmentation/CA1 plane segmentation (PlaneSegmentation) no description
  Dataset /processing/ophys/ImageSegmentation/CA1 plane segmentation/id (ElementIdentifiers)  | shape = (231,) | dtype = int64
  Group /processing/ophys/ImageSegmentation/CA1 plane segmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/CA1 plane segmentation/imaging_plane/Green (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/CA1 plane segmentation/imaging_plane/device (Device) Losonczy lab Femto3D-Atlas
  Dataset /processing/ophys/ImageSegmentation/CA1 plane segmentation/pixel_mask (VectorData) Pixel masks for each ROI | shape = (350658,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/ImageSegmentation/CA1 plane segmentation/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (231,) | dtype = uint32
  session_description: Random foraging: session 1 of 4. Experiment group: imvgat.
  session_start_time: 2019-06-13T18:02:27+00:00
  timestamps_reference_time: 2019-06-13T18:02:27+00:00
