
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000538/draft
name: Comparing the 1P and 2P Voltage Contrast of JEDI2P and Voltron2_JF525
contributor: [{'name': 'Brooks, F. Phil', 'roleName': ['dcite:Author', 'dcite:DataCurator', 'dcite:DataManager', 'dcite:Investigation', 'dcite:ProjectMember', 'dcite:Researcher'], 'schemaKey': 'Person', 'identifier': '0000-0002-4334-8192', 'includeInCitation': True}, {'name': 'Davis, Hunter C.', 'roleName': ['dcite:Author', 'dcite:Conceptualization', 'dcite:DataCollector', 'dcite:DataCurator', 'dcite:DataManager', 'dcite:FormalAnalysis', 'dcite:Investigation', 'dcite:ProjectMember'], 'schemaKey': 'Person', 'includeInCitation': True}, {'url': 'https://cohenweb.rc.fas.harvard.edu/', 'name': 'Cohen, Adam', 'email': 'cohen@chemistry.harvard.edu', 'roleName': ['dcite:ContactPerson', 'dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-8699-2404', 'affiliation': [{'name': 'Harvard University', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/03vek6s52'}], 'includeInCitation': True}, {'name': 'National Institutes of Health (NIH)', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01cwqze88', 'awardNumber': '1 R01 NS 126043-01', 'includeInCitation': False}]
description: This dataset demonstrates the voltage contrast of JEDI2P and Voltron2_JF525 under 1P and 2P illumination.
assetsSummary: {'species': [{'name': 'Homo sapiens - Human', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9606'}], 'approach': [], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 1954273200, 'numberOfFiles': 11, 'numberOfSubjects': 11, 'variableMeasured': [], 'measurementTechnique': []}

Dandiset 000538 has 11 NWB files.
11 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Confocal_1 (TimeSeries) Deepsee
  Group /acquisition/camera_1 (ImageSeries) no description
  Group /acquisition/camera_1/device (Device) Optopatch Camera
  Group /acquisition/daq_aif_channel_1 (TimeSeries) aif_1:PatchFB
  Group /acquisition/daq_aif_channel_2 (TimeSeries) aif_2:2Prefpd
  Group /acquisition/daq_aof_channel_1 (TimeSeries) aof_1:488 AOTF
  Group /acquisition/daq_aof_channel_2 (TimeSeries) aof_2:EOM
  Group /acquisition/daq_aof_channel_3 (TimeSeries) aof_3:PatchV
  Group /acquisition/daq_dof_channel_1 (TimeSeries) dof_1:1P Shutter
  Group /acquisition/daq_dof_channel_2 (TimeSeries) dof_2:2P Shutter
  file_create_date: ['2023-05-10T12:46:15.999000-04:00']
  Group /general/devices/Rig (Device) Adaptive_Upright | Git Info (Branch, Hash, Remote, URL): Hunter_Development 5330b5d909c7c9ff0d6740be6a13e82c2d0135b5 origin git@Hunter:adamcohenlab/2020RigControl.git
  institution: Harvard University
  lab: Adam Cohen Lab
  Group /general/subject (Subject) 
  identifier: 173732Voltron2JF525cell2_488
  session_description: 173732Voltron2JF525cell2_488
  session_start_time: 2023-03-02T17:37:32.000000-05:00
  timestamps_reference_time: 2023-03-02T17:37:32.000000-05:00
