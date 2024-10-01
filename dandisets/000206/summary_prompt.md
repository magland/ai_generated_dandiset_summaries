
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000206/0.220103.2119
name: Visual cortical activity in mice performing naturalistic virtual foraging task
contributor: [{'name': 'Smith, Spencer', 'email': 'slabcloudcomp@gmail.com', 'roleName': ['dcite:Author', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0002-2021-7034', 'affiliation': [{'name': 'University of California Santa Barbara', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/02t274463'}], 'includeInCitation': True}, {'name': 'McGreal, Ryan', 'email': 'ryanpmcgreal@ucsb.edu', 'roleName': ['dcite:ProjectManager'], 'schemaKey': 'Person', 'identifier': '0000-0001-5849-4312', 'affiliation': [{'name': 'University of California Santa Barbara', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/02t274463'}], 'includeInCitation': True}, {'name': 'Canzano, Joseph', 'email': 'jscanzano@ucsb.edu', 'roleName': ['dcite:Author', 'dcite:DataCollector', 'dcite:DataCurator'], 'schemaKey': 'Person', 'identifier': '0000-0002-5371-4846', 'affiliation': [{'name': 'University of California Santa Barbara', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/02t274463'}], 'includeInCitation': True}]
description: Large FOV two-photon calcium imaging dataset recorded from V1 L2/3 neurons from mouse performing a naturalistic foraging task in virtual reality.
assetsSummary: {'species': [{'name': 'House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}, {'name': 'behavioral approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 118359600, 'numberOfFiles': 1, 'numberOfSubjects': 1, 'variableMeasured': ['SpatialSeries', 'ImagingPlane', 'Position', 'OpticalChannel'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000206 has 1 NWB files.
1 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2021-12-22T19:50:00.931000-08:00']
  Group /general/devices/Device (Device) 
  Group /general/optophysiology/imaging_plane (ImagingPlane) 
  Group /general/optophysiology/imaging_plane/device (Device) 
  Group /general/optophysiology/imaging_plane/optical_channel (OpticalChannel) 
  Group /general/subject (Subject) 
  identifier: TIGRE296_1
  Group /intervals/trials (TimeIntervals) trial data, parameters, and outcomes
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (171,) | dtype = int32
  Dataset /intervals/trials/outcome (VectorData) 1 for hit 0 for miss | shape = (171,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) start time of trial | shape = (171,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) end of trials | shape = (171,) | dtype = float64
  Dataset /intervals/trials/targetx (VectorData) left/right position of target | shape = (171,) | dtype = float64
  Dataset /intervals/trials/targetz (VectorData) distance to target | shape = (171,) | dtype = float64
  Group /processing/behavior (ProcessingModule) contains behavioral data
  Group /processing/behavior/Position (Position) 
  Group /processing/behavior/Position/SpatialSeries (SpatialSeries) no description
  Group /processing/ophys (ProcessingModule) contains optical physiology data
  Group /processing/ophys/TimeSeries (TimeSeries) cellular deltafovf
  session_description: mouse in virtual foraging task
  session_start_time: 2021-07-01T05:30:01.000000-07:00
  timestamps_reference_time: 2021-07-01T05:30:01.000000-07:00
