
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000624/draft
name: A brainstem circuit for the expression of defensive facial reactions in rat
contributor: [{'name': 'Rinehart, Duane', 'email': 'duane.rinehart@gmail.com', 'roleName': ['dcite:DataManager'], 'schemaKey': 'Person', 'identifier': '0000-0001-9245-2124', 'affiliation': [{'name': 'University of California, San Diego', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/0168r3w48'}], 'includeInCitation': True}, {'name': 'Amalia Callado-Pérez', 'email': 'amalia.callado.perez@gmail.com', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-2255-4640', 'affiliation': [{'name': 'Université Laval', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/04sjchr03'}, {'name': 'University of California, San Diego', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/0168r3w48'}], 'includeInCitation': True}, {'name': 'Kleinfeld, David', 'email': 'dk@physics.ucsd.edu', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0001-9797-4722', 'affiliation': [{'name': 'University of California, San Diego', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/0168r3w48'}], 'includeInCitation': True}, {'name': 'Fassihi, Arash', 'email': 'arfassihi@gmail.com', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0001-7477-7080', 'affiliation': [{'name': 'University of California, San Diego', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/0168r3w48'}], 'includeInCitation': True}, {'name': 'Dechênes, Martin', 'email': 'martin.deschenes@fmed.ulaval.ca', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-5385-6633', 'affiliation': [{'name': 'Université Laval', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/04sjchr03'}], 'includeInCitation': True}, {'name': 'Moore, Jeffrey D.', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [{'name': 'University of Southern California', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/03taz7m60'}], 'includeInCitation': True}, {'name': 'Demers, Maxime', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [{'name': 'Université Laval', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/04sjchr03'}], 'includeInCitation': True}, {'name': 'National Institute of Health', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': 'NS107466', 'contactPoint': [], 'includeInCitation': False}, {'name': 'National Institute of Health', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': 'NS097265', 'contactPoint': [], 'includeInCitation': False}, {'name': 'Canadian Institute of Health Research', 'roleName': [], 'schemaKey': 'Organization', 'awardNumber': 'MT-5877', 'contactPoint': [], 'includeInCitation': False}]
description: Chemoreceptors in the nasal epithelium can trigger an apneic reaction and a grimace in response to airborne irritants. Callado Perez et al. find that the underlying circuit does not involve olfaction. Rather, activation of neurons in the muralis subnucleus of the spinal trigeminal complex will inhibit the Pre-Bötzinger inhalation oscillator.
assetsSummary: {'species': [{'name': 'Rattus norvegicus - Norway rat', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10116'}], 'approach': [{'name': 'behavioral approach', 'schemaKey': 'ApproachType'}, {'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 130570933952, 'numberOfFiles': 45, 'numberOfSubjects': 10, 'variableMeasured': ['ProcessingModule', 'Units', 'BehavioralEvents'], 'measurementTechnique': [{'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000624 has 27 NWB files.
8 of these NWB files are of type 1.
19 of these NWB files are of type 2.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2023-10-13T11:07:26.566879-07:00']
  Group /general/subject (Subject) 
  identifier: Rat10
  Group /intervals/trials (TimeIntervals) trial data and properties
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (6,) | dtype = int64
  Dataset /intervals/trials/start_time (VectorData) start time of ammonia stimulation in samples FS_2k | shape = (6,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) start time of ammonia stimulation in samples FS_2k | shape = (6,) | dtype = float64
  Group /processing/behavior (ProcessingModule) stores behavioral data.
  Group /processing/behavior/BehavioralEvents (BehavioralEvents) 
  Group /processing/behavior/BehavioralEvents/lever_presses (TimeSeries) The voltage value and the timestamp of inspiration
  session_description: Muralis unit response to Ammonia stimulation in anesthetized rat
  session_start_time: ['2022-12-15T12:00:00.000000-08:00']
  timestamps_reference_time: ['2022-12-15T12:00:00.000000-08:00']
  Group /units (Units) units table
  Dataset /units/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /units/spike_times (VectorData) no description | shape = (561,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) indexes data | shape = (1,) | dtype = uint64


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/IxmageSeries (ImageSeries) rat-heafixed_grimace
  file_create_date: ['2023-10-13T11:25:03.251663-07:00']
  Group /general/devices/ A602f camera (Device) NA
  experiment_description: grimace response in head fixed rat
  experimenter: ['Max']
  institution: Université Laval
  stimulus: NH3 or airpuff 
  Group /general/subject (Subject) 
  identifier: sept_22_2022_Rat332_s1
  session_description: rat-heafixed_grimace
  session_start_time: 2022-09-22T00:00:00+00:00
  timestamps_reference_time: 2022-09-22T00:00:00+00:00
