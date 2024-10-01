
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000410/draft
name: Joshi et al (2023) Dynamic Synchronization between Hippocampal Spatial Representations and the Stepping Rhythm
contributor: [{'name': 'Joshi, Abhilasha', 'email': 'ajoshineuro@gmail.com', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}]
description: This dateset includes electrophysiological data from from dorsal CA1 of rats running on a linear or w-shaped track. Please contact Abhilasha Joshi or Loren Frank for more information about this data. 
assetsSummary: {'species': [{'name': 'Rattus norvegicus - Norway rat', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10116'}], 'approach': [{'name': 'behavioral approach', 'schemaKey': 'ApproachType'}, {'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 2802041975041, 'numberOfFiles': 22, 'numberOfSubjects': 5, 'variableMeasured': ['SpatialSeries', 'ProcessingModule', 'Position', 'BehavioralEvents', 'ElectricalSeries'], 'measurementTechnique': [{'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000410 has 19 NWB files.
4 of these NWB files are of type 1.
12 of these NWB files are of type 2.
1 of these NWB files are of type 3.
1 of these NWB files are of type 4.
1 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/e-series (ElectricalSeries) Recording of extracellular voltage
  Dataset /acquisition/e-series/electrodes (DynamicTableRegion) - | shape = (128,) | dtype = int64
  file_create_date: ['2022-12-03T19:40:09.062036-08:00']
  Group /general/devices/camera_device 0 (CameraDevice) 
  Group /general/devices/camera_device 1 (CameraDevice) 
  Group /general/devices/dataacq_device0 (DataAcqDevice) 
  Group /general/devices/header_device (HeaderDevice) 
  Group /general/devices/probe 0 (Probe) 
  Group /general/devices/probe 0/0 (Shank) 
  Group /general/devices/probe 0/0/0 (ShanksElectrode) 
  Group /general/devices/probe 0/0/1 (ShanksElectrode) 
  Group /general/devices/probe 0/0/2 (ShanksElectrode) 
  Group /general/devices/probe 0/0/3 (ShanksElectrode) 
  experiment_description: Theta and gait
  experimenter: ['Joshi, Abhilasha']
  Group /general/extracellular_ephys/0 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/0/device (Probe) 
  Group /general/extracellular_ephys/0/device/0 (Shank) 
  Group /general/extracellular_ephys/0/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/0/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/0/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/0/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/1 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/1/device (Probe) 
  Group /general/extracellular_ephys/1/device/0 (Shank) 
  Group /general/extracellular_ephys/1/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/1/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/1/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/1/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/10 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/10/device (Probe) 
  Group /general/extracellular_ephys/10/device/0 (Shank) 
  Group /general/extracellular_ephys/10/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/10/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/10/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/10/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/11 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/11/device (Probe) 
  Group /general/extracellular_ephys/11/device/0 (Shank) 
  Group /general/extracellular_ephys/11/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/11/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/11/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/11/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/12 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/12/device (Probe) 
  Group /general/extracellular_ephys/12/device/0 (Shank) 
  Group /general/extracellular_ephys/12/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/12/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/12/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/12/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/13 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/13/device (Probe) 
  Group /general/extracellular_ephys/13/device/0 (Shank) 
  Group /general/extracellular_ephys/13/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/13/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/13/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/13/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/14 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/14/device (Probe) 
  Group /general/extracellular_ephys/14/device/0 (Shank) 
  Group /general/extracellular_ephys/14/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/14/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/14/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/14/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/15 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/15/device (Probe) 
  Group /general/extracellular_ephys/15/device/0 (Shank) 
  Group /general/extracellular_ephys/15/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/15/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/15/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/15/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/16 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/16/device (Probe) 
  Group /general/extracellular_ephys/16/device/0 (Shank) 
  Group /general/extracellular_ephys/16/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/16/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/16/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/16/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/17 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/17/device (Probe) 
  Group /general/extracellular_ephys/17/device/0 (Shank) 
  Group /general/extracellular_ephys/17/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/17/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/17/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/17/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/18 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/18/device (Probe) 
  Group /general/extracellular_ephys/18/device/0 (Shank) 
  Group /general/extracellular_ephys/18/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/18/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/18/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/18/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/19 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/19/device (Probe) 
  Group /general/extracellular_ephys/19/device/0 (Shank) 
  Group /general/extracellular_ephys/19/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/19/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/19/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/19/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/2 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/2/device (Probe) 
  Group /general/extracellular_ephys/2/device/0 (Shank) 
  Group /general/extracellular_ephys/2/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/2/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/2/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/2/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/20 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/20/device (Probe) 
  Group /general/extracellular_ephys/20/device/0 (Shank) 
  Group /general/extracellular_ephys/20/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/20/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/20/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/20/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/21 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/21/device (Probe) 
  Group /general/extracellular_ephys/21/device/0 (Shank) 
  Group /general/extracellular_ephys/21/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/21/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/21/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/21/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/22 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/22/device (Probe) 
  Group /general/extracellular_ephys/22/device/0 (Shank) 
  Group /general/extracellular_ephys/22/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/22/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/22/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/22/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/23 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/23/device (Probe) 
  Group /general/extracellular_ephys/23/device/0 (Shank) 
  Group /general/extracellular_ephys/23/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/23/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/23/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/23/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/24 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/24/device (Probe) 
  Group /general/extracellular_ephys/24/device/0 (Shank) 
  Group /general/extracellular_ephys/24/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/24/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/24/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/24/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/25 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/25/device (Probe) 
  Group /general/extracellular_ephys/25/device/0 (Shank) 
  Group /general/extracellular_ephys/25/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/25/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/25/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/25/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/26 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/26/device (Probe) 
  Group /general/extracellular_ephys/26/device/0 (Shank) 
  Group /general/extracellular_ephys/26/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/26/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/26/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/26/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/27 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/27/device (Probe) 
  Group /general/extracellular_ephys/27/device/0 (Shank) 
  Group /general/extracellular_ephys/27/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/27/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/27/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/27/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/28 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/28/device (Probe) 
  Group /general/extracellular_ephys/28/device/0 (Shank) 
  Group /general/extracellular_ephys/28/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/28/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/28/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/28/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/29 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/29/device (Probe) 
  Group /general/extracellular_ephys/29/device/0 (Shank) 
  Group /general/extracellular_ephys/29/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/29/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/29/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/29/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/3 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/3/device (Probe) 
  Group /general/extracellular_ephys/3/device/0 (Shank) 
  Group /general/extracellular_ephys/3/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/3/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/3/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/3/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/30 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/30/device (Probe) 
  Group /general/extracellular_ephys/30/device/0 (Shank) 
  Group /general/extracellular_ephys/30/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/30/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/30/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/30/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/31 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/31/device (Probe) 
  Group /general/extracellular_ephys/31/device/0 (Shank) 
  Group /general/extracellular_ephys/31/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/31/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/31/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/31/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/4 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/4/device (Probe) 
  Group /general/extracellular_ephys/4/device/0 (Shank) 
  Group /general/extracellular_ephys/4/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/4/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/4/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/4/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/5 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/5/device (Probe) 
  Group /general/extracellular_ephys/5/device/0 (Shank) 
  Group /general/extracellular_ephys/5/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/5/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/5/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/5/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/6 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/6/device (Probe) 
  Group /general/extracellular_ephys/6/device/0 (Shank) 
  Group /general/extracellular_ephys/6/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/6/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/6/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/6/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/7 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/7/device (Probe) 
  Group /general/extracellular_ephys/7/device/0 (Shank) 
  Group /general/extracellular_ephys/7/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/7/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/7/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/7/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/8 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/8/device (Probe) 
  Group /general/extracellular_ephys/8/device/0 (Shank) 
  Group /general/extracellular_ephys/8/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/8/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/8/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/8/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/9 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/9/device (Probe) 
  Group /general/extracellular_ephys/9/device/0 (Shank) 
  Group /general/extracellular_ephys/9/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/9/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/9/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/9/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/bad_channel (VectorData) True if noisy or disconnected | shape = (128,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/channel_id (VectorData) None | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/hwChan (VectorData) SpikeGadgets Hardware channel | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/ntrode_id (VectorData) Experimenter defined ID for this probe | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/probe_electrode (VectorData) the number of this electrode with respect to the probe | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/probe_shank (VectorData) The shank of the probe this channel is located on | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/ref_elect_id (VectorData) “Experimenter selected reference electrode id” | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/rel_x (VectorData) None | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_y (VectorData) None | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_z (VectorData) None | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (128,) | dtype = float64
  institution: University of California, San Francisco
  lab: Loren Frank
  session_id: jaq_01
  Group /general/subject (Subject) 
  identifier: 59ab4f50-7385-11ed-9616-5b730c2cfb9f
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (7,) | dtype = int64
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (7,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (7,) | dtype = float64
  Dataset /intervals/epochs/tags (VectorData) user-defined tags | shape = (7,) | dtype = object
  Dataset /intervals/epochs/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (7,) | dtype = uint8
  Group /processing/analog (ProcessingModule) Contains all analog data
  Group /processing/analog/analog (BehavioralEvents) 
  Group /processing/analog/analog/analog (TimeSeries) MagY   GyroX   AccelZ   MagX   GyroY   GyroZ   timestamps   AccelY   AccelX   MagZ   
  Group /processing/associated_files (ProcessingModule) Contains all associated files data
  Group /processing/associated_files/statescript_r1 (AssociatedFiles) state script log run 1
  Group /processing/associated_files/statescript_r2 (AssociatedFiles) state script log run 2
  Group /processing/associated_files/statescript_r3 (AssociatedFiles) state script log run 3
  Group /processing/behavior (ProcessingModule) Contains all behavior-related data
  Group /processing/behavior/behavioral_events (BehavioralEvents) 
  Group /processing/behavior/behavioral_events/Poke2 (TimeSeries) Din2
  Group /processing/behavior/position (Position) 
  Group /processing/behavior/position/series_0 (SpatialSeries) video_frame_ind
  Group /processing/behavior/position/series_1 (SpatialSeries) video_frame_ind
  Group /processing/behavior/position/series_2 (SpatialSeries) video_frame_ind
  Group /processing/behavior/position/series_3 (SpatialSeries) video_frame_ind
  Group /processing/behavior/position/series_4 (SpatialSeries) video_frame_ind
  Group /processing/behavior/position/series_5 (SpatialSeries) video_frame_ind
  Group /processing/behavior/position/series_6 (SpatialSeries) video_frame_ind
  Group /processing/sample_count (ProcessingModule) corespondence between sample count and timestamps
  Group /processing/sample_count/sample_count (TimeSeries) acquisition system sample count
  Group /processing/tasks (ProcessingModule) Contains all tasks information
  Group /processing/tasks/task_0 (DynamicTable) 
  Dataset /processing/tasks/task_0/camera_id (VectorData) the ID number of the camera used for video | shape = (1, 1) | dtype = int64
  Dataset /processing/tasks/task_0/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /processing/tasks/task_0/task_description (VectorData) a description of the task | shape = (1,) | dtype = object
  Dataset /processing/tasks/task_0/task_environment (VectorData) the environment in which the animal performed the task | shape = (1,) | dtype = object
  Dataset /processing/tasks/task_0/task_epochs (VectorData) the temporal epochs where the animal was exposed to this task | shape = (1, 4) | dtype = int64
  Dataset /processing/tasks/task_0/task_name (VectorData) the name of the task | shape = (1,) | dtype = object
  Group /processing/tasks/task_1 (DynamicTable) 
  Dataset /processing/tasks/task_1/camera_id (VectorData) the ID number of the camera used for video | shape = (1, 1) | dtype = int64
  Dataset /processing/tasks/task_1/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /processing/tasks/task_1/task_description (VectorData) a description of the task | shape = (1,) | dtype = object
  Dataset /processing/tasks/task_1/task_environment (VectorData) the environment in which the animal performed the task | shape = (1,) | dtype = object
  Dataset /processing/tasks/task_1/task_epochs (VectorData) the temporal epochs where the animal was exposed to this task | shape = (1, 3) | dtype = int64
  Dataset /processing/tasks/task_1/task_name (VectorData) the name of the task | shape = (1,) | dtype = object
  session_description: Theta and gait
  session_start_time: 2019-08-26T16:53:46.625000-07:00
  timestamps_reference_time: 1970-01-01T00:00:00+00:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/e-series (ElectricalSeries) Recording of extracellular voltage
  Dataset /acquisition/e-series/electrodes (DynamicTableRegion) - | shape = (128,) | dtype = int64
  file_create_date: ['2022-12-04T02:51:01.402590-08:00']
  Group /general/devices/camera_device 0 (CameraDevice) 
  Group /general/devices/camera_device 1 (CameraDevice) 
  Group /general/devices/dataacq_device0 (DataAcqDevice) 
  Group /general/devices/header_device (HeaderDevice) 
  Group /general/devices/probe 0 (Probe) 
  Group /general/devices/probe 0/0 (Shank) 
  Group /general/devices/probe 0/0/0 (ShanksElectrode) 
  Group /general/devices/probe 0/0/1 (ShanksElectrode) 
  Group /general/devices/probe 0/0/2 (ShanksElectrode) 
  Group /general/devices/probe 0/0/3 (ShanksElectrode) 
  experiment_description: Theta and gait
  experimenter: ['Joshi, Abhilasha']
  Group /general/extracellular_ephys/0 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/0/device (Probe) 
  Group /general/extracellular_ephys/0/device/0 (Shank) 
  Group /general/extracellular_ephys/0/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/0/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/0/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/0/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/1 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/1/device (Probe) 
  Group /general/extracellular_ephys/1/device/0 (Shank) 
  Group /general/extracellular_ephys/1/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/1/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/1/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/1/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/10 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/10/device (Probe) 
  Group /general/extracellular_ephys/10/device/0 (Shank) 
  Group /general/extracellular_ephys/10/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/10/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/10/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/10/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/11 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/11/device (Probe) 
  Group /general/extracellular_ephys/11/device/0 (Shank) 
  Group /general/extracellular_ephys/11/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/11/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/11/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/11/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/12 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/12/device (Probe) 
  Group /general/extracellular_ephys/12/device/0 (Shank) 
  Group /general/extracellular_ephys/12/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/12/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/12/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/12/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/13 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/13/device (Probe) 
  Group /general/extracellular_ephys/13/device/0 (Shank) 
  Group /general/extracellular_ephys/13/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/13/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/13/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/13/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/14 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/14/device (Probe) 
  Group /general/extracellular_ephys/14/device/0 (Shank) 
  Group /general/extracellular_ephys/14/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/14/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/14/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/14/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/15 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/15/device (Probe) 
  Group /general/extracellular_ephys/15/device/0 (Shank) 
  Group /general/extracellular_ephys/15/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/15/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/15/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/15/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/16 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/16/device (Probe) 
  Group /general/extracellular_ephys/16/device/0 (Shank) 
  Group /general/extracellular_ephys/16/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/16/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/16/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/16/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/17 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/17/device (Probe) 
  Group /general/extracellular_ephys/17/device/0 (Shank) 
  Group /general/extracellular_ephys/17/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/17/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/17/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/17/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/18 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/18/device (Probe) 
  Group /general/extracellular_ephys/18/device/0 (Shank) 
  Group /general/extracellular_ephys/18/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/18/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/18/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/18/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/19 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/19/device (Probe) 
  Group /general/extracellular_ephys/19/device/0 (Shank) 
  Group /general/extracellular_ephys/19/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/19/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/19/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/19/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/2 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/2/device (Probe) 
  Group /general/extracellular_ephys/2/device/0 (Shank) 
  Group /general/extracellular_ephys/2/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/2/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/2/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/2/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/20 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/20/device (Probe) 
  Group /general/extracellular_ephys/20/device/0 (Shank) 
  Group /general/extracellular_ephys/20/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/20/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/20/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/20/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/21 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/21/device (Probe) 
  Group /general/extracellular_ephys/21/device/0 (Shank) 
  Group /general/extracellular_ephys/21/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/21/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/21/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/21/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/22 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/22/device (Probe) 
  Group /general/extracellular_ephys/22/device/0 (Shank) 
  Group /general/extracellular_ephys/22/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/22/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/22/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/22/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/23 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/23/device (Probe) 
  Group /general/extracellular_ephys/23/device/0 (Shank) 
  Group /general/extracellular_ephys/23/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/23/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/23/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/23/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/24 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/24/device (Probe) 
  Group /general/extracellular_ephys/24/device/0 (Shank) 
  Group /general/extracellular_ephys/24/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/24/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/24/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/24/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/25 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/25/device (Probe) 
  Group /general/extracellular_ephys/25/device/0 (Shank) 
  Group /general/extracellular_ephys/25/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/25/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/25/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/25/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/26 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/26/device (Probe) 
  Group /general/extracellular_ephys/26/device/0 (Shank) 
  Group /general/extracellular_ephys/26/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/26/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/26/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/26/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/27 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/27/device (Probe) 
  Group /general/extracellular_ephys/27/device/0 (Shank) 
  Group /general/extracellular_ephys/27/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/27/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/27/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/27/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/28 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/28/device (Probe) 
  Group /general/extracellular_ephys/28/device/0 (Shank) 
  Group /general/extracellular_ephys/28/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/28/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/28/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/28/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/29 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/29/device (Probe) 
  Group /general/extracellular_ephys/29/device/0 (Shank) 
  Group /general/extracellular_ephys/29/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/29/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/29/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/29/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/3 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/3/device (Probe) 
  Group /general/extracellular_ephys/3/device/0 (Shank) 
  Group /general/extracellular_ephys/3/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/3/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/3/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/3/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/30 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/30/device (Probe) 
  Group /general/extracellular_ephys/30/device/0 (Shank) 
  Group /general/extracellular_ephys/30/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/30/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/30/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/30/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/31 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/31/device (Probe) 
  Group /general/extracellular_ephys/31/device/0 (Shank) 
  Group /general/extracellular_ephys/31/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/31/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/31/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/31/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/4 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/4/device (Probe) 
  Group /general/extracellular_ephys/4/device/0 (Shank) 
  Group /general/extracellular_ephys/4/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/4/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/4/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/4/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/5 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/5/device (Probe) 
  Group /general/extracellular_ephys/5/device/0 (Shank) 
  Group /general/extracellular_ephys/5/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/5/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/5/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/5/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/6 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/6/device (Probe) 
  Group /general/extracellular_ephys/6/device/0 (Shank) 
  Group /general/extracellular_ephys/6/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/6/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/6/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/6/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/7 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/7/device (Probe) 
  Group /general/extracellular_ephys/7/device/0 (Shank) 
  Group /general/extracellular_ephys/7/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/7/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/7/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/7/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/8 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/8/device (Probe) 
  Group /general/extracellular_ephys/8/device/0 (Shank) 
  Group /general/extracellular_ephys/8/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/8/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/8/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/8/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/9 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/9/device (Probe) 
  Group /general/extracellular_ephys/9/device/0 (Shank) 
  Group /general/extracellular_ephys/9/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/9/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/9/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/9/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/bad_channel (VectorData) True if noisy or disconnected | shape = (128,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/channel_id (VectorData) None | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/hwChan (VectorData) SpikeGadgets Hardware channel | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/ntrode_id (VectorData) Experimenter defined ID for this probe | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/probe_electrode (VectorData) the number of this electrode with respect to the probe | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/probe_shank (VectorData) The shank of the probe this channel is located on | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/ref_elect_id (VectorData) “Experimenter selected reference electrode id” | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/rel_x (VectorData) None | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_y (VectorData) None | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_z (VectorData) None | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (128,) | dtype = float64
  institution: University of California, San Francisco
  lab: Loren Frank
  session_id: jaq_02
  Group /general/subject (Subject) 
  identifier: 8add9a74-73c1-11ed-9616-5b730c2cfb9f
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (9,) | dtype = int64
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (9,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (9,) | dtype = float64
  Dataset /intervals/epochs/tags (VectorData) user-defined tags | shape = (9,) | dtype = object
  Dataset /intervals/epochs/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (9,) | dtype = uint8
  Group /processing/analog (ProcessingModule) Contains all analog data
  Group /processing/analog/analog (BehavioralEvents) 
  Group /processing/analog/analog/analog (TimeSeries) MagZ   GyroY   timestamps   AccelZ   AccelX   AccelY   MagX   GyroZ   MagY   GyroX   
  Group /processing/associated_files (ProcessingModule) Contains all associated files data
  Group /processing/associated_files/statescript_r1 (AssociatedFiles) state script log run 1
  Group /processing/associated_files/statescript_r2 (AssociatedFiles) state script log run 2
  Group /processing/associated_files/statescript_r3 (AssociatedFiles) state script log run 3
  Group /processing/associated_files/statescript_r4 (AssociatedFiles) state script log run 4
  Group /processing/behavior (ProcessingModule) Contains all behavior-related data
  Group /processing/behavior/behavioral_events (BehavioralEvents) 
  Group /processing/behavior/behavioral_events/Poke2 (TimeSeries) Din2
  Group /processing/behavior/position (Position) 
  Group /processing/behavior/position/series_0 (SpatialSeries) video_frame_ind
  Group /processing/behavior/position/series_1 (SpatialSeries) video_frame_ind
  Group /processing/behavior/position/series_2 (SpatialSeries) video_frame_ind
  Group /processing/behavior/position/series_3 (SpatialSeries) video_frame_ind
  Group /processing/behavior/position/series_4 (SpatialSeries) video_frame_ind
  Group /processing/behavior/position/series_5 (SpatialSeries) video_frame_ind
  Group /processing/behavior/position/series_6 (SpatialSeries) video_frame_ind
  Group /processing/behavior/position/series_7 (SpatialSeries) video_frame_ind
  Group /processing/behavior/position/series_8 (SpatialSeries) video_frame_ind
  Group /processing/sample_count (ProcessingModule) corespondence between sample count and timestamps
  Group /processing/sample_count/sample_count (TimeSeries) acquisition system sample count
  Group /processing/tasks (ProcessingModule) Contains all tasks information
  Group /processing/tasks/task_0 (DynamicTable) 
  Dataset /processing/tasks/task_0/camera_id (VectorData) the ID number of the camera used for video | shape = (1, 1) | dtype = int64
  Dataset /processing/tasks/task_0/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /processing/tasks/task_0/task_description (VectorData) a description of the task | shape = (1,) | dtype = object
  Dataset /processing/tasks/task_0/task_environment (VectorData) the environment in which the animal performed the task | shape = (1,) | dtype = object
  Dataset /processing/tasks/task_0/task_epochs (VectorData) the temporal epochs where the animal was exposed to this task | shape = (1, 5) | dtype = int64
  Dataset /processing/tasks/task_0/task_name (VectorData) the name of the task | shape = (1,) | dtype = object
  Group /processing/tasks/task_1 (DynamicTable) 
  Dataset /processing/tasks/task_1/camera_id (VectorData) the ID number of the camera used for video | shape = (1, 1) | dtype = int64
  Dataset /processing/tasks/task_1/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /processing/tasks/task_1/task_description (VectorData) a description of the task | shape = (1,) | dtype = object
  Dataset /processing/tasks/task_1/task_environment (VectorData) the environment in which the animal performed the task | shape = (1,) | dtype = object
  Dataset /processing/tasks/task_1/task_epochs (VectorData) the temporal epochs where the animal was exposed to this task | shape = (1, 4) | dtype = int64
  Dataset /processing/tasks/task_1/task_name (VectorData) the name of the task | shape = (1,) | dtype = object
  session_description: Theta and gait
  session_start_time: 2019-08-27T13:48:12.916000-07:00
  timestamps_reference_time: 1970-01-01T00:00:00+00:00


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/e-series (ElectricalSeries) Recording of extracellular voltage
  Dataset /acquisition/e-series/electrodes (DynamicTableRegion) - | shape = (128,) | dtype = int64
  file_create_date: ['2023-01-09T21:47:48.148548-08:00']
  Group /general/devices/camera_device 0 (CameraDevice) 
  Group /general/devices/camera_device 1 (CameraDevice) 
  Group /general/devices/dataacq_device0 (DataAcqDevice) 
  Group /general/devices/header_device (HeaderDevice) 
  Group /general/devices/probe 0 (Probe) 
  Group /general/devices/probe 0/0 (Shank) 
  Group /general/devices/probe 0/0/0 (ShanksElectrode) 
  Group /general/devices/probe 0/0/1 (ShanksElectrode) 
  Group /general/devices/probe 0/0/2 (ShanksElectrode) 
  Group /general/devices/probe 0/0/3 (ShanksElectrode) 
  experiment_description: Theta and gait
  experimenter: ['Joshi, Abhilasha']
  Group /general/extracellular_ephys/0 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/0/device (Probe) 
  Group /general/extracellular_ephys/0/device/0 (Shank) 
  Group /general/extracellular_ephys/0/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/0/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/0/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/0/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/1 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/1/device (Probe) 
  Group /general/extracellular_ephys/1/device/0 (Shank) 
  Group /general/extracellular_ephys/1/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/1/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/1/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/1/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/10 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/10/device (Probe) 
  Group /general/extracellular_ephys/10/device/0 (Shank) 
  Group /general/extracellular_ephys/10/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/10/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/10/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/10/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/11 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/11/device (Probe) 
  Group /general/extracellular_ephys/11/device/0 (Shank) 
  Group /general/extracellular_ephys/11/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/11/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/11/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/11/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/12 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/12/device (Probe) 
  Group /general/extracellular_ephys/12/device/0 (Shank) 
  Group /general/extracellular_ephys/12/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/12/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/12/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/12/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/13 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/13/device (Probe) 
  Group /general/extracellular_ephys/13/device/0 (Shank) 
  Group /general/extracellular_ephys/13/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/13/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/13/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/13/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/14 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/14/device (Probe) 
  Group /general/extracellular_ephys/14/device/0 (Shank) 
  Group /general/extracellular_ephys/14/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/14/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/14/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/14/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/15 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/15/device (Probe) 
  Group /general/extracellular_ephys/15/device/0 (Shank) 
  Group /general/extracellular_ephys/15/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/15/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/15/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/15/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/16 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/16/device (Probe) 
  Group /general/extracellular_ephys/16/device/0 (Shank) 
  Group /general/extracellular_ephys/16/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/16/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/16/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/16/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/17 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/17/device (Probe) 
  Group /general/extracellular_ephys/17/device/0 (Shank) 
  Group /general/extracellular_ephys/17/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/17/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/17/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/17/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/18 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/18/device (Probe) 
  Group /general/extracellular_ephys/18/device/0 (Shank) 
  Group /general/extracellular_ephys/18/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/18/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/18/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/18/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/19 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/19/device (Probe) 
  Group /general/extracellular_ephys/19/device/0 (Shank) 
  Group /general/extracellular_ephys/19/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/19/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/19/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/19/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/2 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/2/device (Probe) 
  Group /general/extracellular_ephys/2/device/0 (Shank) 
  Group /general/extracellular_ephys/2/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/2/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/2/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/2/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/20 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/20/device (Probe) 
  Group /general/extracellular_ephys/20/device/0 (Shank) 
  Group /general/extracellular_ephys/20/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/20/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/20/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/20/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/21 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/21/device (Probe) 
  Group /general/extracellular_ephys/21/device/0 (Shank) 
  Group /general/extracellular_ephys/21/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/21/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/21/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/21/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/22 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/22/device (Probe) 
  Group /general/extracellular_ephys/22/device/0 (Shank) 
  Group /general/extracellular_ephys/22/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/22/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/22/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/22/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/23 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/23/device (Probe) 
  Group /general/extracellular_ephys/23/device/0 (Shank) 
  Group /general/extracellular_ephys/23/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/23/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/23/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/23/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/24 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/24/device (Probe) 
  Group /general/extracellular_ephys/24/device/0 (Shank) 
  Group /general/extracellular_ephys/24/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/24/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/24/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/24/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/25 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/25/device (Probe) 
  Group /general/extracellular_ephys/25/device/0 (Shank) 
  Group /general/extracellular_ephys/25/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/25/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/25/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/25/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/26 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/26/device (Probe) 
  Group /general/extracellular_ephys/26/device/0 (Shank) 
  Group /general/extracellular_ephys/26/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/26/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/26/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/26/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/27 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/27/device (Probe) 
  Group /general/extracellular_ephys/27/device/0 (Shank) 
  Group /general/extracellular_ephys/27/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/27/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/27/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/27/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/28 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/28/device (Probe) 
  Group /general/extracellular_ephys/28/device/0 (Shank) 
  Group /general/extracellular_ephys/28/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/28/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/28/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/28/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/29 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/29/device (Probe) 
  Group /general/extracellular_ephys/29/device/0 (Shank) 
  Group /general/extracellular_ephys/29/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/29/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/29/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/29/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/3 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/3/device (Probe) 
  Group /general/extracellular_ephys/3/device/0 (Shank) 
  Group /general/extracellular_ephys/3/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/3/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/3/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/3/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/30 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/30/device (Probe) 
  Group /general/extracellular_ephys/30/device/0 (Shank) 
  Group /general/extracellular_ephys/30/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/30/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/30/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/30/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/31 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/31/device (Probe) 
  Group /general/extracellular_ephys/31/device/0 (Shank) 
  Group /general/extracellular_ephys/31/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/31/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/31/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/31/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/4 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/4/device (Probe) 
  Group /general/extracellular_ephys/4/device/0 (Shank) 
  Group /general/extracellular_ephys/4/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/4/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/4/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/4/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/5 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/5/device (Probe) 
  Group /general/extracellular_ephys/5/device/0 (Shank) 
  Group /general/extracellular_ephys/5/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/5/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/5/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/5/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/6 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/6/device (Probe) 
  Group /general/extracellular_ephys/6/device/0 (Shank) 
  Group /general/extracellular_ephys/6/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/6/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/6/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/6/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/7 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/7/device (Probe) 
  Group /general/extracellular_ephys/7/device/0 (Shank) 
  Group /general/extracellular_ephys/7/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/7/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/7/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/7/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/8 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/8/device (Probe) 
  Group /general/extracellular_ephys/8/device/0 (Shank) 
  Group /general/extracellular_ephys/8/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/8/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/8/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/8/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/9 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/9/device (Probe) 
  Group /general/extracellular_ephys/9/device/0 (Shank) 
  Group /general/extracellular_ephys/9/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/9/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/9/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/9/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/bad_channel (VectorData) True if noisy or disconnected | shape = (128,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/channel_id (VectorData) None | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/hwChan (VectorData) SpikeGadgets Hardware channel | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/ntrode_id (VectorData) Experimenter defined ID for this probe | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/probe_electrode (VectorData) the number of this electrode with respect to the probe | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/probe_shank (VectorData) The shank of the probe this channel is located on | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/ref_elect_id (VectorData) “Experimenter selected reference electrode id” | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/rel_x (VectorData) None | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_y (VectorData) None | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_z (VectorData) None | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (128,) | dtype = float64
  institution: University of California, San Francisco
  lab: Loren Frank
  session_id: jaq_03
  Group /general/subject (Subject) 
  identifier: 501ffd18-90aa-11ed-9616-5b730c2cfb9f
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (16,) | dtype = int64
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (16,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (16,) | dtype = float64
  Dataset /intervals/epochs/tags (VectorData) user-defined tags | shape = (16,) | dtype = object
  Dataset /intervals/epochs/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (16,) | dtype = uint8
  Group /processing/analog (ProcessingModule) Contains all analog data
  Group /processing/analog/analog (BehavioralEvents) 
  Group /processing/analog/analog/analog (TimeSeries) GyroX   GyroZ   AccelZ   AccelY   MagX   GyroY   MagZ   timestamps   MagY   AccelX   
  Group /processing/associated_files (ProcessingModule) Contains all associated files data
  Group /processing/associated_files/statescript_r1 (AssociatedFiles) state script log run 1
  Group /processing/associated_files/statescript_r2 (AssociatedFiles) state script log run 2
  Group /processing/associated_files/statescript_r3 (AssociatedFiles) state script log run 3
  Group /processing/associated_files/statescript_r4 (AssociatedFiles) state script log run 4
  Group /processing/associated_files/statescript_r5 (AssociatedFiles) state script log run 5
  Group /processing/associated_files/statescript_r6 (AssociatedFiles) state script log run 6
  Group /processing/associated_files/statescript_r7 (AssociatedFiles) state script log run 7
  Group /processing/associated_files/statescript_r8 (AssociatedFiles) state script log run 8
  Group /processing/behavior (ProcessingModule) Contains all behavior-related data
  Group /processing/behavior/behavioral_events (BehavioralEvents) 
  Group /processing/behavior/behavioral_events/Poke2 (TimeSeries) Din2
  Group /processing/behavior/position (Position) 
  Group /processing/behavior/position/series_0 (SpatialSeries) video_frame_ind
  Group /processing/behavior/position/series_1 (SpatialSeries) video_frame_ind
  Group /processing/behavior/position/series_10 (SpatialSeries) video_frame_ind
  Group /processing/behavior/position/series_11 (SpatialSeries) video_frame_ind
  Group /processing/behavior/position/series_12 (SpatialSeries) video_frame_ind
  Group /processing/behavior/position/series_13 (SpatialSeries) video_frame_ind
  Group /processing/behavior/position/series_14 (SpatialSeries) video_frame_ind
  Group /processing/behavior/position/series_15 (SpatialSeries) video_frame_ind
  Group /processing/behavior/position/series_2 (SpatialSeries) video_frame_ind
  Group /processing/behavior/position/series_3 (SpatialSeries) video_frame_ind
  Group /processing/behavior/position/series_4 (SpatialSeries) video_frame_ind
  Group /processing/behavior/position/series_5 (SpatialSeries) video_frame_ind
  Group /processing/behavior/position/series_6 (SpatialSeries) video_frame_ind
  Group /processing/behavior/position/series_7 (SpatialSeries) video_frame_ind
  Group /processing/behavior/position/series_8 (SpatialSeries) video_frame_ind
  Group /processing/behavior/position/series_9 (SpatialSeries) video_frame_ind
  Group /processing/sample_count (ProcessingModule) corespondence between sample count and timestamps
  Group /processing/sample_count/sample_count (TimeSeries) acquisition system sample count
  Group /processing/tasks (ProcessingModule) Contains all tasks information
  Group /processing/tasks/task_0 (DynamicTable) 
  Dataset /processing/tasks/task_0/camera_id (VectorData) the ID number of the camera used for video | shape = (1, 1) | dtype = int64
  Dataset /processing/tasks/task_0/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /processing/tasks/task_0/task_description (VectorData) a description of the task | shape = (1,) | dtype = object
  Dataset /processing/tasks/task_0/task_environment (VectorData) the environment in which the animal performed the task | shape = (1,) | dtype = object
  Dataset /processing/tasks/task_0/task_epochs (VectorData) the temporal epochs where the animal was exposed to this task | shape = (1, 8) | dtype = int64
  Dataset /processing/tasks/task_0/task_name (VectorData) the name of the task | shape = (1,) | dtype = object
  Group /processing/tasks/task_1 (DynamicTable) 
  Dataset /processing/tasks/task_1/camera_id (VectorData) the ID number of the camera used for video | shape = (1, 1) | dtype = int64
  Dataset /processing/tasks/task_1/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /processing/tasks/task_1/task_description (VectorData) a description of the task | shape = (1,) | dtype = object
  Dataset /processing/tasks/task_1/task_environment (VectorData) the environment in which the animal performed the task | shape = (1,) | dtype = object
  Dataset /processing/tasks/task_1/task_epochs (VectorData) the temporal epochs where the animal was exposed to this task | shape = (1, 8) | dtype = int64
  Dataset /processing/tasks/task_1/task_name (VectorData) the name of the task | shape = (1,) | dtype = object
  session_description: Theta and gait
  session_start_time: 2019-08-29T09:40:14.566000-07:00
  timestamps_reference_time: 1970-01-01T00:00:00+00:00


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/e-series (ElectricalSeries) Recording of extracellular voltage
  Dataset /acquisition/e-series/electrodes (DynamicTableRegion) - | shape = (128,) | dtype = int64
  file_create_date: ['2023-01-10T18:03:43.835694-08:00']
  Group /general/devices/camera_device 0 (CameraDevice) 
  Group /general/devices/camera_device 1 (CameraDevice) 
  Group /general/devices/dataacq_device0 (DataAcqDevice) 
  Group /general/devices/header_device (HeaderDevice) 
  Group /general/devices/probe 0 (Probe) 
  Group /general/devices/probe 0/0 (Shank) 
  Group /general/devices/probe 0/0/0 (ShanksElectrode) 
  Group /general/devices/probe 0/0/1 (ShanksElectrode) 
  Group /general/devices/probe 0/0/2 (ShanksElectrode) 
  Group /general/devices/probe 0/0/3 (ShanksElectrode) 
  experiment_description: Theta and gait
  experimenter: ['Joshi, Abhilasha']
  Group /general/extracellular_ephys/0 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/0/device (Probe) 
  Group /general/extracellular_ephys/0/device/0 (Shank) 
  Group /general/extracellular_ephys/0/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/0/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/0/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/0/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/1 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/1/device (Probe) 
  Group /general/extracellular_ephys/1/device/0 (Shank) 
  Group /general/extracellular_ephys/1/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/1/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/1/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/1/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/10 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/10/device (Probe) 
  Group /general/extracellular_ephys/10/device/0 (Shank) 
  Group /general/extracellular_ephys/10/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/10/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/10/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/10/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/11 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/11/device (Probe) 
  Group /general/extracellular_ephys/11/device/0 (Shank) 
  Group /general/extracellular_ephys/11/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/11/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/11/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/11/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/12 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/12/device (Probe) 
  Group /general/extracellular_ephys/12/device/0 (Shank) 
  Group /general/extracellular_ephys/12/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/12/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/12/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/12/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/13 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/13/device (Probe) 
  Group /general/extracellular_ephys/13/device/0 (Shank) 
  Group /general/extracellular_ephys/13/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/13/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/13/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/13/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/14 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/14/device (Probe) 
  Group /general/extracellular_ephys/14/device/0 (Shank) 
  Group /general/extracellular_ephys/14/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/14/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/14/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/14/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/15 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/15/device (Probe) 
  Group /general/extracellular_ephys/15/device/0 (Shank) 
  Group /general/extracellular_ephys/15/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/15/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/15/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/15/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/16 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/16/device (Probe) 
  Group /general/extracellular_ephys/16/device/0 (Shank) 
  Group /general/extracellular_ephys/16/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/16/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/16/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/16/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/17 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/17/device (Probe) 
  Group /general/extracellular_ephys/17/device/0 (Shank) 
  Group /general/extracellular_ephys/17/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/17/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/17/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/17/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/18 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/18/device (Probe) 
  Group /general/extracellular_ephys/18/device/0 (Shank) 
  Group /general/extracellular_ephys/18/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/18/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/18/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/18/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/19 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/19/device (Probe) 
  Group /general/extracellular_ephys/19/device/0 (Shank) 
  Group /general/extracellular_ephys/19/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/19/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/19/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/19/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/2 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/2/device (Probe) 
  Group /general/extracellular_ephys/2/device/0 (Shank) 
  Group /general/extracellular_ephys/2/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/2/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/2/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/2/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/20 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/20/device (Probe) 
  Group /general/extracellular_ephys/20/device/0 (Shank) 
  Group /general/extracellular_ephys/20/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/20/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/20/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/20/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/21 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/21/device (Probe) 
  Group /general/extracellular_ephys/21/device/0 (Shank) 
  Group /general/extracellular_ephys/21/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/21/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/21/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/21/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/22 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/22/device (Probe) 
  Group /general/extracellular_ephys/22/device/0 (Shank) 
  Group /general/extracellular_ephys/22/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/22/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/22/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/22/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/23 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/23/device (Probe) 
  Group /general/extracellular_ephys/23/device/0 (Shank) 
  Group /general/extracellular_ephys/23/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/23/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/23/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/23/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/24 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/24/device (Probe) 
  Group /general/extracellular_ephys/24/device/0 (Shank) 
  Group /general/extracellular_ephys/24/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/24/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/24/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/24/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/25 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/25/device (Probe) 
  Group /general/extracellular_ephys/25/device/0 (Shank) 
  Group /general/extracellular_ephys/25/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/25/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/25/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/25/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/26 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/26/device (Probe) 
  Group /general/extracellular_ephys/26/device/0 (Shank) 
  Group /general/extracellular_ephys/26/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/26/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/26/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/26/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/27 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/27/device (Probe) 
  Group /general/extracellular_ephys/27/device/0 (Shank) 
  Group /general/extracellular_ephys/27/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/27/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/27/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/27/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/28 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/28/device (Probe) 
  Group /general/extracellular_ephys/28/device/0 (Shank) 
  Group /general/extracellular_ephys/28/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/28/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/28/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/28/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/29 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/29/device (Probe) 
  Group /general/extracellular_ephys/29/device/0 (Shank) 
  Group /general/extracellular_ephys/29/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/29/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/29/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/29/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/3 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/3/device (Probe) 
  Group /general/extracellular_ephys/3/device/0 (Shank) 
  Group /general/extracellular_ephys/3/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/3/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/3/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/3/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/30 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/30/device (Probe) 
  Group /general/extracellular_ephys/30/device/0 (Shank) 
  Group /general/extracellular_ephys/30/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/30/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/30/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/30/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/31 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/31/device (Probe) 
  Group /general/extracellular_ephys/31/device/0 (Shank) 
  Group /general/extracellular_ephys/31/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/31/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/31/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/31/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/4 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/4/device (Probe) 
  Group /general/extracellular_ephys/4/device/0 (Shank) 
  Group /general/extracellular_ephys/4/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/4/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/4/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/4/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/5 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/5/device (Probe) 
  Group /general/extracellular_ephys/5/device/0 (Shank) 
  Group /general/extracellular_ephys/5/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/5/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/5/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/5/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/6 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/6/device (Probe) 
  Group /general/extracellular_ephys/6/device/0 (Shank) 
  Group /general/extracellular_ephys/6/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/6/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/6/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/6/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/7 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/7/device (Probe) 
  Group /general/extracellular_ephys/7/device/0 (Shank) 
  Group /general/extracellular_ephys/7/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/7/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/7/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/7/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/8 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/8/device (Probe) 
  Group /general/extracellular_ephys/8/device/0 (Shank) 
  Group /general/extracellular_ephys/8/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/8/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/8/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/8/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/9 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/9/device (Probe) 
  Group /general/extracellular_ephys/9/device/0 (Shank) 
  Group /general/extracellular_ephys/9/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/9/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/9/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/9/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/bad_channel (VectorData) True if noisy or disconnected | shape = (128,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/channel_id (VectorData) None | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/hwChan (VectorData) SpikeGadgets Hardware channel | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/ntrode_id (VectorData) Experimenter defined ID for this probe | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/probe_electrode (VectorData) the number of this electrode with respect to the probe | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/probe_shank (VectorData) The shank of the probe this channel is located on | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/ref_elect_id (VectorData) “Experimenter selected reference electrode id” | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/rel_x (VectorData) None | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_y (VectorData) None | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_z (VectorData) None | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (128,) | dtype = float64
  institution: University of California, San Francisco
  lab: Loren Frank
  session_id: Monty_03
  Group /general/subject (Subject) 
  identifier: 2d1a693e-9154-11ed-8c0d-8716c0a62e3c
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (19,) | dtype = int64
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (19,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (19,) | dtype = float64
  Dataset /intervals/epochs/tags (VectorData) user-defined tags | shape = (19,) | dtype = object
  Dataset /intervals/epochs/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (19,) | dtype = uint8
  Group /processing/analog (ProcessingModule) Contains all analog data
  Group /processing/analog/analog (BehavioralEvents) 
  Group /processing/analog/analog/analog (TimeSeries) GyroZ   AccelZ   MagZ   MagY   AccelY   timestamps   AccelX   GyroX   MagX   GyroY   
  Group /processing/associated_files (ProcessingModule) Contains all associated files data
  Group /processing/associated_files/statescript_r1 (AssociatedFiles) state script log run 1
  Group /processing/associated_files/statescript_r2 (AssociatedFiles) state script log run 2
  Group /processing/associated_files/statescript_r3 (AssociatedFiles) state script log run 3
  Group /processing/associated_files/statescript_r4 (AssociatedFiles) state script log run 4
  Group /processing/associated_files/statescript_r5 (AssociatedFiles) state script log run 5
  Group /processing/associated_files/statescript_r6 (AssociatedFiles) state script log run 6
  Group /processing/associated_files/statescript_r7 (AssociatedFiles) state script log run 7
  Group /processing/associated_files/statescript_r8 (AssociatedFiles) state script log run 8
  Group /processing/associated_files/statescript_r9 (AssociatedFiles) state script log run 9
  Group /processing/behavior (ProcessingModule) Contains all behavior-related data
  Group /processing/behavior/behavioral_events (BehavioralEvents) 
  Group /processing/behavior/behavioral_events/Poke2 (TimeSeries) Din2
  Group /processing/behavior/position (Position) 
  Group /processing/behavior/position/series_0 (SpatialSeries) video_frame_ind
  Group /processing/behavior/position/series_1 (SpatialSeries) video_frame_ind
  Group /processing/behavior/position/series_10 (SpatialSeries) video_frame_ind
  Group /processing/behavior/position/series_11 (SpatialSeries) video_frame_ind
  Group /processing/behavior/position/series_12 (SpatialSeries) video_frame_ind
  Group /processing/behavior/position/series_13 (SpatialSeries) video_frame_ind
  Group /processing/behavior/position/series_14 (SpatialSeries) video_frame_ind
  Group /processing/behavior/position/series_15 (SpatialSeries) video_frame_ind
  Group /processing/behavior/position/series_16 (SpatialSeries) video_frame_ind
  Group /processing/behavior/position/series_17 (SpatialSeries) video_frame_ind
  Group /processing/behavior/position/series_18 (SpatialSeries) video_frame_ind
  Group /processing/behavior/position/series_2 (SpatialSeries) video_frame_ind
  Group /processing/behavior/position/series_3 (SpatialSeries) video_frame_ind
  Group /processing/behavior/position/series_4 (SpatialSeries) video_frame_ind
  Group /processing/behavior/position/series_5 (SpatialSeries) video_frame_ind
  Group /processing/behavior/position/series_6 (SpatialSeries) video_frame_ind
  Group /processing/behavior/position/series_7 (SpatialSeries) video_frame_ind
  Group /processing/behavior/position/series_8 (SpatialSeries) video_frame_ind
  Group /processing/behavior/position/series_9 (SpatialSeries) video_frame_ind
  Group /processing/sample_count (ProcessingModule) corespondence between sample count and timestamps
  Group /processing/sample_count/sample_count (TimeSeries) acquisition system sample count
  Group /processing/tasks (ProcessingModule) Contains all tasks information
  Group /processing/tasks/task_0 (DynamicTable) 
  Dataset /processing/tasks/task_0/camera_id (VectorData) the ID number of the camera used for video | shape = (1, 1) | dtype = int64
  Dataset /processing/tasks/task_0/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /processing/tasks/task_0/task_description (VectorData) a description of the task | shape = (1,) | dtype = object
  Dataset /processing/tasks/task_0/task_environment (VectorData) the environment in which the animal performed the task | shape = (1,) | dtype = object
  Dataset /processing/tasks/task_0/task_epochs (VectorData) the temporal epochs where the animal was exposed to this task | shape = (1, 10) | dtype = int64
  Dataset /processing/tasks/task_0/task_name (VectorData) the name of the task | shape = (1,) | dtype = object
  Group /processing/tasks/task_1 (DynamicTable) 
  Dataset /processing/tasks/task_1/camera_id (VectorData) the ID number of the camera used for video | shape = (1, 1) | dtype = int64
  Dataset /processing/tasks/task_1/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /processing/tasks/task_1/task_description (VectorData) a description of the task | shape = (1,) | dtype = object
  Dataset /processing/tasks/task_1/task_environment (VectorData) the environment in which the animal performed the task | shape = (1,) | dtype = object
  Dataset /processing/tasks/task_1/task_epochs (VectorData) the temporal epochs where the animal was exposed to this task | shape = (1, 9) | dtype = int64
  Dataset /processing/tasks/task_1/task_name (VectorData) the name of the task | shape = (1,) | dtype = object
  session_description: Theta and gait
  session_start_time: 2020-09-15T09:12:15.581000-07:00
  timestamps_reference_time: 1970-01-01T00:00:00+00:00


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  Group /acquisition/e-series (ElectricalSeries) Recording of extracellular voltage
  Dataset /acquisition/e-series/electrodes (DynamicTableRegion) - | shape = (128,) | dtype = int64
  file_create_date: ['2023-01-10T12:00:59.510085-08:00']
  Group /general/devices/camera_device 0 (CameraDevice) 
  Group /general/devices/camera_device 1 (CameraDevice) 
  Group /general/devices/dataacq_device0 (DataAcqDevice) 
  Group /general/devices/header_device (HeaderDevice) 
  Group /general/devices/probe 0 (Probe) 
  Group /general/devices/probe 0/0 (Shank) 
  Group /general/devices/probe 0/0/0 (ShanksElectrode) 
  Group /general/devices/probe 0/0/1 (ShanksElectrode) 
  Group /general/devices/probe 0/0/2 (ShanksElectrode) 
  Group /general/devices/probe 0/0/3 (ShanksElectrode) 
  experiment_description: Theta and gait
  experimenter: ['Joshi, Abhilasha']
  Group /general/extracellular_ephys/0 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/0/device (Probe) 
  Group /general/extracellular_ephys/0/device/0 (Shank) 
  Group /general/extracellular_ephys/0/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/0/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/0/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/0/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/1 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/1/device (Probe) 
  Group /general/extracellular_ephys/1/device/0 (Shank) 
  Group /general/extracellular_ephys/1/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/1/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/1/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/1/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/10 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/10/device (Probe) 
  Group /general/extracellular_ephys/10/device/0 (Shank) 
  Group /general/extracellular_ephys/10/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/10/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/10/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/10/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/11 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/11/device (Probe) 
  Group /general/extracellular_ephys/11/device/0 (Shank) 
  Group /general/extracellular_ephys/11/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/11/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/11/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/11/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/12 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/12/device (Probe) 
  Group /general/extracellular_ephys/12/device/0 (Shank) 
  Group /general/extracellular_ephys/12/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/12/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/12/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/12/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/13 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/13/device (Probe) 
  Group /general/extracellular_ephys/13/device/0 (Shank) 
  Group /general/extracellular_ephys/13/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/13/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/13/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/13/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/14 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/14/device (Probe) 
  Group /general/extracellular_ephys/14/device/0 (Shank) 
  Group /general/extracellular_ephys/14/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/14/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/14/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/14/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/15 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/15/device (Probe) 
  Group /general/extracellular_ephys/15/device/0 (Shank) 
  Group /general/extracellular_ephys/15/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/15/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/15/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/15/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/16 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/16/device (Probe) 
  Group /general/extracellular_ephys/16/device/0 (Shank) 
  Group /general/extracellular_ephys/16/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/16/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/16/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/16/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/17 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/17/device (Probe) 
  Group /general/extracellular_ephys/17/device/0 (Shank) 
  Group /general/extracellular_ephys/17/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/17/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/17/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/17/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/18 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/18/device (Probe) 
  Group /general/extracellular_ephys/18/device/0 (Shank) 
  Group /general/extracellular_ephys/18/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/18/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/18/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/18/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/19 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/19/device (Probe) 
  Group /general/extracellular_ephys/19/device/0 (Shank) 
  Group /general/extracellular_ephys/19/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/19/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/19/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/19/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/2 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/2/device (Probe) 
  Group /general/extracellular_ephys/2/device/0 (Shank) 
  Group /general/extracellular_ephys/2/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/2/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/2/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/2/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/20 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/20/device (Probe) 
  Group /general/extracellular_ephys/20/device/0 (Shank) 
  Group /general/extracellular_ephys/20/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/20/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/20/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/20/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/21 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/21/device (Probe) 
  Group /general/extracellular_ephys/21/device/0 (Shank) 
  Group /general/extracellular_ephys/21/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/21/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/21/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/21/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/22 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/22/device (Probe) 
  Group /general/extracellular_ephys/22/device/0 (Shank) 
  Group /general/extracellular_ephys/22/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/22/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/22/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/22/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/23 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/23/device (Probe) 
  Group /general/extracellular_ephys/23/device/0 (Shank) 
  Group /general/extracellular_ephys/23/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/23/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/23/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/23/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/24 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/24/device (Probe) 
  Group /general/extracellular_ephys/24/device/0 (Shank) 
  Group /general/extracellular_ephys/24/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/24/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/24/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/24/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/25 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/25/device (Probe) 
  Group /general/extracellular_ephys/25/device/0 (Shank) 
  Group /general/extracellular_ephys/25/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/25/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/25/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/25/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/26 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/26/device (Probe) 
  Group /general/extracellular_ephys/26/device/0 (Shank) 
  Group /general/extracellular_ephys/26/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/26/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/26/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/26/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/27 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/27/device (Probe) 
  Group /general/extracellular_ephys/27/device/0 (Shank) 
  Group /general/extracellular_ephys/27/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/27/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/27/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/27/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/28 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/28/device (Probe) 
  Group /general/extracellular_ephys/28/device/0 (Shank) 
  Group /general/extracellular_ephys/28/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/28/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/28/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/28/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/29 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/29/device (Probe) 
  Group /general/extracellular_ephys/29/device/0 (Shank) 
  Group /general/extracellular_ephys/29/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/29/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/29/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/29/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/3 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/3/device (Probe) 
  Group /general/extracellular_ephys/3/device/0 (Shank) 
  Group /general/extracellular_ephys/3/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/3/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/3/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/3/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/30 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/30/device (Probe) 
  Group /general/extracellular_ephys/30/device/0 (Shank) 
  Group /general/extracellular_ephys/30/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/30/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/30/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/30/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/31 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/31/device (Probe) 
  Group /general/extracellular_ephys/31/device/0 (Shank) 
  Group /general/extracellular_ephys/31/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/31/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/31/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/31/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/4 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/4/device (Probe) 
  Group /general/extracellular_ephys/4/device/0 (Shank) 
  Group /general/extracellular_ephys/4/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/4/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/4/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/4/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/5 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/5/device (Probe) 
  Group /general/extracellular_ephys/5/device/0 (Shank) 
  Group /general/extracellular_ephys/5/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/5/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/5/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/5/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/6 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/6/device (Probe) 
  Group /general/extracellular_ephys/6/device/0 (Shank) 
  Group /general/extracellular_ephys/6/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/6/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/6/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/6/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/7 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/7/device (Probe) 
  Group /general/extracellular_ephys/7/device/0 (Shank) 
  Group /general/extracellular_ephys/7/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/7/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/7/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/7/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/8 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/8/device (Probe) 
  Group /general/extracellular_ephys/8/device/0 (Shank) 
  Group /general/extracellular_ephys/8/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/8/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/8/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/8/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/9 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/9/device (Probe) 
  Group /general/extracellular_ephys/9/device/0 (Shank) 
  Group /general/extracellular_ephys/9/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/9/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/9/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/9/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/bad_channel (VectorData) True if noisy or disconnected | shape = (128,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/channel_id (VectorData) None | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/hwChan (VectorData) SpikeGadgets Hardware channel | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/ntrode_id (VectorData) Experimenter defined ID for this probe | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/probe_electrode (VectorData) the number of this electrode with respect to the probe | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/probe_shank (VectorData) The shank of the probe this channel is located on | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/ref_elect_id (VectorData) “Experimenter selected reference electrode id” | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/rel_x (VectorData) None | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_y (VectorData) None | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_z (VectorData) None | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (128,) | dtype = float64
  institution: University of California, San Francisco
  lab: Loren Frank
  session_id: Monty_04
  Group /general/subject (Subject) 
  identifier: 808dfa1e-9121-11ed-8c0d-8716c0a62e3c
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (11,) | dtype = int64
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (11,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (11,) | dtype = float64
  Dataset /intervals/epochs/tags (VectorData) user-defined tags | shape = (11,) | dtype = object
  Dataset /intervals/epochs/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (11,) | dtype = uint8
  Group /processing/analog (ProcessingModule) Contains all analog data
  Group /processing/analog/analog (BehavioralEvents) 
  Group /processing/analog/analog/analog (TimeSeries) AccelZ   GyroY   GyroX   MagX   timestamps   GyroZ   MagY   AccelX   MagZ   AccelY   
  Group /processing/associated_files (ProcessingModule) Contains all associated files data
  Group /processing/associated_files/statescript_r1 (AssociatedFiles) state script log run 1
  Group /processing/associated_files/statescript_r2 (AssociatedFiles) state script log run 2
  Group /processing/associated_files/statescript_r3 (AssociatedFiles) state script log run 3
  Group /processing/associated_files/statescript_r4 (AssociatedFiles) state script log run 4
  Group /processing/associated_files/statescript_r5 (AssociatedFiles) state script log run 5
  Group /processing/behavior (ProcessingModule) Contains all behavior-related data
  Group /processing/behavior/behavioral_events (BehavioralEvents) 
  Group /processing/behavior/behavioral_events/Poke2 (TimeSeries) Din2
  Group /processing/behavior/position (Position) 
  Group /processing/behavior/position/series_0 (SpatialSeries) video_frame_ind
  Group /processing/behavior/position/series_1 (SpatialSeries) video_frame_ind
  Group /processing/behavior/position/series_10 (SpatialSeries) video_frame_ind
  Group /processing/behavior/position/series_2 (SpatialSeries) video_frame_ind
  Group /processing/behavior/position/series_3 (SpatialSeries) video_frame_ind
  Group /processing/behavior/position/series_4 (SpatialSeries) video_frame_ind
  Group /processing/behavior/position/series_5 (SpatialSeries) video_frame_ind
  Group /processing/behavior/position/series_6 (SpatialSeries) video_frame_ind
  Group /processing/behavior/position/series_7 (SpatialSeries) video_frame_ind
  Group /processing/behavior/position/series_8 (SpatialSeries) video_frame_ind
  Group /processing/behavior/position/series_9 (SpatialSeries) video_frame_ind
  Group /processing/sample_count (ProcessingModule) corespondence between sample count and timestamps
  Group /processing/sample_count/sample_count (TimeSeries) acquisition system sample count
  Group /processing/tasks (ProcessingModule) Contains all tasks information
  Group /processing/tasks/task_0 (DynamicTable) 
  Dataset /processing/tasks/task_0/camera_id (VectorData) the ID number of the camera used for video | shape = (1, 1) | dtype = int64
  Dataset /processing/tasks/task_0/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /processing/tasks/task_0/task_description (VectorData) a description of the task | shape = (1,) | dtype = object
  Dataset /processing/tasks/task_0/task_environment (VectorData) the environment in which the animal performed the task | shape = (1,) | dtype = object
  Dataset /processing/tasks/task_0/task_epochs (VectorData) the temporal epochs where the animal was exposed to this task | shape = (1, 6) | dtype = int64
  Dataset /processing/tasks/task_0/task_name (VectorData) the name of the task | shape = (1,) | dtype = object
  Group /processing/tasks/task_1 (DynamicTable) 
  Dataset /processing/tasks/task_1/camera_id (VectorData) the ID number of the camera used for video | shape = (1, 1) | dtype = int64
  Dataset /processing/tasks/task_1/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /processing/tasks/task_1/task_description (VectorData) a description of the task | shape = (1,) | dtype = object
  Dataset /processing/tasks/task_1/task_environment (VectorData) the environment in which the animal performed the task | shape = (1,) | dtype = object
  Dataset /processing/tasks/task_1/task_epochs (VectorData) the temporal epochs where the animal was exposed to this task | shape = (1, 5) | dtype = int64
  Dataset /processing/tasks/task_1/task_name (VectorData) the name of the task | shape = (1,) | dtype = object
  session_description: Theta and gait
  session_start_time: 2020-09-16T15:19:54.372000-07:00
  timestamps_reference_time: 1970-01-01T00:00:00+00:00
