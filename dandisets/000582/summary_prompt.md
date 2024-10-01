
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000582/draft
name: Conjunctive Representation of Position, Direction, and Velocity in Entorhinal Cortex
contributor: [{'name': 'Sargolini, Francesca', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-5038-3746', 'affiliation': [], 'includeInCitation': True}, {'name': 'Fyhn, Marianne', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Hafting, Torkel', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'McNaughton, Bruce L.', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Witter, Menno P.', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Moser, May-Britt', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Moser, Edvard I.', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Waade, Haagen', 'email': 'haagen.waade@ntnu.no', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0003-4675-2569', 'affiliation': [], 'includeInCitation': True}, {'name': 'Ball, Simon', 'email': 'simon.ball@ntnu.no', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}]
description: The dataset includes spike times for recorded grid cells from the medial entorhinal cortex (MEC) in rats that explored two-dimensional environments. The behavioral data includes position from the tracking LEDs. 

This sample was published in Sargolini et al. (Science, 2006).

Grid cells in the medial entorhinal cortex (MEC) are part of an environment-independent spatial coordinate system. To determine how information about location, direction, and distance is integrated in the grid-cell network, we recorded from each principal cell layer of MEC in rats that explored two-dimensional environments. Whereas layer II was predominated by grid cells, grid cells colocalized with head-direction cells and conjunctive grid x head-direction cells in the deeper layers. All cell types were modulated by running speed. The conjunction of positional, directional, and translational information in a single MEC cell type may enable grid coordinates to be updated during self-motion-based navigation.

assetsSummary: {'species': [{'name': 'Rattus norvegicus - Norway rat', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10116'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}, {'name': 'behavioral approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 1812381475, 'numberOfFiles': 115, 'numberOfSubjects': 14, 'variableMeasured': ['ElectricalSeries', 'Position', 'Units', 'ElectrodeGroup', 'ProcessingModule', 'LFP', 'SpatialSeries'], 'measurementTechnique': [{'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'signal filtering technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000582 has 100 NWB files.
47 of these NWB files are of type 1.
53 of these NWB files are of type 2.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeries (ElectricalSeries) The EEG signals from one electrode amplified 8000-10000 times, lowpass-filtered at 500 Hz (single pole), and stored at 4800 Hz (16 bits/sample).
  Dataset /acquisition/ElectricalSeries/electrodes (DynamicTableRegion) all electrodes | shape = (1,) | dtype = int64
  file_create_date: ['2023-09-16T15:50:09.775622+02:00']
  Group /general/devices/EEG (Device) The device used to record EEG signals.
  experiment_description: The sample includes conjunctive cells and head direction cells from layers III and V of medial entorhinal cortex and have been published in Sargolini et al. (Science, 2006).
  experimenter: ['Sargolini, Francesca']
  Group /general/extracellular_ephys/ElectrodeGroup (ElectrodeGroup) The name of the ElectrodeGroup this electrode is a part of.
  Group /general/extracellular_ephys/ElectrodeGroup/device (Device) The device used to record EEG signals.
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (1,) | dtype = object
  institution: Centre for the Biology of Memory, Norwegian University of Science and Technology
  keywords: ['medial entorhinal cortex' 'spike times' 'position']
  lab: Moser
  related_publications: ['https://doi.org/10.1126/science.1125572']
  session_id: 17010302
  Group /general/subject (Subject) 
  identifier: 294b7de1-a624-44d8-b1a1-28028dd2cf0c
  Group /processing/behavior (ProcessingModule) Processed behavioral data.
  Group /processing/behavior/Position (Position) 
  Group /processing/behavior/Position/SpatialSeriesLED1 (SpatialSeries) Position (x, y) for the first tracking LED.
  Group /processing/ecephys (ProcessingModule) Processed electrical series data.
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/ElectricalSeriesLFP (ElectricalSeries) The EEG signals from one electrode stored at 250 Hz.
  Dataset /processing/ecephys/LFP/ElectricalSeriesLFP/electrodes (DynamicTableRegion) all electrodes | shape = (1,) | dtype = int64
  session_description: This session includes spike and position times for recorded cells from a Long Evans rat that was running in a 1 x 1 meter enclosure. The cells were recorded in the dorsocaudal 25% portion of the medial entorhinal cortex (MEC).Position is given for two LEDs to enable calculation of head direction.
  session_start_time: 1900-01-01T00:00:00+01:00
  timestamps_reference_time: 1900-01-01T00:00:00+01:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/depth (VectorData) Indicates the depth of the inserted electrodes in meters. | shape = (8,) | dtype = float64
  Dataset /units/hemisphere (VectorData) Indicates which hemisphere the electrodes were inserted above MEC. | shape = (8,) | dtype = object
  Dataset /units/histology (VectorData) The layer of MEC of the grid cell. | shape = (8,) | dtype = object
  Dataset /units/id (ElementIdentifiers)  | shape = (8,) | dtype = int64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (9087,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (8,) | dtype = uint16
  Dataset /units/unit_name (VectorData) The identifier of the cell, based on tetrode number and cell number. | shape = (8,) | dtype = object


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeries (ElectricalSeries) The EEG signals from one electrode amplified 8000-10000 times, lowpass-filtered at 500 Hz (single pole), and stored at 4800 Hz (16 bits/sample).
  Dataset /acquisition/ElectricalSeries/electrodes (DynamicTableRegion) all electrodes | shape = (1,) | dtype = int64
  file_create_date: ['2023-09-16T15:50:58.446493+02:00']
  Group /general/devices/EEG (Device) The device used to record EEG signals.
  experiment_description: The sample includes conjunctive cells and head direction cells from layers III and V of medial entorhinal cortex and have been published in Sargolini et al. (Science, 2006).
  experimenter: ['Sargolini, Francesca']
  Group /general/extracellular_ephys/ElectrodeGroup (ElectrodeGroup) The name of the ElectrodeGroup this electrode is a part of.
  Group /general/extracellular_ephys/ElectrodeGroup/device (Device) The device used to record EEG signals.
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (1,) | dtype = object
  institution: Centre for the Biology of Memory, Norwegian University of Science and Technology
  keywords: ['medial entorhinal cortex' 'spike times' 'position']
  lab: Moser
  related_publications: ['https://doi.org/10.1126/science.1125572']
  session_id: 01060511
  Group /general/subject (Subject) 
  identifier: c4d6df29-834e-48ef-bb08-a155390faa26
  Group /processing/behavior (ProcessingModule) Processed behavioral data.
  Group /processing/behavior/Position (Position) 
  Group /processing/behavior/Position/SpatialSeriesLED1 (SpatialSeries) Position (x, y) for the first tracking LED.
  Group /processing/behavior/Position/SpatialSeriesLED2 (SpatialSeries) Position (x, y) for the second tracking LED.
  Group /processing/ecephys (ProcessingModule) Processed electrical series data.
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/ElectricalSeriesLFP (ElectricalSeries) The EEG signals from one electrode stored at 250 Hz.
  Dataset /processing/ecephys/LFP/ElectricalSeriesLFP/electrodes (DynamicTableRegion) all electrodes | shape = (1,) | dtype = int64
  session_description: This session includes spike and position times for recorded cells from a Long Evans rat that was running in a 1 x 1 meter enclosure. The cells were recorded in the dorsocaudal 25% portion of the medial entorhinal cortex (MEC).Position is given for two LEDs to enable calculation of head direction.
  session_start_time: 1900-01-01T00:00:00+01:00
  timestamps_reference_time: 1900-01-01T00:00:00+01:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/depth (VectorData) Indicates the depth of the inserted electrodes in meters. | shape = (3,) | dtype = float64
  Dataset /units/hemisphere (VectorData) Indicates which hemisphere the electrodes were inserted above MEC. | shape = (3,) | dtype = object
  Dataset /units/histology (VectorData) The layer of MEC of the grid cell. | shape = (3,) | dtype = object
  Dataset /units/id (ElementIdentifiers)  | shape = (3,) | dtype = int64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (5072,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (3,) | dtype = uint16
  Dataset /units/unit_name (VectorData) The identifier of the cell, based on tetrode number and cell number. | shape = (3,) | dtype = object
