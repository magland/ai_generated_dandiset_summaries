
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000968/draft
name: Engineering luminopsins with improved coupling efficiencies
contributor: [{'name': 'Slaviero, Ashley', 'email': 'slavi1a@cmich.edu', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}]
description: Intracellular voltage patch clamp recordings in HEK cells for various luminopsins. All recordings from analysis in "Engineering luminopsins with improved coupling efficiencies" by Slaviero et al 
assetsSummary: {'schemaKey': 'AssetsSummary', 'numberOfBytes': 0, 'numberOfFiles': 0}

Dandiset 000968 has 1 NWB files.
1 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/izero-response-01-ch-0 (IZeroClampSeries) Response to: not described
  Group /acquisition/izero-response-01-ch-0/electrode (IntracellularElectrode) 
  Group /acquisition/izero-response-01-ch-0/electrode/device (Device) no description
  Group /acquisition/izero-response-01-ch-1 (IZeroClampSeries) Response to: not described
  Group /acquisition/izero-response-01-ch-1/electrode (IntracellularElectrode) 
  Group /acquisition/izero-response-01-ch-1/electrode/device (Device) no description
  Group /acquisition/izero-response-02-ch-0 (IZeroClampSeries) Response to: not described
  Group /acquisition/izero-response-02-ch-0/electrode (IntracellularElectrode) 
  Group /acquisition/izero-response-02-ch-0/electrode/device (Device) no description
  Group /acquisition/izero-response-02-ch-1 (IZeroClampSeries) Response to: not described
  Group /acquisition/izero-response-02-ch-1/electrode (IntracellularElectrode) 
  Group /acquisition/izero-response-02-ch-1/electrode/device (Device) no description
  file_create_date: ['2024-04-28T11:33:25.341869-04:00']
  Group /general/DandiIcephysMetadata (DandiIcephysMetadata) 
  Group /general/devices/DeviceIcephys (Device) no description
  experimenter: ['Slaviero, Ashley']
  institution: Central Michigan University
  Group /general/intracellular_ephys/electrode-0 (IntracellularElectrode) 
  Group /general/intracellular_ephys/electrode-0/device (Device) no description
  Group /general/intracellular_ephys/electrode-1 (IntracellularElectrode) 
  Group /general/intracellular_ephys/electrode-1/device (Device) no description
  Group /general/intracellular_ephys/intracellular_recordings (IntracellularRecordingsTable) A table to group together a stimulus and response from a single electrode and a single simultaneous recording and for storing metadata about the intracellular recording.
  Group /general/intracellular_ephys/intracellular_recordings/electrodes (IntracellularElectrodesTable) Table for storing intracellular electrode related metadata.
  Dataset /general/intracellular_ephys/intracellular_recordings/electrodes/electrode (VectorData) Column for storing the reference to the intracellular electrode | shape = (4,) | dtype = object
  Dataset /general/intracellular_ephys/intracellular_recordings/electrodes/id (ElementIdentifiers)  | shape = (4,) | dtype = int64
  Dataset /general/intracellular_ephys/intracellular_recordings/id (ElementIdentifiers)  | shape = (4,) | dtype = int64
  Group /general/intracellular_ephys/intracellular_recordings/responses (IntracellularResponsesTable) Table for storing intracellular response related metadata.
  Dataset /general/intracellular_ephys/intracellular_recordings/responses/id (ElementIdentifiers)  | shape = (4,) | dtype = int64
  Dataset /general/intracellular_ephys/intracellular_recordings/responses/response (TimeSeriesReferenceVectorData) Column storing the reference to the recorded response for the recording (rows) | shape = (4,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Group /general/intracellular_ephys/intracellular_recordings/stimuli (IntracellularStimuliTable) Table for storing intracellular stimulus related metadata.
  Dataset /general/intracellular_ephys/intracellular_recordings/stimuli/id (ElementIdentifiers)  | shape = (4,) | dtype = int64
  Dataset /general/intracellular_ephys/intracellular_recordings/stimuli/stimulus (TimeSeriesReferenceVectorData) Column storing the reference to the recorded stimulus for the recording (rows) | shape = (4,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Group /general/intracellular_ephys/sequential_recordings (SequentialRecordingsTable) A table for grouping different intracellular recording simultaneous_recordings from the SimultaneousRecordingsTable table together. This is typically used to group together simultaneous_recordings where the a sequence of stimuli of the same type with varying parameters have been presented in a sequence.
  Dataset /general/intracellular_ephys/sequential_recordings/id (ElementIdentifiers)  | shape = (2,) | dtype = int64
  Dataset /general/intracellular_ephys/sequential_recordings/simultaneous_recordings (DynamicTableRegion) Column with references to one or more rows in the SimultaneousRecordingsTable table | shape = (2,) | dtype = int64
  Dataset /general/intracellular_ephys/sequential_recordings/simultaneous_recordings_index (VectorIndex) Index for VectorData 'simultaneous_recordings' | shape = (2,) | dtype = uint8
  Dataset /general/intracellular_ephys/sequential_recordings/stimulus_type (VectorData) Column storing the type of stimulus used for the sequential recording | shape = (2,) | dtype = object
  Group /general/intracellular_ephys/simultaneous_recordings (SimultaneousRecordingsTable) A table for grouping different intracellular recordings from theIntracellularRecordingsTable table together that were recorded simultaneously from different electrodes.
  Dataset /general/intracellular_ephys/simultaneous_recordings/id (ElementIdentifiers)  | shape = (2,) | dtype = int64
  Dataset /general/intracellular_ephys/simultaneous_recordings/recordings (DynamicTableRegion) Column with references to one or more rows in the IntracellularRecordingsTable table | shape = (4,) | dtype = int64
  Dataset /general/intracellular_ephys/simultaneous_recordings/recordings_index (VectorIndex) Index for VectorData 'recordings' | shape = (2,) | dtype = uint8
  lab: Hochgeschwender Lab
  Group /general/subject (Subject) 
  identifier: ID18
  session_description: Intracellular electrophysiology experiment (HEK).
  session_start_time: 2023-05-18T15:37:47-04:00
  timestamps_reference_time: 2023-05-18T15:37:47-04:00
