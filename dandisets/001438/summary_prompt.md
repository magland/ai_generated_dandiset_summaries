
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001438/draft
name: Old rats persistently switch between allocentric and procedural strategies across learning of the Morris watermaze
contributor: [{'name': 'Sponseller, Mia', 'email': 'miasponseller@arizona.edu', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}]
description: Data sheets required used for analysis
assetsSummary: {'schemaKey': 'AssetsSummary', 'numberOfBytes': 0, 'numberOfFiles': 0}

Dandiset 001438 has 1 NWB files.
1 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2025-05-20T16:40:24.632944-07:00']
  source_script: Created using NeuroConv v0.7.3
  Group /general/subject (Subject) 
  identifier: d707a870-67fd-4d49-98ca-9b9216b36781
  Group /intervals/trials (TimeIntervals) experimental trials generated from /Users/miasponseller/Desktop/MWM_results_04-06-2025_for_dandi.xlsx
  Dataset /intervals/trials/Age (VectorData) Age | shape = (2472,) | dtype = object
  Dataset /intervals/trials/Cohort (VectorData) Cohort | shape = (2472,) | dtype = int64
  Dataset /intervals/trials/Track_ID (VectorData) Track_ID | shape = (2472,) | dtype = object
  Dataset /intervals/trials/_Arena (VectorData) _Arena | shape = (2472,) | dtype = object
  Dataset /intervals/trials/_Day (VectorData) _Day | shape = (2472,) | dtype = int64
  Dataset /intervals/trials/_TargetID (VectorData) _TargetID | shape = (2472,) | dtype = int64
  Dataset /intervals/trials/_Trial (VectorData) _Trial | shape = (2472,) | dtype = int64
  Dataset /intervals/trials/chaining (VectorData) chaining | shape = (2472,) | dtype = float64
  Dataset /intervals/trials/circling (VectorData) circling | shape = (2472,) | dtype = float64
  Dataset /intervals/trials/confidence (VectorData) confidence | shape = (2472,) | dtype = float64
  Dataset /intervals/trials/corrected_search (VectorData) corrected_search | shape = (2472,) | dtype = float64
  Dataset /intervals/trials/direct_path (VectorData) direct_path | shape = (2472,) | dtype = float64
  Dataset /intervals/trials/directed_search (VectorData) directed_search | shape = (2472,) | dtype = float64
  Dataset /intervals/trials/distance.from.goal (VectorData) distance.from.goal | shape = (2472,) | dtype = float64
  Dataset /intervals/trials/distance.from.old.goal (VectorData) distance.from.old.goal | shape = (2472,) | dtype = float64
  Dataset /intervals/trials/efficiency (VectorData) efficiency | shape = (2472,) | dtype = float64
  Dataset /intervals/trials/goal.crossings (VectorData) goal.crossings | shape = (2472,) | dtype = int64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (2472,) | dtype = int64
  Dataset /intervals/trials/initial.heading.error (VectorData) initial.heading.error | shape = (2472,) | dtype = float64
  Dataset /intervals/trials/initial.reversal.error (VectorData) initial.reversal.error | shape = (2472,) | dtype = float64
  Dataset /intervals/trials/initial.trajectory.error (VectorData) initial.trajectory.error | shape = (2472,) | dtype = float64
  Dataset /intervals/trials/latency.to.goal (VectorData) latency.to.goal | shape = (2472,) | dtype = float64
  Dataset /intervals/trials/latency.to.old.goal (VectorData) latency.to.old.goal | shape = (2472,) | dtype = float64
  Dataset /intervals/trials/name (VectorData) name | shape = (2472,) | dtype = object
  Dataset /intervals/trials/old.goal.crossings (VectorData) old.goal.crossings | shape = (2472,) | dtype = float64
  Dataset /intervals/trials/path.length (VectorData) path.length | shape = (2472,) | dtype = float64
  Dataset /intervals/trials/pd (VectorData) pd | shape = (2472,) | dtype = float64
  Dataset /intervals/trials/perseverance (VectorData) perseverance | shape = (2472,) | dtype = float64
  Dataset /intervals/trials/random_path (VectorData) random_path | shape = (2472,) | dtype = float64
  Dataset /intervals/trials/roaming.entropy (VectorData) roaming.entropy | shape = (2472,) | dtype = float64
  Dataset /intervals/trials/scanning (VectorData) scanning | shape = (2472,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (2472,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (2472,) | dtype = float64
  Dataset /intervals/trials/strategy (VectorData) strategy | shape = (2472,) | dtype = int64
  Dataset /intervals/trials/thigmotaxis (VectorData) thigmotaxis | shape = (2472,) | dtype = float64
  Dataset /intervals/trials/time.in.annulus.zone (VectorData) time.in.annulus.zone | shape = (2472,) | dtype = float64
  Dataset /intervals/trials/time.in.e.quadrant (VectorData) time.in.e.quadrant | shape = (2472,) | dtype = float64
  Dataset /intervals/trials/time.in.far.wall.zone (VectorData) time.in.far.wall.zone | shape = (2472,) | dtype = float64
  Dataset /intervals/trials/time.in.goal.zone (VectorData) time.in.goal.zone | shape = (2472,) | dtype = float64
  Dataset /intervals/trials/time.in.n.quadrant (VectorData) time.in.n.quadrant | shape = (2472,) | dtype = float64
  Dataset /intervals/trials/time.in.old.goal.zone (VectorData) time.in.old.goal.zone | shape = (2472,) | dtype = float64
  Dataset /intervals/trials/time.in.s.quadrant (VectorData) time.in.s.quadrant | shape = (2472,) | dtype = float64
  Dataset /intervals/trials/time.in.w.quadrant (VectorData) time.in.w.quadrant | shape = (2472,) | dtype = float64
  Dataset /intervals/trials/time.in.wall.zone (VectorData) time.in.wall.zone | shape = (2472,) | dtype = float64
  Dataset /intervals/trials/total.time (VectorData) total.time | shape = (2472,) | dtype = float64
  Dataset /intervals/trials/velocity (VectorData) velocity | shape = (2472,) | dtype = float64
  session_description: No description.
  session_start_time: 2025-04-06T00:00:00-07:00
  timestamps_reference_time: 2025-04-06T00:00:00-07:00
