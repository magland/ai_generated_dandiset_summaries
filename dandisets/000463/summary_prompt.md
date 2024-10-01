
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000463/draft
name: Electrophysiological Recordings in Anesthetized Rats in the Primary Somatosensory Cortex with Phased Ultrasound Array Stimulation
contributor: [{'name': 'Ramachandran, Sandhya', 'email': 's.ramachandran8@gmail.com', 'roleName': ['dcite:ContactPerson', 'dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'He, Bin', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Yu, Kai', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Gao, Huan', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'NIH NS124564', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'contactPoint': [], 'includeInCitation': False}, {'name': 'NIH EB029354', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'contactPoint': [], 'includeInCitation': False}, {'name': 'Carnegie Mellon University', 'roleName': ['dcite:Affiliation'], 'schemaKey': 'Organization', 'contactPoint': [], 'includeInCitation': False}]
description: In these recordings, we test different intensities and PRFs (pulse repetition frequencies) of ultrasound stimulation using a phased ultrasound array to stimulate the somatosensory cortex of rats anesthetized with 2% isoflurane through inhalation. Recordings are taken using 32 channel Neuronexus electrodes. Ultrasound stimulation is delivered every 2.5 seconds, and each recording has either 200 or 500 trials. 
assetsSummary: {'species': [{'name': 'Rattus norvegicus - Norway rat', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10116'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 64199969632, 'numberOfFiles': 29, 'numberOfSubjects': 4, 'variableMeasured': ['ElectrodeGroup', 'LFP', 'ElectricalSeries', 'ProcessingModule'], 'measurementTechnique': [{'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'signal filtering technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000463 has 29 NWB files.
29 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeries (ElectricalSeries) no description
  Dataset /acquisition/ElectricalSeries/electrodes (DynamicTableRegion) all electrodes | shape = (32,) | dtype = int64
  file_create_date: ['2023-03-23T01:35:13.000000-07:00' '2023-03-23T01:36:23.127000-07:00']
  Group /general/devices/array (Device) A1x32-Poly3-10mm-50-177-A32
  Group /general/extracellular_ephys/electrodes (DynamicTable) all electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) my description | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) my description | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) my description | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (32,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) my description | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) my description | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) my description | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) my description | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) my description | shape = (32,) | dtype = float64
  Group /general/extracellular_ephys/shank1 (ElectrodeGroup) electrode group for shank1
  Group /general/extracellular_ephys/shank1/device (Device) A1x32-Poly3-10mm-50-177-A32
  institution: Carnegie Mellon University
  Group /general/subject (Subject) 
  identifier: BH395_3000Hz_5V
  Group /processing/ecephys (ProcessingModule) extracellular electrophysiology
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/ElectricalSeries (ElectricalSeries) no description
  Dataset /processing/ecephys/LFP/ElectricalSeries/electrodes (DynamicTableRegion) all electrodes | shape = (32,) | dtype = int64
  session_description: Rat Ultrasound Array Stimulation
  session_start_time: 2022-12-13T17:40:39.000000-08:00
  timestamps_reference_time: 2022-12-13T17:40:39.000000-08:00
