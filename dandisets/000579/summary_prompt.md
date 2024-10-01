
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000579/0.230728.1727
name: Two-photon calcium imaging of mouse posterior cortical areas during dynamic navigation decisions (Tseng et al., 2022, Neuron)
contributor: [{'name': 'Tseng, Shih-Yi', 'email': 'shihyitseng41@gmail.com', 'roleName': ['dcite:ContactPerson', 'dcite:Author', 'dcite:DataCollector', 'dcite:DataCurator', 'dcite:DataManager', 'dcite:FormalAnalysis', 'dcite:Conceptualization'], 'schemaKey': 'Person', 'identifier': '0000-0002-5029-433X', 'affiliation': [{'name': 'Harvard Medical School', 'schemaKey': 'Affiliation'}], 'includeInCitation': True}, {'name': 'Chettih, Selmaan', 'roleName': ['dcite:Author', 'dcite:Conceptualization'], 'schemaKey': 'Person', 'identifier': '0000-0003-2045-3747', 'affiliation': [{'name': 'Harvard Medical School', 'schemaKey': 'Affiliation'}], 'includeInCitation': True}, {'name': 'Harvey, Christopher', 'email': 'Christopher_Harvey@hms.harvard.edu ', 'roleName': ['dcite:Conceptualization', 'dcite:FundingAcquisition', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0001-9850-2268', 'affiliation': [{'name': 'Harvard Medical School', 'schemaKey': 'Affiliation'}], 'includeInCitation': True}, {'url': 'http://www.nih.gov/', 'name': 'National Institutes of Health Director’s Pioneer Award', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01cwqze88', 'awardNumber': 'DP1 MH125776', 'contactPoint': [], 'includeInCitation': False}, {'url': 'https://www.ninds.nih.gov/', 'name': 'National Institute of Neurological Disorders and Stroke', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01s5ya894', 'awardNumber': 'R01 NS089521', 'contactPoint': [], 'includeInCitation': False}, {'url': 'https://www.nimh.nih.gov/', 'name': 'National Institute of Mental Health', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/04xeg9z08', 'awardNumber': 'R01 MH107620', 'contactPoint': [], 'includeInCitation': False}, {'url': 'https://braininitiative.nih.gov/', 'name': 'National Institutes of Health BRAIN Initiative', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01cwqze88', 'awardNumber': 'R01 NS108410', 'contactPoint': [], 'includeInCitation': False}]
description: This is the dataset for Tseng et al, "Shared and specialized coding across posterior cortical areas for dynamic navigation decisions" in Neuron (2022). The dataset contains calcium activity of >200,000 neurons recorded from 6 different cortical areas in mouse posterior cortex L2/3 and L5 using two-photon imaging, including V1 and secondary visual areas, retrosplenial cortex (RSC) and posterior parietal cortex (PPC), while the mice were performing a flexible decision-making task based on rule-switching during virtual navigation. There are total 300 behavior + imaging sessions collected from 8 mice. The neurons in each experiment have been registered into the Allen Institute Mouse Common Coordinate Framework (CCF) based on widefield retinotopy. In addition, these neurons contain fluorescent labels of retroAAV injected in one of the two sets of projection targets: an anterior part of anterior cingulate cortex/secondary motor cortex (ACC/M2) and striatum, or a posterior part of ACC/M2 and orbitofrontal cortex (OFC).   

Please see the related paper for more details: https://doi.org/10.1016/j.neuron.2022.05.012

Additional resources:

- Jupyter notebook for a tutorial to read and extract information from these NWB files: https://github.com/sytseng/Notebook_for_Dandiset_000579

- NWB extension code for custom lab meta data (required for reading NWB files): https://github.com/sytseng/ndx-harvey-swac 

- Code and tutorials for fitting GLM to neural activity in Tensorflow 2: https://github.com/sytseng/GLM_Tensorflow_2
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}, {'name': 'behavioral approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 245591965505, 'numberOfFiles': 308, 'numberOfSubjects': 8, 'variableMeasured': ['ImagingPlane', 'ProcessingModule', 'OpticalChannel', 'Position', 'SpatialSeries', 'BehavioralTimeSeries', 'PlaneSegmentation'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000579 has 98 NWB files.
2 of these NWB files are of type 1.
83 of these NWB files are of type 2.
1 of these NWB files are of type 3.
1 of these NWB files are of type 4.
11 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2023-07-21T10:38:21.955419-04:00']
  Group /general/devices/two_photon_microscope (Device) Two-photon microscope
  experiment_description: Widefield retinotopy and 2p window vessel and retrograde label overview
  experimenter: ['Tseng, Shih-Yi']
  Group /general/harvey_lab_swac_metadata_mouse (LabMetaDataMouse) 
  institution: Harvard Medical School
  keywords: ['cortex' 'retinotopy' 'widefield imaging']
  lab: Harvey Lab
  Group /general/optophysiology/ImagingPlane_mScarlet_800nm (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane_mScarlet_800nm/OpticalChannel_mScarlet (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane_mScarlet_800nm/device (Device) Two-photon microscope
  Group /general/optophysiology/ImagingPlane_mTagBFP2_850nm (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane_mTagBFP2_850nm/OpticalChannel_mTagBFP2 (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane_mTagBFP2_850nm/device (Device) Two-photon microscope
  related_publications: ['doi:10.1016/j.neuron.2022.05.012']
  session_id: Mouse_10_widefield_retinotopy_and_window_vessel
  Group /general/subject (Subject) 
  surgery: cranial window creation date:2017-05-26, 3.5 mm diameter, left posterior cortex; AAVretro injection date:2017-05-26; GCaMP6s injection date:2017-09-11; performed by Shih-Yi Tseng and Selmaan N. Chettih
  virus: AAV2/1-synapsin-GCaMP6s-WPRE-SV40 in left V1 x2 sites, PM x1, AM x1, MM x1, RSC x1, visA x2, 1/10 dilution, 70nl per site in L23 and 100nl per site in L5; AAV2retro-Syn-mTagBFP2 in left posterior ACC/M2 x4, undiluted, 300 nl per site, coordinate (mm from bregma): (A 0.25, L 0.3, D 0.4), (A 0.25, L 0.3, D 0.85), (A 0.1, L 0.7, D 0.3), (A 0.1, L 0.7, D 0.8); AAV2retro-Syn-mScarlet in left  ORBvl x1, ORBl x1, 1/5 dilution, 500 nl per site, coordinate (mm from bregma): (A 2.45, L 0.75, D 1.8), (A 2.45, L 1.25, D 1.85)
  identifier: Mouse_10_widefield_retinotopy_and_window_vessel
  Group /processing/ophys (ProcessingModule) cranial window vessel image under 2P microscope
  Group /processing/ophys/whole_window_mScarlet_img_2p (Images) raw and processed mScarlet images for the whole window with stitching FOVs under 2P microscope
  Dataset /processing/ophys/whole_window_mScarlet_img_2p/processed_whole_window_mScarlet_img_L2 (GrayscaleImage) processed image of stitched mScarlet image in L2 (remove the overlaping regions, resize to 660.533 pixels per mm, and rotate 90 degree + fliplr so now x axis is ~lateral to medial, y axis is ~posterior to anterior, same orientation as WF vessel).Use the Registration__rs_to_ccf_mm_transformation_matrix in lab_meta_data to transform the resize/processed image to CCF. | shape = (1786, 1991) | dtype = float64
  Dataset /processing/ophys/whole_window_mScarlet_img_2p/processed_whole_window_mScarlet_img_L3 (GrayscaleImage) processed image of stitched mScarlet image in L3 (remove the overlaping regions, resize to 660.533 pixels per mm, and rotate 90 degree + fliplr so now x axis is ~lateral to medial, y axis is ~posterior to anterior, same orientation as WF vessel).Use the Registration__rs_to_ccf_mm_transformation_matrix in lab_meta_data to transform the resize/processed image to CCF. | shape = (1786, 1991) | dtype = float64
  Dataset /processing/ophys/whole_window_mScarlet_img_2p/processed_whole_window_mScarlet_img_L5 (GrayscaleImage) processed image of stitched mScarlet image in L5 (remove the overlaping regions, resize to 660.533 pixels per mm, and rotate 90 degree + fliplr so now x axis is ~lateral to medial, y axis is ~posterior to anterior, same orientation as WF vessel) | shape = (1786, 1991) | dtype = float64
  Dataset /processing/ophys/whole_window_mScarlet_img_2p/raw_whole_window_mScarlet_img_L2 (GrayscaleImage) raw mScarlet image in L2 for the whole window with stitching FOVs under 2P microscope | shape = (2048, 2048) | dtype = uint16
  Dataset /processing/ophys/whole_window_mScarlet_img_2p/raw_whole_window_mScarlet_img_L3 (GrayscaleImage) raw mScarlet image in L3 for the whole window with stitching FOVs under 2P microscope | shape = (2048, 2048) | dtype = uint16
  Dataset /processing/ophys/whole_window_mScarlet_img_2p/raw_whole_window_mScarlet_img_L5 (GrayscaleImage) raw mScarlet image in L5 for the whole window with stitching FOVs under 2P microscope | shape = (2048, 2048) | dtype = uint16
  Group /processing/ophys/whole_window_mTagBFP2_img_2p (Images) raw and processed mTagBFP2 images for the whole window with stitching FOVs under 2P microscope
  Dataset /processing/ophys/whole_window_mTagBFP2_img_2p/processed_whole_window_mTagBFP2_img_L2 (GrayscaleImage) processed image of stitched mTagBFP2 image in L2 (remove the overlaping regions, resize to 660.533 pixels per mm, and rotate 90 degree + fliplr so now x axis is ~lateral to medial, y axis is ~posterior to anterior, same orientation as WF vessel).Use the Registration__rs_to_ccf_mm_transformation_matrix in lab_meta_data to transform the resize/processed image to CCF. | shape = (1786, 1991) | dtype = float64
  Dataset /processing/ophys/whole_window_mTagBFP2_img_2p/processed_whole_window_mTagBFP2_img_L3 (GrayscaleImage) processed image of stitched mTagBFP2 image in L3 (remove the overlaping regions, resize to 660.533 pixels per mm, and rotate 90 degree + fliplr so now x axis is ~lateral to medial, y axis is ~posterior to anterior, same orientation as WF vessel).Use the Registration__rs_to_ccf_mm_transformation_matrix in lab_meta_data to transform the resize/processed image to CCF. | shape = (1786, 1991) | dtype = float64
  Dataset /processing/ophys/whole_window_mTagBFP2_img_2p/processed_whole_window_mTagBFP2_img_L5 (GrayscaleImage) processed image of stitched mTagBFP2 image in L5 (remove the overlaping regions, resize to 660.533 pixels per mm, and rotate 90 degree + fliplr so now x axis is ~lateral to medial, y axis is ~posterior to anterior, same orientation as WF vessel).Use the Registration__rs_to_ccf_mm_transformation_matrix in lab_meta_data to transform the resize/processed image to CCF. | shape = (1786, 1991) | dtype = float64
  Dataset /processing/ophys/whole_window_mTagBFP2_img_2p/raw_whole_window_mTagBFP2_img_L2 (GrayscaleImage) raw mTagBFP2 image in L2 for the whole window with stitching FOVs under 2P microscope | shape = (2048, 2048) | dtype = uint16
  Dataset /processing/ophys/whole_window_mTagBFP2_img_2p/raw_whole_window_mTagBFP2_img_L3 (GrayscaleImage) raw mTagBFP2 image in L3 for the whole window with stitching FOVs under 2P microscope | shape = (2048, 2048) | dtype = uint16
  Dataset /processing/ophys/whole_window_mTagBFP2_img_2p/raw_whole_window_mTagBFP2_img_L5 (GrayscaleImage) raw mTagBFP2 image in L5 for the whole window with stitching FOVs under 2P microscope | shape = (2048, 2048) | dtype = uint16
  Group /processing/ophys/whole_window_vessel_img_2p (Images) raw and processed images of vessel pattern at brain surface for the whole window with stitching FOVs under 2P microscope
  Dataset /processing/ophys/whole_window_vessel_img_2p/processed_whole_window_vessel_img_2p (GrayscaleImage) processed image of stitched vessel pattern (remove the overlaping regions, resize to 660.533 pixels per mm, and rotate 90 degree + fliplr so now x axis is ~lateral to medial, y axis is ~posterior to anterior, same orientation as WF vessel). Use the Registration__rs_to_ccf_mm_transformation_matrix in lab_meta_data to transform the resize/processed image to CCF. | shape = (1786, 1991) | dtype = float64
  Dataset /processing/ophys/whole_window_vessel_img_2p/raw_whole_window_vessel_img_2p (GrayscaleImage) raw image of vessel pattern at brain surface for the whole window with stitching FOVs under 2P microscope | shape = (2048, 2048) | dtype = uint16
  Group /processing/retinotopy (ProcessingModule) widefield and cranial window vessel image
  Group /processing/retinotopy/widefield_imaging (Images) results of widefield imaging in this mouse. Use the Registration__wf_to_rs_mm_transformation_matrix in lab_meta_data to algin the WF images to the resize/processed images.
  Dataset /processing/retinotopy/widefield_imaging/axis_1_phase_map_altitude (GrayscaleImage) axis 1 (altitude) phase map in degree collected with widefield imaging | shape = (512, 512) | dtype = float64
  Dataset /processing/retinotopy/widefield_imaging/axis_2_phase_map_azimuth (GrayscaleImage) axis 2 (azimuth) phase map in degree collected with widefield imaging | shape = (512, 512) | dtype = float64
  Dataset /processing/retinotopy/widefield_imaging/field_sign_map (GrayscaleImage) field sign map collected with widefield imaging | shape = (512, 512) | dtype = float64
  Dataset /processing/retinotopy/widefield_imaging/power_map_avg (GrayscaleImage) average FFT power map collected with widefield imaging | shape = (512, 512) | dtype = float64
  Dataset /processing/retinotopy/widefield_imaging/widefield_vessel_image (GrayscaleImage) image of vessel pattern at brain surface for the whole window collected with widefield imaging | shape = (512, 512) | dtype = uint16
  session_description: Widefield retinotopy and 2p window vessel and retrograde label overview
  session_start_time: 2017-11-17T00:00:00-05:00
  timestamps_reference_time: 2017-11-17T00:00:00-05:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Virmen_forward_lateral_velocity_timeseries (TimeSeries) Raw forward and lateral velocity (in maze) in Virmen frames (sampled at ~30 Hz)
  Group /acquisition/Virmen_maze_world_timeseries (TimeSeries) Maze world in Virmen frames (sampled at ~30 Hz), 1:WLV, 2:BRV, 3:WRV, 4:BLV, 5:WLN, 6:BRN, 7:WRN, 8:BLN; B/W:black/white cue, L/R:left/right reward location, V/N:visually-guided/normal trial
  Group /acquisition/Virmen_positions (Position) 
  Group /acquisition/Virmen_positions/Virmen_forward_lateral_positions (SpatialSeries) Raw forward and lateral position in Virmen frames (sampled at ~30 Hz)
  Group /acquisition/Virmen_reward_timeseries (TimeSeries) Reward in Virmen frames (sampled at ~30 Hz), 1: reward delivered
  Group /acquisition/Virmen_trial_number_timeseries (TimeSeries) Trial number in Virmen frames (sampled at ~30 Hz)
  Group /acquisition/Virmen_trial_phase_timeseries (TimeSeries) Trial phase in Virmen frames (sampled at ~30 Hz), 0: maze, -1: feedback delay/feedback, -2: visual feedback onset, 1: ITI
  Group /acquisition/imaging_frame_timeseries (TimeSeries) Two photon imaging frame signals sampled at 2000 Hz
  Group /acquisition/lick_timeseries (TimeSeries) Analog lick signals sampled at 2000 Hz (some sessions have signal loss due to acquisition problems, so not a reliable signal)
  Group /acquisition/raw_velocity_timeseries (TimeSeries) Raw velocity of the spherical treadmill sampled at 2000 Hz, array of the shape: timestampes x [pitch, roll, yaw]
  Group /acquisition/virmen_frame_timeseries (TimeSeries) Virmen frame signals sampled at 2000 Hz
  file_create_date: ['2023-07-20T13:54:15.563879-04:00']
  Group /general/devices/two_photon_microscope (Device) Two-photon microscope
  experiment_description: Mouse performing a dynamic navigation task with calcium imaging in V1 layer 2/3
  experimenter: ['Tseng, Shih-Yi']
  Group /general/harvey_lab_swac_metadata_session (LabMetaDataSession) 
  institution: Harvard Medical School
  keywords: ['mouse' 'decision-making' 'navigation' 'virtual reality' 'cortex'
   'calcium imaging' 'two-photon imaging']
  lab: Harvey Lab
  Group /general/optophysiology/ImagingPlane_GCaMP6s_920nm (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane_GCaMP6s_920nm/OpticalChannel_GCaMP (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane_GCaMP6s_920nm/device (Device) Two-photon microscope
  Group /general/optophysiology/ImagingPlane_mScarlet_800nm (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane_mScarlet_800nm/OpticalChannel_GCaMP (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane_mScarlet_800nm/OpticalChannel_mScarlet (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane_mScarlet_800nm/device (Device) Two-photon microscope
  Group /general/optophysiology/ImagingPlane_mTagBFP2_850nm (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane_mTagBFP2_850nm/OpticalChannel_GCaMP (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane_mTagBFP2_850nm/OpticalChannel_mTagBFP2 (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane_mTagBFP2_850nm/device (Device) Two-photon microscope
  related_publications: ['doi:10.1016/j.neuron.2022.05.012']
  session_id: mouse_10_session_date_2017-09-21_area_V1_L23_multi_plane_imaging
  stimulus: maze_stem_length=200.0;maze_stem_width=10.01;maze_arm_length=50.0;maze_arm_width=60.0;cue_delay_length=0.0;wall_height=20.0;max_position=255.0;frac_non_visually_guided_trials=0.7;choice_bias_penalty=2;feedback_delay=1.0;reward_delay=3.0;iti_correct=2.0;iti_incorrect=4.0
  Group /general/subject (Subject) 
  surgery: cranial window creation date:2017-05-26, 3.5 mm diameter, left posterior cortex; AAVretro injection date:2017-05-26; GCaMP6s injection date:2017-09-11; performed by Shih-Yi Tseng and Selmaan N. Chettih
  virus: AAV2/1-synapsin-GCaMP6s-WPRE-SV40 in left V1 x2 sites, PM x1, AM x1, MM x1, RSC x1, visA x2, 1/10 dilution, 70nl per site in L23 and 100nl per site in L5; AAV2retro-Syn-mTagBFP2 in left posterior ACC/M2 x4, undiluted, 300 nl per site, coordinate (mm from bregma): (A 0.25, L 0.3, D 0.4), (A 0.25, L 0.3, D 0.85), (A 0.1, L 0.7, D 0.3), (A 0.1, L 0.7, D 0.8); AAV2retro-Syn-mScarlet in left  ORBvl x1, ORBl x1, 1/5 dilution, 500 nl per site, coordinate (mm from bregma): (A 2.45, L 0.75, D 1.8), (A 2.45, L 1.25, D 1.85)
  identifier: Mouse_10_session_date_2017-09-21
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/epoch_type (VectorData) type of epoch: maze, maze_stem, maze_arm, feedback_delay, feedback, iti, feedback_and_iti | shape = (2869,) | dtype = object
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (2869,) | dtype = int32
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (2869,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (2869,) | dtype = float64
  Dataset /intervals/epochs/trial_id (VectorData) trial number for this epoch | shape = (2869,) | dtype = int32
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/association_mat (VectorData) behavioral LSTM predicted conditional probability, order: P(R|W), P(L|W), P(R|B), P(L|B) | shape = (410, 4) | dtype = float64
  Dataset /intervals/trials/bias_following (VectorData) the bias-following on the trial (between -0.5 ~ 0.5) | shape = (410,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (410,) | dtype = int32
  Dataset /intervals/trials/is_choL (VectorData) whether the mouse made a left choice on the trial (True: left, False: right) | shape = (410,) | dtype = bool
  Dataset /intervals/trials/is_correct (VectorData) whether the trial was correct (True: correct, False: incorrect) | shape = (410,) | dtype = bool
  Dataset /intervals/trials/is_cueB (VectorData) whether the trial had a black cue (True: black, False: white) | shape = (410,) | dtype = bool
  Dataset /intervals/trials/is_ruleA (VectorData) whether the trial happened during rule A (True: rule A (BL,WR), False: rule B(WL,BR)) | shape = (410,) | dtype = bool
  Dataset /intervals/trials/is_switch (VectorData) whether a rule switch happened on the trial (True: switch, False: non-switch) | shape = (410,) | dtype = bool
  Dataset /intervals/trials/is_vis (VectorData) whether the trial was a visually guided trial (True: visually guided, False: non-visually guided) | shape = (410,) | dtype = bool
  Dataset /intervals/trials/prob_actual_cho (VectorData) the probability of actual choice on the trial, i.e. P(actual choice|actual cue) | shape = (410,) | dtype = float64
  Dataset /intervals/trials/rule_belief (VectorData) the rule belief on the trial (pos: rule B, neg: rule A) | shape = (410,) | dtype = float64
  Dataset /intervals/trials/rule_following (VectorData) the rule-following on the trial (between -0.5 ~ 0.5) | shape = (410,) | dtype = float64
  Dataset /intervals/trials/signed_bias (VectorData) the singed choice bias on the trial (pos: left bias, neg: right bias) | shape = (410,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (410,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (410,) | dtype = float64
  Dataset /intervals/trials/trial_offset_plane_frame_idx (VectorData) correspoding imaging frame index for this trial offset for each imaging plane | shape = (410, 5) | dtype = int32
  Dataset /intervals/trials/trial_onset_plane_frame_idx (VectorData) correspoding imaging frame index for this trial onset for each imaging plane | shape = (410, 5) | dtype = int32
  Group /processing/behavior (ProcessingModule) processed behavioral data
  Group /processing/behavior/frame_aligned_position (Position) 
  Group /processing/behavior/frame_aligned_position/frame_aligned_forward_and_lateral_position (SpatialSeries) forward and lateral position aligned to imaging frames (30 Hz)
  Group /processing/behavior/frame_aligned_time_from_choice_point (TimeSeries) time elapsed (sec) from choice point aligned to imaging frames (neg: maze, pos: feedback and ITI)
  Group /processing/behavior/frame_aligned_trial_number (TimeSeries) trial number aligned to imaging frames
  Group /processing/behavior/frame_aligned_velocity (BehavioralTimeSeries) 
  Group /processing/behavior/frame_aligned_velocity/frame_aligned_pitch_roll_yaw_velocity (TimeSeries) velocity of the spherical treadmill (pitch, roll, yaw) aligned to imaging frames (30 Hz)
  Group /processing/behavior/frame_to_verm_index_conversion (TimeSeries) correspoding verm frame index for each imaging frame
  Group /processing/behavior/plane_idx_for_imaging_frames (TimeSeries) plane index for imaging frames
  Group /processing/behavior/velocity_RNN_prediction_for_choice_and_cue (BehavioralTimeSeries) 
  Group /processing/behavior/velocity_RNN_prediction_for_choice_and_cue/velocity_RNN_prediction_for_choice_and_cue (TimeSeries) velocity RNN prediction (forward choice, reverse choice, forward cue, reverse cue) aligned to mid imaging frames (idx=2) of each 6 Hz volume (or pseudovolume for plane imaging)
  Group /processing/behavior/verm_to_frame_index_conversion (TimeSeries) correspoding imaging frame index for each verm frame
  Group /processing/ophys (ProcessingModule) two photon calcium imaging processed data
  Group /processing/ophys/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation_0 (PlaneSegmentation) Plane segmentation of imagine plane 0
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_0/ap (VectorData) ap location (mm from bregma) | shape = (131,) | dtype = float64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_0/area (VectorData) cortical area where this cell is located | shape = (131,) | dtype = object
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_0/depth (VectorData) depth (mm from pia) | shape = (131,) | dtype = float64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_0/id (ElementIdentifiers)  | shape = (131,) | dtype = int32
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation_0/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation_0/imaging_plane/OpticalChannel_GCaMP (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation_0/imaging_plane/device (Device) Two-photon microscope
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_0/mScarlet (VectorData) whether this cell is labeled with Scarlet | shape = (131,) | dtype = bool
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_0/mTagBFP2 (VectorData) whether this cell is labeled with mTagBFP2 | shape = (131,) | dtype = bool
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_0/ml (VectorData) ml location (mm from bregma) | shape = (131,) | dtype = float64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_0/pixel_mask (VectorData) Pixel masks for each ROI | shape = (11101,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_0/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (131,) | dtype = uint16
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation_1 (PlaneSegmentation) Plane segmentation of imagine plane 1
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_1/ap (VectorData) ap location (mm from bregma) | shape = (137,) | dtype = float64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_1/area (VectorData) cortical area where this cell is located | shape = (137,) | dtype = object
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_1/depth (VectorData) depth (mm from pia) | shape = (137,) | dtype = float64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_1/id (ElementIdentifiers)  | shape = (137,) | dtype = int32
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation_1/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation_1/imaging_plane/OpticalChannel_GCaMP (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation_1/imaging_plane/device (Device) Two-photon microscope
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_1/mScarlet (VectorData) whether this cell is labeled with Scarlet | shape = (137,) | dtype = bool
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_1/mTagBFP2 (VectorData) whether this cell is labeled with mTagBFP2 | shape = (137,) | dtype = bool
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_1/ml (VectorData) ml location (mm from bregma) | shape = (137,) | dtype = float64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_1/pixel_mask (VectorData) Pixel masks for each ROI | shape = (10066,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_1/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (137,) | dtype = uint16
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation_2 (PlaneSegmentation) Plane segmentation of imagine plane 2
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_2/ap (VectorData) ap location (mm from bregma) | shape = (98,) | dtype = float64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_2/area (VectorData) cortical area where this cell is located | shape = (98,) | dtype = object
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_2/depth (VectorData) depth (mm from pia) | shape = (98,) | dtype = float64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_2/id (ElementIdentifiers)  | shape = (98,) | dtype = int32
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation_2/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation_2/imaging_plane/OpticalChannel_GCaMP (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation_2/imaging_plane/device (Device) Two-photon microscope
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_2/mScarlet (VectorData) whether this cell is labeled with Scarlet | shape = (98,) | dtype = bool
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_2/mTagBFP2 (VectorData) whether this cell is labeled with mTagBFP2 | shape = (98,) | dtype = bool
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_2/ml (VectorData) ml location (mm from bregma) | shape = (98,) | dtype = float64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_2/pixel_mask (VectorData) Pixel masks for each ROI | shape = (6551,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_2/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (98,) | dtype = uint16
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation_3 (PlaneSegmentation) Plane segmentation of imagine plane 3
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_3/ap (VectorData) ap location (mm from bregma) | shape = (78,) | dtype = float64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_3/area (VectorData) cortical area where this cell is located | shape = (78,) | dtype = object
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_3/depth (VectorData) depth (mm from pia) | shape = (78,) | dtype = float64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_3/id (ElementIdentifiers)  | shape = (78,) | dtype = int32
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation_3/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation_3/imaging_plane/OpticalChannel_GCaMP (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation_3/imaging_plane/device (Device) Two-photon microscope
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_3/mScarlet (VectorData) whether this cell is labeled with Scarlet | shape = (78,) | dtype = bool
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_3/mTagBFP2 (VectorData) whether this cell is labeled with mTagBFP2 | shape = (78,) | dtype = bool
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_3/ml (VectorData) ml location (mm from bregma) | shape = (78,) | dtype = float64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_3/pixel_mask (VectorData) Pixel masks for each ROI | shape = (5185,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_3/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (78,) | dtype = uint16
  Group /processing/ophys/deconvolved_activity_plane_0 (RoiResponseSeries) Deconvolved activity for ROIs in PlaneSegmentation_0
  Dataset /processing/ophys/deconvolved_activity_plane_0/rois (DynamicTableRegion) the ROIs in PlaneSegmentation_0 | shape = (131,) | dtype = int32
  Group /processing/ophys/deconvolved_activity_plane_1 (RoiResponseSeries) Deconvolved activity for ROIs in PlaneSegmentation_1
  Dataset /processing/ophys/deconvolved_activity_plane_1/rois (DynamicTableRegion) the ROIs in PlaneSegmentation_1 | shape = (137,) | dtype = int32
  Group /processing/ophys/deconvolved_activity_plane_2 (RoiResponseSeries) Deconvolved activity for ROIs in PlaneSegmentation_2
  Dataset /processing/ophys/deconvolved_activity_plane_2/rois (DynamicTableRegion) the ROIs in PlaneSegmentation_2 | shape = (98,) | dtype = int32
  Group /processing/ophys/deconvolved_activity_plane_3 (RoiResponseSeries) Deconvolved activity for ROIs in PlaneSegmentation_3
  Dataset /processing/ophys/deconvolved_activity_plane_3/rois (DynamicTableRegion) the ROIs in PlaneSegmentation_3 | shape = (78,) | dtype = int32
  Group /processing/ophys/df_over_f_plane_0 (DfOverF) 
  Group /processing/ophys/df_over_f_plane_0/dF_over_F_plane_0 (RoiResponseSeries) dF/F for ROIs in PlaneSegmentation_0
  Dataset /processing/ophys/df_over_f_plane_0/dF_over_F_plane_0/rois (DynamicTableRegion) the ROIs in PlaneSegmentation_0 | shape = (131,) | dtype = int32
  Group /processing/ophys/df_over_f_plane_1 (DfOverF) 
  Group /processing/ophys/df_over_f_plane_1/dF_over_F_plane_1 (RoiResponseSeries) dF/F for ROIs in PlaneSegmentation_1
  Dataset /processing/ophys/df_over_f_plane_1/dF_over_F_plane_1/rois (DynamicTableRegion) the ROIs in PlaneSegmentation_1 | shape = (137,) | dtype = int32
  Group /processing/ophys/df_over_f_plane_2 (DfOverF) 
  Group /processing/ophys/df_over_f_plane_2/dF_over_F_plane_2 (RoiResponseSeries) dF/F for ROIs in PlaneSegmentation_2
  Dataset /processing/ophys/df_over_f_plane_2/dF_over_F_plane_2/rois (DynamicTableRegion) the ROIs in PlaneSegmentation_2 | shape = (98,) | dtype = int32
  Group /processing/ophys/df_over_f_plane_3 (DfOverF) 
  Group /processing/ophys/df_over_f_plane_3/dF_over_F_plane_3 (RoiResponseSeries) dF/F for ROIs in PlaneSegmentation_3
  Dataset /processing/ophys/df_over_f_plane_3/dF_over_F_plane_3/rois (DynamicTableRegion) the ROIs in PlaneSegmentation_3 | shape = (78,) | dtype = int32
  Group /processing/ophys/static_GCaMP_and_retrograde_label_image_plane_0 (Images) static unmixed images for GCaMP and retrograde labels of the FOV
  Dataset /processing/ophys/static_GCaMP_and_retrograde_label_image_plane_0/GCaMP_800nm (GrayscaleImage) static unmixed GCaMP image of the FOV with excitation 800 nm | shape = (512, 512) | dtype = float64
  Dataset /processing/ophys/static_GCaMP_and_retrograde_label_image_plane_0/GCaMP_850nm (GrayscaleImage) static unmixed GCaMP image of the FOV with excitation 850 nm | shape = (512, 512) | dtype = float64
  Dataset /processing/ophys/static_GCaMP_and_retrograde_label_image_plane_0/mScarlet_800nm (GrayscaleImage) static unmixed mScarlet image of the FOV with excitation 800 nm | shape = (512, 512) | dtype = float64
  Dataset /processing/ophys/static_GCaMP_and_retrograde_label_image_plane_0/mTagBFP2_850nm (GrayscaleImage) static unmixed mTagBFP2 image of the FOV with excitation 850 nm | shape = (512, 512) | dtype = float64
  Group /processing/ophys/static_GCaMP_and_retrograde_label_image_plane_1 (Images) static unmixed images for GCaMP and retrograde labels of the FOV
  Dataset /processing/ophys/static_GCaMP_and_retrograde_label_image_plane_1/GCaMP_800nm (GrayscaleImage) static unmixed GCaMP image of the FOV with excitation 800 nm | shape = (512, 512) | dtype = float64
  Dataset /processing/ophys/static_GCaMP_and_retrograde_label_image_plane_1/GCaMP_850nm (GrayscaleImage) static unmixed GCaMP image of the FOV with excitation 850 nm | shape = (512, 512) | dtype = float64
  Dataset /processing/ophys/static_GCaMP_and_retrograde_label_image_plane_1/mScarlet_800nm (GrayscaleImage) static unmixed mScarlet image of the FOV with excitation 800 nm | shape = (512, 512) | dtype = float64
  Dataset /processing/ophys/static_GCaMP_and_retrograde_label_image_plane_1/mTagBFP2_850nm (GrayscaleImage) static unmixed mTagBFP2 image of the FOV with excitation 850 nm | shape = (512, 512) | dtype = float64
  Group /processing/ophys/static_GCaMP_and_retrograde_label_image_plane_2 (Images) static unmixed images for GCaMP and retrograde labels of the FOV
  Dataset /processing/ophys/static_GCaMP_and_retrograde_label_image_plane_2/GCaMP_800nm (GrayscaleImage) static unmixed GCaMP image of the FOV with excitation 800 nm | shape = (512, 512) | dtype = float64
  Dataset /processing/ophys/static_GCaMP_and_retrograde_label_image_plane_2/GCaMP_850nm (GrayscaleImage) static unmixed GCaMP image of the FOV with excitation 850 nm | shape = (512, 512) | dtype = float64
  Dataset /processing/ophys/static_GCaMP_and_retrograde_label_image_plane_2/mScarlet_800nm (GrayscaleImage) static unmixed mScarlet image of the FOV with excitation 800 nm | shape = (512, 512) | dtype = float64
  Dataset /processing/ophys/static_GCaMP_and_retrograde_label_image_plane_2/mTagBFP2_850nm (GrayscaleImage) static unmixed mTagBFP2 image of the FOV with excitation 850 nm | shape = (512, 512) | dtype = float64
  Group /processing/ophys/static_GCaMP_and_retrograde_label_image_plane_3 (Images) static unmixed images for GCaMP and retrograde labels of the FOV
  Dataset /processing/ophys/static_GCaMP_and_retrograde_label_image_plane_3/GCaMP_800nm (GrayscaleImage) static unmixed GCaMP image of the FOV with excitation 800 nm | shape = (512, 512) | dtype = float64
  Dataset /processing/ophys/static_GCaMP_and_retrograde_label_image_plane_3/GCaMP_850nm (GrayscaleImage) static unmixed GCaMP image of the FOV with excitation 850 nm | shape = (512, 512) | dtype = float64
  Dataset /processing/ophys/static_GCaMP_and_retrograde_label_image_plane_3/mScarlet_800nm (GrayscaleImage) static unmixed mScarlet image of the FOV with excitation 800 nm | shape = (512, 512) | dtype = float64
  Dataset /processing/ophys/static_GCaMP_and_retrograde_label_image_plane_3/mTagBFP2_850nm (GrayscaleImage) static unmixed mTagBFP2 image of the FOV with excitation 850 nm | shape = (512, 512) | dtype = float64
  Group /processing/ophys/vessel_img (Images) image of vessel pattern at brain surface for this FOV
  Dataset /processing/ophys/vessel_img/vessel_img (GrayscaleImage) image of vessel pattern at brain surface for this FOV | shape = (512, 512) | dtype = float64
  session_description: Mouse performing a dynamic navigation task with calcium imaging in V1 layer 2/3
  session_start_time: 2017-09-21T15:38:46.170661-04:00
  timestamps_reference_time: 2017-09-21T15:38:46.170661-04:00


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Virmen_forward_lateral_velocity_timeseries (TimeSeries) Raw forward and lateral velocity (in maze) in Virmen frames (sampled at ~30 Hz)
  Group /acquisition/Virmen_maze_world_timeseries (TimeSeries) Maze world in Virmen frames (sampled at ~30 Hz), 1:WLV, 2:BRV, 3:WRV, 4:BLV, 5:WLN, 6:BRN, 7:WRN, 8:BLN; B/W:black/white cue, L/R:left/right reward location, V/N:visually-guided/normal trial
  Group /acquisition/Virmen_positions (Position) 
  Group /acquisition/Virmen_positions/Virmen_forward_lateral_positions (SpatialSeries) Raw forward and lateral position in Virmen frames (sampled at ~30 Hz)
  Group /acquisition/Virmen_reward_timeseries (TimeSeries) Reward in Virmen frames (sampled at ~30 Hz), 1: reward delivered
  Group /acquisition/Virmen_trial_number_timeseries (TimeSeries) Trial number in Virmen frames (sampled at ~30 Hz)
  Group /acquisition/Virmen_trial_phase_timeseries (TimeSeries) Trial phase in Virmen frames (sampled at ~30 Hz), 0: maze, -1: feedback delay/feedback, -2: visual feedback onset, 1: ITI
  Group /acquisition/imaging_frame_timeseries (TimeSeries) Two photon imaging frame signals sampled at 2000 Hz
  Group /acquisition/lick_timeseries (TimeSeries) Analog lick signals sampled at 2000 Hz (some sessions have signal loss due to acquisition problems, so not a reliable signal)
  Group /acquisition/raw_velocity_timeseries (TimeSeries) Raw velocity of the spherical treadmill sampled at 2000 Hz, array of the shape: timestampes x [pitch, roll, yaw]
  Group /acquisition/virmen_frame_timeseries (TimeSeries) Virmen frame signals sampled at 2000 Hz
  file_create_date: ['2023-07-20T13:35:27.373154-04:00']
  Group /general/devices/two_photon_microscope (Device) Two-photon microscope
  experiment_description: Mouse performing a dynamic navigation task with calcium imaging in visA layer 2/3
  experimenter: ['Tseng, Shih-Yi']
  Group /general/harvey_lab_swac_metadata_session (LabMetaDataSession) 
  institution: Harvard Medical School
  keywords: ['mouse' 'decision-making' 'navigation' 'virtual reality' 'cortex'
   'calcium imaging' 'two-photon imaging']
  lab: Harvey Lab
  Group /general/optophysiology/ImagingPlane_GCaMP6s_920nm (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane_GCaMP6s_920nm/OpticalChannel_GCaMP (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane_GCaMP6s_920nm/device (Device) Two-photon microscope
  Group /general/optophysiology/ImagingPlane_mScarlet_800nm (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane_mScarlet_800nm/OpticalChannel_GCaMP (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane_mScarlet_800nm/OpticalChannel_mScarlet (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane_mScarlet_800nm/device (Device) Two-photon microscope
  Group /general/optophysiology/ImagingPlane_mTagBFP2_850nm (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane_mTagBFP2_850nm/OpticalChannel_GCaMP (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane_mTagBFP2_850nm/OpticalChannel_mTagBFP2 (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane_mTagBFP2_850nm/device (Device) Two-photon microscope
  related_publications: ['doi:10.1016/j.neuron.2022.05.012']
  session_id: mouse_3_session_date_2017-05-16_area_visA_L23_multi_plane_imaging
  stimulus: maze_stem_length=200.0;maze_stem_width=10.01;maze_arm_length=50.0;maze_arm_width=60.0;cue_delay_length=60;wall_height=20.0;max_position=255.0;frac_non_visually_guided_trials=1.0;choice_bias_penalty=0;feedback_delay=1.0;reward_delay=3.0;iti_correct=2.0;iti_incorrect=2.0
  Group /general/subject (Subject) 
  surgery: cranial window creation date:2017-04-03, 3.5 mm diameter, left posterior cortex; AAVretro injection date:2017-04-03; GCaMP6s injection date:2017-04-03; performed by Shih-Yi Tseng and Selmaan N. Chettih
  virus: AAV2/1-synapsin-GCaMP6s-WPRE-SV40 in left V1 x3 sites, PM x1, AM x0, MM x1, RSC x1, visA x1, 1/10 dilution, 140nl per site in L23 and 140nl per site in L5; AAV2retro-Syn-mTagBFP2 in left anterior ACC/M2 x3, undiluted, 300 nl per site, coordinate (mm from bregma): (A 0.95, L 0.6, D 1.0), (A 0.95, L 0.6, D 0.3), (A 0.95, L 0.8, D 0.3); AAV2retro-Syn-mScarlet in left striatum x3, 1/20 dilution, 300 nl per site, coordinate (mm from bregma): (A 0.95, L 1.2, D 2.1), (A 1.0, L 1.75, D 2.1), (P 0.15, L 2.15, D 2.1); mScarlet expression did not come up when examining it under the 2P microscope (due to the higher dilution)
  identifier: Mouse_3_session_date_2017-05-16
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/epoch_type (VectorData) type of epoch: maze, maze_stem, maze_arm, feedback_delay, feedback, iti, feedback_and_iti | shape = (3296,) | dtype = object
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (3296,) | dtype = int32
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (3296,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (3296,) | dtype = float64
  Dataset /intervals/epochs/trial_id (VectorData) trial number for this epoch | shape = (3296,) | dtype = int32
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/association_mat (VectorData) behavioral LSTM predicted conditional probability, order: P(R|W), P(L|W), P(R|B), P(L|B) | shape = (471, 4) | dtype = float64
  Dataset /intervals/trials/bias_following (VectorData) the bias-following on the trial (between -0.5 ~ 0.5) | shape = (471,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (471,) | dtype = int32
  Dataset /intervals/trials/is_choL (VectorData) whether the mouse made a left choice on the trial (True: left, False: right) | shape = (471,) | dtype = bool
  Dataset /intervals/trials/is_correct (VectorData) whether the trial was correct (True: correct, False: incorrect) | shape = (471,) | dtype = bool
  Dataset /intervals/trials/is_cueB (VectorData) whether the trial had a black cue (True: black, False: white) | shape = (471,) | dtype = bool
  Dataset /intervals/trials/is_ruleA (VectorData) whether the trial happened during rule A (True: rule A (BL,WR), False: rule B(WL,BR)) | shape = (471,) | dtype = bool
  Dataset /intervals/trials/is_switch (VectorData) whether a rule switch happened on the trial (True: switch, False: non-switch) | shape = (471,) | dtype = bool
  Dataset /intervals/trials/is_vis (VectorData) whether the trial was a visually guided trial (True: visually guided, False: non-visually guided) | shape = (471,) | dtype = bool
  Dataset /intervals/trials/prob_actual_cho (VectorData) the probability of actual choice on the trial, i.e. P(actual choice|actual cue) | shape = (471,) | dtype = float64
  Dataset /intervals/trials/rule_belief (VectorData) the rule belief on the trial (pos: rule B, neg: rule A) | shape = (471,) | dtype = float64
  Dataset /intervals/trials/rule_following (VectorData) the rule-following on the trial (between -0.5 ~ 0.5) | shape = (471,) | dtype = float64
  Dataset /intervals/trials/signed_bias (VectorData) the singed choice bias on the trial (pos: left bias, neg: right bias) | shape = (471,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (471,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (471,) | dtype = float64
  Dataset /intervals/trials/trial_offset_plane_frame_idx (VectorData) correspoding imaging frame index for this trial offset for each imaging plane | shape = (471, 5) | dtype = int32
  Dataset /intervals/trials/trial_onset_plane_frame_idx (VectorData) correspoding imaging frame index for this trial onset for each imaging plane | shape = (471, 5) | dtype = int32
  Group /processing/behavior (ProcessingModule) processed behavioral data
  Group /processing/behavior/frame_aligned_position (Position) 
  Group /processing/behavior/frame_aligned_position/frame_aligned_forward_and_lateral_position (SpatialSeries) forward and lateral position aligned to imaging frames (30 Hz)
  Group /processing/behavior/frame_aligned_time_from_choice_point (TimeSeries) time elapsed (sec) from choice point aligned to imaging frames (neg: maze, pos: feedback and ITI)
  Group /processing/behavior/frame_aligned_trial_number (TimeSeries) trial number aligned to imaging frames
  Group /processing/behavior/frame_aligned_velocity (BehavioralTimeSeries) 
  Group /processing/behavior/frame_aligned_velocity/frame_aligned_pitch_roll_yaw_velocity (TimeSeries) velocity of the spherical treadmill (pitch, roll, yaw) aligned to imaging frames (30 Hz)
  Group /processing/behavior/frame_to_verm_index_conversion (TimeSeries) correspoding verm frame index for each imaging frame
  Group /processing/behavior/plane_idx_for_imaging_frames (TimeSeries) plane index for imaging frames
  Group /processing/behavior/velocity_RNN_prediction_for_choice_and_cue (BehavioralTimeSeries) 
  Group /processing/behavior/velocity_RNN_prediction_for_choice_and_cue/velocity_RNN_prediction_for_choice_and_cue (TimeSeries) velocity RNN prediction (forward choice, reverse choice, forward cue, reverse cue) aligned to mid imaging frames (idx=2) of each 6 Hz volume (or pseudovolume for plane imaging)
  Group /processing/behavior/verm_to_frame_index_conversion (TimeSeries) correspoding imaging frame index for each verm frame
  Group /processing/ophys (ProcessingModule) two photon calcium imaging processed data
  Group /processing/ophys/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation_0 (PlaneSegmentation) Plane segmentation of imagine plane 0
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_0/ap (VectorData) ap location (mm from bregma) | shape = (351,) | dtype = float64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_0/area (VectorData) cortical area where this cell is located | shape = (351,) | dtype = object
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_0/depth (VectorData) depth (mm from pia) | shape = (351,) | dtype = float64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_0/id (ElementIdentifiers)  | shape = (351,) | dtype = int32
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation_0/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation_0/imaging_plane/OpticalChannel_GCaMP (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation_0/imaging_plane/device (Device) Two-photon microscope
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_0/mScarlet (VectorData) whether this cell is labeled with Scarlet | shape = (351,) | dtype = bool
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_0/mTagBFP2 (VectorData) whether this cell is labeled with mTagBFP2 | shape = (351,) | dtype = bool
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_0/ml (VectorData) ml location (mm from bregma) | shape = (351,) | dtype = float64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_0/pixel_mask (VectorData) Pixel masks for each ROI | shape = (35847,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_0/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (351,) | dtype = uint16
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation_1 (PlaneSegmentation) Plane segmentation of imagine plane 1
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_1/ap (VectorData) ap location (mm from bregma) | shape = (293,) | dtype = float64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_1/area (VectorData) cortical area where this cell is located | shape = (293,) | dtype = object
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_1/depth (VectorData) depth (mm from pia) | shape = (293,) | dtype = float64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_1/id (ElementIdentifiers)  | shape = (293,) | dtype = int32
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation_1/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation_1/imaging_plane/OpticalChannel_GCaMP (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation_1/imaging_plane/device (Device) Two-photon microscope
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_1/mScarlet (VectorData) whether this cell is labeled with Scarlet | shape = (293,) | dtype = bool
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_1/mTagBFP2 (VectorData) whether this cell is labeled with mTagBFP2 | shape = (293,) | dtype = bool
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_1/ml (VectorData) ml location (mm from bregma) | shape = (293,) | dtype = float64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_1/pixel_mask (VectorData) Pixel masks for each ROI | shape = (29543,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_1/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (293,) | dtype = uint16
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation_2 (PlaneSegmentation) Plane segmentation of imagine plane 2
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_2/ap (VectorData) ap location (mm from bregma) | shape = (180,) | dtype = float64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_2/area (VectorData) cortical area where this cell is located | shape = (180,) | dtype = object
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_2/depth (VectorData) depth (mm from pia) | shape = (180,) | dtype = float64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_2/id (ElementIdentifiers)  | shape = (180,) | dtype = int32
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation_2/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation_2/imaging_plane/OpticalChannel_GCaMP (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation_2/imaging_plane/device (Device) Two-photon microscope
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_2/mScarlet (VectorData) whether this cell is labeled with Scarlet | shape = (180,) | dtype = bool
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_2/mTagBFP2 (VectorData) whether this cell is labeled with mTagBFP2 | shape = (180,) | dtype = bool
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_2/ml (VectorData) ml location (mm from bregma) | shape = (180,) | dtype = float64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_2/pixel_mask (VectorData) Pixel masks for each ROI | shape = (16839,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_2/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (180,) | dtype = uint16
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation_3 (PlaneSegmentation) Plane segmentation of imagine plane 3
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_3/ap (VectorData) ap location (mm from bregma) | shape = (193,) | dtype = float64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_3/area (VectorData) cortical area where this cell is located | shape = (193,) | dtype = object
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_3/depth (VectorData) depth (mm from pia) | shape = (193,) | dtype = float64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_3/id (ElementIdentifiers)  | shape = (193,) | dtype = int32
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation_3/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation_3/imaging_plane/OpticalChannel_GCaMP (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation_3/imaging_plane/device (Device) Two-photon microscope
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_3/mScarlet (VectorData) whether this cell is labeled with Scarlet | shape = (193,) | dtype = bool
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_3/mTagBFP2 (VectorData) whether this cell is labeled with mTagBFP2 | shape = (193,) | dtype = bool
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_3/ml (VectorData) ml location (mm from bregma) | shape = (193,) | dtype = float64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_3/pixel_mask (VectorData) Pixel masks for each ROI | shape = (16786,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_3/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (193,) | dtype = uint16
  Group /processing/ophys/deconvolved_activity_plane_0 (RoiResponseSeries) Deconvolved activity for ROIs in PlaneSegmentation_0
  Dataset /processing/ophys/deconvolved_activity_plane_0/rois (DynamicTableRegion) the ROIs in PlaneSegmentation_0 | shape = (351,) | dtype = int32
  Group /processing/ophys/deconvolved_activity_plane_1 (RoiResponseSeries) Deconvolved activity for ROIs in PlaneSegmentation_1
  Dataset /processing/ophys/deconvolved_activity_plane_1/rois (DynamicTableRegion) the ROIs in PlaneSegmentation_1 | shape = (293,) | dtype = int32
  Group /processing/ophys/deconvolved_activity_plane_2 (RoiResponseSeries) Deconvolved activity for ROIs in PlaneSegmentation_2
  Dataset /processing/ophys/deconvolved_activity_plane_2/rois (DynamicTableRegion) the ROIs in PlaneSegmentation_2 | shape = (180,) | dtype = int32
  Group /processing/ophys/deconvolved_activity_plane_3 (RoiResponseSeries) Deconvolved activity for ROIs in PlaneSegmentation_3
  Dataset /processing/ophys/deconvolved_activity_plane_3/rois (DynamicTableRegion) the ROIs in PlaneSegmentation_3 | shape = (193,) | dtype = int32
  Group /processing/ophys/df_over_f_plane_0 (DfOverF) 
  Group /processing/ophys/df_over_f_plane_0/dF_over_F_plane_0 (RoiResponseSeries) dF/F for ROIs in PlaneSegmentation_0
  Dataset /processing/ophys/df_over_f_plane_0/dF_over_F_plane_0/rois (DynamicTableRegion) the ROIs in PlaneSegmentation_0 | shape = (351,) | dtype = int32
  Group /processing/ophys/df_over_f_plane_1 (DfOverF) 
  Group /processing/ophys/df_over_f_plane_1/dF_over_F_plane_1 (RoiResponseSeries) dF/F for ROIs in PlaneSegmentation_1
  Dataset /processing/ophys/df_over_f_plane_1/dF_over_F_plane_1/rois (DynamicTableRegion) the ROIs in PlaneSegmentation_1 | shape = (293,) | dtype = int32
  Group /processing/ophys/df_over_f_plane_2 (DfOverF) 
  Group /processing/ophys/df_over_f_plane_2/dF_over_F_plane_2 (RoiResponseSeries) dF/F for ROIs in PlaneSegmentation_2
  Dataset /processing/ophys/df_over_f_plane_2/dF_over_F_plane_2/rois (DynamicTableRegion) the ROIs in PlaneSegmentation_2 | shape = (180,) | dtype = int32
  Group /processing/ophys/df_over_f_plane_3 (DfOverF) 
  Group /processing/ophys/df_over_f_plane_3/dF_over_F_plane_3 (RoiResponseSeries) dF/F for ROIs in PlaneSegmentation_3
  Dataset /processing/ophys/df_over_f_plane_3/dF_over_F_plane_3/rois (DynamicTableRegion) the ROIs in PlaneSegmentation_3 | shape = (193,) | dtype = int32
  Group /processing/ophys/static_GCaMP_and_retrograde_label_image_plane_0 (Images) static unmixed images for GCaMP and retrograde labels of the FOV
  Dataset /processing/ophys/static_GCaMP_and_retrograde_label_image_plane_0/GCaMP_800nm (GrayscaleImage) static unmixed GCaMP image of the FOV with excitation 800 nm | shape = (512, 512) | dtype = float64
  Dataset /processing/ophys/static_GCaMP_and_retrograde_label_image_plane_0/GCaMP_850nm (GrayscaleImage) static unmixed GCaMP image of the FOV with excitation 850 nm | shape = (512, 512) | dtype = float64
  Dataset /processing/ophys/static_GCaMP_and_retrograde_label_image_plane_0/mScarlet_800nm (GrayscaleImage) static unmixed mScarlet image of the FOV with excitation 800 nm | shape = (512, 512) | dtype = float64
  Dataset /processing/ophys/static_GCaMP_and_retrograde_label_image_plane_0/mTagBFP2_850nm (GrayscaleImage) static unmixed mTagBFP2 image of the FOV with excitation 850 nm | shape = (512, 512) | dtype = float64
  Group /processing/ophys/static_GCaMP_and_retrograde_label_image_plane_1 (Images) static unmixed images for GCaMP and retrograde labels of the FOV
  Dataset /processing/ophys/static_GCaMP_and_retrograde_label_image_plane_1/GCaMP_800nm (GrayscaleImage) static unmixed GCaMP image of the FOV with excitation 800 nm | shape = (512, 512) | dtype = float64
  Dataset /processing/ophys/static_GCaMP_and_retrograde_label_image_plane_1/GCaMP_850nm (GrayscaleImage) static unmixed GCaMP image of the FOV with excitation 850 nm | shape = (512, 512) | dtype = float64
  Dataset /processing/ophys/static_GCaMP_and_retrograde_label_image_plane_1/mScarlet_800nm (GrayscaleImage) static unmixed mScarlet image of the FOV with excitation 800 nm | shape = (512, 512) | dtype = float64
  Dataset /processing/ophys/static_GCaMP_and_retrograde_label_image_plane_1/mTagBFP2_850nm (GrayscaleImage) static unmixed mTagBFP2 image of the FOV with excitation 850 nm | shape = (512, 512) | dtype = float64
  Group /processing/ophys/static_GCaMP_and_retrograde_label_image_plane_2 (Images) static unmixed images for GCaMP and retrograde labels of the FOV
  Dataset /processing/ophys/static_GCaMP_and_retrograde_label_image_plane_2/GCaMP_800nm (GrayscaleImage) static unmixed GCaMP image of the FOV with excitation 800 nm | shape = (512, 512) | dtype = float64
  Dataset /processing/ophys/static_GCaMP_and_retrograde_label_image_plane_2/GCaMP_850nm (GrayscaleImage) static unmixed GCaMP image of the FOV with excitation 850 nm | shape = (512, 512) | dtype = float64
  Dataset /processing/ophys/static_GCaMP_and_retrograde_label_image_plane_2/mScarlet_800nm (GrayscaleImage) static unmixed mScarlet image of the FOV with excitation 800 nm | shape = (512, 512) | dtype = float64
  Dataset /processing/ophys/static_GCaMP_and_retrograde_label_image_plane_2/mTagBFP2_850nm (GrayscaleImage) static unmixed mTagBFP2 image of the FOV with excitation 850 nm | shape = (512, 512) | dtype = float64
  Group /processing/ophys/static_GCaMP_and_retrograde_label_image_plane_3 (Images) static unmixed images for GCaMP and retrograde labels of the FOV
  Dataset /processing/ophys/static_GCaMP_and_retrograde_label_image_plane_3/GCaMP_800nm (GrayscaleImage) static unmixed GCaMP image of the FOV with excitation 800 nm | shape = (512, 512) | dtype = float64
  Dataset /processing/ophys/static_GCaMP_and_retrograde_label_image_plane_3/GCaMP_850nm (GrayscaleImage) static unmixed GCaMP image of the FOV with excitation 850 nm | shape = (512, 512) | dtype = float64
  Dataset /processing/ophys/static_GCaMP_and_retrograde_label_image_plane_3/mScarlet_800nm (GrayscaleImage) static unmixed mScarlet image of the FOV with excitation 800 nm | shape = (512, 512) | dtype = float64
  Dataset /processing/ophys/static_GCaMP_and_retrograde_label_image_plane_3/mTagBFP2_850nm (GrayscaleImage) static unmixed mTagBFP2 image of the FOV with excitation 850 nm | shape = (512, 512) | dtype = float64
  session_description: Mouse performing a dynamic navigation task with calcium imaging in visA layer 2/3
  session_start_time: 2017-05-16T14:34:23.089680-04:00
  timestamps_reference_time: 2017-05-16T14:34:23.089680-04:00


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2023-07-21T10:32:37.070285-04:00']
  Group /general/devices/two_photon_microscope (Device) Two-photon microscope
  experiment_description: Widefield retinotopy and 2p window vessel and retrograde label overview
  experimenter: ['Tseng, Shih-Yi']
  Group /general/harvey_lab_swac_metadata_mouse (LabMetaDataMouse) 
  institution: Harvard Medical School
  keywords: ['cortex' 'retinotopy' 'widefield imaging']
  lab: Harvey Lab
  Group /general/optophysiology/ImagingPlane_mTagBFP2_850nm (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane_mTagBFP2_850nm/OpticalChannel_mTagBFP2 (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane_mTagBFP2_850nm/device (Device) Two-photon microscope
  related_publications: ['doi:10.1016/j.neuron.2022.05.012']
  session_id: Mouse_3_widefield_retinotopy_and_window_vessel
  Group /general/subject (Subject) 
  surgery: cranial window creation date:2017-04-03, 3.5 mm diameter, left posterior cortex; AAVretro injection date:2017-04-03; GCaMP6s injection date:2017-04-03; performed by Shih-Yi Tseng and Selmaan N. Chettih
  virus: AAV2/1-synapsin-GCaMP6s-WPRE-SV40 in left V1 x3 sites, PM x1, AM x0, MM x1, RSC x1, visA x1, 1/10 dilution, 140nl per site in L23 and 140nl per site in L5; AAV2retro-Syn-mTagBFP2 in left anterior ACC/M2 x3, undiluted, 300 nl per site, coordinate (mm from bregma): (A 0.95, L 0.6, D 1.0), (A 0.95, L 0.6, D 0.3), (A 0.95, L 0.8, D 0.3); AAV2retro-Syn-mScarlet in left striatum x3, 1/20 dilution, 300 nl per site, coordinate (mm from bregma): (A 0.95, L 1.2, D 2.1), (A 1.0, L 1.75, D 2.1), (P 0.15, L 2.15, D 2.1); mScarlet expression did not come up when examining it under the 2P microscope (due to the higher dilution)
  identifier: Mouse_3_widefield_retinotopy_and_window_vessel
  Group /processing/ophys (ProcessingModule) cranial window vessel image under 2P microscope
  Group /processing/ophys/whole_window_mTagBFP2_img_2p (Images) raw and processed mTagBFP2 images for the whole window with stitching FOVs under 2P microscope
  Dataset /processing/ophys/whole_window_mTagBFP2_img_2p/processed_whole_window_mTagBFP2_img_L2 (GrayscaleImage) processed image of stitched mTagBFP2 image in L2 (remove the overlaping regions, resize to 660.533 pixels per mm, and rotate 90 degree + fliplr so now x axis is ~lateral to medial, y axis is ~posterior to anterior, same orientation as WF vessel).Use the Registration__rs_to_ccf_mm_transformation_matrix in lab_meta_data to transform the resize/processed image to CCF. | shape = (1786, 1991) | dtype = float64
  Dataset /processing/ophys/whole_window_mTagBFP2_img_2p/processed_whole_window_mTagBFP2_img_L3 (GrayscaleImage) processed image of stitched mTagBFP2 image in L3 (remove the overlaping regions, resize to 660.533 pixels per mm, and rotate 90 degree + fliplr so now x axis is ~lateral to medial, y axis is ~posterior to anterior, same orientation as WF vessel).Use the Registration__rs_to_ccf_mm_transformation_matrix in lab_meta_data to transform the resize/processed image to CCF. | shape = (1786, 1991) | dtype = float64
  Dataset /processing/ophys/whole_window_mTagBFP2_img_2p/processed_whole_window_mTagBFP2_img_L5 (GrayscaleImage) processed image of stitched mTagBFP2 image in L5 (remove the overlaping regions, resize to 660.533 pixels per mm, and rotate 90 degree + fliplr so now x axis is ~lateral to medial, y axis is ~posterior to anterior, same orientation as WF vessel).Use the Registration__rs_to_ccf_mm_transformation_matrix in lab_meta_data to transform the resize/processed image to CCF. | shape = (1786, 1991) | dtype = float64
  Dataset /processing/ophys/whole_window_mTagBFP2_img_2p/raw_whole_window_mTagBFP2_img_L2 (GrayscaleImage) raw mTagBFP2 image in L2 for the whole window with stitching FOVs under 2P microscope | shape = (2048, 2048) | dtype = uint16
  Dataset /processing/ophys/whole_window_mTagBFP2_img_2p/raw_whole_window_mTagBFP2_img_L3 (GrayscaleImage) raw mTagBFP2 image in L3 for the whole window with stitching FOVs under 2P microscope | shape = (2048, 2048) | dtype = uint16
  Dataset /processing/ophys/whole_window_mTagBFP2_img_2p/raw_whole_window_mTagBFP2_img_L5 (GrayscaleImage) raw mTagBFP2 image in L5 for the whole window with stitching FOVs under 2P microscope | shape = (2048, 2048) | dtype = uint16
  Group /processing/ophys/whole_window_vessel_img_2p (Images) raw and processed images of vessel pattern at brain surface for the whole window with stitching FOVs under 2P microscope
  Dataset /processing/ophys/whole_window_vessel_img_2p/processed_whole_window_vessel_img_2p (GrayscaleImage) processed image of stitched vessel pattern (remove the overlaping regions, resize to 660.533 pixels per mm, and rotate 90 degree + fliplr so now x axis is ~lateral to medial, y axis is ~posterior to anterior, same orientation as WF vessel). Use the Registration__rs_to_ccf_mm_transformation_matrix in lab_meta_data to transform the resize/processed image to CCF. | shape = (1786, 1991) | dtype = float64
  Dataset /processing/ophys/whole_window_vessel_img_2p/raw_whole_window_vessel_img_2p (GrayscaleImage) raw image of vessel pattern at brain surface for the whole window with stitching FOVs under 2P microscope | shape = (2048, 2048) | dtype = uint16
  Group /processing/retinotopy (ProcessingModule) widefield and cranial window vessel image
  Group /processing/retinotopy/widefield_imaging (Images) results of widefield imaging in this mouse. Use the Registration__wf_to_rs_mm_transformation_matrix in lab_meta_data to algin the WF images to the resize/processed images.
  Dataset /processing/retinotopy/widefield_imaging/axis_1_phase_map_altitude (GrayscaleImage) axis 1 (altitude) phase map in degree collected with widefield imaging | shape = (512, 512) | dtype = float64
  Dataset /processing/retinotopy/widefield_imaging/axis_2_phase_map_azimuth (GrayscaleImage) axis 2 (azimuth) phase map in degree collected with widefield imaging | shape = (512, 512) | dtype = float64
  Dataset /processing/retinotopy/widefield_imaging/field_sign_map (GrayscaleImage) field sign map collected with widefield imaging | shape = (512, 512) | dtype = float64
  Dataset /processing/retinotopy/widefield_imaging/power_map_avg (GrayscaleImage) average FFT power map collected with widefield imaging | shape = (512, 512) | dtype = float64
  Dataset /processing/retinotopy/widefield_imaging/widefield_vessel_image (GrayscaleImage) image of vessel pattern at brain surface for the whole window collected with widefield imaging | shape = (512, 512) | dtype = uint16
  session_description: Widefield retinotopy and 2p window vessel and retrograde label overview
  session_start_time: 2017-10-19T00:00:00-04:00
  timestamps_reference_time: 2017-10-19T00:00:00-04:00


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Virmen_forward_lateral_velocity_timeseries (TimeSeries) Raw forward and lateral velocity (in maze) in Virmen frames (sampled at ~30 Hz)
  Group /acquisition/Virmen_maze_world_timeseries (TimeSeries) Maze world in Virmen frames (sampled at ~30 Hz), 1:WLV, 2:BRV, 3:WRV, 4:BLV, 5:WLN, 6:BRN, 7:WRN, 8:BLN; B/W:black/white cue, L/R:left/right reward location, V/N:visually-guided/normal trial
  Group /acquisition/Virmen_positions (Position) 
  Group /acquisition/Virmen_positions/Virmen_forward_lateral_positions (SpatialSeries) Raw forward and lateral position in Virmen frames (sampled at ~30 Hz)
  Group /acquisition/Virmen_reward_timeseries (TimeSeries) Reward in Virmen frames (sampled at ~30 Hz), 1: reward delivered
  Group /acquisition/Virmen_trial_number_timeseries (TimeSeries) Trial number in Virmen frames (sampled at ~30 Hz)
  Group /acquisition/Virmen_trial_phase_timeseries (TimeSeries) Trial phase in Virmen frames (sampled at ~30 Hz), 0: maze, -1: feedback delay/feedback, -2: visual feedback onset, 1: ITI
  Group /acquisition/imaging_frame_timeseries (TimeSeries) Two photon imaging frame signals sampled at 2000 Hz
  Group /acquisition/lick_timeseries (TimeSeries) Analog lick signals sampled at 2000 Hz (some sessions have signal loss due to acquisition problems, so not a reliable signal)
  Group /acquisition/raw_velocity_timeseries (TimeSeries) Raw velocity of the spherical treadmill sampled at 2000 Hz, array of the shape: timestampes x [pitch, roll, yaw]
  Group /acquisition/virmen_frame_timeseries (TimeSeries) Virmen frame signals sampled at 2000 Hz
  file_create_date: ['2023-07-20T13:18:04.402449-04:00']
  Group /general/devices/two_photon_microscope (Device) Two-photon microscope
  experiment_description: Mouse performing a dynamic navigation task with calcium imaging in AM layer 2/3
  experimenter: ['Tseng, Shih-Yi']
  Group /general/harvey_lab_swac_metadata_session (LabMetaDataSession) 
  institution: Harvard Medical School
  keywords: ['mouse' 'decision-making' 'navigation' 'virtual reality' 'cortex'
   'calcium imaging' 'two-photon imaging']
  lab: Harvey Lab
  Group /general/optophysiology/ImagingPlane_GCaMP6s_920nm (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane_GCaMP6s_920nm/OpticalChannel_GCaMP (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane_GCaMP6s_920nm/device (Device) Two-photon microscope
  Group /general/optophysiology/ImagingPlane_mScarlet_800nm (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane_mScarlet_800nm/OpticalChannel_GCaMP (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane_mScarlet_800nm/OpticalChannel_mScarlet (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane_mScarlet_800nm/device (Device) Two-photon microscope
  Group /general/optophysiology/ImagingPlane_mTagBFP2_850nm (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane_mTagBFP2_850nm/OpticalChannel_GCaMP (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane_mTagBFP2_850nm/OpticalChannel_mTagBFP2 (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane_mTagBFP2_850nm/device (Device) Two-photon microscope
  related_publications: ['doi:10.1016/j.neuron.2022.05.012']
  session_id: mouse_3_session_date_2017-04-27_area_AM_L23_single_plane_imaging
  stimulus: maze_stem_length=200.0;maze_stem_width=10.01;maze_arm_length=50.0;maze_arm_width=60.0;cue_delay_length=0.0;wall_height=20.0;max_position=255.0;frac_non_visually_guided_trials=1.0;choice_bias_penalty=0;feedback_delay=1.0;reward_delay=3.0;iti_correct=2.0;iti_incorrect=2.0
  Group /general/subject (Subject) 
  surgery: cranial window creation date:2017-04-03, 3.5 mm diameter, left posterior cortex; AAVretro injection date:2017-04-03; GCaMP6s injection date:2017-04-03; performed by Shih-Yi Tseng and Selmaan N. Chettih
  virus: AAV2/1-synapsin-GCaMP6s-WPRE-SV40 in left V1 x3 sites, PM x1, AM x0, MM x1, RSC x1, visA x1, 1/10 dilution, 140nl per site in L23 and 140nl per site in L5; AAV2retro-Syn-mTagBFP2 in left anterior ACC/M2 x3, undiluted, 300 nl per site, coordinate (mm from bregma): (A 0.95, L 0.6, D 1.0), (A 0.95, L 0.6, D 0.3), (A 0.95, L 0.8, D 0.3); AAV2retro-Syn-mScarlet in left striatum x3, 1/20 dilution, 300 nl per site, coordinate (mm from bregma): (A 0.95, L 1.2, D 2.1), (A 1.0, L 1.75, D 2.1), (P 0.15, L 2.15, D 2.1); mScarlet expression did not come up when examining it under the 2P microscope (due to the higher dilution)
  identifier: Mouse_3_session_date_2017-04-27
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/epoch_type (VectorData) type of epoch: maze, maze_stem, maze_arm, feedback_delay, feedback, iti, feedback_and_iti | shape = (3464,) | dtype = object
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (3464,) | dtype = int32
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (3464,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (3464,) | dtype = float64
  Dataset /intervals/epochs/trial_id (VectorData) trial number for this epoch | shape = (3464,) | dtype = int32
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/association_mat (VectorData) behavioral LSTM predicted conditional probability, order: P(R|W), P(L|W), P(R|B), P(L|B) | shape = (495, 4) | dtype = float64
  Dataset /intervals/trials/bias_following (VectorData) the bias-following on the trial (between -0.5 ~ 0.5) | shape = (495,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (495,) | dtype = int32
  Dataset /intervals/trials/is_choL (VectorData) whether the mouse made a left choice on the trial (True: left, False: right) | shape = (495,) | dtype = bool
  Dataset /intervals/trials/is_correct (VectorData) whether the trial was correct (True: correct, False: incorrect) | shape = (495,) | dtype = bool
  Dataset /intervals/trials/is_cueB (VectorData) whether the trial had a black cue (True: black, False: white) | shape = (495,) | dtype = bool
  Dataset /intervals/trials/is_ruleA (VectorData) whether the trial happened during rule A (True: rule A (BL,WR), False: rule B(WL,BR)) | shape = (495,) | dtype = bool
  Dataset /intervals/trials/is_switch (VectorData) whether a rule switch happened on the trial (True: switch, False: non-switch) | shape = (495,) | dtype = bool
  Dataset /intervals/trials/is_vis (VectorData) whether the trial was a visually guided trial (True: visually guided, False: non-visually guided) | shape = (495,) | dtype = bool
  Dataset /intervals/trials/prob_actual_cho (VectorData) the probability of actual choice on the trial, i.e. P(actual choice|actual cue) | shape = (495,) | dtype = float64
  Dataset /intervals/trials/rule_belief (VectorData) the rule belief on the trial (pos: rule B, neg: rule A) | shape = (495,) | dtype = float64
  Dataset /intervals/trials/rule_following (VectorData) the rule-following on the trial (between -0.5 ~ 0.5) | shape = (495,) | dtype = float64
  Dataset /intervals/trials/signed_bias (VectorData) the singed choice bias on the trial (pos: left bias, neg: right bias) | shape = (495,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (495,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (495,) | dtype = float64
  Dataset /intervals/trials/trial_offset_plane_frame_idx (VectorData) correspoding imaging frame index for this trial offset for each imaging plane | shape = (495, 1) | dtype = int32
  Dataset /intervals/trials/trial_onset_plane_frame_idx (VectorData) correspoding imaging frame index for this trial onset for each imaging plane | shape = (495, 1) | dtype = int32
  Group /processing/behavior (ProcessingModule) processed behavioral data
  Group /processing/behavior/frame_aligned_position (Position) 
  Group /processing/behavior/frame_aligned_position/frame_aligned_forward_and_lateral_position (SpatialSeries) forward and lateral position aligned to imaging frames (30 Hz)
  Group /processing/behavior/frame_aligned_time_from_choice_point (TimeSeries) time elapsed (sec) from choice point aligned to imaging frames (neg: maze, pos: feedback and ITI)
  Group /processing/behavior/frame_aligned_trial_number (TimeSeries) trial number aligned to imaging frames
  Group /processing/behavior/frame_aligned_velocity (BehavioralTimeSeries) 
  Group /processing/behavior/frame_aligned_velocity/frame_aligned_pitch_roll_yaw_velocity (TimeSeries) velocity of the spherical treadmill (pitch, roll, yaw) aligned to imaging frames (30 Hz)
  Group /processing/behavior/frame_to_verm_index_conversion (TimeSeries) correspoding verm frame index for each imaging frame
  Group /processing/behavior/velocity_RNN_prediction_for_choice_and_cue (BehavioralTimeSeries) 
  Group /processing/behavior/velocity_RNN_prediction_for_choice_and_cue/velocity_RNN_prediction_for_choice_and_cue (TimeSeries) velocity RNN prediction (forward choice, reverse choice, forward cue, reverse cue) aligned to mid imaging frames (idx=2) of each 6 Hz volume (or pseudovolume for plane imaging)
  Group /processing/behavior/verm_to_frame_index_conversion (TimeSeries) correspoding imaging frame index for each verm frame
  Group /processing/ophys (ProcessingModule) two photon calcium imaging processed data
  Group /processing/ophys/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation_0 (PlaneSegmentation) Plane segmentation of imagine plane 0
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_0/ap (VectorData) ap location (mm from bregma) | shape = (229,) | dtype = float64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_0/area (VectorData) cortical area where this cell is located | shape = (229,) | dtype = object
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_0/depth (VectorData) depth (mm from pia) | shape = (229,) | dtype = float64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_0/id (ElementIdentifiers)  | shape = (229,) | dtype = int32
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation_0/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation_0/imaging_plane/OpticalChannel_GCaMP (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation_0/imaging_plane/device (Device) Two-photon microscope
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_0/mScarlet (VectorData) whether this cell is labeled with Scarlet | shape = (229,) | dtype = bool
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_0/mTagBFP2 (VectorData) whether this cell is labeled with mTagBFP2 | shape = (229,) | dtype = bool
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_0/ml (VectorData) ml location (mm from bregma) | shape = (229,) | dtype = float64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_0/pixel_mask (VectorData) Pixel masks for each ROI | shape = (26421,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation_0/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (229,) | dtype = uint16
  Group /processing/ophys/deconvolved_activity_plane_0 (RoiResponseSeries) Deconvolved activity for ROIs in PlaneSegmentation_0
  Dataset /processing/ophys/deconvolved_activity_plane_0/rois (DynamicTableRegion) the ROIs in PlaneSegmentation_0 | shape = (229,) | dtype = int32
  Group /processing/ophys/df_over_f_plane_0 (DfOverF) 
  Group /processing/ophys/df_over_f_plane_0/dF_over_F_plane_0 (RoiResponseSeries) dF/F for ROIs in PlaneSegmentation_0
  Dataset /processing/ophys/df_over_f_plane_0/dF_over_F_plane_0/rois (DynamicTableRegion) the ROIs in PlaneSegmentation_0 | shape = (229,) | dtype = int32
  Group /processing/ophys/static_GCaMP_and_retrograde_label_image_plane_0 (Images) static unmixed images for GCaMP and retrograde labels of the FOV
  Dataset /processing/ophys/static_GCaMP_and_retrograde_label_image_plane_0/GCaMP_800nm (GrayscaleImage) static unmixed GCaMP image of the FOV with excitation 800 nm | shape = (512, 512) | dtype = float64
  Dataset /processing/ophys/static_GCaMP_and_retrograde_label_image_plane_0/GCaMP_850nm (GrayscaleImage) static unmixed GCaMP image of the FOV with excitation 850 nm | shape = (512, 512) | dtype = float64
  Dataset /processing/ophys/static_GCaMP_and_retrograde_label_image_plane_0/mScarlet_800nm (GrayscaleImage) static unmixed mScarlet image of the FOV with excitation 800 nm | shape = (512, 512) | dtype = float64
  Dataset /processing/ophys/static_GCaMP_and_retrograde_label_image_plane_0/mTagBFP2_850nm (GrayscaleImage) static unmixed mTagBFP2 image of the FOV with excitation 850 nm | shape = (512, 512) | dtype = float64
  Group /processing/ophys/vessel_img (Images) image of vessel pattern at brain surface for this FOV
  Dataset /processing/ophys/vessel_img/vessel_img (GrayscaleImage) image of vessel pattern at brain surface for this FOV | shape = (512, 512) | dtype = float64
  session_description: Mouse performing a dynamic navigation task with calcium imaging in AM layer 2/3
  session_start_time: 2017-04-27T16:32:24.231202-04:00
  timestamps_reference_time: 2017-04-27T16:32:24.231202-04:00
