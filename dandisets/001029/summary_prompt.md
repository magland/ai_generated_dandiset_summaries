
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001029/draft
name: Depth dependence of 1P and 2P fluorescence
contributor: [{'name': 'Brooks, Frederick', 'email': 'fbrooks@g.harvard.edu', 'roleName': ['dcite:Author', 'dcite:Conceptualization', 'dcite:DataCurator', 'dcite:DataManager', 'dcite:ProjectMember', 'dcite:Researcher'], 'schemaKey': 'Person', 'identifier': '0000-0002-4334-8192', 'affiliation': [], 'includeInCitation': True}, {'name': 'Davis, Hunter C.', 'roleName': ['dcite:Author', 'dcite:Conceptualization', 'dcite:DataCollector', 'dcite:DataCurator', 'dcite:DataManager', 'dcite:FormalAnalysis', 'dcite:Investigation', 'dcite:ProjectMember', 'dcite:Researcher'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Wong-Campos, J. David', 'roleName': ['dcite:DataCollector', 'dcite:ProjectMember', 'dcite:Researcher'], 'schemaKey': 'Person', 'includeInCitation': True}, {'url': 'https://cohenweb.rc.fas.harvard.edu/', 'name': 'Cohen, Adam E.', 'email': 'cohen@chemistry.harvard.edu', 'roleName': ['dcite:Author', 'dcite:Conceptualization', 'dcite:ContactPerson', 'dcite:FundingAcquisition', 'dcite:Supervision'], 'schemaKey': 'Person', 'identifier': '0000-0002-8699-2404', 'includeInCitation': True}, {'name': 'NIH', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01cwqze88', 'awardNumber': 'R01-NS126043', 'includeInCitation': False}]
description: In vivo measurements of 1P and 2P fluorescence from JEDI-2P voltage indicator at depths ranging from the surface to 500 um.
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 5192080120, 'numberOfFiles': 41, 'numberOfSubjects': 1, 'variableMeasured': [], 'measurementTechnique': []}

Dandiset 001029 has 51 NWB files.
17 of these NWB files are of type 1.
34 of these NWB files are of type 2.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/image_collection (Images) A static snapshot
  Dataset /acquisition/image_collection/snap (GrayscaleImage)  | shape = (687, 950) | dtype = float64
  file_create_date: ['2024-05-16T16:56:44.045299-04:00']
  experiment_description: 2P snapshot; Depth: 150um
  experimenter: ['Davis, Hunter']
  institution: Harvard University
  lab: Adam Cohen Lab
  Group /general/subject (Subject) 
  identifier: 135024fov1snapreal
  session_description: 135024fov1snapreal
  session_start_time: ['2023-01-14T13:50:24.000000-05:00']
  timestamps_reference_time: ['2023-01-14T13:50:24.000000-05:00']


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Confocal_1 (TimeSeries) Deepsee
  Group /acquisition/DMD_1 (ImageSeries) no description
  Group /acquisition/DMD_1/device (Device) ALP_DMD_Device
  Group /acquisition/SLM_1 (ImageSeries) no description
  Group /acquisition/SLM_1/device (Device) Meadowlark_HDMI_SLM
  Group /acquisition/camera_1 (ImageSeries) no description
  Group /acquisition/camera_1/device (Device) \0
  Group /acquisition/daq_aof_channel_1 (TimeSeries) aof_1:aotf
  Group /acquisition/daq_dof_channel_1 (TimeSeries) dof_1:shutter
  file_create_date: ['2024-05-16T16:56:38.741850-04:00']
  Group /general/devices/Rig (Device) Adaptive_Upright
  experiment_description: 1P on target; Depth: 150um
  experimenter: ['Davis, Hunter']
  institution: Harvard University
  lab: Adam Cohen Lab
  Group /general/subject (Subject) 
  identifier: 135507fov1_1P
  session_description: 135507fov1_1P
  session_start_time: ['2023-01-14T13:55:07.000000-05:00']
  timestamps_reference_time: ['2023-01-14T13:55:07.000000-05:00']
