
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000251/draft
name: A Unified Framework for Dopamine Signals across Timescales
contributor: [{'name': 'Kim, HyungGoo', 'roleName': ['dcite:ContactPerson', 'dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Malik, Athar', 'roleName': [], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Mikhael, John', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Bech, Pol', 'roleName': [], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Tsutsui-Kimura, Iku', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Sun, Fangmiao', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Zhang, Yajun', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Li, Yulong', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Watabe-Uchida, Mitsuko', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Gershman, Samuel', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Uchida, Naoshige', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}]
description: This dandiset contains the data associated with "A Unified Framework for Dopamine Signals across Timescales" (Kim et al. 2020). It is comprised of fiber photometry data, single-unit recordings, stimulus variables, and behavioral measurements across a wide variety of experimental manipulations. 
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'behavioral approach', 'schemaKey': 'ApproachType'}, {'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 2170119624, 'numberOfFiles': 513, 'numberOfSubjects': 53, 'variableMeasured': ['SpatialSeries', 'ProcessingModule', 'Units'], 'measurementTechnique': [{'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000251 has 100 NWB files.
100 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/lick_times (Events) lick times
  Group /acquisition/treadmill_velocity (TimeSeries) no description
  file_create_date: ['2023-04-20T22:00:16.187785-04:00']
  session_id: Ca_VS_VR_2
  Group /general/subject (Subject) 
  identifier: Ca_VS_VR_2
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (150,) | dtype = int64
  Dataset /intervals/trials/rew (VectorData) rew | shape = (150,) | dtype = float64
  Dataset /intervals/trials/scene_move (VectorData) scene_move | shape = (150,) | dtype = float64
  Dataset /intervals/trials/scene_pause (VectorData) scene_pause | shape = (150,) | dtype = float64
  Dataset /intervals/trials/scene_resume (VectorData) scene_resume | shape = (150,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (150,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (150,) | dtype = float64
  Dataset /intervals/trials/teleport (VectorData) teleport | shape = (150,) | dtype = float64
  Dataset /intervals/trials/trial_type (VectorData) type of trial (i.e. speed, teleport, etc.) | shape = (150,) | dtype = object
  Dataset /intervals/trials/vstim_off (VectorData) vstim_off | shape = (150,) | dtype = float64
  Dataset /intervals/trials/vstim_on (VectorData) vstim_on | shape = (150,) | dtype = float64
  Group /processing/ophys (ProcessingModule) fiber photometry (GCaMP)
  Group /processing/ophys/fluorescence (TimeSeries) VS GCaMP fluorescence (dF/F)
  session_description: Data for Kim et al. 2020.
  session_start_time: 2017-11-29T13:41:34-04:56
  Group /stimulus/presentation/TrackPosition (SpatialSeries) Virtual reality track position
  timestamps_reference_time: 2017-11-29T13:41:34-04:56
