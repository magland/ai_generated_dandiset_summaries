
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001473/draft
name: R01 NS121918 data
contributor: [{'name': 'Wu, Jiang', 'email': 'jiangwu@caltech.edu', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}]
description: raw calcium imaging data from freely moving animals
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 35261650848, 'numberOfFiles': 4, 'numberOfSubjects': 3, 'variableMeasured': ['ImagingPlane', 'OpticalChannel', 'OnePhotonSeries'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'one-photon microscopy technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 001473 has 5 NWB files.
5 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/1pInternal (OnePhotonSeries) no description
  Group /acquisition/1pInternal/imaging_plane (ImagingPlane) 
  Group /acquisition/1pInternal/imaging_plane/device (Device) My one-photon miniscope
  Group /acquisition/1pInternal/imaging_plane/optical_channel (OpticalChannel) 
  file_create_date: ['2025-06-05T23:50:55.899319-07:00']
  Group /general/devices/Device (Device) My one-photon miniscope
  Group /general/optophysiology/imaging_plane (ImagingPlane) 
  Group /general/optophysiology/imaging_plane/device (Device) My one-photon miniscope
  Group /general/optophysiology/imaging_plane/optical_channel (OpticalChannel) 
  Group /general/subject (Subject) 
  identifier: Mouse793_Day1
  session_description: mouse in maze exploration
  session_start_time: ['2025-04-12T18:38:47.000000-07:00']
  timestamps_reference_time: ['2025-04-12T18:38:47.000000-07:00']
