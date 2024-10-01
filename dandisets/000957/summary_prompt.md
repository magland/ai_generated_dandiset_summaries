
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000957/0.240731.0249
name: Neuropixels Ultra Probe Imposed Motion Dataset
contributor: [{'name': 'Ye, Zhiwen', 'email': 'yezhiwen@uw.edu', 'roleName': ['dcite:ContactPerson', 'dcite:DataCollector'], 'schemaKey': 'Person', 'identifier': '0000-0003-4311-1037', 'affiliation': [{'name': 'University of Washington', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/00cvxb145'}], 'includeInCitation': True}, {'name': 'Shaker, Jordan', 'email': 'jshaker@uw.edu', 'roleName': ['dcite:DataCollector'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Steinmetz, Nicholas', 'email': 'nick.steinmetz@gmail.com', 'roleName': ['dcite:ProjectManager'], 'schemaKey': 'Person', 'identifier': '0000-0001-7029-2908', 'includeInCitation': True}, {'name': 'NIH', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01cwqze88', 'awardNumber': 'NIH BRAIN Initiative (U01NS113252)', 'includeInCitation': False}]
description: Neuropixels Ultra Probe Imposed Motion Dataset provides a dataset, where neural activity was recorded with Neuropixels Ultra (NP Ultra) in awake mouse visual cortex.  NP Ultra probe measures neural activity at ultra-high density, with 6-micron center-to-center spacing between sites, in 8x48 site configuration (total width x length: 48 x 288 micron). 

Probe up-down motion was artificially imposed in the brain tissue during brain recording. A total of 10 steps forward and 9 alternating steps
backwards were imposed for each session, with 25 μm travel in each direction at 1 μm/sec speed. This results in 25 micron net displacement by the end of the imposed motion.

118 natural images were presented at random times with repetition before and after imposed motion, for "fingerprinting" the identities of the visual cortical neurons with their unique visual responses.

This dataset provides an opportunity for designing and testing spike sorting algorithms, with neural activity sampled at an unprecedented spatiotemporal resolution.(1) Manually imposed motion and (2)neural identification with visual responses pre- and post- motion provide ground truth reference for testing the accuracy of motion correction and spike sorting.
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 530955950647, 'numberOfFiles': 10, 'numberOfSubjects': 5, 'variableMeasured': ['ElectrodeGroup', 'ElectricalSeries'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000957 has 10 NWB files.
4 of these NWB files are of type 1.
6 of these NWB files are of type 2.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeriesAP (ElectricalSeries) Acquisition traces for the ElectricalSeriesAP.
  Dataset /acquisition/ElectricalSeriesAP/electrodes (DynamicTableRegion) electrode_table_region | shape = (384,) | dtype = int32
  Group /acquisition/ElectricalSeriesLF (ElectricalSeries) Acquisition traces for the ElectricalSeriesLF.
  Dataset /acquisition/ElectricalSeriesLF/electrodes (DynamicTableRegion) electrode_table_region | shape = (384,) | dtype = int32
  Group /acquisition/manipulator_trigger (TimeSeries) analog signal of manipulator up and down motion
  file_create_date: ['2024-04-03T00:12:47.375679-07:00']
  Group /general/devices/Neuropixel-Imec (Device) {"probe_type": "0", "probe_type_description": "NP1.0", "flex_part_number": "NP2_FLEX_0", "connected_base_station_part_number": "NP2_QBSC_00"}
  experiment_description: Imposed motion in V1
  experimenter: ['Ye, Zhiwen']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/channel_name (VectorData) no description | shape = (768,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/contact_shapes (VectorData) The shape of the electrode | shape = (768,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/gain_to_uV (VectorData) no description | shape = (768,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (768,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (768,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (768,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/inter_sample_shift (VectorData) no description | shape = (768,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (768,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/offset_to_uV (VectorData) no description | shape = (768,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_x (VectorData) rel_x | shape = (768,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_y (VectorData) rel_y | shape = (768,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/shank_electrode_number (VectorData) 0-indexed channel within a shank. | shape = (768,) | dtype = float64
  Group /general/extracellular_ephys/s0 (ElectrodeGroup) a group representing shank s0
  Group /general/extracellular_ephys/s0/device (Device) {"probe_type": "0", "probe_type_description": "NP1.0", "flex_part_number": "NP2_FLEX_0", "connected_base_station_part_number": "NP2_QBSC_00"}
  institution: University of Washington
  keywords: ['Neuropixels ultra, imposed motion']
  lab: Steinmetz lab
  related_publications: ['https://doi.org/10.1101/2023.08.23.554527']
  session_id: 1
  Group /general/subject (Subject) 
  identifier: f31247d5-e368-42db-acdf-c1543144d880
  session_description: Auto-generated by neuroconv
  session_start_time: 2021-05-01T15:44:27-07:00
  Group /stimulus/presentation/post_motion_stim_duration (TimeSeries) stimulus duration (s), stimulus timestamps (s) in timestamps field
  Group /stimulus/presentation/post_motion_stim_index (IndexSeries) no description
  Group /stimulus/presentation/post_motion_stim_index/indexed_images (Images) 118_image_serials_ordered_for_indexing
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_0 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_1 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_10 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_100 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_101 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_102 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_103 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_104 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_105 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_106 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_107 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_108 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_109 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_11 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_110 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_111 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_112 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_113 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_114 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_115 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_116 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_117 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_12 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_13 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_14 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_15 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_16 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_17 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_18 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_19 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_2 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_20 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_21 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_22 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_23 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_24 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_25 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_26 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_27 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_28 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_29 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_3 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_30 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_31 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_32 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_33 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_34 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_35 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_36 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_37 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_38 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_39 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_4 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_40 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_41 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_42 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_43 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_44 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_45 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_46 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_47 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_48 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_49 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_5 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_50 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_51 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_52 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_53 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_54 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_55 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_56 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_57 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_58 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_59 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_6 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_60 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_61 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_62 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_63 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_64 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_65 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_66 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_67 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_68 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_69 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_7 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_70 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_71 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_72 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_73 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_74 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_75 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_76 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_77 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_78 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_79 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_8 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_80 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_81 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_82 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_83 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_84 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_85 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_86 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_87 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_88 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_89 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_9 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_90 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_91 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_92 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_93 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_94 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_95 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_96 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_97 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_98 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/natural_scene_99 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/post_motion_stim_index/indexed_images/order_of_images (ImageReferences)  | shape = (118,) | dtype = object
  Group /stimulus/presentation/pre_motion_stim_duration (TimeSeries) stimulus duration (s), stimulus timestamps (s) in timestamps field
  Group /stimulus/presentation/pre_motion_stim_index (IndexSeries) no description
  Group /stimulus/presentation/pre_motion_stim_index/indexed_images (Images) 118_image_serials_ordered_for_indexing
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_0 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_1 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_10 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_100 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_101 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_102 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_103 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_104 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_105 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_106 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_107 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_108 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_109 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_11 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_110 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_111 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_112 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_113 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_114 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_115 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_116 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_117 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_12 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_13 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_14 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_15 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_16 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_17 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_18 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_19 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_2 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_20 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_21 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_22 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_23 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_24 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_25 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_26 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_27 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_28 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_29 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_3 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_30 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_31 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_32 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_33 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_34 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_35 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_36 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_37 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_38 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_39 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_4 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_40 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_41 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_42 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_43 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_44 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_45 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_46 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_47 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_48 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_49 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_5 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_50 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_51 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_52 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_53 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_54 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_55 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_56 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_57 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_58 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_59 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_6 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_60 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_61 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_62 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_63 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_64 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_65 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_66 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_67 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_68 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_69 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_7 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_70 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_71 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_72 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_73 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_74 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_75 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_76 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_77 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_78 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_79 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_8 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_80 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_81 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_82 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_83 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_84 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_85 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_86 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_87 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_88 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_89 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_9 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_90 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_91 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_92 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_93 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_94 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_95 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_96 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_97 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_98 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/natural_scene_99 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/pre_motion_stim_index/indexed_images/order_of_images (ImageReferences)  | shape = (118,) | dtype = object
  Group /stimulus/templates/template_118_images (Images) 118_image_serials_ordered_for_indexing
  Dataset /stimulus/templates/template_118_images/natural_scene_0 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_1 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_10 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_100 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_101 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_102 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_103 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_104 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_105 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_106 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_107 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_108 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_109 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_11 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_110 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_111 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_112 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_113 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_114 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_115 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_116 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_117 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_12 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_13 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_14 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_15 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_16 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_17 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_18 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_19 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_2 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_20 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_21 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_22 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_23 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_24 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_25 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_26 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_27 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_28 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_29 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_3 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_30 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_31 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_32 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_33 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_34 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_35 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_36 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_37 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_38 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_39 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_4 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_40 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_41 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_42 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_43 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_44 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_45 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_46 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_47 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_48 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_49 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_5 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_50 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_51 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_52 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_53 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_54 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_55 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_56 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_57 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_58 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_59 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_6 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_60 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_61 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_62 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_63 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_64 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_65 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_66 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_67 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_68 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_69 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_7 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_70 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_71 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_72 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_73 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_74 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_75 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_76 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_77 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_78 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_79 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_8 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_80 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_81 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_82 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_83 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_84 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_85 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_86 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_87 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_88 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_89 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_9 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_90 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_91 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_92 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_93 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_94 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_95 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_96 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_97 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_98 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_99 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/order_of_images (ImageReferences)  | shape = (118,) | dtype = object
  timestamps_reference_time: 2021-05-01T15:44:27-07:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeriesAP (ElectricalSeries) Acquisition traces for the ElectricalSeriesAP.
  Dataset /acquisition/ElectricalSeriesAP/electrodes (DynamicTableRegion) electrode_table_region | shape = (384,) | dtype = int32
  Group /acquisition/ElectricalSeriesLF (ElectricalSeries) Acquisition traces for the ElectricalSeriesLF.
  Dataset /acquisition/ElectricalSeriesLF/electrodes (DynamicTableRegion) electrode_table_region | shape = (384,) | dtype = int32
  Group /acquisition/manipulator_trigger (TimeSeries) analog signal of manipulator up and down motion
  file_create_date: ['2024-04-06T17:22:24.425464-07:00']
  Group /general/devices/Neuropixel-Imec (Device) {"probe_type": "0", "probe_type_description": "NP1.0", "flex_part_number": "NP2_FLEX_0", "connected_base_station_part_number": "NP2_QBSC_00"}
  experiment_description: Neuropixels ultra impsoed motion in V1
  experimenter: ['Ye, Zhiwen']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/channel_name (VectorData) no description | shape = (768,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/contact_shapes (VectorData) The shape of the electrode | shape = (768,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/gain_to_uV (VectorData) no description | shape = (768,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (768,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (768,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (768,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/inter_sample_shift (VectorData) no description | shape = (768,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (768,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/offset_to_uV (VectorData) no description | shape = (768,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_x (VectorData) rel_x | shape = (768,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_y (VectorData) rel_y | shape = (768,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/shank_electrode_number (VectorData) 0-indexed channel within a shank. | shape = (768,) | dtype = float64
  Group /general/extracellular_ephys/s0 (ElectrodeGroup) a group representing shank s0
  Group /general/extracellular_ephys/s0/device (Device) {"probe_type": "0", "probe_type_description": "NP1.0", "flex_part_number": "NP2_FLEX_0", "connected_base_station_part_number": "NP2_QBSC_00"}
  institution: University of Washington
  keywords: ['Neuropixels ultra, imposed motion, V1']
  lab: Steinmetz lab
  session_id: 1
  Group /general/subject (Subject) 
  identifier: 4fd843a0-2bce-48dc-92bc-a708ebe28bdd
  session_description: Auto-generated by neuroconv
  session_start_time: 2021-11-30T16:10:26-08:00
  Group /stimulus/presentation/all_stim_duration (TimeSeries) stimulus duration (s), stimulus timestamps (s) in timestamps field
  Group /stimulus/presentation/all_stim_index (IndexSeries) no description
  Group /stimulus/presentation/all_stim_index/indexed_images (Images) 118_image_serials_ordered_for_indexing
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_0 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_1 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_10 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_100 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_101 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_102 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_103 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_104 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_105 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_106 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_107 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_108 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_109 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_11 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_110 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_111 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_112 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_113 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_114 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_115 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_116 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_117 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_12 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_13 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_14 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_15 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_16 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_17 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_18 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_19 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_2 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_20 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_21 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_22 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_23 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_24 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_25 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_26 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_27 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_28 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_29 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_3 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_30 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_31 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_32 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_33 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_34 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_35 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_36 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_37 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_38 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_39 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_4 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_40 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_41 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_42 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_43 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_44 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_45 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_46 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_47 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_48 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_49 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_5 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_50 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_51 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_52 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_53 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_54 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_55 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_56 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_57 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_58 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_59 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_6 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_60 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_61 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_62 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_63 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_64 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_65 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_66 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_67 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_68 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_69 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_7 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_70 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_71 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_72 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_73 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_74 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_75 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_76 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_77 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_78 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_79 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_8 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_80 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_81 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_82 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_83 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_84 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_85 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_86 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_87 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_88 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_89 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_9 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_90 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_91 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_92 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_93 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_94 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_95 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_96 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_97 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_98 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/natural_scene_99 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/presentation/all_stim_index/indexed_images/order_of_images (ImageReferences)  | shape = (118,) | dtype = object
  Group /stimulus/templates/template_118_images (Images) 118_image_serials_ordered_for_indexing
  Dataset /stimulus/templates/template_118_images/natural_scene_0 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_1 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_10 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_100 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_101 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_102 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_103 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_104 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_105 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_106 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_107 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_108 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_109 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_11 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_110 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_111 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_112 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_113 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_114 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_115 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_116 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_117 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_12 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_13 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_14 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_15 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_16 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_17 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_18 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_19 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_2 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_20 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_21 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_22 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_23 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_24 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_25 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_26 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_27 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_28 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_29 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_3 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_30 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_31 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_32 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_33 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_34 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_35 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_36 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_37 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_38 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_39 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_4 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_40 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_41 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_42 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_43 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_44 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_45 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_46 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_47 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_48 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_49 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_5 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_50 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_51 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_52 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_53 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_54 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_55 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_56 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_57 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_58 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_59 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_6 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_60 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_61 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_62 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_63 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_64 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_65 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_66 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_67 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_68 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_69 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_7 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_70 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_71 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_72 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_73 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_74 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_75 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_76 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_77 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_78 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_79 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_8 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_80 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_81 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_82 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_83 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_84 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_85 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_86 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_87 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_88 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_89 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_9 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_90 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_91 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_92 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_93 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_94 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_95 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_96 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_97 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_98 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/natural_scene_99 (GrayscaleImage)  | shape = (459, 587) | dtype = float64
  Dataset /stimulus/templates/template_118_images/order_of_images (ImageReferences)  | shape = (118,) | dtype = object
  timestamps_reference_time: 2021-11-30T16:10:26-08:00
