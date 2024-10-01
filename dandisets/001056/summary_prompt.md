
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001056/draft
name: NeuroTask - Center-Out with bump: A Benchmark Dataset for Multi-Task, -Session and -Subject Neural Analysis
contributor: [{'name': 'Filipe, A. Carolina', 'email': 'a.carolina.filipe@gmail.com', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Park, Il Memming', 'schemaKey': 'Person', 'includeInCitation': True}]
description: NeuroTask is a benchmark dataset designed to facilitate the development of accurate and efficient methods for analyzing multi-session, multi-task, and multi-subject neural data. NeuroTask integrates 6 datasets from motor cortical regions, covering 7 tasks across 17 subjects.

Check out the github repository for more resources and some example notebooks:https://github.com/catniplab/NeuroTask/tree/nwb

This dataset includes:
- Spike counts per unit
- Behavioral data (hand/cursor position, velocity, force)
- Events indications

assetsSummary: {'species': [{'name': 'Macaca mulatta - Rhesus monkey', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9544'}], 'approach': [], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 54454695, 'numberOfFiles': 1, 'numberOfSubjects': 2, 'variableMeasured': ['ProcessingModule'], 'measurementTechnique': [{'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 001056 has 1 NWB files.
1 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2024-07-01T18:31:59.235216+01:00']
  experiment_description:  Monkeys performed a simple center-out task, where on some random trials during the center-hold period, the manipulandum applied a perturbation to the monkey’s hand.
  experimenter: [' Raeed H, Chowdhury; Joshua I, Glaser; Lee E, Miller']
  institution: University of Pittsburgh
  keywords: ['benchmark' 'monkey' 'center out' 'bump' 'reaching']
  notes: Recordings from Area2
  related_publications: ['https://doi.org/10.5061/dryad.nk98sf7q7 ']
  Group /general/subject (Subject) 
  identifier: Chowdhury_CObump
  Group /processing/behavior (ProcessingModule) Behavior data, units: angles: radians, hand position: cm,cursor position : mm 
  Group /processing/behavior/bump_dir (TimeSeries) no description
  Group /processing/behavior/hand_pos_x (TimeSeries) no description
  Group /processing/behavior/hand_pos_y (TimeSeries) no description
  Group /processing/behavior/hand_vel_x (TimeSeries) no description
  Group /processing/behavior/hand_vel_y (TimeSeries) no description
  Group /processing/behavior/target_dir (TimeSeries) no description
  Group /processing/events (ProcessingModule) Events indications
  Group /processing/events/EventBump (TimeSeries) no description
  Group /processing/events/EventGo_cue (TimeSeries) no description
  Group /processing/events/EventTarget_Onset (TimeSeries) no description
  Group /processing/events/result (TimeSeries) no description
  Group /processing/indices (ProcessingModule) Indices to filter per session, animal and trial
  Group /processing/indices/animal (TimeSeries) no description
  Group /processing/indices/datasetID (TimeSeries) no description
  Group /processing/indices/session (TimeSeries) no description
  Group /processing/indices/trial_id (TimeSeries) no description
  Group /processing/spikes (ProcessingModule) Spike counts.Recordings from these channels were thresholded online to detect spikes, which were sorted offline into putative single units. 
  Group /processing/spikes/spikes_counts (TimeSeries) no description
  session_description:  Center-Out with bump task
  session_start_time: 2016-08-22T02:30:03-07:00
  timestamps_reference_time: 2016-08-22T02:30:03-07:00
