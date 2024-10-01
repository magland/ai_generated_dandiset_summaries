
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000302/draft
name: Habenular neurophysiology
contributor: [{'name': 'National Institutes of Health (NIH)', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': '1 U19 NS 118284-01', 'contactPoint': [], 'includeInCitation': False}, {'name': 'Jo, YoungJu', 'email': 'yjjo@stanford.edu', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0002-2364-7160', 'affiliation': [{'name': 'Stanford University', 'schemaKey': 'Affiliation'}], 'includeInCitation': True}]
description: Habenular neurophysiology data associated with Sylwestrak*, Jo*, Vesuna* et al. Cell (2022).
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'behavioral approach', 'schemaKey': 'ApproachType'}, {'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}, {'name': 'optogenetic approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 1078714284, 'numberOfFiles': 32, 'numberOfSubjects': 12, 'variableMeasured': ['BehavioralEvents', 'ProcessingModule', 'Units', 'ElectrodeGroup', 'OptogeneticSeries'], 'measurementTechnique': [{'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000302 has 32 NWB files.
11 of these NWB files are of type 1.
20 of these NWB files are of type 2.
1 of these NWB files are of type 3.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2023-05-04T03:51:03.208135-07:00']
  Group /general/devices/Probe0 (Device) Neuropixels 2.0 4-shank
  experiment_description: mouse performing a reward-seeking task; Neuropixels 2.0 recording targeted to the medial habenula; transcranial optotagging of Tac1 neurons
  experimenter: ['Jo, YoungJu']
  Group /general/extracellular_ephys/Probe0 (ElectrodeGroup) electrode group for Probe0
  Group /general/extracellular_ephys/Probe0/device (Device) Neuropixels 2.0 4-shank
  Group /general/extracellular_ephys/electrodes (DynamicTable) all probes
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) my description | shape = (383,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) my description | shape = (383,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (383,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) my description | shape = (383,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) my description | shape = (383,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) my description | shape = (383,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) my description | shape = (383,) | dtype = float64
  institution: Stanford University
  keywords: ['electrophysiology' 'habenula']
  lab: Deisseroth
  related_publications: ['doi: 10.1016/j.cell.2022.08.019']
  Group /general/subject (Subject) 
  identifier: 170_20210905
  Group /intervals/trials (TimeIntervals) trials table
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (137,) | dtype = int64
  Dataset /intervals/trials/responseTime (VectorData) time from Go cue onset to lick (2 for no lick trials) | shape = (137,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Go cue onset timestamps | shape = (137,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Go cue onset timestamps (duplicate) | shape = (137,) | dtype = float64
  Dataset /intervals/trials/trial_type (VectorData) 1 = lick-reward, 2 = lick-noreward, 3 = no lick, 0 = perturbation | shape = (137,) | dtype = float64
  Group /processing/behavior (ProcessingModule) stores behavioral events
  Group /processing/behavior/BehavioralEvents (BehavioralEvents) 
  Group /processing/behavior/BehavioralEvents/timestamp_lick (TimeSeries) lick timestamps
  Group /processing/behavior/BehavioralEvents/timestamp_reward (TimeSeries) reward timestamps
  session_description:  
  session_start_time: 2021-09-05T00:00:00.000000-07:00
  timestamps_reference_time: 2021-09-05T00:00:00.000000-07:00
  Group /units (Units) units table
  Dataset /units/avg_firing_rate (VectorData) QC metric | shape = (506,) | dtype = float64
  Dataset /units/channel_index (VectorData) electrode channel closest to the unit | shape = (506,) | dtype = float64
  Dataset /units/id (ElementIdentifiers)  | shape = (506,) | dtype = int64
  Dataset /units/isi_violation (VectorData) QC metric | shape = (506,) | dtype = float64
  Dataset /units/probe_index (VectorData) equivalent to "group" in electrode specification | shape = (506,) | dtype = float64
  Dataset /units/region (VectorData) brain region specified in "id" column of structure_tree_safe_2017.csv | shape = (506,) | dtype = float64
  Dataset /units/salt_I (VectorData) optotagging metric | shape = (506,) | dtype = float64
  Dataset /units/salt_p (VectorData) optotagging metric | shape = (506,) | dtype = float64
  Dataset /units/spike_probability (VectorData) optotagging metric | shape = (506,) | dtype = float64
  Dataset /units/spike_times (VectorData) spike times | shape = (4478683,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) indexes data | shape = (506,) | dtype = uint64
  Dataset /units/unit_index (VectorData) Kilosort/Phy unit index (within each probe) | shape = (506,) | dtype = int64
  Dataset /units/x (VectorData) +x = posterior | shape = (506,) | dtype = float64
  Dataset /units/y (VectorData) +y = inferior | shape = (506,) | dtype = float64
  Dataset /units/z (VectorData) +z = subjects right | shape = (506,) | dtype = float64


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2023-05-04T03:51:03.902167-07:00']
  Group /general/devices/Probe0 (Device) Neuropixels 2.0 4-shank
  Group /general/devices/StimLaser (Device) OBIS
  experiment_description: mouse performing a reward-seeking task; Neuropixels 2.0 recording targeted to the medial habenula; transcranial optotagging of Tac1 neurons
  experimenter: ['Jo, YoungJu']
  Group /general/extracellular_ephys/Probe0 (ElectrodeGroup) electrode group for Probe0
  Group /general/extracellular_ephys/Probe0/device (Device) Neuropixels 2.0 4-shank
  Group /general/extracellular_ephys/electrodes (DynamicTable) all probes
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) my description | shape = (383,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) my description | shape = (383,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (383,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) my description | shape = (383,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) my description | shape = (383,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) my description | shape = (383,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) my description | shape = (383,) | dtype = float64
  institution: Stanford University
  keywords: ['electrophysiology' 'habenula']
  lab: Deisseroth
  Group /general/optogenetics/OptogeneticStimulusSite (OptogeneticStimulusSite) 
  Group /general/optogenetics/OptogeneticStimulusSite/device (Device) OBIS
  related_publications: ['doi: 10.1016/j.cell.2022.08.019']
  Group /general/subject (Subject) 
  identifier: 171_20210920
  Group /intervals/stim (TimeIntervals) individual stim pulses
  Dataset /intervals/stim/freq (VectorData) frequency in Hz | shape = (6300,) | dtype = float64
  Dataset /intervals/stim/id (ElementIdentifiers)  | shape = (6300,) | dtype = int64
  Dataset /intervals/stim/power (VectorData) unit: analog voltage input | shape = (6300,) | dtype = float64
  Dataset /intervals/stim/start_time (VectorData) pulse onset | shape = (6300,) | dtype = float64
  Dataset /intervals/stim/stop_time (VectorData) pulse offset | shape = (6300,) | dtype = float64
  Dataset /intervals/stim/width (VectorData) width in seconds | shape = (6300,) | dtype = float64
  Group /intervals/stimblock (TimeIntervals) 1-second stim blocks for optotagging
  Dataset /intervals/stimblock/freq (VectorData) frequency in Hz | shape = (290,) | dtype = float64
  Dataset /intervals/stimblock/id (ElementIdentifiers)  | shape = (290,) | dtype = int64
  Dataset /intervals/stimblock/num_pulse (VectorData) number of pulses within each stim block | shape = (290,) | dtype = float64
  Dataset /intervals/stimblock/power (VectorData) unit: analog voltage input | shape = (290,) | dtype = float64
  Dataset /intervals/stimblock/start_time (VectorData) stim block onset | shape = (290,) | dtype = float64
  Dataset /intervals/stimblock/stop_time (VectorData) stim block offset | shape = (290,) | dtype = float64
  Dataset /intervals/stimblock/width (VectorData) width in seconds | shape = (290,) | dtype = float64
  Group /intervals/trials (TimeIntervals) trials table
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (153,) | dtype = int64
  Dataset /intervals/trials/responseTime (VectorData) time from Go cue onset to lick (2 for no lick trials) | shape = (153,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Go cue onset timestamps | shape = (153,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Go cue onset timestamps (duplicate) | shape = (153,) | dtype = float64
  Dataset /intervals/trials/trial_type (VectorData) 1 = lick-reward, 2 = lick-noreward, 3 = no lick, 0 = perturbation | shape = (153,) | dtype = float64
  Group /processing/behavior (ProcessingModule) stores behavioral events
  Group /processing/behavior/BehavioralEvents (BehavioralEvents) 
  Group /processing/behavior/BehavioralEvents/timestamp_lick (TimeSeries) lick timestamps
  Group /processing/behavior/BehavioralEvents/timestamp_reward (TimeSeries) reward timestamps
  session_description:  
  session_start_time: 2021-09-20T00:00:00.000000-07:00
  Group /stimulus/presentation/OptogeneticSeries (OptogeneticSeries) dummy -- data in intervals below
  Group /stimulus/presentation/OptogeneticSeries/site (OptogeneticStimulusSite) 
  Group /stimulus/presentation/OptogeneticSeries/site/device (Device) OBIS
  timestamps_reference_time: 2021-09-20T00:00:00.000000-07:00
  Group /units (Units) units table
  Dataset /units/avg_firing_rate (VectorData) QC metric | shape = (580,) | dtype = float64
  Dataset /units/channel_index (VectorData) electrode channel closest to the unit | shape = (580,) | dtype = float64
  Dataset /units/id (ElementIdentifiers)  | shape = (580,) | dtype = int64
  Dataset /units/isi_violation (VectorData) QC metric | shape = (580,) | dtype = float64
  Dataset /units/probe_index (VectorData) equivalent to "group" in electrode specification | shape = (580,) | dtype = float64
  Dataset /units/region (VectorData) brain region specified in "id" column of structure_tree_safe_2017.csv | shape = (580,) | dtype = float64
  Dataset /units/salt_I (VectorData) optotagging metric | shape = (580,) | dtype = float64
  Dataset /units/salt_p (VectorData) optotagging metric | shape = (580,) | dtype = float64
  Dataset /units/spike_probability (VectorData) optotagging metric | shape = (580,) | dtype = float64
  Dataset /units/spike_times (VectorData) spike times | shape = (4184947,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) indexes data | shape = (580,) | dtype = uint64
  Dataset /units/unit_index (VectorData) Kilosort/Phy unit index (within each probe) | shape = (580,) | dtype = int64
  Dataset /units/x (VectorData) +x = posterior | shape = (580,) | dtype = float64
  Dataset /units/y (VectorData) +y = inferior | shape = (580,) | dtype = float64
  Dataset /units/z (VectorData) +z = subjects right | shape = (580,) | dtype = float64


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2023-05-04T03:51:09.365670-07:00']
  Group /general/devices/Probe0 (Device) Neuropixels 2.0 4-shank
  Group /general/devices/StimLaser (Device) OBIS
  experiment_description: mouse performing a reward-seeking task; Neuropixels 2.0 recording targeted to the medial habenula; transcranial optotagging of Tac1 neurons
  experimenter: ['Jo, YoungJu']
  Group /general/extracellular_ephys/Probe0 (ElectrodeGroup) electrode group for Probe0
  Group /general/extracellular_ephys/Probe0/device (Device) Neuropixels 2.0 4-shank
  Group /general/extracellular_ephys/electrodes (DynamicTable) all probes
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) my description | shape = (383,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) my description | shape = (383,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (383,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) my description | shape = (383,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) my description | shape = (383,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) my description | shape = (383,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) my description | shape = (383,) | dtype = float64
  institution: Stanford University
  keywords: ['electrophysiology' 'habenula']
  lab: Deisseroth
  Group /general/optogenetics/OptogeneticStimulusSite (OptogeneticStimulusSite) 
  Group /general/optogenetics/OptogeneticStimulusSite/device (Device) OBIS
  related_publications: ['doi: 10.1016/j.cell.2022.08.019']
  Group /general/subject (Subject) 
  identifier: 174_20210910
  Group /intervals/trials (TimeIntervals) trials table
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (110,) | dtype = int64
  Dataset /intervals/trials/responseTime (VectorData) time from Go cue onset to lick (2 for no lick trials) | shape = (110,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Go cue onset timestamps | shape = (110,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Go cue onset timestamps (duplicate) | shape = (110,) | dtype = float64
  Dataset /intervals/trials/trial_type (VectorData) 1 = lick-reward, 2 = lick-noreward, 3 = no lick, 0 = perturbation | shape = (110,) | dtype = float64
  Group /processing/behavior (ProcessingModule) stores behavioral events
  Group /processing/behavior/BehavioralEvents (BehavioralEvents) 
  Group /processing/behavior/BehavioralEvents/timestamp_lick (TimeSeries) lick timestamps
  Group /processing/behavior/BehavioralEvents/timestamp_reward (TimeSeries) reward timestamps
  session_description:  
  session_start_time: 2021-09-10T00:00:00.000000-07:00
  Group /stimulus/presentation/OptogeneticSeries (OptogeneticSeries) dummy -- data in intervals below
  Group /stimulus/presentation/OptogeneticSeries/site (OptogeneticStimulusSite) 
  Group /stimulus/presentation/OptogeneticSeries/site/device (Device) OBIS
  timestamps_reference_time: 2021-09-10T00:00:00.000000-07:00
  Group /units (Units) units table
  Dataset /units/avg_firing_rate (VectorData) QC metric | shape = (281,) | dtype = float64
  Dataset /units/channel_index (VectorData) electrode channel closest to the unit | shape = (281,) | dtype = float64
  Dataset /units/id (ElementIdentifiers)  | shape = (281,) | dtype = int64
  Dataset /units/isi_violation (VectorData) QC metric | shape = (281,) | dtype = float64
  Dataset /units/probe_index (VectorData) equivalent to "group" in electrode specification | shape = (281,) | dtype = float64
  Dataset /units/region (VectorData) brain region specified in "id" column of structure_tree_safe_2017.csv | shape = (281,) | dtype = float64
  Dataset /units/salt_I (VectorData) optotagging metric | shape = (281,) | dtype = float64
  Dataset /units/salt_p (VectorData) optotagging metric | shape = (281,) | dtype = float64
  Dataset /units/spike_probability (VectorData) optotagging metric | shape = (281,) | dtype = float64
  Dataset /units/spike_times (VectorData) spike times | shape = (4247473,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) indexes data | shape = (281,) | dtype = uint64
  Dataset /units/unit_index (VectorData) Kilosort/Phy unit index (within each probe) | shape = (281,) | dtype = int64
  Dataset /units/x (VectorData) +x = posterior | shape = (281,) | dtype = float64
  Dataset /units/y (VectorData) +y = inferior | shape = (281,) | dtype = float64
  Dataset /units/z (VectorData) +z = subjects right | shape = (281,) | dtype = float64
