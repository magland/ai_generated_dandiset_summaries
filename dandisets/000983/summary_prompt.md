
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000983/draft
name: In vitro electrochemical impedance spectroscopy data - materials
contributor: [{'name': 'National Institutes of Health (NIH)', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': '1 UO1 NS 126052-01', 'includeInCitation': False}, {'name': 'Orazem, Mark', 'email': 'morazem@che.ufl.edu', 'schemaKey': 'Person', 'identifier': '0000-0003-3668-7767', 'includeInCitation': True}, {'name': 'Cogan, Stuart', 'email': 'stuart.cogan@utdallas.edu', 'schemaKey': 'Person', 'identifier': '0000-0001-6316-3032', 'includeInCitation': True}, {'name': 'Otto, Kevin', 'email': 'kevin.otto@bme.ufl.edu', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0002-2317-6194', 'includeInCitation': True}]
description: Electrochemical impedance spectroscopy (EIS) data from multichannel microelectrode arrays coated with 
poly(3,4-ethylenedioxythiophene) (PEDOT),
sputtered iridium oxide (SIROF),
 ruthenium oxide (RuOx),
and Titanium nitride (TiN).
The project is supported by NIH 1U01NS126052-01.
assetsSummary: {'species': [{'name': 'Unidentified', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_32644'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 7441656, 'numberOfFiles': 38, 'numberOfSubjects': 66, 'variableMeasured': ['ElectrodeGroup'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000983 has 12 NWB files.
2 of these NWB files are of type 1.
3 of these NWB files are of type 2.
2 of these NWB files are of type 3.
3 of these NWB files are of type 4.
2 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/EIS_Impedance (DynamicTable) This table stores frequency, Z-real, Z-imaginary values of EIS experiment
  Dataset /acquisition/EIS_Impedance/frequency (VectorData)  | shape = (65,) | dtype = float64
  Dataset /acquisition/EIS_Impedance/id (ElementIdentifiers)  | shape = (65,) | dtype = int32
  Dataset /acquisition/EIS_Impedance/zimaginary (VectorData)  | shape = (65,) | dtype = float64
  Dataset /acquisition/EIS_Impedance/zreal (VectorData)  | shape = (65,) | dtype = float64
  file_create_date: ['2024-05-07T17:24:22.275002-05:00']
  Group /general/devices/GAMRY (Device) This device is used to measure impedance values of a Potentiostatic EIS experiment
  experiment_description: PEDOTPSS on Au_2000um2_after 50M pulses_invitro
  experimenter: ['Amirhossein Azami' ' Cogan Lab' ' UTD']
  Group /general/extracellular_ephys/PEDOTPSS on Au (ElectrodeGroup) electrode group
  Group /general/extracellular_ephys/PEDOTPSS on Au/device (Device) This device is used to measure impedance values of a Potentiostatic EIS experiment
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
  identifier: 1099_20240201_72_D.DTA
  session_description: PEDOTPSS on Au_2000um2_after 50M pulses_invitro
  session_start_time: 2024-02-01T14:50:10-04:56
  timestamps_reference_time: 2024-02-01T14:50:10-04:56


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/EIS_Impedance (DynamicTable) This table stores frequency, Z-real, Z-imaginary values of EIS experiment
  Dataset /acquisition/EIS_Impedance/frequency (VectorData)  | shape = (65,) | dtype = float64
  Dataset /acquisition/EIS_Impedance/id (ElementIdentifiers)  | shape = (65,) | dtype = int32
  Dataset /acquisition/EIS_Impedance/zimaginary (VectorData)  | shape = (65,) | dtype = float64
  Dataset /acquisition/EIS_Impedance/zreal (VectorData)  | shape = (65,) | dtype = float64
  file_create_date: ['2024-05-07T18:11:58.934939-05:00']
  Group /general/devices/GAMRY (Device) This device is used to measure impedance values of a Potentiostatic EIS experiment
  experiment_description: TiN_585nm_2000um2_in vitro
  experimenter: ['Justin Abbott' ' Cogan Lab' ' UTD']
  Group /general/extracellular_ephys/TiN_585nm (ElectrodeGroup) electrode group
  Group /general/extracellular_ephys/TiN_585nm/device (Device) This device is used to measure impedance values of a Potentiostatic EIS experiment
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
  identifier: 110503_E_2.DTA
  session_description: TiN_585nm_2000um2_in vitro
  session_start_time: 2024-04-25T14:46:33-04:56
  timestamps_reference_time: 2024-04-25T14:46:33-04:56


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/EIS_Impedance (DynamicTable) This table stores frequency, Z-real, Z-imaginary values of EIS experiment
  Dataset /acquisition/EIS_Impedance/frequency (VectorData)  | shape = (65,) | dtype = float64
  Dataset /acquisition/EIS_Impedance/id (ElementIdentifiers)  | shape = (65,) | dtype = int32
  Dataset /acquisition/EIS_Impedance/zimaginary (VectorData)  | shape = (65,) | dtype = float64
  Dataset /acquisition/EIS_Impedance/zreal (VectorData)  | shape = (65,) | dtype = float64
  file_create_date: ['2024-05-07T17:49:57.006819-05:00']
  Group /general/devices/GAMRY (Device) This device is used to measure impedance values of a Potentiostatic EIS experiment
  experiment_description: RuOx_15mTorr_310nm_2000um2_in vitro
  experimenter: ['Yupeng Wu' ' Cogan Lab' ' UTD']
  Group /general/extracellular_ephys/RuOx_15mTorr_310nm (ElectrodeGroup) electrode group
  Group /general/extracellular_ephys/RuOx_15mTorr_310nm/device (Device) This device is used to measure impedance values of a Potentiostatic EIS experiment
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
  identifier: 1092_56_A15b_2.DTA
  session_description: RuOx_15mTorr_310nm_2000um2_in vitro
  session_start_time: 2023-06-09T14:59:18-04:56
  timestamps_reference_time: 2023-06-09T14:59:18-04:56


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/EIS_Impedance (DynamicTable) This table stores frequency, Z-real, Z-imaginary values of EIS experiment
  Dataset /acquisition/EIS_Impedance/frequency (VectorData)  | shape = (65,) | dtype = float64
  Dataset /acquisition/EIS_Impedance/id (ElementIdentifiers)  | shape = (65,) | dtype = int32
  Dataset /acquisition/EIS_Impedance/zimaginary (VectorData)  | shape = (65,) | dtype = float64
  Dataset /acquisition/EIS_Impedance/zreal (VectorData)  | shape = (65,) | dtype = float64
  file_create_date: ['2024-05-07T18:17:22.437559-05:00']
  Group /general/devices/GAMRY (Device) This device is used to measure impedance values of a Potentiostatic EIS experiment
  experiment_description: TiN_900nm_2000um2_in vitro
  experimenter: ['Justin Abbott' ' Cogan Lab' ' UTD']
  Group /general/extracellular_ephys/TiN_900nm (ElectrodeGroup) electrode group
  Group /general/extracellular_ephys/TiN_900nm/device (Device) This device is used to measure impedance values of a Potentiostatic EIS experiment
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
  identifier: 110501_M_2.DTA
  session_description: TiN_900nm_2000um2_in vitro
  session_start_time: 2024-04-02T17:46:28-04:56
  timestamps_reference_time: 2024-04-02T17:46:28-04:56


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  Group /acquisition/EIS_Impedance (DynamicTable) This table stores frequency, Z-real, Z-imaginary values of EIS experiment
  Dataset /acquisition/EIS_Impedance/frequency (VectorData)  | shape = (61,) | dtype = float64
  Dataset /acquisition/EIS_Impedance/id (ElementIdentifiers)  | shape = (61,) | dtype = int32
  Dataset /acquisition/EIS_Impedance/zimaginary (VectorData)  | shape = (61,) | dtype = float64
  Dataset /acquisition/EIS_Impedance/zreal (VectorData)  | shape = (61,) | dtype = float64
  file_create_date: ['2024-05-07T18:31:13.474413-05:00']
  Group /general/devices/GAMRY (Device) This device is used to measure impedance values of a Potentiostatic EIS experiment
  experiment_description: RuOx_30mTorr_230nm_2000um2_in vitro
  experimenter: ['Yupeng Wu' ' Cogan Lab' ' UTD']
  Group /general/extracellular_ephys/RuOx_30mTorr_230nm (ElectrodeGroup) electrode group
  Group /general/extracellular_ephys/RuOx_30mTorr_230nm/device (Device) This device is used to measure impedance values of a Potentiostatic EIS experiment
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
  identifier: 1097_9_A7.DTA
  session_description: RuOx_30mTorr_230nm_2000um2_in vitro
  session_start_time: 2023-04-26T18:03:22-04:56
  timestamps_reference_time: 2023-04-26T18:03:22-04:56
