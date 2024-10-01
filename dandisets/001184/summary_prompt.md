
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001184/0.240829.1458
name: Brain-wide microstrokes affect the stability of memory circuits in the hippocampus
contributor: [{'name': 'Heiser, Hendrik', 'email': 'hendrik-heiser@gmx.de', 'roleName': ['dcite:Author', 'dcite:DataCollector', 'dcite:DataCurator', 'dcite:DataManager', 'dcite:FormalAnalysis', 'dcite:Researcher', 'dcite:Validation'], 'schemaKey': 'Person', 'identifier': '0000-0003-1725-5571', 'affiliation': [], 'includeInCitation': True}, {'name': 'Wahl, Anna-Sophia', 'email': 'annasophia.wahl@med.uni-muenchen.de', 'roleName': ['dcite:Author', 'dcite:Conceptualization', 'dcite:FundingAcquisition', 'dcite:Investigation', 'dcite:ProjectLeader', 'dcite:Supervision', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0001-9498-4263', 'includeInCitation': True}]
description: Data for the publication "Brain-wide microstrokes affect the stability of memory circuits in the hippocampus".
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}, {'name': 'behavioral approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 130937573056, 'numberOfFiles': 309, 'numberOfSubjects': 21, 'variableMeasured': ['Position', 'OpticalChannel', 'ImagingPlane', 'SpatialSeries', 'BehavioralEvents', 'BehavioralEpochs', 'BehavioralTimeSeries', 'PlaneSegmentation', 'TwoPhotonSeries', 'ProcessingModule'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'two-photon microscopy technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 001184 has 100 NWB files.
100 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/TwoPhotonSeries (TwoPhotonSeries) Metadata for two-photon recording
  Group /acquisition/TwoPhotonSeries/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeries/imaging_plane/GCaMP6f (OpticalChannel) 
  Group /acquisition/TwoPhotonSeries/imaging_plane/device (Device) Scientifica Hyperscope
  file_create_date: ['2024-08-27T16:12:29.947773+02:00']
  Group /general/devices/Microscope (Device) Scientifica Hyperscope
  experiment_description: Chronic two-photon calcium imaging of hippocampal CA1 networks during a VR-based spatial navigation task, before and after microstrokes. Behavioral parameters recorded are running speed, VR position and licking (tongue touches to the water spout).
  experimenter: ['Heiser, Hendrik']
  institution: Brain Research Institute, University of Zurich
  keywords: ['two-photon calcium imaging' 'virtual reality' 'spatial navigation'
   'hippocampus' 'CA1' 'stroke' 'microlesions' 'microspheres'
   'chronic recording']
  lab: Wahl Lab
  Group /general/optophysiology/CA1 (ImagingPlane) 
  Group /general/optophysiology/CA1/GCaMP6f (OpticalChannel) 
  Group /general/optophysiology/CA1/device (Device) Scientifica Hyperscope
  session_id: session_hheise_M108_2022-08-08_01
  Group /general/subject (Subject) 
  identifier: b0868d59-81a0-4d85-9408-7ead4e368120
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/blr_perf (VectorData) Performance measured as Binned Lick Ratio (ratio of individual licks within vs. outside of reward zones). Computed per trial. Not used in paper. | shape = (8,) | dtype = float32
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (8,) | dtype = int32
  Dataset /intervals/trials/si_perf (VectorData) Performance measured as Spatial Information contained in lick histogram. Computed per sessionfrom trial-averaged lick histogram. Used in paper. | shape = (8,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (8,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (8,) | dtype = float64
  Group /processing/behavior (ProcessingModule) Processed behavioral data
  Group /processing/behavior/BehavioralEpochs (BehavioralEpochs) 
  Group /processing/behavior/BehavioralEpochs/licking (IntervalSeries) Intervals when the animal was licking (tongue touches the water spout).
  Group /processing/behavior/BehavioralEpochs/reward_zones (IntervalSeries) Intervals when the animal was inside a reward zone.
  Group /processing/behavior/BehavioralEpochs/running (IntervalSeries) Intervals when the animal was running (speed > 5 cm/s).
  Group /processing/behavior/BehavioralEvents (BehavioralEvents) 
  Group /processing/behavior/BehavioralEvents/valve_openings (TimeSeries) The duration of open water valve as a water reward.
  Group /processing/behavior/BehavioralTimeSeries (BehavioralTimeSeries) 
  Group /processing/behavior/BehavioralTimeSeries/speed (TimeSeries) The speed of the animal measured over time.
  Group /processing/behavior/Position (Position) 
  Group /processing/behavior/Position/SpatialSeries (SpatialSeries) Position of the mouse inside the linear VR corridor.
  Group /processing/ophys (ProcessingModule) motion-corrected, segmented and detrended two-photon data
  Group /processing/ophys/DfOverF (DfOverF) 
  Group /processing/ophys/DfOverF/RoiResponseSeries (RoiResponseSeries) dF/F responses for all ROIs
  Dataset /processing/ophys/DfOverF/RoiResponseSeries/rois (DynamicTableRegion) All accepted ROIs | shape = (941,) | dtype = int32
  Group /processing/ophys/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation (PlaneSegmentation) CaImAn Segmentation result
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/id (ElementIdentifiers)  | shape = (941,) | dtype = int32
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (941, 488, 488) | dtype = float16
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/GCaMP6f (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/device (Device) Scientifica Hyperscope
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/reference_images/LocalCorrelationImage (ImageSeries) Local correlation image of motion-corrected session acquisition. Highlights functional units (putative ROIs) in the field of view.
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/reference_images/LocalCorrelationImage/device (Device) Scientifica Hyperscope
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/reference_images/MeanIntensityImage (ImageSeries) Mean intensity projection of motion-corrected session acquisition. Highlights anatomical structure of the field of view.
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/reference_images/MeanIntensityImage/device (Device) Scientifica Hyperscope
  session_description: {'Mouse': 108, 'Date': datetime.date(2022, 8, 8), 'Phase': 'healthy', 'Days after microsphere injection': -4}
  session_start_time: 2022-08-08T16:31:18.080000+02:00
  timestamps_reference_time: 2022-08-08T16:31:18.080000+02:00
