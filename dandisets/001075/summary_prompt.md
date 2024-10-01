
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001075/0.240930.1859
name: Neural signal propagation atlas of Caenorhabditis elegans
contributor: [{'name': 'Baker, Cody', 'email': 'cody.c.baker.phd@gmail.com', 'roleName': ['dcite:DataCurator'], 'schemaKey': 'Person', 'identifier': '0000-0002-0829-4790', 'affiliation': [], 'includeInCitation': False}, {'name': 'Randi, Francesco', 'roleName': ['dcite:Author', 'dcite:DataCollector'], 'schemaKey': 'Person', 'identifier': '0000-0002-6200-7254', 'includeInCitation': True}, {'name': 'Sharma, Anuj', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0001-5061-9731', 'includeInCitation': True}, {'name': 'Dvali, Sophie', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0001-8565-7148', 'includeInCitation': True}, {'url': 'https://phy.princeton.edu/people/andrew-leifer', 'name': 'Leifer, Andrew M.', 'email': 'leifer@princeton.edu', 'roleName': ['dcite:ContactPerson', 'dcite:Author', 'dcite:Conceptualization'], 'schemaKey': 'Person', 'identifier': '0000-0002-5362-5093', 'includeInCitation': True}, {'url': 'http://www.ninds.nih.gov/', 'name': 'Institutes of Health National Institute of Neurological Disorders and Stroke', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01s5ya894', 'awardNumber': 'DP2-NS116768', 'includeInCitation': False}, {'url': 'https://www.simonsfoundation.org', 'name': 'Simons Foundation', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01cmst727', 'awardNumber': 'SCGB 543003', 'includeInCitation': False}, {'url': 'http://www.theswartzfoundation.org/', 'name': 'Swartz Foundation', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/04eqn7j88', 'includeInCitation': False}, {'url': 'https://www.nsf.gov', 'name': 'National Science Foundation', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/021nxhr62', 'awardNumber': 'PHY-1734030', 'includeInCitation': False}, {'url': 'https://orip.nih.gov', 'name': 'NIH Office of Research Infrastructure Programs', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01jdyfj45', 'awardNumber': 'P40 OD010440', 'includeInCitation': False}]
description: The dataset used in the paper "Randi, F., Sharma, A.K., Dvali, S. et al. Neural signal propagation atlas of Caenorhabditis elegans. Nature 623, 406–414 (2023)."

Establishing how neural function emerges from network properties is a fundamental problem in neuroscience. Here, to better understand the relationship between the structure and the function of a nervous system, we systematically measure signal propagation in 23,433 pairs of neurons across the head of the nematode Caenorhabditis elegans by direct optogenetic activation and simultaneous whole-brain calcium imaging. We measure the sign (excitatory or inhibitory), strength, temporal properties and causal direction of signal propagation between these neurons to create a functional atlas. We find that signal propagation differs from model predictions that are based on anatomy. Using mutants, we show that extrasynaptic signalling not visible from anatomy contributes to this difference. We identify many instances of dense-core-vesicle-dependent signalling, including on timescales of less than a second, that evoke acute calcium transients—often where no direct wired connection exists but where relevant neuropeptides and receptors are expressed. We propose that, in such cases, extrasynaptically released neuropeptides serve a similar function to that of classical neurotransmitters. Finally, our measured signal propagation atlas better predicts the neural dynamics of spontaneous activity than do models based on anatomy. We conclude that both synaptic and extrasynaptic signalling drive neural dynamics on short timescales, and that measurements of evoked signal propagation are crucial for interpreting neural function.

Read the paper at: https://www.nature.com/articles/s41586-023-06683-4
assetsSummary: {'species': [{'name': 'Caenorhabditis elegans', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_6239'}], 'approach': [{'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 4074234123623, 'numberOfFiles': 223, 'numberOfSubjects': 113, 'variableMeasured': ['OpticalChannel', 'ProcessingModule', 'PlaneSegmentation', 'ImagingPlane'], 'measurementTechnique': [{'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 001075 has 71 NWB files.
52 of these NWB files are of type 1.
7 of these NWB files are of type 2.
1 of these NWB files are of type 3.
9 of these NWB files are of type 4.
2 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/NeuroPALImaging (VariableDepthMultiChannelMicroscopyVolume) A static volume scan used for NeuroPAL registration.
  Group /acquisition/NeuroPALImaging/imaging_space (VolumetricImagingSpace) 
  Group /acquisition/NeuroPALImaging/imaging_space/microscope (Microscope) 
  Dataset /acquisition/NeuroPALImaging/light_sources (VectorData) Light sources used by this MultiChannelVolume. | shape = (4,) | dtype = object
  Group /acquisition/NeuroPALImaging/microscope (Microscope) 
  Dataset /acquisition/NeuroPALImaging/optical_channels (VectorData) Optical channels ordered to correspond to the third axis (e.g., [0, 0, :, 0]) of the data for this MultiChannelVolume. | shape = (4,) | dtype = object
  Group /acquisition/PumpProbeImagingGreen (VariableDepthMicroscopySeries) The raw functional imaging data of the variable-depth PumpProbe scan.
  Group /acquisition/PumpProbeImagingGreen/imaging_space (PlanarImagingSpace) 
  Group /acquisition/PumpProbeImagingGreen/imaging_space/microscope (Microscope) 
  Group /acquisition/PumpProbeImagingGreen/light_source (MicroscopyLightSource) 
  Group /acquisition/PumpProbeImagingGreen/microscope (Microscope) 
  Group /acquisition/PumpProbeImagingGreen/optical_channel (MicroscopyOpticalChannel) 
  Group /acquisition/PumpProbeImagingRed (VariableDepthMicroscopySeries) The raw functional imaging data of the variable-depth PumpProbe scan.
  Group /acquisition/PumpProbeImagingRed/imaging_space (PlanarImagingSpace) 
  Group /acquisition/PumpProbeImagingRed/imaging_space/microscope (Microscope) 
  Group /acquisition/PumpProbeImagingRed/light_source (MicroscopyLightSource) 
  Group /acquisition/PumpProbeImagingRed/microscope (Microscope) 
  Group /acquisition/PumpProbeImagingRed/optical_channel (MicroscopyOpticalChannel) 
  file_create_date: ['2024-09-18T17:23:23.534595-04:00']
  Group /general/CyOFP1.5Filter (MicroscopyOpticalChannel) 
  Group /general/GreenOpticalChannel (MicroscopyOpticalChannel) 
  Group /general/NeuroPALImagingSpace (VolumetricImagingSpace) 
  Group /general/NeuroPALImagingSpace/microscope (Microscope) 
  Group /general/PumpProbeImagingSpace (PlanarImagingSpace) 
  Group /general/PumpProbeImagingSpace/microscope (Microscope) 
  Group /general/RedOpticalChannel (MicroscopyOpticalChannel) 
  Group /general/devices/CyOFP1.5LightSource (MicroscopyLightSource) 
  Group /general/devices/LightSource (MicroscopyLightSource) 
  Group /general/devices/Microscope (Microscope) 
  Group /general/devices/MicroscopyLightSource (MicroscopyLightSource) 
  Group /general/devices/mNeptune2.5LightSource (MicroscopyLightSource) 
  Group /general/devices/mtagBFP2LightSource (MicroscopyLightSource) 
  Group /general/devices/tagRFP-TLightSource (MicroscopyLightSource) 
  experiment_description: 
      To measure signal propagation, we activated each single neuron, one at a time, through two-photon stimulation,
      while simultaneously recording the calcium activity of the population at cellular resolution using spinning disk
      confocal microscopy. We recorded activity from 113 wild-type (WT)-background animals, each for up to 40min, while
      stimulating a mostly randomly selected sequence of neurons one by one every 30s. We spatially restricted our
      two-photon activation in three dimensions to be the size of a typical C. elegans neuron, to minimize off-target
      activation of neighbouring neurons. Animals were immobilized but awake,and pharyngeal pumping was visible during
      recordings.
      
  experimenter: ['Randi, Francesco']
  institution: Princeton University
  keywords: ['C. elegans' 'optogenetics' 'functional connectivity']
  lab: Leifer Lab
  Group /general/mNeptune2.5Filter (MicroscopyOpticalChannel) 
  Group /general/mtagBFP2Filter (MicroscopyOpticalChannel) 
  source_script: Created using NeuroConv v0.6.1
  Group /general/subject (CElegansSubject) 
  Group /general/tagRFP-TFilter (MicroscopyOpticalChannel) 
  identifier: 1011d066-a0db-416f-85b9-6c3f9f1227e2
  session_description: 
  session_start_time: 2021-08-24T10:40:00-04:00
  timestamps_reference_time: 2021-08-24T10:40:00-04:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2024-09-30T14:05:41.612101-04:00']
  Group /general/NeuroPALImagingSpace (VolumetricImagingSpace) 
  Group /general/NeuroPALImagingSpace/microscope (Microscope) 
  Group /general/OptogeneticStimulusTarget0 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget0/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget1 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget1/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget10 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget10/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget11 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget11/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget12 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget12/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget13 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget13/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget14 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget14/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget15 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget15/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget16 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget16/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget17 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget17/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget18 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget18/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget19 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget19/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget2 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget2/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget20 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget20/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget21 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget21/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget22 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget22/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget23 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget23/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget24 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget24/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget25 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget25/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget26 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget26/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget27 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget27/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget28 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget28/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget29 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget29/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget3 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget3/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget30 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget30/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget31 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget31/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget32 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget32/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget33 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget33/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget34 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget34/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget35 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget35/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget36 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget36/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget37 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget37/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget38 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget38/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget39 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget39/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget4 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget4/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget40 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget40/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget41 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget41/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget42 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget42/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget43 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget43/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget44 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget44/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget45 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget45/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget46 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget46/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget47 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget47/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget48 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget48/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget49 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget49/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget5 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget5/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget50 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget50/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget51 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget51/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget52 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget52/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget53 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget53/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget54 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget54/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget55 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget55/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget56 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget56/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget57 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget57/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget58 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget58/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget59 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget59/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget6 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget6/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget60 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget60/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget61 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget61/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget62 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget62/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget63 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget63/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget64 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget64/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget65 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget65/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget66 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget66/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget67 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget67/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget68 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget68/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget69 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget69/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget7 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget7/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget8 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget8/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget9 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget9/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/PumpProbeImagingSpace (PlanarImagingSpace) 
  Group /general/PumpProbeImagingSpace/microscope (Microscope) 
  Group /general/TemporalFocusing (TemporalFocusing) We used temporal focusing to spatially restrict the size of the two-photon excitation spot along the microscope axis. A motorized iris was used to set its lateral size. For temporal focusing, the first-order diffraction from a reflective grating, oriented orthogonally to the microscope axis, was collected and travelled through the motorized iris, placed on a plane conjugate to the grating.To arbitrarily position the two-photon excitation spot in the sample volume, the beam then travelled through an electrically tunable lens (Optotune EL-16-40-TC, on a plane conjugate to the objective), to set its position along the microscope axis, and finally was reflected by two galvo-mirrors to set its lateral position. The pulsed beam was then combined with the imaging light path by a dichroic mirror immediately before entering the back of the objective.
  Group /general/devices/AmplifiedLaser (LightSource) For two-photon optogenetic targeting, we used an optical parametric amplifier (OPA; Light Conversion ORPHEUS) pumped by a femtosecond amplified laser (Light Conversion PHAROS).
  Group /general/devices/Microscope (Microscope) 
  Group /general/devices/OptogeneticDevice (Device) 
  experiment_description: 
      To measure signal propagation, we activated each single neuron, one at a time, through two-photon stimulation,
      while simultaneously recording the calcium activity of the population at cellular resolution using spinning disk
      confocal microscopy. We recorded activity from 113 wild-type (WT)-background animals, each for up to 40min, while
      stimulating a mostly randomly selected sequence of neurons one by one every 30s. We spatially restricted our
      two-photon activation in three dimensions to be the size of a typical C. elegans neuron, to minimize off-target
      activation of neighbouring neurons. Animals were immobilized but awake,and pharyngeal pumping was visible during
      recordings.
      
  experimenter: ['Randi, Francesco']
  institution: Princeton University
  keywords: ['C. elegans' 'optogenetics' 'functional connectivity']
  lab: Leifer Lab
  Group /general/optogenetics/PatternedOptogeneticStimulusSite (PatternedOptogeneticStimulusSite) 
  Group /general/optogenetics/PatternedOptogeneticStimulusSite/device (Device) 
  Group /general/optogenetics/PatternedOptogeneticStimulusSite/light_source (LightSource) For two-photon optogenetic targeting, we used an optical parametric amplifier (OPA; Light Conversion ORPHEUS) pumped by a femtosecond amplified laser (Light Conversion PHAROS).
  Group /general/optophysiology/TargetImagingPlane (ImagingPlane) 
  Group /general/optophysiology/TargetImagingPlane/DummyOpticalChannel (OpticalChannel) 
  Group /general/optophysiology/TargetImagingPlane/device (Device) 
  source_script: Created using NeuroConv v0.6.1
  Group /general/subject (CElegansSubject) 
  identifier: f0ab1f61-abe9-4d0b-bcb4-2ce1ff95c4c4
  Group /intervals/OptogeneticStimulusTable (PatternedOptogeneticStimulusTable) Every 30 seconds, a random neuron was selected among the neurons found in the current volumetric image, on the basis of only its tagRFP-T signal. After galvo-mirrors and the tunable lens set the position of the two-photon spot on that neuron, a 500-ms (300-ms for the unc-31-mutant strain) train of light pulses was used to optogenetically stimulate that neuron. The duration of stimulus illumination for the unc-31-mutant strain was selected to elicit calcium transients in stimulated neurons with a distribution of amplitudes such that the maximum amplitude was similar to those in WT-background animals. The output of the laser was controlled through the external interface to its built-in pulse picker, and the power of the laser at the sample was 1.2mW at 500kHz. Neuron identities were assigned to stimulated neurons after the completion of experiments using NeuroPAL.
  Dataset /intervals/OptogeneticStimulusTable/id (ElementIdentifiers)  | shape = (70,) | dtype = int32
  Dataset /intervals/OptogeneticStimulusTable/power (VectorData) Power (in Watts) defined as a scalar. All rois in target receive the same photostimulation power. | shape = (70,) | dtype = float64
  Dataset /intervals/OptogeneticStimulusTable/start_time (VectorData) Start time of epoch, in seconds | shape = (70,) | dtype = float64
  Dataset /intervals/OptogeneticStimulusTable/stimulus_pattern (VectorData) Link to the stimulus pattern. | shape = (70,) | dtype = object
  Dataset /intervals/OptogeneticStimulusTable/stimulus_site (VectorData) Link to the stimulus site. | shape = (70,) | dtype = object
  Dataset /intervals/OptogeneticStimulusTable/stop_time (VectorData) Stop time of epoch, in seconds | shape = (70,) | dtype = float64
  Dataset /intervals/OptogeneticStimulusTable/target_pumpprobe_id (VectorData) Manually targeted ID in the PumpProbe space. Values are upcast to float to allow NaN; cast back to int to lookup correspond NeuroPAL label. | shape = (70,) | dtype = float64
  Dataset /intervals/OptogeneticStimulusTable/targets (VectorData) Targeted rois for the stimulus onset. | shape = (70,) | dtype = object
  Group /processing/ophys (ProcessingModule) Contains segmented imaging data.
  Group /processing/ophys/GreenSignals (MicroscopyResponseSeriesContainer) 
  Group /processing/ophys/GreenSignals/BaseGreenSignal (MicroscopyResponseSeries) Average baseline fluorescence for the 'Green' optical channel extracted from the raw imaging and averaged over a volume defined as a complete scan cycle over volumetric depths. This series includes NaNs for certain frame values that could not be inferred from the imaging data.
  Dataset /processing/ophys/GreenSignals/BaseGreenSignal/table_region (DynamicTableRegion)  | shape = (114,) | dtype = int32
  Group /processing/ophys/GreenSignals/InterpolatedGreenSignal (MicroscopyResponseSeries) Average baseline fluorescence for the 'Green' optical channel extracted from the raw imaging and averaged over a volume defined as a complete scan cycle over volumetric depths. This series has interpolated the NaN frames in the corresponding 'base' signal.
  Dataset /processing/ophys/GreenSignals/InterpolatedGreenSignal/table_region (DynamicTableRegion)  | shape = (114,) | dtype = int32
  Group /processing/ophys/NeuroPALSegmentations (MicroscopySegmentations) 
  Group /processing/ophys/NeuroPALSegmentations/NeuroPALPlaneSegmentation (MicroscopyPlaneSegmentation) The NeuroPAL segmentation of the C. elegans brain with cell labels.
  Dataset /processing/ophys/NeuroPALSegmentations/NeuroPALPlaneSegmentation/centroids (VectorData) The centroids of each ROI. | shape = (170, 3) | dtype = int32
  Dataset /processing/ophys/NeuroPALSegmentations/NeuroPALPlaneSegmentation/id (ElementIdentifiers)  | shape = (170,) | dtype = int32
  Group /processing/ophys/NeuroPALSegmentations/NeuroPALPlaneSegmentation/imaging_space (VolumetricImagingSpace) 
  Group /processing/ophys/NeuroPALSegmentations/NeuroPALPlaneSegmentation/imaging_space/microscope (Microscope) 
  Dataset /processing/ophys/NeuroPALSegmentations/NeuroPALPlaneSegmentation/labels (VectorData) The C. elegans cell names labeled from the NeuroPAL imaging. | shape = (170,) | dtype = object
  Dataset /processing/ophys/NeuroPALSegmentations/NeuroPALPlaneSegmentation/labels_comments (VectorData) Various comments about the cell label classification process. | shape = (170,) | dtype = object
  Dataset /processing/ophys/NeuroPALSegmentations/NeuroPALPlaneSegmentation/labels_confidences (VectorData) The C. elegans cell names labeled from the NeuroPAL imaging. | shape = (170,) | dtype = float64
  Dataset /processing/ophys/NeuroPALSegmentations/NeuroPALPlaneSegmentation/voxel_mask (VectorData) Voxel masks for each ROI: a list of indices and weights for the ROI. Voxel masks are concatenated and parsing of this dataset is maintained by the PlaneSegmentation | shape = (1530,) | dtype = [('x', '<u4'), ('y', '<u4'), ('z', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/NeuroPALSegmentations/NeuroPALPlaneSegmentation/voxel_mask_index (VectorIndex) Index for VectorData 'voxel_mask' | shape = (170,) | dtype = uint16
  Group /processing/ophys/PumpProbeGreenSegmentations (MicroscopySegmentations) 
  Group /processing/ophys/PumpProbeGreenSegmentations/PumpProbeGreenPlaneSegmentation (MicroscopyPlaneSegmentation) The PumpProbe segmentation of the C. elegans brain. Only some of these local ROI IDs match the NeuroPAL IDs with cell labels. Note that the Z-axis of the `voxel_mask` is in reference to the index of that depth in its scan cycle.
  Dataset /processing/ophys/PumpProbeGreenSegmentations/PumpProbeGreenPlaneSegmentation/centroids (VectorData) The centroids of each ROI. | shape = (114, 3) | dtype = int32
  Dataset /processing/ophys/PumpProbeGreenSegmentations/PumpProbeGreenPlaneSegmentation/id (ElementIdentifiers)  | shape = (114,) | dtype = int32
  Group /processing/ophys/PumpProbeGreenSegmentations/PumpProbeGreenPlaneSegmentation/imaging_space (PlanarImagingSpace) 
  Group /processing/ophys/PumpProbeGreenSegmentations/PumpProbeGreenPlaneSegmentation/imaging_space/microscope (Microscope) 
  Dataset /processing/ophys/PumpProbeGreenSegmentations/PumpProbeGreenPlaneSegmentation/neuropal_ids (VectorData) The NeuroPAL ROI ID that has been matched to this PumpProbe ID. Blank means the ROI was not matched. | shape = (114,) | dtype = object
  Dataset /processing/ophys/PumpProbeGreenSegmentations/PumpProbeGreenPlaneSegmentation/voxel_mask (VectorData) Voxel masks for each ROI: a list of indices and weights for the ROI. Voxel masks are concatenated and parsing of this dataset is maintained by the PlaneSegmentation | shape = (8550,) | dtype = [('x', '<u4'), ('y', '<u4'), ('z', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/PumpProbeGreenSegmentations/PumpProbeGreenPlaneSegmentation/voxel_mask_index (VectorIndex) Index for VectorData 'voxel_mask' | shape = (114,) | dtype = uint16
  Group /processing/ophys/PumpProbeRedSegmentations (MicroscopySegmentations) 
  Group /processing/ophys/PumpProbeRedSegmentations/PumpProbeRedPlaneSegmentation (MicroscopyPlaneSegmentation) The PumpProbe segmentation of the C. elegans brain. Only some of these local ROI IDs match the NeuroPAL IDs with cell labels. Note that the Z-axis of the `voxel_mask` is in reference to the index of that depth in its scan cycle.
  Dataset /processing/ophys/PumpProbeRedSegmentations/PumpProbeRedPlaneSegmentation/centroids (VectorData) The centroids of each ROI. | shape = (114, 3) | dtype = int32
  Dataset /processing/ophys/PumpProbeRedSegmentations/PumpProbeRedPlaneSegmentation/id (ElementIdentifiers)  | shape = (114,) | dtype = int32
  Group /processing/ophys/PumpProbeRedSegmentations/PumpProbeRedPlaneSegmentation/imaging_space (PlanarImagingSpace) 
  Group /processing/ophys/PumpProbeRedSegmentations/PumpProbeRedPlaneSegmentation/imaging_space/microscope (Microscope) 
  Dataset /processing/ophys/PumpProbeRedSegmentations/PumpProbeRedPlaneSegmentation/neuropal_ids (VectorData) The NeuroPAL ROI ID that has been matched to this PumpProbe ID. Blank means the ROI was not matched. | shape = (114,) | dtype = object
  Dataset /processing/ophys/PumpProbeRedSegmentations/PumpProbeRedPlaneSegmentation/voxel_mask (VectorData) Voxel masks for each ROI: a list of indices and weights for the ROI. Voxel masks are concatenated and parsing of this dataset is maintained by the PlaneSegmentation | shape = (8550,) | dtype = [('x', '<u4'), ('y', '<u4'), ('z', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/PumpProbeRedSegmentations/PumpProbeRedPlaneSegmentation/voxel_mask_index (VectorIndex) Index for VectorData 'voxel_mask' | shape = (114,) | dtype = uint16
  Group /processing/ophys/RedSignals (MicroscopyResponseSeriesContainer) 
  Group /processing/ophys/RedSignals/BaseRedSignal (MicroscopyResponseSeries) Average baseline fluorescence for the 'Red' optical channel extracted from the raw imaging and averaged over a volume defined as a complete scan cycle over volumetric depths. This series includes NaNs for certain frame values that could not be inferred from the imaging data.
  Dataset /processing/ophys/RedSignals/BaseRedSignal/table_region (DynamicTableRegion)  | shape = (114,) | dtype = int32
  Group /processing/ophys/RedSignals/InterpolatedRedSignal (MicroscopyResponseSeries) Average baseline fluorescence for the 'Red' optical channel extracted from the raw imaging and averaged over a volume defined as a complete scan cycle over volumetric depths. This series has interpolated the NaN frames in the corresponding 'base' signal.
  Dataset /processing/ophys/RedSignals/InterpolatedRedSignal/table_region (DynamicTableRegion)  | shape = (114,) | dtype = int32
  Group /processing/ophys/TargetedImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/TargetedImageSegmentation/TargetPlaneSegmentation (PlaneSegmentation) Table for storing the target centroids, defined by a one-voxel mask.
  Dataset /processing/ophys/TargetedImageSegmentation/TargetPlaneSegmentation/depth_in_um (VectorData) Targeted depth in micrometers. | shape = (70,) | dtype = float64
  Dataset /processing/ophys/TargetedImageSegmentation/TargetPlaneSegmentation/id (ElementIdentifiers)  | shape = (70,) | dtype = int32
  Group /processing/ophys/TargetedImageSegmentation/TargetPlaneSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys/TargetedImageSegmentation/TargetPlaneSegmentation/imaging_plane/DummyOpticalChannel (OpticalChannel) 
  Group /processing/ophys/TargetedImageSegmentation/TargetPlaneSegmentation/imaging_plane/device (Device) 
  Dataset /processing/ophys/TargetedImageSegmentation/TargetPlaneSegmentation/pixel_mask (VectorData) Pixel masks for each ROI | shape = (70,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/TargetedImageSegmentation/TargetPlaneSegmentation/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (70,) | dtype = uint8
  session_description: 
  session_start_time: 2021-08-24T10:40:00-04:00
  timestamps_reference_time: 2021-08-24T10:40:00-04:00


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2024-09-30T14:05:49.628085-04:00']
  Group /general/NeuroPALImagingSpace (VolumetricImagingSpace) 
  Group /general/NeuroPALImagingSpace/microscope (Microscope) 
  Group /general/OptogeneticStimulusTarget0 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget0/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget1 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget1/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget10 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget10/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget11 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget11/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget12 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget12/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget13 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget13/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget14 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget14/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget15 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget15/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget16 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget16/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget17 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget17/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget18 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget18/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget19 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget19/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget2 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget2/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget20 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget20/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget21 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget21/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget22 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget22/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget23 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget23/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget24 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget24/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget25 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget25/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget26 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget26/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget27 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget27/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget28 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget28/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget29 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget29/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget3 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget3/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget30 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget30/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget31 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget31/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget32 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget32/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget33 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget33/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget34 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget34/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget35 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget35/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget36 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget36/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget37 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget37/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget38 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget38/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget39 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget39/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget4 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget4/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget40 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget40/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget41 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget41/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget42 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget42/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget43 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget43/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget44 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget44/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget45 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget45/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget46 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget46/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget47 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget47/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget48 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget48/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget49 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget49/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget5 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget5/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget50 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget50/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget51 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget51/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget52 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget52/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget53 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget53/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget54 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget54/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget55 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget55/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget56 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget56/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget57 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget57/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget58 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget58/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget59 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget59/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget6 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget6/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget60 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget60/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget61 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget61/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget62 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget62/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget63 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget63/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget64 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget64/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget65 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget65/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget66 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget66/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget67 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget67/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget68 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget68/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget69 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget69/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget7 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget7/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget70 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget70/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget71 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget71/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget72 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget72/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget73 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget73/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget74 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget74/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget75 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget75/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget76 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget76/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget77 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget77/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget78 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget78/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget79 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget79/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget8 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget8/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget80 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget80/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget81 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget81/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget82 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget82/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget83 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget83/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget84 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget84/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget9 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget9/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/PumpProbeImagingSpace (PlanarImagingSpace) 
  Group /general/PumpProbeImagingSpace/microscope (Microscope) 
  Group /general/TemporalFocusing (TemporalFocusing) We used temporal focusing to spatially restrict the size of the two-photon excitation spot along the microscope axis. A motorized iris was used to set its lateral size. For temporal focusing, the first-order diffraction from a reflective grating, oriented orthogonally to the microscope axis, was collected and travelled through the motorized iris, placed on a plane conjugate to the grating.To arbitrarily position the two-photon excitation spot in the sample volume, the beam then travelled through an electrically tunable lens (Optotune EL-16-40-TC, on a plane conjugate to the objective), to set its position along the microscope axis, and finally was reflected by two galvo-mirrors to set its lateral position. The pulsed beam was then combined with the imaging light path by a dichroic mirror immediately before entering the back of the objective.
  Group /general/devices/AmplifiedLaser (LightSource) For two-photon optogenetic targeting, we used an optical parametric amplifier (OPA; Light Conversion ORPHEUS) pumped by a femtosecond amplified laser (Light Conversion PHAROS).
  Group /general/devices/Microscope (Microscope) 
  Group /general/devices/OptogeneticDevice (Device) 
  experiment_description: 
      To measure signal propagation, we activated each single neuron, one at a time, through two-photon stimulation,
      while simultaneously recording the calcium activity of the population at cellular resolution using spinning disk
      confocal microscopy. We recorded activity from 113 wild-type (WT)-background animals, each for up to 40min, while
      stimulating a mostly randomly selected sequence of neurons one by one every 30s. We spatially restricted our
      two-photon activation in three dimensions to be the size of a typical C. elegans neuron, to minimize off-target
      activation of neighbouring neurons. Animals were immobilized but awake,and pharyngeal pumping was visible during
      recordings.
      
  experimenter: ['Randi, Francesco']
  institution: Princeton University
  keywords: ['C. elegans' 'optogenetics' 'functional connectivity']
  lab: Leifer Lab
  Group /general/optogenetics/PatternedOptogeneticStimulusSite (PatternedOptogeneticStimulusSite) 
  Group /general/optogenetics/PatternedOptogeneticStimulusSite/device (Device) 
  Group /general/optogenetics/PatternedOptogeneticStimulusSite/light_source (LightSource) For two-photon optogenetic targeting, we used an optical parametric amplifier (OPA; Light Conversion ORPHEUS) pumped by a femtosecond amplified laser (Light Conversion PHAROS).
  Group /general/optophysiology/TargetImagingPlane (ImagingPlane) 
  Group /general/optophysiology/TargetImagingPlane/DummyOpticalChannel (OpticalChannel) 
  Group /general/optophysiology/TargetImagingPlane/device (Device) 
  source_script: Created using NeuroConv v0.6.1
  Group /general/subject (CElegansSubject) 
  identifier: 3fef7880-e8f5-466d-ba53-ef6afa75443c
  Group /intervals/OptogeneticStimulusTable (PatternedOptogeneticStimulusTable) Every 30 seconds, a random neuron was selected among the neurons found in the current volumetric image, on the basis of only its tagRFP-T signal. After galvo-mirrors and the tunable lens set the position of the two-photon spot on that neuron, a 500-ms (300-ms for the unc-31-mutant strain) train of light pulses was used to optogenetically stimulate that neuron. The duration of stimulus illumination for the unc-31-mutant strain was selected to elicit calcium transients in stimulated neurons with a distribution of amplitudes such that the maximum amplitude was similar to those in WT-background animals. The output of the laser was controlled through the external interface to its built-in pulse picker, and the power of the laser at the sample was 1.2mW at 500kHz. Neuron identities were assigned to stimulated neurons after the completion of experiments using NeuroPAL.
  Dataset /intervals/OptogeneticStimulusTable/id (ElementIdentifiers)  | shape = (85,) | dtype = int32
  Dataset /intervals/OptogeneticStimulusTable/power (VectorData) Power (in Watts) defined as a scalar. All rois in target receive the same photostimulation power. | shape = (85,) | dtype = float64
  Dataset /intervals/OptogeneticStimulusTable/start_time (VectorData) Start time of epoch, in seconds | shape = (85,) | dtype = float64
  Dataset /intervals/OptogeneticStimulusTable/stimulus_pattern (VectorData) Link to the stimulus pattern. | shape = (85,) | dtype = object
  Dataset /intervals/OptogeneticStimulusTable/stimulus_site (VectorData) Link to the stimulus site. | shape = (85,) | dtype = object
  Dataset /intervals/OptogeneticStimulusTable/stop_time (VectorData) Stop time of epoch, in seconds | shape = (85,) | dtype = float64
  Dataset /intervals/OptogeneticStimulusTable/target_pumpprobe_id (VectorData) Manually targeted ID in the PumpProbe space. Values are upcast to float to allow NaN; cast back to int to lookup correspond NeuroPAL label. | shape = (85,) | dtype = float64
  Dataset /intervals/OptogeneticStimulusTable/targets (VectorData) Targeted rois for the stimulus onset. | shape = (85,) | dtype = object
  Group /processing/ophys (ProcessingModule) Contains segmented imaging data.
  Group /processing/ophys/GreenSignals (MicroscopyResponseSeriesContainer) 
  Group /processing/ophys/GreenSignals/BaseGreenSignal (MicroscopyResponseSeries) Average baseline fluorescence for the 'Green' optical channel extracted from the raw imaging and averaged over a volume defined as a complete scan cycle over volumetric depths. This series includes NaNs for certain frame values that could not be inferred from the imaging data.
  Dataset /processing/ophys/GreenSignals/BaseGreenSignal/table_region (DynamicTableRegion)  | shape = (136,) | dtype = int32
  Group /processing/ophys/GreenSignals/InterpolatedGreenSignal (MicroscopyResponseSeries) Average baseline fluorescence for the 'Green' optical channel extracted from the raw imaging and averaged over a volume defined as a complete scan cycle over volumetric depths. This series has interpolated the NaN frames in the corresponding 'base' signal.
  Dataset /processing/ophys/GreenSignals/InterpolatedGreenSignal/table_region (DynamicTableRegion)  | shape = (136,) | dtype = int32
  Group /processing/ophys/NeuroPALSegmentations (MicroscopySegmentations) 
  Group /processing/ophys/NeuroPALSegmentations/NeuroPALPlaneSegmentation (MicroscopyPlaneSegmentation) The NeuroPAL segmentation of the C. elegans brain with cell labels.
  Dataset /processing/ophys/NeuroPALSegmentations/NeuroPALPlaneSegmentation/centroids (VectorData) The centroids of each ROI. | shape = (180, 3) | dtype = int32
  Dataset /processing/ophys/NeuroPALSegmentations/NeuroPALPlaneSegmentation/id (ElementIdentifiers)  | shape = (180,) | dtype = int32
  Group /processing/ophys/NeuroPALSegmentations/NeuroPALPlaneSegmentation/imaging_space (VolumetricImagingSpace) 
  Group /processing/ophys/NeuroPALSegmentations/NeuroPALPlaneSegmentation/imaging_space/microscope (Microscope) 
  Dataset /processing/ophys/NeuroPALSegmentations/NeuroPALPlaneSegmentation/labels (VectorData) The C. elegans cell names labeled from the NeuroPAL imaging. | shape = (180,) | dtype = object
  Dataset /processing/ophys/NeuroPALSegmentations/NeuroPALPlaneSegmentation/labels_comments (VectorData) Various comments about the cell label classification process. | shape = (180,) | dtype = object
  Dataset /processing/ophys/NeuroPALSegmentations/NeuroPALPlaneSegmentation/labels_confidences (VectorData) The C. elegans cell names labeled from the NeuroPAL imaging. | shape = (180,) | dtype = float64
  Dataset /processing/ophys/NeuroPALSegmentations/NeuroPALPlaneSegmentation/voxel_mask (VectorData) Voxel masks for each ROI: a list of indices and weights for the ROI. Voxel masks are concatenated and parsing of this dataset is maintained by the PlaneSegmentation | shape = (1620,) | dtype = [('x', '<u4'), ('y', '<u4'), ('z', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/NeuroPALSegmentations/NeuroPALPlaneSegmentation/voxel_mask_index (VectorIndex) Index for VectorData 'voxel_mask' | shape = (180,) | dtype = uint16
  Group /processing/ophys/PumpProbeGreenSegmentations (MicroscopySegmentations) 
  Group /processing/ophys/PumpProbeGreenSegmentations/PumpProbeGreenPlaneSegmentation (MicroscopyPlaneSegmentation) The PumpProbe segmentation of the C. elegans brain. Only some of these local ROI IDs match the NeuroPAL IDs with cell labels. Note that the Z-axis of the `voxel_mask` is in reference to the index of that depth in its scan cycle.
  Dataset /processing/ophys/PumpProbeGreenSegmentations/PumpProbeGreenPlaneSegmentation/centroids (VectorData) The centroids of each ROI. | shape = (136, 3) | dtype = int32
  Dataset /processing/ophys/PumpProbeGreenSegmentations/PumpProbeGreenPlaneSegmentation/id (ElementIdentifiers)  | shape = (136,) | dtype = int32
  Group /processing/ophys/PumpProbeGreenSegmentations/PumpProbeGreenPlaneSegmentation/imaging_space (PlanarImagingSpace) 
  Group /processing/ophys/PumpProbeGreenSegmentations/PumpProbeGreenPlaneSegmentation/imaging_space/microscope (Microscope) 
  Dataset /processing/ophys/PumpProbeGreenSegmentations/PumpProbeGreenPlaneSegmentation/neuropal_ids (VectorData) The NeuroPAL ROI ID that has been matched to this PumpProbe ID. Blank means the ROI was not matched. | shape = (136,) | dtype = object
  Dataset /processing/ophys/PumpProbeGreenSegmentations/PumpProbeGreenPlaneSegmentation/voxel_mask (VectorData) Voxel masks for each ROI: a list of indices and weights for the ROI. Voxel masks are concatenated and parsing of this dataset is maintained by the PlaneSegmentation | shape = (10200,) | dtype = [('x', '<u4'), ('y', '<u4'), ('z', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/PumpProbeGreenSegmentations/PumpProbeGreenPlaneSegmentation/voxel_mask_index (VectorIndex) Index for VectorData 'voxel_mask' | shape = (136,) | dtype = uint16
  Group /processing/ophys/PumpProbeRedSegmentations (MicroscopySegmentations) 
  Group /processing/ophys/PumpProbeRedSegmentations/PumpProbeRedPlaneSegmentation (MicroscopyPlaneSegmentation) The PumpProbe segmentation of the C. elegans brain. Only some of these local ROI IDs match the NeuroPAL IDs with cell labels. Note that the Z-axis of the `voxel_mask` is in reference to the index of that depth in its scan cycle.
  Dataset /processing/ophys/PumpProbeRedSegmentations/PumpProbeRedPlaneSegmentation/centroids (VectorData) The centroids of each ROI. | shape = (136, 3) | dtype = int32
  Dataset /processing/ophys/PumpProbeRedSegmentations/PumpProbeRedPlaneSegmentation/id (ElementIdentifiers)  | shape = (136,) | dtype = int32
  Group /processing/ophys/PumpProbeRedSegmentations/PumpProbeRedPlaneSegmentation/imaging_space (PlanarImagingSpace) 
  Group /processing/ophys/PumpProbeRedSegmentations/PumpProbeRedPlaneSegmentation/imaging_space/microscope (Microscope) 
  Dataset /processing/ophys/PumpProbeRedSegmentations/PumpProbeRedPlaneSegmentation/neuropal_ids (VectorData) The NeuroPAL ROI ID that has been matched to this PumpProbe ID. Blank means the ROI was not matched. | shape = (136,) | dtype = object
  Dataset /processing/ophys/PumpProbeRedSegmentations/PumpProbeRedPlaneSegmentation/voxel_mask (VectorData) Voxel masks for each ROI: a list of indices and weights for the ROI. Voxel masks are concatenated and parsing of this dataset is maintained by the PlaneSegmentation | shape = (10200,) | dtype = [('x', '<u4'), ('y', '<u4'), ('z', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/PumpProbeRedSegmentations/PumpProbeRedPlaneSegmentation/voxel_mask_index (VectorIndex) Index for VectorData 'voxel_mask' | shape = (136,) | dtype = uint16
  Group /processing/ophys/RedSignals (MicroscopyResponseSeriesContainer) 
  Group /processing/ophys/RedSignals/BaseRedSignal (MicroscopyResponseSeries) Average baseline fluorescence for the 'Red' optical channel extracted from the raw imaging and averaged over a volume defined as a complete scan cycle over volumetric depths. This series includes NaNs for certain frame values that could not be inferred from the imaging data.
  Dataset /processing/ophys/RedSignals/BaseRedSignal/table_region (DynamicTableRegion)  | shape = (136,) | dtype = int32
  Group /processing/ophys/RedSignals/InterpolatedRedSignal (MicroscopyResponseSeries) Average baseline fluorescence for the 'Red' optical channel extracted from the raw imaging and averaged over a volume defined as a complete scan cycle over volumetric depths. This series has interpolated the NaN frames in the corresponding 'base' signal.
  Dataset /processing/ophys/RedSignals/InterpolatedRedSignal/table_region (DynamicTableRegion)  | shape = (136,) | dtype = int32
  Group /processing/ophys/TargetedImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/TargetedImageSegmentation/TargetPlaneSegmentation (PlaneSegmentation) Table for storing the target centroids, defined by a one-voxel mask.
  Dataset /processing/ophys/TargetedImageSegmentation/TargetPlaneSegmentation/depth_in_um (VectorData) Targeted depth in micrometers. | shape = (85,) | dtype = float64
  Dataset /processing/ophys/TargetedImageSegmentation/TargetPlaneSegmentation/id (ElementIdentifiers)  | shape = (85,) | dtype = int32
  Group /processing/ophys/TargetedImageSegmentation/TargetPlaneSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys/TargetedImageSegmentation/TargetPlaneSegmentation/imaging_plane/DummyOpticalChannel (OpticalChannel) 
  Group /processing/ophys/TargetedImageSegmentation/TargetPlaneSegmentation/imaging_plane/device (Device) 
  Dataset /processing/ophys/TargetedImageSegmentation/TargetPlaneSegmentation/pixel_mask (VectorData) Pixel masks for each ROI | shape = (85,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/TargetedImageSegmentation/TargetPlaneSegmentation/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (85,) | dtype = uint8
  session_description: 
  session_start_time: 2021-08-24T11:49:40-04:00
  timestamps_reference_time: 2021-08-24T11:49:40-04:00


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2024-09-30T14:06:50.662204-04:00']
  Group /general/NeuroPALImagingSpace (VolumetricImagingSpace) 
  Group /general/NeuroPALImagingSpace/microscope (Microscope) 
  Group /general/OptogeneticStimulusTarget0 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget0/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget1 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget1/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget10 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget10/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget11 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget11/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget12 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget12/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget13 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget13/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget14 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget14/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget15 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget15/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget16 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget16/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget17 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget17/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget18 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget18/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget19 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget19/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget2 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget2/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget20 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget20/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget21 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget21/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget22 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget22/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget23 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget23/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget24 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget24/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget25 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget25/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget26 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget26/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget27 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget27/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget28 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget28/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget29 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget29/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget3 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget3/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget30 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget30/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget31 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget31/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget32 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget32/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget33 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget33/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget34 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget34/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget35 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget35/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget36 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget36/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget37 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget37/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget38 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget38/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget39 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget39/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget4 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget4/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget40 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget40/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget41 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget41/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget42 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget42/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget43 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget43/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget44 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget44/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget45 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget45/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget46 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget46/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget47 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget47/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget48 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget48/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget49 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget49/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget5 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget5/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget50 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget50/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget51 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget51/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget52 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget52/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget53 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget53/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget54 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget54/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget55 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget55/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget56 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget56/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget57 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget57/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget58 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget58/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget59 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget59/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget6 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget6/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget7 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget7/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget8 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget8/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget9 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget9/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/PumpProbeImagingSpace (PlanarImagingSpace) 
  Group /general/PumpProbeImagingSpace/microscope (Microscope) 
  Group /general/TemporalFocusing (TemporalFocusing) We used temporal focusing to spatially restrict the size of the two-photon excitation spot along the microscope axis. A motorized iris was used to set its lateral size. For temporal focusing, the first-order diffraction from a reflective grating, oriented orthogonally to the microscope axis, was collected and travelled through the motorized iris, placed on a plane conjugate to the grating.To arbitrarily position the two-photon excitation spot in the sample volume, the beam then travelled through an electrically tunable lens (Optotune EL-16-40-TC, on a plane conjugate to the objective), to set its position along the microscope axis, and finally was reflected by two galvo-mirrors to set its lateral position. The pulsed beam was then combined with the imaging light path by a dichroic mirror immediately before entering the back of the objective.
  Group /general/devices/AmplifiedLaser (LightSource) For two-photon optogenetic targeting, we used an optical parametric amplifier (OPA; Light Conversion ORPHEUS) pumped by a femtosecond amplified laser (Light Conversion PHAROS).
  Group /general/devices/Microscope (Microscope) 
  Group /general/devices/OptogeneticDevice (Device) 
  experiment_description: 
      To measure signal propagation, we activated each single neuron, one at a time, through two-photon stimulation,
      while simultaneously recording the calcium activity of the population at cellular resolution using spinning disk
      confocal microscopy. We recorded activity from 113 wild-type (WT)-background animals, each for up to 40min, while
      stimulating a mostly randomly selected sequence of neurons one by one every 30s. We spatially restricted our
      two-photon activation in three dimensions to be the size of a typical C. elegans neuron, to minimize off-target
      activation of neighbouring neurons. Animals were immobilized but awake,and pharyngeal pumping was visible during
      recordings.
      
  experimenter: ['Randi, Francesco']
  institution: Princeton University
  keywords: ['C. elegans' 'optogenetics' 'functional connectivity']
  lab: Leifer Lab
  Group /general/optogenetics/PatternedOptogeneticStimulusSite (PatternedOptogeneticStimulusSite) 
  Group /general/optogenetics/PatternedOptogeneticStimulusSite/device (Device) 
  Group /general/optogenetics/PatternedOptogeneticStimulusSite/light_source (LightSource) For two-photon optogenetic targeting, we used an optical parametric amplifier (OPA; Light Conversion ORPHEUS) pumped by a femtosecond amplified laser (Light Conversion PHAROS).
  Group /general/optophysiology/TargetImagingPlane (ImagingPlane) 
  Group /general/optophysiology/TargetImagingPlane/DummyOpticalChannel (OpticalChannel) 
  Group /general/optophysiology/TargetImagingPlane/device (Device) 
  source_script: Created using NeuroConv v0.6.1
  Group /general/subject (CElegansSubject) 
  identifier: c24e10af-e2f1-4162-9c60-79322b683b8f
  Group /intervals/OptogeneticStimulusTable (PatternedOptogeneticStimulusTable) Every 30 seconds, a random neuron was selected among the neurons found in the current volumetric image, on the basis of only its tagRFP-T signal. After galvo-mirrors and the tunable lens set the position of the two-photon spot on that neuron, a 500-ms (300-ms for the unc-31-mutant strain) train of light pulses was used to optogenetically stimulate that neuron. The duration of stimulus illumination for the unc-31-mutant strain was selected to elicit calcium transients in stimulated neurons with a distribution of amplitudes such that the maximum amplitude was similar to those in WT-background animals. The output of the laser was controlled through the external interface to its built-in pulse picker, and the power of the laser at the sample was 1.2mW at 500kHz. Neuron identities were assigned to stimulated neurons after the completion of experiments using NeuroPAL.
  Dataset /intervals/OptogeneticStimulusTable/id (ElementIdentifiers)  | shape = (60,) | dtype = int32
  Dataset /intervals/OptogeneticStimulusTable/power (VectorData) Power (in Watts) defined as a scalar. All rois in target receive the same photostimulation power. | shape = (60,) | dtype = float64
  Dataset /intervals/OptogeneticStimulusTable/start_time (VectorData) Start time of epoch, in seconds | shape = (60,) | dtype = float64
  Dataset /intervals/OptogeneticStimulusTable/stimulus_pattern (VectorData) Link to the stimulus pattern. | shape = (60,) | dtype = object
  Dataset /intervals/OptogeneticStimulusTable/stimulus_site (VectorData) Link to the stimulus site. | shape = (60,) | dtype = object
  Dataset /intervals/OptogeneticStimulusTable/stop_time (VectorData) Stop time of epoch, in seconds | shape = (60,) | dtype = float64
  Dataset /intervals/OptogeneticStimulusTable/target_pumpprobe_id (VectorData) Manually targeted ID in the PumpProbe space. Values are upcast to float to allow NaN; cast back to int to lookup correspond NeuroPAL label. | shape = (60,) | dtype = float64
  Dataset /intervals/OptogeneticStimulusTable/targets (VectorData) Targeted rois for the stimulus onset. | shape = (60,) | dtype = object
  Group /processing/ophys (ProcessingModule) Contains segmented imaging data.
  Group /processing/ophys/GreenSignals (MicroscopyResponseSeriesContainer) 
  Group /processing/ophys/GreenSignals/BaseGreenSignal (MicroscopyResponseSeries) Average baseline fluorescence for the 'Green' optical channel extracted from the raw imaging and averaged over a volume defined as a complete scan cycle over volumetric depths. This series includes NaNs for certain frame values that could not be inferred from the imaging data.
  Dataset /processing/ophys/GreenSignals/BaseGreenSignal/table_region (DynamicTableRegion)  | shape = (136,) | dtype = int32
  Group /processing/ophys/GreenSignals/InterpolatedGreenSignal (MicroscopyResponseSeries) Average baseline fluorescence for the 'Green' optical channel extracted from the raw imaging and averaged over a volume defined as a complete scan cycle over volumetric depths. This series has interpolated the NaN frames in the corresponding 'base' signal.
  Dataset /processing/ophys/GreenSignals/InterpolatedGreenSignal/table_region (DynamicTableRegion)  | shape = (136,) | dtype = int32
  Group /processing/ophys/NeuroPALSegmentations (MicroscopySegmentations) 
  Group /processing/ophys/NeuroPALSegmentations/NeuroPALPlaneSegmentation (MicroscopyPlaneSegmentation) The NeuroPAL segmentation of the C. elegans brain with cell labels.
  Dataset /processing/ophys/NeuroPALSegmentations/NeuroPALPlaneSegmentation/centroids (VectorData) The centroids of each ROI. | shape = (164, 3) | dtype = int32
  Dataset /processing/ophys/NeuroPALSegmentations/NeuroPALPlaneSegmentation/id (ElementIdentifiers)  | shape = (164,) | dtype = int32
  Group /processing/ophys/NeuroPALSegmentations/NeuroPALPlaneSegmentation/imaging_space (VolumetricImagingSpace) 
  Group /processing/ophys/NeuroPALSegmentations/NeuroPALPlaneSegmentation/imaging_space/microscope (Microscope) 
  Dataset /processing/ophys/NeuroPALSegmentations/NeuroPALPlaneSegmentation/labels (VectorData) The C. elegans cell names labeled from the NeuroPAL imaging. | shape = (164,) | dtype = object
  Dataset /processing/ophys/NeuroPALSegmentations/NeuroPALPlaneSegmentation/labels_comments (VectorData) Various comments about the cell label classification process. | shape = (164,) | dtype = object
  Dataset /processing/ophys/NeuroPALSegmentations/NeuroPALPlaneSegmentation/labels_confidences (VectorData) The C. elegans cell names labeled from the NeuroPAL imaging. | shape = (164,) | dtype = float64
  Dataset /processing/ophys/NeuroPALSegmentations/NeuroPALPlaneSegmentation/voxel_mask (VectorData) Voxel masks for each ROI: a list of indices and weights for the ROI. Voxel masks are concatenated and parsing of this dataset is maintained by the PlaneSegmentation | shape = (1476,) | dtype = [('x', '<u4'), ('y', '<u4'), ('z', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/NeuroPALSegmentations/NeuroPALPlaneSegmentation/voxel_mask_index (VectorIndex) Index for VectorData 'voxel_mask' | shape = (164,) | dtype = uint16
  Group /processing/ophys/PumpProbeGreenSegmentations (MicroscopySegmentations) 
  Group /processing/ophys/PumpProbeGreenSegmentations/PumpProbeGreenPlaneSegmentation (MicroscopyPlaneSegmentation) The PumpProbe segmentation of the C. elegans brain. Only some of these local ROI IDs match the NeuroPAL IDs with cell labels. Note that the Z-axis of the `voxel_mask` is in reference to the index of that depth in its scan cycle.
  Dataset /processing/ophys/PumpProbeGreenSegmentations/PumpProbeGreenPlaneSegmentation/centroids (VectorData) The centroids of each ROI. | shape = (136, 3) | dtype = int32
  Dataset /processing/ophys/PumpProbeGreenSegmentations/PumpProbeGreenPlaneSegmentation/id (ElementIdentifiers)  | shape = (136,) | dtype = int32
  Group /processing/ophys/PumpProbeGreenSegmentations/PumpProbeGreenPlaneSegmentation/imaging_space (PlanarImagingSpace) 
  Group /processing/ophys/PumpProbeGreenSegmentations/PumpProbeGreenPlaneSegmentation/imaging_space/microscope (Microscope) 
  Dataset /processing/ophys/PumpProbeGreenSegmentations/PumpProbeGreenPlaneSegmentation/neuropal_ids (VectorData) The NeuroPAL ROI ID that has been matched to this PumpProbe ID. Blank means the ROI was not matched. | shape = (136,) | dtype = object
  Dataset /processing/ophys/PumpProbeGreenSegmentations/PumpProbeGreenPlaneSegmentation/voxel_mask (VectorData) Voxel masks for each ROI: a list of indices and weights for the ROI. Voxel masks are concatenated and parsing of this dataset is maintained by the PlaneSegmentation | shape = (10200,) | dtype = [('x', '<u4'), ('y', '<u4'), ('z', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/PumpProbeGreenSegmentations/PumpProbeGreenPlaneSegmentation/voxel_mask_index (VectorIndex) Index for VectorData 'voxel_mask' | shape = (136,) | dtype = uint16
  Group /processing/ophys/PumpProbeRedSegmentations (MicroscopySegmentations) 
  Group /processing/ophys/PumpProbeRedSegmentations/PumpProbeRedPlaneSegmentation (MicroscopyPlaneSegmentation) The PumpProbe segmentation of the C. elegans brain. Only some of these local ROI IDs match the NeuroPAL IDs with cell labels. Note that the Z-axis of the `voxel_mask` is in reference to the index of that depth in its scan cycle.
  Dataset /processing/ophys/PumpProbeRedSegmentations/PumpProbeRedPlaneSegmentation/centroids (VectorData) The centroids of each ROI. | shape = (136, 3) | dtype = int32
  Dataset /processing/ophys/PumpProbeRedSegmentations/PumpProbeRedPlaneSegmentation/id (ElementIdentifiers)  | shape = (136,) | dtype = int32
  Group /processing/ophys/PumpProbeRedSegmentations/PumpProbeRedPlaneSegmentation/imaging_space (PlanarImagingSpace) 
  Group /processing/ophys/PumpProbeRedSegmentations/PumpProbeRedPlaneSegmentation/imaging_space/microscope (Microscope) 
  Dataset /processing/ophys/PumpProbeRedSegmentations/PumpProbeRedPlaneSegmentation/neuropal_ids (VectorData) The NeuroPAL ROI ID that has been matched to this PumpProbe ID. Blank means the ROI was not matched. | shape = (136,) | dtype = object
  Dataset /processing/ophys/PumpProbeRedSegmentations/PumpProbeRedPlaneSegmentation/voxel_mask (VectorData) Voxel masks for each ROI: a list of indices and weights for the ROI. Voxel masks are concatenated and parsing of this dataset is maintained by the PlaneSegmentation | shape = (10200,) | dtype = [('x', '<u4'), ('y', '<u4'), ('z', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/PumpProbeRedSegmentations/PumpProbeRedPlaneSegmentation/voxel_mask_index (VectorIndex) Index for VectorData 'voxel_mask' | shape = (136,) | dtype = uint16
  Group /processing/ophys/RedSignals (MicroscopyResponseSeriesContainer) 
  Group /processing/ophys/RedSignals/BaseRedSignal (MicroscopyResponseSeries) Average baseline fluorescence for the 'Red' optical channel extracted from the raw imaging and averaged over a volume defined as a complete scan cycle over volumetric depths. This series includes NaNs for certain frame values that could not be inferred from the imaging data.
  Dataset /processing/ophys/RedSignals/BaseRedSignal/table_region (DynamicTableRegion)  | shape = (136,) | dtype = int32
  Group /processing/ophys/RedSignals/InterpolatedRedSignal (MicroscopyResponseSeries) Average baseline fluorescence for the 'Red' optical channel extracted from the raw imaging and averaged over a volume defined as a complete scan cycle over volumetric depths. This series has interpolated the NaN frames in the corresponding 'base' signal.
  Dataset /processing/ophys/RedSignals/InterpolatedRedSignal/table_region (DynamicTableRegion)  | shape = (136,) | dtype = int32
  Group /processing/ophys/TargetedImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/TargetedImageSegmentation/TargetPlaneSegmentation (PlaneSegmentation) Table for storing the target centroids, defined by a one-voxel mask.
  Dataset /processing/ophys/TargetedImageSegmentation/TargetPlaneSegmentation/depth_in_um (VectorData) Targeted depth in micrometers. | shape = (60,) | dtype = float64
  Dataset /processing/ophys/TargetedImageSegmentation/TargetPlaneSegmentation/id (ElementIdentifiers)  | shape = (60,) | dtype = int32
  Group /processing/ophys/TargetedImageSegmentation/TargetPlaneSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys/TargetedImageSegmentation/TargetPlaneSegmentation/imaging_plane/DummyOpticalChannel (OpticalChannel) 
  Group /processing/ophys/TargetedImageSegmentation/TargetPlaneSegmentation/imaging_plane/device (Device) 
  Dataset /processing/ophys/TargetedImageSegmentation/TargetPlaneSegmentation/pixel_mask (VectorData) Pixel masks for each ROI | shape = (60,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/TargetedImageSegmentation/TargetPlaneSegmentation/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (60,) | dtype = uint8
  session_description: 
  session_start_time: 2021-08-30T14:41:55-04:00
  timestamps_reference_time: 2021-08-30T14:41:55-04:00


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2024-09-30T14:15:11.702613-04:00']
  Group /general/NeuroPALImagingSpace (VolumetricImagingSpace) 
  Group /general/NeuroPALImagingSpace/microscope (Microscope) 
  Group /general/OptogeneticStimulusTarget0 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget0/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget1 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget1/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget10 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget10/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget11 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget11/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget12 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget12/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget13 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget13/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget14 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget14/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget15 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget15/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget16 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget16/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget17 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget17/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget18 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget18/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget19 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget19/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget2 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget2/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget20 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget20/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget21 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget21/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget22 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget22/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget23 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget23/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget24 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget24/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget25 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget25/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget26 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget26/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget27 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget27/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget28 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget28/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget29 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget29/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget3 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget3/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget30 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget30/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget31 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget31/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget32 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget32/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget33 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget33/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget34 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget34/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget35 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget35/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget36 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget36/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget37 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget37/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget38 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget38/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget39 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget39/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget4 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget4/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget40 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget40/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget41 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget41/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget42 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget42/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget5 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget5/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget6 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget6/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget7 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget7/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget8 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget8/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/OptogeneticStimulusTarget9 (OptogeneticStimulusTarget) 
  Dataset /general/OptogeneticStimulusTarget9/targeted_rois (DynamicTableRegion) The targeted ROI. | shape = (1,) | dtype = int32
  Group /general/PumpProbeImagingSpace (PlanarImagingSpace) 
  Group /general/PumpProbeImagingSpace/microscope (Microscope) 
  Group /general/TemporalFocusing (TemporalFocusing) We used temporal focusing to spatially restrict the size of the two-photon excitation spot along the microscope axis. A motorized iris was used to set its lateral size. For temporal focusing, the first-order diffraction from a reflective grating, oriented orthogonally to the microscope axis, was collected and travelled through the motorized iris, placed on a plane conjugate to the grating.To arbitrarily position the two-photon excitation spot in the sample volume, the beam then travelled through an electrically tunable lens (Optotune EL-16-40-TC, on a plane conjugate to the objective), to set its position along the microscope axis, and finally was reflected by two galvo-mirrors to set its lateral position. The pulsed beam was then combined with the imaging light path by a dichroic mirror immediately before entering the back of the objective.
  Group /general/devices/AmplifiedLaser (LightSource) For two-photon optogenetic targeting, we used an optical parametric amplifier (OPA; Light Conversion ORPHEUS) pumped by a femtosecond amplified laser (Light Conversion PHAROS).
  Group /general/devices/Microscope (Microscope) 
  Group /general/devices/OptogeneticDevice (Device) 
  experiment_description: 
      To measure signal propagation, we activated each single neuron, one at a time, through two-photon stimulation,
      while simultaneously recording the calcium activity of the population at cellular resolution using spinning disk
      confocal microscopy. We recorded activity from 113 wild-type (WT)-background animals, each for up to 40min, while
      stimulating a mostly randomly selected sequence of neurons one by one every 30s. We spatially restricted our
      two-photon activation in three dimensions to be the size of a typical C. elegans neuron, to minimize off-target
      activation of neighbouring neurons. Animals were immobilized but awake,and pharyngeal pumping was visible during
      recordings.
      
  experimenter: ['Randi, Francesco']
  institution: Princeton University
  keywords: ['C. elegans' 'optogenetics' 'functional connectivity']
  lab: Leifer Lab
  Group /general/optogenetics/PatternedOptogeneticStimulusSite (PatternedOptogeneticStimulusSite) 
  Group /general/optogenetics/PatternedOptogeneticStimulusSite/device (Device) 
  Group /general/optogenetics/PatternedOptogeneticStimulusSite/light_source (LightSource) For two-photon optogenetic targeting, we used an optical parametric amplifier (OPA; Light Conversion ORPHEUS) pumped by a femtosecond amplified laser (Light Conversion PHAROS).
  Group /general/optophysiology/TargetImagingPlane (ImagingPlane) 
  Group /general/optophysiology/TargetImagingPlane/DummyOpticalChannel (OpticalChannel) 
  Group /general/optophysiology/TargetImagingPlane/device (Device) 
  source_script: Created using NeuroConv v0.6.1
  Group /general/subject (CElegansSubject) 
  identifier: 3b8d0234-c3d4-48fa-8daf-799856bbe5da
  Group /intervals/OptogeneticStimulusTable (PatternedOptogeneticStimulusTable) Every 30 seconds, a random neuron was selected among the neurons found in the current volumetric image, on the basis of only its tagRFP-T signal. After galvo-mirrors and the tunable lens set the position of the two-photon spot on that neuron, a 500-ms (300-ms for the unc-31-mutant strain) train of light pulses was used to optogenetically stimulate that neuron. The duration of stimulus illumination for the unc-31-mutant strain was selected to elicit calcium transients in stimulated neurons with a distribution of amplitudes such that the maximum amplitude was similar to those in WT-background animals. The output of the laser was controlled through the external interface to its built-in pulse picker, and the power of the laser at the sample was 1.2mW at 500kHz. Neuron identities were assigned to stimulated neurons after the completion of experiments using NeuroPAL.
  Dataset /intervals/OptogeneticStimulusTable/id (ElementIdentifiers)  | shape = (43,) | dtype = int32
  Dataset /intervals/OptogeneticStimulusTable/power (VectorData) Power (in Watts) defined as a scalar. All rois in target receive the same photostimulation power. | shape = (43,) | dtype = float64
  Dataset /intervals/OptogeneticStimulusTable/start_time (VectorData) Start time of epoch, in seconds | shape = (43,) | dtype = float64
  Dataset /intervals/OptogeneticStimulusTable/stimulus_pattern (VectorData) Link to the stimulus pattern. | shape = (43,) | dtype = object
  Dataset /intervals/OptogeneticStimulusTable/stimulus_site (VectorData) Link to the stimulus site. | shape = (43,) | dtype = object
  Dataset /intervals/OptogeneticStimulusTable/stop_time (VectorData) Stop time of epoch, in seconds | shape = (43,) | dtype = float64
  Dataset /intervals/OptogeneticStimulusTable/target_pumpprobe_id (VectorData) Manually targeted ID in the PumpProbe space. Values are upcast to float to allow NaN; cast back to int to lookup correspond NeuroPAL label. | shape = (43,) | dtype = float64
  Dataset /intervals/OptogeneticStimulusTable/targets (VectorData) Targeted rois for the stimulus onset. | shape = (43,) | dtype = object
  Group /processing/ophys (ProcessingModule) Contains segmented imaging data.
  Group /processing/ophys/GreenSignals (MicroscopyResponseSeriesContainer) 
  Group /processing/ophys/GreenSignals/BaseGreenSignal (MicroscopyResponseSeries) Average baseline fluorescence for the 'Green' optical channel extracted from the raw imaging and averaged over a volume defined as a complete scan cycle over volumetric depths. This series includes NaNs for certain frame values that could not be inferred from the imaging data.
  Dataset /processing/ophys/GreenSignals/BaseGreenSignal/table_region (DynamicTableRegion)  | shape = (122,) | dtype = int32
  Group /processing/ophys/GreenSignals/InterpolatedGreenSignal (MicroscopyResponseSeries) Average baseline fluorescence for the 'Green' optical channel extracted from the raw imaging and averaged over a volume defined as a complete scan cycle over volumetric depths. This series has interpolated the NaN frames in the corresponding 'base' signal.
  Dataset /processing/ophys/GreenSignals/InterpolatedGreenSignal/table_region (DynamicTableRegion)  | shape = (122,) | dtype = int32
  Group /processing/ophys/NeuroPALSegmentations (MicroscopySegmentations) 
  Group /processing/ophys/NeuroPALSegmentations/NeuroPALPlaneSegmentation (MicroscopyPlaneSegmentation) The NeuroPAL segmentation of the C. elegans brain with cell labels.
  Dataset /processing/ophys/NeuroPALSegmentations/NeuroPALPlaneSegmentation/centroids (VectorData) The centroids of each ROI. | shape = (147, 3) | dtype = int32
  Dataset /processing/ophys/NeuroPALSegmentations/NeuroPALPlaneSegmentation/id (ElementIdentifiers)  | shape = (147,) | dtype = int32
  Group /processing/ophys/NeuroPALSegmentations/NeuroPALPlaneSegmentation/imaging_space (VolumetricImagingSpace) 
  Group /processing/ophys/NeuroPALSegmentations/NeuroPALPlaneSegmentation/imaging_space/microscope (Microscope) 
  Dataset /processing/ophys/NeuroPALSegmentations/NeuroPALPlaneSegmentation/labels (VectorData) The C. elegans cell names labeled from the NeuroPAL imaging. | shape = (147,) | dtype = object
  Dataset /processing/ophys/NeuroPALSegmentations/NeuroPALPlaneSegmentation/labels_comments (VectorData) Various comments about the cell label classification process. | shape = (147,) | dtype = object
  Dataset /processing/ophys/NeuroPALSegmentations/NeuroPALPlaneSegmentation/labels_confidences (VectorData) The C. elegans cell names labeled from the NeuroPAL imaging. | shape = (147,) | dtype = float64
  Dataset /processing/ophys/NeuroPALSegmentations/NeuroPALPlaneSegmentation/voxel_mask (VectorData) Voxel masks for each ROI: a list of indices and weights for the ROI. Voxel masks are concatenated and parsing of this dataset is maintained by the PlaneSegmentation | shape = (1323,) | dtype = [('x', '<u4'), ('y', '<u4'), ('z', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/NeuroPALSegmentations/NeuroPALPlaneSegmentation/voxel_mask_index (VectorIndex) Index for VectorData 'voxel_mask' | shape = (147,) | dtype = uint16
  Group /processing/ophys/PumpProbeGreenSegmentations (MicroscopySegmentations) 
  Group /processing/ophys/PumpProbeGreenSegmentations/PumpProbeGreenPlaneSegmentation (MicroscopyPlaneSegmentation) The PumpProbe segmentation of the C. elegans brain. Only some of these local ROI IDs match the NeuroPAL IDs with cell labels. Note that the Z-axis of the `voxel_mask` is in reference to the index of that depth in its scan cycle.
  Dataset /processing/ophys/PumpProbeGreenSegmentations/PumpProbeGreenPlaneSegmentation/centroids (VectorData) The centroids of each ROI. | shape = (122, 3) | dtype = int32
  Dataset /processing/ophys/PumpProbeGreenSegmentations/PumpProbeGreenPlaneSegmentation/id (ElementIdentifiers)  | shape = (122,) | dtype = int32
  Group /processing/ophys/PumpProbeGreenSegmentations/PumpProbeGreenPlaneSegmentation/imaging_space (PlanarImagingSpace) 
  Group /processing/ophys/PumpProbeGreenSegmentations/PumpProbeGreenPlaneSegmentation/imaging_space/microscope (Microscope) 
  Dataset /processing/ophys/PumpProbeGreenSegmentations/PumpProbeGreenPlaneSegmentation/neuropal_ids (VectorData) The NeuroPAL ROI ID that has been matched to this PumpProbe ID. Blank means the ROI was not matched. | shape = (122,) | dtype = object
  Dataset /processing/ophys/PumpProbeGreenSegmentations/PumpProbeGreenPlaneSegmentation/voxel_mask (VectorData) Voxel masks for each ROI: a list of indices and weights for the ROI. Voxel masks are concatenated and parsing of this dataset is maintained by the PlaneSegmentation | shape = (9150,) | dtype = [('x', '<u4'), ('y', '<u4'), ('z', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/PumpProbeGreenSegmentations/PumpProbeGreenPlaneSegmentation/voxel_mask_index (VectorIndex) Index for VectorData 'voxel_mask' | shape = (122,) | dtype = uint16
  Group /processing/ophys/PumpProbeRedSegmentations (MicroscopySegmentations) 
  Group /processing/ophys/PumpProbeRedSegmentations/PumpProbeRedPlaneSegmentation (MicroscopyPlaneSegmentation) The PumpProbe segmentation of the C. elegans brain. Only some of these local ROI IDs match the NeuroPAL IDs with cell labels. Note that the Z-axis of the `voxel_mask` is in reference to the index of that depth in its scan cycle.
  Dataset /processing/ophys/PumpProbeRedSegmentations/PumpProbeRedPlaneSegmentation/centroids (VectorData) The centroids of each ROI. | shape = (122, 3) | dtype = int32
  Dataset /processing/ophys/PumpProbeRedSegmentations/PumpProbeRedPlaneSegmentation/id (ElementIdentifiers)  | shape = (122,) | dtype = int32
  Group /processing/ophys/PumpProbeRedSegmentations/PumpProbeRedPlaneSegmentation/imaging_space (PlanarImagingSpace) 
  Group /processing/ophys/PumpProbeRedSegmentations/PumpProbeRedPlaneSegmentation/imaging_space/microscope (Microscope) 
  Dataset /processing/ophys/PumpProbeRedSegmentations/PumpProbeRedPlaneSegmentation/neuropal_ids (VectorData) The NeuroPAL ROI ID that has been matched to this PumpProbe ID. Blank means the ROI was not matched. | shape = (122,) | dtype = object
  Dataset /processing/ophys/PumpProbeRedSegmentations/PumpProbeRedPlaneSegmentation/voxel_mask (VectorData) Voxel masks for each ROI: a list of indices and weights for the ROI. Voxel masks are concatenated and parsing of this dataset is maintained by the PlaneSegmentation | shape = (9150,) | dtype = [('x', '<u4'), ('y', '<u4'), ('z', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/PumpProbeRedSegmentations/PumpProbeRedPlaneSegmentation/voxel_mask_index (VectorIndex) Index for VectorData 'voxel_mask' | shape = (122,) | dtype = uint16
  Group /processing/ophys/RedSignals (MicroscopyResponseSeriesContainer) 
  Group /processing/ophys/RedSignals/BaseRedSignal (MicroscopyResponseSeries) Average baseline fluorescence for the 'Red' optical channel extracted from the raw imaging and averaged over a volume defined as a complete scan cycle over volumetric depths. This series includes NaNs for certain frame values that could not be inferred from the imaging data.
  Dataset /processing/ophys/RedSignals/BaseRedSignal/table_region (DynamicTableRegion)  | shape = (122,) | dtype = int32
  Group /processing/ophys/RedSignals/InterpolatedRedSignal (MicroscopyResponseSeries) Average baseline fluorescence for the 'Red' optical channel extracted from the raw imaging and averaged over a volume defined as a complete scan cycle over volumetric depths. This series has interpolated the NaN frames in the corresponding 'base' signal.
  Dataset /processing/ophys/RedSignals/InterpolatedRedSignal/table_region (DynamicTableRegion)  | shape = (122,) | dtype = int32
  Group /processing/ophys/TargetedImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/TargetedImageSegmentation/TargetPlaneSegmentation (PlaneSegmentation) Table for storing the target centroids, defined by a one-voxel mask.
  Dataset /processing/ophys/TargetedImageSegmentation/TargetPlaneSegmentation/depth_in_um (VectorData) Targeted depth in micrometers. | shape = (43,) | dtype = float64
  Dataset /processing/ophys/TargetedImageSegmentation/TargetPlaneSegmentation/id (ElementIdentifiers)  | shape = (43,) | dtype = int32
  Group /processing/ophys/TargetedImageSegmentation/TargetPlaneSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys/TargetedImageSegmentation/TargetPlaneSegmentation/imaging_plane/DummyOpticalChannel (OpticalChannel) 
  Group /processing/ophys/TargetedImageSegmentation/TargetPlaneSegmentation/imaging_plane/device (Device) 
  Dataset /processing/ophys/TargetedImageSegmentation/TargetPlaneSegmentation/pixel_mask (VectorData) Pixel masks for each ROI | shape = (43,) | dtype = [('x', '<u4'), ('y', '<u4'), ('weight', '<f4')]
  Dataset /processing/ophys/TargetedImageSegmentation/TargetPlaneSegmentation/pixel_mask_index (VectorIndex) Index for VectorData 'pixel_mask' | shape = (43,) | dtype = uint8
  session_description: 
  session_start_time: 2023-03-17T12:48:58-04:00
  timestamps_reference_time: 2023-03-17T12:48:58-04:00
