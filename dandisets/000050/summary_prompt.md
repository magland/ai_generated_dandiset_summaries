
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000050/draft
name: Allen Institute - Run Tuning in the Mouse Visual Cortex
description: Allen Institute for Brain Science, MindScope Project.
assetsSummary: {'species': [{'name': 'House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}, {'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}, {'name': 'behavioral approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 26372579632, 'numberOfFiles': 56, 'numberOfSubjects': 18, 'variableMeasured': ['TwoPhotonSeries', 'Units', 'PlaneSegmentation', 'BehavioralTimeSeries'], 'measurementTechnique': [{'name': 'two-photon microscopy technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000050 has 56 NWB files.
4 of these NWB files are of type 1.
19 of these NWB files are of type 2.
6 of these NWB files are of type 3.
27 of these NWB files are of type 4.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2020-12-03T12:56:39.137006-08:00']
  Group /general/devices/CAM2P.1 (Device) 
  Group /general/optophysiology/imaging_plane_1 (ImagingPlane) 
  Group /general/optophysiology/imaging_plane_1/device (Device) 
  Group /general/optophysiology/imaging_plane_1/optical_channel (OpticalChannel) 
  session_id: 684856233
  Group /general/subject (Subject) 
  identifier: 685495363
  Group /intervals/epochs (TimeIntervals) 
  Dataset /intervals/epochs/direction (VectorData) no description | shape = (1207,) | dtype = float64
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (1207,) | dtype = int64
  Dataset /intervals/epochs/spatial_frequency (VectorData) no description | shape = (1207,) | dtype = float64
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (1207,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1207,) | dtype = float64
  Dataset /intervals/epochs/tags (VectorData) user-defined tags | shape = (1207,) | dtype = object
  Dataset /intervals/epochs/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (1207,) | dtype = uint16
  Dataset /intervals/epochs/temporal_frequency (VectorData) no description | shape = (1207,) | dtype = float64
  Dataset /intervals/epochs/timeseries (VectorData) index into a TimeSeries object | shape = (1207,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/epochs/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (1207,) | dtype = uint16
  Group /processing/brain_observatory_pipeline (ProcessingModule) contains optical physiology processed data
  Group /processing/brain_observatory_pipeline/Fluorescence (Fluorescence) 
  Group /processing/brain_observatory_pipeline/Fluorescence/DfOverF (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/Fluorescence/DfOverF/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (15,) | dtype = int64
  Group /processing/brain_observatory_pipeline/Fluorescence/demixed_traces (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/Fluorescence/demixed_traces/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (15,) | dtype = int64
  Group /processing/brain_observatory_pipeline/Fluorescence/neuropil_traces (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/Fluorescence/neuropil_traces/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (15,) | dtype = int64
  Group /processing/brain_observatory_pipeline/Fluorescence/raw_traces (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/Fluorescence/raw_traces/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (15,) | dtype = int64
  Group /processing/brain_observatory_pipeline/ImageSegmentation (ImageSegmentation) 
  Group /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation (PlaneSegmentation) Segmentation for imaging plane (de Vries et al., 2019, Nat Neurosci)
  Dataset /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/id (ElementIdentifiers)  | shape = (15,) | dtype = int64
  Dataset /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (15, 512, 512) | dtype = uint8
  Group /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/imaging_plane/device (Device) 
  Group /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/imaging_plane/optical_channel (OpticalChannel) 
  Dataset /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/neuropil_r (VectorData) neuropil_r | shape = (15,) | dtype = float64
  Group /processing/brain_observatory_pipeline/MotionCorrection (TimeSeries) Number of pixels shifts measured during motion correction
  Group /processing/brain_observatory_pipeline/RunningBehavior (BehavioralTimeSeries) 
  Group /processing/brain_observatory_pipeline/RunningBehavior/running_speed (TimeSeries) Speed of the mouse on a rotating wheel
  Group /processing/brain_observatory_pipeline/l0_events (Fluorescence) 
  Group /processing/brain_observatory_pipeline/l0_events/dff_events (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/l0_events/dff_events/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (15,) | dtype = int64
  Group /processing/brain_observatory_pipeline/l0_events/true_false_events (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/l0_events/true_false_events/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (15,) | dtype = int64
  Group /processing/brain_observatory_pipeline/max_project (TwoPhotonSeries) no description
  Group /processing/brain_observatory_pipeline/max_project/imaging_plane (ImagingPlane) 
  Group /processing/brain_observatory_pipeline/max_project/imaging_plane/device (Device) 
  Group /processing/brain_observatory_pipeline/max_project/imaging_plane/optical_channel (OpticalChannel) 
  Group /processing/stimulus (ProcessingModule) Stimulus Times processing
  Group /processing/stimulus/timestamps (TimeSeries) no description
  session_description: OphysSession
  session_start_time: 2018-04-16T17:49:19.066000-07:00
  timestamps_reference_time: 2018-04-16T17:49:19.066000-07:00
  Group /units (Units) 
  Dataset /units/cell_id (VectorData) no description | shape = (15,) | dtype = int64
  Dataset /units/id (ElementIdentifiers)  | shape = (15,) | dtype = int64
  Dataset /units/pos_x (VectorData) no description | shape = (15,) | dtype = int64
  Dataset /units/pos_y (VectorData) no description | shape = (15,) | dtype = int64


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2020-12-03T12:57:27.805734-08:00']
  Group /general/devices/CAM2P.1 (Device) 
  Group /general/optophysiology/imaging_plane_1 (ImagingPlane) 
  Group /general/optophysiology/imaging_plane_1/device (Device) 
  Group /general/optophysiology/imaging_plane_1/optical_channel (OpticalChannel) 
  session_id: 693508136
  Group /general/subject (Subject) 
  identifier: 693876096
  Group /intervals/epochs (TimeIntervals) 
  Dataset /intervals/epochs/direction (VectorData) no description | shape = (1207,) | dtype = float64
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (1207,) | dtype = int64
  Dataset /intervals/epochs/spatial_frequency (VectorData) no description | shape = (1207,) | dtype = float64
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (1207,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1207,) | dtype = float64
  Dataset /intervals/epochs/tags (VectorData) user-defined tags | shape = (1207,) | dtype = object
  Dataset /intervals/epochs/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (1207,) | dtype = uint16
  Dataset /intervals/epochs/temporal_frequency (VectorData) no description | shape = (1207,) | dtype = float64
  Dataset /intervals/epochs/timeseries (VectorData) index into a TimeSeries object | shape = (1207,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/epochs/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (1207,) | dtype = uint16
  Group /processing/brain_observatory_pipeline (ProcessingModule) contains optical physiology processed data
  Group /processing/brain_observatory_pipeline/EyeBehavior (BehavioralTimeSeries) 
  Group /processing/brain_observatory_pipeline/EyeBehavior/eye_area (TimeSeries) no description
  Group /processing/brain_observatory_pipeline/EyeBehavior/pupil_area (TimeSeries) no description
  Group /processing/brain_observatory_pipeline/EyeBehavior/screen_coordinates_spherical (TimeSeries) no description
  Group /processing/brain_observatory_pipeline/Fluorescence (Fluorescence) 
  Group /processing/brain_observatory_pipeline/Fluorescence/DfOverF (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/Fluorescence/DfOverF/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (14,) | dtype = int64
  Group /processing/brain_observatory_pipeline/Fluorescence/demixed_traces (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/Fluorescence/demixed_traces/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (14,) | dtype = int64
  Group /processing/brain_observatory_pipeline/Fluorescence/neuropil_traces (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/Fluorescence/neuropil_traces/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (14,) | dtype = int64
  Group /processing/brain_observatory_pipeline/Fluorescence/raw_traces (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/Fluorescence/raw_traces/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (14,) | dtype = int64
  Group /processing/brain_observatory_pipeline/ImageSegmentation (ImageSegmentation) 
  Group /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation (PlaneSegmentation) Segmentation for imaging plane (de Vries et al., 2019, Nat Neurosci)
  Dataset /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/id (ElementIdentifiers)  | shape = (14,) | dtype = int64
  Dataset /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (14, 512, 512) | dtype = uint8
  Group /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/imaging_plane/device (Device) 
  Group /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/imaging_plane/optical_channel (OpticalChannel) 
  Dataset /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/neuropil_r (VectorData) neuropil_r | shape = (14,) | dtype = float64
  Group /processing/brain_observatory_pipeline/MotionCorrection (TimeSeries) Number of pixels shifts measured during motion correction
  Group /processing/brain_observatory_pipeline/RunningBehavior (BehavioralTimeSeries) 
  Group /processing/brain_observatory_pipeline/RunningBehavior/running_speed (TimeSeries) Speed of the mouse on a rotating wheel
  Group /processing/brain_observatory_pipeline/l0_events (Fluorescence) 
  Group /processing/brain_observatory_pipeline/l0_events/dff_events (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/l0_events/dff_events/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (14,) | dtype = int64
  Group /processing/brain_observatory_pipeline/l0_events/true_false_events (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/l0_events/true_false_events/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (14,) | dtype = int64
  Group /processing/brain_observatory_pipeline/max_project (TwoPhotonSeries) no description
  Group /processing/brain_observatory_pipeline/max_project/imaging_plane (ImagingPlane) 
  Group /processing/brain_observatory_pipeline/max_project/imaging_plane/device (Device) 
  Group /processing/brain_observatory_pipeline/max_project/imaging_plane/optical_channel (OpticalChannel) 
  Group /processing/stimulus (ProcessingModule) Stimulus Times processing
  Group /processing/stimulus/timestamps (TimeSeries) no description
  session_description: OphysSession
  session_start_time: 2018-05-03T17:30:53.322000-07:00
  timestamps_reference_time: 2018-05-03T17:30:53.322000-07:00
  Group /units (Units) 
  Dataset /units/cell_id (VectorData) no description | shape = (14,) | dtype = int64
  Dataset /units/id (ElementIdentifiers)  | shape = (14,) | dtype = int64
  Dataset /units/pos_x (VectorData) no description | shape = (14,) | dtype = int64
  Dataset /units/pos_y (VectorData) no description | shape = (14,) | dtype = int64


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2020-12-07T11:28:38.108138-08:00']
  Group /general/devices/CAM2P.2 (Device) 
  Group /general/optophysiology/imaging_plane_1 (ImagingPlane) 
  Group /general/optophysiology/imaging_plane_1/device (Device) 
  Group /general/optophysiology/imaging_plane_1/optical_channel (OpticalChannel) 
  session_id: 773939791
  Group /general/subject (Subject) 
  identifier: 774438172
  Group /intervals/epochs (TimeIntervals) 
  Dataset /intervals/epochs/direction (VectorData) no description | shape = (1207,) | dtype = float64
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (1207,) | dtype = int64
  Dataset /intervals/epochs/spatial_frequency (VectorData) no description | shape = (1207,) | dtype = float64
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (1207,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1207,) | dtype = float64
  Dataset /intervals/epochs/tags (VectorData) user-defined tags | shape = (1207,) | dtype = object
  Dataset /intervals/epochs/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (1207,) | dtype = uint16
  Dataset /intervals/epochs/temporal_frequency (VectorData) no description | shape = (1207,) | dtype = float64
  Dataset /intervals/epochs/timeseries (VectorData) index into a TimeSeries object | shape = (1207,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/epochs/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (1207,) | dtype = uint16
  Group /processing/brain_observatory_pipeline (ProcessingModule) contains optical physiology processed data
  Group /processing/brain_observatory_pipeline/Fluorescence (Fluorescence) 
  Group /processing/brain_observatory_pipeline/Fluorescence/DfOverF (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/Fluorescence/DfOverF/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (78,) | dtype = int64
  Group /processing/brain_observatory_pipeline/Fluorescence/demixed_traces (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/Fluorescence/demixed_traces/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (78,) | dtype = int64
  Group /processing/brain_observatory_pipeline/Fluorescence/neuropil_traces (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/Fluorescence/neuropil_traces/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (78,) | dtype = int64
  Group /processing/brain_observatory_pipeline/Fluorescence/raw_traces (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/Fluorescence/raw_traces/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (78,) | dtype = int64
  Group /processing/brain_observatory_pipeline/ImageSegmentation (ImageSegmentation) 
  Group /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation (PlaneSegmentation) Segmentation for imaging plane (de Vries et al., 2019, Nat Neurosci)
  Dataset /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/id (ElementIdentifiers)  | shape = (78,) | dtype = int64
  Dataset /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (78, 512, 512) | dtype = uint8
  Group /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/imaging_plane/device (Device) 
  Group /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/imaging_plane/optical_channel (OpticalChannel) 
  Dataset /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/neuropil_r (VectorData) neuropil_r | shape = (78,) | dtype = float64
  Group /processing/brain_observatory_pipeline/MotionCorrection (TimeSeries) Number of pixels shifts measured during motion correction
  Group /processing/brain_observatory_pipeline/RunningBehavior (BehavioralTimeSeries) 
  Group /processing/brain_observatory_pipeline/RunningBehavior/running_speed (TimeSeries) Speed of the mouse on a rotating wheel
  Group /processing/brain_observatory_pipeline/l0_events (Fluorescence) 
  Group /processing/brain_observatory_pipeline/l0_events/dff_events (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/l0_events/dff_events/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (78,) | dtype = int64
  Group /processing/brain_observatory_pipeline/l0_events/true_false_events (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/l0_events/true_false_events/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (78,) | dtype = int64
  Group /processing/brain_observatory_pipeline/max_project (TwoPhotonSeries) no description
  Group /processing/brain_observatory_pipeline/max_project/imaging_plane (ImagingPlane) 
  Group /processing/brain_observatory_pipeline/max_project/imaging_plane/device (Device) 
  Group /processing/brain_observatory_pipeline/max_project/imaging_plane/optical_channel (OpticalChannel) 
  Group /processing/stimulus (ProcessingModule) Stimulus Times processing
  Group /processing/stimulus/timestamps (TimeSeries) no description
  session_description: OphysSession
  session_start_time: 2018-11-06T16:13:26.240000-08:00
  timestamps_reference_time: 2018-11-06T16:13:26.240000-08:00
  Group /units (Units) 
  Dataset /units/cell_id (VectorData) no description | shape = (78,) | dtype = int64
  Dataset /units/id (ElementIdentifiers)  | shape = (78,) | dtype = int64
  Dataset /units/pos_x (VectorData) no description | shape = (78,) | dtype = int64
  Dataset /units/pos_y (VectorData) no description | shape = (78,) | dtype = int64


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2020-12-07T11:24:51.026896-08:00']
  Group /general/devices/CAM2P.2 (Device) 
  Group /general/optophysiology/imaging_plane_1 (ImagingPlane) 
  Group /general/optophysiology/imaging_plane_1/device (Device) 
  Group /general/optophysiology/imaging_plane_1/optical_channel (OpticalChannel) 
  session_id: 722975630
  Group /general/subject (Subject) 
  identifier: 723148283
  Group /intervals/epochs (TimeIntervals) 
  Dataset /intervals/epochs/direction (VectorData) no description | shape = (1207,) | dtype = float64
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (1207,) | dtype = int64
  Dataset /intervals/epochs/spatial_frequency (VectorData) no description | shape = (1207,) | dtype = float64
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (1207,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1207,) | dtype = float64
  Dataset /intervals/epochs/tags (VectorData) user-defined tags | shape = (1207,) | dtype = object
  Dataset /intervals/epochs/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (1207,) | dtype = uint16
  Dataset /intervals/epochs/temporal_frequency (VectorData) no description | shape = (1207,) | dtype = float64
  Dataset /intervals/epochs/timeseries (VectorData) index into a TimeSeries object | shape = (1207,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/epochs/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (1207,) | dtype = uint16
  Group /processing/brain_observatory_pipeline (ProcessingModule) contains optical physiology processed data
  Group /processing/brain_observatory_pipeline/EyeBehavior (BehavioralTimeSeries) 
  Group /processing/brain_observatory_pipeline/EyeBehavior/eye_area (TimeSeries) no description
  Group /processing/brain_observatory_pipeline/EyeBehavior/pupil_area (TimeSeries) no description
  Group /processing/brain_observatory_pipeline/EyeBehavior/screen_coordinates_spherical (TimeSeries) no description
  Group /processing/brain_observatory_pipeline/Fluorescence (Fluorescence) 
  Group /processing/brain_observatory_pipeline/Fluorescence/DfOverF (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/Fluorescence/DfOverF/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (86,) | dtype = int64
  Group /processing/brain_observatory_pipeline/Fluorescence/demixed_traces (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/Fluorescence/demixed_traces/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (86,) | dtype = int64
  Group /processing/brain_observatory_pipeline/Fluorescence/neuropil_traces (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/Fluorescence/neuropil_traces/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (86,) | dtype = int64
  Group /processing/brain_observatory_pipeline/Fluorescence/raw_traces (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/Fluorescence/raw_traces/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (86,) | dtype = int64
  Group /processing/brain_observatory_pipeline/ImageSegmentation (ImageSegmentation) 
  Group /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation (PlaneSegmentation) Segmentation for imaging plane (de Vries et al., 2019, Nat Neurosci)
  Dataset /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/id (ElementIdentifiers)  | shape = (86,) | dtype = int64
  Dataset /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (86, 512, 512) | dtype = uint8
  Group /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/imaging_plane/device (Device) 
  Group /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/imaging_plane/optical_channel (OpticalChannel) 
  Dataset /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/neuropil_r (VectorData) neuropil_r | shape = (86,) | dtype = float64
  Group /processing/brain_observatory_pipeline/MotionCorrection (TimeSeries) Number of pixels shifts measured during motion correction
  Group /processing/brain_observatory_pipeline/RunningBehavior (BehavioralTimeSeries) 
  Group /processing/brain_observatory_pipeline/RunningBehavior/running_speed (TimeSeries) Speed of the mouse on a rotating wheel
  Group /processing/brain_observatory_pipeline/l0_events (Fluorescence) 
  Group /processing/brain_observatory_pipeline/l0_events/dff_events (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/l0_events/dff_events/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (86,) | dtype = int64
  Group /processing/brain_observatory_pipeline/l0_events/true_false_events (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/l0_events/true_false_events/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (86,) | dtype = int64
  Group /processing/brain_observatory_pipeline/max_project (TwoPhotonSeries) no description
  Group /processing/brain_observatory_pipeline/max_project/imaging_plane (ImagingPlane) 
  Group /processing/brain_observatory_pipeline/max_project/imaging_plane/device (Device) 
  Group /processing/brain_observatory_pipeline/max_project/imaging_plane/optical_channel (OpticalChannel) 
  Group /processing/stimulus (ProcessingModule) Stimulus Times processing
  Group /processing/stimulus/timestamps (TimeSeries) no description
  session_description: OphysSession
  session_start_time: 2018-07-21T00:05:50.764000-07:00
  timestamps_reference_time: 2018-07-21T00:05:50.764000-07:00
  Group /units (Units) 
  Dataset /units/cell_id (VectorData) no description | shape = (86,) | dtype = int64
  Dataset /units/id (ElementIdentifiers)  | shape = (86,) | dtype = int64
  Dataset /units/pos_x (VectorData) no description | shape = (86,) | dtype = int64
  Dataset /units/pos_y (VectorData) no description | shape = (86,) | dtype = int64
