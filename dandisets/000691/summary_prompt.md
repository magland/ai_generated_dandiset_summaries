
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000691/draft
name: An optical design enabling lightweight and large field-of-view head-mounted microscopes
contributor: [{'name': 'Scherrer, Joseph R.', 'email': 'fee@mit.edu', 'roleName': ['dcite:Author', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0003-0424-3483', 'affiliation': [], 'includeInCitation': True}, {'name': 'Lynch, Galen F.', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Zhang, Jie J.', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Fee, Michale S.', 'email': 'fee@mit.edu', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0001-7539-1745', 'affiliation': [], 'includeInCitation': True}, {'name': 'Simons Foundation', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01cmst727', 'awardNumber': '542977ASPI', 'contactPoint': [], 'includeInCitation': False}, {'name': 'National Institutes of Health', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01cwqze88', 'awardNumber': 'R21 EY028381-01', 'contactPoint': [], 'includeInCitation': False}, {'name': 'McKnight Foundation', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'contactPoint': [], 'includeInCitation': False}, {'name': 'Harold and Ruth Newman Family Hertz Graduate Fellowship', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'contactPoint': [], 'includeInCitation': False}]
description: Here we present a fluorescence microscope light path that enables imaging, during free behavior, of thousands of neurons in mice and hundreds of neurons in juvenile songbirds. The light path eliminates traditional illumination optics, allowing for head-mounted microscopes that have both a lower weight and a larger field of view (FOV) than previously possible. Using this light path, we designed two microscopes: one optimized for FOV (~4 mm FOV; 1.4 g), and the other optimized for weight (1.0 mm FOV; 1.0 g). 
This dataset includes the calcium imaging data from our microscope optimized for weight. For this experiment, we stereotactically located a region of the mouse brain at coordinates associatied with primary visual and somatosensory regions, performed approximately 20 viral injections of GCaMP7f across a 4-mm-diameter region of cortex, and then implanted a 4-mm-diameter glass window in the skull. After letting each mouse recover, we installed our head-mounted microscope and allowed it to freely explore a circular maze while recording calcium activity for several minutes.
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 15338089927, 'numberOfFiles': 2, 'numberOfSubjects': 1, 'variableMeasured': ['TwoPhotonSeries', 'ImagingPlane', 'ProcessingModule', 'PlaneSegmentation', 'OpticalChannel'], 'measurementTechnique': [{'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'two-photon microscopy technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000691 has 1 NWB files.
1 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/TwoPhotonSeries (TwoPhotonSeries) Calcium imaging data at ~30 fps in grayscale format
  Group /acquisition/TwoPhotonSeries/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeries/imaging_plane/OpticalChannel (OpticalChannel) 
  Group /acquisition/TwoPhotonSeries/imaging_plane/channel_0 (OpticalChannel) 
  Group /acquisition/TwoPhotonSeries/imaging_plane/device (Device) 
  Group /acquisition/Video: home_arena_2021-07-26T13_50_50 (ImageSeries) Behavior video of animal moving in environment at ~30 fps
  file_create_date: ['2022-11-27T21:52:11.894383+01:00']
  Group /general/devices/Microscope (Device) 
  experiment_description: Here we present a fluorescence microscope light path that enables imaging, during free behavior, of thousands of neurons in mice and hundreds of neurons in juvenile songbirds. The light path eliminates traditional illumination optics, allowing for head-mounted microscopes that have both a lower weight and a larger field of view (FOV) than previously possible. Using this light path, we designed two microscopes: one optimized for FOV (~4 mm FOV; 1.4 g), and the other optimized for weight (1.0 mm FOV; 1.0 g). This dataset includes the calcium imaging data from our microscope optimized for weight.For this experiment, we stereotactically located a region of the mouse brain at coordinates associatied with primary visual and somatosensory regions, performed approximately 20 viral injections of GCaMP7f across a 4-mm-diameter region of cortex, and then implanted a 4-mm-diameter glass window in the skull. After letting each mouse recover, we installed our head-mounted microscope and allowed it to freely explore a circular maze while recording calcium activity for several minutes.
  experimenter: ['Scherrer, Joseph']
  institution: Massachusetts Institute of Technology
  lab: Fee Lab
  Group /general/optophysiology/ImagingPlane (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane/OpticalChannel (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane/channel_0 (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane/device (Device) 
  related_publications: ['https://doi.org/10.1038/s41592-023-01806-1']
  session_id: 2021-07-26T13-50-50
  Group /general/subject (Subject) 
  surgery: 4mm glass window implant over right visual and somatosensory cortex
  
  virus: GCaMP7f
  identifier: 0a2c0092-990e-4bfb-adf5-30daa2fcde6f
  Group /processing/ophys (ProcessingModule) contains optical physiology processed data
  Group /processing/ophys/DfOverF (DfOverF) 
  Group /processing/ophys/DfOverF/RoiResponseSeries (RoiResponseSeries) Array of df/F traces.
  Dataset /processing/ophys/DfOverF/RoiResponseSeries/rois (DynamicTableRegion) region for Imaging plane0 | shape = (2948,) | dtype = int64
  Group /processing/ophys/ImageSegmentation (EXTRACTSegmentation) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation (PlaneSegmentation) Segmented ROIs
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/ROICentroids (VectorData) The x, y, (z) centroids of each ROI. | shape = (2948, 2) | dtype = int64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/id (ElementIdentifiers)  | shape = (2948,) | dtype = int64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/image_mask (VectorData) Image masks for each ROI. | shape = (2948, 808, 608) | dtype = float32
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/OpticalChannel (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/channel_0 (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/device (Device) 
  Group /processing/ophys/SegmentationImages (Images) no description
  Dataset /processing/ophys/SegmentationImages/f_per_pixel (GrayscaleImage)  | shape = (808, 608) | dtype = float64
  Dataset /processing/ophys/SegmentationImages/max_image (GrayscaleImage)  | shape = (808, 608) | dtype = float64
  Dataset /processing/ophys/SegmentationImages/summary_image (GrayscaleImage)  | shape = (808, 608) | dtype = float64
  session_description: This session includes calcium imaging recorded from a head-mounted microscope in a freely moving mouse while simultaneously recording more than a thousand neurons in cortex.
  session_start_time: 2021-07-26T13:50:50.236377-04:00
  timestamps_reference_time: 2021-07-26T13:50:50.236377-04:00
