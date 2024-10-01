
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000951/0.240418.2218
name: Dataset for Mapping model units to visual neurons reveals population code for social behavior
contributor: [{'url': 'https://cowleygroup.cshl.edu/', 'name': 'Cowley, Benjamin', 'email': 'cowley@cshl.edu', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0003-2681-2448', 'affiliation': [{'name': 'Cold Spring Harbor Laboratory', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/02qz8b764'}], 'includeInCitation': True}, {'name': 'Calhoun, Adam', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0001-9347-7956', 'awardNumber': 'Simons Collaboration on the Global Brain Postdoctoral Fellowship', 'includeInCitation': True}, {'name': 'Rangarajan, Nivedita', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Ireland, Elise', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'includeInCitation': True}, {'url': 'https://pillowlab.princeton.edu/', 'name': 'Pillow, Jonathan', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'awardNumber': 'The Simons Collaboration on the Global Brain Investigator Awards and NIH BRAIN Initiative Award (R01 NS104899)', 'includeInCitation': True}, {'url': 'https://murthylab.princeton.edu/', 'name': 'Murthy, Mala', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0003-3063-3389', 'awardNumber': 'The Simons Collaboration on the Global Brain Investigator Awards and NIH BRAIN Initiative Award (R01 NS104899), and an HHMI Faculty Scholar Award and NINDS R35 Research Program Award.', 'includeInCitation': True}]
description: This is the dataset for the paper "Mapping model units to visual neurons reveals population code for social behavior" from Cowley et al., 2024. It contains 459 fruit fly courtship sessions, where 23 different LC neuron types have been silenced in male fruit flies.  The data comprise raw camera recordings, processed SLEAP joint position tracks, song labels, male behavior, and reconstructed stimuli. The dataset also contains calcium imaging data of male flies for 5 different LC neuron types, including raw TIF images and processed dF/F responses.
assetsSummary: {'species': [{'name': 'Drosophila melanogaster - Fruit fly', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_7227'}], 'approach': [{'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}, {'name': 'behavioral approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 486506743673, 'numberOfFiles': 1413, 'numberOfSubjects': 486, 'variableMeasured': ['ProcessingModule', 'PlaneSegmentation', 'OpticalChannel', 'ImagingPlane', 'TwoPhotonSeries', 'BehavioralTimeSeries', 'SpatialSeries'], 'measurementTechnique': [{'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'two-photon microscopy technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000951 has 100 NWB files.
36 of these NWB files are of type 1.
32 of these NWB files are of type 2.
32 of these NWB files are of type 3.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/TwoPhotonSeries (TwoPhotonSeries) Imaging data from two-photon excitation microscopy.
  Group /acquisition/TwoPhotonSeries/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeries/imaging_plane/Green (OpticalChannel) 
  Group /acquisition/TwoPhotonSeries/imaging_plane/OpticalChannel (OpticalChannel) 
  Group /acquisition/TwoPhotonSeries/imaging_plane/device (Device) We recorded LC responses of a head-fixed male fly using a custom-built two-photon microscope with a 40x objective and a two-photon laser (Coherent) tuned to 920 nm for imaging of GCaMP6f. The laser is from Coherent Labs tuned to 920 nm for imaging of GCaMP6f. A 562 nm dichroic split the emission light into red and green channels, which were then passed through a red 545-604 nm and green 485-555 nm bandpass filter respectively. Data was recorded from the green channel.
  file_create_date: ['2024-03-30T10:53:24.805031-04:00']
  Group /general/devices/Microscope (Device) We recorded LC responses of a head-fixed male fly using a custom-built two-photon microscope with a 40x objective and a two-photon laser (Coherent) tuned to 920 nm for imaging of GCaMP6f. The laser is from Coherent Labs tuned to 920 nm for imaging of GCaMP6f. A 562 nm dichroic split the emission light into red and green channels, which were then passed through a red 545-604 nm and green 485-555 nm bandpass filter respectively. Data was recorded from the green channel.
  experiment_description: Courtship experiment with knockout training
  experimenter: ['Cowley, Benjamin R.' 'Calhoun, Adam J.' 'Rangarajan, Nivedita'
   'Ireland, Elise' 'Turner, Maxwell H.' 'Pillow, Jonathan W' 'Murthy, Mala']
  institution: Princeton
  keywords: ['optical physiology' 'fly' 'behavior' 'deep learning']
  lab: Murthy
  Group /general/optophysiology/ImagingPlane (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane/Green (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane/OpticalChannel (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane/device (Device) We recorded LC responses of a head-fixed male fly using a custom-built two-photon microscope with a 40x objective and a two-photon laser (Coherent) tuned to 920 nm for imaging of GCaMP6f. The laser is from Coherent Labs tuned to 920 nm for imaging of GCaMP6f. A 562 nm dichroic split the emission light into red and green channels, which were then passed through a red 545-604 nm and green 485-555 nm bandpass filter respectively. Data was recorded from the green channel.
  related_publications: ['https://doi.org/10.1101/2022.07.18.500505']
  Group /general/subject (Subject) 
  identifier: 431b1896-7c54-4461-b1bf-24354dea07a7
  Group /processing/ophys (ProcessingModule) No description.
  Group /processing/ophys/DfOverF (DfOverF) 
  Group /processing/ophys/DfOverF/RoiResponseSeries (RoiResponseSeries) Array of df/F traces.
  Dataset /processing/ophys/DfOverF/RoiResponseSeries/rois (DynamicTableRegion) The ROIs for ImagingPlane. | shape = (1,) | dtype = int64
  Group /processing/ophys/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation (PlaneSegmentation) Segmented ROIs
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/Accepted (VectorData) 1 if ROI was accepted or 0 if rejected as a cell during segmentation operation. | shape = (1,) | dtype = int64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/ROICentroids (VectorData) The x, y, (z) centroids of each ROI. | shape = (1, 2) | dtype = int64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/Rejected (VectorData) 1 if ROI was rejected or 0 if accepted as a cell during segmentation operation. | shape = (1,) | dtype = int64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/image_mask (VectorData) Image masks for each ROI. | shape = (1, 256, 256) | dtype = float64
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/Green (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/OpticalChannel (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/device (Device) We recorded LC responses of a head-fixed male fly using a custom-built two-photon microscope with a 40x objective and a two-photon laser (Coherent) tuned to 920 nm for imaging of GCaMP6f. The laser is from Coherent Labs tuned to 920 nm for imaging of GCaMP6f. A 562 nm dichroic split the emission light into red and green channels, which were then passed through a red 545-604 nm and green 485-555 nm bandpass filter respectively. Data was recorded from the green channel.
  session_description: The rich variety of behaviors observed in animals arises through the interplay between sensory processing and motor control. To understand these sensorimotor transformations, it is useful to build models that predict not only neural responses to sensory input but also how each neuron causally contributes to behavior. Here we demonstrate a novel modeling approach to identify a one-to-one mapping between internal units in a deep neural network and real neurons by predicting the behavioral changes arising from systematic perturbations of more than a dozen neuronal cell types. A key ingredient we introduce is “knockout training”, which involves perturbing the network during training to match the perturbations of the real neurons during behavioral experiments. We apply this approach to model the sensorimotor transformations of Drosophila melanogaster males during a complex, visually-guided social behavior. The visual projection neurons at the interface between the optic lobe and central brain form a set of discrete channels, and prior work indicates that each channel encodes a specific visual feature to drive a particular behavior. Our model reaches a different conclusion---Combinations of visual projection neurons, including those involved in non-social behaviors, drive male interactions with the female, forming a rich population code for behavior. Overall, our framework consolidates behavioral effects elicited from various neural perturbations into a single, unified model, providing a map from stimulus to neuronal cell type to behavior, and enabling future incorporation of the brain’s wiring diagram into the model.
  session_start_time: 2021-05-25T00:00:00-04:00
  Group /stimulus/presentation/nivexp_backnforth (ImageSeries) nivexp_backnforth
  Group /stimulus/presentation/nivexp_looming (ImageSeries) nivexp_looming
  Group /stimulus/presentation/nivexp_niv_angular_velocity_speed0 (ImageSeries) nivexp_niv_angular_velocity_speed0
  Group /stimulus/presentation/nivexp_niv_angular_velocity_speed1 (ImageSeries) nivexp_niv_angular_velocity_speed1
  Group /stimulus/presentation/nivexp_niv_angular_velocity_speed2 (ImageSeries) nivexp_niv_angular_velocity_speed2
  Group /stimulus/presentation/nivexp_niv_angular_velocity_speed3 (ImageSeries) nivexp_niv_angular_velocity_speed3
  Group /stimulus/presentation/nivexp_niv_looming_speed0 (ImageSeries) nivexp_niv_looming_speed0
  Group /stimulus/presentation/nivexp_niv_looming_speed1 (ImageSeries) nivexp_niv_looming_speed1
  Group /stimulus/presentation/nivexp_niv_looming_speed2 (ImageSeries) nivexp_niv_looming_speed2
  Group /stimulus/presentation/nivexp_niv_looming_speed3 (ImageSeries) nivexp_niv_looming_speed3
  Group /stimulus/presentation/nivexp_niv_sweeping_spot_radius0_speed0 (ImageSeries) nivexp_niv_sweeping_spot_radius0_speed0
  Group /stimulus/presentation/nivexp_niv_sweeping_spot_radius0_speed1 (ImageSeries) nivexp_niv_sweeping_spot_radius0_speed1
  Group /stimulus/presentation/nivexp_niv_sweeping_spot_radius0_speed2 (ImageSeries) nivexp_niv_sweeping_spot_radius0_speed2
  Group /stimulus/presentation/nivexp_niv_sweeping_spot_radius0_speed3 (ImageSeries) nivexp_niv_sweeping_spot_radius0_speed3
  Group /stimulus/presentation/nivexp_niv_sweeping_spot_radius0_speed4 (ImageSeries) nivexp_niv_sweeping_spot_radius0_speed4
  Group /stimulus/presentation/nivexp_niv_sweeping_spot_radius0_speed5 (ImageSeries) nivexp_niv_sweeping_spot_radius0_speed5
  Group /stimulus/presentation/nivexp_niv_sweeping_spot_radius0_speed6 (ImageSeries) nivexp_niv_sweeping_spot_radius0_speed6
  Group /stimulus/presentation/nivexp_niv_sweeping_spot_radius1_speed0 (ImageSeries) nivexp_niv_sweeping_spot_radius1_speed0
  Group /stimulus/presentation/nivexp_niv_sweeping_spot_radius2_speed0 (ImageSeries) nivexp_niv_sweeping_spot_radius2_speed0
  Group /stimulus/presentation/nivexp_niv_sweeping_spot_radius3_speed0 (ImageSeries) nivexp_niv_sweeping_spot_radius3_speed0
  Group /stimulus/presentation/nivexp_niv_sweeping_spot_radius4_speed0 (ImageSeries) nivexp_niv_sweeping_spot_radius4_speed0
  Group /stimulus/presentation/nivexp_niv_sweeping_spot_radius5_speed0 (ImageSeries) nivexp_niv_sweeping_spot_radius5_speed0
  Group /stimulus/presentation/nivexp_niv_sweeping_spot_radius6_speed0 (ImageSeries) nivexp_niv_sweeping_spot_radius6_speed0
  Group /stimulus/presentation/nivexp_niv_sweeping_spot_radius7_speed0 (ImageSeries) nivexp_niv_sweeping_spot_radius7_speed0
  Group /stimulus/presentation/nivexp_niv_sweeping_spot_radius8_speed0 (ImageSeries) nivexp_niv_sweeping_spot_radius8_speed0
  Group /stimulus/presentation/nivexp_optimized_changes_in_ori (ImageSeries) nivexp_optimized_changes_in_ori
  Group /stimulus/presentation/nivexp_optimized_forward_vels (ImageSeries) nivexp_optimized_forward_vels
  Group /stimulus/presentation/nivexp_optimized_forward_vels_fixedlocation (ImageSeries) nivexp_optimized_forward_vels_fixedlocation
  Group /stimulus/presentation/nivexp_optimized_lateral_vels (ImageSeries) nivexp_optimized_lateral_vels
  Group /stimulus/presentation/nivexp_optimized_lateral_vels_fasttransition (ImageSeries) nivexp_optimized_lateral_vels_fasttransition
  Group /stimulus/presentation/nivexp_rotate (ImageSeries) nivexp_rotate
  Group /stimulus/presentation/nivexp_wildtype (ImageSeries) nivexp_wildtype
  timestamps_reference_time: 2021-05-25T00:00:00-04:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2024-04-01T18:50:36.271292-04:00']
  session_id: ('LC10a_fly0_170905_1023',)
  Group /general/subject (Subject) 
  identifier: 958098a7-76d7-45fd-974c-77e85325bd2e
  session_description: Processed SLEAP pose data
  session_start_time: 2017-09-05T10:23:00-04:00
  timestamps_reference_time: 2017-09-05T10:23:00-04:00


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Courtship behavior video (ImageSeries) Camera recording of male and female movement in arena, saved as mp4.
  file_create_date: ['2024-04-02T07:13:24.232527-04:00']
  experiment_description: Camera and microphone recordings of courtship behavior between male and female fruit flies.
  institution: Princeton University
  lab: Murthy Laboratory
  session_id: LC10a_fly0_170905_1023
  Group /general/subject (Subject) 
  identifier: 22bc3771-5b5f-43bf-b95d-575f69052abc
  Group /processing/behavior (ProcessingModule) Processed behavioral data
  Group /processing/behavior/Joint positions of head and body for male and female (BehavioralTimeSeries) 
  Group /processing/behavior/Joint positions of head and body for male and female/female body position (SpatialSeries) Position (x, y) in arena.
  Group /processing/behavior/Joint positions of head and body for male and female/female head position (SpatialSeries) Position (x, y) in arena.
  Group /processing/behavior/Joint positions of head and body for male and female/male body position (SpatialSeries) Position (x, y) in arena.
  Group /processing/behavior/Joint positions of head and body for male and female/male head position (SpatialSeries) Position (x, y) in arena.
  Group /processing/behavior/Male courtship behavior (BehavioralTimeSeries) 
  Group /processing/behavior/Male courtship behavior/male Pfast song (TimeSeries) Pfast song, 1-->Pfast song present, 0-->no song
  Group /processing/behavior/Male courtship behavior/male Pslow song (TimeSeries) Pslow song, 1-->Pslow song present, 0-->no song
  Group /processing/behavior/Male courtship behavior/male angular velocity (TimeSeries) Angular velocity in visual degrees/bin. To convert to visual degrees/s, multiply by frame rate 30Hz. Ang vel < 0 --> turn to the left.
  Group /processing/behavior/Male courtship behavior/male forward velocity (TimeSeries) Forward velocity in mm/bin. To convert to mm/s, multiply by frame rate 30Hz. Forward vel > 0 --> move forward.
  Group /processing/behavior/Male courtship behavior/male lateral velocity (TimeSeries) Lateral velocity in mm/bin. To convert to mm/s, multiply by frame rate 30Hz. Lat vel < 0 --> move to the left.
  Group /processing/behavior/Male courtship behavior/male sine song (TimeSeries) Sine song, 1-->sine song present, 0-->no song
  Group /processing/behavior/Reconstructed stimuli (ImageSeries) Stimuli reconstructed from the male's point of view during courtship.
  Group /processing/behavior/Song labels (BehavioralTimeSeries) 
  Group /processing/behavior/Song labels/song labels (TimeSeries) The song label for each frame. 0-->no song, 1-->Pfast, 2-->Pslow, 3-->sine. NaN ---> copulation occurred (ignore these frames)
  session_description: courtship session
  session_start_time: 2017-09-05T10:23:00-04:00
  timestamps_reference_time: 2017-09-05T10:23:00-04:00
