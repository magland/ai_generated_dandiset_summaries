
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001073/draft
name: LITMUS: Rat-based simulated motor unit dataset with 3 levels of waveform shape variability
contributor: [{'name': "O'Connell, Sean", 'email': 'sean_oc@emory.edu', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}]
description: Three synthetic datasets based on real multi-channel intramuscular recordings of motor unit action potentials from 10 unique motor units with high SNR (200-250). Each dataset has 8 channels and is 10 minutes long. Although low background noise was observed, waveform shapes were observed to have an inherent shape variability, so this Dandiset provides three different levels of waveform shape noise variability: 0, 2, and 4 STD (computed from the Kilosort spatial template matrix).
assetsSummary: {'species': [{'name': 'Rattus norvegicus - Norway rat', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10116'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 495900228, 'numberOfFiles': 3, 'numberOfSubjects': 3, 'variableMeasured': ['ElectricalSeries', 'ElectrodeGroup'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 001073 has 3 NWB files.
3 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeries (ElectricalSeries) Acquisition traces for the ElectricalSeries.
  Dataset /acquisition/ElectricalSeries/electrodes (DynamicTableRegion) electrode_table_region | shape = (8,) | dtype = int64
  file_create_date: ['2024-06-21T17:52:50.092916-04:00']
  Group /general/devices/Myomatrix, RF400 (Device) Ecephys probe. Automatically generated.
  Group /general/devices/Open Ephys Acquisition System (Device) Open source electrophysiology acquisition system
  experiment_description: Waveforms taken from locomotion of a rat on a treadmill
  experimenter: ["O'Connell, Sean"]
  Group /general/extracellular_ephys/ElectrodeGroup (ElectrodeGroup) Simulation based on a bipolar EMG recording with 4 separate threads and 8 channels per thread
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
  session_id: LITMUS_Rat_0-STD
  source_script: Created using NeuroConv v0.4.11
  Group /general/subject (Subject) 
  identifier: 2210c52d-b9f4-43cd-849f-e82017a4390b
  session_description: Simulated data with shape noise 0 STD
  session_start_time: 2022-11-17T17:08:07-05:00
  timestamps_reference_time: 2022-11-17T17:08:07-05:00
