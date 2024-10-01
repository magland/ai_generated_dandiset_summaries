
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000454/0.230302.2331
name: Guide to the construction and use of an adaptive optics two-photon microscope with direct wavefront sensing
contributor: [{'url': 'http://ucsd.edu/', 'name': 'Klienfeld, David', 'email': 'dk@physics.ucsd.edu', 'roleName': ['dcite:Author', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'url': 'http://ucsd.edu/', 'name': 'Yao, Pantong', 'email': 'p1yao@health.ucsd.edu', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'url': 'http://ucsd.edu/', 'name': 'Liu, Rui', 'email': 'rul087@physics.ucsd.edu', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'url': 'http://ucsd.edu/', 'name': 'Broginni, Thomas', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'url': 'http://www.bu.edu/', 'name': 'Thunemann, Martin', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'url': 'http://ucsd.edu/', 'name': 'University of California, San Diego', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/0168r3w48', 'awardNumber': 'U24 EB028942', 'contactPoint': [], 'includeInCitation': True}, {'url': 'http://www.bu.edu/', 'name': 'Boston University', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/05qwgg493', 'awardNumber': 'U19 NS123717', 'contactPoint': [], 'includeInCitation': True}, {'url': 'http://ucsd.edu/', 'name': 'University of California, San Diego', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/0168r3w48', 'awardNumber': 'U19 NS107466', 'contactPoint': [], 'includeInCitation': True}]
description: Two-photon microscopy, combined with appropriate optical labeling, has enabled the study of structure and function throughout animals and their organ systems, especially nervous systems. This methodology enables, for example, the measurement and tracking of sub-micrometer structures within brain cells, the spatio-temporal mapping of spikes in individual neurons, and the spatio-temporal mapping of transmitter release in individual synapses. Yet the spatial resolution of two-photon microscopy rapidly degrades as imaging is attempted at depths more than a few scattering lengths into tissue, i.e., below the superficial layers that constitute the top 300 to 400 µm of neocortex. To obviate this limitation, we measure the wavefront of the guide star at the focus of the excitation beam and utilize adaptive optics that alters the incident wavefront to achieve an improved focal volume. We describe the construction, calibration, and operation of a two-photon microscope that incorporates adaptive optics to restore diffraction-limited resolution throughout the nearly 900 µm depth of mouse cortex. Our realization utilizes a guide star formed by excitation of red-shifted dye within the blood serum to directly measure the wavefront. We incorporate predominantly commercial optical, optomechanical, mechanical, and electronic components; computer aided design models of the exceptional custom components are supplied. The resultant adaptive-optics two-photon microscope is modular and allows for expanded imaging and optical excitation capabilities. We demonstrate our methodology in mouse neocortex by imaging the morphology of somatostatin-expressing neurons that lie 700 µm beneath the pia, calcium dynamics of layer 5b projection neurons, and thalamocortical glutamate transmission to L4 neurons.
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 7401238168, 'numberOfFiles': 4, 'numberOfSubjects': 5, 'variableMeasured': ['TwoPhotonSeries', 'ImagingPlane', 'OpticalChannel'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'two-photon microscopy technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000454 has 4 NWB files.
1 of these NWB files are of type 1.
1 of these NWB files are of type 2.
1 of these NWB files are of type 3.
1 of these NWB files are of type 4.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/TwoPhotonSeries (TwoPhotonSeries) no description
  Group /acquisition/TwoPhotonSeries/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeries/imaging_plane/OpticalChannel2 (OpticalChannel) 
  Group /acquisition/TwoPhotonSeries/imaging_plane/device (Device) Adaptive optic - two photon laser scanning microscope
  file_create_date: ['2023-03-02T13:26:11.639504-08:00']
  Group /general/devices/AO-TPLSM (Device) Adaptive optic - two photon laser scanning microscope
  experimenter: ['Yao, Pantong']
  institution: UC San Diego
  keywords: ['Researchers: Yao, Pantong']
  Group /general/optophysiology/ROI2_SplC_9x_stk_avg100_670_690um_zernike60_00001.tif (ImagingPlane) 
  Group /general/optophysiology/ROI2_SplC_9x_stk_avg100_670_690um_zernike60_00001.tif/OpticalChannel2 (OpticalChannel) 
  Group /general/optophysiology/ROI2_SplC_9x_stk_avg100_670_690um_zernike60_00001.tif/device (Device) Adaptive optic - two photon laser scanning microscope
  Group /general/subject (Subject) 
  identifier: 
  session_description: Fig 17
  session_start_time: 2023-03-02T00:00:00-08:00
  timestamps_reference_time: 2023-03-02T00:00:00-08:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/TwoPhotonSeries (TwoPhotonSeries) no description
  Group /acquisition/TwoPhotonSeries/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeries/imaging_plane/OpticalChannel2 (OpticalChannel) 
  Group /acquisition/TwoPhotonSeries/imaging_plane/device (Device) Adaptive optic - two photon laser scanning microscope
  file_create_date: ['2023-03-02T13:26:18.781728-08:00']
  Group /general/devices/AO-TPLSM (Device) Adaptive optic - two photon laser scanning microscope
  experimenter: ['Yao, Pantong']
  institution: UC San Diego
  keywords: ['Researchers: Yao, Pantong']
  Group /general/optophysiology/ROI2_SysC_9x_stk_avg100_670_690um_00001.tif (ImagingPlane) 
  Group /general/optophysiology/ROI2_SysC_9x_stk_avg100_670_690um_00001.tif/OpticalChannel2 (OpticalChannel) 
  Group /general/optophysiology/ROI2_SysC_9x_stk_avg100_670_690um_00001.tif/device (Device) Adaptive optic - two photon laser scanning microscope
  Group /general/subject (Subject) 
  identifier: 
  session_description: Fig 17
  session_start_time: 2023-03-02T00:00:00-08:00
  timestamps_reference_time: 2023-03-02T00:00:00-08:00


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/TwoPhotonSeries (TwoPhotonSeries) no description
  Group /acquisition/TwoPhotonSeries/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeries/imaging_plane/OpticalChannel2 (OpticalChannel) 
  Group /acquisition/TwoPhotonSeries/imaging_plane/device (Device) Adaptive optic - two photon laser scanning microscope
  file_create_date: ['2023-03-02T13:26:33.115183-08:00']
  Group /general/devices/AO-TPLSM (Device) Adaptive optic - two photon laser scanning microscope
  experimenter: ['Yao, Pantong']
  institution: UC San Diego
  keywords: ['Researchers: Yao, Pantong']
  Group /general/optophysiology/exp5_combined_MCM2.tif (ImagingPlane) 
  Group /general/optophysiology/exp5_combined_MCM2.tif/OpticalChannel2 (OpticalChannel) 
  Group /general/optophysiology/exp5_combined_MCM2.tif/device (Device) Adaptive optic - two photon laser scanning microscope
  Group /general/subject (Subject) 
  identifier: 
  session_description: Fig 18
  session_start_time: 2023-03-02T00:00:00-08:00
  timestamps_reference_time: 2023-03-02T00:00:00-08:00


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/TwoPhotonSeries (TwoPhotonSeries) no description
  Group /acquisition/TwoPhotonSeries/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeries/imaging_plane/OpticalChannel1 (OpticalChannel) 
  Group /acquisition/TwoPhotonSeries/imaging_plane/device (Device) Adaptive optic - two photon laser scanning microscope
  file_create_date: ['2023-03-02T13:26:28.880719-08:00']
  Group /general/devices/AO-TPLSM (Device) Adaptive optic - two photon laser scanning microscope
  experimenter: ['Yao, Pantong']
  institution: UC San Diego
  keywords: ['Researchers: Yao, Pantong']
  Group /general/optophysiology/B2_roi6_5hz_00001_MCM1.tif (ImagingPlane) 
  Group /general/optophysiology/B2_roi6_5hz_00001_MCM1.tif/OpticalChannel1 (OpticalChannel) 
  Group /general/optophysiology/B2_roi6_5hz_00001_MCM1.tif/device (Device) Adaptive optic - two photon laser scanning microscope
  Group /general/subject (Subject) 
  identifier: 
  session_description: Fig 18
  session_start_time: 2023-03-02T00:00:00-08:00
  timestamps_reference_time: 2023-03-02T00:00:00-08:00
