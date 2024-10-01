
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000696/draft
name: The organization of context versus content coding in the hippocampus and neocortex
contributor: [{'name': 'Ning, Wing', 'email': 'wingning@bu.edu', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}]
description: High-density silicon probe recordings from primary somatosensory cortex, posterior parietal cortex, and dorsal hippocampus (CA1) in head-fixed mice while running on a treadmill virtual reality task with different tactile cues.
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 3849974839417, 'numberOfFiles': 5, 'numberOfSubjects': 5, 'variableMeasured': ['ElectrodeGroup', 'ElectricalSeries'], 'measurementTechnique': [{'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000696 has 6 NWB files.
6 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeries (ElectricalSeries) voltage data recorded from the amplifiers of an Intan Technologies chip
  Dataset /acquisition/ElectricalSeries/electrodes (DynamicTableRegion) Intan electrode table region | shape = (512,) | dtype = int32
  Group /acquisition/TimeSeries_analog_input (TimeSeries) analog input data recorded from an Intan Technologies system
  Group /acquisition/TimeSeries_aux_input (TimeSeries) voltage data recorded from the auxiliary input of an Intan Technologies chip
  Group /acquisition/TimeSeries_digital_input (TimeSeries) digital input data recorded from an Intan Technologies system
  file_create_date: ['2023-11-11T21:38:57.146231-08:00']
  Group /general/devices/Intan Recording Controller (Device) 512-channel or 1024-channel RHD2000 Recording Controller, part number C3004 or C3008. File version 3.0
  Group /general/extracellular_ephys/Intan Port A electrode group (ElectrodeGroup) description
  Group /general/extracellular_ephys/Intan Port A electrode group/device (Device) 512-channel or 1024-channel RHD2000 Recording Controller, part number C3004 or C3008. File version 3.0
  Group /general/extracellular_ephys/Intan Port B electrode group (ElectrodeGroup) description
  Group /general/extracellular_ephys/Intan Port B electrode group/device (Device) 512-channel or 1024-channel RHD2000 Recording Controller, part number C3004 or C3008. File version 3.0
  Group /general/extracellular_ephys/Intan Port C electrode group (ElectrodeGroup) description
  Group /general/extracellular_ephys/Intan Port C electrode group/device (Device) 512-channel or 1024-channel RHD2000 Recording Controller, part number C3004 or C3008. File version 3.0
  Group /general/extracellular_ephys/Intan Port D electrode group (ElectrodeGroup) description
  Group /general/extracellular_ephys/Intan Port D electrode group/device (Device) 512-channel or 1024-channel RHD2000 Recording Controller, part number C3004 or C3008. File version 3.0
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/custom_channel_name (VectorData) custom, user-editable name of this channel | shape = (512,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering, including the filter name and frequency cutoffs | shape = (512,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (512,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (512,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (512,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the electrode, in ohms | shape = (512,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/imp_phase (VectorData) phase (in degrees) of complex impedance of this channel | shape = (512,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (512,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/native_channel_name (VectorData) native, uneditable name (for example, A-000)of this channel | shape = (512,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the position (+x is posterior) | shape = (512,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the position (+y is inferior) | shape = (512,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the position (+z is right) | shape = (512,) | dtype = float64
  Group /general/subject (Subject) 
  identifier: U:\Winny\Data\TR11_5-16-2023\TR11merged
  session_description: cue swap across VR contexts
  session_start_time: 2023-05-16T18:01:40-07:00
  timestamps_reference_time: 2023-05-16T18:01:40-07:00
