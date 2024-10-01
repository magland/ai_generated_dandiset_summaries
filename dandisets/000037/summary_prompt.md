
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000037/0.240209.1623
name: Allen Institute Openscope - Responses to inconsistent stimuli in somata and distal apical dendrites in primary visual cortex
contributor: [{'url': 'https://colleenjg.github.io/', 'name': 'Gillon, Colleen J.', 'email': 'colleen.gillon@mail.utoronto.ca', 'roleName': ['dcite:Author', 'dcite:ContactPerson', 'dcite:DataCurator', 'dcite:FormalAnalysis'], 'schemaKey': 'Person', 'identifier': '0000-0002-2253-7816', 'affiliation': [{'name': 'University of Toronto', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/03dbr7087'}], 'includeInCitation': True}, {'name': 'Lecoq, Jérôme A.', 'email': 'jeromel@alleninstitute.org', 'roleName': ['dcite:Author', 'dcite:Conceptualization', 'dcite:ContactPerson', 'dcite:DataCollector', 'dcite:DataCurator', 'dcite:FundingAcquisition', 'dcite:Resources', 'dcite:Supervision'], 'schemaKey': 'Person', 'identifier': '0000-0002-0131-0938', 'affiliation': [{'name': 'Allen Institute', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/03cpe7c52'}], 'includeInCitation': True}, {'name': 'Pina, Jason E.', 'roleName': ['dcite:Author', 'dcite:DataCollector', 'dcite:FormalAnalysis'], 'schemaKey': 'Person', 'identifier': '0000-0003-1385-8762', 'affiliation': [{'name': 'York University', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/05fq50484'}], 'includeInCitation': True}, {'name': 'Zylberberg, Joel', 'email': 'joelzy@yorku.ca', 'roleName': ['dcite:Author', 'dcite:Conceptualization', 'dcite:FormalAnalysis', 'dcite:Supervision'], 'schemaKey': 'Person', 'identifier': '0000-0002-8208-5698', 'affiliation': [{'name': 'York University', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/05fq50484'}], 'includeInCitation': True}, {'name': 'Richards, Blake A.', 'email': 'blake.richards@mcgill.ca', 'roleName': ['dcite:Author', 'dcite:Conceptualization', 'dcite:FormalAnalysis', 'dcite:Supervision'], 'schemaKey': 'Person', 'identifier': '0000-0001-9662-2151', 'affiliation': [{'name': 'McGill University', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/01pxwe438'}, {'name': 'Mila - Quebec Artificial Intelligence Institute', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/05c22rx21'}], 'includeInCitation': True}, {'url': 'https://alleninstitute.org/', 'name': 'Allen Institute', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/03cpe7c52', 'contactPoint': [], 'includeInCitation': False}, {'name': 'Falconwood Foundation', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'contactPoint': [], 'includeInCitation': False}, {'url': 'http://www.nserc-crsng.gc.ca/index_eng.asp', 'name': 'Natural Sciences and Engineering Research Council', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01h531d29', 'contactPoint': [], 'includeInCitation': False}, {'url': 'http://www.cifar.ca/', 'name': 'Canadian Institute for Advanced Research', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01sdtdd95', 'contactPoint': [], 'includeInCitation': False}, {'url': 'http://www.sloan.org/', 'name': 'Alfred P. Sloan Foundation', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/052csg198', 'contactPoint': [], 'includeInCitation': False}, {'url': 'http://www.chairs-chaires.gc.ca/home-accueil-eng.aspx', 'name': 'Canada Research Chairs', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/0517h6h17', 'contactPoint': [], 'includeInCitation': False}, {'url': 'https://www.ontario.ca/page/government', 'name': 'Government of Ontario', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/015pzp858', 'contactPoint': [], 'includeInCitation': False}]
description: This dataset was collected for the Credit Assignment project, as part of the Allen Institute for Brain Science's OpenScope project. The most up-to-date links to the publications associated with this dataset (a dataset descriptor paper and an analysis paper) can be found by going to the metadata Github repository, linked below.

Briefly, mice were habituated to head-fixation on a running disc over a period of 11 days. Over the last 6 days, mice were presented with repeating stimulus sequences, with consistent features. These sessions are not included in the dataset, as imaging was not performed. Following habituation, sequences with inconsistent features were introduced over three sessions, while two-photon calcium imaging was performed in pyramidal neurons of primary visual cortex (VisP). Specifically, recordings for each mouse were made in one of four planes: L2/3 somata, L5 somata, L2/3 distal apical dendrites or L5 distal apical dendrites. As mice gained experience with the inconsistent sequences, responses to these events were found to evolve in opposite ways in the dendritic and somatic compartments.

The dataset includes 50 sessions total, recorded in 13 subjects, with at least 3 sessions per subject. Each session file includes: **(1)** ROI dF/F traces, **(2)** ROI masks, **(3)** ROI tracking information (where applicable), **(4)** running velocity traces, **(5)** pupil diameter traces, **(6)** pupil centroid position traces in x and y, **(7)** stimulus parameters. Note that gaze was not computed for this dataset. What is provided is the position of the pupil centroid in the pupil recording videos. In addition, a second, slightly larger version of each file was created, also including: **(8)** stimulus frame images (identifiable by `+image` in the file name). Lastly, a third, much larger version of each file was created, also including: **(9)** the motion corrected imaging stack (identifiable by `_obj-raw` in the file name).

Certain sessions in this dataset were excluded from our analyses for quality control reasons. They are provided here, as the reasons we excluded them from our analyses may not pose a problem for all use cases. The metadata Github repository, linked below, provides detailed information about each session. 

Release notes for each version of the dataset are provided in the CHANGES file.
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}, {'name': 'behavioral approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 2484974036912, 'numberOfFiles': 151, 'numberOfSubjects': 13, 'variableMeasured': ['ProcessingModule', 'SpatialSeries', 'PlaneSegmentation', 'OpticalChannel', 'BehavioralTimeSeries', 'ImagingPlane', 'PupilTracking', 'TwoPhotonSeries'], 'measurementTechnique': [{'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'two-photon microscopy technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000037 has 94 NWB files.
28 of these NWB files are of type 1.
27 of these NWB files are of type 2.
27 of these NWB files are of type 3.
6 of these NWB files are of type 4.
6 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2022-09-25T04:53:02.714938-07:00' '2023-04-04T15:55:40.600830-07:00']
  Group /general/devices/2p_microscope (Device) Allen Institute two-photon pipeline: CAM2P.2
  institution: Allen Institute for Brain Science
  Group /general/optophysiology/ImagingPlane (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane/device (Device) Allen Institute two-photon pipeline: CAM2P.2
  Group /general/optophysiology/ImagingPlane/optical_channel (OpticalChannel) 
  session_id: 758519303
  Group /general/subject (Subject) 
  identifier: 758519303_with_stim
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/gabor_frame (VectorData) Gabor frame or set, defined by Gabor patch locations and sizes (A, B, C, D or U, G). | shape = (8844,) | dtype = object
  Dataset /intervals/trials/gabor_kappa (VectorData) Kappa (dispersion) of the von Mises distribution used to sample Gabor patch orientations (degrees). | shape = (8844,) | dtype = float64
  Dataset /intervals/trials/gabor_locations_x (VectorData) Locations along the x dimension (width) of the Gabor patch centers (in pixels), centered on the middle of the screen. All locations are for the unwarped stimulus. | shape = (163200,) | dtype = float64
  Dataset /intervals/trials/gabor_locations_x_index (VectorIndex) Index for VectorData 'gabor_locations_x' | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/gabor_locations_y (VectorData) Locations along the y dimension (height) of Gabor patch centers (in pixels), centered on the middle of the screen. All locations are for the unwarped stimulus. | shape = (163200,) | dtype = float64
  Dataset /intervals/trials/gabor_locations_y_index (VectorIndex) Index for VectorData 'gabor_locations_y' | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/gabor_mean_orientation (VectorData) Mean orientation of the von Mises distribution used to sample Gabor patch orientations (degrees, [0, 360]. | shape = (8844,) | dtype = float64
  Dataset /intervals/trials/gabor_number (VectorData) Number of Gabor patches on-screen (before warping mask is applied). | shape = (8844,) | dtype = float64
  Dataset /intervals/trials/gabor_orientations (VectorData) Orientations of the Gabor patches (degrees, [0, 360]). | shape = (163200,) | dtype = int16
  Dataset /intervals/trials/gabor_orientations_index (VectorIndex) Index for VectorData 'gabor_orientations' | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/gabor_sizes (VectorData) Gabor patch sizes (in pixels, with patch width defined, as in psychopy, as width across 6 standard deviations). | shape = (163200,) | dtype = int32
  Dataset /intervals/trials/gabor_sizes_index (VectorIndex) Index for VectorData 'gabor_sizes' | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/main_flow_direction (VectorData) Main direction of flow for the squares (all moving at 50 visual degrees/second). Flow directions are either rightward (nasal-to-temporal) or leftward (temporal-to-nasal). | shape = (8844,) | dtype = object
  Dataset /intervals/trials/num_frames_stim (VectorData) Stop frame number for the stimulus frames (excluded). | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/num_frames_twop (VectorData) Stop frame number for the two-photon frames (excluded). | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/square_locations_x (VectorData) Locations along the x dimension (width) of square centers for each frame of the trial (in pixels), (square x stimulus frame), centered on the middle of the screen. Note that squares disappear a bit off-screen, and are (re)initialized a bit off-screen. All locations are for the unwarped stimulus. | shape = (214200, 60) | dtype = int32
  Dataset /intervals/trials/square_locations_x_index (VectorIndex) Index for VectorData 'square_locations_x' | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/square_locations_y (VectorData) Locations along the y dimension (height) of square centers for each frame of the trial (in pixels), (square x stimulus frame), centered on the middle of the screen. Note that squares are (re)initialized a bit off-screen area. All locations are for the unwarped stimulus. | shape = (214200, 60) | dtype = int32
  Dataset /intervals/trials/square_locations_y_index (VectorIndex) Index for VectorData 'square_locations_y' | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/square_number (VectorData) Total number of squares present, both in the off and on-screen areas (before warping mask is applied). | shape = (8844,) | dtype = float64
  Dataset /intervals/trials/square_proportion_flipped (VectorData) Proportion of squares moving in the direction opposite to the main flow (all moving at 50 visual degrees/second). | shape = (8844,) | dtype = float64
  Dataset /intervals/trials/square_size (VectorData) Size of the squares (in pixels). | shape = (8844,) | dtype = float64
  Dataset /intervals/trials/start_frame_stim (VectorData) Start frame number for the stimulus frames. | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/start_frame_stim_template (VectorData) Start frame number for the trial in the corresponding template. | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/start_frame_twop (VectorData) Start frame number for the two-photon frames. | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (8844,) | dtype = float64
  Dataset /intervals/trials/stimulus_template_name (VectorData) Name of the stimulus template for the trial. | shape = (8844,) | dtype = object
  Dataset /intervals/trials/stimulus_type (VectorData) Type of stimulus presented during the trial. | shape = (8844,) | dtype = object
  Dataset /intervals/trials/stop_frame_stim (VectorData) Stop frame number for the stimulus frames (excluded). | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/stop_frame_twop (VectorData) Stop frame number for the two-photon frames (excluded). | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (8844,) | dtype = float64
  Dataset /intervals/trials/unexpected (VectorData) Whether the stimulus features are expected (0) or unexpected (1). | shape = (8844,) | dtype = float64
  Group /processing/behavior (ProcessingModule) preprocessed behavioral data
  Group /processing/behavior/BehavioralTimeSeries (BehavioralTimeSeries) 
  Group /processing/behavior/BehavioralTimeSeries/running_velocity (TimeSeries) Velocity of the mouse on a rotating disc.
  Group /processing/behavior/PupilTracking (PupilTracking) 
  Group /processing/behavior/PupilTracking/pupil_diameter (TimeSeries) Diameter of the mouse pupil (right) facing the stimulus presentation screen.
  Group /processing/behavior/PupilTracking/pupil_position_x (SpatialSeries) Position in x of the center of the mouse pupil (right) facing the stimulus presentation screen.
  Group /processing/behavior/PupilTracking/pupil_position_y (SpatialSeries) Position in y of the center of the mouse pupil (right) facing the stimulus presentation screen.
  Group /processing/ophys (ProcessingModule) OpenScope processing pipeline
  Group /processing/ophys/DfOverF (DfOverF) 
  Group /processing/ophys/DfOverF/RoiResponseSeries (RoiResponseSeries) ROI traces
  Dataset /processing/ophys/DfOverF/RoiResponseSeries/rois (DynamicTableRegion) Segmented cells with cell_specimen_ids (height x width) | shape = (96,) | dtype = int32
  Group /processing/ophys/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation (PlaneSegmentation) Segmentation for imaging plane (de Vries et al., 2019, Nat Neurosci)
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/id (ElementIdentifiers)  | shape = (96,) | dtype = int32
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (96, 512, 512) | dtype = uint8
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/device (Device) Allen Institute two-photon pipeline: CAM2P.2
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/optical_channel (OpticalChannel) 
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/tracking_id (VectorData) ROI tracking index (NaN for untracked ROIs) | shape = (96,) | dtype = float64
  Group /processing/ophys/PlaneImages (Images) Plane images.
  Dataset /processing/ophys/PlaneImages/max_projection (GrayscaleImage) Normalized maximum projection of the motion corrected z-stack, averaged over 8 frames (hei x wid). | shape = (512, 512) | dtype = uint8
  session_description: Allen Institute OpenScope dataset
  session_start_time: 2018-09-26T17:29:17.502000-07:00
  Group /stimulus/presentation/gabors (IndexSeries) gabors index
  Group /stimulus/presentation/gabors/indexed_timeseries (ImageSeries) Template for Gabor sequence stimulus (frames x height x width x channels) (unwarped, masked)
  Group /stimulus/presentation/grayscreen (IndexSeries) grayscreen index
  Group /stimulus/presentation/grayscreen/indexed_timeseries (ImageSeries) Template for Grayscreen stimulus (frames x height x width x channels) (unwarped, masked)
  Group /stimulus/presentation/visflow_left (IndexSeries) visflow_left index
  Group /stimulus/presentation/visflow_left/indexed_timeseries (ImageSeries) Template for leftward (nasal) visual flow stimulus (frames x height x width x channels) (unwarped, masked)
  Group /stimulus/presentation/visflow_right (IndexSeries) visflow_right index
  Group /stimulus/presentation/visflow_right/indexed_timeseries (ImageSeries) Template for rightward (temporal) visual flow stimulus (frames x height x width x channels) (unwarped, masked)
  Group /stimulus/templates/gabors (ImageSeries) Template for Gabor sequence stimulus (frames x height x width x channels) (unwarped, masked)
  Group /stimulus/templates/grayscreen (ImageSeries) Template for Grayscreen stimulus (frames x height x width x channels) (unwarped, masked)
  Group /stimulus/templates/visflow_left (ImageSeries) Template for leftward (nasal) visual flow stimulus (frames x height x width x channels) (unwarped, masked)
  Group /stimulus/templates/visflow_right (ImageSeries) Template for rightward (temporal) visual flow stimulus (frames x height x width x channels) (unwarped, masked)
  timestamps_reference_time: 2018-09-26T17:29:17.502000-07:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2022-09-25T04:53:02.714938-07:00' '2023-04-03T21:37:34.089423-07:00']
  Group /general/devices/2p_microscope (Device) Allen Institute two-photon pipeline: CAM2P.2
  institution: Allen Institute for Brain Science
  Group /general/optophysiology/ImagingPlane (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane/device (Device) Allen Institute two-photon pipeline: CAM2P.2
  Group /general/optophysiology/ImagingPlane/optical_channel (OpticalChannel) 
  session_id: 758519303
  Group /general/subject (Subject) 
  identifier: 758519303
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/gabor_frame (VectorData) Gabor frame or set, defined by Gabor patch locations and sizes (A, B, C, D or U, G). | shape = (8844,) | dtype = object
  Dataset /intervals/trials/gabor_kappa (VectorData) Kappa (dispersion) of the von Mises distribution used to sample Gabor patch orientations (degrees). | shape = (8844,) | dtype = float64
  Dataset /intervals/trials/gabor_locations_x (VectorData) Locations along the x dimension (width) of the Gabor patch centers (in pixels), centered on the middle of the screen. All locations are for the unwarped stimulus. | shape = (163200,) | dtype = float64
  Dataset /intervals/trials/gabor_locations_x_index (VectorIndex) Index for VectorData 'gabor_locations_x' | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/gabor_locations_y (VectorData) Locations along the y dimension (height) of Gabor patch centers (in pixels), centered on the middle of the screen. All locations are for the unwarped stimulus. | shape = (163200,) | dtype = float64
  Dataset /intervals/trials/gabor_locations_y_index (VectorIndex) Index for VectorData 'gabor_locations_y' | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/gabor_mean_orientation (VectorData) Mean orientation of the von Mises distribution used to sample Gabor patch orientations (degrees, [0, 360]. | shape = (8844,) | dtype = float64
  Dataset /intervals/trials/gabor_number (VectorData) Number of Gabor patches on-screen (before warping mask is applied). | shape = (8844,) | dtype = float64
  Dataset /intervals/trials/gabor_orientations (VectorData) Orientations of the Gabor patches (degrees, [0, 360]). | shape = (163200,) | dtype = int16
  Dataset /intervals/trials/gabor_orientations_index (VectorIndex) Index for VectorData 'gabor_orientations' | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/gabor_sizes (VectorData) Gabor patch sizes (in pixels, with patch width defined, as in psychopy, as width across 6 standard deviations). | shape = (163200,) | dtype = int32
  Dataset /intervals/trials/gabor_sizes_index (VectorIndex) Index for VectorData 'gabor_sizes' | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/main_flow_direction (VectorData) Main direction of flow for the squares (all moving at 50 visual degrees/second). Flow directions are either rightward (nasal-to-temporal) or leftward (temporal-to-nasal). | shape = (8844,) | dtype = object
  Dataset /intervals/trials/num_frames_stim (VectorData) Stop frame number for the stimulus frames (excluded). | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/num_frames_twop (VectorData) Stop frame number for the two-photon frames (excluded). | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/square_locations_x (VectorData) Locations along the x dimension (width) of square centers for each frame of the trial (in pixels), (square x stimulus frame), centered on the middle of the screen. Note that squares disappear a bit off-screen, and are (re)initialized a bit off-screen. All locations are for the unwarped stimulus. | shape = (214200, 60) | dtype = int32
  Dataset /intervals/trials/square_locations_x_index (VectorIndex) Index for VectorData 'square_locations_x' | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/square_locations_y (VectorData) Locations along the y dimension (height) of square centers for each frame of the trial (in pixels), (square x stimulus frame), centered on the middle of the screen. Note that squares are (re)initialized a bit off-screen area. All locations are for the unwarped stimulus. | shape = (214200, 60) | dtype = int32
  Dataset /intervals/trials/square_locations_y_index (VectorIndex) Index for VectorData 'square_locations_y' | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/square_number (VectorData) Total number of squares present, both in the off and on-screen areas (before warping mask is applied). | shape = (8844,) | dtype = float64
  Dataset /intervals/trials/square_proportion_flipped (VectorData) Proportion of squares moving in the direction opposite to the main flow (all moving at 50 visual degrees/second). | shape = (8844,) | dtype = float64
  Dataset /intervals/trials/square_size (VectorData) Size of the squares (in pixels). | shape = (8844,) | dtype = float64
  Dataset /intervals/trials/start_frame_stim (VectorData) Start frame number for the stimulus frames. | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/start_frame_stim_template (VectorData) Start frame number for the trial in the corresponding template. | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/start_frame_twop (VectorData) Start frame number for the two-photon frames. | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (8844,) | dtype = float64
  Dataset /intervals/trials/stimulus_template_name (VectorData) Name of the stimulus template for the trial. | shape = (8844,) | dtype = object
  Dataset /intervals/trials/stimulus_type (VectorData) Type of stimulus presented during the trial. | shape = (8844,) | dtype = object
  Dataset /intervals/trials/stop_frame_stim (VectorData) Stop frame number for the stimulus frames (excluded). | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/stop_frame_twop (VectorData) Stop frame number for the two-photon frames (excluded). | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (8844,) | dtype = float64
  Dataset /intervals/trials/unexpected (VectorData) Whether the stimulus features are expected (0) or unexpected (1). | shape = (8844,) | dtype = float64
  Group /processing/behavior (ProcessingModule) preprocessed behavioral data
  Group /processing/behavior/BehavioralTimeSeries (BehavioralTimeSeries) 
  Group /processing/behavior/BehavioralTimeSeries/running_velocity (TimeSeries) Velocity of the mouse on a rotating disc.
  Group /processing/behavior/PupilTracking (PupilTracking) 
  Group /processing/behavior/PupilTracking/pupil_diameter (TimeSeries) Diameter of the mouse pupil (right) facing the stimulus presentation screen.
  Group /processing/behavior/PupilTracking/pupil_position_x (SpatialSeries) Position in x of the center of the mouse pupil (right) facing the stimulus presentation screen.
  Group /processing/behavior/PupilTracking/pupil_position_y (SpatialSeries) Position in y of the center of the mouse pupil (right) facing the stimulus presentation screen.
  Group /processing/ophys (ProcessingModule) OpenScope processing pipeline
  Group /processing/ophys/DfOverF (DfOverF) 
  Group /processing/ophys/DfOverF/RoiResponseSeries (RoiResponseSeries) ROI traces
  Dataset /processing/ophys/DfOverF/RoiResponseSeries/rois (DynamicTableRegion) Segmented cells with cell_specimen_ids (height x width) | shape = (96,) | dtype = int32
  Group /processing/ophys/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation (PlaneSegmentation) Segmentation for imaging plane (de Vries et al., 2019, Nat Neurosci)
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/id (ElementIdentifiers)  | shape = (96,) | dtype = int32
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (96, 512, 512) | dtype = uint8
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/device (Device) Allen Institute two-photon pipeline: CAM2P.2
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/optical_channel (OpticalChannel) 
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/tracking_id (VectorData) ROI tracking index (NaN for untracked ROIs) | shape = (96,) | dtype = float64
  Group /processing/ophys/PlaneImages (Images) Plane images.
  Dataset /processing/ophys/PlaneImages/max_projection (GrayscaleImage) Normalized maximum projection of the motion corrected z-stack, averaged over 8 frames (hei x wid). | shape = (512, 512) | dtype = uint8
  session_description: Allen Institute OpenScope dataset
  session_start_time: 2018-09-26T17:29:17.502000-07:00
  timestamps_reference_time: 2018-09-26T17:29:17.502000-07:00


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/motion_corrected_stack (TwoPhotonSeries) Motion corrected imaging stack (frames x height x width).
  Group /acquisition/motion_corrected_stack/imaging_plane (ImagingPlane) 
  Group /acquisition/motion_corrected_stack/imaging_plane/device (Device) Allen Institute two-photon pipeline: CAM2P.2
  Group /acquisition/motion_corrected_stack/imaging_plane/optical_channel (OpticalChannel) 
  file_create_date: ['2022-09-25T04:53:02.714938-07:00' '2023-04-05T06:05:53.890395-07:00']
  Group /general/devices/2p_microscope (Device) Allen Institute two-photon pipeline: CAM2P.2
  institution: Allen Institute for Brain Science
  Group /general/optophysiology/ImagingPlane (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane/device (Device) Allen Institute two-photon pipeline: CAM2P.2
  Group /general/optophysiology/ImagingPlane/optical_channel (OpticalChannel) 
  session_id: 758519303
  Group /general/subject (Subject) 
  identifier: 758519303_with_stim_and_stack
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/gabor_frame (VectorData) Gabor frame or set, defined by Gabor patch locations and sizes (A, B, C, D or U, G). | shape = (8844,) | dtype = object
  Dataset /intervals/trials/gabor_kappa (VectorData) Kappa (dispersion) of the von Mises distribution used to sample Gabor patch orientations (degrees). | shape = (8844,) | dtype = float64
  Dataset /intervals/trials/gabor_locations_x (VectorData) Locations along the x dimension (width) of the Gabor patch centers (in pixels), centered on the middle of the screen. All locations are for the unwarped stimulus. | shape = (163200,) | dtype = float64
  Dataset /intervals/trials/gabor_locations_x_index (VectorIndex) Index for VectorData 'gabor_locations_x' | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/gabor_locations_y (VectorData) Locations along the y dimension (height) of Gabor patch centers (in pixels), centered on the middle of the screen. All locations are for the unwarped stimulus. | shape = (163200,) | dtype = float64
  Dataset /intervals/trials/gabor_locations_y_index (VectorIndex) Index for VectorData 'gabor_locations_y' | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/gabor_mean_orientation (VectorData) Mean orientation of the von Mises distribution used to sample Gabor patch orientations (degrees, [0, 360]. | shape = (8844,) | dtype = float64
  Dataset /intervals/trials/gabor_number (VectorData) Number of Gabor patches on-screen (before warping mask is applied). | shape = (8844,) | dtype = float64
  Dataset /intervals/trials/gabor_orientations (VectorData) Orientations of the Gabor patches (degrees, [0, 360]). | shape = (163200,) | dtype = int16
  Dataset /intervals/trials/gabor_orientations_index (VectorIndex) Index for VectorData 'gabor_orientations' | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/gabor_sizes (VectorData) Gabor patch sizes (in pixels, with patch width defined, as in psychopy, as width across 6 standard deviations). | shape = (163200,) | dtype = int32
  Dataset /intervals/trials/gabor_sizes_index (VectorIndex) Index for VectorData 'gabor_sizes' | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/main_flow_direction (VectorData) Main direction of flow for the squares (all moving at 50 visual degrees/second). Flow directions are either rightward (nasal-to-temporal) or leftward (temporal-to-nasal). | shape = (8844,) | dtype = object
  Dataset /intervals/trials/num_frames_stim (VectorData) Stop frame number for the stimulus frames (excluded). | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/num_frames_twop (VectorData) Stop frame number for the two-photon frames (excluded). | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/square_locations_x (VectorData) Locations along the x dimension (width) of square centers for each frame of the trial (in pixels), (square x stimulus frame), centered on the middle of the screen. Note that squares disappear a bit off-screen, and are (re)initialized a bit off-screen. All locations are for the unwarped stimulus. | shape = (214200, 60) | dtype = int32
  Dataset /intervals/trials/square_locations_x_index (VectorIndex) Index for VectorData 'square_locations_x' | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/square_locations_y (VectorData) Locations along the y dimension (height) of square centers for each frame of the trial (in pixels), (square x stimulus frame), centered on the middle of the screen. Note that squares are (re)initialized a bit off-screen area. All locations are for the unwarped stimulus. | shape = (214200, 60) | dtype = int32
  Dataset /intervals/trials/square_locations_y_index (VectorIndex) Index for VectorData 'square_locations_y' | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/square_number (VectorData) Total number of squares present, both in the off and on-screen areas (before warping mask is applied). | shape = (8844,) | dtype = float64
  Dataset /intervals/trials/square_proportion_flipped (VectorData) Proportion of squares moving in the direction opposite to the main flow (all moving at 50 visual degrees/second). | shape = (8844,) | dtype = float64
  Dataset /intervals/trials/square_size (VectorData) Size of the squares (in pixels). | shape = (8844,) | dtype = float64
  Dataset /intervals/trials/start_frame_stim (VectorData) Start frame number for the stimulus frames. | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/start_frame_stim_template (VectorData) Start frame number for the trial in the corresponding template. | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/start_frame_twop (VectorData) Start frame number for the two-photon frames. | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (8844,) | dtype = float64
  Dataset /intervals/trials/stimulus_template_name (VectorData) Name of the stimulus template for the trial. | shape = (8844,) | dtype = object
  Dataset /intervals/trials/stimulus_type (VectorData) Type of stimulus presented during the trial. | shape = (8844,) | dtype = object
  Dataset /intervals/trials/stop_frame_stim (VectorData) Stop frame number for the stimulus frames (excluded). | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/stop_frame_twop (VectorData) Stop frame number for the two-photon frames (excluded). | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (8844,) | dtype = float64
  Dataset /intervals/trials/unexpected (VectorData) Whether the stimulus features are expected (0) or unexpected (1). | shape = (8844,) | dtype = float64
  Group /processing/behavior (ProcessingModule) preprocessed behavioral data
  Group /processing/behavior/BehavioralTimeSeries (BehavioralTimeSeries) 
  Group /processing/behavior/BehavioralTimeSeries/running_velocity (TimeSeries) Velocity of the mouse on a rotating disc.
  Group /processing/behavior/PupilTracking (PupilTracking) 
  Group /processing/behavior/PupilTracking/pupil_diameter (TimeSeries) Diameter of the mouse pupil (right) facing the stimulus presentation screen.
  Group /processing/behavior/PupilTracking/pupil_position_x (SpatialSeries) Position in x of the center of the mouse pupil (right) facing the stimulus presentation screen.
  Group /processing/behavior/PupilTracking/pupil_position_y (SpatialSeries) Position in y of the center of the mouse pupil (right) facing the stimulus presentation screen.
  Group /processing/ophys (ProcessingModule) OpenScope processing pipeline
  Group /processing/ophys/DfOverF (DfOverF) 
  Group /processing/ophys/DfOverF/RoiResponseSeries (RoiResponseSeries) ROI traces
  Dataset /processing/ophys/DfOverF/RoiResponseSeries/rois (DynamicTableRegion) Segmented cells with cell_specimen_ids (height x width) | shape = (96,) | dtype = int32
  Group /processing/ophys/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation (PlaneSegmentation) Segmentation for imaging plane (de Vries et al., 2019, Nat Neurosci)
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/id (ElementIdentifiers)  | shape = (96,) | dtype = int32
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (96, 512, 512) | dtype = uint8
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/device (Device) Allen Institute two-photon pipeline: CAM2P.2
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/optical_channel (OpticalChannel) 
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/tracking_id (VectorData) ROI tracking index (NaN for untracked ROIs) | shape = (96,) | dtype = float64
  Group /processing/ophys/PlaneImages (Images) Plane images.
  Dataset /processing/ophys/PlaneImages/max_projection (GrayscaleImage) Normalized maximum projection of the motion corrected z-stack, averaged over 8 frames (hei x wid). | shape = (512, 512) | dtype = uint8
  session_description: Allen Institute OpenScope dataset
  session_start_time: 2018-09-26T17:29:17.502000-07:00
  Group /stimulus/presentation/gabors (IndexSeries) gabors index
  Group /stimulus/presentation/gabors/indexed_timeseries (ImageSeries) Template for Gabor sequence stimulus (frames x height x width x channels) (unwarped, masked)
  Group /stimulus/presentation/grayscreen (IndexSeries) grayscreen index
  Group /stimulus/presentation/grayscreen/indexed_timeseries (ImageSeries) Template for Grayscreen stimulus (frames x height x width x channels) (unwarped, masked)
  Group /stimulus/presentation/visflow_left (IndexSeries) visflow_left index
  Group /stimulus/presentation/visflow_left/indexed_timeseries (ImageSeries) Template for leftward (nasal) visual flow stimulus (frames x height x width x channels) (unwarped, masked)
  Group /stimulus/presentation/visflow_right (IndexSeries) visflow_right index
  Group /stimulus/presentation/visflow_right/indexed_timeseries (ImageSeries) Template for rightward (temporal) visual flow stimulus (frames x height x width x channels) (unwarped, masked)
  Group /stimulus/templates/gabors (ImageSeries) Template for Gabor sequence stimulus (frames x height x width x channels) (unwarped, masked)
  Group /stimulus/templates/grayscreen (ImageSeries) Template for Grayscreen stimulus (frames x height x width x channels) (unwarped, masked)
  Group /stimulus/templates/visflow_left (ImageSeries) Template for leftward (nasal) visual flow stimulus (frames x height x width x channels) (unwarped, masked)
  Group /stimulus/templates/visflow_right (ImageSeries) Template for rightward (temporal) visual flow stimulus (frames x height x width x channels) (unwarped, masked)
  timestamps_reference_time: 2018-09-26T17:29:17.502000-07:00


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2022-09-24T22:32:36.231878-07:00' '2023-04-04T15:55:46.512674-07:00']
  Group /general/devices/2p_microscope (Device) Allen Institute two-photon pipeline: CAM2P.1
  institution: Allen Institute for Brain Science
  Group /general/optophysiology/ImagingPlane (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane/device (Device) Allen Institute two-photon pipeline: CAM2P.1
  Group /general/optophysiology/ImagingPlane/optical_channel (OpticalChannel) 
  session_id: 759666166
  Group /general/subject (Subject) 
  identifier: 759666166_with_stim
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/gabor_frame (VectorData) Gabor frame or set, defined by Gabor patch locations and sizes (A, B, C, D or U, G). | shape = (8844,) | dtype = object
  Dataset /intervals/trials/gabor_kappa (VectorData) Kappa (dispersion) of the von Mises distribution used to sample Gabor patch orientations (degrees). | shape = (8844,) | dtype = float64
  Dataset /intervals/trials/gabor_locations_x (VectorData) Locations along the x dimension (width) of the Gabor patch centers (in pixels), centered on the middle of the screen. All locations are for the unwarped stimulus. | shape = (163200,) | dtype = float64
  Dataset /intervals/trials/gabor_locations_x_index (VectorIndex) Index for VectorData 'gabor_locations_x' | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/gabor_locations_y (VectorData) Locations along the y dimension (height) of Gabor patch centers (in pixels), centered on the middle of the screen. All locations are for the unwarped stimulus. | shape = (163200,) | dtype = float64
  Dataset /intervals/trials/gabor_locations_y_index (VectorIndex) Index for VectorData 'gabor_locations_y' | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/gabor_mean_orientation (VectorData) Mean orientation of the von Mises distribution used to sample Gabor patch orientations (degrees, [0, 360]. | shape = (8844,) | dtype = float64
  Dataset /intervals/trials/gabor_number (VectorData) Number of Gabor patches on-screen (before warping mask is applied). | shape = (8844,) | dtype = float64
  Dataset /intervals/trials/gabor_orientations (VectorData) Orientations of the Gabor patches (degrees, [0, 360]). | shape = (163200,) | dtype = int16
  Dataset /intervals/trials/gabor_orientations_index (VectorIndex) Index for VectorData 'gabor_orientations' | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/gabor_sizes (VectorData) Gabor patch sizes (in pixels, with patch width defined, as in psychopy, as width across 6 standard deviations). | shape = (163200,) | dtype = int32
  Dataset /intervals/trials/gabor_sizes_index (VectorIndex) Index for VectorData 'gabor_sizes' | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/main_flow_direction (VectorData) Main direction of flow for the squares (all moving at 50 visual degrees/second). Flow directions are either rightward (nasal-to-temporal) or leftward (temporal-to-nasal). | shape = (8844,) | dtype = object
  Dataset /intervals/trials/num_frames_stim (VectorData) Stop frame number for the stimulus frames (excluded). | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/num_frames_twop (VectorData) Stop frame number for the two-photon frames (excluded). | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/square_locations_x (VectorData) Locations along the x dimension (width) of square centers for each frame of the trial (in pixels), (square x stimulus frame), centered on the middle of the screen. Note that squares disappear a bit off-screen, and are (re)initialized a bit off-screen. All locations are for the unwarped stimulus. | shape = (214200, 60) | dtype = int32
  Dataset /intervals/trials/square_locations_x_index (VectorIndex) Index for VectorData 'square_locations_x' | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/square_locations_y (VectorData) Locations along the y dimension (height) of square centers for each frame of the trial (in pixels), (square x stimulus frame), centered on the middle of the screen. Note that squares are (re)initialized a bit off-screen area. All locations are for the unwarped stimulus. | shape = (214200, 60) | dtype = int32
  Dataset /intervals/trials/square_locations_y_index (VectorIndex) Index for VectorData 'square_locations_y' | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/square_number (VectorData) Total number of squares present, both in the off and on-screen areas (before warping mask is applied). | shape = (8844,) | dtype = float64
  Dataset /intervals/trials/square_proportion_flipped (VectorData) Proportion of squares moving in the direction opposite to the main flow (all moving at 50 visual degrees/second). | shape = (8844,) | dtype = float64
  Dataset /intervals/trials/square_size (VectorData) Size of the squares (in pixels). | shape = (8844,) | dtype = float64
  Dataset /intervals/trials/start_frame_stim (VectorData) Start frame number for the stimulus frames. | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/start_frame_stim_template (VectorData) Start frame number for the trial in the corresponding template. | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/start_frame_twop (VectorData) Start frame number for the two-photon frames. | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (8844,) | dtype = float64
  Dataset /intervals/trials/stimulus_template_name (VectorData) Name of the stimulus template for the trial. | shape = (8844,) | dtype = object
  Dataset /intervals/trials/stimulus_type (VectorData) Type of stimulus presented during the trial. | shape = (8844,) | dtype = object
  Dataset /intervals/trials/stop_frame_stim (VectorData) Stop frame number for the stimulus frames (excluded). | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/stop_frame_twop (VectorData) Stop frame number for the two-photon frames (excluded). | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (8844,) | dtype = float64
  Dataset /intervals/trials/unexpected (VectorData) Whether the stimulus features are expected (0) or unexpected (1). | shape = (8844,) | dtype = float64
  Group /processing/behavior (ProcessingModule) preprocessed behavioral data
  Group /processing/behavior/BehavioralTimeSeries (BehavioralTimeSeries) 
  Group /processing/behavior/BehavioralTimeSeries/running_velocity (TimeSeries) Velocity of the mouse on a rotating disc.
  Group /processing/behavior/PupilTracking (PupilTracking) 
  Group /processing/behavior/PupilTracking/pupil_diameter (TimeSeries) Diameter of the mouse pupil (right) facing the stimulus presentation screen.
  Group /processing/behavior/PupilTracking/pupil_position_x (SpatialSeries) Position in x of the center of the mouse pupil (right) facing the stimulus presentation screen.
  Group /processing/behavior/PupilTracking/pupil_position_y (SpatialSeries) Position in y of the center of the mouse pupil (right) facing the stimulus presentation screen.
  Group /processing/ophys (ProcessingModule) OpenScope processing pipeline
  Group /processing/ophys/DfOverF (DfOverF) 
  Group /processing/ophys/DfOverF/RoiResponseSeries (RoiResponseSeries) Dendritic ROI traces obtained using booleanized masks.
  Dataset /processing/ophys/DfOverF/RoiResponseSeries/rois (DynamicTableRegion) Segmented dendrites (height x width) | shape = (942,) | dtype = int32
  Group /processing/ophys/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation (PlaneSegmentation) Segmentation for imaging plane optimized for dendritic ROI extraction (Inan et al., 2017, NIPS)
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/id (ElementIdentifiers)  | shape = (942,) | dtype = int32
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (942, 512, 512) | dtype = float64
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/device (Device) Allen Institute two-photon pipeline: CAM2P.1
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/optical_channel (OpticalChannel) 
  Group /processing/ophys/PlaneImages (Images) Plane images.
  Dataset /processing/ophys/PlaneImages/max_projection (GrayscaleImage) Normalized maximum projection of the motion corrected z-stack, averaged over 8 frames (hei x wid). | shape = (512, 512) | dtype = uint8
  session_description: Allen Institute OpenScope dataset
  session_start_time: 2018-10-01T18:02:56.523000-07:00
  Group /stimulus/presentation/gabors (IndexSeries) gabors index
  Group /stimulus/presentation/gabors/indexed_timeseries (ImageSeries) Template for Gabor sequence stimulus (frames x height x width x channels) (unwarped, masked)
  Group /stimulus/presentation/grayscreen (IndexSeries) grayscreen index
  Group /stimulus/presentation/grayscreen/indexed_timeseries (ImageSeries) Template for Grayscreen stimulus (frames x height x width x channels) (unwarped, masked)
  Group /stimulus/presentation/visflow_left (IndexSeries) visflow_left index
  Group /stimulus/presentation/visflow_left/indexed_timeseries (ImageSeries) Template for leftward (nasal) visual flow stimulus (frames x height x width x channels) (unwarped, masked)
  Group /stimulus/presentation/visflow_right (IndexSeries) visflow_right index
  Group /stimulus/presentation/visflow_right/indexed_timeseries (ImageSeries) Template for rightward (temporal) visual flow stimulus (frames x height x width x channels) (unwarped, masked)
  Group /stimulus/templates/gabors (ImageSeries) Template for Gabor sequence stimulus (frames x height x width x channels) (unwarped, masked)
  Group /stimulus/templates/grayscreen (ImageSeries) Template for Grayscreen stimulus (frames x height x width x channels) (unwarped, masked)
  Group /stimulus/templates/visflow_left (ImageSeries) Template for leftward (nasal) visual flow stimulus (frames x height x width x channels) (unwarped, masked)
  Group /stimulus/templates/visflow_right (ImageSeries) Template for rightward (temporal) visual flow stimulus (frames x height x width x channels) (unwarped, masked)
  timestamps_reference_time: 2018-10-01T18:02:56.523000-07:00


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2022-09-24T22:32:36.231878-07:00' '2023-04-03T21:37:43.217912-07:00']
  Group /general/devices/2p_microscope (Device) Allen Institute two-photon pipeline: CAM2P.1
  institution: Allen Institute for Brain Science
  Group /general/optophysiology/ImagingPlane (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane/device (Device) Allen Institute two-photon pipeline: CAM2P.1
  Group /general/optophysiology/ImagingPlane/optical_channel (OpticalChannel) 
  session_id: 759666166
  Group /general/subject (Subject) 
  identifier: 759666166
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/gabor_frame (VectorData) Gabor frame or set, defined by Gabor patch locations and sizes (A, B, C, D or U, G). | shape = (8844,) | dtype = object
  Dataset /intervals/trials/gabor_kappa (VectorData) Kappa (dispersion) of the von Mises distribution used to sample Gabor patch orientations (degrees). | shape = (8844,) | dtype = float64
  Dataset /intervals/trials/gabor_locations_x (VectorData) Locations along the x dimension (width) of the Gabor patch centers (in pixels), centered on the middle of the screen. All locations are for the unwarped stimulus. | shape = (163200,) | dtype = float64
  Dataset /intervals/trials/gabor_locations_x_index (VectorIndex) Index for VectorData 'gabor_locations_x' | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/gabor_locations_y (VectorData) Locations along the y dimension (height) of Gabor patch centers (in pixels), centered on the middle of the screen. All locations are for the unwarped stimulus. | shape = (163200,) | dtype = float64
  Dataset /intervals/trials/gabor_locations_y_index (VectorIndex) Index for VectorData 'gabor_locations_y' | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/gabor_mean_orientation (VectorData) Mean orientation of the von Mises distribution used to sample Gabor patch orientations (degrees, [0, 360]. | shape = (8844,) | dtype = float64
  Dataset /intervals/trials/gabor_number (VectorData) Number of Gabor patches on-screen (before warping mask is applied). | shape = (8844,) | dtype = float64
  Dataset /intervals/trials/gabor_orientations (VectorData) Orientations of the Gabor patches (degrees, [0, 360]). | shape = (163200,) | dtype = int16
  Dataset /intervals/trials/gabor_orientations_index (VectorIndex) Index for VectorData 'gabor_orientations' | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/gabor_sizes (VectorData) Gabor patch sizes (in pixels, with patch width defined, as in psychopy, as width across 6 standard deviations). | shape = (163200,) | dtype = int32
  Dataset /intervals/trials/gabor_sizes_index (VectorIndex) Index for VectorData 'gabor_sizes' | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/main_flow_direction (VectorData) Main direction of flow for the squares (all moving at 50 visual degrees/second). Flow directions are either rightward (nasal-to-temporal) or leftward (temporal-to-nasal). | shape = (8844,) | dtype = object
  Dataset /intervals/trials/num_frames_stim (VectorData) Stop frame number for the stimulus frames (excluded). | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/num_frames_twop (VectorData) Stop frame number for the two-photon frames (excluded). | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/square_locations_x (VectorData) Locations along the x dimension (width) of square centers for each frame of the trial (in pixels), (square x stimulus frame), centered on the middle of the screen. Note that squares disappear a bit off-screen, and are (re)initialized a bit off-screen. All locations are for the unwarped stimulus. | shape = (214200, 60) | dtype = int32
  Dataset /intervals/trials/square_locations_x_index (VectorIndex) Index for VectorData 'square_locations_x' | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/square_locations_y (VectorData) Locations along the y dimension (height) of square centers for each frame of the trial (in pixels), (square x stimulus frame), centered on the middle of the screen. Note that squares are (re)initialized a bit off-screen area. All locations are for the unwarped stimulus. | shape = (214200, 60) | dtype = int32
  Dataset /intervals/trials/square_locations_y_index (VectorIndex) Index for VectorData 'square_locations_y' | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/square_number (VectorData) Total number of squares present, both in the off and on-screen areas (before warping mask is applied). | shape = (8844,) | dtype = float64
  Dataset /intervals/trials/square_proportion_flipped (VectorData) Proportion of squares moving in the direction opposite to the main flow (all moving at 50 visual degrees/second). | shape = (8844,) | dtype = float64
  Dataset /intervals/trials/square_size (VectorData) Size of the squares (in pixels). | shape = (8844,) | dtype = float64
  Dataset /intervals/trials/start_frame_stim (VectorData) Start frame number for the stimulus frames. | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/start_frame_stim_template (VectorData) Start frame number for the trial in the corresponding template. | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/start_frame_twop (VectorData) Start frame number for the two-photon frames. | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (8844,) | dtype = float64
  Dataset /intervals/trials/stimulus_template_name (VectorData) Name of the stimulus template for the trial. | shape = (8844,) | dtype = object
  Dataset /intervals/trials/stimulus_type (VectorData) Type of stimulus presented during the trial. | shape = (8844,) | dtype = object
  Dataset /intervals/trials/stop_frame_stim (VectorData) Stop frame number for the stimulus frames (excluded). | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/stop_frame_twop (VectorData) Stop frame number for the two-photon frames (excluded). | shape = (8844,) | dtype = int32
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (8844,) | dtype = float64
  Dataset /intervals/trials/unexpected (VectorData) Whether the stimulus features are expected (0) or unexpected (1). | shape = (8844,) | dtype = float64
  Group /processing/behavior (ProcessingModule) preprocessed behavioral data
  Group /processing/behavior/BehavioralTimeSeries (BehavioralTimeSeries) 
  Group /processing/behavior/BehavioralTimeSeries/running_velocity (TimeSeries) Velocity of the mouse on a rotating disc.
  Group /processing/behavior/PupilTracking (PupilTracking) 
  Group /processing/behavior/PupilTracking/pupil_diameter (TimeSeries) Diameter of the mouse pupil (right) facing the stimulus presentation screen.
  Group /processing/behavior/PupilTracking/pupil_position_x (SpatialSeries) Position in x of the center of the mouse pupil (right) facing the stimulus presentation screen.
  Group /processing/behavior/PupilTracking/pupil_position_y (SpatialSeries) Position in y of the center of the mouse pupil (right) facing the stimulus presentation screen.
  Group /processing/ophys (ProcessingModule) OpenScope processing pipeline
  Group /processing/ophys/DfOverF (DfOverF) 
  Group /processing/ophys/DfOverF/RoiResponseSeries (RoiResponseSeries) Dendritic ROI traces obtained using booleanized masks.
  Dataset /processing/ophys/DfOverF/RoiResponseSeries/rois (DynamicTableRegion) Segmented dendrites (height x width) | shape = (942,) | dtype = int32
  Group /processing/ophys/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation (PlaneSegmentation) Segmentation for imaging plane optimized for dendritic ROI extraction (Inan et al., 2017, NIPS)
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/id (ElementIdentifiers)  | shape = (942,) | dtype = int32
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (942, 512, 512) | dtype = float64
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/device (Device) Allen Institute two-photon pipeline: CAM2P.1
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/optical_channel (OpticalChannel) 
  Group /processing/ophys/PlaneImages (Images) Plane images.
  Dataset /processing/ophys/PlaneImages/max_projection (GrayscaleImage) Normalized maximum projection of the motion corrected z-stack, averaged over 8 frames (hei x wid). | shape = (512, 512) | dtype = uint8
  session_description: Allen Institute OpenScope dataset
  session_start_time: 2018-10-01T18:02:56.523000-07:00
  timestamps_reference_time: 2018-10-01T18:02:56.523000-07:00
