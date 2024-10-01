
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001084/draft
name: Targeted micro-fiber arrays for measuring and manipulating localized multi-scale neural dynamics over large, deep brain volumes during behavior
contributor: [{'name': 'Vu, Mai-Anh T.', 'email': 'maianhvu@bu.edu', 'roleName': ['dcite:Author', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0003-4766-1159', 'affiliation': [], 'includeInCitation': True}, {'name': 'Brown, Eleanor H.', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Wen, Michelle J.', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Noggle, Christian A.', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Zhang, Zicheng', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Monk, Kevin J.', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Bouabid, Safa', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Mroz, Lydia', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Graham, Benjamin M.', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Zhuo, Yizhou', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Li, Yulong', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Otchy, Timothy M.', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Tian, Lin', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Davison, Ian G.', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Boas, David A.', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Howe, Mark W.', 'email': 'mwhowe@bu.edu', 'roleName': ['dcite:Author', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0002-6865-5084', 'affiliation': [], 'includeInCitation': True}, {'name': 'Michael J. Fox Foundation', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/03arq3225', 'awardNumber': 'ASAP-020370', 'includeInCitation': False}, {'name': 'National Institute of Mental Health', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/04xeg9z08', 'awardNumber': 'R01 MH125835', 'includeInCitation': False}, {'name': 'Parkinson’s Foundation', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/05mx85j86', 'awardNumber': 'PF-SF-JFA-836662', 'includeInCitation': False}, {'name': 'National Institute of Mental Health', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/04xeg9z08', 'awardNumber': 'F32MH120894', 'includeInCitation': False}, {'name': 'National Institute of Mental Health', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/04xeg9z08', 'awardNumber': '1F31NS127536', 'includeInCitation': False}, {'name': 'National Institute on Deafness and Other Communication Disorders', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/04mhx6838', 'awardNumber': ' F32DC020665', 'includeInCitation': False}, {'name': 'National Institute of Neurological Disorders and Stroke\u200b', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01s5ya894', 'awardNumber': ' RF1NS128975', 'includeInCitation': False}]
description: Neural population dynamics relevant to behavior vary over multiple spatial and temporal scales across three-dimensional volumes. Current optical approaches lack the spatial coverage and resolution necessary to measure and manipulate naturally occurring patterns of large-scale, distributed dynamics within and across deep brain regions such as the striatum. We designed a new micro-fiber array approach capable of chronically measuring and optogenetically manipulating local dynamics across over 100 targeted locations simultaneously in head-fixed and freely moving mice, enabling the investigation of cell-type- and neurotransmitter-specific signals over arbitrary 3D volumes at a spatial resolution and coverage previously inaccessible. We applied this method to resolve rapid dopamine release dynamics across the striatum, revealing distinct, modality-specific spatiotemporal patterns in response to salient sensory stimuli extending over millimeters of tissue.
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 823109975937, 'numberOfFiles': 179, 'numberOfSubjects': 16, 'variableMeasured': ['OpticalChannel', 'ImagingPlane', 'PlaneSegmentation', 'ProcessingModule'], 'measurementTechnique': [{'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 001084 has 50 NWB files.
2 of these NWB files are of type 1.
11 of these NWB files are of type 2.
35 of these NWB files are of type 3.
1 of these NWB files are of type 4.
1 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/FiberPhotometryResponseSeriesGreen (FiberPhotometryResponseSeries) Raw fluorescence traces acquired with multi-fiber array implanted in the striatum.
  Dataset /acquisition/FiberPhotometryResponseSeriesGreen/fiber_photometry_table_region (DynamicTableRegion) source fibers | shape = (82,) | dtype = int64
  Group /acquisition/FiberPhotometryResponseSeriesGreenIsosbestic (FiberPhotometryResponseSeries) Raw fluorescence traces acquired with multi-fiber array implanted in the striatum.
  Dataset /acquisition/FiberPhotometryResponseSeriesGreenIsosbestic/fiber_photometry_table_region (DynamicTableRegion) source fibers | shape = (82,) | dtype = int64
  Group /acquisition/OnePhotonSeriesGreen (OnePhotonSeries) Fiber bundle imaging acquired using HCImage Live (Hamamatsu). For dual-wavelength excitation and emission, two LEDs were triggered by 5V digital TTL pulses which alternated at either 11Hz (30ms exposure) or 18Hz (20ms exposure).
  Group /acquisition/OnePhotonSeriesGreen/imaging_plane (ImagingPlane) 
  Group /acquisition/OnePhotonSeriesGreen/imaging_plane/Green (OpticalChannel) 
  Group /acquisition/OnePhotonSeriesGreen/imaging_plane/device (Device) The microscope (Hamamatsu Orca Fusion BT Gen III) used to acquire the image of the fiber bundle.
  Group /acquisition/OnePhotonSeriesGreenIsosbestic (OnePhotonSeries) Fiber bundle imaging acquired using HCImage Live (Hamamatsu). For dual-wavelength excitation and emission, two LEDs were triggered by 5V digital TTL pulses which alternated at either 11Hz (30ms exposure) or 18Hz (20ms exposure).
  Group /acquisition/OnePhotonSeriesGreenIsosbestic/imaging_plane (ImagingPlane) 
  Group /acquisition/OnePhotonSeriesGreenIsosbestic/imaging_plane/Green (OpticalChannel) 
  Group /acquisition/OnePhotonSeriesGreenIsosbestic/imaging_plane/device (Device) The microscope (Hamamatsu Orca Fusion BT Gen III) used to acquire the image of the fiber bundle.
  file_create_date: ['2024-08-08T16:10:21.372751+02:00']
  Group /general/FiberPhotometry (FiberPhotometry) 
  Group /general/FiberPhotometry/FiberPhotometryTable (FiberPhotometryTable) Contains the metadata for the fiber photometry experiment.
  Dataset /general/FiberPhotometry/FiberPhotometryTable/allen_atlas_coordinates (VectorData) The fiber tip coordinates (AP, ML, DV) in Allen Brain Atlas coordinates | shape = (164, 3) | dtype = int64
  Dataset /general/FiberPhotometry/FiberPhotometryTable/coordinates (VectorData) Fiber placement in stereotactic coordinates (AP, ML, DV) mm relative to Bregma. | shape = (164, 3) | dtype = float64
  Dataset /general/FiberPhotometry/FiberPhotometryTable/dichroic_mirror (VectorData) Link to the dichroic mirror device. | shape = (164,) | dtype = object
  Dataset /general/FiberPhotometry/FiberPhotometryTable/emission_filter (VectorData) Link to the emission filter device. | shape = (164,) | dtype = object
  Dataset /general/FiberPhotometry/FiberPhotometryTable/excitation_filter (VectorData) Link to the excitation filter device. | shape = (164,) | dtype = object
  Dataset /general/FiberPhotometry/FiberPhotometryTable/excitation_source (VectorData) Link to the excitation source device. | shape = (164,) | dtype = object
  Dataset /general/FiberPhotometry/FiberPhotometryTable/id (ElementIdentifiers)  | shape = (164,) | dtype = int64
  Dataset /general/FiberPhotometry/FiberPhotometryTable/included (VectorData) Whether this fiber has been successfully implanted. | shape = (164,) | dtype = bool
  Dataset /general/FiberPhotometry/FiberPhotometryTable/indicator (VectorData) Link to the indicator object. | shape = (164,) | dtype = object
  Dataset /general/FiberPhotometry/FiberPhotometryTable/location (VectorData) Location of fiber. | shape = (164,) | dtype = object
  Dataset /general/FiberPhotometry/FiberPhotometryTable/optical_fiber (VectorData) Link to the optical fiber device. | shape = (164,) | dtype = object
  Dataset /general/FiberPhotometry/FiberPhotometryTable/photodetector (VectorData) Link to the photodetector device. | shape = (164,) | dtype = object
  Group /general/devices/CMOSCamera (Device) A tube lens in each path (Thor labs, No TTL165-A) focused emission light onto the CMOS sensors of the cameras to form an image of the fiber bundle.
  Group /general/devices/CollimatingBeamProbe (Device) Light from the LEDs is filtered, coupled into a liquid light guide with lenses and the collimating beam probe.
  Group /general/devices/DichroicMirror1 (DichroicMirror) The dichroic mirror used to reflect green and pass red fluorescence
  Group /general/devices/ExcitationSource405 (ExcitationSource) Violet LED (405 nm, Thorlabs, No. SOLIS-405C) for the isosbestic control.
  Group /general/devices/ExcitationSource470 (ExcitationSource) Blue excitation light (470 nm LED, Thorlabs, No. SOLIS-470C) and violet excitation light (for the isosbestic control)
  were coupled into the optic fiber such that a power of 0.75 mW was delivered to the fiber tip.
  Then, 470 nm and 405 nm excitation were alternated at 100 Hz using a waveform generator,
  each filtered with a corresponding filter.
  
  Group /general/devices/FiberArray (OpticalFiber) The optical fiber used in a multi-fiber arrays configuration, fabricated in-house to enable large scale measurements across deep brain volumes. Bare fibers were cut into pieces (ca. 3cm) then mounted under a microscope into 55-60μm diameter holes in a custom 3D printed grid (3mm W x 5mm L, Boston Micro Fabrication), measured under a dissection microscope to target a particular depth beneath the grid, and secured in place with UV glue (Norland Optical Adhesive 61). Each array contained between 30 and 103 fibers separated by a minimum of 220μm radially and 250μm axially. Separation was calculated to achieve maximal coverage of the striatum volume with no overlap in the collection fields of individual fibers. Fibers were cut with a fiber scribe, and the distal ends were inspected to ensure a uniform cut, and re-cut as necessary. Distal ends were then glued inside an 1cm ca. section of polyimide tube (0.8-1.3mm diameter, MicroLumen) then cut with a fresh razorblade. The bundled fibers inside the tube were then polished on fine grained polishing paper (ThorLabs,polished first with 6 μm, followed by 3 μm) to create a smooth, uniform fiber bundle surface for imaging. A larger diameter post was mounted on one side of the plastic grid to facilitate holding during implantation.
  Group /general/devices/GCaMP7f (Indicator) Green calcium sensor
  Group /general/devices/HamamatsuMicroscope (Device) The microscope (Hamamatsu Orca Fusion BT Gen III) used to acquire the image of the fiber bundle.
  Group /general/devices/Lens1 (Device) Lens focus at 60 mm.
  Group /general/devices/Lens2 (Device) Lens focus at 30 mm.
  Group /general/devices/LiquidLightGuide (Device) The liquid light guide is coupled into a filter cube on the microscope and excitation light is reflected into the back aperture of the microscope objective by a dichroic beam-splitter.
  Group /general/devices/MicroManipulator (Device) The microscope was attached to a micromanipulator to allow fine manual focusing and mounted on a rotatable arm extending over the head-fixation setup to allow for coarse positioning of the objective over the mouse.
  Group /general/devices/MicroscopeObjective (Device) Magnification 10x, Numerical Aperture 0.3.
  Group /general/devices/OpticalFilter405 (BandOpticalFilter) The band-pass filter used to isolate the 405 and 415 nm excitation light.
  Group /general/devices/OpticalFilter470 (BandOpticalFilter) The band-pass filter used to isolate the 470 nm excitation light.
  Group /general/devices/OpticalFilter525 (BandOpticalFilter) The band-pass filter used to isolate the green emitted light after passing through a dichroic (Chroma, No. 532rdc) that reflected green and passed red fluorescence.
  Group /general/devices/TubeLens (Device) A tube lens in each path focuses emission light onto the CMOS sensors of the cameras to form an image of the fiber bundle.
  experiment_description: Neural population dynamics relevant to behavior vary over multiple spatial and temporal scales across
  three-dimensional volumes. Current optical approaches lack the spatial coverage and resolution necessary to measure
  and manipulate naturally occurring patterns of large-scale, distributed dynamics within and across deep brain
  regions such as the striatum. We designed a new micro-fiber array approach capable of chronically measuring and
  optogenetically manipulating local dynamics across over 100 targeted locations simultaneously in head-fixed and
  freely moving mice, enabling the investigation of cell-type- and neurotransmitter-specific signals over arbitrary
  3D volumes at a spatial resolution and coverage previously inaccessible. We applied this method to resolve rapid
  dopamine release dynamics across the striatum, revealing distinct, modality-specific spatiotemporal patterns in
  response to salient sensory stimuli extending over millimeters of tissue. Targeted optogenetics enabled flexible
  control of neural signaling on multiple spatial scales, better matching endogenous signaling patterns, and the
  spatial localization of behavioral function across large circuits.
  
  experimenter: ['Vu, Mai-Anh']
  institution: Boston University
  keywords: ['multi-fiber photometry' 'behaving mice' 'freely moving mice' 'striatum'
   'dopamine']
  lab: Howe
  Group /general/optophysiology/ImagingPlaneGreen (ImagingPlane) 
  Group /general/optophysiology/ImagingPlaneGreen/Green (OpticalChannel) 
  Group /general/optophysiology/ImagingPlaneGreen/device (Device) The microscope (Hamamatsu Orca Fusion BT Gen III) used to acquire the image of the fiber bundle.
  Group /general/optophysiology/ImagingPlaneGreenIsosbestic (ImagingPlane) 
  Group /general/optophysiology/ImagingPlaneGreenIsosbestic/Green (OpticalChannel) 
  Group /general/optophysiology/ImagingPlaneGreenIsosbestic/device (Device) The microscope (Hamamatsu Orca Fusion BT Gen III) used to acquire the image of the fiber bundle.
  pharmacology: Mice were anesthetized under isoflurane (1-3%) and placed in a stereotaxic frame.
  A large craniotomy was performed with a surgical drill (Midwest Tradition 790044, Avtec Dental RMWT) to expose the
  cortical surface above the striatum. Mice were injected with AAVs to express genetically encoded proteins for
  optical measurements and manipulations. Virus (~200-800nL per site) was injected stereotaxically through a
  pulled glass pipette (diameter 30-50µm) at a rate of ~100nL/min. For striatum expression, virus was injected at
  10-40 total locations chosen to maximize overlap with fiber positions. For midbrain targeting, for one set of mice,
  we injected the 4 sites relative to bregma: AP = -3.05, ML = 0.6, DV = -4.6 and DV = -4.25; AP = -3.5, ML = 1.25,
  DV = -3.9 and DV = -4.5. For a midbrain targeting in another set of mice, we injected at 3.07mm caudal to the bregma
  at 4 sites: ML = 0.5mm, DV =-4.00 mm and -4.25 mm, ML = 1mm, DV = -4.125mm and ML = 1.5 mm, DV = -3.8 mm below the dura.
  
  protocol: https://doi.org/10.17504/protocols.io.bp2l6xyrklqe/v1
  related_publications: ['https://doi.org/10.1016/j.neuron.2023.12.011']
  session_id: 221118
  source_script: Created using NeuroConv v0.5.0
  Group /general/subject (Subject) 
  identifier: b84a5b00-41c4-434b-b6bd-337e3e6b3870
  Group /processing/behavior (ProcessingModule) Contains the velocity signals from two optical mouse sensors (Logitech G203 mice with hard plastic shells removed).
  Group /processing/behavior/AngularVelocity (TimeSeries) The angular velocity from yaw (rotational) velocity converted to radians/s.
  Group /processing/behavior/TimeIntervals (TimeIntervals) Mice were presented with either visual (blue LED) or auditory (12 kHz tone) stimuli at random intervals (4–40 s). For experiments with water reward delivery, a water spout mounted on a post delivered water rewards (9 μL, Figure 1B) at random time intervals (randomly drawn from a 5-30s uniform distribution) through a water spout and solenoid valve gated electronically. Licking was monitored by a capacitive touch circuit connected to the spout.
  Dataset /processing/behavior/TimeIntervals/event_type (VectorData) The type of event (licking, light, tone or reward delivery). | shape = (2251,) | dtype = object
  Dataset /processing/behavior/TimeIntervals/id (ElementIdentifiers)  | shape = (2251,) | dtype = int64
  Dataset /processing/behavior/TimeIntervals/start_time (VectorData) Start time of epoch, in seconds | shape = (2251,) | dtype = float64
  Dataset /processing/behavior/TimeIntervals/stop_time (VectorData) Stop time of epoch, in seconds | shape = (2251,) | dtype = float64
  Group /processing/behavior/Velocity (TimeSeries) Velocity for the roll and pitch (x, y) measured in m/s.
  Group /processing/ophys (ProcessingModule) Constains the processed imaging and fiber photometry data.
  Group /processing/ophys/BaselineFiberPhotometryResponseSeriesGreen (FiberPhotometryResponseSeries) Baseline fluorescence traces acquired with multi-fiber array implanted in the striatum.
  Dataset /processing/ophys/BaselineFiberPhotometryResponseSeriesGreen/fiber_photometry_table_region (DynamicTableRegion) source fibers | shape = (82,) | dtype = int64
  Group /processing/ophys/BaselineFiberPhotometryResponseSeriesGreenIsosbestic (FiberPhotometryResponseSeries) Baseline fluorescence traces acquired with multi-fiber array implanted in the striatum.
  Dataset /processing/ophys/BaselineFiberPhotometryResponseSeriesGreenIsosbestic/fiber_photometry_table_region (DynamicTableRegion) source fibers | shape = (82,) | dtype = int64
  Group /processing/ophys/DfOverFFiberPhotometryResponseSeriesGreen (FiberPhotometryResponseSeries) Baseline corrected (DF/F) fluorescence traces acquired with multi-fiber array implanted in the striatum.
  Dataset /processing/ophys/DfOverFFiberPhotometryResponseSeriesGreen/fiber_photometry_table_region (DynamicTableRegion) source fibers | shape = (82,) | dtype = int64
  Group /processing/ophys/DfOverFFiberPhotometryResponseSeriesGreenIsosbestic (FiberPhotometryResponseSeries) Baseline corrected (DF/F) fluorescence traces acquired with multi-fiber array implanted in the striatum.
  Dataset /processing/ophys/DfOverFFiberPhotometryResponseSeriesGreenIsosbestic/fiber_photometry_table_region (DynamicTableRegion) source fibers | shape = (82,) | dtype = int64
  Group /processing/ophys/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation (PlaneSegmentation) Segmented ROIs
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/Accepted (VectorData) 1 if ROI was accepted or 0 if rejected as a cell during segmentation operation. | shape = (82,) | dtype = int64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/ROICentroids (VectorData) The x, y, (z) centroids of each ROI. | shape = (82, 2) | dtype = float64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/Rejected (VectorData) 1 if ROI was rejected or 0 if accepted as a cell during segmentation operation. | shape = (82,) | dtype = int64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/id (ElementIdentifiers)  | shape = (82,) | dtype = int64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/image_mask (VectorData) Image masks for each ROI. | shape = (82, 353, 353) | dtype = float64
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/Green (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/device (Device) The microscope (Hamamatsu Orca Fusion BT Gen III) used to acquire the image of the fiber bundle.
  session_description: This dataset contains fiber photometry recordings from multi-fiber arrays implanted in the striatum in mice running
  on a treadmill while receiving either visual (blue LED) or auditory (12 kHz tone) stimuli at random intervals (4–40 s).
  Some sessions may include water reward delivery, where a water spout mounted on a post delivered water rewards (9 μL) at random time intervals (randomly drawn from a 5-30s uniform distribution) through a water spout and solenoid valve gated electronically.
  Licking was monitored by a capacitive touch circuit connected to the spout.
  
  session_start_time: 2022-11-18T16:10:03-05:00
  timestamps_reference_time: 2022-11-18T16:10:03-05:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/FiberPhotometryResponseSeriesGreen (FiberPhotometryResponseSeries) Raw fluorescence traces acquired with multi-fiber array implanted in the striatum.
  Dataset /acquisition/FiberPhotometryResponseSeriesGreen/fiber_photometry_table_region (DynamicTableRegion) source fibers | shape = (64,) | dtype = int64
  Group /acquisition/OnePhotonSeriesGreen (OnePhotonSeries) Fiber bundle imaging acquired using HCImage Live (Hamamatsu). Single wavelength excitation and emission was performed with continuous, internally triggered imaging at 30Hz.
  Group /acquisition/OnePhotonSeriesGreen/imaging_plane (ImagingPlane) 
  Group /acquisition/OnePhotonSeriesGreen/imaging_plane/Green (OpticalChannel) 
  Group /acquisition/OnePhotonSeriesGreen/imaging_plane/device (Device) The microscope (Hamamatsu Orca Fusion BT Gen III) used to acquire the image of the fiber bundle.
  file_create_date: ['2024-08-07T15:02:24.368319+02:00']
  Group /general/FiberPhotometry (FiberPhotometry) 
  Group /general/FiberPhotometry/FiberPhotometryTable (FiberPhotometryTable) Contains the metadata for the fiber photometry experiment.
  Dataset /general/FiberPhotometry/FiberPhotometryTable/allen_atlas_coordinates (VectorData) The fiber tip coordinates (AP, ML, DV) in Allen Brain Atlas coordinates | shape = (64, 3) | dtype = int64
  Dataset /general/FiberPhotometry/FiberPhotometryTable/coordinates (VectorData) Fiber placement in stereotactic coordinates (AP, ML, DV) mm relative to Bregma. | shape = (64, 3) | dtype = float64
  Dataset /general/FiberPhotometry/FiberPhotometryTable/dichroic_mirror (VectorData) Link to the dichroic mirror device. | shape = (64,) | dtype = object
  Dataset /general/FiberPhotometry/FiberPhotometryTable/emission_filter (VectorData) Link to the emission filter device. | shape = (64,) | dtype = object
  Dataset /general/FiberPhotometry/FiberPhotometryTable/excitation_filter (VectorData) Link to the excitation filter device. | shape = (64,) | dtype = object
  Dataset /general/FiberPhotometry/FiberPhotometryTable/excitation_source (VectorData) Link to the excitation source device. | shape = (64,) | dtype = object
  Dataset /general/FiberPhotometry/FiberPhotometryTable/id (ElementIdentifiers)  | shape = (64,) | dtype = int64
  Dataset /general/FiberPhotometry/FiberPhotometryTable/included (VectorData) Whether this fiber has been successfully implanted. | shape = (64,) | dtype = bool
  Dataset /general/FiberPhotometry/FiberPhotometryTable/indicator (VectorData) Link to the indicator object. | shape = (64,) | dtype = object
  Dataset /general/FiberPhotometry/FiberPhotometryTable/location (VectorData) Location of fiber. | shape = (64,) | dtype = object
  Dataset /general/FiberPhotometry/FiberPhotometryTable/optical_fiber (VectorData) Link to the optical fiber device. | shape = (64,) | dtype = object
  Dataset /general/FiberPhotometry/FiberPhotometryTable/photodetector (VectorData) Link to the photodetector device. | shape = (64,) | dtype = object
  Group /general/devices/CMOSCamera (Device) A tube lens in each path (Thor labs, No TTL165-A) focused emission light onto the CMOS sensors of the cameras to form an image of the fiber bundle.
  Group /general/devices/CollimatingBeamProbe (Device) Light from the LEDs is filtered, coupled into a liquid light guide with lenses and the collimating beam probe.
  Group /general/devices/DichroicMirror1 (DichroicMirror) The dichroic mirror used to reflect green and pass red fluorescence
  Group /general/devices/ExcitationSource470 (ExcitationSource) Blue excitation light (470 nm LED, Thorlabs, No. SOLIS-470C) and violet excitation light (for the isosbestic control)
  were coupled into the optic fiber such that a power of 0.75 mW was delivered to the fiber tip.
  Then, 470 nm and 405 nm excitation were alternated at 100 Hz using a waveform generator,
  each filtered with a corresponding filter.
  
  Group /general/devices/FiberArray (OpticalFiber) The optical fiber used in a multi-fiber arrays configuration, fabricated in-house to enable large scale measurements across deep brain volumes. Bare fibers were cut into pieces (ca. 3cm) then mounted under a microscope into 55-60μm diameter holes in a custom 3D printed grid (3mm W x 5mm L, Boston Micro Fabrication), measured under a dissection microscope to target a particular depth beneath the grid, and secured in place with UV glue (Norland Optical Adhesive 61). Each array contained between 30 and 103 fibers separated by a minimum of 220μm radially and 250μm axially. Separation was calculated to achieve maximal coverage of the striatum volume with no overlap in the collection fields of individual fibers. Fibers were cut with a fiber scribe, and the distal ends were inspected to ensure a uniform cut, and re-cut as necessary. Distal ends were then glued inside an 1cm ca. section of polyimide tube (0.8-1.3mm diameter, MicroLumen) then cut with a fresh razorblade. The bundled fibers inside the tube were then polished on fine grained polishing paper (ThorLabs,polished first with 6 μm, followed by 3 μm) to create a smooth, uniform fiber bundle surface for imaging. A larger diameter post was mounted on one side of the plastic grid to facilitate holding during implantation.
  Group /general/devices/HamamatsuMicroscope (Device) The microscope (Hamamatsu Orca Fusion BT Gen III) used to acquire the image of the fiber bundle.
  Group /general/devices/Lens1 (Device) Lens focus at 60 mm.
  Group /general/devices/Lens2 (Device) Lens focus at 30 mm.
  Group /general/devices/LiquidLightGuide (Device) The liquid light guide is coupled into a filter cube on the microscope and excitation light is reflected into the back aperture of the microscope objective by a dichroic beam-splitter.
  Group /general/devices/MicroManipulator (Device) The microscope was attached to a micromanipulator to allow fine manual focusing and mounted on a rotatable arm extending over the head-fixation setup to allow for coarse positioning of the objective over the mouse.
  Group /general/devices/MicroscopeObjective (Device) Magnification 10x, Numerical Aperture 0.3.
  Group /general/devices/OpticalFilter470 (BandOpticalFilter) The band-pass filter used to isolate the 470 nm excitation light.
  Group /general/devices/OpticalFilter525 (BandOpticalFilter) The band-pass filter used to isolate the green emitted light after passing through a dichroic (Chroma, No. 532rdc) that reflected green and passed red fluorescence.
  Group /general/devices/TubeLens (Device) A tube lens in each path focuses emission light onto the CMOS sensors of the cameras to form an image of the fiber bundle.
  Group /general/devices/dLight1.3b (Indicator) green dopamine sensor
  experiment_description: Neural population dynamics relevant to behavior vary over multiple spatial and temporal scales across
  three-dimensional volumes. Current optical approaches lack the spatial coverage and resolution necessary to measure
  and manipulate naturally occurring patterns of large-scale, distributed dynamics within and across deep brain
  regions such as the striatum. We designed a new micro-fiber array approach capable of chronically measuring and
  optogenetically manipulating local dynamics across over 100 targeted locations simultaneously in head-fixed and
  freely moving mice, enabling the investigation of cell-type- and neurotransmitter-specific signals over arbitrary
  3D volumes at a spatial resolution and coverage previously inaccessible. We applied this method to resolve rapid
  dopamine release dynamics across the striatum, revealing distinct, modality-specific spatiotemporal patterns in
  response to salient sensory stimuli extending over millimeters of tissue. Targeted optogenetics enabled flexible
  control of neural signaling on multiple spatial scales, better matching endogenous signaling patterns, and the
  spatial localization of behavioral function across large circuits.
  
  experimenter: ['Vu, Mai-Anh']
  institution: Boston University
  keywords: ['multi-fiber photometry' 'behaving mice' 'freely moving mice' 'striatum'
   'dopamine']
  lab: Howe
  Group /general/optophysiology/ImagingPlaneGreen (ImagingPlane) 
  Group /general/optophysiology/ImagingPlaneGreen/Green (OpticalChannel) 
  Group /general/optophysiology/ImagingPlaneGreen/device (Device) The microscope (Hamamatsu Orca Fusion BT Gen III) used to acquire the image of the fiber bundle.
  pharmacology: Mice were anesthetized under isoflurane (1-3%) and placed in a stereotaxic frame.
  A large craniotomy was performed with a surgical drill (Midwest Tradition 790044, Avtec Dental RMWT) to expose the
  cortical surface above the striatum. Mice were injected with AAVs to express genetically encoded proteins for
  optical measurements and manipulations. Virus (~200-800nL per site) was injected stereotaxically through a
  pulled glass pipette (diameter 30-50µm) at a rate of ~100nL/min. For striatum expression, virus was injected at
  10-40 total locations chosen to maximize overlap with fiber positions. For midbrain targeting, for one set of mice,
  we injected the 4 sites relative to bregma: AP = -3.05, ML = 0.6, DV = -4.6 and DV = -4.25; AP = -3.5, ML = 1.25,
  DV = -3.9 and DV = -4.5. For a midbrain targeting in another set of mice, we injected at 3.07mm caudal to the bregma
  at 4 sites: ML = 0.5mm, DV =-4.00 mm and -4.25 mm, ML = 1mm, DV = -4.125mm and ML = 1.5 mm, DV = -3.8 mm below the dura.
  
  protocol: https://doi.org/10.17504/protocols.io.bp2l6xyrklqe/v1
  related_publications: ['https://doi.org/10.1016/j.neuron.2023.12.011']
  session_id: 210819
  source_script: Created using NeuroConv v0.5.0
  Group /general/subject (Subject) 
  identifier: 367d89ad-435d-43d6-85f9-4ce97dd0fcf8
  Group /processing/behavior (ProcessingModule) Contains the velocity signals from two optical mouse sensors (Logitech G203 mice with hard plastic shells removed).
  Group /processing/behavior/AngularVelocity (TimeSeries) The angular velocity from yaw (rotational) velocity converted to radians/s.
  Group /processing/behavior/TimeIntervals (TimeIntervals) Mice were presented with either visual (blue LED) or auditory (12 kHz tone) stimuli at random intervals (4–40 s). For experiments with water reward delivery, a water spout mounted on a post delivered water rewards (9 μL, Figure 1B) at random time intervals (randomly drawn from a 5-30s uniform distribution) through a water spout and solenoid valve gated electronically. Licking was monitored by a capacitive touch circuit connected to the spout.
  Dataset /processing/behavior/TimeIntervals/event_type (VectorData) The type of event (licking, light, tone or reward delivery). | shape = (648,) | dtype = object
  Dataset /processing/behavior/TimeIntervals/id (ElementIdentifiers)  | shape = (648,) | dtype = int64
  Dataset /processing/behavior/TimeIntervals/start_time (VectorData) Start time of epoch, in seconds | shape = (648,) | dtype = float64
  Dataset /processing/behavior/TimeIntervals/stop_time (VectorData) Stop time of epoch, in seconds | shape = (648,) | dtype = float64
  Group /processing/behavior/Velocity (TimeSeries) Velocity for the roll and pitch (x, y) measured in m/s.
  Group /processing/ophys (ProcessingModule) Constains the processed imaging and fiber photometry data.
  Group /processing/ophys/BaselineFiberPhotometryResponseSeriesGreen (FiberPhotometryResponseSeries) Baseline fluorescence traces acquired with multi-fiber array implanted in the striatum.
  Dataset /processing/ophys/BaselineFiberPhotometryResponseSeriesGreen/fiber_photometry_table_region (DynamicTableRegion) source fibers | shape = (64,) | dtype = int64
  Group /processing/ophys/DfOverFFiberPhotometryResponseSeriesGreen (FiberPhotometryResponseSeries) Baseline corrected (DF/F) fluorescence traces acquired with multi-fiber array implanted in the striatum.
  Dataset /processing/ophys/DfOverFFiberPhotometryResponseSeriesGreen/fiber_photometry_table_region (DynamicTableRegion) source fibers | shape = (64,) | dtype = int64
  Group /processing/ophys/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation (PlaneSegmentation) Segmented ROIs
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/Accepted (VectorData) 1 if ROI was accepted or 0 if rejected as a cell during segmentation operation. | shape = (64,) | dtype = int64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/ROICentroids (VectorData) The x, y, (z) centroids of each ROI. | shape = (64, 2) | dtype = float64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/Rejected (VectorData) 1 if ROI was rejected or 0 if accepted as a cell during segmentation operation. | shape = (64,) | dtype = int64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/id (ElementIdentifiers)  | shape = (64,) | dtype = int64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/image_mask (VectorData) Image masks for each ROI. | shape = (64, 355, 354) | dtype = uint8
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/Green (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/device (Device) The microscope (Hamamatsu Orca Fusion BT Gen III) used to acquire the image of the fiber bundle.
  session_description: This dataset contains fiber photometry recordings from multi-fiber arrays implanted in the striatum in mice running
  on a treadmill while receiving either visual (blue LED) or auditory (12 kHz tone) stimuli at random intervals (4–40 s).
  Some sessions may include water reward delivery, where a water spout mounted on a post delivered water rewards (9 μL) at random time intervals (randomly drawn from a 5-30s uniform distribution) through a water spout and solenoid valve gated electronically.
  Licking was monitored by a capacitive touch circuit connected to the spout.
  
  session_start_time: 2021-08-19T11:44:21-04:00
  timestamps_reference_time: 2021-08-19T11:44:21-04:00


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/FiberPhotometryResponseSeriesGreen (FiberPhotometryResponseSeries) Raw fluorescence traces acquired with multi-fiber array implanted in the striatum.
  Dataset /acquisition/FiberPhotometryResponseSeriesGreen/fiber_photometry_table_region (DynamicTableRegion) source fibers | shape = (64,) | dtype = int64
  Group /acquisition/OnePhotonSeriesGreen (OnePhotonSeries) Fiber bundle imaging acquired using HCImage Live (Hamamatsu). Single wavelength excitation and emission was performed with continuous, internally triggered imaging at 30Hz.
  Group /acquisition/OnePhotonSeriesGreen/imaging_plane (ImagingPlane) 
  Group /acquisition/OnePhotonSeriesGreen/imaging_plane/Green (OpticalChannel) 
  Group /acquisition/OnePhotonSeriesGreen/imaging_plane/device (Device) The microscope (Hamamatsu Orca Fusion BT Gen III) used to acquire the image of the fiber bundle.
  file_create_date: ['2024-08-07T15:28:48.206523+02:00']
  Group /general/FiberPhotometry (FiberPhotometry) 
  Group /general/FiberPhotometry/FiberPhotometryTable (FiberPhotometryTable) Contains the metadata for the fiber photometry experiment.
  Dataset /general/FiberPhotometry/FiberPhotometryTable/allen_atlas_coordinates (VectorData) The fiber tip coordinates (AP, ML, DV) in Allen Brain Atlas coordinates | shape = (64, 3) | dtype = int64
  Dataset /general/FiberPhotometry/FiberPhotometryTable/coordinates (VectorData) Fiber placement in stereotactic coordinates (AP, ML, DV) mm relative to Bregma. | shape = (64, 3) | dtype = float64
  Dataset /general/FiberPhotometry/FiberPhotometryTable/dichroic_mirror (VectorData) Link to the dichroic mirror device. | shape = (64,) | dtype = object
  Dataset /general/FiberPhotometry/FiberPhotometryTable/emission_filter (VectorData) Link to the emission filter device. | shape = (64,) | dtype = object
  Dataset /general/FiberPhotometry/FiberPhotometryTable/excitation_filter (VectorData) Link to the excitation filter device. | shape = (64,) | dtype = object
  Dataset /general/FiberPhotometry/FiberPhotometryTable/excitation_source (VectorData) Link to the excitation source device. | shape = (64,) | dtype = object
  Dataset /general/FiberPhotometry/FiberPhotometryTable/id (ElementIdentifiers)  | shape = (64,) | dtype = int64
  Dataset /general/FiberPhotometry/FiberPhotometryTable/included (VectorData) Whether this fiber has been successfully implanted. | shape = (64,) | dtype = bool
  Dataset /general/FiberPhotometry/FiberPhotometryTable/indicator (VectorData) Link to the indicator object. | shape = (64,) | dtype = object
  Dataset /general/FiberPhotometry/FiberPhotometryTable/location (VectorData) Location of fiber. | shape = (64,) | dtype = object
  Dataset /general/FiberPhotometry/FiberPhotometryTable/optical_fiber (VectorData) Link to the optical fiber device. | shape = (64,) | dtype = object
  Dataset /general/FiberPhotometry/FiberPhotometryTable/photodetector (VectorData) Link to the photodetector device. | shape = (64,) | dtype = object
  Group /general/devices/CMOSCamera (Device) A tube lens in each path (Thor labs, No TTL165-A) focused emission light onto the CMOS sensors of the cameras to form an image of the fiber bundle.
  Group /general/devices/CollimatingBeamProbe (Device) Light from the LEDs is filtered, coupled into a liquid light guide with lenses and the collimating beam probe.
  Group /general/devices/DichroicMirror1 (DichroicMirror) The dichroic mirror used to reflect green and pass red fluorescence
  Group /general/devices/ExcitationSource470 (ExcitationSource) Blue excitation light (470 nm LED, Thorlabs, No. SOLIS-470C) and violet excitation light (for the isosbestic control)
  were coupled into the optic fiber such that a power of 0.75 mW was delivered to the fiber tip.
  Then, 470 nm and 405 nm excitation were alternated at 100 Hz using a waveform generator,
  each filtered with a corresponding filter.
  
  Group /general/devices/FiberArray (OpticalFiber) The optical fiber used in a multi-fiber arrays configuration, fabricated in-house to enable large scale measurements across deep brain volumes. Bare fibers were cut into pieces (ca. 3cm) then mounted under a microscope into 55-60μm diameter holes in a custom 3D printed grid (3mm W x 5mm L, Boston Micro Fabrication), measured under a dissection microscope to target a particular depth beneath the grid, and secured in place with UV glue (Norland Optical Adhesive 61). Each array contained between 30 and 103 fibers separated by a minimum of 220μm radially and 250μm axially. Separation was calculated to achieve maximal coverage of the striatum volume with no overlap in the collection fields of individual fibers. Fibers were cut with a fiber scribe, and the distal ends were inspected to ensure a uniform cut, and re-cut as necessary. Distal ends were then glued inside an 1cm ca. section of polyimide tube (0.8-1.3mm diameter, MicroLumen) then cut with a fresh razorblade. The bundled fibers inside the tube were then polished on fine grained polishing paper (ThorLabs,polished first with 6 μm, followed by 3 μm) to create a smooth, uniform fiber bundle surface for imaging. A larger diameter post was mounted on one side of the plastic grid to facilitate holding during implantation.
  Group /general/devices/HamamatsuMicroscope (Device) The microscope (Hamamatsu Orca Fusion BT Gen III) used to acquire the image of the fiber bundle.
  Group /general/devices/Lens1 (Device) Lens focus at 60 mm.
  Group /general/devices/Lens2 (Device) Lens focus at 30 mm.
  Group /general/devices/LiquidLightGuide (Device) The liquid light guide is coupled into a filter cube on the microscope and excitation light is reflected into the back aperture of the microscope objective by a dichroic beam-splitter.
  Group /general/devices/MicroManipulator (Device) The microscope was attached to a micromanipulator to allow fine manual focusing and mounted on a rotatable arm extending over the head-fixation setup to allow for coarse positioning of the objective over the mouse.
  Group /general/devices/MicroscopeObjective (Device) Magnification 10x, Numerical Aperture 0.3.
  Group /general/devices/OpticalFilter470 (BandOpticalFilter) The band-pass filter used to isolate the 470 nm excitation light.
  Group /general/devices/OpticalFilter525 (BandOpticalFilter) The band-pass filter used to isolate the green emitted light after passing through a dichroic (Chroma, No. 532rdc) that reflected green and passed red fluorescence.
  Group /general/devices/TubeLens (Device) A tube lens in each path focuses emission light onto the CMOS sensors of the cameras to form an image of the fiber bundle.
  Group /general/devices/dLight1.3b (Indicator) green dopamine sensor
  experiment_description: Neural population dynamics relevant to behavior vary over multiple spatial and temporal scales across
  three-dimensional volumes. Current optical approaches lack the spatial coverage and resolution necessary to measure
  and manipulate naturally occurring patterns of large-scale, distributed dynamics within and across deep brain
  regions such as the striatum. We designed a new micro-fiber array approach capable of chronically measuring and
  optogenetically manipulating local dynamics across over 100 targeted locations simultaneously in head-fixed and
  freely moving mice, enabling the investigation of cell-type- and neurotransmitter-specific signals over arbitrary
  3D volumes at a spatial resolution and coverage previously inaccessible. We applied this method to resolve rapid
  dopamine release dynamics across the striatum, revealing distinct, modality-specific spatiotemporal patterns in
  response to salient sensory stimuli extending over millimeters of tissue. Targeted optogenetics enabled flexible
  control of neural signaling on multiple spatial scales, better matching endogenous signaling patterns, and the
  spatial localization of behavioral function across large circuits.
  
  experimenter: ['Vu, Mai-Anh']
  institution: Boston University
  keywords: ['multi-fiber photometry' 'behaving mice' 'freely moving mice' 'striatum'
   'dopamine']
  lab: Howe
  Group /general/optophysiology/ImagingPlaneGreen (ImagingPlane) 
  Group /general/optophysiology/ImagingPlaneGreen/Green (OpticalChannel) 
  Group /general/optophysiology/ImagingPlaneGreen/device (Device) The microscope (Hamamatsu Orca Fusion BT Gen III) used to acquire the image of the fiber bundle.
  pharmacology: Mice were anesthetized under isoflurane (1-3%) and placed in a stereotaxic frame.
  A large craniotomy was performed with a surgical drill (Midwest Tradition 790044, Avtec Dental RMWT) to expose the
  cortical surface above the striatum. Mice were injected with AAVs to express genetically encoded proteins for
  optical measurements and manipulations. Virus (~200-800nL per site) was injected stereotaxically through a
  pulled glass pipette (diameter 30-50µm) at a rate of ~100nL/min. For striatum expression, virus was injected at
  10-40 total locations chosen to maximize overlap with fiber positions. For midbrain targeting, for one set of mice,
  we injected the 4 sites relative to bregma: AP = -3.05, ML = 0.6, DV = -4.6 and DV = -4.25; AP = -3.5, ML = 1.25,
  DV = -3.9 and DV = -4.5. For a midbrain targeting in another set of mice, we injected at 3.07mm caudal to the bregma
  at 4 sites: ML = 0.5mm, DV =-4.00 mm and -4.25 mm, ML = 1mm, DV = -4.125mm and ML = 1.5 mm, DV = -3.8 mm below the dura.
  
  protocol: https://doi.org/10.17504/protocols.io.bp2l6xyrklqe/v1
  related_publications: ['https://doi.org/10.1016/j.neuron.2023.12.011']
  session_id: 210903
  source_script: Created using NeuroConv v0.5.0
  Group /general/subject (Subject) 
  identifier: d3d79286-930f-41f1-a521-b16d0822063f
  Group /processing/behavior (ProcessingModule) Contains the velocity signals from two optical mouse sensors (Logitech G203 mice with hard plastic shells removed).
  Group /processing/behavior/AngularVelocity (TimeSeries) The angular velocity from yaw (rotational) velocity converted to radians/s.
  Group /processing/behavior/TimeIntervals (TimeIntervals) Mice were presented with either visual (blue LED) or auditory (12 kHz tone) stimuli at random intervals (4–40 s). For experiments with water reward delivery, a water spout mounted on a post delivered water rewards (9 μL, Figure 1B) at random time intervals (randomly drawn from a 5-30s uniform distribution) through a water spout and solenoid valve gated electronically. Licking was monitored by a capacitive touch circuit connected to the spout.
  Dataset /processing/behavior/TimeIntervals/event_type (VectorData) The type of event (licking, light, tone or reward delivery). | shape = (688,) | dtype = object
  Dataset /processing/behavior/TimeIntervals/id (ElementIdentifiers)  | shape = (688,) | dtype = int64
  Dataset /processing/behavior/TimeIntervals/start_time (VectorData) Start time of epoch, in seconds | shape = (688,) | dtype = float64
  Dataset /processing/behavior/TimeIntervals/stop_time (VectorData) Stop time of epoch, in seconds | shape = (688,) | dtype = float64
  Group /processing/behavior/Velocity (TimeSeries) Velocity for the roll and pitch (x, y) measured in m/s.
  Group /processing/ophys (ProcessingModule) Constains the processed imaging and fiber photometry data.
  Group /processing/ophys/BaselineFiberPhotometryResponseSeriesGreen (FiberPhotometryResponseSeries) Baseline fluorescence traces acquired with multi-fiber array implanted in the striatum.
  Dataset /processing/ophys/BaselineFiberPhotometryResponseSeriesGreen/fiber_photometry_table_region (DynamicTableRegion) source fibers | shape = (64,) | dtype = int64
  Group /processing/ophys/DfOverFFiberPhotometryResponseSeriesGreen (FiberPhotometryResponseSeries) Baseline corrected (DF/F) fluorescence traces acquired with multi-fiber array implanted in the striatum.
  Dataset /processing/ophys/DfOverFFiberPhotometryResponseSeriesGreen/fiber_photometry_table_region (DynamicTableRegion) source fibers | shape = (64,) | dtype = int64
  Group /processing/ophys/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation (PlaneSegmentation) Segmented ROIs
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/Accepted (VectorData) 1 if ROI was accepted or 0 if rejected as a cell during segmentation operation. | shape = (64,) | dtype = int64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/ROICentroids (VectorData) The x, y, (z) centroids of each ROI. | shape = (64, 2) | dtype = float64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/Rejected (VectorData) 1 if ROI was rejected or 0 if accepted as a cell during segmentation operation. | shape = (64,) | dtype = int64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/id (ElementIdentifiers)  | shape = (64,) | dtype = int64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/image_mask (VectorData) Image masks for each ROI. | shape = (64, 356, 354) | dtype = uint8
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/Green (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/device (Device) The microscope (Hamamatsu Orca Fusion BT Gen III) used to acquire the image of the fiber bundle.
  Group /processing/ophys/OnePhotonSeriesMotionCorrectedGreen (OnePhotonSeries) The motion corrected fiber bundle imaging data.
  Group /processing/ophys/OnePhotonSeriesMotionCorrectedGreen/imaging_plane (ImagingPlane) 
  Group /processing/ophys/OnePhotonSeriesMotionCorrectedGreen/imaging_plane/Green (OpticalChannel) 
  Group /processing/ophys/OnePhotonSeriesMotionCorrectedGreen/imaging_plane/device (Device) The microscope (Hamamatsu Orca Fusion BT Gen III) used to acquire the image of the fiber bundle.
  session_description: This dataset contains fiber photometry recordings from multi-fiber arrays implanted in the striatum in mice running
  on a treadmill while receiving either visual (blue LED) or auditory (12 kHz tone) stimuli at random intervals (4–40 s).
  Some sessions may include water reward delivery, where a water spout mounted on a post delivered water rewards (9 μL) at random time intervals (randomly drawn from a 5-30s uniform distribution) through a water spout and solenoid valve gated electronically.
  Licking was monitored by a capacitive touch circuit connected to the spout.
  
  session_start_time: 2021-09-03T09:20:07-04:00
  timestamps_reference_time: 2021-09-03T09:20:07-04:00


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/FiberPhotometryResponseSeriesGreen (FiberPhotometryResponseSeries) Raw fluorescence traces acquired with multi-fiber array implanted in the striatum.
  Dataset /acquisition/FiberPhotometryResponseSeriesGreen/fiber_photometry_table_region (DynamicTableRegion) source fibers | shape = (103,) | dtype = int64
  Group /acquisition/OnePhotonSeriesGreen (OnePhotonSeries) Fiber bundle imaging acquired using HCImage Live (Hamamatsu). Single wavelength excitation and emission was performed with continuous, internally triggered imaging at 30Hz.
  Group /acquisition/OnePhotonSeriesGreen/imaging_plane (ImagingPlane) 
  Group /acquisition/OnePhotonSeriesGreen/imaging_plane/Green (OpticalChannel) 
  Group /acquisition/OnePhotonSeriesGreen/imaging_plane/device (Device) The microscope (Hamamatsu Orca Fusion BT Gen III) used to acquire the image of the fiber bundle.
  Group /acquisition/Video: DL18-body-11102021161110-0000 (ImageSeries) Video recorded by camera.
  Group /acquisition/Video: DL18-lick-11102021161113-0000 (ImageSeries) Video recorded by camera.
  file_create_date: ['2024-08-07T12:49:57.171344+02:00']
  Group /general/FiberPhotometry (FiberPhotometry) 
  Group /general/FiberPhotometry/FiberPhotometryTable (FiberPhotometryTable) Contains the metadata for the fiber photometry experiment.
  Dataset /general/FiberPhotometry/FiberPhotometryTable/allen_atlas_coordinates (VectorData) The fiber tip coordinates (AP, ML, DV) in Allen Brain Atlas coordinates | shape = (103, 3) | dtype = int64
  Dataset /general/FiberPhotometry/FiberPhotometryTable/coordinates (VectorData) Fiber placement in stereotactic coordinates (AP, ML, DV) mm relative to Bregma. | shape = (103, 3) | dtype = float64
  Dataset /general/FiberPhotometry/FiberPhotometryTable/dichroic_mirror (VectorData) Link to the dichroic mirror device. | shape = (103,) | dtype = object
  Dataset /general/FiberPhotometry/FiberPhotometryTable/emission_filter (VectorData) Link to the emission filter device. | shape = (103,) | dtype = object
  Dataset /general/FiberPhotometry/FiberPhotometryTable/excitation_filter (VectorData) Link to the excitation filter device. | shape = (103,) | dtype = object
  Dataset /general/FiberPhotometry/FiberPhotometryTable/excitation_source (VectorData) Link to the excitation source device. | shape = (103,) | dtype = object
  Dataset /general/FiberPhotometry/FiberPhotometryTable/id (ElementIdentifiers)  | shape = (103,) | dtype = int64
  Dataset /general/FiberPhotometry/FiberPhotometryTable/included (VectorData) Whether this fiber has been successfully implanted. | shape = (103,) | dtype = bool
  Dataset /general/FiberPhotometry/FiberPhotometryTable/indicator (VectorData) Link to the indicator object. | shape = (103,) | dtype = object
  Dataset /general/FiberPhotometry/FiberPhotometryTable/location (VectorData) Location of fiber. | shape = (103,) | dtype = object
  Dataset /general/FiberPhotometry/FiberPhotometryTable/optical_fiber (VectorData) Link to the optical fiber device. | shape = (103,) | dtype = object
  Dataset /general/FiberPhotometry/FiberPhotometryTable/photodetector (VectorData) Link to the photodetector device. | shape = (103,) | dtype = object
  Group /general/devices/CMOSCamera (Device) A tube lens in each path (Thor labs, No TTL165-A) focused emission light onto the CMOS sensors of the cameras to form an image of the fiber bundle.
  Group /general/devices/CollimatingBeamProbe (Device) Light from the LEDs is filtered, coupled into a liquid light guide with lenses and the collimating beam probe.
  Group /general/devices/DichroicMirror1 (DichroicMirror) The dichroic mirror used to reflect green and pass red fluorescence
  Group /general/devices/ExcitationSource470 (ExcitationSource) Blue excitation light (470 nm LED, Thorlabs, No. SOLIS-470C) and violet excitation light (for the isosbestic control)
  were coupled into the optic fiber such that a power of 0.75 mW was delivered to the fiber tip.
  Then, 470 nm and 405 nm excitation were alternated at 100 Hz using a waveform generator,
  each filtered with a corresponding filter.
  
  Group /general/devices/FiberArray (OpticalFiber) The optical fiber used in a multi-fiber arrays configuration, fabricated in-house to enable large scale measurements across deep brain volumes. Bare fibers were cut into pieces (ca. 3cm) then mounted under a microscope into 55-60μm diameter holes in a custom 3D printed grid (3mm W x 5mm L, Boston Micro Fabrication), measured under a dissection microscope to target a particular depth beneath the grid, and secured in place with UV glue (Norland Optical Adhesive 61). Each array contained between 30 and 103 fibers separated by a minimum of 220μm radially and 250μm axially. Separation was calculated to achieve maximal coverage of the striatum volume with no overlap in the collection fields of individual fibers. Fibers were cut with a fiber scribe, and the distal ends were inspected to ensure a uniform cut, and re-cut as necessary. Distal ends were then glued inside an 1cm ca. section of polyimide tube (0.8-1.3mm diameter, MicroLumen) then cut with a fresh razorblade. The bundled fibers inside the tube were then polished on fine grained polishing paper (ThorLabs,polished first with 6 μm, followed by 3 μm) to create a smooth, uniform fiber bundle surface for imaging. A larger diameter post was mounted on one side of the plastic grid to facilitate holding during implantation.
  Group /general/devices/HamamatsuMicroscope (Device) The microscope (Hamamatsu Orca Fusion BT Gen III) used to acquire the image of the fiber bundle.
  Group /general/devices/Lens1 (Device) Lens focus at 60 mm.
  Group /general/devices/Lens2 (Device) Lens focus at 30 mm.
  Group /general/devices/LiquidLightGuide (Device) The liquid light guide is coupled into a filter cube on the microscope and excitation light is reflected into the back aperture of the microscope objective by a dichroic beam-splitter.
  Group /general/devices/MicroManipulator (Device) The microscope was attached to a micromanipulator to allow fine manual focusing and mounted on a rotatable arm extending over the head-fixation setup to allow for coarse positioning of the objective over the mouse.
  Group /general/devices/MicroscopeObjective (Device) Magnification 10x, Numerical Aperture 0.3.
  Group /general/devices/OpticalFilter470 (BandOpticalFilter) The band-pass filter used to isolate the 470 nm excitation light.
  Group /general/devices/OpticalFilter525 (BandOpticalFilter) The band-pass filter used to isolate the green emitted light after passing through a dichroic (Chroma, No. 532rdc) that reflected green and passed red fluorescence.
  Group /general/devices/TubeLens (Device) A tube lens in each path focuses emission light onto the CMOS sensors of the cameras to form an image of the fiber bundle.
  Group /general/devices/dLight1.3b (Indicator) green dopamine sensor
  experiment_description: Neural population dynamics relevant to behavior vary over multiple spatial and temporal scales across
  three-dimensional volumes. Current optical approaches lack the spatial coverage and resolution necessary to measure
  and manipulate naturally occurring patterns of large-scale, distributed dynamics within and across deep brain
  regions such as the striatum. We designed a new micro-fiber array approach capable of chronically measuring and
  optogenetically manipulating local dynamics across over 100 targeted locations simultaneously in head-fixed and
  freely moving mice, enabling the investigation of cell-type- and neurotransmitter-specific signals over arbitrary
  3D volumes at a spatial resolution and coverage previously inaccessible. We applied this method to resolve rapid
  dopamine release dynamics across the striatum, revealing distinct, modality-specific spatiotemporal patterns in
  response to salient sensory stimuli extending over millimeters of tissue. Targeted optogenetics enabled flexible
  control of neural signaling on multiple spatial scales, better matching endogenous signaling patterns, and the
  spatial localization of behavioral function across large circuits.
  
  experimenter: ['Vu, Mai-Anh']
  institution: Boston University
  keywords: ['multi-fiber photometry' 'behaving mice' 'freely moving mice' 'striatum'
   'dopamine']
  lab: Howe
  Group /general/optophysiology/ImagingPlaneGreen (ImagingPlane) 
  Group /general/optophysiology/ImagingPlaneGreen/Green (OpticalChannel) 
  Group /general/optophysiology/ImagingPlaneGreen/device (Device) The microscope (Hamamatsu Orca Fusion BT Gen III) used to acquire the image of the fiber bundle.
  pharmacology: Mice were anesthetized under isoflurane (1-3%) and placed in a stereotaxic frame.
  A large craniotomy was performed with a surgical drill (Midwest Tradition 790044, Avtec Dental RMWT) to expose the
  cortical surface above the striatum. Mice were injected with AAVs to express genetically encoded proteins for
  optical measurements and manipulations. Virus (~200-800nL per site) was injected stereotaxically through a
  pulled glass pipette (diameter 30-50µm) at a rate of ~100nL/min. For striatum expression, virus was injected at
  10-40 total locations chosen to maximize overlap with fiber positions. For midbrain targeting, for one set of mice,
  we injected the 4 sites relative to bregma: AP = -3.05, ML = 0.6, DV = -4.6 and DV = -4.25; AP = -3.5, ML = 1.25,
  DV = -3.9 and DV = -4.5. For a midbrain targeting in another set of mice, we injected at 3.07mm caudal to the bregma
  at 4 sites: ML = 0.5mm, DV =-4.00 mm and -4.25 mm, ML = 1mm, DV = -4.125mm and ML = 1.5 mm, DV = -3.8 mm below the dura.
  
  protocol: https://doi.org/10.17504/protocols.io.bp2l6xyrklqe/v1
  related_publications: ['https://doi.org/10.1016/j.neuron.2023.12.011']
  session_id: 211110
  source_script: Created using NeuroConv v0.5.0
  Group /general/subject (Subject) 
  identifier: 62948f98-4f3d-4a29-8862-b84fa994c6ce
  Group /processing/behavior (ProcessingModule) Contains the velocity signals from two optical mouse sensors (Logitech G203 mice with hard plastic shells removed).
  Group /processing/behavior/AngularVelocity (TimeSeries) The angular velocity from yaw (rotational) velocity converted to radians/s.
  Group /processing/behavior/TimeIntervals (TimeIntervals) Mice were presented with either visual (blue LED) or auditory (12 kHz tone) stimuli at random intervals (4–40 s). For experiments with water reward delivery, a water spout mounted on a post delivered water rewards (9 μL, Figure 1B) at random time intervals (randomly drawn from a 5-30s uniform distribution) through a water spout and solenoid valve gated electronically. Licking was monitored by a capacitive touch circuit connected to the spout.
  Dataset /processing/behavior/TimeIntervals/event_type (VectorData) The type of event (licking, light, tone or reward delivery). | shape = (163,) | dtype = object
  Dataset /processing/behavior/TimeIntervals/id (ElementIdentifiers)  | shape = (163,) | dtype = int64
  Dataset /processing/behavior/TimeIntervals/start_time (VectorData) Start time of epoch, in seconds | shape = (163,) | dtype = float64
  Dataset /processing/behavior/TimeIntervals/stop_time (VectorData) Stop time of epoch, in seconds | shape = (163,) | dtype = float64
  Group /processing/behavior/Velocity (TimeSeries) Velocity for the roll and pitch (x, y) measured in m/s.
  Group /processing/ophys (ProcessingModule) Constains the processed imaging and fiber photometry data.
  Group /processing/ophys/BaselineFiberPhotometryResponseSeriesGreen (FiberPhotometryResponseSeries) Baseline fluorescence traces acquired with multi-fiber array implanted in the striatum.
  Dataset /processing/ophys/BaselineFiberPhotometryResponseSeriesGreen/fiber_photometry_table_region (DynamicTableRegion) source fibers | shape = (103,) | dtype = int64
  Group /processing/ophys/DfOverFFiberPhotometryResponseSeriesGreen (FiberPhotometryResponseSeries) Baseline corrected (DF/F) fluorescence traces acquired with multi-fiber array implanted in the striatum.
  Dataset /processing/ophys/DfOverFFiberPhotometryResponseSeriesGreen/fiber_photometry_table_region (DynamicTableRegion) source fibers | shape = (103,) | dtype = int64
  Group /processing/ophys/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation (PlaneSegmentation) Segmented ROIs
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/Accepted (VectorData) 1 if ROI was accepted or 0 if rejected as a cell during segmentation operation. | shape = (103,) | dtype = int64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/ROICentroids (VectorData) The x, y, (z) centroids of each ROI. | shape = (103, 2) | dtype = float64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/Rejected (VectorData) 1 if ROI was rejected or 0 if accepted as a cell during segmentation operation. | shape = (103,) | dtype = int64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/id (ElementIdentifiers)  | shape = (103,) | dtype = int64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/image_mask (VectorData) Image masks for each ROI. | shape = (103, 381, 378) | dtype = uint8
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/Green (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/device (Device) The microscope (Hamamatsu Orca Fusion BT Gen III) used to acquire the image of the fiber bundle.
  Group /processing/ophys/OnePhotonSeriesMotionCorrectedGreen (OnePhotonSeries) The motion corrected fiber bundle imaging data.
  Group /processing/ophys/OnePhotonSeriesMotionCorrectedGreen/imaging_plane (ImagingPlane) 
  Group /processing/ophys/OnePhotonSeriesMotionCorrectedGreen/imaging_plane/Green (OpticalChannel) 
  Group /processing/ophys/OnePhotonSeriesMotionCorrectedGreen/imaging_plane/device (Device) The microscope (Hamamatsu Orca Fusion BT Gen III) used to acquire the image of the fiber bundle.
  session_description: This dataset contains fiber photometry recordings from multi-fiber arrays implanted in the striatum in mice running
  on a treadmill while receiving either visual (blue LED) or auditory (12 kHz tone) stimuli at random intervals (4–40 s).
  Some sessions may include water reward delivery, where a water spout mounted on a post delivered water rewards (9 μL) at random time intervals (randomly drawn from a 5-30s uniform distribution) through a water spout and solenoid valve gated electronically.
  Licking was monitored by a capacitive touch circuit connected to the spout.
  
  session_start_time: 2021-11-10T16:12:41-05:00
  timestamps_reference_time: 2021-11-10T16:12:41-05:00


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  Group /acquisition/FiberPhotometryResponseSeriesGreen (FiberPhotometryResponseSeries) Raw fluorescence traces acquired with multi-fiber array implanted in the striatum.
  Dataset /acquisition/FiberPhotometryResponseSeriesGreen/fiber_photometry_table_region (DynamicTableRegion) source fibers | shape = (84,) | dtype = int64
  Group /acquisition/OnePhotonSeriesGreen (OnePhotonSeries) Fiber bundle imaging acquired using HCImage Live (Hamamatsu). Single wavelength excitation and emission was performed with continuous, internally triggered imaging at 30Hz.
  Group /acquisition/OnePhotonSeriesGreen/imaging_plane (ImagingPlane) 
  Group /acquisition/OnePhotonSeriesGreen/imaging_plane/Green (OpticalChannel) 
  Group /acquisition/OnePhotonSeriesGreen/imaging_plane/device (Device) The microscope (Hamamatsu Orca Fusion BT Gen III) used to acquire the image of the fiber bundle.
  Group /acquisition/Video: DL20-body-01112022113753-0000 (ImageSeries) Video recorded by camera.
  Group /acquisition/Video: DL20-lick-01112022113749-0000 (ImageSeries) Video recorded by camera.
  file_create_date: ['2024-08-07T14:18:32.605762+02:00']
  Group /general/FiberPhotometry (FiberPhotometry) 
  Group /general/FiberPhotometry/FiberPhotometryTable (FiberPhotometryTable) Contains the metadata for the fiber photometry experiment.
  Dataset /general/FiberPhotometry/FiberPhotometryTable/allen_atlas_coordinates (VectorData) The fiber tip coordinates (AP, ML, DV) in Allen Brain Atlas coordinates | shape = (84, 3) | dtype = int64
  Dataset /general/FiberPhotometry/FiberPhotometryTable/coordinates (VectorData) Fiber placement in stereotactic coordinates (AP, ML, DV) mm relative to Bregma. | shape = (84, 3) | dtype = float64
  Dataset /general/FiberPhotometry/FiberPhotometryTable/dichroic_mirror (VectorData) Link to the dichroic mirror device. | shape = (84,) | dtype = object
  Dataset /general/FiberPhotometry/FiberPhotometryTable/emission_filter (VectorData) Link to the emission filter device. | shape = (84,) | dtype = object
  Dataset /general/FiberPhotometry/FiberPhotometryTable/excitation_filter (VectorData) Link to the excitation filter device. | shape = (84,) | dtype = object
  Dataset /general/FiberPhotometry/FiberPhotometryTable/excitation_source (VectorData) Link to the excitation source device. | shape = (84,) | dtype = object
  Dataset /general/FiberPhotometry/FiberPhotometryTable/id (ElementIdentifiers)  | shape = (84,) | dtype = int64
  Dataset /general/FiberPhotometry/FiberPhotometryTable/included (VectorData) Whether this fiber has been successfully implanted. | shape = (84,) | dtype = bool
  Dataset /general/FiberPhotometry/FiberPhotometryTable/indicator (VectorData) Link to the indicator object. | shape = (84,) | dtype = object
  Dataset /general/FiberPhotometry/FiberPhotometryTable/location (VectorData) Location of fiber. | shape = (84,) | dtype = object
  Dataset /general/FiberPhotometry/FiberPhotometryTable/optical_fiber (VectorData) Link to the optical fiber device. | shape = (84,) | dtype = object
  Dataset /general/FiberPhotometry/FiberPhotometryTable/photodetector (VectorData) Link to the photodetector device. | shape = (84,) | dtype = object
  Group /general/devices/CMOSCamera (Device) A tube lens in each path (Thor labs, No TTL165-A) focused emission light onto the CMOS sensors of the cameras to form an image of the fiber bundle.
  Group /general/devices/CollimatingBeamProbe (Device) Light from the LEDs is filtered, coupled into a liquid light guide with lenses and the collimating beam probe.
  Group /general/devices/DichroicMirror1 (DichroicMirror) The dichroic mirror used to reflect green and pass red fluorescence
  Group /general/devices/ExcitationSource470 (ExcitationSource) Blue excitation light (470 nm LED, Thorlabs, No. SOLIS-470C) and violet excitation light (for the isosbestic control)
  were coupled into the optic fiber such that a power of 0.75 mW was delivered to the fiber tip.
  Then, 470 nm and 405 nm excitation were alternated at 100 Hz using a waveform generator,
  each filtered with a corresponding filter.
  
  Group /general/devices/FiberArray (OpticalFiber) The optical fiber used in a multi-fiber arrays configuration, fabricated in-house to enable large scale measurements across deep brain volumes. Bare fibers were cut into pieces (ca. 3cm) then mounted under a microscope into 55-60μm diameter holes in a custom 3D printed grid (3mm W x 5mm L, Boston Micro Fabrication), measured under a dissection microscope to target a particular depth beneath the grid, and secured in place with UV glue (Norland Optical Adhesive 61). Each array contained between 30 and 103 fibers separated by a minimum of 220μm radially and 250μm axially. Separation was calculated to achieve maximal coverage of the striatum volume with no overlap in the collection fields of individual fibers. Fibers were cut with a fiber scribe, and the distal ends were inspected to ensure a uniform cut, and re-cut as necessary. Distal ends were then glued inside an 1cm ca. section of polyimide tube (0.8-1.3mm diameter, MicroLumen) then cut with a fresh razorblade. The bundled fibers inside the tube were then polished on fine grained polishing paper (ThorLabs,polished first with 6 μm, followed by 3 μm) to create a smooth, uniform fiber bundle surface for imaging. A larger diameter post was mounted on one side of the plastic grid to facilitate holding during implantation.
  Group /general/devices/HamamatsuMicroscope (Device) The microscope (Hamamatsu Orca Fusion BT Gen III) used to acquire the image of the fiber bundle.
  Group /general/devices/Lens1 (Device) Lens focus at 60 mm.
  Group /general/devices/Lens2 (Device) Lens focus at 30 mm.
  Group /general/devices/LiquidLightGuide (Device) The liquid light guide is coupled into a filter cube on the microscope and excitation light is reflected into the back aperture of the microscope objective by a dichroic beam-splitter.
  Group /general/devices/MicroManipulator (Device) The microscope was attached to a micromanipulator to allow fine manual focusing and mounted on a rotatable arm extending over the head-fixation setup to allow for coarse positioning of the objective over the mouse.
  Group /general/devices/MicroscopeObjective (Device) Magnification 10x, Numerical Aperture 0.3.
  Group /general/devices/OpticalFilter470 (BandOpticalFilter) The band-pass filter used to isolate the 470 nm excitation light.
  Group /general/devices/OpticalFilter525 (BandOpticalFilter) The band-pass filter used to isolate the green emitted light after passing through a dichroic (Chroma, No. 532rdc) that reflected green and passed red fluorescence.
  Group /general/devices/TubeLens (Device) A tube lens in each path focuses emission light onto the CMOS sensors of the cameras to form an image of the fiber bundle.
  Group /general/devices/dLight1.3b (Indicator) green dopamine sensor
  experiment_description: Neural population dynamics relevant to behavior vary over multiple spatial and temporal scales across
  three-dimensional volumes. Current optical approaches lack the spatial coverage and resolution necessary to measure
  and manipulate naturally occurring patterns of large-scale, distributed dynamics within and across deep brain
  regions such as the striatum. We designed a new micro-fiber array approach capable of chronically measuring and
  optogenetically manipulating local dynamics across over 100 targeted locations simultaneously in head-fixed and
  freely moving mice, enabling the investigation of cell-type- and neurotransmitter-specific signals over arbitrary
  3D volumes at a spatial resolution and coverage previously inaccessible. We applied this method to resolve rapid
  dopamine release dynamics across the striatum, revealing distinct, modality-specific spatiotemporal patterns in
  response to salient sensory stimuli extending over millimeters of tissue. Targeted optogenetics enabled flexible
  control of neural signaling on multiple spatial scales, better matching endogenous signaling patterns, and the
  spatial localization of behavioral function across large circuits.
  
  experimenter: ['Vu, Mai-Anh']
  institution: Boston University
  keywords: ['multi-fiber photometry' 'behaving mice' 'freely moving mice' 'striatum'
   'dopamine']
  lab: Howe
  Group /general/optophysiology/ImagingPlaneGreen (ImagingPlane) 
  Group /general/optophysiology/ImagingPlaneGreen/Green (OpticalChannel) 
  Group /general/optophysiology/ImagingPlaneGreen/device (Device) The microscope (Hamamatsu Orca Fusion BT Gen III) used to acquire the image of the fiber bundle.
  pharmacology: Mice were anesthetized under isoflurane (1-3%) and placed in a stereotaxic frame.
  A large craniotomy was performed with a surgical drill (Midwest Tradition 790044, Avtec Dental RMWT) to expose the
  cortical surface above the striatum. Mice were injected with AAVs to express genetically encoded proteins for
  optical measurements and manipulations. Virus (~200-800nL per site) was injected stereotaxically through a
  pulled glass pipette (diameter 30-50µm) at a rate of ~100nL/min. For striatum expression, virus was injected at
  10-40 total locations chosen to maximize overlap with fiber positions. For midbrain targeting, for one set of mice,
  we injected the 4 sites relative to bregma: AP = -3.05, ML = 0.6, DV = -4.6 and DV = -4.25; AP = -3.5, ML = 1.25,
  DV = -3.9 and DV = -4.5. For a midbrain targeting in another set of mice, we injected at 3.07mm caudal to the bregma
  at 4 sites: ML = 0.5mm, DV =-4.00 mm and -4.25 mm, ML = 1mm, DV = -4.125mm and ML = 1.5 mm, DV = -3.8 mm below the dura.
  
  protocol: https://doi.org/10.17504/protocols.io.bp2l6xyrklqe/v1
  related_publications: ['https://doi.org/10.1016/j.neuron.2023.12.011']
  session_id: 220111
  source_script: Created using NeuroConv v0.5.0
  Group /general/subject (Subject) 
  identifier: 38d0037a-1583-4e68-8e15-42361924533c
  Group /processing/behavior (ProcessingModule) Contains the velocity signals from two optical mouse sensors (Logitech G203 mice with hard plastic shells removed).
  Group /processing/behavior/AngularVelocity (TimeSeries) The angular velocity from yaw (rotational) velocity converted to radians/s.
  Group /processing/behavior/TimeIntervals (TimeIntervals) Mice were presented with either visual (blue LED) or auditory (12 kHz tone) stimuli at random intervals (4–40 s). For experiments with water reward delivery, a water spout mounted on a post delivered water rewards (9 μL, Figure 1B) at random time intervals (randomly drawn from a 5-30s uniform distribution) through a water spout and solenoid valve gated electronically. Licking was monitored by a capacitive touch circuit connected to the spout.
  Dataset /processing/behavior/TimeIntervals/event_type (VectorData) The type of event (licking, light, tone or reward delivery). | shape = (41,) | dtype = object
  Dataset /processing/behavior/TimeIntervals/id (ElementIdentifiers)  | shape = (41,) | dtype = int64
  Dataset /processing/behavior/TimeIntervals/start_time (VectorData) Start time of epoch, in seconds | shape = (41,) | dtype = float64
  Dataset /processing/behavior/TimeIntervals/stop_time (VectorData) Stop time of epoch, in seconds | shape = (41,) | dtype = float64
  Group /processing/behavior/Velocity (TimeSeries) Velocity for the roll and pitch (x, y) measured in m/s.
  Group /processing/ophys (ProcessingModule) Constains the processed imaging and fiber photometry data.
  Group /processing/ophys/BaselineFiberPhotometryResponseSeriesGreen (FiberPhotometryResponseSeries) Baseline fluorescence traces acquired with multi-fiber array implanted in the striatum.
  Dataset /processing/ophys/BaselineFiberPhotometryResponseSeriesGreen/fiber_photometry_table_region (DynamicTableRegion) source fibers | shape = (84,) | dtype = int64
  Group /processing/ophys/DfOverFFiberPhotometryResponseSeriesGreen (FiberPhotometryResponseSeries) Baseline corrected (DF/F) fluorescence traces acquired with multi-fiber array implanted in the striatum.
  Dataset /processing/ophys/DfOverFFiberPhotometryResponseSeriesGreen/fiber_photometry_table_region (DynamicTableRegion) source fibers | shape = (84,) | dtype = int64
  Group /processing/ophys/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation (PlaneSegmentation) Segmented ROIs
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/Accepted (VectorData) 1 if ROI was accepted or 0 if rejected as a cell during segmentation operation. | shape = (84,) | dtype = int64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/ROICentroids (VectorData) The x, y, (z) centroids of each ROI. | shape = (84, 2) | dtype = float64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/Rejected (VectorData) 1 if ROI was rejected or 0 if accepted as a cell during segmentation operation. | shape = (84,) | dtype = int64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/id (ElementIdentifiers)  | shape = (84,) | dtype = int64
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentation/image_mask (VectorData) Image masks for each ROI. | shape = (84, 354, 353) | dtype = uint8
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/Green (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentation/imaging_plane/device (Device) The microscope (Hamamatsu Orca Fusion BT Gen III) used to acquire the image of the fiber bundle.
  session_description: This dataset contains fiber photometry recordings from multi-fiber arrays implanted in the striatum in mice running
  on a treadmill while receiving either visual (blue LED) or auditory (12 kHz tone) stimuli at random intervals (4–40 s).
  Some sessions may include water reward delivery, where a water spout mounted on a post delivered water rewards (9 μL) at random time intervals (randomly drawn from a 5-30s uniform distribution) through a water spout and solenoid valve gated electronically.
  Licking was monitored by a capacitive touch circuit connected to the spout.
  
  session_start_time: 2022-01-11T11:41:45-05:00
  timestamps_reference_time: 2022-01-11T11:41:45-05:00
