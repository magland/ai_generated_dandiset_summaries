
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001201/draft
name: LINK: Long-Term Intracortical Neural Activity and Kinematics
contributor: [{'name': 'Temmar, Hisham', 'email': 'htemmar@umich.edu', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}]
description: This dataset contains multiunit threshold crossings, spiking band power, and behavioral data from a macaque performing a self-paced finger movement task, across 6 experimental sessions spanning 2.5 years. The dataset may be useful in evaluating the stability of decoding algorithms across long time frames.

96 channels of neural activity was recorded from Utah microelectrode arrays implanted in the motor cortex (M1). The positions & velocities of the index finger and middle-ring-small fingers were recorded using a manipulandum, where positions were normalized between full flexion and full extension. The experimental task was to move the two finger groups to acquire targets cued on a screen. 

Each day has 375 trials of center-out targets (trials alternating between the targets at a non-center location and then both targets at center), and 375 trials of random targets (target position for each finger chosen randomly at each trial, with a maximum flexion difference between fingers of 50%).

Example code with an interactive GUI to visualize the data: https://github.com/chesteklab/monkey-dataset-sfn-2024
Further details on the experimental setup can be found in Nason et al. 2021, Neuron  (DOI: 10.1016/j.neuron.2021.08.009)
assetsSummary: {'species': [{'name': 'Macaca mulatta - Rhesus monkey', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9544'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 274731808, 'numberOfFiles': 7, 'numberOfSubjects': 2, 'variableMeasured': ['ProcessingModule', 'ElectrodeGroup'], 'measurementTechnique': [{'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 001201 has 12 NWB files.
12 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2024-10-01T18:17:50.965684+00:00']
  Group /general/devices/Utah Array (Device) 96-electrode Utah array
  experiment_description: Behavioral and neural data from Utah Array recordings from a macaque doing finger movements
  experimenter: ['Chestek Lab']
  Group /general/extracellular_ephys/Utah Array (ElectrodeGroup) Utah Array electrode group
  Group /general/extracellular_ephys/Utah Array/device (Device) 96-electrode Utah array
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering, including the filter name and frequency cutoffs | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (96,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (96,) | dtype = object
  institution: University of Michigan
  keywords: ['neural decoding' 'finger movements' 'motor cortex']
  lab: Chestek Lab
  Group /general/subject (Subject) 
  identifier: 2021-10-15_CO_nwb
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (375,) | dtype = int32
  Dataset /intervals/trials/index_target_position (VectorData) Index target position | shape = (375,) | dtype = float64
  Dataset /intervals/trials/mrp_target_position (VectorData) MRP target position | shape = (375,) | dtype = float64
  Dataset /intervals/trials/run_id (VectorData) Run ID | shape = (375,) | dtype = int64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (375,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (375,) | dtype = float64
  Dataset /intervals/trials/target_style (VectorData) Target style (CO or RD) | shape = (375,) | dtype = object
  Dataset /intervals/trials/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (2250,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/trials/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (375,) | dtype = uint16
  Dataset /intervals/trials/trial_count (VectorData) Trial count | shape = (375,) | dtype = int64
  Dataset /intervals/trials/trial_number (VectorData) Trial number | shape = (375,) | dtype = int64
  Group /processing/behavior (ProcessingModule) Processed behavioral data
  Group /processing/behavior/index_position (TimeSeries) Index flexion position, from fully extended (0) to fully flexed (1)
  Group /processing/behavior/index_velocity (TimeSeries) Velocity of index flexion
  Group /processing/behavior/mrp_position (TimeSeries) Middle-ring-pinky flexion position, from fully extended (0) to fully flexed (1)
  Group /processing/behavior/mrp_velocity (TimeSeries) Velocity of middle-ring-pinky flexion
  Group /processing/ecephys (ProcessingModule) Binned (20ms) and processed neural data
  Group /processing/ecephys/SpikingBandPower (TimeSeries) Spiking Band Power across time
  Group /processing/ecephys/ThresholdCrossings (TimeSeries) Threshold crossings across time
  session_description: Neural and behavioral data for target style CO
  session_start_time: 2021-10-15T00:00:00+00:00
  timestamps_reference_time: 2021-10-15T00:00:00+00:00
