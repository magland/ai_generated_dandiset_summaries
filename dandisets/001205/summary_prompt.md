
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001205/draft
name: Adaptation to visual sparsity enhances responses to isolated stimuli
contributor: [{'name': 'Gou, Tong', 'email': 'tong.gou@yale.edu', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}]
description: Associated Reference Publication: Sensory systems adapt their response properties to the statistics of their inputs. For instance, visual systems adapt to low-order statistics like mean and variance to encode stimuli efficiently or to facilitate specific downstream computations. However, it remains unclear how other statistical features affect sensory adaptation. Here, we explore how Drosophila’s visual motion circuits adapt to stimulus sparsity, a measure of the signal’s intermittency not captured by low-order statistics alone. Early visual neurons in both ON and OFF pathways alter their responses dramatically with stimulus sparsity, responding positively to both light and dark sparse stimuli but linearly to dense stimuli. These changes extend to downstream ON and OFF direction-selective neurons, which are activated by sparse stimuli of both polarities, but respond with opposite signs to light and dark regions of dense stimuli. Thus, sparse stimuli activate both ON and OFF pathways, recruiting a larger fraction of the circuit and potentially enhancing the salience of isolated stimuli. Overall, our results reveal visual response properties that increase the fraction of the circuit responding to sparse, isolated stimuli.
assetsSummary: {'species': [{'name': 'Drosophila melanogaster - Fruit fly', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_7227'}], 'approach': [{'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 136084878697, 'numberOfFiles': 277, 'numberOfSubjects': 277, 'variableMeasured': ['TwoPhotonSeries', 'OpticalChannel', 'ImagingPlane'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'two-photon microscopy technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 001205 has 100 NWB files.
100 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/TwoPhotonSeries (TwoPhotonSeries) no description
  Group /acquisition/TwoPhotonSeries/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeries/imaging_plane/device (Device) 
  Group /acquisition/TwoPhotonSeries/imaging_plane/optical_channel (OpticalChannel) 
  file_create_date: ['2024-10-15T19:23:09.084000-04:00']
  Group /general/devices/Device (Device) 
  experimenter: ['Tong Gou']
  institution: Yale University
  Group /general/optophysiology/imaging_plane (ImagingPlane) 
  Group /general/optophysiology/imaging_plane/device (Device) 
  Group /general/optophysiology/imaging_plane/optical_channel (OpticalChannel) 
  Group /general/subject (Subject) 
  identifier: w_+;UASGC6f_R21A05AD;R31H09DBD_+cda646b8-83b1-42e3-8431-9cd44f842934
  session_description: 2 Photon Imaging
  session_start_time: 2022-01-24T15:41:58.000000-05:00
  timestamps_reference_time: 2022-01-24T15:41:58.000000-05:00
