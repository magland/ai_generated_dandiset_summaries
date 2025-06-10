
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001424/draft
name: Predictive Processing Community - SLAP2
contributor: [{'name': 'Lecoq, Jerome', 'email': 'jeromel@alleninstitute.org', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}]
description: This dataset contains data acquired on the SLAP2 platform as part of the OpenScope predictive processing community project
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 4914839332, 'numberOfFiles': 2, 'numberOfSubjects': 1, 'variableMeasured': ['OpticalChannel', 'PlaneSegmentation', 'ImagingPlane', 'ProcessingModule'], 'measurementTechnique': [{'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 001424 has 3 NWB files.
3 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/DMD1_activity_image (ImageSeries) Activity image (standard deviation projection) for DMD1
  Group /acquisition/DMD1_mean_image (ImageSeries) Mean fluorescence image for DMD1
  Group /acquisition/DMD2_activity_image (ImageSeries) Activity image (standard deviation projection) for DMD2
  Group /acquisition/DMD2_mean_image (ImageSeries) Mean fluorescence image for DMD2
  file_create_date: ['2025-06-05T20:14:46.655789+00:00']
  Group /general/devices/SLAP2 (Device) SLAP2 (Swept, Confocally-Aligned Planar Excitation) microscope
  experimenter: ['Seyedolmohadesin' 'rcpeene' 'jeromelecoq' 'KasparP']
  institution: Allen Institute
  lab: unknown
  notes: SLAP2 glutamate imaging experiment with drifting gratings
  Group /general/optophysiology/iGluSnFR4_DMD1 (ImagingPlane) 
  Group /general/optophysiology/iGluSnFR4_DMD1/device (Device) SLAP2 (Swept, Confocally-Aligned Planar Excitation) microscope
  Group /general/optophysiology/iGluSnFR4_DMD1/iGluSnFR4 (OpticalChannel) 
  Group /general/optophysiology/iGluSnFR4_DMD2 (ImagingPlane) 
  Group /general/optophysiology/iGluSnFR4_DMD2/device (Device) SLAP2 (Swept, Confocally-Aligned Planar Excitation) microscope
  Group /general/optophysiology/iGluSnFR4_DMD2/iGluSnFR4 (OpticalChannel) 
  Group /general/subject (Subject) 
  identifier: SLAP2-794237-20250605201446
  Group /intervals/stimulus_presentations (TimeIntervals) Visual stimulus presentations
  Dataset /intervals/stimulus_presentations/contrast (VectorData) Contrast of the grating | shape = (2130,) | dtype = float64
  Dataset /intervals/stimulus_presentations/delay (VectorData) Delay in seconds | shape = (2130,) | dtype = float64
  Dataset /intervals/stimulus_presentations/diameter (VectorData) Diameter of the grating in degrees | shape = (2130,) | dtype = float64
  Dataset /intervals/stimulus_presentations/id (ElementIdentifiers)  | shape = (2130,) | dtype = int64
  Dataset /intervals/stimulus_presentations/orientation (VectorData) Orientation of drifting grating in degrees | shape = (2130,) | dtype = float64
  Dataset /intervals/stimulus_presentations/spatial_frequency (VectorData) Spatial frequency of the grating in cycles/degree | shape = (2130,) | dtype = float64
  Dataset /intervals/stimulus_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (2130,) | dtype = float64
  Dataset /intervals/stimulus_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (2130,) | dtype = float64
  Dataset /intervals/stimulus_presentations/temporal_frequency (VectorData) Temporal frequency of the grating in Hz | shape = (2130,) | dtype = float64
  Dataset /intervals/stimulus_presentations/trial (VectorData) Trial number | shape = (2130,) | dtype = float64
  Dataset /intervals/stimulus_presentations/x_position (VectorData) X position of the grating | shape = (2130,) | dtype = float64
  Dataset /intervals/stimulus_presentations/y_position (VectorData) Y position of the grating | shape = (2130,) | dtype = float64
  Group /processing/ophys (ProcessingModule) Contains optical physiology processed data
  Group /processing/ophys/DMD1_f0 (RoiResponseSeries) no description
  Dataset /processing/ophys/DMD1_f0/rois (DynamicTableRegion) All ROIs for DMD1 | shape = (171,) | dtype = int64
  Group /processing/ophys/DMD2_f0 (RoiResponseSeries) no description
  Dataset /processing/ophys/DMD2_f0/rois (DynamicTableRegion) All ROIs for DMD2 | shape = (52,) | dtype = int64
  Group /processing/ophys/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/ImageSegmentation/DMD1_plane_segmentation (PlaneSegmentation) ROIs for DMD1
  Dataset /processing/ophys/ImageSegmentation/DMD1_plane_segmentation/id (ElementIdentifiers)  | shape = (171,) | dtype = int64
  Dataset /processing/ophys/ImageSegmentation/DMD1_plane_segmentation/image_mask (VectorData) Image masks for each ROI | shape = (171, 514, 878) | dtype = float32
  Group /processing/ophys/ImageSegmentation/DMD1_plane_segmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/DMD1_plane_segmentation/imaging_plane/device (Device) SLAP2 (Swept, Confocally-Aligned Planar Excitation) microscope
  Group /processing/ophys/ImageSegmentation/DMD1_plane_segmentation/imaging_plane/iGluSnFR4 (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/DMD2_plane_segmentation (PlaneSegmentation) ROIs for DMD2
  Dataset /processing/ophys/ImageSegmentation/DMD2_plane_segmentation/id (ElementIdentifiers)  | shape = (52,) | dtype = int64
  Dataset /processing/ophys/ImageSegmentation/DMD2_plane_segmentation/image_mask (VectorData) Image masks for each ROI | shape = (52, 442, 327) | dtype = float32
  Group /processing/ophys/ImageSegmentation/DMD2_plane_segmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/DMD2_plane_segmentation/imaging_plane/device (Device) SLAP2 (Swept, Confocally-Aligned Planar Excitation) microscope
  Group /processing/ophys/ImageSegmentation/DMD2_plane_segmentation/imaging_plane/iGluSnFR4 (OpticalChannel) 
  Group /processing/ophys/df (Fluorescence) 
  Group /processing/ophys/df/DMD1_df (RoiResponseSeries) no description
  Dataset /processing/ophys/df/DMD1_df/rois (DynamicTableRegion) All ROIs for DMD1 | shape = (171,) | dtype = int64
  Group /processing/ophys/df/DMD2_df (RoiResponseSeries) no description
  Dataset /processing/ophys/df/DMD2_df/rois (DynamicTableRegion) All ROIs for DMD2 | shape = (52,) | dtype = int64
  Group /processing/ophys/dff (DfOverF) 
  Group /processing/ophys/dff/DMD1_dff (RoiResponseSeries) no description
  Dataset /processing/ophys/dff/DMD1_dff/rois (DynamicTableRegion) All ROIs for DMD1 | shape = (171,) | dtype = int64
  Group /processing/ophys/dff/DMD2_dff (RoiResponseSeries) no description
  Dataset /processing/ophys/dff/DMD2_dff/rois (DynamicTableRegion) All ROIs for DMD2 | shape = (52,) | dtype = int64
  session_description: Glutamate imaging with iGluSnFR4
  session_start_time: 2025-04-03T10:38:30+00:00
  timestamps_reference_time: 2025-04-03T10:38:30+00:00
