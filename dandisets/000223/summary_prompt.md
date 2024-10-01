
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000223/0.220823.0826
name: Inferring monosynaptic connections from paired spine calcium imaging and large-scale recording of extracellular spiking
contributor: [{'name': 'Xue, Xiaohan', 'email': 'xiaohan.xue@outlook.com', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0001-5398-2368', 'affiliation': [{'name': 'ETH Zurich', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/05a28rw58'}], 'awardNumber': 'China Scholarship Council; ERC advanced grant 694829', 'includeInCitation': True}, {'name': 'Buccino, Alessio', 'email': 'alessiop.buccino@gmail.com', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0003-3661-527X', 'affiliation': [{'name': 'ETH Zurich', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/05a28rw58'}], 'awardNumber': 'ETH Zurich Postdoctoral Fellowship 19-2 FEL-17', 'includeInCitation': True}, {'name': 'Kumar, Sreedhar Saseendran', 'email': 'sreedhar.kumar@bsse.ethz.ch', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-5272-6474', 'affiliation': [{'name': 'ETH Zurich', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/05a28rw58'}], 'awardNumber': 'ERC advanced grant 694829', 'includeInCitation': True}, {'name': 'Hierlemann, Andreas', 'email': 'andreas.hierlemann@bsse.ethz.ch', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-3838-2468', 'affiliation': [{'name': 'ETH Zurich', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/05a28rw58'}], 'awardNumber': 'ERC advanced grant 694829', 'includeInCitation': True}, {'name': 'Bartram, Julian', 'email': 'julian.bartram@bsse.ethz.ch', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0001-7513-1716', 'affiliation': [{'name': 'ETH Zurich', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/05a28rw58'}], 'awardNumber': 'ERC advanced grant 694829', 'includeInCitation': True}]
description: This dataset contains paired calcium imaging and high-density microelectrode array (HD-MEA) recordings from cortical embryonic cell cultures. 
The data is used to infer monosynaptic connections using dendritic spine calcium traces and extracellular spiking.
Each file includes:
- raw extracellular recordings 
- spike-sorted units
- imaging series
- segmentation ROIs (of the target spines and adjacent dendritic shaft)
assetsSummary: {'species': [{'name': 'Rattus norvegicus - Norway rat', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10116'}], 'approach': [{'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}, {'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 84273722669, 'numberOfFiles': 20, 'numberOfSubjects': 10, 'variableMeasured': ['PlaneSegmentation', 'ElectrodeGroup', 'ProcessingModule', 'ElectricalSeries', 'TwoPhotonSeries', 'Units'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'two-photon microscopy technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000223 has 20 NWB files.
20 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeries_raw (ElectricalSeries) Raw acquired data
  Dataset /acquisition/ElectricalSeries_raw/electrodes (DynamicTableRegion) electrode_table_region | shape = (964,) | dtype = int64
  Group /acquisition/TwoPhotonSeries (TwoPhotonSeries) no description
  Group /acquisition/TwoPhotonSeries/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeries/imaging_plane/channel_0 (OpticalChannel) 
  Group /acquisition/TwoPhotonSeries/imaging_plane/device (Device) Mea1k HD-MEA device with 26'400 electrodes. 1024 recorded simultaneously.
  file_create_date: ['2022-02-16T22:19:57.630589+01:00']
  Group /general/devices/Mea1k HD-MEA (Device) Mea1k HD-MEA device with 26'400 electrodes. 1024 recorded simultaneously.
  Group /general/devices/Nikon NiE upright confocal microscope (Device) Nikon NiE upright microscope equipped with Yokogawa W1 spinning disk scan head, an Andor iXon Ultra EMCCD camera (Oxford Instruments), and 40x/0.80 NA or 60x/1.00 NA water-objectives (Nikon)
  experiment_description: Recording of network-wide extracellular activity with HD-MEA and simultaneous super-resolution calcium imaging to extract single spine responses
  experimenter: ['Xiaohan Xue']
  Group /general/extracellular_ephys/0 (ElectrodeGroup) no description
  Group /general/extracellular_ephys/0/device (Device) Mea1k HD-MEA device with 26'400 electrodes. 1024 recorded simultaneously.
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/electrode (VectorData) electrode | shape = (964,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (964,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/gain_to_uV (VectorData) gain_to_uV | shape = (964,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (964,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (964,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (964,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (964,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (964,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/rel_x (VectorData) the x coordinate within the electrode group | shape = (964,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_y (VectorData) the y coordinate within the electrode group | shape = (964,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (964,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (964,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (964,) | dtype = float64
  institution: ETH Zurich
  lab: Bio Engineering Laboratory (BEL) - Department of Bio Systems Science and Engineeering (D-BSSE)
  Group /general/optophysiology/ImagingPlane (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane/channel_0 (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane/device (Device) Mea1k HD-MEA device with 26'400 electrodes. 1024 recorded simultaneously.
  Group /general/subject (Subject) 
  identifier: rec8_chip2282
  Group /processing/ophys (ProcessingModule) contains optical physiology processed data
  Group /processing/ophys/Fluorescence (Fluorescence) 
  Group /processing/ophys/Fluorescence/Dff (RoiResponseSeries) no description
  Dataset /processing/ophys/Fluorescence/Dff/rois (DynamicTableRegion) region for Imaging plane0 | shape = (2,) | dtype = int64
  Group /processing/ophys/Fluorescence/RoiResponseSeries (RoiResponseSeries) no description
  Dataset /processing/ophys/Fluorescence/RoiResponseSeries/rois (DynamicTableRegion) region for Imaging plane0 | shape = (2,) | dtype = int64
  Group /processing/ophys/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation (PlaneSegmentation) Segmented ROIs
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/Accepted (VectorData) 1 if ROi was accepted or 0 if rejected as a cell during segmentation operation | shape = (2,) | dtype = int64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/Rejected (VectorData) 1 if ROi was rejected or 0 if accepted as a cell during segmentation operation | shape = (2,) | dtype = int64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/RoiCentroid (VectorData) x,y location of centroid of the roi in image_mask | shape = (2, 2) | dtype = int64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/id (ElementIdentifiers)  | shape = (2,) | dtype = int64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/image_mask (VectorData) image masks | shape = (2, 512, 512) | dtype = bool
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/channel_0 (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/device (Device) Mea1k HD-MEA device with 26'400 electrodes. 1024 recorded simultaneously.
  session_description: Simultaneous Ca2+ imaging-HD MEA recording to map monosynaptic connections.
  session_start_time: 2019-09-14T14:54:58+02:00
  timestamps_reference_time: 2019-09-14T14:54:58+02:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/id (ElementIdentifiers)  | shape = (159,) | dtype = int64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (139365,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (159,) | dtype = uint32
