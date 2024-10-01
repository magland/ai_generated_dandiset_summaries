
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000470/draft
name: Test
contributor: [{'name': 'Krishnan, Seetha', 'email': 'seethakris@gmail.com', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}]
description: Test data
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 128199784, 'numberOfFiles': 1, 'numberOfSubjects': 1, 'variableMeasured': ['ImagingPlane', 'ProcessingModule', 'OpticalChannel'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000470 has 1 NWB files.
1 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Cellxrawfluoresence (TimeSeries) Raw fluoresence trace for each cell obtained after suite2p
  file_create_date: ['2023-04-02T16:20:25.905054+05:30']
  Group /general/devices/Rig1 (Device) Sheffield Lab 2-p rig
  experiment_description: Mouse was trained with reward in a familiar environment. Reward was then unexpectadly removed for a few trials and then put back again.
  experimenter: ['Krishnan, Seetha']
  institution: University of Chicago
  lab: Sheffield Lab
  Group /general/optophysiology/ImagingPlane (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane/OpticalChannel (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane/device (Device) Sheffield Lab 2-p rig
  related_publications: ['https://doi.org/10.1038/s41467-022-34465-5']
  Group /general/subject (Subject) 
  identifier: NR6
  Group /processing/ophys (ProcessingModule) segmented data using suite2p
  session_description: Reward expectation extinction
  session_start_time: 2021-12-13T02:30:00-06:00
  timestamps_reference_time: 2021-12-13T02:30:00-06:00
