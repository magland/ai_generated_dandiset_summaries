
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001210/0.241111.1757
name: Intrinsic optical imaging (IOI) and GCaMP mouse brain data, with and without rigidified carotid artery
contributor: [{'name': 'Bakker, Marleen', 'email': 'marleenbakkermarleen@gmail.com', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}]
description: Dataset corresponding to the article "Neurovascular Coupling over Cortical Brain Areas and Resting State  Network Connectivity With and Without Rigidified Carotid Artery". 
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}, {'name': 'behavioral approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 56677001352, 'numberOfFiles': 6, 'numberOfSubjects': 2, 'variableMeasured': ['OpticalChannel', 'ImagingPlane', 'SpatialSeries', 'Position', 'ProcessingModule'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 001210 has 6 NWB files.
2 of these NWB files are of type 1.
4 of these NWB files are of type 2.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/1pInternal (OnePhotonSeries) fluo_567
  Group /acquisition/1pInternal/imaging_plane (ImagingPlane) 
  Group /acquisition/1pInternal/imaging_plane/device (Device) Camera Model: CS2100M on LightTrackOiS200 system
  Group /acquisition/1pInternal/imaging_plane/optical_channel (OpticalChannel) 
  file_create_date: ['2024-11-11T11:33:24.398831-05:00']
  Group /general/devices/Device (Device) Camera Model: CS2100M on LightTrackOiS200 system
  experimenter: ['Bakker, Marleen']
  institution: Institut Cardiologie Montreal
  Group /general/optophysiology/imaging_plane (ImagingPlane) 
  Group /general/optophysiology/imaging_plane/device (Device) Camera Model: CS2100M on LightTrackOiS200 system
  Group /general/optophysiology/imaging_plane/optical_channel (OpticalChannel) 
  Group /general/subject (Subject) 
  identifier: M32-A1-R2-GCaMP
  Group /processing/behavior (ProcessingModule) Additional Acquisition information and movement measured by treadmill, already in binary (0 is movement, 1 is no movement)
  Group /processing/behavior/Position (Position) 
  Group /processing/behavior/Position/SpatialSeries (SpatialSeries) no description
  session_description: combined GCaMP IOI data
  session_start_time: ['2023-03-16T15:26:15.000000-04:00']
  timestamps_reference_time: ['2023-03-16T15:26:15.000000-04:00']


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/1pInternal (OnePhotonSeries) red
  Group /acquisition/1pInternal/imaging_plane (ImagingPlane) 
  Group /acquisition/1pInternal/imaging_plane/device (Device) Camera Model: CS2100M on LightTrackOiS200 system
  Group /acquisition/1pInternal/imaging_plane/optical_channel (OpticalChannel) 
  file_create_date: ['2024-11-11T11:34:45.461255-05:00']
  Group /general/devices/Device (Device) Camera Model: CS2100M on LightTrackOiS200 system
  experimenter: ['Bakker, Marleen']
  institution: Institut Cardiologie Montreal
  Group /general/optophysiology/imaging_plane (ImagingPlane) 
  Group /general/optophysiology/imaging_plane/device (Device) Camera Model: CS2100M on LightTrackOiS200 system
  Group /general/optophysiology/imaging_plane/optical_channel (OpticalChannel) 
  Group /general/subject (Subject) 
  identifier: M32-A1-R2-Red
  session_description: combined GCaMP IOI data
  session_start_time: ['2023-03-16T15:26:15.000000-04:00']
  timestamps_reference_time: ['2023-03-16T15:26:15.000000-04:00']
