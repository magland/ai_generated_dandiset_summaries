
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001063/draft
name: Broken time reversal symmetry in motion detection
contributor: [{'name': 'Wu, Nathan', 'email': 'mrwun2002@gmail.com', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}]
description: Our intuition suggests that when a movie is played in reverse, our perception of motion in the reversed movie will be perfectly inverted compared to the original. This intuition is also reflected in many classical theoretical and practical models of motion detection. However, here we demonstrate that this symmetry of motion perception upon time reversal is often broken in real visual systems. In this work, we designed a set of visual stimuli to investigate how stimulus symmetries affect time reversal symmetry breaking in the fruit fly Drosophila’s well-studied optomotor rotation behavior. We discovered a suite of new stimuli with a wide variety of different properties that can lead to broken time reversal symmetries in fly behavioral responses. We then trained neural network models to predict the velocity of scenes with both natural and artificial contrast distributions. Training with naturalistic contrast distributions yielded models that break time reversal symmetry, even when the training data was time reversal symmetric. We show analytically and numerically that the breaking of time reversal symmetry in the model responses can arise from contrast asymmetry in the training data, but can also arise from other features of the contrast distribution. Furthermore, shallower neural network models can exhibit stronger symmetry breaking than deeper ones, suggesting that less flexible neural networks promote some forms of time reversal symmetry breaking. Overall, these results reveal a surprising feature of biological motion detectors and suggest that it could arise from constrained optimization in natural environments.
assetsSummary: {'species': [{'name': 'Drosophila melanogaster - Fruit fly', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_7227'}], 'approach': [], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 148356576, 'numberOfFiles': 213, 'numberOfSubjects': 218, 'variableMeasured': [], 'measurementTechnique': []}

Dandiset 001063 has 100 NWB files.
100 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/TimeSeries (TimeSeries) T,XC,XCT fly no 12318734159920924704 optomotor turning on an air-supported ball
  file_create_date: ['2024-06-17T00:26:42.596831-04:00' '2024-06-17T00:26:42.632797-04:00']
  experiment_description: optomotor turning of Drosophila on air-supported balls when presented with visual stimuli
  experimenter: ['Wu, Nathan']
  institution: Yale University
  keywords: ['motion detection' 'symmetry' 'symmetry breaking' 'algorithm'
   'Drosophila']
  lab: Clark Lab
  related_publications: ['https://doi.org/10.1101/2024.06.08.598068']
  Group /general/subject (Subject) 
  identifier: T,XC,XCT 11-8-2022 17:16:54 12318734159920924704
  session_description: T,XC,XCT 11-8-2022 17:16:54
  session_start_time: ['2022-11-08T17:16:54.000000-05:00']
  timestamps_reference_time: ['2022-11-08T17:16:54.000000-05:00']
