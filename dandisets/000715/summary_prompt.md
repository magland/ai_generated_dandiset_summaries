
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000715/0.240614.1942
name: NeuroPAL: Atlas of C. elegans neuron locations and colors in NeuroPAL worm
contributor: [{'name': 'Yemini, Eviatar', 'email': 'evictor.yemini@umassmed.edu', 'roleName': ['dcite:Author', 'dcite:Conceptualization', 'dcite:DataCollector', 'dcite:Methodology'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Venkatachalam, Vivek', 'roleName': ['dcite:ProjectMember', 'dcite:Researcher'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Lin, Albert', 'roleName': ['dcite:ProjectMember'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Varol, Erdem', 'roleName': ['dcite:ProjectMember'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Sprague, Daniel', 'email': 'Daniel.sprague@ucsf.edu', 'roleName': ['dcite:Author', 'dcite:DataCurator', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Paninski, Liam', 'roleName': ['dcite:ProjectMember'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Samuel, Arivinthan', 'roleName': ['dcite:ProjectMember'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Hobert, Oliver', 'roleName': ['dcite:Investigation'], 'schemaKey': 'Person', 'includeInCitation': True}]
description: 10 original NeuroPAL datasets used to train the statistical atlas in 'Statistical Atlas of C. elegans Neurons' and 'NeuroPAL: A Multicolor Atlas for Whole-Brain Neuronal Identification in C. elegans.


assetsSummary: {'species': [{'name': 'Caenorhabditis elegans', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_6239'}], 'approach': [{'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 835049434, 'numberOfFiles': 10, 'numberOfSubjects': 10, 'variableMeasured': ['PlaneSegmentation', 'ProcessingModule'], 'measurementTechnique': [{'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000715 has 10 NWB files.
10 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/NeuroPALImageRaw (MultiChannelVolume) 
  Group /acquisition/NeuroPALImageRaw/imaging_volume (ImagingVolume) 
  Group /acquisition/NeuroPALImageRaw/imaging_volume/CyOFP1 (OpticalChannelPlus) 
  Group /acquisition/NeuroPALImageRaw/imaging_volume/GFP-GCaMP (OpticalChannelPlus) 
  Group /acquisition/NeuroPALImageRaw/imaging_volume/Tag RFP-T (OpticalChannelPlus) 
  Group /acquisition/NeuroPALImageRaw/imaging_volume/device (Device) Spinning Disk Confocal Nikon Ti-e 60x Objective, 1.2 NA	Nikon CFI Plan Apochromat VC 60XC WI
  Group /acquisition/NeuroPALImageRaw/imaging_volume/mNeptune 2.5 (OpticalChannelPlus) 
  Group /acquisition/NeuroPALImageRaw/imaging_volume/mTagBFP2 (OpticalChannelPlus) 
  Group /acquisition/NeuroPALImageRaw/imaging_volume/order_optical_channels (OpticalChannelReferences) 
  file_create_date: ['2024-02-26T15:34:19.004261-08:00']
  Group /general/devices/Spinning disk confocal (Device) Spinning Disk Confocal Nikon Ti-e 60x Objective, 1.2 NA	Nikon CFI Plan Apochromat VC 60XC WI
  experiment_description: NeuroPAL whole-brain structural images
  experimenter: ['Yemini, Eviatar']
  institution: Columbia University
  lab: Hobert lab
  Group /general/optophysiology/NeuroPALImVol (ImagingVolume) 
  Group /general/optophysiology/NeuroPALImVol/CyOFP1 (OpticalChannelPlus) 
  Group /general/optophysiology/NeuroPALImVol/GFP-GCaMP (OpticalChannelPlus) 
  Group /general/optophysiology/NeuroPALImVol/Tag RFP-T (OpticalChannelPlus) 
  Group /general/optophysiology/NeuroPALImVol/device (Device) Spinning Disk Confocal Nikon Ti-e 60x Objective, 1.2 NA	Nikon CFI Plan Apochromat VC 60XC WI
  Group /general/optophysiology/NeuroPALImVol/mNeptune 2.5 (OpticalChannelPlus) 
  Group /general/optophysiology/NeuroPALImVol/mTagBFP2 (OpticalChannelPlus) 
  Group /general/optophysiology/NeuroPALImVol/order_optical_channels (OpticalChannelReferences) 
  related_publications: ['NeuroPAL: A Multicolor Atlas for Whole-Brain Neuronal Identification in C. elegans']
  Group /general/subject (CElegansSubject) 
  identifier: 11_YAaLR
  Group /processing/NeuroPAL (ProcessingModule) NeuroPAL image data and metadata
  Group /processing/NeuroPAL/NeuroPALSegmentation (ImageSegmentation) 
  Group /processing/NeuroPAL/NeuroPALSegmentation/NeuroPALNeurons (PlaneSegmentation) Neuron centers for multichannel volumetric image. Weight set at 1 for all voxels. Labels refers to cell ID of segmented neurons.
  Dataset /processing/NeuroPAL/NeuroPALSegmentation/NeuroPALNeurons/ID_labels (VectorData) ROI ID labels | shape = (777,) | dtype = object
  Dataset /processing/NeuroPAL/NeuroPALSegmentation/NeuroPALNeurons/ID_labels_index (VectorIndex) Index for VectorData 'ID_labels' | shape = (194,) | dtype = uint16
  Dataset /processing/NeuroPAL/NeuroPALSegmentation/NeuroPALNeurons/id (ElementIdentifiers)  | shape = (194,) | dtype = int64
  Group /processing/NeuroPAL/NeuroPALSegmentation/NeuroPALNeurons/imaging_plane (ImagingVolume) 
  Group /processing/NeuroPAL/NeuroPALSegmentation/NeuroPALNeurons/imaging_plane/CyOFP1 (OpticalChannelPlus) 
  Group /processing/NeuroPAL/NeuroPALSegmentation/NeuroPALNeurons/imaging_plane/GFP-GCaMP (OpticalChannelPlus) 
  Group /processing/NeuroPAL/NeuroPALSegmentation/NeuroPALNeurons/imaging_plane/Tag RFP-T (OpticalChannelPlus) 
  Group /processing/NeuroPAL/NeuroPALSegmentation/NeuroPALNeurons/imaging_plane/device (Device) Spinning Disk Confocal Nikon Ti-e 60x Objective, 1.2 NA	Nikon CFI Plan Apochromat VC 60XC WI
  Group /processing/NeuroPAL/NeuroPALSegmentation/NeuroPALNeurons/imaging_plane/mNeptune 2.5 (OpticalChannelPlus) 
  Group /processing/NeuroPAL/NeuroPALSegmentation/NeuroPALNeurons/imaging_plane/mTagBFP2 (OpticalChannelPlus) 
  Group /processing/NeuroPAL/NeuroPALSegmentation/NeuroPALNeurons/imaging_plane/order_optical_channels (OpticalChannelReferences) 
  Dataset /processing/NeuroPAL/NeuroPALSegmentation/NeuroPALNeurons/voxel_mask (VectorData) Voxel masks for each ROI | shape = (194,) | dtype = [('x', '<u4'), ('y', '<u4'), ('z', '<u4'), ('weight', '<f4')]
  Dataset /processing/NeuroPAL/NeuroPALSegmentation/NeuroPALNeurons/voxel_mask_index (VectorIndex) Index for VectorData 'voxel_mask' | shape = (194,) | dtype = uint8
  session_description: C. elegans head NeuroPAL
  session_start_time: 2021-01-07T00:00:00-08:00
  timestamps_reference_time: 2021-01-07T00:00:00-08:00
