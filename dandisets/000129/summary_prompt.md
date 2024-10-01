
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000129/draft
name: MC_RTT: macaque motor cortex spiking activity during self-paced reaching
contributor: [{'name': 'Pei, Felix', 'email': 'felp8484@gmail.com', 'roleName': ['dcite:ContactPerson', 'dcite:Maintainer'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': False}, {'name': "O'Doherty, Joseph", 'roleName': ['dcite:Author', 'dcite:DataCollector'], 'schemaKey': 'Person', 'identifier': '0000-0001-8175-5699', 'affiliation': [{'name': 'University of California, San Francisco', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/043mz5j54'}], 'includeInCitation': True}]
description: This dataset contains sorted unit spiking times and behavioral data from a macaque performing a self-paced reaching task. In the experimental task, the subject reached between targets randomly selected from an 8x8 grid without gaps or pre-movement delay intervals. Neural activity was recorded from an electrode array implanted in the primary motor cortex. Finger position, cursor position, and target position were also recorded during the experiment. Provided as part of the Neural Latents Benchmark: https://neurallatents.github.io.
assetsSummary: {'species': [{'name': 'Rhesus monkey', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9544'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 50965512, 'numberOfFiles': 2, 'numberOfSubjects': 1, 'variableMeasured': ['Units', 'ElectrodeGroup', 'ProcessingModule'], 'measurementTechnique': [{'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000129 has 2 NWB files.
1 of these NWB files are of type 1.
1 of these NWB files are of type 2.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2021-09-01T22:06:54.478701-04:00']
  Group /general/devices/electrode_array (Device) 96-electrode Utah array
  experiment_description: Self-paced reaches to targets arranged in a grid without gaps or pre-movement delay intervals
  experimenter: ["Joseph E. O'Doherty"]
  Group /general/extracellular_ephys/electrode_group (ElectrodeGroup) Implanted electrodes in Utah Array
  Group /general/extracellular_ephys/electrode_group/device (Device) 96-electrode Utah array
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (96,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (96,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (96,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (96,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (96,) | dtype = float64
  institution: University of California, San Francisco
  keywords: ['motor cortex' 'reaching' 'macaque' 'Neural Latents Benchmark']
  lab: Sabes
  related_publications: ['https://doi.org/10.1088/1741-2552/aa9e95']
  session_id: 20170202_02
  Group /general/subject (Subject) 
  identifier: 71d867ae-0b92-11ec-96df-0db753c69267
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (272,) | dtype = int64
  Dataset /intervals/trials/split (VectorData) Trial split that the trial belongs to for the Neural Latents Benchmark. Can be "train", "val", "test", or "none" | shape = (272,) | dtype = object
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (272,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (272,) | dtype = float64
  session_description: Data from monkey Indy performing self-paced random target reaching task. This file contains segments of trials from the full session on 2017-02-02 that are to be used for evaluating models for the Neural Latents Benchmark.
  session_start_time: 2017-02-02T00:00:00-08:00
  timestamps_reference_time: 2017-02-02T00:00:00-08:00
  Group /units (Units) data on spiking units
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (98,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex) Index for VectorData 'electrodes' | shape = (98,) | dtype = uint8
  Dataset /units/heldout (VectorData) Whether the unit is held out in the test data (True) or not (False) in the Neural Latents Benchmark | shape = (98,) | dtype = bool
  Dataset /units/id (ElementIdentifiers)  | shape = (98,) | dtype = int64
  Dataset /units/obs_intervals (VectorData) the observation intervals for each unit | shape = (26656, 2) | dtype = float64
  Dataset /units/obs_intervals_index (VectorIndex) Index for VectorData 'obs_intervals' | shape = (98,) | dtype = uint16
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (66548,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (98,) | dtype = uint32


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2021-09-01T22:06:51.827229-04:00']
  Group /general/devices/electrode_array (Device) 96-electrode Utah array
  experiment_description: Self-paced reaches to targets arranged in a grid without gaps or pre-movement delay intervals
  experimenter: ["Joseph E. O'Doherty"]
  Group /general/extracellular_ephys/electrode_group (ElectrodeGroup) Implanted electrodes in Utah Array
  Group /general/extracellular_ephys/electrode_group/device (Device) 96-electrode Utah array
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (96,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (96,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (96,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (96,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (96,) | dtype = float64
  institution: University of California, San Francisco
  keywords: ['motor cortex' 'reaching' 'macaque' 'Neural Latents Benchmark']
  lab: Sabes
  related_publications: ['https://doi.org/10.1088/1741-2552/aa9e95']
  session_id: 20170202_02
  Group /general/subject (Subject) 
  identifier: 7043e134-0b92-11ec-96df-0db753c69267
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (1080,) | dtype = int64
  Dataset /intervals/trials/split (VectorData) Trial split that the trial belongs to for the Neural Latents Benchmark. Can be "train", "val", "test", or "none" | shape = (1080,) | dtype = object
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (1080,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1080,) | dtype = float64
  Group /processing/behavior (ProcessingModule) Processed behavioral data
  Group /processing/behavior/cursor_pos (SpatialSeries) The position of the cursor in Cartesian coordinates (x, y) in mm. Recorded at 250 Hz and upsampled to 1 kHz
  Group /processing/behavior/finger_pos (SpatialSeries) The position of the working fingertip in Cartesian coordinates (x, y, z), as reported by the hand tracker in mm. Recorded at 250 Hz and upsampled to 1 kHz
  Group /processing/behavior/finger_vel (TimeSeries) The x and y velocity of the finger in mm/s. Calculated offline from upsampled finger position
  Group /processing/behavior/target_pos (SpatialSeries) The position of the target in Cartesian coordinates (x, y) in mm. Recorded at 250 Hz and upsampled to 1 kHz
  session_description: Data from monkey Indy performing self-paced random target reaching task. This file contains continuous segments of the full session on 2017-02-02 that can be used for training models for the Neural Latents Benchmark.
  session_start_time: 2017-02-02T00:00:00-08:00
  timestamps_reference_time: 2017-02-02T00:00:00-08:00
  Group /units (Units) data on spiking units
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (130,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex) Index for VectorData 'electrodes' | shape = (130,) | dtype = uint8
  Dataset /units/heldout (VectorData) Whether the unit is held out in the test data (True) or not (False) in the Neural Latents Benchmark | shape = (130,) | dtype = bool
  Dataset /units/id (ElementIdentifiers)  | shape = (130,) | dtype = int64
  Dataset /units/obs_intervals (VectorData) the observation intervals for each unit | shape = (520, 2) | dtype = float64
  Dataset /units/obs_intervals_index (VectorIndex) Index for VectorData 'obs_intervals' | shape = (130,) | dtype = uint16
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (339874,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (130,) | dtype = uint32
