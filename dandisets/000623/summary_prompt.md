
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000623/0.240227.2023
name: Data for: Multimodal single-neuron, intracranial EEG, and fMRI brain responses during movie watching in human patients
contributor: [{'name': 'Keles, Umit', 'roleName': ['dcite:Author', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Dubois, Julien', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Le, Kevin J. M.', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Tyszka, J. Michael', 'roleName': [], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Kahn, David A.', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Kyzar, Michael', 'email': 'kyzarnexus@gmail.com', 'roleName': ['dcite:ProjectMember', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0009-0004-4392-9933', 'affiliation': [], 'includeInCitation': False}, {'name': 'Reed, Chrystal M.', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Chung, Jeffrey M. ', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Mamelak, Adam N.', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Adolphs, Ralph', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Rutishauser, Ueli', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}]
description: We present a multimodal dataset of intracranial recordings, fMRI, and eye tracking in 20 participants during movie watching. Recordings consist of single neurons, local field potential, and intracranial EEG activity acquired from depth electrodes targeting the amygdala, hippocampus, and medial frontal cortex implanted for monitoring of epileptic seizures. Participants watched an 8-min long excerpt from the video "Bang! You're Dead" and performed a recognition memory test for movie content. 3 T fMRI activity was recorded prior to surgery in 11 of these participants while performing the same task. This NWB- and BIDS-formatted dataset includes spike times, field potential activity, behavior, eye tracking, electrode locations, demographics, and functional and structural MRI scans. For technical validation, we provide signal quality metrics, assess eye tracking quality, behavior, the tuning of cells and high-frequency broadband power field potentials to familiarity and event boundaries, and show brain-wide inter-subject correlations for fMRI. This dataset will facilitate the investigation of brain activity during movie watching, recognition memory, and the neural basis of the fMRI-BOLD signal.

This dataset accompanies the following data descriptor: Keles, U., Dubois, J., Le, K.J.M., Tyszka, J.M., Kahn, D.A., Reed, C.M., Chung, J.M., Mamelak, A.N., Adolphs, R. and Rutishauser, U. Multimodal single-neuron, intracranial EEG, and fMRI brain responses during movie watching in human patients. Sci Data 11, 214 (2024). [Link to paper](https://doi.org/10.1038/s41597-024-03029-1)

Sample code to access and analyze this dataset has been provided: https://github.com/rutishauserlab/bmovie-release-NWB-BIDS
assetsSummary: {'species': [{'name': 'Homo sapiens - Human', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9606'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}, {'name': 'behavioral approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 27744749325, 'numberOfFiles': 29, 'numberOfSubjects': 16, 'variableMeasured': ['ElectricalSeries', 'LFP', 'EyeTracking', 'ElectrodeGroup', 'BehavioralTimeSeries', 'PupilTracking', 'SpatialSeries', 'ProcessingModule', 'Units'], 'measurementTechnique': [{'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'signal filtering technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000623 has 25 NWB files.
16 of these NWB files are of type 1.
3 of these NWB files are of type 2.
2 of these NWB files are of type 3.
2 of these NWB files are of type 4.
2 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/events_ttl (TimeSeries) The events correspond to the TTL markers for each session. 
                            The TTL markers are the following: 
                            4 = start of the movie, 40-49 = frame number mapping to a log file, 
                            33 = keypress, 7 = start probe for recognition, 9 = startITI, 1 = start fixation, 
                            10 = end fixation, 52 = screen of instruction, 66 = end of experiment
  Group /acquisition/experiment_ids (TimeSeries) The experimentid (or task_id) corresponds to the encoding 
                                   (i.e., movie watching as one trial) or recognition trials. 
                                   The encoding is indexed by: 2. 
                                   The recognition trials are indexed by: 3.
  file_create_date: ['2023-09-26T12:21:16.160388-07:00']
  Group /general/devices/Neuralynx-Atlas (Device) CS - Neuralynx-Atlas
  experiment_description: The data contained within this file describe a movie watching and new/old recognition task performed in patients with intractable epilepsy implanted with depth electrodes and Behnke-Fried microwires in the human Medical Temporal Lobe (MTL).
  experimenter: ['Julien Dubois, PhD']
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-1 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-1/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-10 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-10/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-11 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-11/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-12 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-12/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-13 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-13/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-14 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-14/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-15 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-15/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-16 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-16/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-17 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-17/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-18 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-18/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-19 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-19/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-2 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-2/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-20 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-20/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-21 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-21/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-22 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-22/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-23 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-23/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-24 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-24/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-25 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-25/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-26 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-26/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-27 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-27/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-28 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-28/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-29 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-29/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-3 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-3/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-30 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-30/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-31 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-31/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-32 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-32/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-33 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-33/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-34 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-34/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-35 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-35/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-36 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-36/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-37 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-37/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-38 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-38/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-39 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-39/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-4 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-4/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-40 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-40/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-41 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-41/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-42 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-42/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-43 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-43/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-44 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-44/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-45 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-45/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-46 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-46/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-47 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-47/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-48 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-48/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-49 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-49/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-5 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-5/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-50 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-50/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-51 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-51/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-52 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-52/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-53 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-53/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-54 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-54/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-55 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-55/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-56 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-56/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-57 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-57/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-58 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-58/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-59 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-59/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-6 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-6/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-60 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-60/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-61 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-61/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-62 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-62/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-63 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-63/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-64 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-64/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-65 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-65/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-66 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-66/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-67 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-67/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-68 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-68/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-69 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-69/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-7 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-7/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-70 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-70/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-71 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-71/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-72 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-72/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-73 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-73/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-74 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-74/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-75 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-75/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-76 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-76/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-77 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-77/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-78 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-78/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-79 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-79/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-8 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-8/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-80 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-80/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-81 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-81/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-82 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-82/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-83 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-83/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-84 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-84/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-85 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-85/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-86 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-86/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-87 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-87/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-88 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-88/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-89 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-89/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-9 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-9/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-90 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-90/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-91 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-91/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-92 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-92/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-93 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-93/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-94 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-94/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-95 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-95/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-96 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-96/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-1 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-1/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-10 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-10/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-11 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-11/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-12 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-12/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-13 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-13/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-14 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-14/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-15 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-15/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-16 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-16/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-17 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-17/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-18 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-18/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-19 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-19/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-2 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-2/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-20 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-20/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-21 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-21/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-22 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-22/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-23 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-23/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-24 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-24/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-25 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-25/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-26 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-26/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-27 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-27/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-28 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-28/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-29 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-29/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-3 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-3/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-30 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-30/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-31 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-31/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-32 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-32/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-33 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-33/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-34 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-34/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-35 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-35/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-36 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-36/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-37 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-37/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-38 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-38/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-39 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-39/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-4 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-4/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-40 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-40/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-41 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-41/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-42 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-42/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-43 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-43/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-44 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-44/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-45 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-45/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-46 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-46/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-47 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-47/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-48 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-48/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-49 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-49/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-5 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-5/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-50 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-50/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-51 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-51/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-52 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-52/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-53 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-53/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-54 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-54/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-55 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-55/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-56 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-56/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-57 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-57/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-58 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-58/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-59 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-59/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-6 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-6/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-60 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-60/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-61 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-61/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-62 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-62/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-63 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-63/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-64 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-64/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-65 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-65/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-66 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-66/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-67 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-67/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-68 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-68/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-69 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-69/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-7 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-7/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-70 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-70/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-71 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-71/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-72 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-72/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-73 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-73/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-74 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-74/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-75 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-75/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-76 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-76/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-77 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-77/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-78 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-78/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-79 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-79/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-8 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-8/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-80 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-80/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-9 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-9/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (176,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (176,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (176,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (176,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/origchannel (VectorData) The original channel ID for the channel | shape = (176,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/origchannel_name (VectorData) The original lab specific channel name for the channel | shape = (176,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/pairwise_distances (VectorData) Pairwise distance between all possible pairs of units on the channel | shape = (176,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the position (+x is posterior) | shape = (176,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the position (+y is inferior) | shape = (176,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the position (+z is right) | shape = (176,) | dtype = float64
  institution: Cedars-Sinai Medical Center
  keywords: ['Intracranial Recordings' 'Intractable Epilepsy' 'Single-Unit Recordings'
   'Cognitive Neuroscience' 'Local field potentials' 'Movie' 'Neurosurgery']
  lab: The Rutishauser Laboratory at Cedars-Sinai Medical Center
  session_id: P41CSR1
  Group /general/subject (Subject) 
  identifier: P41CS_R1
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/actual_response (VectorData) The button pressed during experiment, 1-6, where
                               1:new-sure, 2:new-unsure, 3:new-guessing, 4:old-guessing, 5:old-unsure, 6:old-sure | shape = (41,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (41,) | dtype = int64
  Dataset /intervals/trials/response_confidence (VectorData) The confidence level of response 
                                (1=guessing, 2=unsure, 3=sure) for each each new/old trial | shape = (41,) | dtype = float64
  Dataset /intervals/trials/response_correct (VectorData) Whether the response was correct=1 or incorrect=0 for each new/old trial | shape = (41,) | dtype = float64
  Dataset /intervals/trials/response_time (VectorData) The response time for each new/old trial | shape = (41,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (41,) | dtype = float64
  Dataset /intervals/trials/stim_phase (VectorData) Encoding (movie watching) or recognition phase during the session | shape = (41,) | dtype = object
  Dataset /intervals/trials/stimulus_file (VectorData) The file name for the stimulus | shape = (41,) | dtype = object
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (41,) | dtype = float64
  Group /processing/behavior (ProcessingModule) processed behavioral data
  Group /processing/behavior/Blink (BehavioralTimeSeries) 
  Group /processing/behavior/Blink/TimeSeries (TimeSeries) blink information for R eye; timestamps are start times; data are 'Duration'
  Group /processing/behavior/EyeTracking (EyeTracking) 
  Group /processing/behavior/EyeTracking/SpatialSeries (SpatialSeries) (x,y) of gaze points
  Group /processing/behavior/Fixation (BehavioralTimeSeries) 
  Group /processing/behavior/Fixation/TimeSeries (TimeSeries) fixation information for R eye; timestamps are start times; columns are 
              ['Duration', 'FixationX', 'FixationY', 'Pupil_size_avg']
  Group /processing/behavior/PupilTracking (PupilTracking) 
  Group /processing/behavior/PupilTracking/TimeSeries (TimeSeries) pupil size (number of pixels inside the pupil contour)
  Group /processing/behavior/Saccade (BehavioralTimeSeries) 
  Group /processing/behavior/Saccade/TimeSeries (TimeSeries) saccade information for R eye; timestamps are start times; columns are 
          ['Duration', 'StartX', 'StartY', 'EndX', 'EndY', 'Ampl', 'Pupil_vel']
  Group /processing/ecephys (ProcessingModule) processed extracellular electrophysiology data
  Group /processing/ecephys/LFP_macro (LFP) 
  Group /processing/ecephys/LFP_macro/ElectricalSeries (ElectricalSeries) Local field potentials from macro electrodes. Note that the session starts at 10.0 seconds.
  Dataset /processing/ecephys/LFP_macro/ElectricalSeries/electrodes (DynamicTableRegion) electrodes for macros | shape = (96,) | dtype = int64
  Group /processing/ecephys/LFP_micro (LFP) 
  Group /processing/ecephys/LFP_micro/ElectricalSeries (ElectricalSeries) Local field potentials from micro-wires. Note that the session starts at 10.0 seconds.
  Dataset /processing/ecephys/LFP_micro/ElectricalSeries/electrodes (DynamicTableRegion) electrodes for micros | shape = (80,) | dtype = int64
  session_description: Movie watching and new/old recognition task for session: P41CS_R1
  session_start_time: 2016-08-01T00:00:00-07:00
  Group /stimulus/presentation/movieframe_time (AnnotationSeries) Movie frame numbers associated with time instances during 
                                        the encoding (movie watching) phase [starts counting from 0--Python way]
  timestamps_reference_time: 2016-08-01T00:00:00-07:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/cv2 (VectorData) The mean modified coefficient of variation of variability in the ISI (CV2) | shape = (7,) | dtype = float64
  Dataset /units/electrode_id (VectorData) The id number of corresponding electrode 
                              (used to replace 'electrodes' entry, usage: nwbfile.electrodes[electrode_id]) | shape = (7,) | dtype = int64
  Dataset /units/electrodegroup_label (VectorData) The label for corresponding electrode group 
                              (used to replace 'electrode_group' entry, 
                              usage: nwbfile.electrode_groups[electrodegroup_label]) | shape = (7,) | dtype = object
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (7,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex) Index for VectorData 'electrodes' | shape = (7,) | dtype = uint8
  Dataset /units/id (ElementIdentifiers)  | shape = (7,) | dtype = int64
  Dataset /units/isibelow (VectorData) The proportion of inter-spike intervals (ISIs) which are shorter than 3 ms | shape = (7,) | dtype = float64
  Dataset /units/isolationdist (VectorData) The isolation distance of the unit | shape = (7,) | dtype = float64
  Dataset /units/meanSNR (VectorData) The SNR of the entire waveform of the unit | shape = (7,) | dtype = float64
  Dataset /units/origcluster_id (VectorData) The original OSort cluster id | shape = (7,) | dtype = int64
  Dataset /units/peakSNR (VectorData) The SNR of the mean waveform peak of the unit | shape = (7,) | dtype = float64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (6580,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (7,) | dtype = uint16
  Dataset /units/unit_id (VectorData) The unit id in lab specific format | shape = (7,) | dtype = object
  Dataset /units/unit_id_session (VectorData) The unit id with session info in lab specific format | shape = (7,) | dtype = object
  Dataset /units/waveform_mean_encoding (VectorData) The mean waveform for encoding phase | shape = (7, 256) | dtype = float64
  Dataset /units/waveform_mean_recognition (VectorData) The mean waveform for the recognition phase | shape = (7, 256) | dtype = float64
  Dataset /units/waveform_mean_sampling_rate (VectorData) The sampling rate of waveform | shape = (7, 1) | dtype = int64


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/events_ttl (TimeSeries) The events correspond to the TTL markers for each session. 
                            The TTL markers are the following: 
                            4 = start of the movie, 40-49 = frame number mapping to a log file, 
                            33 = keypress, 7 = start probe for recognition, 9 = startITI, 1 = start fixation, 
                            10 = end fixation, 52 = screen of instruction, 66 = end of experiment
  Group /acquisition/experiment_ids (TimeSeries) The experimentid (or task_id) corresponds to the encoding 
                                   (i.e., movie watching as one trial) or recognition trials. 
                                   The encoding is indexed by: 2. 
                                   The recognition trials are indexed by: 3.
  file_create_date: ['2023-09-26T12:23:14.646843-07:00']
  Group /general/devices/Neuralynx-Atlas (Device) CS - Neuralynx-Atlas
  experiment_description: The data contained within this file describe a movie watching and new/old recognition task performed in patients with intractable epilepsy implanted with depth electrodes and Behnke-Fried microwires in the human Medical Temporal Lobe (MTL).
  experimenter: ['Julien Dubois, PhD']
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-1 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-1/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-10 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-10/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-11 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-11/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-12 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-12/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-13 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-13/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-14 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-14/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-15 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-15/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-16 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-16/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-17 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-17/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-18 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-18/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-19 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-19/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-2 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-2/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-20 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-20/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-21 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-21/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-22 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-22/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-23 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-23/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-24 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-24/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-25 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-25/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-26 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-26/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-27 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-27/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-28 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-28/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-29 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-29/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-3 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-3/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-30 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-30/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-31 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-31/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-32 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-32/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-33 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-33/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-34 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-34/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-35 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-35/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-36 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-36/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-37 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-37/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-38 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-38/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-39 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-39/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-4 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-4/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-40 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-40/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-41 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-41/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-42 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-42/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-43 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-43/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-44 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-44/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-45 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-45/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-46 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-46/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-47 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-47/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-48 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-48/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-49 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-49/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-5 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-5/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-50 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-50/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-51 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-51/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-52 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-52/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-53 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-53/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-54 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-54/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-55 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-55/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-56 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-56/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-57 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-57/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-58 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-58/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-59 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-59/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-6 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-6/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-60 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-60/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-61 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-61/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-62 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-62/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-63 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-63/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-64 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-64/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-65 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-65/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-66 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-66/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-67 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-67/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-68 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-68/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-69 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-69/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-7 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-7/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-70 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-70/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-71 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-71/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-72 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-72/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-73 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-73/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-74 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-74/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-75 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-75/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-76 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-76/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-77 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-77/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-78 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-78/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-79 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-79/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-8 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-8/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-80 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-80/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-81 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-81/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-82 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-82/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-83 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-83/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-84 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-84/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-85 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-85/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-86 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-86/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-87 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-87/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-88 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-88/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-89 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-89/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-9 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-9/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-90 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-90/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-91 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-91/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-92 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-92/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-93 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-93/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-94 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-94/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-95 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-95/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-96 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-96/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-1 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-1/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-10 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-10/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-11 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-11/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-12 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-12/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-13 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-13/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-14 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-14/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-15 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-15/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-16 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-16/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-17 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-17/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-18 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-18/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-19 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-19/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-2 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-2/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-20 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-20/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-21 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-21/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-22 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-22/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-23 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-23/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-24 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-24/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-25 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-25/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-26 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-26/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-27 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-27/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-28 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-28/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-29 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-29/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-3 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-3/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-30 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-30/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-31 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-31/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-32 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-32/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-33 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-33/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-34 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-34/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-35 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-35/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-36 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-36/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-37 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-37/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-38 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-38/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-39 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-39/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-4 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-4/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-40 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-40/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-41 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-41/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-42 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-42/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-43 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-43/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-44 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-44/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-45 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-45/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-46 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-46/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-47 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-47/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-48 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-48/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-49 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-49/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-5 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-5/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-50 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-50/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-51 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-51/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-52 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-52/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-53 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-53/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-54 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-54/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-55 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-55/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-56 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-56/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-57 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-57/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-58 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-58/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-59 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-59/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-6 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-6/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-60 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-60/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-61 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-61/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-62 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-62/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-63 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-63/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-64 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-64/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-7 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-7/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-8 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-8/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-9 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-9/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (160,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (160,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (160,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (160,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/origchannel (VectorData) The original channel ID for the channel | shape = (160,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/origchannel_name (VectorData) The original lab specific channel name for the channel | shape = (160,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/pairwise_distances (VectorData) Pairwise distance between all possible pairs of units on the channel | shape = (160,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the position (+x is posterior) | shape = (160,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the position (+y is inferior) | shape = (160,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the position (+z is right) | shape = (160,) | dtype = float64
  institution: Cedars-Sinai Medical Center
  keywords: ['Intracranial Recordings' 'Intractable Epilepsy' 'Single-Unit Recordings'
   'Cognitive Neuroscience' 'Local field potentials' 'Movie' 'Neurosurgery']
  lab: The Rutishauser Laboratory at Cedars-Sinai Medical Center
  session_id: P42CSR1
  Group /general/subject (Subject) 
  identifier: P42CS_R1
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/actual_response (VectorData) The button pressed during experiment, 1-6, where
                               1:new-sure, 2:new-unsure, 3:new-guessing, 4:old-guessing, 5:old-unsure, 6:old-sure | shape = (41,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (41,) | dtype = int64
  Dataset /intervals/trials/response_confidence (VectorData) The confidence level of response 
                                (1=guessing, 2=unsure, 3=sure) for each each new/old trial | shape = (41,) | dtype = float64
  Dataset /intervals/trials/response_correct (VectorData) Whether the response was correct=1 or incorrect=0 for each new/old trial | shape = (41,) | dtype = float64
  Dataset /intervals/trials/response_time (VectorData) The response time for each new/old trial | shape = (41,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (41,) | dtype = float64
  Dataset /intervals/trials/stim_phase (VectorData) Encoding (movie watching) or recognition phase during the session | shape = (41,) | dtype = object
  Dataset /intervals/trials/stimulus_file (VectorData) The file name for the stimulus | shape = (41,) | dtype = object
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (41,) | dtype = float64
  Group /processing/behavior (ProcessingModule) processed behavioral data
  Group /processing/behavior/Blink (BehavioralTimeSeries) 
  Group /processing/behavior/Blink/TimeSeries (TimeSeries) blink information for R eye; timestamps are start times; data are 'Duration'
  Group /processing/behavior/EyeTracking (EyeTracking) 
  Group /processing/behavior/EyeTracking/SpatialSeries (SpatialSeries) (x,y) of gaze points
  Group /processing/behavior/Fixation (BehavioralTimeSeries) 
  Group /processing/behavior/Fixation/TimeSeries (TimeSeries) fixation information for R eye; timestamps are start times; columns are 
              ['Duration', 'FixationX', 'FixationY', 'Pupil_size_avg']
  Group /processing/behavior/PupilTracking (PupilTracking) 
  Group /processing/behavior/PupilTracking/TimeSeries (TimeSeries) pupil size (number of pixels inside the pupil contour)
  Group /processing/behavior/Saccade (BehavioralTimeSeries) 
  Group /processing/behavior/Saccade/TimeSeries (TimeSeries) saccade information for R eye; timestamps are start times; columns are 
          ['Duration', 'StartX', 'StartY', 'EndX', 'EndY', 'Ampl', 'Pupil_vel']
  Group /processing/ecephys (ProcessingModule) processed extracellular electrophysiology data
  Group /processing/ecephys/LFP_macro (LFP) 
  Group /processing/ecephys/LFP_macro/ElectricalSeries (ElectricalSeries) Local field potentials from macro electrodes. Note that the session starts at 10.0 seconds.
  Dataset /processing/ecephys/LFP_macro/ElectricalSeries/electrodes (DynamicTableRegion) electrodes for macros | shape = (96,) | dtype = int64
  Group /processing/ecephys/LFP_micro (LFP) 
  Group /processing/ecephys/LFP_micro/ElectricalSeries (ElectricalSeries) Local field potentials from micro-wires. Note that the session starts at 10.0 seconds.
  Dataset /processing/ecephys/LFP_micro/ElectricalSeries/electrodes (DynamicTableRegion) electrodes for micros | shape = (64,) | dtype = int64
  session_description: Movie watching and new/old recognition task for session: P42CS_R1
  session_start_time: 2016-08-01T00:00:00-07:00
  Group /stimulus/presentation/movieframe_time (AnnotationSeries) Movie frame numbers associated with time instances during 
                                        the encoding (movie watching) phase [starts counting from 0--Python way]
  timestamps_reference_time: 2016-08-01T00:00:00-07:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/cv2 (VectorData) The mean modified coefficient of variation of variability in the ISI (CV2) | shape = (50,) | dtype = float64
  Dataset /units/electrode_id (VectorData) The id number of corresponding electrode 
                              (used to replace 'electrodes' entry, usage: nwbfile.electrodes[electrode_id]) | shape = (50,) | dtype = int64
  Dataset /units/electrodegroup_label (VectorData) The label for corresponding electrode group 
                              (used to replace 'electrode_group' entry, 
                              usage: nwbfile.electrode_groups[electrodegroup_label]) | shape = (50,) | dtype = object
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (50,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex) Index for VectorData 'electrodes' | shape = (50,) | dtype = uint8
  Dataset /units/id (ElementIdentifiers)  | shape = (50,) | dtype = int64
  Dataset /units/isibelow (VectorData) The proportion of inter-spike intervals (ISIs) which are shorter than 3 ms | shape = (50,) | dtype = float64
  Dataset /units/isolationdist (VectorData) The isolation distance of the unit | shape = (50,) | dtype = float64
  Dataset /units/meanSNR (VectorData) The SNR of the entire waveform of the unit | shape = (50,) | dtype = float64
  Dataset /units/origcluster_id (VectorData) The original OSort cluster id | shape = (50,) | dtype = int64
  Dataset /units/peakSNR (VectorData) The SNR of the mean waveform peak of the unit | shape = (50,) | dtype = float64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (136628,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (50,) | dtype = uint32
  Dataset /units/unit_id (VectorData) The unit id in lab specific format | shape = (50,) | dtype = object
  Dataset /units/unit_id_session (VectorData) The unit id with session info in lab specific format | shape = (50,) | dtype = object
  Dataset /units/waveform_mean_encoding (VectorData) The mean waveform for encoding phase | shape = (50, 256) | dtype = float64
  Dataset /units/waveform_mean_recognition (VectorData) The mean waveform for the recognition phase | shape = (50, 256) | dtype = float64
  Dataset /units/waveform_mean_sampling_rate (VectorData) The sampling rate of waveform | shape = (50, 1) | dtype = int64


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/events_ttl (TimeSeries) The events correspond to the TTL markers for each session. 
                            The TTL markers are the following: 
                            4 = start of the movie, 40-49 = frame number mapping to a log file, 
                            33 = keypress, 7 = start probe for recognition, 9 = startITI, 1 = start fixation, 
                            10 = end fixation, 52 = screen of instruction, 66 = end of experiment
  Group /acquisition/experiment_ids (TimeSeries) The experimentid (or task_id) corresponds to the encoding 
                                   (i.e., movie watching as one trial) or recognition trials. 
                                   The encoding is indexed by: 2. 
                                   The recognition trials are indexed by: 3.
  file_create_date: ['2023-09-26T12:35:12.721297-07:00']
  Group /general/devices/Neuralynx-Atlas (Device) CS - Neuralynx-Atlas
  experiment_description: The data contained within this file describe a movie watching and new/old recognition task performed in patients with intractable epilepsy implanted with depth electrodes and Behnke-Fried microwires in the human Medical Temporal Lobe (MTL).
  experimenter: ['Julien Dubois, PhD']
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-1 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-1/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-10 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-10/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-100 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-100/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-101 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-101/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-102 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-102/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-103 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-103/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-104 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-104/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-105 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-105/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-106 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-106/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-107 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-107/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-108 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-108/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-109 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-109/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-11 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-11/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-110 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-110/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-111 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-111/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-112 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-112/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-113 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-113/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-114 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-114/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-115 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-115/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-116 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-116/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-117 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-117/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-118 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-118/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-119 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-119/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-12 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-12/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-120 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-120/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-121 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-121/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-122 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-122/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-123 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-123/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-124 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-124/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-125 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-125/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-126 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-126/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-127 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-127/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-128 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-128/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-13 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-13/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-14 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-14/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-15 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-15/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-16 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-16/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-17 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-17/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-18 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-18/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-19 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-19/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-2 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-2/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-20 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-20/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-21 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-21/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-22 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-22/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-23 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-23/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-24 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-24/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-25 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-25/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-26 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-26/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-27 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-27/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-28 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-28/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-29 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-29/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-3 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-3/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-30 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-30/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-31 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-31/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-32 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-32/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-33 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-33/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-34 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-34/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-35 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-35/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-36 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-36/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-37 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-37/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-38 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-38/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-39 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-39/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-4 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-4/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-40 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-40/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-41 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-41/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-42 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-42/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-43 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-43/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-44 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-44/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-45 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-45/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-46 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-46/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-47 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-47/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-48 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-48/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-49 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-49/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-5 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-5/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-50 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-50/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-51 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-51/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-52 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-52/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-53 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-53/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-54 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-54/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-55 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-55/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-56 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-56/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-57 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-57/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-58 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-58/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-59 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-59/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-6 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-6/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-60 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-60/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-61 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-61/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-62 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-62/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-63 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-63/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-64 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-64/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-65 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-65/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-66 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-66/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-67 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-67/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-68 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-68/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-69 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-69/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-7 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-7/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-70 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-70/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-71 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-71/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-72 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-72/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-73 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-73/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-74 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-74/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-75 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-75/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-76 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-76/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-77 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-77/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-78 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-78/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-79 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-79/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-8 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-8/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-80 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-80/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-81 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-81/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-82 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-82/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-83 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-83/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-84 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-84/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-85 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-85/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-86 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-86/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-87 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-87/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-88 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-88/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-89 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-89/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-9 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-9/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-90 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-90/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-91 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-91/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-92 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-92/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-93 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-93/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-94 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-94/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-95 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-95/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-96 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-96/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-97 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-97/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-98 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-98/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-99 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-99/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-1 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-1/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-10 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-10/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-11 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-11/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-12 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-12/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-13 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-13/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-14 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-14/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-15 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-15/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-16 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-16/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-17 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-17/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-18 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-18/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-19 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-19/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-2 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-2/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-20 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-20/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-21 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-21/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-22 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-22/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-23 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-23/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-24 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-24/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-25 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-25/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-26 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-26/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-27 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-27/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-28 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-28/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-29 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-29/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-3 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-3/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-30 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-30/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-31 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-31/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-32 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-32/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-33 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-33/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-34 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-34/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-35 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-35/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-36 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-36/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-37 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-37/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-38 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-38/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-39 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-39/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-4 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-4/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-40 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-40/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-41 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-41/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-42 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-42/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-43 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-43/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-44 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-44/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-45 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-45/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-46 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-46/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-47 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-47/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-48 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-48/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-49 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-49/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-5 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-5/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-50 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-50/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-51 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-51/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-52 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-52/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-53 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-53/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-54 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-54/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-55 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-55/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-56 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-56/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-57 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-57/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-58 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-58/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-59 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-59/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-6 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-6/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-60 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-60/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-61 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-61/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-62 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-62/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-63 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-63/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-64 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-64/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-65 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-65/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-66 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-66/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-67 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-67/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-68 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-68/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-69 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-69/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-7 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-7/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-70 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-70/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-71 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-71/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-72 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-72/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-73 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-73/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-74 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-74/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-75 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-75/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-76 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-76/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-77 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-77/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-78 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-78/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-79 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-79/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-8 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-8/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-80 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-80/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-9 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-9/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (208,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (208,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (208,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (208,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/origchannel (VectorData) The original channel ID for the channel | shape = (208,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/origchannel_name (VectorData) The original lab specific channel name for the channel | shape = (208,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/pairwise_distances (VectorData) Pairwise distance between all possible pairs of units on the channel | shape = (208,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the position (+x is posterior) | shape = (208,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the position (+y is inferior) | shape = (208,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the position (+z is right) | shape = (208,) | dtype = float64
  institution: Cedars-Sinai Medical Center
  keywords: ['Intracranial Recordings' 'Intractable Epilepsy' 'Single-Unit Recordings'
   'Cognitive Neuroscience' 'Local field potentials' 'Movie' 'Neurosurgery']
  lab: The Rutishauser Laboratory at Cedars-Sinai Medical Center
  session_id: P51CSR1
  Group /general/subject (Subject) 
  identifier: P51CS_R1
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/actual_response (VectorData) The button pressed during experiment, 1-6, where
                               1:new-sure, 2:new-unsure, 3:new-guessing, 4:old-guessing, 5:old-unsure, 6:old-sure | shape = (41,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (41,) | dtype = int64
  Dataset /intervals/trials/response_confidence (VectorData) The confidence level of response 
                                (1=guessing, 2=unsure, 3=sure) for each each new/old trial | shape = (41,) | dtype = float64
  Dataset /intervals/trials/response_correct (VectorData) Whether the response was correct=1 or incorrect=0 for each new/old trial | shape = (41,) | dtype = float64
  Dataset /intervals/trials/response_time (VectorData) The response time for each new/old trial | shape = (41,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (41,) | dtype = float64
  Dataset /intervals/trials/stim_phase (VectorData) Encoding (movie watching) or recognition phase during the session | shape = (41,) | dtype = object
  Dataset /intervals/trials/stimulus_file (VectorData) The file name for the stimulus | shape = (41,) | dtype = object
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (41,) | dtype = float64
  Group /processing/behavior (ProcessingModule) processed behavioral data
  Group /processing/behavior/Blink (BehavioralTimeSeries) 
  Group /processing/behavior/Blink/TimeSeries (TimeSeries) blink information for L eye; timestamps are start times; data are 'Duration'
  Group /processing/behavior/EyeTracking (EyeTracking) 
  Group /processing/behavior/EyeTracking/SpatialSeries (SpatialSeries) (x,y) of gaze points
  Group /processing/behavior/Fixation (BehavioralTimeSeries) 
  Group /processing/behavior/Fixation/TimeSeries (TimeSeries) fixation information for L eye; timestamps are start times; columns are 
              ['Duration', 'FixationX', 'FixationY', 'Pupil_size_avg']
  Group /processing/behavior/PupilTracking (PupilTracking) 
  Group /processing/behavior/PupilTracking/TimeSeries (TimeSeries) pupil size (number of pixels inside the pupil contour)
  Group /processing/behavior/Saccade (BehavioralTimeSeries) 
  Group /processing/behavior/Saccade/TimeSeries (TimeSeries) saccade information for L eye; timestamps are start times; columns are 
          ['Duration', 'StartX', 'StartY', 'EndX', 'EndY', 'Ampl', 'Pupil_vel']
  Group /processing/ecephys (ProcessingModule) processed extracellular electrophysiology data
  Group /processing/ecephys/LFP_macro (LFP) 
  Group /processing/ecephys/LFP_macro/ElectricalSeries (ElectricalSeries) Local field potentials from macro electrodes. Note that the session starts at 10.0 seconds.
  Dataset /processing/ecephys/LFP_macro/ElectricalSeries/electrodes (DynamicTableRegion) electrodes for macros | shape = (128,) | dtype = int64
  Group /processing/ecephys/LFP_micro (LFP) 
  Group /processing/ecephys/LFP_micro/ElectricalSeries (ElectricalSeries) Local field potentials from micro-wires. Note that the session starts at 10.0 seconds.
  Dataset /processing/ecephys/LFP_micro/ElectricalSeries/electrodes (DynamicTableRegion) electrodes for micros | shape = (80,) | dtype = int64
  session_description: Movie watching and new/old recognition task for session: P51CS_R1
  session_start_time: 2017-07-01T00:00:00-07:00
  Group /stimulus/presentation/movieframe_time (AnnotationSeries) Movie frame numbers associated with time instances during 
                                        the encoding (movie watching) phase [starts counting from 0--Python way]
  timestamps_reference_time: 2017-07-01T00:00:00-07:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/cv2 (VectorData) The mean modified coefficient of variation of variability in the ISI (CV2) | shape = (30,) | dtype = float64
  Dataset /units/electrode_id (VectorData) The id number of corresponding electrode 
                              (used to replace 'electrodes' entry, usage: nwbfile.electrodes[electrode_id]) | shape = (30,) | dtype = int64
  Dataset /units/electrodegroup_label (VectorData) The label for corresponding electrode group 
                              (used to replace 'electrode_group' entry, 
                              usage: nwbfile.electrode_groups[electrodegroup_label]) | shape = (30,) | dtype = object
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (30,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex) Index for VectorData 'electrodes' | shape = (30,) | dtype = uint8
  Dataset /units/id (ElementIdentifiers)  | shape = (30,) | dtype = int64
  Dataset /units/isibelow (VectorData) The proportion of inter-spike intervals (ISIs) which are shorter than 3 ms | shape = (30,) | dtype = float64
  Dataset /units/isolationdist (VectorData) The isolation distance of the unit | shape = (30,) | dtype = float64
  Dataset /units/meanSNR (VectorData) The SNR of the entire waveform of the unit | shape = (30,) | dtype = float64
  Dataset /units/origcluster_id (VectorData) The original OSort cluster id | shape = (30,) | dtype = int64
  Dataset /units/peakSNR (VectorData) The SNR of the mean waveform peak of the unit | shape = (30,) | dtype = float64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (17044,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (30,) | dtype = uint16
  Dataset /units/unit_id (VectorData) The unit id in lab specific format | shape = (30,) | dtype = object
  Dataset /units/unit_id_session (VectorData) The unit id with session info in lab specific format | shape = (30,) | dtype = object
  Dataset /units/waveform_mean_encoding (VectorData) The mean waveform for encoding phase | shape = (30, 256) | dtype = float64
  Dataset /units/waveform_mean_recognition (VectorData) The mean waveform for the recognition phase | shape = (30, 256) | dtype = float64
  Dataset /units/waveform_mean_sampling_rate (VectorData) The sampling rate of waveform | shape = (30, 1) | dtype = int64


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/events_ttl (TimeSeries) The events correspond to the TTL markers for each session. 
                            The TTL markers are the following: 
                            4 = start of the movie, 40-49 = frame number mapping to a log file, 
                            33 = keypress, 7 = start probe for recognition, 9 = startITI, 1 = start fixation, 
                            10 = end fixation, 52 = screen of instruction, 66 = end of experiment
  Group /acquisition/experiment_ids (TimeSeries) The experimentid (or task_id) corresponds to the encoding 
                                   (i.e., movie watching as one trial) or recognition trials. 
                                   The encoding is indexed by: 2. 
                                   The recognition trials are indexed by: 3.
  file_create_date: ['2023-09-26T12:44:27.471548-07:00']
  Group /general/devices/Neuralynx-Atlas (Device) CS - Neuralynx-Atlas
  experiment_description: The data contained within this file describe a movie watching and new/old recognition task performed in patients with intractable epilepsy implanted with depth electrodes and Behnke-Fried microwires in the human Medical Temporal Lobe (MTL).
  experimenter: ['Julien Dubois, PhD']
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-1 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-1/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-10 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-10/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-100 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-100/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-101 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-101/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-102 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-102/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-103 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-103/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-104 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-104/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-105 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-105/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-106 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-106/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-11 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-11/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-12 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-12/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-13 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-13/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-14 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-14/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-15 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-15/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-16 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-16/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-17 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-17/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-18 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-18/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-19 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-19/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-2 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-2/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-20 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-20/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-21 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-21/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-22 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-22/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-23 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-23/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-24 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-24/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-25 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-25/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-26 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-26/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-27 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-27/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-28 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-28/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-29 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-29/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-3 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-3/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-30 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-30/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-31 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-31/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-32 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-32/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-33 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-33/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-34 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-34/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-35 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-35/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-36 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-36/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-37 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-37/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-38 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-38/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-39 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-39/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-4 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-4/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-40 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-40/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-41 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-41/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-42 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-42/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-43 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-43/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-44 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-44/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-45 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-45/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-46 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-46/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-47 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-47/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-48 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-48/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-49 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-49/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-5 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-5/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-50 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-50/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-51 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-51/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-52 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-52/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-53 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-53/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-54 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-54/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-55 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-55/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-56 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-56/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-57 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-57/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-58 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-58/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-59 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-59/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-6 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-6/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-60 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-60/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-61 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-61/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-62 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-62/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-63 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-63/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-64 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-64/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-65 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-65/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-66 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-66/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-67 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-67/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-68 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-68/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-69 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-69/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-7 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-7/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-70 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-70/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-71 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-71/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-72 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-72/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-73 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-73/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-74 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-74/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-75 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-75/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-76 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-76/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-77 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-77/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-78 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-78/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-79 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-79/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-8 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-8/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-80 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-80/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-81 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-81/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-82 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-82/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-83 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-83/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-84 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-84/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-85 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-85/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-86 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-86/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-87 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-87/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-88 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-88/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-89 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-89/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-9 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-9/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-90 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-90/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-91 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-91/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-92 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-92/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-93 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-93/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-94 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-94/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-95 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-95/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-96 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-96/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-97 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-97/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-98 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-98/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-99 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-99/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-1 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-1/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-10 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-10/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-11 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-11/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-12 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-12/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-13 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-13/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-14 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-14/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-15 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-15/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-16 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-16/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-17 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-17/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-18 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-18/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-19 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-19/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-2 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-2/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-20 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-20/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-21 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-21/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-22 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-22/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-23 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-23/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-24 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-24/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-25 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-25/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-26 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-26/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-27 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-27/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-28 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-28/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-29 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-29/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-3 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-3/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-30 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-30/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-31 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-31/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-32 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-32/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-33 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-33/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-34 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-34/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-35 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-35/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-36 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-36/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-37 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-37/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-38 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-38/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-39 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-39/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-4 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-4/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-40 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-40/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-41 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-41/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-42 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-42/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-43 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-43/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-44 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-44/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-45 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-45/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-46 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-46/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-47 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-47/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-48 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-48/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-49 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-49/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-5 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-5/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-50 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-50/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-51 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-51/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-52 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-52/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-53 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-53/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-54 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-54/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-55 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-55/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-56 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-56/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-57 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-57/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-58 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-58/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-59 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-59/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-6 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-6/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-60 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-60/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-61 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-61/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-62 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-62/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-63 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-63/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-64 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-64/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-65 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-65/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-66 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-66/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-67 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-67/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-68 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-68/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-69 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-69/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-7 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-7/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-70 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-70/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-71 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-71/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-72 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-72/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-73 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-73/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-74 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-74/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-75 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-75/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-76 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-76/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-77 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-77/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-78 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-78/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-79 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-79/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-8 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-8/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-80 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-80/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-9 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-9/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (186,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (186,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (186,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (186,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/origchannel (VectorData) The original channel ID for the channel | shape = (186,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/origchannel_name (VectorData) The original lab specific channel name for the channel | shape = (186,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/pairwise_distances (VectorData) Pairwise distance between all possible pairs of units on the channel | shape = (186,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the position (+x is posterior) | shape = (186,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the position (+y is inferior) | shape = (186,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the position (+z is right) | shape = (186,) | dtype = float64
  institution: Cedars-Sinai Medical Center
  keywords: ['Intracranial Recordings' 'Intractable Epilepsy' 'Single-Unit Recordings'
   'Cognitive Neuroscience' 'Local field potentials' 'Movie' 'Neurosurgery']
  lab: The Rutishauser Laboratory at Cedars-Sinai Medical Center
  session_id: P56CSR1
  Group /general/subject (Subject) 
  identifier: P56CS_R1
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/actual_response (VectorData) The button pressed during experiment, 1-6, where
                               1:new-sure, 2:new-unsure, 3:new-guessing, 4:old-guessing, 5:old-unsure, 6:old-sure | shape = (41,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (41,) | dtype = int64
  Dataset /intervals/trials/response_confidence (VectorData) The confidence level of response 
                                (1=guessing, 2=unsure, 3=sure) for each each new/old trial | shape = (41,) | dtype = float64
  Dataset /intervals/trials/response_correct (VectorData) Whether the response was correct=1 or incorrect=0 for each new/old trial | shape = (41,) | dtype = float64
  Dataset /intervals/trials/response_time (VectorData) The response time for each new/old trial | shape = (41,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (41,) | dtype = float64
  Dataset /intervals/trials/stim_phase (VectorData) Encoding (movie watching) or recognition phase during the session | shape = (41,) | dtype = object
  Dataset /intervals/trials/stimulus_file (VectorData) The file name for the stimulus | shape = (41,) | dtype = object
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (41,) | dtype = float64
  Group /processing/behavior (ProcessingModule) processed behavioral data
  Group /processing/behavior/Blink (BehavioralTimeSeries) 
  Group /processing/behavior/Blink/TimeSeries (TimeSeries) blink information for L eye; timestamps are start times; data are 'Duration'
  Group /processing/behavior/EyeTracking (EyeTracking) 
  Group /processing/behavior/EyeTracking/SpatialSeries (SpatialSeries) (x,y) of gaze points
  Group /processing/behavior/Fixation (BehavioralTimeSeries) 
  Group /processing/behavior/Fixation/TimeSeries (TimeSeries) fixation information for L eye; timestamps are start times; columns are 
              ['Duration', 'FixationX', 'FixationY', 'Pupil_size_avg']
  Group /processing/behavior/PupilTracking (PupilTracking) 
  Group /processing/behavior/PupilTracking/TimeSeries (TimeSeries) pupil size (number of pixels inside the pupil contour)
  Group /processing/behavior/Saccade (BehavioralTimeSeries) 
  Group /processing/behavior/Saccade/TimeSeries (TimeSeries) saccade information for L eye; timestamps are start times; columns are 
          ['Duration', 'StartX', 'StartY', 'EndX', 'EndY', 'Ampl', 'Pupil_vel']
  Group /processing/ecephys (ProcessingModule) processed extracellular electrophysiology data
  Group /processing/ecephys/LFP_macro (LFP) 
  Group /processing/ecephys/LFP_macro/ElectricalSeries (ElectricalSeries) Local field potentials from macro electrodes. Note that the session starts at 10.0 seconds.
  Dataset /processing/ecephys/LFP_macro/ElectricalSeries/electrodes (DynamicTableRegion) electrodes for macros | shape = (106,) | dtype = int64
  Group /processing/ecephys/LFP_micro (LFP) 
  Group /processing/ecephys/LFP_micro/ElectricalSeries (ElectricalSeries) Local field potentials from micro-wires. Note that the session starts at 10.0 seconds.
  Dataset /processing/ecephys/LFP_micro/ElectricalSeries/electrodes (DynamicTableRegion) electrodes for micros | shape = (80,) | dtype = int64
  session_description: Movie watching and new/old recognition task for session: P56CS_R1
  session_start_time: 2018-04-01T00:00:00-07:00
  Group /stimulus/presentation/movieframe_time (AnnotationSeries) Movie frame numbers associated with time instances during 
                                        the encoding (movie watching) phase [starts counting from 0--Python way]
  timestamps_reference_time: 2018-04-01T00:00:00-07:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/cv2 (VectorData) The mean modified coefficient of variation of variability in the ISI (CV2) | shape = (30,) | dtype = float64
  Dataset /units/electrode_id (VectorData) The id number of corresponding electrode 
                              (used to replace 'electrodes' entry, usage: nwbfile.electrodes[electrode_id]) | shape = (30,) | dtype = int64
  Dataset /units/electrodegroup_label (VectorData) The label for corresponding electrode group 
                              (used to replace 'electrode_group' entry, 
                              usage: nwbfile.electrode_groups[electrodegroup_label]) | shape = (30,) | dtype = object
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (30,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex) Index for VectorData 'electrodes' | shape = (30,) | dtype = uint8
  Dataset /units/id (ElementIdentifiers)  | shape = (30,) | dtype = int64
  Dataset /units/isibelow (VectorData) The proportion of inter-spike intervals (ISIs) which are shorter than 3 ms | shape = (30,) | dtype = float64
  Dataset /units/isolationdist (VectorData) The isolation distance of the unit | shape = (30,) | dtype = float64
  Dataset /units/meanSNR (VectorData) The SNR of the entire waveform of the unit | shape = (30,) | dtype = float64
  Dataset /units/origcluster_id (VectorData) The original OSort cluster id | shape = (30,) | dtype = int64
  Dataset /units/peakSNR (VectorData) The SNR of the mean waveform peak of the unit | shape = (30,) | dtype = float64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (174808,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (30,) | dtype = uint32
  Dataset /units/unit_id (VectorData) The unit id in lab specific format | shape = (30,) | dtype = object
  Dataset /units/unit_id_session (VectorData) The unit id with session info in lab specific format | shape = (30,) | dtype = object
  Dataset /units/waveform_mean_encoding (VectorData) The mean waveform for encoding phase | shape = (30, 256) | dtype = float64
  Dataset /units/waveform_mean_recognition (VectorData) The mean waveform for the recognition phase | shape = (30, 256) | dtype = float64
  Dataset /units/waveform_mean_sampling_rate (VectorData) The sampling rate of waveform | shape = (30, 1) | dtype = int64


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  Group /acquisition/events_ttl (TimeSeries) The events correspond to the TTL markers for each session. 
                            The TTL markers are the following: 
                            4 = start of the movie, 40-49 = frame number mapping to a log file, 
                            33 = keypress, 7 = start probe for recognition, 9 = startITI, 1 = start fixation, 
                            10 = end fixation, 52 = screen of instruction, 66 = end of experiment
  Group /acquisition/experiment_ids (TimeSeries) The experimentid (or task_id) corresponds to the encoding 
                                   (i.e., movie watching as one trial) or recognition trials. 
                                   The encoding is indexed by: 2. 
                                   The recognition trials are indexed by: 3.
  file_create_date: ['2023-09-26T12:47:07.277467-07:00']
  Group /general/devices/Neuralynx-Atlas (Device) CS - Neuralynx-Atlas
  experiment_description: The data contained within this file describe a movie watching and new/old recognition task performed in patients with intractable epilepsy implanted with depth electrodes and Behnke-Fried microwires in the human Medical Temporal Lobe (MTL).
  experimenter: ['Julien Dubois, PhD']
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-1 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-1/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-10 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-10/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-100 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-100/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-101 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-101/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-102 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-102/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-11 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-11/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-12 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-12/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-13 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-13/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-14 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-14/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-15 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-15/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-16 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-16/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-17 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-17/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-18 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-18/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-19 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-19/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-2 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-2/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-20 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-20/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-21 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-21/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-22 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-22/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-23 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-23/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-24 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-24/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-25 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-25/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-26 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-26/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-27 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-27/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-28 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-28/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-29 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-29/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-3 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-3/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-30 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-30/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-31 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-31/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-32 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-32/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-33 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-33/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-34 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-34/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-35 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-35/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-36 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-36/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-37 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-37/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-38 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-38/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-39 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-39/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-4 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-4/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-40 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-40/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-41 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-41/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-42 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-42/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-43 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-43/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-44 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-44/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-45 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-45/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-46 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-46/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-47 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-47/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-48 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-48/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-49 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-49/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-5 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-5/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-50 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-50/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-51 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-51/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-52 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-52/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-53 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-53/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-54 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-54/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-55 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-55/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-56 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-56/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-57 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-57/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-58 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-58/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-59 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-59/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-6 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-6/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-60 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-60/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-61 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-61/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-62 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-62/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-63 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-63/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-64 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-64/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-65 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-65/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-66 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-66/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-67 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-67/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-68 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-68/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-69 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-69/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-7 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-7/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-70 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-70/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-71 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-71/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-72 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-72/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-73 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-73/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-74 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-74/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-75 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-75/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-76 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-76/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-77 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-77/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-78 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-78/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-79 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-79/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-8 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-8/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-80 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-80/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-81 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-81/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-82 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-82/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-83 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-83/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-84 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-84/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-85 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-85/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-86 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-86/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-87 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-87/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-88 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-88/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-89 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-89/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-9 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-9/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-90 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-90/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-91 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-91/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-92 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-92/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-93 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-93/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-94 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-94/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-95 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-95/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-96 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-96/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-97 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-97/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-98 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-98/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-99 (ElectrodeGroup) macros
  Group /general/extracellular_ephys/Neuralynx-Atlas-macros-99/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-1 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-1/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-10 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-10/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-11 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-11/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-12 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-12/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-13 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-13/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-14 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-14/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-15 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-15/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-16 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-16/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-17 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-17/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-18 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-18/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-19 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-19/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-2 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-2/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-20 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-20/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-21 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-21/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-22 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-22/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-23 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-23/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-24 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-24/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-25 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-25/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-26 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-26/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-27 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-27/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-28 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-28/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-29 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-29/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-3 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-3/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-30 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-30/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-31 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-31/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-32 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-32/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-33 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-33/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-34 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-34/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-35 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-35/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-36 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-36/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-37 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-37/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-38 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-38/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-39 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-39/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-4 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-4/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-40 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-40/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-41 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-41/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-42 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-42/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-43 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-43/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-44 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-44/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-45 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-45/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-46 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-46/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-47 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-47/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-48 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-48/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-49 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-49/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-5 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-5/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-50 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-50/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-51 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-51/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-52 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-52/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-53 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-53/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-54 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-54/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-55 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-55/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-56 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-56/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-57 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-57/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-58 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-58/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-59 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-59/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-6 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-6/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-60 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-60/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-61 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-61/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-62 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-62/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-63 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-63/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-64 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-64/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-65 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-65/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-66 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-66/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-67 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-67/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-68 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-68/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-69 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-69/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-7 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-7/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-70 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-70/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-71 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-71/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-72 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-72/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-73 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-73/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-74 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-74/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-75 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-75/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-76 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-76/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-77 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-77/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-78 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-78/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-79 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-79/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-8 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-8/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-80 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-80/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-9 (ElectrodeGroup) Behnke Fried/Micro Inner Wire Bundle (Behnke-Fried BF08R-SP05X-000 and WB09R-SP00X-0B6; Ad-Tech Medical)
  Group /general/extracellular_ephys/Neuralynx-Atlas-microwire-9/device (Device) CS - Neuralynx-Atlas
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (182,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (182,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (182,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (182,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/origchannel (VectorData) The original channel ID for the channel | shape = (182,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/origchannel_name (VectorData) The original lab specific channel name for the channel | shape = (182,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/pairwise_distances (VectorData) Pairwise distance between all possible pairs of units on the channel | shape = (182,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the position (+x is posterior) | shape = (182,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the position (+y is inferior) | shape = (182,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the position (+z is right) | shape = (182,) | dtype = float64
  institution: Cedars-Sinai Medical Center
  keywords: ['Intracranial Recordings' 'Intractable Epilepsy' 'Single-Unit Recordings'
   'Cognitive Neuroscience' 'Local field potentials' 'Movie' 'Neurosurgery']
  lab: The Rutishauser Laboratory at Cedars-Sinai Medical Center
  session_id: P57CSR1
  Group /general/subject (Subject) 
  identifier: P57CS_R1
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/actual_response (VectorData) The button pressed during experiment, 1-6, where
                               1:new-sure, 2:new-unsure, 3:new-guessing, 4:old-guessing, 5:old-unsure, 6:old-sure | shape = (41,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (41,) | dtype = int64
  Dataset /intervals/trials/response_confidence (VectorData) The confidence level of response 
                                (1=guessing, 2=unsure, 3=sure) for each each new/old trial | shape = (41,) | dtype = float64
  Dataset /intervals/trials/response_correct (VectorData) Whether the response was correct=1 or incorrect=0 for each new/old trial | shape = (41,) | dtype = float64
  Dataset /intervals/trials/response_time (VectorData) The response time for each new/old trial | shape = (41,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (41,) | dtype = float64
  Dataset /intervals/trials/stim_phase (VectorData) Encoding (movie watching) or recognition phase during the session | shape = (41,) | dtype = object
  Dataset /intervals/trials/stimulus_file (VectorData) The file name for the stimulus | shape = (41,) | dtype = object
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (41,) | dtype = float64
  Group /processing/behavior (ProcessingModule) processed behavioral data
  Group /processing/behavior/Blink (BehavioralTimeSeries) 
  Group /processing/behavior/Blink/TimeSeries (TimeSeries) blink information for L eye; timestamps are start times; data are 'Duration'
  Group /processing/behavior/EyeTracking (EyeTracking) 
  Group /processing/behavior/EyeTracking/SpatialSeries (SpatialSeries) (x,y) of gaze points
  Group /processing/behavior/Fixation (BehavioralTimeSeries) 
  Group /processing/behavior/Fixation/TimeSeries (TimeSeries) fixation information for L eye; timestamps are start times; columns are 
              ['Duration', 'FixationX', 'FixationY', 'Pupil_size_avg']
  Group /processing/behavior/PupilTracking (PupilTracking) 
  Group /processing/behavior/PupilTracking/TimeSeries (TimeSeries) pupil size (number of pixels inside the pupil contour)
  Group /processing/behavior/Saccade (BehavioralTimeSeries) 
  Group /processing/behavior/Saccade/TimeSeries (TimeSeries) saccade information for L eye; timestamps are start times; columns are 
          ['Duration', 'StartX', 'StartY', 'EndX', 'EndY', 'Ampl', 'Pupil_vel']
  Group /processing/ecephys (ProcessingModule) processed extracellular electrophysiology data
  Group /processing/ecephys/LFP_macro (LFP) 
  Group /processing/ecephys/LFP_macro/ElectricalSeries (ElectricalSeries) Local field potentials from macro electrodes. Note that the session starts at 10.0 seconds.
  Dataset /processing/ecephys/LFP_macro/ElectricalSeries/electrodes (DynamicTableRegion) electrodes for macros | shape = (102,) | dtype = int64
  Group /processing/ecephys/LFP_micro (LFP) 
  Group /processing/ecephys/LFP_micro/ElectricalSeries (ElectricalSeries) Local field potentials from micro-wires. Note that the session starts at 10.0 seconds.
  Dataset /processing/ecephys/LFP_micro/ElectricalSeries/electrodes (DynamicTableRegion) electrodes for micros | shape = (80,) | dtype = int64
  session_description: Movie watching and new/old recognition task for session: P57CS_R1
  session_start_time: 2018-06-01T00:00:00-07:00
  Group /stimulus/presentation/movieframe_time (AnnotationSeries) Movie frame numbers associated with time instances during 
                                        the encoding (movie watching) phase [starts counting from 0--Python way]
  timestamps_reference_time: 2018-06-01T00:00:00-07:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/cv2 (VectorData) The mean modified coefficient of variation of variability in the ISI (CV2) | shape = (33,) | dtype = float64
  Dataset /units/electrode_id (VectorData) The id number of corresponding electrode 
                              (used to replace 'electrodes' entry, usage: nwbfile.electrodes[electrode_id]) | shape = (33,) | dtype = int64
  Dataset /units/electrodegroup_label (VectorData) The label for corresponding electrode group 
                              (used to replace 'electrode_group' entry, 
                              usage: nwbfile.electrode_groups[electrodegroup_label]) | shape = (33,) | dtype = object
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (33,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex) Index for VectorData 'electrodes' | shape = (33,) | dtype = uint8
  Dataset /units/id (ElementIdentifiers)  | shape = (33,) | dtype = int64
  Dataset /units/isibelow (VectorData) The proportion of inter-spike intervals (ISIs) which are shorter than 3 ms | shape = (33,) | dtype = float64
  Dataset /units/isolationdist (VectorData) The isolation distance of the unit | shape = (33,) | dtype = float64
  Dataset /units/meanSNR (VectorData) The SNR of the entire waveform of the unit | shape = (33,) | dtype = float64
  Dataset /units/origcluster_id (VectorData) The original OSort cluster id | shape = (33,) | dtype = int64
  Dataset /units/peakSNR (VectorData) The SNR of the mean waveform peak of the unit | shape = (33,) | dtype = float64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (59864,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (33,) | dtype = uint16
  Dataset /units/unit_id (VectorData) The unit id in lab specific format | shape = (33,) | dtype = object
  Dataset /units/unit_id_session (VectorData) The unit id with session info in lab specific format | shape = (33,) | dtype = object
  Dataset /units/waveform_mean_encoding (VectorData) The mean waveform for encoding phase | shape = (33, 256) | dtype = float64
  Dataset /units/waveform_mean_recognition (VectorData) The mean waveform for the recognition phase | shape = (33, 256) | dtype = float64
  Dataset /units/waveform_mean_sampling_rate (VectorData) The sampling rate of waveform | shape = (33, 1) | dtype = int64
