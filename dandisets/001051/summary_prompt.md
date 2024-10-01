
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001051/draft
name: Large-scale Neuropixels recordings through SHIELD implant during visual change detection task with dynamic gating of engagement
contributor: [{'name': 'Bennett, Corbett', 'email': 'corbennett@gmail.com', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Sridhar, Arjun', 'schemaKey': 'Person', 'includeInCitation': True}]
description: This dataset was collected at the Allen Institute. It includes data from 99 electrophysiology sessions featuring multi-Neuropixel recordings throughout the left hemisphere while mice performed a visual change detection task. This dataset is closely related to the Allen Institute Visual Behavior Neuropixels (VBN) dataset, but differs in two important ways: 
First, whereas the VBN recordings were focused on visual cortical areas and underlying subcortical regions, this dataset features recordings from throughout the left hemisphere, including frontal and medial cortical areas and the striatum. 
Second, we have modified the behavioral task for this dataset to experimentally manipulate task engagement. During the VBN recordings, an hour of active behavior was followed by a passive behavior block during which the lick spout was retracted and mice were presented with the same visual stimuli but now with no opportunity to lick for reward. In practice, mice often satiated before the passive block. For this dataset, we interposed a 'no-reward' block in the middle of active behavior. During this new epoch, the lick spout remained extended but licks for visual changes no longer triggered reward. At the end of the no-reward block, auto-rewards were given to indicate that rewards were once again available, and many mice resumed licking for changes.

To better understand how to access and analyze this dataset, we encourage potential users to refer to the resources below. The data in DANDI is structured as follows: each subject has session NWBs identified by date of acquisition. Then, there are LFP NWBs for up to 6 probes for each session, identified by a probe id. For the LFP, each session NWB has a probes table that has the probe ids for the LFP data associated with that session. Use this table to get the probe ids and corresponding LFP NWBs. Examples  of opening a NWB file and accessing the probes table can be seen at the GitHub below under tutorials. In addition, there is a dynamic gating sessions metadata table at the GitHub repository below that has an acquisition date column, which can be used to map to a session id (the session column in the metadata tables). This will be useful for parsing the metadata tables for multi-session analysis.

1) This repository includes a quick-start tutorial notebook as well as metadata tables for the sessions, probes, channels and units included in this dataset: https://github.com/AllenInstitute/SHIELD_Dynamic_Gating_Analysis
2) To learn more about the basic visual change detection task as well as the general structure of the nwb files, consult the documentation available for the Allen Observatory Visual Behavior Neuropixels dataset here: https://portal.brain-map.org/circuits-behavior/visual-behavior-neuropixels

This dataset was used in the following preprint: 
SHIELD: Skull-shaped hemispheric implants enabling large-scale-electrophysiology datasets in the mouse brain [https://doi.org/10.1101/2023.11.12.566771]
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 1799705339503, 'numberOfFiles': 663, 'numberOfSubjects': 27, 'variableMeasured': ['Units', 'ProcessingModule', 'LFP', 'ElectricalSeries'], 'measurementTechnique': [{'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'signal filtering technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 001051 has 17 NWB files.
2 of these NWB files are of type 1.
12 of these NWB files are of type 2.
1 of these NWB files are of type 3.
1 of these NWB files are of type 4.
1 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/EyeTracking (EllipseEyeTracking) 
  Group /acquisition/EyeTracking/corneal_reflection_tracking (EllipseSeries) no description
  Group /acquisition/EyeTracking/eye_tracking (EllipseSeries) no description
  Group /acquisition/EyeTracking/likely_blink (TimeSeries) blinks
  Group /acquisition/EyeTracking/pupil_tracking (EllipseSeries) no description
  Group /acquisition/v_in (TimeSeries) The theoretical maximum voltage that the running wheel encoder will reach prior to "wrapping". This should theoretically be 5V (after crossing 5V goes to 0V, or vice versa). In practice the encoder does not always reach this value before wrapping, which can cause transient spikes in speed at the voltage "wraps".
  Group /acquisition/v_sig (TimeSeries) Voltage signal from the running wheel encoder
  file_create_date: ['2023-09-14T15:08:57.908750+00:00']
  Group /general/devices/NP.1 (Device) Allen Brain Observatory - Scientifica 2P Rig
  Group /general/devices/probeA (EcephysProbe) Neuropixels 1.0 Probe
  Group /general/devices/probeB (EcephysProbe) Neuropixels 1.0 Probe
  Group /general/devices/probeC (EcephysProbe) Neuropixels 1.0 Probe
  Group /general/devices/probeD (EcephysProbe) Neuropixels 1.0 Probe
  Group /general/devices/probeE (EcephysProbe) Neuropixels 1.0 Probe
  Group /general/devices/probeF (EcephysProbe) Neuropixels 1.0 Probe
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering, including the filter name and frequency cutoffs | shape = (2304,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (2304,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (2304,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (2304,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the electrode, in ohms | shape = (2304,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (2304,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/probe_channel_number (VectorData) The local index of electrode/channel on device | shape = (2304,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/probe_horizontal_position (VectorData) Width-wise position of electrode/channel on device (microns) | shape = (2304,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/probe_id (VectorData) The unique id of this electrode's/channel's device | shape = (2304,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/probe_vertical_position (VectorData) Length-wise position of electrode/channel on device (microns) | shape = (2304,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/valid_data (VectorData) Whether data from this electrode/channel is usable | shape = (2304,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the position (+x is posterior) | shape = (2304,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the position (+y is inferior) | shape = (2304,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the position (+z is right) | shape = (2304,) | dtype = float64
  Group /general/extracellular_ephys/probeA (EcephysElectrodeGroup) Ecephys Electrode Group
  Group /general/extracellular_ephys/probeA/device (EcephysProbe) Neuropixels 1.0 Probe
  Group /general/extracellular_ephys/probeB (EcephysElectrodeGroup) Ecephys Electrode Group
  Group /general/extracellular_ephys/probeB/device (EcephysProbe) Neuropixels 1.0 Probe
  Group /general/extracellular_ephys/probeC (EcephysElectrodeGroup) Ecephys Electrode Group
  Group /general/extracellular_ephys/probeC/device (EcephysProbe) Neuropixels 1.0 Probe
  Group /general/extracellular_ephys/probeD (EcephysElectrodeGroup) Ecephys Electrode Group
  Group /general/extracellular_ephys/probeD/device (EcephysProbe) Neuropixels 1.0 Probe
  Group /general/extracellular_ephys/probeE (EcephysElectrodeGroup) Ecephys Electrode Group
  Group /general/extracellular_ephys/probeE/device (EcephysProbe) Neuropixels 1.0 Probe
  Group /general/extracellular_ephys/probeF (EcephysElectrodeGroup) Ecephys Electrode Group
  Group /general/extracellular_ephys/probeF/device (EcephysProbe) Neuropixels 1.0 Probe
  institution: Allen Institute for Brain Science
  keywords: ['visual' 'behavior' 'task']
  Group /general/metadata (BehaviorMetadata) 
  Group /general/subject (BehaviorSubject) 
  Group /general/task_parameters (BehaviorTaskParameters) 
  identifier: 1173189336
  Group /intervals/dynamic_routing_image_set_presentations (TimeIntervals) Presentation times and stimuli details for 'dynamic_routing_image_set' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/dynamic_routing_image_set_presentations/active (VectorData) No description | shape = (5206,) | dtype = bool
  Dataset /intervals/dynamic_routing_image_set_presentations/duration (VectorData) No description | shape = (5206,) | dtype = float64
  Dataset /intervals/dynamic_routing_image_set_presentations/end_frame (VectorData) No description | shape = (5206,) | dtype = int32
  Dataset /intervals/dynamic_routing_image_set_presentations/flashes_since_change (VectorData) No description | shape = (5206,) | dtype = float64
  Dataset /intervals/dynamic_routing_image_set_presentations/id (ElementIdentifiers)  | shape = (5206,) | dtype = int32
  Dataset /intervals/dynamic_routing_image_set_presentations/image_name (VectorData) No description | shape = (5206,) | dtype = object
  Dataset /intervals/dynamic_routing_image_set_presentations/is_change (VectorData) No description | shape = (5206,) | dtype = bool
  Dataset /intervals/dynamic_routing_image_set_presentations/is_image_novel (VectorData) No description | shape = (5206,) | dtype = bool
  Dataset /intervals/dynamic_routing_image_set_presentations/omitted (VectorData) No description | shape = (5206,) | dtype = bool
  Dataset /intervals/dynamic_routing_image_set_presentations/rewarded (VectorData) No description | shape = (5206,) | dtype = bool
  Dataset /intervals/dynamic_routing_image_set_presentations/start_frame (VectorData) No description | shape = (5206,) | dtype = int32
  Dataset /intervals/dynamic_routing_image_set_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (5206,) | dtype = float64
  Dataset /intervals/dynamic_routing_image_set_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (5206,) | dtype = int32
  Dataset /intervals/dynamic_routing_image_set_presentations/stimulus_name (VectorData) Name of stimulus | shape = (5206,) | dtype = object
  Dataset /intervals/dynamic_routing_image_set_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (5206,) | dtype = float64
  Dataset /intervals/dynamic_routing_image_set_presentations/tags (VectorData) user-defined tags | shape = (5206,) | dtype = object
  Dataset /intervals/dynamic_routing_image_set_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (5206,) | dtype = uint16
  Dataset /intervals/dynamic_routing_image_set_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (5206,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/dynamic_routing_image_set_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (5206,) | dtype = uint16
  Group /intervals/flash_250ms_presentations (TimeIntervals) Presentation times and stimuli details for 'C:/ProgramData/StimulusFiles/dev/flash_250ms' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/flash_250ms_presentations/active (VectorData) No description | shape = (150,) | dtype = bool
  Dataset /intervals/flash_250ms_presentations/color (VectorData) No description | shape = (150,) | dtype = float64
  Dataset /intervals/flash_250ms_presentations/contrast (VectorData) Contrast of stimulus | shape = (150,) | dtype = float64
  Dataset /intervals/flash_250ms_presentations/duration (VectorData) No description | shape = (150,) | dtype = float64
  Dataset /intervals/flash_250ms_presentations/end_frame (VectorData) No description | shape = (150,) | dtype = int32
  Dataset /intervals/flash_250ms_presentations/id (ElementIdentifiers)  | shape = (150,) | dtype = int32
  Dataset /intervals/flash_250ms_presentations/is_change (VectorData) No description | shape = (150,) | dtype = bool
  Dataset /intervals/flash_250ms_presentations/is_image_novel (VectorData) No description | shape = (150,) | dtype = bool
  Dataset /intervals/flash_250ms_presentations/omitted (VectorData) No description | shape = (150,) | dtype = bool
  Dataset /intervals/flash_250ms_presentations/rewarded (VectorData) No description | shape = (150,) | dtype = bool
  Dataset /intervals/flash_250ms_presentations/start_frame (VectorData) No description | shape = (150,) | dtype = int32
  Dataset /intervals/flash_250ms_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (150,) | dtype = float64
  Dataset /intervals/flash_250ms_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (150,) | dtype = int32
  Dataset /intervals/flash_250ms_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (150,) | dtype = float64
  Dataset /intervals/flash_250ms_presentations/stimulus_name (VectorData) Name of stimulus | shape = (150,) | dtype = object
  Dataset /intervals/flash_250ms_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (150,) | dtype = float64
  Dataset /intervals/flash_250ms_presentations/tags (VectorData) user-defined tags | shape = (150,) | dtype = object
  Dataset /intervals/flash_250ms_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (150,) | dtype = uint8
  Dataset /intervals/flash_250ms_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (150,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/flash_250ms_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (150,) | dtype = uint8
  Group /intervals/gabor_20_deg_250ms_presentations (TimeIntervals) Presentation times and stimuli details for 'C:/ProgramData/StimulusFiles/dev/gabor_20_deg_250ms' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/gabor_20_deg_250ms_presentations/active (VectorData) No description | shape = (3645,) | dtype = bool
  Dataset /intervals/gabor_20_deg_250ms_presentations/contrast (VectorData) Contrast of stimulus | shape = (3645,) | dtype = float64
  Dataset /intervals/gabor_20_deg_250ms_presentations/duration (VectorData) No description | shape = (3645,) | dtype = float64
  Dataset /intervals/gabor_20_deg_250ms_presentations/end_frame (VectorData) No description | shape = (3645,) | dtype = int32
  Dataset /intervals/gabor_20_deg_250ms_presentations/id (ElementIdentifiers)  | shape = (3645,) | dtype = int32
  Dataset /intervals/gabor_20_deg_250ms_presentations/is_change (VectorData) No description | shape = (3645,) | dtype = bool
  Dataset /intervals/gabor_20_deg_250ms_presentations/is_image_novel (VectorData) No description | shape = (3645,) | dtype = bool
  Dataset /intervals/gabor_20_deg_250ms_presentations/omitted (VectorData) No description | shape = (3645,) | dtype = bool
  Dataset /intervals/gabor_20_deg_250ms_presentations/orientation (VectorData) Orientation of stimulus | shape = (3645,) | dtype = float64
  Dataset /intervals/gabor_20_deg_250ms_presentations/position_x (VectorData) No description | shape = (3645,) | dtype = float64
  Dataset /intervals/gabor_20_deg_250ms_presentations/position_y (VectorData) No description | shape = (3645,) | dtype = float64
  Dataset /intervals/gabor_20_deg_250ms_presentations/rewarded (VectorData) No description | shape = (3645,) | dtype = bool
  Dataset /intervals/gabor_20_deg_250ms_presentations/spatial_frequency (VectorData) Spatial frequency of stimulus | shape = (3645,) | dtype = float64
  Dataset /intervals/gabor_20_deg_250ms_presentations/start_frame (VectorData) No description | shape = (3645,) | dtype = int32
  Dataset /intervals/gabor_20_deg_250ms_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (3645,) | dtype = float64
  Dataset /intervals/gabor_20_deg_250ms_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (3645,) | dtype = int32
  Dataset /intervals/gabor_20_deg_250ms_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (3645,) | dtype = float64
  Dataset /intervals/gabor_20_deg_250ms_presentations/stimulus_name (VectorData) Name of stimulus | shape = (3645,) | dtype = object
  Dataset /intervals/gabor_20_deg_250ms_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (3645,) | dtype = float64
  Dataset /intervals/gabor_20_deg_250ms_presentations/tags (VectorData) user-defined tags | shape = (3645,) | dtype = object
  Dataset /intervals/gabor_20_deg_250ms_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (3645,) | dtype = uint16
  Dataset /intervals/gabor_20_deg_250ms_presentations/temporal_frequency (VectorData) Temporal frequency of stimulus | shape = (3645,) | dtype = float64
  Dataset /intervals/gabor_20_deg_250ms_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (3645,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/gabor_20_deg_250ms_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (3645,) | dtype = uint16
  Group /intervals/spontaneous_presentations (TimeIntervals) Presentation times and stimuli details for 'spontaneous' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/spontaneous_presentations/active (VectorData) No description | shape = (2,) | dtype = bool
  Dataset /intervals/spontaneous_presentations/duration (VectorData) No description | shape = (2,) | dtype = float64
  Dataset /intervals/spontaneous_presentations/end_frame (VectorData) No description | shape = (2,) | dtype = int32
  Dataset /intervals/spontaneous_presentations/id (ElementIdentifiers)  | shape = (2,) | dtype = int32
  Dataset /intervals/spontaneous_presentations/is_change (VectorData) No description | shape = (2,) | dtype = bool
  Dataset /intervals/spontaneous_presentations/is_image_novel (VectorData) No description | shape = (2,) | dtype = bool
  Dataset /intervals/spontaneous_presentations/omitted (VectorData) No description | shape = (2,) | dtype = bool
  Dataset /intervals/spontaneous_presentations/rewarded (VectorData) No description | shape = (2,) | dtype = bool
  Dataset /intervals/spontaneous_presentations/start_frame (VectorData) No description | shape = (2,) | dtype = int32
  Dataset /intervals/spontaneous_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (2,) | dtype = float64
  Dataset /intervals/spontaneous_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (2,) | dtype = int32
  Dataset /intervals/spontaneous_presentations/stimulus_name (VectorData) Name of stimulus | shape = (2,) | dtype = object
  Dataset /intervals/spontaneous_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (2,) | dtype = float64
  Dataset /intervals/spontaneous_presentations/tags (VectorData) user-defined tags | shape = (2,) | dtype = object
  Dataset /intervals/spontaneous_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (2,) | dtype = uint8
  Dataset /intervals/spontaneous_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (2,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/spontaneous_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (2,) | dtype = uint8
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/aborted (VectorData) NOT IMPLEMENTED: aborted | shape = (798,) | dtype = bool
  Dataset /intervals/trials/auto_rewarded (VectorData) NOT IMPLEMENTED: auto_rewarded | shape = (798,) | dtype = bool
  Dataset /intervals/trials/catch (VectorData) NOT IMPLEMENTED: catch | shape = (798,) | dtype = bool
  Dataset /intervals/trials/change_frame (VectorData) NOT IMPLEMENTED: change_frame | shape = (798,) | dtype = float64
  Dataset /intervals/trials/change_image_name (VectorData) NOT IMPLEMENTED: change_image_name | shape = (798,) | dtype = object
  Dataset /intervals/trials/change_time (VectorData) NOT IMPLEMENTED: change_time | shape = (798,) | dtype = float64
  Dataset /intervals/trials/correct_reject (VectorData) NOT IMPLEMENTED: correct_reject | shape = (798,) | dtype = bool
  Dataset /intervals/trials/false_alarm (VectorData) NOT IMPLEMENTED: false_alarm | shape = (798,) | dtype = bool
  Dataset /intervals/trials/go (VectorData) NOT IMPLEMENTED: go | shape = (798,) | dtype = bool
  Dataset /intervals/trials/hit (VectorData) NOT IMPLEMENTED: hit | shape = (798,) | dtype = bool
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (798,) | dtype = int32
  Dataset /intervals/trials/initial_image_name (VectorData) NOT IMPLEMENTED: initial_image_name | shape = (798,) | dtype = object
  Dataset /intervals/trials/is_change (VectorData) NOT IMPLEMENTED: is_change | shape = (798,) | dtype = bool
  Dataset /intervals/trials/is_sham_change (VectorData) NOT IMPLEMENTED: is_sham_change | shape = (798,) | dtype = bool
  Dataset /intervals/trials/lick_times (VectorData) NOT IMPLEMENTED: lick_times | shape = (2607,) | dtype = float64
  Dataset /intervals/trials/lick_times_index (VectorIndex) Index for VectorData 'lick_times' | shape = (798,) | dtype = uint16
  Dataset /intervals/trials/miss (VectorData) NOT IMPLEMENTED: miss | shape = (798,) | dtype = bool
  Dataset /intervals/trials/no_reward_epoch (VectorData) NOT IMPLEMENTED: no_reward_epoch | shape = (798,) | dtype = bool
  Dataset /intervals/trials/omitted_reward (VectorData) NOT IMPLEMENTED: omitted_reward | shape = (798,) | dtype = bool
  Dataset /intervals/trials/response_latency (VectorData) NOT IMPLEMENTED: response_latency | shape = (798,) | dtype = float64
  Dataset /intervals/trials/response_time (VectorData) NOT IMPLEMENTED: response_time | shape = (798,) | dtype = float64
  Dataset /intervals/trials/reward_time (VectorData) NOT IMPLEMENTED: reward_time | shape = (798,) | dtype = float64
  Dataset /intervals/trials/reward_volume (VectorData) NOT IMPLEMENTED: reward_volume | shape = (798,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (798,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (798,) | dtype = float64
  Dataset /intervals/trials/trial_length (VectorData) NOT IMPLEMENTED: trial_length | shape = (798,) | dtype = float64
  Group /processing/eye_tracking_rig_metadata (ProcessingModule) Eye tracking rig metadata module
  Group /processing/eye_tracking_rig_metadata/eye_tracking_rig_metadata (OphysEyeTrackingRigMetadata) 
  Group /processing/licking (ProcessingModule) Licking behavior processing module
  Group /processing/licking/licks (TimeSeries) Timestamps and stimulus presentation frame indices for lick events
  Group /processing/optotagging (ProcessingModule) optogenetic stimulution data
  Group /processing/optotagging/optogenetic_stimulation (TimeIntervals) 
  Dataset /processing/optotagging/optogenetic_stimulation/condition (VectorData) no description | shape = (300,) | dtype = object
  Dataset /processing/optotagging/optogenetic_stimulation/duration (VectorData) no description | shape = (300,) | dtype = float64
  Dataset /processing/optotagging/optogenetic_stimulation/id (ElementIdentifiers)  | shape = (300,) | dtype = int32
  Dataset /processing/optotagging/optogenetic_stimulation/level (VectorData) no description | shape = (300,) | dtype = float64
  Dataset /processing/optotagging/optogenetic_stimulation/start_time (VectorData) Start time of epoch, in seconds | shape = (300,) | dtype = float64
  Dataset /processing/optotagging/optogenetic_stimulation/stimulus_name (VectorData) no description | shape = (300,) | dtype = object
  Dataset /processing/optotagging/optogenetic_stimulation/stop_time (VectorData) Stop time of epoch, in seconds | shape = (300,) | dtype = float64
  Dataset /processing/optotagging/optogenetic_stimulation/tags (VectorData) user-defined tags | shape = (300,) | dtype = object
  Dataset /processing/optotagging/optogenetic_stimulation/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (300,) | dtype = uint16
  Dataset /processing/optotagging/optogenetic_stimulation/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (300,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /processing/optotagging/optogenetic_stimulation/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (300,) | dtype = uint16
  Group /processing/optotagging/optotagging (TimeSeries) no description
  Group /processing/rewards (ProcessingModule) Licking behavior processing module
  Group /processing/rewards/autorewarded (TimeSeries) no description
  Group /processing/rewards/volume (TimeSeries) no description
  Group /processing/running (ProcessingModule) Running speed processing module
  Group /processing/running/dx (TimeSeries) Running wheel angular change, computed during data collection
  Group /processing/running/speed (TimeSeries) no description
  Group /processing/running/speed_unfiltered (TimeSeries) no description
  Group /processing/stimulus (ProcessingModule) Stimulus Times processing
  Group /processing/stimulus/timestamps (TimeSeries) no description
  session_description: EPHYS_2
  session_start_time: 2022-04-27T04:10:46+00:00
  Group /stimulus/templates/dynamic_routing_image_set (StimulusTemplate) no description
  timestamps_reference_time: 2022-04-27T04:10:46+00:00
  Group /units (Units) 
  Dataset /units/PT_ratio (VectorData) no description | shape = (1758,) | dtype = float64
  Dataset /units/amplitude (VectorData) no description | shape = (1758,) | dtype = float64
  Dataset /units/amplitude_cutoff (VectorData) no description | shape = (1758,) | dtype = float64
  Dataset /units/cluster_id (VectorData) no description | shape = (1758,) | dtype = int64
  Dataset /units/cumulative_drift (VectorData) no description | shape = (1758,) | dtype = float64
  Dataset /units/d_prime (VectorData) no description | shape = (1758,) | dtype = float64
  Dataset /units/firing_rate (VectorData) no description | shape = (1758,) | dtype = float64
  Dataset /units/id (ElementIdentifiers)  | shape = (1758,) | dtype = int32
  Dataset /units/isi_label (VectorData) no description | shape = (1758,) | dtype = object
  Dataset /units/isi_violations (VectorData) no description | shape = (1758,) | dtype = float64
  Dataset /units/isolation_distance (VectorData) no description | shape = (1758,) | dtype = float64
  Dataset /units/l_ratio (VectorData) no description | shape = (1758,) | dtype = float64
  Dataset /units/local_index (VectorData) no description | shape = (1758,) | dtype = int64
  Dataset /units/max_drift (VectorData) no description | shape = (1758,) | dtype = float64
  Dataset /units/nn_hit_rate (VectorData) no description | shape = (1758,) | dtype = float64
  Dataset /units/nn_miss_rate (VectorData) no description | shape = (1758,) | dtype = float64
  Dataset /units/peak_channel_id (VectorData) no description | shape = (1758,) | dtype = int64
  Dataset /units/presence_ratio (VectorData) no description | shape = (1758,) | dtype = float64
  Dataset /units/quality (VectorData) no description | shape = (1758,) | dtype = object
  Dataset /units/recovery_slope (VectorData) no description | shape = (1758,) | dtype = float64
  Dataset /units/repolarization_slope (VectorData) no description | shape = (1758,) | dtype = float64
  Dataset /units/silhouette_score (VectorData) no description | shape = (1758,) | dtype = float64
  Dataset /units/snr (VectorData) no description | shape = (1758,) | dtype = float64
  Dataset /units/spike_amplitudes (VectorData) amplitude (s) of detected spiking events | shape = (57954457,) | dtype = float64
  Dataset /units/spike_amplitudes_index (VectorIndex) Index for VectorData 'spike_amplitudes' | shape = (1758,) | dtype = uint32
  Dataset /units/spike_times (VectorData) times (s) of detected spiking events | shape = (57954457,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (1758,) | dtype = uint32
  Dataset /units/spread (VectorData) no description | shape = (1758,) | dtype = float64
  Dataset /units/structure_layer (VectorData) no description | shape = (1758,) | dtype = object
  Dataset /units/velocity_above (VectorData) no description | shape = (1758,) | dtype = float64
  Dataset /units/velocity_below (VectorData) no description | shape = (1758,) | dtype = float64
  Dataset /units/waveform_duration (VectorData) no description | shape = (1758,) | dtype = float64
  Dataset /units/waveform_mean (VectorData) mean waveforms on peak channels (over samples) | shape = (675072, 82) | dtype = float64
  Dataset /units/waveform_mean_index (VectorIndex) Index for VectorData 'waveform_mean' | shape = (1758,) | dtype = uint32


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/EyeTracking (EllipseEyeTracking) 
  Group /acquisition/EyeTracking/corneal_reflection_tracking (EllipseSeries) no description
  Group /acquisition/EyeTracking/eye_tracking (EllipseSeries) no description
  Group /acquisition/EyeTracking/likely_blink (TimeSeries) blinks
  Group /acquisition/EyeTracking/pupil_tracking (EllipseSeries) no description
  Group /acquisition/v_in (TimeSeries) The theoretical maximum voltage that the running wheel encoder will reach prior to "wrapping". This should theoretically be 5V (after crossing 5V goes to 0V, or vice versa). In practice the encoder does not always reach this value before wrapping, which can cause transient spikes in speed at the voltage "wraps".
  Group /acquisition/v_sig (TimeSeries) Voltage signal from the running wheel encoder
  file_create_date: ['2024-05-28T17:50:38.409186+00:00']
  Group /general/devices/NP.1 (Device) Allen Brain Observatory - Scientifica 2P Rig
  Group /general/devices/probeA (EcephysProbe) Neuropixels 1.0 Probe
  Group /general/devices/probeB (EcephysProbe) Neuropixels 1.0 Probe
  Group /general/devices/probeC (EcephysProbe) Neuropixels 1.0 Probe
  Group /general/devices/probeD (EcephysProbe) Neuropixels 1.0 Probe
  Group /general/devices/probeE (EcephysProbe) Neuropixels 1.0 Probe
  Group /general/devices/probeF (EcephysProbe) Neuropixels 1.0 Probe
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering, including the filter name and frequency cutoffs | shape = (2304,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (2304,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (2304,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (2304,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the electrode, in ohms | shape = (2304,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (2304,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/probe_channel_number (VectorData) The local index of electrode/channel on device | shape = (2304,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/probe_horizontal_position (VectorData) Width-wise position of electrode/channel on device (microns) | shape = (2304,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/probe_id (VectorData) The unique id of this electrode's/channel's device | shape = (2304,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/probe_vertical_position (VectorData) Length-wise position of electrode/channel on device (microns) | shape = (2304,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/valid_data (VectorData) Whether data from this electrode/channel is usable | shape = (2304,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the position (+x is posterior) | shape = (2304,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the position (+y is inferior) | shape = (2304,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the position (+z is right) | shape = (2304,) | dtype = float64
  Group /general/extracellular_ephys/probeA (EcephysElectrodeGroup) Ecephys Electrode Group
  Group /general/extracellular_ephys/probeA/device (EcephysProbe) Neuropixels 1.0 Probe
  Group /general/extracellular_ephys/probeB (EcephysElectrodeGroup) Ecephys Electrode Group
  Group /general/extracellular_ephys/probeB/device (EcephysProbe) Neuropixels 1.0 Probe
  Group /general/extracellular_ephys/probeC (EcephysElectrodeGroup) Ecephys Electrode Group
  Group /general/extracellular_ephys/probeC/device (EcephysProbe) Neuropixels 1.0 Probe
  Group /general/extracellular_ephys/probeD (EcephysElectrodeGroup) Ecephys Electrode Group
  Group /general/extracellular_ephys/probeD/device (EcephysProbe) Neuropixels 1.0 Probe
  Group /general/extracellular_ephys/probeE (EcephysElectrodeGroup) Ecephys Electrode Group
  Group /general/extracellular_ephys/probeE/device (EcephysProbe) Neuropixels 1.0 Probe
  Group /general/extracellular_ephys/probeF (EcephysElectrodeGroup) Ecephys Electrode Group
  Group /general/extracellular_ephys/probeF/device (EcephysProbe) Neuropixels 1.0 Probe
  institution: Allen Institute for Brain Science
  keywords: ['visual' 'behavior' 'task']
  Group /general/metadata (BehaviorMetadata) 
  Group /general/subject (BehaviorSubject) 
  Group /general/task_parameters (BehaviorTaskParameters) 
  identifier: 1182427414
  Group /intervals/dynamic_routing_image_set_presentations (TimeIntervals) Presentation times and stimuli details for 'dynamic_routing_image_set' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/dynamic_routing_image_set_presentations/active (VectorData) No description | shape = (5200,) | dtype = bool
  Dataset /intervals/dynamic_routing_image_set_presentations/duration (VectorData) No description | shape = (5200,) | dtype = float64
  Dataset /intervals/dynamic_routing_image_set_presentations/end_frame (VectorData) No description | shape = (5200,) | dtype = int32
  Dataset /intervals/dynamic_routing_image_set_presentations/flashes_since_change (VectorData) No description | shape = (5200,) | dtype = float64
  Dataset /intervals/dynamic_routing_image_set_presentations/id (ElementIdentifiers)  | shape = (5200,) | dtype = int32
  Dataset /intervals/dynamic_routing_image_set_presentations/image_name (VectorData) No description | shape = (5200,) | dtype = object
  Dataset /intervals/dynamic_routing_image_set_presentations/is_change (VectorData) No description | shape = (5200,) | dtype = bool
  Dataset /intervals/dynamic_routing_image_set_presentations/is_image_novel (VectorData) No description | shape = (5200,) | dtype = bool
  Dataset /intervals/dynamic_routing_image_set_presentations/omitted (VectorData) No description | shape = (5200,) | dtype = bool
  Dataset /intervals/dynamic_routing_image_set_presentations/rewarded (VectorData) No description | shape = (5200,) | dtype = bool
  Dataset /intervals/dynamic_routing_image_set_presentations/start_frame (VectorData) No description | shape = (5200,) | dtype = int32
  Dataset /intervals/dynamic_routing_image_set_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (5200,) | dtype = float64
  Dataset /intervals/dynamic_routing_image_set_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (5200,) | dtype = int32
  Dataset /intervals/dynamic_routing_image_set_presentations/stimulus_name (VectorData) Name of stimulus | shape = (5200,) | dtype = object
  Dataset /intervals/dynamic_routing_image_set_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (5200,) | dtype = float64
  Dataset /intervals/dynamic_routing_image_set_presentations/tags (VectorData) user-defined tags | shape = (5200,) | dtype = object
  Dataset /intervals/dynamic_routing_image_set_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (5200,) | dtype = uint16
  Dataset /intervals/dynamic_routing_image_set_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (5200,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/dynamic_routing_image_set_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (5200,) | dtype = uint16
  Group /intervals/flash_250ms_presentations (TimeIntervals) Presentation times and stimuli details for 'C:/ProgramData/StimulusFiles/dev/flash_250ms' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/flash_250ms_presentations/active (VectorData) No description | shape = (150,) | dtype = bool
  Dataset /intervals/flash_250ms_presentations/color (VectorData) No description | shape = (150,) | dtype = float64
  Dataset /intervals/flash_250ms_presentations/contrast (VectorData) Contrast of stimulus | shape = (150,) | dtype = float64
  Dataset /intervals/flash_250ms_presentations/duration (VectorData) No description | shape = (150,) | dtype = float64
  Dataset /intervals/flash_250ms_presentations/end_frame (VectorData) No description | shape = (150,) | dtype = int32
  Dataset /intervals/flash_250ms_presentations/id (ElementIdentifiers)  | shape = (150,) | dtype = int32
  Dataset /intervals/flash_250ms_presentations/is_change (VectorData) No description | shape = (150,) | dtype = bool
  Dataset /intervals/flash_250ms_presentations/is_image_novel (VectorData) No description | shape = (150,) | dtype = bool
  Dataset /intervals/flash_250ms_presentations/omitted (VectorData) No description | shape = (150,) | dtype = bool
  Dataset /intervals/flash_250ms_presentations/rewarded (VectorData) No description | shape = (150,) | dtype = bool
  Dataset /intervals/flash_250ms_presentations/start_frame (VectorData) No description | shape = (150,) | dtype = int32
  Dataset /intervals/flash_250ms_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (150,) | dtype = float64
  Dataset /intervals/flash_250ms_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (150,) | dtype = int32
  Dataset /intervals/flash_250ms_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (150,) | dtype = float64
  Dataset /intervals/flash_250ms_presentations/stimulus_name (VectorData) Name of stimulus | shape = (150,) | dtype = object
  Dataset /intervals/flash_250ms_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (150,) | dtype = float64
  Dataset /intervals/flash_250ms_presentations/tags (VectorData) user-defined tags | shape = (150,) | dtype = object
  Dataset /intervals/flash_250ms_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (150,) | dtype = uint8
  Dataset /intervals/flash_250ms_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (150,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/flash_250ms_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (150,) | dtype = uint8
  Group /intervals/gabor_20_deg_250ms_presentations (TimeIntervals) Presentation times and stimuli details for 'C:/ProgramData/StimulusFiles/dev/gabor_20_deg_250ms' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/gabor_20_deg_250ms_presentations/active (VectorData) No description | shape = (3645,) | dtype = bool
  Dataset /intervals/gabor_20_deg_250ms_presentations/contrast (VectorData) Contrast of stimulus | shape = (3645,) | dtype = float64
  Dataset /intervals/gabor_20_deg_250ms_presentations/duration (VectorData) No description | shape = (3645,) | dtype = float64
  Dataset /intervals/gabor_20_deg_250ms_presentations/end_frame (VectorData) No description | shape = (3645,) | dtype = int32
  Dataset /intervals/gabor_20_deg_250ms_presentations/id (ElementIdentifiers)  | shape = (3645,) | dtype = int32
  Dataset /intervals/gabor_20_deg_250ms_presentations/is_change (VectorData) No description | shape = (3645,) | dtype = bool
  Dataset /intervals/gabor_20_deg_250ms_presentations/is_image_novel (VectorData) No description | shape = (3645,) | dtype = bool
  Dataset /intervals/gabor_20_deg_250ms_presentations/omitted (VectorData) No description | shape = (3645,) | dtype = bool
  Dataset /intervals/gabor_20_deg_250ms_presentations/orientation (VectorData) Orientation of stimulus | shape = (3645,) | dtype = float64
  Dataset /intervals/gabor_20_deg_250ms_presentations/position_x (VectorData) No description | shape = (3645,) | dtype = float64
  Dataset /intervals/gabor_20_deg_250ms_presentations/position_y (VectorData) No description | shape = (3645,) | dtype = float64
  Dataset /intervals/gabor_20_deg_250ms_presentations/rewarded (VectorData) No description | shape = (3645,) | dtype = bool
  Dataset /intervals/gabor_20_deg_250ms_presentations/spatial_frequency (VectorData) Spatial frequency of stimulus | shape = (3645,) | dtype = float64
  Dataset /intervals/gabor_20_deg_250ms_presentations/start_frame (VectorData) No description | shape = (3645,) | dtype = int32
  Dataset /intervals/gabor_20_deg_250ms_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (3645,) | dtype = float64
  Dataset /intervals/gabor_20_deg_250ms_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (3645,) | dtype = int32
  Dataset /intervals/gabor_20_deg_250ms_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (3645,) | dtype = float64
  Dataset /intervals/gabor_20_deg_250ms_presentations/stimulus_name (VectorData) Name of stimulus | shape = (3645,) | dtype = object
  Dataset /intervals/gabor_20_deg_250ms_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (3645,) | dtype = float64
  Dataset /intervals/gabor_20_deg_250ms_presentations/tags (VectorData) user-defined tags | shape = (3645,) | dtype = object
  Dataset /intervals/gabor_20_deg_250ms_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (3645,) | dtype = uint16
  Dataset /intervals/gabor_20_deg_250ms_presentations/temporal_frequency (VectorData) Temporal frequency of stimulus | shape = (3645,) | dtype = float64
  Dataset /intervals/gabor_20_deg_250ms_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (3645,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/gabor_20_deg_250ms_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (3645,) | dtype = uint16
  Group /intervals/spontaneous_presentations (TimeIntervals) Presentation times and stimuli details for 'spontaneous' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/spontaneous_presentations/active (VectorData) No description | shape = (2,) | dtype = bool
  Dataset /intervals/spontaneous_presentations/duration (VectorData) No description | shape = (2,) | dtype = float64
  Dataset /intervals/spontaneous_presentations/end_frame (VectorData) No description | shape = (2,) | dtype = int32
  Dataset /intervals/spontaneous_presentations/id (ElementIdentifiers)  | shape = (2,) | dtype = int32
  Dataset /intervals/spontaneous_presentations/is_change (VectorData) No description | shape = (2,) | dtype = bool
  Dataset /intervals/spontaneous_presentations/is_image_novel (VectorData) No description | shape = (2,) | dtype = bool
  Dataset /intervals/spontaneous_presentations/omitted (VectorData) No description | shape = (2,) | dtype = bool
  Dataset /intervals/spontaneous_presentations/rewarded (VectorData) No description | shape = (2,) | dtype = bool
  Dataset /intervals/spontaneous_presentations/start_frame (VectorData) No description | shape = (2,) | dtype = int32
  Dataset /intervals/spontaneous_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (2,) | dtype = float64
  Dataset /intervals/spontaneous_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (2,) | dtype = int32
  Dataset /intervals/spontaneous_presentations/stimulus_name (VectorData) Name of stimulus | shape = (2,) | dtype = object
  Dataset /intervals/spontaneous_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (2,) | dtype = float64
  Dataset /intervals/spontaneous_presentations/tags (VectorData) user-defined tags | shape = (2,) | dtype = object
  Dataset /intervals/spontaneous_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (2,) | dtype = uint8
  Dataset /intervals/spontaneous_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (2,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/spontaneous_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (2,) | dtype = uint8
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/aborted (VectorData) NOT IMPLEMENTED: aborted | shape = (612,) | dtype = bool
  Dataset /intervals/trials/auto_rewarded (VectorData) NOT IMPLEMENTED: auto_rewarded | shape = (612,) | dtype = bool
  Dataset /intervals/trials/catch (VectorData) NOT IMPLEMENTED: catch | shape = (612,) | dtype = bool
  Dataset /intervals/trials/change_frame (VectorData) NOT IMPLEMENTED: change_frame | shape = (612,) | dtype = float64
  Dataset /intervals/trials/change_image_name (VectorData) NOT IMPLEMENTED: change_image_name | shape = (612,) | dtype = object
  Dataset /intervals/trials/change_time (VectorData) NOT IMPLEMENTED: change_time | shape = (612,) | dtype = float64
  Dataset /intervals/trials/correct_reject (VectorData) NOT IMPLEMENTED: correct_reject | shape = (612,) | dtype = bool
  Dataset /intervals/trials/false_alarm (VectorData) NOT IMPLEMENTED: false_alarm | shape = (612,) | dtype = bool
  Dataset /intervals/trials/go (VectorData) NOT IMPLEMENTED: go | shape = (612,) | dtype = bool
  Dataset /intervals/trials/hit (VectorData) NOT IMPLEMENTED: hit | shape = (612,) | dtype = bool
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (612,) | dtype = int32
  Dataset /intervals/trials/initial_image_name (VectorData) NOT IMPLEMENTED: initial_image_name | shape = (612,) | dtype = object
  Dataset /intervals/trials/is_change (VectorData) NOT IMPLEMENTED: is_change | shape = (612,) | dtype = bool
  Dataset /intervals/trials/lick_times (VectorData) NOT IMPLEMENTED: lick_times | shape = (989,) | dtype = float64
  Dataset /intervals/trials/lick_times_index (VectorIndex) Index for VectorData 'lick_times' | shape = (612,) | dtype = uint16
  Dataset /intervals/trials/miss (VectorData) NOT IMPLEMENTED: miss | shape = (612,) | dtype = bool
  Dataset /intervals/trials/response_latency (VectorData) NOT IMPLEMENTED: response_latency | shape = (612,) | dtype = float64
  Dataset /intervals/trials/response_time (VectorData) NOT IMPLEMENTED: response_time | shape = (612,) | dtype = float64
  Dataset /intervals/trials/reward_time (VectorData) NOT IMPLEMENTED: reward_time | shape = (612,) | dtype = float64
  Dataset /intervals/trials/reward_volume (VectorData) NOT IMPLEMENTED: reward_volume | shape = (612,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (612,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (612,) | dtype = float64
  Dataset /intervals/trials/trial_length (VectorData) NOT IMPLEMENTED: trial_length | shape = (612,) | dtype = float64
  Group /processing/eye_tracking_rig_metadata (ProcessingModule) Eye tracking rig metadata module
  Group /processing/eye_tracking_rig_metadata/eye_tracking_rig_metadata (OphysEyeTrackingRigMetadata) 
  Group /processing/licking (ProcessingModule) Licking behavior processing module
  Group /processing/licking/licks (TimeSeries) Timestamps and stimulus presentation frame indices for lick events
  Group /processing/optotagging (ProcessingModule) optogenetic stimulution data
  Group /processing/optotagging/optogenetic_stimulation (TimeIntervals) 
  Dataset /processing/optotagging/optogenetic_stimulation/condition (VectorData) no description | shape = (300,) | dtype = object
  Dataset /processing/optotagging/optogenetic_stimulation/duration (VectorData) no description | shape = (300,) | dtype = float64
  Dataset /processing/optotagging/optogenetic_stimulation/id (ElementIdentifiers)  | shape = (300,) | dtype = int32
  Dataset /processing/optotagging/optogenetic_stimulation/level (VectorData) no description | shape = (300,) | dtype = float64
  Dataset /processing/optotagging/optogenetic_stimulation/start_time (VectorData) Start time of epoch, in seconds | shape = (300,) | dtype = float64
  Dataset /processing/optotagging/optogenetic_stimulation/stimulus_name (VectorData) no description | shape = (300,) | dtype = object
  Dataset /processing/optotagging/optogenetic_stimulation/stop_time (VectorData) Stop time of epoch, in seconds | shape = (300,) | dtype = float64
  Dataset /processing/optotagging/optogenetic_stimulation/tags (VectorData) user-defined tags | shape = (300,) | dtype = object
  Dataset /processing/optotagging/optogenetic_stimulation/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (300,) | dtype = uint16
  Dataset /processing/optotagging/optogenetic_stimulation/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (300,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /processing/optotagging/optogenetic_stimulation/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (300,) | dtype = uint16
  Group /processing/optotagging/optotagging (TimeSeries) no description
  Group /processing/rewards (ProcessingModule) Licking behavior processing module
  Group /processing/rewards/autorewarded (TimeSeries) no description
  Group /processing/rewards/volume (TimeSeries) no description
  Group /processing/running (ProcessingModule) Running speed processing module
  Group /processing/running/dx (TimeSeries) Running wheel angular change, computed during data collection
  Group /processing/running/speed (TimeSeries) no description
  Group /processing/running/speed_unfiltered (TimeSeries) no description
  Group /processing/stimulus (ProcessingModule) Stimulus Times processing
  Group /processing/stimulus/timestamps (TimeSeries) no description
  session_description: EPHYS_1
  session_start_time: 2022-06-06T22:35:05.429000+00:00
  Group /stimulus/templates/dynamic_routing_image_set (StimulusTemplate) no description
  timestamps_reference_time: 2022-06-06T22:35:05.429000+00:00
  Group /units (Units) 
  Dataset /units/PT_ratio (VectorData) no description | shape = (2267,) | dtype = float64
  Dataset /units/amplitude (VectorData) no description | shape = (2267,) | dtype = float64
  Dataset /units/amplitude_cutoff (VectorData) no description | shape = (2267,) | dtype = float64
  Dataset /units/cluster_id (VectorData) no description | shape = (2267,) | dtype = int64
  Dataset /units/cumulative_drift (VectorData) no description | shape = (2267,) | dtype = float64
  Dataset /units/d_prime (VectorData) no description | shape = (2267,) | dtype = float64
  Dataset /units/firing_rate (VectorData) no description | shape = (2267,) | dtype = float64
  Dataset /units/id (ElementIdentifiers)  | shape = (2267,) | dtype = int32
  Dataset /units/isi_label (VectorData) no description | shape = (2267,) | dtype = object
  Dataset /units/isi_violations (VectorData) no description | shape = (2267,) | dtype = float64
  Dataset /units/isolation_distance (VectorData) no description | shape = (2267,) | dtype = float64
  Dataset /units/l_ratio (VectorData) no description | shape = (2267,) | dtype = float64
  Dataset /units/local_index (VectorData) no description | shape = (2267,) | dtype = int64
  Dataset /units/max_drift (VectorData) no description | shape = (2267,) | dtype = float64
  Dataset /units/nn_hit_rate (VectorData) no description | shape = (2267,) | dtype = float64
  Dataset /units/nn_miss_rate (VectorData) no description | shape = (2267,) | dtype = float64
  Dataset /units/peak_channel_id (VectorData) no description | shape = (2267,) | dtype = int64
  Dataset /units/presence_ratio (VectorData) no description | shape = (2267,) | dtype = float64
  Dataset /units/quality (VectorData) no description | shape = (2267,) | dtype = object
  Dataset /units/recovery_slope (VectorData) no description | shape = (2267,) | dtype = float64
  Dataset /units/repolarization_slope (VectorData) no description | shape = (2267,) | dtype = float64
  Dataset /units/silhouette_score (VectorData) no description | shape = (2267,) | dtype = float64
  Dataset /units/snr (VectorData) no description | shape = (2267,) | dtype = float64
  Dataset /units/spike_amplitudes (VectorData) amplitude (s) of detected spiking events | shape = (79857982,) | dtype = float64
  Dataset /units/spike_amplitudes_index (VectorIndex) Index for VectorData 'spike_amplitudes' | shape = (2267,) | dtype = uint32
  Dataset /units/spike_times (VectorData) times (s) of detected spiking events | shape = (79857982,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (2267,) | dtype = uint32
  Dataset /units/spread (VectorData) no description | shape = (2267,) | dtype = float64
  Dataset /units/structure_layer (VectorData) no description | shape = (2267,) | dtype = object
  Dataset /units/velocity_above (VectorData) no description | shape = (2267,) | dtype = float64
  Dataset /units/velocity_below (VectorData) no description | shape = (2267,) | dtype = float64
  Dataset /units/waveform_duration (VectorData) no description | shape = (2267,) | dtype = float64
  Dataset /units/waveform_mean (VectorData) mean waveforms on peak channels (over samples) | shape = (870528, 82) | dtype = float64
  Dataset /units/waveform_mean_index (VectorIndex) Index for VectorData 'waveform_mean' | shape = (2267,) | dtype = uint32


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/probe_0_lfp (LFP) 
  Group /acquisition/probe_0_lfp/probe_0_lfp_data (ElectricalSeries) no description
  Dataset /acquisition/probe_0_lfp/probe_0_lfp_data/electrodes (DynamicTableRegion) lfp channels on probe 0 | shape = (96,) | dtype = int32
  Group /acquisition/probe_0_lfp_data (ElectricalSeries) no description
  Dataset /acquisition/probe_0_lfp_data/electrodes (DynamicTableRegion) lfp channels on probe 0 | shape = (96,) | dtype = int32
  file_create_date: ['2024-05-28T17:50:43.338255-07:00']
  Group /general/devices/NP.1 (Device) Allen Brain Observatory - Scientifica 2P Rig
  Group /general/devices/probeA (EcephysProbe) Neuropixels 1.0 Probe
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering, including the filter name and frequency cutoffs | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (96,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the electrode, in ohms | shape = (96,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/probe_channel_number (VectorData) The local index of electrode/channel on device | shape = (96,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/probe_horizontal_position (VectorData) Width-wise position of electrode/channel on device (microns) | shape = (96,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/probe_id (VectorData) The unique id of this electrode's/channel's device | shape = (96,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/probe_vertical_position (VectorData) Length-wise position of electrode/channel on device (microns) | shape = (96,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/valid_data (VectorData) Whether data from this electrode/channel is usable | shape = (96,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the position (+x is posterior) | shape = (96,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the position (+y is inferior) | shape = (96,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the position (+z is right) | shape = (96,) | dtype = float64
  Group /general/extracellular_ephys/probeA (EcephysElectrodeGroup) Ecephys Electrode Group
  Group /general/extracellular_ephys/probeA/device (EcephysProbe) Neuropixels 1.0 Probe
  institution: Allen Institute for Brain Science
  Group /general/metadata (BehaviorMetadata) 
  session_id: None
  Group /general/subject (BehaviorSubject) 
  identifier: 0
  Group /processing/current_source_density (ProcessingModule) Precalculated current source density
  Group /processing/current_source_density/ecephys_csd (EcephysCSD) 
  Group /processing/current_source_density/ecephys_csd/current_source_density (TimeSeries) no description
  session_description: LFP data and associated info for one probe
  session_start_time: 2022-06-06T22:35:05.429000+00:00
  timestamps_reference_time: 2022-06-06T22:35:05.429000+00:00


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/probe_10_lfp (LFP) 
  Group /acquisition/probe_10_lfp/probe_10_lfp_data (ElectricalSeries) no description
  Dataset /acquisition/probe_10_lfp/probe_10_lfp_data/electrodes (DynamicTableRegion) lfp channels on probe 10 | shape = (84,) | dtype = int32
  Group /acquisition/probe_10_lfp_data (ElectricalSeries) no description
  Dataset /acquisition/probe_10_lfp_data/electrodes (DynamicTableRegion) lfp channels on probe 10 | shape = (84,) | dtype = int32
  file_create_date: ['2024-05-28T15:18:00.703554-07:00']
  Group /general/devices/NP.1 (Device) Allen Brain Observatory - Scientifica 2P Rig
  Group /general/devices/probeE (EcephysProbe) Neuropixels 1.0 Probe
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering, including the filter name and frequency cutoffs | shape = (84,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (84,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (84,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (84,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the electrode, in ohms | shape = (84,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (84,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/probe_channel_number (VectorData) The local index of electrode/channel on device | shape = (84,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/probe_horizontal_position (VectorData) Width-wise position of electrode/channel on device (microns) | shape = (84,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/probe_id (VectorData) The unique id of this electrode's/channel's device | shape = (84,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/probe_vertical_position (VectorData) Length-wise position of electrode/channel on device (microns) | shape = (84,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/valid_data (VectorData) Whether data from this electrode/channel is usable | shape = (84,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the position (+x is posterior) | shape = (84,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the position (+y is inferior) | shape = (84,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the position (+z is right) | shape = (84,) | dtype = float64
  Group /general/extracellular_ephys/probeE (EcephysElectrodeGroup) Ecephys Electrode Group
  Group /general/extracellular_ephys/probeE/device (EcephysProbe) Neuropixels 1.0 Probe
  institution: Allen Institute for Brain Science
  Group /general/metadata (BehaviorMetadata) 
  session_id: None
  Group /general/subject (BehaviorSubject) 
  identifier: 10
  Group /processing/current_source_density (ProcessingModule) Precalculated current source density
  Group /processing/current_source_density/ecephys_csd (EcephysCSD) 
  Group /processing/current_source_density/ecephys_csd/current_source_density (TimeSeries) no description
  session_description: LFP data and associated info for one probe
  session_start_time: 2022-06-07T21:25:34.215000+00:00
  timestamps_reference_time: 2022-06-07T21:25:34.215000+00:00


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  Group /acquisition/probe_11_lfp (LFP) 
  Group /acquisition/probe_11_lfp/probe_11_lfp_data (ElectricalSeries) no description
  Dataset /acquisition/probe_11_lfp/probe_11_lfp_data/electrodes (DynamicTableRegion) lfp channels on probe 11 | shape = (96,) | dtype = int32
  Group /acquisition/probe_11_lfp_data (ElectricalSeries) no description
  Dataset /acquisition/probe_11_lfp_data/electrodes (DynamicTableRegion) lfp channels on probe 11 | shape = (96,) | dtype = int32
  file_create_date: ['2024-05-28T15:18:01.291957-07:00']
  Group /general/devices/NP.1 (Device) Allen Brain Observatory - Scientifica 2P Rig
  Group /general/devices/probeF (EcephysProbe) Neuropixels 1.0 Probe
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering, including the filter name and frequency cutoffs | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (96,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the electrode, in ohms | shape = (96,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/probe_channel_number (VectorData) The local index of electrode/channel on device | shape = (96,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/probe_horizontal_position (VectorData) Width-wise position of electrode/channel on device (microns) | shape = (96,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/probe_id (VectorData) The unique id of this electrode's/channel's device | shape = (96,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/probe_vertical_position (VectorData) Length-wise position of electrode/channel on device (microns) | shape = (96,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/valid_data (VectorData) Whether data from this electrode/channel is usable | shape = (96,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the position (+x is posterior) | shape = (96,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the position (+y is inferior) | shape = (96,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the position (+z is right) | shape = (96,) | dtype = float64
  Group /general/extracellular_ephys/probeF (EcephysElectrodeGroup) Ecephys Electrode Group
  Group /general/extracellular_ephys/probeF/device (EcephysProbe) Neuropixels 1.0 Probe
  institution: Allen Institute for Brain Science
  Group /general/metadata (BehaviorMetadata) 
  session_id: None
  Group /general/subject (BehaviorSubject) 
  identifier: 11
  Group /processing/current_source_density (ProcessingModule) Precalculated current source density
  Group /processing/current_source_density/ecephys_csd (EcephysCSD) 
  Group /processing/current_source_density/ecephys_csd/current_source_density (TimeSeries) no description
  session_description: LFP data and associated info for one probe
  session_start_time: 2022-06-07T21:25:34.215000+00:00
  timestamps_reference_time: 2022-06-07T21:25:34.215000+00:00
