
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000068/draft
name: Testing
contributor: []
description: Nothing to see
assetsSummary: {'species': [], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 362448, 'numberOfFiles': 2, 'numberOfSubjects': 1, 'variableMeasured': ['VoltageClampSeries', 'CurrentClampStimulusSeries', 'CurrentClampSeries', 'VoltageClampStimulusSeries'], 'measurementTechnique': [{'name': 'voltage clamp technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'current clamp technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000068 has 2 NWB files.
2 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ccs (CurrentClampSeries) no description
  Group /acquisition/ccs/electrode (IntracellularElectrode) 
  Group /acquisition/ccs/electrode/device (Device) 
  Group /acquisition/vcs (VoltageClampSeries) no description
  Group /acquisition/vcs/electrode (IntracellularElectrode) 
  Group /acquisition/vcs/electrode/device (Device) 
  file_create_date: ['2021-04-23T21:04:36.999065+02:00']
  Group /general/devices/Heka ITC-1600 (Device) 
  experiment_description: I went on an adventure with thirteen dwarves to reclaim vast treasures.
  experimenter: ['Dr. Bilbo Baggins']
  institution: University of Middle Earth at the Shire
  Group /general/intracellular_ephys/elec0 (IntracellularElectrode) 
  Group /general/intracellular_ephys/elec0/device (Device) 
  Group /general/intracellular_ephys/sweep_table (SweepTable) A sweep table groups different PatchClampSeries together.
  Dataset /general/intracellular_ephys/sweep_table/id (ElementIdentifiers)  | shape = (4,) | dtype = int32
  Dataset /general/intracellular_ephys/sweep_table/series (VectorData) PatchClampSeries with the same sweep number | shape = (4,) | dtype = object
  Dataset /general/intracellular_ephys/sweep_table/series_index (VectorIndex) Index for VectorData 'series' | shape = (4,) | dtype = uint8
  Dataset /general/intracellular_ephys/sweep_table/sweep_number (VectorData) Sweep number of the entries in that row | shape = (4,) | dtype = uint32
  lab: Bag End Laboratory
  session_id: LONELYMTN
  Group /general/subject (Subject) 
  identifier: EXAMPLE_ID
  session_description: my first synthetic recording
  session_start_time: 2021-04-23T21:04:36.999065+02:00
  Group /stimulus/presentation/ccss (CurrentClampStimulusSeries) no description
  Group /stimulus/presentation/ccss/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/ccss/electrode/device (Device) 
  Group /stimulus/presentation/vcss (VoltageClampStimulusSeries) no description
  Group /stimulus/presentation/vcss/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/vcss/electrode/device (Device) 
  timestamps_reference_time: 2021-04-23T21:04:36.999065+02:00
