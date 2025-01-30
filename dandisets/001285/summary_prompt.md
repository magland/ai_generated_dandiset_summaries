
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001285/0.250110.2125
name: EEG Anesthesia Dataset
contributor: [{'name': 'Yousefi, Ali', 'email': 'aliyousefi@uh.edu', 'roleName': ['dcite:ContactPerson', 'dcite:DataCurator', 'dcite:DataManager'], 'schemaKey': 'Person', 'identifier': '0009-0006-8777-8262', 'includeInCitation': False}]
description: The experimental protocol for the dataset is described in detail in Purdon PL, Pierce ET, Mukamel EA, et al. Electroencephalogram signatures of loss and recovery of consciousness from propofol. Proc Natl Acad Sci U S A. 2013;110(12):E1142-E1151, doi:10.1073/pnas.1221180110. 
In summary, ten healthy, consenting volunteers aged 18–36 years participated in a study approved by the MGH Human Research Committee. The study examined induction and emergence from propofol anesthesia using a computer-controlled infusion system (StanPump) based on the Schnider pharmacokinetic-pharmacodynamic model. Subjects performed a behavioral task to identify the points of loss and recovery of consciousness while 64-channel EEG recordings were obtained. The protocol began with a 20-minute baseline EEG recording. Propofol was then administered in increasing effect-site concentrations, with each concentration maintained for 14 minutes, followed by decreasing effect-site concentrations designed to bracket the point of loss of consciousness. Each declining concentration was also held for 14 minutes. During all phases of the protocol—baseline, increasing, and decreasing concentrations—subjects performed a yes-no behavioral task every 4 seconds to document the times of loss and recovery of consciousness. After the propofol infusion was stopped, an additional 20-minute baseline EEG and behavioral recording period was conducted. Throughout the study, participants were instructed to keep their eyes closed to minimize eye-blink artifacts.

assetsSummary: {'species': [{'name': 'Homo sapiens - Human', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9606'}], 'approach': [], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 1186908720, 'numberOfFiles': 1, 'numberOfSubjects': 1, 'variableMeasured': [], 'measurementTechnique': []}

Dandiset 001285 has 1 NWB files.
1 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/example_timeseries (TimeSeries) no description
  file_create_date: ['2025-01-10T14:24:38.000000Z' '2025-01-10T15:20:12.139064-06:00']
  experimenter: ['Yousefi, Ali' 'Brown, Emery']
  notes: Experimenter: Yousefi, Ali (ORCID: orcid.org/0000-0001-2345-6789, Affiliation: University of Houston)
  Group /general/subject (Subject) 
  identifier: NWB123
  session_description: EEG Session Example
  session_start_time: ['2025-01-10T14:24:38.000000Z']
  timestamps_reference_time: ['2025-01-10T14:24:38.000000Z']
