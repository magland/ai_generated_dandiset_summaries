
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001045/0.250607.0101
name: Comparison of Fluid Flow In the Pial Perivascular Spaces of Rats and Mice
contributor: [{'name': 'Zhao, Yue', 'email': 'yuezhao@rochester.edu', 'roleName': ['dcite:ContactPerson', 'dcite:Maintainer'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': False}, {'name': 'Quirk, Keelin', 'email': 'kquirk@ur.rochester.edu', 'roleName': ['dcite:Author', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Ladron de Guevara, Antonio', 'email': 'antonio_ladron@urmc.rochester.edu', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Raghunandan, Aditya', 'email': 'araghuna@ur.rochester.edu', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Nedergaard, Maiken', 'email': 'maiken_nedergaard@urmc.rochester.edu', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Kelley, Douglas H. ', 'email': 'd.h.kelley@rochester.edu', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'United States Army', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/00afsp483', 'awardNumber': 'MURI W911NF1910280', 'includeInCitation': False}, {'name': 'National Institutes of Health', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01cwqze88', 'awardNumber': 'U19NS128613, R01AT012312', 'includeInCitation': False}, {'name': 'Lundbeck Foundation', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/03hz8wd80', 'awardNumber': 'R386–2021–165', 'includeInCitation': False}, {'name': 'Novo Nordisk Foundation', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/04txyc737', 'awardNumber': 'NNF20OC0066419', 'includeInCitation': False}, {'name': 'Nick Simons Foundation', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/00se21e39', 'awardNumber': '811237', 'includeInCitation': False}, {'name': 'Adelson Foundation', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/0001ew531', 'includeInCitation': False}]
description: This data includes several visualizations of five different rat’s pial perivascular spaces. It includes videos of fluid motion and z-stacks of arteries and perivascular spaces. These images were acquired using a two-photon microscope.
assetsSummary: {'species': [{'name': 'Rattus norvegicus - Norway rat', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10116'}, {'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 447436412442, 'numberOfFiles': 50, 'numberOfSubjects': 14, 'variableMeasured': [], 'measurementTechnique': []}

Dandiset 001045 has 50 NWB files.
33 of these NWB files are of type 1.
17 of these NWB files are of type 2.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ECG (TimeSeries) ECG
  Group /acquisition/Movies (ImageSeries) movie
  Group /acquisition/Resp (TimeSeries) Resp
  file_create_date: ['2025-06-06T19:29:08.046376-04:00']
  experiment_description: gly_BPN_BPN_WT_Mice 
  experimenter: ['Ladron de Guevara, Antonio']
  institution: University of Rochester
  keywords: ['Glymphatic, Perivascular space, Periarterial space, Cerebrospinal fluid.']
  session_id: m-20210315_PTV_BPN-BPH_M1_particles
  Group /general/subject (Subject) 
  identifier: gly_BPN_20210315_PTV_BPN-BPH_M1_particles
  session_description: particles, ECG, respiration
  session_start_time: ['2021-02-17T10:50:11.000000-05:00']
  timestamps_reference_time: ['2021-02-17T10:50:11.000000-05:00']


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Z-stack images (ImageSeries) z-stack images at 1-micron increments
  file_create_date: ['2025-06-06T15:43:07.461596-04:00']
  experiment_description: gly_Rat_Zstack_Rats
  experimenter: ['Ladron de Guevara, Antonio']
  institution: University of Rochester
  keywords: ['Glymphatic, Perivascular space, Periarterial space, Cerebrospinal fluid.']
  session_id: r-22-07-06-rat2_zstasck-up-1x
  Group /general/subject (Subject) 
  identifier: gly_Rat_22-07-06-rat2_zstasck-up-1x
  session_description: zstasck-up-1x
  session_start_time: ['2022-07-06T13:58:11.000000-05:00']
  timestamps_reference_time: ['2022-07-06T13:58:11.000000-05:00']
