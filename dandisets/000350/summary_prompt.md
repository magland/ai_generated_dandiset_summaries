
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000350/0.240822.1759
name: Glia Accumulate Evidence that Actions Are Futile and Suppress Unsuccessful Behavior
contributor: [{'name': 'Mu, Yu', 'email': 'muy@janelia.hhmi.org', 'roleName': ['dcite:Author', 'dcite:Conceptualization', 'dcite:ContactPerson', 'dcite:DataCollector', 'dcite:DataManager'], 'schemaKey': 'Person', 'identifier': '0000-0001-9297-4854', 'affiliation': [{'name': 'Janelia Research Campus', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/013sk6x84'}], 'includeInCitation': True}, {'name': 'Bennett, Davis V.', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-5056-407X', 'affiliation': [{'name': 'Janelia Research Campus', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/013sk6x84'}, {'name': 'University of Chicago', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/024mw5h28'}], 'includeInCitation': True}, {'name': 'Rubinov, Mikail', 'roleName': ['dcite:Author', 'dcite:FormalAnalysis'], 'schemaKey': 'Person', 'identifier': '0000-0002-4787-7075', 'affiliation': [{'name': 'Janelia Research Campus', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/013sk6x84'}, {'name': 'Vanderbilt University', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/02vm5rt34'}], 'includeInCitation': True}, {'name': 'Lim, Jing-Xuan', 'roleName': ['dcite:DataManager'], 'schemaKey': 'Person', 'identifier': '0000-0002-5983-9164', 'affiliation': [{'name': 'Howard Hughes Medical Institute', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/006w34k90'}], 'includeInCitation': True}, {'name': 'Yang, Chao-Tsung', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [{'name': 'Janelia Research Campus', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/013sk6x84'}], 'includeInCitation': True}, {'name': 'Tanimoto, Masashi', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-7653-1081', 'affiliation': [{'name': 'Janelia Research Campus', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/013sk6x84'}], 'includeInCitation': True}, {'name': 'Mensh, Brett D. ', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0003-2288-054X', 'affiliation': [{'name': 'Janelia Research Campus', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/013sk6x84'}], 'includeInCitation': True}, {'name': 'Looger, Loren L.', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-7531-1757', 'affiliation': [{'name': 'Janelia Research Campus', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/013sk6x84'}], 'includeInCitation': True}, {'name': 'Narayan, Sujatha', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-3741-1319', 'affiliation': [{'name': 'Janelia Research Campus', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/013sk6x84'}], 'includeInCitation': True}, {'url': 'https://www.janelia.org/lab/ahrens-lab', 'name': 'Ahrens, Misha B.', 'email': 'ahrensm@janelia.hhmi.org', 'roleName': ['dcite:Author', 'dcite:Conceptualization', 'dcite:ContactPerson', 'dcite:Investigation', 'dcite:ProjectLeader', 'dcite:ProjectManager', 'dcite:ProjectAdministration'], 'schemaKey': 'Person', 'identifier': '0000-0002-3457-4462', 'affiliation': [{'name': 'Janelia Research Campus', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/013sk6x84'}], 'includeInCitation': True}, {'url': 'http://www.hhmi.org/', 'name': 'Howard Hughes Medical Institute', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/006w34k90', 'awardNumber': '325171', 'contactPoint': [], 'includeInCitation': False}, {'url': 'https://www.simonsfoundation.org', 'name': 'Simons Collaboration on the Global Brain Awards', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01cmst727', 'awardNumber': '542943SPI', 'contactPoint': [], 'includeInCitation': False}, {'url': 'https://www.catalystneuro.com/team/', 'name': 'Baker, Cody', 'email': 'cody.c.baker.phd@gmail.com', 'roleName': ['dcite:Software', 'dcite:DataCurator'], 'schemaKey': 'Person', 'identifier': '0000-0002-0829-4790', 'affiliation': [{'name': 'CatalystNeuro', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/01d74sk53'}], 'includeInCitation': False}]
description: When a behavior repeatedly fails to achieve its goal, animals often give up and become passive, which can be strategic for preserving energy or regrouping between attempts. It is unknown how the brain identifies behavioral failures and mediates this behavioral-state switch. In larval zebrafish swimming in virtual reality, visual feedback can be withheld so that swim attempts fail to trigger expected visual flow. After tens of seconds of such motor futility, animals became passive for similar durations. Whole-brain calcium imaging revealed noradrenergic neurons that responded specifically to failed swim attempts and radial astrocytes whose calcium levels accumulated with increasing numbers of failed attempts. Using cell ablation and optogenetic or chemogenetic activation, we found that noradrenergic neurons progressively activated brainstem radial astrocytes, which then suppressed swimming. Thus, radial astrocytes perform a computation critical for behavior: they accumulate evidence that current actions are ineffective and consequently drive changes in behavioral states.
assetsSummary: {'species': [{'name': 'Danio rerio - Zebra fish', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_7955'}], 'approach': [{'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 5865794202897, 'numberOfFiles': 12, 'numberOfSubjects': 12, 'variableMeasured': ['TwoPhotonSeries', 'OpticalChannel', 'ProcessingModule', 'ImagingPlane', 'PlaneSegmentation'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'two-photon microscopy technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000350 has 12 NWB files.
3 of these NWB files are of type 1.
2 of these NWB files are of type 2.
1 of these NWB files are of type 3.
4 of these NWB files are of type 4.
2 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/BaselineStimulusVelocitySignal (TimeSeries) Raw signal for drift speed of visual grating presented to the subject.
  Group /acquisition/FrameCaptureTTLSignal (TimeSeries) Raw synchronization signal detecting shutter activation for the optical physiology camera. Forms the basis of the timestamps for the TwoPhotonSeries and corresponding Fluorescence. Values of the TTL signal significantly above 3.5 indicate start of volume scan; values significantly close to 3.5 indicate the scan of a single plane.
  
  Group /acquisition/GliaOnePhotonSeries (TwoPhotonSeries) Full resolution of images from whole-brain calcium imaging.
  Group /acquisition/GliaOnePhotonSeries/imaging_plane (ImagingPlane) 
  Group /acquisition/GliaOnePhotonSeries/imaging_plane/GliaOpticalChannel (OpticalChannel) 
  Group /acquisition/GliaOnePhotonSeries/imaging_plane/device (Device) Confocal imaging was done using a Zeiss LSM 710, LSM 880 upright confocal, or a Zeiss LSM 800.
  Group /acquisition/StimulusGainSignal (TimeSeries) Raw signal tracking the gain of the visual stimulus.
  Group /acquisition/StimulusParameterSignals (TimeSeries) A collection of raw stimulus parameter signals.
  Group /acquisition/StimulusTypeSignal (TimeSeries) Raw signal tracking the type of the presented visual stimulus. Most of the time this will likely just be a binary signal for tracking the on/off status.
  
  Group /acquisition/SwimSignals (TimeSeries) Raw ephys signals from electrodes attached to the tail of the paralyzed subject. Tracks 'effective' motor output of subject for use in virtual reality environment. This is later classified to define the state intervals (Active vs. Passive) and trials (closed-loop or open-loop)
  
  Group /acquisition/TotalStimulusVelocitySignal (TimeSeries) Raw signal calculating (drift speed - motosensory gain) x swim power.
  file_create_date: ['2022-11-21T11:14:19.469846+00:00']
  Group /general/devices/Microscope (Device) Confocal imaging was done using a Zeiss LSM 710, LSM 880 upright confocal, or a Zeiss LSM 800.
  experiment_description: When a behavior repeatedly fails to achieve its goal, animals often give up and become passive, which can be strategic for preserving energy or regrouping between attempts. It is unknown how the brain identifies behavioral failures and mediates this behavioral-state switch. In larval zebrafish swimming in virtual reality, visual feedback can be withheld so that swim attempts fail to trigger expected visual flow. After tens of seconds of such motor futility, animals became passive for similar durations. Whole-brain calcium imaging revealed noradrenergic neurons that responded specifically to failed swim attempts and radial astrocytes whose calcium levels accumulated with increasing numbers of failed attempts. Using cell ablation and optogenetic or chemogenetic activation, we found that noradrenergic neurons progressively activated brainstem radial astrocytes, which then suppressed swimming. Thus, radial astrocytes perform a computation critical for behavior; they accumulate evidence that current actions are ineffective and consequently drive changes in behavioral states.
  
  experimenter: ['Mu, Yu' 'Bennett, Davis V.' 'Rubinov, Mikail' 'Narayan, Sujatha'
   'Yang, Chao-Tsung' 'Tanimoto, Masashi' 'Mensh, Brett D.'
   'Looger, Loren L.' 'Ahrens, Misha B.']
  institution: Janelia Research Campus
  keywords: ['neuroscience' 'glia' 'astrocytes' 'norepinephrine' 'noradrenaline'
   'learned helplessness' 'zebrafish' 'neuromodulation' 'behavioral states'
   'evidence accumulation']
  lab: Ahrens Lab
  Group /general/optophysiology/GliaVolume (ImagingPlane) 
  Group /general/optophysiology/GliaVolume/GliaOpticalChannel (OpticalChannel) 
  Group /general/optophysiology/GliaVolume/device (Device) Confocal imaging was done using a Zeiss LSM 710, LSM 880 upright confocal, or a Zeiss LSM 800.
  related_publications: ['https://doi.org/10.1016/j.cell.2019.05.050']
  Group /general/subject (Subject) 
  identifier: 85b1b021-bacf-496f-99ed-db7256104475
  Group /processing/behavior (ProcessingModule) Contains processed behavioral data.
  Group /processing/behavior/ActivityStates (TimeIntervals) Classified periods of activity (passive, active, or transient).
  Dataset /processing/behavior/ActivityStates/id (ElementIdentifiers)  | shape = (3,) | dtype = int64
  Dataset /processing/behavior/ActivityStates/start_time (VectorData) Start time of epoch, in seconds | shape = (3,) | dtype = float64
  Dataset /processing/behavior/ActivityStates/state_type (VectorData) The type of classified state. | shape = (3,) | dtype = object
  Dataset /processing/behavior/ActivityStates/stop_time (VectorData) Stop time of epoch, in seconds | shape = (3,) | dtype = float64
  Group /processing/behavior/BurstEvents (AnnotatedEventsTable) Events of classified bursting activity.
  Dataset /processing/behavior/BurstEvents/event_description (VectorData) Description for each event type. | shape = (1,) | dtype = object
  Dataset /processing/behavior/BurstEvents/event_times (VectorData) Event times for each event type. | shape = (5729,) | dtype = float64
  Dataset /processing/behavior/BurstEvents/event_times_index (VectorIndex) Index for VectorData 'event_times' | shape = (1,) | dtype = uint16
  Dataset /processing/behavior/BurstEvents/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /processing/behavior/BurstEvents/label (VectorData) Label for each event type. | shape = (1,) | dtype = object
  Group /processing/behavior/FilteredSwimSignals (TimeSeries) A filtered version of the raw SwimSignals in acquisition.
  Group /processing/behavior/SwimIntervals (TimeIntervals) Intervals of time when subject is estimated to be swimming.
  Dataset /processing/behavior/SwimIntervals/id (ElementIdentifiers)  | shape = (446,) | dtype = int64
  Dataset /processing/behavior/SwimIntervals/power (VectorData) Estimated power of the swim event. | shape = (446,) | dtype = float64
  Dataset /processing/behavior/SwimIntervals/start_time (VectorData) Start time of epoch, in seconds | shape = (446,) | dtype = float64
  Dataset /processing/behavior/SwimIntervals/stop_time (VectorData) Stop time of epoch, in seconds | shape = (446,) | dtype = float64
  Dataset /processing/behavior/SwimIntervals/width (VectorData) Estimated width spanned by the swim event. | shape = (446,) | dtype = float64
  session_description: A single-color optic channel recording of either a neuron or a glia population.
  session_start_time: 2016-10-22T15:10:03-04:00
  timestamps_reference_time: 2016-10-22T15:10:03-04:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/BaselineStimulusVelocitySignal (TimeSeries) Raw signal for drift speed of visual grating presented to the subject.
  Group /acquisition/FrameCaptureTTLSignal (TimeSeries) Raw synchronization signal detecting shutter activation for the optical physiology camera. Forms the basis of the timestamps for the TwoPhotonSeries and corresponding Fluorescence. Values of the TTL signal significantly above 3.5 indicate start of volume scan; values significantly close to 3.5 indicate the scan of a single plane.
  
  Group /acquisition/GliaOnePhotonSeries (TwoPhotonSeries) Full resolution images from glia-specific optical channel of whole-brain calcium imaging.
  Group /acquisition/GliaOnePhotonSeries/imaging_plane (ImagingPlane) 
  Group /acquisition/GliaOnePhotonSeries/imaging_plane/GliaOpticalChannel (OpticalChannel) 
  Group /acquisition/GliaOnePhotonSeries/imaging_plane/device (Device) Confocal imaging was done using LSM 710, LSM 880 upright, or LSM 800.
  Group /acquisition/NeuronOnePhotonSeries (TwoPhotonSeries) Full resolution images from neuron-specific optical channel of whole-brain calcium imaging.
  Group /acquisition/NeuronOnePhotonSeries/imaging_plane (ImagingPlane) 
  Group /acquisition/NeuronOnePhotonSeries/imaging_plane/NeuronOpticalChannel (OpticalChannel) 
  Group /acquisition/NeuronOnePhotonSeries/imaging_plane/device (Device) Confocal imaging was done using LSM 710, LSM 880 upright, or LSM 800.
  Group /acquisition/StimulusGainSignal (TimeSeries) Raw signal tracking the gain of the visual stimulus.
  Group /acquisition/StimulusParameterSignals (TimeSeries) A collection of raw stimulus parameter signals.
  Group /acquisition/StimulusTypeSignal (TimeSeries) Raw signal tracking the type of the presented visual stimulus. Most of the time this will likely just be a binary signal for tracking the on/off status.
  
  Group /acquisition/SwimSignals (TimeSeries) Raw ephys signals from electrodes attached to the tail of the paralyzed subject. Tracks 'effective' motor output of subject for use in virtual reality environment. This is later classified to define the state intervals (Active vs. Passive) and trials (closed-loop or open-loop)
  
  Group /acquisition/TotalStimulusVelocitySignal (TimeSeries) Raw signal calculating (drift speed - motosensory gain) x swim power.
  file_create_date: ['2022-11-05T02:29:16.920789+00:00']
  Group /general/devices/Microscope (Device) Confocal imaging was done using LSM 710, LSM 880 upright, or LSM 800.
  experiment_description: When a behavior repeatedly fails to achieve its goal, animals often give up and become passive, which can be strategic for preserving energy or regrouping between attempts. It is unknown how the brain identifies behavioral failures and mediates this behavioral-state switch. In larval zebrafish swimming in virtual reality, visual feedback can be withheld so that swim attempts fail to trigger expected visual flow. After tens of seconds of such motor futility, animals became passive for similar durations. Whole-brain calcium imaging revealed noradrenergic neurons that responded specifically to failed swim attempts and radial astrocytes whose calcium levels accumulated with increasing numbers of failed attempts. Using cell ablation and optogenetic or chemogenetic activation, we found that noradrenergic neurons progressively activated brainstem radial astrocytes, which then suppressed swimming. Thus, radial astrocytes perform a computation critical for behavior; they accumulate evidence that current actions are ineffective and consequently drive changes in behavioral states.
  
  experimenter: ['Mu, Yu' 'Bennett, Davis V.' 'Rubinov, Mikail' 'Narayan, Sujatha'
   'Yang, Chao-Tsung' 'Tanimoto, Masashi' 'Mensh, Brett D.'
   'Looger, Loren L.' 'Ahrens, Misha B.']
  institution: Janelia Research Campus
  keywords: ['neuroscience' 'glia' 'astrocytes' 'norepinephrine' 'noradrenaline'
   'learned helplessness' 'zebrafish' 'neuromodulation' 'behavioral states'
   'evidence accumulation']
  lab: Ahrens Lab
  Group /general/optophysiology/GliaVolume (ImagingPlane) 
  Group /general/optophysiology/GliaVolume/GliaOpticalChannel (OpticalChannel) 
  Group /general/optophysiology/GliaVolume/device (Device) Confocal imaging was done using LSM 710, LSM 880 upright, or LSM 800.
  Group /general/optophysiology/NeuronVolume (ImagingPlane) 
  Group /general/optophysiology/NeuronVolume/NeuronOpticalChannel (OpticalChannel) 
  Group /general/optophysiology/NeuronVolume/device (Device) Confocal imaging was done using LSM 710, LSM 880 upright, or LSM 800.
  related_publications: ['https://doi.org/10.1016/j.cell.2019.05.050']
  Group /general/subject (Subject) 
  identifier: 90da1b0e-181c-4ded-b756-898aa365de6f
  Group /processing/behavior (ProcessingModule) Contains processed behavioral data.
  Group /processing/behavior/ActivityStates (TimeIntervals) Classified periods of activity (passive, active, or transient).
  Dataset /processing/behavior/ActivityStates/id (ElementIdentifiers)  | shape = (80,) | dtype = int64
  Dataset /processing/behavior/ActivityStates/start_time (VectorData) Start time of epoch, in seconds | shape = (80,) | dtype = float64
  Dataset /processing/behavior/ActivityStates/state_type (VectorData) The type of classified state. | shape = (80,) | dtype = object
  Dataset /processing/behavior/ActivityStates/stop_time (VectorData) Stop time of epoch, in seconds | shape = (80,) | dtype = float64
  Group /processing/behavior/BurstEvents (AnnotatedEventsTable) Events of classified bursting activity.
  Dataset /processing/behavior/BurstEvents/event_description (VectorData) Description for each event type. | shape = (1,) | dtype = object
  Dataset /processing/behavior/BurstEvents/event_times (VectorData) Event times for each event type. | shape = (14122,) | dtype = float64
  Dataset /processing/behavior/BurstEvents/event_times_index (VectorIndex) Index for VectorData 'event_times' | shape = (1,) | dtype = uint16
  Dataset /processing/behavior/BurstEvents/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /processing/behavior/BurstEvents/label (VectorData) Label for each event type. | shape = (1,) | dtype = object
  Group /processing/behavior/FilteredSwimSignals (TimeSeries) A filtered version of the raw SwimSignals in acquisition.
  Group /processing/behavior/SwimIntervals (TimeIntervals) Intervals of time when subject is estimated to be swimming.
  Dataset /processing/behavior/SwimIntervals/id (ElementIdentifiers)  | shape = (2550,) | dtype = int64
  Dataset /processing/behavior/SwimIntervals/power (VectorData) Estimated power of the swim event. | shape = (2550,) | dtype = float64
  Dataset /processing/behavior/SwimIntervals/start_time (VectorData) Start time of epoch, in seconds | shape = (2550,) | dtype = float64
  Dataset /processing/behavior/SwimIntervals/stop_time (VectorData) Stop time of epoch, in seconds | shape = (2550,) | dtype = float64
  Dataset /processing/behavior/SwimIntervals/width (VectorData) Estimated width spanned by the swim event. | shape = (2550,) | dtype = float64
  Group /processing/ophys (ProcessingModule) optical physiology processed data
  Group /processing/ophys/DfOverF (DfOverF) 
  Group /processing/ophys/DfOverF/GliaDfOverF (RoiResponseSeries) Segmented regions of interest (ROIs) and detrended activity for the glia indicator type.
  Dataset /processing/ophys/DfOverF/GliaDfOverF/rois (DynamicTableRegion) Region reference to ROI table. | shape = (100840,) | dtype = int64
  Group /processing/ophys/DfOverF/NeuronDfOverF (RoiResponseSeries) Segmented regions of interest (ROIs) and detrended activity for the neuron indicator type.
  Dataset /processing/ophys/DfOverF/NeuronDfOverF/rois (DynamicTableRegion) Region reference to ROI table. | shape = (109918,) | dtype = int64
  Group /processing/ophys/Fluorescence (Fluorescence) 
  Group /processing/ophys/Fluorescence/GliaFluorescence (RoiResponseSeries) Segmented regions of interest (ROIs) and detrended activity for the glia indicator type.
  Dataset /processing/ophys/Fluorescence/GliaFluorescence/rois (DynamicTableRegion) Region reference to ROI table. | shape = (100840,) | dtype = int64
  Group /processing/ophys/Fluorescence/NeuronFluorescence (RoiResponseSeries) Segmented regions of interest (ROIs) and detrended activity for the neuron indicator type.
  Dataset /processing/ophys/Fluorescence/NeuronFluorescence/rois (DynamicTableRegion) Region reference to ROI table. | shape = (109918,) | dtype = int64
  Group /processing/ophys/VolumeSegmentation (ImageSegmentation) 
  Group /processing/ophys/VolumeSegmentation/GliaVolumeSegmentation (PlaneSegmentation) Segmented ROIs for the glia.
  Dataset /processing/ophys/VolumeSegmentation/GliaVolumeSegmentation/id (ElementIdentifiers)  | shape = (100840,) | dtype = int64
  Group /processing/ophys/VolumeSegmentation/GliaVolumeSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys/VolumeSegmentation/GliaVolumeSegmentation/imaging_plane/GliaOpticalChannel (OpticalChannel) 
  Group /processing/ophys/VolumeSegmentation/GliaVolumeSegmentation/imaging_plane/device (Device) Confocal imaging was done using LSM 710, LSM 880 upright, or LSM 800.
  Group /processing/ophys/VolumeSegmentation/GliaVolumeSegmentation/reference_images/GliaOnePhotonSeries (TwoPhotonSeries) Full resolution images from glia-specific optical channel of whole-brain calcium imaging.
  Group /processing/ophys/VolumeSegmentation/GliaVolumeSegmentation/reference_images/GliaOnePhotonSeries/imaging_plane (ImagingPlane) 
  Group /processing/ophys/VolumeSegmentation/GliaVolumeSegmentation/reference_images/GliaOnePhotonSeries/imaging_plane/GliaOpticalChannel (OpticalChannel) 
  Group /processing/ophys/VolumeSegmentation/GliaVolumeSegmentation/reference_images/GliaOnePhotonSeries/imaging_plane/device (Device) Confocal imaging was done using LSM 710, LSM 880 upright, or LSM 800.
  Dataset /processing/ophys/VolumeSegmentation/GliaVolumeSegmentation/voxel_mask (VectorData) Voxel masks for each ROI | shape = (5903864,) | dtype = [('x', '<u4'), ('y', '<u4'), ('z', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/VolumeSegmentation/GliaVolumeSegmentation/voxel_mask_index (VectorIndex) Index for VectorData 'voxel_mask' | shape = (100840,) | dtype = uint32
  Group /processing/ophys/VolumeSegmentation/NeuronVolumeSegmentation (PlaneSegmentation) Segmented ROIs for the neurons.
  Dataset /processing/ophys/VolumeSegmentation/NeuronVolumeSegmentation/id (ElementIdentifiers)  | shape = (109918,) | dtype = int64
  Group /processing/ophys/VolumeSegmentation/NeuronVolumeSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys/VolumeSegmentation/NeuronVolumeSegmentation/imaging_plane/NeuronOpticalChannel (OpticalChannel) 
  Group /processing/ophys/VolumeSegmentation/NeuronVolumeSegmentation/imaging_plane/device (Device) Confocal imaging was done using LSM 710, LSM 880 upright, or LSM 800.
  Group /processing/ophys/VolumeSegmentation/NeuronVolumeSegmentation/reference_images/NeuronOnePhotonSeries (TwoPhotonSeries) Full resolution images from neuron-specific optical channel of whole-brain calcium imaging.
  Group /processing/ophys/VolumeSegmentation/NeuronVolumeSegmentation/reference_images/NeuronOnePhotonSeries/imaging_plane (ImagingPlane) 
  Group /processing/ophys/VolumeSegmentation/NeuronVolumeSegmentation/reference_images/NeuronOnePhotonSeries/imaging_plane/NeuronOpticalChannel (OpticalChannel) 
  Group /processing/ophys/VolumeSegmentation/NeuronVolumeSegmentation/reference_images/NeuronOnePhotonSeries/imaging_plane/device (Device) Confocal imaging was done using LSM 710, LSM 880 upright, or LSM 800.
  Dataset /processing/ophys/VolumeSegmentation/NeuronVolumeSegmentation/voxel_mask (VectorData) Voxel masks for each ROI | shape = (6439825,) | dtype = [('x', '<u4'), ('y', '<u4'), ('z', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/VolumeSegmentation/NeuronVolumeSegmentation/voxel_mask_index (VectorIndex) Index for VectorData 'voxel_mask' | shape = (109918,) | dtype = uint32
  session_description: A dual-color optic channel recording of both neuron and glia populations.
  session_start_time: 2016-11-09T21:19:50-05:00
  timestamps_reference_time: 2016-11-09T21:19:50-05:00


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/BaselineStimulusVelocitySignal (TimeSeries) Raw signal for drift speed of visual grating presented to the subject.
  Group /acquisition/FrameCaptureTTLSignal (TimeSeries) Raw synchronization signal detecting shutter activation for the optical physiology camera. Forms the basis of the timestamps for the TwoPhotonSeries and corresponding Fluorescence. Values of the TTL signal significantly above 3.5 indicate start of volume scan; values significantly close to 3.5 indicate the scan of a single plane.
  
  Group /acquisition/NeuronOnePhotonSeries (TwoPhotonSeries) Full resolution of images from whole-brain calcium imaging.
  Group /acquisition/NeuronOnePhotonSeries/imaging_plane (ImagingPlane) 
  Group /acquisition/NeuronOnePhotonSeries/imaging_plane/NeuronOpticalChannel (OpticalChannel) 
  Group /acquisition/NeuronOnePhotonSeries/imaging_plane/device (Device) Confocal imaging was done using a Zeiss LSM 710, LSM 880 upright confocal, or a Zeiss LSM 800.
  Group /acquisition/StimulusGainSignal (TimeSeries) Raw signal tracking the gain of the visual stimulus.
  Group /acquisition/StimulusParameterSignals (TimeSeries) A collection of raw stimulus parameter signals.
  Group /acquisition/StimulusTypeSignal (TimeSeries) Raw signal tracking the type of the presented visual stimulus. Most of the time this will likely just be a binary signal for tracking the on/off status.
  
  Group /acquisition/SwimSignals (TimeSeries) Raw ephys signals from electrodes attached to the tail of the paralyzed subject. Tracks 'effective' motor output of subject for use in virtual reality environment. This is later classified to define the state intervals (Active vs. Passive) and trials (closed-loop or open-loop)
  
  Group /acquisition/TotalStimulusVelocitySignal (TimeSeries) Raw signal calculating (drift speed - motosensory gain) x swim power.
  file_create_date: ['2022-11-21T11:14:19.458103+00:00']
  Group /general/devices/Microscope (Device) Confocal imaging was done using a Zeiss LSM 710, LSM 880 upright confocal, or a Zeiss LSM 800.
  experiment_description: When a behavior repeatedly fails to achieve its goal, animals often give up and become passive, which can be strategic for preserving energy or regrouping between attempts. It is unknown how the brain identifies behavioral failures and mediates this behavioral-state switch. In larval zebrafish swimming in virtual reality, visual feedback can be withheld so that swim attempts fail to trigger expected visual flow. After tens of seconds of such motor futility, animals became passive for similar durations. Whole-brain calcium imaging revealed noradrenergic neurons that responded specifically to failed swim attempts and radial astrocytes whose calcium levels accumulated with increasing numbers of failed attempts. Using cell ablation and optogenetic or chemogenetic activation, we found that noradrenergic neurons progressively activated brainstem radial astrocytes, which then suppressed swimming. Thus, radial astrocytes perform a computation critical for behavior; they accumulate evidence that current actions are ineffective and consequently drive changes in behavioral states.
  
  experimenter: ['Mu, Yu' 'Bennett, Davis V.' 'Rubinov, Mikail' 'Narayan, Sujatha'
   'Yang, Chao-Tsung' 'Tanimoto, Masashi' 'Mensh, Brett D.'
   'Looger, Loren L.' 'Ahrens, Misha B.']
  institution: Janelia Research Campus
  keywords: ['neuroscience' 'glia' 'astrocytes' 'norepinephrine' 'noradrenaline'
   'learned helplessness' 'zebrafish' 'neuromodulation' 'behavioral states'
   'evidence accumulation']
  lab: Ahrens Lab
  Group /general/optophysiology/NeuronVolume (ImagingPlane) 
  Group /general/optophysiology/NeuronVolume/NeuronOpticalChannel (OpticalChannel) 
  Group /general/optophysiology/NeuronVolume/device (Device) Confocal imaging was done using a Zeiss LSM 710, LSM 880 upright confocal, or a Zeiss LSM 800.
  related_publications: ['https://doi.org/10.1016/j.cell.2019.05.050']
  Group /general/subject (Subject) 
  identifier: 05da7bfc-a2c5-483c-8413-0e6510e97dd4
  Group /processing/behavior (ProcessingModule) Contains processed behavioral data.
  Group /processing/behavior/ActivityStates (TimeIntervals) Classified periods of activity (passive, active, or transient).
  Dataset /processing/behavior/ActivityStates/id (ElementIdentifiers)  | shape = (108,) | dtype = int64
  Dataset /processing/behavior/ActivityStates/start_time (VectorData) Start time of epoch, in seconds | shape = (108,) | dtype = float64
  Dataset /processing/behavior/ActivityStates/state_type (VectorData) The type of classified state. | shape = (108,) | dtype = object
  Dataset /processing/behavior/ActivityStates/stop_time (VectorData) Stop time of epoch, in seconds | shape = (108,) | dtype = float64
  Group /processing/behavior/BurstEvents (AnnotatedEventsTable) Events of classified bursting activity.
  Dataset /processing/behavior/BurstEvents/event_description (VectorData) Description for each event type. | shape = (1,) | dtype = object
  Dataset /processing/behavior/BurstEvents/event_times (VectorData) Event times for each event type. | shape = (7073,) | dtype = float64
  Dataset /processing/behavior/BurstEvents/event_times_index (VectorIndex) Index for VectorData 'event_times' | shape = (1,) | dtype = uint16
  Dataset /processing/behavior/BurstEvents/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /processing/behavior/BurstEvents/label (VectorData) Label for each event type. | shape = (1,) | dtype = object
  Group /processing/behavior/FilteredSwimSignals (TimeSeries) A filtered version of the raw SwimSignals in acquisition.
  Group /processing/behavior/SwimIntervals (TimeIntervals) Intervals of time when subject is estimated to be swimming.
  Dataset /processing/behavior/SwimIntervals/id (ElementIdentifiers)  | shape = (1014,) | dtype = int64
  Dataset /processing/behavior/SwimIntervals/power (VectorData) Estimated power of the swim event. | shape = (1014,) | dtype = float64
  Dataset /processing/behavior/SwimIntervals/start_time (VectorData) Start time of epoch, in seconds | shape = (1014,) | dtype = float64
  Dataset /processing/behavior/SwimIntervals/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1014,) | dtype = float64
  Dataset /processing/behavior/SwimIntervals/width (VectorData) Estimated width spanned by the swim event. | shape = (1014,) | dtype = float64
  session_description: A single-color optic channel recording of either a neuron or a glia population.
  session_start_time: 2017-01-11T12:33:55-05:00
  timestamps_reference_time: 2017-01-11T12:33:55-05:00


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/BaselineStimulusVelocitySignal (TimeSeries) Raw signal for drift speed of visual grating presented to the subject.
  Group /acquisition/FrameCaptureTTLSignal (TimeSeries) Raw synchronization signal detecting shutter activation for the optical physiology camera. Forms the basis of the timestamps for the TwoPhotonSeries and corresponding Fluorescence. Values of the TTL signal significantly above 3.5 indicate start of volume scan; values significantly close to 3.5 indicate the scan of a single plane.
  
  Group /acquisition/NeuronOnePhotonSeries (TwoPhotonSeries) Full resolution of images from whole-brain calcium imaging.
  Group /acquisition/NeuronOnePhotonSeries/imaging_plane (ImagingPlane) 
  Group /acquisition/NeuronOnePhotonSeries/imaging_plane/NeuronOpticalChannel (OpticalChannel) 
  Group /acquisition/NeuronOnePhotonSeries/imaging_plane/device (Device) Confocal imaging was done using a Zeiss LSM 710, LSM 880 upright confocal, or a Zeiss LSM 800.
  Group /acquisition/StimulusGainSignal (TimeSeries) Raw signal tracking the gain of the visual stimulus.
  Group /acquisition/StimulusParameterSignals (TimeSeries) A collection of raw stimulus parameter signals.
  Group /acquisition/StimulusTypeSignal (TimeSeries) Raw signal tracking the type of the presented visual stimulus. Most of the time this will likely just be a binary signal for tracking the on/off status.
  
  Group /acquisition/SwimSignals (TimeSeries) Raw ephys signals from electrodes attached to the tail of the paralyzed subject. Tracks 'effective' motor output of subject for use in virtual reality environment. This is later classified to define the state intervals (Active vs. Passive) and trials (closed-loop or open-loop)
  
  Group /acquisition/TotalStimulusVelocitySignal (TimeSeries) Raw signal calculating (drift speed - motosensory gain) x swim power.
  file_create_date: ['2022-11-03T04:01:13.549691+00:00']
  Group /general/devices/Microscope (Device) Confocal imaging was done using a Zeiss LSM 710, LSM 880 upright confocal, or a Zeiss LSM 800.
  experiment_description: When a behavior repeatedly fails to achieve its goal, animals often give up and become passive, which can be strategic for preserving energy or regrouping between attempts. It is unknown how the brain identifies behavioral failures and mediates this behavioral-state switch. In larval zebrafish swimming in virtual reality, visual feedback can be withheld so that swim attempts fail to trigger expected visual flow. After tens of seconds of such motor futility, animals became passive for similar durations. Whole-brain calcium imaging revealed noradrenergic neurons that responded specifically to failed swim attempts and radial astrocytes whose calcium levels accumulated with increasing numbers of failed attempts. Using cell ablation and optogenetic or chemogenetic activation, we found that noradrenergic neurons progressively activated brainstem radial astrocytes, which then suppressed swimming. Thus, radial astrocytes perform a computation critical for behavior; they accumulate evidence that current actions are ineffective and consequently drive changes in behavioral states.
  
  experimenter: ['Mu, Yu' 'Bennett, Davis V.' 'Rubinov, Mikail' 'Narayan, Sujatha'
   'Yang, Chao-Tsung' 'Tanimoto, Masashi' 'Mensh, Brett D.'
   'Looger, Loren L.' 'Ahrens, Misha B.']
  institution: Janelia Research Campus
  keywords: ['neuroscience' 'glia' 'astrocytes' 'norepinephrine' 'noradrenaline'
   'learned helplessness' 'zebrafish' 'neuromodulation' 'behavioral states'
   'evidence accumulation']
  lab: Ahrens Lab
  Group /general/optophysiology/NeuronVolume (ImagingPlane) 
  Group /general/optophysiology/NeuronVolume/NeuronOpticalChannel (OpticalChannel) 
  Group /general/optophysiology/NeuronVolume/device (Device) Confocal imaging was done using a Zeiss LSM 710, LSM 880 upright confocal, or a Zeiss LSM 800.
  related_publications: ['https://doi.org/10.1016/j.cell.2019.05.050']
  Group /general/subject (Subject) 
  identifier: 29091915-5f29-4477-853f-ca5d30c6d16a
  Group /processing/behavior (ProcessingModule) Contains processed behavioral data.
  Group /processing/behavior/ActivityStates (TimeIntervals) Classified periods of activity (passive, active, or transient).
  Dataset /processing/behavior/ActivityStates/id (ElementIdentifiers)  | shape = (196,) | dtype = int64
  Dataset /processing/behavior/ActivityStates/start_time (VectorData) Start time of epoch, in seconds | shape = (196,) | dtype = float64
  Dataset /processing/behavior/ActivityStates/state_type (VectorData) The type of classified state. | shape = (196,) | dtype = object
  Dataset /processing/behavior/ActivityStates/stop_time (VectorData) Stop time of epoch, in seconds | shape = (196,) | dtype = float64
  Group /processing/behavior/BurstEvents (AnnotatedEventsTable) Events of classified bursting activity.
  Dataset /processing/behavior/BurstEvents/event_description (VectorData) Description for each event type. | shape = (1,) | dtype = object
  Dataset /processing/behavior/BurstEvents/event_times (VectorData) Event times for each event type. | shape = (22226,) | dtype = float64
  Dataset /processing/behavior/BurstEvents/event_times_index (VectorIndex) Index for VectorData 'event_times' | shape = (1,) | dtype = uint16
  Dataset /processing/behavior/BurstEvents/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /processing/behavior/BurstEvents/label (VectorData) Label for each event type. | shape = (1,) | dtype = object
  Group /processing/behavior/FilteredSwimSignals (TimeSeries) A filtered version of the raw SwimSignals in acquisition.
  Group /processing/behavior/SwimIntervals (TimeIntervals) Intervals of time when subject is estimated to be swimming.
  Dataset /processing/behavior/SwimIntervals/id (ElementIdentifiers)  | shape = (1126,) | dtype = int64
  Dataset /processing/behavior/SwimIntervals/power (VectorData) Estimated power of the swim event. | shape = (1126,) | dtype = float64
  Dataset /processing/behavior/SwimIntervals/start_time (VectorData) Start time of epoch, in seconds | shape = (1126,) | dtype = float64
  Dataset /processing/behavior/SwimIntervals/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1126,) | dtype = float64
  Dataset /processing/behavior/SwimIntervals/width (VectorData) Estimated width spanned by the swim event. | shape = (1126,) | dtype = float64
  Group /processing/ophys (ProcessingModule) Processed data for the optical physiology.
  Group /processing/ophys/DfOverF (DfOverF) 
  Group /processing/ophys/DfOverF/NeuronDfOverF (RoiResponseSeries) Segmented regions of interest (ROIs) and detrended activity for the neuron indicator type.
  Dataset /processing/ophys/DfOverF/NeuronDfOverF/rois (DynamicTableRegion) Region reference to ROI table. | shape = (85452,) | dtype = int64
  Group /processing/ophys/Fluorescence (Fluorescence) 
  Group /processing/ophys/Fluorescence/NeuronFluorescence (RoiResponseSeries) Segmented regions of interest (ROIs) and detrended activity for the neuron indicator type.
  Dataset /processing/ophys/Fluorescence/NeuronFluorescence/rois (DynamicTableRegion) Region reference to ROI table. | shape = (85452,) | dtype = int64
  Group /processing/ophys/VolumeSegmentation (ImageSegmentation) 
  Group /processing/ophys/VolumeSegmentation/NeuronVolumeSegmentation (PlaneSegmentation) Segmented ROIs for the neural cells.
  Dataset /processing/ophys/VolumeSegmentation/NeuronVolumeSegmentation/id (ElementIdentifiers)  | shape = (85452,) | dtype = int64
  Group /processing/ophys/VolumeSegmentation/NeuronVolumeSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys/VolumeSegmentation/NeuronVolumeSegmentation/imaging_plane/NeuronOpticalChannel (OpticalChannel) 
  Group /processing/ophys/VolumeSegmentation/NeuronVolumeSegmentation/imaging_plane/device (Device) Confocal imaging was done using a Zeiss LSM 710, LSM 880 upright confocal, or a Zeiss LSM 800.
  Dataset /processing/ophys/VolumeSegmentation/NeuronVolumeSegmentation/voxel_mask (VectorData) Voxel masks for each ROI | shape = (8017183,) | dtype = [('x', '<u4'), ('y', '<u4'), ('z', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/VolumeSegmentation/NeuronVolumeSegmentation/voxel_mask_index (VectorIndex) Index for VectorData 'voxel_mask' | shape = (85452,) | dtype = uint32
  session_description: See the experiment_description.
  session_start_time: 2017-01-13T12:49:07-05:00
  timestamps_reference_time: 2017-01-13T12:49:07-05:00


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  Group /acquisition/BaselineStimulusVelocitySignal (TimeSeries) Raw signal for drift speed of visual grating presented to the subject.
  Group /acquisition/FrameCaptureTTLSignal (TimeSeries) Raw synchronization signal detecting shutter activation for the optical physiology camera. Forms the basis of the timestamps for the TwoPhotonSeries and corresponding Fluorescence. Values of the TTL signal significantly above 3.5 indicate start of volume scan; values significantly close to 3.5 indicate the scan of a single plane.
  
  Group /acquisition/GliaOnePhotonSeries (TwoPhotonSeries) Full resolution images from glia-specific optical channel of whole-brain calcium imaging.
  Group /acquisition/GliaOnePhotonSeries/imaging_plane (ImagingPlane) 
  Group /acquisition/GliaOnePhotonSeries/imaging_plane/GliaOpticalChannel (OpticalChannel) 
  Group /acquisition/GliaOnePhotonSeries/imaging_plane/device (Device) Confocal imaging was done using LSM 710, LSM 880 upright, or LSM 800.
  Group /acquisition/NeuronOnePhotonSeries (TwoPhotonSeries) Full resolution images from neuron-specific optical channel of whole-brain calcium imaging.
  Group /acquisition/NeuronOnePhotonSeries/imaging_plane (ImagingPlane) 
  Group /acquisition/NeuronOnePhotonSeries/imaging_plane/NeuronOpticalChannel (OpticalChannel) 
  Group /acquisition/NeuronOnePhotonSeries/imaging_plane/device (Device) Confocal imaging was done using LSM 710, LSM 880 upright, or LSM 800.
  Group /acquisition/StimulusGainSignal (TimeSeries) Raw signal tracking the gain of the visual stimulus.
  Group /acquisition/StimulusParameterSignals (TimeSeries) A collection of raw stimulus parameter signals.
  Group /acquisition/StimulusTypeSignal (TimeSeries) Raw signal tracking the type of the presented visual stimulus. Most of the time this will likely just be a binary signal for tracking the on/off status.
  
  Group /acquisition/SwimSignals (TimeSeries) Raw ephys signals from electrodes attached to the tail of the paralyzed subject. Tracks 'effective' motor output of subject for use in virtual reality environment. This is later classified to define the state intervals (Active vs. Passive) and trials (closed-loop or open-loop)
  
  Group /acquisition/TotalStimulusVelocitySignal (TimeSeries) Raw signal calculating (drift speed - motosensory gain) x swim power.
  file_create_date: ['2022-11-13T15:36:01.809774+00:00']
  Group /general/devices/Microscope (Device) Confocal imaging was done using LSM 710, LSM 880 upright, or LSM 800.
  experiment_description: When a behavior repeatedly fails to achieve its goal, animals often give up and become passive, which can be strategic for preserving energy or regrouping between attempts. It is unknown how the brain identifies behavioral failures and mediates this behavioral-state switch. In larval zebrafish swimming in virtual reality, visual feedback can be withheld so that swim attempts fail to trigger expected visual flow. After tens of seconds of such motor futility, animals became passive for similar durations. Whole-brain calcium imaging revealed noradrenergic neurons that responded specifically to failed swim attempts and radial astrocytes whose calcium levels accumulated with increasing numbers of failed attempts. Using cell ablation and optogenetic or chemogenetic activation, we found that noradrenergic neurons progressively activated brainstem radial astrocytes, which then suppressed swimming. Thus, radial astrocytes perform a computation critical for behavior; they accumulate evidence that current actions are ineffective and consequently drive changes in behavioral states.
  
  experimenter: ['Mu, Yu' 'Bennett, Davis V.' 'Rubinov, Mikail' 'Narayan, Sujatha'
   'Yang, Chao-Tsung' 'Tanimoto, Masashi' 'Mensh, Brett D.'
   'Looger, Loren L.' 'Ahrens, Misha B.']
  institution: Janelia Research Campus
  keywords: ['neuroscience' 'glia' 'astrocytes' 'norepinephrine' 'noradrenaline'
   'learned helplessness' 'zebrafish' 'neuromodulation' 'behavioral states'
   'evidence accumulation']
  lab: Ahrens Lab
  Group /general/optophysiology/GliaVolume (ImagingPlane) 
  Group /general/optophysiology/GliaVolume/GliaOpticalChannel (OpticalChannel) 
  Group /general/optophysiology/GliaVolume/device (Device) Confocal imaging was done using LSM 710, LSM 880 upright, or LSM 800.
  Group /general/optophysiology/NeuronVolume (ImagingPlane) 
  Group /general/optophysiology/NeuronVolume/NeuronOpticalChannel (OpticalChannel) 
  Group /general/optophysiology/NeuronVolume/device (Device) Confocal imaging was done using LSM 710, LSM 880 upright, or LSM 800.
  related_publications: ['https://doi.org/10.1016/j.cell.2019.05.050']
  Group /general/subject (Subject) 
  identifier: 87046eac-745a-47a7-8625-35254e9fbcde
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (146,) | dtype = int64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (146,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (146,) | dtype = float64
  Dataset /intervals/trials/trial_type (VectorData) Closed-loop, open-loop, or other. | shape = (146,) | dtype = object
  Group /processing/behavior (ProcessingModule) Contains processed behavioral data.
  Group /processing/behavior/ActivityStates (TimeIntervals) Classified periods of activity (passive, active, or transient).
  Dataset /processing/behavior/ActivityStates/id (ElementIdentifiers)  | shape = (246,) | dtype = int64
  Dataset /processing/behavior/ActivityStates/start_time (VectorData) Start time of epoch, in seconds | shape = (246,) | dtype = float64
  Dataset /processing/behavior/ActivityStates/state_type (VectorData) The type of classified state. | shape = (246,) | dtype = object
  Dataset /processing/behavior/ActivityStates/stop_time (VectorData) Stop time of epoch, in seconds | shape = (246,) | dtype = float64
  Group /processing/behavior/BurstEvents (AnnotatedEventsTable) Events of classified bursting activity.
  Dataset /processing/behavior/BurstEvents/event_description (VectorData) Description for each event type. | shape = (1,) | dtype = object
  Dataset /processing/behavior/BurstEvents/event_times (VectorData) Event times for each event type. | shape = (13773,) | dtype = float64
  Dataset /processing/behavior/BurstEvents/event_times_index (VectorIndex) Index for VectorData 'event_times' | shape = (1,) | dtype = uint16
  Dataset /processing/behavior/BurstEvents/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /processing/behavior/BurstEvents/label (VectorData) Label for each event type. | shape = (1,) | dtype = object
  Group /processing/behavior/FilteredSwimSignals (TimeSeries) A filtered version of the raw SwimSignals in acquisition.
  Group /processing/behavior/SwimIntervals (TimeIntervals) Intervals of time when subject is estimated to be swimming.
  Dataset /processing/behavior/SwimIntervals/id (ElementIdentifiers)  | shape = (559,) | dtype = int64
  Dataset /processing/behavior/SwimIntervals/power (VectorData) Estimated power of the swim event. | shape = (559,) | dtype = float64
  Dataset /processing/behavior/SwimIntervals/start_time (VectorData) Start time of epoch, in seconds | shape = (559,) | dtype = float64
  Dataset /processing/behavior/SwimIntervals/stop_time (VectorData) Stop time of epoch, in seconds | shape = (559,) | dtype = float64
  Dataset /processing/behavior/SwimIntervals/width (VectorData) Estimated width spanned by the swim event. | shape = (559,) | dtype = float64
  Group /processing/ophys (ProcessingModule) optical physiology processed data
  Group /processing/ophys/DfOverF (DfOverF) 
  Group /processing/ophys/DfOverF/GliaDfOverF (RoiResponseSeries) Segmented regions of interest (ROIs) and detrended activity for the glia indicator type.
  Dataset /processing/ophys/DfOverF/GliaDfOverF/rois (DynamicTableRegion) Region reference to ROI table. | shape = (126467,) | dtype = int64
  Group /processing/ophys/DfOverF/NeuronDfOverF (RoiResponseSeries) Segmented regions of interest (ROIs) and detrended activity for the neuron indicator type.
  Dataset /processing/ophys/DfOverF/NeuronDfOverF/rois (DynamicTableRegion) Region reference to ROI table. | shape = (111378,) | dtype = int64
  Group /processing/ophys/Fluorescence (Fluorescence) 
  Group /processing/ophys/Fluorescence/GliaFluorescence (RoiResponseSeries) Segmented regions of interest (ROIs) and detrended activity for the glia indicator type.
  Dataset /processing/ophys/Fluorescence/GliaFluorescence/rois (DynamicTableRegion) Region reference to ROI table. | shape = (126467,) | dtype = int64
  Group /processing/ophys/Fluorescence/NeuronFluorescence (RoiResponseSeries) Segmented regions of interest (ROIs) and detrended activity for the neuron indicator type.
  Dataset /processing/ophys/Fluorescence/NeuronFluorescence/rois (DynamicTableRegion) Region reference to ROI table. | shape = (111378,) | dtype = int64
  Group /processing/ophys/VolumeSegmentation (ImageSegmentation) 
  Group /processing/ophys/VolumeSegmentation/GliaVolumeSegmentation (PlaneSegmentation) Segmented ROIs for the glia.
  Dataset /processing/ophys/VolumeSegmentation/GliaVolumeSegmentation/id (ElementIdentifiers)  | shape = (126467,) | dtype = int64
  Group /processing/ophys/VolumeSegmentation/GliaVolumeSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys/VolumeSegmentation/GliaVolumeSegmentation/imaging_plane/GliaOpticalChannel (OpticalChannel) 
  Group /processing/ophys/VolumeSegmentation/GliaVolumeSegmentation/imaging_plane/device (Device) Confocal imaging was done using LSM 710, LSM 880 upright, or LSM 800.
  Group /processing/ophys/VolumeSegmentation/GliaVolumeSegmentation/reference_images/GliaOnePhotonSeries (TwoPhotonSeries) Full resolution images from glia-specific optical channel of whole-brain calcium imaging.
  Group /processing/ophys/VolumeSegmentation/GliaVolumeSegmentation/reference_images/GliaOnePhotonSeries/imaging_plane (ImagingPlane) 
  Group /processing/ophys/VolumeSegmentation/GliaVolumeSegmentation/reference_images/GliaOnePhotonSeries/imaging_plane/GliaOpticalChannel (OpticalChannel) 
  Group /processing/ophys/VolumeSegmentation/GliaVolumeSegmentation/reference_images/GliaOnePhotonSeries/imaging_plane/device (Device) Confocal imaging was done using LSM 710, LSM 880 upright, or LSM 800.
  Dataset /processing/ophys/VolumeSegmentation/GliaVolumeSegmentation/voxel_mask (VectorData) Voxel masks for each ROI | shape = (10686483,) | dtype = [('x', '<u4'), ('y', '<u4'), ('z', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/VolumeSegmentation/GliaVolumeSegmentation/voxel_mask_index (VectorIndex) Index for VectorData 'voxel_mask' | shape = (126467,) | dtype = uint32
  Group /processing/ophys/VolumeSegmentation/NeuronVolumeSegmentation (PlaneSegmentation) Segmented ROIs for the neurons.
  Dataset /processing/ophys/VolumeSegmentation/NeuronVolumeSegmentation/id (ElementIdentifiers)  | shape = (111378,) | dtype = int64
  Group /processing/ophys/VolumeSegmentation/NeuronVolumeSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys/VolumeSegmentation/NeuronVolumeSegmentation/imaging_plane/NeuronOpticalChannel (OpticalChannel) 
  Group /processing/ophys/VolumeSegmentation/NeuronVolumeSegmentation/imaging_plane/device (Device) Confocal imaging was done using LSM 710, LSM 880 upright, or LSM 800.
  Group /processing/ophys/VolumeSegmentation/NeuronVolumeSegmentation/reference_images/NeuronOnePhotonSeries (TwoPhotonSeries) Full resolution images from neuron-specific optical channel of whole-brain calcium imaging.
  Group /processing/ophys/VolumeSegmentation/NeuronVolumeSegmentation/reference_images/NeuronOnePhotonSeries/imaging_plane (ImagingPlane) 
  Group /processing/ophys/VolumeSegmentation/NeuronVolumeSegmentation/reference_images/NeuronOnePhotonSeries/imaging_plane/NeuronOpticalChannel (OpticalChannel) 
  Group /processing/ophys/VolumeSegmentation/NeuronVolumeSegmentation/reference_images/NeuronOnePhotonSeries/imaging_plane/device (Device) Confocal imaging was done using LSM 710, LSM 880 upright, or LSM 800.
  Dataset /processing/ophys/VolumeSegmentation/NeuronVolumeSegmentation/voxel_mask (VectorData) Voxel masks for each ROI | shape = (9427734,) | dtype = [('x', '<u4'), ('y', '<u4'), ('z', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/VolumeSegmentation/NeuronVolumeSegmentation/voxel_mask_index (VectorIndex) Index for VectorData 'voxel_mask' | shape = (111378,) | dtype = uint32
  session_description: A dual-color optic channel recording of both neuron and glia populations.
  session_start_time: 2017-02-28T16:57:30-05:00
  timestamps_reference_time: 2017-02-28T16:57:30-05:00
