
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000012/draft
name: Kriegstein2020
contributor: [{'name': 'Zhou, Li', 'roleName': ['dcite:Author', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [{'name': 'Eli and Edythe Broad Center of Regeneration Medicine and Stem Cell Research UCSF School of Medicine', 'schemaKey': 'Affiliation', 'includeInCitation': False}], 'includeInCitation': True}, {'name': 'Kriegstein, Arnold', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0001-5742-2990', 'affiliation': [], 'includeInCitation': True}]
description: Data from the Kriegstein Lab as part of the BICCN
assetsSummary: {'species': [{'name': 'Human', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9606'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 487524911, 'numberOfCells': 38, 'numberOfFiles': 297, 'numberOfSamples': 8, 'numberOfSubjects': 4, 'variableMeasured': ['VoltageClampStimulusSeries', 'VoltageClampSeries'], 'measurementTechnique': [{'name': 'voltage clamp technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000012 has 63 NWB files.
16 of these NWB files are of type 1.
17 of these NWB files are of type 2.
3 of these NWB files are of type 3.
6 of these NWB files are of type 4.
21 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/index_0 (IZeroClampSeries) {
      "cycle_id": 0,
      "file": "18516000.abf",
      "name": "IN 0",
      "number": 0,
      "protocol": "0 cc_Vrest",
      "protocolPath": "D:\\li zhou\\Params\\ins\\0 cc_Vrest.pro"
  }
  Group /acquisition/index_0/electrode (IntracellularElectrode) 
  Group /acquisition/index_0/electrode/device (Device) 
  file_create_date: ['2021-03-24T17:28:37.896401-04:00']
  Group /general/DandiIcephysMetadata (DandiIcephysMetadata) 
  Group /general/devices/DD132X with MultiClamp 700 (Device) 
  experiment_description: Clampex v10.3.2.1
  experimenter: ['Li Zhou']
  institution: UCSF
  Group /general/intracellular_ephys/Electrode 0 (IntracellularElectrode) 
  Group /general/intracellular_ephys/Electrode 0/device (Device) 
  Group /general/intracellular_ephys/sweep_table (SweepTable) A sweep table groups different PatchClampSeries together.
  Dataset /general/intracellular_ephys/sweep_table/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /general/intracellular_ephys/sweep_table/series (VectorData) PatchClampSeries with the same sweep number | shape = (1,) | dtype = object
  Dataset /general/intracellular_ephys/sweep_table/series_index (VectorIndex) Index for VectorData 'series' | shape = (1,) | dtype = uint8
  Dataset /general/intracellular_ephys/sweep_table/sweep_number (VectorData) Sweep number of the entries in that row | shape = (1,) | dtype = uint64
  session_id: 18516000
  source_script: {
      "git_revision": "(add_metadata) aadd7d2",
      "package_version": "1.4.0",
      "repo": "https://github.com/AllenInstitute/ipfx"
  }
  Group /general/subject (Subject) 
  identifier: 8c0546550685546d34e49c48f32d738c22199cd48c0d2f601fb8e21b810292b5
  session_description: PLACEHOLDER
  session_start_time: 2018-05-16T19:47:27.843000-04:00
  timestamps_reference_time: 2018-05-16T19:47:27.843000-04:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/index_0 (VoltageClampSeries) {
      "cycle_id": 0,
      "file": "18516002.abf",
      "name": "IN 0",
      "number": 0,
      "protocol": "1 VC negative voltage",
      "protocolPath": "D:\\li zhou\\Params\\ins\\1 VC negative voltage.pro"
  }
  Group /acquisition/index_0/electrode (IntracellularElectrode) 
  Group /acquisition/index_0/electrode/device (Device) 
  Group /acquisition/index_1 (VoltageClampSeries) {
      "cycle_id": 1,
      "file": "18516002.abf",
      "name": "IN 0",
      "number": 0,
      "protocol": "1 VC negative voltage",
      "protocolPath": "D:\\li zhou\\Params\\ins\\1 VC negative voltage.pro"
  }
  Group /acquisition/index_1/electrode (IntracellularElectrode) 
  Group /acquisition/index_1/electrode/device (Device) 
  Group /acquisition/index_2 (VoltageClampSeries) {
      "cycle_id": 2,
      "file": "18516002.abf",
      "name": "IN 0",
      "number": 0,
      "protocol": "1 VC negative voltage",
      "protocolPath": "D:\\li zhou\\Params\\ins\\1 VC negative voltage.pro"
  }
  Group /acquisition/index_2/electrode (IntracellularElectrode) 
  Group /acquisition/index_2/electrode/device (Device) 
  Group /acquisition/index_3 (VoltageClampSeries) {
      "cycle_id": 3,
      "file": "18516002.abf",
      "name": "IN 0",
      "number": 0,
      "protocol": "1 VC negative voltage",
      "protocolPath": "D:\\li zhou\\Params\\ins\\1 VC negative voltage.pro"
  }
  Group /acquisition/index_3/electrode (IntracellularElectrode) 
  Group /acquisition/index_3/electrode/device (Device) 
  Group /acquisition/index_4 (VoltageClampSeries) {
      "cycle_id": 4,
      "file": "18516002.abf",
      "name": "IN 0",
      "number": 0,
      "protocol": "1 VC negative voltage",
      "protocolPath": "D:\\li zhou\\Params\\ins\\1 VC negative voltage.pro"
  }
  Group /acquisition/index_4/electrode (IntracellularElectrode) 
  Group /acquisition/index_4/electrode/device (Device) 
  Group /acquisition/index_5 (VoltageClampSeries) {
      "cycle_id": 5,
      "file": "18516002.abf",
      "name": "IN 0",
      "number": 0,
      "protocol": "1 VC negative voltage",
      "protocolPath": "D:\\li zhou\\Params\\ins\\1 VC negative voltage.pro"
  }
  Group /acquisition/index_5/electrode (IntracellularElectrode) 
  Group /acquisition/index_5/electrode/device (Device) 
  Group /acquisition/index_6 (VoltageClampSeries) {
      "cycle_id": 6,
      "file": "18516002.abf",
      "name": "IN 0",
      "number": 0,
      "protocol": "1 VC negative voltage",
      "protocolPath": "D:\\li zhou\\Params\\ins\\1 VC negative voltage.pro"
  }
  Group /acquisition/index_6/electrode (IntracellularElectrode) 
  Group /acquisition/index_6/electrode/device (Device) 
  Group /acquisition/index_7 (VoltageClampSeries) {
      "cycle_id": 7,
      "file": "18516002.abf",
      "name": "IN 0",
      "number": 0,
      "protocol": "1 VC negative voltage",
      "protocolPath": "D:\\li zhou\\Params\\ins\\1 VC negative voltage.pro"
  }
  Group /acquisition/index_7/electrode (IntracellularElectrode) 
  Group /acquisition/index_7/electrode/device (Device) 
  Group /acquisition/index_8 (VoltageClampSeries) {
      "cycle_id": 8,
      "file": "18516002.abf",
      "name": "IN 0",
      "number": 0,
      "protocol": "1 VC negative voltage",
      "protocolPath": "D:\\li zhou\\Params\\ins\\1 VC negative voltage.pro"
  }
  Group /acquisition/index_8/electrode (IntracellularElectrode) 
  Group /acquisition/index_8/electrode/device (Device) 
  Group /acquisition/index_9 (VoltageClampSeries) {
      "cycle_id": 9,
      "file": "18516002.abf",
      "name": "IN 0",
      "number": 0,
      "protocol": "1 VC negative voltage",
      "protocolPath": "D:\\li zhou\\Params\\ins\\1 VC negative voltage.pro"
  }
  Group /acquisition/index_9/electrode (IntracellularElectrode) 
  Group /acquisition/index_9/electrode/device (Device) 
  file_create_date: ['2021-03-24T17:28:39.847104-04:00']
  Group /general/DandiIcephysMetadata (DandiIcephysMetadata) 
  Group /general/devices/DD132X with MultiClamp 700 (Device) 
  experiment_description: Clampex v10.3.2.1
  experimenter: ['Li Zhou']
  institution: UCSF
  Group /general/intracellular_ephys/Electrode 0 (IntracellularElectrode) 
  Group /general/intracellular_ephys/Electrode 0/device (Device) 
  Group /general/intracellular_ephys/sweep_table (SweepTable) A sweep table groups different PatchClampSeries together.
  Dataset /general/intracellular_ephys/sweep_table/id (ElementIdentifiers)  | shape = (20,) | dtype = int64
  Dataset /general/intracellular_ephys/sweep_table/series (VectorData) PatchClampSeries with the same sweep number | shape = (20,) | dtype = object
  Dataset /general/intracellular_ephys/sweep_table/series_index (VectorIndex) Index for VectorData 'series' | shape = (20,) | dtype = uint8
  Dataset /general/intracellular_ephys/sweep_table/sweep_number (VectorData) Sweep number of the entries in that row | shape = (20,) | dtype = uint64
  session_id: 18516002
  source_script: {
      "git_revision": "(add_metadata) aadd7d2",
      "package_version": "1.4.0",
      "repo": "https://github.com/AllenInstitute/ipfx"
  }
  Group /general/subject (Subject) 
  identifier: e520f1286e0b5e56f50b3b8d736a51011d1cf1fbb9a9315fa5286a67a1e8dda4
  session_description: PLACEHOLDER
  session_start_time: 2018-05-16T19:47:59.390000-04:00
  Group /stimulus/presentation/index_0 (VoltageClampStimulusSeries) {
      "cycle_id": 0,
      "file": "18516002.abf",
      "name": "CC OUT 0",
      "number": 0,
      "protocol": "1 VC negative voltage",
      "protocolPath": "D:\\li zhou\\Params\\ins\\1 VC negative voltage.pro"
  }
  Group /stimulus/presentation/index_0/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_0/electrode/device (Device) 
  Group /stimulus/presentation/index_1 (VoltageClampStimulusSeries) {
      "cycle_id": 1,
      "file": "18516002.abf",
      "name": "CC OUT 0",
      "number": 0,
      "protocol": "1 VC negative voltage",
      "protocolPath": "D:\\li zhou\\Params\\ins\\1 VC negative voltage.pro"
  }
  Group /stimulus/presentation/index_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_1/electrode/device (Device) 
  Group /stimulus/presentation/index_2 (VoltageClampStimulusSeries) {
      "cycle_id": 2,
      "file": "18516002.abf",
      "name": "CC OUT 0",
      "number": 0,
      "protocol": "1 VC negative voltage",
      "protocolPath": "D:\\li zhou\\Params\\ins\\1 VC negative voltage.pro"
  }
  Group /stimulus/presentation/index_2/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_2/electrode/device (Device) 
  Group /stimulus/presentation/index_3 (VoltageClampStimulusSeries) {
      "cycle_id": 3,
      "file": "18516002.abf",
      "name": "CC OUT 0",
      "number": 0,
      "protocol": "1 VC negative voltage",
      "protocolPath": "D:\\li zhou\\Params\\ins\\1 VC negative voltage.pro"
  }
  Group /stimulus/presentation/index_3/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_3/electrode/device (Device) 
  Group /stimulus/presentation/index_4 (VoltageClampStimulusSeries) {
      "cycle_id": 4,
      "file": "18516002.abf",
      "name": "CC OUT 0",
      "number": 0,
      "protocol": "1 VC negative voltage",
      "protocolPath": "D:\\li zhou\\Params\\ins\\1 VC negative voltage.pro"
  }
  Group /stimulus/presentation/index_4/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_4/electrode/device (Device) 
  Group /stimulus/presentation/index_5 (VoltageClampStimulusSeries) {
      "cycle_id": 5,
      "file": "18516002.abf",
      "name": "CC OUT 0",
      "number": 0,
      "protocol": "1 VC negative voltage",
      "protocolPath": "D:\\li zhou\\Params\\ins\\1 VC negative voltage.pro"
  }
  Group /stimulus/presentation/index_5/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_5/electrode/device (Device) 
  Group /stimulus/presentation/index_6 (VoltageClampStimulusSeries) {
      "cycle_id": 6,
      "file": "18516002.abf",
      "name": "CC OUT 0",
      "number": 0,
      "protocol": "1 VC negative voltage",
      "protocolPath": "D:\\li zhou\\Params\\ins\\1 VC negative voltage.pro"
  }
  Group /stimulus/presentation/index_6/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_6/electrode/device (Device) 
  Group /stimulus/presentation/index_7 (VoltageClampStimulusSeries) {
      "cycle_id": 7,
      "file": "18516002.abf",
      "name": "CC OUT 0",
      "number": 0,
      "protocol": "1 VC negative voltage",
      "protocolPath": "D:\\li zhou\\Params\\ins\\1 VC negative voltage.pro"
  }
  Group /stimulus/presentation/index_7/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_7/electrode/device (Device) 
  Group /stimulus/presentation/index_8 (VoltageClampStimulusSeries) {
      "cycle_id": 8,
      "file": "18516002.abf",
      "name": "CC OUT 0",
      "number": 0,
      "protocol": "1 VC negative voltage",
      "protocolPath": "D:\\li zhou\\Params\\ins\\1 VC negative voltage.pro"
  }
  Group /stimulus/presentation/index_8/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_8/electrode/device (Device) 
  Group /stimulus/presentation/index_9 (VoltageClampStimulusSeries) {
      "cycle_id": 9,
      "file": "18516002.abf",
      "name": "CC OUT 0",
      "number": 0,
      "protocol": "1 VC negative voltage",
      "protocolPath": "D:\\li zhou\\Params\\ins\\1 VC negative voltage.pro"
  }
  Group /stimulus/presentation/index_9/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_9/electrode/device (Device) 
  timestamps_reference_time: 2018-05-16T19:47:59.390000-04:00


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/index_0 (CurrentClampSeries) {
      "cycle_id": 0,
      "file": "18516004.abf",
      "name": "IN 0",
      "number": 0,
      "protocol": "2 cc negative current step Li",
      "protocolPath": "D:\\li zhou\\Params\\ins\\2 cc negative current step Li.pro"
  }
  Group /acquisition/index_0/electrode (IntracellularElectrode) 
  Group /acquisition/index_0/electrode/device (Device) 
  Group /acquisition/index_1 (CurrentClampSeries) {
      "cycle_id": 1,
      "file": "18516004.abf",
      "name": "IN 0",
      "number": 0,
      "protocol": "2 cc negative current step Li",
      "protocolPath": "D:\\li zhou\\Params\\ins\\2 cc negative current step Li.pro"
  }
  Group /acquisition/index_1/electrode (IntracellularElectrode) 
  Group /acquisition/index_1/electrode/device (Device) 
  Group /acquisition/index_2 (CurrentClampSeries) {
      "cycle_id": 2,
      "file": "18516004.abf",
      "name": "IN 0",
      "number": 0,
      "protocol": "2 cc negative current step Li",
      "protocolPath": "D:\\li zhou\\Params\\ins\\2 cc negative current step Li.pro"
  }
  Group /acquisition/index_2/electrode (IntracellularElectrode) 
  Group /acquisition/index_2/electrode/device (Device) 
  Group /acquisition/index_3 (CurrentClampSeries) {
      "cycle_id": 3,
      "file": "18516004.abf",
      "name": "IN 0",
      "number": 0,
      "protocol": "2 cc negative current step Li",
      "protocolPath": "D:\\li zhou\\Params\\ins\\2 cc negative current step Li.pro"
  }
  Group /acquisition/index_3/electrode (IntracellularElectrode) 
  Group /acquisition/index_3/electrode/device (Device) 
  Group /acquisition/index_4 (CurrentClampSeries) {
      "cycle_id": 4,
      "file": "18516004.abf",
      "name": "IN 0",
      "number": 0,
      "protocol": "2 cc negative current step Li",
      "protocolPath": "D:\\li zhou\\Params\\ins\\2 cc negative current step Li.pro"
  }
  Group /acquisition/index_4/electrode (IntracellularElectrode) 
  Group /acquisition/index_4/electrode/device (Device) 
  Group /acquisition/index_5 (CurrentClampSeries) {
      "cycle_id": 5,
      "file": "18516004.abf",
      "name": "IN 0",
      "number": 0,
      "protocol": "2 cc negative current step Li",
      "protocolPath": "D:\\li zhou\\Params\\ins\\2 cc negative current step Li.pro"
  }
  Group /acquisition/index_5/electrode (IntracellularElectrode) 
  Group /acquisition/index_5/electrode/device (Device) 
  file_create_date: ['2021-03-24T17:28:42.473599-04:00']
  Group /general/DandiIcephysMetadata (DandiIcephysMetadata) 
  Group /general/devices/DD132X with MultiClamp 700 (Device) 
  experiment_description: Clampex v10.3.2.1
  experimenter: ['Li Zhou']
  institution: UCSF
  Group /general/intracellular_ephys/Electrode 0 (IntracellularElectrode) 
  Group /general/intracellular_ephys/Electrode 0/device (Device) 
  Group /general/intracellular_ephys/sweep_table (SweepTable) A sweep table groups different PatchClampSeries together.
  Dataset /general/intracellular_ephys/sweep_table/id (ElementIdentifiers)  | shape = (12,) | dtype = int64
  Dataset /general/intracellular_ephys/sweep_table/series (VectorData) PatchClampSeries with the same sweep number | shape = (12,) | dtype = object
  Dataset /general/intracellular_ephys/sweep_table/series_index (VectorIndex) Index for VectorData 'series' | shape = (12,) | dtype = uint8
  Dataset /general/intracellular_ephys/sweep_table/sweep_number (VectorData) Sweep number of the entries in that row | shape = (12,) | dtype = uint64
  session_id: 18516004
  source_script: {
      "git_revision": "(add_metadata) aadd7d2",
      "package_version": "1.4.0",
      "repo": "https://github.com/AllenInstitute/ipfx"
  }
  Group /general/subject (Subject) 
  identifier: b2e6040496ee6d219c801dbf50148ee99b7338b9e9a6f0be9890a465f7b00f25
  session_description: PLACEHOLDER
  session_start_time: 2018-05-16T19:49:14.515000-04:00
  Group /stimulus/presentation/index_0 (CurrentClampStimulusSeries) {
      "cycle_id": 0,
      "file": "18516004.abf",
      "name": "CC OUT 0",
      "number": 0,
      "protocol": "2 cc negative current step Li",
      "protocolPath": "D:\\li zhou\\Params\\ins\\2 cc negative current step Li.pro"
  }
  Group /stimulus/presentation/index_0/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_0/electrode/device (Device) 
  Group /stimulus/presentation/index_1 (CurrentClampStimulusSeries) {
      "cycle_id": 1,
      "file": "18516004.abf",
      "name": "CC OUT 0",
      "number": 0,
      "protocol": "2 cc negative current step Li",
      "protocolPath": "D:\\li zhou\\Params\\ins\\2 cc negative current step Li.pro"
  }
  Group /stimulus/presentation/index_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_1/electrode/device (Device) 
  Group /stimulus/presentation/index_2 (CurrentClampStimulusSeries) {
      "cycle_id": 2,
      "file": "18516004.abf",
      "name": "CC OUT 0",
      "number": 0,
      "protocol": "2 cc negative current step Li",
      "protocolPath": "D:\\li zhou\\Params\\ins\\2 cc negative current step Li.pro"
  }
  Group /stimulus/presentation/index_2/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_2/electrode/device (Device) 
  Group /stimulus/presentation/index_3 (CurrentClampStimulusSeries) {
      "cycle_id": 3,
      "file": "18516004.abf",
      "name": "CC OUT 0",
      "number": 0,
      "protocol": "2 cc negative current step Li",
      "protocolPath": "D:\\li zhou\\Params\\ins\\2 cc negative current step Li.pro"
  }
  Group /stimulus/presentation/index_3/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_3/electrode/device (Device) 
  Group /stimulus/presentation/index_4 (CurrentClampStimulusSeries) {
      "cycle_id": 4,
      "file": "18516004.abf",
      "name": "CC OUT 0",
      "number": 0,
      "protocol": "2 cc negative current step Li",
      "protocolPath": "D:\\li zhou\\Params\\ins\\2 cc negative current step Li.pro"
  }
  Group /stimulus/presentation/index_4/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_4/electrode/device (Device) 
  Group /stimulus/presentation/index_5 (CurrentClampStimulusSeries) {
      "cycle_id": 5,
      "file": "18516004.abf",
      "name": "CC OUT 0",
      "number": 0,
      "protocol": "2 cc negative current step Li",
      "protocolPath": "D:\\li zhou\\Params\\ins\\2 cc negative current step Li.pro"
  }
  Group /stimulus/presentation/index_5/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_5/electrode/device (Device) 
  timestamps_reference_time: 2018-05-16T19:49:14.515000-04:00


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/index_0 (CurrentClampSeries) {
      "cycle_id": 0,
      "file": "18516005.abf",
      "name": "IN 0",
      "number": 0,
      "protocol": "2 cc negative current step Li",
      "protocolPath": "D:\\li zhou\\Params\\ins\\2 cc negative current step Li.pro"
  }
  Group /acquisition/index_0/electrode (IntracellularElectrode) 
  Group /acquisition/index_0/electrode/device (Device) 
  Group /acquisition/index_1 (CurrentClampSeries) {
      "cycle_id": 1,
      "file": "18516005.abf",
      "name": "IN 0",
      "number": 0,
      "protocol": "2 cc negative current step Li",
      "protocolPath": "D:\\li zhou\\Params\\ins\\2 cc negative current step Li.pro"
  }
  Group /acquisition/index_1/electrode (IntracellularElectrode) 
  Group /acquisition/index_1/electrode/device (Device) 
  Group /acquisition/index_2 (CurrentClampSeries) {
      "cycle_id": 2,
      "file": "18516005.abf",
      "name": "IN 0",
      "number": 0,
      "protocol": "2 cc negative current step Li",
      "protocolPath": "D:\\li zhou\\Params\\ins\\2 cc negative current step Li.pro"
  }
  Group /acquisition/index_2/electrode (IntracellularElectrode) 
  Group /acquisition/index_2/electrode/device (Device) 
  Group /acquisition/index_3 (CurrentClampSeries) {
      "cycle_id": 3,
      "file": "18516005.abf",
      "name": "IN 0",
      "number": 0,
      "protocol": "2 cc negative current step Li",
      "protocolPath": "D:\\li zhou\\Params\\ins\\2 cc negative current step Li.pro"
  }
  Group /acquisition/index_3/electrode (IntracellularElectrode) 
  Group /acquisition/index_3/electrode/device (Device) 
  Group /acquisition/index_4 (CurrentClampSeries) {
      "cycle_id": 4,
      "file": "18516005.abf",
      "name": "IN 0",
      "number": 0,
      "protocol": "2 cc negative current step Li",
      "protocolPath": "D:\\li zhou\\Params\\ins\\2 cc negative current step Li.pro"
  }
  Group /acquisition/index_4/electrode (IntracellularElectrode) 
  Group /acquisition/index_4/electrode/device (Device) 
  Group /acquisition/index_5 (CurrentClampSeries) {
      "cycle_id": 5,
      "file": "18516005.abf",
      "name": "IN 0",
      "number": 0,
      "protocol": "2 cc negative current step Li",
      "protocolPath": "D:\\li zhou\\Params\\ins\\2 cc negative current step Li.pro"
  }
  Group /acquisition/index_5/electrode (IntracellularElectrode) 
  Group /acquisition/index_5/electrode/device (Device) 
  Group /acquisition/index_6 (CurrentClampSeries) {
      "cycle_id": 6,
      "file": "18516005.abf",
      "name": "IN 0",
      "number": 0,
      "protocol": "2 cc negative current step Li",
      "protocolPath": "D:\\li zhou\\Params\\ins\\2 cc negative current step Li.pro"
  }
  Group /acquisition/index_6/electrode (IntracellularElectrode) 
  Group /acquisition/index_6/electrode/device (Device) 
  Group /acquisition/index_7 (CurrentClampSeries) {
      "cycle_id": 7,
      "file": "18516005.abf",
      "name": "IN 0",
      "number": 0,
      "protocol": "2 cc negative current step Li",
      "protocolPath": "D:\\li zhou\\Params\\ins\\2 cc negative current step Li.pro"
  }
  Group /acquisition/index_7/electrode (IntracellularElectrode) 
  Group /acquisition/index_7/electrode/device (Device) 
  Group /acquisition/index_8 (CurrentClampSeries) {
      "cycle_id": 8,
      "file": "18516005.abf",
      "name": "IN 0",
      "number": 0,
      "protocol": "2 cc negative current step Li",
      "protocolPath": "D:\\li zhou\\Params\\ins\\2 cc negative current step Li.pro"
  }
  Group /acquisition/index_8/electrode (IntracellularElectrode) 
  Group /acquisition/index_8/electrode/device (Device) 
  Group /acquisition/index_9 (CurrentClampSeries) {
      "cycle_id": 9,
      "file": "18516005.abf",
      "name": "IN 0",
      "number": 0,
      "protocol": "2 cc negative current step Li",
      "protocolPath": "D:\\li zhou\\Params\\ins\\2 cc negative current step Li.pro"
  }
  Group /acquisition/index_9/electrode (IntracellularElectrode) 
  Group /acquisition/index_9/electrode/device (Device) 
  file_create_date: ['2021-03-24T17:28:43.874359-04:00']
  Group /general/DandiIcephysMetadata (DandiIcephysMetadata) 
  Group /general/devices/DD132X with MultiClamp 700 (Device) 
  experiment_description: Clampex v10.3.2.1
  experimenter: ['Li Zhou']
  institution: UCSF
  Group /general/intracellular_ephys/Electrode 0 (IntracellularElectrode) 
  Group /general/intracellular_ephys/Electrode 0/device (Device) 
  Group /general/intracellular_ephys/sweep_table (SweepTable) A sweep table groups different PatchClampSeries together.
  Dataset /general/intracellular_ephys/sweep_table/id (ElementIdentifiers)  | shape = (20,) | dtype = int64
  Dataset /general/intracellular_ephys/sweep_table/series (VectorData) PatchClampSeries with the same sweep number | shape = (20,) | dtype = object
  Dataset /general/intracellular_ephys/sweep_table/series_index (VectorIndex) Index for VectorData 'series' | shape = (20,) | dtype = uint8
  Dataset /general/intracellular_ephys/sweep_table/sweep_number (VectorData) Sweep number of the entries in that row | shape = (20,) | dtype = uint64
  session_id: 18516005
  source_script: {
      "git_revision": "(add_metadata) aadd7d2",
      "package_version": "1.4.0",
      "repo": "https://github.com/AllenInstitute/ipfx"
  }
  Group /general/subject (Subject) 
  identifier: b2e6040496ee6d219c801dbf50148ee99b7338b9e9a6f0be9890a465f7b00f25
  session_description: PLACEHOLDER
  session_start_time: 2018-05-16T19:50:23.578000-04:00
  Group /stimulus/presentation/index_0 (CurrentClampStimulusSeries) {
      "cycle_id": 0,
      "file": "18516005.abf",
      "name": "CC OUT 0",
      "number": 0,
      "protocol": "2 cc negative current step Li",
      "protocolPath": "D:\\li zhou\\Params\\ins\\2 cc negative current step Li.pro"
  }
  Group /stimulus/presentation/index_0/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_0/electrode/device (Device) 
  Group /stimulus/presentation/index_1 (CurrentClampStimulusSeries) {
      "cycle_id": 1,
      "file": "18516005.abf",
      "name": "CC OUT 0",
      "number": 0,
      "protocol": "2 cc negative current step Li",
      "protocolPath": "D:\\li zhou\\Params\\ins\\2 cc negative current step Li.pro"
  }
  Group /stimulus/presentation/index_1/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_1/electrode/device (Device) 
  Group /stimulus/presentation/index_2 (CurrentClampStimulusSeries) {
      "cycle_id": 2,
      "file": "18516005.abf",
      "name": "CC OUT 0",
      "number": 0,
      "protocol": "2 cc negative current step Li",
      "protocolPath": "D:\\li zhou\\Params\\ins\\2 cc negative current step Li.pro"
  }
  Group /stimulus/presentation/index_2/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_2/electrode/device (Device) 
  Group /stimulus/presentation/index_3 (CurrentClampStimulusSeries) {
      "cycle_id": 3,
      "file": "18516005.abf",
      "name": "CC OUT 0",
      "number": 0,
      "protocol": "2 cc negative current step Li",
      "protocolPath": "D:\\li zhou\\Params\\ins\\2 cc negative current step Li.pro"
  }
  Group /stimulus/presentation/index_3/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_3/electrode/device (Device) 
  Group /stimulus/presentation/index_4 (CurrentClampStimulusSeries) {
      "cycle_id": 4,
      "file": "18516005.abf",
      "name": "CC OUT 0",
      "number": 0,
      "protocol": "2 cc negative current step Li",
      "protocolPath": "D:\\li zhou\\Params\\ins\\2 cc negative current step Li.pro"
  }
  Group /stimulus/presentation/index_4/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_4/electrode/device (Device) 
  Group /stimulus/presentation/index_5 (CurrentClampStimulusSeries) {
      "cycle_id": 5,
      "file": "18516005.abf",
      "name": "CC OUT 0",
      "number": 0,
      "protocol": "2 cc negative current step Li",
      "protocolPath": "D:\\li zhou\\Params\\ins\\2 cc negative current step Li.pro"
  }
  Group /stimulus/presentation/index_5/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_5/electrode/device (Device) 
  Group /stimulus/presentation/index_6 (CurrentClampStimulusSeries) {
      "cycle_id": 6,
      "file": "18516005.abf",
      "name": "CC OUT 0",
      "number": 0,
      "protocol": "2 cc negative current step Li",
      "protocolPath": "D:\\li zhou\\Params\\ins\\2 cc negative current step Li.pro"
  }
  Group /stimulus/presentation/index_6/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_6/electrode/device (Device) 
  Group /stimulus/presentation/index_7 (CurrentClampStimulusSeries) {
      "cycle_id": 7,
      "file": "18516005.abf",
      "name": "CC OUT 0",
      "number": 0,
      "protocol": "2 cc negative current step Li",
      "protocolPath": "D:\\li zhou\\Params\\ins\\2 cc negative current step Li.pro"
  }
  Group /stimulus/presentation/index_7/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_7/electrode/device (Device) 
  Group /stimulus/presentation/index_8 (CurrentClampStimulusSeries) {
      "cycle_id": 8,
      "file": "18516005.abf",
      "name": "CC OUT 0",
      "number": 0,
      "protocol": "2 cc negative current step Li",
      "protocolPath": "D:\\li zhou\\Params\\ins\\2 cc negative current step Li.pro"
  }
  Group /stimulus/presentation/index_8/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_8/electrode/device (Device) 
  Group /stimulus/presentation/index_9 (CurrentClampStimulusSeries) {
      "cycle_id": 9,
      "file": "18516005.abf",
      "name": "CC OUT 0",
      "number": 0,
      "protocol": "2 cc negative current step Li",
      "protocolPath": "D:\\li zhou\\Params\\ins\\2 cc negative current step Li.pro"
  }
  Group /stimulus/presentation/index_9/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_9/electrode/device (Device) 
  timestamps_reference_time: 2018-05-16T19:50:23.578000-04:00


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  Group /acquisition/index_00 (VoltageClampSeries) {
      "cycle_id": 0,
      "file": "18516006.abf",
      "name": "IN 0",
      "number": 0,
      "protocol": "3 VC step NaK (whole cell compensation)",
      "protocolPath": "D:\\li zhou\\Params\\ins\\3 VC step NaK (whole cell compensation).pro"
  }
  Group /acquisition/index_00/electrode (IntracellularElectrode) 
  Group /acquisition/index_00/electrode/device (Device) 
  Group /acquisition/index_01 (VoltageClampSeries) {
      "cycle_id": 1,
      "file": "18516006.abf",
      "name": "IN 0",
      "number": 0,
      "protocol": "3 VC step NaK (whole cell compensation)",
      "protocolPath": "D:\\li zhou\\Params\\ins\\3 VC step NaK (whole cell compensation).pro"
  }
  Group /acquisition/index_01/electrode (IntracellularElectrode) 
  Group /acquisition/index_01/electrode/device (Device) 
  Group /acquisition/index_02 (VoltageClampSeries) {
      "cycle_id": 2,
      "file": "18516006.abf",
      "name": "IN 0",
      "number": 0,
      "protocol": "3 VC step NaK (whole cell compensation)",
      "protocolPath": "D:\\li zhou\\Params\\ins\\3 VC step NaK (whole cell compensation).pro"
  }
  Group /acquisition/index_02/electrode (IntracellularElectrode) 
  Group /acquisition/index_02/electrode/device (Device) 
  Group /acquisition/index_03 (VoltageClampSeries) {
      "cycle_id": 3,
      "file": "18516006.abf",
      "name": "IN 0",
      "number": 0,
      "protocol": "3 VC step NaK (whole cell compensation)",
      "protocolPath": "D:\\li zhou\\Params\\ins\\3 VC step NaK (whole cell compensation).pro"
  }
  Group /acquisition/index_03/electrode (IntracellularElectrode) 
  Group /acquisition/index_03/electrode/device (Device) 
  Group /acquisition/index_04 (VoltageClampSeries) {
      "cycle_id": 4,
      "file": "18516006.abf",
      "name": "IN 0",
      "number": 0,
      "protocol": "3 VC step NaK (whole cell compensation)",
      "protocolPath": "D:\\li zhou\\Params\\ins\\3 VC step NaK (whole cell compensation).pro"
  }
  Group /acquisition/index_04/electrode (IntracellularElectrode) 
  Group /acquisition/index_04/electrode/device (Device) 
  Group /acquisition/index_05 (VoltageClampSeries) {
      "cycle_id": 5,
      "file": "18516006.abf",
      "name": "IN 0",
      "number": 0,
      "protocol": "3 VC step NaK (whole cell compensation)",
      "protocolPath": "D:\\li zhou\\Params\\ins\\3 VC step NaK (whole cell compensation).pro"
  }
  Group /acquisition/index_05/electrode (IntracellularElectrode) 
  Group /acquisition/index_05/electrode/device (Device) 
  Group /acquisition/index_06 (VoltageClampSeries) {
      "cycle_id": 6,
      "file": "18516006.abf",
      "name": "IN 0",
      "number": 0,
      "protocol": "3 VC step NaK (whole cell compensation)",
      "protocolPath": "D:\\li zhou\\Params\\ins\\3 VC step NaK (whole cell compensation).pro"
  }
  Group /acquisition/index_06/electrode (IntracellularElectrode) 
  Group /acquisition/index_06/electrode/device (Device) 
  Group /acquisition/index_07 (VoltageClampSeries) {
      "cycle_id": 7,
      "file": "18516006.abf",
      "name": "IN 0",
      "number": 0,
      "protocol": "3 VC step NaK (whole cell compensation)",
      "protocolPath": "D:\\li zhou\\Params\\ins\\3 VC step NaK (whole cell compensation).pro"
  }
  Group /acquisition/index_07/electrode (IntracellularElectrode) 
  Group /acquisition/index_07/electrode/device (Device) 
  Group /acquisition/index_08 (VoltageClampSeries) {
      "cycle_id": 8,
      "file": "18516006.abf",
      "name": "IN 0",
      "number": 0,
      "protocol": "3 VC step NaK (whole cell compensation)",
      "protocolPath": "D:\\li zhou\\Params\\ins\\3 VC step NaK (whole cell compensation).pro"
  }
  Group /acquisition/index_08/electrode (IntracellularElectrode) 
  Group /acquisition/index_08/electrode/device (Device) 
  Group /acquisition/index_09 (VoltageClampSeries) {
      "cycle_id": 9,
      "file": "18516006.abf",
      "name": "IN 0",
      "number": 0,
      "protocol": "3 VC step NaK (whole cell compensation)",
      "protocolPath": "D:\\li zhou\\Params\\ins\\3 VC step NaK (whole cell compensation).pro"
  }
  Group /acquisition/index_09/electrode (IntracellularElectrode) 
  Group /acquisition/index_09/electrode/device (Device) 
  Group /acquisition/index_10 (VoltageClampSeries) {
      "cycle_id": 10,
      "file": "18516006.abf",
      "name": "IN 0",
      "number": 0,
      "protocol": "3 VC step NaK (whole cell compensation)",
      "protocolPath": "D:\\li zhou\\Params\\ins\\3 VC step NaK (whole cell compensation).pro"
  }
  Group /acquisition/index_10/electrode (IntracellularElectrode) 
  Group /acquisition/index_10/electrode/device (Device) 
  Group /acquisition/index_11 (VoltageClampSeries) {
      "cycle_id": 11,
      "file": "18516006.abf",
      "name": "IN 0",
      "number": 0,
      "protocol": "3 VC step NaK (whole cell compensation)",
      "protocolPath": "D:\\li zhou\\Params\\ins\\3 VC step NaK (whole cell compensation).pro"
  }
  Group /acquisition/index_11/electrode (IntracellularElectrode) 
  Group /acquisition/index_11/electrode/device (Device) 
  Group /acquisition/index_12 (VoltageClampSeries) {
      "cycle_id": 12,
      "file": "18516006.abf",
      "name": "IN 0",
      "number": 0,
      "protocol": "3 VC step NaK (whole cell compensation)",
      "protocolPath": "D:\\li zhou\\Params\\ins\\3 VC step NaK (whole cell compensation).pro"
  }
  Group /acquisition/index_12/electrode (IntracellularElectrode) 
  Group /acquisition/index_12/electrode/device (Device) 
  Group /acquisition/index_13 (VoltageClampSeries) {
      "cycle_id": 13,
      "file": "18516006.abf",
      "name": "IN 0",
      "number": 0,
      "protocol": "3 VC step NaK (whole cell compensation)",
      "protocolPath": "D:\\li zhou\\Params\\ins\\3 VC step NaK (whole cell compensation).pro"
  }
  Group /acquisition/index_13/electrode (IntracellularElectrode) 
  Group /acquisition/index_13/electrode/device (Device) 
  Group /acquisition/index_14 (VoltageClampSeries) {
      "cycle_id": 14,
      "file": "18516006.abf",
      "name": "IN 0",
      "number": 0,
      "protocol": "3 VC step NaK (whole cell compensation)",
      "protocolPath": "D:\\li zhou\\Params\\ins\\3 VC step NaK (whole cell compensation).pro"
  }
  Group /acquisition/index_14/electrode (IntracellularElectrode) 
  Group /acquisition/index_14/electrode/device (Device) 
  Group /acquisition/index_15 (VoltageClampSeries) {
      "cycle_id": 15,
      "file": "18516006.abf",
      "name": "IN 0",
      "number": 0,
      "protocol": "3 VC step NaK (whole cell compensation)",
      "protocolPath": "D:\\li zhou\\Params\\ins\\3 VC step NaK (whole cell compensation).pro"
  }
  Group /acquisition/index_15/electrode (IntracellularElectrode) 
  Group /acquisition/index_15/electrode/device (Device) 
  Group /acquisition/index_16 (VoltageClampSeries) {
      "cycle_id": 16,
      "file": "18516006.abf",
      "name": "IN 0",
      "number": 0,
      "protocol": "3 VC step NaK (whole cell compensation)",
      "protocolPath": "D:\\li zhou\\Params\\ins\\3 VC step NaK (whole cell compensation).pro"
  }
  Group /acquisition/index_16/electrode (IntracellularElectrode) 
  Group /acquisition/index_16/electrode/device (Device) 
  Group /acquisition/index_17 (VoltageClampSeries) {
      "cycle_id": 17,
      "file": "18516006.abf",
      "name": "IN 0",
      "number": 0,
      "protocol": "3 VC step NaK (whole cell compensation)",
      "protocolPath": "D:\\li zhou\\Params\\ins\\3 VC step NaK (whole cell compensation).pro"
  }
  Group /acquisition/index_17/electrode (IntracellularElectrode) 
  Group /acquisition/index_17/electrode/device (Device) 
  Group /acquisition/index_18 (VoltageClampSeries) {
      "cycle_id": 18,
      "file": "18516006.abf",
      "name": "IN 0",
      "number": 0,
      "protocol": "3 VC step NaK (whole cell compensation)",
      "protocolPath": "D:\\li zhou\\Params\\ins\\3 VC step NaK (whole cell compensation).pro"
  }
  Group /acquisition/index_18/electrode (IntracellularElectrode) 
  Group /acquisition/index_18/electrode/device (Device) 
  Group /acquisition/index_19 (VoltageClampSeries) {
      "cycle_id": 19,
      "file": "18516006.abf",
      "name": "IN 0",
      "number": 0,
      "protocol": "3 VC step NaK (whole cell compensation)",
      "protocolPath": "D:\\li zhou\\Params\\ins\\3 VC step NaK (whole cell compensation).pro"
  }
  Group /acquisition/index_19/electrode (IntracellularElectrode) 
  Group /acquisition/index_19/electrode/device (Device) 
  file_create_date: ['2021-03-24T17:28:45.158184-04:00']
  Group /general/DandiIcephysMetadata (DandiIcephysMetadata) 
  Group /general/devices/DD132X with MultiClamp 700 (Device) 
  experiment_description: Clampex v10.3.2.1
  experimenter: ['Li Zhou']
  institution: UCSF
  Group /general/intracellular_ephys/Electrode 0 (IntracellularElectrode) 
  Group /general/intracellular_ephys/Electrode 0/device (Device) 
  Group /general/intracellular_ephys/sweep_table (SweepTable) A sweep table groups different PatchClampSeries together.
  Dataset /general/intracellular_ephys/sweep_table/id (ElementIdentifiers)  | shape = (40,) | dtype = int64
  Dataset /general/intracellular_ephys/sweep_table/series (VectorData) PatchClampSeries with the same sweep number | shape = (40,) | dtype = object
  Dataset /general/intracellular_ephys/sweep_table/series_index (VectorIndex) Index for VectorData 'series' | shape = (40,) | dtype = uint8
  Dataset /general/intracellular_ephys/sweep_table/sweep_number (VectorData) Sweep number of the entries in that row | shape = (40,) | dtype = uint64
  session_id: 18516006
  source_script: {
      "git_revision": "(add_metadata) aadd7d2",
      "package_version": "1.4.0",
      "repo": "https://github.com/AllenInstitute/ipfx"
  }
  Group /general/subject (Subject) 
  identifier: 55f93d887ae37a2ed46a3509143a3fa57a8b61c498fd39c9c5062b889fa22650
  session_description: PLACEHOLDER
  session_start_time: 2018-05-16T21:21:20.653000-04:00
  Group /stimulus/presentation/index_00 (VoltageClampStimulusSeries) {
      "cycle_id": 0,
      "file": "18516006.abf",
      "name": "OUT 0",
      "number": 0,
      "protocol": "3 VC step NaK (whole cell compensation)",
      "protocolPath": "D:\\li zhou\\Params\\ins\\3 VC step NaK (whole cell compensation).pro"
  }
  Group /stimulus/presentation/index_00/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_00/electrode/device (Device) 
  Group /stimulus/presentation/index_01 (VoltageClampStimulusSeries) {
      "cycle_id": 1,
      "file": "18516006.abf",
      "name": "OUT 0",
      "number": 0,
      "protocol": "3 VC step NaK (whole cell compensation)",
      "protocolPath": "D:\\li zhou\\Params\\ins\\3 VC step NaK (whole cell compensation).pro"
  }
  Group /stimulus/presentation/index_01/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_01/electrode/device (Device) 
  Group /stimulus/presentation/index_02 (VoltageClampStimulusSeries) {
      "cycle_id": 2,
      "file": "18516006.abf",
      "name": "OUT 0",
      "number": 0,
      "protocol": "3 VC step NaK (whole cell compensation)",
      "protocolPath": "D:\\li zhou\\Params\\ins\\3 VC step NaK (whole cell compensation).pro"
  }
  Group /stimulus/presentation/index_02/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_02/electrode/device (Device) 
  Group /stimulus/presentation/index_03 (VoltageClampStimulusSeries) {
      "cycle_id": 3,
      "file": "18516006.abf",
      "name": "OUT 0",
      "number": 0,
      "protocol": "3 VC step NaK (whole cell compensation)",
      "protocolPath": "D:\\li zhou\\Params\\ins\\3 VC step NaK (whole cell compensation).pro"
  }
  Group /stimulus/presentation/index_03/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_03/electrode/device (Device) 
  Group /stimulus/presentation/index_04 (VoltageClampStimulusSeries) {
      "cycle_id": 4,
      "file": "18516006.abf",
      "name": "OUT 0",
      "number": 0,
      "protocol": "3 VC step NaK (whole cell compensation)",
      "protocolPath": "D:\\li zhou\\Params\\ins\\3 VC step NaK (whole cell compensation).pro"
  }
  Group /stimulus/presentation/index_04/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_04/electrode/device (Device) 
  Group /stimulus/presentation/index_05 (VoltageClampStimulusSeries) {
      "cycle_id": 5,
      "file": "18516006.abf",
      "name": "OUT 0",
      "number": 0,
      "protocol": "3 VC step NaK (whole cell compensation)",
      "protocolPath": "D:\\li zhou\\Params\\ins\\3 VC step NaK (whole cell compensation).pro"
  }
  Group /stimulus/presentation/index_05/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_05/electrode/device (Device) 
  Group /stimulus/presentation/index_06 (VoltageClampStimulusSeries) {
      "cycle_id": 6,
      "file": "18516006.abf",
      "name": "OUT 0",
      "number": 0,
      "protocol": "3 VC step NaK (whole cell compensation)",
      "protocolPath": "D:\\li zhou\\Params\\ins\\3 VC step NaK (whole cell compensation).pro"
  }
  Group /stimulus/presentation/index_06/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_06/electrode/device (Device) 
  Group /stimulus/presentation/index_07 (VoltageClampStimulusSeries) {
      "cycle_id": 7,
      "file": "18516006.abf",
      "name": "OUT 0",
      "number": 0,
      "protocol": "3 VC step NaK (whole cell compensation)",
      "protocolPath": "D:\\li zhou\\Params\\ins\\3 VC step NaK (whole cell compensation).pro"
  }
  Group /stimulus/presentation/index_07/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_07/electrode/device (Device) 
  Group /stimulus/presentation/index_08 (VoltageClampStimulusSeries) {
      "cycle_id": 8,
      "file": "18516006.abf",
      "name": "OUT 0",
      "number": 0,
      "protocol": "3 VC step NaK (whole cell compensation)",
      "protocolPath": "D:\\li zhou\\Params\\ins\\3 VC step NaK (whole cell compensation).pro"
  }
  Group /stimulus/presentation/index_08/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_08/electrode/device (Device) 
  Group /stimulus/presentation/index_09 (VoltageClampStimulusSeries) {
      "cycle_id": 9,
      "file": "18516006.abf",
      "name": "OUT 0",
      "number": 0,
      "protocol": "3 VC step NaK (whole cell compensation)",
      "protocolPath": "D:\\li zhou\\Params\\ins\\3 VC step NaK (whole cell compensation).pro"
  }
  Group /stimulus/presentation/index_09/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_09/electrode/device (Device) 
  Group /stimulus/presentation/index_10 (VoltageClampStimulusSeries) {
      "cycle_id": 10,
      "file": "18516006.abf",
      "name": "OUT 0",
      "number": 0,
      "protocol": "3 VC step NaK (whole cell compensation)",
      "protocolPath": "D:\\li zhou\\Params\\ins\\3 VC step NaK (whole cell compensation).pro"
  }
  Group /stimulus/presentation/index_10/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_10/electrode/device (Device) 
  Group /stimulus/presentation/index_11 (VoltageClampStimulusSeries) {
      "cycle_id": 11,
      "file": "18516006.abf",
      "name": "OUT 0",
      "number": 0,
      "protocol": "3 VC step NaK (whole cell compensation)",
      "protocolPath": "D:\\li zhou\\Params\\ins\\3 VC step NaK (whole cell compensation).pro"
  }
  Group /stimulus/presentation/index_11/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_11/electrode/device (Device) 
  Group /stimulus/presentation/index_12 (VoltageClampStimulusSeries) {
      "cycle_id": 12,
      "file": "18516006.abf",
      "name": "OUT 0",
      "number": 0,
      "protocol": "3 VC step NaK (whole cell compensation)",
      "protocolPath": "D:\\li zhou\\Params\\ins\\3 VC step NaK (whole cell compensation).pro"
  }
  Group /stimulus/presentation/index_12/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_12/electrode/device (Device) 
  Group /stimulus/presentation/index_13 (VoltageClampStimulusSeries) {
      "cycle_id": 13,
      "file": "18516006.abf",
      "name": "OUT 0",
      "number": 0,
      "protocol": "3 VC step NaK (whole cell compensation)",
      "protocolPath": "D:\\li zhou\\Params\\ins\\3 VC step NaK (whole cell compensation).pro"
  }
  Group /stimulus/presentation/index_13/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_13/electrode/device (Device) 
  Group /stimulus/presentation/index_14 (VoltageClampStimulusSeries) {
      "cycle_id": 14,
      "file": "18516006.abf",
      "name": "OUT 0",
      "number": 0,
      "protocol": "3 VC step NaK (whole cell compensation)",
      "protocolPath": "D:\\li zhou\\Params\\ins\\3 VC step NaK (whole cell compensation).pro"
  }
  Group /stimulus/presentation/index_14/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_14/electrode/device (Device) 
  Group /stimulus/presentation/index_15 (VoltageClampStimulusSeries) {
      "cycle_id": 15,
      "file": "18516006.abf",
      "name": "OUT 0",
      "number": 0,
      "protocol": "3 VC step NaK (whole cell compensation)",
      "protocolPath": "D:\\li zhou\\Params\\ins\\3 VC step NaK (whole cell compensation).pro"
  }
  Group /stimulus/presentation/index_15/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_15/electrode/device (Device) 
  Group /stimulus/presentation/index_16 (VoltageClampStimulusSeries) {
      "cycle_id": 16,
      "file": "18516006.abf",
      "name": "OUT 0",
      "number": 0,
      "protocol": "3 VC step NaK (whole cell compensation)",
      "protocolPath": "D:\\li zhou\\Params\\ins\\3 VC step NaK (whole cell compensation).pro"
  }
  Group /stimulus/presentation/index_16/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_16/electrode/device (Device) 
  Group /stimulus/presentation/index_17 (VoltageClampStimulusSeries) {
      "cycle_id": 17,
      "file": "18516006.abf",
      "name": "OUT 0",
      "number": 0,
      "protocol": "3 VC step NaK (whole cell compensation)",
      "protocolPath": "D:\\li zhou\\Params\\ins\\3 VC step NaK (whole cell compensation).pro"
  }
  Group /stimulus/presentation/index_17/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_17/electrode/device (Device) 
  Group /stimulus/presentation/index_18 (VoltageClampStimulusSeries) {
      "cycle_id": 18,
      "file": "18516006.abf",
      "name": "OUT 0",
      "number": 0,
      "protocol": "3 VC step NaK (whole cell compensation)",
      "protocolPath": "D:\\li zhou\\Params\\ins\\3 VC step NaK (whole cell compensation).pro"
  }
  Group /stimulus/presentation/index_18/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_18/electrode/device (Device) 
  Group /stimulus/presentation/index_19 (VoltageClampStimulusSeries) {
      "cycle_id": 19,
      "file": "18516006.abf",
      "name": "OUT 0",
      "number": 0,
      "protocol": "3 VC step NaK (whole cell compensation)",
      "protocolPath": "D:\\li zhou\\Params\\ins\\3 VC step NaK (whole cell compensation).pro"
  }
  Group /stimulus/presentation/index_19/electrode (IntracellularElectrode) 
  Group /stimulus/presentation/index_19/electrode/device (Device) 
  timestamps_reference_time: 2018-05-16T21:21:20.653000-04:00
