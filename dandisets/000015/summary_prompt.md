
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000015/0.220126.1914
name: A Map of Anticipatory Activity in Mouse Motor Cortex
contributor: [{'name': 'Chen, Tsai-Wen', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Li, Nuo', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Daie, Kayvon', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Svoboda, Karel', 'roleName': ['dcite:Author', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0002-6670-7362', 'affiliation': [], 'includeInCitation': True}]
description: Data from "A Map of Anticipatory Activity in Mouse Motor Cortex" Chen et al. Neuron 2017
assetsSummary: {'species': [{'name': 'House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'behavioral approach', 'schemaKey': 'ApproachType'}, {'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 17159727736, 'numberOfFiles': 210, 'numberOfSubjects': 6, 'variableMeasured': ['BehavioralEvents', 'PlaneSegmentation'], 'measurementTechnique': [{'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000015 has 100 NWB files.
100 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/images (Images) Structural images of a scanning
  Dataset /acquisition/images/GCaMP at 940nm (GrayscaleImage)  | shape = (512, 512) | dtype = float32
  file_create_date: ['2020-01-16T00:15:35.107470+00:00']
  Group /general/devices/two-photon microscope with Thorlabs resonant galvo scannner (Device) 
  experiment_description: Two-photon experiment recorded in left_vm1
  experimenter: ['Tsai-Wen Chen']
  institution: Janelia Research Campus
  keywords: ['motor planning' 'anterior lateral cortex' 'medial motor cortex' 'ALM'
   'MM' 'Two-photon imaging']
  Group /general/optophysiology/ImagingPlane (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane/device (Device) 
  Group /general/optophysiology/ImagingPlane/green (OpticalChannel) 
  related_publications: ['http://dx.doi.org/10.1016/j.neuron.2017.05.005']
  Group /general/subject (Subject) 
  virus: []
  identifier: an041_2014-08-21_9
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/early_lick (VectorData) varchar(32) # | shape = (103,) | dtype = bool
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (103,) | dtype = int64
  Dataset /intervals/trials/outcome (VectorData) varchar(32) # | shape = (103,) | dtype = object
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (103,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (103,) | dtype = float64
  Dataset /intervals/trials/task (VectorData) varchar(12) # task type | shape = (103,) | dtype = object
  Dataset /intervals/trials/task_protocol (VectorData) tinyint # task protocol | shape = (103,) | dtype = int64
  Dataset /intervals/trials/trial_instruction (VectorData) varchar(16) # | shape = (103,) | dtype = object
  Group /processing/behavior (ProcessingModule) Time of behavioral events in this session
  Group /processing/behavior/BehavioralEvents (BehavioralEvents) 
  Group /processing/behavior/BehavioralEvents/delay (TimeSeries) Time stamps of the beginning of the delay period on each trial.
  Group /processing/behavior/BehavioralEvents/go (TimeSeries) Time stamps of the go cue signal on each trial.
  Group /processing/behavior/BehavioralEvents/sample (TimeSeries) Time stamps of the beginning of the sampling period on each trial.
  Group /processing/ophys (ProcessingModule) Processing result of imaging
  Group /processing/ophys/Fluorescence (Fluorescence) 
  Group /processing/ophys/Fluorescence/NeuropilResponseSeries (RoiResponseSeries) average fluorescence of the neuropil surrounding the roi
  Dataset /processing/ophys/Fluorescence/NeuropilResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (137,) | dtype = int64
  Group /processing/ophys/Fluorescence/RoiResponseSeries (RoiResponseSeries) average fluorescence of roi
  Dataset /processing/ophys/Fluorescence/RoiResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (137,) | dtype = int64
  Group /processing/ophys/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation (PlaneSegmentation) output from segmenting the current imaging plane
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/cell_type (VectorData) PT, IT, or unknown | shape = (137,) | dtype = object
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/id (ElementIdentifiers)  | shape = (137,) | dtype = int64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (137, 512, 512) | dtype = bool
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/device (Device) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/green (OpticalChannel) 
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/included (VectorData) whether to include this roi into later analyses | shape = (137,) | dtype = bool
  session_description: Imaging session
  session_start_time: 2014-08-21T00:00:00+00:00
  timestamps_reference_time: 2014-08-21T00:00:00+00:00
