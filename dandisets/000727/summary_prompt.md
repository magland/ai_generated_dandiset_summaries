
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000727/0.240106.0043
name: Mapping the Neural Dynamics of Locomotion across the Drosophila Brain
contributor: [{'name': 'Brezovec, Luke', 'roleName': ['dcite:Author', 'dcite:Researcher', 'dcite:Software', 'dcite:Visualization', 'dcite:ContactPerson', 'dcite:Conceptualization', 'dcite:DataCollector'], 'schemaKey': 'Person', 'identifier': '0000-0001-9341-3565', 'affiliation': [], 'includeInCitation': True}, {'name': 'Berger, Andrew', 'roleName': ['dcite:Author', 'dcite:DataManager', 'dcite:Software'], 'schemaKey': 'Person', 'identifier': '0000-0003-4880-1264', 'affiliation': [], 'includeInCitation': True}, {'name': 'Druckmann, Shaul ', 'roleName': ['dcite:Author', 'dcite:FormalAnalysis', 'dcite:Researcher'], 'schemaKey': 'Person', 'identifier': '0000-0003-0068-3377', 'affiliation': [], 'includeInCitation': True}, {'url': 'http://clandininlab.stanford.edu/', 'name': 'Clandinin, Thomas', 'email': 'trc@stanford.edu', 'roleName': ['dcite:Author', 'dcite:Supervision', 'dcite:FundingAcquisition', 'dcite:ContactPerson', 'dcite:Conceptualization'], 'schemaKey': 'Person', 'identifier': '0000-0001-6277-6849', 'affiliation': [], 'includeInCitation': True}, {'url': 'http://www.nih.gov/', 'name': 'National Institutes of Health', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01cwqze88', 'awardNumber': 'R01EY022628,5U19NS104655,3R01NS11006003,5P30EY02687704', 'contactPoint': [], 'includeInCitation': False}, {'url': 'https://www.simonsfoundation.org', 'name': 'Simons Foundation', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01cmst727', 'contactPoint': [], 'includeInCitation': False}, {'name': 'Mayorquin, Heberto', 'roleName': ['dcite:DataCurator'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': False}, {'name': 'Trapani, Alessandra', 'roleName': ['dcite:DataCurator'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': False}]
description: Walking is a fundamental mode of locomotion, yet its neural correlates are unknown at brain-wide scale in any animal. We use volumetric two-photon imaging to map neural activity associated with walking across the entire brain of Drosophila. We detect locomotor signals in approximately 40% of the brain, identify a global signal associated with the transition from rest to walking, and define clustered neural signals selectively associated with changes in forward or angular velocity. These networks span functionally diverse brain regions, and include regions that have not been previously linked to locomotion. We also identify time-varying trajectories of neural activity that anticipate future movements, and that represent sequential engagement of clusters of neurons with different behavioral selectivity. These motor maps suggest a dynamical systems framework for constructing walking maneuvers reminiscent of models of forelimb reaching in primates and set a foundation for understanding how local circuits interact across large-scale networks.
assetsSummary: {'species': [{'name': 'Drosophila melanogaster - Fruit fly', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_7227'}], 'approach': [{'name': 'behavioral approach', 'schemaKey': 'ApproachType'}, {'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 609568504598, 'numberOfFiles': 18, 'numberOfSubjects': 9, 'variableMeasured': ['OpticalChannel', 'ImagingPlane', 'Position', 'ProcessingModule', 'TwoPhotonSeries', 'SpatialSeries'], 'measurementTechnique': [{'name': 'two-photon microscopy technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000727 has 5 NWB files.
1 of these NWB files are of type 1.
1 of these NWB files are of type 2.
1 of these NWB files are of type 3.
1 of these NWB files are of type 4.
1 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/TwoPhotonSeriesAnatomicalGreen (TwoPhotonSeries) Anatomical imaging data (GCaMP6f)
  Group /acquisition/TwoPhotonSeriesAnatomicalGreen/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeriesAnatomicalGreen/imaging_plane/Green (OpticalChannel) 
  Group /acquisition/TwoPhotonSeriesAnatomicalGreen/imaging_plane/device (Device) Bruker Ultima IV, Version 5.5.64.100
  Group /acquisition/TwoPhotonSeriesAnatomicalRed (TwoPhotonSeries) Anatomical imaging data (tdTomato)
  Group /acquisition/TwoPhotonSeriesAnatomicalRed/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeriesAnatomicalRed/imaging_plane/Red (OpticalChannel) 
  Group /acquisition/TwoPhotonSeriesAnatomicalRed/imaging_plane/device (Device) Bruker Ultima IV, Version 5.5.64.100
  Group /acquisition/TwoPhotonSeriesFunctionalGreen (TwoPhotonSeries) Functional imaging data (GCaMP6f)
  Group /acquisition/TwoPhotonSeriesFunctionalGreen/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeriesFunctionalGreen/imaging_plane/Green (OpticalChannel) 
  Group /acquisition/TwoPhotonSeriesFunctionalGreen/imaging_plane/device (Device) Bruker Ultima IV, Version 5.5.64.100
  Group /acquisition/TwoPhotonSeriesFunctionalRed (TwoPhotonSeries) Functional imaging data (tdTomato)
  Group /acquisition/TwoPhotonSeriesFunctionalRed/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeriesFunctionalRed/imaging_plane/Red (OpticalChannel) 
  Group /acquisition/TwoPhotonSeriesFunctionalRed/imaging_plane/device (Device) Bruker Ultima IV, Version 5.5.64.100
  Group /acquisition/Video: fictrac-20200228_161226-raw (ImageSeries) Video recorded by camera.
  file_create_date: ['2023-12-10T02:40:07.303276+01:00']
  Group /general/devices/BrukerFluorescenceMicroscope (Device) Bruker Ultima IV, Version 5.5.64.100
  Group /general/devices/Flea FL3-U3-13E4M-C (Device) Sensor used for imaging with FicTrac at 50 Hz with Edmund Optics 100 mm C Series Fixed Focal Length Lens
  experiment_description: We use volumetric two-photon imaging to map neural activity associated with walking across the entire brain of Drosophila. We detect locomotor signals in approximately 40% of the brain, identify a global signal associated with the transition from rest to walking, and define clustered neural signals selectively associated with changes in forward or angular velocity.
  experimenter: ['Brezovec, Luke' 'Berger, Andrew' 'Druckmann, Saul' 'Clandinin, Thomas']
  institution: Stanford
  keywords: ['walking' 'neural Correlates' 'brain-wide Scale' 'drosophila'
   'volumetric two-photon imaging' 'neural activity mapping'
   'locomotor signals']
  lab: Clandinin
  Group /general/optophysiology/ImagingPlaneFunctionalGreenProcessed (ImagingPlane) 
  Group /general/optophysiology/ImagingPlaneFunctionalGreenProcessed/Green (OpticalChannel) 
  Group /general/optophysiology/ImagingPlaneFunctionalGreenProcessed/device (Device) Bruker Ultima IV, Version 5.5.64.100
  Group /general/optophysiology/ImagingPlaneGCaMP6fAnatomical (ImagingPlane) 
  Group /general/optophysiology/ImagingPlaneGCaMP6fAnatomical/Green (OpticalChannel) 
  Group /general/optophysiology/ImagingPlaneGCaMP6fAnatomical/device (Device) Bruker Ultima IV, Version 5.5.64.100
  Group /general/optophysiology/ImagingPlaneGCaMP6fFunctional (ImagingPlane) 
  Group /general/optophysiology/ImagingPlaneGCaMP6fFunctional/Green (OpticalChannel) 
  Group /general/optophysiology/ImagingPlaneGCaMP6fFunctional/device (Device) Bruker Ultima IV, Version 5.5.64.100
  Group /general/optophysiology/ImagingPlanetdTomatoAnatomical (ImagingPlane) 
  Group /general/optophysiology/ImagingPlanetdTomatoAnatomical/Red (OpticalChannel) 
  Group /general/optophysiology/ImagingPlanetdTomatoAnatomical/device (Device) Bruker Ultima IV, Version 5.5.64.100
  Group /general/optophysiology/ImagingPlanetdTomatoFunctional (ImagingPlane) 
  Group /general/optophysiology/ImagingPlanetdTomatoFunctional/Red (OpticalChannel) 
  Group /general/optophysiology/ImagingPlanetdTomatoFunctional/device (Device) Bruker Ultima IV, Version 5.5.64.100
  related_publications: ['https://doi.org/10.1101/2022.03.20.485047']
  session_id: 20200228161226
  Group /general/subject (Subject) 
  surgery: Each fly was anesthetized on a chilled Peltier plate with a thermally coupled custom holder. Each immobilized fly was carefully fitted into a custom mount consisting of 3D-printed plastic and a custom cut steel shim to tightly nestle the head and thorax. To fix the fly to the mount, UV-curable glue was placed and cured on the dorsal region of the face between the eyes, and on the thorax. A saline solution was added to the dish for dissection (103 mM NaCl, 3 mM KCl, 5 mM TES, 1 mM NaH2PO4, 4 mM MgCl2, 1.5 mM CaCl2, 10 mM trehalose, 10 mM glucose, 7 mM sucrose, and 26 mM NaHCO3). Using a tungsten needle the posterior head cuticle was carefully cut and removed to reveal the whole brain (Figure S1). Dissection forceps were used to remove fat and trachea.
  identifier: d7ec53a6-989f-4daa-8b0e-0d440fe83718
  Group /processing/behavior (ProcessingModule) No description.
  Group /processing/behavior/FicTrac (Position) 
  Group /processing/behavior/FicTrac/SpatialSeriesAnimalHeading (SpatialSeries) Animal's heading direction in radians from the lab's perspective.
  Group /processing/behavior/FicTrac/SpatialSeriesIntegratedMotion (SpatialSeries) Integrated x/y position of the sphere in laboratory coordinates, neglecting heading.
  Group /processing/behavior/FicTrac/SpatialSeriesMovementDirection (SpatialSeries) Instantaneous running direction of the animal in the lab coordinates. Direction inferred by the ball's rotation (roll and pitch)
  Group /processing/behavior/FicTrac/SpatialSeriesMovementSpeed (SpatialSeries) Instantaneous running speed of the animal in radians per frame.
  Group /processing/behavior/FicTrac/SpatialSeriesPosition (SpatialSeries) x and y positions in the lab frame in radians, inferred by integrating the rotation over time.
  Group /processing/behavior/FicTrac/SpatialSeriesRotationCameraFrame (SpatialSeries) Orientation in radians from the camera's perspective. x: rotation to the sphere's right (pitch), y: rotation under the sphere (yaw), z: rotation behind the sphere (roll)
  Group /processing/behavior/FicTrac/SpatialSeriesRotationDeltaCameraFrame (SpatialSeries) Change in orientation since last frame from the camera's perspective. x: rotation to the sphere's right (pitch), y: rotation under the sphere (yaw), z: rotation behind the sphere (roll)
  Group /processing/behavior/FicTrac/SpatialSeriesRotationDeltaError (SpatialSeries) Error in rotation delta in radians from the lab's perspective.
  Group /processing/behavior/FicTrac/SpatialSeriesRotationDeltaLabFrame (SpatialSeries) Change in orientation since last frame from the lab's perspective. x: rotation in front of subject (roll), y: rotation to subject's right (pitch), z: rotation under the subject (yaw)
  Group /processing/behavior/FicTrac/SpatialSeriesRotationLabFrame (SpatialSeries) Orientation in radians from the lab's perspective. x: rotation in front of subject (roll), y: rotation to subject's right (pitch), z: rotation under the subject (yaw)
  Group /processing/ophys (ProcessingModule) No description.
  Group /processing/ophys/TwoPhotonSeriesFunctionalGreenProcessed (TwoPhotonSeries) motion corrected high-pass temporal filtered z-scored and registered into a common space, the Functional Drosophila Atlas
  Group /processing/ophys/TwoPhotonSeriesFunctionalGreenProcessed/imaging_plane (ImagingPlane) 
  Group /processing/ophys/TwoPhotonSeriesFunctionalGreenProcessed/imaging_plane/Green (OpticalChannel) 
  Group /processing/ophys/TwoPhotonSeriesFunctionalGreenProcessed/imaging_plane/device (Device) Bruker Ultima IV, Version 5.5.64.100
  session_description: We use volumetric two-photon imaging to map neural activity associated with walking across the entire brain of Drosophila. We detect locomotor signals in approximately 40% of the brain, identify a global signal associated with the transition from rest to walking, and define clustered neural signals selectively associated with changes in forward or angular velocity.
  session_start_time: 2020-02-28T16:12:42.799114-08:00
  timestamps_reference_time: 2020-02-28T16:12:42.799114-08:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/TwoPhotonSeriesAnatomicalGreen (TwoPhotonSeries) Anatomical imaging data (GCaMP6f)
  Group /acquisition/TwoPhotonSeriesAnatomicalGreen/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeriesAnatomicalGreen/imaging_plane/Green (OpticalChannel) 
  Group /acquisition/TwoPhotonSeriesAnatomicalGreen/imaging_plane/device (Device) Bruker Ultima IV, Version 5.5.64.100
  Group /acquisition/TwoPhotonSeriesAnatomicalRed (TwoPhotonSeries) Anatomical imaging data (tdTomato)
  Group /acquisition/TwoPhotonSeriesAnatomicalRed/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeriesAnatomicalRed/imaging_plane/Red (OpticalChannel) 
  Group /acquisition/TwoPhotonSeriesAnatomicalRed/imaging_plane/device (Device) Bruker Ultima IV, Version 5.5.64.100
  Group /acquisition/TwoPhotonSeriesFunctionalGreen (TwoPhotonSeries) Functional imaging data (GCaMP6f)
  Group /acquisition/TwoPhotonSeriesFunctionalGreen/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeriesFunctionalGreen/imaging_plane/Green (OpticalChannel) 
  Group /acquisition/TwoPhotonSeriesFunctionalGreen/imaging_plane/device (Device) Bruker Ultima IV, Version 5.5.64.100
  Group /acquisition/TwoPhotonSeriesFunctionalRed (TwoPhotonSeries) Functional imaging data (tdTomato)
  Group /acquisition/TwoPhotonSeriesFunctionalRed/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeriesFunctionalRed/imaging_plane/Red (OpticalChannel) 
  Group /acquisition/TwoPhotonSeriesFunctionalRed/imaging_plane/device (Device) Bruker Ultima IV, Version 5.5.64.100
  Group /acquisition/Video: fictrac-20200618_081653-raw (ImageSeries) Video recorded by camera.
  file_create_date: ['2023-12-10T11:15:48.049415+01:00']
  Group /general/devices/BrukerFluorescenceMicroscope (Device) Bruker Ultima IV, Version 5.5.64.100
  Group /general/devices/Flea FL3-U3-13E4M-C (Device) Sensor used for imaging with FicTrac at 50 Hz with Edmund Optics 100 mm C Series Fixed Focal Length Lens
  experiment_description: We use volumetric two-photon imaging to map neural activity associated with walking across the entire brain of Drosophila. We detect locomotor signals in approximately 40% of the brain, identify a global signal associated with the transition from rest to walking, and define clustered neural signals selectively associated with changes in forward or angular velocity.
  experimenter: ['Brezovec, Luke' 'Berger, Andrew' 'Druckmann, Saul' 'Clandinin, Thomas']
  institution: Stanford
  keywords: ['walking' 'neural Correlates' 'brain-wide Scale' 'drosophila'
   'volumetric two-photon imaging' 'neural activity mapping'
   'locomotor signals']
  lab: Clandinin
  Group /general/optophysiology/ImagingPlaneFunctionalGreenProcessed (ImagingPlane) 
  Group /general/optophysiology/ImagingPlaneFunctionalGreenProcessed/Green (OpticalChannel) 
  Group /general/optophysiology/ImagingPlaneFunctionalGreenProcessed/device (Device) Bruker Ultima IV, Version 5.5.64.100
  Group /general/optophysiology/ImagingPlaneGCaMP6fAnatomical (ImagingPlane) 
  Group /general/optophysiology/ImagingPlaneGCaMP6fAnatomical/Green (OpticalChannel) 
  Group /general/optophysiology/ImagingPlaneGCaMP6fAnatomical/device (Device) Bruker Ultima IV, Version 5.5.64.100
  Group /general/optophysiology/ImagingPlaneGCaMP6fFunctional (ImagingPlane) 
  Group /general/optophysiology/ImagingPlaneGCaMP6fFunctional/Green (OpticalChannel) 
  Group /general/optophysiology/ImagingPlaneGCaMP6fFunctional/device (Device) Bruker Ultima IV, Version 5.5.64.100
  Group /general/optophysiology/ImagingPlanetdTomatoAnatomical (ImagingPlane) 
  Group /general/optophysiology/ImagingPlanetdTomatoAnatomical/Red (OpticalChannel) 
  Group /general/optophysiology/ImagingPlanetdTomatoAnatomical/device (Device) Bruker Ultima IV, Version 5.5.64.100
  Group /general/optophysiology/ImagingPlanetdTomatoFunctional (ImagingPlane) 
  Group /general/optophysiology/ImagingPlanetdTomatoFunctional/Red (OpticalChannel) 
  Group /general/optophysiology/ImagingPlanetdTomatoFunctional/device (Device) Bruker Ultima IV, Version 5.5.64.100
  related_publications: ['https://doi.org/10.1101/2022.03.20.485047']
  session_id: 20200618081653
  Group /general/subject (Subject) 
  surgery: Each fly was anesthetized on a chilled Peltier plate with a thermally coupled custom holder. Each immobilized fly was carefully fitted into a custom mount consisting of 3D-printed plastic and a custom cut steel shim to tightly nestle the head and thorax. To fix the fly to the mount, UV-curable glue was placed and cured on the dorsal region of the face between the eyes, and on the thorax. A saline solution was added to the dish for dissection (103 mM NaCl, 3 mM KCl, 5 mM TES, 1 mM NaH2PO4, 4 mM MgCl2, 1.5 mM CaCl2, 10 mM trehalose, 10 mM glucose, 7 mM sucrose, and 26 mM NaHCO3). Using a tungsten needle the posterior head cuticle was carefully cut and removed to reveal the whole brain (Figure S1). Dissection forceps were used to remove fat and trachea.
  identifier: 0607caf0-359b-4a23-bf52-068caabd884a
  Group /processing/behavior (ProcessingModule) No description.
  Group /processing/behavior/FicTrac (Position) 
  Group /processing/behavior/FicTrac/SpatialSeriesAnimalHeading (SpatialSeries) Animal's heading direction in radians from the lab's perspective.
  Group /processing/behavior/FicTrac/SpatialSeriesIntegratedMotion (SpatialSeries) Integrated x/y position of the sphere in laboratory coordinates, neglecting heading.
  Group /processing/behavior/FicTrac/SpatialSeriesMovementDirection (SpatialSeries) Instantaneous running direction of the animal in the lab coordinates. Direction inferred by the ball's rotation (roll and pitch)
  Group /processing/behavior/FicTrac/SpatialSeriesMovementSpeed (SpatialSeries) Instantaneous running speed of the animal in radians per frame.
  Group /processing/behavior/FicTrac/SpatialSeriesPosition (SpatialSeries) x and y positions in the lab frame in radians, inferred by integrating the rotation over time.
  Group /processing/behavior/FicTrac/SpatialSeriesRotationCameraFrame (SpatialSeries) Orientation in radians from the camera's perspective. x: rotation to the sphere's right (pitch), y: rotation under the sphere (yaw), z: rotation behind the sphere (roll)
  Group /processing/behavior/FicTrac/SpatialSeriesRotationDeltaCameraFrame (SpatialSeries) Change in orientation since last frame from the camera's perspective. x: rotation to the sphere's right (pitch), y: rotation under the sphere (yaw), z: rotation behind the sphere (roll)
  Group /processing/behavior/FicTrac/SpatialSeriesRotationDeltaError (SpatialSeries) Error in rotation delta in radians from the lab's perspective.
  Group /processing/behavior/FicTrac/SpatialSeriesRotationDeltaLabFrame (SpatialSeries) Change in orientation since last frame from the lab's perspective. x: rotation in front of subject (roll), y: rotation to subject's right (pitch), z: rotation under the subject (yaw)
  Group /processing/behavior/FicTrac/SpatialSeriesRotationLabFrame (SpatialSeries) Orientation in radians from the lab's perspective. x: rotation in front of subject (roll), y: rotation to subject's right (pitch), z: rotation under the subject (yaw)
  Group /processing/ophys (ProcessingModule) No description.
  Group /processing/ophys/TwoPhotonSeriesFunctionalGreenProcessed (TwoPhotonSeries) motion corrected high-pass temporal filtered z-scored and registered into a common space, the Functional Drosophila Atlas
  Group /processing/ophys/TwoPhotonSeriesFunctionalGreenProcessed/imaging_plane (ImagingPlane) 
  Group /processing/ophys/TwoPhotonSeriesFunctionalGreenProcessed/imaging_plane/Green (OpticalChannel) 
  Group /processing/ophys/TwoPhotonSeriesFunctionalGreenProcessed/imaging_plane/device (Device) Bruker Ultima IV, Version 5.5.64.100
  session_description: We use volumetric two-photon imaging to map neural activity associated with walking across the entire brain of Drosophila. We detect locomotor signals in approximately 40% of the brain, identify a global signal associated with the transition from rest to walking, and define clustered neural signals selectively associated with changes in forward or angular velocity.
  session_start_time: 2020-06-18T08:17:27.446655-07:00
  timestamps_reference_time: 2020-06-18T08:17:27.446655-07:00


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/TwoPhotonSeriesAnatomicalGreen (TwoPhotonSeries) Anatomical imaging data (GCaMP6f)
  Group /acquisition/TwoPhotonSeriesAnatomicalGreen/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeriesAnatomicalGreen/imaging_plane/Green (OpticalChannel) 
  Group /acquisition/TwoPhotonSeriesAnatomicalGreen/imaging_plane/device (Device) Bruker Ultima IV, Version 5.5.64.100
  Group /acquisition/TwoPhotonSeriesAnatomicalRed (TwoPhotonSeries) Anatomical imaging data (tdTomato)
  Group /acquisition/TwoPhotonSeriesAnatomicalRed/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeriesAnatomicalRed/imaging_plane/Red (OpticalChannel) 
  Group /acquisition/TwoPhotonSeriesAnatomicalRed/imaging_plane/device (Device) Bruker Ultima IV, Version 5.5.64.100
  Group /acquisition/TwoPhotonSeriesFunctionalGreen (TwoPhotonSeries) Functional imaging data (GCaMP6f)
  Group /acquisition/TwoPhotonSeriesFunctionalGreen/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeriesFunctionalGreen/imaging_plane/Green (OpticalChannel) 
  Group /acquisition/TwoPhotonSeriesFunctionalGreen/imaging_plane/device (Device) Bruker Ultima IV, Version 5.5.64.100
  Group /acquisition/TwoPhotonSeriesFunctionalRed (TwoPhotonSeries) Functional imaging data (tdTomato)
  Group /acquisition/TwoPhotonSeriesFunctionalRed/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeriesFunctionalRed/imaging_plane/Red (OpticalChannel) 
  Group /acquisition/TwoPhotonSeriesFunctionalRed/imaging_plane/device (Device) Bruker Ultima IV, Version 5.5.64.100
  Group /acquisition/Video: fictrac-20200620_122048-raw (ImageSeries) Video recorded by camera.
  file_create_date: ['2023-12-10T00:55:46.182324+01:00']
  Group /general/devices/BrukerFluorescenceMicroscope (Device) Bruker Ultima IV, Version 5.5.64.100
  Group /general/devices/Flea FL3-U3-13E4M-C (Device) Sensor used for imaging with FicTrac at 50 Hz with Edmund Optics 100 mm C Series Fixed Focal Length Lens
  experiment_description: We use volumetric two-photon imaging to map neural activity associated with walking across the entire brain of Drosophila. We detect locomotor signals in approximately 40% of the brain, identify a global signal associated with the transition from rest to walking, and define clustered neural signals selectively associated with changes in forward or angular velocity.
  experimenter: ['Brezovec, Luke' 'Berger, Andrew' 'Druckmann, Saul' 'Clandinin, Thomas']
  institution: Stanford
  keywords: ['walking' 'neural Correlates' 'brain-wide Scale' 'drosophila'
   'volumetric two-photon imaging' 'neural activity mapping'
   'locomotor signals']
  lab: Clandinin
  Group /general/optophysiology/ImagingPlaneFunctionalGreenProcessed (ImagingPlane) 
  Group /general/optophysiology/ImagingPlaneFunctionalGreenProcessed/Green (OpticalChannel) 
  Group /general/optophysiology/ImagingPlaneFunctionalGreenProcessed/device (Device) Bruker Ultima IV, Version 5.5.64.100
  Group /general/optophysiology/ImagingPlaneGCaMP6fAnatomical (ImagingPlane) 
  Group /general/optophysiology/ImagingPlaneGCaMP6fAnatomical/Green (OpticalChannel) 
  Group /general/optophysiology/ImagingPlaneGCaMP6fAnatomical/device (Device) Bruker Ultima IV, Version 5.5.64.100
  Group /general/optophysiology/ImagingPlaneGCaMP6fFunctional (ImagingPlane) 
  Group /general/optophysiology/ImagingPlaneGCaMP6fFunctional/Green (OpticalChannel) 
  Group /general/optophysiology/ImagingPlaneGCaMP6fFunctional/device (Device) Bruker Ultima IV, Version 5.5.64.100
  Group /general/optophysiology/ImagingPlanetdTomatoAnatomical (ImagingPlane) 
  Group /general/optophysiology/ImagingPlanetdTomatoAnatomical/Red (OpticalChannel) 
  Group /general/optophysiology/ImagingPlanetdTomatoAnatomical/device (Device) Bruker Ultima IV, Version 5.5.64.100
  Group /general/optophysiology/ImagingPlanetdTomatoFunctional (ImagingPlane) 
  Group /general/optophysiology/ImagingPlanetdTomatoFunctional/Red (OpticalChannel) 
  Group /general/optophysiology/ImagingPlanetdTomatoFunctional/device (Device) Bruker Ultima IV, Version 5.5.64.100
  related_publications: ['https://doi.org/10.1101/2022.03.20.485047']
  session_id: 20200620122048
  Group /general/subject (Subject) 
  surgery: Each fly was anesthetized on a chilled Peltier plate with a thermally coupled custom holder. Each immobilized fly was carefully fitted into a custom mount consisting of 3D-printed plastic and a custom cut steel shim to tightly nestle the head and thorax. To fix the fly to the mount, UV-curable glue was placed and cured on the dorsal region of the face between the eyes, and on the thorax. A saline solution was added to the dish for dissection (103 mM NaCl, 3 mM KCl, 5 mM TES, 1 mM NaH2PO4, 4 mM MgCl2, 1.5 mM CaCl2, 10 mM trehalose, 10 mM glucose, 7 mM sucrose, and 26 mM NaHCO3). Using a tungsten needle the posterior head cuticle was carefully cut and removed to reveal the whole brain (Figure S1). Dissection forceps were used to remove fat and trachea.
  identifier: 50dd499d-f9bb-4581-ba3e-4cc198d24105
  Group /processing/behavior (ProcessingModule) No description.
  Group /processing/behavior/FicTrac (Position) 
  Group /processing/behavior/FicTrac/SpatialSeriesAnimalHeading (SpatialSeries) Animal's heading direction in radians from the lab's perspective.
  Group /processing/behavior/FicTrac/SpatialSeriesIntegratedMotion (SpatialSeries) Integrated x/y position of the sphere in laboratory coordinates, neglecting heading.
  Group /processing/behavior/FicTrac/SpatialSeriesMovementDirection (SpatialSeries) Instantaneous running direction of the animal in the lab coordinates. Direction inferred by the ball's rotation (roll and pitch)
  Group /processing/behavior/FicTrac/SpatialSeriesMovementSpeed (SpatialSeries) Instantaneous running speed of the animal in radians per frame.
  Group /processing/behavior/FicTrac/SpatialSeriesPosition (SpatialSeries) x and y positions in the lab frame in radians, inferred by integrating the rotation over time.
  Group /processing/behavior/FicTrac/SpatialSeriesRotationCameraFrame (SpatialSeries) Orientation in radians from the camera's perspective. x: rotation to the sphere's right (pitch), y: rotation under the sphere (yaw), z: rotation behind the sphere (roll)
  Group /processing/behavior/FicTrac/SpatialSeriesRotationDeltaCameraFrame (SpatialSeries) Change in orientation since last frame from the camera's perspective. x: rotation to the sphere's right (pitch), y: rotation under the sphere (yaw), z: rotation behind the sphere (roll)
  Group /processing/behavior/FicTrac/SpatialSeriesRotationDeltaError (SpatialSeries) Error in rotation delta in radians from the lab's perspective.
  Group /processing/behavior/FicTrac/SpatialSeriesRotationDeltaLabFrame (SpatialSeries) Change in orientation since last frame from the lab's perspective. x: rotation in front of subject (roll), y: rotation to subject's right (pitch), z: rotation under the subject (yaw)
  Group /processing/behavior/FicTrac/SpatialSeriesRotationLabFrame (SpatialSeries) Orientation in radians from the lab's perspective. x: rotation in front of subject (roll), y: rotation to subject's right (pitch), z: rotation under the subject (yaw)
  Group /processing/ophys (ProcessingModule) No description.
  Group /processing/ophys/TwoPhotonSeriesFunctionalGreenProcessed (TwoPhotonSeries) motion corrected high-pass temporal filtered z-scored and registered into a common space, the Functional Drosophila Atlas
  Group /processing/ophys/TwoPhotonSeriesFunctionalGreenProcessed/imaging_plane (ImagingPlane) 
  Group /processing/ophys/TwoPhotonSeriesFunctionalGreenProcessed/imaging_plane/Green (OpticalChannel) 
  Group /processing/ophys/TwoPhotonSeriesFunctionalGreenProcessed/imaging_plane/device (Device) Bruker Ultima IV, Version 5.5.64.100
  session_description: We use volumetric two-photon imaging to map neural activity associated with walking across the entire brain of Drosophila. We detect locomotor signals in approximately 40% of the brain, identify a global signal associated with the transition from rest to walking, and define clustered neural signals selectively associated with changes in forward or angular velocity.
  session_start_time: 2020-06-20T12:20:53.684457-07:00
  timestamps_reference_time: 2020-06-20T12:20:53.684457-07:00


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/TwoPhotonSeriesAnatomicalGreen (TwoPhotonSeries) Anatomical imaging data (GCaMP6f)
  Group /acquisition/TwoPhotonSeriesAnatomicalGreen/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeriesAnatomicalGreen/imaging_plane/Green (OpticalChannel) 
  Group /acquisition/TwoPhotonSeriesAnatomicalGreen/imaging_plane/device (Device) Bruker Ultima IV, Version 5.5.64.100
  Group /acquisition/TwoPhotonSeriesAnatomicalRed (TwoPhotonSeries) Anatomical imaging data (tdTomato)
  Group /acquisition/TwoPhotonSeriesAnatomicalRed/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeriesAnatomicalRed/imaging_plane/Red (OpticalChannel) 
  Group /acquisition/TwoPhotonSeriesAnatomicalRed/imaging_plane/device (Device) Bruker Ultima IV, Version 5.5.64.100
  Group /acquisition/TwoPhotonSeriesFunctionalGreen (TwoPhotonSeries) Functional imaging data (GCaMP6f)
  Group /acquisition/TwoPhotonSeriesFunctionalGreen/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeriesFunctionalGreen/imaging_plane/Green (OpticalChannel) 
  Group /acquisition/TwoPhotonSeriesFunctionalGreen/imaging_plane/device (Device) Bruker Ultima IV, Version 5.5.64.100
  Group /acquisition/TwoPhotonSeriesFunctionalRed (TwoPhotonSeries) Functional imaging data (tdTomato)
  Group /acquisition/TwoPhotonSeriesFunctionalRed/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeriesFunctionalRed/imaging_plane/Red (OpticalChannel) 
  Group /acquisition/TwoPhotonSeriesFunctionalRed/imaging_plane/device (Device) Bruker Ultima IV, Version 5.5.64.100
  Group /acquisition/Video: fictrac-20200627_113329-raw (ImageSeries) Video recorded by camera.
  file_create_date: ['2023-12-10T07:41:07.920260+01:00']
  Group /general/devices/BrukerFluorescenceMicroscope (Device) Bruker Ultima IV, Version 5.5.64.100
  Group /general/devices/Flea FL3-U3-13E4M-C (Device) Sensor used for imaging with FicTrac at 50 Hz with Edmund Optics 100 mm C Series Fixed Focal Length Lens
  experiment_description: We use volumetric two-photon imaging to map neural activity associated with walking across the entire brain of Drosophila. We detect locomotor signals in approximately 40% of the brain, identify a global signal associated with the transition from rest to walking, and define clustered neural signals selectively associated with changes in forward or angular velocity.
  experimenter: ['Brezovec, Luke' 'Berger, Andrew' 'Druckmann, Saul' 'Clandinin, Thomas']
  institution: Stanford
  keywords: ['walking' 'neural Correlates' 'brain-wide Scale' 'drosophila'
   'volumetric two-photon imaging' 'neural activity mapping'
   'locomotor signals']
  lab: Clandinin
  Group /general/optophysiology/ImagingPlaneFunctionalGreenProcessed (ImagingPlane) 
  Group /general/optophysiology/ImagingPlaneFunctionalGreenProcessed/Green (OpticalChannel) 
  Group /general/optophysiology/ImagingPlaneFunctionalGreenProcessed/device (Device) Bruker Ultima IV, Version 5.5.64.100
  Group /general/optophysiology/ImagingPlaneGCaMP6fAnatomical (ImagingPlane) 
  Group /general/optophysiology/ImagingPlaneGCaMP6fAnatomical/Green (OpticalChannel) 
  Group /general/optophysiology/ImagingPlaneGCaMP6fAnatomical/device (Device) Bruker Ultima IV, Version 5.5.64.100
  Group /general/optophysiology/ImagingPlaneGCaMP6fFunctional (ImagingPlane) 
  Group /general/optophysiology/ImagingPlaneGCaMP6fFunctional/Green (OpticalChannel) 
  Group /general/optophysiology/ImagingPlaneGCaMP6fFunctional/device (Device) Bruker Ultima IV, Version 5.5.64.100
  Group /general/optophysiology/ImagingPlanetdTomatoAnatomical (ImagingPlane) 
  Group /general/optophysiology/ImagingPlanetdTomatoAnatomical/Red (OpticalChannel) 
  Group /general/optophysiology/ImagingPlanetdTomatoAnatomical/device (Device) Bruker Ultima IV, Version 5.5.64.100
  Group /general/optophysiology/ImagingPlanetdTomatoFunctional (ImagingPlane) 
  Group /general/optophysiology/ImagingPlanetdTomatoFunctional/Red (OpticalChannel) 
  Group /general/optophysiology/ImagingPlanetdTomatoFunctional/device (Device) Bruker Ultima IV, Version 5.5.64.100
  related_publications: ['https://doi.org/10.1101/2022.03.20.485047']
  session_id: 20200627113329
  Group /general/subject (Subject) 
  surgery: Each fly was anesthetized on a chilled Peltier plate with a thermally coupled custom holder. Each immobilized fly was carefully fitted into a custom mount consisting of 3D-printed plastic and a custom cut steel shim to tightly nestle the head and thorax. To fix the fly to the mount, UV-curable glue was placed and cured on the dorsal region of the face between the eyes, and on the thorax. A saline solution was added to the dish for dissection (103 mM NaCl, 3 mM KCl, 5 mM TES, 1 mM NaH2PO4, 4 mM MgCl2, 1.5 mM CaCl2, 10 mM trehalose, 10 mM glucose, 7 mM sucrose, and 26 mM NaHCO3). Using a tungsten needle the posterior head cuticle was carefully cut and removed to reveal the whole brain (Figure S1). Dissection forceps were used to remove fat and trachea.
  identifier: 448c7f49-bd88-4c41-907c-538edd7ddee4
  Group /processing/behavior (ProcessingModule) No description.
  Group /processing/behavior/FicTrac (Position) 
  Group /processing/behavior/FicTrac/SpatialSeriesAnimalHeading (SpatialSeries) Animal's heading direction in radians from the lab's perspective.
  Group /processing/behavior/FicTrac/SpatialSeriesIntegratedMotion (SpatialSeries) Integrated x/y position of the sphere in laboratory coordinates, neglecting heading.
  Group /processing/behavior/FicTrac/SpatialSeriesMovementDirection (SpatialSeries) Instantaneous running direction of the animal in the lab coordinates. Direction inferred by the ball's rotation (roll and pitch)
  Group /processing/behavior/FicTrac/SpatialSeriesMovementSpeed (SpatialSeries) Instantaneous running speed of the animal in radians per frame.
  Group /processing/behavior/FicTrac/SpatialSeriesPosition (SpatialSeries) x and y positions in the lab frame in radians, inferred by integrating the rotation over time.
  Group /processing/behavior/FicTrac/SpatialSeriesRotationCameraFrame (SpatialSeries) Orientation in radians from the camera's perspective. x: rotation to the sphere's right (pitch), y: rotation under the sphere (yaw), z: rotation behind the sphere (roll)
  Group /processing/behavior/FicTrac/SpatialSeriesRotationDeltaCameraFrame (SpatialSeries) Change in orientation since last frame from the camera's perspective. x: rotation to the sphere's right (pitch), y: rotation under the sphere (yaw), z: rotation behind the sphere (roll)
  Group /processing/behavior/FicTrac/SpatialSeriesRotationDeltaError (SpatialSeries) Error in rotation delta in radians from the lab's perspective.
  Group /processing/behavior/FicTrac/SpatialSeriesRotationDeltaLabFrame (SpatialSeries) Change in orientation since last frame from the lab's perspective. x: rotation in front of subject (roll), y: rotation to subject's right (pitch), z: rotation under the subject (yaw)
  Group /processing/behavior/FicTrac/SpatialSeriesRotationLabFrame (SpatialSeries) Orientation in radians from the lab's perspective. x: rotation in front of subject (roll), y: rotation to subject's right (pitch), z: rotation under the subject (yaw)
  Group /processing/ophys (ProcessingModule) No description.
  Group /processing/ophys/TwoPhotonSeriesFunctionalGreenProcessed (TwoPhotonSeries) motion corrected high-pass temporal filtered z-scored and registered into a common space, the Functional Drosophila Atlas
  Group /processing/ophys/TwoPhotonSeriesFunctionalGreenProcessed/imaging_plane (ImagingPlane) 
  Group /processing/ophys/TwoPhotonSeriesFunctionalGreenProcessed/imaging_plane/Green (OpticalChannel) 
  Group /processing/ophys/TwoPhotonSeriesFunctionalGreenProcessed/imaging_plane/device (Device) Bruker Ultima IV, Version 5.5.64.100
  session_description: We use volumetric two-photon imaging to map neural activity associated with walking across the entire brain of Drosophila. We detect locomotor signals in approximately 40% of the brain, identify a global signal associated with the transition from rest to walking, and define clustered neural signals selectively associated with changes in forward or angular velocity.
  session_start_time: 2020-06-27T11:33:37.100887-07:00
  timestamps_reference_time: 2020-06-27T11:33:37.100887-07:00


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  Group /acquisition/TwoPhotonSeriesAnatomicalGreen (TwoPhotonSeries) Anatomical imaging data (GCaMP6f)
  Group /acquisition/TwoPhotonSeriesAnatomicalGreen/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeriesAnatomicalGreen/imaging_plane/Green (OpticalChannel) 
  Group /acquisition/TwoPhotonSeriesAnatomicalGreen/imaging_plane/device (Device) Bruker Ultima IV, Version 5.5.64.100
  Group /acquisition/TwoPhotonSeriesAnatomicalRed (TwoPhotonSeries) Anatomical imaging data (tdTomato)
  Group /acquisition/TwoPhotonSeriesAnatomicalRed/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeriesAnatomicalRed/imaging_plane/Red (OpticalChannel) 
  Group /acquisition/TwoPhotonSeriesAnatomicalRed/imaging_plane/device (Device) Bruker Ultima IV, Version 5.5.64.100
  Group /acquisition/TwoPhotonSeriesFunctionalGreen (TwoPhotonSeries) Functional imaging data (GCaMP6f)
  Group /acquisition/TwoPhotonSeriesFunctionalGreen/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeriesFunctionalGreen/imaging_plane/Green (OpticalChannel) 
  Group /acquisition/TwoPhotonSeriesFunctionalGreen/imaging_plane/device (Device) Bruker Ultima IV, Version 5.5.64.100
  Group /acquisition/TwoPhotonSeriesFunctionalRed (TwoPhotonSeries) Functional imaging data (tdTomato)
  Group /acquisition/TwoPhotonSeriesFunctionalRed/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeriesFunctionalRed/imaging_plane/Red (OpticalChannel) 
  Group /acquisition/TwoPhotonSeriesFunctionalRed/imaging_plane/device (Device) Bruker Ultima IV, Version 5.5.64.100
  Group /acquisition/Video: fictrac-20200627_130208-raw (ImageSeries) Video recorded by camera.
  file_create_date: ['2023-12-10T09:34:05.642255+01:00']
  Group /general/devices/BrukerFluorescenceMicroscope (Device) Bruker Ultima IV, Version 5.5.64.100
  Group /general/devices/Flea FL3-U3-13E4M-C (Device) Sensor used for imaging with FicTrac at 50 Hz with Edmund Optics 100 mm C Series Fixed Focal Length Lens
  experiment_description: We use volumetric two-photon imaging to map neural activity associated with walking across the entire brain of Drosophila. We detect locomotor signals in approximately 40% of the brain, identify a global signal associated with the transition from rest to walking, and define clustered neural signals selectively associated with changes in forward or angular velocity.
  experimenter: ['Brezovec, Luke' 'Berger, Andrew' 'Druckmann, Saul' 'Clandinin, Thomas']
  institution: Stanford
  keywords: ['walking' 'neural Correlates' 'brain-wide Scale' 'drosophila'
   'volumetric two-photon imaging' 'neural activity mapping'
   'locomotor signals']
  lab: Clandinin
  Group /general/optophysiology/ImagingPlaneFunctionalGreenProcessed (ImagingPlane) 
  Group /general/optophysiology/ImagingPlaneFunctionalGreenProcessed/Green (OpticalChannel) 
  Group /general/optophysiology/ImagingPlaneFunctionalGreenProcessed/device (Device) Bruker Ultima IV, Version 5.5.64.100
  Group /general/optophysiology/ImagingPlaneGCaMP6fAnatomical (ImagingPlane) 
  Group /general/optophysiology/ImagingPlaneGCaMP6fAnatomical/Green (OpticalChannel) 
  Group /general/optophysiology/ImagingPlaneGCaMP6fAnatomical/device (Device) Bruker Ultima IV, Version 5.5.64.100
  Group /general/optophysiology/ImagingPlaneGCaMP6fFunctional (ImagingPlane) 
  Group /general/optophysiology/ImagingPlaneGCaMP6fFunctional/Green (OpticalChannel) 
  Group /general/optophysiology/ImagingPlaneGCaMP6fFunctional/device (Device) Bruker Ultima IV, Version 5.5.64.100
  Group /general/optophysiology/ImagingPlanetdTomatoAnatomical (ImagingPlane) 
  Group /general/optophysiology/ImagingPlanetdTomatoAnatomical/Red (OpticalChannel) 
  Group /general/optophysiology/ImagingPlanetdTomatoAnatomical/device (Device) Bruker Ultima IV, Version 5.5.64.100
  Group /general/optophysiology/ImagingPlanetdTomatoFunctional (ImagingPlane) 
  Group /general/optophysiology/ImagingPlanetdTomatoFunctional/Red (OpticalChannel) 
  Group /general/optophysiology/ImagingPlanetdTomatoFunctional/device (Device) Bruker Ultima IV, Version 5.5.64.100
  related_publications: ['https://doi.org/10.1101/2022.03.20.485047']
  session_id: 20200627130208
  Group /general/subject (Subject) 
  surgery: Each fly was anesthetized on a chilled Peltier plate with a thermally coupled custom holder. Each immobilized fly was carefully fitted into a custom mount consisting of 3D-printed plastic and a custom cut steel shim to tightly nestle the head and thorax. To fix the fly to the mount, UV-curable glue was placed and cured on the dorsal region of the face between the eyes, and on the thorax. A saline solution was added to the dish for dissection (103 mM NaCl, 3 mM KCl, 5 mM TES, 1 mM NaH2PO4, 4 mM MgCl2, 1.5 mM CaCl2, 10 mM trehalose, 10 mM glucose, 7 mM sucrose, and 26 mM NaHCO3). Using a tungsten needle the posterior head cuticle was carefully cut and removed to reveal the whole brain (Figure S1). Dissection forceps were used to remove fat and trachea.
  identifier: c93466b0-17dd-4aee-bfe0-2d501a46ec5e
  Group /processing/behavior (ProcessingModule) No description.
  Group /processing/behavior/FicTrac (Position) 
  Group /processing/behavior/FicTrac/SpatialSeriesAnimalHeading (SpatialSeries) Animal's heading direction in radians from the lab's perspective.
  Group /processing/behavior/FicTrac/SpatialSeriesIntegratedMotion (SpatialSeries) Integrated x/y position of the sphere in laboratory coordinates, neglecting heading.
  Group /processing/behavior/FicTrac/SpatialSeriesMovementDirection (SpatialSeries) Instantaneous running direction of the animal in the lab coordinates. Direction inferred by the ball's rotation (roll and pitch)
  Group /processing/behavior/FicTrac/SpatialSeriesMovementSpeed (SpatialSeries) Instantaneous running speed of the animal in radians per frame.
  Group /processing/behavior/FicTrac/SpatialSeriesPosition (SpatialSeries) x and y positions in the lab frame in radians, inferred by integrating the rotation over time.
  Group /processing/behavior/FicTrac/SpatialSeriesRotationCameraFrame (SpatialSeries) Orientation in radians from the camera's perspective. x: rotation to the sphere's right (pitch), y: rotation under the sphere (yaw), z: rotation behind the sphere (roll)
  Group /processing/behavior/FicTrac/SpatialSeriesRotationDeltaCameraFrame (SpatialSeries) Change in orientation since last frame from the camera's perspective. x: rotation to the sphere's right (pitch), y: rotation under the sphere (yaw), z: rotation behind the sphere (roll)
  Group /processing/behavior/FicTrac/SpatialSeriesRotationDeltaError (SpatialSeries) Error in rotation delta in radians from the lab's perspective.
  Group /processing/behavior/FicTrac/SpatialSeriesRotationDeltaLabFrame (SpatialSeries) Change in orientation since last frame from the lab's perspective. x: rotation in front of subject (roll), y: rotation to subject's right (pitch), z: rotation under the subject (yaw)
  Group /processing/behavior/FicTrac/SpatialSeriesRotationLabFrame (SpatialSeries) Orientation in radians from the lab's perspective. x: rotation in front of subject (roll), y: rotation to subject's right (pitch), z: rotation under the subject (yaw)
  Group /processing/ophys (ProcessingModule) No description.
  Group /processing/ophys/TwoPhotonSeriesFunctionalGreenProcessed (TwoPhotonSeries) motion corrected high-pass temporal filtered z-scored and registered into a common space, the Functional Drosophila Atlas
  Group /processing/ophys/TwoPhotonSeriesFunctionalGreenProcessed/imaging_plane (ImagingPlane) 
  Group /processing/ophys/TwoPhotonSeriesFunctionalGreenProcessed/imaging_plane/Green (OpticalChannel) 
  Group /processing/ophys/TwoPhotonSeriesFunctionalGreenProcessed/imaging_plane/device (Device) Bruker Ultima IV, Version 5.5.64.100
  session_description: We use volumetric two-photon imaging to map neural activity associated with walking across the entire brain of Drosophila. We detect locomotor signals in approximately 40% of the brain, identify a global signal associated with the transition from rest to walking, and define clustered neural signals selectively associated with changes in forward or angular velocity.
  session_start_time: 2020-06-27T13:02:18.301376-07:00
  timestamps_reference_time: 2020-06-27T13:02:18.301376-07:00
