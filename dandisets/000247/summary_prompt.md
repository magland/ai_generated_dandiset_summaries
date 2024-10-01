
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000247/draft
name: Calcium imaging of egg-laying related neurons in head-fixed Drosophila
contributor: [{'name': 'National Institutes of Health (NIH)', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': '1 R01 NS 121904-01', 'contactPoint': [], 'includeInCitation': False}, {'name': 'Vijayan, Vikram', 'email': 'vvijayan@rockefeller.edu', 'roleName': ['dcite:Author', 'dcite:Conceptualization', 'dcite:ContactPerson', 'dcite:DataCollector'], 'schemaKey': 'Person', 'identifier': '0000-0003-3948-7568', 'affiliation': [{'name': 'Rockefeller University', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/0420db125'}, {'name': 'Howard Hughes Medical Institute', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/006w34k90'}], 'includeInCitation': True}, {'name': 'Maimon, Gaby', 'email': 'maimon@rockefeller.edu', 'roleName': ['dcite:Author', 'dcite:Conceptualization', 'dcite:ContactPerson', 'dcite:Supervision'], 'schemaKey': 'Person', 'identifier': '0000-0003-1219-5856', 'affiliation': [{'name': 'Rockefeller University', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/0420bd125'}, {'name': 'Howard Hughes Medical Institute', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/006w34k90'}], 'includeInCitation': True}, {'name': 'Leon Levy Foundation', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'contactPoint': [], 'includeInCitation': False}, {'name': 'Kavli Neural Systems Institute', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'contactPoint': [], 'includeInCitation': False}, {'name': 'The Rockefeller University', 'roleName': ['dcite:Funder', 'dcite:Affiliation'], 'schemaKey': 'Organization', 'contactPoint': [], 'includeInCitation': False}, {'name': 'Howard Hughes Medical Institute', 'roleName': ['dcite:Funder', 'dcite:Affiliation'], 'schemaKey': 'Organization', 'contactPoint': [], 'includeInCitation': False}]
description: Datasets on 2-photon calcium imaging of oviposition descending neurons (oviDNs) as head-fixed flies walk and lay eggs on an agarose-laden wheel. Each NWB file contains time series data from an individual recording session from an individual fly: imaging data, behavior data, and stimulation data (if applicable). A variety of fly genotypes and a variety of environments (egg-laying wheels) were used. Data and methods are described in "A rise-to-threshold signal for a relative value deliberation" (https://www.biorxiv.org/content/10.1101/2021.09.23.461548v1). Please contact Vikram Vijayan and/or Gaby Maimon for more information including different download options and different raw/processed data formats.
assetsSummary: {'species': [{'name': 'Drosophila melanogaster - Fruit fly', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_7227'}], 'approach': [], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 30300179800, 'numberOfFiles': 194, 'numberOfSubjects': 158, 'variableMeasured': ['ProcessingModule'], 'measurementTechnique': [{'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000247 has 29 NWB files.
13 of these NWB files are of type 1.
2 of these NWB files are of type 2.
7 of these NWB files are of type 3.
3 of these NWB files are of type 4.
4 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2022-06-09T15:39:07.014000-04:00']
  experiment_description: GCaMP7 imaging of oviDNs on an egg-laying wheel (see sucrose concentration and agarose concentration in behavior_mod to extract composition of wheel and stimulation_mod, if applicable, for any optogenetics)
  experimenter: ['Vikram Vijayan']
  institution: The Rockefeller University / HHMI
  session_id: 2019_11_11_0000_oviDNSS1&SS01048_GCaMP7f.nwb
  Group /general/subject (Subject) 
  identifier: 2019_11_11_0000_oviDNSS1&SS01048_GCaMP7f.nwb
  Group /processing/behavior (ProcessingModule) contains behavioral data
  Group /processing/behavior/agarose concentration (TimeSeries) agarose concentration of current substrate
  Group /processing/behavior/body angle (TimeSeries) body angle
  Group /processing/behavior/body length (TimeSeries) body length normalized to median
  Group /processing/behavior/proboscis length (TimeSeries) proboscis length normalized to median
  Group /processing/behavior/sucrose concentration (TimeSeries) sucrose concentration of current substrate
  Group /processing/behavior/velocity (TimeSeries) speed
  Group /processing/behavior/wheel position (TimeSeries) wheel position
  Group /processing/ophys (ProcessingModule) ccontains 2-photon calcium imaging data
  Group /processing/ophys/background ROI df over f (TimeSeries) background ROI
  Group /processing/ophys/background ROI mean signal in ROI (TimeSeries) background ROI
  Group /processing/ophys/left oviDNa df over f (TimeSeries) left oviDNa
  Group /processing/ophys/left oviDNa mean signal in ROI (TimeSeries) left oviDNa
  Group /processing/ophys/left oviDNb df over f (TimeSeries) left oviDNb
  Group /processing/ophys/left oviDNb mean signal in ROI (TimeSeries) left oviDNb
  session_description: fly on egg-laying wheel
  session_start_time: 2021-01-01T01:01:01.000000-05:00
  timestamps_reference_time: 2021-01-01T01:01:01.000000-05:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2022-06-09T15:40:11.465000-04:00']
  experiment_description: GCaMP7 imaging of oviDNs on an egg-laying wheel (see sucrose concentration and agarose concentration in behavior_mod to extract composition of wheel and stimulation_mod, if applicable, for any optogenetics)
  experimenter: ['Vikram Vijayan']
  institution: The Rockefeller University / HHMI
  session_id: 2019_11_18_0001_oviDNSS1&SS01048_GCaMP7f.nwb
  Group /general/subject (Subject) 
  identifier: 2019_11_18_0001_oviDNSS1&SS01048_GCaMP7f.nwb
  Group /processing/behavior (ProcessingModule) contains behavioral data
  Group /processing/behavior/agarose concentration (TimeSeries) agarose concentration of current substrate
  Group /processing/behavior/body angle (TimeSeries) body angle
  Group /processing/behavior/body length (TimeSeries) body length normalized to median
  Group /processing/behavior/proboscis length (TimeSeries) proboscis length normalized to median
  Group /processing/behavior/sucrose concentration (TimeSeries) sucrose concentration of current substrate
  Group /processing/behavior/velocity (TimeSeries) speed
  Group /processing/behavior/wheel position (TimeSeries) wheel position
  Group /processing/ophys (ProcessingModule) ccontains 2-photon calcium imaging data
  Group /processing/ophys/background ROI df over f (TimeSeries) background ROI
  Group /processing/ophys/background ROI mean signal in ROI (TimeSeries) background ROI
  Group /processing/ophys/right oviDNb df over f (TimeSeries) right oviDNb
  Group /processing/ophys/right oviDNb mean signal in ROI (TimeSeries) right oviDNb
  session_description: fly on egg-laying wheel
  session_start_time: 2021-01-01T01:01:01.000000-05:00
  timestamps_reference_time: 2021-01-01T01:01:01.000000-05:00


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2022-06-09T15:40:32.945000-04:00']
  experiment_description: GCaMP7 imaging of oviDNs on an egg-laying wheel (see sucrose concentration and agarose concentration in behavior_mod to extract composition of wheel and stimulation_mod, if applicable, for any optogenetics)
  experimenter: ['Vikram Vijayan']
  institution: The Rockefeller University / HHMI
  session_id: 2019_11_22_0004_oviDNSS1&SS01048_GCaMP7f.nwb
  Group /general/subject (Subject) 
  identifier: 2019_11_22_0004_oviDNSS1&SS01048_GCaMP7f.nwb
  Group /processing/behavior (ProcessingModule) contains behavioral data
  Group /processing/behavior/agarose concentration (TimeSeries) agarose concentration of current substrate
  Group /processing/behavior/body angle (TimeSeries) body angle
  Group /processing/behavior/body length (TimeSeries) body length normalized to median
  Group /processing/behavior/proboscis length (TimeSeries) proboscis length normalized to median
  Group /processing/behavior/sucrose concentration (TimeSeries) sucrose concentration of current substrate
  Group /processing/behavior/velocity (TimeSeries) speed
  Group /processing/behavior/wheel position (TimeSeries) wheel position
  Group /processing/ophys (ProcessingModule) ccontains 2-photon calcium imaging data
  Group /processing/ophys/background ROI df over f (TimeSeries) background ROI
  Group /processing/ophys/background ROI mean signal in ROI (TimeSeries) background ROI
  Group /processing/ophys/left oviDNa df over f (TimeSeries) left oviDNa
  Group /processing/ophys/left oviDNa mean signal in ROI (TimeSeries) left oviDNa
  Group /processing/ophys/left oviDNb df over f (TimeSeries) left oviDNb
  Group /processing/ophys/left oviDNb mean signal in ROI (TimeSeries) left oviDNb
  Group /processing/ophys/right oviDNa df over f (TimeSeries) right oviDNa
  Group /processing/ophys/right oviDNa mean signal in ROI (TimeSeries) right oviDNa
  Group /processing/ophys/right oviDNb df over f (TimeSeries) right oviDNb
  Group /processing/ophys/right oviDNb mean signal in ROI (TimeSeries) right oviDNb
  session_description: fly on egg-laying wheel
  session_start_time: 2021-01-01T01:01:01.000000-05:00
  timestamps_reference_time: 2021-01-01T01:01:01.000000-05:00


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2022-06-09T15:41:19.882000-04:00']
  experiment_description: GCaMP7 imaging of oviDNs on an egg-laying wheel (see sucrose concentration and agarose concentration in behavior_mod to extract composition of wheel and stimulation_mod, if applicable, for any optogenetics)
  experimenter: ['Vikram Vijayan']
  institution: The Rockefeller University / HHMI
  session_id: 2019_11_25_0000_oviDNSS1&SS01048_GCaMP7f.nwb
  Group /general/subject (Subject) 
  identifier: 2019_11_25_0000_oviDNSS1&SS01048_GCaMP7f.nwb
  Group /processing/behavior (ProcessingModule) contains behavioral data
  Group /processing/behavior/agarose concentration (TimeSeries) agarose concentration of current substrate
  Group /processing/behavior/body angle (TimeSeries) body angle
  Group /processing/behavior/body length (TimeSeries) body length normalized to median
  Group /processing/behavior/proboscis length (TimeSeries) proboscis length normalized to median
  Group /processing/behavior/sucrose concentration (TimeSeries) sucrose concentration of current substrate
  Group /processing/behavior/velocity (TimeSeries) speed
  Group /processing/behavior/wheel position (TimeSeries) wheel position
  Group /processing/ophys (ProcessingModule) ccontains 2-photon calcium imaging data
  Group /processing/ophys/background ROI df over f (TimeSeries) background ROI
  Group /processing/ophys/background ROI mean signal in ROI (TimeSeries) background ROI
  Group /processing/ophys/left oviDNb df over f (TimeSeries) left oviDNb
  Group /processing/ophys/left oviDNb mean signal in ROI (TimeSeries) left oviDNb
  Group /processing/ophys/right oviDNb df over f (TimeSeries) right oviDNb
  Group /processing/ophys/right oviDNb mean signal in ROI (TimeSeries) right oviDNb
  session_description: fly on egg-laying wheel
  session_start_time: 2021-01-01T01:01:01.000000-05:00
  timestamps_reference_time: 2021-01-01T01:01:01.000000-05:00


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2022-06-09T15:42:21.734000-04:00']
  experiment_description: GCaMP7 imaging of oviDNs on an egg-laying wheel (see sucrose concentration and agarose concentration in behavior_mod to extract composition of wheel and stimulation_mod, if applicable, for any optogenetics)
  experimenter: ['Vikram Vijayan']
  institution: The Rockefeller University / HHMI
  session_id: 2019_11_25_0003_oviDNSS1&SS01048_GCaMP7f.nwb
  Group /general/subject (Subject) 
  identifier: 2019_11_25_0003_oviDNSS1&SS01048_GCaMP7f.nwb
  Group /processing/behavior (ProcessingModule) contains behavioral data
  Group /processing/behavior/agarose concentration (TimeSeries) agarose concentration of current substrate
  Group /processing/behavior/body angle (TimeSeries) body angle
  Group /processing/behavior/body length (TimeSeries) body length normalized to median
  Group /processing/behavior/proboscis length (TimeSeries) proboscis length normalized to median
  Group /processing/behavior/sucrose concentration (TimeSeries) sucrose concentration of current substrate
  Group /processing/behavior/velocity (TimeSeries) speed
  Group /processing/behavior/wheel position (TimeSeries) wheel position
  Group /processing/ophys (ProcessingModule) ccontains 2-photon calcium imaging data
  Group /processing/ophys/background ROI df over f (TimeSeries) background ROI
  Group /processing/ophys/background ROI mean signal in ROI (TimeSeries) background ROI
  Group /processing/ophys/left oviDNa df over f (TimeSeries) left oviDNa
  Group /processing/ophys/left oviDNa mean signal in ROI (TimeSeries) left oviDNa
  Group /processing/ophys/left oviDNb df over f (TimeSeries) left oviDNb
  Group /processing/ophys/left oviDNb mean signal in ROI (TimeSeries) left oviDNb
  Group /processing/ophys/right oviDNb df over f (TimeSeries) right oviDNb
  Group /processing/ophys/right oviDNb mean signal in ROI (TimeSeries) right oviDNb
  session_description: fly on egg-laying wheel
  session_start_time: 2021-01-01T01:01:01.000000-05:00
  timestamps_reference_time: 2021-01-01T01:01:01.000000-05:00
