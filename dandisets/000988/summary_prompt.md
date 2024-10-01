
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000988/draft
name: Photophysics-informed two-photon voltage imaging using FRET-opsin voltage indicators
contributor: [{'name': 'Brooks, Frederick', 'email': 'fbrooks@g.harvard.edu', 'roleName': ['dcite:Author', 'dcite:Conceptualization', 'dcite:DataCollector', 'dcite:DataCurator', 'dcite:Investigation', 'dcite:Researcher', 'dcite:Visualization'], 'schemaKey': 'Person', 'identifier': '0000-0002-4334-8192', 'affiliation': [], 'includeInCitation': True}, {'name': 'Davis, Hunter C.', 'roleName': ['dcite:Conceptualization', 'dcite:Investigation', 'dcite:ProjectMember'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Park, Pojeong', 'roleName': ['dcite:DataCollector', 'dcite:ProjectMember', 'dcite:Researcher'], 'schemaKey': 'Person', 'identifier': '0000-0002-5574-6104', 'includeInCitation': True}, {'name': 'Qi, Yitong', 'roleName': ['dcite:Investigation', 'dcite:ProjectMember'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Cohen, Adam E.', 'email': 'cohen@chemistry.harvard.edu', 'roleName': ['dcite:Author', 'dcite:Conceptualization', 'dcite:ContactPerson', 'dcite:FundingAcquisition', 'dcite:Supervision'], 'schemaKey': 'Person', 'identifier': '0000-0002-8699-2404', 'includeInCitation': True}, {'name': 'NIH', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01cwqze88', 'awardNumber': '1R01NS133755; 1RF1NS126043', 'includeInCitation': False}, {'name': 'NSF', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/021nxhr62', 'awardNumber': 'OMA-2121044', 'includeInCitation': False}]
description: Voltage imaging from HEK cells, ex vivo mouse brain slice, and in vivo anaesthetized mouse barrel cortex.
One-photon photophysical exploration experiments, and two photon voltage sensitive recordings using Voltron1/2 and various dyes.
assetsSummary: {'species': [{'name': 'Homo sapiens - Human', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9606'}, {'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 66961144697, 'numberOfFiles': 174, 'numberOfSubjects': 175, 'variableMeasured': [], 'measurementTechnique': []}

Dandiset 000988 has 74 NWB files.
40 of these NWB files are of type 1.
25 of these NWB files are of type 2.
4 of these NWB files are of type 3.
4 of these NWB files are of type 4.
1 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/DMD_1 (ImageSeries) no description
  Group /acquisition/DMD_1/device (Device) ALP_DMD_Device
  Group /acquisition/camera_1 (ImageSeries) no description
  Group /acquisition/camera_1/device (Device) \0
  Group /acquisition/daq_aif_channel_1 (TimeSeries) aif_1:Patch_I
  Group /acquisition/daq_aif_channel_2 (TimeSeries) aif_2:Patch_V_feedback
  Group /acquisition/daq_aof_channel_1 (TimeSeries) aof_1:V
  Group /acquisition/daq_aof_channel_2 (TimeSeries) aof_2:594 AOTF
  Group /acquisition/daq_dof_channel_1 (TimeSeries) dof_1:Global Shutter
  Group /acquisition/daq_dof_channel_2 (TimeSeries) dof_2:594 Shutter
  file_create_date: ['2024-05-13T17:55:10.457626-04:00']
  Group /general/devices/Rig (Device) Northwest
  experiment_description: Voltage Steps
  experimenter: ['Brooks, Frederick P']
  institution: Harvard University
  lab: Adam Cohen Lab
  notes: Voltron2JF608
  Group /general/subject (Subject) 
  identifier: 104306voltron2_608_cell2_vsteps_OD1
  session_description: 104306voltron2_608_cell2_vsteps_OD1
  session_start_time: ['2023-03-30T10:43:06.000000-04:00']
  timestamps_reference_time: ['2023-03-30T10:43:06.000000-04:00']


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Confocal_1 (TimeSeries) Deepsee
  Group /acquisition/DMD_1 (ImageSeries) no description
  Group /acquisition/DMD_1/device (Device) ALP_DMD_Device
  Group /acquisition/SLM_1 (ImageSeries) no description
  Group /acquisition/SLM_1/device (Device) Meadowlark_HDMI_SLM
  Group /acquisition/camera_1 (ImageSeries) no description
  Group /acquisition/camera_1/device (Device) S/N: 001430
  Group /acquisition/daq_aif_channel_1 (TimeSeries) aif_1:refPD
  Group /acquisition/daq_aif_channel_2 (TimeSeries) aif_2:Patch_I
  Group /acquisition/daq_aif_channel_3 (TimeSeries) aif_3:1PrefPD
  Group /acquisition/daq_aof_channel_1 (TimeSeries) aof_1:V
  Group /acquisition/daq_aof_channel_2 (TimeSeries) aof_2:2P EOM
  Group /acquisition/daq_aof_channel_3 (TimeSeries) aof_3:AOTF
  Group /acquisition/daq_dof_channel_1 (TimeSeries) dof_1:2P Shutter
  Group /acquisition/daq_dof_channel_2 (TimeSeries) dof_2:1P Shutter
  file_create_date: ['2024-05-13T18:25:17.472758-04:00']
  Group /general/devices/Rig (Device) Adaptive_Upright
  experiment_description: 2P Voltage Steps
  experimenter: ['Brooks, Frederick P']
  institution: Harvard University
  lab: Adam Cohen Lab
  notes: Voltron2JF549
  Group /general/subject (Subject) 
  identifier: 104828cell1_jf549_1040nm_Vsteps
  session_description: 104828cell1_jf549_1040nm_Vsteps
  session_start_time: ['2023-03-29T10:48:28.000000-04:00']
  timestamps_reference_time: ['2023-03-29T10:48:28.000000-04:00']


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Confocal_1 (TimeSeries) Deepsee
  Group /acquisition/DMD_1 (ImageSeries) no description
  Group /acquisition/DMD_1/device (Device) ALP_DMD_Device
  Group /acquisition/SLM_1 (ImageSeries) no description
  Group /acquisition/SLM_1/device (Device) Meadowlark_HDMI_SLM
  Group /acquisition/camera_1 (ImageSeries) no description
  Group /acquisition/camera_1/device (Device) S/N: 001430
  Group /acquisition/daq_aif_channel_1 (TimeSeries) aif_1:refPD
  Group /acquisition/daq_aif_channel_2 (TimeSeries) aif_2:Patch_I
  Group /acquisition/daq_aif_channel_3 (TimeSeries) aif_3:1PrefPD
  Group /acquisition/daq_aof_channel_1 (TimeSeries) aof_1:V
  Group /acquisition/daq_aof_channel_2 (TimeSeries) aof_2:2P EOM
  Group /acquisition/daq_dof_channel_1 (TimeSeries) dof_1:2P shutter
  file_create_date: ['2024-05-13T19:02:56.672996-04:00']
  Group /general/devices/Rig (Device) Adaptive_Upright
  experiment_description: 2P Inversion
  experimenter: ['Brooks, Frederick P']
  institution: Harvard University
  lab: Adam Cohen Lab
  notes: Voltron2JF549
  Group /general/subject (Subject) 
  identifier: 105552cell1_jf549_1040nm_findinv
  session_description: 105552cell1_jf549_1040nm_findinv
  session_start_time: ['2023-03-29T10:55:52.000000-04:00']
  timestamps_reference_time: ['2023-03-29T10:55:52.000000-04:00']


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Confocal_1 (TimeSeries) Deepsee
  Group /acquisition/DMD_1 (ImageSeries) no description
  Group /acquisition/DMD_1/device (Device) ALP_DMD_Device
  Group /acquisition/SLM_1 (ImageSeries) no description
  Group /acquisition/SLM_1/device (Device) Meadowlark_HDMI_SLM
  Group /acquisition/camera_1 (ImageSeries) no description
  Group /acquisition/camera_1/device (Device) S/N: 001430
  Group /acquisition/daq_aif_channel_1 (TimeSeries) aif_1:refPD
  Group /acquisition/daq_aif_channel_2 (TimeSeries) aif_2:Patch_I
  Group /acquisition/daq_aif_channel_3 (TimeSeries) aif_3:1PrefPD
  Group /acquisition/daq_aof_channel_1 (TimeSeries) aof_1:V
  Group /acquisition/daq_aof_channel_2 (TimeSeries) aof_2:2P EOM
  Group /acquisition/daq_aof_channel_3 (TimeSeries) aof_3:Green AOTF
  Group /acquisition/daq_aof_channel_4 (TimeSeries) aof_4:Blue AOTF
  Group /acquisition/daq_dof_channel_1 (TimeSeries) dof_1:2P Shutter
  Group /acquisition/daq_dof_channel_2 (TimeSeries) dof_2:1P Shutter
  file_create_date: ['2024-05-13T18:36:46.548289-04:00']
  Group /general/devices/Rig (Device) Adaptive_Upright
  experiment_description: 2P Voltage Steps
  experimenter: ['Brooks, Frederick P']
  institution: Harvard University
  lab: Adam Cohen Lab
  notes: Voltron2JF585
  Group /general/subject (Subject) 
  identifier: 122122session2_voltron2_JF585_cell2_vsteps_withblue
  session_description: 122122session2_voltron2_JF585_cell2_vsteps_withblue
  session_start_time: ['2023-03-16T12:21:22.000000-04:00']
  timestamps_reference_time: ['2023-03-16T12:21:22.000000-04:00']


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Confocal_1 (TimeSeries) Deepsee
  Group /acquisition/DMD_1 (ImageSeries) no description
  Group /acquisition/DMD_1/device (Device) ALP_DMD_Device
  Group /acquisition/SLM_1 (ImageSeries) no description
  Group /acquisition/SLM_1/device (Device) Meadowlark_HDMI_SLM
  Group /acquisition/camera_1 (ImageSeries) no description
  Group /acquisition/camera_1/device (Device) S/N: 001430
  Group /acquisition/daq_aif_channel_1 (TimeSeries) aif_1:refPD
  Group /acquisition/daq_aif_channel_2 (TimeSeries) aif_2:Patch_I
  Group /acquisition/daq_aof_channel_1 (TimeSeries) aof_1:V
  Group /acquisition/daq_aof_channel_2 (TimeSeries) aof_2:2P EOM
  Group /acquisition/daq_aof_channel_3 (TimeSeries) aof_3:AOTF
  Group /acquisition/daq_dof_channel_1 (TimeSeries) dof_1:2P shutter
  file_create_date: ['2024-05-13T19:04:04.613465-04:00']
  Group /general/devices/Rig (Device) Adaptive_Upright
  experiment_description: 2P Inversion
  experimenter: ['Brooks, Frederick P']
  institution: Harvard University
  lab: Adam Cohen Lab
  notes: Voltron1JF608
  Group /general/subject (Subject) 
  identifier: 132231voltron1JF608cell1_inversion2P
  session_description: 132231voltron1JF608cell1_inversion2P
  session_start_time: ['2023-03-16T13:22:31.000000-04:00']
  timestamps_reference_time: ['2023-03-16T13:22:31.000000-04:00']
