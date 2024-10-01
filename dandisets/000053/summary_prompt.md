
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000053/0.210819.0345
name: Recordings from medial entorhinal cortex during linear track and open exploration
contributor: [{'name': 'Mallory, Caitlin S.', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0003-2865-0235', 'affiliation': [{'name': 'Stanford University', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/00f54p054'}], 'includeInCitation': True}, {'name': 'Hardcastle, Kiah', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-2337-9290', 'affiliation': [{'name': 'Stanford University', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/00f54p054'}], 'includeInCitation': True}, {'name': 'Campbell, Malcolm G.', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-1971-8923', 'affiliation': [{'name': 'Stanford University', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/00f54p054'}], 'includeInCitation': True}, {'name': 'Attinger, Alexander', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-6129-3199', 'affiliation': [{'name': 'Stanford University', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/00f54p054'}], 'includeInCitation': True}, {'name': 'Low, Isabel I. C.', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0001-6465-8459', 'affiliation': [{'name': 'Stanford University', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/00f54p054'}], 'includeInCitation': True}, {'name': 'Raymond, Jennifer L.', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-8145-747X', 'affiliation': [{'name': 'Stanford University', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/00f54p054'}], 'includeInCitation': True}, {'name': 'Giocomo, Lisa M.', 'roleName': ['dcite:Author', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0003-0416-2528', 'affiliation': [{'name': 'Stanford University', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/00f54p054'}], 'includeInCitation': True}]
description: This dataset contains two task types. The first is tetrode recordings from medial entorhinal cortex during open field navigation with simultaneous inertial measurements of the head, and the second is Neuropixel recordings from medial entorhinal cortex during navigation down a virtual linear track with simultaneous eye measurements.
assetsSummary: {'species': [{'name': 'House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'behavioral approach', 'schemaKey': 'ApproachType'}, {'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 1393128766605, 'numberOfFiles': 359, 'numberOfSubjects': 34, 'variableMeasured': ['LFP', 'Position', 'Units', 'ElectrodeGroup', 'EyeTracking', 'SpatialSeries', 'ProcessingModule'], 'measurementTechnique': [{'name': 'signal filtering technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000053 has 100 NWB files.
100 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2020-12-22T15:28:09.604560-05:00']
  experiment_description: arena size (cm): [75.]
  institution: Stanford University
  lab: Giocomo
  Group /general/subject (Subject) 
  identifier: rectangle_012902
  Group /processing/behavior (ProcessingModule) contains processed behavioral data
  Group /processing/behavior/Position (Position) 
  Group /processing/behavior/Position/position (SpatialSeries) no description
  Group /processing/behavior/azimuthal_head_velocity (TimeSeries) no description
  Group /processing/behavior/body_speed (TimeSeries) no description
  Group /processing/behavior/head_direction (TimeSeries) azimuth
  session_description: free exploration.
  session_start_time: 2019-01-29T00:00:00-08:00
  timestamps_reference_time: 2019-01-29T00:00:00-08:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/cell_id (VectorData) string-based cell id | shape = (8,) | dtype = object
  Dataset /units/id (ElementIdentifiers)  | shape = (8,) | dtype = int64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (13958,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (8,) | dtype = uint16
