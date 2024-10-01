
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001023/draft
name: In vitro electrochemical impedance spectroscopy data - Accuracy Contour Plot
contributor: [{'name': 'National Institutes of Health (NIH)', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': '1 UO1 NS 126052-01', 'includeInCitation': False}, {'name': 'Orazem, Mark', 'email': 'morazem@che.ufl.edu', 'schemaKey': 'Person', 'identifier': '0000-0003-3668-7767', 'includeInCitation': True}, {'name': 'Cogan, Stuart', 'email': 'stuart.cogan@utdallas.edu', 'schemaKey': 'Person', 'identifier': '0000-0001-6316-3032', 'includeInCitation': True}, {'name': 'Otto, Kevin', 'email': 'kevin.otto@bme.ufl.edu', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0002-2317-6194', 'includeInCitation': True}]
description: EIS data for the accuracy contour plot of G2 electrodes in this UO1 project.
assetsSummary: {'schemaKey': 'AssetsSummary', 'numberOfBytes': 0, 'numberOfFiles': 0}

Dandiset 001023 has 10 NWB files.
1 of these NWB files are of type 1.
3 of these NWB files are of type 2.
4 of these NWB files are of type 3.
2 of these NWB files are of type 4.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/EIS_Impedance (DynamicTable) This table stores frequency, Z-real, Z-imaginary values of EIS experiment
  Dataset /acquisition/EIS_Impedance/frequency (VectorData)  | shape = (88,) | dtype = float64
  Dataset /acquisition/EIS_Impedance/id (ElementIdentifiers)  | shape = (88,) | dtype = int32
  Dataset /acquisition/EIS_Impedance/zimaginary (VectorData)  | shape = (88,) | dtype = float64
  Dataset /acquisition/EIS_Impedance/zreal (VectorData)  | shape = (88,) | dtype = float64
  file_create_date: ['2024-05-14T17:43:39.957583-04:00']
  Group /general/devices/GAMRY (Device) This device is used to measure impedance values of a Potentiostatic EIS experiment
  experiment_description: EIS
  experimenter: ['Cynthia Ezeh']
  Group /general/extracellular_ephys/G2 buried loop         (ElectrodeGroup) electrode group
  Group /general/extracellular_ephys/G2 buried loop        /device (Device) This device is used to measure impedance values of a Potentiostatic EIS experiment
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/area (VectorData) area of electrode | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/electrode_name (VectorData) label of electrode | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/material (VectorData) material of electrode | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/units (VectorData) units in which area is measured | shape = (1,) | dtype = object
  session_id: EIS experiment ID
  Group /general/subject (Subject) 
  identifier: G2_09_Loop_11C &30W_TDT_Air #2.DTA.txt
  session_description: EIS
  session_start_time: 2024-02-29T21:08:19-04:56
  timestamps_reference_time: 2024-02-29T21:08:19-04:56


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/EIS_Impedance (DynamicTable) This table stores frequency, Z-real, Z-imaginary values of EIS experiment
  Dataset /acquisition/EIS_Impedance/frequency (VectorData)  | shape = (88,) | dtype = float64
  Dataset /acquisition/EIS_Impedance/id (ElementIdentifiers)  | shape = (88,) | dtype = int32
  Dataset /acquisition/EIS_Impedance/zimaginary (VectorData)  | shape = (88,) | dtype = float64
  Dataset /acquisition/EIS_Impedance/zreal (VectorData)  | shape = (88,) | dtype = float64
  file_create_date: ['2024-05-14T17:46:52.618623-04:00']
  Group /general/devices/GAMRY (Device) This device is used to measure impedance values of a Potentiostatic EIS experiment
  experiment_description: EIS
  experimenter: ['Cynthia Ezeh']
  Group /general/extracellular_ephys/G2 buried loop (ElectrodeGroup) electrode group
  Group /general/extracellular_ephys/G2 buried loop/device (Device) This device is used to measure impedance values of a Potentiostatic EIS experiment
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/area (VectorData) area of electrode | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/electrode_name (VectorData) label of electrode | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/material (VectorData) material of electrode | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/units (VectorData) units in which area is measured | shape = (1,) | dtype = object
  session_id: EIS experiment ID
  Group /general/subject (Subject) 
  identifier: G2_09_Loop_11C &30W_TDT_PBS#3.DTA
  session_description: EIS
  session_start_time: 2024-02-29T19:53:57-04:56
  timestamps_reference_time: 2024-02-29T19:53:57-04:56


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/EIS_Impedance (DynamicTable) This table stores frequency, Z-real, Z-imaginary values of EIS experiment
  Dataset /acquisition/EIS_Impedance/frequency (VectorData)  | shape = (88,) | dtype = float64
  Dataset /acquisition/EIS_Impedance/id (ElementIdentifiers)  | shape = (88,) | dtype = int32
  Dataset /acquisition/EIS_Impedance/zimaginary (VectorData)  | shape = (88,) | dtype = float64
  Dataset /acquisition/EIS_Impedance/zreal (VectorData)  | shape = (88,) | dtype = float64
  file_create_date: ['2024-05-14T18:19:04.861443-04:00']
  Group /general/devices/GAMRY (Device) This device is used to measure impedance values of a Potentiostatic EIS experiment
  experiment_description: EIS
  experimenter: ['Cynthia Ezeh']
  Group /general/extracellular_ephys/G2 buried terminal (ElectrodeGroup) electrode group
  Group /general/extracellular_ephys/G2 buried terminal/device (Device) This device is used to measure impedance values of a Potentiostatic EIS experiment
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/area (VectorData) area of electrode | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/electrode_name (VectorData) label of electrode | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/material (VectorData) material of electrode | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/units (VectorData) units in which area is measured | shape = (1,) | dtype = object
  session_id: EIS experiment ID
  Group /general/subject (Subject) 
  identifier: G2_09_Ter_C23_TDT_Air_#1.DTA
  session_description: EIS
  session_start_time: 2024-02-29T16:18:53-04:56
  timestamps_reference_time: 2024-02-29T16:18:53-04:56


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/EIS_Impedance (DynamicTable) This table stores frequency, Z-real, Z-imaginary values of EIS experiment
  Dataset /acquisition/EIS_Impedance/frequency (VectorData)  | shape = (81,) | dtype = float64
  Dataset /acquisition/EIS_Impedance/id (ElementIdentifiers)  | shape = (81,) | dtype = int32
  Dataset /acquisition/EIS_Impedance/zimaginary (VectorData)  | shape = (81,) | dtype = float64
  Dataset /acquisition/EIS_Impedance/zreal (VectorData)  | shape = (81,) | dtype = float64
  file_create_date: ['2024-05-14T17:00:26.497969-04:00']
  Group /general/devices/GAMRY (Device) This device is used to measure impedance values of a Potentiostatic EIS experiment
  experiment_description: EIS
  experimenter: ['Cynthia Ezeh']
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
  identifier: Gamry_Ref_600P_open_lead_air.DTA
  session_description: EIS
  session_start_time: 2024-02-22T20:51:35-04:56
  timestamps_reference_time: 2024-02-22T20:51:35-04:56
