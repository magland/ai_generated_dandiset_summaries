
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000296/0.220805.1724
name: Drosophila visual neural responses to stochastic stimuli
contributor: [{'name': 'Gonzalez, Aneysis', 'email': 'aneysis.gonzalez@yale.edu', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}]
description: Associated Reference Publication: Excitatory and inhibitory neural dynamics jointly tune motion detection
Neurons integrate excitatory and inhibitory signals to produce their outputs, but the role of input timing in this integration remains poorly understood. Motion detection is a paradigmatic example of this integration, since theories of motion detection rely on different delays in visual signals. These delays allow circuits to compare scenes at different times to calculate the direction and speed of motion. Different motion detection circuits have different velocity sensitivity, but it remains untested how the response dynamics of individual cell types drive this tuning. Here, we sped up or slowed down specific neuron types in Drosophila’s motion detection circuit by manipulating ion channel expression. Altering the dynamics of individual neuron types upstream of motion detectors increased their sensitivity to fast or slow visual motion, exposing distinct roles for excitatory and inhibitory dynamics in tuning directional signals, including a role for the amacrine cell CT1. A circuit model constrained by functional data and anatomy qualitatively reproduced the observed tuning changes. Overall, these results reveal how excitatory and inhibitory dynamics together tune a canonical circuit computation.
assetsSummary: {'species': [{'name': 'Drosophila melanogaster - Fruit fly', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_7227'}], 'approach': [{'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 745311363665, 'numberOfFiles': 1278, 'numberOfSubjects': 1188, 'variableMeasured': ['ImagingPlane', 'OpticalChannel', 'TwoPhotonSeries'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'two-photon microscopy technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000296 has 100 NWB files.
100 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/TwoPhotonSeries (TwoPhotonSeries) no description
  Group /acquisition/TwoPhotonSeries/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeries/imaging_plane/device (Device) 
  Group /acquisition/TwoPhotonSeries/imaging_plane/optical_channel (OpticalChannel) 
  file_create_date: ['2022-08-03T02:28:58.006000-04:00']
  Group /general/devices/Device (Device) 
  experimenter: ['Aneysis Gonzalez']
  Group /general/optophysiology/imaging_plane (ImagingPlane) 
  Group /general/optophysiology/imaging_plane/device (Device) 
  Group /general/optophysiology/imaging_plane/optical_channel (OpticalChannel) 
  Group /general/subject (Subject) 
  identifier: Mi1_GC6f_CacRNAi
  session_description: 2 Photon Imaging
  session_start_time: 2017-09-11T13:53:06.000000-04:00
  timestamps_reference_time: 2017-09-11T13:53:06.000000-04:00
