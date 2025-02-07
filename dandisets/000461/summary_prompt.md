
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000461/draft
name: Cohen Tickertapes Exploratory Data 1
contributor: [{'name': 'Davis Ozawa, Hunter', 'email': 'hdavis@caltech.edu', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'url': 'https://nih.gov', 'name': 'National Institutes of Health', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01cwqze88', 'awardNumber': '1 R21 EY 033669-01', 'contactPoint': [], 'includeInCitation': True}]
description: Exploratory dataset for the second generation of molecular tickertapes in the Adam Cohen Lab.
assetsSummary: {'species': [{'name': 'Canis lupus familiaris - Dog', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9615'}], 'approach': [{'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 23369106, 'numberOfFiles': 14, 'numberOfSubjects': 12, 'variableMeasured': ['OpticalChannel', 'ImagingPlane', 'TwoPhotonSeries'], 'measurementTechnique': [{'name': 'two-photon microscopy technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000461 has 14 NWB files.
14 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/TwoPhotonSeries (TwoPhotonSeries) Imaging data from two-photon excitation microscopy.
  Group /acquisition/TwoPhotonSeries/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeries/imaging_plane/OpticalChannel (OpticalChannel) 
  Group /acquisition/TwoPhotonSeries/imaging_plane/device (Device) 
  file_create_date: ['2023-03-13T19:38:32.929293-04:00']
  Group /general/devices/Microscope (Device) 
  Group /general/optophysiology/ImagingPlane (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane/OpticalChannel (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane/device (Device) 
  Group /general/subject (Subject) 
  identifier: 75432f90-1d99-4e65-81e8-d4c71d3e3193
  session_description: Auto-generated by neuroconv
  session_start_time: 2023-02-22T15:00:00-05:00
  timestamps_reference_time: 2023-02-22T15:00:00-05:00
