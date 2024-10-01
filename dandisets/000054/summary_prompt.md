
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000054/0.210819.1547
name: Plitt & Giocomo (2021) Experience Dependent Contextual Codes in the Hippocampus. Nat Neuro
contributor: [{'url': 'https://pubmed.ncbi.nlm.nih.gov/?cmd=search&term=Mark+H.+Plitt', 'name': 'Plitt, Mark', 'email': 'markplitt@gmail.com', 'roleName': ['dcite:Author', 'dcite:ContactPerson', 'dcite:DataCollector', 'dcite:DataCurator'], 'schemaKey': 'Person', 'identifier': '0000-0002-7154-6292', 'affiliation': [{'name': 'Department of Neurobiology, Stanford University, Stanford, CA, USA', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/03mtd9a03'}], 'includeInCitation': True}, {'url': 'https://pubmed.ncbi.nlm.nih.gov/?cmd=search&term=Lisa+M.+Giocomo', 'name': 'Giocomo, Lisa M.', 'email': 'giocomo@gmail.com', 'roleName': ['dcite:Author', 'dcite:Supervision', 'dcite:Researcher'], 'schemaKey': 'Person', 'identifier': '0000-0003-0416-2528', 'affiliation': [{'name': 'Stanford University', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/00f54p054'}], 'includeInCitation': True}]
description: Data included in Plitt & Giocomo (2021) Nature Neuroscience
assetsSummary: {'species': [{'name': 'House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'behavioral approach', 'schemaKey': 'ApproachType'}, {'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 1959122435577, 'numberOfFiles': 85, 'numberOfSubjects': 10, 'variableMeasured': ['PlaneSegmentation', 'TwoPhotonSeries', 'BehavioralTimeSeries', 'ProcessingModule'], 'measurementTechnique': [{'name': 'two-photon microscopy technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000054 has 85 NWB files.
1 of these NWB files are of type 1.
76 of these NWB files are of type 2.
3 of these NWB files are of type 3.
5 of these NWB files are of type 4.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/TwoPhotonSeries (TwoPhotonSeries) no description
  Group /acquisition/TwoPhotonSeries/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeries/imaging_plane/channel_0 (OpticalChannel) 
  Group /acquisition/TwoPhotonSeries/imaging_plane/device (Device) 
  file_create_date: ['2021-03-01T16:50:55.182813-05:00']
  Group /general/devices/Microscope (Device) 
  experiment_description: TwoTower_foraging
  experimenter: ['Mark Plitt']
  institution: Stanford University School of Medicine
  lab: GiocomoLab
  Group /general/optophysiology/ImagingPlane (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane/channel_0 (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane/device (Device) 
  Group /general/subject (Subject) 
  surgery: cannula implant date: 2020-02-20 00:00:00
  virus: virus injection date: 2020-02-20 00:00:00, virus: AAV1-CAG-FLEX-GCaMP6f-WPRE
  identifier: 3cf23589-be46-41f3-b280-8dfcf7636fa5
  Group /processing/ophys (ProcessingModule) contains optical physiology processed data
  Group /processing/ophys/Fluorescence (Fluorescence) 
  Group /processing/ophys/Fluorescence/Deconvolved (RoiResponseSeries) no description
  Dataset /processing/ophys/Fluorescence/Deconvolved/rois (DynamicTableRegion) region for Imaging plane0 | shape = (1033,) | dtype = int64
  Group /processing/ophys/Fluorescence/Neuropil (RoiResponseSeries) no description
  Dataset /processing/ophys/Fluorescence/Neuropil/rois (DynamicTableRegion) region for Imaging plane0 | shape = (1033,) | dtype = int64
  Group /processing/ophys/Fluorescence/RoiResponseSeries (RoiResponseSeries) no description
  Dataset /processing/ophys/Fluorescence/RoiResponseSeries/rois (DynamicTableRegion) region for Imaging plane0 | shape = (1033,) | dtype = int64
  Group /processing/ophys/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation (PlaneSegmentation) Segmented ROIs
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/Accepted (VectorData) 1 if ROi was accepted or 0 if rejected as a cell during segmentation operation | shape = (1033,) | dtype = int64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/Rejected (VectorData) 1 if ROi was rejected or 0 if accepted as a cell during segmentation operation | shape = (1033,) | dtype = int64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/RoiCentroid (VectorData) x,y location of centroid of the roi in image_mask | shape = (1033, 2) | dtype = int64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/id (ElementIdentifiers)  | shape = (1033,) | dtype = int64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/image_mask (VectorData) image masks | shape = (1033, 796, 512) | dtype = float64
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/channel_0 (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/device (Device) 
  Group /processing/ophys/SegmentationImages (Images) no description
  Dataset /processing/ophys/SegmentationImages/correlation (GrayscaleImage)  | shape = (796, 512) | dtype = float32
  Dataset /processing/ophys/SegmentationImages/mean (GrayscaleImage)  | shape = (796, 512) | dtype = float64
  session_description: TwoTower_foraging_001_001
  session_start_time: 2020-03-13T21:00:00-07:00
  timestamps_reference_time: 2020-03-13T21:00:00-07:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/TwoPhotonSeries (TwoPhotonSeries) no description
  Group /acquisition/TwoPhotonSeries/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeries/imaging_plane/channel_0 (OpticalChannel) 
  Group /acquisition/TwoPhotonSeries/imaging_plane/device (Device) 
  file_create_date: ['2021-03-01T11:53:37.192654-05:00']
  Group /general/devices/Microscope (Device) 
  experiment_description: TwoTower_foraging
  experimenter: ['Mark Plitt']
  institution: Stanford University School of Medicine
  lab: GiocomoLab
  Group /general/optophysiology/ImagingPlane (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane/channel_0 (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane/device (Device) 
  Group /general/subject (Subject) 
  surgery: cannula implant date: 2019-03-14 00:00:00
  virus: virus injection date: 2019-03-14 00:00:00, virus: AAV1-CAG-FLEX-GCaMP6f-WPRE
  identifier: c05b1b8f-2721-4880-87bc-e849134c703e
  Group /processing/behavior (ProcessingModule) Container for behavior time series
  Group /processing/behavior/BehavioralTimeSeries (BehavioralTimeSeries) 
  Group /processing/behavior/BehavioralTimeSeries/dz (TimeSeries) (virtual cm) raw rotary encoder information
  Group /processing/behavior/BehavioralTimeSeries/lick (TimeSeries) number of licks in 2P frame
  Group /processing/behavior/BehavioralTimeSeries/lick rate (TimeSeries) smooth version of no. licks
  Group /processing/behavior/BehavioralTimeSeries/pos (TimeSeries) (virtual cm) position on virtual reality track
  Group /processing/behavior/BehavioralTimeSeries/rzone (TimeSeries) information about collisions with objects in virtual track, 0-collision
  Group /processing/behavior/BehavioralTimeSeries/speed (TimeSeries) mouse's speed on ball
  Group /processing/behavior/BehavioralTimeSeries/teleport (TimeSeries) information about collisions with objects in virtual track, 0-collision
  Group /processing/behavior/BehavioralTimeSeries/tstart (TimeSeries) information about collisions with objects in virtual track, 0-collision
  Group /processing/ophys (ProcessingModule) contains optical physiology processed data
  Group /processing/ophys/Fluorescence (Fluorescence) 
  Group /processing/ophys/Fluorescence/Deconvolved (RoiResponseSeries) no description
  Dataset /processing/ophys/Fluorescence/Deconvolved/rois (DynamicTableRegion) region for Imaging plane0 | shape = (1003,) | dtype = int64
  Group /processing/ophys/Fluorescence/Neuropil (RoiResponseSeries) no description
  Dataset /processing/ophys/Fluorescence/Neuropil/rois (DynamicTableRegion) region for Imaging plane0 | shape = (1003,) | dtype = int64
  Group /processing/ophys/Fluorescence/RoiResponseSeries (RoiResponseSeries) no description
  Dataset /processing/ophys/Fluorescence/RoiResponseSeries/rois (DynamicTableRegion) region for Imaging plane0 | shape = (1003,) | dtype = int64
  Group /processing/ophys/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation (PlaneSegmentation) Segmented ROIs
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/Accepted (VectorData) 1 if ROi was accepted or 0 if rejected as a cell during segmentation operation | shape = (1003,) | dtype = int64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/Rejected (VectorData) 1 if ROi was rejected or 0 if accepted as a cell during segmentation operation | shape = (1003,) | dtype = int64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/RoiCentroid (VectorData) x,y location of centroid of the roi in image_mask | shape = (1003, 2) | dtype = int64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/id (ElementIdentifiers)  | shape = (1003,) | dtype = int64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/image_mask (VectorData) image masks | shape = (1003, 796, 512) | dtype = float64
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/channel_0 (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/device (Device) 
  Group /processing/ophys/SegmentationImages (Images) no description
  Dataset /processing/ophys/SegmentationImages/correlation (GrayscaleImage)  | shape = (796, 512) | dtype = float32
  Dataset /processing/ophys/SegmentationImages/mean (GrayscaleImage)  | shape = (796, 512) | dtype = float64
  session_description: TwoTower_foraging_001_006
  session_start_time: 2019-04-07T21:00:00-07:00
  Group /stimulus/presentation/bckgndJitter (TimeSeries) information about stimulus in arbitrary units
  Group /stimulus/presentation/morph (TimeSeries) information about stimulus in arbitrary units
  Group /stimulus/presentation/reward (TimeSeries) number of rewards dispensed 
  Group /stimulus/presentation/towerJitter (TimeSeries) information about stimulus in arbitrary units
  Group /stimulus/presentation/wallJitter (TimeSeries) information about stimulus in arbitrary units
  timestamps_reference_time: 2019-04-07T21:00:00-07:00


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/TwoPhotonSeries (TwoPhotonSeries) no description
  Group /acquisition/TwoPhotonSeries/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeries/imaging_plane/channel_0 (OpticalChannel) 
  Group /acquisition/TwoPhotonSeries/imaging_plane/device (Device) 
  file_create_date: ['2021-03-01T16:50:53.047194-05:00']
  Group /general/devices/Microscope (Device) 
  experiment_description: TwoTower_foraging
  experimenter: ['Mark Plitt']
  institution: Stanford University School of Medicine
  lab: GiocomoLab
  Group /general/optophysiology/ImagingPlane (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane/channel_0 (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane/device (Device) 
  Group /general/subject (Subject) 
  surgery: cannula implant date: 2020-02-20 00:00:00
  virus: virus injection date: 2020-02-20 00:00:00, virus: AAV1-CAG-FLEX-GCaMP6f-WPRE
  identifier: 41a2c96c-dca5-4829-97f1-3b98534598de
  Group /processing/behavior (ProcessingModule) Container for behavior time series
  Group /processing/behavior/BehavioralTimeSeries (BehavioralTimeSeries) 
  Group /processing/behavior/BehavioralTimeSeries/dz (TimeSeries) (virtual cm) raw rotary encoder information
  Group /processing/behavior/BehavioralTimeSeries/lick (TimeSeries) number of licks in 2P frame
  Group /processing/behavior/BehavioralTimeSeries/lick rate (TimeSeries) smooth version of no. licks
  Group /processing/behavior/BehavioralTimeSeries/pos (TimeSeries) (virtual cm) position on virtual reality track
  Group /processing/behavior/BehavioralTimeSeries/rzone (TimeSeries) information about collisions with objects in virtual track, 0-collision
  Group /processing/behavior/BehavioralTimeSeries/speed (TimeSeries) mouse's speed on ball
  Group /processing/behavior/BehavioralTimeSeries/teleport (TimeSeries) information about collisions with objects in virtual track, 0-collision
  Group /processing/behavior/BehavioralTimeSeries/tstart (TimeSeries) information about collisions with objects in virtual track, 0-collision
  session_description: TwoTower_foraging_002_006
  session_start_time: 2020-03-19T21:00:00-07:00
  Group /stimulus/presentation/bckgndJitter (TimeSeries) information about stimulus in arbitrary units
  Group /stimulus/presentation/morph (TimeSeries) information about stimulus in arbitrary units
  Group /stimulus/presentation/reward (TimeSeries) number of rewards dispensed 
  Group /stimulus/presentation/towerJitter (TimeSeries) information about stimulus in arbitrary units
  Group /stimulus/presentation/wallJitter (TimeSeries) information about stimulus in arbitrary units
  timestamps_reference_time: 2020-03-19T21:00:00-07:00


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/TwoPhotonSeries (TwoPhotonSeries) no description
  Group /acquisition/TwoPhotonSeries/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeries/imaging_plane/channel_0 (OpticalChannel) 
  Group /acquisition/TwoPhotonSeries/imaging_plane/device (Device) 
  file_create_date: ['2021-03-02T09:07:01.785253-05:00']
  Group /general/devices/Microscope (Device) 
  experiment_description: TwoTower_foraging
  experimenter: ['Mark Plitt']
  institution: Stanford University School of Medicine
  lab: GiocomoLab
  Group /general/optophysiology/ImagingPlane (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane/channel_0 (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane/device (Device) 
  Group /general/subject (Subject) 
  surgery: cannula implant date: 2019-01-09 00:00:00
  virus: virus injection date: 2018-12-20 00:00:00, virus: AAV-PHP.eB-EF1a-DIO-GCaMP6f (retro-orbital injection)
  identifier: 938d137e-45c6-4344-ba0f-d9a420d2b66c
  session_description: TwoTower_foraging_002_002
  session_start_time: 2019-02-06T21:00:00-08:00
  timestamps_reference_time: 2019-02-06T21:00:00-08:00
