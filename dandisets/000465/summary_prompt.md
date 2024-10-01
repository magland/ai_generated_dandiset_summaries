
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000465/0.230530.2349
name: Human brain mapping with multithousand-channel PtNRGrids resolves spatiotemporal dynamics
contributor: [{'name': 'Tchoe, Youngbin', 'email': 'ybtchoe@gmail.com', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}]
description: This dataset contains recordings from PtNRGrids, which are devices designed to record electrocorticography (ECoG) activities from the brain surface at high-spatial resolution. PtNRGrids used here were a square-shaped array with 1024 channels and a 150-µm pitch, which was implanted to record neural activity from the entire right primary somatosensory barrel cortex. The sensory response on the brain was evoked by delivering air puffs through a microcapillary tube to individually stimulate individual whiskers on the contralateral side. This dataset demonstrates the high-spatial resolution recording capability of PtNRGrids isolate functional cortical columns in sub-mm resolution from the surface of the brain.

[Publication corresponding to this dataset] Tchoe, Youngbin, et al. "Human brain mapping with multithousand-channel PtNRGrids resolves spatiotemporal dynamics." Science translational medicine 14.628 (2022): eabj1441.
[Electrode mapping information & Basic analysis codes] Github: https://ytchoe.github.io/
assetsSummary: {'species': [{'name': 'Rattus norvegicus - Norway rat', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10116'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 129066795249, 'numberOfFiles': 36, 'numberOfSubjects': 4, 'variableMeasured': ['ElectrodeGroup', 'ElectricalSeries'], 'measurementTechnique': [{'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000465 has 36 NWB files.
2 of these NWB files are of type 1.
34 of these NWB files are of type 2.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeries (ElectricalSeries) voltage data recorded from the amplifiers of an Intan Technologies chip
  Dataset /acquisition/ElectricalSeries/electrodes (DynamicTableRegion) Intan electrode table region | shape = (1024,) | dtype = int32
  Group /acquisition/TimeSeries_aux_input (TimeSeries) voltage data recorded from the auxiliary input of an Intan Technologies chip
  Group /acquisition/TimeSeries_supply_voltage (TimeSeries) supply voltage data recorded from an Intan Technologies chip
  file_create_date: ['2023-05-19T23:16:44.118159+09:00']
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
  Dataset /general/extracellular_ephys/electrodes/native_channel_name (VectorData) native, uneditable name (for example, A-000) of this channel | shape = (1024,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the position (+x is posterior) | shape = (1024,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the position (+y is inferior) | shape = (1024,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the position (+z is right) | shape = (1024,) | dtype = float64
  Group /general/subject (Subject) 
  identifier: C:\Rat_data\Rat1\Baseline_Rat_implanted_200317_102302
  session_description: Baseline recordings on the barrel cortex + Fine functional mapping of rat barrel cortex (right side) with micro-ECoG grids with 1024 channels, 150 µm pitch, 30 µm diameter
  session_start_time: 2020-03-17T10:23:02+09:00
  timestamps_reference_time: 2020-03-17T10:23:02+09:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeries (ElectricalSeries) voltage data recorded from the amplifiers of an Intan Technologies chip
  Dataset /acquisition/ElectricalSeries/electrodes (DynamicTableRegion) Intan electrode table region | shape = (1024,) | dtype = int32
  Group /acquisition/TimeSeries_analog_input (TimeSeries) analog input data recorded from an Intan Technologies system
  Group /acquisition/TimeSeries_aux_input (TimeSeries) voltage data recorded from the auxiliary input of an Intan Technologies chip
  Group /acquisition/TimeSeries_supply_voltage (TimeSeries) supply voltage data recorded from an Intan Technologies chip
  file_create_date: ['2023-05-19T23:53:19.272488+09:00']
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
  Dataset /general/extracellular_ephys/electrodes/native_channel_name (VectorData) native, uneditable name (for example, A-000) of this channel | shape = (1024,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the position (+x is posterior) | shape = (1024,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the position (+y is inferior) | shape = (1024,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the position (+z is right) | shape = (1024,) | dtype = float64
  Group /general/subject (Subject) 
  identifier: C:\Rat_data\Rat1\Whiskers_left_D4_200317_104800
  session_description: Sensory stimulation of contralateral D4 whisker with 20 psi air-puff every 1 s + Fine functional mapping of rat barrel cortex (right side) with micro-ECoG grids with 1024 channels, 150 µm pitch, 30 µm diameter
  session_start_time: 2020-03-17T10:48:00+09:00
  timestamps_reference_time: 2020-03-17T10:48:00+09:00
