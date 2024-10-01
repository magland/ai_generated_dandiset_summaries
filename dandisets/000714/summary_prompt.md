
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000714/0.240611.1954
name: Segmented and labeled NeuroPAL structural images
contributor: [{'name': 'Sprague, Daniel', 'email': 'daniel.y.sprague@gmail.com', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Chaudhary, Shivesh', 'email': 'shiveshc@gmail.com', 'roleName': ['dcite:Author', 'dcite:ContactPerson', 'dcite:DataCollector', 'dcite:Conceptualization', 'dcite:FormalAnalysis', 'dcite:Investigation', 'dcite:Methodology', 'dcite:Validation', 'dcite:Software'], 'schemaKey': 'Person', 'affiliation': [{'name': 'School of Chemical & Biomolecular Engineering, Georgia Institute of Technology, Atlanta, United States', 'schemaKey': 'Affiliation'}], 'includeInCitation': True}, {'name': 'Lee, Sol Ah', 'roleName': ['dcite:Investigation'], 'schemaKey': 'Person', 'affiliation': [{'name': 'School of Chemical & Biomolecular Engineering, Georgia Institute of Technology, Atlanta, United States', 'schemaKey': 'Affiliation'}], 'includeInCitation': True}, {'name': 'Li, Yueyi', 'roleName': ['dcite:Investigation'], 'schemaKey': 'Person', 'affiliation': [{'name': 'School of Chemical & Biomolecular Engineering, Georgia Institute of Technology, Atlanta, United States', 'schemaKey': 'Affiliation'}], 'includeInCitation': True}, {'name': 'Patel, Dhaval S', 'roleName': ['dcite:Methodology'], 'schemaKey': 'Person', 'affiliation': [{'name': 'School of Chemical & Biomolecular Engineering, Georgia Institute of Technology, Atlanta, United States', 'schemaKey': 'Affiliation'}], 'includeInCitation': True}, {'name': 'Lu, Hang', 'roleName': ['dcite:Conceptualization', 'dcite:FormalAnalysis', 'dcite:Investigation', 'dcite:Methodology', 'dcite:ProjectAdministration', 'dcite:Visualization'], 'schemaKey': 'Person', 'affiliation': [{'name': 'School of Chemical & Biomolecular Engineering, Georgia Institute of Technology, Atlanta, United States', 'schemaKey': 'Affiliation'}], 'includeInCitation': True}]
description: Segmented and labeled NeuroPAL datasets from "Graphical-model framework for automated annotation of cell identities in dense cellular images" by Shivesh Chaudhary, et al.
assetsSummary: {'species': [{'name': 'Caenorhabditis elegans', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_6239'}], 'approach': [{'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 478075700, 'numberOfFiles': 9, 'numberOfSubjects': 9, 'variableMeasured': ['ProcessingModule', 'PlaneSegmentation'], 'measurementTechnique': [{'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000714 has 9 NWB files.
9 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/NeuroPALImageRaw (MultiChannelVolume) 
  Group /acquisition/NeuroPALImageRaw/imaging_volume (ImagingVolume) 
  Group /acquisition/NeuroPALImageRaw/imaging_volume/CyOFP1 (OpticalChannelPlus) 
  Group /acquisition/NeuroPALImageRaw/imaging_volume/Tag RFP-T (OpticalChannelPlus) 
  Group /acquisition/NeuroPALImageRaw/imaging_volume/device (Device) Perkin Elmer spinning disk confocal microscope 40x Objective, oil objective with an EMCCD camera
  Group /acquisition/NeuroPALImageRaw/imaging_volume/mNeptune 2.5 (OpticalChannelPlus) 
  Group /acquisition/NeuroPALImageRaw/imaging_volume/mTagBFP2 (OpticalChannelPlus) 
  Group /acquisition/NeuroPALImageRaw/imaging_volume/order_optical_channels (OpticalChannelReferences) 
  file_create_date: ['2024-02-26T15:34:22.344318-08:00']
  Group /general/devices/Spinning disk confocal (Device) Perkin Elmer spinning disk confocal microscope 40x Objective, oil objective with an EMCCD camera
  experiment_description: NeuroPAL whole-brain structural images
  experimenter: ['Chaudhary, Shivesh']
  institution: Georgia Tech University
  lab: Lu Lab
  Group /general/optophysiology/NeuroPALImVol (ImagingVolume) 
  Group /general/optophysiology/NeuroPALImVol/CyOFP1 (OpticalChannelPlus) 
  Group /general/optophysiology/NeuroPALImVol/Tag RFP-T (OpticalChannelPlus) 
  Group /general/optophysiology/NeuroPALImVol/device (Device) Perkin Elmer spinning disk confocal microscope 40x Objective, oil objective with an EMCCD camera
  Group /general/optophysiology/NeuroPALImVol/mNeptune 2.5 (OpticalChannelPlus) 
  Group /general/optophysiology/NeuroPALImVol/mTagBFP2 (OpticalChannelPlus) 
  Group /general/optophysiology/NeuroPALImVol/order_optical_channels (OpticalChannelReferences) 
  related_publications: ['Graphical-model framework for automated annotation of cell identities in dense cellular images']
  Group /general/subject (CElegansSubject) 
  identifier: 1
  Group /processing/NeuroPAL (ProcessingModule) NeuroPAL image data and metadata
  Group /processing/NeuroPAL/NeuroPALSegmentation (ImageSegmentation) 
  Group /processing/NeuroPAL/NeuroPALSegmentation/NeuroPALNeurons (PlaneSegmentation) Neuron centers for multichannel volumetric image. Weight set at 1 for all voxels. Labels refers to cell ID of segmented neurons.
  Dataset /processing/NeuroPAL/NeuroPALSegmentation/NeuroPALNeurons/ID_labels (VectorData) ROI ID labels | shape = (257,) | dtype = object
  Dataset /processing/NeuroPAL/NeuroPALSegmentation/NeuroPALNeurons/ID_labels_index (VectorIndex) Index for VectorData 'ID_labels' | shape = (113,) | dtype = uint16
  Dataset /processing/NeuroPAL/NeuroPALSegmentation/NeuroPALNeurons/id (ElementIdentifiers)  | shape = (113,) | dtype = int64
  Group /processing/NeuroPAL/NeuroPALSegmentation/NeuroPALNeurons/imaging_plane (ImagingVolume) 
  Group /processing/NeuroPAL/NeuroPALSegmentation/NeuroPALNeurons/imaging_plane/CyOFP1 (OpticalChannelPlus) 
  Group /processing/NeuroPAL/NeuroPALSegmentation/NeuroPALNeurons/imaging_plane/Tag RFP-T (OpticalChannelPlus) 
  Group /processing/NeuroPAL/NeuroPALSegmentation/NeuroPALNeurons/imaging_plane/device (Device) Perkin Elmer spinning disk confocal microscope 40x Objective, oil objective with an EMCCD camera
  Group /processing/NeuroPAL/NeuroPALSegmentation/NeuroPALNeurons/imaging_plane/mNeptune 2.5 (OpticalChannelPlus) 
  Group /processing/NeuroPAL/NeuroPALSegmentation/NeuroPALNeurons/imaging_plane/mTagBFP2 (OpticalChannelPlus) 
  Group /processing/NeuroPAL/NeuroPALSegmentation/NeuroPALNeurons/imaging_plane/order_optical_channels (OpticalChannelReferences) 
  Dataset /processing/NeuroPAL/NeuroPALSegmentation/NeuroPALNeurons/voxel_mask (VectorData) Voxel masks for each ROI | shape = (113,) | dtype = [('x', '<u4'), ('y', '<u4'), ('z', '<u4'), ('weight', '<f4')]
  Dataset /processing/NeuroPAL/NeuroPALSegmentation/NeuroPALNeurons/voxel_mask_index (VectorIndex) Index for VectorData 'voxel_mask' | shape = (113,) | dtype = uint8
  session_description: C. elegans head NeuroPAL
  session_start_time: 2021-02-24T00:00:00-08:00
  timestamps_reference_time: 2021-02-24T00:00:00-08:00
