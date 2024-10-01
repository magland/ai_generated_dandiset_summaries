
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000347/draft
name: Multiphoton imaging in macaque visual cortex (preliminary data)
contributor: [{'name': 'Chatterjee, Soumya', 'email': 'curmudgeonly@gmail.com', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}]
description: Two- and three-photon imaging from V1/V2 labeled with GCaMP6s. Grating stimuli (sf x dir).
assetsSummary: {'species': [{'name': 'Macaca nemestrina - Pig-tailed macaque', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9545'}], 'approach': [{'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 26039386048, 'numberOfFiles': 9, 'numberOfSubjects': 3, 'variableMeasured': ['OpticalChannel', 'PlaneSegmentation', 'ImagingPlane', 'TwoPhotonSeries', 'ProcessingModule'], 'measurementTechnique': [{'name': 'two-photon microscopy technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000347 has 9 NWB files.
1 of these NWB files are of type 1.
8 of these NWB files are of type 2.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/raw data (TwoPhotonSeries) no description
  Group /acquisition/raw data/imaging_plane (ImagingPlane) 
  Group /acquisition/raw data/imaging_plane/OpticalChannel (OpticalChannel) 
  Group /acquisition/raw data/imaging_plane/device (Device) Sutter MOM
  file_create_date: ['2022-10-21T13:42:37.739460-07:00']
  Group /general/devices/Microscope (Device) Sutter MOM
  institution: Allen Institute for Brain Science, University of Washington
  Group /general/optophysiology/ImagingPlane (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane/OpticalChannel (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane/device (Device) Sutter MOM
  Group /general/subject (Subject) 
  identifier: 131_007_01
  Group /intervals/stimulus_table (TimeIntervals) intervals for each stim condition
  Dataset /intervals/stimulus_table/direction (VectorData) grating param | shape = (240,) | dtype = float64
  Dataset /intervals/stimulus_table/id (ElementIdentifiers)  | shape = (240,) | dtype = int32
  Dataset /intervals/stimulus_table/sf (VectorData) grating param | shape = (240,) | dtype = float64
  Dataset /intervals/stimulus_table/start_time (VectorData) Start time of epoch, in seconds | shape = (240,) | dtype = float64
  Dataset /intervals/stimulus_table/stop_time (VectorData) Stop time of epoch, in seconds | shape = (240,) | dtype = float64
  Group /processing/ophys (ProcessingModule) optical physiology processed data
  Group /processing/ophys/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation (PlaneSegmentation) Suite2p segmentation output, with manual cell curation
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/id (ElementIdentifiers)  | shape = (1874,) | dtype = int32
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/OpticalChannel (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/device (Device) Sutter MOM
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/iscell (VectorData) cells following manual curation | shape = (1874,) | dtype = float64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/pixel_mask (VectorData) Pixel masks for each ROI | shape = (48043,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1874,) | dtype = uint16
  Group /processing/ophys/MotionCorrection (MotionCorrection) 
  Group /processing/ophys/MotionCorrection/CorrectedImageStack (CorrectedImageStack) 
  Group /processing/ophys/MotionCorrection/CorrectedImageStack/corrected (ImageSeries) no description
  Group /processing/ophys/MotionCorrection/CorrectedImageStack/original (TwoPhotonSeries) no description
  Group /processing/ophys/MotionCorrection/CorrectedImageStack/original/imaging_plane (ImagingPlane) 
  Group /processing/ophys/MotionCorrection/CorrectedImageStack/original/imaging_plane/OpticalChannel (OpticalChannel) 
  Group /processing/ophys/MotionCorrection/CorrectedImageStack/original/imaging_plane/device (Device) Sutter MOM
  Group /processing/ophys/MotionCorrection/CorrectedImageStack/xy_translation (TimeSeries) no description
  session_description: direction, sf stim matrix responses from V1/V2
  session_start_time: 2021-11-16T20:31:00-08:00
  timestamps_reference_time: 2021-11-16T20:31:00-08:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/raw data (TwoPhotonSeries) no description
  Group /acquisition/raw data/imaging_plane (ImagingPlane) 
  Group /acquisition/raw data/imaging_plane/OpticalChannel (OpticalChannel) 
  Group /acquisition/raw data/imaging_plane/device (Device) Sutter MOM
  file_create_date: ['2022-10-21T14:18:41.556305-07:00']
  Group /general/devices/Microscope (Device) Sutter MOM
  institution: Allen Institute for Brain Science, University of Washington
  Group /general/optophysiology/ImagingPlane (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane/OpticalChannel (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane/device (Device) Sutter MOM
  Group /general/subject (Subject) 
  identifier: 132_003_01
  Group /intervals/stimulus_table (TimeIntervals) intervals for each stim condition
  Dataset /intervals/stimulus_table/direction (VectorData) grating param | shape = (360,) | dtype = float64
  Dataset /intervals/stimulus_table/id (ElementIdentifiers)  | shape = (360,) | dtype = int32
  Dataset /intervals/stimulus_table/sf (VectorData) grating param | shape = (360,) | dtype = float64
  Dataset /intervals/stimulus_table/start_time (VectorData) Start time of epoch, in seconds | shape = (360,) | dtype = float64
  Dataset /intervals/stimulus_table/stop_time (VectorData) Stop time of epoch, in seconds | shape = (360,) | dtype = float64
  Group /processing/ophys (ProcessingModule) optical physiology processed data
  Group /processing/ophys/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation (PlaneSegmentation) Suite2p segmentation output, with manual cell curation
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/id (ElementIdentifiers)  | shape = (4707,) | dtype = int32
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/OpticalChannel (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/device (Device) Sutter MOM
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/iscell (VectorData) cells following manual curation | shape = (4707,) | dtype = float64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/pixel_mask (VectorData) Pixel masks for each ROI | shape = (20449,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (4707,) | dtype = uint16
  session_description: deep apicals; direction, sf stim matrix responses from V1/V2
  session_start_time: 2021-12-15T00:32:00-08:00
  timestamps_reference_time: 2021-12-15T00:32:00-08:00
