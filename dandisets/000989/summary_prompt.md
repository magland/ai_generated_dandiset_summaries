
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000989/draft
name: In vitro electrochemical impedance spectroscopy data - G1 and G2
contributor: [{'name': 'National Institutes of Health (NIH)', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': '1 UO1 NS 126052-01', 'includeInCitation': False}, {'name': 'Otto, Kevin', 'email': 'kevin.otto@bme.ufl.edu', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0002-2317-6194', 'includeInCitation': True}, {'name': 'Orazem, Mark', 'email': 'morazem@che.ufl.edu', 'schemaKey': 'Person', 'identifier': '0000-0003-3668-7767', 'includeInCitation': True}, {'name': 'Cogan, Stuart', 'email': 'stuart.cogan@utdallas.edu', 'schemaKey': 'Person', 'identifier': '0000-0001-6316-3032', 'includeInCitation': True}]
description: Representative EIS data of G1 and G2 electrodes for all channels in this UO1 project.
For G1 electrodes, the relationship between the diameter of electrode contacts and the electrode number is as follows:
5 (um): 2, 9, 16, 24
10: 1, 11, 23, 31
15: 8, 10, 22, 30
20: 3, 15, 21, 25
25: 6, 7, 12, 26
30: 13, 18, 19, 27
40: 4, 14, 20 28
50: 5, 17, 29, 32
For G2 electrodes, the relationship between the diameter of electrode contacts and the electrode number is as follows:
5 (um): 2, 3, 4, 5, 6, 7, 17, 18, 19, 20, 22
10: 9, 12, 13, 14, 15, 16, 25, 26, 27, 28, 29, 32
circuit: 1-8, 11-30
terminal: 23, 31
reference (4004 um^2): 10, 24
assetsSummary: {'species': [{'name': 'Unidentified', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_32644'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 52322892, 'numberOfFiles': 257, 'numberOfSubjects': 8, 'variableMeasured': ['ElectrodeGroup'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000989 has 100 NWB files.
32 of these NWB files are of type 1.
32 of these NWB files are of type 2.
4 of these NWB files are of type 3.
32 of these NWB files are of type 4.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/EIS_Impedance (DynamicTable) This table stores frequency, Z-real, Z-imaginary values of EIS experiment
  Dataset /acquisition/EIS_Impedance/frequency (VectorData)  | shape = (51,) | dtype = float64
  Dataset /acquisition/EIS_Impedance/id (ElementIdentifiers)  | shape = (51,) | dtype = int32
  Dataset /acquisition/EIS_Impedance/zimaginary (VectorData)  | shape = (51,) | dtype = float64
  Dataset /acquisition/EIS_Impedance/zreal (VectorData)  | shape = (51,) | dtype = float64
  file_create_date: ['2024-05-13T22:19:16.676032-04:00']
  Group /general/devices/Autolab (Device) Basic CSV data with no additional metadata
  experiment_description: In Vitro EIS
  experimenter: ['Qiwei Dong']
  Group /general/extracellular_ephys/G1_12A62 (ElectrodeGroup) electrode group
  Group /general/extracellular_ephys/G1_12A62/device (Device) Basic CSV data with no additional metadata
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
  identifier: EIS_ch14_0.223312377929688Vocp_1.csv
  session_description: In Vitro EIS
  session_start_time: 2024-05-13T22:19:16.676032-04:00
  timestamps_reference_time: 2024-05-13T22:19:16.676032-04:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/EIS_Impedance (DynamicTable) This table stores frequency, Z-real, Z-imaginary values of EIS experiment
  Dataset /acquisition/EIS_Impedance/frequency (VectorData)  | shape = (51,) | dtype = float64
  Dataset /acquisition/EIS_Impedance/id (ElementIdentifiers)  | shape = (51,) | dtype = int32
  Dataset /acquisition/EIS_Impedance/zimaginary (VectorData)  | shape = (51,) | dtype = float64
  Dataset /acquisition/EIS_Impedance/zreal (VectorData)  | shape = (51,) | dtype = float64
  file_create_date: ['2024-05-13T22:04:00.338937-04:00']
  Group /general/devices/Autolab (Device) Basic CSV data with no additional metadata
  experiment_description: In Vitro EIS
  experimenter: ['Qiwei Dong']
  Group /general/extracellular_ephys/G1_12A5B (ElectrodeGroup) electrode group
  Group /general/extracellular_ephys/G1_12A5B/device (Device) Basic CSV data with no additional metadata
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
  identifier: EIS_ch3_0.243611335754395Vocp_1.csv
  session_description: In Vitro EIS
  session_start_time: 2024-05-13T22:04:00.338937-04:00
  timestamps_reference_time: 2024-05-13T22:04:00.338937-04:00


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/EIS_Impedance (DynamicTable) This table stores frequency, Z-real, Z-imaginary values of EIS experiment
  Dataset /acquisition/EIS_Impedance/frequency (VectorData)  | shape = (51,) | dtype = float64
  Dataset /acquisition/EIS_Impedance/id (ElementIdentifiers)  | shape = (51,) | dtype = int32
  Dataset /acquisition/EIS_Impedance/zimaginary (VectorData)  | shape = (51,) | dtype = float64
  Dataset /acquisition/EIS_Impedance/zreal (VectorData)  | shape = (51,) | dtype = float64
  file_create_date: ['2024-05-13T22:21:10.735454-04:00']
  Group /general/devices/Autolab (Device) Basic CSV data with no additional metadata
  experiment_description: In Vitro EIS
  experimenter: ['Qiwei Dong']
  Group /general/extracellular_ephys/G1_12A63 (ElectrodeGroup) electrode group
  Group /general/extracellular_ephys/G1_12A63/device (Device) Basic CSV data with no additional metadata
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
  identifier: EIS_ch19_0.163321495056152Vocp_1.csv
  session_description: In Vitro EIS
  session_start_time: 2024-05-13T22:21:10.735454-04:00
  timestamps_reference_time: 2024-05-13T22:21:10.735454-04:00


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/EIS_Impedance (DynamicTable) This table stores frequency, Z-real, Z-imaginary values of EIS experiment
  Dataset /acquisition/EIS_Impedance/frequency (VectorData)  | shape = (51,) | dtype = float64
  Dataset /acquisition/EIS_Impedance/id (ElementIdentifiers)  | shape = (51,) | dtype = int32
  Dataset /acquisition/EIS_Impedance/zimaginary (VectorData)  | shape = (51,) | dtype = float64
  Dataset /acquisition/EIS_Impedance/zreal (VectorData)  | shape = (51,) | dtype = float64
  file_create_date: ['2024-05-13T22:17:27.297856-04:00']
  Group /general/devices/Autolab (Device) Basic CSV data with no additional metadata
  experiment_description: In Vitro EIS
  experimenter: ['Qiwei Dong']
  Group /general/extracellular_ephys/G1_12A5D (ElectrodeGroup) electrode group
  Group /general/extracellular_ephys/G1_12A5D/device (Device) Basic CSV data with no additional metadata
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
  identifier: EIS_ch20_0.184238433837891Vocp_1.csv
  session_description: In Vitro EIS
  session_start_time: 2024-05-13T22:17:27.297856-04:00
  timestamps_reference_time: 2024-05-13T22:17:27.297856-04:00
