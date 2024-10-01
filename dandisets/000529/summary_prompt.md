
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000529/draft
name: Test 2
contributor: [{'name': 'Dewberry, Savannah', 'email': 'ls.dewberry@ufl.edu', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}]
description: try to upload EIS
assetsSummary: {'species': [{'name': 'Rattus norvegicus - Norway rat', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10116'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 5265108, 'numberOfFiles': 27, 'numberOfSubjects': 3, 'variableMeasured': ['ElectrodeGroup'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000529 has 27 NWB files.
14 of these NWB files are of type 1.
7 of these NWB files are of type 2.
6 of these NWB files are of type 3.


Here is a summary of the type 1 NWB files:
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
  file_create_date: ['2023-05-03T18:35:47.692992-04:00']
  Group /general/devices/GAMRY (Device) This device is used to measure impedance values of a Potentiostatic EIS experiment
  experiment_description: in vitro experiment, please disregard animal
  experimenter: ['Wu Yupeng']
  Group /general/extracellular_ephys/1092_9 (ElectrodeGroup) SIROF coated (Sputtered Iridium Oxide),  SIROF film are rejuvenated for 500 cycles (no more rejuvenation can be done based on cyclic voltammetry)
  Group /general/extracellular_ephys/1092_9/device (Device) This device is used to measure impedance values of a Potentiostatic EIS experiment
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
  identifier: 1092_9_O2.DTA
  session_description: EIS vs. 0.2V Eref
  session_start_time: 2022-10-29T06:14:57-04:56
  timestamps_reference_time: 2022-10-29T06:14:57-04:56
