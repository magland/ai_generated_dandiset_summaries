
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001357/draft
name: High-Density Recording Reveals Sparse Clusters (But Not Columns) for Shape and Texture Encoding in Macaque V4
contributor: [{'name': 'Kim, Taekjun', 'email': 'taekjunkim1223@gmail.com', 'roleName': ['dcite:ContactPerson', 'dcite:DataManager'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Namima, Tomoyuki', 'email': 't.namima@gmail.com', 'roleName': ['dcite:Author', 'dcite:Researcher', 'dcite:DataCollector', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Pasupathy, Anitha', 'email': 'pasupat@uw.edu', 'roleName': ['dcite:Author', 'dcite:ProjectLeader', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Kempkes, Erin', 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Zamarashkina, Polina', 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Owen, Natalia', 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'National Eye Institute', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': '', 'awardNumber': 'R01 EY018839, R01 EY029601, P30 EY01730', 'includeInCitation': False}, {'name': 'National Institute of Neurological Disorders and Stroke', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': 'U01 NS131810-01', 'includeInCitation': False}, {'name': 'National Institute OF Health', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': 'P51 OD010425', 'includeInCitation': False}, {'name': 'Japan Society for the Promotion of Science', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': 'KAKENHI Grant 23K06785 ', 'includeInCitation': False}, {'name': 'Japan Science and Technology', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': 'ERATO JPMJER1801, CREST JPMJCR18A5', 'includeInCitation': False}]
description: We used high-density Neuropixels probes in two awake monkeys (one female and one male) to characterize the shape and texture tuning of dozens of neurons simultaneously. The shape set included 15 simple geometric shapes each presented at eight different rotations in 45° increments, resulting in a total of 120 shape stimuli. Shapes were filled with a uniform color, either darker or brighter than the background luminance. The texture stimulus set was composed of 40 naturalistic grayscale textures. Each texture image was presented in three versions: original, contrast-reversed, or spectrally-matched noise

More detailed information associated with this dataset is described in https://doi.org/10.1523/JNEUROSCI.1893-23.2024 
assetsSummary: {'species': [{'name': 'Macaca mulatta - Rhesus monkey', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9544'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 241533432, 'numberOfFiles': 159, 'numberOfSubjects': 2, 'variableMeasured': ['Units', 'ElectrodeGroup'], 'measurementTechnique': [{'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 001357 has 100 NWB files.
52 of these NWB files are of type 1.
17 of these NWB files are of type 2.
31 of these NWB files are of type 3.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2025-03-11T07:24:23.570981-07:00']
  Group /general/devices/Neuropixels (Device) bank0_384ch
  experimenter: ['Namima, Tomoyuki']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (384,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (384,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (384,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/label (VectorData) label of electrode | shape = (384,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (384,) | dtype = object
  Group /general/extracellular_ephys/probe0 (ElectrodeGroup) electrode group for probe 0
  Group /general/extracellular_ephys/probe0/device (Device) bank0_384ch
  institution: University of Washington
  lab: Pasupathy Lab
  session_id: 20190717SL
  Group /general/subject (Subject) 
  identifier: 20190717SL
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/cond_ID (VectorData) stimulus condition ID | shape = (2178,) | dtype = int64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (2178,) | dtype = int64
  Dataset /intervals/trials/luminance (VectorData) luminance (cd/m2) | shape = (2178,) | dtype = int64
  Dataset /intervals/trials/pdOffTS (VectorData) photodiode OFF time | shape = (2178,) | dtype = float64
  Dataset /intervals/trials/pdOnTS (VectorData) photodiode ON time | shape = (2178,) | dtype = float64
  Dataset /intervals/trials/pen_ID (VectorData) penetration ID | shape = (2178,) | dtype = object
  Dataset /intervals/trials/rotation (VectorData) shape rotation | shape = (2178,) | dtype = float64
  Dataset /intervals/trials/ses_ID (VectorData) session ID | shape = (2178,) | dtype = object
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (2178,) | dtype = float64
  Dataset /intervals/trials/stim_ID (VectorData) shape stim ID | shape = (2178,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (2178,) | dtype = float64
  Dataset /intervals/trials/sub_ID (VectorData) subject ID | shape = (2178,) | dtype = object
  session_description: V4 shape screen
  session_start_time: 2019-07-17T10:30:00-07:00
  timestamps_reference_time: 2019-07-17T10:30:00-07:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/best_ch (VectorData) best channel | shape = (11,) | dtype = float64
  Dataset /units/depth (VectorData) distance from the electrode tip | shape = (11,) | dtype = float64
  Dataset /units/id (ElementIdentifiers)  | shape = (11,) | dtype = int64
  Dataset /units/is_sua (VectorData) sua = 1, mua = 0 | shape = (11,) | dtype = int64
  Dataset /units/pen_ID (VectorData) penetration ID | shape = (11,) | dtype = object
  Dataset /units/probe_num (VectorData) probe number | shape = (11,) | dtype = int64
  Dataset /units/ses_ID (VectorData) session ID | shape = (11,) | dtype = object
  Dataset /units/spike_times (VectorData) spike_times | shape = (125124,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (11,) | dtype = uint32
  Dataset /units/sub_ID (VectorData) subject ID | shape = (11,) | dtype = object
  Dataset /units/unit_ID (VectorData) unit ID | shape = (11,) | dtype = float64


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2025-03-11T12:06:16.254256-07:00']
  Group /general/devices/Neuropixels (Device) bank0_384ch
  experimenter: ['Namima, Tomoyuki']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (384,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (384,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (384,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/label (VectorData) label of electrode | shape = (384,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (384,) | dtype = object
  Group /general/extracellular_ephys/probe0 (ElectrodeGroup) electrode group for probe 0
  Group /general/extracellular_ephys/probe0/device (Device) bank0_384ch
  institution: University of Washington
  lab: Pasupathy Lab
  session_id: 20210412SP
  Group /general/subject (Subject) 
  identifier: 20210412SP
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/cond_ID (VectorData) stimulus condition ID | shape = (632,) | dtype = int64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (632,) | dtype = int64
  Dataset /intervals/trials/pdOffTS (VectorData) photodiode OFF time | shape = (632,) | dtype = float64
  Dataset /intervals/trials/pdOnTS (VectorData) photodiode ON time | shape = (632,) | dtype = float64
  Dataset /intervals/trials/pen_ID (VectorData) penetration ID | shape = (632,) | dtype = object
  Dataset /intervals/trials/position (VectorData) position ID (0-4) | shape = (632,) | dtype = float64
  Dataset /intervals/trials/ses_ID (VectorData) session ID | shape = (632,) | dtype = object
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (632,) | dtype = float64
  Dataset /intervals/trials/stim_ID (VectorData) shape stim ID | shape = (632,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (632,) | dtype = float64
  Dataset /intervals/trials/sub_ID (VectorData) subject ID | shape = (632,) | dtype = object
  session_description: V4 shape screen. position test
  session_start_time: 2021-04-12T10:30:00-07:00
  timestamps_reference_time: 2021-04-12T10:30:00-07:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/best_ch (VectorData) best channel | shape = (37,) | dtype = float64
  Dataset /units/depth (VectorData) distance from the electrode tip | shape = (37,) | dtype = float64
  Dataset /units/id (ElementIdentifiers)  | shape = (37,) | dtype = int64
  Dataset /units/is_sua (VectorData) sua = 1, mua = 0 | shape = (37,) | dtype = int64
  Dataset /units/pen_ID (VectorData) penetration ID | shape = (37,) | dtype = object
  Dataset /units/probe_num (VectorData) probe number | shape = (37,) | dtype = int64
  Dataset /units/ses_ID (VectorData) session ID | shape = (37,) | dtype = object
  Dataset /units/spike_times (VectorData) spike_times | shape = (49405,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (37,) | dtype = uint16
  Dataset /units/sub_ID (VectorData) subject ID | shape = (37,) | dtype = object
  Dataset /units/unit_ID (VectorData) unit ID | shape = (37,) | dtype = float64


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2025-03-11T12:50:11.725774-07:00']
  Group /general/devices/Neuropixels (Device) bank0_384ch
  experimenter: ['Namima, Tomoyuki']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (384,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (384,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (384,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/label (VectorData) label of electrode | shape = (384,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (384,) | dtype = object
  Group /general/extracellular_ephys/probe0 (ElectrodeGroup) electrode group for probe 0
  Group /general/extracellular_ephys/probe0/device (Device) bank0_384ch
  institution: University of Washington
  lab: Pasupathy Lab
  session_id: 20200628TX
  Group /general/subject (Subject) 
  identifier: 20200628TX
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/cond_ID (VectorData) stimulus condition ID | shape = (1024,) | dtype = int64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (1024,) | dtype = int64
  Dataset /intervals/trials/mode (VectorData) 0 (normal), 1 (reversed), 2 (spectral noise) | shape = (1024,) | dtype = float64
  Dataset /intervals/trials/pdOffTS (VectorData) photodiode OFF time | shape = (1024,) | dtype = float64
  Dataset /intervals/trials/pdOnTS (VectorData) photodiode ON time | shape = (1024,) | dtype = float64
  Dataset /intervals/trials/pen_ID (VectorData) penetration ID | shape = (1024,) | dtype = object
  Dataset /intervals/trials/ses_ID (VectorData) session ID | shape = (1024,) | dtype = object
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (1024,) | dtype = float64
  Dataset /intervals/trials/stim_ID (VectorData) texture stim ID | shape = (1024,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1024,) | dtype = float64
  Dataset /intervals/trials/sub_ID (VectorData) subject ID | shape = (1024,) | dtype = object
  session_description: V4 texture screen
  session_start_time: 2020-06-28T10:30:00-07:00
  timestamps_reference_time: 2020-06-28T10:30:00-07:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/best_ch (VectorData) best channel | shape = (33,) | dtype = float64
  Dataset /units/depth (VectorData) distance from the electrode tip | shape = (33,) | dtype = float64
  Dataset /units/id (ElementIdentifiers)  | shape = (33,) | dtype = int64
  Dataset /units/is_sua (VectorData) sua = 1, mua = 0 | shape = (33,) | dtype = int64
  Dataset /units/pen_ID (VectorData) penetration ID | shape = (33,) | dtype = object
  Dataset /units/probe_num (VectorData) probe number | shape = (33,) | dtype = int64
  Dataset /units/ses_ID (VectorData) session ID | shape = (33,) | dtype = object
  Dataset /units/spike_times (VectorData) spike_times | shape = (87747,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (33,) | dtype = uint32
  Dataset /units/sub_ID (VectorData) subject ID | shape = (33,) | dtype = object
  Dataset /units/unit_ID (VectorData) unit ID | shape = (33,) | dtype = float64
