
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000952/0.240731.1609
name: 32 CH local field potential recording of rodents performing a temporal discounting task
contributor: [{'name': 'Koloski, Miranda ', 'email': 'mfrancoeur@health.ucsd.edu', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}]
description: Local field potential (LFP) recordings from 12 male Long-Evans rats during a temporal discounting task. LFP was recording using an RHD interface board (Intantech) and Open Ephys recording software. Data was recorded at 1Khz, with a band-pass filter set at 0.3 to 999 Hz during acquisition. Physiology data was integrated with behavioral data using a lab-streaming-layer (LSL) protocol. Recordings are taken from 32 different brain areas. Subjects chose between a small (10uL/ 1s) reward delivered after a fixed short delay (500ms after response) or a large (30uL/3s) reward delivered after a fixed delay that varied from session to session (500ms, 1, 2, 5, 10, 20s). 
assetsSummary: {'species': [{'name': 'Rattus norvegicus - Norway rat', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10116'}], 'approach': [], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 74361063204, 'numberOfFiles': 216, 'numberOfSubjects': 73, 'variableMeasured': [], 'measurementTechnique': []}

Dandiset 000952 has 21 NWB files.
17 of these NWB files are of type 1.
1 of these NWB files are of type 2.
1 of these NWB files are of type 3.
1 of these NWB files are of type 4.
1 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/R125_BrainER_raspberrypi-102 (TimeSeries) Behavioral data
  Group /acquisition/R125_LFP_neatlabsrat2 (TimeSeries) Electrophysiology data
  file_create_date: ['2024-07-13T22:23:18.363965-07:00']
  Group /general/subject (Subject) 
  identifier: 09212020_Rat#R125
  session_description: Probabilistic reversal learning task
  session_start_time: 2020-09-21T00:00:00-07:00
  timestamps_reference_time: 2020-09-21T00:00:00-07:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/R125_BrainER_raspberrypi-104 (TimeSeries) Behavioral data
  Group /acquisition/R125_LFP_neatlabs-HP-Z2-Mini-G3-Workstation (TimeSeries) Electrophysiology data
  file_create_date: ['2024-07-14T00:52:00.840559-07:00']
  Group /general/subject (Subject) 
  identifier: 10072020_Rat#R125
  session_description: Probabilistic reversal learning task
  session_start_time: 2020-10-07T00:00:00-07:00
  timestamps_reference_time: 2020-10-07T00:00:00-07:00


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/R125_S5_BrainER_raspberrypi-102 (TimeSeries) Behavioral data
  Group /acquisition/R125_S5_LFP_neatlabsrat2 (TimeSeries) Electrophysiology data
  file_create_date: ['2024-07-14T05:35:54.169597-07:00']
  Group /general/subject (Subject) 
  identifier: 10202020_Rat#R125_S5
  session_description: Probabilistic reversal learning task
  session_start_time: 2020-10-20T00:00:00-07:00
  timestamps_reference_time: 2020-10-20T00:00:00-07:00


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/R125_BrainER_raspberrypi-105 (TimeSeries) Behavioral data
  file_create_date: ['2024-07-14T05:59:13.165777-07:00']
  Group /general/subject (Subject) 
  identifier: 10222020_Rat#R125
  session_description: Probabilistic reversal learning task
  session_start_time: 2020-10-22T00:00:00-07:00
  timestamps_reference_time: 2020-10-22T00:00:00-07:00


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  Group /acquisition/R125_BrainER_raspberrypi-100 (TimeSeries) Behavioral data
  file_create_date: ['2024-07-14T05:59:25.030583-07:00']
  Group /general/subject (Subject) 
  identifier: 10232020_Rat#R125
  session_description: Probabilistic reversal learning task
  session_start_time: 2020-10-23T00:00:00-07:00
  timestamps_reference_time: 2020-10-23T00:00:00-07:00
