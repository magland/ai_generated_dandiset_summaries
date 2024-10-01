
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000173/0.220927.0404
name: Neural Spiking Data in Primary Somatosensory Cortex before and after Transcranial Focused Ultrasound Stimulation in Rats
contributor: [{'name': 'Ramachandran, Sandhya', 'email': 'sandhyar@andrew.cmu.edu', 'roleName': ['dcite:DataCollector', 'dcite:Author', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [{'name': 'Carnegie Mellon University', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/05x2bcf33'}], 'includeInCitation': True}, {'name': 'Carnegie Mellon University', 'roleName': ['dcite:Affiliation'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/05x2bcf33', 'contactPoint': [], 'includeInCitation': True}, {'name': 'Niu, Xiaodan', 'email': 'xiaodann@andrew.cmu.edu', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [{'name': 'Carnegie Mellon University', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/05x2bcf33'}], 'includeInCitation': True}, {'name': 'Yu, Kai', 'email': 'yukai@cmu.edu', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [{'name': 'Carnegie Mellon University', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/05x2bcf33'}], 'includeInCitation': True}, {'name': 'He, Bin', 'email': 'bhe1@andrew.cmu.edu', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [{'name': 'Carnegie Mellon University', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/05x2bcf33'}], 'includeInCitation': True}, {'name': 'NIH MH114233', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'contactPoint': [], 'includeInCitation': False}, {'name': 'NIH NS124564 ', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'contactPoint': [], 'includeInCitation': False}]
description: In this study, we investigate how transcranial focused ultrasound (tFUS) modulates neural interaction and response to peripheral electrical limb stimulation through intracranial multi-electrode recordings in the rat somatosensory cortex. Rats were anesthetized using isoflurane anesthesia at 2%. Recordings were taken while delivering peripheral electrical stimulation once every 5 seconds to analyze the neural response in the rat S1HL region, before and after ultrasound. We delivered ultrasound for 5 minutes in a pulsed pattern at 5 different stimulation repetition frequencies (10 Hz, 50 Hz, 75 Hz, 100 Hz, and 125 Hz) to induce frequency dependent plasticity in a manner similar to that found following tetanic electrical stimulation. The fundamental frequency of ultrasound used was 0.5 MHz, the pulse repetition frequency (PRF) was 3 kHz, and the total duty cycle was 36%. This dataset includes spike timing data from the recordings including time before and after ultrasound stimulation, for both true ultrasound conditions and sham ultrasound conditions in which ultrasound is directed off target. Details of the study are in the following publication: S. Ramachandran, X. Niu, K. Yu, B. He, "Transcranial ultrasound neuromodulation induces neuronal correlation change in the rat somatosensory cortex", 2022 J. Neural Eng. 19 056002 https://pubmed.ncbi.nlm.nih.gov/35947970/. Please cite this publication if you would use a portion of the data. 
assetsSummary: {'species': [{'name': 'Rattus norvegicus - Norway rat', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10116'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 240963992, 'numberOfFiles': 118, 'numberOfSubjects': 30, 'variableMeasured': ['Units'], 'measurementTechnique': [{'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000173 has 100 NWB files.
100 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2022-03-24T10:57:52.206000-07:00']
  institution: Carnegie Mellon Univeristy
  Group /general/subject (Subject) 
  identifier: BH243_100sham
  session_description: Rat SEP induction
  session_start_time: 2021-11-03T00:00:00.000000-07:00
  timestamps_reference_time: 2021-11-03T00:00:00.000000-07:00
  Group /units (Units) units table
  Dataset /units/id (ElementIdentifiers)  | shape = (20,) | dtype = int64
  Dataset /units/spike_times (VectorData) /units/spike_times | shape = (117397,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) indexes data | shape = (20,) | dtype = uint64
