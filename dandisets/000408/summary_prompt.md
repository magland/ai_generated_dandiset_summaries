
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000408/draft
name: In vitro electrochemical impedance spectroscopy data - microelectrode arrays
contributor: [{'name': 'National Institutes of Health (NIH)', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': '1 U01 NS 126052-01'}, {'name': 'Otto, Kevin', 'email': 'kevin.otto@bme.ufl.edu', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0002-2317-6194', 'includeInCitation': True}, {'name': 'Orazem, Mark', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0003-3668-7767', 'includeInCitation': True}, {'name': 'Cogan, Stuart', 'schemaKey': 'Person', 'identifier': '0000-0001-6316-3032', 'includeInCitation': True}]
description: Electrochemical impedance spectroscopy (EIS) data from multichannel microelectrode arrays coated with activated iridium oxide (AIROF), sputtered iridium oxide (SIROF), or ruthenium oxide (RuOx). Supported by NIH 1U01NS126052-01.
assetsSummary: {'species': [{'name': 'Rattus norvegicus - Norway rat', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10116'}, {'name': 'Unidentified', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_32644'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 44500560, 'numberOfFiles': 228, 'numberOfSubjects': 3, 'variableMeasured': ['ElectrodeGroup'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000408 has 100 NWB files.
88 of these NWB files are of type 1.
7 of these NWB files are of type 2.
5 of these NWB files are of type 3.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/EIS_Impedance (DynamicTable) This table stores frequency, Z-real, Z-imaginary values of EIS experiment
  Dataset /acquisition/EIS_Impedance/frequency (VectorData)  | shape = (65,) | dtype = float64
  Dataset /acquisition/EIS_Impedance/id (ElementIdentifiers)  | shape = (65,) | dtype = int32
  Dataset /acquisition/EIS_Impedance/zimaginary (VectorData)  | shape = (65,) | dtype = float64
  Dataset /acquisition/EIS_Impedance/zreal (VectorData)  | shape = (65,) | dtype = float64
  file_create_date: ['2023-07-31T19:59:24.828947-04:00']
  Group /general/devices/GAMRY (Device) This device is used to measure impedance values of a Potentiostatic EIS experiment
  experiment_description: EIS vs V Eoc
  experimenter: ['Yupeng']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/area (VectorData) area of electrode | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/electrode_name (VectorData) label of electrode | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/material (VectorData) material of electrode | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/units (VectorData) units in which area is measured | shape = (1,) | dtype = object
  Group /general/extracellular_ephys/unknown (ElectrodeGroup) electrode group
  Group /general/extracellular_ephys/unknown/device (Device) This device is used to measure impedance values of a Potentiostatic EIS experiment
  session_id: EIS experiment ID
  Group /general/subject (Subject) 
  identifier: 1092_23_A1.DTA
  session_description: EIS vs V Eoc
  session_start_time: 2023-02-20T11:11:14-04:56
  timestamps_reference_time: 2023-02-20T11:11:14-04:56


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/EIS_Impedance (DynamicTable) This table stores frequency, Z-real, Z-imaginary values of EIS experiment
  Dataset /acquisition/EIS_Impedance/frequency (VectorData)  | shape = (65,) | dtype = float64
  Dataset /acquisition/EIS_Impedance/id (ElementIdentifiers)  | shape = (65,) | dtype = int32
  Dataset /acquisition/EIS_Impedance/zimaginary (VectorData)  | shape = (65,) | dtype = float64
  Dataset /acquisition/EIS_Impedance/zreal (VectorData)  | shape = (65,) | dtype = float64
  file_create_date: ['2023-05-03T18:44:43.875176-04:00']
  Group /general/devices/GAMRY (Device) This device is used to measure impedance values of a Potentiostatic EIS experiment
  experiment_description: in vitro experiment, please disregard animal
  experimenter: ['Wu Yupeng']
  Group /general/extracellular_ephys/A02 LOTME19738 (ElectrodeGroup) AIROF coated (Activated Iridium Oxide)
  Group /general/extracellular_ephys/A02 LOTME19738/device (Device) This device is used to measure impedance values of a Potentiostatic EIS experiment
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/area (VectorData) area of electrode | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/electrode_name (VectorData) label of electrode | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/units (VectorData) units in which area is measured | shape = (1,) | dtype = object
  institution: University of Texas at Dallas
  lab: Cogan Lab
  session_id: EIS experiment ID
  Group /general/subject (Subject) 
  identifier: 107837ZD.DTA
  session_description: EIS vs 0V Eoc
  session_start_time: 2022-07-21T13:43:41-04:56
  timestamps_reference_time: 2022-07-21T13:43:41-04:56


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/EIS_Impedance (DynamicTable) This table stores frequency, Z-real, Z-imaginary values of EIS experiment
  Dataset /acquisition/EIS_Impedance/frequency (VectorData)  | shape = (65,) | dtype = float64
  Dataset /acquisition/EIS_Impedance/id (ElementIdentifiers)  | shape = (65,) | dtype = int32
  Dataset /acquisition/EIS_Impedance/zimaginary (VectorData)  | shape = (65,) | dtype = float64
  Dataset /acquisition/EIS_Impedance/zreal (VectorData)  | shape = (65,) | dtype = float64
  file_create_date: ['2023-05-03T18:54:52.548214-04:00']
  Group /general/devices/GAMRY (Device) This device is used to measure impedance values of a Potentiostatic EIS experiment
  experiment_description: in vitro experiment, please disregard animal
  experimenter: ['Wu Yupeng']
  Group /general/extracellular_ephys/1092_12 (ElectrodeGroup) RuOx coated (Sputtered Ruthenium Oxide). Not rejuvenated.
  Group /general/extracellular_ephys/1092_12/device (Device) This device is used to measure impedance values of a Potentiostatic EIS experiment
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/area (VectorData) area of electrode | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/electrode_name (VectorData) label of electrode | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/units (VectorData) units in which area is measured | shape = (1,) | dtype = object
  institution: University of Texas at Dallas
  lab: Cogan Lab
  session_id: EIS experiment ID
  Group /general/subject (Subject) 
  identifier: 1092_12_W2.DTA
  session_description: EIS vs -0.4V Eref
  session_start_time: 2022-11-17T14:25:13-04:56
  timestamps_reference_time: 2022-11-17T14:25:13-04:56
