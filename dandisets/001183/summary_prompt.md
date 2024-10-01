
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001183/draft
name: Neural circuits for social modulation of a persistent negative emotional state
contributor: [{'name': 'National Institutes of Health (NIH)', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': '1 R01 NS 132912-01'}]
description: electrophysiological recording from neurons in medial preoptic area under chronic restrain stress
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 68032063, 'numberOfCells': 36, 'numberOfFiles': 37, 'numberOfSamples': 36, 'numberOfSubjects': 36, 'variableMeasured': [], 'measurementTechnique': []}

Dandiset 001183 has 38 NWB files.
38 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/izero-response-01-ch-0 (IZeroClampSeries) Response to: long_square
  Group /acquisition/izero-response-01-ch-0/electrode (IntracellularElectrode) 
  Group /acquisition/izero-response-01-ch-0/electrode/device (Device) no description
  file_create_date: ['2024-08-30T14:41:00.897006-07:00']
  Group /general/DandiIcephysMetadata (DandiIcephysMetadata) 
  Group /general/devices/DeviceIcephys (Device) no description
  experimenter: ['Catherine Tao']
  institution: USC
  Group /general/intracellular_ephys/electrode-0 (IntracellularElectrode) 
  Group /general/intracellular_ephys/electrode-0/device (Device) no description
  Group /general/intracellular_ephys/intracellular_recordings (IntracellularRecordingsTable) A table to group together a stimulus and response from a single electrode and a single simultaneous recording and for storing metadata about the intracellular recording.
  Group /general/intracellular_ephys/intracellular_recordings/electrodes (IntracellularElectrodesTable) Table for storing intracellular electrode related metadata.
  Dataset /general/intracellular_ephys/intracellular_recordings/electrodes/electrode (VectorData) Column for storing the reference to the intracellular electrode | shape = (1,) | dtype = object
  Dataset /general/intracellular_ephys/intracellular_recordings/electrodes/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Dataset /general/intracellular_ephys/intracellular_recordings/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /general/intracellular_ephys/intracellular_recordings/responses (IntracellularResponsesTable) Table for storing intracellular response related metadata.
  Dataset /general/intracellular_ephys/intracellular_recordings/responses/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Dataset /general/intracellular_ephys/intracellular_recordings/responses/response (TimeSeriesReferenceVectorData) Column storing the reference to the recorded response for the recording (rows) | shape = (1,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Group /general/intracellular_ephys/intracellular_recordings/stimuli (IntracellularStimuliTable) Table for storing intracellular stimulus related metadata.
  Dataset /general/intracellular_ephys/intracellular_recordings/stimuli/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Dataset /general/intracellular_ephys/intracellular_recordings/stimuli/stimulus (TimeSeriesReferenceVectorData) Column storing the reference to the recorded stimulus for the recording (rows) | shape = (1,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Group /general/intracellular_ephys/sequential_recordings (SequentialRecordingsTable) A table for grouping different intracellular recording simultaneous_recordings from the SimultaneousRecordingsTable table together. This is typically used to group together simultaneous_recordings where the a sequence of stimuli of the same type with varying parameters have been presented in a sequence.
  Dataset /general/intracellular_ephys/sequential_recordings/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Dataset /general/intracellular_ephys/sequential_recordings/simultaneous_recordings (DynamicTableRegion) Column with references to one or more rows in the SimultaneousRecordingsTable table | shape = (1,) | dtype = int32
  Dataset /general/intracellular_ephys/sequential_recordings/simultaneous_recordings_index (VectorIndex) Index for VectorData 'simultaneous_recordings' | shape = (1,) | dtype = uint8
  Dataset /general/intracellular_ephys/sequential_recordings/stimulus_type (VectorData) Column storing the type of stimulus used for the sequential recording | shape = (1,) | dtype = object
  Group /general/intracellular_ephys/simultaneous_recordings (SimultaneousRecordingsTable) A table for grouping different intracellular recordings from theIntracellularRecordingsTable table together that were recorded simultaneously from different electrodes.
  Dataset /general/intracellular_ephys/simultaneous_recordings/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Dataset /general/intracellular_ephys/simultaneous_recordings/recordings (DynamicTableRegion) Column with references to one or more rows in the IntracellularRecordingsTable table | shape = (1,) | dtype = int32
  Dataset /general/intracellular_ephys/simultaneous_recordings/recordings_index (VectorIndex) Index for VectorData 'recordings' | shape = (1,) | dtype = uint8
  lab: Dr. Li Zhang lab
  source_script: Created using NeuroConv v0.6.1
  Group /general/subject (Subject) 
  identifier: ID_2020_02_15_0000
  session_description: Intracellular electrophysiology experiment.
  session_start_time: 2020-02-15T16:14:36-08:00
  timestamps_reference_time: 2020-02-15T16:14:36-08:00
