
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000723/0.240716.1414
name: VR-SASE Virtual Reality Dendritic Spine Analysis
contributor: [{'name': 'Reimer, Marike', 'email': 'marike.reimer@yale.edu', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}]
description: The VR-SASE workflow uses Open Brush, open source, virtual reality art software, and Blender to segment neurons.  A DataJoint pipeline determines spatial distribution of dendritic spines, filters them based on morphological parameters and is exported into a CSV for further analysis.
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 208220320, 'numberOfFiles': 30, 'numberOfSubjects': 10, 'variableMeasured': ['ProcessingModule', 'ImagingPlane', 'PlaneSegmentation', 'OpticalChannel'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000723 has 5 NWB files.
1 of these NWB files are of type 1.
1 of these NWB files are of type 2.
1 of these NWB files are of type 3.
1 of these NWB files are of type 4.
1 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Reference Image Sequence (Images) A sequence of images used to create 3D model.
  file_create_date: ['2024-07-10T13:23:19.699729-04:00']
  Group /general/devices/iXon EMCCD 1 (Device) 
  experiment_description: We developed a dendritic spine analysis platform using virtual reality and Blender to study the efficacy of romidepsin as a treatment to reduce spasticity and abnormal dendritic spine growth following a spinal cord contusion injury.
  experimenter: ['']
  institution: Yale University
  lab: 
  notes: 
  Group /general/optophysiology/488nm GFP CF40 (ImagingPlane) 
  Group /general/optophysiology/488nm GFP CF40/Green (OpticalChannel) 
  Group /general/optophysiology/488nm GFP CF40/device (Device) 
  pharmacology: Vehicle 1% DMSO inject IP 4 weeks after SCI
  protocol: 
  slices: Coronal
  Group /general/subject (Subject) 
  surgery: Sham
  identifier: Dendrite1
  Group /processing/MorphologyData (ProcessingModule) Contains processed morphology data from Blender.
  Group /processing/MorphologyData/ImageSegmentation (ImageSegmentation) 
  Group /processing/MorphologyData/ImageSegmentation/MushroomSpine_0_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/MushroomSpine_0_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/MushroomSpine_0_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/MushroomSpine_0_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/MushroomSpine_0_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/MushroomSpine_0_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/MushroomSpine_0_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/MushroomSpine_0_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/MushroomSpine_0_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/MushroomSpine_0_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/MushroomSpine_0_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_7_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_7_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_7_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_7_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_7_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_7_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_7_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_7_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_7_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_7_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_7_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_2_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_2_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_2_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_2_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_2_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_2_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_2_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_2_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_2_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_2_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_2_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  session_description: Image stacks of neurons were converted into OBJs, traced in Tilt Brush, and then segmented in Blender.
  session_start_time: 2024-07-10T13:23:19.699729-04:00
  timestamps_reference_time: 2024-07-10T13:23:19.699729-04:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Reference Image Sequence (Images) A sequence of images used to create 3D model.
  file_create_date: ['2024-07-10T13:22:08.783323-04:00']
  Group /general/devices/iXon EMCCD 1 (Device) 
  experiment_description: We developed a dendritic spine analysis platform using virtual reality and Blender to study the efficacy of romidepsin as a treatment to reduce spasticity and abnormal dendritic spine growth following a spinal cord contusion injury.
  experimenter: ['']
  institution: Yale University
  lab: 
  notes: 
  Group /general/optophysiology/488nm GFP CF40 (ImagingPlane) 
  Group /general/optophysiology/488nm GFP CF40/Green (OpticalChannel) 
  Group /general/optophysiology/488nm GFP CF40/device (Device) 
  pharmacology: Vehicle 1% DMSO inject IP 4 weeks after SCI
  protocol: 
  slices: Coronal
  Group /general/subject (Subject) 
  surgery: Sham
  identifier: Dendrite2
  Group /processing/MorphologyData (ProcessingModule) Contains processed morphology data from Blender.
  Group /processing/MorphologyData/ImageSegmentation (ImageSegmentation) 
  Group /processing/MorphologyData/ImageSegmentation/MushroomSpine_0_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/MushroomSpine_0_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/MushroomSpine_0_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/MushroomSpine_0_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/MushroomSpine_0_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/MushroomSpine_0_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/MushroomSpine_0_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/MushroomSpine_0_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/MushroomSpine_0_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/MushroomSpine_0_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/MushroomSpine_0_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_0_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_0_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_0_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_0_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_0_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_0_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_0_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_0_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_0_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_0_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_0_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_1_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_1_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_1_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_1_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_1_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_1_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_1_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_1_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_1_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_1_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_1_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_2_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_2_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_2_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_2_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_2_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_2_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_2_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_2_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_2_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_2_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_2_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_3_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_3_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_3_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_3_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_3_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_3_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_3_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_3_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_3_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_3_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_3_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_4_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_4_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_4_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_4_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_4_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_4_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_4_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_4_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_4_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_4_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_4_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_0_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_0_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_0_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_0_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_0_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_0_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_0_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_0_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_0_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_0_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_0_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_1_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_1_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_1_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_1_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_1_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_1_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_1_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_1_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_1_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_1_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_1_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_2.001_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_2.001_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_2.001_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_2.001_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_2.001_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_2.001_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_2.001_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_2.001_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_2.001_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_2.001_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_2.001_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_3_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_3_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_3_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_3_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_3_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_3_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_3_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_3_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_3_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_3_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_3_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_4_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_4_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_4_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_4_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_4_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_4_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_4_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_4_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_4_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_4_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_4_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_5_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_5_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_5_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_5_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_5_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_5_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_5_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_5_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_5_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_5_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_5_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_6_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_6_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_6_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_6_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_6_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_6_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_6_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_6_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_6_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_6_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_6_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  session_description: Image stacks of neurons were converted into OBJs, traced in Tilt Brush, and then segmented in Blender.
  session_start_time: 2024-07-10T13:22:08.783323-04:00
  timestamps_reference_time: 2024-07-10T13:22:08.783323-04:00


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Reference Image Sequence (Images) A sequence of images used to create 3D model.
  file_create_date: ['2024-07-10T13:22:33.797832-04:00']
  Group /general/devices/iXon EMCCD 1 (Device) 
  experiment_description: We developed a dendritic spine analysis platform using virtual reality and Blender to study the efficacy of romidepsin as a treatment to reduce spasticity and abnormal dendritic spine growth following a spinal cord contusion injury.
  experimenter: ['']
  institution: Yale University
  lab: 
  notes: 
  Group /general/optophysiology/488nm GFP CF40 (ImagingPlane) 
  Group /general/optophysiology/488nm GFP CF40/Green (OpticalChannel) 
  Group /general/optophysiology/488nm GFP CF40/device (Device) 
  pharmacology: Vehicle 1% DMSO inject IP 4 weeks after SCI
  protocol: 
  slices: Coronal
  Group /general/subject (Subject) 
  surgery: Sham
  identifier: Dendrite2a
  Group /processing/MorphologyData (ProcessingModule) Contains processed morphology data from Blender.
  Group /processing/MorphologyData/ImageSegmentation (ImageSegmentation) 
  Group /processing/MorphologyData/ImageSegmentation/DisconnectedSpine_35.001_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/DisconnectedSpine_35.001_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/DisconnectedSpine_35.001_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/DisconnectedSpine_35.001_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/DisconnectedSpine_35.001_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/DisconnectedSpine_35.001_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/DisconnectedSpine_35.001_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/DisconnectedSpine_35.001_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/DisconnectedSpine_35.001_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/DisconnectedSpine_35.001_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/DisconnectedSpine_35.001_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/DisconnectedSpine_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/DisconnectedSpine_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/DisconnectedSpine_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/DisconnectedSpine_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/DisconnectedSpine_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/DisconnectedSpine_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/DisconnectedSpine_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/DisconnectedSpine_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/DisconnectedSpine_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/DisconnectedSpine_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/DisconnectedSpine_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/MushroomSpine_3_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/MushroomSpine_3_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/MushroomSpine_3_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/MushroomSpine_3_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/MushroomSpine_3_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/MushroomSpine_3_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/MushroomSpine_3_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/MushroomSpine_3_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/MushroomSpine_3_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/MushroomSpine_3_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/MushroomSpine_3_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/MushroomSpine_4.001_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/MushroomSpine_4.001_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/MushroomSpine_4.001_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/MushroomSpine_4.001_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/MushroomSpine_4.001_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/MushroomSpine_4.001_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/MushroomSpine_4.001_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/MushroomSpine_4.001_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/MushroomSpine_4.001_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/MushroomSpine_4.001_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/MushroomSpine_4.001_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/MushroomSpine_4_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/MushroomSpine_4_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/MushroomSpine_4_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/MushroomSpine_4_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/MushroomSpine_4_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/MushroomSpine_4_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/MushroomSpine_4_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/MushroomSpine_4_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/MushroomSpine_4_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/MushroomSpine_4_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/MushroomSpine_4_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_14_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_14_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_14_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_14_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_14_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_14_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_14_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_14_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_14_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_14_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_14_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_15.001_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_15.001_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_15.001_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_15.001_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_15.001_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_15.001_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_15.001_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_15.001_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_15.001_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_15.001_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_15.001_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_15_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_15_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_15_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_15_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_15_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_15_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_15_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_15_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_15_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_15_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_15_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_16.001_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_16.001_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_16.001_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_16.001_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_16.001_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_16.001_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_16.001_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_16.001_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_16.001_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_16.001_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_16.001_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_16_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_16_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_16_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_16_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_16_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_16_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_16_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_16_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_16_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_16_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_16_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_17_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_17_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_17_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_17_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_17_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_17_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_17_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_17_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_17_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_17_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_17_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_18_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_18_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_18_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_18_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_18_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_18_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_18_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_18_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_18_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_18_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_18_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_19_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_19_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_19_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_19_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_19_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_19_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_19_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_19_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_19_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_19_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_19_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_20_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_20_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_20_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_20_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_20_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_20_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_20_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_20_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_20_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_20_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_20_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_21.002_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_21.002_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_21.002_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_21.002_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_21.002_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_21.002_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_21.002_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_21.002_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_21.002_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_21.002_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_21.002_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_21_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_21_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_21_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_21_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_21_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_21_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_21_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_21_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_21_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_21_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_21_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_22_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_22_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_22_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_22_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_22_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_22_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_22_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_22_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_22_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_22_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_22_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_23_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_23_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_23_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_23_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_23_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_23_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_23_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_23_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_23_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_23_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_23_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_24.001_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_24.001_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_24.001_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_24.001_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_24.001_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_24.001_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_24.001_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_24.001_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_24.001_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_24.001_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_24.001_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_25_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_25_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_25_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_25_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_25_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_25_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_25_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_25_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_25_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_25_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_25_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_26.001_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_26.001_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_26.001_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_26.001_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_26.001_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_26.001_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_26.001_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_26.001_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_26.001_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_26.001_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_26.001_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_26_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_26_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_26_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_26_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_26_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_26_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_26_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_26_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_26_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_26_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_26_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_27_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_27_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_27_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_27_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_27_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_27_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_27_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_27_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_27_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_27_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_27_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_28_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_28_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_28_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_28_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_28_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_28_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_28_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_28_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_28_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_28_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_28_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_29_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_29_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_29_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_29_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_29_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_29_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_29_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_29_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_29_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_29_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_29_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_30_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_30_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_30_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_30_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_30_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_30_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_30_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_30_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_30_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_30_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_30_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_31_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_31_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_31_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_31_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_31_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_31_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_31_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_31_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_31_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_31_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_31_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_32_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_32_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_32_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_32_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_32_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_32_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_32_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_32_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_32_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_32_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_32_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_33_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_33_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_33_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_33_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_33_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_33_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_33_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_33_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_33_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_33_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_33_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_34_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_34_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_34_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_34_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_34_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_34_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_34_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_34_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_34_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_34_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_34_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_35_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_35_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_35_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_35_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_35_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_35_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_35_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_35_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_35_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_35_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_35_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_17_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_17_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_17_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_17_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_17_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_17_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_17_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_17_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_17_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_17_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_17_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_18_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_18_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_18_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_18_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_18_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_18_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_18_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_18_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_18_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_18_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_18_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_19_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_19_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_19_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_19_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_19_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_19_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_19_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_19_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_19_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_19_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_19_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_1_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_1_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_1_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_1_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_1_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_1_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_1_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_1_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_1_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_1_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_1_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_20_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_20_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_20_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_20_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_20_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_20_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_20_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_20_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_20_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_20_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_20_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_22_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_22_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_22_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_22_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_22_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_22_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_22_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_22_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_22_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_22_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_22_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_23_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_23_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_23_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_23_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_23_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_23_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_23_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_23_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_23_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_23_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_23_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_24_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_24_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_24_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_24_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_24_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_24_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_24_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_24_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_24_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_24_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_24_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  session_description: Image stacks of neurons were converted into OBJs, traced in Tilt Brush, and then segmented in Blender.
  session_start_time: 2024-07-10T13:22:33.797832-04:00
  timestamps_reference_time: 2024-07-10T13:22:33.797832-04:00


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Reference Image Sequence (Images) A sequence of images used to create 3D model.
  file_create_date: ['2024-07-10T13:23:04.483069-04:00']
  Group /general/devices/iXon EMCCD 1 (Device) 
  experiment_description: We developed a dendritic spine analysis platform using virtual reality and Blender to study the efficacy of romidepsin as a treatment to reduce spasticity and abnormal dendritic spine growth following a spinal cord contusion injury.
  experimenter: ['']
  institution: Yale University
  lab: 
  notes: 
  Group /general/optophysiology/488nm GFP CF40 (ImagingPlane) 
  Group /general/optophysiology/488nm GFP CF40/Green (OpticalChannel) 
  Group /general/optophysiology/488nm GFP CF40/device (Device) 
  pharmacology: Vehicle 1% DMSO inject IP 4 weeks after SCI
  protocol: 
  slices: Coronal
  Group /general/subject (Subject) 
  surgery: Sham
  identifier: Dendrite2b
  Group /processing/MorphologyData (ProcessingModule) Contains processed morphology data from Blender.
  Group /processing/MorphologyData/ImageSegmentation (ImageSegmentation) 
  Group /processing/MorphologyData/ImageSegmentation/MushroomSpine_1_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/MushroomSpine_1_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/MushroomSpine_1_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/MushroomSpine_1_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/MushroomSpine_1_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/MushroomSpine_1_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/MushroomSpine_1_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/MushroomSpine_1_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/MushroomSpine_1_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/MushroomSpine_1_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/MushroomSpine_1_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/MushroomSpine_2_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/MushroomSpine_2_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/MushroomSpine_2_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/MushroomSpine_2_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/MushroomSpine_2_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/MushroomSpine_2_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/MushroomSpine_2_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/MushroomSpine_2_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/MushroomSpine_2_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/MushroomSpine_2_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/MushroomSpine_2_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_0_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_0_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_0_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_0_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_0_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_0_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_0_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_0_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_0_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_0_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_0_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_10.001_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_10.001_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_10.001_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_10.001_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_10.001_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_10.001_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_10.001_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_10.001_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_10.001_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_10.001_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_10.001_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_10_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_10_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_10_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_10_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_10_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_10_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_10_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_10_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_10_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_10_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_10_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_11_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_11_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_11_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_11_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_11_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_11_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_11_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_11_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_11_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_11_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_11_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_12_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_12_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_12_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_12_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_12_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_12_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_12_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_12_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_12_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_12_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_12_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_18_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_18_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_18_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_18_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_18_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_18_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_18_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_18_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_18_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_18_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_18_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_19_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_19_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_19_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_19_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_19_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_19_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_19_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_19_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_19_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_19_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_19_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_1_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_1_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_1_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_1_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_1_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_1_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_1_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_1_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_1_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_1_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_1_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_23_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_23_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_23_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_23_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_23_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_23_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_23_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_23_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_23_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_23_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_23_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_2_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_2_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_2_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_2_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_2_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_2_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_2_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_2_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_2_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_2_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_2_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_3.001_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_3.001_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_3.001_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_3.001_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_3.001_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_3.001_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_3.001_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_3.001_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_3.001_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_3.001_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_3.001_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_33.001_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_33.001_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_33.001_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_33.001_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_33.001_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_33.001_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_33.001_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_33.001_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_33.001_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_33.001_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_33.001_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_3_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_3_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_3_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_3_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_3_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_3_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_3_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_3_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_3_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_3_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_3_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_4_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_4_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_4_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_4_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_4_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_4_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_4_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_4_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_4_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_4_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_4_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_5_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_5_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_5_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_5_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_5_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_5_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_5_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_5_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_5_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_5_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_5_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_6.001_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_6.001_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_6.001_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_6.001_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_6.001_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_6.001_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_6.001_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_6.001_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_6.001_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_6.001_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_6.001_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_7_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_7_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_7_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_7_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_7_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_7_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_7_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_7_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_7_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_7_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_7_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_9.001_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_9.001_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_9.001_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_9.001_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_9.001_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_9.001_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_9.001_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_9.001_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_9.001_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_9.001_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_9.001_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_9_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_9_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_9_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_9_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_9_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_9_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_9_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_9_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_9_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_9_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_9_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_11_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_11_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_11_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_11_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_11_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_11_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_11_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_11_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_11_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_11_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_11_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_13_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_13_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_13_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_13_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_13_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_13_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_13_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_13_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_13_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_13_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_13_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_14_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_14_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_14_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_14_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_14_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_14_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_14_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_14_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_14_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_14_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_14_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_18_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_18_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_18_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_18_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_18_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_18_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_18_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_18_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_18_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_18_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_18_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_28.001_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_28.001_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_28.001_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_28.001_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_28.001_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_28.001_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_28.001_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_28.001_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_28.001_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_28.001_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_28.001_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_2_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_2_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_2_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_2_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_2_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_2_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_2_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_2_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_2_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_2_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_2_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_30_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_30_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_30_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_30_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_30_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_30_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_30_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_30_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_30_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_30_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_30_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_4_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_4_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_4_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_4_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_4_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_4_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_4_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_4_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_4_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_4_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_4_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_5_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_5_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_5_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_5_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_5_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_5_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_5_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_5_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_5_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_5_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_5_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_6_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_6_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_6_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_6_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_6_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_6_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_6_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_6_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_6_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_6_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_6_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_8_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_8_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_8_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_8_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_8_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_8_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_8_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_8_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_8_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_8_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_8_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  session_description: Image stacks of neurons were converted into OBJs, traced in Tilt Brush, and then segmented in Blender.
  session_start_time: 2024-07-10T13:23:04.483069-04:00
  timestamps_reference_time: 2024-07-10T13:23:04.483069-04:00


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Reference Image Sequence (Images) A sequence of images used to create 3D model.
  file_create_date: ['2024-07-10T13:23:38.829070-04:00']
  Group /general/devices/iXon EMCCD 1 (Device) 
  experiment_description: We developed a dendritic spine analysis platform using virtual reality and Blender to study the efficacy of romidepsin as a treatment to reduce spasticity and abnormal dendritic spine growth following a spinal cord contusion injury.
  experimenter: ['']
  institution: Yale University
  lab: 
  notes: 
  Group /general/optophysiology/488nm GFP CF40 (ImagingPlane) 
  Group /general/optophysiology/488nm GFP CF40/Green (OpticalChannel) 
  Group /general/optophysiology/488nm GFP CF40/device (Device) 
  pharmacology: Vehicle
  protocol: 
  slices: Coronal
  Group /general/subject (Subject) 
  surgery: Contusion: (50 kDyn) SCI at the thoracic vertebral level 11 (T11), lumbar segment 2 (L2)
  identifier: Dendrite1b
  Group /processing/MorphologyData (ProcessingModule) Contains processed morphology data from Blender.
  Group /processing/MorphologyData/ImageSegmentation (ImageSegmentation) 
  Group /processing/MorphologyData/ImageSegmentation/DisconnectedSpine_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/DisconnectedSpine_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/DisconnectedSpine_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/DisconnectedSpine_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/DisconnectedSpine_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/DisconnectedSpine_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/DisconnectedSpine_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/DisconnectedSpine_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/DisconnectedSpine_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/DisconnectedSpine_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/DisconnectedSpine_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_10_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_10_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_10_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_10_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_10_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_10_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_10_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_10_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_10_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_10_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_10_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_11_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_11_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_11_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_11_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_11_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_11_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_11_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_11_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_11_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_11_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_11_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_12_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_12_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_12_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_12_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_12_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_12_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_12_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_12_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_12_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_12_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_12_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_13_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_13_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_13_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_13_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_13_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_13_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_13_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_13_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_13_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_13_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_13_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_14_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_14_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_14_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_14_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_14_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_14_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_14_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_14_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_14_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_14_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_14_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_15_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_15_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_15_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_15_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_15_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_15_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_15_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_15_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_15_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_15_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_15_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_16_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_16_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_16_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_16_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_16_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_16_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_16_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_16_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_16_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_16_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_16_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_17_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_17_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_17_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_17_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_17_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_17_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_17_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_17_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_17_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_17_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_17_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_18_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_18_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_18_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_18_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_18_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_18_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_18_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_18_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_18_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_18_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_18_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_19_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_19_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_19_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_19_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_19_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_19_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_19_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_19_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_19_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_19_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_19_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_20_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_20_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_20_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_20_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_20_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_20_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_20_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_20_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_20_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_20_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_20_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_21_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_21_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_21_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_21_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_21_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_21_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_21_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_21_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_21_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_21_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_21_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_22_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_22_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_22_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_22_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_22_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_22_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_22_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_22_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_22_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_22_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_22_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_9_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_9_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_9_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_9_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_9_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_9_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_9_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_9_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_9_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_9_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_9_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/StubbySpine_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/StubbySpine_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_1_plane_segmentaton (PlaneSegmentation) output from segmenting a mesh in Blender
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_1_plane_segmentaton/center_of_mass (VectorData) center_of_mass | shape = (1, 3) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_1_plane_segmentaton/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_1_plane_segmentaton/imaging_plane (ImagingPlane) 
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_1_plane_segmentaton/imaging_plane/Green (OpticalChannel) 
  Group /processing/MorphologyData/ImageSegmentation/ThinSpine_1_plane_segmentaton/imaging_plane/device (Device) 
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_1_plane_segmentaton/length (VectorData) length | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_1_plane_segmentaton/pixel_mask (VectorData) Pixel masks for each ROI | shape = (1,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_1_plane_segmentaton/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (1,) | dtype = uint8
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_1_plane_segmentaton/surface_area (VectorData) surface_area | shape = (1,) | dtype = float64
  Dataset /processing/MorphologyData/ImageSegmentation/ThinSpine_1_plane_segmentaton/volume (VectorData) volume | shape = (1,) | dtype = float64
  session_description: Image stacks of neurons were converted into OBJs, traced in Tilt Brush, and then segmented in Blender.
  session_start_time: 2024-07-10T13:23:38.829070-04:00
  timestamps_reference_time: 2024-07-10T13:23:38.829070-04:00
