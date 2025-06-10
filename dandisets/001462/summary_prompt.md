
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001462/0.250602.1536
name: 1R01NS138075-01
contributor: [{'name': 'Kitamura, Takashi', 'email': 'Takashi.Kitamura@UTSouthwestern.edu', 'roleName': ['dcite:Supervision', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'awardNumber': '1R01NS138075-01'}]
description: Neural circuit mechanisms for a mirror-induced self-directed behavior. in vivo calcium imaging from ACC neurons and animal behavior data during mirror exposure for 5 days.
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 148260571664, 'numberOfFiles': 13, 'numberOfSubjects': 3, 'variableMeasured': ['OpticalChannel', 'ImagingPlane', 'TwoPhotonSeries'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'two-photon microscopy technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 001462 has 13 NWB files.
13 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/BehavioralVideo (ImageSeries) Behavioral video recording
  Group /acquisition/TwoPhotonSeries (TwoPhotonSeries) Calcium imaging data from Inscopix
  Group /acquisition/TwoPhotonSeries/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeries/imaging_plane/Ca_Green (OpticalChannel) 
  Group /acquisition/TwoPhotonSeries/imaging_plane/device (Device) Inscopix nVista microscope
  file_create_date: ['2025-06-01T19:40:32.185667-05:00']
  Group /general/devices/Inscopix_microscope (Device) Inscopix nVista microscope
  experiment_description: Calcium imaging with behavioral recording
  experimenter: ['Indra']
  institution: UT Southwestern Medical Center
  keywords: ['two-photon' 'calcium imaging' 'behavior' 'mouse']
  lab: Kitamura Lab
  Group /general/optophysiology/ImagingPlane (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane/Ca_Green (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane/device (Device) Inscopix nVista microscope
  protocol: One-photon imaging protocol
  Group /general/subject (Subject) 
  identifier: sub-mouse02_ses-02
  session_description: Calcium imaging with behavioral recording
  session_start_time: 2025-06-02T00:40:32.154610+00:00
  timestamps_reference_time: 2025-06-02T00:40:32.154610+00:00
