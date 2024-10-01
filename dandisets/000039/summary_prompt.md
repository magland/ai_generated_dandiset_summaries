
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000039/0.230223.1216
name: Allen Institute – Contrast tuning in mouse visual cortex with calcium imaging
contributor: [{'name': 'Millman, Dan', 'roleName': ['dcite:ContactPerson', 'dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-6255-6085', 'includeInCitation': True}, {'name': 'Vries, Saskia de', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-3704-3499', 'includeInCitation': True}]
description: A two photon calcium imaging dataset from Allen Institute measuring responses to full-field drifting gratings (approx. 120x90 degrees of visual space) of 8 directions and 6 contrasts (5%, 10%, 20%, 40%, 60%, 80%). Mouse Cre lines expressing GCaMP6f were imaged to record responses of   pyramidal neurons across cortical layers (Cux2: layer 2/3; Rorb: layer 4; Rbp4: layer 5; Ntsr1: layer 6) as well as inhibitory interneurons (Vip and Sst). All experimental sessions took place on the same data collection pipeline as the Allen Brain Observatory (see http://observatory.brain-map.org/visualcoding) and have the same visual stimulus monitor calibration and positioning, two photon imaging systems and image processing pipeline, and running wheel to track locomotion.

 Data are subject to Allen Institute Terms of Use policy, available at: http://www.alleninstitute.org/legal/terms-use/
assetsSummary: {'species': [{'name': 'House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}, {'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}, {'name': 'behavioral approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 22607247880, 'numberOfFiles': 100, 'numberOfSubjects': 32, 'variableMeasured': ['Units', 'PlaneSegmentation', 'TwoPhotonSeries', 'BehavioralTimeSeries'], 'measurementTechnique': [{'name': 'two-photon microscopy technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000039 has 100 NWB files.
10 of these NWB files are of type 1.
34 of these NWB files are of type 2.
13 of these NWB files are of type 3.
43 of these NWB files are of type 4.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2021-09-01T12:25:42.502759-07:00']
  Group /general/devices/CAM2P.1 (Device) 
  Group /general/optophysiology/imaging_plane_1 (ImagingPlane) 
  Group /general/optophysiology/imaging_plane_1/device (Device) 
  Group /general/optophysiology/imaging_plane_1/optical_channel (OpticalChannel) 
  session_id: 682746585
  Group /general/subject (Subject) 
  identifier: 683250025
  Group /intervals/epochs (TimeIntervals) 
  Dataset /intervals/epochs/contrast (VectorData) no description | shape = (720,) | dtype = float64
  Dataset /intervals/epochs/direction (VectorData) no description | shape = (720,) | dtype = float64
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (720,) | dtype = int64
  Dataset /intervals/epochs/spatial_frequency (VectorData) no description | shape = (720,) | dtype = float64
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (720,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (720,) | dtype = float64
  Dataset /intervals/epochs/tags (VectorData) user-defined tags | shape = (720,) | dtype = object
  Dataset /intervals/epochs/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (720,) | dtype = uint16
  Dataset /intervals/epochs/temporal_frequency (VectorData) no description | shape = (720,) | dtype = float64
  Dataset /intervals/epochs/timeseries (VectorData) index into a TimeSeries object | shape = (720,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/epochs/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (720,) | dtype = uint16
  Group /processing/brain_observatory_pipeline (ProcessingModule) contains optical physiology processed data
  Group /processing/brain_observatory_pipeline/Fluorescence (Fluorescence) 
  Group /processing/brain_observatory_pipeline/Fluorescence/DfOverF (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/Fluorescence/DfOverF/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (27,) | dtype = int64
  Group /processing/brain_observatory_pipeline/Fluorescence/demixed_traces (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/Fluorescence/demixed_traces/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (27,) | dtype = int64
  Group /processing/brain_observatory_pipeline/Fluorescence/neuropil_traces (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/Fluorescence/neuropil_traces/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (27,) | dtype = int64
  Group /processing/brain_observatory_pipeline/Fluorescence/raw_traces (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/Fluorescence/raw_traces/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (27,) | dtype = int64
  Group /processing/brain_observatory_pipeline/ImageSegmentation (ImageSegmentation) 
  Group /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation (PlaneSegmentation) Segmentation for imaging plane (de Vries et al., 2019, Nat Neurosci)
  Dataset /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/id (ElementIdentifiers)  | shape = (27,) | dtype = int64
  Dataset /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (27, 512, 512) | dtype = uint8
  Group /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/imaging_plane/device (Device) 
  Group /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/imaging_plane/optical_channel (OpticalChannel) 
  Dataset /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/neuropil_r (VectorData) neuropil_r | shape = (27,) | dtype = float64
  Group /processing/brain_observatory_pipeline/MotionCorrection (TimeSeries) Number of pixels shifts measured during motion correction
  Group /processing/brain_observatory_pipeline/RunningBehavior (BehavioralTimeSeries) 
  Group /processing/brain_observatory_pipeline/RunningBehavior/running_speed (TimeSeries) Speed of the mouse on a rotating wheel
  Group /processing/brain_observatory_pipeline/l0_events (Fluorescence) 
  Group /processing/brain_observatory_pipeline/l0_events/dff_events (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/l0_events/dff_events/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (27,) | dtype = int64
  Group /processing/brain_observatory_pipeline/l0_events/true_false_events (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/l0_events/true_false_events/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (27,) | dtype = int64
  Group /processing/brain_observatory_pipeline/max_project (TwoPhotonSeries) no description
  Group /processing/brain_observatory_pipeline/max_project/imaging_plane (ImagingPlane) 
  Group /processing/brain_observatory_pipeline/max_project/imaging_plane/device (Device) 
  Group /processing/brain_observatory_pipeline/max_project/imaging_plane/optical_channel (OpticalChannel) 
  Group /processing/stimulus (ProcessingModule) Stimulus Times processing
  Group /processing/stimulus/timestamps (TimeSeries) no description
  session_description: OphysSession
  session_start_time: 2018-04-12T16:58:50.822000-07:00
  timestamps_reference_time: 2018-04-12T16:58:50.822000-07:00
  Group /units (Units) 
  Dataset /units/cell_id (VectorData) no description | shape = (27,) | dtype = int64
  Dataset /units/id (ElementIdentifiers)  | shape = (27,) | dtype = int64
  Dataset /units/pos_x (VectorData) no description | shape = (27,) | dtype = int64
  Dataset /units/pos_y (VectorData) no description | shape = (27,) | dtype = int64


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2021-09-01T12:35:49.967004-07:00']
  Group /general/devices/CAM2P.1 (Device) 
  Group /general/optophysiology/imaging_plane_1 (ImagingPlane) 
  Group /general/optophysiology/imaging_plane_1/device (Device) 
  Group /general/optophysiology/imaging_plane_1/optical_channel (OpticalChannel) 
  session_id: 694856258
  Group /general/subject (Subject) 
  identifier: 695087599
  Group /intervals/epochs (TimeIntervals) 
  Dataset /intervals/epochs/contrast (VectorData) no description | shape = (720,) | dtype = float64
  Dataset /intervals/epochs/direction (VectorData) no description | shape = (720,) | dtype = float64
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (720,) | dtype = int64
  Dataset /intervals/epochs/spatial_frequency (VectorData) no description | shape = (720,) | dtype = float64
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (720,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (720,) | dtype = float64
  Dataset /intervals/epochs/tags (VectorData) user-defined tags | shape = (720,) | dtype = object
  Dataset /intervals/epochs/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (720,) | dtype = uint16
  Dataset /intervals/epochs/temporal_frequency (VectorData) no description | shape = (720,) | dtype = float64
  Dataset /intervals/epochs/timeseries (VectorData) index into a TimeSeries object | shape = (720,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/epochs/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (720,) | dtype = uint16
  Group /processing/brain_observatory_pipeline (ProcessingModule) contains optical physiology processed data
  Group /processing/brain_observatory_pipeline/EyeBehavior (BehavioralTimeSeries) 
  Group /processing/brain_observatory_pipeline/EyeBehavior/eye_area (TimeSeries) no description
  Group /processing/brain_observatory_pipeline/EyeBehavior/pupil_area (TimeSeries) no description
  Group /processing/brain_observatory_pipeline/EyeBehavior/screen_coordinates_spherical (TimeSeries) no description
  Group /processing/brain_observatory_pipeline/Fluorescence (Fluorescence) 
  Group /processing/brain_observatory_pipeline/Fluorescence/DfOverF (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/Fluorescence/DfOverF/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (6,) | dtype = int64
  Group /processing/brain_observatory_pipeline/Fluorescence/demixed_traces (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/Fluorescence/demixed_traces/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (6,) | dtype = int64
  Group /processing/brain_observatory_pipeline/Fluorescence/neuropil_traces (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/Fluorescence/neuropil_traces/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (6,) | dtype = int64
  Group /processing/brain_observatory_pipeline/Fluorescence/raw_traces (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/Fluorescence/raw_traces/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (6,) | dtype = int64
  Group /processing/brain_observatory_pipeline/ImageSegmentation (ImageSegmentation) 
  Group /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation (PlaneSegmentation) Segmentation for imaging plane (de Vries et al., 2019, Nat Neurosci)
  Dataset /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/id (ElementIdentifiers)  | shape = (6,) | dtype = int64
  Dataset /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (6, 512, 512) | dtype = uint8
  Group /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/imaging_plane/device (Device) 
  Group /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/imaging_plane/optical_channel (OpticalChannel) 
  Dataset /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/neuropil_r (VectorData) neuropil_r | shape = (6,) | dtype = float64
  Group /processing/brain_observatory_pipeline/MotionCorrection (TimeSeries) Number of pixels shifts measured during motion correction
  Group /processing/brain_observatory_pipeline/RunningBehavior (BehavioralTimeSeries) 
  Group /processing/brain_observatory_pipeline/RunningBehavior/running_speed (TimeSeries) Speed of the mouse on a rotating wheel
  Group /processing/brain_observatory_pipeline/l0_events (Fluorescence) 
  Group /processing/brain_observatory_pipeline/l0_events/dff_events (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/l0_events/dff_events/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (6,) | dtype = int64
  Group /processing/brain_observatory_pipeline/l0_events/true_false_events (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/l0_events/true_false_events/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (6,) | dtype = int64
  Group /processing/brain_observatory_pipeline/max_project (TwoPhotonSeries) no description
  Group /processing/brain_observatory_pipeline/max_project/imaging_plane (ImagingPlane) 
  Group /processing/brain_observatory_pipeline/max_project/imaging_plane/device (Device) 
  Group /processing/brain_observatory_pipeline/max_project/imaging_plane/optical_channel (OpticalChannel) 
  Group /processing/stimulus (ProcessingModule) Stimulus Times processing
  Group /processing/stimulus/timestamps (TimeSeries) no description
  session_description: OphysSession
  session_start_time: 2018-05-07T22:33:55.204000-07:00
  timestamps_reference_time: 2018-05-07T22:33:55.204000-07:00
  Group /units (Units) 
  Dataset /units/cell_id (VectorData) no description | shape = (6,) | dtype = int64
  Dataset /units/id (ElementIdentifiers)  | shape = (6,) | dtype = int64
  Dataset /units/pos_x (VectorData) no description | shape = (6,) | dtype = int64
  Dataset /units/pos_y (VectorData) no description | shape = (6,) | dtype = int64


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2021-09-01T12:26:16.284164-07:00']
  Group /general/devices/CAM2P.2 (Device) 
  Group /general/optophysiology/imaging_plane_1 (ImagingPlane) 
  Group /general/optophysiology/imaging_plane_1/device (Device) 
  Group /general/optophysiology/imaging_plane_1/optical_channel (OpticalChannel) 
  session_id: 696537321
  Group /general/subject (Subject) 
  identifier: 696672708
  Group /intervals/epochs (TimeIntervals) 
  Dataset /intervals/epochs/contrast (VectorData) no description | shape = (720,) | dtype = float64
  Dataset /intervals/epochs/direction (VectorData) no description | shape = (720,) | dtype = float64
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (720,) | dtype = int64
  Dataset /intervals/epochs/spatial_frequency (VectorData) no description | shape = (720,) | dtype = float64
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (720,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (720,) | dtype = float64
  Dataset /intervals/epochs/tags (VectorData) user-defined tags | shape = (720,) | dtype = object
  Dataset /intervals/epochs/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (720,) | dtype = uint16
  Dataset /intervals/epochs/temporal_frequency (VectorData) no description | shape = (720,) | dtype = float64
  Dataset /intervals/epochs/timeseries (VectorData) index into a TimeSeries object | shape = (720,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/epochs/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (720,) | dtype = uint16
  Group /processing/brain_observatory_pipeline (ProcessingModule) contains optical physiology processed data
  Group /processing/brain_observatory_pipeline/Fluorescence (Fluorescence) 
  Group /processing/brain_observatory_pipeline/Fluorescence/DfOverF (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/Fluorescence/DfOverF/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (13,) | dtype = int64
  Group /processing/brain_observatory_pipeline/Fluorescence/demixed_traces (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/Fluorescence/demixed_traces/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (13,) | dtype = int64
  Group /processing/brain_observatory_pipeline/Fluorescence/neuropil_traces (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/Fluorescence/neuropil_traces/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (13,) | dtype = int64
  Group /processing/brain_observatory_pipeline/Fluorescence/raw_traces (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/Fluorescence/raw_traces/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (13,) | dtype = int64
  Group /processing/brain_observatory_pipeline/ImageSegmentation (ImageSegmentation) 
  Group /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation (PlaneSegmentation) Segmentation for imaging plane (de Vries et al., 2019, Nat Neurosci)
  Dataset /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/id (ElementIdentifiers)  | shape = (13,) | dtype = int64
  Dataset /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (13, 512, 512) | dtype = uint8
  Group /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/imaging_plane/device (Device) 
  Group /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/imaging_plane/optical_channel (OpticalChannel) 
  Dataset /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/neuropil_r (VectorData) neuropil_r | shape = (13,) | dtype = float64
  Group /processing/brain_observatory_pipeline/MotionCorrection (TimeSeries) Number of pixels shifts measured during motion correction
  Group /processing/brain_observatory_pipeline/RunningBehavior (BehavioralTimeSeries) 
  Group /processing/brain_observatory_pipeline/RunningBehavior/running_speed (TimeSeries) Speed of the mouse on a rotating wheel
  Group /processing/brain_observatory_pipeline/l0_events (Fluorescence) 
  Group /processing/brain_observatory_pipeline/l0_events/dff_events (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/l0_events/dff_events/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (13,) | dtype = int64
  Group /processing/brain_observatory_pipeline/l0_events/true_false_events (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/l0_events/true_false_events/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (13,) | dtype = int64
  Group /processing/brain_observatory_pipeline/max_project (TwoPhotonSeries) no description
  Group /processing/brain_observatory_pipeline/max_project/imaging_plane (ImagingPlane) 
  Group /processing/brain_observatory_pipeline/max_project/imaging_plane/device (Device) 
  Group /processing/brain_observatory_pipeline/max_project/imaging_plane/optical_channel (OpticalChannel) 
  Group /processing/stimulus (ProcessingModule) Stimulus Times processing
  Group /processing/stimulus/timestamps (TimeSeries) no description
  session_description: OphysSession
  session_start_time: 2018-05-10T22:59:32.830000-07:00
  timestamps_reference_time: 2018-05-10T22:59:32.830000-07:00
  Group /units (Units) 
  Dataset /units/cell_id (VectorData) no description | shape = (13,) | dtype = int64
  Dataset /units/id (ElementIdentifiers)  | shape = (13,) | dtype = int64
  Dataset /units/pos_x (VectorData) no description | shape = (13,) | dtype = int64
  Dataset /units/pos_y (VectorData) no description | shape = (13,) | dtype = int64


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2021-09-01T12:29:36.665642-07:00']
  Group /general/devices/CAM2P.2 (Device) 
  Group /general/optophysiology/imaging_plane_1 (ImagingPlane) 
  Group /general/optophysiology/imaging_plane_1/device (Device) 
  Group /general/optophysiology/imaging_plane_1/optical_channel (OpticalChannel) 
  session_id: 686569087
  Group /general/subject (Subject) 
  identifier: 686912322
  Group /intervals/epochs (TimeIntervals) 
  Dataset /intervals/epochs/contrast (VectorData) no description | shape = (720,) | dtype = float64
  Dataset /intervals/epochs/direction (VectorData) no description | shape = (720,) | dtype = float64
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (720,) | dtype = int64
  Dataset /intervals/epochs/spatial_frequency (VectorData) no description | shape = (720,) | dtype = float64
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (720,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (720,) | dtype = float64
  Dataset /intervals/epochs/tags (VectorData) user-defined tags | shape = (720,) | dtype = object
  Dataset /intervals/epochs/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (720,) | dtype = uint16
  Dataset /intervals/epochs/temporal_frequency (VectorData) no description | shape = (720,) | dtype = float64
  Dataset /intervals/epochs/timeseries (VectorData) index into a TimeSeries object | shape = (720,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/epochs/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (720,) | dtype = uint16
  Group /processing/brain_observatory_pipeline (ProcessingModule) contains optical physiology processed data
  Group /processing/brain_observatory_pipeline/EyeBehavior (BehavioralTimeSeries) 
  Group /processing/brain_observatory_pipeline/EyeBehavior/eye_area (TimeSeries) no description
  Group /processing/brain_observatory_pipeline/EyeBehavior/pupil_area (TimeSeries) no description
  Group /processing/brain_observatory_pipeline/EyeBehavior/screen_coordinates_spherical (TimeSeries) no description
  Group /processing/brain_observatory_pipeline/Fluorescence (Fluorescence) 
  Group /processing/brain_observatory_pipeline/Fluorescence/DfOverF (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/Fluorescence/DfOverF/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (26,) | dtype = int64
  Group /processing/brain_observatory_pipeline/Fluorescence/demixed_traces (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/Fluorescence/demixed_traces/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (26,) | dtype = int64
  Group /processing/brain_observatory_pipeline/Fluorescence/neuropil_traces (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/Fluorescence/neuropil_traces/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (26,) | dtype = int64
  Group /processing/brain_observatory_pipeline/Fluorescence/raw_traces (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/Fluorescence/raw_traces/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (26,) | dtype = int64
  Group /processing/brain_observatory_pipeline/ImageSegmentation (ImageSegmentation) 
  Group /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation (PlaneSegmentation) Segmentation for imaging plane (de Vries et al., 2019, Nat Neurosci)
  Dataset /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/id (ElementIdentifiers)  | shape = (26,) | dtype = int64
  Dataset /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (26, 512, 512) | dtype = uint8
  Group /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/imaging_plane/device (Device) 
  Group /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/imaging_plane/optical_channel (OpticalChannel) 
  Dataset /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/neuropil_r (VectorData) neuropil_r | shape = (26,) | dtype = float64
  Group /processing/brain_observatory_pipeline/MotionCorrection (TimeSeries) Number of pixels shifts measured during motion correction
  Group /processing/brain_observatory_pipeline/RunningBehavior (BehavioralTimeSeries) 
  Group /processing/brain_observatory_pipeline/RunningBehavior/running_speed (TimeSeries) Speed of the mouse on a rotating wheel
  Group /processing/brain_observatory_pipeline/l0_events (Fluorescence) 
  Group /processing/brain_observatory_pipeline/l0_events/dff_events (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/l0_events/dff_events/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (26,) | dtype = int64
  Group /processing/brain_observatory_pipeline/l0_events/true_false_events (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/l0_events/true_false_events/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (26,) | dtype = int64
  Group /processing/brain_observatory_pipeline/max_project (TwoPhotonSeries) no description
  Group /processing/brain_observatory_pipeline/max_project/imaging_plane (ImagingPlane) 
  Group /processing/brain_observatory_pipeline/max_project/imaging_plane/device (Device) 
  Group /processing/brain_observatory_pipeline/max_project/imaging_plane/optical_channel (OpticalChannel) 
  Group /processing/stimulus (ProcessingModule) Stimulus Times processing
  Group /processing/stimulus/timestamps (TimeSeries) no description
  session_description: OphysSession
  session_start_time: 2018-04-19T17:23:04.009000-07:00
  timestamps_reference_time: 2018-04-19T17:23:04.009000-07:00
  Group /units (Units) 
  Dataset /units/cell_id (VectorData) no description | shape = (26,) | dtype = int64
  Dataset /units/id (ElementIdentifiers)  | shape = (26,) | dtype = int64
  Dataset /units/pos_x (VectorData) no description | shape = (26,) | dtype = int64
  Dataset /units/pos_y (VectorData) no description | shape = (26,) | dtype = int64
