
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000774/draft
name: Spatial and temporal propagation of spiking activity in response to electrical stimulation in visual cortex
contributor: [{'name': 'National Institutes of Health (NIH)', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': '1 R01 NS 120850-01'}, {'url': 'denmanlab.github.io', 'name': 'Denman, Daniel', 'email': 'daniel.denman@cuanschutz.edu', 'roleName': ['dcite:Author', 'dcite:Conceptualization', 'dcite:ContactPerson', 'dcite:FundingAcquisition', 'dcite:Investigation', 'dcite:Maintainer', 'dcite:Methodology', 'dcite:ProjectLeader', 'dcite:ProjectAdministration', 'dcite:Supervision', 'dcite:Validation', 'dcite:Software'], 'schemaKey': 'Person', 'identifier': '0000-0003-1075-1265', 'affiliation': [{'name': 'University of Colorado Anschutz Medical Campus', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/03wmf1y16'}], 'includeInCitation': True}, {'name': 'Jordan Hickman', 'email': 'jordan.hickman@cuanschutz.edu', 'roleName': ['dcite:Author', 'dcite:Conceptualization', 'dcite:DataCollector', 'dcite:DataCurator', 'dcite:DataManager', 'dcite:FormalAnalysis', 'dcite:Methodology', 'dcite:Producer', 'dcite:ProjectMember', 'dcite:Researcher', 'dcite:Software', 'dcite:Visualization'], 'schemaKey': 'Person', 'identifier': '0000-0002-9048-2247', 'affiliation': [{'name': 'University of Colorado Anschutz Medical Campus', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/03wmf1y16'}], 'includeInCitation': True}]
description: Three dimensional measurement of electrical activity around a point source of electrical stimulation in neocortex. Electrical stimuli are single pulses with varying  amplitude and polarity. Stimuli are delivered near the middle layers of primary visual cortex; exact positions for each stimulation site in Common Coordinate Framework (CCF) coordinates are provided. Measurements are made with three simultaneous Neuropixels 1.0 electrodes roughly orthogonally placed around the stimulation site. The crossing point is approximately hundreds of microns deeper to the stimulation site. CCF coordinated for each electrode are also provided. Sampling covers at least one millimeter in all directions around stimulation, including across cortical area boundaries and across boundaries to deeper brain structures including hippocampus. 
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 1358542068, 'numberOfFiles': 10, 'numberOfSubjects': 10, 'variableMeasured': ['Units', 'ElectrodeGroup'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000774 has 10 NWB files.
4 of these NWB files are of type 1.
4 of these NWB files are of type 2.
1 of these NWB files are of type 3.
1 of these NWB files are of type 4.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2024-01-05T14:19:54.166645-07:00']
  Group /general/devices/DenmanLab_EphysRig2 (Device) Orthogonal neuropixel rig with 3 Neuropixels and electrical stimulator
  experiment_description: Electrical stimulation with orthogonal neuropixels in visual cortex
  experimenter: ['Hickman, Jordan']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering, including the filter name and frequency cutoffs | shape = (1152,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (1152,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (1152,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (1152,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the electrode, in ohms | shape = (1152,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (1152,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the position (+x is posterior) | shape = (1152,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the position (+y is inferior) | shape = (1152,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the position (+z is right) | shape = (1152,) | dtype = float64
  Group /general/extracellular_ephys/probeprobeA (ElectrodeGroup) Neuropixels1.0_probeA
  Group /general/extracellular_ephys/probeprobeA/device (Device) Orthogonal neuropixel rig with 3 Neuropixels and electrical stimulator
  Group /general/extracellular_ephys/probeprobeB (ElectrodeGroup) Neuropixels1.0_probeB
  Group /general/extracellular_ephys/probeprobeB/device (Device) Orthogonal neuropixel rig with 3 Neuropixels and electrical stimulator
  Group /general/extracellular_ephys/probeprobeC (ElectrodeGroup) Neuropixels1.0_probeC
  Group /general/extracellular_ephys/probeprobeC/device (Device) Orthogonal neuropixel rig with 3 Neuropixels and electrical stimulator
  institution: University of Colorado Anschutz Medical Campus
  keywords: ['orthogonal' 'estim' 'electrical stimulation' 'multi-NPs' 'visual cortex']
  lab: Denman Lab
  session_id: jlh14_2022-06-14_g0
  Group /general/subject (Subject) 
  identifier: E:\\jlh14_2022-06-14_g0
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (1,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1,) | dtype = float64
  Dataset /intervals/epochs/tags (VectorData) user-defined tags | shape = (1,) | dtype = object
  Dataset /intervals/epochs/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (1,) | dtype = uint8
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/amplitude (VectorData) amplitude in uA | shape = (450,) | dtype = int32
  Dataset /intervals/trials/contact_negative (VectorData) the negative (cathodal) contact for a trial | shape = (450,) | dtype = int32
  Dataset /intervals/trials/contact_positive (VectorData) the positive (anodal) contact used | shape = (450,) | dtype = int32
  Dataset /intervals/trials/contacts (VectorData) the stimulation contacts and polarities used on the stim electrode | shape = (450,) | dtype = object
  Dataset /intervals/trials/event_period (VectorData) milliseconds | shape = (450,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (450,) | dtype = int32
  Dataset /intervals/trials/notes (VectorData) general notes from recording | shape = (450,) | dtype = object
  Dataset /intervals/trials/polarity (VectorData) bipolar or monopolar | shape = (450,) | dtype = object
  Dataset /intervals/trials/pulse_duration (VectorData) usecs | shape = (450,) | dtype = int32
  Dataset /intervals/trials/pulse_number (VectorData) event quantity | shape = (450,) | dtype = int32
  Dataset /intervals/trials/run (VectorData) the run number where each run generally represents a unique parameter space | shape = (450,) | dtype = int32
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (450,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (450,) | dtype = float64
  Dataset /intervals/trials/train_duration (VectorData) train duration (s) | shape = (450,) | dtype = float64
  Dataset /intervals/trials/train_period (VectorData) train period (s) | shape = (450,) | dtype = float64
  Dataset /intervals/trials/train_quantity (VectorData) train quantity | shape = (450,) | dtype = int32
  Dataset /intervals/trials/waveform_shape (VectorData) monophasic, biphasic or triphasic | shape = (450,) | dtype = object
  session_description: jlh14
  session_start_time: 2024-01-05T14:19:54.166114-07:00
  timestamps_reference_time: 2024-01-05T14:19:54.166114-07:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/KSamplitude (VectorData) Kilosort amplitude | shape = (1099,) | dtype = float64
  Dataset /units/KScontamination (VectorData) Kilosort ISI contamination | shape = (1099,) | dtype = float64
  Dataset /units/KSlabel (VectorData) Kilosort label | shape = (1099,) | dtype = object
  Dataset /units/ch (VectorData) channel number | shape = (1099,) | dtype = int32
  Dataset /units/group (VectorData) user label of good/mua | shape = (1099,) | dtype = object
  Dataset /units/id (ElementIdentifiers)  | shape = (1099,) | dtype = int32
  Dataset /units/no_spikes (VectorData) total number of spikes across recording | shape = (1099,) | dtype = int32
  Dataset /units/probe (VectorData) probe ID | shape = (1099,) | dtype = object
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (6298011,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (1099,) | dtype = uint32
  Dataset /units/template (VectorData) Kilosort template | shape = (1099, 82, 300) | dtype = float32
  Dataset /units/unit_id (VectorData) cluster ID from KS2 | shape = (1099,) | dtype = object


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2024-01-04T15:26:59.286988-07:00']
  Group /general/devices/DenmanLab_EphysRig2 (Device) Orthogonal neuropixel rig with 3 Neuropixels and electrical stimulator
  experiment_description: Electrical stimulation with orthogonal neuropixels in visual cortex
  experimenter: ['Hickman, Jordan']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering, including the filter name and frequency cutoffs | shape = (1152,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (1152,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (1152,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (1152,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the electrode, in ohms | shape = (1152,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (1152,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the position (+x is posterior) | shape = (1152,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the position (+y is inferior) | shape = (1152,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the position (+z is right) | shape = (1152,) | dtype = float64
  Group /general/extracellular_ephys/probeA (ElectrodeGroup) Neuropixels1.0_A
  Group /general/extracellular_ephys/probeA/device (Device) Orthogonal neuropixel rig with 3 Neuropixels and electrical stimulator
  Group /general/extracellular_ephys/probeB (ElectrodeGroup) Neuropixels1.0_B
  Group /general/extracellular_ephys/probeB/device (Device) Orthogonal neuropixel rig with 3 Neuropixels and electrical stimulator
  Group /general/extracellular_ephys/probeC (ElectrodeGroup) Neuropixels1.0_C
  Group /general/extracellular_ephys/probeC/device (Device) Orthogonal neuropixel rig with 3 Neuropixels and electrical stimulator
  institution: University of Colorado Anschutz Medical Campus
  keywords: ['orthogonal' 'estim' 'electrical stimulation' 'multi-NPs' 'visual cortex']
  lab: Denman Lab
  session_id: jlh31_2023-01-24_14-30-23
  Group /general/subject (Subject) 
  identifier: E:\\jlh31_2023-01-24_14-30-23
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (1,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1,) | dtype = float64
  Dataset /intervals/epochs/tags (VectorData) user-defined tags | shape = (1,) | dtype = object
  Dataset /intervals/epochs/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (1,) | dtype = uint8
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/amplitude (VectorData) amplitude in uA | shape = (2700,) | dtype = int32
  Dataset /intervals/trials/contact_negative (VectorData) the negative (cathodal) contact for a trial | shape = (2700,) | dtype = int32
  Dataset /intervals/trials/contact_negative_coord (VectorData) the ccf coordinate for the cathodal contact | shape = (2700, 3) | dtype = float64
  Dataset /intervals/trials/contact_positive (VectorData) the positive (anodal) contact used | shape = (2700,) | dtype = int32
  Dataset /intervals/trials/contact_positive_coord (VectorData) the ccf coordinate for the anodal contact | shape = (2700, 3) | dtype = float64
  Dataset /intervals/trials/contacts (VectorData) the stimulation contacts and polarities used on the stim electrode | shape = (2700,) | dtype = object
  Dataset /intervals/trials/event_period (VectorData) milliseconds | shape = (2700,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (2700,) | dtype = int32
  Dataset /intervals/trials/notes (VectorData) general notes from recording | shape = (2700,) | dtype = object
  Dataset /intervals/trials/polarity (VectorData) bipolar or monopolar | shape = (2700,) | dtype = object
  Dataset /intervals/trials/pulse_duration (VectorData) usecs | shape = (2700,) | dtype = int32
  Dataset /intervals/trials/pulse_number (VectorData) event quantity | shape = (2700,) | dtype = int32
  Dataset /intervals/trials/run (VectorData) the run number where each run generally represents a unique parameter space | shape = (2700,) | dtype = int32
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (2700,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (2700,) | dtype = float64
  Dataset /intervals/trials/train_duration (VectorData) train duration (s) | shape = (2700,) | dtype = float64
  Dataset /intervals/trials/train_period (VectorData) train period (s) | shape = (2700,) | dtype = float64
  Dataset /intervals/trials/train_quantity (VectorData) train quantity | shape = (2700,) | dtype = int32
  Dataset /intervals/trials/waveform_shape (VectorData) monophasic, biphasic or triphasic | shape = (2700,) | dtype = object
  session_description: jlh31
  session_start_time: 2024-01-04T15:26:59.285987-07:00
  timestamps_reference_time: 2024-01-04T15:26:59.285987-07:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/KSamplitude (VectorData) Kilosort amplitude | shape = (600,) | dtype = float64
  Dataset /units/KScontamination (VectorData) Kilosort ISI contamination | shape = (600,) | dtype = float64
  Dataset /units/KSlabel (VectorData) Kilosort label | shape = (600,) | dtype = object
  Dataset /units/brain_reg (VectorData) brain region of ch unit was recorded on | shape = (600,) | dtype = object
  Dataset /units/ccf_coordinates (VectorData) the ccf brain space coordinates (AP, DV, ML) for the channel the unit was recorded on | shape = (600, 3) | dtype = float64
  Dataset /units/ch (VectorData) channel number | shape = (600,) | dtype = int32
  Dataset /units/distance_from_stim (VectorData) List of euclidean distances to each stimulation contact: use trials dataframe to identify appropriate stim contact | shape = (600, 16) | dtype = float64
  Dataset /units/group (VectorData) user label of good/mua | shape = (600,) | dtype = object
  Dataset /units/id (ElementIdentifiers)  | shape = (600,) | dtype = int32
  Dataset /units/no_spikes (VectorData) total number of spikes across recording | shape = (600,) | dtype = int32
  Dataset /units/probe (VectorData) probe ID | shape = (600,) | dtype = object
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (14432434,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (600,) | dtype = uint32
  Dataset /units/template (VectorData) Kilosort template | shape = (600, 82, 200) | dtype = float32
  Dataset /units/unit_id (VectorData) cluster ID from KS2 | shape = (600,) | dtype = object


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2024-01-04T16:39:47.302854-07:00']
  Group /general/devices/DenmanLab_EphysRig2 (Device) Orthogonal neuropixel rig with 3 Neuropixels and electrical stimulator
  experiment_description: Electrical stimulation with orthogonal neuropixels in visual cortex
  experimenter: ['Hickman, Jordan']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering, including the filter name and frequency cutoffs | shape = (768,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (768,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (768,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (768,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the electrode, in ohms | shape = (768,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (768,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the position (+x is posterior) | shape = (768,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the position (+y is inferior) | shape = (768,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the position (+z is right) | shape = (768,) | dtype = float64
  Group /general/extracellular_ephys/probeA (ElectrodeGroup) Neuropixels1.0_A
  Group /general/extracellular_ephys/probeA/device (Device) Orthogonal neuropixel rig with 3 Neuropixels and electrical stimulator
  Group /general/extracellular_ephys/probeB (ElectrodeGroup) Neuropixels1.0_B
  Group /general/extracellular_ephys/probeB/device (Device) Orthogonal neuropixel rig with 3 Neuropixels and electrical stimulator
  institution: University of Colorado Anschutz Medical Campus
  keywords: ['orthogonal' 'estim' 'electrical stimulation' 'multi-NPs' 'visual cortex']
  lab: Denman Lab
  session_id: jlh33_2023-02-22_15-24-35
  Group /general/subject (Subject) 
  identifier: E:\\jlh33_2023-02-22_15-24-35
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (1,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1,) | dtype = float64
  Dataset /intervals/epochs/tags (VectorData) user-defined tags | shape = (1,) | dtype = object
  Dataset /intervals/epochs/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (1,) | dtype = uint8
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/amplitude (VectorData) amplitude in uA | shape = (1440,) | dtype = int32
  Dataset /intervals/trials/contact_negative (VectorData) the negative (cathodal) contact for a trial | shape = (1440,) | dtype = int32
  Dataset /intervals/trials/contact_negative_coord (VectorData) the ccf coordinate for the cathodal contact | shape = (1440, 3) | dtype = float64
  Dataset /intervals/trials/contact_positive (VectorData) the positive (anodal) contact used | shape = (1440,) | dtype = int32
  Dataset /intervals/trials/contact_positive_coord (VectorData) the ccf coordinate for the anodal contact | shape = (1440, 3) | dtype = float64
  Dataset /intervals/trials/contacts (VectorData) the stimulation contacts and polarities used on the stim electrode | shape = (1440,) | dtype = object
  Dataset /intervals/trials/event_period (VectorData) milliseconds | shape = (1440,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (1440,) | dtype = int32
  Dataset /intervals/trials/notes (VectorData) general notes from recording | shape = (1440,) | dtype = object
  Dataset /intervals/trials/polarity (VectorData) bipolar or monopolar | shape = (1440,) | dtype = object
  Dataset /intervals/trials/pulse_duration (VectorData) usecs | shape = (1440,) | dtype = int32
  Dataset /intervals/trials/pulse_number (VectorData) event quantity | shape = (1440,) | dtype = int32
  Dataset /intervals/trials/run (VectorData) the run number where each run generally represents a unique parameter space | shape = (1440,) | dtype = int32
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (1440,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1440,) | dtype = float64
  Dataset /intervals/trials/train_duration (VectorData) train duration (s) | shape = (1440,) | dtype = float64
  Dataset /intervals/trials/train_period (VectorData) train period (s) | shape = (1440,) | dtype = float64
  Dataset /intervals/trials/train_quantity (VectorData) train quantity | shape = (1440,) | dtype = int32
  Dataset /intervals/trials/waveform_shape (VectorData) monophasic, biphasic or triphasic | shape = (1440,) | dtype = object
  session_description: jlh33
  session_start_time: 2024-01-04T16:39:47.301853-07:00
  timestamps_reference_time: 2024-01-04T16:39:47.301853-07:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/KSamplitude (VectorData) Kilosort amplitude | shape = (258,) | dtype = float64
  Dataset /units/KScontamination (VectorData) Kilosort ISI contamination | shape = (258,) | dtype = float64
  Dataset /units/KSlabel (VectorData) Kilosort label | shape = (258,) | dtype = object
  Dataset /units/brain_reg (VectorData) brain region of ch unit was recorded on | shape = (258,) | dtype = object
  Dataset /units/ccf_coordinates (VectorData) the ccf brain space coordinates (AP, DV, ML) for the channel the unit was recorded on | shape = (258, 3) | dtype = float64
  Dataset /units/ch (VectorData) channel number | shape = (258,) | dtype = int32
  Dataset /units/distance_from_stim (VectorData) List of euclidean distances to each stimulation contact: use trials dataframe to identify appropriate stim contact | shape = (258, 16) | dtype = float64
  Dataset /units/group (VectorData) user label of good/mua | shape = (258,) | dtype = object
  Dataset /units/id (ElementIdentifiers)  | shape = (258,) | dtype = int32
  Dataset /units/no_spikes (VectorData) total number of spikes across recording | shape = (258,) | dtype = int32
  Dataset /units/probe (VectorData) probe ID | shape = (258,) | dtype = object
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (3803317,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (258,) | dtype = uint32
  Dataset /units/template (VectorData) Kilosort template | shape = (258, 82, 300) | dtype = float32
  Dataset /units/unit_id (VectorData) cluster ID from KS2 | shape = (258,) | dtype = object


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2024-01-08T10:33:57.552999-07:00']
  Group /general/devices/DenmanLab_EphysRig2 (Device) Orthogonal neuropixel rig with 3 Neuropixels and electrical stimulator
  experiment_description: Electrical stimulation with orthogonal neuropixels in visual cortex
  experimenter: ['Hickman, Jordan']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering, including the filter name and frequency cutoffs | shape = (768,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (768,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (768,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (768,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the electrode, in ohms | shape = (768,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (768,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the position (+x is posterior) | shape = (768,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the position (+y is inferior) | shape = (768,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the position (+z is right) | shape = (768,) | dtype = float64
  Group /general/extracellular_ephys/probeB (ElectrodeGroup) Neuropixels1.0_B
  Group /general/extracellular_ephys/probeB/device (Device) Orthogonal neuropixel rig with 3 Neuropixels and electrical stimulator
  Group /general/extracellular_ephys/probeC (ElectrodeGroup) Neuropixels1.0_C
  Group /general/extracellular_ephys/probeC/device (Device) Orthogonal neuropixel rig with 3 Neuropixels and electrical stimulator
  institution: University of Colorado Anschutz Medical Campus
  keywords: ['orthogonal' 'estim' 'electrical stimulation' 'multi-NPs' 'visual cortex']
  lab: Denman Lab
  session_id: jlh40_2023-08-21_16-01-34
  Group /general/subject (Subject) 
  identifier: E:\\jlh40_2023-08-21_16-01-34
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (1,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1,) | dtype = float64
  Dataset /intervals/epochs/tags (VectorData) user-defined tags | shape = (1,) | dtype = object
  Dataset /intervals/epochs/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (1,) | dtype = uint8
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/amplitude (VectorData) amplitude in uA | shape = (825,) | dtype = int32
  Dataset /intervals/trials/contact_negative (VectorData) the negative (cathodal) contact for a trial | shape = (825,) | dtype = float64
  Dataset /intervals/trials/contact_negative_coord (VectorData) the ccf coordinate for the cathodal contact | shape = (825, 3) | dtype = float64
  Dataset /intervals/trials/contact_positive (VectorData) the positive (anodal) contact used | shape = (825,) | dtype = int32
  Dataset /intervals/trials/contact_positive_coord (VectorData) the ccf coordinate for the anodal contact | shape = (825, 3) | dtype = int32
  Dataset /intervals/trials/contacts (VectorData) the stimulation contacts and polarities used on the stim electrode | shape = (825,) | dtype = object
  Dataset /intervals/trials/event_period (VectorData) milliseconds | shape = (825,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (825,) | dtype = int32
  Dataset /intervals/trials/notes (VectorData) general notes from recording | shape = (825,) | dtype = object
  Dataset /intervals/trials/polarity (VectorData) bipolar or monopolar | shape = (825,) | dtype = object
  Dataset /intervals/trials/pulse_duration (VectorData) usecs | shape = (825,) | dtype = int32
  Dataset /intervals/trials/pulse_number (VectorData) event quantity | shape = (825,) | dtype = int32
  Dataset /intervals/trials/run (VectorData) the run number where each run generally represents a unique parameter space | shape = (825,) | dtype = int32
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (825,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (825,) | dtype = float64
  Dataset /intervals/trials/train_duration (VectorData) train duration (s) | shape = (825,) | dtype = float64
  Dataset /intervals/trials/train_period (VectorData) train period (s) | shape = (825,) | dtype = float64
  Dataset /intervals/trials/train_quantity (VectorData) train quantity | shape = (825,) | dtype = int32
  Dataset /intervals/trials/waveform_shape (VectorData) monophasic, biphasic or triphasic | shape = (825,) | dtype = object
  session_description: jlh40
  session_start_time: 2024-01-08T10:33:57.551999-07:00
  timestamps_reference_time: 2024-01-08T10:33:57.551999-07:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/KSamplitude (VectorData) Kilosort amplitude | shape = (660,) | dtype = float64
  Dataset /units/KScontamination (VectorData) Kilosort ISI contamination | shape = (660,) | dtype = float64
  Dataset /units/KSlabel (VectorData) Kilosort label | shape = (660,) | dtype = object
  Dataset /units/brain_reg (VectorData) brain region of ch unit was recorded on | shape = (660,) | dtype = object
  Dataset /units/ccf_coordinates (VectorData) the ccf brain space coordinates (AP, DV, ML) for the channel the unit was recorded on | shape = (660, 3) | dtype = float64
  Dataset /units/ch (VectorData) channel number | shape = (660,) | dtype = int32
  Dataset /units/distance_from_stim (VectorData) List of euclidean distances to each stimulation contact: use trials dataframe to identify appropriate stim contact | shape = (660, 16) | dtype = float64
  Dataset /units/group (VectorData) user label of good/mua | shape = (660,) | dtype = object
  Dataset /units/id (ElementIdentifiers)  | shape = (660,) | dtype = int32
  Dataset /units/no_spikes (VectorData) total number of spikes across recording | shape = (660,) | dtype = int32
  Dataset /units/probe (VectorData) probe ID | shape = (660,) | dtype = object
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (3244006,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (660,) | dtype = uint32
  Dataset /units/template (VectorData) Kilosort template | shape = (660, 82, 300) | dtype = float32
  Dataset /units/unit_id (VectorData) cluster ID from KS2 | shape = (660,) | dtype = object
