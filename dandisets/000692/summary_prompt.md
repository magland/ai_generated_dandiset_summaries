
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000692/0.240402.2118
name: Whole-brain spontaneous GCaMP activity with NeuroPAL cell ID information of semi-restricted worms
contributor: [{'name': 'Suzuki, Ryoga', 'roleName': ['dcite:Author', 'dcite:DataCollector', 'dcite:FormalAnalysis', 'dcite:Investigation', 'dcite:ProjectMember', 'dcite:Researcher', 'dcite:Software'], 'schemaKey': 'Person', 'affiliation': [{'name': 'Nagoya City University', 'schemaKey': 'Affiliation'}], 'includeInCitation': True}, {'url': 'https://github.com/WenChentao', 'name': 'Wen, Chentao', 'email': 'chentao.wen@riken.jp', 'roleName': ['dcite:Author', 'dcite:Methodology', 'dcite:Researcher', 'dcite:Software'], 'schemaKey': 'Person', 'identifier': '0000-0002-8609-476X', 'affiliation': [{'name': 'RIKEN Center for Biosystems Dynamics Research', 'schemaKey': 'Affiliation'}], 'includeInCitation': True}, {'name': 'Sprague, Daniel', 'email': 'Daniel.Sprague@ucsf.edu', 'roleName': ['dcite:Software'], 'schemaKey': 'Person', 'identifier': '0009-0001-7773-2280', 'affiliation': [{'name': 'UCSF Department of Neurology', 'schemaKey': 'Affiliation'}], 'includeInCitation': True}, {'url': 'https://www.bdr.riken.jp/en/research/labs/onami-s/index.html', 'name': 'Onami, Shuichi', 'email': 'sonami@riken.jp', 'roleName': ['dcite:Author', 'dcite:Methodology', 'dcite:Software', 'dcite:Supervision'], 'schemaKey': 'Person', 'identifier': '0000-0002-8255-1724', 'affiliation': [{'name': 'RIKEN Center for Biosystems Dynamics Research', 'schemaKey': 'Affiliation'}], 'includeInCitation': True}, {'name': 'Kimura, Koutarou D', 'email': 'kokimura@nsc.nagoya-cu.ac.jp', 'roleName': ['dcite:Author', 'dcite:Conceptualization', 'dcite:ContactPerson', 'dcite:FundingAcquisition', 'dcite:Methodology', 'dcite:ProjectLeader', 'dcite:Supervision', 'dcite:Validation'], 'schemaKey': 'Person', 'identifier': '0000-0002-3359-1578', 'affiliation': [{'name': 'Nagoya City University', 'schemaKey': 'Affiliation'}], 'includeInCitation': True}]
description: Spontaneous neuronal activities were extracted from GCaMP and tagRFP images, covering nearly all neurons in the nematode C. elegans brain. Cell segmentation and tracking were performed using 3DeeCellTracker (https://github.com/WenChentao/3DeeCellTracker). Neuronal identity information was derived from NeuroPAL signals with the NeuroPAL Auto-ID software (https://www.yeminilab.com/neuropal) and manual corrections. During the data acquisition, worms were semi-restricted in a microfluidic device (https://www.nature.com/articles/nature06292). Note: There are occasional transient failures in neuronal tracking. We recommend researchers to use a moving median filter (e.g., ±3) on the time series data to address this issue.
assetsSummary: {'species': [{'name': 'Caenorhabditis elegans', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_6239'}], 'approach': [{'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 80537036658, 'numberOfFiles': 9, 'numberOfSubjects': 9, 'variableMeasured': ['PlaneSegmentation', 'ProcessingModule'], 'measurementTechnique': [{'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000692 has 9 NWB files.
9 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/CalciumImageSeries (MultiChannelVolumeSeries) Raw GCaMP (channel 0) and RFP (channel 1) image series
  Group /acquisition/CalciumImageSeries/device (Device) Nikon Eclipe Ti-U Inverted Microscope with Yokogawa CSU-X1 SoRA, 40x objective 1.3 NA
  Group /acquisition/CalciumImageSeries/imaging_volume (ImagingVolume) 
  Group /acquisition/CalciumImageSeries/imaging_volume/GCaMP (OpticalChannelPlus) 
  Group /acquisition/CalciumImageSeries/imaging_volume/TagRFP-T (OpticalChannelPlus) 
  Group /acquisition/CalciumImageSeries/imaging_volume/device (Device) Nikon Eclipe Ti-U Inverted Microscope with Yokogawa CSU-X1 SoRA, 40x objective 1.3 NA
  Group /acquisition/CalciumImageSeries/imaging_volume/order_optical_channels (OpticalChannelReferences) 
  Group /acquisition/NeuroPALImageRaw (MultiChannelVolume) 
  Group /acquisition/NeuroPALImageRaw/imaging_volume (ImagingVolume) 
  Group /acquisition/NeuroPALImageRaw/imaging_volume/CyOFP1 (OpticalChannelPlus) 
  Group /acquisition/NeuroPALImageRaw/imaging_volume/Tag RFP-T (OpticalChannelPlus) 
  Group /acquisition/NeuroPALImageRaw/imaging_volume/device (Device) Nikon Eclipe Ti-U Inverted Microscope with Yokogawa CSU-X1 SoRA, 40x objective 1.3 NA
  Group /acquisition/NeuroPALImageRaw/imaging_volume/mNeptune 2.5 (OpticalChannelPlus) 
  Group /acquisition/NeuroPALImageRaw/imaging_volume/mTagBFP2 (OpticalChannelPlus) 
  Group /acquisition/NeuroPALImageRaw/imaging_volume/order_optical_channels (OpticalChannelReferences) 
  file_create_date: ['2023-10-07T22:17:13.356042+09:00']
  Group /general/devices/Spinning disk confocal (Device) Nikon Eclipe Ti-U Inverted Microscope with Yokogawa CSU-X1 SoRA, 40x objective 1.3 NA
  institution: Nagoya City University
  lab: Kimura lab
  Group /general/optophysiology/CalciumImVol (ImagingVolume) 
  Group /general/optophysiology/CalciumImVol/GCaMP (OpticalChannelPlus) 
  Group /general/optophysiology/CalciumImVol/TagRFP-T (OpticalChannelPlus) 
  Group /general/optophysiology/CalciumImVol/device (Device) Nikon Eclipe Ti-U Inverted Microscope with Yokogawa CSU-X1 SoRA, 40x objective 1.3 NA
  Group /general/optophysiology/CalciumImVol/order_optical_channels (OpticalChannelReferences) 
  Group /general/optophysiology/NeuroPALImVol (ImagingVolume) 
  Group /general/optophysiology/NeuroPALImVol/CyOFP1 (OpticalChannelPlus) 
  Group /general/optophysiology/NeuroPALImVol/Tag RFP-T (OpticalChannelPlus) 
  Group /general/optophysiology/NeuroPALImVol/device (Device) Nikon Eclipe Ti-U Inverted Microscope with Yokogawa CSU-X1 SoRA, 40x objective 1.3 NA
  Group /general/optophysiology/NeuroPALImVol/mNeptune 2.5 (OpticalChannelPlus) 
  Group /general/optophysiology/NeuroPALImVol/mTagBFP2 (OpticalChannelPlus) 
  Group /general/optophysiology/NeuroPALImVol/order_optical_channels (OpticalChannelReferences) 
  related_publications: ['unpublished']
  Group /general/subject (CElegansSubject) 
  identifier: 20230918-9-54-0
  Group /processing/CalciumActivity (ProcessingModule) Calcium and RFP image series metadata, segmentation, and fluorescence data
  Group /processing/CalciumActivity/CalciumSeriesSegmentation (MultiChannelVolumeSeries) Tracking results based on RFP image series, each value i indicates that voxel belongs to ROI i,value 0 indicate that voxel belongs to the background
  Group /processing/CalciumActivity/CalciumSeriesSegmentation/device (Device) Nikon Eclipe Ti-U Inverted Microscope with Yokogawa CSU-X1 SoRA, 40x objective 1.3 NA
  Group /processing/CalciumActivity/CalciumSeriesSegmentation/imaging_volume (ImagingVolume) 
  Group /processing/CalciumActivity/CalciumSeriesSegmentation/imaging_volume/GCaMP (OpticalChannelPlus) 
  Group /processing/CalciumActivity/CalciumSeriesSegmentation/imaging_volume/TagRFP-T (OpticalChannelPlus) 
  Group /processing/CalciumActivity/CalciumSeriesSegmentation/imaging_volume/device (Device) Nikon Eclipe Ti-U Inverted Microscope with Yokogawa CSU-X1 SoRA, 40x objective 1.3 NA
  Group /processing/CalciumActivity/CalciumSeriesSegmentation/imaging_volume/order_optical_channels (OpticalChannelReferences) 
  Group /processing/CalciumActivity/NeuronIDs (SegmentationLabels) 
  Group /processing/CalciumActivity/NeuronIDs/MCVSeriesSegmentation (MultiChannelVolumeSeries) Tracking results based on RFP image series, each value i indicates that voxel belongs to ROI i,value 0 indicate that voxel belongs to the background
  Group /processing/CalciumActivity/NeuronIDs/MCVSeriesSegmentation/device (Device) Nikon Eclipe Ti-U Inverted Microscope with Yokogawa CSU-X1 SoRA, 40x objective 1.3 NA
  Group /processing/CalciumActivity/NeuronIDs/MCVSeriesSegmentation/imaging_volume (ImagingVolume) 
  Group /processing/CalciumActivity/NeuronIDs/MCVSeriesSegmentation/imaging_volume/GCaMP (OpticalChannelPlus) 
  Group /processing/CalciumActivity/NeuronIDs/MCVSeriesSegmentation/imaging_volume/TagRFP-T (OpticalChannelPlus) 
  Group /processing/CalciumActivity/NeuronIDs/MCVSeriesSegmentation/imaging_volume/device (Device) Nikon Eclipe Ti-U Inverted Microscope with Yokogawa CSU-X1 SoRA, 40x objective 1.3 NA
  Group /processing/CalciumActivity/NeuronIDs/MCVSeriesSegmentation/imaging_volume/order_optical_channels (OpticalChannelReferences) 
  Group /processing/CalciumActivity/SegmentationVol1 (ImageSegmentation) 
  Group /processing/CalciumActivity/SegmentationVol1/Seg_tpoint_1 (PlaneSegmentation) Neuron segmentation for time point 1 in RFP image series
  Dataset /processing/CalciumActivity/SegmentationVol1/Seg_tpoint_1/id (ElementIdentifiers)  | shape = (156,) | dtype = int64
  Group /processing/CalciumActivity/SegmentationVol1/Seg_tpoint_1/imaging_plane (ImagingVolume) 
  Group /processing/CalciumActivity/SegmentationVol1/Seg_tpoint_1/imaging_plane/GCaMP (OpticalChannelPlus) 
  Group /processing/CalciumActivity/SegmentationVol1/Seg_tpoint_1/imaging_plane/TagRFP-T (OpticalChannelPlus) 
  Group /processing/CalciumActivity/SegmentationVol1/Seg_tpoint_1/imaging_plane/device (Device) Nikon Eclipe Ti-U Inverted Microscope with Yokogawa CSU-X1 SoRA, 40x objective 1.3 NA
  Group /processing/CalciumActivity/SegmentationVol1/Seg_tpoint_1/imaging_plane/order_optical_channels (OpticalChannelReferences) 
  Dataset /processing/CalciumActivity/SegmentationVol1/Seg_tpoint_1/voxel_mask (VectorData) Voxel masks for each ROI | shape = (156,) | dtype = [('x', '<u4'), ('y', '<u4'), ('z', '<u4'), ('weight', '<f4')]
  Dataset /processing/CalciumActivity/SegmentationVol1/Seg_tpoint_1/voxel_mask_index (VectorIndex) Index for VectorData 'voxel_mask' | shape = (156,) | dtype = uint8
  Group /processing/CalciumActivity/SignalRawFluor (Fluorescence) 
  Group /processing/CalciumActivity/SignalRawFluor/SignalCalciumImResponseSeries (RoiResponseSeries) GCaMP activities of all neurons tracked in RFP images
  Dataset /processing/CalciumActivity/SignalRawFluor/SignalCalciumImResponseSeries/rois (DynamicTableRegion) All segmented neurons at vol #1 of RFP image | shape = (156,) | dtype = int64
  Group /processing/NeuroPAL (ProcessingModule) NeuroPAL image metadata and segmentation
  Group /processing/NeuroPAL/NeuroPALSegmentation (ImageSegmentation) 
  Group /processing/NeuroPAL/NeuroPALSegmentation/NeuroPALNeurons (PlaneSegmentation) Neuron centers for multichannel volumetric image. Weight set at 1 for all voxels. Labels refers to character IDs of segmented neurons
  Dataset /processing/NeuroPAL/NeuroPALSegmentation/NeuroPALNeurons/ID_labels (VectorData) ROI ID labels | shape = (612,) | dtype = object
  Dataset /processing/NeuroPAL/NeuroPALSegmentation/NeuroPALNeurons/ID_labels_index (VectorIndex) Index for VectorData 'ID_labels' | shape = (150,) | dtype = uint16
  Dataset /processing/NeuroPAL/NeuroPALSegmentation/NeuroPALNeurons/id (ElementIdentifiers)  | shape = (150,) | dtype = int64
  Group /processing/NeuroPAL/NeuroPALSegmentation/NeuroPALNeurons/imaging_plane (ImagingVolume) 
  Group /processing/NeuroPAL/NeuroPALSegmentation/NeuroPALNeurons/imaging_plane/CyOFP1 (OpticalChannelPlus) 
  Group /processing/NeuroPAL/NeuroPALSegmentation/NeuroPALNeurons/imaging_plane/Tag RFP-T (OpticalChannelPlus) 
  Group /processing/NeuroPAL/NeuroPALSegmentation/NeuroPALNeurons/imaging_plane/device (Device) Nikon Eclipe Ti-U Inverted Microscope with Yokogawa CSU-X1 SoRA, 40x objective 1.3 NA
  Group /processing/NeuroPAL/NeuroPALSegmentation/NeuroPALNeurons/imaging_plane/mNeptune 2.5 (OpticalChannelPlus) 
  Group /processing/NeuroPAL/NeuroPALSegmentation/NeuroPALNeurons/imaging_plane/mTagBFP2 (OpticalChannelPlus) 
  Group /processing/NeuroPAL/NeuroPALSegmentation/NeuroPALNeurons/imaging_plane/order_optical_channels (OpticalChannelReferences) 
  Dataset /processing/NeuroPAL/NeuroPALSegmentation/NeuroPALNeurons/voxel_mask (VectorData) Voxel masks for each ROI | shape = (150,) | dtype = [('x', '<u4'), ('y', '<u4'), ('z', '<u4'), ('weight', '<f4')]
  Dataset /processing/NeuroPAL/NeuroPALSegmentation/NeuroPALNeurons/voxel_mask_index (VectorIndex) Index for VectorData 'voxel_mask' | shape = (150,) | dtype = uint8
  session_description: NeuroPAL+ Calcium Imaging without Stimulation
  session_start_time: 2023-09-18T09:54:00+09:00
  timestamps_reference_time: 2023-09-18T09:54:00+09:00
