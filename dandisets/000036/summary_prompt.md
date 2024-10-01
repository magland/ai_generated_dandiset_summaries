
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000036/0.230515.1917
name: Allen Institute Openscope - Measuring Stimulus-Evoked Neurophysiological Differentiation in Distinct Populations of Neurons in Mouse Visual Cortex
contributor: [{'url': 'https://alleninstitute.org/person/jerome-lecoq/', 'name': 'Lecoq, Jerome', 'email': 'jeromel@alleninstitute.org', 'roleName': ['dcite:Author', 'dcite:DataCollector', 'dcite:DataCurator', 'dcite:DataManager', 'dcite:FundingAcquisition', 'dcite:Methodology', 'dcite:ProjectAdministration', 'dcite:Supervision', 'dcite:Validation', 'dcite:ContactPerson', 'dcite:Producer'], 'schemaKey': 'Person', 'identifier': '0000-0002-0131-0938', 'affiliation': [], 'includeInCitation': True}, {'url': 'http://willmayner.com', 'name': 'Mayner, Will', 'email': 'wmayner@gmail.com', 'roleName': ['dcite:Author', 'dcite:Conceptualization', 'dcite:ContactPerson', 'dcite:FormalAnalysis', 'dcite:Investigation', 'dcite:Methodology', 'dcite:ProjectLeader', 'dcite:Researcher', 'dcite:Software'], 'schemaKey': 'Person', 'identifier': '0000-0002-9737-6260', 'affiliation': [], 'includeInCitation': True}]
description: Despite significant progress in understanding neural coding, it remains unclear how the coordinated activity of large populations of neurons relates to what an observer actually perceives. Since neurophysiological differences must underlie differences among percepts, differentiation analysis-quantifying distinct patterns of neurophysiological activity-has been proposed as an "inside-out" approach that addresses this question. This methodology contrasts with "outside-in" approaches such as feature tuning and decoding analyses, which are defined in terms of extrinsic experimental variables. Here, we used two-photon calcium imaging in mice of both sexes to systematically survey stimulus-evoked neurophysiological differentiation (ND) in excitatory neuronal populations in layers (L)2/3, L4, and L5 across five visual cortical areas (primary, lateromedial, anterolateral, posteromedial, and anteromedial) in response to naturalistic and phase-scrambled movie stimuli. We find that unscrambled stimuli evoke greater ND than scrambled stimuli specifically in L2/3 of the anterolateral and anteromedial areas, and that this effect is modulated by arousal state and locomotion. By contrast, decoding performance was far above chance and did not vary substantially across areas and layers. Differentiation also differed within the unscrambled stimulus set, suggesting that differentiation analysis may be used to probe the ethological relevance of individual stimuli.

For more details, consult the associated publication : https://doi.org/10.1523/eneuro.0280-21.2021
assetsSummary: {'species': [], 'approach': [{'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}, {'name': 'behavioral approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 79771339536, 'numberOfFiles': 57, 'numberOfSubjects': 9, 'variableMeasured': ['BehavioralTimeSeries', 'PlaneSegmentation'], 'measurementTechnique': [{'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000036 has 57 NWB files.
57 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2020-08-18T19:12:14.330018-07:00']
  Group /general/devices/2p_microscope (Device) Allen Institute two-photon pipeline: CAM2P.1
  Group /general/optophysiology/imaging_plane_1 (ImagingPlane) 
  Group /general/optophysiology/imaging_plane_1/device (Device) Allen Institute two-photon pipeline: CAM2P.1
  Group /general/optophysiology/imaging_plane_1/optical_channel (OpticalChannel) 
  Group /general/subject (Subject) 
  identifier: 717007376
  Group /processing/behavior (ProcessingModule) preprocessed behavioral data
  Group /processing/behavior/BehavioralTimeSeries (BehavioralTimeSeries) 
  Group /processing/behavior/BehavioralTimeSeries/running_velocity (TimeSeries) Velocity of the mouse on a rotating wheel
  Group /processing/ophys (ProcessingModule) OpenScope processing pipeline
  Group /processing/ophys/DfOverF (DfOverF) 
  Group /processing/ophys/DfOverF/imaging_plane_1 (RoiResponseSeries) no description
  Dataset /processing/ophys/DfOverF/imaging_plane_1/rois (DynamicTableRegion) segmented cells with cell_specimen_ids | shape = (41,) | dtype = int32
  Group /processing/ophys/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation (PlaneSegmentation) Segmentation for imaging plane (de Vries et al., 2019, Nat Neurosci)
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/id (ElementIdentifiers)  | shape = (41,) | dtype = int32
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (41, 512, 512) | dtype = uint8
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/device (Device) Allen Institute two-photon pipeline: CAM2P.1
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/optical_channel (OpticalChannel) 
  session_description: Allen Institute OpenScope dataset
  session_start_time: 2018-07-05T15:29:08.784000-07:00
  Group /stimulus/presentation/conspecifics (IndexSeries) no description
  Group /stimulus/presentation/conspecifics/indexed_timeseries (ImageSeries) no description
  Group /stimulus/presentation/crickets (IndexSeries) no description
  Group /stimulus/presentation/crickets/indexed_timeseries (ImageSeries) no description
  Group /stimulus/presentation/dots (IndexSeries) no description
  Group /stimulus/presentation/dots/indexed_timeseries (ImageSeries) no description
  Group /stimulus/presentation/human_montage (IndexSeries) no description
  Group /stimulus/presentation/human_montage/indexed_timeseries (ImageSeries) no description
  Group /stimulus/presentation/man_writing (IndexSeries) no description
  Group /stimulus/presentation/man_writing/indexed_timeseries (ImageSeries) no description
  Group /stimulus/presentation/mouse_montage_1 (IndexSeries) no description
  Group /stimulus/presentation/mouse_montage_1/indexed_timeseries (ImageSeries) no description
  Group /stimulus/presentation/mouse_montage_1_spatial_phase_scramble (IndexSeries) no description
  Group /stimulus/presentation/mouse_montage_1_spatial_phase_scramble/indexed_timeseries (ImageSeries) no description
  Group /stimulus/presentation/mouse_montage_1_temporal_phase_scramble (IndexSeries) no description
  Group /stimulus/presentation/mouse_montage_1_temporal_phase_scramble/indexed_timeseries (ImageSeries) no description
  Group /stimulus/presentation/mouse_montage_2 (IndexSeries) no description
  Group /stimulus/presentation/mouse_montage_2/indexed_timeseries (ImageSeries) no description
  Group /stimulus/presentation/mousecam (IndexSeries) no description
  Group /stimulus/presentation/mousecam/indexed_timeseries (ImageSeries) no description
  Group /stimulus/presentation/mousecam_spatial_phase_scramble (IndexSeries) no description
  Group /stimulus/presentation/mousecam_spatial_phase_scramble/indexed_timeseries (ImageSeries) no description
  Group /stimulus/presentation/noise (IndexSeries) no description
  Group /stimulus/presentation/noise/indexed_timeseries (ImageSeries) no description
  Group /stimulus/presentation/snake (IndexSeries) no description
  Group /stimulus/presentation/snake/indexed_timeseries (ImageSeries) no description
  Group /stimulus/presentation/spontaneous (IndexSeries) no description
  Group /stimulus/presentation/spontaneous/indexed_timeseries (ImageSeries) no description
  Group /stimulus/templates/conspecifics (ImageSeries) no description
  Group /stimulus/templates/crickets (ImageSeries) no description
  Group /stimulus/templates/dots (ImageSeries) no description
  Group /stimulus/templates/human_montage (ImageSeries) no description
  Group /stimulus/templates/man_writing (ImageSeries) no description
  Group /stimulus/templates/mouse_montage_1 (ImageSeries) no description
  Group /stimulus/templates/mouse_montage_1_spatial_phase_scramble (ImageSeries) no description
  Group /stimulus/templates/mouse_montage_1_temporal_phase_scramble (ImageSeries) no description
  Group /stimulus/templates/mouse_montage_2 (ImageSeries) no description
  Group /stimulus/templates/mousecam (ImageSeries) no description
  Group /stimulus/templates/mousecam_spatial_phase_scramble (ImageSeries) no description
  Group /stimulus/templates/noise (ImageSeries) no description
  Group /stimulus/templates/snake (ImageSeries) no description
  Group /stimulus/templates/spontaneous (ImageSeries) no description
  timestamps_reference_time: 2018-07-05T15:29:08.784000-07:00
