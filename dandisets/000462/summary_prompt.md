
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000462/0.230416.2132
name: HippocampusRewardDataset
contributor: [{'name': 'Krishnan, Seetha', 'email': 'seethakris@gmail.com', 'roleName': ['dcite:ContactPerson', 'dcite:Author', 'dcite:Conceptualization', 'dcite:DataCollector', 'dcite:DataCurator', 'dcite:DataManager', 'dcite:FormalAnalysis', 'dcite:Investigation', 'dcite:Methodology', 'dcite:Visualization', 'dcite:Validation'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}]
description: Dataset that applies to the paper.
Krishnan, S., Heer, C., Cherian, C. et al. Nat Commun 13, 6662 (2022). https://doi.org/10.1038/s41467-022-34465-5

Uploaded datasets include data from WT mice where mice underwent a reward expectation extinction task as described in Figures 1-3. Four datasets with DREADD manipulation of VTA dopaminergic neurons and controls are also included as described in Figure 4. All datasets are processed raw fluorescence obtained from suite2p. Behavior data is also included.

Scripts used for analysis can be found on https://github.com/seethakris/HPCrewardpaper
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 6494591109, 'numberOfFiles': 14, 'numberOfSubjects': 14, 'variableMeasured': ['ProcessingModule', 'OpticalChannel', 'ImagingPlane'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000462 has 14 NWB files.
14 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Behaviordata (TimeSeries) Behavior data downsampled to imaging rate. First column is running behavior, second is reward times, third is lick behavior
  Group /acquisition/Cellxrawfluoresence (TimeSeries) Raw fluoresence trace for each cell obtained after suite2p. Number of frames per session: Rewarded: 12000, Unrewarded: 15000, ReRewarded:12000, BeforeSaline:12000, AfterSaline:20000, BeforeCNO:12000, AfterCNO:20000, BeforeDCZ:12000, AfterDCZ:20000
  file_create_date: ['2023-04-12T10:15:28.531379-05:00']
  Group /general/devices/Rig1 (Device) Sheffield Lab 2-p rig
  experiment_description: Mice were trained in a familiar environment with reward. Four Experiment days occured. On Day1, reward was removed. On Day2, mice were place in the familiar environment with reward and injected with saline. On Day3 and 4, mice were injected with a DREADD ligand
  experimenter: ['Krishnan, Seetha']
  institution: University of Chicago
  keywords: ['Hippocampus' 'Reward' 'Placecells' 'CA1' 'Virtual Reality paradigm']
  lab: Sheffield Lab
  Group /general/optophysiology/ImagingPlane (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane/OpticalChannel (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane/device (Device) Sheffield Lab 2-p rig
  related_publications: ['https://doi.org/10.1038/s41467-022-34465-5']
  Group /general/subject (Subject) 
  identifier: 009
  Group /processing/ophys (ProcessingModule) segmented data using suite2p
  session_description: Reward expectation extinction
  session_start_time: 2021-12-13T02:30:00-06:00
  timestamps_reference_time: 2021-12-13T02:30:00-06:00
