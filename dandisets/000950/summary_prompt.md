
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000950/draft
name: FALCON Benchmark H2: Human Handwriting iBCI
contributor: [{'name': 'Karpowicz, Brianna M', 'email': 'brianna.karpowicz@emory.edu', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': False}, {'name': 'Fan, Chaofei', 'roleName': ['dcite:Author', 'dcite:DataCollector'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Hahn, Nick', 'roleName': ['dcite:DataCollector', 'dcite:Author'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Kamdar, Foram', 'roleName': ['dcite:Author', 'dcite:DataCollector'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Avansino, Donald', 'roleName': ['dcite:Author', 'dcite:DataCollector'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Wilson, Guy', 'roleName': ['dcite:Author', 'dcite:DataCollector'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Hochberg, Leigh', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Shenoy, Krishna V', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Henderson, Jaime', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Willett, Frank', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Office of Research and Development, Rehabilitation R&D Service, Department of Veterans Affairs', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': 'nos. N2864C and A2295R', 'includeInCitation': False}, {'name': 'Wu Tsai Neurosciences Institute', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'includeInCitation': False}, {'name': 'Howard Hughes Medical Institute', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'includeInCitation': False}, {'name': 'Larry and Pamela Garlick', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'includeInCitation': False}, {'name': 'Simons Foundation Collaboration on the Global Brain', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'includeInCitation': False}, {'name': 'National Institute of Health', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': 'NIH-NIDCD U01DC017844, NIH-NIDCD R01DC014034, NIH-NIBIB R01EB028171', 'includeInCitation': False}]
description: The dataset contains neural activity from participant T5, who gave informed consent and was enrolled in the BrainGate2 Neural Interface System clinical trial (ClinicalTrials.gov Identifier: NCT00912041, registered June 3, 2009). This pilot clinical trial was approved under an Investigational Device Exemption (IDE) by the US Food and Drug Administration (Investigational Device Exemption #G090003). Permission was also granted by the Institutional Review Boards of Stanford University (protocol #20804). Data was recorded from two 96-channel intracortical electrode arrays in the hand "knob" area of of T5's left hemisphere precentral gyrus. On each trial, T5 was prompted to copy a cued sentence by writing individual characters, separated by a ">" space character. Decoded letters appeared on the screen below the prompt.

In each datafile, the `acquisitions` field contains `binned_spikes` (binned at 20ms) and the `eval_mask` used for determining valid FALCON evaluation periods. The `trials` field contains trial metadata including the prompt that T5 was asked to attempt to write (`cue`) and the experimental block that each trial belongs to (`block_num`).

As part of the FALCON challenge, dataset files are released in three ways. The `held-in-calib` data includes many trials of data intended for calibration of decoders in the FALCON challenge. The `held-in-minival` data is a small subset of the `held-in-calib` data intended for FALCON models to validate submission format. Lastly, `held-out-calib` data are separate sessions of data from `held-in-calib`, but have much fewer trials, intended to be used for few-shot recalibration. Please bear in mind these factors if making use of this dataset for purposes outside of the FALCON Benchmark. Each dataset split is considered one "subject" by the DANDI repository; only data from one iBCI participant is included.
assetsSummary: {'species': [{'name': 'Homo sapiens - Human', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9606'}], 'approach': [], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 1224956736, 'numberOfFiles': 47, 'numberOfSubjects': 3, 'variableMeasured': [], 'measurementTechnique': []}

Dandiset 000950 has 47 NWB files.
47 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/binned_spikes (TimeSeries) Threshold crossings aggregated in 20ms bins
  Group /acquisition/eval_mask (TimeSeries) Timesteps to KEEP covariates (for training, eval).
  file_create_date: ['2024-03-27T09:56:21.782651-04:00']
  experiment_description: handwriting with prompted sentences
  experimenter: ['Chaofei Fan']
  institution: Stanford University
  lab: NPTL
  Group /general/subject (Subject) 
  identifier: T5_2022.05.18_held_in_calib
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/block_num (VectorData) experimental block trial belonged to | shape = (30,) | dtype = int64
  Dataset /intervals/trials/cue (VectorData) sentence participant was prompted to write | shape = (30,) | dtype = object
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (30,) | dtype = int64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (30,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (30,) | dtype = float64
  session_description: human BCI participant performing attempted handwriting task
  session_start_time: 2022-05-18T00:00:00-05:00
  timestamps_reference_time: 2022-05-18T00:00:00-05:00
