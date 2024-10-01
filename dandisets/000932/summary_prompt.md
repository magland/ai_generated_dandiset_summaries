
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000932/0.240317.0101
name: An electroencephalogram microdisplay to visualize neuronal activity on the brain surface
contributor: [{'name': 'Tchoe, Youngbin', 'email': 'ybtchoe@gmail.com', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}]
description: These datasets contain electrocorticography recordings from the brains of pigs and rats, utilizing a 1024-channel intracranial electroencephalography (iEEG) microdisplay. These recordings were obtained from animals that participated in the study documented in the paper titled 'An electroencephalogram microdisplay to visualize neuronal activity on the brain surface'. The data includes noise that can be filtered out. For detailed instructions on this process, please consult the accompanying journal article.
assetsSummary: {'species': [{'name': 'Sus scrofa domesticus - Domestic pig', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9825'}, {'name': 'Rattus norvegicus - Norway rat', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10116'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 199844377549, 'numberOfFiles': 238, 'numberOfSubjects': 10, 'variableMeasured': ['ElectricalSeries', 'ElectrodeGroup'], 'measurementTechnique': [{'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000932 has 100 NWB files.
100 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeries (ElectricalSeries) voltage data recorded from the amplifiers of an Intan Technologies chip
  Dataset /acquisition/ElectricalSeries/electrodes (DynamicTableRegion) Intan electrode table region | shape = (1024,) | dtype = int32
  Group /acquisition/TimeSeries_analog_input (TimeSeries) analog input data recorded from an Intan Technologies system
  Group /acquisition/TimeSeries_aux_input (TimeSeries) voltage data recorded from the auxiliary input of an Intan Technologies chip
  Group /acquisition/TimeSeries_supply_voltage (TimeSeries) supply voltage data recorded from an Intan Technologies chip
  file_create_date: ['2024-03-16T14:29:13.961402+09:00']
  Group /general/devices/Intan Recording Controller (Device) 512-channel or 1024-channel RHD2000 Recording Controller, part number C3004 or C3008. File version 2.0
  Group /general/extracellular_ephys/Intan Port A electrode group (ElectrodeGroup) description
  Group /general/extracellular_ephys/Intan Port A electrode group/device (Device) 512-channel or 1024-channel RHD2000 Recording Controller, part number C3004 or C3008. File version 2.0
  Group /general/extracellular_ephys/Intan Port B electrode group (ElectrodeGroup) description
  Group /general/extracellular_ephys/Intan Port B electrode group/device (Device) 512-channel or 1024-channel RHD2000 Recording Controller, part number C3004 or C3008. File version 2.0
  Group /general/extracellular_ephys/Intan Port C electrode group (ElectrodeGroup) description
  Group /general/extracellular_ephys/Intan Port C electrode group/device (Device) 512-channel or 1024-channel RHD2000 Recording Controller, part number C3004 or C3008. File version 2.0
  Group /general/extracellular_ephys/Intan Port D electrode group (ElectrodeGroup) description
  Group /general/extracellular_ephys/Intan Port D electrode group/device (Device) 512-channel or 1024-channel RHD2000 Recording Controller, part number C3004 or C3008. File version 2.0
  Group /general/extracellular_ephys/Intan Port E electrode group (ElectrodeGroup) description
  Group /general/extracellular_ephys/Intan Port E electrode group/device (Device) 512-channel or 1024-channel RHD2000 Recording Controller, part number C3004 or C3008. File version 2.0
  Group /general/extracellular_ephys/Intan Port F electrode group (ElectrodeGroup) description
  Group /general/extracellular_ephys/Intan Port F electrode group/device (Device) 512-channel or 1024-channel RHD2000 Recording Controller, part number C3004 or C3008. File version 2.0
  Group /general/extracellular_ephys/Intan Port G electrode group (ElectrodeGroup) description
  Group /general/extracellular_ephys/Intan Port G electrode group/device (Device) 512-channel or 1024-channel RHD2000 Recording Controller, part number C3004 or C3008. File version 2.0
  Group /general/extracellular_ephys/Intan Port H electrode group (ElectrodeGroup) description
  Group /general/extracellular_ephys/Intan Port H electrode group/device (Device) 512-channel or 1024-channel RHD2000 Recording Controller, part number C3004 or C3008. File version 2.0
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/custom_channel_name (VectorData) custom, user-editable name of this channel | shape = (1024,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering, including the filter name and frequency cutoffs | shape = (1024,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (1024,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (1024,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (1024,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the electrode, in ohms | shape = (1024,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/imp_phase (VectorData) phase (in degrees) of complex impedance of this channel | shape = (1024,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (1024,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/native_channel_name (VectorData) native, uneditable name (for example, A-000)of this channel | shape = (1024,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the position (+x is posterior) | shape = (1024,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the position (+y is inferior) | shape = (1024,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the position (+z is right) | shape = (1024,) | dtype = float64
  Group /general/subject (Subject) 
  identifier: D:\DATA_STM_2024\Pigs\Pig_case_11162022\Ojemann_3mA_1ms_221116_120452
  session_description: no description provided
  session_start_time: 2022-11-16T12:04:52+09:00
  timestamps_reference_time: 2022-11-16T12:04:52+09:00
