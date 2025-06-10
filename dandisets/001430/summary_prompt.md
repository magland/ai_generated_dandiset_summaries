
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001430/draft
name: Aging-associated decrease of PGC-1α promotes pain chronification
contributor: [{'name': 'Shen, Shiqian', 'email': 'sshen2@mgh.harvard.edu', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Ding, Weihua', 'schemaKey': 'Person'}, {'name': 'Wu, Xinbo', 'schemaKey': 'Person'}, {'name': 'National Institute of Health (NIH)', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': 'R61 NS126029'}, {'name': 'National Institute of Health (NIH)', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': 'R03 AG067947'}, {'name': 'National Institute of Health (NIH)', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': 'R01 AG082975'}, {'name': 'National Institute of Health (NIH)', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': 'R01 AG070141'}]
description: aging-associated decrease of PGC-1α promotes pain chronification, which might be harnessed to alleviate the burden of chronic pain in older individuals.
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 668573140, 'numberOfFiles': 8, 'numberOfSubjects': 1, 'variableMeasured': ['ImagingPlane', 'TwoPhotonSeries', 'OpticalChannel'], 'measurementTechnique': [{'name': 'two-photon microscopy technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 001430 has 8 NWB files.
4 of these NWB files are of type 1.
1 of these NWB files are of type 2.
1 of these NWB files are of type 3.
1 of these NWB files are of type 4.
1 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/TwoPhotonSeries (TwoPhotonSeries) Raw calcium imaging data
  Group /acquisition/TwoPhotonSeries/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeries/imaging_plane/OpticalChannel (OpticalChannel) 
  Group /acquisition/TwoPhotonSeries/imaging_plane/device (Device) Two-photon microscope
  file_create_date: ['2025-04-30T14:52:10.019701-04:00']
  Group /general/devices/Microscope (Device) Two-photon microscope
  experimenter: ['Weihua Ding']
  institution: MGH
  lab: Shen-lab
  Group /general/optophysiology/ImagingPlane (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane/OpticalChannel (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane/device (Device) Two-photon microscope
  source_script: Created using NeuroConv v0.6.0
  Group /general/subject (Subject) 
  identifier: 8b894638-18cc-41c0-b26d-b3a47a4b7d5b
  session_description: Calcium imaging of hippocampal neurons
  session_start_time: 2020-07-13T00:00:00-04:00
  timestamps_reference_time: 2020-07-13T00:00:00-04:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/condition_CCI-PGC1a_plus_- (TimeSeries) CCI-PGC1a +/-: Mechanical allodynia over time (0=no pain, 2=max)
  Group /acquisition/condition_CCI-PGC1a_plus_-.1 (TimeSeries) CCI-PGC1a +/-.1: Mechanical allodynia over time (0=no pain, 2=max)
  Group /acquisition/condition_CCI-PGC1a_plus_-.2 (TimeSeries) CCI-PGC1a +/-.2: Mechanical allodynia over time (0=no pain, 2=max)
  Group /acquisition/condition_CCI-PGC1a_plus_-.3 (TimeSeries) CCI-PGC1a +/-.3: Mechanical allodynia over time (0=no pain, 2=max)
  Group /acquisition/condition_CCI-PGC1a_plus_-.4 (TimeSeries) CCI-PGC1a +/-.4: Mechanical allodynia over time (0=no pain, 2=max)
  Group /acquisition/condition_CCI-PGC1a_plus_-.5 (TimeSeries) CCI-PGC1a +/-.5: Mechanical allodynia over time (0=no pain, 2=max)
  Group /acquisition/condition_CCI-PGC1a_plus_-.6 (TimeSeries) CCI-PGC1a +/-.6: Mechanical allodynia over time (0=no pain, 2=max)
  Group /acquisition/condition_CCI-PGC1a_plus_-.7 (TimeSeries) CCI-PGC1a +/-.7: Mechanical allodynia over time (0=no pain, 2=max)
  Group /acquisition/condition_CCI-PGC1a_plus_plus (TimeSeries) CCI-PGC1a +/+: Mechanical allodynia over time (0=no pain, 2=max)
  Group /acquisition/condition_CCI-PGC1a_plus_plus.1 (TimeSeries) CCI-PGC1a +/+.1: Mechanical allodynia over time (0=no pain, 2=max)
  Group /acquisition/condition_CCI-PGC1a_plus_plus.2 (TimeSeries) CCI-PGC1a +/+.2: Mechanical allodynia over time (0=no pain, 2=max)
  Group /acquisition/condition_CCI-PGC1a_plus_plus.3 (TimeSeries) CCI-PGC1a +/+.3: Mechanical allodynia over time (0=no pain, 2=max)
  Group /acquisition/condition_CCI-PGC1a_plus_plus.4 (TimeSeries) CCI-PGC1a +/+.4: Mechanical allodynia over time (0=no pain, 2=max)
  Group /acquisition/condition_CCI-PGC1a_plus_plus.5 (TimeSeries) CCI-PGC1a +/+.5: Mechanical allodynia over time (0=no pain, 2=max)
  Group /acquisition/condition_CCI-PGC1a_plus_plus.6 (TimeSeries) CCI-PGC1a +/+.6: Mechanical allodynia over time (0=no pain, 2=max)
  Group /acquisition/condition_CCI-PGC1a_plus_plus.7 (TimeSeries) CCI-PGC1a +/+.7: Mechanical allodynia over time (0=no pain, 2=max)
  Group /acquisition/condition_Sham-PGC1a_plus_- (TimeSeries) Sham-PGC1a +/-: Mechanical allodynia over time (0=no pain, 2=max)
  Group /acquisition/condition_Sham-PGC1a_plus_-.1 (TimeSeries) Sham-PGC1a +/-.1: Mechanical allodynia over time (0=no pain, 2=max)
  Group /acquisition/condition_Sham-PGC1a_plus_-.2 (TimeSeries) Sham-PGC1a +/-.2: Mechanical allodynia over time (0=no pain, 2=max)
  Group /acquisition/condition_Sham-PGC1a_plus_-.3 (TimeSeries) Sham-PGC1a +/-.3: Mechanical allodynia over time (0=no pain, 2=max)
  Group /acquisition/condition_Sham-PGC1a_plus_-.4 (TimeSeries) Sham-PGC1a +/-.4: Mechanical allodynia over time (0=no pain, 2=max)
  Group /acquisition/condition_Sham-PGC1a_plus_-.5 (TimeSeries) Sham-PGC1a +/-.5: Mechanical allodynia over time (0=no pain, 2=max)
  Group /acquisition/condition_Sham-PGC1a_plus_-.6 (TimeSeries) Sham-PGC1a +/-.6: Mechanical allodynia over time (0=no pain, 2=max)
  Group /acquisition/condition_Sham-PGC1a_plus_-.7 (TimeSeries) Sham-PGC1a +/-.7: Mechanical allodynia over time (0=no pain, 2=max)
  Group /acquisition/condition_Sham-PGC1a_plus_plus (TimeSeries) Sham-PGC1a +/+: Mechanical allodynia over time (0=no pain, 2=max)
  Group /acquisition/condition_Sham-PGC1a_plus_plus.1 (TimeSeries) Sham-PGC1a +/+.1: Mechanical allodynia over time (0=no pain, 2=max)
  Group /acquisition/condition_Sham-PGC1a_plus_plus.2 (TimeSeries) Sham-PGC1a +/+.2: Mechanical allodynia over time (0=no pain, 2=max)
  Group /acquisition/condition_Sham-PGC1a_plus_plus.3 (TimeSeries) Sham-PGC1a +/+.3: Mechanical allodynia over time (0=no pain, 2=max)
  Group /acquisition/condition_Sham-PGC1a_plus_plus.4 (TimeSeries) Sham-PGC1a +/+.4: Mechanical allodynia over time (0=no pain, 2=max)
  Group /acquisition/condition_Sham-PGC1a_plus_plus.5 (TimeSeries) Sham-PGC1a +/+.5: Mechanical allodynia over time (0=no pain, 2=max)
  Group /acquisition/condition_Sham-PGC1a_plus_plus.6 (TimeSeries) Sham-PGC1a +/+.6: Mechanical allodynia over time (0=no pain, 2=max)
  Group /acquisition/condition_Sham-PGC1a_plus_plus.7 (TimeSeries) Sham-PGC1a +/+.7: Mechanical allodynia over time (0=no pain, 2=max)
  Group /acquisition/condition_Unnamed__1 (TimeSeries) Unnamed: 1: Mechanical allodynia over time (0=no pain, 2=max)
  file_create_date: ['2025-05-01T12:51:59.400055-04:00']
  experimenter: ['Shiqian Shen']
  institution: MGH
  keywords: ['Aging' 'Pain' 'PGC1a' 'Behavior']
  lab: Shen-lab
  Group /general/subject (Subject) 
  identifier: PGC1a_Behavior_2024
  session_description: Mechanical allodynia scores in PGC1a genotypes (Sham vs. CCI)
  session_start_time: 2025-05-01T16:51:59.400055+00:00
  timestamps_reference_time: 2025-05-01T16:51:59.400055+00:00


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/condition_CCI-female (TimeSeries) CCI-female: Mechanical allodynia over time (0=no pain, 2=max)
  Group /acquisition/condition_CCI-female.1 (TimeSeries) CCI-female.1: Mechanical allodynia over time (0=no pain, 2=max)
  Group /acquisition/condition_CCI-female.2 (TimeSeries) CCI-female.2: Mechanical allodynia over time (0=no pain, 2=max)
  Group /acquisition/condition_CCI-female.3 (TimeSeries) CCI-female.3: Mechanical allodynia over time (0=no pain, 2=max)
  Group /acquisition/condition_CCI-male (TimeSeries) CCI-male: Mechanical allodynia over time (0=no pain, 2=max)
  Group /acquisition/condition_CCI-male.1 (TimeSeries) CCI-male.1: Mechanical allodynia over time (0=no pain, 2=max)
  Group /acquisition/condition_CCI-male.2 (TimeSeries) CCI-male.2: Mechanical allodynia over time (0=no pain, 2=max)
  Group /acquisition/condition_CCI-male.3 (TimeSeries) CCI-male.3: Mechanical allodynia over time (0=no pain, 2=max)
  Group /acquisition/condition_Sham-male (TimeSeries) Sham-male: Mechanical allodynia over time (0=no pain, 2=max)
  Group /acquisition/condition_Sham-male.1 (TimeSeries) Sham-male.1: Mechanical allodynia over time (0=no pain, 2=max)
  Group /acquisition/condition_Sham-male.2 (TimeSeries) Sham-male.2: Mechanical allodynia over time (0=no pain, 2=max)
  Group /acquisition/condition_Sham-male.3 (TimeSeries) Sham-male.3: Mechanical allodynia over time (0=no pain, 2=max)
  Group /acquisition/condition_sham-female (TimeSeries) sham-female: Mechanical allodynia over time (0=no pain, 2=max)
  Group /acquisition/condition_sham-female.1 (TimeSeries) sham-female.1: Mechanical allodynia over time (0=no pain, 2=max)
  Group /acquisition/condition_sham-female.2 (TimeSeries) sham-female.2: Mechanical allodynia over time (0=no pain, 2=max)
  Group /acquisition/condition_sham-female.3 (TimeSeries) sham-female.3: Mechanical allodynia over time (0=no pain, 2=max)
  file_create_date: ['2025-05-01T12:53:08.849662-04:00']
  experimenter: ['Shiqian Shen']
  institution: MGH
  keywords: ['Aging' 'Pain' 'PGC1a' 'Behavior']
  lab: Shen-lab
  Group /general/subject (Subject) 
  identifier: PGC1a_Behavior_2024
  session_description: Mechanical allodynia scores in PGC1a genotypes (Sham vs. CCI)
  session_start_time: 2025-05-01T16:53:08.849662+00:00
  timestamps_reference_time: 2025-05-01T16:53:08.849662+00:00


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Fluorescence2D_Blue (ImageSeries) no description
  file_create_date: ['2025-05-01T11:17:16.250897-04:00']
  experimenter: ['Shiqian Shen']
  institution: MGH
  lab: Neurobiology Lab
  related_publications: ['https://doi.org/examplepublication']
  Group /general/subject (Subject) 
  identifier: fluoro_img_blue
  session_description: Single fluorescence image (blue channel)
  session_start_time: 2025-05-01T15:17:16.250897+00:00
  timestamps_reference_time: 2025-05-01T15:17:16.250897+00:00


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Fluorescence2D_Green (ImageSeries) no description
  file_create_date: ['2025-05-01T11:43:49.891658-04:00']
  experimenter: ['Shiqian Shen']
  institution: MGH
  lab: Neurobiology Lab
  related_publications: ['https://doi.org/examplepublication']
  Group /general/subject (Subject) 
  identifier: fluoro_img_blue
  session_description: Single fluorescence image (blue channel)
  session_start_time: 2025-05-01T15:43:49.891658+00:00
  timestamps_reference_time: 2025-05-01T15:43:49.891658+00:00
