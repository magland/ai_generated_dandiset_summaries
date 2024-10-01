
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000547/0.230822.1616
name: Perivascular Pumping of Cerebrospinal Fluid in the Brain with a Valve Mechanism
contributor: [{'name': 'Zhao, Yue', 'email': 'yuezhao@rochester.edu', 'roleName': ['dcite:ContactPerson', 'dcite:DataManager', 'dcite:Maintainer'], 'schemaKey': 'Person', 'affiliation': [{'name': 'University of Rochester', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/022kthw22'}], 'includeInCitation': True}, {'name': 'Gan, Yiming', 'email': 'ygan12@ur.rochester.edu', 'roleName': ['dcite:Author', 'dcite:ContactPerson', 'dcite:ProjectManager', 'dcite:Researcher'], 'schemaKey': 'Person', 'identifier': '0000-0002-2463-6316', 'affiliation': [{'name': 'University of Rochester', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/022kthw22'}], 'includeInCitation': True}, {'name': 'Kelley, Douglas', 'email': 'd.h.kelley@rochester.edu', 'roleName': ['dcite:Author', 'dcite:ProjectLeader', 'dcite:Researcher'], 'schemaKey': 'Person', 'identifier': '0000-0001-9658-2954', 'affiliation': [{'name': 'University of Rochester', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/022kthw22'}], 'includeInCitation': True}, {'name': 'Holstein-Rønsbo, Stephanie', 'email': 'stephanie.rathlou@sund.ku.dk', 'roleName': ['dcite:Author', 'dcite:DataCollector', 'dcite:Researcher'], 'schemaKey': 'Person', 'affiliation': [{'name': 'University of Copenhagen', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/035b05819'}], 'includeInCitation': True}, {'name': 'Boster, Kimberly', 'email': 'kboster@ur.rochester.edu', 'roleName': ['dcite:Author', 'dcite:Researcher'], 'schemaKey': 'Person', 'identifier': '0000-0001-5178-128X', 'affiliation': [{'name': 'University of Rochester', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/022kthw22'}], 'includeInCitation': True}, {'name': 'Thomas, John', 'email': 'thomas@me.rochester.edu', 'roleName': ['dcite:Author', 'dcite:Researcher'], 'schemaKey': 'Person', 'affiliation': [{'name': 'University of Rochester', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/022kthw22'}], 'includeInCitation': True}, {'name': 'Nedergaard, Maiken', 'email': 'nedergaard@sund.ku.dk', 'roleName': ['dcite:Author', 'dcite:Researcher'], 'schemaKey': 'Person', 'affiliation': [{'name': 'University of Rochester', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/022kthw22'}], 'includeInCitation': True}, {'name': 'United States Army', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/00afsp483', 'awardNumber': 'MURI W911NF1910280', 'contactPoint': [], 'includeInCitation': False}, {'name': 'National Center for Complementary and Integrative Health', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/00190t495', 'awardNumber': 'R01AT012312', 'contactPoint': [], 'includeInCitation': False}, {'name': 'National Institute of Health', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/05h1kgg64', 'awardNumber': 'U19NS128613', 'contactPoint': [], 'includeInCitation': False}]
description: This dataset contains the 2-photon recordings of the penetrating arteries of mice, included in the project "Perivascular Pumping of Cerebrospinal Fluid in the Brain with a Valve Mechanism".
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 17585558608, 'numberOfFiles': 70, 'numberOfSubjects': 9, 'variableMeasured': ['OpticalChannel', 'ImagingPlane', 'ProcessingModule', 'TwoPhotonSeries'], 'measurementTechnique': [{'name': 'two-photon microscopy technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000547 has 70 NWB files.
27 of these NWB files are of type 1.
43 of these NWB files are of type 2.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/TwoPhotonSeriesChanA (TwoPhotonSeries) Two-photon series for ChanA
  Group /acquisition/TwoPhotonSeriesChanA/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeriesChanA/imaging_plane/device (Device) Bergamo II
  Group /acquisition/TwoPhotonSeriesChanA/imaging_plane/optical_channel (OpticalChannel) 
  file_create_date: ['2023-07-11T12:23:48.112071-04:00' '2023-07-11T12:23:52.236495-04:00']
  Group /general/devices/Device (Device) Bergamo II
  experiment_description: We imaged penetrating arteries from the MCA at two different z-depths: 0 and 100 µm while stimulating whiskers with air puffs to induce functional hyperemia. 
  experimenter: ['Holstein-Rønsbo, Stephanie']
  institution: University of Copenhagen
  keywords: ['Neurovascular coupling, functional hyperemia, penetrating arteries, MCA.']
  Group /general/optophysiology/imaging_plane1 (ImagingPlane) 
  Group /general/optophysiology/imaging_plane1/device (Device) Bergamo II
  Group /general/optophysiology/imaging_plane1/optical_channel (OpticalChannel) 
  session_id: 1strec_0
  Group /general/subject (Subject) 
  identifier: 2021-09-01 11:01:46
  Group /processing/ophys (ProcessingModule) contains optical physiology data
  Group /processing/ophys/ImageSegmentation (ImageSegmentation) 
  session_description: 90 sec rec at 0 µm with whisker stimulation from 30-60 s.
  session_start_time: 2021-09-01T11:01:46.000000-04:00
  timestamps_reference_time: 2021-09-01T11:01:46.000000-04:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/TwoPhotonSeriesChanA (TwoPhotonSeries) Two-photon series for ChanA
  Group /acquisition/TwoPhotonSeriesChanA/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeriesChanA/imaging_plane/device (Device) Bergamo II
  Group /acquisition/TwoPhotonSeriesChanA/imaging_plane/optical_channel (OpticalChannel) 
  file_create_date: ['2023-07-26T16:08:10.140726-04:00']
  Group /general/devices/Device (Device) Bergamo II
  experiment_description: We imaged penetrating arteries from the MCA at two different z-depths: 0 and 100 µm while stimulating whiskers with air puffs to induce functional hyperemia. 
  experimenter: ['Holstein-Rønsbo, Stephanie']
  institution: University of Copenhagen
  keywords: ['Neurovascular coupling, functional hyperemia, penetrating arteries, MCA.']
  Group /general/optophysiology/imaging_plane1 (ImagingPlane) 
  Group /general/optophysiology/imaging_plane1/device (Device) Bergamo II
  Group /general/optophysiology/imaging_plane1/optical_channel (OpticalChannel) 
  session_id: 311_10threc_100
  Group /general/subject (Subject) 
  identifier: 2021-09-10 10:33:01
  session_description: 90 sec rec at 0 µm with whisker stimulation from 30-60 s.
  session_start_time: 2021-09-10T10:33:01.000000-04:00
  timestamps_reference_time: 2021-09-10T10:33:01.000000-04:00
