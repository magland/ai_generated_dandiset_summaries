
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000617/0.250312.0130
name: Allen Institute Openscope - Sequence Learning Project
contributor: [{'name': 'National Institutes of Health (NIH)', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': '1 U24 NS 113646-02'}, {'url': 'https://alleninstitute.org/', 'name': 'Allen Institute', 'roleName': ['dcite:Producer', 'dcite:Funder', 'dcite:Affiliation'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/03cpe7c52', 'includeInCitation': False}, {'name': 'Berry, Michael', 'email': 'berry@princeton.edu', 'roleName': ['dcite:ContactPerson', 'dcite:Conceptualization', 'dcite:Author', 'dcite:Investigation', 'dcite:ProjectLeader'], 'schemaKey': 'Person', 'identifier': '0000-0003-4133-7999', 'includeInCitation': True}, {'name': 'Lecoq, Jérôme', 'email': 'jeromel@alleninstitute.org', 'roleName': ['dcite:ContactPerson', 'dcite:DataManager', 'dcite:FundingAcquisition', 'dcite:Maintainer', 'dcite:ProjectManager', 'dcite:ProjectAdministration', 'dcite:Software', 'dcite:Supervision'], 'schemaKey': 'Person', 'identifier': '0000-0002-0131-0938', 'includeInCitation': True}, {'name': 'Amaya, Avalon', 'roleName': ['dcite:DataCollector'], 'schemaKey': 'Person', 'identifier': '0000-0003-2274-2892', 'includeInCitation': True}, {'name': 'Wilkes, Josh', 'roleName': ['dcite:DataCollector'], 'schemaKey': 'Person', 'identifier': '0009-0005-4858-2219', 'includeInCitation': True}, {'name': 'Nguyen, Katrina', 'roleName': ['dcite:DataCollector'], 'schemaKey': 'Person', 'identifier': '0009-0009-8547-9703', 'includeInCitation': True}, {'name': 'Peene, Carter', 'roleName': ['dcite:DataCurator', 'dcite:DataManager', 'dcite:Software'], 'schemaKey': 'Person', 'identifier': '0009-0000-6660-2264', 'includeInCitation': True}, {'name': 'Bawany, Ahad', 'roleName': ['dcite:DataCurator', 'dcite:DataManager', 'dcite:Software'], 'schemaKey': 'Person', 'identifier': '0009-0002-5495-5411', 'includeInCitation': True}, {'name': 'Han, Warren Han', 'roleName': ['dcite:DataCollector'], 'schemaKey': 'Person', 'identifier': '0009-0006-0104-0380', 'includeInCitation': True}, {'name': 'Seid,  Samuel', 'roleName': ['dcite:DataCollector', 'dcite:DataCurator'], 'schemaKey': 'Person', 'identifier': '0000-0002-5403-7816', 'includeInCitation': True}, {'name': 'Young, Ahrial', 'roleName': ['dcite:DataCollector', 'dcite:DataCurator'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Naidoo, Robyn', 'roleName': ['dcite:DataCollector'], 'schemaKey': 'Person', 'identifier': '0009-0004-0996-8808', 'includeInCitation': True}, {'name': 'Ha, Vivian', 'roleName': ['dcite:DataCollector', 'dcite:DataCurator'], 'schemaKey': 'Person', 'identifier': '0009-0005-0093-3825', 'includeInCitation': True}, {'name': 'Johnson, Tye', 'roleName': ['dcite:DataCollector'], 'schemaKey': 'Person', 'identifier': '0009-0006-7239-7571', 'includeInCitation': True}, {'name': 'Williford, Ali', 'roleName': ['dcite:Supervision'], 'schemaKey': 'Person', 'identifier': '0009-0000-7282-7515', 'includeInCitation': True}, {'name': 'Swapp, Jackie', 'roleName': ['dcite:Supervision'], 'schemaKey': 'Person', 'identifier': '0009-0008-4965-6242', 'includeInCitation': True}, {'name': 'Caldejon, Shiella', 'roleName': ['dcite:DataCollector', 'dcite:DataCurator', 'dcite:DataManager', 'dcite:Supervision'], 'schemaKey': 'Person', 'includeInCitation': True}]
description: Adaptive and coordinated behavior requires that an animal be able to make predictions about the near and even far future. This intuition that some neural computations should be ‘predictive’ in their character has a long history, starting with ideas about how the receptive field structure of retinal ganglion cells relate to the statistics of natural visual scenes. Ideas about predictive computation have been most influential in thinking about the function of the neocortex. Here, the relatively stereotyped local circuitry of the neocortex has long led to speculation that each local circuit might be carrying out a somewhat similar, fundamental computation on its specific inputs. In addition, the organization of sensory-motor pathways into hierarchies (e.g., V1, V2, V4, IT in the ventral visual stream) with stereotyped feedforward and feedback connections has motivated ideas about hierarchical predictive codes, where higher levels of the hierarchy send predictions down to the lower level that then compares its inputs against the predictions and only send the surprises up the hierarchy (such as in the work of Mumford, Rao & Ballard, and Friston). Despite the wide influence of ideas about predictive coding, there is relatively little experimental evidence that such computations occur in multiple cortical areas, perhaps serving as a ‘canonical computation’ of the neocortical microcircuit. Our experimental design is based on a Sequence Learning Experiment, in which head-fixed mice passively view sequences of three different natural movie clips (labeled ‘A’, ‘B’, ‘C’), each having a duration of 2 seconds. We begin with one recording session (day #0), where the movie clips are presented in random order along with a 2 second grey screen (labeled ‘X’). Each stimulus occurs a total of 525 times, allowing a thorough characterization of neural responses before any sequence learning has occurred. Next, there are 3 recording sessions where the three movie clips are presented in a repeating temporal sequence, ABCABC…, for 500 times, in order to train the mouse’s brain. This training allows the mouse to potentially use the identity of the current movie clip predict the next movie clip. In addition, each sequence training session includes a period of random-order presentation, in order to assess changes in neural tuning during sequence learning. Finally, our last session (day #4) had stimuli presented in random order, allowing us to test more thoroughly how responses changed due to sequence learning.

Our design uses 2-photon microscopy with eight simultaneously recorded fields-of-view. The fields-of-view will include both layer 2/3 and layer 4 as well as from multiple cortical areas: V1 (VISp), LM (VISl), AM (VISam), and PM (VISpm). The experiment used the Cux2-CreERTS2:Camk2a-tTa; Ai93(TITL-GCaMP6f) mouse line, which has expression in excitatory neurons of both layer 4 and 2/3.
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 13197788224949, 'numberOfFiles': 1197, 'numberOfSubjects': 13, 'variableMeasured': ['OpticalChannel', 'PlaneSegmentation', 'ProcessingModule', 'ImagingPlane', 'TwoPhotonSeries'], 'measurementTechnique': [{'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'two-photon microscopy technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000617 has 100 NWB files.
50 of these NWB files are of type 1.
50 of these NWB files are of type 2.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/raw_suite2p_motion_corrected (TwoPhotonSeries) no description
  Group /acquisition/raw_suite2p_motion_corrected/imaging_plane (ImagingPlane) 
  Group /acquisition/raw_suite2p_motion_corrected/imaging_plane/channel_1 (OpticalChannel) 
  Group /acquisition/raw_suite2p_motion_corrected/imaging_plane/device (Device) Allen Brain Observatory - Mesoscope 2P Rig
  Group /acquisition/v_in (TimeSeries) The theoretical maximum voltage that the running wheel encoder will reach prior to "wrapping". This should theoretically be 5V (after crossing 5V goes to 0V, or vice versa). In practice the encoder does not always reach this value before wrapping, which can cause transient spikes in speed at the voltage "wraps".
  Group /acquisition/v_sig (TimeSeries) Voltage signal from the running wheel encoder
  file_create_date: ['2025-02-05T14:05:26.589139+00:00']
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
  timestamps_reference_time: 2023-06-30T16:04:51.055000+00:00


Here is a summary of the type 2 NWB files:
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
