
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000297/draft
name: UHN whole-cell patch-clamp excitability recordings from human cortical neurons
contributor: [{'name': 'Howard, Derek', 'email': 'derekhoward@gmail.com', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Homeira Moradi, Chameh', 'email': 'homeira.moradi@uhnresearch.ca', 'roleName': ['dcite:Author', 'dcite:DataCollector', 'dcite:DataCurator'], 'schemaKey': 'Person', 'identifier': '0000-0002-8009-147X', 'affiliation': [], 'includeInCitation': True}, {'name': 'Taufik A Valiante', 'email': 'taufik.valiante@uhn.ca', 'roleName': ['dcite:DataCollector', 'dcite:Supervision'], 'schemaKey': 'Person', 'identifier': '0000-0002-3443-3790', 'affiliation': [], 'includeInCitation': True}, {'name': 'Shreejoy Tripathy', 'email': 'shreejoy.tripathy@camh.ca', 'roleName': ['dcite:Author', 'dcite:Conceptualization', 'dcite:DataCurator', 'dcite:Supervision'], 'schemaKey': 'Person', 'identifier': '0000-0002-1007-9061', 'affiliation': [], 'includeInCitation': True}]
description: Whole-cell current clamp recordings from surgically resected human cortical tissue 
assetsSummary: {'species': [{'name': 'Homo sapiens - Human', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9606'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 231099211, 'numberOfFiles': 118, 'numberOfSubjects': 197, 'variableMeasured': ['CurrentClampSeries', 'VoltageClampStimulusSeries', 'CurrentClampStimulusSeries'], 'measurementTechnique': [{'name': 'voltage clamp technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'current clamp technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000297 has 9 NWB files.
1 of these NWB files are of type 1.
1 of these NWB files are of type 2.
4 of these NWB files are of type 3.
2 of these NWB files are of type 4.
1 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Index_0_0_0 (CurrentClampSeries) {
      "comments": [
          "C1, RMP 60.1mV, gain 20, DC 25, every 20s"
      ],
      "file_name": "18201004.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 0
  }
  Group /acquisition/Index_0_0_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_0_0/electrode/device (Device) 
  Group /acquisition/Index_0_1_0 (CurrentClampSeries) {
      "comments": [
          "C1, RMP 60.1mV, gain 20, DC 25, every 20s"
      ],
      "file_name": "18201004.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 1
  }
  Group /acquisition/Index_0_1_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_1_0/electrode/device (Device) 
  Group /acquisition/Index_0_2_0 (CurrentClampSeries) {
      "comments": [
          "C1, RMP 60.1mV, gain 20, DC 25, every 20s"
      ],
      "file_name": "18201004.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 2
  }
  Group /acquisition/Index_0_2_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_2_0/electrode/device (Device) 
  Group /acquisition/Index_0_3_0 (CurrentClampSeries) {
      "comments": [
          "C1, RMP 60.1mV, gain 20, DC 25, every 20s"
      ],
      "file_name": "18201004.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 3
  }
  Group /acquisition/Index_0_3_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_3_0/electrode/device (Device) 
  Group /acquisition/Index_0_4_0 (CurrentClampSeries) {
      "comments": [
          "C1, RMP 60.1mV, gain 20, DC 25, every 20s"
      ],
      "file_name": "18201004.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 4
  }
  Group /acquisition/Index_0_4_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_4_0/electrode/device (Device) 
  Group /acquisition/Index_0_5_0 (CurrentClampSeries) {
      "comments": [
          "C1, RMP 60.1mV, gain 20, DC 25, every 20s"
      ],
      "file_name": "18201004.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 5
  }
  Group /acquisition/Index_0_5_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_5_0/electrode/device (Device) 
  Group /acquisition/Index_0_6_0 (CurrentClampSeries) {
      "comments": [
          "C1, RMP 60.1mV, gain 20, DC 25, every 20s"
      ],
      "file_name": "18201004.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 6
  }
  Group /acquisition/Index_0_6_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_6_0/electrode/device (Device) 
  Group /acquisition/Index_0_7_0 (CurrentClampSeries) {
      "comments": [
          "C1, RMP 60.1mV, gain 20, DC 25, every 20s"
      ],
      "file_name": "18201004.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 7
  }
  Group /acquisition/Index_0_7_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_7_0/electrode/device (Device) 
  file_create_date: ['2022-07-07T17:50:09.805703-04:00']
  Group /general/devices/Clampex 9.2.1.9 (Device) 
  experiment_description: 
  Group /general/intracellular_ephys/elec0 (IntracellularElectrode) 
  Group /general/intracellular_ephys/elec0/device (Device) 
  Group /general/intracellular_ephys/sweep_table (SweepTable) A sweep table groups different PatchClampSeries together.
  Dataset /general/intracellular_ephys/sweep_table/id (ElementIdentifiers)  | shape = (16,) | dtype = int64
  Dataset /general/intracellular_ephys/sweep_table/series (VectorData) PatchClampSeries with the same sweep number | shape = (16,) | dtype = object
  Dataset /general/intracellular_ephys/sweep_table/series_index (VectorIndex) Index for VectorData 'series' | shape = (16,) | dtype = uint8
  Dataset /general/intracellular_ephys/sweep_table/sweep_number (VectorData) Sweep number of the entries in that row | shape = (16,) | dtype = uint32
  notes: 
  session_id: PLACEHOLDER
  source_script: {
      "git_revision": "(main) 0.2.2-11-g54c8f8d",
      "package_version": "0.2.2+11.g54c8f8d",
      "repo": "https://github.com/byte-physics/x-to-nwb"
  }
  Group /general/subject (Subject) 
  identifier: 18201004.abf
  session_description: PLACEHOLDER
  session_start_time: 2018-02-01T12:56:09.421000-05:00
  Group /stimulus/presentation/Index_0_0_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C1, RMP 60.1mV, gain 20, DC 25, every 20s"
      ],
      "file_name": "18201004.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 0
  }
  Group /stimulus/presentation/Index_0_0_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_0_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_1_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C1, RMP 60.1mV, gain 20, DC 25, every 20s"
      ],
      "file_name": "18201004.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 1
  }
  Group /stimulus/presentation/Index_0_1_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_1_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_2_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C1, RMP 60.1mV, gain 20, DC 25, every 20s"
      ],
      "file_name": "18201004.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 2
  }
  Group /stimulus/presentation/Index_0_2_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_2_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_3_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C1, RMP 60.1mV, gain 20, DC 25, every 20s"
      ],
      "file_name": "18201004.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 3
  }
  Group /stimulus/presentation/Index_0_3_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_3_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_4_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C1, RMP 60.1mV, gain 20, DC 25, every 20s"
      ],
      "file_name": "18201004.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 4
  }
  Group /stimulus/presentation/Index_0_4_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_4_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_5_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C1, RMP 60.1mV, gain 20, DC 25, every 20s"
      ],
      "file_name": "18201004.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 5
  }
  Group /stimulus/presentation/Index_0_5_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_5_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_6_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C1, RMP 60.1mV, gain 20, DC 25, every 20s"
      ],
      "file_name": "18201004.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 6
  }
  Group /stimulus/presentation/Index_0_6_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_6_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_7_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C1, RMP 60.1mV, gain 20, DC 25, every 20s"
      ],
      "file_name": "18201004.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 7
  }
  Group /stimulus/presentation/Index_0_7_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_7_1/electrode/device (Device) 
  timestamps_reference_time: 2018-02-01T12:56:09.421000-05:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Index_0_0_0 (CurrentClampSeries) {
      "comments": [
          "C3, RMP -66.5 mv, layer 5"
      ],
      "file_name": "18201011.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 0
  }
  Group /acquisition/Index_0_0_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_0_0/electrode/device (Device) 
  Group /acquisition/Index_0_10_0 (CurrentClampSeries) {
      "comments": [
          "C3, RMP -66.5 mv, layer 5"
      ],
      "file_name": "18201011.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 10
  }
  Group /acquisition/Index_0_10_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_10_0/electrode/device (Device) 
  Group /acquisition/Index_0_11_0 (CurrentClampSeries) {
      "comments": [
          "C3, RMP -66.5 mv, layer 5"
      ],
      "file_name": "18201011.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 11
  }
  Group /acquisition/Index_0_11_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_11_0/electrode/device (Device) 
  Group /acquisition/Index_0_12_0 (CurrentClampSeries) {
      "comments": [
          "C3, RMP -66.5 mv, layer 5"
      ],
      "file_name": "18201011.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 12
  }
  Group /acquisition/Index_0_12_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_12_0/electrode/device (Device) 
  Group /acquisition/Index_0_1_0 (CurrentClampSeries) {
      "comments": [
          "C3, RMP -66.5 mv, layer 5"
      ],
      "file_name": "18201011.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 1
  }
  Group /acquisition/Index_0_1_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_1_0/electrode/device (Device) 
  Group /acquisition/Index_0_2_0 (CurrentClampSeries) {
      "comments": [
          "C3, RMP -66.5 mv, layer 5"
      ],
      "file_name": "18201011.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 2
  }
  Group /acquisition/Index_0_2_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_2_0/electrode/device (Device) 
  Group /acquisition/Index_0_3_0 (CurrentClampSeries) {
      "comments": [
          "C3, RMP -66.5 mv, layer 5"
      ],
      "file_name": "18201011.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 3
  }
  Group /acquisition/Index_0_3_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_3_0/electrode/device (Device) 
  Group /acquisition/Index_0_4_0 (CurrentClampSeries) {
      "comments": [
          "C3, RMP -66.5 mv, layer 5"
      ],
      "file_name": "18201011.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 4
  }
  Group /acquisition/Index_0_4_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_4_0/electrode/device (Device) 
  Group /acquisition/Index_0_5_0 (CurrentClampSeries) {
      "comments": [
          "C3, RMP -66.5 mv, layer 5"
      ],
      "file_name": "18201011.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 5
  }
  Group /acquisition/Index_0_5_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_5_0/electrode/device (Device) 
  Group /acquisition/Index_0_6_0 (CurrentClampSeries) {
      "comments": [
          "C3, RMP -66.5 mv, layer 5"
      ],
      "file_name": "18201011.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 6
  }
  Group /acquisition/Index_0_6_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_6_0/electrode/device (Device) 
  Group /acquisition/Index_0_7_0 (CurrentClampSeries) {
      "comments": [
          "C3, RMP -66.5 mv, layer 5"
      ],
      "file_name": "18201011.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 7
  }
  Group /acquisition/Index_0_7_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_7_0/electrode/device (Device) 
  Group /acquisition/Index_0_8_0 (CurrentClampSeries) {
      "comments": [
          "C3, RMP -66.5 mv, layer 5"
      ],
      "file_name": "18201011.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 8
  }
  Group /acquisition/Index_0_8_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_8_0/electrode/device (Device) 
  Group /acquisition/Index_0_9_0 (CurrentClampSeries) {
      "comments": [
          "C3, RMP -66.5 mv, layer 5"
      ],
      "file_name": "18201011.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 9
  }
  Group /acquisition/Index_0_9_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_9_0/electrode/device (Device) 
  file_create_date: ['2022-07-07T17:50:10.716877-04:00']
  Group /general/devices/Clampex 9.2.1.9 (Device) 
  experiment_description: 
  Group /general/intracellular_ephys/elec0 (IntracellularElectrode) 
  Group /general/intracellular_ephys/elec0/device (Device) 
  Group /general/intracellular_ephys/sweep_table (SweepTable) A sweep table groups different PatchClampSeries together.
  Dataset /general/intracellular_ephys/sweep_table/id (ElementIdentifiers)  | shape = (26,) | dtype = int64
  Dataset /general/intracellular_ephys/sweep_table/series (VectorData) PatchClampSeries with the same sweep number | shape = (26,) | dtype = object
  Dataset /general/intracellular_ephys/sweep_table/series_index (VectorIndex) Index for VectorData 'series' | shape = (26,) | dtype = uint8
  Dataset /general/intracellular_ephys/sweep_table/sweep_number (VectorData) Sweep number of the entries in that row | shape = (26,) | dtype = uint32
  notes: 
  session_id: PLACEHOLDER
  source_script: {
      "git_revision": "(main) 0.2.2-11-g54c8f8d",
      "package_version": "0.2.2+11.g54c8f8d",
      "repo": "https://github.com/byte-physics/x-to-nwb"
  }
  Group /general/subject (Subject) 
  identifier: 18201011.abf
  session_description: PLACEHOLDER
  session_start_time: 2018-02-01T13:56:54.968000-05:00
  Group /stimulus/presentation/Index_0_0_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C3, RMP -66.5 mv, layer 5"
      ],
      "file_name": "18201011.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 0
  }
  Group /stimulus/presentation/Index_0_0_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_0_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_10_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C3, RMP -66.5 mv, layer 5"
      ],
      "file_name": "18201011.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 10
  }
  Group /stimulus/presentation/Index_0_10_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_10_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_11_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C3, RMP -66.5 mv, layer 5"
      ],
      "file_name": "18201011.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 11
  }
  Group /stimulus/presentation/Index_0_11_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_11_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_12_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C3, RMP -66.5 mv, layer 5"
      ],
      "file_name": "18201011.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 12
  }
  Group /stimulus/presentation/Index_0_12_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_12_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_1_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C3, RMP -66.5 mv, layer 5"
      ],
      "file_name": "18201011.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 1
  }
  Group /stimulus/presentation/Index_0_1_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_1_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_2_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C3, RMP -66.5 mv, layer 5"
      ],
      "file_name": "18201011.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 2
  }
  Group /stimulus/presentation/Index_0_2_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_2_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_3_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C3, RMP -66.5 mv, layer 5"
      ],
      "file_name": "18201011.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 3
  }
  Group /stimulus/presentation/Index_0_3_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_3_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_4_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C3, RMP -66.5 mv, layer 5"
      ],
      "file_name": "18201011.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 4
  }
  Group /stimulus/presentation/Index_0_4_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_4_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_5_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C3, RMP -66.5 mv, layer 5"
      ],
      "file_name": "18201011.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 5
  }
  Group /stimulus/presentation/Index_0_5_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_5_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_6_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C3, RMP -66.5 mv, layer 5"
      ],
      "file_name": "18201011.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 6
  }
  Group /stimulus/presentation/Index_0_6_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_6_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_7_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C3, RMP -66.5 mv, layer 5"
      ],
      "file_name": "18201011.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 7
  }
  Group /stimulus/presentation/Index_0_7_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_7_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_8_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C3, RMP -66.5 mv, layer 5"
      ],
      "file_name": "18201011.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 8
  }
  Group /stimulus/presentation/Index_0_8_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_8_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_9_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C3, RMP -66.5 mv, layer 5"
      ],
      "file_name": "18201011.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 9
  }
  Group /stimulus/presentation/Index_0_9_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_9_1/electrode/device (Device) 
  timestamps_reference_time: 2018-02-01T13:56:54.968000-05:00


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Index_0_0_0 (CurrentClampSeries) {
      "comments": [
          "C3;  l2/3 ; RMP -63.2 mv; offset -22.5mv"
      ],
      "file_name": "18220008.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 0
  }
  Group /acquisition/Index_0_0_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_0_0/electrode/device (Device) 
  Group /acquisition/Index_0_10_0 (CurrentClampSeries) {
      "comments": [
          "C3;  l2/3 ; RMP -63.2 mv; offset -22.5mv"
      ],
      "file_name": "18220008.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 10
  }
  Group /acquisition/Index_0_10_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_10_0/electrode/device (Device) 
  Group /acquisition/Index_0_11_0 (CurrentClampSeries) {
      "comments": [
          "C3;  l2/3 ; RMP -63.2 mv; offset -22.5mv"
      ],
      "file_name": "18220008.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 11
  }
  Group /acquisition/Index_0_11_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_11_0/electrode/device (Device) 
  Group /acquisition/Index_0_12_0 (CurrentClampSeries) {
      "comments": [
          "C3;  l2/3 ; RMP -63.2 mv; offset -22.5mv"
      ],
      "file_name": "18220008.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 12
  }
  Group /acquisition/Index_0_12_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_12_0/electrode/device (Device) 
  Group /acquisition/Index_0_13_0 (CurrentClampSeries) {
      "comments": [
          "C3;  l2/3 ; RMP -63.2 mv; offset -22.5mv"
      ],
      "file_name": "18220008.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 13
  }
  Group /acquisition/Index_0_13_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_13_0/electrode/device (Device) 
  Group /acquisition/Index_0_14_0 (CurrentClampSeries) {
      "comments": [
          "C3;  l2/3 ; RMP -63.2 mv; offset -22.5mv"
      ],
      "file_name": "18220008.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 14
  }
  Group /acquisition/Index_0_14_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_14_0/electrode/device (Device) 
  Group /acquisition/Index_0_1_0 (CurrentClampSeries) {
      "comments": [
          "C3;  l2/3 ; RMP -63.2 mv; offset -22.5mv"
      ],
      "file_name": "18220008.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 1
  }
  Group /acquisition/Index_0_1_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_1_0/electrode/device (Device) 
  Group /acquisition/Index_0_2_0 (CurrentClampSeries) {
      "comments": [
          "C3;  l2/3 ; RMP -63.2 mv; offset -22.5mv"
      ],
      "file_name": "18220008.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 2
  }
  Group /acquisition/Index_0_2_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_2_0/electrode/device (Device) 
  Group /acquisition/Index_0_3_0 (CurrentClampSeries) {
      "comments": [
          "C3;  l2/3 ; RMP -63.2 mv; offset -22.5mv"
      ],
      "file_name": "18220008.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 3
  }
  Group /acquisition/Index_0_3_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_3_0/electrode/device (Device) 
  Group /acquisition/Index_0_4_0 (CurrentClampSeries) {
      "comments": [
          "C3;  l2/3 ; RMP -63.2 mv; offset -22.5mv"
      ],
      "file_name": "18220008.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 4
  }
  Group /acquisition/Index_0_4_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_4_0/electrode/device (Device) 
  Group /acquisition/Index_0_5_0 (CurrentClampSeries) {
      "comments": [
          "C3;  l2/3 ; RMP -63.2 mv; offset -22.5mv"
      ],
      "file_name": "18220008.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 5
  }
  Group /acquisition/Index_0_5_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_5_0/electrode/device (Device) 
  Group /acquisition/Index_0_6_0 (CurrentClampSeries) {
      "comments": [
          "C3;  l2/3 ; RMP -63.2 mv; offset -22.5mv"
      ],
      "file_name": "18220008.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 6
  }
  Group /acquisition/Index_0_6_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_6_0/electrode/device (Device) 
  Group /acquisition/Index_0_7_0 (CurrentClampSeries) {
      "comments": [
          "C3;  l2/3 ; RMP -63.2 mv; offset -22.5mv"
      ],
      "file_name": "18220008.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 7
  }
  Group /acquisition/Index_0_7_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_7_0/electrode/device (Device) 
  Group /acquisition/Index_0_8_0 (CurrentClampSeries) {
      "comments": [
          "C3;  l2/3 ; RMP -63.2 mv; offset -22.5mv"
      ],
      "file_name": "18220008.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 8
  }
  Group /acquisition/Index_0_8_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_8_0/electrode/device (Device) 
  Group /acquisition/Index_0_9_0 (CurrentClampSeries) {
      "comments": [
          "C3;  l2/3 ; RMP -63.2 mv; offset -22.5mv"
      ],
      "file_name": "18220008.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 9
  }
  Group /acquisition/Index_0_9_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_9_0/electrode/device (Device) 
  file_create_date: ['2022-07-07T17:50:11.743218-04:00']
  Group /general/devices/Clampex 9.2.1.9 (Device) 
  experiment_description: 
  Group /general/intracellular_ephys/elec0 (IntracellularElectrode) 
  Group /general/intracellular_ephys/elec0/device (Device) 
  Group /general/intracellular_ephys/sweep_table (SweepTable) A sweep table groups different PatchClampSeries together.
  Dataset /general/intracellular_ephys/sweep_table/id (ElementIdentifiers)  | shape = (30,) | dtype = int64
  Dataset /general/intracellular_ephys/sweep_table/series (VectorData) PatchClampSeries with the same sweep number | shape = (30,) | dtype = object
  Dataset /general/intracellular_ephys/sweep_table/series_index (VectorIndex) Index for VectorData 'series' | shape = (30,) | dtype = uint8
  Dataset /general/intracellular_ephys/sweep_table/sweep_number (VectorData) Sweep number of the entries in that row | shape = (30,) | dtype = uint32
  notes: 
  session_id: PLACEHOLDER
  source_script: {
      "git_revision": "(main) 0.2.2-11-g54c8f8d",
      "package_version": "0.2.2+11.g54c8f8d",
      "repo": "https://github.com/byte-physics/x-to-nwb"
  }
  Group /general/subject (Subject) 
  identifier: 18220008.abf
  session_description: PLACEHOLDER
  session_start_time: 2018-02-20T15:11:59.265000-05:00
  Group /stimulus/presentation/Index_0_0_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C3;  l2/3 ; RMP -63.2 mv; offset -22.5mv"
      ],
      "file_name": "18220008.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 0
  }
  Group /stimulus/presentation/Index_0_0_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_0_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_10_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C3;  l2/3 ; RMP -63.2 mv; offset -22.5mv"
      ],
      "file_name": "18220008.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 10
  }
  Group /stimulus/presentation/Index_0_10_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_10_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_11_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C3;  l2/3 ; RMP -63.2 mv; offset -22.5mv"
      ],
      "file_name": "18220008.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 11
  }
  Group /stimulus/presentation/Index_0_11_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_11_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_12_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C3;  l2/3 ; RMP -63.2 mv; offset -22.5mv"
      ],
      "file_name": "18220008.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 12
  }
  Group /stimulus/presentation/Index_0_12_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_12_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_13_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C3;  l2/3 ; RMP -63.2 mv; offset -22.5mv"
      ],
      "file_name": "18220008.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 13
  }
  Group /stimulus/presentation/Index_0_13_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_13_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_14_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C3;  l2/3 ; RMP -63.2 mv; offset -22.5mv"
      ],
      "file_name": "18220008.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 14
  }
  Group /stimulus/presentation/Index_0_14_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_14_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_1_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C3;  l2/3 ; RMP -63.2 mv; offset -22.5mv"
      ],
      "file_name": "18220008.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 1
  }
  Group /stimulus/presentation/Index_0_1_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_1_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_2_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C3;  l2/3 ; RMP -63.2 mv; offset -22.5mv"
      ],
      "file_name": "18220008.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 2
  }
  Group /stimulus/presentation/Index_0_2_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_2_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_3_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C3;  l2/3 ; RMP -63.2 mv; offset -22.5mv"
      ],
      "file_name": "18220008.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 3
  }
  Group /stimulus/presentation/Index_0_3_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_3_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_4_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C3;  l2/3 ; RMP -63.2 mv; offset -22.5mv"
      ],
      "file_name": "18220008.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 4
  }
  Group /stimulus/presentation/Index_0_4_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_4_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_5_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C3;  l2/3 ; RMP -63.2 mv; offset -22.5mv"
      ],
      "file_name": "18220008.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 5
  }
  Group /stimulus/presentation/Index_0_5_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_5_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_6_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C3;  l2/3 ; RMP -63.2 mv; offset -22.5mv"
      ],
      "file_name": "18220008.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 6
  }
  Group /stimulus/presentation/Index_0_6_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_6_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_7_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C3;  l2/3 ; RMP -63.2 mv; offset -22.5mv"
      ],
      "file_name": "18220008.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 7
  }
  Group /stimulus/presentation/Index_0_7_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_7_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_8_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C3;  l2/3 ; RMP -63.2 mv; offset -22.5mv"
      ],
      "file_name": "18220008.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 8
  }
  Group /stimulus/presentation/Index_0_8_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_8_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_9_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C3;  l2/3 ; RMP -63.2 mv; offset -22.5mv"
      ],
      "file_name": "18220008.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 9
  }
  Group /stimulus/presentation/Index_0_9_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_9_1/electrode/device (Device) 
  timestamps_reference_time: 2018-02-20T15:11:59.265000-05:00


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Index_0_0_0 (CurrentClampSeries) {
      "comments": [
          "C1; L2/3; RMP -70.5; Offset 20 mv;1s;-220/40"
      ],
      "file_name": "18320005.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 0
  }
  Group /acquisition/Index_0_0_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_0_0/electrode/device (Device) 
  Group /acquisition/Index_0_10_0 (CurrentClampSeries) {
      "comments": [
          "C1; L2/3; RMP -70.5; Offset 20 mv;1s;-220/40"
      ],
      "file_name": "18320005.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 10
  }
  Group /acquisition/Index_0_10_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_10_0/electrode/device (Device) 
  Group /acquisition/Index_0_11_0 (CurrentClampSeries) {
      "comments": [
          "C1; L2/3; RMP -70.5; Offset 20 mv;1s;-220/40"
      ],
      "file_name": "18320005.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 11
  }
  Group /acquisition/Index_0_11_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_11_0/electrode/device (Device) 
  Group /acquisition/Index_0_12_0 (CurrentClampSeries) {
      "comments": [
          "C1; L2/3; RMP -70.5; Offset 20 mv;1s;-220/40"
      ],
      "file_name": "18320005.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 12
  }
  Group /acquisition/Index_0_12_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_12_0/electrode/device (Device) 
  Group /acquisition/Index_0_13_0 (CurrentClampSeries) {
      "comments": [
          "C1; L2/3; RMP -70.5; Offset 20 mv;1s;-220/40"
      ],
      "file_name": "18320005.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 13
  }
  Group /acquisition/Index_0_13_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_13_0/electrode/device (Device) 
  Group /acquisition/Index_0_1_0 (CurrentClampSeries) {
      "comments": [
          "C1; L2/3; RMP -70.5; Offset 20 mv;1s;-220/40"
      ],
      "file_name": "18320005.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 1
  }
  Group /acquisition/Index_0_1_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_1_0/electrode/device (Device) 
  Group /acquisition/Index_0_2_0 (CurrentClampSeries) {
      "comments": [
          "C1; L2/3; RMP -70.5; Offset 20 mv;1s;-220/40"
      ],
      "file_name": "18320005.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 2
  }
  Group /acquisition/Index_0_2_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_2_0/electrode/device (Device) 
  Group /acquisition/Index_0_3_0 (CurrentClampSeries) {
      "comments": [
          "C1; L2/3; RMP -70.5; Offset 20 mv;1s;-220/40"
      ],
      "file_name": "18320005.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 3
  }
  Group /acquisition/Index_0_3_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_3_0/electrode/device (Device) 
  Group /acquisition/Index_0_4_0 (CurrentClampSeries) {
      "comments": [
          "C1; L2/3; RMP -70.5; Offset 20 mv;1s;-220/40"
      ],
      "file_name": "18320005.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 4
  }
  Group /acquisition/Index_0_4_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_4_0/electrode/device (Device) 
  Group /acquisition/Index_0_5_0 (CurrentClampSeries) {
      "comments": [
          "C1; L2/3; RMP -70.5; Offset 20 mv;1s;-220/40"
      ],
      "file_name": "18320005.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 5
  }
  Group /acquisition/Index_0_5_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_5_0/electrode/device (Device) 
  Group /acquisition/Index_0_6_0 (CurrentClampSeries) {
      "comments": [
          "C1; L2/3; RMP -70.5; Offset 20 mv;1s;-220/40"
      ],
      "file_name": "18320005.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 6
  }
  Group /acquisition/Index_0_6_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_6_0/electrode/device (Device) 
  Group /acquisition/Index_0_7_0 (CurrentClampSeries) {
      "comments": [
          "C1; L2/3; RMP -70.5; Offset 20 mv;1s;-220/40"
      ],
      "file_name": "18320005.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 7
  }
  Group /acquisition/Index_0_7_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_7_0/electrode/device (Device) 
  Group /acquisition/Index_0_8_0 (CurrentClampSeries) {
      "comments": [
          "C1; L2/3; RMP -70.5; Offset 20 mv;1s;-220/40"
      ],
      "file_name": "18320005.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 8
  }
  Group /acquisition/Index_0_8_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_8_0/electrode/device (Device) 
  Group /acquisition/Index_0_9_0 (CurrentClampSeries) {
      "comments": [
          "C1; L2/3; RMP -70.5; Offset 20 mv;1s;-220/40"
      ],
      "file_name": "18320005.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 9
  }
  Group /acquisition/Index_0_9_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_9_0/electrode/device (Device) 
  file_create_date: ['2022-07-07T17:50:04.395735-04:00']
  Group /general/devices/Clampex 9.2.1.9 (Device) 
  experiment_description: 
  Group /general/intracellular_ephys/elec0 (IntracellularElectrode) 
  Group /general/intracellular_ephys/elec0/device (Device) 
  Group /general/intracellular_ephys/sweep_table (SweepTable) A sweep table groups different PatchClampSeries together.
  Dataset /general/intracellular_ephys/sweep_table/id (ElementIdentifiers)  | shape = (28,) | dtype = int64
  Dataset /general/intracellular_ephys/sweep_table/series (VectorData) PatchClampSeries with the same sweep number | shape = (28,) | dtype = object
  Dataset /general/intracellular_ephys/sweep_table/series_index (VectorIndex) Index for VectorData 'series' | shape = (28,) | dtype = uint8
  Dataset /general/intracellular_ephys/sweep_table/sweep_number (VectorData) Sweep number of the entries in that row | shape = (28,) | dtype = uint32
  notes: 
  session_id: PLACEHOLDER
  source_script: {
      "git_revision": "(main) 0.2.2-11-g54c8f8d",
      "package_version": "0.2.2+11.g54c8f8d",
      "repo": "https://github.com/byte-physics/x-to-nwb"
  }
  Group /general/subject (Subject) 
  identifier: 18320005.abf
  session_description: PLACEHOLDER
  session_start_time: 2018-03-20T13:43:52.125000-04:00
  Group /stimulus/presentation/Index_0_0_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C1; L2/3; RMP -70.5; Offset 20 mv;1s;-220/40"
      ],
      "file_name": "18320005.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 0
  }
  Group /stimulus/presentation/Index_0_0_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_0_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_10_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C1; L2/3; RMP -70.5; Offset 20 mv;1s;-220/40"
      ],
      "file_name": "18320005.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 10
  }
  Group /stimulus/presentation/Index_0_10_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_10_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_11_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C1; L2/3; RMP -70.5; Offset 20 mv;1s;-220/40"
      ],
      "file_name": "18320005.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 11
  }
  Group /stimulus/presentation/Index_0_11_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_11_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_12_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C1; L2/3; RMP -70.5; Offset 20 mv;1s;-220/40"
      ],
      "file_name": "18320005.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 12
  }
  Group /stimulus/presentation/Index_0_12_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_12_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_13_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C1; L2/3; RMP -70.5; Offset 20 mv;1s;-220/40"
      ],
      "file_name": "18320005.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 13
  }
  Group /stimulus/presentation/Index_0_13_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_13_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_1_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C1; L2/3; RMP -70.5; Offset 20 mv;1s;-220/40"
      ],
      "file_name": "18320005.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 1
  }
  Group /stimulus/presentation/Index_0_1_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_1_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_2_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C1; L2/3; RMP -70.5; Offset 20 mv;1s;-220/40"
      ],
      "file_name": "18320005.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 2
  }
  Group /stimulus/presentation/Index_0_2_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_2_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_3_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C1; L2/3; RMP -70.5; Offset 20 mv;1s;-220/40"
      ],
      "file_name": "18320005.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 3
  }
  Group /stimulus/presentation/Index_0_3_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_3_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_4_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C1; L2/3; RMP -70.5; Offset 20 mv;1s;-220/40"
      ],
      "file_name": "18320005.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 4
  }
  Group /stimulus/presentation/Index_0_4_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_4_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_5_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C1; L2/3; RMP -70.5; Offset 20 mv;1s;-220/40"
      ],
      "file_name": "18320005.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 5
  }
  Group /stimulus/presentation/Index_0_5_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_5_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_6_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C1; L2/3; RMP -70.5; Offset 20 mv;1s;-220/40"
      ],
      "file_name": "18320005.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 6
  }
  Group /stimulus/presentation/Index_0_6_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_6_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_7_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C1; L2/3; RMP -70.5; Offset 20 mv;1s;-220/40"
      ],
      "file_name": "18320005.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 7
  }
  Group /stimulus/presentation/Index_0_7_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_7_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_8_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C1; L2/3; RMP -70.5; Offset 20 mv;1s;-220/40"
      ],
      "file_name": "18320005.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 8
  }
  Group /stimulus/presentation/Index_0_8_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_8_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_9_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C1; L2/3; RMP -70.5; Offset 20 mv;1s;-220/40"
      ],
      "file_name": "18320005.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 9
  }
  Group /stimulus/presentation/Index_0_9_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_9_1/electrode/device (Device) 
  timestamps_reference_time: 2018-03-20T13:43:52.125000-04:00


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Index_0_0_0 (CurrentClampSeries) {
      "comments": [
          "C3; L2/3; RMP -71.3; offset -27 mv;"
      ],
      "file_name": "18320021.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 0
  }
  Group /acquisition/Index_0_0_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_0_0/electrode/device (Device) 
  Group /acquisition/Index_0_10_0 (CurrentClampSeries) {
      "comments": [
          "C3; L2/3; RMP -71.3; offset -27 mv;"
      ],
      "file_name": "18320021.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 10
  }
  Group /acquisition/Index_0_10_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_10_0/electrode/device (Device) 
  Group /acquisition/Index_0_11_0 (CurrentClampSeries) {
      "comments": [
          "C3; L2/3; RMP -71.3; offset -27 mv;"
      ],
      "file_name": "18320021.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 11
  }
  Group /acquisition/Index_0_11_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_11_0/electrode/device (Device) 
  Group /acquisition/Index_0_1_0 (CurrentClampSeries) {
      "comments": [
          "C3; L2/3; RMP -71.3; offset -27 mv;"
      ],
      "file_name": "18320021.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 1
  }
  Group /acquisition/Index_0_1_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_1_0/electrode/device (Device) 
  Group /acquisition/Index_0_2_0 (CurrentClampSeries) {
      "comments": [
          "C3; L2/3; RMP -71.3; offset -27 mv;"
      ],
      "file_name": "18320021.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 2
  }
  Group /acquisition/Index_0_2_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_2_0/electrode/device (Device) 
  Group /acquisition/Index_0_3_0 (CurrentClampSeries) {
      "comments": [
          "C3; L2/3; RMP -71.3; offset -27 mv;"
      ],
      "file_name": "18320021.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 3
  }
  Group /acquisition/Index_0_3_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_3_0/electrode/device (Device) 
  Group /acquisition/Index_0_4_0 (CurrentClampSeries) {
      "comments": [
          "C3; L2/3; RMP -71.3; offset -27 mv;"
      ],
      "file_name": "18320021.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 4
  }
  Group /acquisition/Index_0_4_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_4_0/electrode/device (Device) 
  Group /acquisition/Index_0_5_0 (CurrentClampSeries) {
      "comments": [
          "C3; L2/3; RMP -71.3; offset -27 mv;"
      ],
      "file_name": "18320021.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 5
  }
  Group /acquisition/Index_0_5_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_5_0/electrode/device (Device) 
  Group /acquisition/Index_0_6_0 (CurrentClampSeries) {
      "comments": [
          "C3; L2/3; RMP -71.3; offset -27 mv;"
      ],
      "file_name": "18320021.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 6
  }
  Group /acquisition/Index_0_6_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_6_0/electrode/device (Device) 
  Group /acquisition/Index_0_7_0 (CurrentClampSeries) {
      "comments": [
          "C3; L2/3; RMP -71.3; offset -27 mv;"
      ],
      "file_name": "18320021.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 7
  }
  Group /acquisition/Index_0_7_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_7_0/electrode/device (Device) 
  Group /acquisition/Index_0_8_0 (CurrentClampSeries) {
      "comments": [
          "C3; L2/3; RMP -71.3; offset -27 mv;"
      ],
      "file_name": "18320021.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 8
  }
  Group /acquisition/Index_0_8_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_8_0/electrode/device (Device) 
  Group /acquisition/Index_0_9_0 (CurrentClampSeries) {
      "comments": [
          "C3; L2/3; RMP -71.3; offset -27 mv;"
      ],
      "file_name": "18320021.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 9
  }
  Group /acquisition/Index_0_9_0/electrode (IntracellularElectrode) 
  Group /acquisition/Index_0_9_0/electrode/device (Device) 
  file_create_date: ['2022-07-07T17:50:05.422165-04:00']
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
  identifier: 18320021.abf
  session_description: PLACEHOLDER
  session_start_time: 2018-03-20T16:51:16.156000-04:00
  Group /stimulus/presentation/Index_0_0_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C3; L2/3; RMP -71.3; offset -27 mv;"
      ],
      "file_name": "18320021.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 0
  }
  Group /stimulus/presentation/Index_0_0_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_0_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_10_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C3; L2/3; RMP -71.3; offset -27 mv;"
      ],
      "file_name": "18320021.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 10
  }
  Group /stimulus/presentation/Index_0_10_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_10_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_11_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C3; L2/3; RMP -71.3; offset -27 mv;"
      ],
      "file_name": "18320021.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 11
  }
  Group /stimulus/presentation/Index_0_11_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_11_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_1_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C3; L2/3; RMP -71.3; offset -27 mv;"
      ],
      "file_name": "18320021.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 1
  }
  Group /stimulus/presentation/Index_0_1_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_1_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_2_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C3; L2/3; RMP -71.3; offset -27 mv;"
      ],
      "file_name": "18320021.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 2
  }
  Group /stimulus/presentation/Index_0_2_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_2_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_3_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C3; L2/3; RMP -71.3; offset -27 mv;"
      ],
      "file_name": "18320021.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 3
  }
  Group /stimulus/presentation/Index_0_3_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_3_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_4_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C3; L2/3; RMP -71.3; offset -27 mv;"
      ],
      "file_name": "18320021.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 4
  }
  Group /stimulus/presentation/Index_0_4_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_4_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_5_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C3; L2/3; RMP -71.3; offset -27 mv;"
      ],
      "file_name": "18320021.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 5
  }
  Group /stimulus/presentation/Index_0_5_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_5_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_6_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C3; L2/3; RMP -71.3; offset -27 mv;"
      ],
      "file_name": "18320021.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 6
  }
  Group /stimulus/presentation/Index_0_6_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_6_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_7_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C3; L2/3; RMP -71.3; offset -27 mv;"
      ],
      "file_name": "18320021.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 7
  }
  Group /stimulus/presentation/Index_0_7_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_7_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_8_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C3; L2/3; RMP -71.3; offset -27 mv;"
      ],
      "file_name": "18320021.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 8
  }
  Group /stimulus/presentation/Index_0_8_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_8_1/electrode/device (Device) 
  Group /stimulus/presentation/Index_0_9_1 (CurrentClampStimulusSeries) {
      "comments": [
          "C3; L2/3; RMP -71.3; offset -27 mv;"
      ],
      "file_name": "18320021.abf",
      "file_version": "1.8.3.0",
      "protocol": "long Square 1S - 220-330-40 low R",
      "protocol_path": "C:\\Documents and Settings\\Zhang\\Desktop\\Homeira\\protocol\\long Square 1S - 220-330-40 low R.pro",
      "sweep_number": 9
  }
  Group /stimulus/presentation/Index_0_9_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/Index_0_9_1/electrode/device (Device) 
  timestamps_reference_time: 2018-03-20T16:51:16.156000-04:00
