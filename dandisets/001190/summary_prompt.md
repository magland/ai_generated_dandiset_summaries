
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001190/draft
name: In vivo Calcium Imaging: Genotype Data: NOR
contributor: [{'name': 'Fitting, Sylvia ', 'email': 'sfitting@email.unc.edu', 'roleName': ['dcite:ContactPerson', 'dcite:Conceptualization', 'dcite:FundingAcquisition', 'dcite:Author', 'dcite:Investigation', 'dcite:ProjectLeader', 'dcite:Sponsor'], 'schemaKey': 'Person', 'affiliation': [{'name': 'University of North Carolina at Chapel Hill', 'schemaKey': 'Affiliation'}], 'includeInCitation': True}, {'name': 'Yadav-Samudrala, Barkha', 'email': 'yadavb@email.unc.edu', 'roleName': ['dcite:Conceptualization', 'dcite:ContactPerson', 'dcite:DataCollector', 'dcite:DataCurator', 'dcite:DataManager', 'dcite:FormalAnalysis', 'dcite:Investigation', 'dcite:Methodology', 'dcite:Producer', 'dcite:ProjectLeader', 'dcite:ProjectManager', 'dcite:ProjectMember', 'dcite:ProjectAdministration', 'dcite:Researcher', 'dcite:Validation', 'dcite:Visualization'], 'schemaKey': 'Person', 'identifier': '0000-0002-2967-2017', 'includeInCitation': True}]
description: Data set for Tat(-) and Tat(+) male mice comparing genotype differences without any drug treatment
Researcher: Barkha J. Yadav Samudrala and Sylvia Fitting
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 220201651439, 'numberOfFiles': 16, 'numberOfSubjects': 8, 'variableMeasured': ['PlaneSegmentation', 'ImagingPlane', 'ProcessingModule', 'OpticalChannel'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 001190 has 8 NWB files.
8 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ImageSeries (ImageSeries) Behavior camera imaging data
  Group /acquisition/ImageSeries/device (Device) 
  Group /acquisition/OnePhotonSeries (OnePhotonSeries) Miniscope imaging data
  Group /acquisition/OnePhotonSeries/imaging_plane (ImagingPlane) 
  Group /acquisition/OnePhotonSeries/imaging_plane/OpticalChannel (OpticalChannel) 
  Group /acquisition/OnePhotonSeries/imaging_plane/device (Device) NVista3
  file_create_date: ['2024-09-23T16:12:10.738872+00:00']
  Group /general/devices/BehaviorCamera (Device) 
  Group /general/devices/Miniscope (Device) NVista3
  Group /general/optophysiology/ImagingPlane (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane/OpticalChannel (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane/device (Device) NVista3
  Group /general/subject (Subject) 
  identifier: 1eb3131c-c663-4814-8c7b-b980f769940c
  Group /processing/ophys (ProcessingModule) Optical physiology data obtained by processing raw calcium imaging data
  Group /processing/ophys/EventAmplitude (RoiResponseSeries) Amplitude of neural events associated with spatial footprints
  Dataset /processing/ophys/EventAmplitude/rois (DynamicTableRegion) ROIs | shape = (55,) | dtype = int64
  Group /processing/ophys/Fluorescence (Fluorescence) 
  Group /processing/ophys/Fluorescence/RoiResponseSeries (RoiResponseSeries) Fluorescence data associated with spatial footprints
  Dataset /processing/ophys/Fluorescence/RoiResponseSeries/rois (DynamicTableRegion) ROIs | shape = (55,) | dtype = int64
  Group /processing/ophys/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation (PlaneSegmentation) Footprints of individual cells obtained by segmenting the field of view
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/id (ElementIdentifiers)  | shape = (55,) | dtype = int64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (55, 638, 396) | dtype = float32
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/OpticalChannel (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/device (Device) NVista3
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/reference_images/OnePhotonSeries (OnePhotonSeries) Miniscope imaging data
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/reference_images/OnePhotonSeries/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/reference_images/OnePhotonSeries/imaging_plane/OpticalChannel (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/reference_images/OnePhotonSeries/imaging_plane/device (Device) NVista3
  session_description: HIV-1 Tat tg mice [Tat(-)]
  session_start_time: 2023-04-20T10:17:32.100000+00:00
  timestamps_reference_time: 2023-04-20T10:17:32.100000+00:00
