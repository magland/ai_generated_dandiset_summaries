
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000150/draft
name: test_release_openscope
contributor: [{'name': ', ', 'email': 'ahad.bawany@alleninstitute.org', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}]
description: Just a test to see if uploading our newly generated NWBs is successful 
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 706988912, 'numberOfFiles': 1, 'numberOfSubjects': 1, 'variableMeasured': ['ProcessingModule', 'OpticalChannel', 'PlaneSegmentation', 'ImagingPlane'], 'measurementTechnique': [{'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000150 has 2 NWB files.
2 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/v_in (TimeSeries) The theoretical maximum voltage that the running wheel encoder will reach prior to "wrapping". This should theoretically be 5V (after crossing 5V goes to 0V, or vice versa). In practice the encoder does not always reach this value before wrapping, which can cause transient spikes in speed at the voltage "wraps".
  Group /acquisition/v_sig (TimeSeries) Voltage signal from the running wheel encoder
  file_create_date: ['2025-02-18T10:31:00.305861+00:00']
  Group /general/devices/MESO.2 (Device) Allen Brain Observatory - Mesoscope 2P Rig
  experiment_description: ophys session
  institution: Allen Institute for Brain Science
  keywords: ['2-photon' 'calcium imaging' 'visual cortex' 'behavior' 'task']
  Group /general/metadata (OphysMetadata) 
  Group /general/optophysiology/imaging_plane_1 (ImagingPlane) 
  Group /general/optophysiology/imaging_plane_1/channel_1 (OpticalChannel) 
  Group /general/optophysiology/imaging_plane_1/device (Device) Allen Brain Observatory - Mesoscope 2P Rig
  Group /general/subject (Subject) 
  surgery:  Structure: VISp
  identifier: 1280384858
  Group /intervals/gray_presentations (TimeIntervals) Presentation times and stimuli details for 'gray' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/gray_presentations/color (VectorData) No description | shape = (63000,) | dtype = object
  Dataset /intervals/gray_presentations/contrast (VectorData) Contrast of stimulus | shape = (63000,) | dtype = float64
  Dataset /intervals/gray_presentations/frame (VectorData) Frame of movie stimulus | shape = (63000,) | dtype = float64
  Dataset /intervals/gray_presentations/id (ElementIdentifiers)  | shape = (63000,) | dtype = int64
  Dataset /intervals/gray_presentations/opacity (VectorData) Opacity of stimulus | shape = (63000,) | dtype = float64
  Dataset /intervals/gray_presentations/orientation (VectorData) Orientation of stimulus | shape = (63000,) | dtype = float64
  Dataset /intervals/gray_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (63000,) | dtype = object
  Dataset /intervals/gray_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (63000,) | dtype = float64
  Dataset /intervals/gray_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (63000,) | dtype = float64
  Dataset /intervals/gray_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (63000,) | dtype = float64
  Dataset /intervals/gray_presentations/stimulus_name (VectorData) Name of stimulus | shape = (63000,) | dtype = object
  Dataset /intervals/gray_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (63000,) | dtype = float64
  Dataset /intervals/gray_presentations/tags (VectorData) user-defined tags | shape = (63000,) | dtype = object
  Dataset /intervals/gray_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (63000,) | dtype = uint16
  Dataset /intervals/gray_presentations/timeseries (VectorData) index into a TimeSeries object | shape = (63000,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/gray_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (63000,) | dtype = uint16
  Dataset /intervals/gray_presentations/units (VectorData) Units of stimulus size | shape = (63000,) | dtype = object
  Group /intervals/movie_clip_A_presentations (TimeIntervals) Presentation times and stimuli details for 'movie_clip_A' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/movie_clip_A_presentations/color (VectorData) No description | shape = (63000,) | dtype = object
  Dataset /intervals/movie_clip_A_presentations/contrast (VectorData) Contrast of stimulus | shape = (63000,) | dtype = float64
  Dataset /intervals/movie_clip_A_presentations/frame (VectorData) Frame of movie stimulus | shape = (63000,) | dtype = float64
  Dataset /intervals/movie_clip_A_presentations/id (ElementIdentifiers)  | shape = (63000,) | dtype = int64
  Dataset /intervals/movie_clip_A_presentations/opacity (VectorData) Opacity of stimulus | shape = (63000,) | dtype = float64
  Dataset /intervals/movie_clip_A_presentations/orientation (VectorData) Orientation of stimulus | shape = (63000,) | dtype = float64
  Dataset /intervals/movie_clip_A_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (63000,) | dtype = object
  Dataset /intervals/movie_clip_A_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (63000,) | dtype = float64
  Dataset /intervals/movie_clip_A_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (63000,) | dtype = float64
  Dataset /intervals/movie_clip_A_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (63000,) | dtype = float64
  Dataset /intervals/movie_clip_A_presentations/stimulus_name (VectorData) Name of stimulus | shape = (63000,) | dtype = object
  Dataset /intervals/movie_clip_A_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (63000,) | dtype = float64
  Dataset /intervals/movie_clip_A_presentations/tags (VectorData) user-defined tags | shape = (63000,) | dtype = object
  Dataset /intervals/movie_clip_A_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (63000,) | dtype = uint16
  Dataset /intervals/movie_clip_A_presentations/timeseries (VectorData) index into a TimeSeries object | shape = (63000,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/movie_clip_A_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (63000,) | dtype = uint16
  Dataset /intervals/movie_clip_A_presentations/units (VectorData) Units of stimulus size | shape = (63000,) | dtype = object
  Group /intervals/movie_clip_B_presentations (TimeIntervals) Presentation times and stimuli details for 'movie_clip_B' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/movie_clip_B_presentations/color (VectorData) No description | shape = (63000,) | dtype = object
  Dataset /intervals/movie_clip_B_presentations/contrast (VectorData) Contrast of stimulus | shape = (63000,) | dtype = float64
  Dataset /intervals/movie_clip_B_presentations/frame (VectorData) Frame of movie stimulus | shape = (63000,) | dtype = float64
  Dataset /intervals/movie_clip_B_presentations/id (ElementIdentifiers)  | shape = (63000,) | dtype = int64
  Dataset /intervals/movie_clip_B_presentations/opacity (VectorData) Opacity of stimulus | shape = (63000,) | dtype = float64
  Dataset /intervals/movie_clip_B_presentations/orientation (VectorData) Orientation of stimulus | shape = (63000,) | dtype = float64
  Dataset /intervals/movie_clip_B_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (63000,) | dtype = object
  Dataset /intervals/movie_clip_B_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (63000,) | dtype = float64
  Dataset /intervals/movie_clip_B_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (63000,) | dtype = float64
  Dataset /intervals/movie_clip_B_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (63000,) | dtype = float64
  Dataset /intervals/movie_clip_B_presentations/stimulus_name (VectorData) Name of stimulus | shape = (63000,) | dtype = object
  Dataset /intervals/movie_clip_B_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (63000,) | dtype = float64
  Dataset /intervals/movie_clip_B_presentations/tags (VectorData) user-defined tags | shape = (63000,) | dtype = object
  Dataset /intervals/movie_clip_B_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (63000,) | dtype = uint16
  Dataset /intervals/movie_clip_B_presentations/timeseries (VectorData) index into a TimeSeries object | shape = (63000,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/movie_clip_B_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (63000,) | dtype = uint16
  Dataset /intervals/movie_clip_B_presentations/units (VectorData) Units of stimulus size | shape = (63000,) | dtype = object
  Group /intervals/movie_clip_C_presentations (TimeIntervals) Presentation times and stimuli details for 'movie_clip_C' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/movie_clip_C_presentations/color (VectorData) No description | shape = (63000,) | dtype = object
  Dataset /intervals/movie_clip_C_presentations/contrast (VectorData) Contrast of stimulus | shape = (63000,) | dtype = float64
  Dataset /intervals/movie_clip_C_presentations/frame (VectorData) Frame of movie stimulus | shape = (63000,) | dtype = float64
  Dataset /intervals/movie_clip_C_presentations/id (ElementIdentifiers)  | shape = (63000,) | dtype = int64
  Dataset /intervals/movie_clip_C_presentations/opacity (VectorData) Opacity of stimulus | shape = (63000,) | dtype = float64
  Dataset /intervals/movie_clip_C_presentations/orientation (VectorData) Orientation of stimulus | shape = (63000,) | dtype = float64
  Dataset /intervals/movie_clip_C_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (63000,) | dtype = object
  Dataset /intervals/movie_clip_C_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (63000,) | dtype = float64
  Dataset /intervals/movie_clip_C_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (63000,) | dtype = float64
  Dataset /intervals/movie_clip_C_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (63000,) | dtype = float64
  Dataset /intervals/movie_clip_C_presentations/stimulus_name (VectorData) Name of stimulus | shape = (63000,) | dtype = object
  Dataset /intervals/movie_clip_C_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (63000,) | dtype = float64
  Dataset /intervals/movie_clip_C_presentations/tags (VectorData) user-defined tags | shape = (63000,) | dtype = object
  Dataset /intervals/movie_clip_C_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (63000,) | dtype = uint16
  Dataset /intervals/movie_clip_C_presentations/timeseries (VectorData) index into a TimeSeries object | shape = (63000,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/movie_clip_C_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (63000,) | dtype = uint16
  Dataset /intervals/movie_clip_C_presentations/units (VectorData) Units of stimulus size | shape = (63000,) | dtype = object
  Group /processing/ophys (ProcessingModule) Ophys processing module
  Group /processing/ophys/corrected_fluorescence (Fluorescence) 
  Group /processing/ophys/corrected_fluorescence/traces (RoiResponseSeries) no description
  Dataset /processing/ophys/corrected_fluorescence/traces/rois (DynamicTableRegion) segmented cells labeled by cell_specimen_id | shape = (121,) | dtype = int64
  Group /processing/ophys/dff (DfOverF) 
  Group /processing/ophys/dff/traces (RoiResponseSeries) no description
  Dataset /processing/ophys/dff/traces/rois (DynamicTableRegion) segmented cells labeled by cell_specimen_id | shape = (121,) | dtype = int64
  Group /processing/ophys/event_detection (OphysEventDetection) no description
  Dataset /processing/ophys/event_detection/rois (DynamicTableRegion) Cells with detected events | shape = (121,) | dtype = int64
  Group /processing/ophys/image_segmentation (ImageSegmentation) 
  Group /processing/ophys/image_segmentation/cell_specimen_table (PlaneSegmentation) Segmented rois
  Dataset /processing/ophys/image_segmentation/cell_specimen_table/cell_specimen_id (VectorData) Unified id of segmented cell across experiments (after cell matching) | shape = (121,) | dtype = int64
  Dataset /processing/ophys/image_segmentation/cell_specimen_table/height (VectorData) Height of ROI in pixels | shape = (121,) | dtype = int64
  Dataset /processing/ophys/image_segmentation/cell_specimen_table/id (ElementIdentifiers)  | shape = (121,) | dtype = int64
  Dataset /processing/ophys/image_segmentation/cell_specimen_table/image_mask (VectorData) Image masks for each ROI | shape = (121, 512, 512) | dtype = bool
  Group /processing/ophys/image_segmentation/cell_specimen_table/imaging_plane (ImagingPlane) 
  Group /processing/ophys/image_segmentation/cell_specimen_table/imaging_plane/channel_1 (OpticalChannel) 
  Group /processing/ophys/image_segmentation/cell_specimen_table/imaging_plane/device (Device) Allen Brain Observatory - Mesoscope 2P Rig
  Dataset /processing/ophys/image_segmentation/cell_specimen_table/mask_image_plane (VectorData) Which image plane an ROI resides on. Overlapping ROIs are stored on different mask image planes. | shape = (121,) | dtype = int64
  Dataset /processing/ophys/image_segmentation/cell_specimen_table/max_correction_down (VectorData) Max motion correction in down direction in pixels | shape = (121,) | dtype = float64
  Dataset /processing/ophys/image_segmentation/cell_specimen_table/max_correction_left (VectorData) Max motion correction in left direction in pixels | shape = (121,) | dtype = float64
  Dataset /processing/ophys/image_segmentation/cell_specimen_table/max_correction_right (VectorData) Max motion correction in right direction in pixels | shape = (121,) | dtype = float64
  Dataset /processing/ophys/image_segmentation/cell_specimen_table/max_correction_up (VectorData) Max motion correction in up direction in pixels | shape = (121,) | dtype = float64
  Dataset /processing/ophys/image_segmentation/cell_specimen_table/valid_roi (VectorData) Indicates if cell classification found the ROI to be a cell or not | shape = (121,) | dtype = bool
  Dataset /processing/ophys/image_segmentation/cell_specimen_table/width (VectorData) Width of ROI in pixels | shape = (121,) | dtype = int64
  Dataset /processing/ophys/image_segmentation/cell_specimen_table/x (VectorData) x position of ROI in Image Plane in pixels (top left corner) | shape = (121,) | dtype = int64
  Dataset /processing/ophys/image_segmentation/cell_specimen_table/y (VectorData) y position of ROI in Image Plane in pixels (top left corner) | shape = (121,) | dtype = int64
  Group /processing/ophys/images (Images) no description
  Dataset /processing/ophys/images/average_image (GrayscaleImage) average_image image at pixels/cm resolution | shape = (512, 512) | dtype = uint8
  Dataset /processing/ophys/images/max_projection (GrayscaleImage) max_projection image at pixels/cm resolution | shape = (512, 512) | dtype = uint8
  Dataset /processing/ophys/images/segmentation_mask_image (GrayscaleImage) segmentation_mask_image image at pixels/cm resolution | shape = (512, 512) | dtype = int64
  Group /processing/ophys/neuropil_trace (Fluorescence) 
  Group /processing/ophys/neuropil_trace/traces (RoiResponseSeries) no description
  Dataset /processing/ophys/neuropil_trace/traces/rois (DynamicTableRegion) segmented cells labeled by cell_specimen_id | shape = (121,) | dtype = int64
  Group /processing/ophys/ophys_motion_correction_x (TimeSeries) no description
  Group /processing/ophys/ophys_motion_correction_y (TimeSeries) no description
  Group /processing/running (ProcessingModule) Running speed processing module
  Group /processing/running/dx (TimeSeries) Running wheel angular change, computed during data collection
  Group /processing/running/speed (TimeSeries) no description
  Group /processing/running/speed_unfiltered (TimeSeries) no description
  Group /processing/stimulus (ProcessingModule) Stimulus Times processing
  Group /processing/stimulus/timestamps (TimeSeries) no description
  Group /processing/stimulus_ophys (ProcessingModule) Stimulus Times processing
  Group /processing/stimulus_ophys/timestamps (TimeSeries) no description
  session_description: Ophys Session
  session_start_time: 2023-06-30T16:04:51.055000+00:00
  Group /stimulus/templates/gray (ImageSeries) no description
  Group /stimulus/templates/movie_clip_A (ImageSeries) no description
  Group /stimulus/templates/movie_clip_B (ImageSeries) no description
  Group /stimulus/templates/movie_clip_C (ImageSeries) no description
  timestamps_reference_time: 2023-06-30T16:04:51.055000+00:00
