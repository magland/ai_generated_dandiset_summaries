
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000537/draft
name: Scaling of GEVI Fluorescence with 1P and 2P Illumination
contributor: [{'name': 'Davis, Hunter C.', 'roleName': ['dcite:Author', 'dcite:Conceptualization', 'dcite:DataCollector', 'dcite:DataCurator', 'dcite:DataManager', 'dcite:FormalAnalysis', 'dcite:Investigation', 'dcite:ProjectMember'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Brooks, F. Phil', 'roleName': ['dcite:Author', 'dcite:DataCollector', 'dcite:DataCurator', 'dcite:DataManager', 'dcite:Investigation', 'dcite:ProjectMember'], 'schemaKey': 'Person', 'identifier': '0000-0002-4334-8192', 'includeInCitation': True}, {'url': 'https://cohenweb.rc.fas.harvard.edu/', 'name': 'Cohen, Adam E.', 'email': 'cohen@chemistry.harvard.edu', 'roleName': ['dcite:ContactPerson', 'dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-8699-2404', 'affiliation': [{'name': 'Harvard University', 'schemaKey': 'Affiliation'}], 'includeInCitation': True}, {'name': 'National Institutes of Health (NIH)', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': '1 R01 NS 126043-01'}]
description: This dataset contains videos demonstrating the fluorescence of Human Embryonic Kidney (HEK) cells transfected with common genetically encoded voltage indicators (GEVIs). 
assetsSummary: {'species': [{'name': 'Homo sapiens - Human', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9606'}], 'approach': [], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 6440628584, 'numberOfFiles': 125, 'numberOfSubjects': 125, 'variableMeasured': [], 'measurementTechnique': []}

Dandiset 000537 has 100 NWB files.
100 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Confocal_1 (TimeSeries) Deepsee
  Group /acquisition/camera_1 (ImageSeries) no description
  Group /acquisition/camera_1/device (Device) Optopatch Camera
  Group /acquisition/daq_aif_channel_1 (TimeSeries) aif_1:ref_PD
  Group /acquisition/daq_aof_channel_1 (TimeSeries) aof_1:aotf
  Group /acquisition/daq_aof_channel_2 (TimeSeries) aof_2:eom
  Group /acquisition/daq_dof_channel_1 (TimeSeries) dof_1:488shutter
  Group /acquisition/daq_dof_channel_2 (TimeSeries) dof_2:DSShutter
  file_create_date: ['2023-05-10T12:20:56.148000-04:00']
  Group /general/devices/Rig (Device) Adaptive_Upright | Git Info (Branch, Hash, Remote, URL): master a24418db1fc6f44b817cbf594950222208a022aa origin git@Hunter:adamcohenlab/2020RigControl.git
  institution: Harvard University
  lab: Adam Cohen Lab
  Group /general/subject (Subject) 
  identifier: 035955cell2_JF525
  session_description: 035955cell2_JF525
  session_start_time: 2022-07-29T03:59:55.000000-04:00
  timestamps_reference_time: 2022-07-29T03:59:55.000000-04:00
