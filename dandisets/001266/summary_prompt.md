
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001266/0.250106.0948
name: Dendritic excitations govern back-propagation via a spike-rate accelerometer
contributor: [{'name': 'Park, Pojeong', 'email': 'pojeong_park@fas.harvard.edu', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-5574-6104', 'affiliation': [], 'includeInCitation': True}, {'name': 'Wong-Campos, David', 'email': 'jwongcampos@gmail.com', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Itkis, Daniel G.', 'email': 'ditkis@g.harvard.edu', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0009-0003-8948-2260', 'includeInCitation': True}, {'name': 'Lee, Byung Hun', 'email': 'byunghun_lee@fas.harvard.edu', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-0001-4846', 'includeInCitation': True}, {'name': 'Qi, Yitong', 'email': 'yitongqi@fas.harvard.edu', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Davis, Hunter C.', 'email': 'huntercoledavis@gmail.com', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Antin, Benjamin', 'email': 'ba2617@cumc.columbia.edu', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-3361-985X', 'includeInCitation': True}, {'name': 'Pasarkar, Amol', 'email': 'app2139@columbia.edu', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'includeInCitation': False}, {'name': 'Grimm, Jonathan B.', 'email': 'grimmj@janelia.hhmi.org', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0003-0331-4200', 'includeInCitation': True}, {'name': 'Plutkis, Sarah E.', 'email': 'plutkiss@janelia.hhmi.org', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0009-0003-1822-0466', 'includeInCitation': True}, {'name': 'Holland, Katie L.', 'email': 'Katie.Holland@ucsf.edu', 'schemaKey': 'Person', 'identifier': '0009-0007-1183-195X', 'includeInCitation': True}, {'name': 'Paninski, Liam', 'email': 'lmp2107@columbia.edu', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-0276-7032', 'includeInCitation': True}, {'name': 'Lavis, Luke D.', 'email': 'lavisl@janelia.hhmi.org', 'schemaKey': 'Person', 'identifier': '0000-0002-0789-6343', 'includeInCitation': True}, {'name': 'Cohen, Adam E.', 'email': 'cohen@chemistry.harvard.edu', 'roleName': ['dcite:Author', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0002-8699-2404', 'includeInCitation': True}]
description: These data are described in: https://doi.org/10.1038/s41467-025-55819-9.  Dendritic voltage imaging was performed in mouse hippocampal brain slices. Optopatch-V (CAG::LR-Voltron2-p2a-LR-CheRiff-eYFP; Addgene #203228) was expressed via in utero electroporation. The voltage indicator was loaded with JFx608 HTL dye.  Voltage imaging and targeted optogenetic stimulation were performed on a custom one-photon microscope. Please see Source Data File on the Nature Communications website for an index mapping files on DANDI to paper figure panels.

assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 97094228036, 'numberOfFiles': 84, 'numberOfSubjects': 87, 'variableMeasured': [], 'measurementTechnique': []}

Dandiset 001266 has 83 NWB files.
10 of these NWB files are of type 1.
18 of these NWB files are of type 2.
31 of these NWB files are of type 3.
23 of these NWB files are of type 4.
1 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/camera_1 (ImageSeries) no description
  Group /acquisition/camera_1/device (Device) 
  Group /acquisition/daq_aof_channel_1 (TimeSeries) aof_1:mod594
  Group /acquisition/daq_aof_channel_2 (TimeSeries) aof_2:mod488
  file_create_date: ['2024-11-29T13:15:00.870215-05:00']
  Group /general/devices/Rig (Device) Behavior_Upright
  experiment_description: SNAPT (Fig.1)
  experimenter: ['Brooks, Frederick P']
  institution: Harvard University
  lab: Adam Cohen Lab
  notes: LR-Voltron2-P2A-LR-CheRiff-eYFPJFx608
  Group /general/subject (Subject) 
  identifier: 153609PP070_P27_Cell1_soma_step_20ms
  session_description: 153609PP070_P27_Cell1_soma_step_20ms
  session_start_time: ['2022-11-19T15:36:09.000000-05:00']
  timestamps_reference_time: ['2022-11-19T15:36:09.000000-05:00']


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/camera_1 (ImageSeries) no description
  Group /acquisition/camera_1/device (Device) 
  Group /acquisition/daq_aif_channel_1 (TimeSeries) aif_1:Primary_out
  Group /acquisition/daq_aif_channel_2 (TimeSeries) aif_2:Secondary_out
  Group /acquisition/daq_aof_channel_1 (TimeSeries) aof_1:mod594
  Group /acquisition/daq_aof_channel_2 (TimeSeries) aof_2:PatchInput-freq
  Group /acquisition/daq_dof_channel_1 (TimeSeries) dof_1:488Shutter
  Group /acquisition/daq_dof_channel_2 (TimeSeries) dof_2:488enable
  Group /acquisition/daq_dof_channel_3 (TimeSeries) dof_3:enable594
  file_create_date: ['2024-12-05T00:13:26.093059-05:00']
  Group /general/devices/Rig (Device) Behavior_Upright
  experiment_description: Patch clamp (Fig. S2b)
  experimenter: ['Park, Pojeong']
  institution: Harvard University
  lab: Adam Cohen Lab
  notes: LR-Voltron2-P2A-LR-CheRiff-eYFPJFx608
  Group /general/subject (Subject) 
  identifier: 000820PP070_P17_V2_11_freq_opto_2khz
  session_description: 000820PP070_P17_V2_11_freq_opto_2khz
  session_start_time: ['2023-08-31T00:08:20.000000-04:00']
  timestamps_reference_time: ['2023-08-31T00:08:20.000000-04:00']


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/camera_1 (ImageSeries) no description
  Group /acquisition/camera_1/device (Device) 
  Group /acquisition/daq_aof_channel_1 (TimeSeries) aof_1:mod594
  Group /acquisition/daq_aof_channel_2 (TimeSeries) aof_2:mod488
  Group /acquisition/daq_dof_channel_1 (TimeSeries) dof_1:488Shutter
  Group /acquisition/daq_dof_channel_2 (TimeSeries) dof_2:488enable
  Group /acquisition/daq_dof_channel_3 (TimeSeries) dof_3:enable594
  file_create_date: ['2024-11-29T15:14:11.202978-05:00']
  Group /general/devices/Rig (Device) Behavior_Upright
  experiment_description: period_doubling (Fig. S15)
  experimenter: ['Brooks, Frederick P']
  institution: Harvard University
  lab: Adam Cohen Lab
  notes: LR-Voltron2-P2A-LR-CheRiff-eYFPJFx608
  Group /general/subject (Subject) 
  identifier: 001459PP070_P23_CA1_Cell4_blue_alone
  session_description: 001459PP070_P23_CA1_Cell4_blue_alone
  session_start_time: ['2022-05-10T00:14:59.000000-04:00']
  timestamps_reference_time: ['2022-05-10T00:14:59.000000-04:00']


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/camera_1 (ImageSeries) no description
  Group /acquisition/camera_1/device (Device) 
  Group /acquisition/daq_aof_channel_1 (TimeSeries) aof_1:mod594
  Group /acquisition/daq_aof_channel_2 (TimeSeries) aof_2:mod488
  Group /acquisition/daq_aof_channel_3 (TimeSeries) aof_3:stim1 (distal)
  Group /acquisition/daq_dof_channel_1 (TimeSeries) dof_1:enable594
  Group /acquisition/daq_dof_channel_2 (TimeSeries) dof_2:shutter488
  Group /acquisition/daq_dof_channel_3 (TimeSeries) dof_3:enable488
  file_create_date: ['2024-11-29T15:48:53.472166-05:00']
  Group /general/devices/Rig (Device) Behavior_Upright
  experiment_description: Plateau (Fig.S22-3)
  experimenter: ['Brooks, Frederick P']
  institution: Harvard University
  lab: Adam Cohen Lab
  notes: LR-Voltron2-P2A-LR-CheRiff-eYFPJFx608
  Group /general/subject (Subject) 
  identifier: 002658PP070_P17_Cell2_soma_30ms+EFS_40V_0 ms
  session_description: 002658PP070_P17_Cell2_soma_30ms+EFS_40V_0 ms
  session_start_time: ['2023-04-25T00:26:58.000000-04:00']
  timestamps_reference_time: ['2023-04-25T00:26:58.000000-04:00']


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  Group /acquisition/camera_1 (ImageSeries) no description
  Group /acquisition/camera_1/device (Device) 
  Group /acquisition/daq_aif_channel_1 (TimeSeries) aif_1:Primary_out
  Group /acquisition/daq_aif_channel_2 (TimeSeries) aif_2:Secondary_out
  Group /acquisition/daq_aof_channel_1 (TimeSeries) aof_1:mod488
  Group /acquisition/daq_aof_channel_2 (TimeSeries) aof_2:mod594
  Group /acquisition/daq_dof_channel_1 (TimeSeries) dof_1:488Shutter
  Group /acquisition/daq_dof_channel_2 (TimeSeries) dof_2:488enable
  Group /acquisition/daq_dof_channel_3 (TimeSeries) dof_3:enable594
  Group /acquisition/daq_dof_channel_4 (TimeSeries) dof_4:DMD_trigger
  file_create_date: ['2024-11-29T14:35:53.810946-05:00']
  Group /general/devices/Rig (Device) Behavior_Upright
  experiment_description: eYFP_calibration(Fig. S4a)
  experimenter: ['Brooks, Frederick P']
  institution: Harvard University
  lab: Adam Cohen Lab
  notes: LR-Voltron2-P2A-LR-CheRiff-eYFPJFx608
  Group /general/subject (Subject) 
  identifier: 163225PP070_P10_Cell2_soma_488_shift_yaxis
  session_description: 163225PP070_P10_Cell2_soma_488_shift_yaxis
  session_start_time: ['2023-09-05T16:32:25.000000-04:00']
  timestamps_reference_time: ['2023-09-05T16:32:25.000000-04:00']
