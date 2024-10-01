
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000473/0.230417.1502
name: Esr1+ hypothalamic-habenula neurons shape aversive states.
contributor: [{'name': 'Calvigioni, Daniela', 'email': 'daniela.calvigioni@ki.se', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-6122-9744', 'affiliation': [], 'includeInCitation': True}, {'name': 'Fuzik, Janos', 'email': 'janos.fuzik@ki.se', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-5408-4882', 'affiliation': [], 'includeInCitation': True}, {'name': 'Le Merre, Pierre', 'email': 'pierre.le.merre@ki.se', 'roleName': ['dcite:ContactPerson', 'dcite:Author', 'dcite:DataCollector', 'dcite:DataCurator', 'dcite:DataManager'], 'schemaKey': 'Person', 'identifier': '0000-0003-4205-7411', 'affiliation': [], 'includeInCitation': True}, {'name': 'Slashcheva, Marina', 'email': 'marina.slashcheva@ki.se', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Jung, Felix', 'email': 'felix.jung@ki.se', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Ortiz, Cantin', 'email': 'cantin.ortiz@pasteur.fr', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Lentini, Antonio', 'email': 'antonio.lentini@ki.se', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Csillag, Veronika', 'email': 'veronika.csillag@ki.se', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Graziano, Marta', 'email': 'marta.graziano@ki.se', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Nikolakopoulou, Ifigeneia', 'email': 'ifigeneia.nikolakopoulou@ki.se', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Weglage, Moritz', 'email': 'moritz.weglage@ki.se', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Lazaridis, Iakovos', 'email': 'iaklaz@mit.edu', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Kim, Hoseok', 'email': 'kim.hoseok@ki.se', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Lenzi, Irene', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Park, Hyunsoo', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Reinius, Björn', 'email': 'Björn Reinius <bjorn.reinius@ki.se>', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Carlén, Marie', 'email': 'marie.carlen@ki.se', 'roleName': ['dcite:Author', 'dcite:Conceptualization'], 'schemaKey': 'Person', 'identifier': '0000-0003-1658-1631', 'affiliation': [], 'includeInCitation': True}, {'name': 'Meletis, Konstantinos', 'email': 'dinos.meletis@ki.se', 'roleName': ['dcite:Author', 'dcite:Conceptualization'], 'schemaKey': 'Person', 'identifier': '0000-0001-5665-4781', 'affiliation': [], 'includeInCitation': True}]
description: Prefrontal cortex (PFC) high-density extracellular recordings (Neuropixels) in head-fixed mice during an aversive-conditioning task. Neuronal responses to internally generated (i.e. pathway-specific optogenetic activation, see the main article for details) and externally derived (i.e. air puffs) aversive signals have been recorded.
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}, {'name': 'optogenetic approach', 'schemaKey': 'ApproachType'}, {'name': 'behavioral approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 113558681447, 'numberOfFiles': 25, 'numberOfSubjects': 25, 'variableMeasured': ['PupilTracking', 'ElectrodeGroup', 'ElectricalSeries', 'ProcessingModule', 'OptogeneticSeries', 'Units', 'LFP', 'BehavioralTimeSeries'], 'measurementTechnique': [{'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'signal filtering technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000473 has 25 NWB files.
1 of these NWB files are of type 1.
24 of these NWB files are of type 2.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /analysis/LFP saturation start (TimeSeries) start times of the LFP saturation epoch
  Group /analysis/LFP saturation stop (TimeSeries) stop times of the LFP saturation epoch
  Group /analysis/spike saturation start (TimeSeries) start times of the spike saturation epoch
  Group /analysis/spike saturation stop (TimeSeries) stop times of the spike saturation epoch
  file_create_date: ['2023-04-14T16:38:18.799906+02:00']
  Group /general/devices/array (Device) Neuropixels 3B1
  Group /general/devices/laser (Device) laser-473nm
  experiment_description: Neuropixels recording in mPFC during aversive conditioning task
  experimenter: ['Le Merre, Pierre']
  Group /general/extracellular_ephys/electrodes (DynamicTable) all electrodes
  Dataset /general/extracellular_ephys/electrodes/AP (VectorData) my description | shape = (383,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/DV (VectorData) my description | shape = (383,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/ML (VectorData) my description | shape = (383,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) my description | shape = (383,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) my description | shape = (383,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) my description | shape = (383,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (383,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) my description | shape = (383,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/label (VectorData) my description | shape = (383,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) my description | shape = (383,) | dtype = object
  Group /general/extracellular_ephys/probe1 (ElectrodeGroup) electrode group for probe1
  Group /general/extracellular_ephys/probe1/device (Device) Neuropixels 3B1
  institution: Karolinska Institutet
  keywords: ['Prefrontal Cortex' 'Auditory Processing' 'Aversion']
  lab: Carlen Lab
  Group /general/optogenetics/OptogeneticStimulusSite (OptogeneticStimulusSite) 
  Group /general/optogenetics/OptogeneticStimulusSite/device (Device) laser-473nm
  session_id: 128514_20191215-probe0
  stimulus: ['pure tone, blue noise, photostim, air puff']
  Group /general/subject (Subject) 
  surgery: Mice were prepared for electrophysiology and optogenetics with a recording chamber, a headpost and optic fibers. The scalp and periosteum over the dorsal surface of the skull were removed. A layer of cyanoacrylate adhesive (Locite) was directly applied to the intact skull. A custom made headpost  and optic fibers were placed on the skull (headpost: approximately over cerebellum and right hemisphere; optic fibers: over LHA) and cemented in place with Palavit/Paladur.
  identifier: 128514_20191215-probe0
  Group /intervals/trials (TimeIntervals) trial data and properties
  Dataset /intervals/trials/Block (VectorData) Block number | shape = (571,) | dtype = float64
  Dataset /intervals/trials/airpuff (VectorData) bolean for airpuff | shape = (571,) | dtype = float64
  Dataset /intervals/trials/airpuff_amp (VectorData) Airpuff volatge control amplitude (V) | shape = (571,) | dtype = float64
  Dataset /intervals/trials/airpuff_duration (VectorData) Airpuff duration (s) | shape = (571,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (571,) | dtype = int64
  Dataset /intervals/trials/opto_freq (VectorData) pulse train frequency | shape = (571,) | dtype = float64
  Dataset /intervals/trials/opto_power (VectorData) laser power | shape = (571,) | dtype = float64
  Dataset /intervals/trials/opto_pulse_duration (VectorData) pulse duration (s) | shape = (571,) | dtype = float64
  Dataset /intervals/trials/opto_pulse_ts (VectorData) individual pulses timestamps | shape = (571, 20) | dtype = float64
  Dataset /intervals/trials/optogenetics (VectorData) bolean for optogenetics | shape = (571,) | dtype = bool
  Dataset /intervals/trials/sound (VectorData) bolean for sound | shape = (571,) | dtype = float64
  Dataset /intervals/trials/sound_amp (VectorData) sound amplitude | shape = (571,) | dtype = float64
  Dataset /intervals/trials/sound_bluenoise (VectorData) bolean for blue noise | shape = (571,) | dtype = float64
  Dataset /intervals/trials/sound_freq (VectorData) sound frequency | shape = (571,) | dtype = float64
  Dataset /intervals/trials/sound_puretone (VectorData) bolean for sound | shape = (571,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) start time of trial | shape = (571,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) end of each trial | shape = (571,) | dtype = float64
  Group /processing/behavior (ProcessingModule) Behavior
  Group /processing/behavior/BehavioralTimeSeries (BehavioralTimeSeries) 
  Group /processing/behavior/BehavioralTimeSeries/face_motion_data (TimeSeries) 1st three face motion traces extracted with Facemap algorithm form the face movie
  Group /processing/behavior/Blink (BehavioralTimeSeries) 
  Group /processing/behavior/Blink/blink (TimeSeries) Blink trace extracted with Facemap algorithm form the pupil movies
  Group /processing/behavior/PupilTracking (PupilTracking) 
  Group /processing/behavior/PupilTracking/eye_area (TimeSeries) smoothed pupil trace extracted with Facemap algorithm form the pupil movies
  Group /processing/ecephys (ProcessingModule) extracellular electrophysiology
  Group /processing/ecephys/EMG (LFP) 
  Group /processing/ecephys/EMG/ElectricalSeries (ElectricalSeries) EMG
  Dataset /processing/ecephys/EMG/ElectricalSeries/electrodes (DynamicTableRegion) EMG electrode | shape = (1,) | dtype = int64
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/ElectricalSeries (ElectricalSeries) LFP
  Dataset /processing/ecephys/LFP/ElectricalSeries/electrodes (DynamicTableRegion) all electrodes | shape = (383,) | dtype = int64
  session_description: Neuropixels recording in mPFC during aversive conditioning task
  session_start_time: 2019-12-15T17:33:28.000000+01:00
  Group /stimulus/presentation/AudStim_10kHz (TimeSeries) Sound Amplitude in V corresponding to different sound pressures
  Group /stimulus/presentation/OptogeneticSeries (OptogeneticSeries) Optogenetic stim pulse data: pulse of 5ms with 1ms SinRamp in and out, Optical power in data (mW)
  Group /stimulus/presentation/OptogeneticSeries/site (OptogeneticStimulusSite) 
  Group /stimulus/presentation/OptogeneticSeries/site/device (Device) laser-473nm
  Group /stimulus/presentation/air_puff (TimeSeries) Air Puff in V corresponding to TTL
  Group /stimulus/presentation/passive_bluenoise (TimeSeries) Sound Amplitude in V corresponding to different sound pressures
  timestamps_reference_time: 2019-12-15T17:33:28.000000+01:00
  Group /units (Units) units table
  Dataset /units/FS (VectorData) logical vector for fast spiking units | shape = (758,) | dtype = bool
  Dataset /units/HW (VectorData) Half width (ms) | shape = (758,) | dtype = float64
  Dataset /units/PTR (VectorData) Peak to trough ratio | shape = (758,) | dtype = float64
  Dataset /units/Peak_to_Trough (VectorData) Peak to Trough (ms) | shape = (758,) | dtype = float64
  Dataset /units/PeaktoBaseline (VectorData) Peak to Baseline (ms) | shape = (758,) | dtype = float64
  Dataset /units/PeaktoBaselineArea (VectorData) Peak to Baseline Area | shape = (758,) | dtype = float64
  Dataset /units/PeaktoOnset (VectorData) Peak to Onset (uV) | shape = (758,) | dtype = float64
  Dataset /units/PeaktoOnsetTime (VectorData) Peak to Onset Time (ms) | shape = (758,) | dtype = float64
  Dataset /units/RS (VectorData) logical vector for regular spiking units | shape = (758,) | dtype = bool
  Dataset /units/TroughSize (VectorData) TroughSize (uV) | shape = (758,) | dtype = float64
  Dataset /units/dVdT (VectorData) dVdT (uV.ms-1) | shape = (758,) | dtype = float64
  Dataset /units/duration (VectorData) duration (ms) | shape = (758,) | dtype = float64
  Dataset /units/electrodes (DynamicTableRegion) electrode of the Main Waveform | shape = (758,) | dtype = int64
  Dataset /units/height (VectorData) Height (uV) | shape = (758,) | dtype = float64
  Dataset /units/id (ElementIdentifiers)  | shape = (758,) | dtype = int64
  Dataset /units/quality (VectorData) ISI violation, false positive rate | shape = (758, 2) | dtype = float64
  Dataset /units/spike_times (VectorData) spike times | shape = (12766340,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) indexes data | shape = (758,) | dtype = uint64
  Dataset /units/waveform_means (VectorData) mean of waveform | shape = (758, 82000) | dtype = float64


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /analysis/LFP saturation start (TimeSeries) start times of the LFP saturation epoch
  Group /analysis/LFP saturation stop (TimeSeries) stop times of the LFP saturation epoch
  Group /analysis/spike saturation start (TimeSeries) start times of the spike saturation epoch
  Group /analysis/spike saturation stop (TimeSeries) stop times of the spike saturation epoch
  file_create_date: ['2023-04-14T18:12:58.617373+02:00']
  Group /general/devices/array (Device) Neuropixels 3B1
  Group /general/devices/laser (Device) laser-473nm
  experiment_description: Neuropixels recording in mPFC during aversive conditioning task
  experimenter: ['Le Merre, Pierre']
  Group /general/extracellular_ephys/electrodes (DynamicTable) all electrodes
  Dataset /general/extracellular_ephys/electrodes/AP (VectorData) my description | shape = (383,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/DV (VectorData) my description | shape = (383,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/ML (VectorData) my description | shape = (383,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) my description | shape = (383,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) my description | shape = (383,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) my description | shape = (383,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (383,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) my description | shape = (383,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/label (VectorData) my description | shape = (383,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) my description | shape = (383,) | dtype = object
  Group /general/extracellular_ephys/probe1 (ElectrodeGroup) electrode group for probe1
  Group /general/extracellular_ephys/probe1/device (Device) Neuropixels 3B1
  institution: Karolinska Institutet
  keywords: ['Prefrontal Cortex' 'Auditory Processing' 'Aversion']
  lab: Carlen Lab
  Group /general/optogenetics/OptogeneticStimulusSite (OptogeneticStimulusSite) 
  Group /general/optogenetics/OptogeneticStimulusSite/device (Device) laser-473nm
  session_id: 128515_20191216-probe0
  stimulus: ['pure tone, blue noise, photostim, air puff']
  Group /general/subject (Subject) 
  surgery: Mice were prepared for electrophysiology and optogenetics with a recording chamber, a headpost and optic fibers. The scalp and periosteum over the dorsal surface of the skull were removed. A layer of cyanoacrylate adhesive (Locite) was directly applied to the intact skull. A custom made headpost  and optic fibers were placed on the skull (headpost: approximately over cerebellum and right hemisphere; optic fibers: over LHA) and cemented in place with Palavit/Paladur.
  identifier: 128515_20191216-probe0
  Group /intervals/trials (TimeIntervals) trial data and properties
  Dataset /intervals/trials/Block (VectorData) Block number | shape = (610,) | dtype = float64
  Dataset /intervals/trials/airpuff (VectorData) bolean for airpuff | shape = (610,) | dtype = float64
  Dataset /intervals/trials/airpuff_amp (VectorData) Airpuff volatge control amplitude (V) | shape = (610,) | dtype = float64
  Dataset /intervals/trials/airpuff_duration (VectorData) Airpuff duration (s) | shape = (610,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (610,) | dtype = int64
  Dataset /intervals/trials/opto_freq (VectorData) pulse train frequency | shape = (610,) | dtype = float64
  Dataset /intervals/trials/opto_power (VectorData) laser power | shape = (610,) | dtype = float64
  Dataset /intervals/trials/opto_pulse_duration (VectorData) pulse duration (s) | shape = (610,) | dtype = float64
  Dataset /intervals/trials/opto_pulse_ts (VectorData) individual pulses timestamps | shape = (610, 20) | dtype = float64
  Dataset /intervals/trials/optogenetics (VectorData) bolean for optogenetics | shape = (610,) | dtype = bool
  Dataset /intervals/trials/sound (VectorData) bolean for sound | shape = (610,) | dtype = float64
  Dataset /intervals/trials/sound_amp (VectorData) sound amplitude | shape = (610,) | dtype = float64
  Dataset /intervals/trials/sound_bluenoise (VectorData) bolean for blue noise | shape = (610,) | dtype = float64
  Dataset /intervals/trials/sound_freq (VectorData) sound frequency | shape = (610,) | dtype = float64
  Dataset /intervals/trials/sound_puretone (VectorData) bolean for sound | shape = (610,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) start time of trial | shape = (610,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) end of each trial | shape = (610,) | dtype = float64
  Group /processing/ecephys (ProcessingModule) extracellular electrophysiology
  Group /processing/ecephys/EMG (LFP) 
  Group /processing/ecephys/EMG/ElectricalSeries (ElectricalSeries) EMG
  Dataset /processing/ecephys/EMG/ElectricalSeries/electrodes (DynamicTableRegion) EMG electrode | shape = (1,) | dtype = int64
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/ElectricalSeries (ElectricalSeries) LFP
  Dataset /processing/ecephys/LFP/ElectricalSeries/electrodes (DynamicTableRegion) all electrodes | shape = (383,) | dtype = int64
  session_description: Neuropixels recording in mPFC during aversive conditioning task
  session_start_time: 2019-12-16T14:24:11.000000+01:00
  Group /stimulus/presentation/AudStim_10kHz (TimeSeries) Sound Amplitude in V corresponding to different sound pressures
  Group /stimulus/presentation/OptogeneticSeries (OptogeneticSeries) Optogenetic stim pulse data: pulse of 5ms with 1ms SinRamp in and out, Optical power in data (mW)
  Group /stimulus/presentation/OptogeneticSeries/site (OptogeneticStimulusSite) 
  Group /stimulus/presentation/OptogeneticSeries/site/device (Device) laser-473nm
  Group /stimulus/presentation/air_puff (TimeSeries) Air Puff in V corresponding to TTL
  Group /stimulus/presentation/passive_bluenoise (TimeSeries) Sound Amplitude in V corresponding to different sound pressures
  timestamps_reference_time: 2019-12-16T14:24:11.000000+01:00
  Group /units (Units) units table
  Dataset /units/FS (VectorData) logical vector for fast spiking units | shape = (293,) | dtype = bool
  Dataset /units/HW (VectorData) Half width (ms) | shape = (293,) | dtype = float64
  Dataset /units/PTR (VectorData) Peak to trough ratio | shape = (293,) | dtype = float64
  Dataset /units/Peak_to_Trough (VectorData) Peak to Trough (ms) | shape = (293,) | dtype = float64
  Dataset /units/PeaktoBaseline (VectorData) Peak to Baseline (ms) | shape = (293,) | dtype = float64
  Dataset /units/PeaktoBaselineArea (VectorData) Peak to Baseline Area | shape = (293,) | dtype = float64
  Dataset /units/PeaktoOnset (VectorData) Peak to Onset (uV) | shape = (293,) | dtype = float64
  Dataset /units/PeaktoOnsetTime (VectorData) Peak to Onset Time (ms) | shape = (293,) | dtype = float64
  Dataset /units/RS (VectorData) logical vector for regular spiking units | shape = (293,) | dtype = bool
  Dataset /units/TroughSize (VectorData) TroughSize (uV) | shape = (293,) | dtype = float64
  Dataset /units/dVdT (VectorData) dVdT (uV.ms-1) | shape = (293,) | dtype = float64
  Dataset /units/duration (VectorData) duration (ms) | shape = (293,) | dtype = float64
  Dataset /units/electrodes (DynamicTableRegion) electrode of the Main Waveform | shape = (293,) | dtype = int64
  Dataset /units/height (VectorData) Height (uV) | shape = (293,) | dtype = float64
  Dataset /units/id (ElementIdentifiers)  | shape = (293,) | dtype = int64
  Dataset /units/quality (VectorData) ISI violation, false positive rate | shape = (293, 2) | dtype = float64
  Dataset /units/spike_times (VectorData) spike times | shape = (7317053,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) indexes data | shape = (293,) | dtype = uint64
  Dataset /units/waveform_means (VectorData) mean of waveform | shape = (293, 82000) | dtype = float64
