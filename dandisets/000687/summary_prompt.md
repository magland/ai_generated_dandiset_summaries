
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000687/draft
name: similarity-weighted interleaved learning
contributor: [{'name': 'Saxena, Rajat', 'email': 'rajatsxn94@gmail.com', 'roleName': ['dcite:ContactPerson', 'dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Shobe, Justin', 'email': 'jshobe@gmail.com', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'McNaughton, Bruce', 'email': 'brucemcn@uci.edu', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'National Institute of Health (BRAIN )', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/05h1kgg64', 'awardNumber': 'NS121764', 'contactPoint': [], 'includeInCitation': False}, {'name': 'Defense Advanced Research Projects Agency', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/02caytj08', 'awardNumber': 'HR00111820021', 'contactPoint': [], 'includeInCitation': False}]
description: High-density silicon probe recordings from dorsal and intermediate CA1, primary visual cortex, and antero-lateral visual cortex in mice while they are exploring VR environments with different levels of similarity. The experiment was aimed at studying the content of replay across superficial and deep layers of visual cortex. 
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 3431932754105, 'numberOfFiles': 9, 'numberOfSubjects': 8, 'variableMeasured': ['ElectrodeGroup', 'ElectricalSeries'], 'measurementTechnique': [{'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000687 has 11 NWB files.
2 of these NWB files are of type 1.
9 of these NWB files are of type 2.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeries (ElectricalSeries) voltage data recorded from the amplifiers of an Intan Technologies chip
  Dataset /acquisition/ElectricalSeries/electrodes (DynamicTableRegion) Intan electrode table region | shape = (256,) | dtype = int64
  Group /acquisition/TimeSeries_analog_input (TimeSeries) analog input data recorded from an Intan Technologies system
  Group /acquisition/TimeSeries_aux_input (TimeSeries) voltage data recorded from the auxiliary input of an Intan Technologies chip
  Group /acquisition/TimeSeries_digital_input (TimeSeries) digital input data recorded from an Intan Technologies system
  file_create_date: ['2023-11-06T10:34:26.777136-08:00']
  Group /general/devices/Intan Recording Controller (Device) 512-channel or 1024-channel RHD2000 Recording Controller, part number C3004 or C3008. File version 3.0
  Group /general/extracellular_ephys/Intan Port B electrode group (ElectrodeGroup) description
  Group /general/extracellular_ephys/Intan Port B electrode group/device (Device) 512-channel or 1024-channel RHD2000 Recording Controller, part number C3004 or C3008. File version 3.0
  Group /general/extracellular_ephys/Intan Port C electrode group (ElectrodeGroup) description
  Group /general/extracellular_ephys/Intan Port C electrode group/device (Device) 512-channel or 1024-channel RHD2000 Recording Controller, part number C3004 or C3008. File version 3.0
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/custom_channel_name (VectorData) custom, user-editable name of this channel | shape = (256,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering, including the filter name and frequency cutoffs | shape = (256,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (256,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (256,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (256,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the electrode, in ohms | shape = (256,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/imp_phase (VectorData) phase (in degrees) of complex impedance of this channel | shape = (256,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (256,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/native_channel_name (VectorData) native, uneditable name (for example, A-000)of this channel | shape = (256,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the position (+x is posterior) | shape = (256,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the position (+y is inferior) | shape = (256,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the position (+z is right) | shape = (256,) | dtype = float64
  Group /general/subject (Subject) 
  identifier: swil10merged
  session_description: fully interleaved + blocked novel
  session_start_time: 2021-07-17T17:07:31-07:00
  timestamps_reference_time: 2021-07-17T17:07:31-07:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeries (ElectricalSeries) voltage data recorded from the amplifiers of an Intan Technologies chip
  Dataset /acquisition/ElectricalSeries/electrodes (DynamicTableRegion) Intan electrode table region | shape = (512,) | dtype = int64
  Group /acquisition/TimeSeries_analog_input (TimeSeries) analog input data recorded from an Intan Technologies system
  Group /acquisition/TimeSeries_aux_input (TimeSeries) voltage data recorded from the auxiliary input of an Intan Technologies chip
  Group /acquisition/TimeSeries_digital_input (TimeSeries) digital input data recorded from an Intan Technologies system
  file_create_date: ['2023-11-09T08:19:11.745597-08:00']
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
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (512,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the electrode, in ohms | shape = (512,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/imp_phase (VectorData) phase (in degrees) of complex impedance of this channel | shape = (512,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (512,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/native_channel_name (VectorData) native, uneditable name (for example, A-000)of this channel | shape = (512,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the position (+x is posterior) | shape = (512,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the position (+y is inferior) | shape = (512,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the position (+z is right) | shape = (512,) | dtype = float64
  Group /general/subject (Subject) 
  identifier: sub-swil105_ecephys
  session_description: interleaved blocks
  session_start_time: 2022-04-15T16:05:08-07:00
  timestamps_reference_time: 2022-04-15T16:05:08-07:00
