
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000246/draft
name: developing CaMPARI3
contributor: [{'name': 'Icardi, Jacob', 'email': 'icardij@ccf.org', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}]
description: This dataset contains in vivo and in vitro data for the development of CaMPARI3.
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 2134855240972, 'numberOfFiles': 1027, 'numberOfSubjects': 146, 'variableMeasured': ['OpticalChannel', 'TwoPhotonSeries', 'PlaneSegmentation', 'ProcessingModule', 'ImagingPlane'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'two-photon microscopy technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000246 has 100 NWB files.
44 of these NWB files are of type 1.
56 of these NWB files are of type 2.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/in vitro screening data (TimeSeries) screening results of purified protein, ordered as (1) delta f/f, mean, (2) delta f/f, STDEV, (3) F, mean, (4) F, STDEV, (5) delta R/R, mean, (6) delta R/R, STDEV
  file_create_date: ['2024-02-13T12:14:39.942643-05:00']
  experimenter: ['Campbell, Robert']
  session_id: fluorescence_recording
  Group /general/subject (Subject) 
  identifier: CaMPARI1-A146L-C150T-C202A
  session_description: in vitro flourescence of purified protein
  session_start_time: 2023-01-01T00:00:00-05:00
  timestamps_reference_time: 2023-01-01T00:00:00-05:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/TwoPhotonSeries (TwoPhotonSeries) Frames*Depth*Channel
  Group /acquisition/TwoPhotonSeries/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeries/imaging_plane/device (Device) 
  Group /acquisition/TwoPhotonSeries/imaging_plane/optical_channel (OpticalChannel) 
  file_create_date: ['2022-10-25T15:53:15.246000-04:00']
  Group /general/devices/Device (Device) 
  experimenter: ['Dan Margevicius' '']
  institution: Lerner Research Institute
  Group /general/optophysiology/imaging_plane (ImagingPlane) 
  Group /general/optophysiology/imaging_plane/device (Device) 
  Group /general/optophysiology/imaging_plane/optical_channel (OpticalChannel) 
  Group /general/subject (Subject) 
  identifier: Ser5-synapsin DC1-5L_C2-5R-1 left FOV1_postPC100%1_lambda1040_um200_x2_pwr100
  Group /processing/ophys (ProcessingModule) contains optical physiology data
  Group /processing/ophys/Fluorescence (Fluorescence) 
  Group /processing/ophys/Fluorescence/RoiResponseSeries (RoiResponseSeries) red to green ratio from same cell
  Dataset /processing/ophys/Fluorescence/RoiResponseSeries/rois (DynamicTableRegion) all ROIs | shape = (63,) | dtype = int8
  Group /processing/ophys/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation (PlaneSegmentation) Cells segmented from visual cortex, n_rois*x*y
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/id (ElementIdentifiers)  | shape = (1024,) | dtype = int64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/image_mask (VectorData) image masks | shape = (1024, 1024, 63) | dtype = float64
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/device (Device) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/optical_channel (OpticalChannel) 
  session_description: in vivo Mouse Brain Imaging and Photoconversion
  session_start_time: 2022-04-05T00:00:00.000000-04:00
  timestamps_reference_time: 2022-04-05T00:00:00.000000-04:00
