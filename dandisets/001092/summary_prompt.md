
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001092/draft
name: HaloTag Time-Stamping of cFos Transcription in Mouse Brain
contributor: [{'name': 'NIH', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01cwqze88', 'awardNumber': '1 R21 EY 033669-02', 'includeInCitation': False}, {'name': 'Cohen, Adam E.', 'email': 'cohen@chemistry.harvard.edu', 'roleName': ['dcite:ContactPerson', 'dcite:FundingAcquisition', 'dcite:Supervision'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Moult, Eric', 'email': 'eric_moult@harvard.edu', 'roleName': ['dcite:Author', 'dcite:Conceptualization', 'dcite:DataCollector', 'dcite:DataCurator', 'dcite:DataManager', 'dcite:Investigation', 'dcite:Researcher'], 'schemaKey': 'Person', 'includeInCitation': True}]
description: These images are from a cross-sectional slice through a tet-tag mouse brain expressing a TRE::HaloTag-NLS construct. The mouse was intravenously injected with HaloTag-ligand-JF669 on day 1 and HaloTag-ligand-JF552 on day 2. 
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 12627889, 'numberOfFiles': 3, 'numberOfSubjects': 2, 'variableMeasured': ['TwoPhotonSeries', 'ImagingPlane', 'OpticalChannel'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'two-photon microscopy technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 001092 has 3 NWB files.
3 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/TwoPhotonSeries (TwoPhotonSeries) Imaging data from two-photon excitation microscopy.
  Group /acquisition/TwoPhotonSeries/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeries/imaging_plane/OpticalChannel (OpticalChannel) 
  Group /acquisition/TwoPhotonSeries/imaging_plane/device (Device) 
  file_create_date: ['2024-07-19T22:22:58.047591-04:00']
  Group /general/devices/Microscope (Device) 
  Group /general/optophysiology/ImagingPlane (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane/OpticalChannel (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane/device (Device) 
  source_script: Created using NeuroConv v0.5.0
  Group /general/subject (Subject) 
  identifier: c444c191-440b-4183-b88c-b2831f5823e3
  session_description: 
  session_start_time: 2024-07-19T19:20:00-04:00
  timestamps_reference_time: 2024-07-19T19:20:00-04:00
