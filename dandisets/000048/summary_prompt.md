
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000048/draft
name: Electrical and optical physiology in in vivo population-scale two-photon calcium imaging
contributor: [{'name': 'Ledochowitsch, Peter', 'roleName': ['dcite:Author', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Huang, Lawrence', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Knoblich, Ulf', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Oliver, Michael', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Lecoq, Jerome', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Reid, Clay', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Li, Lu', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Zeng, Hongkui', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Koch, Christof', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Waters, Jack', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Vries, Saskia E.J. de', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Buice, Michael A.', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'includeInCitation': True}]
description: Spiking activity and simultaneously recorded fluorescence signals in transgenic mice expressing GCaMP6

We present a dataset consisting of simultaneously measured fluorescence and spiking activity of pyramidal neurons in layer 2/3 of primary visual cortex in transgenic mouse lines expressing genetically-encoded calcium indicators (GECIs) GCaMP6s or GCaMP6f.

Reference: https://portal.brain-map.org/explore/circuits/oephys
assetsSummary: {'species': [], 'approach': [{'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}, {'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 590267164, 'numberOfFiles': 1, 'numberOfSubjects': 1, 'variableMeasured': ['PlaneSegmentation', 'TwoPhotonSeries', 'ElectrodeGroup', 'Units'], 'measurementTechnique': [{'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'two-photon microscopy technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000048 has 1 NWB files.
1 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeries_raw (ElectricalSeries) ADDME
  Dataset /acquisition/ElectricalSeries_raw/electrodes (DynamicTableRegion) electrode | shape = (1,) | dtype = int32
  Group /acquisition/TwoPhotonSeries_green (TwoPhotonSeries) no description
  Group /acquisition/TwoPhotonSeries_green/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeries_green/imaging_plane/device (Device) 
  Group /acquisition/TwoPhotonSeries_green/imaging_plane/optical_channel (OpticalChannel) 
  file_create_date: ['2020-12-08T22:03:32.795517+01:00']
  Group /general/devices/Bruker 2-p microscope (Device) 
  Group /general/devices/MultiClamp 700B (Device) 
  Group /general/extracellular_ephys/ElectrodeGroup (ElectrodeGroup) 2-p targeted cell-attached
  Group /general/extracellular_ephys/ElectrodeGroup/device (Device) 
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (1,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (1,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (1,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (1,) | dtype = float64
  institution: Allen Institute for Brain Science
  Group /general/optophysiology/ImagingPlane (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane/device (Device) 
  Group /general/optophysiology/ImagingPlane/optical_channel (OpticalChannel) 
  pharmacology: Isoflurane
  Group /general/subject (Subject) 
  identifier: 102086
  Group /processing/ecephys (ProcessingModule) contains extracellular electrophysiology processed data
  Group /processing/ecephys/ElectricalSeries_processed (ElectricalSeries) voltage trace filtered between 250 Hz and 5 kHz
  Dataset /processing/ecephys/ElectricalSeries_processed/electrodes (DynamicTableRegion) electrode | shape = (1,) | dtype = int32
  Group /processing/ophys (ProcessingModule) contains optical physiology processed data
  Group /processing/ophys/Fluorescence (Fluorescence) 
  Group /processing/ophys/Fluorescence/roi_response_series (RoiResponseSeries) no description
  Dataset /processing/ophys/Fluorescence/roi_response_series/rois (DynamicTableRegion) unique cell ROI | shape = (1,) | dtype = int32
  Group /processing/ophys/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/ImageSegmentation/plane_segmentation (PlaneSegmentation) ADDME
  Dataset /processing/ophys/ImageSegmentation/plane_segmentation/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/ophys/ImageSegmentation/plane_segmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/plane_segmentation/imaging_plane/device (Device) 
  Group /processing/ophys/ImageSegmentation/plane_segmentation/imaging_plane/optical_channel (OpticalChannel) 
  Dataset /processing/ophys/ImageSegmentation/plane_segmentation/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1715, 3) | dtype = int32
  Dataset /processing/ophys/ImageSegmentation/plane_segmentation/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint16
  session_description: example conversion
  session_start_time: 1900-01-01T00:00:00-05:00
  timestamps_reference_time: 1900-01-01T00:00:00-05:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (233,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (1,) | dtype = uint8
