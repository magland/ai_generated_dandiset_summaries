
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000292/0.220708.1652
name: UHN whole-cell patch-clamp excitability recordings from mouse cortical neurons
contributor: [{'name': 'Howard, Derek', 'email': 'derekhoward@gmail.com', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0002-6621-9473', 'affiliation': [], 'includeInCitation': True}, {'name': 'Chameh, Homeira Moradi', 'email': 'homeira.moradi@uhnresearch.ca', 'roleName': ['dcite:Author', 'dcite:DataCollector', 'dcite:DataCurator'], 'schemaKey': 'Person', 'identifier': '0000-0002-8009-147X', 'affiliation': [{'name': 'Krembil Brain Institute, University Health Network', 'schemaKey': 'Affiliation'}], 'includeInCitation': True}, {'name': 'Valiante, Taufik', 'email': 'taufik.valiante@uhn.ca', 'roleName': ['dcite:DataCollector', 'dcite:Supervision'], 'schemaKey': 'Person', 'identifier': '0000-0002-3443-3790', 'affiliation': [{'name': 'Krembil Brain Institute, University Health Network', 'schemaKey': 'Affiliation'}], 'includeInCitation': True}, {'name': 'Tripathy, Shreejoy', 'email': 'shreejoy.tripathy@camh.ca', 'roleName': ['dcite:Conceptualization', 'dcite:DataCurator', 'dcite:Supervision'], 'schemaKey': 'Person', 'identifier': '0000-0002-1007-9061', 'affiliation': [], 'includeInCitation': True}]
description: Whole-cell patch clamp recordings from acute mouse brain slices of layer 5 cortex.
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 13764872, 'numberOfFiles': 11, 'numberOfSubjects': 11, 'variableMeasured': ['CurrentClampSeries', 'CurrentClampStimulusSeries', 'VoltageClampStimulusSeries'], 'measurementTechnique': [{'name': 'current clamp technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'voltage clamp technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000292 has 10 NWB files.
1 of these NWB files are of type 1.
1 of these NWB files are of type 2.
1 of these NWB files are of type 3.
4 of these NWB files are of type 4.
3 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Index_0_0_0 (CurrentClampSeries) {
      "comments": [
          "C4, L5, RMP: --59.4 mv"
      ],
      "file_name": "18118024.abf",
      "file_version": "1.8.3.0",
      "protocol": "I-V curve ,-400 pA",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\WNP\\I-V curve ,-400 pA.pro",
      "sweep_number": 0
  }
  Group /acquisition/Index_0_0_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_0_0/electrode/device (Device) 
  Group /acquisition/Index_0_10_0 (CurrentClampSeries) {
      "comments": [
          "C4, L5, RMP: --59.4 mv"
      ],
      "file_name": "18118024.abf",
      "file_version": "1.8.3.0",
      "protocol": "I-V curve ,-400 pA",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\WNP\\I-V curve ,-400 pA.pro",
      "sweep_number": 10
  }
  Group /acquisition/Index_0_10_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_10_0/electrode/device (Device) 
  Group /acquisition/Index_0_11_0 (CurrentClampSeries) {
      "comments": [
          "C4, L5, RMP: --59.4 mv"
      ],
      "file_name": "18118024.abf",
      "file_version": "1.8.3.0",
      "protocol": "I-V curve ,-400 pA",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\WNP\\I-V curve ,-400 pA.pro",
      "sweep_number": 11
  }
  Group /acquisition/Index_0_11_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_11_0/electrode/device (Device) 
  Group /acquisition/Index_0_12_0 (CurrentClampSeries) {
      "comments": [
          "C4, L5, RMP: --59.4 mv"
      ],
      "file_name": "18118024.abf",
      "file_version": "1.8.3.0",
      "protocol": "I-V curve ,-400 pA",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\WNP\\I-V curve ,-400 pA.pro",
      "sweep_number": 12
  }
  Group /acquisition/Index_0_12_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_12_0/electrode/device (Device) 
  Group /acquisition/Index_0_13_0 (CurrentClampSeries) {
      "comments": [
          "C4, L5, RMP: --59.4 mv"
      ],
      "file_name": "18118024.abf",
      "file_version": "1.8.3.0",
      "protocol": "I-V curve ,-400 pA",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\WNP\\I-V curve ,-400 pA.pro",
      "sweep_number": 13
  }
  Group /acquisition/Index_0_13_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_13_0/electrode/device (Device) 
  Group /acquisition/Index_0_14_0 (CurrentClampSeries) {
      "comments": [
          "C4, L5, RMP: --59.4 mv"
      ],
      "file_name": "18118024.abf",
      "file_version": "1.8.3.0",
      "protocol": "I-V curve ,-400 pA",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\WNP\\I-V curve ,-400 pA.pro",
      "sweep_number": 14
  }
  Group /acquisition/Index_0_14_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_14_0/electrode/device (Device) 
  Group /acquisition/Index_0_15_0 (CurrentClampSeries) {
      "comments": [
          "C4, L5, RMP: --59.4 mv"
      ],
      "file_name": "18118024.abf",
      "file_version": "1.8.3.0",
      "protocol": "I-V curve ,-400 pA",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\WNP\\I-V curve ,-400 pA.pro",
      "sweep_number": 15
  }
  Group /acquisition/Index_0_15_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_15_0/electrode/device (Device) 
  Group /acquisition/Index_0_1_0 (CurrentClampSeries) {
      "comments": [
          "C4, L5, RMP: --59.4 mv"
      ],
      "file_name": "18118024.abf",
      "file_version": "1.8.3.0",
      "protocol": "I-V curve ,-400 pA",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\WNP\\I-V curve ,-400 pA.pro",
      "sweep_number": 1
  }
  Group /acquisition/Index_0_1_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_1_0/electrode/device (Device) 
  Group /acquisition/Index_0_2_0 (CurrentClampSeries) {
      "comments": [
          "C4, L5, RMP: --59.4 mv"
      ],
      "file_name": "18118024.abf",
      "file_version": "1.8.3.0",
      "protocol": "I-V curve ,-400 pA",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\WNP\\I-V curve ,-400 pA.pro",
      "sweep_number": 2
  }
  Group /acquisition/Index_0_2_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_2_0/electrode/device (Device) 
  Group /acquisition/Index_0_3_0 (CurrentClampSeries) {
      "comments": [
          "C4, L5, RMP: --59.4 mv"
      ],
      "file_name": "18118024.abf",
      "file_version": "1.8.3.0",
      "protocol": "I-V curve ,-400 pA",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\WNP\\I-V curve ,-400 pA.pro",
      "sweep_number": 3
  }
  Group /acquisition/Index_0_3_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_3_0/electrode/device (Device) 
  Group /acquisition/Index_0_4_0 (CurrentClampSeries) {
      "comments": [
          "C4, L5, RMP: --59.4 mv"
      ],
      "file_name": "18118024.abf",
      "file_version": "1.8.3.0",
      "protocol": "I-V curve ,-400 pA",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\WNP\\I-V curve ,-400 pA.pro",
      "sweep_number": 4
  }
  Group /acquisition/Index_0_4_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_4_0/electrode/device (Device) 
  Group /acquisition/Index_0_5_0 (CurrentClampSeries) {
      "comments": [
          "C4, L5, RMP: --59.4 mv"
      ],
      "file_name": "18118024.abf",
      "file_version": "1.8.3.0",
      "protocol": "I-V curve ,-400 pA",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\WNP\\I-V curve ,-400 pA.pro",
      "sweep_number": 5
  }
  Group /acquisition/Index_0_5_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_5_0/electrode/device (Device) 
  Group /acquisition/Index_0_6_0 (CurrentClampSeries) {
      "comments": [
          "C4, L5, RMP: --59.4 mv"
      ],
      "file_name": "18118024.abf",
      "file_version": "1.8.3.0",
      "protocol": "I-V curve ,-400 pA",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\WNP\\I-V curve ,-400 pA.pro",
      "sweep_number": 6
  }
  Group /acquisition/Index_0_6_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_6_0/electrode/device (Device) 
  Group /acquisition/Index_0_7_0 (CurrentClampSeries) {
      "comments": [
          "C4, L5, RMP: --59.4 mv"
      ],
      "file_name": "18118024.abf",
      "file_version": "1.8.3.0",
      "protocol": "I-V curve ,-400 pA",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\WNP\\I-V curve ,-400 pA.pro",
      "sweep_number": 7
  }
  Group /acquisition/Index_0_7_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_7_0/electrode/device (Device) 
  Group /acquisition/Index_0_8_0 (CurrentClampSeries) {
      "comments": [
          "C4, L5, RMP: --59.4 mv"
      ],
      "file_name": "18118024.abf",
      "file_version": "1.8.3.0",
      "protocol": "I-V curve ,-400 pA",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\WNP\\I-V curve ,-400 pA.pro",
      "sweep_number": 8
  }
  Group /acquisition/Index_0_8_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_8_0/electrode/device (Device) 
  Group /acquisition/Index_0_9_0 (CurrentClampSeries) {
      "comments": [
          "C4, L5, RMP: --59.4 mv"
      ],
      "file_name": "18118024.abf",
      "file_version": "1.8.3.0",
      "protocol": "I-V curve ,-400 pA",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\WNP\\I-V curve ,-400 pA.pro",
      "sweep_number": 9
  }
  Group /acquisition/Index_0_9_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_9_0/electrode/device (Device) 
  file_create_date: ['2022-07-07T17:52:23.800907-04:00']
  Group /general/devices/Clampex 9.2.1.9 (Device) 
  experiment_description: 
  Group /general/intracellular_ephys/elec0 (IntracellularElectrode) 
  Group /general/intracellular_ephys/elec0/device (Device) 
  Group /general/intracellular_ephys/sweep_table (SweepTable) A sweep table groups different PatchClampSeries together.
  Dataset /general/intracellular_ephys/sweep_table/id (ElementIdentifiers)  | shape = (32,) | dtype = int64
  Dataset /general/intracellular_ephys/sweep_table/series (VectorData) PatchClampSeries with the same sweep number | shape = (32,) | dtype = object
  Dataset /general/intracellular_ephys/sweep_table/series_index (VectorIndex) Index for VectorData 'series' | shape = (32,) | dtype = uint8
  Dataset /general/intracellular_ephys/sweep_table/sweep_number (VectorData) Sweep number of the entries in that row | shape = (32,) | dtype = uint32
  notes: 
  session_id: PLACEHOLDER
  source_script: {
      "git_revision": "(main) 0.2.2-11-g54c8f8d",
      "package_version": "0.2.2+11.g54c8f8d",
      "repo": "https://github.com/byte-physics/x-to-nwb"
  }
  Group /general/subject (Subject) 
  identifier: 18118024.abf
  session_description: PLACEHOLDER
  session_start_time: 2018-01-18T14:11:46.671000-05:00
  Group /stimulus/presentation/Index_0_0_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C4, L5, RMP: --59.4 mv"
      ],
      "file_name": "18118024.abf",
      "file_version": "1.8.3.0",
      "protocol": "I-V curve ,-400 pA",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\WNP\\I-V curve ,-400 pA.pro",
      "sweep_number": 0
  }
  Group /stimulus/presentation/Index_0_0_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_0_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_10_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C4, L5, RMP: --59.4 mv"
      ],
      "file_name": "18118024.abf",
      "file_version": "1.8.3.0",
      "protocol": "I-V curve ,-400 pA",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\WNP\\I-V curve ,-400 pA.pro",
      "sweep_number": 10
  }
  Group /stimulus/presentation/Index_0_10_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_10_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_11_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C4, L5, RMP: --59.4 mv"
      ],
      "file_name": "18118024.abf",
      "file_version": "1.8.3.0",
      "protocol": "I-V curve ,-400 pA",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\WNP\\I-V curve ,-400 pA.pro",
      "sweep_number": 11
  }
  Group /stimulus/presentation/Index_0_11_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_11_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_12_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C4, L5, RMP: --59.4 mv"
      ],
      "file_name": "18118024.abf",
      "file_version": "1.8.3.0",
      "protocol": "I-V curve ,-400 pA",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\WNP\\I-V curve ,-400 pA.pro",
      "sweep_number": 12
  }
  Group /stimulus/presentation/Index_0_12_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_12_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_13_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C4, L5, RMP: --59.4 mv"
      ],
      "file_name": "18118024.abf",
      "file_version": "1.8.3.0",
      "protocol": "I-V curve ,-400 pA",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\WNP\\I-V curve ,-400 pA.pro",
      "sweep_number": 13
  }
  Group /stimulus/presentation/Index_0_13_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_13_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_14_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C4, L5, RMP: --59.4 mv"
      ],
      "file_name": "18118024.abf",
      "file_version": "1.8.3.0",
      "protocol": "I-V curve ,-400 pA",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\WNP\\I-V curve ,-400 pA.pro",
      "sweep_number": 14
  }
  Group /stimulus/presentation/Index_0_14_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_14_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_15_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C4, L5, RMP: --59.4 mv"
      ],
      "file_name": "18118024.abf",
      "file_version": "1.8.3.0",
      "protocol": "I-V curve ,-400 pA",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\WNP\\I-V curve ,-400 pA.pro",
      "sweep_number": 15
  }
  Group /stimulus/presentation/Index_0_15_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_15_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_1_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C4, L5, RMP: --59.4 mv"
      ],
      "file_name": "18118024.abf",
      "file_version": "1.8.3.0",
      "protocol": "I-V curve ,-400 pA",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\WNP\\I-V curve ,-400 pA.pro",
      "sweep_number": 1
  }
  Group /stimulus/presentation/Index_0_1_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_1_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_2_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C4, L5, RMP: --59.4 mv"
      ],
      "file_name": "18118024.abf",
      "file_version": "1.8.3.0",
      "protocol": "I-V curve ,-400 pA",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\WNP\\I-V curve ,-400 pA.pro",
      "sweep_number": 2
  }
  Group /stimulus/presentation/Index_0_2_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_2_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_3_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C4, L5, RMP: --59.4 mv"
      ],
      "file_name": "18118024.abf",
      "file_version": "1.8.3.0",
      "protocol": "I-V curve ,-400 pA",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\WNP\\I-V curve ,-400 pA.pro",
      "sweep_number": 3
  }
  Group /stimulus/presentation/Index_0_3_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_3_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_4_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C4, L5, RMP: --59.4 mv"
      ],
      "file_name": "18118024.abf",
      "file_version": "1.8.3.0",
      "protocol": "I-V curve ,-400 pA",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\WNP\\I-V curve ,-400 pA.pro",
      "sweep_number": 4
  }
  Group /stimulus/presentation/Index_0_4_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_4_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_5_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C4, L5, RMP: --59.4 mv"
      ],
      "file_name": "18118024.abf",
      "file_version": "1.8.3.0",
      "protocol": "I-V curve ,-400 pA",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\WNP\\I-V curve ,-400 pA.pro",
      "sweep_number": 5
  }
  Group /stimulus/presentation/Index_0_5_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_5_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_6_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C4, L5, RMP: --59.4 mv"
      ],
      "file_name": "18118024.abf",
      "file_version": "1.8.3.0",
      "protocol": "I-V curve ,-400 pA",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\WNP\\I-V curve ,-400 pA.pro",
      "sweep_number": 6
  }
  Group /stimulus/presentation/Index_0_6_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_6_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_7_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C4, L5, RMP: --59.4 mv"
      ],
      "file_name": "18118024.abf",
      "file_version": "1.8.3.0",
      "protocol": "I-V curve ,-400 pA",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\WNP\\I-V curve ,-400 pA.pro",
      "sweep_number": 7
  }
  Group /stimulus/presentation/Index_0_7_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_7_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_8_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C4, L5, RMP: --59.4 mv"
      ],
      "file_name": "18118024.abf",
      "file_version": "1.8.3.0",
      "protocol": "I-V curve ,-400 pA",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\WNP\\I-V curve ,-400 pA.pro",
      "sweep_number": 8
  }
  Group /stimulus/presentation/Index_0_8_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_8_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_9_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C4, L5, RMP: --59.4 mv"
      ],
      "file_name": "18118024.abf",
      "file_version": "1.8.3.0",
      "protocol": "I-V curve ,-400 pA",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\WNP\\I-V curve ,-400 pA.pro",
      "sweep_number": 9
  }
  Group /stimulus/presentation/Index_0_9_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_9_1/electrode/device (Device) 
  timestamps_reference_time: 2018-01-18T14:11:46.671000-05:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Index_0_0_0 (CurrentClampSeries) {
      "comments": [
          "C5,  L5, RMP: -75.2 mv"
      ],
      "file_name": "18130014.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 0
  }
  Group /acquisition/Index_0_0_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_0_0/electrode/device (Device) 
  Group /acquisition/Index_0_10_0 (CurrentClampSeries) {
      "comments": [
          "C5,  L5, RMP: -75.2 mv"
      ],
      "file_name": "18130014.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 10
  }
  Group /acquisition/Index_0_10_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_10_0/electrode/device (Device) 
  Group /acquisition/Index_0_1_0 (CurrentClampSeries) {
      "comments": [
          "C5,  L5, RMP: -75.2 mv"
      ],
      "file_name": "18130014.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 1
  }
  Group /acquisition/Index_0_1_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_1_0/electrode/device (Device) 
  Group /acquisition/Index_0_2_0 (CurrentClampSeries) {
      "comments": [
          "C5,  L5, RMP: -75.2 mv"
      ],
      "file_name": "18130014.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 2
  }
  Group /acquisition/Index_0_2_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_2_0/electrode/device (Device) 
  Group /acquisition/Index_0_3_0 (CurrentClampSeries) {
      "comments": [
          "C5,  L5, RMP: -75.2 mv"
      ],
      "file_name": "18130014.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 3
  }
  Group /acquisition/Index_0_3_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_3_0/electrode/device (Device) 
  Group /acquisition/Index_0_4_0 (CurrentClampSeries) {
      "comments": [
          "C5,  L5, RMP: -75.2 mv"
      ],
      "file_name": "18130014.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 4
  }
  Group /acquisition/Index_0_4_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_4_0/electrode/device (Device) 
  Group /acquisition/Index_0_5_0 (CurrentClampSeries) {
      "comments": [
          "C5,  L5, RMP: -75.2 mv"
      ],
      "file_name": "18130014.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 5
  }
  Group /acquisition/Index_0_5_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_5_0/electrode/device (Device) 
  Group /acquisition/Index_0_6_0 (CurrentClampSeries) {
      "comments": [
          "C5,  L5, RMP: -75.2 mv"
      ],
      "file_name": "18130014.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 6
  }
  Group /acquisition/Index_0_6_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_6_0/electrode/device (Device) 
  Group /acquisition/Index_0_7_0 (CurrentClampSeries) {
      "comments": [
          "C5,  L5, RMP: -75.2 mv"
      ],
      "file_name": "18130014.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 7
  }
  Group /acquisition/Index_0_7_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_7_0/electrode/device (Device) 
  Group /acquisition/Index_0_8_0 (CurrentClampSeries) {
      "comments": [
          "C5,  L5, RMP: -75.2 mv"
      ],
      "file_name": "18130014.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 8
  }
  Group /acquisition/Index_0_8_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_8_0/electrode/device (Device) 
  Group /acquisition/Index_0_9_0 (CurrentClampSeries) {
      "comments": [
          "C5,  L5, RMP: -75.2 mv"
      ],
      "file_name": "18130014.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 9
  }
  Group /acquisition/Index_0_9_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_9_0/electrode/device (Device) 
  file_create_date: ['2022-07-07T17:52:19.283357-04:00']
  Group /general/devices/Clampex 9.2.1.9 (Device) 
  experiment_description: 
  Group /general/intracellular_ephys/elec0 (IntracellularElectrode) 
  Group /general/intracellular_ephys/elec0/device (Device) 
  Group /general/intracellular_ephys/sweep_table (SweepTable) A sweep table groups different PatchClampSeries together.
  Dataset /general/intracellular_ephys/sweep_table/id (ElementIdentifiers)  | shape = (22,) | dtype = int64
  Dataset /general/intracellular_ephys/sweep_table/series (VectorData) PatchClampSeries with the same sweep number | shape = (22,) | dtype = object
  Dataset /general/intracellular_ephys/sweep_table/series_index (VectorIndex) Index for VectorData 'series' | shape = (22,) | dtype = uint8
  Dataset /general/intracellular_ephys/sweep_table/sweep_number (VectorData) Sweep number of the entries in that row | shape = (22,) | dtype = uint32
  notes: 
  session_id: PLACEHOLDER
  source_script: {
      "git_revision": "(main) 0.2.2-11-g54c8f8d",
      "package_version": "0.2.2+11.g54c8f8d",
      "repo": "https://github.com/byte-physics/x-to-nwb"
  }
  Group /general/subject (Subject) 
  identifier: 18130014.abf
  session_description: PLACEHOLDER
  session_start_time: 2018-01-30T15:57:40.031000-05:00
  Group /stimulus/presentation/Index_0_0_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C5,  L5, RMP: -75.2 mv"
      ],
      "file_name": "18130014.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 0
  }
  Group /stimulus/presentation/Index_0_0_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_0_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_10_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C5,  L5, RMP: -75.2 mv"
      ],
      "file_name": "18130014.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 10
  }
  Group /stimulus/presentation/Index_0_10_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_10_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_1_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C5,  L5, RMP: -75.2 mv"
      ],
      "file_name": "18130014.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 1
  }
  Group /stimulus/presentation/Index_0_1_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_1_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_2_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C5,  L5, RMP: -75.2 mv"
      ],
      "file_name": "18130014.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 2
  }
  Group /stimulus/presentation/Index_0_2_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_2_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_3_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C5,  L5, RMP: -75.2 mv"
      ],
      "file_name": "18130014.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 3
  }
  Group /stimulus/presentation/Index_0_3_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_3_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_4_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C5,  L5, RMP: -75.2 mv"
      ],
      "file_name": "18130014.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 4
  }
  Group /stimulus/presentation/Index_0_4_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_4_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_5_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C5,  L5, RMP: -75.2 mv"
      ],
      "file_name": "18130014.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 5
  }
  Group /stimulus/presentation/Index_0_5_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_5_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_6_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C5,  L5, RMP: -75.2 mv"
      ],
      "file_name": "18130014.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 6
  }
  Group /stimulus/presentation/Index_0_6_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_6_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_7_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C5,  L5, RMP: -75.2 mv"
      ],
      "file_name": "18130014.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 7
  }
  Group /stimulus/presentation/Index_0_7_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_7_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_8_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C5,  L5, RMP: -75.2 mv"
      ],
      "file_name": "18130014.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 8
  }
  Group /stimulus/presentation/Index_0_8_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_8_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_9_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C5,  L5, RMP: -75.2 mv"
      ],
      "file_name": "18130014.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 9
  }
  Group /stimulus/presentation/Index_0_9_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_9_1/electrode/device (Device) 
  timestamps_reference_time: 2018-01-30T15:57:40.031000-05:00


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Index_0_0_0 (CurrentClampSeries) {
      "comments": [
          "C6 RMP -63..2 mv;layer 5,",
          "C6 RMP -63..2 mv;layer 5,"
      ],
      "file_name": "18208024.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 0
  }
  Group /acquisition/Index_0_0_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_0_0/electrode/device (Device) 
  Group /acquisition/Index_0_10_0 (CurrentClampSeries) {
      "comments": [
          "C6 RMP -63..2 mv;layer 5,",
          "C6 RMP -63..2 mv;layer 5,"
      ],
      "file_name": "18208024.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 10
  }
  Group /acquisition/Index_0_10_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_10_0/electrode/device (Device) 
  Group /acquisition/Index_0_11_0 (CurrentClampSeries) {
      "comments": [
          "C6 RMP -63..2 mv;layer 5,",
          "C6 RMP -63..2 mv;layer 5,"
      ],
      "file_name": "18208024.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 11
  }
  Group /acquisition/Index_0_11_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_11_0/electrode/device (Device) 
  Group /acquisition/Index_0_1_0 (CurrentClampSeries) {
      "comments": [
          "C6 RMP -63..2 mv;layer 5,",
          "C6 RMP -63..2 mv;layer 5,"
      ],
      "file_name": "18208024.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 1
  }
  Group /acquisition/Index_0_1_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_1_0/electrode/device (Device) 
  Group /acquisition/Index_0_2_0 (CurrentClampSeries) {
      "comments": [
          "C6 RMP -63..2 mv;layer 5,",
          "C6 RMP -63..2 mv;layer 5,"
      ],
      "file_name": "18208024.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 2
  }
  Group /acquisition/Index_0_2_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_2_0/electrode/device (Device) 
  Group /acquisition/Index_0_3_0 (CurrentClampSeries) {
      "comments": [
          "C6 RMP -63..2 mv;layer 5,",
          "C6 RMP -63..2 mv;layer 5,"
      ],
      "file_name": "18208024.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 3
  }
  Group /acquisition/Index_0_3_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_3_0/electrode/device (Device) 
  Group /acquisition/Index_0_4_0 (CurrentClampSeries) {
      "comments": [
          "C6 RMP -63..2 mv;layer 5,",
          "C6 RMP -63..2 mv;layer 5,"
      ],
      "file_name": "18208024.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 4
  }
  Group /acquisition/Index_0_4_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_4_0/electrode/device (Device) 
  Group /acquisition/Index_0_5_0 (CurrentClampSeries) {
      "comments": [
          "C6 RMP -63..2 mv;layer 5,",
          "C6 RMP -63..2 mv;layer 5,"
      ],
      "file_name": "18208024.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 5
  }
  Group /acquisition/Index_0_5_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_5_0/electrode/device (Device) 
  Group /acquisition/Index_0_6_0 (CurrentClampSeries) {
      "comments": [
          "C6 RMP -63..2 mv;layer 5,",
          "C6 RMP -63..2 mv;layer 5,"
      ],
      "file_name": "18208024.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 6
  }
  Group /acquisition/Index_0_6_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_6_0/electrode/device (Device) 
  Group /acquisition/Index_0_7_0 (CurrentClampSeries) {
      "comments": [
          "C6 RMP -63..2 mv;layer 5,",
          "C6 RMP -63..2 mv;layer 5,"
      ],
      "file_name": "18208024.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 7
  }
  Group /acquisition/Index_0_7_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_7_0/electrode/device (Device) 
  Group /acquisition/Index_0_8_0 (CurrentClampSeries) {
      "comments": [
          "C6 RMP -63..2 mv;layer 5,",
          "C6 RMP -63..2 mv;layer 5,"
      ],
      "file_name": "18208024.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 8
  }
  Group /acquisition/Index_0_8_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_8_0/electrode/device (Device) 
  Group /acquisition/Index_0_9_0 (CurrentClampSeries) {
      "comments": [
          "C6 RMP -63..2 mv;layer 5,",
          "C6 RMP -63..2 mv;layer 5,"
      ],
      "file_name": "18208024.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 9
  }
  Group /acquisition/Index_0_9_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_9_0/electrode/device (Device) 
  file_create_date: ['2022-07-07T17:52:22.644759-04:00']
  Group /general/devices/Clampex 9.2.1.9 (Device) 
  experiment_description: 
  Group /general/intracellular_ephys/elec0 (IntracellularElectrode) 
  Group /general/intracellular_ephys/elec0/device (Device) 
  Group /general/intracellular_ephys/sweep_table (SweepTable) A sweep table groups different PatchClampSeries together.
  Dataset /general/intracellular_ephys/sweep_table/id (ElementIdentifiers)  | shape = (24,) | dtype = int64
  Dataset /general/intracellular_ephys/sweep_table/series (VectorData) PatchClampSeries with the same sweep number | shape = (24,) | dtype = object
  Dataset /general/intracellular_ephys/sweep_table/series_index (VectorIndex) Index for VectorData 'series' | shape = (24,) | dtype = uint8
  Dataset /general/intracellular_ephys/sweep_table/sweep_number (VectorData) Sweep number of the entries in that row | shape = (24,) | dtype = uint32
  notes: 
  session_id: PLACEHOLDER
  source_script: {
      "git_revision": "(main) 0.2.2-11-g54c8f8d",
      "package_version": "0.2.2+11.g54c8f8d",
      "repo": "https://github.com/byte-physics/x-to-nwb"
  }
  Group /general/subject (Subject) 
  identifier: 18208024.abf
  session_description: PLACEHOLDER
  session_start_time: 2018-02-08T17:12:25.687000-05:00
  Group /stimulus/presentation/Index_0_0_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C6 RMP -63..2 mv;layer 5,",
          "C6 RMP -63..2 mv;layer 5,"
      ],
      "file_name": "18208024.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 0
  }
  Group /stimulus/presentation/Index_0_0_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_0_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_10_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C6 RMP -63..2 mv;layer 5,",
          "C6 RMP -63..2 mv;layer 5,"
      ],
      "file_name": "18208024.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 10
  }
  Group /stimulus/presentation/Index_0_10_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_10_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_11_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C6 RMP -63..2 mv;layer 5,",
          "C6 RMP -63..2 mv;layer 5,"
      ],
      "file_name": "18208024.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 11
  }
  Group /stimulus/presentation/Index_0_11_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_11_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_1_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C6 RMP -63..2 mv;layer 5,",
          "C6 RMP -63..2 mv;layer 5,"
      ],
      "file_name": "18208024.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 1
  }
  Group /stimulus/presentation/Index_0_1_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_1_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_2_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C6 RMP -63..2 mv;layer 5,",
          "C6 RMP -63..2 mv;layer 5,"
      ],
      "file_name": "18208024.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 2
  }
  Group /stimulus/presentation/Index_0_2_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_2_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_3_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C6 RMP -63..2 mv;layer 5,",
          "C6 RMP -63..2 mv;layer 5,"
      ],
      "file_name": "18208024.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 3
  }
  Group /stimulus/presentation/Index_0_3_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_3_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_4_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C6 RMP -63..2 mv;layer 5,",
          "C6 RMP -63..2 mv;layer 5,"
      ],
      "file_name": "18208024.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 4
  }
  Group /stimulus/presentation/Index_0_4_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_4_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_5_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C6 RMP -63..2 mv;layer 5,",
          "C6 RMP -63..2 mv;layer 5,"
      ],
      "file_name": "18208024.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 5
  }
  Group /stimulus/presentation/Index_0_5_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_5_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_6_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C6 RMP -63..2 mv;layer 5,",
          "C6 RMP -63..2 mv;layer 5,"
      ],
      "file_name": "18208024.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 6
  }
  Group /stimulus/presentation/Index_0_6_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_6_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_7_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C6 RMP -63..2 mv;layer 5,",
          "C6 RMP -63..2 mv;layer 5,"
      ],
      "file_name": "18208024.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 7
  }
  Group /stimulus/presentation/Index_0_7_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_7_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_8_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C6 RMP -63..2 mv;layer 5,",
          "C6 RMP -63..2 mv;layer 5,"
      ],
      "file_name": "18208024.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 8
  }
  Group /stimulus/presentation/Index_0_8_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_8_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_9_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C6 RMP -63..2 mv;layer 5,",
          "C6 RMP -63..2 mv;layer 5,"
      ],
      "file_name": "18208024.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 9
  }
  Group /stimulus/presentation/Index_0_9_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_9_1/electrode/device (Device) 
  timestamps_reference_time: 2018-02-08T17:12:25.687000-05:00


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/index_00 (CurrentClampSeries) {
      "cycle_id": 0,
      "file": "19o22001.abf",
      "name": "Vm_sec",
      "number": 2,
      "protocol": "I-V curve ,-400 pA",
      "protocolPath": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\I-V curve ,-400 pA.pro"
  }
  Group /acquisition/index_00/electrode (IntracellularElectrode) 
  Group /acquisition/index_00/electrode/device (Device) 
  Group /acquisition/index_01 (CurrentClampSeries) {
      "cycle_id": 1,
      "file": "19o22001.abf",
      "name": "Vm_sec",
      "number": 2,
      "protocol": "I-V curve ,-400 pA",
      "protocolPath": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\I-V curve ,-400 pA.pro"
  }
  Group /acquisition/index_01/electrode (IntracellularElectrode) 
  Group /acquisition/index_01/electrode/device (Device) 
  Group /acquisition/index_02 (CurrentClampSeries) {
      "cycle_id": 2,
      "file": "19o22001.abf",
      "name": "Vm_sec",
      "number": 2,
      "protocol": "I-V curve ,-400 pA",
      "protocolPath": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\I-V curve ,-400 pA.pro"
  }
  Group /acquisition/index_02/electrode (IntracellularElectrode) 
  Group /acquisition/index_02/electrode/device (Device) 
  Group /acquisition/index_03 (CurrentClampSeries) {
      "cycle_id": 3,
      "file": "19o22001.abf",
      "name": "Vm_sec",
      "number": 2,
      "protocol": "I-V curve ,-400 pA",
      "protocolPath": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\I-V curve ,-400 pA.pro"
  }
  Group /acquisition/index_03/electrode (IntracellularElectrode) 
  Group /acquisition/index_03/electrode/device (Device) 
  Group /acquisition/index_04 (CurrentClampSeries) {
      "cycle_id": 4,
      "file": "19o22001.abf",
      "name": "Vm_sec",
      "number": 2,
      "protocol": "I-V curve ,-400 pA",
      "protocolPath": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\I-V curve ,-400 pA.pro"
  }
  Group /acquisition/index_04/electrode (IntracellularElectrode) 
  Group /acquisition/index_04/electrode/device (Device) 
  Group /acquisition/index_05 (CurrentClampSeries) {
      "cycle_id": 5,
      "file": "19o22001.abf",
      "name": "Vm_sec",
      "number": 2,
      "protocol": "I-V curve ,-400 pA",
      "protocolPath": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\I-V curve ,-400 pA.pro"
  }
  Group /acquisition/index_05/electrode (IntracellularElectrode) 
  Group /acquisition/index_05/electrode/device (Device) 
  Group /acquisition/index_06 (CurrentClampSeries) {
      "cycle_id": 6,
      "file": "19o22001.abf",
      "name": "Vm_sec",
      "number": 2,
      "protocol": "I-V curve ,-400 pA",
      "protocolPath": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\I-V curve ,-400 pA.pro"
  }
  Group /acquisition/index_06/electrode (IntracellularElectrode) 
  Group /acquisition/index_06/electrode/device (Device) 
  Group /acquisition/index_07 (CurrentClampSeries) {
      "cycle_id": 7,
      "file": "19o22001.abf",
      "name": "Vm_sec",
      "number": 2,
      "protocol": "I-V curve ,-400 pA",
      "protocolPath": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\I-V curve ,-400 pA.pro"
  }
  Group /acquisition/index_07/electrode (IntracellularElectrode) 
  Group /acquisition/index_07/electrode/device (Device) 
  Group /acquisition/index_08 (CurrentClampSeries) {
      "cycle_id": 8,
      "file": "19o22001.abf",
      "name": "Vm_sec",
      "number": 2,
      "protocol": "I-V curve ,-400 pA",
      "protocolPath": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\I-V curve ,-400 pA.pro"
  }
  Group /acquisition/index_08/electrode (IntracellularElectrode) 
  Group /acquisition/index_08/electrode/device (Device) 
  Group /acquisition/index_09 (CurrentClampSeries) {
      "cycle_id": 9,
      "file": "19o22001.abf",
      "name": "Vm_sec",
      "number": 2,
      "protocol": "I-V curve ,-400 pA",
      "protocolPath": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\I-V curve ,-400 pA.pro"
  }
  Group /acquisition/index_09/electrode (IntracellularElectrode) 
  Group /acquisition/index_09/electrode/device (Device) 
  Group /acquisition/index_10 (CurrentClampSeries) {
      "cycle_id": 10,
      "file": "19o22001.abf",
      "name": "Vm_sec",
      "number": 2,
      "protocol": "I-V curve ,-400 pA",
      "protocolPath": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\I-V curve ,-400 pA.pro"
  }
  Group /acquisition/index_10/electrode (IntracellularElectrode) 
  Group /acquisition/index_10/electrode/device (Device) 
  Group /acquisition/index_11 (CurrentClampSeries) {
      "cycle_id": 11,
      "file": "19o22001.abf",
      "name": "Vm_sec",
      "number": 2,
      "protocol": "I-V curve ,-400 pA",
      "protocolPath": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\I-V curve ,-400 pA.pro"
  }
  Group /acquisition/index_11/electrode (IntracellularElectrode) 
  Group /acquisition/index_11/electrode/device (Device) 
  Group /acquisition/index_12 (CurrentClampSeries) {
      "cycle_id": 12,
      "file": "19o22001.abf",
      "name": "Vm_sec",
      "number": 2,
      "protocol": "I-V curve ,-400 pA",
      "protocolPath": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\I-V curve ,-400 pA.pro"
  }
  Group /acquisition/index_12/electrode (IntracellularElectrode) 
  Group /acquisition/index_12/electrode/device (Device) 
  Group /acquisition/index_13 (CurrentClampSeries) {
      "cycle_id": 13,
      "file": "19o22001.abf",
      "name": "Vm_sec",
      "number": 2,
      "protocol": "I-V curve ,-400 pA",
      "protocolPath": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\I-V curve ,-400 pA.pro"
  }
  Group /acquisition/index_13/electrode (IntracellularElectrode) 
  Group /acquisition/index_13/electrode/device (Device) 
  Group /acquisition/index_14 (CurrentClampSeries) {
      "cycle_id": 14,
      "file": "19o22001.abf",
      "name": "Vm_sec",
      "number": 2,
      "protocol": "I-V curve ,-400 pA",
      "protocolPath": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\I-V curve ,-400 pA.pro"
  }
  Group /acquisition/index_14/electrode (IntracellularElectrode) 
  Group /acquisition/index_14/electrode/device (Device) 
  file_create_date: ['2022-07-07T17:51:22.762371-04:00']
  Group /general/devices/Digidata 1440 with MultiClamp 700 (Device) 
  experiment_description: Clampex v10.6.2.2
  Group /general/intracellular_ephys/Electrode 0 (IntracellularElectrode) 
  Group /general/intracellular_ephys/Electrode 0/device (Device) 
  Group /general/intracellular_ephys/Electrode 1 (IntracellularElectrode) 
  Group /general/intracellular_ephys/Electrode 1/device (Device) 
  Group /general/intracellular_ephys/sweep_table (SweepTable) A sweep table groups different PatchClampSeries together.
  Dataset /general/intracellular_ephys/sweep_table/id (ElementIdentifiers)  | shape = (30,) | dtype = int64
  Dataset /general/intracellular_ephys/sweep_table/series (VectorData) PatchClampSeries with the same sweep number | shape = (30,) | dtype = object
  Dataset /general/intracellular_ephys/sweep_table/series_index (VectorIndex) Index for VectorData 'series' | shape = (30,) | dtype = uint8
  Dataset /general/intracellular_ephys/sweep_table/sweep_number (VectorData) Sweep number of the entries in that row | shape = (30,) | dtype = uint64
  session_id: PLACEHOLDER
  source_script: {
      "git_revision": "(main) 0.2.2-11-g54c8f8d",
      "package_version": "0.2.2+11.g54c8f8d",
      "repo": "https://github.com/byte-physics/x-to-nwb"
  }
  Group /general/subject (Subject) 
  identifier: 7d6e3e1e1b38116fbfb8b536ae0b21c1254f21dbd962939f9b015d62a593cb81
  session_description: PLACEHOLDER
  session_start_time: 2019-10-22T15:02:02.515000-04:00
  Group /stimulus/presentation/index_01 (VoltageClampStimulusSeries) {
      "cycle_id": 0,
      "file": "19o22001.abf",
      "name": "I_clampsec",
      "number": 1,
      "protocol": "I-V curve ,-400 pA",
      "protocolPath": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\I-V curve ,-400 pA.pro"
  }
  Group /stimulus/presentation/index_01/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_01/electrode/device (Device) 
  Group /stimulus/presentation/index_03 (VoltageClampStimulusSeries) {
      "cycle_id": 1,
      "file": "19o22001.abf",
      "name": "I_clampsec",
      "number": 1,
      "protocol": "I-V curve ,-400 pA",
      "protocolPath": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\I-V curve ,-400 pA.pro"
  }
  Group /stimulus/presentation/index_03/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_03/electrode/device (Device) 
  Group /stimulus/presentation/index_05 (VoltageClampStimulusSeries) {
      "cycle_id": 2,
      "file": "19o22001.abf",
      "name": "I_clampsec",
      "number": 1,
      "protocol": "I-V curve ,-400 pA",
      "protocolPath": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\I-V curve ,-400 pA.pro"
  }
  Group /stimulus/presentation/index_05/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_05/electrode/device (Device) 
  Group /stimulus/presentation/index_07 (VoltageClampStimulusSeries) {
      "cycle_id": 3,
      "file": "19o22001.abf",
      "name": "I_clampsec",
      "number": 1,
      "protocol": "I-V curve ,-400 pA",
      "protocolPath": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\I-V curve ,-400 pA.pro"
  }
  Group /stimulus/presentation/index_07/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_07/electrode/device (Device) 
  Group /stimulus/presentation/index_09 (VoltageClampStimulusSeries) {
      "cycle_id": 4,
      "file": "19o22001.abf",
      "name": "I_clampsec",
      "number": 1,
      "protocol": "I-V curve ,-400 pA",
      "protocolPath": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\I-V curve ,-400 pA.pro"
  }
  Group /stimulus/presentation/index_09/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_09/electrode/device (Device) 
  Group /stimulus/presentation/index_11 (VoltageClampStimulusSeries) {
      "cycle_id": 5,
      "file": "19o22001.abf",
      "name": "I_clampsec",
      "number": 1,
      "protocol": "I-V curve ,-400 pA",
      "protocolPath": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\I-V curve ,-400 pA.pro"
  }
  Group /stimulus/presentation/index_11/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_11/electrode/device (Device) 
  Group /stimulus/presentation/index_13 (VoltageClampStimulusSeries) {
      "cycle_id": 6,
      "file": "19o22001.abf",
      "name": "I_clampsec",
      "number": 1,
      "protocol": "I-V curve ,-400 pA",
      "protocolPath": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\I-V curve ,-400 pA.pro"
  }
  Group /stimulus/presentation/index_13/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_13/electrode/device (Device) 
  Group /stimulus/presentation/index_15 (VoltageClampStimulusSeries) {
      "cycle_id": 7,
      "file": "19o22001.abf",
      "name": "I_clampsec",
      "number": 1,
      "protocol": "I-V curve ,-400 pA",
      "protocolPath": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\I-V curve ,-400 pA.pro"
  }
  Group /stimulus/presentation/index_15/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_15/electrode/device (Device) 
  Group /stimulus/presentation/index_17 (VoltageClampStimulusSeries) {
      "cycle_id": 8,
      "file": "19o22001.abf",
      "name": "I_clampsec",
      "number": 1,
      "protocol": "I-V curve ,-400 pA",
      "protocolPath": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\I-V curve ,-400 pA.pro"
  }
  Group /stimulus/presentation/index_17/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_17/electrode/device (Device) 
  Group /stimulus/presentation/index_19 (VoltageClampStimulusSeries) {
      "cycle_id": 9,
      "file": "19o22001.abf",
      "name": "I_clampsec",
      "number": 1,
      "protocol": "I-V curve ,-400 pA",
      "protocolPath": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\I-V curve ,-400 pA.pro"
  }
  Group /stimulus/presentation/index_19/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_19/electrode/device (Device) 
  Group /stimulus/presentation/index_21 (VoltageClampStimulusSeries) {
      "cycle_id": 10,
      "file": "19o22001.abf",
      "name": "I_clampsec",
      "number": 1,
      "protocol": "I-V curve ,-400 pA",
      "protocolPath": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\I-V curve ,-400 pA.pro"
  }
  Group /stimulus/presentation/index_21/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_21/electrode/device (Device) 
  Group /stimulus/presentation/index_23 (VoltageClampStimulusSeries) {
      "cycle_id": 11,
      "file": "19o22001.abf",
      "name": "I_clampsec",
      "number": 1,
      "protocol": "I-V curve ,-400 pA",
      "protocolPath": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\I-V curve ,-400 pA.pro"
  }
  Group /stimulus/presentation/index_23/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_23/electrode/device (Device) 
  Group /stimulus/presentation/index_25 (VoltageClampStimulusSeries) {
      "cycle_id": 12,
      "file": "19o22001.abf",
      "name": "I_clampsec",
      "number": 1,
      "protocol": "I-V curve ,-400 pA",
      "protocolPath": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\I-V curve ,-400 pA.pro"
  }
  Group /stimulus/presentation/index_25/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_25/electrode/device (Device) 
  Group /stimulus/presentation/index_27 (VoltageClampStimulusSeries) {
      "cycle_id": 13,
      "file": "19o22001.abf",
      "name": "I_clampsec",
      "number": 1,
      "protocol": "I-V curve ,-400 pA",
      "protocolPath": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\I-V curve ,-400 pA.pro"
  }
  Group /stimulus/presentation/index_27/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_27/electrode/device (Device) 
  Group /stimulus/presentation/index_29 (VoltageClampStimulusSeries) {
      "cycle_id": 14,
      "file": "19o22001.abf",
      "name": "I_clampsec",
      "number": 1,
      "protocol": "I-V curve ,-400 pA",
      "protocolPath": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\I-V curve ,-400 pA.pro"
  }
  Group /stimulus/presentation/index_29/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_29/electrode/device (Device) 
  timestamps_reference_time: 2019-10-22T15:02:02.515000-04:00


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  Group /acquisition/index_00 (CurrentClampSeries) {
      "cycle_id": 0,
      "file": "19o22018.abf",
      "name": "Vm_sec",
      "number": 2,
      "protocol": "I-V curve ,-400 pA",
      "protocolPath": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\I-V curve ,-400 pA.pro"
  }
  Group /acquisition/index_00/electrode (IntracellularElectrode) 
  Group /acquisition/index_00/electrode/device (Device) 
  Group /acquisition/index_01 (CurrentClampSeries) {
      "cycle_id": 1,
      "file": "19o22018.abf",
      "name": "Vm_sec",
      "number": 2,
      "protocol": "I-V curve ,-400 pA",
      "protocolPath": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\I-V curve ,-400 pA.pro"
  }
  Group /acquisition/index_01/electrode (IntracellularElectrode) 
  Group /acquisition/index_01/electrode/device (Device) 
  Group /acquisition/index_02 (CurrentClampSeries) {
      "cycle_id": 2,
      "file": "19o22018.abf",
      "name": "Vm_sec",
      "number": 2,
      "protocol": "I-V curve ,-400 pA",
      "protocolPath": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\I-V curve ,-400 pA.pro"
  }
  Group /acquisition/index_02/electrode (IntracellularElectrode) 
  Group /acquisition/index_02/electrode/device (Device) 
  Group /acquisition/index_03 (CurrentClampSeries) {
      "cycle_id": 3,
      "file": "19o22018.abf",
      "name": "Vm_sec",
      "number": 2,
      "protocol": "I-V curve ,-400 pA",
      "protocolPath": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\I-V curve ,-400 pA.pro"
  }
  Group /acquisition/index_03/electrode (IntracellularElectrode) 
  Group /acquisition/index_03/electrode/device (Device) 
  Group /acquisition/index_04 (CurrentClampSeries) {
      "cycle_id": 4,
      "file": "19o22018.abf",
      "name": "Vm_sec",
      "number": 2,
      "protocol": "I-V curve ,-400 pA",
      "protocolPath": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\I-V curve ,-400 pA.pro"
  }
  Group /acquisition/index_04/electrode (IntracellularElectrode) 
  Group /acquisition/index_04/electrode/device (Device) 
  Group /acquisition/index_05 (CurrentClampSeries) {
      "cycle_id": 5,
      "file": "19o22018.abf",
      "name": "Vm_sec",
      "number": 2,
      "protocol": "I-V curve ,-400 pA",
      "protocolPath": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\I-V curve ,-400 pA.pro"
  }
  Group /acquisition/index_05/electrode (IntracellularElectrode) 
  Group /acquisition/index_05/electrode/device (Device) 
  Group /acquisition/index_06 (CurrentClampSeries) {
      "cycle_id": 6,
      "file": "19o22018.abf",
      "name": "Vm_sec",
      "number": 2,
      "protocol": "I-V curve ,-400 pA",
      "protocolPath": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\I-V curve ,-400 pA.pro"
  }
  Group /acquisition/index_06/electrode (IntracellularElectrode) 
  Group /acquisition/index_06/electrode/device (Device) 
  Group /acquisition/index_07 (CurrentClampSeries) {
      "cycle_id": 7,
      "file": "19o22018.abf",
      "name": "Vm_sec",
      "number": 2,
      "protocol": "I-V curve ,-400 pA",
      "protocolPath": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\I-V curve ,-400 pA.pro"
  }
  Group /acquisition/index_07/electrode (IntracellularElectrode) 
  Group /acquisition/index_07/electrode/device (Device) 
  Group /acquisition/index_08 (CurrentClampSeries) {
      "cycle_id": 8,
      "file": "19o22018.abf",
      "name": "Vm_sec",
      "number": 2,
      "protocol": "I-V curve ,-400 pA",
      "protocolPath": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\I-V curve ,-400 pA.pro"
  }
  Group /acquisition/index_08/electrode (IntracellularElectrode) 
  Group /acquisition/index_08/electrode/device (Device) 
  Group /acquisition/index_09 (CurrentClampSeries) {
      "cycle_id": 9,
      "file": "19o22018.abf",
      "name": "Vm_sec",
      "number": 2,
      "protocol": "I-V curve ,-400 pA",
      "protocolPath": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\I-V curve ,-400 pA.pro"
  }
  Group /acquisition/index_09/electrode (IntracellularElectrode) 
  Group /acquisition/index_09/electrode/device (Device) 
  Group /acquisition/index_10 (CurrentClampSeries) {
      "cycle_id": 10,
      "file": "19o22018.abf",
      "name": "Vm_sec",
      "number": 2,
      "protocol": "I-V curve ,-400 pA",
      "protocolPath": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\I-V curve ,-400 pA.pro"
  }
  Group /acquisition/index_10/electrode (IntracellularElectrode) 
  Group /acquisition/index_10/electrode/device (Device) 
  Group /acquisition/index_11 (CurrentClampSeries) {
      "cycle_id": 11,
      "file": "19o22018.abf",
      "name": "Vm_sec",
      "number": 2,
      "protocol": "I-V curve ,-400 pA",
      "protocolPath": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\I-V curve ,-400 pA.pro"
  }
  Group /acquisition/index_11/electrode (IntracellularElectrode) 
  Group /acquisition/index_11/electrode/device (Device) 
  Group /acquisition/index_12 (CurrentClampSeries) {
      "cycle_id": 12,
      "file": "19o22018.abf",
      "name": "Vm_sec",
      "number": 2,
      "protocol": "I-V curve ,-400 pA",
      "protocolPath": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\I-V curve ,-400 pA.pro"
  }
  Group /acquisition/index_12/electrode (IntracellularElectrode) 
  Group /acquisition/index_12/electrode/device (Device) 
  Group /acquisition/index_13 (CurrentClampSeries) {
      "cycle_id": 13,
      "file": "19o22018.abf",
      "name": "Vm_sec",
      "number": 2,
      "protocol": "I-V curve ,-400 pA",
      "protocolPath": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\I-V curve ,-400 pA.pro"
  }
  Group /acquisition/index_13/electrode (IntracellularElectrode) 
  Group /acquisition/index_13/electrode/device (Device) 
  file_create_date: ['2022-07-07T17:51:24.204255-04:00']
  Group /general/devices/Digidata 1440 with MultiClamp 700 (Device) 
  experiment_description: Clampex v10.6.2.2
  Group /general/intracellular_ephys/Electrode 0 (IntracellularElectrode) 
  Group /general/intracellular_ephys/Electrode 0/device (Device) 
  Group /general/intracellular_ephys/Electrode 1 (IntracellularElectrode) 
  Group /general/intracellular_ephys/Electrode 1/device (Device) 
  Group /general/intracellular_ephys/sweep_table (SweepTable) A sweep table groups different PatchClampSeries together.
  Dataset /general/intracellular_ephys/sweep_table/id (ElementIdentifiers)  | shape = (28,) | dtype = int64
  Dataset /general/intracellular_ephys/sweep_table/series (VectorData) PatchClampSeries with the same sweep number | shape = (28,) | dtype = object
  Dataset /general/intracellular_ephys/sweep_table/series_index (VectorIndex) Index for VectorData 'series' | shape = (28,) | dtype = uint8
  Dataset /general/intracellular_ephys/sweep_table/sweep_number (VectorData) Sweep number of the entries in that row | shape = (28,) | dtype = uint64
  session_id: PLACEHOLDER
  source_script: {
      "git_revision": "(main) 0.2.2-11-g54c8f8d",
      "package_version": "0.2.2+11.g54c8f8d",
      "repo": "https://github.com/byte-physics/x-to-nwb"
  }
  Group /general/subject (Subject) 
  identifier: 7d6e3e1e1b38116fbfb8b536ae0b21c1254f21dbd962939f9b015d62a593cb81
  session_description: PLACEHOLDER
  session_start_time: 2019-10-22T16:07:18.140000-04:00
  Group /stimulus/presentation/index_01 (VoltageClampStimulusSeries) {
      "cycle_id": 0,
      "file": "19o22018.abf",
      "name": "I_clampsec",
      "number": 1,
      "protocol": "I-V curve ,-400 pA",
      "protocolPath": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\I-V curve ,-400 pA.pro"
  }
  Group /stimulus/presentation/index_01/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_01/electrode/device (Device) 
  Group /stimulus/presentation/index_03 (VoltageClampStimulusSeries) {
      "cycle_id": 1,
      "file": "19o22018.abf",
      "name": "I_clampsec",
      "number": 1,
      "protocol": "I-V curve ,-400 pA",
      "protocolPath": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\I-V curve ,-400 pA.pro"
  }
  Group /stimulus/presentation/index_03/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_03/electrode/device (Device) 
  Group /stimulus/presentation/index_05 (VoltageClampStimulusSeries) {
      "cycle_id": 2,
      "file": "19o22018.abf",
      "name": "I_clampsec",
      "number": 1,
      "protocol": "I-V curve ,-400 pA",
      "protocolPath": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\I-V curve ,-400 pA.pro"
  }
  Group /stimulus/presentation/index_05/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_05/electrode/device (Device) 
  Group /stimulus/presentation/index_07 (VoltageClampStimulusSeries) {
      "cycle_id": 3,
      "file": "19o22018.abf",
      "name": "I_clampsec",
      "number": 1,
      "protocol": "I-V curve ,-400 pA",
      "protocolPath": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\I-V curve ,-400 pA.pro"
  }
  Group /stimulus/presentation/index_07/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_07/electrode/device (Device) 
  Group /stimulus/presentation/index_09 (VoltageClampStimulusSeries) {
      "cycle_id": 4,
      "file": "19o22018.abf",
      "name": "I_clampsec",
      "number": 1,
      "protocol": "I-V curve ,-400 pA",
      "protocolPath": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\I-V curve ,-400 pA.pro"
  }
  Group /stimulus/presentation/index_09/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_09/electrode/device (Device) 
  Group /stimulus/presentation/index_11 (VoltageClampStimulusSeries) {
      "cycle_id": 5,
      "file": "19o22018.abf",
      "name": "I_clampsec",
      "number": 1,
      "protocol": "I-V curve ,-400 pA",
      "protocolPath": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\I-V curve ,-400 pA.pro"
  }
  Group /stimulus/presentation/index_11/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_11/electrode/device (Device) 
  Group /stimulus/presentation/index_13 (VoltageClampStimulusSeries) {
      "cycle_id": 6,
      "file": "19o22018.abf",
      "name": "I_clampsec",
      "number": 1,
      "protocol": "I-V curve ,-400 pA",
      "protocolPath": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\I-V curve ,-400 pA.pro"
  }
  Group /stimulus/presentation/index_13/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_13/electrode/device (Device) 
  Group /stimulus/presentation/index_15 (VoltageClampStimulusSeries) {
      "cycle_id": 7,
      "file": "19o22018.abf",
      "name": "I_clampsec",
      "number": 1,
      "protocol": "I-V curve ,-400 pA",
      "protocolPath": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\I-V curve ,-400 pA.pro"
  }
  Group /stimulus/presentation/index_15/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_15/electrode/device (Device) 
  Group /stimulus/presentation/index_17 (VoltageClampStimulusSeries) {
      "cycle_id": 8,
      "file": "19o22018.abf",
      "name": "I_clampsec",
      "number": 1,
      "protocol": "I-V curve ,-400 pA",
      "protocolPath": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\I-V curve ,-400 pA.pro"
  }
  Group /stimulus/presentation/index_17/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_17/electrode/device (Device) 
  Group /stimulus/presentation/index_19 (VoltageClampStimulusSeries) {
      "cycle_id": 9,
      "file": "19o22018.abf",
      "name": "I_clampsec",
      "number": 1,
      "protocol": "I-V curve ,-400 pA",
      "protocolPath": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\I-V curve ,-400 pA.pro"
  }
  Group /stimulus/presentation/index_19/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_19/electrode/device (Device) 
  Group /stimulus/presentation/index_21 (VoltageClampStimulusSeries) {
      "cycle_id": 10,
      "file": "19o22018.abf",
      "name": "I_clampsec",
      "number": 1,
      "protocol": "I-V curve ,-400 pA",
      "protocolPath": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\I-V curve ,-400 pA.pro"
  }
  Group /stimulus/presentation/index_21/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_21/electrode/device (Device) 
  Group /stimulus/presentation/index_23 (VoltageClampStimulusSeries) {
      "cycle_id": 11,
      "file": "19o22018.abf",
      "name": "I_clampsec",
      "number": 1,
      "protocol": "I-V curve ,-400 pA",
      "protocolPath": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\I-V curve ,-400 pA.pro"
  }
  Group /stimulus/presentation/index_23/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_23/electrode/device (Device) 
  Group /stimulus/presentation/index_25 (VoltageClampStimulusSeries) {
      "cycle_id": 12,
      "file": "19o22018.abf",
      "name": "I_clampsec",
      "number": 1,
      "protocol": "I-V curve ,-400 pA",
      "protocolPath": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\I-V curve ,-400 pA.pro"
  }
  Group /stimulus/presentation/index_25/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_25/electrode/device (Device) 
  Group /stimulus/presentation/index_27 (VoltageClampStimulusSeries) {
      "cycle_id": 13,
      "file": "19o22018.abf",
      "name": "I_clampsec",
      "number": 1,
      "protocol": "I-V curve ,-400 pA",
      "protocolPath": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\I-V curve ,-400 pA.pro"
  }
  Group /stimulus/presentation/index_27/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_27/electrode/device (Device) 
  timestamps_reference_time: 2019-10-22T16:07:18.140000-04:00
