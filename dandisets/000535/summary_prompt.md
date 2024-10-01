
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000535/0.230524.0416
name: Allen Institute Openscope - Effects of Periodic Visual Stimulation on Neural Activity in Mouse Visual Cortex
contributor: [{'name': 'Lecoq, Jerome', 'email': 'jeromel@alleninstitute.org', 'roleName': ['dcite:DataCollector', 'dcite:DataCurator', 'dcite:DataManager', 'dcite:FundingAcquisition', 'dcite:Maintainer', 'dcite:Methodology', 'dcite:Producer', 'dcite:ProjectManager', 'dcite:ProjectAdministration', 'dcite:Software', 'dcite:Supervision', 'dcite:Validation', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0002-0131-0938', 'affiliation': [], 'includeInCitation': True}, {'name': 'Murdock, Mitchell H.', 'email': 'mitchm@mit.edu', 'roleName': ['dcite:Conceptualization', 'dcite:DataCurator', 'dcite:FormalAnalysis', 'dcite:Investigation', 'dcite:Methodology', 'dcite:Software', 'dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-0131-0938', 'affiliation': [], 'includeInCitation': True}, {'name': 'Arkhipov, Anton', 'email': 'antona@alleninstitute.org', 'roleName': ['dcite:Author', 'dcite:Conceptualization', 'dcite:DataManager', 'dcite:Investigation', 'dcite:Software', 'dcite:Supervision', 'dcite:Validation', 'dcite:FundingAcquisition', 'dcite:Maintainer', 'dcite:Producer', 'dcite:ProjectManager', 'dcite:DataCurator', 'dcite:ProjectLeader', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0003-1106-8310', 'affiliation': [], 'includeInCitation': True}, {'name': 'Ito, Shinya', 'email': 'shinya.ito@alleninstitute.org', 'roleName': ['dcite:Author', 'dcite:FormalAnalysis', 'dcite:Researcher', 'dcite:Software', 'dcite:Validation', 'dcite:Investigation', 'dcite:Methodology', 'dcite:Visualization'], 'schemaKey': 'Person', 'identifier': '0000-0001-5529-223X', 'affiliation': [], 'includeInCitation': True}, {'name': 'Ren, Naixin', 'email': 'naixin.ren@alleninstitute.org', 'roleName': ['dcite:Author', 'dcite:FormalAnalysis', 'dcite:Investigation', 'dcite:Methodology', 'dcite:Software', 'dcite:Validation', 'dcite:Visualization'], 'schemaKey': 'Person', 'identifier': '0000-0002-3074-281X', 'affiliation': [], 'includeInCitation': True}, {'name': 'Billeh, Yazan N.', 'email': 'yaz.billeh@gmail.com', 'roleName': ['dcite:Author', 'dcite:FormalAnalysis', 'dcite:Investigation', 'dcite:Methodology', 'dcite:Researcher', 'dcite:Software'], 'schemaKey': 'Person', 'identifier': '0000-0001-5200-4992', 'affiliation': [], 'includeInCitation': True}]
description: This study investigates the effects of periodic sensory stimulation (PSS) on the activity of neurons of different types in the mouse visual cortex. The PSS modality used is the flickering light visual stimulation. The dataset provides calcium imaging data from VIP (vasoactive intestinal peptide), SST (somatostatin), and PV (parvalbumin) expressing inhibitory neuron, as well as excitatory neurons in V1, in mice exposed to different visual stimulation conditions.
 
The visual stimulus is provided by an LED strip that is programmed for 4 conditions: 40 Hz flicker (gamma frequency), 8 Hz flicker (theta frequency), random frequency (light delivered with a random interval determined by a Poisson process with an average frequency of 40 Hz), and constant light on. Those conditions are reported in NWB file trial table. The LED strip was positioned in front of the mouse right eye in place of the visual stimulation screen used in (De Vries, Lecoq, Buice et al, Nature Neuroscience 2020). Light illumination started approximately 485 seconds into the experiment. The exact timing can be found in the stimulus table. Each mouse was recorded multiple times with individual cells matched. Each recording session only used one of the above stimulus conditions.
 
The data includes images from layers 2/3 and 5 (layer 4 instead of 5 for VIP) of the left visual cortex, capturing the contributions of superficial and deep cortical neurons to the network dynamics under visual PSS. The dataset was collected from 5 mice for SST, 6 mice for VIP, 2 mice for PV, and 2 mice for excitatory neurons. Mice were awake but not trained to perform any tasks. They were passively viewing the LED strip.  All animal procedures were approved by the Institutional Animal Care and Use Committee (IACUC) at the Allen Institute for Brain Science in compliance with NIH guidelines.
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}, {'name': 'behavioral approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 6827396992, 'numberOfFiles': 115, 'numberOfSubjects': 15, 'variableMeasured': ['OpticalChannel', 'ImagingPlane', 'PlaneSegmentation', 'BehavioralTimeSeries', 'ProcessingModule'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000535 has 100 NWB files.
100 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2023-05-16T10:28:51.294012-07:00']
  Group /general/devices/2p_microscope (Device) Allen Institute two-photon pipeline: CAM2P.1
  Group /general/optophysiology/ImagingPlane (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane/device (Device) Allen Institute two-photon pipeline: CAM2P.1
  Group /general/optophysiology/ImagingPlane/optical_channel (OpticalChannel) 
  Group /general/subject (Subject) 
  identifier: 884465600
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (1,) | dtype = float64
  Dataset /intervals/trials/stimulus (VectorData) the stimulus presented during the trial | shape = (1,) | dtype = object
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1,) | dtype = float64
  Group /processing/behavior (ProcessingModule) preprocessed behavioral data
  Group /processing/behavior/BehavioralTimeSeries (BehavioralTimeSeries) 
  Group /processing/behavior/BehavioralTimeSeries/running_velocity (TimeSeries) Velocity of the mouse on a rotating disc.
  Group /processing/ophys (ProcessingModule) OpenScope processing pipeline
  Group /processing/ophys/DfOverF (DfOverF) 
  Group /processing/ophys/DfOverF/RoiResponseSeries (RoiResponseSeries) ROI traces
  Dataset /processing/ophys/DfOverF/RoiResponseSeries/rois (DynamicTableRegion) Segmented cells with cell_specimen_ids (height x width) | shape = (6,) | dtype = int32
  Group /processing/ophys/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation (PlaneSegmentation) Segmentation for imaging plane (de Vries et al., 2019, Nat Neurosci)
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/id (ElementIdentifiers)  | shape = (6,) | dtype = int32
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (6, 512, 512) | dtype = uint8
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/device (Device) Allen Institute two-photon pipeline: CAM2P.1
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/optical_channel (OpticalChannel) 
  session_description: Allen Institute OpenScope dataset
  session_start_time: 2019-06-11T18:18:40.349000-07:00
  timestamps_reference_time: 2019-06-11T18:18:40.349000-07:00
