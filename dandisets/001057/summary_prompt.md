
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001057/draft
name: NeuroTask - Center-Out Target Task: A Benchmark Dataset for Multi-Task, -Session and -Subject Neural Analysis
contributor: [{'name': 'Filipe, A. Carolina', 'email': 'a.carolina.filipe@gmail.com', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Park, Il Memming', 'schemaKey': 'Person', 'includeInCitation': True}]
description: NeuroTask is a benchmark dataset designed to facilitate the development of accurate and efficient methods for analyzing multi-session, multi-task, and multi-subject neural data. NeuroTask integrates 6 datasets from motor cortical regions, covering 7 tasks across 17 subjects.

Check out the github repository for more resources and some example notebooks:https://github.com/catniplab/NeuroTask/tree/nwb

This dataset includes:
- Spike counts per unit
- Behavioral data (hand/cursor position, velocity, force)
- Events indications
assetsSummary: {'species': [{'name': 'Macaca mulatta - Rhesus monkey', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9544'}], 'approach': [], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 1724680097, 'numberOfFiles': 4, 'numberOfSubjects': 6, 'variableMeasured': ['ProcessingModule'], 'measurementTechnique': [{'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 001057 has 4 NWB files.
1 of these NWB files are of type 1.
2 of these NWB files are of type 2.
1 of these NWB files are of type 3.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2024-07-01T19:14:14.612414+01:00']
  experiment_description: Monkeys controlled a cursor on a screen using a two-link, planar manipulandum. They performed a simple center-out task to one of the eight possible targets after a variable delayed period.
  experimenter: ["Gallego-Carracedo, Cecilia'"]
  institution: Imperial College London
  keywords: ['benchmark' 'monkey' 'center out' 'reaching']
  notes: Chewie (Animal 1) had recordings from the M1 area, while Han and Lando (Animals 2 and 3) were recorded from Area 2. Mihili (Animal 4) had recordings from M1 (odd numbers) in alternating sessions with recordings from PMd (even numbers).
  related_publications: ['https://doi.org/10.7554/eLife.73155']
  Group /general/subject (Subject) 
  identifier: Gallego_CO
  Group /processing/behavior (ProcessingModule) Behavior data, units: angles: radians, hand position: cm,cursor position : mm 
  Group /processing/behavior/hand_vel_x (TimeSeries) no description
  Group /processing/behavior/hand_vel_y (TimeSeries) no description
  Group /processing/behavior/target_dir (TimeSeries) no description
  Group /processing/events (ProcessingModule) Events indications
  Group /processing/events/result (TimeSeries) no description
  Group /processing/indices (ProcessingModule) Indices to filter per session, animal and trial
  Group /processing/indices/animal (TimeSeries) no description
  Group /processing/indices/datasetID (TimeSeries) no description
  Group /processing/indices/session (TimeSeries) no description
  Group /processing/indices/trial_id (TimeSeries) no description
  Group /processing/spikes (ProcessingModule) Spike counts.Recordings from these channels were thresholded online to detect spikes, which were sorted offline into putative single units. 
  Group /processing/spikes/spikes_counts (TimeSeries) no description
  session_description: Center-Out Target task
  session_start_time: 2016-08-22T02:30:03-07:00
  timestamps_reference_time: 2016-08-22T02:30:03-07:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2024-07-01T19:05:43.467413+01:00']
  experiment_description: Monkeys performed a center-out (CO) reaching task using an upright planar manipulandum. They initiated each trial by moving the hand to the center of the workspace. After a random delay, one of eight outer targets was presented.
  experimenter: ["Xuan, Ma'"]
  institution: Northwestern University
  keywords: ['benchmark' 'monkey' 'center out' 'reaching']
  notes: Recordings from M1
  related_publications: ['doi.org/10.7554/elife.84296;doi.org/10.5281/zenodo.8247498 ']
  Group /general/subject (Subject) 
  identifier: MaXuan_CO
  Group /processing/behavior (ProcessingModule) Behavior data, units: angles: radians, hand position: cm,cursor position : mm 
  Group /processing/behavior/cursor_acc_x (TimeSeries) no description
  Group /processing/behavior/cursor_acc_y (TimeSeries) no description
  Group /processing/behavior/cursor_pos_x (TimeSeries) no description
  Group /processing/behavior/cursor_pos_y (TimeSeries) no description
  Group /processing/behavior/cursor_vel_x (TimeSeries) no description
  Group /processing/behavior/cursor_vel_y (TimeSeries) no description
  Group /processing/behavior/force_x (TimeSeries) no description
  Group /processing/behavior/force_y (TimeSeries) no description
  Group /processing/behavior/target_ID (TimeSeries) no description
  Group /processing/behavior/target_dir (TimeSeries) no description
  Group /processing/events (ProcessingModule) Events indications
  Group /processing/events/result (TimeSeries) no description
  Group /processing/indices (ProcessingModule) Indices to filter per session, animal and trial
  Group /processing/indices/animal (TimeSeries) no description
  Group /processing/indices/datasetID (TimeSeries) no description
  Group /processing/indices/session (TimeSeries) no description
  Group /processing/indices/trial_id (TimeSeries) no description
  Group /processing/spikes (ProcessingModule) Spike counts.Recordings from these channels were thresholded online to detect spikes, which were sorted offline into putative single units. 
  Group /processing/spikes/spikes_counts (TimeSeries) no description
  session_description: Center-Out Target task
  session_start_time: 2016-08-22T02:30:03-07:00
  timestamps_reference_time: 2016-08-22T02:30:03-07:00


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2024-07-01T18:53:08.469303+01:00']
  experiment_description: The subjects performed a delayed center-out movement task. Seated in a primate chair, they used a 2-D planar manipulandum to control a computer cursor. Each trial began by moving to a center target (2 × 2 × 2 cm) and holding for 500 – 1500 ms. A 2 cm target then appeared randomly in one of eight outer positions at an 8 cm radial distance. For Animal 2, a variable delay period of 500 – 1500 ms followed before an auditory 'Go' cue. For Animal 1, the 'Go' cue was given immediately. Subjects had 1000 – 1300 ms to reach the target and had to hold it for 500 ms to receive a success tone and a liquid reward.
  experimenter: ["Dyer,Eva'"]
  institution: Northwestern University
  keywords: ['benchmark' 'monkey' 'center out' 'reaching']
  notes: Recordings from M1
  related_publications: ['doi: 10.1038/s41551-017-0169-7']
  Group /general/subject (Subject) 
  identifier: Dyer_CO
  Group /processing/behavior (ProcessingModule) Behavior data, units: angles: radians, hand position: cm,cursor position : mm 
  Group /processing/behavior/force_x (TimeSeries) no description
  Group /processing/behavior/force_y (TimeSeries) no description
  Group /processing/behavior/hand_acc_x (TimeSeries) no description
  Group /processing/behavior/hand_acc_y (TimeSeries) no description
  Group /processing/behavior/hand_pos_x (TimeSeries) no description
  Group /processing/behavior/hand_pos_y (TimeSeries) no description
  Group /processing/behavior/hand_vel_x (TimeSeries) no description
  Group /processing/behavior/hand_vel_y (TimeSeries) no description
  Group /processing/behavior/target_ID (TimeSeries) no description
  Group /processing/behavior/target_dir (TimeSeries) no description
  Group /processing/events (ProcessingModule) Events indications
  Group /processing/events/result (TimeSeries) no description
  Group /processing/indices (ProcessingModule) Indices to filter per session, animal and trial
  Group /processing/indices/animal (TimeSeries) no description
  Group /processing/indices/datasetID (TimeSeries) no description
  Group /processing/indices/session (TimeSeries) no description
  Group /processing/indices/trial_id (TimeSeries) no description
  Group /processing/spikes (ProcessingModule) Spike counts.Recordings from these channels were thresholded online to detect spikes, which were sorted offline into putative single units. 
  Group /processing/spikes/spikes_counts (TimeSeries) no description
  session_description: Center-Out Target task
  session_start_time: 2016-08-22T02:30:03-07:00
  timestamps_reference_time: 2016-08-22T02:30:03-07:00
