
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001333/0.250327.2220
name: Parkinson's Electrophysiological Signal Dataset (PESD)
contributor: [{'name': 'Biswas, Ananna', 'email': 'ananna314.bd@gmail.com', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}]
description: The dataset contains electrophysiological signals from both healthy and parkinsonian subjects. We generated two types of samples from each group. The parkinsonian signals show a relatively high power density at the beta frequency (13 to 30 Hz). Thus, the beta oscillations (13 to 30 Hz) in the subthalamic nucleus (STN) are typically used as the pathological biomarkers for PD symptoms. Each sample includes two types of signals: Beta Average Rectified Voltage (ARV) and Local Field Potential (LFP) from the Subthalamic Nucleus (STN). The ARV signals are in the frequency domain and LFP signals are in the time domain.

Beta ARV Signal: The controller beta values are determined by calculating the Average Rectified Value (ARV) of the beta band. This is achieved by fully rectifying the filtered LFP signal using a fourth-order Chebyshev band-pass filter with an 8 Hz bandwidth, centered around the peak of the LFP power spectrum. Local Field Potential (LFP) - STN: Local Field Potentials are derived from the synchronized activity of neuron populations between the cortex, STN, and thalamus.

More details can be found in our article named, “Preliminary Results of Neuromorphic Controller Design and a Parkinson's Disease Dataset Building for Closed-Loop Deep Brain Stimulation”, available at https://arxiv.org/abs/2407.17756
assetsSummary: {'species': [{'name': 'Homo sapiens - Human', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9606'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 28983392, 'numberOfFiles': 52, 'numberOfSubjects': 5, 'variableMeasured': ['ElectricalSeries', 'LFP', 'ElectrodeGroup', 'ProcessingModule'], 'measurementTechnique': [{'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'signal filtering technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 001333 has 52 NWB files.
22 of these NWB files are of type 1.
30 of these NWB files are of type 2.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2025-03-27T16:53:28.055430-04:00']
  Group /general/devices/NEURON_Simulator (Device) Virtual probe used in NEURON simulation
  experiment_description: The PESD dataset is generated from a cortico-basal-ganglia network for a Parkinsonian computational model. The computational model of the cortico-basal-ganglia is originally presented by Fleming et al. in the article: 'Simulation of Closed-Loop Deep Brain Stimulation Control Schemes for Suppression of Pathological Beta Oscillations in Parkinson's Disease'.
  experimenter: ['Ananna Biswas']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (12,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (12,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (12,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/label (VectorData) label of electrode | shape = (12,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (12,) | dtype = object
  Group /general/extracellular_ephys/shank0 (ElectrodeGroup) Simulated electrode group for shank 0
  Group /general/extracellular_ephys/shank0/device (Device) Virtual probe used in NEURON simulation
  Group /general/extracellular_ephys/shank1 (ElectrodeGroup) Simulated electrode group for shank 1
  Group /general/extracellular_ephys/shank1/device (Device) Virtual probe used in NEURON simulation
  Group /general/extracellular_ephys/shank2 (ElectrodeGroup) Simulated electrode group for shank 2
  Group /general/extracellular_ephys/shank2/device (Device) Virtual probe used in NEURON simulation
  Group /general/extracellular_ephys/shank3 (ElectrodeGroup) Simulated electrode group for shank 3
  Group /general/extracellular_ephys/shank3/device (Device) Virtual probe used in NEURON simulation
  institution: Michigan Technological University
  keywords: ['ecephys' 'LFP' "Parkinson's Disease" 'Beta Band']
  lab: BrainX Lab
  related_publications: ['https://arxiv.org/abs/2407.17756' 'DOI: 10.3389/fnins.2020.00166']
  Group /general/subject (Subject) 
  identifier: 7a68ea11-865a-481a-a5fd-d91fe6def653
  Group /processing/ecephys (ProcessingModule) Processed electrophysiology data
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/Beta_Band_Voltage (ElectricalSeries) no description
  Dataset /processing/ecephys/LFP/Beta_Band_Voltage/electrodes (DynamicTableRegion) all electrodes | shape = (12,) | dtype = int64
  session_description: Parkinson's Electrophysiological Signal Dataset (PESD) Generated from Simulation
  session_start_time: 2025-03-27T16:53:27.990500-04:00
  timestamps_reference_time: 2025-03-27T16:53:27.990500-04:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2025-03-04T02:48:16.348695+00:00']
  Group /general/devices/NEURON_Simulator (Device) Virtual probe used in NEURON simulation
  experiment_description: The PESD dataset is generated from a cortico-basal-ganglia network for a Parkinsonian computational model. The computational model of the cortico-basal-ganglia is originally presented by Fleming et al. in the article: 'Simulation of Closed-Loop Deep Brain Stimulation Control Schemes for Suppression of Pathological Beta Oscillations in Parkinson's Disease'.
  experimenter: ['Ananna Biswas']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (12,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (12,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (12,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/label (VectorData) label of electrode | shape = (12,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (12,) | dtype = object
  Group /general/extracellular_ephys/shank0 (ElectrodeGroup) Simulated electrode group for shank 0
  Group /general/extracellular_ephys/shank0/device (Device) Virtual probe used in NEURON simulation
  Group /general/extracellular_ephys/shank1 (ElectrodeGroup) Simulated electrode group for shank 1
  Group /general/extracellular_ephys/shank1/device (Device) Virtual probe used in NEURON simulation
  Group /general/extracellular_ephys/shank2 (ElectrodeGroup) Simulated electrode group for shank 2
  Group /general/extracellular_ephys/shank2/device (Device) Virtual probe used in NEURON simulation
  Group /general/extracellular_ephys/shank3 (ElectrodeGroup) Simulated electrode group for shank 3
  Group /general/extracellular_ephys/shank3/device (Device) Virtual probe used in NEURON simulation
  institution: Michigan Technological University
  keywords: ['ecephys' 'LFP' "Parkinson's Disease" 'Beta Band']
  lab: BrainX Lab
  related_publications: ['https://arxiv.org/abs/2407.17756' 'DOI: 10.3389/fnins.2020.00166']
  Group /general/subject (Subject) 
  identifier: 720ccaa6-61e7-4608-8c1c-c49a50b64fb0
  Group /processing/ecephys (ProcessingModule) Processed electrophysiology data
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/LFP (ElectricalSeries) no description
  Dataset /processing/ecephys/LFP/LFP/electrodes (DynamicTableRegion) all electrodes | shape = (12,) | dtype = int64
  session_description: Parkinson's Electrophysiological Signal Dataset (PESD) Generated from Simulation
  session_start_time: 2025-03-04T02:48:16.245113+00:00
  timestamps_reference_time: 2025-03-04T02:48:16.245113+00:00
