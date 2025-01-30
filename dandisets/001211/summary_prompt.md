
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001211/draft
name: Neurovascular impulse response function (IRF) during spontaneous activity differentially reflects intrinsic neuromodulation across cortical regions
contributor: [{'name': 'Rauscher, Bradley', 'email': 'bcraus@bu.edu', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0009-0008-1737-059X', 'affiliation': [{'name': 'Boston University', 'schemaKey': 'Affiliation'}], 'includeInCitation': True}, {'name': 'Fomin-Thunemann, Natalie', 'schemaKey': 'Person', 'identifier': '0000-0003-0449-4645', 'includeInCitation': True}, {'name': 'Kura, Sreekanth', 'schemaKey': 'Person', 'identifier': '0000-0002-8071-3259', 'includeInCitation': True}, {'name': 'Doran, Patrick', 'schemaKey': 'Person', 'identifier': '0000-0002-0374-0376', 'includeInCitation': False}, {'name': 'Perez, Pablo', 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Kılıç, Kıvılcım', 'schemaKey': 'Person', 'identifier': '0000-0001-7248-8728', 'includeInCitation': False}, {'name': 'Martin, Emily', 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Balog, Dora', 'schemaKey': 'Person', 'identifier': '0009-0004-5296-5725', 'includeInCitation': True}, {'name': 'Chai, Nathan', 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Froio, Francesca', 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Bloniasz, Patrick', 'schemaKey': 'Person', 'identifier': '0000-0002-8652-7609', 'includeInCitation': True}, {'name': 'Herrema, Kate', 'schemaKey': 'Person', 'identifier': '0000-0003-3929-3798', 'includeInCitation': False}, {'name': 'Tang, Rockwell', 'schemaKey': 'Person', 'identifier': '0000-0003-3044-0085', 'includeInCitation': True}, {'name': 'Knudstrup, Scott', 'schemaKey': 'Person', 'identifier': '0000-0002-5595-2127', 'includeInCitation': False}, {'name': 'Garcia, Andrew', 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Jiang, John', 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Gavornik, Jeffrey', 'schemaKey': 'Person', 'identifier': '0000-0001-8420-8973', 'includeInCitation': True}, {'name': 'Kleinfeld, David', 'schemaKey': 'Person', 'identifier': '0000-0001-9797-4722', 'includeInCitation': True}, {'name': 'Hasselmo, Michael', 'schemaKey': 'Person', 'identifier': '0000-0001-9797-4722', 'includeInCitation': True}, {'name': 'Lewis, Laura', 'schemaKey': 'Person', 'identifier': '0000-0002-4003-0277', 'includeInCitation': True}, {'name': 'Sakadzic, Sava', 'schemaKey': 'Person', 'identifier': '0000-0001-6318-1193', 'includeInCitation': True}, {'name': 'Tian, Lei', 'schemaKey': 'Person', 'identifier': '0000-0002-1316-4456', 'includeInCitation': True}, {'name': 'Mishne, Gal', 'schemaKey': 'Person', 'identifier': '0000-0002-5287-3626', 'includeInCitation': True}, {'name': 'Stephen, Emily', 'schemaKey': 'Person', 'identifier': '0000-0003-1978-9622', 'includeInCitation': True}, {'name': 'Thunemann, Martin', 'schemaKey': 'Person', 'identifier': '0000-0003-4139-079X', 'includeInCitation': True}, {'name': 'Boas, David', 'schemaKey': 'Person', 'identifier': '0000-0002-6709-7711', 'includeInCitation': True}, {'name': 'Devor, Anna', 'schemaKey': 'Person', 'identifier': '0000-0002-5143-3960', 'includeInCitation': True}, {'name': 'Boston University', 'roleName': ['dcite:Affiliation'], 'schemaKey': 'Organization', 'includeInCitation': False}, {'name': 'National Institute of Health', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': 'BRAIN Initiative U19NS123717', 'includeInCitation': False}, {'name': 'National Institute of Health', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': 'BRAIN Initiative R01NS122742', 'includeInCitation': False}, {'name': 'National Institute of Health', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': 'R01DA050159', 'includeInCitation': False}, {'name': 'National Institute of Health', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': 'T32-NS136080', 'includeInCitation': False}, {'name': 'Boston University Kilachand Fund', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'includeInCitation': False}, {'name': 'Boston University Neurophotonics Center', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'includeInCitation': False}]
description: Ascending neuromodulatory projections from deep brain nuclei generate internal brain states that differentially engage specific neuronal cell types. Because neurovascular coupling is cell-type specific and neuromodulatory transmitters have vasoactive properties, we hypothesized that the impulse response function (IRF) linking spontaneous neuronal activity with hemodynamics would depend on neuromodulation. Here, we use widefield cortical imaging to observe the resting state relationship between population level neuronal Ca2+ activity, fluctuations in oxygenation and concentration of hemoglobin, and release of the vasoactive neuromodulators Norepinephrine (NE) and Acetylcholine (ACh). First, the IRF linking neuronal activity and the hemodynamic response failed to predict hemodynamic fluctuations during periods marked by higher arousal (high NE and pupil diameter). Second, hemodynamic fluctuations were well predicted by a regression model factoring in both Ca2+ activity and NE release. Third, Ca2+ and hemodynamic functional connectivity patterns diverged during periods of high arousal. Without accounting for NE neuromodulation and the associated vasoconstriction, diminished hemodynamic coherence, commonly referred to as “functional (dys)connectivity” in BOLD fMRI studies, can be falsely interpreted as neuronal desynchronizations.
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'behavioral approach', 'schemaKey': 'ApproachType'}, {'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 1396937234570, 'numberOfFiles': 41, 'numberOfSubjects': 9, 'variableMeasured': ['BehavioralTimeSeries', 'PlaneSegmentation', 'OpticalChannel', 'ProcessingModule', 'ImagingPlane'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 001211 has 77 NWB files.
3 of these NWB files are of type 1.
74 of these NWB files are of type 2.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/HbO (OnePhotonSeries) HbO widefield movie
  Group /acquisition/HbO/imaging_plane (ImagingPlane) 
  Group /acquisition/HbO/imaging_plane/device (Device) Wide-field 1-photon fluorescent microscope
  Group /acquisition/HbO/imaging_plane/optical_channel (OpticalChannel) 
  Group /acquisition/HbR (OnePhotonSeries) HbR widefield movie
  Group /acquisition/HbR/imaging_plane (ImagingPlane) 
  Group /acquisition/HbR/imaging_plane/device (Device) Wide-field 1-photon fluorescent microscope
  Group /acquisition/HbR/imaging_plane/optical_channel (OpticalChannel) 
  Group /acquisition/gfp_HD (OnePhotonSeries) GRAB widefield movie
  Group /acquisition/gfp_HD/imaging_plane (ImagingPlane) 
  Group /acquisition/gfp_HD/imaging_plane/device (Device) Wide-field 1-photon fluorescent microscope
  Group /acquisition/gfp_HD/imaging_plane/optical_channel (OpticalChannel) 
  Group /acquisition/rfp_HD (OnePhotonSeries) jRGECO widefield movie
  Group /acquisition/rfp_HD/imaging_plane (ImagingPlane) 
  Group /acquisition/rfp_HD/imaging_plane/device (Device) Wide-field 1-photon fluorescent microscope
  Group /acquisition/rfp_HD/imaging_plane/optical_channel (OpticalChannel) 
  file_create_date: ['2024-10-21T13:43:32.171111-04:00' '2024-10-21T14:02:24.829630-04:00']
  Group /general/devices/Device (Device) Wide-field 1-photon fluorescent microscope
  experiment_description: Wide-field experiments on resting-state neurovascular coupling and neuromodulation
  experimenter: ['Froio, Francesca']
  institution: Boston University
  keywords: ['Neurovascular coupling, hemodynamics, norepinephrine, acetylcholine, functional connectivity']
  Group /general/optophysiology/led470 (ImagingPlane) 
  Group /general/optophysiology/led470/device (Device) Wide-field 1-photon fluorescent microscope
  Group /general/optophysiology/led470/optical_channel (OpticalChannel) 
  Group /general/optophysiology/led525 (ImagingPlane) 
  Group /general/optophysiology/led525/device (Device) Wide-field 1-photon fluorescent microscope
  Group /general/optophysiology/led525/optical_channel (OpticalChannel) 
  Group /general/optophysiology/led565 (ImagingPlane) 
  Group /general/optophysiology/led565/device (Device) Wide-field 1-photon fluorescent microscope
  Group /general/optophysiology/led565/optical_channel (OpticalChannel) 
  Group /general/optophysiology/led625 (ImagingPlane) 
  Group /general/optophysiology/led625/device (Device) Wide-field 1-photon fluorescent microscope
  Group /general/optophysiology/led625/optical_channel (OpticalChannel) 
  Group /general/subject (Subject) 
  identifier: Thy1_280-24-05-06_Run02
  Group /processing/behavior (ProcessingModule) stores behavioral data
  Group /processing/behavior/BehavioralTimeSeries (BehavioralTimeSeries) 
  Group /processing/behavior/BehavioralTimeSeries/accelerometer (TimeSeries) body movement of the subject measured over time
  Group /processing/ophys (ProcessingModule) Contains ROIs used in widefield analysis
  Group /processing/ophys/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation (PlaneSegmentation) roi pixel position (x,y) and pixel weight
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/id (ElementIdentifiers)  | shape = (13,) | dtype = int64
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/device (Device) Wide-field 1-photon fluorescent microscope
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/optical_channel (OpticalChannel) 
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/pixel_mask (VectorData) pixel masks | shape = (120675,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/pixel_mask_index (VectorIndex) Index into pixel_mask VectorData | shape = (13,) | dtype = uint32
  session_description: Neurovascular IRF during spontaneous activity differentially reflects intrinsic neuromodulation across cortical regions
  session_start_time: ['2024-05-06T09:00:00.000000-04:00']
  timestamps_reference_time: ['2024-05-06T09:00:00.000000-04:00']


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/HbO (OnePhotonSeries) HbO widefield movie
  Group /acquisition/HbO/imaging_plane (ImagingPlane) 
  Group /acquisition/HbO/imaging_plane/device (Device) Wide-field 1-photon fluorescent microscope
  Group /acquisition/HbO/imaging_plane/optical_channel (OpticalChannel) 
  Group /acquisition/HbR (OnePhotonSeries) HbR widefield movie
  Group /acquisition/HbR/imaging_plane (ImagingPlane) 
  Group /acquisition/HbR/imaging_plane/device (Device) Wide-field 1-photon fluorescent microscope
  Group /acquisition/HbR/imaging_plane/optical_channel (OpticalChannel) 
  Group /acquisition/gfp_HD (OnePhotonSeries) GRAB widefield movie
  Group /acquisition/gfp_HD/imaging_plane (ImagingPlane) 
  Group /acquisition/gfp_HD/imaging_plane/device (Device) Wide-field 1-photon fluorescent microscope
  Group /acquisition/gfp_HD/imaging_plane/optical_channel (OpticalChannel) 
  Group /acquisition/rfp_HD (OnePhotonSeries) jRGECO widefield movie
  Group /acquisition/rfp_HD/imaging_plane (ImagingPlane) 
  Group /acquisition/rfp_HD/imaging_plane/device (Device) Wide-field 1-photon fluorescent microscope
  Group /acquisition/rfp_HD/imaging_plane/optical_channel (OpticalChannel) 
  file_create_date: ['2024-10-21T11:15:08.642138-04:00' '2024-10-21T11:31:33.062302-04:00'
   '2024-10-21T11:49:30.385182-04:00']
  Group /general/devices/Device (Device) Wide-field 1-photon fluorescent microscope
  experiment_description: Wide-field experiments on resting-state neurovascular coupling and neuromodulation
  experimenter: ['Rauscher, Bradley']
  institution: Boston University
  keywords: ['Neurovascular coupling, hemodynamics, norepinephrine, acetylcholine, functional connectivity']
  Group /general/optophysiology/led470 (ImagingPlane) 
  Group /general/optophysiology/led470/device (Device) Wide-field 1-photon fluorescent microscope
  Group /general/optophysiology/led470/optical_channel (OpticalChannel) 
  Group /general/optophysiology/led525 (ImagingPlane) 
  Group /general/optophysiology/led525/device (Device) Wide-field 1-photon fluorescent microscope
  Group /general/optophysiology/led525/optical_channel (OpticalChannel) 
  Group /general/optophysiology/led565 (ImagingPlane) 
  Group /general/optophysiology/led565/device (Device) Wide-field 1-photon fluorescent microscope
  Group /general/optophysiology/led565/optical_channel (OpticalChannel) 
  Group /general/optophysiology/led625 (ImagingPlane) 
  Group /general/optophysiology/led625/device (Device) Wide-field 1-photon fluorescent microscope
  Group /general/optophysiology/led625/optical_channel (OpticalChannel) 
  Group /general/subject (Subject) 
  identifier: Thy1_110-23-09-26_Run03
  Group /processing/behavior (ProcessingModule) stores behavioral data
  Group /processing/behavior/BehavioralTimeSeries (BehavioralTimeSeries) 
  Group /processing/behavior/BehavioralTimeSeries/accelerometer (TimeSeries) body movement of the subject measured over time
  Group /processing/behavior/BehavioralTimeSeries/pupil (TimeSeries) pupil diameter of the subject measured over time
  Group /processing/behavior/BehavioralTimeSeries/whisking (TimeSeries) whisking motion energy of the subject measured over time
  Group /processing/ophys (ProcessingModule) Contains ROIs used in widefield analysis
  Group /processing/ophys/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation (PlaneSegmentation) roi pixel position (x,y) and pixel weight
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/id (ElementIdentifiers)  | shape = (13,) | dtype = int64
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/device (Device) Wide-field 1-photon fluorescent microscope
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/optical_channel (OpticalChannel) 
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/pixel_mask (VectorData) pixel masks | shape = (110960,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/pixel_mask_index (VectorIndex) Index into pixel_mask VectorData | shape = (13,) | dtype = uint32
  session_description: Neurovascular IRF during spontaneous activity differentially reflects intrinsic neuromodulation across cortical regions
  session_start_time: ['2023-09-26T10:00:00.000000-04:00']
  timestamps_reference_time: ['2023-09-26T10:00:00.000000-04:00']
