
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001374/draft
name: Self-Organizing Neural Networks in Organoids Reveal Principles of Forebrain Circuit Assembly
contributor: [{'name': 'Blauvelt, Lon', 'email': 'lblauvel@ucsc.edu', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Hernandez, Sebastion', 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Schweiger, Hunter', 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Cline, Isabel', 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Kaurala, Gregory', 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Robbins, Ash', 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Solis, Daniel', 'schemaKey': 'Person'}, {'name': 'Geng, Jinghui', 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Molen, Tjiste van der', 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Reyes, Francisco', 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Asogwa, Chinweike', 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Voitiuk, Kateryna', 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Rolandi, Marco', 'schemaKey': 'Person'}, {'name': 'Colquitt, Bradley', 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Salama, Sofie', 'schemaKey': 'Person'}, {'name': 'Sharf, Tal', 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Haussler, David', 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Teodorescu, Mircea', 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Mostajo-Radji, Mohammed A.', 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Schmidt Futures', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/014bj2y47', 'awardNumber': 'SF857', 'includeInCitation': False}, {'name': 'National Human Genome Research Institute', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/00baak391', 'awardNumber': '1RM1HG011543', 'includeInCitation': False}, {'name': 'National Science Foundation', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/021nxhr62', 'awardNumber': 'NSF2134955'}, {'name': 'National Institute of Mental Health', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/04t0s7x83', 'awardNumber': '1U24MH132628'}, {'name': 'California Institute for Regenerative Medicine', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/033m8b439', 'awardNumber': 'DISC4-16285'}, {'name': 'University of California Office of the President', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/00dmfq477', 'awardNumber': 'M25PR9045'}, {'name': 'National Science Foundation', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/021nxhr62', 'awardNumber': 'NSF2034037'}, {'name': 'California Institute for Regenerative Medicine', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/033m8b439', 'awardNumber': 'DISC4-16337'}]
description: Ephys data from organoids
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 1548661140428, 'numberOfFiles': 210, 'numberOfSubjects': 1, 'variableMeasured': ['ElectrodeGroup', 'ElectricalSeries'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 001374 has 100 NWB files.
100 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeries (ElectricalSeries) Acquisition traces for the ElectricalSeries.
  Dataset /acquisition/ElectricalSeries/electrodes (DynamicTableRegion) electrode_table_region | shape = (496,) | dtype = int64
  file_create_date: ['2025-05-02T09:58:36.044203+00:00']
  Group /general/devices/DeviceEcephys (Device) Recorded using Maxwell version '20190530'.
  experiment_description: Hmmmm
  experimenter: ['Tal Sharf']
  Group /general/extracellular_ephys/0 (ElectrodeGroup) V1 Maxwell Electrode Group
  Group /general/extracellular_ephys/0/device (Device) Recorded using Maxwell version '20190530'.
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/channel_name (VectorData) unique channel reference | shape = (496,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/electrode (VectorData) Name (number) of the electrode | shape = (496,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/gain_to_physical_unit (VectorData) no description | shape = (496,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (496,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (496,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (496,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (496,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/offset_to_physical_unit (VectorData) no description | shape = (496,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/physical_unit (VectorData) no description | shape = (496,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/rel_x (VectorData) rel_x | shape = (496,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_y (VectorData) rel_y | shape = (496,) | dtype = float64
  institution: UCSC
  keywords: ['ephys' 'mouse' 'organoid']
  source_script: Created using NeuroConv v0.7.3
  Group /general/subject (Subject) 
  identifier: 48792a60-89f9-4f41-b28f-13a3fe02137b
  session_description: 
  session_start_time: 2025-05-02T02:58:36.015342-07:00
  timestamps_reference_time: 2025-05-02T02:58:36.015342-07:00
