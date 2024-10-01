
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000640/0.231108.1843
name: 32-CH Local Field Potential Data During Probabilistic Reversal Learning Task
contributor: [{'name': 'Koloski, Miranda ', 'email': 'mfrancoeur@health.ucsd.edu', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [{'name': 'University of California San Diego', 'schemaKey': 'Affiliation'}, {'name': 'VA Hospital San Diego', 'schemaKey': 'Affiliation'}], 'awardNumber': 'Career Development Award IK2BX006125 ', 'includeInCitation': True}, {'name': 'Ramanathan, Dhakshin', 'email': 'dramanathan@health.ucsd.edu', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'awardNumber': 'National Institutes for Health R01-NS110905', 'includeInCitation': True}]
description: Male Long Evans Rats 7-12 months of age. 24 total animals. 256 sessions.  13 animals received a frontal traumatic brain injury (controlled cortical impact). 11 animals received Sham (no craniotomy no TBI) conditions. One week later, rats underwent a second surgery to implant 32 electrodes (Francoeur et al., Front. Psychiatry, 2021). Rats were trained to perform a self-paced probabilistic reversal learning task in a custom operant box with five noseports, stepper-motors to deliver water reward, houselight, and auditory tones. Local field potential (LFP) streams recorded simultaneously from 32 Brain Regions - recorded using a 32-Channel RHD headstage coupled to a RHD USB interface board (Intan Technologies). Open Ephys software at 1KHz band-pass filter set at 0.3-999Hz during acquisition. Lab-streaming-layer (LSL) was used to integrate physiology data with behavior. Physiology can be time-locked to trial onset (rat responds to start trial), response (rat choice between noseports), reward (time of reward delivery)
assetsSummary: {'species': [{'name': 'Rattus norvegicus - Norway rat', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10116'}], 'approach': [], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 30511569704, 'numberOfFiles': 339, 'numberOfSubjects': 24, 'variableMeasured': [], 'measurementTechnique': []}

Dandiset 000640 has 11 NWB files.
3 of these NWB files are of type 1.
1 of these NWB files are of type 2.
1 of these NWB files are of type 3.
5 of these NWB files are of type 4.
1 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/176_BrainER_raspberrypi-101 (TimeSeries) Behavioral data
  file_create_date: ['2023-09-21T11:16:46.058952-07:00']
  Group /general/subject (Subject) 
  identifier: Rat#176
  session_description: Probabilistic reversal learning task
  session_start_time: 2020-09-21T00:00:00-07:53
  timestamps_reference_time: 2020-09-21T00:00:00-07:53


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/176_BrainER_raspberrypi-107 (TimeSeries) Behavioral data
  file_create_date: ['2023-09-21T11:16:52.478851-07:00']
  Group /general/subject (Subject) 
  identifier: Rat#176
  session_description: Probabilistic reversal learning task
  session_start_time: 2020-09-23T00:00:00-07:53
  timestamps_reference_time: 2020-09-23T00:00:00-07:53


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/176_BrainER_raspberrypi-108 (TimeSeries) Behavioral data
  file_create_date: ['2023-09-21T11:17:03.664261-07:00']
  Group /general/subject (Subject) 
  identifier: Rat#176
  session_description: Probabilistic reversal learning task
  session_start_time: 2020-09-24T00:00:00-07:53
  timestamps_reference_time: 2020-09-24T00:00:00-07:53


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/176_BrainER_raspberrypi-100 (TimeSeries) Behavioral data
  file_create_date: ['2023-09-21T11:17:25.579400-07:00']
  Group /general/subject (Subject) 
  identifier: Rat#176
  session_description: Probabilistic reversal learning task
  session_start_time: 2020-09-29T00:00:00-07:53
  timestamps_reference_time: 2020-09-29T00:00:00-07:53


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  Group /acquisition/176_BrainER_raspberrypi-102 (TimeSeries) Behavioral data
  file_create_date: ['2023-09-21T11:17:48.540956-07:00']
  Group /general/subject (Subject) 
  identifier: Rat#176
  session_description: Probabilistic reversal learning task
  session_start_time: 2020-10-01T00:00:00-07:53
  timestamps_reference_time: 2020-10-01T00:00:00-07:53
