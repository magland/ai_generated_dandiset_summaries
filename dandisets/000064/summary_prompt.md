
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000064/0.221025.1735
name: Simulation extension example
contributor: [{'name': 'Raikov, Ivan', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Milstein, Aaron', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Soltesz, Ivan', 'roleName': ['dcite:Author', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'NINDS', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': '5U19NS104590', 'contactPoint': [], 'includeInCitation': False}]
description: This is data produced by the Soltesz Lab NeuroH5 software (https://github.com/iraikov/neuroh5). The data has been converted to NWB using the ndx-simulation-output extension (https://github.com/catalystneuro/ndx-simulation-output).
assetsSummary: {'species': [], 'approach': [], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 218366752, 'numberOfFiles': 1, 'numberOfSubjects': 1, 'variableMeasured': [], 'measurementTechnique': []}

Dandiset 000064 has 1 NWB files.
1 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/soma_potential (CompartmentSeries) no description
  Dataset /acquisition/soma_potential/compartments (DynamicTableRegion) all soma compartments | shape = (1136,) | dtype = int64
  file_create_date: ['2021-04-06T14:57:57.607475-04:00']
  Group /general/simulation (SimulationMetaData) 
  Group /general/simulation/compartments (Compartments) Somas
  Dataset /general/simulation/compartments/cell_type (VectorData) abbreviation of cell type | shape = (1136,) | dtype = object
  Dataset /general/simulation/compartments/id (ElementIdentifiers)  | shape = (1136,) | dtype = int64
  Dataset /general/simulation/compartments/number (VectorData) cell compartment ids corresponding to a each column in the data | shape = (1136,) | dtype = int64
  Dataset /general/simulation/compartments/number_index (VectorIndex) Index for VectorData 'number' | shape = (1136,) | dtype = uint16
  Group /general/subject (Subject) 
  identifier: Full_Scale_GC_Exc_Sat_LN_results_9600226.bw
  session_description: simulated hippocampal network
  session_start_time: 2021-04-06T14:57:57.607066-04:00
  timestamps_reference_time: 2021-04-06T14:57:57.607066-04:00
