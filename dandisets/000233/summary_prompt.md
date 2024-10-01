
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000233/0.230223.0815
name: A metabolic function of the hippocampal sharp wave-ripple
contributor: [{'name': 'Tingley, David', 'email': 'davidtingley2@gmail.com', 'roleName': ['dcite:Author', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0003-4263-0476', 'affiliation': [{'name': 'New York University', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/0190ak572'}], 'includeInCitation': True}, {'name': 'McClain, Kathryn', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Kaya, Ekin', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [{'name': 'Boğaziçi University', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/03z9tma90'}, {'name': 'New York University', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/0190ak572'}], 'includeInCitation': True}, {'name': 'Carpenter, Jordan', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [{'name': 'Norwegian University of Science and Technology', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/05xg72x27'}, {'name': 'New York University', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/0190ak572'}], 'includeInCitation': True}, {'name': 'Buzsáki, György', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-3100-4800', 'affiliation': [{'name': 'New York University', 'schemaKey': 'Affiliation'}], 'includeInCitation': True}, {'url': 'https://www.nih.gov/', 'name': 'National Institutes of Health', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01cwqze88', 'awardNumber': 'MH122391, U19NS104590, and U19NS107616', 'contactPoint': [], 'includeInCitation': False}]
description: The hippocampus has previously been implicated in both cognitive and endocrine functions. We simultaneously measured electrophysiological activity from the hippocampus and interstitial glucose concentrations in the body of freely behaving rats to identify an activity pattern that may link these disparate functions of the hippocampus. Here we report that clusters of sharp wave-ripples recorded from the hippocampus reliably predicted a decrease in peripheral glucose concentrations within about 10 min. This correlation was not dependent on circadian, ultradian or meal-triggered fluctuations, could be mimicked with optogenetically induced ripples in the hippocampus (but not in the parietal cortex) and was attenuated to chance levels by pharmacogenetically suppressing activity of the lateral septum, which is the major conduit between the hippocampus and the hypothalamus. Our findings demonstrate that a function of the sharp wave-ripple is to modulate peripheral glucose homeostasis, and offer a mechanism for the link between sleep disruption and blood glucose dysregulation in type 2 diabetes.
assetsSummary: {'species': [{'name': 'Rattus norvegicus - Norway rat', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10116'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 12320920243380, 'numberOfFiles': 345, 'numberOfSubjects': 25, 'variableMeasured': ['ElectricalSeries', 'ProcessingModule', 'LFP', 'ElectrodeGroup'], 'measurementTechnique': [{'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'signal filtering technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000233 has 58 NWB files.
9 of these NWB files are of type 1.
22 of these NWB files are of type 2.
2 of these NWB files are of type 3.
24 of these NWB files are of type 4.
1 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Accelerometer (TimeSeries) Raw data from accelerometer sensors.
  Group /acquisition/ElectricalSeriesRaw (ElectricalSeries) Raw acquired data
  Dataset /acquisition/ElectricalSeriesRaw/electrodes (DynamicTableRegion) electrode_table_region | shape = (32,) | dtype = int64
  Group /acquisition/GlucoseLevel (TimeSeries) Raw current from Medtronic iPro2 ISIG tracking.
  file_create_date: ['2022-04-24T05:01:07.926126+00:00']
  Group /general/devices/IntanDevice (Device) Recordings were conducted using the Intan RHD2000 interface board, sampled at 20 kHz. Amplification and  digitization were done on the head stage. Data were visualized with Neurosuite software. All  local field potential (LFP) analyses (ripple detection, state scoring and so on) were conducted on  the 1,250-Hz down-sampled signal.
  
  Group /general/devices/Medtronic iPro2 CGM (Device) Continuous Glucose Monitoring (CGM) system used to track subject glucose levels.
  experiment_description: Experiment condition 'ripple/glucose recording' with surgery condition 'rCA1'.
  experimenter: ['Tingley, David' 'McClain, Kathryn' 'Kaya, Ekin' 'Carpenter, Jordan'
   'Buzsáki, György']
  Group /general/extracellular_ephys/Group1 (ElectrodeGroup) Group1 electrodes.
  Group /general/extracellular_ephys/Group1/device (Device) Recordings were conducted using the Intan RHD2000 interface board, sampled at 20 kHz. Amplification and  digitization were done on the head stage. Data were visualized with Neurosuite software. All  local field potential (LFP) analyses (ripple detection, state scoring and so on) were conducted on  the 1,250-Hz down-sampled signal.
  
  Group /general/extracellular_ephys/Group2 (ElectrodeGroup) Group2 electrodes.
  Group /general/extracellular_ephys/Group2/device (Device) Recordings were conducted using the Intan RHD2000 interface board, sampled at 20 kHz. Amplification and  digitization were done on the head stage. Data were visualized with Neurosuite software. All  local field potential (LFP) analyses (ripple detection, state scoring and so on) were conducted on  the 1,250-Hz down-sampled signal.
  
  Group /general/extracellular_ephys/Group3 (ElectrodeGroup) Group3 electrodes.
  Group /general/extracellular_ephys/Group3/device (Device) Recordings were conducted using the Intan RHD2000 interface board, sampled at 20 kHz. Amplification and  digitization were done on the head stage. Data were visualized with Neurosuite software. All  local field potential (LFP) analyses (ripple detection, state scoring and so on) were conducted on  the 1,250-Hz down-sampled signal.
  
  Group /general/extracellular_ephys/Group4 (ElectrodeGroup) Group4 electrodes.
  Group /general/extracellular_ephys/Group4/device (Device) Recordings were conducted using the Intan RHD2000 interface board, sampled at 20 kHz. Amplification and  digitization were done on the head stage. Data were visualized with Neurosuite software. All  local field potential (LFP) analyses (ripple detection, state scoring and so on) were conducted on  the 1,250-Hz down-sampled signal.
  
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/channel_name (VectorData) unique channel reference | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/gain_to_uV (VectorData) gain_to_uV | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (32,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/rel_x (VectorData) rel_x | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_y (VectorData) rel_y | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/shank_electrode_number (VectorData) 0-indexed channel within a shank. | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (32,) | dtype = float64
  institution: NYU
  keywords: ['glucose' 'ecephys' 'pharmacology']
  lab: Buzsáki
  related_publications: ['https://doi.org/10.1038/s41586-021-03811-w']
  session_id: CGM1_0um_181130_112307
  Group /general/subject (Subject) 
  identifier: 57989eae-ca57-4a4d-92f2-d723096a89cf
  Group /processing/behavior (ProcessingModule) Contains behavioral data concerning classified states.
  Group /processing/behavior/sleep_states (TimeIntervals) Sleep state of the animal.
  Dataset /processing/behavior/sleep_states/id (ElementIdentifiers)  | shape = (64,) | dtype = int64
  Dataset /processing/behavior/sleep_states/label (VectorData) Sleep state. | shape = (64,) | dtype = object
  Dataset /processing/behavior/sleep_states/start_time (VectorData) Start time of epoch, in seconds | shape = (64,) | dtype = float64
  Dataset /processing/behavior/sleep_states/stop_time (VectorData) Stop time of epoch, in seconds | shape = (64,) | dtype = float64
  Group /processing/ecephys (ProcessingModule) Intermediate data from extracellular electrophysiology recordings, e.g., LFP.
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/ElectricalSeriesLFP (ElectricalSeries) Local field potential signal.
  Dataset /processing/ecephys/LFP/ElectricalSeriesLFP/electrodes (DynamicTableRegion) electrode_table_region | shape = (32,) | dtype = int64
  session_description: no description
  session_start_time: 2018-11-29T18:15:00+00:00
  timestamps_reference_time: 2018-11-29T18:15:00+00:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Accelerometer (TimeSeries) Raw data from accelerometer sensors.
  Group /acquisition/ElectricalSeriesRaw (ElectricalSeries) Raw acquired data
  Dataset /acquisition/ElectricalSeriesRaw/electrodes (DynamicTableRegion) electrode_table_region | shape = (32,) | dtype = int64
  Group /acquisition/GlucoseLevel (TimeSeries) Raw current from Medtronic iPro2 ISIG tracking.
  file_create_date: ['2022-04-24T05:01:07.768269+00:00']
  Group /general/devices/IntanDevice (Device) Recordings were conducted using the Intan RHD2000 interface board, sampled at 20 kHz. Amplification and  digitization were done on the head stage. Data were visualized with Neurosuite software. All  local field potential (LFP) analyses (ripple detection, state scoring and so on) were conducted on  the 1,250-Hz down-sampled signal.
  
  Group /general/devices/Medtronic iPro2 CGM (Device) Continuous Glucose Monitoring (CGM) system used to track subject glucose levels.
  experiment_description: Experiment condition 'ripple/glucose recording' with surgery condition 'rCA1'.
  experimenter: ['Tingley, David' 'McClain, Kathryn' 'Kaya, Ekin' 'Carpenter, Jordan'
   'Buzsáki, György']
  Group /general/extracellular_ephys/Group1 (ElectrodeGroup) Group1 electrodes.
  Group /general/extracellular_ephys/Group1/device (Device) Recordings were conducted using the Intan RHD2000 interface board, sampled at 20 kHz. Amplification and  digitization were done on the head stage. Data were visualized with Neurosuite software. All  local field potential (LFP) analyses (ripple detection, state scoring and so on) were conducted on  the 1,250-Hz down-sampled signal.
  
  Group /general/extracellular_ephys/Group2 (ElectrodeGroup) Group2 electrodes.
  Group /general/extracellular_ephys/Group2/device (Device) Recordings were conducted using the Intan RHD2000 interface board, sampled at 20 kHz. Amplification and  digitization were done on the head stage. Data were visualized with Neurosuite software. All  local field potential (LFP) analyses (ripple detection, state scoring and so on) were conducted on  the 1,250-Hz down-sampled signal.
  
  Group /general/extracellular_ephys/Group3 (ElectrodeGroup) Group3 electrodes.
  Group /general/extracellular_ephys/Group3/device (Device) Recordings were conducted using the Intan RHD2000 interface board, sampled at 20 kHz. Amplification and  digitization were done on the head stage. Data were visualized with Neurosuite software. All  local field potential (LFP) analyses (ripple detection, state scoring and so on) were conducted on  the 1,250-Hz down-sampled signal.
  
  Group /general/extracellular_ephys/Group4 (ElectrodeGroup) Group4 electrodes.
  Group /general/extracellular_ephys/Group4/device (Device) Recordings were conducted using the Intan RHD2000 interface board, sampled at 20 kHz. Amplification and  digitization were done on the head stage. Data were visualized with Neurosuite software. All  local field potential (LFP) analyses (ripple detection, state scoring and so on) were conducted on  the 1,250-Hz down-sampled signal.
  
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/channel_name (VectorData) unique channel reference | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/gain_to_uV (VectorData) gain_to_uV | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (32,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/rel_x (VectorData) rel_x | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_y (VectorData) rel_y | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/shank_electrode_number (VectorData) 0-indexed channel within a shank. | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (32,) | dtype = float64
  institution: NYU
  keywords: ['glucose' 'ecephys' 'pharmacology']
  lab: Buzsáki
  related_publications: ['https://doi.org/10.1038/s41586-021-03811-w']
  session_id: CGM1_288um_181130_123859
  Group /general/subject (Subject) 
  identifier: 230f27f2-746e-4681-a892-94ba5f9c3e83
  Group /processing/behavior (ProcessingModule) Contains behavioral data concerning classified states.
  Group /processing/behavior/sleep_states (TimeIntervals) Sleep state of the animal.
  Dataset /processing/behavior/sleep_states/id (ElementIdentifiers)  | shape = (95,) | dtype = int64
  Dataset /processing/behavior/sleep_states/label (VectorData) Sleep state. | shape = (95,) | dtype = object
  Dataset /processing/behavior/sleep_states/start_time (VectorData) Start time of epoch, in seconds | shape = (95,) | dtype = float64
  Dataset /processing/behavior/sleep_states/stop_time (VectorData) Stop time of epoch, in seconds | shape = (95,) | dtype = float64
  Group /processing/ecephys (ProcessingModule) Intermediate data from extracellular electrophysiology recordings, e.g., LFP.
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/ElectricalSeriesLFP (ElectricalSeries) Local field potential signal.
  Dataset /processing/ecephys/LFP/ElectricalSeriesLFP/electrodes (DynamicTableRegion) electrode_table_region | shape = (32,) | dtype = int64
  Group /processing/ecephys/Ripples (TimeIntervals) Identified Ripples events and their metrics.
  Dataset /processing/ecephys/Ripples/amplitude (VectorData) Amplitude of each point on the ripple. | shape = (1, 187) | dtype = float64
  Dataset /processing/ecephys/Ripples/amplitude_index (VectorIndex) Index for VectorData 'amplitude' | shape = (1,) | dtype = uint8
  Dataset /processing/ecephys/Ripples/duration (VectorData) Duration of the ripple event. | shape = (1,) | dtype = float64
  Dataset /processing/ecephys/Ripples/frequency (VectorData) Frequency of each point on the ripple. | shape = (1, 187) | dtype = float64
  Dataset /processing/ecephys/Ripples/frequency_index (VectorIndex) Index for VectorData 'frequency' | shape = (1,) | dtype = uint8
  Dataset /processing/ecephys/Ripples/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /processing/ecephys/Ripples/peak (VectorData) Peak of the ripple. | shape = (1,) | dtype = float64
  Dataset /processing/ecephys/Ripples/peak_amplitude (VectorData) Peak amplitude of the ripple. | shape = (1,) | dtype = float64
  Dataset /processing/ecephys/Ripples/peak_frequency (VectorData) Peak frequency of the ripple. | shape = (1,) | dtype = float64
  Dataset /processing/ecephys/Ripples/peak_normed_power (VectorData) Normed power of the peak. | shape = (1,) | dtype = float64
  Dataset /processing/ecephys/Ripples/phase (VectorData) Phase of each point on the ripple. | shape = (1, 187) | dtype = float64
  Dataset /processing/ecephys/Ripples/phase_index (VectorIndex) Index for VectorData 'phase' | shape = (1,) | dtype = uint8
  Dataset /processing/ecephys/Ripples/ripple (VectorData) Extracted ripple data. | shape = (1, 187) | dtype = float64
  Dataset /processing/ecephys/Ripples/ripple_index (VectorIndex) Index for VectorData 'ripple' | shape = (1,) | dtype = uint8
  Dataset /processing/ecephys/Ripples/start_time (VectorData) Start time of epoch, in seconds | shape = (1,) | dtype = float64
  Dataset /processing/ecephys/Ripples/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1,) | dtype = float64
  session_description: no description
  session_start_time: 2018-11-29T18:15:00+00:00
  timestamps_reference_time: 2018-11-29T18:15:00+00:00


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Accelerometer (TimeSeries) Raw data from accelerometer sensors.
  Group /acquisition/ElectricalSeriesRaw (ElectricalSeries) Raw acquired data
  Dataset /acquisition/ElectricalSeriesRaw/electrodes (DynamicTableRegion) electrode_table_region | shape = (32,) | dtype = int64
  Group /acquisition/GlucoseLevel (TimeSeries) Raw current from Medtronic iPro2 ISIG tracking.
  file_create_date: ['2022-04-24T16:00:56.198719+00:00']
  Group /general/devices/IntanDevice (Device) Recordings were conducted using the Intan RHD2000 interface board, sampled at 20 kHz. Amplification and  digitization were done on the head stage. Data were visualized with Neurosuite software. All  local field potential (LFP) analyses (ripple detection, state scoring and so on) were conducted on  the 1,250-Hz down-sampled signal.
  
  Group /general/devices/Medtronic iPro2 CGM (Device) Continuous Glucose Monitoring (CGM) system used to track subject glucose levels.
  experiment_description: Consult Supplementary Table 1 from the publication for more information about this session.
  experimenter: ['Tingley, David' 'McClain, Kathryn' 'Kaya, Ekin' 'Carpenter, Jordan'
   'Buzsáki, György']
  Group /general/extracellular_ephys/Group1 (ElectrodeGroup) Group1 electrodes.
  Group /general/extracellular_ephys/Group1/device (Device) Recordings were conducted using the Intan RHD2000 interface board, sampled at 20 kHz. Amplification and  digitization were done on the head stage. Data were visualized with Neurosuite software. All  local field potential (LFP) analyses (ripple detection, state scoring and so on) were conducted on  the 1,250-Hz down-sampled signal.
  
  Group /general/extracellular_ephys/Group2 (ElectrodeGroup) Group2 electrodes.
  Group /general/extracellular_ephys/Group2/device (Device) Recordings were conducted using the Intan RHD2000 interface board, sampled at 20 kHz. Amplification and  digitization were done on the head stage. Data were visualized with Neurosuite software. All  local field potential (LFP) analyses (ripple detection, state scoring and so on) were conducted on  the 1,250-Hz down-sampled signal.
  
  Group /general/extracellular_ephys/Group3 (ElectrodeGroup) Group3 electrodes.
  Group /general/extracellular_ephys/Group3/device (Device) Recordings were conducted using the Intan RHD2000 interface board, sampled at 20 kHz. Amplification and  digitization were done on the head stage. Data were visualized with Neurosuite software. All  local field potential (LFP) analyses (ripple detection, state scoring and so on) were conducted on  the 1,250-Hz down-sampled signal.
  
  Group /general/extracellular_ephys/Group4 (ElectrodeGroup) Group4 electrodes.
  Group /general/extracellular_ephys/Group4/device (Device) Recordings were conducted using the Intan RHD2000 interface board, sampled at 20 kHz. Amplification and  digitization were done on the head stage. Data were visualized with Neurosuite software. All  local field potential (LFP) analyses (ripple detection, state scoring and so on) were conducted on  the 1,250-Hz down-sampled signal.
  
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/channel_name (VectorData) unique channel reference | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/gain_to_uV (VectorData) gain_to_uV | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (32,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/rel_x (VectorData) rel_x | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_y (VectorData) rel_y | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/shank_electrode_number (VectorData) 0-indexed channel within a shank. | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (32,) | dtype = float64
  institution: NYU
  keywords: ['glucose' 'ecephys' 'pharmacology']
  lab: Buzsáki
  related_publications: ['https://doi.org/10.1038/s41586-021-03811-w']
  session_id: CGM3_72um_190301_134959
  Group /general/subject (Subject) 
  identifier: 92927947-4d66-48b4-8939-17231146f5fa
  Group /processing/ecephys (ProcessingModule) Intermediate data from extracellular electrophysiology recordings, e.g., LFP.
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/ElectricalSeriesLFP (ElectricalSeries) Local field potential signal.
  Dataset /processing/ecephys/LFP/ElectricalSeriesLFP/electrodes (DynamicTableRegion) electrode_table_region | shape = (32,) | dtype = int64
  session_description: no description
  session_start_time: 2019-03-11T15:52:00+00:00
  timestamps_reference_time: 2019-03-11T15:52:00+00:00


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Accelerometer (TimeSeries) Raw data from accelerometer sensors.
  Group /acquisition/ElectricalSeriesRaw (ElectricalSeries) Raw acquired data
  Dataset /acquisition/ElectricalSeriesRaw/electrodes (DynamicTableRegion) electrode_table_region | shape = (32,) | dtype = int64
  Group /acquisition/GlucoseLevel (TimeSeries) Raw current from Medtronic iPro2 ISIG tracking.
  file_create_date: ['2022-04-24T20:46:46.957133+00:00']
  Group /general/devices/IntanDevice (Device) Recordings were conducted using the Intan RHD2000 interface board, sampled at 20 kHz. Amplification and  digitization were done on the head stage. Data were visualized with Neurosuite software. All  local field potential (LFP) analyses (ripple detection, state scoring and so on) were conducted on  the 1,250-Hz down-sampled signal.
  
  Group /general/devices/Medtronic iPro2 CGM (Device) Continuous Glucose Monitoring (CGM) system used to track subject glucose levels.
  experiment_description: Consult Supplementary Table 1 from the publication for more information about this session.
  experimenter: ['Tingley, David' 'McClain, Kathryn' 'Kaya, Ekin' 'Carpenter, Jordan'
   'Buzsáki, György']
  Group /general/extracellular_ephys/Group1 (ElectrodeGroup) Group1 electrodes.
  Group /general/extracellular_ephys/Group1/device (Device) Recordings were conducted using the Intan RHD2000 interface board, sampled at 20 kHz. Amplification and  digitization were done on the head stage. Data were visualized with Neurosuite software. All  local field potential (LFP) analyses (ripple detection, state scoring and so on) were conducted on  the 1,250-Hz down-sampled signal.
  
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/channel_name (VectorData) unique channel reference | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/gain_to_uV (VectorData) gain_to_uV | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (32,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/rel_x (VectorData) rel_x | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_y (VectorData) rel_y | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/shank_electrode_number (VectorData) 0-indexed channel within a shank. | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (32,) | dtype = float64
  institution: NYU
  keywords: ['glucose' 'ecephys' 'pharmacology']
  lab: Buzsáki
  related_publications: ['https://doi.org/10.1038/s41586-021-03811-w']
  session_id: CGM30_1008um_210125_090922
  Group /general/subject (Subject) 
  identifier: cfbfb30c-47a3-466c-9169-8975c9e99938
  Group /processing/ecephys (ProcessingModule) Intermediate data from extracellular electrophysiology recordings, e.g., LFP.
  Group /processing/ecephys/Ca1Ripples (TimeIntervals) Identified Ca1Ripples events and their metrics.
  Dataset /processing/ecephys/Ca1Ripples/amplitude (VectorData) Amplitude of each point on the ripple. | shape = (15310, 187) | dtype = float64
  Dataset /processing/ecephys/Ca1Ripples/amplitude_index (VectorIndex) Index for VectorData 'amplitude' | shape = (15310,) | dtype = uint16
  Dataset /processing/ecephys/Ca1Ripples/duration (VectorData) Duration of the ripple event. | shape = (15310,) | dtype = float64
  Dataset /processing/ecephys/Ca1Ripples/frequency (VectorData) Frequency of each point on the ripple. | shape = (15310, 187) | dtype = float64
  Dataset /processing/ecephys/Ca1Ripples/frequency_index (VectorIndex) Index for VectorData 'frequency' | shape = (15310,) | dtype = uint16
  Dataset /processing/ecephys/Ca1Ripples/id (ElementIdentifiers)  | shape = (15310,) | dtype = int64
  Dataset /processing/ecephys/Ca1Ripples/peak (VectorData) Peak of the ripple. | shape = (15310,) | dtype = float64
  Dataset /processing/ecephys/Ca1Ripples/peak_amplitude (VectorData) Peak amplitude of the ripple. | shape = (15310,) | dtype = float64
  Dataset /processing/ecephys/Ca1Ripples/peak_frequency (VectorData) Peak frequency of the ripple. | shape = (15310,) | dtype = float64
  Dataset /processing/ecephys/Ca1Ripples/peak_normed_power (VectorData) Normed power of the peak. | shape = (15310,) | dtype = float64
  Dataset /processing/ecephys/Ca1Ripples/phase (VectorData) Phase of each point on the ripple. | shape = (15310, 187) | dtype = float64
  Dataset /processing/ecephys/Ca1Ripples/phase_index (VectorIndex) Index for VectorData 'phase' | shape = (15310,) | dtype = uint16
  Dataset /processing/ecephys/Ca1Ripples/ripple (VectorData) Extracted ripple data. | shape = (15310, 187) | dtype = float64
  Dataset /processing/ecephys/Ca1Ripples/ripple_index (VectorIndex) Index for VectorData 'ripple' | shape = (15310,) | dtype = uint16
  Dataset /processing/ecephys/Ca1Ripples/start_time (VectorData) Start time of epoch, in seconds | shape = (15310,) | dtype = float64
  Dataset /processing/ecephys/Ca1Ripples/stop_time (VectorData) Stop time of epoch, in seconds | shape = (15310,) | dtype = float64
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/ElectricalSeriesLFP (ElectricalSeries) Local field potential signal.
  Dataset /processing/ecephys/LFP/ElectricalSeriesLFP/electrodes (DynamicTableRegion) electrode_table_region | shape = (32,) | dtype = int64
  session_description: Consult Supplementary Table 1 from the publication for more information about this session.
  session_start_time: 2021-01-24T11:02:05+00:00
  timestamps_reference_time: 2021-01-24T11:02:05+00:00


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Accelerometer (TimeSeries) Raw data from accelerometer sensors.
  Group /acquisition/ElectricalSeriesRaw (ElectricalSeries) Raw acquired data
  Dataset /acquisition/ElectricalSeriesRaw/electrodes (DynamicTableRegion) electrode_table_region | shape = (32,) | dtype = int64
  Group /acquisition/GlucoseLevel (TimeSeries) Raw current from Medtronic iPro2 ISIG tracking.
  file_create_date: ['2022-04-24T20:46:46.882218+00:00']
  Group /general/devices/IntanDevice (Device) Recordings were conducted using the Intan RHD2000 interface board, sampled at 20 kHz. Amplification and  digitization were done on the head stage. Data were visualized with Neurosuite software. All  local field potential (LFP) analyses (ripple detection, state scoring and so on) were conducted on  the 1,250-Hz down-sampled signal.
  
  Group /general/devices/Medtronic iPro2 CGM (Device) Continuous Glucose Monitoring (CGM) system used to track subject glucose levels.
  experiment_description: Consult Supplementary Table 1 from the publication for more information about this session.
  experimenter: ['Tingley, David' 'McClain, Kathryn' 'Kaya, Ekin' 'Carpenter, Jordan'
   'Buzsáki, György']
  Group /general/extracellular_ephys/Group1 (ElectrodeGroup) Group1 electrodes.
  Group /general/extracellular_ephys/Group1/device (Device) Recordings were conducted using the Intan RHD2000 interface board, sampled at 20 kHz. Amplification and  digitization were done on the head stage. Data were visualized with Neurosuite software. All  local field potential (LFP) analyses (ripple detection, state scoring and so on) were conducted on  the 1,250-Hz down-sampled signal.
  
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/channel_name (VectorData) unique channel reference | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/gain_to_uV (VectorData) gain_to_uV | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (32,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/rel_x (VectorData) rel_x | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_y (VectorData) rel_y | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/shank_electrode_number (VectorData) 0-indexed channel within a shank. | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (32,) | dtype = float64
  institution: NYU
  keywords: ['glucose' 'ecephys' 'pharmacology']
  lab: Buzsáki
  related_publications: ['https://doi.org/10.1038/s41586-021-03811-w']
  session_id: CGM30_288um_210123_195337
  Group /general/subject (Subject) 
  identifier: 9ae9a3be-0146-4570-9d3f-2e9bfc5e02d1
  Group /processing/ecephys (ProcessingModule) Intermediate data from extracellular electrophysiology recordings, e.g., LFP.
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/ElectricalSeriesLFP (ElectricalSeries) Local field potential signal.
  Dataset /processing/ecephys/LFP/ElectricalSeriesLFP/electrodes (DynamicTableRegion) electrode_table_region | shape = (32,) | dtype = int64
  session_description: Consult Supplementary Table 1 from the publication for more information about this session.
  session_start_time: 2021-01-24T11:02:05+00:00
  timestamps_reference_time: 2021-01-24T11:02:05+00:00
