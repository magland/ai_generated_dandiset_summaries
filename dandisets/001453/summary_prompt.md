
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001453/0.250518.1950
name: Neural circuits underlying divergent visuomotor strategies of zebrafish and Danionella cerebrum
contributor: [{'name': 'Fouke, Kaitlyn', 'email': 'kaitlyn.fouke@duke.edu', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}]
description: This dataset was used in "Neural circuits underlying divergent visuomotor strategies of zebrafish and Danionella cerebrum" (Current Biology, 2025, https://doi.org/10.1016/j.cub.2025.04.027).

Many animals respond to sensory cues with species-specific coordinated movements.1,2 A universal visually guided behavior is the optomotor response (OMR),3,4,5,6 which stabilizes the body by following optic flow induced by displacements in currents.7 While the brain-wide OMR circuits in zebrafish (Danio rerio) have been characterized,8,9,10,11,12 the homologous neural functions across teleost species with different ecological niches, such as Danionella cerebrum,13,14,15 remain largely unexplored. Here, we directly compare larval zebrafish and D. cerebrum to uncover the neural mechanisms underlying the natural variation of visuomotor coordination. Closed-loop behavioral tracking during visual stimulation revealed that D. cerebrum follow optic flow by swimming continuously, punctuated with sharp directional turns, in contrast to the burst-and-glide locomotion of zebrafish.16 Although D. cerebrum swim at higher average speeds, they lack the direction-dependent velocity modulation observed in zebrafish. Two-photon calcium imaging and tail tracking showed that both species exhibit direction-selective encoding in putative homologous regions, with D. cerebrum containing more monocular neurons. D. cerebrum sustain significantly longer directed swims across all stimuli than zebrafish, with zebrafish reducing tail movement duration in response to oblique, turn-inducing stimuli. While locomotion-associated neurons in D. cerebrum display more prolonged activity than zebrafish, lateralized turn-associated neural activity in the hindbrain suggests a shared neural circuit architecture that independently controls movement vigor and direction. These findings highlight the diversity in visuomotor strategies among teleost species with shared circuit motifs, establishing a framework for unraveling the neural mechanisms driving continuous and discrete locomotion.
assetsSummary: {'species': [{'name': 'Danio rerio - Zebra fish', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_7955'}], 'approach': [{'name': 'behavioral approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 3823109128, 'numberOfFiles': 37, 'numberOfSubjects': 25, 'variableMeasured': ['ProcessingModule', 'BehavioralTimeSeries'], 'measurementTechnique': [{'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 001453 has 37 NWB files.
25 of these NWB files are of type 1.
12 of these NWB files are of type 2.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2025-05-15T17:05:10.775789-04:00']
  experiment_description: Danionella and zebrafish freely swimming behavior
  experimenter: ['Fouke, Kaitlyn']
  institution: Duke University
  keywords: ['freely swimming' 'zebrafish' 'behavior' 'tracking']
  lab: Naumann Laboratory
  related_publications: ['doi.org/10.1016/j.cub.2025.04.027']
  Group /general/subject (Subject) 
  identifier: 1b6813d0-d0a1-415d-8a0b-e3caddde9d52
  Group /processing/behavior (ProcessingModule) freely swimming tracking data
  Group /processing/behavior/BehavioralTimeSeries (BehavioralTimeSeries) 
  Group /processing/behavior/BehavioralTimeSeries/f0_theta (TimeSeries) orientation of fish
  Group /processing/behavior/BehavioralTimeSeries/f0_vtheta (TimeSeries) angular velocity
  Group /processing/behavior/BehavioralTimeSeries/f0_vx (TimeSeries) x-velocity of fish
  Group /processing/behavior/BehavioralTimeSeries/f0_vy (TimeSeries) y-velocity of fish
  Group /processing/behavior/BehavioralTimeSeries/f0_x (TimeSeries) x-position of fish
  Group /processing/behavior/BehavioralTimeSeries/f0_y (TimeSeries) y-position of fish
  Group /processing/behavior/BehavioralTimeSeries/stim_index (TimeSeries) stimulus index
  Group /processing/behavior/BehavioralTimeSeries/stimulus (TimeSeries) stimulus ID
  session_description: freely swimming behavior dataset
  session_start_time: 2023-06-20T11:08:54.738665-04:00
  timestamps_reference_time: 2023-06-20T11:08:54.738665-04:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2025-05-15T17:04:59.257539-04:00']
  experiment_description: Danionella and zebrafish freely swimming behavior
  experimenter: ['Fouke, Kaitlyn']
  institution: Duke University
  keywords: ['freely swimming' 'zebrafish' 'behavior' 'tracking']
  lab: Naumann Laboratory
  related_publications: ['doi.org/10.1016/j.cub.2025.04.027']
  Group /general/subject (Subject) 
  identifier: e960b7d5-c2be-485a-bf7a-cad56686f8fd
  Group /processing/behavior (ProcessingModule) freely swimming tracking data
  Group /processing/behavior/BehavioralTimeSeries (BehavioralTimeSeries) 
  Group /processing/behavior/BehavioralTimeSeries/dist (TimeSeries) distance since last frame
  Group /processing/behavior/BehavioralTimeSeries/f0_theta (TimeSeries) orientation of fish
  Group /processing/behavior/BehavioralTimeSeries/f0_vtheta (TimeSeries) angular velocity
  Group /processing/behavior/BehavioralTimeSeries/f0_vx (TimeSeries) x-velocity of fish
  Group /processing/behavior/BehavioralTimeSeries/f0_vy (TimeSeries) y-velocity of fish
  Group /processing/behavior/BehavioralTimeSeries/f0_x (TimeSeries) x-position of fish
  Group /processing/behavior/BehavioralTimeSeries/f0_y (TimeSeries) y-position of fish
  Group /processing/behavior/BehavioralTimeSeries/stim_index (TimeSeries) stimulus index
  Group /processing/behavior/BehavioralTimeSeries/stimulus (TimeSeries) stimulus ID
  session_description: freely swimming behavior dataset
  session_start_time: 2023-10-31T13:55:10.037209-04:00
  timestamps_reference_time: 2023-10-31T13:55:10.037209-04:00
