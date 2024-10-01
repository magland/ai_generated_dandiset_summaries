
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000289/0.240801.1040
name: Two-photon calcium imaging of EPG cells in Drosophila Melanogaster presented with cues of varying reliability
contributor: [{'name': 'National Institutes of Health (NIH)', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': '1 R34 NS 123819-01'}, {'name': 'Basnak, Melanie Ailin', 'email': 'melanie.basnak@gmail.com', 'roleName': ['dcite:Author', 'dcite:ContactPerson', 'dcite:DataCollector', 'dcite:Researcher', 'dcite:Conceptualization'], 'schemaKey': 'Person', 'identifier': '0000-0002-4398-747X', 'affiliation': [], 'includeInCitation': True}, {'name': 'Wilson, Rachel', 'email': 'rachel_wilson@hms.harvard.edu', 'roleName': ['dcite:Author', 'dcite:Conceptualization', 'dcite:ContactPerson', 'dcite:Supervision'], 'schemaKey': 'Person', 'identifier': '0000-0001-8573-9266', 'affiliation': [], 'includeInCitation': True}, {'name': 'Howard Hughes Medical Institute', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'contactPoint': [], 'includeInCitation': False}, {'name': 'Harvard Medical School', 'roleName': ['dcite:Affiliation'], 'schemaKey': 'Organization', 'contactPoint': [], 'includeInCitation': False}]
description: This dandiset contains the data associated with "Uncertainty and learning in a biological ring attractor" (Basnak et al., in preparation). It is comprised of two-photon calcium imaging, stimulus variables, and behavioral measurements of fruit flies presented with cues of varying reliability.
assetsSummary: {'species': [{'name': 'Drosophila melanogaster - Fruit fly', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_7227'}], 'approach': [{'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}, {'name': 'behavioral approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 761176077983, 'numberOfFiles': 221, 'numberOfSubjects': 66, 'variableMeasured': ['OpticalChannel', 'SpatialSeries', 'TwoPhotonSeries', 'CompassDirection', 'ProcessingModule', 'PlaneSegmentation', 'ImagingPlane'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'two-photon microscopy technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000289 has 100 NWB files.
14 of these NWB files are of type 1.
10 of these NWB files are of type 2.
76 of these NWB files are of type 3.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/TwoPhotonSeries (TwoPhotonSeries) no description
  Group /acquisition/TwoPhotonSeries/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeries/imaging_plane/device (Device) 
  Group /acquisition/TwoPhotonSeries/imaging_plane/optical_channel (OpticalChannel) 
  file_create_date: ['2022-08-28T14:03:28.743000-04:00']
  Group /general/devices/Device (Device) 
  experimenter: ['Melanie Basnak']
  institution: Harvard University
  Group /general/optophysiology/imaging_plane (ImagingPlane) 
  Group /general/optophysiology/imaging_plane/device (Device) 
  Group /general/optophysiology/imaging_plane/optical_channel (OpticalChannel) 
  Group /general/subject (Subject) 
  identifier: Fly16
  Group /intervals/trials (TimeIntervals) trial data and properties
  Dataset /intervals/trials/cue_gain (VectorData) gain of the visual cue (where 1 = normal gain, 2 = inverted gain | shape = (3,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (3,) | dtype = int64
  Dataset /intervals/trials/start_time (VectorData) start time of trial | shape = (3,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) end of each trial | shape = (3,) | dtype = float64
  Group /processing/behavior (ProcessingModule) contains behavioral data
  Group /processing/behavior/Position (CompassDirection) 
  Group /processing/behavior/Position/SpatialSeries (SpatialSeries) no description
  Group /processing/ophys (ProcessingModule) contains optical physiology data
  Group /processing/ophys/Fluorescence (Fluorescence) 
  Group /processing/ophys/Fluorescence/RoiResponseSeries (RoiResponseSeries) DF/F associated with each of the coordinates of the PB midline
  Dataset /processing/ophys/Fluorescence/RoiResponseSeries/rois (DynamicTableRegion) midline_rois | shape = (27,) | dtype = int8
  Group /processing/ophys/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation (PlaneSegmentation) contains rois
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/id (ElementIdentifiers)  | shape = (27,) | dtype = int8
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/image_mask (VectorData) segmented of the PB midline that the DF/F traces are associated with | shape = (27, 256, 128) | dtype = int32
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/device (Device) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/optical_channel (OpticalChannel) 
  session_description: fly presented with a bright visual cue of varying gain
  session_start_time: 2021-01-27T12:28:34.000000-05:00
  timestamps_reference_time: 2021-01-27T12:28:34.000000-05:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/TwoPhotonSeries (TwoPhotonSeries) no description
  Group /acquisition/TwoPhotonSeries/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeries/imaging_plane/device (Device) 
  Group /acquisition/TwoPhotonSeries/imaging_plane/optical_channel (OpticalChannel) 
  file_create_date: ['2022-08-17T19:03:36.774000-04:00']
  Group /general/devices/Device (Device) 
  experimenter: ['Melanie Basnak']
  institution: Harvard University
  Group /general/optophysiology/imaging_plane (ImagingPlane) 
  Group /general/optophysiology/imaging_plane/device (Device) 
  Group /general/optophysiology/imaging_plane/optical_channel (OpticalChannel) 
  Group /general/subject (Subject) 
  identifier: Fly1
  Group /intervals/trials (TimeIntervals) trial data and properties
  Dataset /intervals/trials/cue_contrast (VectorData) visual cue contrast (where 1 = zero contrast, 2 = low contrast, 3 = high contrast | shape = (6,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (6,) | dtype = int64
  Dataset /intervals/trials/start_time (VectorData) start time of trial | shape = (6,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) end of each trial | shape = (6,) | dtype = float64
  Group /processing/behavior (ProcessingModule) contains behavioral data
  Group /processing/behavior/Position (CompassDirection) 
  Group /processing/behavior/Position/SpatialSeries (SpatialSeries) no description
  Group /processing/ophys (ProcessingModule) contains optical physiology data
  Group /processing/ophys/Fluorescence (Fluorescence) 
  Group /processing/ophys/Fluorescence/RoiResponseSeries (RoiResponseSeries) DF/F associated with each of the coordinates of the PB midline
  Dataset /processing/ophys/Fluorescence/RoiResponseSeries/rois (DynamicTableRegion) midline_rois | shape = (37,) | dtype = int8
  Group /processing/ophys/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation (PlaneSegmentation) contains rois
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/id (ElementIdentifiers)  | shape = (37,) | dtype = int8
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/image_mask (VectorData) points corresponding to the centroids that the DF/F traces are associated with | shape = (37, 256, 128) | dtype = int32
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/device (Device) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/optical_channel (OpticalChannel) 
  session_description: fly presented with visual cues of varying contrast
  session_start_time: 2020-10-19T00:00:00.000000-04:00
  timestamps_reference_time: 2020-10-19T00:00:00.000000-04:00


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/TwoPhotonSeries (TwoPhotonSeries) no description
  Group /acquisition/TwoPhotonSeries/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeries/imaging_plane/device (Device) 
  Group /acquisition/TwoPhotonSeries/imaging_plane/optical_channel (OpticalChannel) 
  file_create_date: ['2022-08-28T19:26:10.093000-04:00']
  Group /general/devices/Device (Device) 
  experimenter: ['Melanie Basnak']
  institution: Harvard University
  Group /general/optophysiology/imaging_plane (ImagingPlane) 
  Group /general/optophysiology/imaging_plane/device (Device) 
  Group /general/optophysiology/imaging_plane/optical_channel (OpticalChannel) 
  Group /general/subject (Subject) 
  identifier: Fly30
  Group /processing/behavior (ProcessingModule) contains behavioral data
  Group /processing/behavior/Position (CompassDirection) 
  Group /processing/behavior/Position/SpatialSeries (SpatialSeries) no description
  Group /processing/ophys (ProcessingModule) contains optical physiology data
  Group /processing/ophys/Fluorescence (Fluorescence) 
  Group /processing/ophys/Fluorescence/RoiResponseSeries (RoiResponseSeries) DF/F associated with each of the coordinates of the PB midline
  Dataset /processing/ophys/Fluorescence/RoiResponseSeries/rois (DynamicTableRegion) midline_rois | shape = (35,) | dtype = int8
  Group /processing/ophys/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation (PlaneSegmentation) contains rois
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/id (ElementIdentifiers)  | shape = (35,) | dtype = int8
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/image_mask (VectorData) segment of the PB midline that the DF/F traces are associated with | shape = (35, 256, 128) | dtype = int32
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/device (Device) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/optical_channel (OpticalChannel) 
  session_description: fly presented with an initial block of a closed-loop visual cue
  session_start_time: 2021-06-17T10:03:39.000000-04:00
  timestamps_reference_time: 2021-06-17T10:03:39.000000-04:00
