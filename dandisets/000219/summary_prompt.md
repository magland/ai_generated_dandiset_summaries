
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000219/draft
name: Two photon calcium imaging in the CA1 region of the hippocampus in neonatal mice.
contributor: [{'name': 'Dard, Robin', 'email': 'robin.dard@inserm.fr', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}]
description: We performed in vivo 2-photon calcium imaging in the CA1 region of the hippocampus in awake mouse pups aged between 5 and 12 days postnatal. We used GCaMP6s calcium indicator in WT mice or GCaMP6s and flex-tdTomato in GadCre mice to record calcium dynamics from both pyramidal cells and interneurons. The imaging data set was acquired at 8 Hz, in field of view of 400x400 µm. Simultaneously with imaging, we record the spontaneous motor behavior of the mouse pups.
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}, {'name': 'behavioral approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 73147035938, 'numberOfFiles': 62, 'numberOfSubjects': 35, 'variableMeasured': ['BehavioralEpochs', 'PlaneSegmentation', 'BehavioralTimeSeries', 'ProcessingModule'], 'measurementTechnique': [{'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000219 has 26 NWB files.
2 of these NWB files are of type 1.
1 of these NWB files are of type 2.
16 of these NWB files are of type 3.
5 of these NWB files are of type 4.
2 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ci_frames (TimeSeries) no description
  Group /acquisition/motion_corrected_ci_movie (TwoPhotonSeries) no description
  Group /acquisition/motion_corrected_ci_movie/imaging_plane (ImagingPlane) 
  Group /acquisition/motion_corrected_ci_movie/imaging_plane/device (Device) 
  Group /acquisition/motion_corrected_ci_movie/imaging_plane/my_optchan (OpticalChannel) 
  file_create_date: ['2022-02-20T19:46:50.158511+01:00']
  Group /general/devices/2P_device (Device) 
  experiment_description: In-vivo 2P calcium imaging on head fixed mouse pup
  experimenter: ['RD']
  institution: INMED - INSERMU1249
  keywords: ['pup' 'calcium imaging']
  notes: No given note for this NWB
  Group /general/optophysiology/my_imgpln (ImagingPlane) 
  Group /general/optophysiology/my_imgpln/device (Device) 
  Group /general/optophysiology/my_imgpln/my_optchan (OpticalChannel) 
  pharmacology: Anesthesia: Isoflurane 1-3% in a 90% O2 / 10% air mix,  Painkillers: Buprenorphine [0.05-0.1] mg.kg-1
  session_id: 171110_a000
  Group /general/subject (Subject) 
  surgery: Performed by RD on 11/10/17
  identifier: P12D_171029_171110_171110_a000
  Group /intervals/ci_recording_on_pause (TimeIntervals) Intervals that correspond to the time of last frame recorded before the pause, and stop_time is the time of the first frame recorded after the pause, during calcium imagingrecording.
  Dataset /intervals/ci_recording_on_pause/id (ElementIdentifiers)  | shape = (4,) | dtype = int32
  Dataset /intervals/ci_recording_on_pause/start_original_frame (VectorData) Frame after which the pause starts, using frames from theoriginal concatenated movie | shape = (4,) | dtype = int64
  Dataset /intervals/ci_recording_on_pause/start_time (VectorData) Start time of epoch, in seconds | shape = (4,) | dtype = float64
  Dataset /intervals/ci_recording_on_pause/stop_original_frame (VectorData) Frame at which the pause ends, using frames from the original concatenated movie | shape = (4,) | dtype = int64
  Dataset /intervals/ci_recording_on_pause/stop_time (VectorData) Stop time of epoch, in seconds | shape = (4,) | dtype = float64
  Group /intervals/invalid_times (TimeIntervals) time intervals to be removed from analysis
  Dataset /intervals/invalid_times/id (ElementIdentifiers)  | shape = (4,) | dtype = int32
  Dataset /intervals/invalid_times/start_time (VectorData) Start time of epoch, in seconds | shape = (4,) | dtype = float64
  Dataset /intervals/invalid_times/stop_time (VectorData) Stop time of epoch, in seconds | shape = (4,) | dtype = float64
  Group /processing/behavior (ProcessingModule) behavioral data
  Group /processing/behavior/BehavioralEpochs (BehavioralEpochs) 
  Group /processing/behavior/BehavioralEpochs/long_movement (IntervalSeries) time intervals during which long movements happen
  Group /processing/behavior/BehavioralEpochs/twitches (IntervalSeries) time intervals during which twitches happen
  Group /processing/behavior/BehavioralEpochs/unclassified_movement (IntervalSeries) time intervals during which unclassified movements happen
  Group /processing/ophys (ProcessingModule) contains optical physiology processed data
  Group /processing/ophys/all_cells (ImageSegmentation) 
  Group /processing/ophys/all_cells/my_plane_seg (PlaneSegmentation) output from segmenting
  Dataset /processing/ophys/all_cells/my_plane_seg/id (ElementIdentifiers)  | shape = (404,) | dtype = int32
  Dataset /processing/ophys/all_cells/my_plane_seg/image_mask (VectorData) Image masks for each ROI | shape = (404, 180, 175) | dtype = float64
  Group /processing/ophys/all_cells/my_plane_seg/imaging_plane (ImagingPlane) 
  Group /processing/ophys/all_cells/my_plane_seg/imaging_plane/device (Device) 
  Group /processing/ophys/all_cells/my_plane_seg/imaging_plane/my_optchan (OpticalChannel) 
  Dataset /processing/ophys/all_cells/my_plane_seg/pixel_mask (VectorData) Pixel masks for each ROI | shape = (15789,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/all_cells/my_plane_seg/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (404,) | dtype = uint16
  Group /processing/ophys/all_cells/my_plane_seg/reference_images/motion_corrected_ci_movie (TwoPhotonSeries) no description
  Group /processing/ophys/all_cells/my_plane_seg/reference_images/motion_corrected_ci_movie/imaging_plane (ImagingPlane) 
  Group /processing/ophys/all_cells/my_plane_seg/reference_images/motion_corrected_ci_movie/imaging_plane/device (Device) 
  Group /processing/ophys/all_cells/my_plane_seg/reference_images/motion_corrected_ci_movie/imaging_plane/my_optchan (OpticalChannel) 
  Group /processing/ophys/fluorescence_all_cells (Fluorescence) 
  Group /processing/ophys/fluorescence_all_cells/raster dur v26_5_v37_6 (RoiResponseSeries) raster dur v26_5_v37_6
  Dataset /processing/ophys/fluorescence_all_cells/raster dur v26_5_v37_6/rois (DynamicTableRegion) all cells | shape = (404,) | dtype = int32
  Group /processing/ophys/fluorescence_all_cells/raw_traces (RoiResponseSeries) raw traces
  Dataset /processing/ophys/fluorescence_all_cells/raw_traces/rois (DynamicTableRegion) all cells | shape = (404,) | dtype = int32
  Group /processing/ophys/fluorescence_all_cells/raw_traces_wo (RoiResponseSeries) raw traces without overlap
  Dataset /processing/ophys/fluorescence_all_cells/raw_traces_wo/rois (DynamicTableRegion) all cells | shape = (404,) | dtype = int32
  session_description: Session: 171110_a000, from subject: 171029_171110
  session_start_time: 2017-11-10T00:00:00+01:00
  timestamps_reference_time: 2017-11-10T00:00:00+01:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ci_frames (TimeSeries) no description
  Group /acquisition/motion_corrected_ci_movie (TwoPhotonSeries) no description
  Group /acquisition/motion_corrected_ci_movie/imaging_plane (ImagingPlane) 
  Group /acquisition/motion_corrected_ci_movie/imaging_plane/device (Device) 
  Group /acquisition/motion_corrected_ci_movie/imaging_plane/my_optchan (OpticalChannel) 
  file_create_date: ['2022-02-20T19:47:25.074821+01:00']
  Group /general/devices/2P_device (Device) 
  experiment_description: In-vivo 2P calcium imaging on head fixed mouse pup
  experimenter: ['RD']
  institution: INMED - INSERMU1249
  keywords: ['pup' 'calcium imaging']
  notes: No given note for this NWB
  Group /general/optophysiology/my_imgpln (ImagingPlane) 
  Group /general/optophysiology/my_imgpln/device (Device) 
  Group /general/optophysiology/my_imgpln/my_optchan (OpticalChannel) 
  pharmacology: Anesthesia: Isoflurane 1-3% in a 90% O2 / 10% air mix,  Painkillers: Buprenorphine [0.05-0.1] mg.kg-1
  session_id: 171110_a002
  Group /general/subject (Subject) 
  surgery: Performed by RD on 11/10/17
  identifier: P12D_171029_171110_171110_a002
  Group /intervals/ci_recording_on_pause (TimeIntervals) Intervals that correspond to the time of last frame recorded before the pause, and stop_time is the time of the first frame recorded after the pause, during calcium imagingrecording.
  Dataset /intervals/ci_recording_on_pause/id (ElementIdentifiers)  | shape = (4,) | dtype = int32
  Dataset /intervals/ci_recording_on_pause/start_original_frame (VectorData) Frame after which the pause starts, using frames from theoriginal concatenated movie | shape = (4,) | dtype = int64
  Dataset /intervals/ci_recording_on_pause/start_time (VectorData) Start time of epoch, in seconds | shape = (4,) | dtype = float64
  Dataset /intervals/ci_recording_on_pause/stop_original_frame (VectorData) Frame at which the pause ends, using frames from the original concatenated movie | shape = (4,) | dtype = int64
  Dataset /intervals/ci_recording_on_pause/stop_time (VectorData) Stop time of epoch, in seconds | shape = (4,) | dtype = float64
  Group /intervals/invalid_times (TimeIntervals) time intervals to be removed from analysis
  Dataset /intervals/invalid_times/id (ElementIdentifiers)  | shape = (4,) | dtype = int32
  Dataset /intervals/invalid_times/start_time (VectorData) Start time of epoch, in seconds | shape = (4,) | dtype = float64
  Dataset /intervals/invalid_times/stop_time (VectorData) Stop time of epoch, in seconds | shape = (4,) | dtype = float64
  Group /processing/ophys (ProcessingModule) contains optical physiology processed data
  Group /processing/ophys/all_cells (ImageSegmentation) 
  Group /processing/ophys/all_cells/my_plane_seg (PlaneSegmentation) output from segmenting
  Dataset /processing/ophys/all_cells/my_plane_seg/id (ElementIdentifiers)  | shape = (654,) | dtype = int32
  Dataset /processing/ophys/all_cells/my_plane_seg/image_mask (VectorData) Image masks for each ROI | shape = (654, 195, 194) | dtype = float64
  Group /processing/ophys/all_cells/my_plane_seg/imaging_plane (ImagingPlane) 
  Group /processing/ophys/all_cells/my_plane_seg/imaging_plane/device (Device) 
  Group /processing/ophys/all_cells/my_plane_seg/imaging_plane/my_optchan (OpticalChannel) 
  Dataset /processing/ophys/all_cells/my_plane_seg/pixel_mask (VectorData) Pixel masks for each ROI | shape = (22868,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/all_cells/my_plane_seg/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (654,) | dtype = uint16
  Group /processing/ophys/all_cells/my_plane_seg/reference_images/motion_corrected_ci_movie (TwoPhotonSeries) no description
  Group /processing/ophys/all_cells/my_plane_seg/reference_images/motion_corrected_ci_movie/imaging_plane (ImagingPlane) 
  Group /processing/ophys/all_cells/my_plane_seg/reference_images/motion_corrected_ci_movie/imaging_plane/device (Device) 
  Group /processing/ophys/all_cells/my_plane_seg/reference_images/motion_corrected_ci_movie/imaging_plane/my_optchan (OpticalChannel) 
  Group /processing/ophys/fluorescence_all_cells (Fluorescence) 
  Group /processing/ophys/fluorescence_all_cells/raster dur v26_5_v37_6 (RoiResponseSeries) raster dur v26_5_v37_6
  Dataset /processing/ophys/fluorescence_all_cells/raster dur v26_5_v37_6/rois (DynamicTableRegion) all cells | shape = (654,) | dtype = int32
  Group /processing/ophys/fluorescence_all_cells/raw_traces (RoiResponseSeries) raw traces
  Dataset /processing/ophys/fluorescence_all_cells/raw_traces/rois (DynamicTableRegion) all cells | shape = (654,) | dtype = int32
  Group /processing/ophys/fluorescence_all_cells/raw_traces_wo (RoiResponseSeries) raw traces without overlap
  Dataset /processing/ophys/fluorescence_all_cells/raw_traces_wo/rois (DynamicTableRegion) all cells | shape = (654,) | dtype = int32
  Group /processing/ophys/fluorescence_all_cells/spks_suite2p (RoiResponseSeries) deconvolved traces from suite2p
  Dataset /processing/ophys/fluorescence_all_cells/spks_suite2p/rois (DynamicTableRegion) all cells | shape = (654,) | dtype = int32
  session_description: Session: 171110_a002, from subject: 171029_171110
  session_start_time: 2017-11-10T00:00:00+01:00
  timestamps_reference_time: 2017-11-10T00:00:00+01:00


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ci_frames (TimeSeries) no description
  Group /acquisition/motion_corrected_ci_movie (TwoPhotonSeries) no description
  Group /acquisition/motion_corrected_ci_movie/imaging_plane (ImagingPlane) 
  Group /acquisition/motion_corrected_ci_movie/imaging_plane/device (Device) 
  Group /acquisition/motion_corrected_ci_movie/imaging_plane/my_optchan (OpticalChannel) 
  file_create_date: ['2022-02-20T19:48:01.374645+01:00']
  Group /general/devices/2P_device (Device) 
  experiment_description: In-vivo 2P calcium imaging on head fixed mouse pup
  experimenter: ['RD']
  institution: INMED - INSERMU1249
  keywords: ['pup' 'calcium imaging']
  notes: No given note for this NWB
  Group /general/optophysiology/my_imgpln (ImagingPlane) 
  Group /general/optophysiology/my_imgpln/device (Device) 
  Group /general/optophysiology/my_imgpln/my_optchan (OpticalChannel) 
  pharmacology: Anesthesia: Isoflurane 1-3% in a 90% O2 / 10% air mix,  Painkillers: Buprenorphine [0.05-0.1] mg.kg-1
  session_id: 171220_a001
  Group /general/subject (Subject) 
  surgery: Performed by RD on 12/20/17
  virus: Age at injection: p0, Injection-site: ventricle, VirusID: AAV1.Syn.GCaMP6s.WPRE.SV40, Volume: 2 uL, Expression/Labelling: Diluted x2, Source: Addgene
  identifier: P9D_171211_171220_171220_a001
  Group /intervals/ci_recording_on_pause (TimeIntervals) Intervals that correspond to the time of last frame recorded before the pause, and stop_time is the time of the first frame recorded after the pause, during calcium imagingrecording.
  Dataset /intervals/ci_recording_on_pause/id (ElementIdentifiers)  | shape = (4,) | dtype = int32
  Dataset /intervals/ci_recording_on_pause/start_original_frame (VectorData) Frame after which the pause starts, using frames from theoriginal concatenated movie | shape = (4,) | dtype = int64
  Dataset /intervals/ci_recording_on_pause/start_time (VectorData) Start time of epoch, in seconds | shape = (4,) | dtype = float64
  Dataset /intervals/ci_recording_on_pause/stop_original_frame (VectorData) Frame at which the pause ends, using frames from the original concatenated movie | shape = (4,) | dtype = int64
  Dataset /intervals/ci_recording_on_pause/stop_time (VectorData) Stop time of epoch, in seconds | shape = (4,) | dtype = float64
  Group /intervals/invalid_times (TimeIntervals) time intervals to be removed from analysis
  Dataset /intervals/invalid_times/id (ElementIdentifiers)  | shape = (4,) | dtype = int32
  Dataset /intervals/invalid_times/start_time (VectorData) Start time of epoch, in seconds | shape = (4,) | dtype = float64
  Dataset /intervals/invalid_times/stop_time (VectorData) Stop time of epoch, in seconds | shape = (4,) | dtype = float64
  Group /processing/behavior (ProcessingModule) behavioral data
  Group /processing/behavior/BehavioralEpochs (BehavioralEpochs) 
  Group /processing/behavior/BehavioralEpochs/long_movement (IntervalSeries) time intervals during which long movements happen
  Group /processing/behavior/BehavioralEpochs/twitches (IntervalSeries) time intervals during which twitches happen
  Group /processing/behavior/BehavioralEpochs/unclassified_movement (IntervalSeries) time intervals during which unclassified movements happen
  Group /processing/behavior/BehavioralTimeSeries (BehavioralTimeSeries) 
  Group /processing/behavior/BehavioralTimeSeries/piezo_0 (TimeSeries) no description
  Group /processing/ophys (ProcessingModule) contains optical physiology processed data
  Group /processing/ophys/all_cells (ImageSegmentation) 
  Group /processing/ophys/all_cells/my_plane_seg (PlaneSegmentation) output from segmenting
  Dataset /processing/ophys/all_cells/my_plane_seg/id (ElementIdentifiers)  | shape = (372,) | dtype = int32
  Dataset /processing/ophys/all_cells/my_plane_seg/image_mask (VectorData) Image masks for each ROI | shape = (372, 160, 171) | dtype = float64
  Group /processing/ophys/all_cells/my_plane_seg/imaging_plane (ImagingPlane) 
  Group /processing/ophys/all_cells/my_plane_seg/imaging_plane/device (Device) 
  Group /processing/ophys/all_cells/my_plane_seg/imaging_plane/my_optchan (OpticalChannel) 
  Dataset /processing/ophys/all_cells/my_plane_seg/pixel_mask (VectorData) Pixel masks for each ROI | shape = (17770,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/all_cells/my_plane_seg/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (372,) | dtype = uint16
  Group /processing/ophys/all_cells/my_plane_seg/reference_images/motion_corrected_ci_movie (TwoPhotonSeries) no description
  Group /processing/ophys/all_cells/my_plane_seg/reference_images/motion_corrected_ci_movie/imaging_plane (ImagingPlane) 
  Group /processing/ophys/all_cells/my_plane_seg/reference_images/motion_corrected_ci_movie/imaging_plane/device (Device) 
  Group /processing/ophys/all_cells/my_plane_seg/reference_images/motion_corrected_ci_movie/imaging_plane/my_optchan (OpticalChannel) 
  Group /processing/ophys/fluorescence_all_cells (Fluorescence) 
  Group /processing/ophys/fluorescence_all_cells/raster dur v26_5_v37_6 (RoiResponseSeries) raster dur v26_5_v37_6
  Dataset /processing/ophys/fluorescence_all_cells/raster dur v26_5_v37_6/rois (DynamicTableRegion) all cells | shape = (372,) | dtype = int32
  Group /processing/ophys/fluorescence_all_cells/raw_traces (RoiResponseSeries) raw traces
  Dataset /processing/ophys/fluorescence_all_cells/raw_traces/rois (DynamicTableRegion) all cells | shape = (372,) | dtype = int32
  Group /processing/ophys/fluorescence_all_cells/raw_traces_wo (RoiResponseSeries) raw traces without overlap
  Dataset /processing/ophys/fluorescence_all_cells/raw_traces_wo/rois (DynamicTableRegion) all cells | shape = (372,) | dtype = int32
  session_description: Session: 171220_a001, from subject: 171211_171220
  session_start_time: 2017-12-20T00:00:00+01:00
  timestamps_reference_time: 2017-12-20T00:00:00+01:00


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ci_frames (TimeSeries) no description
  Group /acquisition/motion_corrected_ci_movie (TwoPhotonSeries) no description
  Group /acquisition/motion_corrected_ci_movie/imaging_plane (ImagingPlane) 
  Group /acquisition/motion_corrected_ci_movie/imaging_plane/device (Device) 
  Group /acquisition/motion_corrected_ci_movie/imaging_plane/my_optchan (OpticalChannel) 
  file_create_date: ['2022-02-20T19:50:10.880179+01:00']
  Group /general/devices/2P_device (Device) 
  experiment_description: In-vivo 2P calcium imaging on head fixed mouse pup
  experimenter: ['RD']
  institution: INMED - INSERMU1249
  keywords: ['pup' 'calcium imaging']
  notes: No given note for this NWB
  Group /general/optophysiology/my_imgpln (ImagingPlane) 
  Group /general/optophysiology/my_imgpln/device (Device) 
  Group /general/optophysiology/my_imgpln/my_optchan (OpticalChannel) 
  pharmacology: Anesthesia: Isoflurane 1-3% in a 90% O2 / 10% air mix,  Painkillers: Buprenorphine [0.05-0.1] mg.kg-1
  session_id: 180208_a002
  Group /general/subject (Subject) 
  surgery: Performed by RD on 02/08/18
  virus: Age at injection: p0, Injection-site: ventricle, VirusID: AAV1.Syn.GCaMP6s.WPRE.SV40, Volume: 2 uL, Expression/Labelling: Good, Source: Addgene
  identifier: P7D_180201_180208_180208_a002
  Group /intervals/ci_recording_on_pause (TimeIntervals) Intervals that correspond to the time of last frame recorded before the pause, and stop_time is the time of the first frame recorded after the pause, during calcium imagingrecording.
  Dataset /intervals/ci_recording_on_pause/id (ElementIdentifiers)  | shape = (4,) | dtype = int32
  Dataset /intervals/ci_recording_on_pause/start_original_frame (VectorData) Frame after which the pause starts, using frames from theoriginal concatenated movie | shape = (4,) | dtype = int64
  Dataset /intervals/ci_recording_on_pause/start_time (VectorData) Start time of epoch, in seconds | shape = (4,) | dtype = float64
  Dataset /intervals/ci_recording_on_pause/stop_original_frame (VectorData) Frame at which the pause ends, using frames from the original concatenated movie | shape = (4,) | dtype = int64
  Dataset /intervals/ci_recording_on_pause/stop_time (VectorData) Stop time of epoch, in seconds | shape = (4,) | dtype = float64
  Group /intervals/invalid_times (TimeIntervals) time intervals to be removed from analysis
  Dataset /intervals/invalid_times/id (ElementIdentifiers)  | shape = (4,) | dtype = int32
  Dataset /intervals/invalid_times/start_time (VectorData) Start time of epoch, in seconds | shape = (4,) | dtype = float64
  Dataset /intervals/invalid_times/stop_time (VectorData) Stop time of epoch, in seconds | shape = (4,) | dtype = float64
  Group /processing/behavior (ProcessingModule) behavioral data
  Group /processing/behavior/BehavioralEpochs (BehavioralEpochs) 
  Group /processing/behavior/BehavioralEpochs/long_movement (IntervalSeries) time intervals during which long movements happen
  Group /processing/behavior/BehavioralEpochs/twitches (IntervalSeries) time intervals during which twitches happen
  Group /processing/behavior/BehavioralEpochs/unclassified_movement (IntervalSeries) time intervals during which unclassified movements happen
  Group /processing/behavior/BehavioralTimeSeries (BehavioralTimeSeries) 
  Group /processing/behavior/BehavioralTimeSeries/piezo_0 (TimeSeries) no description
  Group /processing/ophys (ProcessingModule) contains optical physiology processed data
  Group /processing/ophys/all_cells (ImageSegmentation) 
  Group /processing/ophys/all_cells/my_plane_seg (PlaneSegmentation) output from segmenting
  Dataset /processing/ophys/all_cells/my_plane_seg/id (ElementIdentifiers)  | shape = (742,) | dtype = int32
  Dataset /processing/ophys/all_cells/my_plane_seg/image_mask (VectorData) Image masks for each ROI | shape = (742, 161, 167) | dtype = float64
  Group /processing/ophys/all_cells/my_plane_seg/imaging_plane (ImagingPlane) 
  Group /processing/ophys/all_cells/my_plane_seg/imaging_plane/device (Device) 
  Group /processing/ophys/all_cells/my_plane_seg/imaging_plane/my_optchan (OpticalChannel) 
  Dataset /processing/ophys/all_cells/my_plane_seg/pixel_mask (VectorData) Pixel masks for each ROI | shape = (25863,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/all_cells/my_plane_seg/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (742,) | dtype = uint16
  Group /processing/ophys/all_cells/my_plane_seg/reference_images/motion_corrected_ci_movie (TwoPhotonSeries) no description
  Group /processing/ophys/all_cells/my_plane_seg/reference_images/motion_corrected_ci_movie/imaging_plane (ImagingPlane) 
  Group /processing/ophys/all_cells/my_plane_seg/reference_images/motion_corrected_ci_movie/imaging_plane/device (Device) 
  Group /processing/ophys/all_cells/my_plane_seg/reference_images/motion_corrected_ci_movie/imaging_plane/my_optchan (OpticalChannel) 
  Group /processing/ophys/fluorescence_all_cells (Fluorescence) 
  Group /processing/ophys/fluorescence_all_cells/raster dur v26_5_v37_6 (RoiResponseSeries) raster dur v26_5_v37_6
  Dataset /processing/ophys/fluorescence_all_cells/raster dur v26_5_v37_6/rois (DynamicTableRegion) all cells | shape = (742,) | dtype = int32
  Group /processing/ophys/fluorescence_all_cells/raw_traces (RoiResponseSeries) raw traces
  Dataset /processing/ophys/fluorescence_all_cells/raw_traces/rois (DynamicTableRegion) all cells | shape = (742,) | dtype = int32
  Group /processing/ophys/fluorescence_all_cells/raw_traces_wo (RoiResponseSeries) raw traces without overlap
  Dataset /processing/ophys/fluorescence_all_cells/raw_traces_wo/rois (DynamicTableRegion) all cells | shape = (742,) | dtype = int32
  Group /processing/ophys/fluorescence_all_cells/spks_suite2p (RoiResponseSeries) deconvolved traces from suite2p
  Dataset /processing/ophys/fluorescence_all_cells/spks_suite2p/rois (DynamicTableRegion) all cells | shape = (742,) | dtype = int32
  session_description: Session: 180208_a002, from subject: 180201_180208
  session_start_time: 2018-02-08T00:00:00+01:00
  timestamps_reference_time: 2018-02-08T00:00:00+01:00


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ci_frames (TimeSeries) no description
  Group /acquisition/motion_corrected_ci_movie (TwoPhotonSeries) no description
  Group /acquisition/motion_corrected_ci_movie/imaging_plane (ImagingPlane) 
  Group /acquisition/motion_corrected_ci_movie/imaging_plane/device (Device) 
  Group /acquisition/motion_corrected_ci_movie/imaging_plane/my_optchan (OpticalChannel) 
  file_create_date: ['2022-02-20T19:51:13.019223+01:00']
  Group /general/devices/2P_device (Device) 
  experiment_description: In-vivo 2P calcium imaging on head fixed mouse pup
  experimenter: ['RD']
  institution: INMED - INSERMU1249
  keywords: ['pup' 'calcium imaging']
  notes: No given note for this NWB
  Group /general/optophysiology/my_imgpln (ImagingPlane) 
  Group /general/optophysiology/my_imgpln/device (Device) 
  Group /general/optophysiology/my_imgpln/my_optchan (OpticalChannel) 
  pharmacology: Anesthesia: Isoflurane 1-3% in a 90% O2 / 10% air mix,  Painkillers: Buprenorphine [0.05-0.1] mg.kg-1
  session_id: 181017_a000
  Group /general/subject (Subject) 
  surgery: Performed by RD on 10/17/18
  virus: Age at injection: p0, Injection-site: ventricle, VirusID: AAV1.Syn.GCaMP6s.WPRE.SV40, Volume: 2 uL, Expression/Labelling: Good, Source: Addgene
  identifier: P8D_181009_181017_181017_a000
  Group /processing/behavior (ProcessingModule) behavioral data
  Group /processing/behavior/BehavioralEpochs (BehavioralEpochs) 
  Group /processing/behavior/BehavioralEpochs/long_movement (IntervalSeries) time intervals during which long movements happen
  Group /processing/behavior/BehavioralEpochs/twitches (IntervalSeries) time intervals during which twitches happen
  Group /processing/behavior/BehavioralEpochs/unclassified_movement (IntervalSeries) time intervals during which unclassified movements happen
  Group /processing/behavior/BehavioralTimeSeries (BehavioralTimeSeries) 
  Group /processing/behavior/BehavioralTimeSeries/piezo_0 (TimeSeries) no description
  Group /processing/ophys (ProcessingModule) contains optical physiology processed data
  Group /processing/ophys/all_cells (ImageSegmentation) 
  Group /processing/ophys/all_cells/my_plane_seg (PlaneSegmentation) output from segmenting
  Dataset /processing/ophys/all_cells/my_plane_seg/id (ElementIdentifiers)  | shape = (627,) | dtype = int32
  Dataset /processing/ophys/all_cells/my_plane_seg/image_mask (VectorData) Image masks for each ROI | shape = (627, 169, 166) | dtype = float64
  Group /processing/ophys/all_cells/my_plane_seg/imaging_plane (ImagingPlane) 
  Group /processing/ophys/all_cells/my_plane_seg/imaging_plane/device (Device) 
  Group /processing/ophys/all_cells/my_plane_seg/imaging_plane/my_optchan (OpticalChannel) 
  Dataset /processing/ophys/all_cells/my_plane_seg/pixel_mask (VectorData) Pixel masks for each ROI | shape = (23416,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/all_cells/my_plane_seg/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (627,) | dtype = uint16
  Group /processing/ophys/all_cells/my_plane_seg/reference_images/motion_corrected_ci_movie (TwoPhotonSeries) no description
  Group /processing/ophys/all_cells/my_plane_seg/reference_images/motion_corrected_ci_movie/imaging_plane (ImagingPlane) 
  Group /processing/ophys/all_cells/my_plane_seg/reference_images/motion_corrected_ci_movie/imaging_plane/device (Device) 
  Group /processing/ophys/all_cells/my_plane_seg/reference_images/motion_corrected_ci_movie/imaging_plane/my_optchan (OpticalChannel) 
  Group /processing/ophys/fluorescence_all_cells (Fluorescence) 
  Group /processing/ophys/fluorescence_all_cells/raster dur v26_5_v37_6 (RoiResponseSeries) raster dur v26_5_v37_6
  Dataset /processing/ophys/fluorescence_all_cells/raster dur v26_5_v37_6/rois (DynamicTableRegion) all cells | shape = (627,) | dtype = int32
  Group /processing/ophys/fluorescence_all_cells/raw_traces (RoiResponseSeries) raw traces
  Dataset /processing/ophys/fluorescence_all_cells/raw_traces/rois (DynamicTableRegion) all cells | shape = (627,) | dtype = int32
  Group /processing/ophys/fluorescence_all_cells/raw_traces_wo (RoiResponseSeries) raw traces without overlap
  Dataset /processing/ophys/fluorescence_all_cells/raw_traces_wo/rois (DynamicTableRegion) all cells | shape = (627,) | dtype = int32
  session_description: Session: 181017_a000, from subject: 181009_181017
  session_start_time: 2018-10-17T00:00:00+02:00
  timestamps_reference_time: 2018-10-17T00:00:00+02:00
