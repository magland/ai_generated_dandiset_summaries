
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001072/draft
name: LITMUS: Rat-based motor unit dataset with 4 STD waveform shape variability
contributor: [{'name': "O'Connell, Sean", 'email': 'sean_oc@emory.edu', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}]
description: This 10-minute, 8-channel dataset contains synthetic data generated from the MUsim repository (https://github.com/snel-repo/MUsim) using real waveforms from 10 motor units recorded intramuscularly with up to 200 SNR. Although low background noise was observed, waveform shapes were observed to have an inherent shape variability. In this Dandiset the level of shape noise simulated is 4 STD (computed from the Kilosort spatial template matrix).
assetsSummary: {'schemaKey': 'AssetsSummary', 'numberOfBytes': 0, 'numberOfFiles': 0}

Dandiset 001072 has 1 NWB files.
1 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeries (ElectricalSeries) Acquisition traces for the ElectricalSeries.
  Dataset /acquisition/ElectricalSeries/electrodes (DynamicTableRegion) electrode_table_region | shape = (8,) | dtype = int64
  file_create_date: ['2024-06-21T17:23:25.754449-04:00']
  Group /general/devices/Myomatrix, RF400 (Device) Ecephys probe. Automatically generated.
  Group /general/devices/Open Ephys Acquisition System (Device) Open source electrophysiology acquisition system
  experiment_description: Waveforms taken from locomotion of a rat on a treadmill
  experimenter: ["O'Connell, Sean"]
  Group /general/extracellular_ephys/ElectrodeGroup (ElectrodeGroup) Bipolar EMG recording with 4 separate threads and 8 channels per thread
  Group /general/extracellular_ephys/ElectrodeGroup/device (Device) Ecephys probe. Automatically generated.
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/channel_name (VectorData) no description | shape = (8,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (8,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (8,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (8,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (8,) | dtype = object
  institution: Wallace H. Coulter Department of Biomedical Engineering, Georgia Tech and Emory University
  keywords: ['LITMUS' 'Motor Unit' 'MUsim' 'SNEL' 'EMUsort' 'Rat' 'EMG']
  lab: SNEL and Sober Lab
  session_id: 2022-11-17_17-08-07
  source_script: Created using NeuroConv v0.4.11
  Group /general/subject (Subject) 
  identifier: be9befea-8f10-4274-b437-0a1c742eecae
  session_description: Simulated data with shape noise 4 STD
  session_start_time: 2022-11-17T17:08:07-05:00
  timestamps_reference_time: 2022-11-17T17:08:07-05:00
