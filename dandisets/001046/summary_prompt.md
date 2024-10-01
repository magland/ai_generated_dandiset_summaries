
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001046/draft
name: FALCON Benchmark B1: zebra finch RA Neuropixels recordings during birdsong
contributor: [{'name': 'Karpowicz, Brianna', 'email': 'brianna.karpowicz@emory.edu', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0001-6519-4641', 'affiliation': [], 'includeInCitation': False}, {'name': 'Tostado-Marcos, Pablo', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-9539-9995', 'includeInCitation': True}, {'name': 'Arneodo, Ezequiel Matias', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-7125-4919', 'includeInCitation': True}, {'name': 'Gentner, Timothy Q.', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-4516-9841', 'includeInCitation': True}, {'name': 'Gilja, Vikash', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-0619-2686', 'includeInCitation': True}, {'name': 'NIH', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': 'NIDCD R01DC018446, NIDCD R01DC008358', 'includeInCitation': False}, {'name': 'NSF ', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': 'EFRI BRAID 2223822', 'includeInCitation': False}, {'name': 'Kavli Institute for the Brain and Mind', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': ' Innovative Research Grant #2021-1759', 'includeInCitation': False}, {'name': ' “La Caixa” Foundation', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'includeInCitation': False}, {'name': 'IIE Fulbright Fellowship', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'includeInCitation': False}, {'name': 'Pew Latin American Fellowship in the Biomedical Sciences', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'includeInCitation': False}]
description: The B1 dataset contains unsorted spike times, audio recordings, and audio spectrograms from a zebra finch songbird during natural vocal behavior. Neural activity was recorded using Neuropixels probes from premotor and motor nuclei. We provide precomputed spectrograms for each session. The raw audio is also provided.

In each datafile we provide the following as `acquisitions`: `tx` (threshold crossings at the full 30kHz resolution), `vocalizations` (the full sampling rate vocal recordings), `eval_mask_audio` (the mask for FALCON evaluation periods to be applied to the vocalizations). We also provide the following in the `trials` field: `spectrogram_times`, `spectrogram_frequencies`, `spectrogram_values`, and `spectrogram_eval_mask`. The spectrogram comprises the FALCON decoding target for this dataset.

As part of the FALCON challenge, dataset files are released in three ways. The `held-in-calib` data includes many trials of data intended for calibration of decoders in the FALCON challenge. The `held-in-minival` data is a small subset of the `held-in-calib` data intended for FALCON models to validate submission format. Lastly, `held-out-calib` data are separate sessions of data from `held-in-calib`, but have much fewer trials, intended to be used for few-shot recalibration. Please bear in mind these factors if making use of this dataset for purposes outside of the FALCON Benchmark. Each dataset split is considered one "subject" by the DANDI repository; only data from one songbird is included.
assetsSummary: {'species': [{'name': 'Taeniopygia guttata - Zebra finch', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_59729'}], 'approach': [], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 1286915940, 'numberOfFiles': 9, 'numberOfSubjects': 3, 'variableMeasured': [], 'measurementTechnique': []}

Dandiset 001046 has 9 NWB files.
9 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/eval_mask_audio (TimeSeries) Mask of audio timestamps considered during FALCON evaluation.
  Group /acquisition/tx (TimeSeries) Threshold crossings (Tx) extracted at original neural sampling rate - 30000 Hz.
  Group /acquisition/vocalizations (TimeSeries) Amplitude waveform of vocal epochs time-aligned to Tx at original recorded audio sampling rate - 25000 Hz.
  file_create_date: ['2024-06-05T17:54:58.851282+00:00']
  experiment_description: Synchronous RA-neural and song data of a Zebra finch implanted with a Neuropixels probe during awake-singing.
  experimenter: ['Dr. Pablo Tostado-Marcos and Dr. Ezequiel Arneodo']
  institution: UC San Diego
  lab: TNEL
  Group /general/subject (Subject) 
  identifier: z_r12r13_21_2021.06.26_held_in_calib
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (11,) | dtype = int64
  Dataset /intervals/trials/spectrogram_eval_mask (VectorData) Mask of timesteps and frequency bands considered during FALCON evaluation. | shape = (11, 158, 880) | dtype = bool
  Dataset /intervals/trials/spectrogram_frequencies (VectorData) Frequency bands associated with the spectrogram data values. | shape = (11, 158) | dtype = float64
  Dataset /intervals/trials/spectrogram_times (VectorData) Times associated with the spectrogram data values. | shape = (11, 880) | dtype = float64
  Dataset /intervals/trials/spectrogram_values (VectorData) Spectrogram data values. | shape = (11, 158, 880) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (11,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (11,) | dtype = float64
  session_description: Freely-awake-singing Zebra finch with a Neuropixels probe implanted in RA.
  session_start_time: 2021-06-26T00:00:00-07:00
  timestamps_reference_time: 2021-06-26T00:00:00-07:00
