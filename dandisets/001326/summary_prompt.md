
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001326/0.250528.1957
name: Brain-wide mouse electrophysiology during aversive stimuli and ketamine
contributor: [{'name': 'National Institutes of Health (NIH)', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': '1 P50 DA 042012-01A1'}, {'name': 'Richman, Ethan', 'email': 'erichamc@gmail.com', 'roleName': ['dcite:Author', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0001-8471-266X'}, {'name': 'Kauvar, Isaac', 'email': 'ikauvar@gmail.com', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-1336-0721'}]
description: Brain-wide electrophysiology associated with Kauvar*, Richman*, Liu* et al. Science (2025). https://doi.org/10.1126/science.adt3971
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 2606908588, 'numberOfFiles': 13, 'numberOfSubjects': 10, 'variableMeasured': ['ElectrodeGroup', 'Units'], 'measurementTechnique': [{'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 001326 has 13 NWB files.
1 of these NWB files are of type 1.
12 of these NWB files are of type 2.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Ketamine infusion start (TimeSeries) Approximate timepoint of manual infusion of ketamine bolus
  file_create_date: ['2025-01-25T14:50:51.152928-08:00']
  Group /general/devices/Neuropixels_Probe_0 (Device) Neuropixels 1.0 probe
  Group /general/devices/Neuropixels_Probe_3 (Device) Neuropixels 1.0 probe
  experiment_description: Neuropixels 1.0 recording with eyepuff assay and ketamine administration.
  experimenter: ['Ethan Richman, Chelsea Li']
  Group /general/extracellular_ephys/ElectrodeGroup0 (ElectrodeGroup) Probe 0 electrode group. xyz is in AIBSAtlas coordinate space
  Group /general/extracellular_ephys/ElectrodeGroup0/device (Device) Neuropixels 1.0 probe
  Group /general/extracellular_ephys/ElectrodeGroup3 (ElectrodeGroup) Probe 3 electrode group. xyz is in AIBSAtlas coordinate space
  Group /general/extracellular_ephys/ElectrodeGroup3/device (Device) Neuropixels 1.0 probe
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering, including the filter name and frequency cutoffs | shape = (764,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (764,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (764,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (764,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the electrode, in ohms | shape = (764,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (764,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the position (+x is posterior) | shape = (764,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the position (+y is inferior) | shape = (764,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the position (+z is right) | shape = (764,) | dtype = float64
  institution: Stanford University
  keywords: ['neuropixels' 'extracellular electrophysiology' 'affective behavior'
   'emotion-like state' 'ketamine' 'eyepuff' 'air puff']
  lab: Deisseroth
  related_publications: ['Kauvar*, Richman*, Liu*, et al., Conserved brain-wide emergence of emotional response from sensation in humans and mice. Science (2025) [DOI TBD]']
  Group /general/subject (Subject) 
  identifier: 8dba30fa-d89a-469e-9eff-c9dc4c9e6721
  Group /intervals/Stimulus presentations (TimeIntervals) experimental intervals
  Dataset /intervals/Stimulus presentations/id (ElementIdentifiers)  | shape = (960,) | dtype = int64
  Dataset /intervals/Stimulus presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (960,) | dtype = float64
  Dataset /intervals/Stimulus presentations/stimulus (VectorData) Type of stimulus delivered | shape = (960,) | dtype = object
  Dataset /intervals/Stimulus presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (960,) | dtype = float64
  session_description: Mouse extracellular ephys data for Kauvar*, Richman*, Liu* et al. Science (2025)
  session_start_time: 2023-07-06T00:00:00-07:00
  timestamps_reference_time: 2023-07-06T00:00:00-07:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/brain_region (VectorData) Assigned AIBS CCFv3 brain region acronym | shape = (154,) | dtype = object
  Dataset /units/channel (VectorData) Closest electrode channel id | shape = (154,) | dtype = int64
  Dataset /units/id (ElementIdentifiers)  | shape = (154,) | dtype = int64
  Dataset /units/n_spikes (VectorData) Number of spikes in the entire recording | shape = (154,) | dtype = float64
  Dataset /units/quality (VectorData) Quality label from Bombcell pipeline | shape = (154,) | dtype = object
  Dataset /units/snr (VectorData) Signal-to-noise ratio | shape = (154,) | dtype = float64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (2753026,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (154,) | dtype = uint32
  Dataset /units/x (VectorData) x location in AIBS CCFv3 brain atlas | shape = (154,) | dtype = float64
  Dataset /units/y (VectorData) y location in AIBS CCFv3 brain atlas | shape = (154,) | dtype = float64
  Dataset /units/z (VectorData) z location in AIBS CCFv3 brain atlas | shape = (154,) | dtype = float64


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Ketamine infusion start (TimeSeries) Approximate timepoint of manual infusion of ketamine bolus
  file_create_date: ['2025-01-25T14:57:50.559052-08:00']
  Group /general/devices/Neuropixels_Probe_0 (Device) Neuropixels 1.0 probe
  Group /general/devices/Neuropixels_Probe_1 (Device) Neuropixels 1.0 probe
  Group /general/devices/Neuropixels_Probe_2 (Device) Neuropixels 1.0 probe
  Group /general/devices/Neuropixels_Probe_3 (Device) Neuropixels 1.0 probe
  experiment_description: Neuropixels 1.0 recording with eyepuff assay and ketamine administration.
  experimenter: ['Ethan Richman, Chelsea Li']
  Group /general/extracellular_ephys/ElectrodeGroup0 (ElectrodeGroup) Probe 0 electrode group. xyz is in AIBSAtlas coordinate space
  Group /general/extracellular_ephys/ElectrodeGroup0/device (Device) Neuropixels 1.0 probe
  Group /general/extracellular_ephys/ElectrodeGroup1 (ElectrodeGroup) Probe 1 electrode group. xyz is in AIBSAtlas coordinate space
  Group /general/extracellular_ephys/ElectrodeGroup1/device (Device) Neuropixels 1.0 probe
  Group /general/extracellular_ephys/ElectrodeGroup2 (ElectrodeGroup) Probe 2 electrode group. xyz is in AIBSAtlas coordinate space
  Group /general/extracellular_ephys/ElectrodeGroup2/device (Device) Neuropixels 1.0 probe
  Group /general/extracellular_ephys/ElectrodeGroup3 (ElectrodeGroup) Probe 3 electrode group. xyz is in AIBSAtlas coordinate space
  Group /general/extracellular_ephys/ElectrodeGroup3/device (Device) Neuropixels 1.0 probe
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering, including the filter name and frequency cutoffs | shape = (1506,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (1506,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (1506,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (1506,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the electrode, in ohms | shape = (1506,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (1506,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the position (+x is posterior) | shape = (1506,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the position (+y is inferior) | shape = (1506,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the position (+z is right) | shape = (1506,) | dtype = float64
  institution: Stanford University
  keywords: ['neuropixels' 'extracellular electrophysiology' 'affective behavior'
   'emotion-like state' 'ketamine' 'eyepuff' 'air puff']
  lab: Deisseroth
  related_publications: ['Kauvar*, Richman*, Liu*, et al., Conserved brain-wide emergence of emotional response from sensation in humans and mice. Science (2025) [DOI TBD]']
  Group /general/subject (Subject) 
  identifier: dc6ccf38-60fc-4e11-beff-2ddae3b03e48
  Group /intervals/Stimulus presentations (TimeIntervals) experimental intervals
  Dataset /intervals/Stimulus presentations/id (ElementIdentifiers)  | shape = (952,) | dtype = int64
  Dataset /intervals/Stimulus presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (952,) | dtype = float64
  Dataset /intervals/Stimulus presentations/stimulus (VectorData) Type of stimulus delivered | shape = (952,) | dtype = object
  Dataset /intervals/Stimulus presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (952,) | dtype = float64
  session_description: Mouse extracellular ephys data for Kauvar*, Richman*, Liu* et al. Science (2025)
  session_start_time: 2023-09-01T00:00:00-07:00
  timestamps_reference_time: 2023-09-01T00:00:00-07:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/brain_region (VectorData) Assigned AIBS CCFv3 brain region acronym | shape = (942,) | dtype = object
  Dataset /units/channel (VectorData) Closest electrode channel id | shape = (942,) | dtype = int64
  Dataset /units/id (ElementIdentifiers)  | shape = (942,) | dtype = int64
  Dataset /units/n_spikes (VectorData) Number of spikes in the entire recording | shape = (942,) | dtype = float64
  Dataset /units/quality (VectorData) Quality label from Bombcell pipeline | shape = (942,) | dtype = object
  Dataset /units/snr (VectorData) Signal-to-noise ratio | shape = (942,) | dtype = float64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (30275497,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (942,) | dtype = uint32
  Dataset /units/x (VectorData) x location in AIBS CCFv3 brain atlas | shape = (942,) | dtype = float64
  Dataset /units/y (VectorData) y location in AIBS CCFv3 brain atlas | shape = (942,) | dtype = float64
  Dataset /units/z (VectorData) z location in AIBS CCFv3 brain atlas | shape = (942,) | dtype = float64
