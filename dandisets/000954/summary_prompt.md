
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000954/draft
name: FALCON Benchmark H1: Human 7DoF Reach and Grasp Motor BCI
contributor: [{'name': 'Ye, Joel', 'email': 'joelye9@gmail.com', 'roleName': ['dcite:ContactPerson', 'dcite:DataCurator'], 'schemaKey': 'Person', 'identifier': '0000-0002-1149-6035', 'affiliation': [], 'includeInCitation': True}, {'name': 'Jennifer L. Collinger', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0002-4517-5395', 'includeInCitation': True}, {'name': 'Robert Gaunt', 'email': 'rag53@pitt.edu', 'roleName': ['dcite:Supervision'], 'schemaKey': 'Person', 'includeInCitation': True}]
description: The dataset contains neural activity from a period of open loop calibration from a human participant with an intracortical brain computer interface. This data was collected under an Investigational
Device Exemption from the Food and Drug Administration and approved by the Institutional Review Board at the University of Pittsburgh (Pittsburgh, Pennsylvania), registered at ClinicalTrials.gov (NCT01894802). The clinical trial is an early feasibility study with a primary outcome of evaluating the safety of an intracortical brain–computer interface for long-term neural recording and stimulation. Data was recorded from two 96-channel intracortical electrode arrays in the hand "knob" area . The 7DoF are: 3D endpoint translation (x,y,z) 1D orientation (roll), and 3D grasp (flex/ext of thumb, index, ring, flex/ext of ring/pinky, thumb abduction).
On each trial, audiovisual cues indicated to the participant to attempt a particular reach or grasp involving a combination of the listed degrees of freedom.

This dataset is part of the FALCON benchmark: https://snel-repo.github.io/falcon. The datafile contains the following data in the acquisition fields: 7D kinematics (`OpenLoopKinematics`), trial numbers (`TrialNum`), and metadata for FALCON evaluation (`eval_mask`, `Blacklist`). The datafile also contains multi-unit spiking activity in the `units` field.

As part of the FALCON challenge, dataset files are released in three ways. The held-in-calib data includes many trials of data intended for calibration of decoders in the FALCON challenge. The held-in-minival data is a small subset of the held-in-calib data intended for FALCON models to validate submission format. Lastly, held-out-calib data are separate sessions of data from held-in-calib, but have much fewer trials, intended to be used for few-shot recalibration. Please bear in mind these factors if making use of this dataset for purposes outside of the FALCON Benchmark. Each dataset split is considered one "subject" by the DANDI repository; only data from one iBCI participant is included.

By downloading this dataset, you are agreeing to terms of the following Data Use Agreement:
- I will receive access to de-identified data and will not attempt to establish the identity of or attempt to contact any of the subjects.
- I will not attempt to make direct contact with PIs, affiliated data partner PIs, or staff at sites concerning the specific results of individual subjects. Data partner PIs may be contacted about potential collaboration opportunities.
- I will not further disclose these data beyond the uses outlined in this agreement and my data use application and understand that redistribution of data in any manner is prohibited.
- I will require anyone on my team who utilizes these data or anyone with whom I share these data to comply with this Data Use Agreement.


assetsSummary: {'species': [{'name': 'Homo sapiens - Human', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9606'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 102258934, 'numberOfFiles': 40, 'numberOfSubjects': 3, 'variableMeasured': ['Units'], 'measurementTechnique': [{'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000954 has 40 NWB files.
40 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/OpenLoopKinematics (TimeSeries) tx,ty,tz,rx,g1,g2,g3
  Group /acquisition/OpenLoopKinematicsVelocity (TimeSeries) tx,ty,tz,rx,g1,g2,g3
  Group /acquisition/TrialNum (TimeSeries) Trial number
  Group /acquisition/eval_mask (TimeSeries) Timesteps to ignore covariates (for training, eval). Neural data is not affected.
  file_create_date: ['2024-04-02T17:25:53.004254-04:00']
  experiment_description: Open loop calibration for human motor BCI
  experimenter: ['Labs, RehabNeuralEngineering']
  institution: University of Pittsburgh
  lab: Rehab Neural Engineering Labs
  Group /general/subject (Subject) 
  identifier: HumanPitt-held_in-calib_01-01-11:17_set1
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (187,) | dtype = int64
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (187,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (187,) | dtype = float64
  Dataset /intervals/epochs/tags (VectorData) user-defined tags | shape = (187,) | dtype = object
  Dataset /intervals/epochs/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (187,) | dtype = uint8
  Dataset /intervals/epochs/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (187,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/epochs/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (187,) | dtype = uint8
  session_description: FALCON H1. Open loop 7DoF calibration.
  session_start_time: 1925-01-01T11:17:40-05:00
  timestamps_reference_time: 1925-01-01T11:17:40-05:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/id (ElementIdentifiers)  | shape = (176,) | dtype = int64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (490706,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (176,) | dtype = uint32
