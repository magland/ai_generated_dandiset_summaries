
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001445/draft
name: In Vivo Electrochemical Impedance Spectroscopy - G3
contributor: [{'name': 'National Institutes of Health (NIH)', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/02qwkrw10', 'awardNumber': '1 UO1 NS 126052-01'}, {'name': 'Orazem, Mark', 'email': 'morazem@che.ufl.edu', 'schemaKey': 'Person', 'identifier': '0000-0003-3668-7767', 'includeInCitation': True}, {'name': 'Cogan, Stuart', 'email': 'stuart.cogan@utdallas.edu', 'schemaKey': 'Person', 'identifier': '0000-0001-6316-3032', 'includeInCitation': True}, {'name': 'Otto, Kevin', 'email': 'kevin.otto@bme.ufl.edu', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0002-2317-6194', 'includeInCitation': True}, {'name': 'Dong, QiWei', 'email': 'dongqiweialexander@gmail.com', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}]
description: Representative EIS data of G3 electrodes implanted in 4 rats, for the first 5 weeks. The map between electrode number and electrode diameter size (in um) is as follows:
1: 5, 2: 1, 3: 20, 4: 5, 5: 1, 6: 5, 7: 20, 8: 5, 9: 1, 10: 100,
11: 1, 12: 15, 13: 10, 14: 15, 15: 15, 16: 1, 17: 1, 18: 1, 19: 5, 20: 1,
21: 5, 22: 20, 23: 20, 24: 100, 25: 10, 26: 10, 27: 15, 28: 10, 29: 1, 30: 1, 
31: 1, 32: 10
assetsSummary: {'species': [{'name': 'Unidentified', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_32644'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 71855668, 'numberOfFiles': 353, 'numberOfSubjects': 4, 'variableMeasured': ['ElectrodeGroup'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 001445 has 100 NWB files.
83 of these NWB files are of type 1.
17 of these NWB files are of type 2.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/EIS_Impedance (DynamicTable) This table stores frequency, Z-real, Z-imaginary values of EIS experiment
  Dataset /acquisition/EIS_Impedance/frequency (VectorData)  | shape = (41,) | dtype = float64
  Dataset /acquisition/EIS_Impedance/id (ElementIdentifiers)  | shape = (41,) | dtype = int32
  Dataset /acquisition/EIS_Impedance/zimaginary (VectorData)  | shape = (41,) | dtype = float64
  Dataset /acquisition/EIS_Impedance/zreal (VectorData)  | shape = (41,) | dtype = float64
  file_create_date: ['2025-05-12T11:33:43.576163-04:00']
  Group /general/devices/Autolab (Device) Basic CSV data with no additional metadata
  experiment_description: In Vivo EIS
  experimenter: ['Qiwei Dong']
  Group /general/extracellular_ephys/G3_10 (ElectrodeGroup) electrode group
  Group /general/extracellular_ephys/G3_10/device (Device) Basic CSV data with no additional metadata
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
  identifier: EIS_ch15_-0.180539131164551Vocp_1.csv
  session_description: In Vivo EIS
  session_start_time: 2025-05-12T11:33:43.576163-04:00
  timestamps_reference_time: 2025-05-12T11:33:43.576163-04:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/EIS_Impedance (DynamicTable) This table stores frequency, Z-real, Z-imaginary values of EIS experiment
  Dataset /acquisition/EIS_Impedance/frequency (VectorData)  | shape = (41,) | dtype = float64
  Dataset /acquisition/EIS_Impedance/id (ElementIdentifiers)  | shape = (41,) | dtype = int32
  Dataset /acquisition/EIS_Impedance/zimaginary (VectorData)  | shape = (41,) | dtype = float64
  Dataset /acquisition/EIS_Impedance/zreal (VectorData)  | shape = (41,) | dtype = float64
  file_create_date: ['2025-05-12T12:10:36.208392-04:00']
  Group /general/devices/Autolab (Device) Basic CSV data with no additional metadata
  experiment_description: In Vivo EIS
  experimenter: ['Qiwei Dong']
  Group /general/extracellular_ephys/G3_11 (ElectrodeGroup) electrode group
  Group /general/extracellular_ephys/G3_11/device (Device) Basic CSV data with no additional metadata
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
  identifier: EIS_ch23_-0.139841079711914Vocp_4.csv
  session_description: In Vivo EIS
  session_start_time: 2025-05-12T12:10:36.208392-04:00
  timestamps_reference_time: 2025-05-12T12:10:36.208392-04:00
