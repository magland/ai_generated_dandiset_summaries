
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000049/0.230223.1424
name: Allen Institute – TF x SF tuning in mouse visual cortex with calcium imaging
contributor: [{'name': 'Millman, Daniel', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-6255-6085', 'affiliation': [], 'includeInCitation': True}, {'name': 'de Vries, Saskia', 'email': 'saskiad@alleninstitute.org', 'roleName': ['dcite:ContactPerson', 'dcite:ProjectLeader'], 'schemaKey': 'Person', 'identifier': '0000-0002-3704-3499', 'affiliation': [], 'includeInCitation': True}]
description: A two photon calcium imaging dataset from Allen Institute measuring responses to full-field drifting gratings (approx. 120x90 degrees of visual space) moving in 4 different directions, at 5 spatial frequencies (0.02, 0.04, 0.08, 0.16, 0.32 cpd), and 5 temporal frequencies (0.5, 1, 2, 4, 8 Hz). The ratio of TF/SF is speed (deg/sec) and the extent to which visual neurons exhibit speed tuning has been shown to vary across some cortical areas (Andermann et al. 2011).
Mouse Cre lines expressing GCaMPf were imaged to record responses of pyramidal neurons across cortical layers (Cux2: layer 2/3; Rorb: layer 4; Rbp4: layer 5; Ntsr1: layer 6) as well as somatostatin inhibitory interneurons (Sst). All Cre lines were imaged in VISp, and some (Cux2 and Sst) were also imaged in VISl, VISal, VISpm, VISam, and VISrl. All experimental sessions took place on the same data collection pipeline as the Allen Brain Observatory (see de Vries, Lecoq, Buice et al. 2020) and have the same visual stimulus monitor calibration and positioning, two photon imaging systems and image processing pipeline, and running wheel to track locomotion. Data are subject to Allen Institute Terms of Use policy, available at: http://www.alleninstitute.org/legal/terms-use/
assetsSummary: {'species': [{'name': 'House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}, {'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}, {'name': 'behavioral approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 22211886496, 'numberOfFiles': 78, 'numberOfSubjects': 27, 'variableMeasured': ['TwoPhotonSeries', 'Units', 'PlaneSegmentation', 'BehavioralTimeSeries'], 'measurementTechnique': [{'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'two-photon microscopy technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000049 has 78 NWB files.
18 of these NWB files are of type 1.
43 of these NWB files are of type 2.
9 of these NWB files are of type 3.
8 of these NWB files are of type 4.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2020-12-03T12:35:38.075669-08:00']
  Group /general/devices/CAM2P.1 (Device) 
  Group /general/optophysiology/imaging_plane_1 (ImagingPlane) 
  Group /general/optophysiology/imaging_plane_1/device (Device) 
  Group /general/optophysiology/imaging_plane_1/optical_channel (OpticalChannel) 
  session_id: 681698752
  Group /general/subject (Subject) 
  identifier: 682731703
  Group /intervals/epochs (TimeIntervals) 
  Dataset /intervals/epochs/contrast (VectorData) no description | shape = (1212,) | dtype = float64
  Dataset /intervals/epochs/direction (VectorData) no description | shape = (1212,) | dtype = float64
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (1212,) | dtype = int64
  Dataset /intervals/epochs/spatial_frequency (VectorData) no description | shape = (1212,) | dtype = float64
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (1212,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1212,) | dtype = float64
  Dataset /intervals/epochs/tags (VectorData) user-defined tags | shape = (1212,) | dtype = object
  Dataset /intervals/epochs/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (1212,) | dtype = uint16
  Dataset /intervals/epochs/temporal_frequency (VectorData) no description | shape = (1212,) | dtype = float64
  Dataset /intervals/epochs/timeseries (VectorData) index into a TimeSeries object | shape = (1212,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/epochs/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (1212,) | dtype = uint16
  Group /processing/brain_observatory_pipeline (ProcessingModule) contains optical physiology processed data
  Group /processing/brain_observatory_pipeline/EyeBehavior (BehavioralTimeSeries) 
  Group /processing/brain_observatory_pipeline/EyeBehavior/eye_area (TimeSeries) no description
  Group /processing/brain_observatory_pipeline/EyeBehavior/pupil_area (TimeSeries) no description
  Group /processing/brain_observatory_pipeline/EyeBehavior/screen_coordinates_spherical (TimeSeries) no description
  Group /processing/brain_observatory_pipeline/Fluorescence (Fluorescence) 
  Group /processing/brain_observatory_pipeline/Fluorescence/DfOverF (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/Fluorescence/DfOverF/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (22,) | dtype = int64
  Group /processing/brain_observatory_pipeline/Fluorescence/demixed_traces (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/Fluorescence/demixed_traces/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (22,) | dtype = int64
  Group /processing/brain_observatory_pipeline/Fluorescence/neuropil_traces (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/Fluorescence/neuropil_traces/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (22,) | dtype = int64
  Group /processing/brain_observatory_pipeline/Fluorescence/raw_traces (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/Fluorescence/raw_traces/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (22,) | dtype = int64
  Group /processing/brain_observatory_pipeline/ImageSegmentation (ImageSegmentation) 
  Group /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation (PlaneSegmentation) Segmentation for imaging plane (de Vries et al., 2019, Nat Neurosci)
  Dataset /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/id (ElementIdentifiers)  | shape = (22,) | dtype = int64
  Dataset /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (22, 512, 512) | dtype = uint8
  Group /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/imaging_plane/device (Device) 
  Group /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/imaging_plane/optical_channel (OpticalChannel) 
  Dataset /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/neuropil_r (VectorData) neuropil_r | shape = (22,) | dtype = float64
  Group /processing/brain_observatory_pipeline/MotionCorrection (TimeSeries) Number of pixels shifts measured during motion correction
  Group /processing/brain_observatory_pipeline/RunningBehavior (BehavioralTimeSeries) 
  Group /processing/brain_observatory_pipeline/RunningBehavior/running_speed (TimeSeries) Speed of the mouse on a rotating wheel
  Group /processing/brain_observatory_pipeline/l0_events (Fluorescence) 
  Group /processing/brain_observatory_pipeline/l0_events/dff_events (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/l0_events/dff_events/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (22,) | dtype = int64
  Group /processing/brain_observatory_pipeline/l0_events/true_false_events (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/l0_events/true_false_events/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (22,) | dtype = int64
  Group /processing/brain_observatory_pipeline/max_project (TwoPhotonSeries) no description
  Group /processing/brain_observatory_pipeline/max_project/imaging_plane (ImagingPlane) 
  Group /processing/brain_observatory_pipeline/max_project/imaging_plane/device (Device) 
  Group /processing/brain_observatory_pipeline/max_project/imaging_plane/optical_channel (OpticalChannel) 
  Group /processing/stimulus (ProcessingModule) Stimulus Times processing
  Group /processing/stimulus/timestamps (TimeSeries) no description
  session_description: OphysSession
  session_start_time: 2018-04-11T17:51:00.070000-07:00
  timestamps_reference_time: 2018-04-11T17:51:00.070000-07:00
  Group /units (Units) 
  Dataset /units/cell_id (VectorData) no description | shape = (22,) | dtype = int64
  Dataset /units/id (ElementIdentifiers)  | shape = (22,) | dtype = int64
  Dataset /units/pos_x (VectorData) no description | shape = (22,) | dtype = int64
  Dataset /units/pos_y (VectorData) no description | shape = (22,) | dtype = int64


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2020-12-03T12:35:00.246823-08:00']
  Group /general/devices/CAM2P.2 (Device) 
  Group /general/optophysiology/imaging_plane_1 (ImagingPlane) 
  Group /general/optophysiology/imaging_plane_1/device (Device) 
  Group /general/optophysiology/imaging_plane_1/optical_channel (OpticalChannel) 
  session_id: 686708257
  Group /general/subject (Subject) 
  identifier: 686916414
  Group /intervals/epochs (TimeIntervals) 
  Dataset /intervals/epochs/contrast (VectorData) no description | shape = (1212,) | dtype = float64
  Dataset /intervals/epochs/direction (VectorData) no description | shape = (1212,) | dtype = float64
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (1212,) | dtype = int64
  Dataset /intervals/epochs/spatial_frequency (VectorData) no description | shape = (1212,) | dtype = float64
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (1212,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1212,) | dtype = float64
  Dataset /intervals/epochs/tags (VectorData) user-defined tags | shape = (1212,) | dtype = object
  Dataset /intervals/epochs/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (1212,) | dtype = uint16
  Dataset /intervals/epochs/temporal_frequency (VectorData) no description | shape = (1212,) | dtype = float64
  Dataset /intervals/epochs/timeseries (VectorData) index into a TimeSeries object | shape = (1212,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/epochs/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (1212,) | dtype = uint16
  Group /processing/brain_observatory_pipeline (ProcessingModule) contains optical physiology processed data
  Group /processing/brain_observatory_pipeline/EyeBehavior (BehavioralTimeSeries) 
  Group /processing/brain_observatory_pipeline/EyeBehavior/eye_area (TimeSeries) no description
  Group /processing/brain_observatory_pipeline/EyeBehavior/pupil_area (TimeSeries) no description
  Group /processing/brain_observatory_pipeline/EyeBehavior/screen_coordinates_spherical (TimeSeries) no description
  Group /processing/brain_observatory_pipeline/Fluorescence (Fluorescence) 
  Group /processing/brain_observatory_pipeline/Fluorescence/DfOverF (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/Fluorescence/DfOverF/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (9,) | dtype = int64
  Group /processing/brain_observatory_pipeline/Fluorescence/demixed_traces (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/Fluorescence/demixed_traces/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (9,) | dtype = int64
  Group /processing/brain_observatory_pipeline/Fluorescence/neuropil_traces (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/Fluorescence/neuropil_traces/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (9,) | dtype = int64
  Group /processing/brain_observatory_pipeline/Fluorescence/raw_traces (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/Fluorescence/raw_traces/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (9,) | dtype = int64
  Group /processing/brain_observatory_pipeline/ImageSegmentation (ImageSegmentation) 
  Group /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation (PlaneSegmentation) Segmentation for imaging plane (de Vries et al., 2019, Nat Neurosci)
  Dataset /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/id (ElementIdentifiers)  | shape = (9,) | dtype = int64
  Dataset /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (9, 512, 512) | dtype = uint8
  Group /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/imaging_plane/device (Device) 
  Group /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/imaging_plane/optical_channel (OpticalChannel) 
  Dataset /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/neuropil_r (VectorData) neuropil_r | shape = (9,) | dtype = float64
  Group /processing/brain_observatory_pipeline/MotionCorrection (TimeSeries) Number of pixels shifts measured during motion correction
  Group /processing/brain_observatory_pipeline/RunningBehavior (BehavioralTimeSeries) 
  Group /processing/brain_observatory_pipeline/RunningBehavior/running_speed (TimeSeries) Speed of the mouse on a rotating wheel
  Group /processing/brain_observatory_pipeline/l0_events (Fluorescence) 
  Group /processing/brain_observatory_pipeline/l0_events/dff_events (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/l0_events/dff_events/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (9,) | dtype = int64
  Group /processing/brain_observatory_pipeline/l0_events/true_false_events (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/l0_events/true_false_events/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (9,) | dtype = int64
  Group /processing/brain_observatory_pipeline/max_project (TwoPhotonSeries) no description
  Group /processing/brain_observatory_pipeline/max_project/imaging_plane (ImagingPlane) 
  Group /processing/brain_observatory_pipeline/max_project/imaging_plane/device (Device) 
  Group /processing/brain_observatory_pipeline/max_project/imaging_plane/optical_channel (OpticalChannel) 
  Group /processing/stimulus (ProcessingModule) Stimulus Times processing
  Group /processing/stimulus/timestamps (TimeSeries) no description
  session_description: OphysSession
  session_start_time: 2018-04-19T20:47:18.661000-07:00
  timestamps_reference_time: 2018-04-19T20:47:18.661000-07:00
  Group /units (Units) 
  Dataset /units/cell_id (VectorData) no description | shape = (9,) | dtype = int64
  Dataset /units/id (ElementIdentifiers)  | shape = (9,) | dtype = int64
  Dataset /units/pos_x (VectorData) no description | shape = (9,) | dtype = int64
  Dataset /units/pos_y (VectorData) no description | shape = (9,) | dtype = int64


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2020-12-03T12:34:41.559696-08:00']
  Group /general/devices/CAM2P.2 (Device) 
  Group /general/optophysiology/imaging_plane_1 (ImagingPlane) 
  Group /general/optophysiology/imaging_plane_1/device (Device) 
  Group /general/optophysiology/imaging_plane_1/optical_channel (OpticalChannel) 
  session_id: 687293842
  Group /general/subject (Subject) 
  identifier: 687497691
  Group /intervals/epochs (TimeIntervals) 
  Dataset /intervals/epochs/contrast (VectorData) no description | shape = (1212,) | dtype = float64
  Dataset /intervals/epochs/direction (VectorData) no description | shape = (1212,) | dtype = float64
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (1212,) | dtype = int64
  Dataset /intervals/epochs/spatial_frequency (VectorData) no description | shape = (1212,) | dtype = float64
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (1212,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1212,) | dtype = float64
  Dataset /intervals/epochs/tags (VectorData) user-defined tags | shape = (1212,) | dtype = object
  Dataset /intervals/epochs/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (1212,) | dtype = uint16
  Dataset /intervals/epochs/temporal_frequency (VectorData) no description | shape = (1212,) | dtype = float64
  Dataset /intervals/epochs/timeseries (VectorData) index into a TimeSeries object | shape = (1212,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/epochs/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (1212,) | dtype = uint16
  Group /processing/brain_observatory_pipeline (ProcessingModule) contains optical physiology processed data
  Group /processing/brain_observatory_pipeline/Fluorescence (Fluorescence) 
  Group /processing/brain_observatory_pipeline/Fluorescence/DfOverF (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/Fluorescence/DfOverF/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (20,) | dtype = int64
  Group /processing/brain_observatory_pipeline/Fluorescence/demixed_traces (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/Fluorescence/demixed_traces/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (20,) | dtype = int64
  Group /processing/brain_observatory_pipeline/Fluorescence/neuropil_traces (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/Fluorescence/neuropil_traces/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (20,) | dtype = int64
  Group /processing/brain_observatory_pipeline/Fluorescence/raw_traces (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/Fluorescence/raw_traces/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (20,) | dtype = int64
  Group /processing/brain_observatory_pipeline/ImageSegmentation (ImageSegmentation) 
  Group /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation (PlaneSegmentation) Segmentation for imaging plane (de Vries et al., 2019, Nat Neurosci)
  Dataset /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/id (ElementIdentifiers)  | shape = (20,) | dtype = int64
  Dataset /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (20, 512, 512) | dtype = uint8
  Group /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/imaging_plane/device (Device) 
  Group /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/imaging_plane/optical_channel (OpticalChannel) 
  Dataset /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/neuropil_r (VectorData) neuropil_r | shape = (20,) | dtype = float64
  Group /processing/brain_observatory_pipeline/MotionCorrection (TimeSeries) Number of pixels shifts measured during motion correction
  Group /processing/brain_observatory_pipeline/RunningBehavior (BehavioralTimeSeries) 
  Group /processing/brain_observatory_pipeline/RunningBehavior/running_speed (TimeSeries) Speed of the mouse on a rotating wheel
  Group /processing/brain_observatory_pipeline/l0_events (Fluorescence) 
  Group /processing/brain_observatory_pipeline/l0_events/dff_events (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/l0_events/dff_events/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (20,) | dtype = int64
  Group /processing/brain_observatory_pipeline/l0_events/true_false_events (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/l0_events/true_false_events/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (20,) | dtype = int64
  Group /processing/brain_observatory_pipeline/max_project (TwoPhotonSeries) no description
  Group /processing/brain_observatory_pipeline/max_project/imaging_plane (ImagingPlane) 
  Group /processing/brain_observatory_pipeline/max_project/imaging_plane/device (Device) 
  Group /processing/brain_observatory_pipeline/max_project/imaging_plane/optical_channel (OpticalChannel) 
  Group /processing/stimulus (ProcessingModule) Stimulus Times processing
  Group /processing/stimulus/timestamps (TimeSeries) no description
  session_description: OphysSession
  session_start_time: 2018-04-20T20:22:35.327000-07:00
  timestamps_reference_time: 2018-04-20T20:22:35.327000-07:00
  Group /units (Units) 
  Dataset /units/cell_id (VectorData) no description | shape = (20,) | dtype = int64
  Dataset /units/id (ElementIdentifiers)  | shape = (20,) | dtype = int64
  Dataset /units/pos_x (VectorData) no description | shape = (20,) | dtype = int64
  Dataset /units/pos_y (VectorData) no description | shape = (20,) | dtype = int64


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2020-12-07T11:54:17.586577-08:00']
  Group /general/devices/CAM2P.1 (Device) 
  Group /general/optophysiology/imaging_plane_1 (ImagingPlane) 
  Group /general/optophysiology/imaging_plane_1/device (Device) 
  Group /general/optophysiology/imaging_plane_1/optical_channel (OpticalChannel) 
  session_id: 692308988
  Group /general/subject (Subject) 
  identifier: 692342504
  Group /intervals/epochs (TimeIntervals) 
  Dataset /intervals/epochs/contrast (VectorData) no description | shape = (1212,) | dtype = float64
  Dataset /intervals/epochs/direction (VectorData) no description | shape = (1212,) | dtype = float64
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (1212,) | dtype = int64
  Dataset /intervals/epochs/spatial_frequency (VectorData) no description | shape = (1212,) | dtype = float64
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (1212,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1212,) | dtype = float64
  Dataset /intervals/epochs/tags (VectorData) user-defined tags | shape = (1212,) | dtype = object
  Dataset /intervals/epochs/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (1212,) | dtype = uint16
  Dataset /intervals/epochs/temporal_frequency (VectorData) no description | shape = (1212,) | dtype = float64
  Dataset /intervals/epochs/timeseries (VectorData) index into a TimeSeries object | shape = (1212,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/epochs/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (1212,) | dtype = uint16
  Group /processing/brain_observatory_pipeline (ProcessingModule) contains optical physiology processed data
  Group /processing/brain_observatory_pipeline/Fluorescence (Fluorescence) 
  Group /processing/brain_observatory_pipeline/Fluorescence/DfOverF (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/Fluorescence/DfOverF/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (252,) | dtype = int64
  Group /processing/brain_observatory_pipeline/Fluorescence/demixed_traces (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/Fluorescence/demixed_traces/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (252,) | dtype = int64
  Group /processing/brain_observatory_pipeline/Fluorescence/neuropil_traces (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/Fluorescence/neuropil_traces/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (252,) | dtype = int64
  Group /processing/brain_observatory_pipeline/Fluorescence/raw_traces (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/Fluorescence/raw_traces/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (252,) | dtype = int64
  Group /processing/brain_observatory_pipeline/ImageSegmentation (ImageSegmentation) 
  Group /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation (PlaneSegmentation) Segmentation for imaging plane (de Vries et al., 2019, Nat Neurosci)
  Dataset /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/id (ElementIdentifiers)  | shape = (252,) | dtype = int64
  Dataset /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (252, 512, 512) | dtype = uint8
  Group /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/imaging_plane/device (Device) 
  Group /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/imaging_plane/optical_channel (OpticalChannel) 
  Dataset /processing/brain_observatory_pipeline/ImageSegmentation/PlaneSegmentation/neuropil_r (VectorData) neuropil_r | shape = (252,) | dtype = float64
  Group /processing/brain_observatory_pipeline/MotionCorrection (TimeSeries) Number of pixels shifts measured during motion correction
  Group /processing/brain_observatory_pipeline/RunningBehavior (BehavioralTimeSeries) 
  Group /processing/brain_observatory_pipeline/RunningBehavior/running_speed (TimeSeries) Speed of the mouse on a rotating wheel
  Group /processing/brain_observatory_pipeline/l0_events (Fluorescence) 
  Group /processing/brain_observatory_pipeline/l0_events/dff_events (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/l0_events/dff_events/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (252,) | dtype = int64
  Group /processing/brain_observatory_pipeline/l0_events/true_false_events (RoiResponseSeries) no description
  Dataset /processing/brain_observatory_pipeline/l0_events/true_false_events/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (252,) | dtype = int64
  Group /processing/brain_observatory_pipeline/max_project (TwoPhotonSeries) no description
  Group /processing/brain_observatory_pipeline/max_project/imaging_plane (ImagingPlane) 
  Group /processing/brain_observatory_pipeline/max_project/imaging_plane/device (Device) 
  Group /processing/brain_observatory_pipeline/max_project/imaging_plane/optical_channel (OpticalChannel) 
  Group /processing/stimulus (ProcessingModule) Stimulus Times processing
  Group /processing/stimulus/timestamps (TimeSeries) no description
  session_description: OphysSession
  session_start_time: 2018-04-30T22:53:55.809000-07:00
  timestamps_reference_time: 2018-04-30T22:53:55.809000-07:00
  Group /units (Units) 
  Dataset /units/cell_id (VectorData) no description | shape = (252,) | dtype = int64
  Dataset /units/id (ElementIdentifiers)  | shape = (252,) | dtype = int64
  Dataset /units/pos_x (VectorData) no description | shape = (252,) | dtype = int64
  Dataset /units/pos_y (VectorData) no description | shape = (252,) | dtype = int64
