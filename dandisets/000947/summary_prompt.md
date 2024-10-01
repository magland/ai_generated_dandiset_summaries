
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000947/0.240510.2211
name: Reach-related Single Unit Activity in the Parkinsonian Macaque
contributor: [{'name': 'Kase, Daisuke', 'email': 'daisuke.kase@pitt.edu', 'roleName': ['dcite:Author', 'dcite:DataCollector'], 'schemaKey': 'Person', 'identifier': '0000-0002-3837-162X', 'includeInCitation': True}, {'name': 'Han, Yan', 'roleName': ['dcite:DataCollector'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Zimnik, Andrew', 'roleName': ['dcite:Author', 'dcite:DataCollector'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Cox, Karin', 'email': 'kmc51@pitt.edu', 'roleName': ['dcite:Author', 'dcite:DataCollector'], 'schemaKey': 'Person', 'identifier': '0000-0002-5418-0508', 'includeInCitation': True}, {'name': 'Turner, Robert', 'email': 'rturner@pitt.edu', 'roleName': ['dcite:Author', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0002-6074-4365', 'includeInCitation': True}, {'name': "Aligning Science Across Parkinson's (ASAP)", 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/03zj4c476', 'awardNumber': 'ASAP-020519', 'includeInCitation': False}, {'name': 'National Institutes of Health (NIH)', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01cwqze88', 'awardNumber': '1 R01 NS 117058-01', 'includeInCitation': False}, {'name': 'National Institutes of Health (NIH)', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01cwqze88', 'awardNumber': '1 R01 NS 070865-01A1', 'includeInCitation': False}]
description: This dataset contains recordings of single-unit activity from from multiple brain areas,  including globus pallidus-internus (GPi), ventrolateral nucleus of the thalamus (VLa and VLp) and the arm-related regions of primary motor cortex, including sulcus (M1-S) and gyrus (M1-G) subregions, in monkeys performing a choice reaction time reaching task. Small numbers of recordings were also obtained from supplementary motor area (SMA), external globus pallidus (GPe), the thalamic reticular nucleus (RTN), striatum (STR) and the region between RTN and VL thalamus (R-V). It contains data from two monkeys before and after the administration of MPTP (1-methyl-4-phenyl-1,2,3,6-tetrahydropyridine), which induces Parkinsonism. The neuronal activity was recorded using 16-contact linear probes (0.5–1.0 MΩ, V-probe, Plexon) or glass-insulated tungsten microelectrodes (0.5–1.5 MΩ, Alpha Omega). The neuronal data were amplified (4×, 2 Hz–7.5 kHz) and digitized at 24.414 kHz (approx., 16-bit resolution; Tucker Davis Technologies). The neuronal data were high-pass filtered (Fpass: 200 Hz, Matlab FIRPM) and thresholded, and candidate action potentials were sorted into clusters in principal components space (Off-line Sorter, Plexon or custom algorithm, TomSort, https://zenodo.org/doi/10.5281/zenodo.11176978).

The recordings for subject Isis before the administration of MPTP (pre-MPTP) were collected by Daisuke Kase.
The recordings for subject Isis after the administration of MPTP (post-MPTP) were collected by Yan Han (韩妍).
The recordings for subject Gaia (pre-MPTP,  post-MPTP) from 2015 were collected by Andrew J. Zimnik.
The recordings for subject Gaia (post-MPTP) from 2016-2017 were also collected by Daisuke Kase.
assetsSummary: {'species': [{'name': 'Macaca mulatta - Rhesus monkey', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9544'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 1048819909625, 'numberOfFiles': 378, 'numberOfSubjects': 2, 'variableMeasured': ['Units', 'ElectrodeGroup', 'ProcessingModule', 'ElectricalSeries'], 'measurementTechnique': [{'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000947 has 74 NWB files.
6 of these NWB files are of type 1.
2 of these NWB files are of type 2.
1 of these NWB files are of type 3.
6 of these NWB files are of type 4.
59 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeries (ElectricalSeries) Acquisition traces for the ElectricalSeries.
  Dataset /acquisition/ElectricalSeries/electrodes (DynamicTableRegion) electrode_table_region | shape = (2,) | dtype = int64
  file_create_date: ['2024-04-30T14:24:13.408649+02:00']
  Group /general/MPTPMetaData (TurnerLabMetaData) 
  Group /general/devices/DeviceEcephys (Device) TDT recording
  experiment_description: This dataset contains recordings of single-unit activity from from multiple cortical areas, 
  including globus pallidus-internus (GPi), ventrolateral nucleus of the thalamus (VLa and VLp) and 
  the arm-related regions of primary motor cortex, including sulcus (M1-S) and gyrus (M1-G) subregions, in MPTP (1-methyl-4-phenyl-1,2,3,6-tetrahydropyridine)-induced parkinsonian monkeys performing a choice
  reaction time reaching task. Small numbers of recordings were also obtained from supplementary motor area (SMA),
  external globus pallidus (GPe), the thalamic reticular nucleus (RTN), striatum (STR) and the region between RTN
  and VL thalamus (R-V).
  The neuronal activity was recorded using 16-contact linear probes (0.5–1.0 MΩ, V-probe, Plexon) or glass-insulated
  tungsten microelectrodes (0.5–1.5 MΩ, Alpha Omega). The neuronal data were amplified (4×, 2 Hz–7.5 kHz) and
  digitized at 24.414 kHz (approx., 16-bit resolution; Tucker Davis Technologies).
  The neuronal data were high-pass filtered (Fpass: 200 Hz, Matlab FIRPM) and thresholded, and candidate action
  potentials were sorted into clusters in principal components space (Off-line Sorter, Plexon).
  
  experimenter: ['Kase, Daisuke' 'Zimnik, Andrew']
  Group /general/extracellular_ephys/Group GPi (ElectrodeGroup) Group AlphaOmega electrodes.
  Group /general/extracellular_ephys/Group GPi/device (Device) TDT recording
  Group /general/extracellular_ephys/Group VL (ElectrodeGroup) Group AlphaOmega electrodes.
  Group /general/extracellular_ephys/Group VL/device (Device) TDT recording
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/acx_x (VectorData) Medio-lateral coordinate relative to the anterior commissure crossing, lateral positive, in millimeters. | shape = (2,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/acx_y (VectorData) Antero-posterior coordinate relative to the anterior commissure crossing, posterior negative, in millimeters. | shape = (2,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/acx_z (VectorData) Dorso-ventral coordinate relative to the anterior commissure crossing, ventral positive, in millimeters. | shape = (2,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/chamber_type (VectorData) The type of the chamber (either Sagittal or Coronal). | shape = (2,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/chamber_x (VectorData) The medio-lateral coordinate relative to the chamber center, lateral positive, in millimeters. | shape = (2,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/chamber_y (VectorData) The antero-posterior coordinate relative to the chamber center, posterior negative, in millimeters. | shape = (2,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/chamber_z (VectorData) The dorso-ventral coordinate relative to the chamber center, ventral positive, in millimeters. | shape = (2,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/channel_ids (VectorData) The identifier of the channels. | shape = (2,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/channel_name (VectorData) The channel names from TDT. | shape = (2,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/electrode_type (VectorData) The type of electrode. | shape = (2,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/gain_to_uV (VectorData) The gain to apply to the traces to convert to microvolts. | shape = (2,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (2,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (2,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (2,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (2,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/offset_to_uV (VectorData) The offset to apply to the traces to convert to microvolts. | shape = (2,) | dtype = float64
  institution: University of Pittsburgh
  keywords: ['extracellular electrophysiology' 'single-unit activity'
   'globus pallidus-internus' 'ventrolateral anterior nucleus'
   'primary motor cortex' 'reaching task' "Parkinson's disease" 'macaque'
   'MPTP']
  lab: Turner
  pharmacology: MPTP (1-methyl-4-phenyl-1,2,3,6-tetrahydropyridine; the chemical compound that induces parkinsonism) administration date 2015-02-09 (ICA; internal carotid artery injection)
  related_publications: ['https://doi.org/10.1101/2023.09.08.556120']
  session_id: post-MPTP-G-150303-1
  Group /general/subject (Subject) 
  identifier: 543e1e84-2cf6-477f-80f7-1dc216aa1d1f
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/cue_onset_time (VectorData) The times of the target and go-cue instruction (reach target and go-cue were instructed simulatneously in this task). | shape = (36,) | dtype = float64
  Dataset /intervals/trials/error_onset_time (VectorData) The times of the error onset. | shape = (36,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (36,) | dtype = int64
  Dataset /intervals/trials/movement_start_time (VectorData) The times of the hand sensor at the home-position off (= onset of the movement). | shape = (36,) | dtype = float64
  Dataset /intervals/trials/reward_start_time (VectorData) The times of the reward onset. | shape = (36,) | dtype = float64
  Dataset /intervals/trials/reward_stop_time (VectorData) The times of the reward offset. | shape = (36,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (36,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (36,) | dtype = float64
  Dataset /intervals/trials/target (VectorData) Defines whether the target was on the left or right side. | shape = (36,) | dtype = object
  Group /processing/ecephys (ProcessingModule) Intermediate data from extracellular electrophysiology recordings, e.g., LFP.
  Group /processing/ecephys/Processed (FilteredEphys) 
  Group /processing/ecephys/Processed/ElectricalSeriesProcessed (ElectricalSeries) High-pass filtered traces (200 Hz) from VL, GPi region.
  Dataset /processing/ecephys/Processed/ElectricalSeriesProcessed/electrodes (DynamicTableRegion) electrode_table_region | shape = (2,) | dtype = int64
  Group /processing/ecephys/units (Units) The units were sorted using the Plexon Offline Sorter v3.
  Dataset /processing/ecephys/units/id (ElementIdentifiers)  | shape = (2,) | dtype = int64
  Dataset /processing/ecephys/units/location (VectorData) The brain region for each unit. | shape = (2,) | dtype = object
  Dataset /processing/ecephys/units/spike_times (VectorData) the spike times for each unit | shape = (5116,) | dtype = float64
  Dataset /processing/ecephys/units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (2,) | dtype = uint16
  Dataset /processing/ecephys/units/unit_name (VectorData) Unique reference for each unit. | shape = (2,) | dtype = object
  session_description: This session contains raw and high-pass filtered (200 Hz) extracellular data from multiple cortical areas,
  including the globus pallidus-internus (GPi) and ventrolateral nucleus of the thalamus (VLa and VLp) in 
  parkinsonian macaque performing a choice reaction time reaching task.
  
  session_start_time: 2015-03-05T12:15:35-08:00
  timestamps_reference_time: 2015-03-05T12:15:35-08:00
  Group /units (Units) The curated single-units from the Plexon Offline Sorter v3, selected based on the quality of spike sorting.
  Dataset /units/channel_ids (VectorData) The electrode channel ids for each unit. | shape = (1,) | dtype = float64
  Dataset /units/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /units/location (VectorData) The brain region for each unit. | shape = (1,) | dtype = object
  Dataset /units/sort_label (VectorData) The sorting label for each unit. | shape = (1,) | dtype = object
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (1200,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (1,) | dtype = uint16
  Dataset /units/unit_name (VectorData) Unique reference for each unit. | shape = (1,) | dtype = object


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeries (ElectricalSeries) Acquisition traces for the ElectricalSeries.
  Dataset /acquisition/ElectricalSeries/electrodes (DynamicTableRegion) electrode_table_region | shape = (17,) | dtype = int64
  file_create_date: ['2024-04-27T08:28:40.467818+02:00']
  Group /general/MPTPMetaData (TurnerLabMetaData) 
  Group /general/devices/DeviceEcephys (Device) TDT recording
  experiment_description: This dataset contains recordings of single-unit activity from from multiple cortical areas, 
  including globus pallidus-internus (GPi), ventrolateral nucleus of the thalamus (VLa and VLp) and 
  the arm-related regions of primary motor cortex, including sulcus (M1-S) and gyrus (M1-G) subregions, in MPTP (1-methyl-4-phenyl-1,2,3,6-tetrahydropyridine)-induced parkinsonian monkeys performing a choice
  reaction time reaching task. Small numbers of recordings were also obtained from supplementary motor area (SMA),
  external globus pallidus (GPe), the thalamic reticular nucleus (RTN), striatum (STR) and the region between RTN
  and VL thalamus (R-V).
  The neuronal activity was recorded using 16-contact linear probes (0.5–1.0 MΩ, V-probe, Plexon) or glass-insulated
  tungsten microelectrodes (0.5–1.5 MΩ, Alpha Omega). The neuronal data were amplified (4×, 2 Hz–7.5 kHz) and
  digitized at 24.414 kHz (approx., 16-bit resolution; Tucker Davis Technologies).
  The neuronal data were high-pass filtered (Fpass: 200 Hz, Matlab FIRPM) and thresholded, and candidate action
  potentials were sorted into clusters in principal components space (Off-line Sorter, Plexon).
  
  experimenter: ['Kase, Daisuke' 'Zimnik, Andrew']
  Group /general/extracellular_ephys/Group GPi (ElectrodeGroup) Group new V-prove electrodes.
  Group /general/extracellular_ephys/Group GPi/device (Device) TDT recording
  Group /general/extracellular_ephys/Group VL (ElectrodeGroup) Group Alpha Omega electrodes.
  Group /general/extracellular_ephys/Group VL/device (Device) TDT recording
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/acx_x (VectorData) Medio-lateral coordinate relative to the anterior commissure crossing, lateral positive, in millimeters. | shape = (17,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/acx_y (VectorData) Antero-posterior coordinate relative to the anterior commissure crossing, posterior negative, in millimeters. | shape = (17,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/acx_z (VectorData) Dorso-ventral coordinate relative to the anterior commissure crossing, ventral positive, in millimeters. | shape = (17,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/chamber_type (VectorData) The type of the chamber (either Sagittal or Coronal). | shape = (17,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/chamber_x (VectorData) The medio-lateral coordinate relative to the chamber center, lateral positive, in millimeters. | shape = (17,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/chamber_y (VectorData) The antero-posterior coordinate relative to the chamber center, posterior negative, in millimeters. | shape = (17,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/chamber_z (VectorData) The dorso-ventral coordinate relative to the chamber center, ventral positive, in millimeters. | shape = (17,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/channel_ids (VectorData) The identifier of the channels. | shape = (17,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/channel_name (VectorData) The channel names from TDT. | shape = (17,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/electrode_type (VectorData) The type of electrode. | shape = (17,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/gain_to_uV (VectorData) The gain to apply to the traces to convert to microvolts. | shape = (17,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (17,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (17,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (17,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (17,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/offset_to_uV (VectorData) The offset to apply to the traces to convert to microvolts. | shape = (17,) | dtype = float64
  institution: University of Pittsburgh
  keywords: ['extracellular electrophysiology' 'single-unit activity'
   'globus pallidus-internus' 'ventrolateral anterior nucleus'
   'primary motor cortex' 'reaching task' "Parkinson's disease" 'macaque'
   'MPTP']
  lab: Turner
  pharmacology: MPTP (1-methyl-4-phenyl-1,2,3,6-tetrahydropyridine; the chemical compound that induces parkinsonism) administration date 2015-02-09 (ICA; internal carotid artery injection)
  related_publications: ['https://doi.org/10.1101/2023.09.08.556120']
  session_id: post-MPTP-G-170302-1
  Group /general/subject (Subject) 
  identifier: 2e826e9f-749b-43b8-a67c-5735c962b976
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/cue_onset_time (VectorData) The times of the target and go-cue instruction (reach target and go-cue were instructed simulatneously in this task). | shape = (60,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (60,) | dtype = int64
  Dataset /intervals/trials/movement_start_time (VectorData) The times of the hand sensor at the home-position off (= onset of the movement). | shape = (60,) | dtype = float64
  Dataset /intervals/trials/movement_stop_time (VectorData) The times of the hand sensor at the reach target on (= end of the movement). | shape = (60,) | dtype = float64
  Dataset /intervals/trials/return_start_time (VectorData) The times of the hand sensor at the reach target off (= onset of the return movement) | shape = (60,) | dtype = float64
  Dataset /intervals/trials/return_stop_time (VectorData) The times of the hand sensor at the home-position on (= end of the return movement) | shape = (60,) | dtype = float64
  Dataset /intervals/trials/reward_start_time (VectorData) The times of the reward onset. | shape = (60,) | dtype = float64
  Dataset /intervals/trials/reward_stop_time (VectorData) The times of the reward offset. | shape = (60,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (60,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (60,) | dtype = float64
  Dataset /intervals/trials/target (VectorData) Defines whether the target was on the left or right side. | shape = (60,) | dtype = object
  Group /processing/ecephys (ProcessingModule) Intermediate data from extracellular electrophysiology recordings, e.g., LFP.
  Group /processing/ecephys/Processed (FilteredEphys) 
  Group /processing/ecephys/Processed/ElectricalSeriesProcessedGPi (ElectricalSeries) High-pass filtered traces (200 Hz) from GPi region.
  Dataset /processing/ecephys/Processed/ElectricalSeriesProcessedGPi/electrodes (DynamicTableRegion) electrode_table_region | shape = (16,) | dtype = int64
  Group /processing/ecephys/Processed/ElectricalSeriesProcessedVL (ElectricalSeries) High-pass filtered traces (200 Hz) from VL region.
  Dataset /processing/ecephys/Processed/ElectricalSeriesProcessedVL/electrodes (DynamicTableRegion) electrode_table_region | shape = (1,) | dtype = int64
  Group /processing/ecephys/units (Units) The units were sorted using the Plexon Offline Sorter v3.
  Dataset /processing/ecephys/units/id (ElementIdentifiers)  | shape = (3,) | dtype = int64
  Dataset /processing/ecephys/units/location (VectorData) The brain region for each unit. | shape = (3,) | dtype = object
  Dataset /processing/ecephys/units/spike_times (VectorData) the spike times for each unit | shape = (570020,) | dtype = float64
  Dataset /processing/ecephys/units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (3,) | dtype = uint32
  Dataset /processing/ecephys/units/unit_name (VectorData) Unique reference for each unit. | shape = (3,) | dtype = object
  session_description: This session contains raw and high-pass filtered (200 Hz) extracellular data from multiple cortical areas,
  including the globus pallidus-internus (GPi) and ventrolateral nucleus of the thalamus (VLa and VLp) in 
  parkinsonian macaque performing a choice reaction time reaching task.
  
  session_start_time: 2017-03-04T14:03:26.000001-08:00
  timestamps_reference_time: 2017-03-04T14:03:26.000001-08:00


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeries (ElectricalSeries) Acquisition traces for the ElectricalSeries.
  Dataset /acquisition/ElectricalSeries/electrodes (DynamicTableRegion) electrode_table_region | shape = (2,) | dtype = int64
  file_create_date: ['2024-04-30T14:19:56.942240+02:00']
  Group /general/MPTPMetaData (TurnerLabMetaData) 
  Group /general/devices/DeviceEcephys (Device) TDT recording
  experiment_description: This dataset contains recordings of single-unit activity from from multiple cortical areas, 
  including globus pallidus-internus (GPi), ventrolateral nucleus of the thalamus (VLa and VLp) and 
  the arm-related regions of primary motor cortex, including sulcus (M1-S) and gyrus (M1-G) subregions, in MPTP (1-methyl-4-phenyl-1,2,3,6-tetrahydropyridine)-induced parkinsonian monkeys performing a choice
  reaction time reaching task. Small numbers of recordings were also obtained from supplementary motor area (SMA),
  external globus pallidus (GPe), the thalamic reticular nucleus (RTN), striatum (STR) and the region between RTN
  and VL thalamus (R-V).
  The neuronal activity was recorded using 16-contact linear probes (0.5–1.0 MΩ, V-probe, Plexon) or glass-insulated
  tungsten microelectrodes (0.5–1.5 MΩ, Alpha Omega). The neuronal data were amplified (4×, 2 Hz–7.5 kHz) and
  digitized at 24.414 kHz (approx., 16-bit resolution; Tucker Davis Technologies).
  The neuronal data were high-pass filtered (Fpass: 200 Hz, Matlab FIRPM) and thresholded, and candidate action
  potentials were sorted into clusters in principal components space (Off-line Sorter, Plexon).
  
  experimenter: ['Kase, Daisuke' 'Zimnik, Andrew']
  Group /general/extracellular_ephys/Group VL (ElectrodeGroup) Group AlphaOmega electrodes.
  Group /general/extracellular_ephys/Group VL/device (Device) TDT recording
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/acx_x (VectorData) Medio-lateral coordinate relative to the anterior commissure crossing, lateral positive, in millimeters. | shape = (2,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/acx_y (VectorData) Antero-posterior coordinate relative to the anterior commissure crossing, posterior negative, in millimeters. | shape = (2,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/acx_z (VectorData) Dorso-ventral coordinate relative to the anterior commissure crossing, ventral positive, in millimeters. | shape = (2,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/chamber_type (VectorData) The type of the chamber (either Sagittal or Coronal). | shape = (2,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/chamber_x (VectorData) The medio-lateral coordinate relative to the chamber center, lateral positive, in millimeters. | shape = (2,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/chamber_y (VectorData) The antero-posterior coordinate relative to the chamber center, posterior negative, in millimeters. | shape = (2,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/chamber_z (VectorData) The dorso-ventral coordinate relative to the chamber center, ventral positive, in millimeters. | shape = (2,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/channel_ids (VectorData) The identifier of the channels. | shape = (2,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/channel_name (VectorData) The channel names from TDT. | shape = (2,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/electrode_type (VectorData) The type of electrode. | shape = (2,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/gain_to_uV (VectorData) The gain to apply to the traces to convert to microvolts. | shape = (2,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (2,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (2,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (2,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (2,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/offset_to_uV (VectorData) The offset to apply to the traces to convert to microvolts. | shape = (2,) | dtype = float64
  institution: University of Pittsburgh
  keywords: ['extracellular electrophysiology' 'single-unit activity'
   'globus pallidus-internus' 'ventrolateral anterior nucleus'
   'primary motor cortex' 'reaching task' "Parkinson's disease" 'macaque'
   'MPTP']
  lab: Turner
  pharmacology: MPTP (1-methyl-4-phenyl-1,2,3,6-tetrahydropyridine; the chemical compound that induces parkinsonism) administration date 2015-02-09 (ICA; internal carotid artery injection)
  related_publications: ['https://doi.org/10.1101/2023.09.08.556120']
  session_id: post-MPTP-G-150324-2
  Group /general/subject (Subject) 
  identifier: 8d0a5e95-3e73-422b-bdfc-c35f755e2a4d
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/cue_onset_time (VectorData) The times of the target and go-cue instruction (reach target and go-cue were instructed simulatneously in this task). | shape = (51,) | dtype = float64
  Dataset /intervals/trials/error_onset_time (VectorData) The times of the error onset. | shape = (51,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (51,) | dtype = int64
  Dataset /intervals/trials/movement_start_time (VectorData) The times of the hand sensor at the home-position off (= onset of the movement). | shape = (51,) | dtype = float64
  Dataset /intervals/trials/reward_start_time (VectorData) The times of the reward onset. | shape = (51,) | dtype = float64
  Dataset /intervals/trials/reward_stop_time (VectorData) The times of the reward offset. | shape = (51,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (51,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (51,) | dtype = float64
  Dataset /intervals/trials/target (VectorData) Defines whether the target was on the left or right side. | shape = (51,) | dtype = object
  Group /processing/ecephys (ProcessingModule) Intermediate data from extracellular electrophysiology recordings, e.g., LFP.
  Group /processing/ecephys/Processed (FilteredEphys) 
  Group /processing/ecephys/Processed/ElectricalSeriesProcessed (ElectricalSeries) High-pass filtered traces (200 Hz) from VL region.
  Dataset /processing/ecephys/Processed/ElectricalSeriesProcessed/electrodes (DynamicTableRegion) electrode_table_region | shape = (2,) | dtype = int64
  Group /processing/ecephys/units (Units) The units were sorted using the Plexon Offline Sorter v3.
  Dataset /processing/ecephys/units/id (ElementIdentifiers)  | shape = (4,) | dtype = int64
  Dataset /processing/ecephys/units/location (VectorData) The brain region for each unit. | shape = (4,) | dtype = object
  Dataset /processing/ecephys/units/spike_times (VectorData) the spike times for each unit | shape = (155658,) | dtype = float64
  Dataset /processing/ecephys/units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (4,) | dtype = uint32
  Dataset /processing/ecephys/units/unit_name (VectorData) Unique reference for each unit. | shape = (4,) | dtype = object
  session_description: This session contains raw and high-pass filtered (200 Hz) extracellular data from multiple cortical areas,
  including the globus pallidus-internus (GPi) and ventrolateral nucleus of the thalamus (VLa and VLp) in 
  parkinsonian macaque performing a choice reaction time reaching task.
  
  session_start_time: 2015-03-26T15:08:46-07:00
  timestamps_reference_time: 2015-03-26T15:08:46-07:00
  Group /units (Units) The curated single-units from the Plexon Offline Sorter v3, selected based on the quality of spike sorting.
  Dataset /units/channel_ids (VectorData) The electrode channel ids for each unit. | shape = (2,) | dtype = float64
  Dataset /units/id (ElementIdentifiers)  | shape = (2,) | dtype = int64
  Dataset /units/location (VectorData) The brain region for each unit. | shape = (2,) | dtype = object
  Dataset /units/sort_label (VectorData) The sorting label for each unit. | shape = (2,) | dtype = object
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (9180,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (2,) | dtype = uint16
  Dataset /units/unit_name (VectorData) Unique reference for each unit. | shape = (2,) | dtype = object


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeries (ElectricalSeries) Acquisition traces for the ElectricalSeries.
  Dataset /acquisition/ElectricalSeries/electrodes (DynamicTableRegion) electrode_table_region | shape = (32,) | dtype = int64
  file_create_date: ['2024-04-27T07:48:44.816819+02:00']
  Group /general/MPTPMetaData (TurnerLabMetaData) 
  Group /general/devices/DeviceEcephys (Device) TDT recording
  experiment_description: This dataset contains recordings of single-unit activity from from multiple cortical areas, 
  including globus pallidus-internus (GPi), ventrolateral nucleus of the thalamus (VLa and VLp) and 
  the arm-related regions of primary motor cortex, including sulcus (M1-S) and gyrus (M1-G) subregions, in MPTP (1-methyl-4-phenyl-1,2,3,6-tetrahydropyridine)-induced parkinsonian monkeys performing a choice
  reaction time reaching task. Small numbers of recordings were also obtained from supplementary motor area (SMA),
  external globus pallidus (GPe), the thalamic reticular nucleus (RTN), striatum (STR) and the region between RTN
  and VL thalamus (R-V).
  The neuronal activity was recorded using 16-contact linear probes (0.5–1.0 MΩ, V-probe, Plexon) or glass-insulated
  tungsten microelectrodes (0.5–1.5 MΩ, Alpha Omega). The neuronal data were amplified (4×, 2 Hz–7.5 kHz) and
  digitized at 24.414 kHz (approx., 16-bit resolution; Tucker Davis Technologies).
  The neuronal data were high-pass filtered (Fpass: 200 Hz, Matlab FIRPM) and thresholded, and candidate action
  potentials were sorted into clusters in principal components space (Off-line Sorter, Plexon).
  
  experimenter: ['Kase, Daisuke' 'Zimnik, Andrew']
  Group /general/extracellular_ephys/Group GPi (ElectrodeGroup) Group new V-prove electrodes.
  Group /general/extracellular_ephys/Group GPi/device (Device) TDT recording
  Group /general/extracellular_ephys/Group VL (ElectrodeGroup) Group old V-prove electrodes.
  Group /general/extracellular_ephys/Group VL/device (Device) TDT recording
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/acx_x (VectorData) Medio-lateral coordinate relative to the anterior commissure crossing, lateral positive, in millimeters. | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/acx_y (VectorData) Antero-posterior coordinate relative to the anterior commissure crossing, posterior negative, in millimeters. | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/acx_z (VectorData) Dorso-ventral coordinate relative to the anterior commissure crossing, ventral positive, in millimeters. | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/chamber_type (VectorData) The type of the chamber (either Sagittal or Coronal). | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/chamber_x (VectorData) The medio-lateral coordinate relative to the chamber center, lateral positive, in millimeters. | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/chamber_y (VectorData) The antero-posterior coordinate relative to the chamber center, posterior negative, in millimeters. | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/chamber_z (VectorData) The dorso-ventral coordinate relative to the chamber center, ventral positive, in millimeters. | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/channel_ids (VectorData) The identifier of the channels. | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/channel_name (VectorData) The channel names from TDT. | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/electrode_type (VectorData) The type of electrode. | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/gain_to_uV (VectorData) The gain to apply to the traces to convert to microvolts. | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (32,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/offset_to_uV (VectorData) The offset to apply to the traces to convert to microvolts. | shape = (32,) | dtype = float64
  institution: University of Pittsburgh
  keywords: ['extracellular electrophysiology' 'single-unit activity'
   'globus pallidus-internus' 'ventrolateral anterior nucleus'
   'primary motor cortex' 'reaching task' "Parkinson's disease" 'macaque'
   'MPTP']
  lab: Turner
  pharmacology: MPTP (1-methyl-4-phenyl-1,2,3,6-tetrahydropyridine; the chemical compound that induces parkinsonism) administration date 2015-02-09 (ICA; internal carotid artery injection)
  related_publications: ['https://doi.org/10.1101/2023.09.08.556120']
  session_id: post-MPTP-G-161114-1
  Group /general/subject (Subject) 
  identifier: f51e86f0-e331-4f56-842e-9d95e2f2d22e
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/cue_onset_time (VectorData) The times of the target and go-cue instruction (reach target and go-cue were instructed simulatneously in this task). | shape = (81,) | dtype = float64
  Dataset /intervals/trials/error_onset_time (VectorData) The times of the error onset. | shape = (81,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (81,) | dtype = int64
  Dataset /intervals/trials/movement_start_time (VectorData) The times of the hand sensor at the home-position off (= onset of the movement). | shape = (81,) | dtype = float64
  Dataset /intervals/trials/movement_stop_time (VectorData) The times of the hand sensor at the reach target on (= end of the movement). | shape = (81,) | dtype = float64
  Dataset /intervals/trials/return_start_time (VectorData) The times of the hand sensor at the reach target off (= onset of the return movement) | shape = (81,) | dtype = float64
  Dataset /intervals/trials/return_stop_time (VectorData) The times of the hand sensor at the home-position on (= end of the return movement) | shape = (81,) | dtype = float64
  Dataset /intervals/trials/reward_start_time (VectorData) The times of the reward onset. | shape = (81,) | dtype = float64
  Dataset /intervals/trials/reward_stop_time (VectorData) The times of the reward offset. | shape = (81,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (81,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (81,) | dtype = float64
  Dataset /intervals/trials/target (VectorData) Defines whether the target was on the left or right side. | shape = (81,) | dtype = object
  Group /processing/ecephys (ProcessingModule) Intermediate data from extracellular electrophysiology recordings, e.g., LFP.
  Group /processing/ecephys/Processed (FilteredEphys) 
  Group /processing/ecephys/Processed/ElectricalSeriesProcessedGPi (ElectricalSeries) High-pass filtered traces (200 Hz) from GPi region.
  Dataset /processing/ecephys/Processed/ElectricalSeriesProcessedGPi/electrodes (DynamicTableRegion) electrode_table_region | shape = (16,) | dtype = int64
  Group /processing/ecephys/Processed/ElectricalSeriesProcessedVL (ElectricalSeries) High-pass filtered traces (200 Hz) from VL region.
  Dataset /processing/ecephys/Processed/ElectricalSeriesProcessedVL/electrodes (DynamicTableRegion) electrode_table_region | shape = (16,) | dtype = int64
  Group /processing/ecephys/units (Units) The units were sorted using the Plexon Offline Sorter v3.
  Dataset /processing/ecephys/units/id (ElementIdentifiers)  | shape = (17,) | dtype = int64
  Dataset /processing/ecephys/units/location (VectorData) The brain region for each unit. | shape = (17,) | dtype = object
  Dataset /processing/ecephys/units/spike_times (VectorData) the spike times for each unit | shape = (1409626,) | dtype = float64
  Dataset /processing/ecephys/units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (17,) | dtype = uint32
  Dataset /processing/ecephys/units/unit_name (VectorData) Unique reference for each unit. | shape = (17,) | dtype = object
  session_description: This session contains raw and high-pass filtered (200 Hz) extracellular data from multiple cortical areas,
  including the globus pallidus-internus (GPi) and ventrolateral nucleus of the thalamus (VLa and VLp) in 
  parkinsonian macaque performing a choice reaction time reaching task.
  
  session_start_time: 2016-11-16T15:17:23-08:00
  timestamps_reference_time: 2016-11-16T15:17:23-08:00


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeries (ElectricalSeries) Acquisition traces for the ElectricalSeries.
  Dataset /acquisition/ElectricalSeries/electrodes (DynamicTableRegion) electrode_table_region | shape = (32,) | dtype = int64
  file_create_date: ['2024-04-27T10:56:49.391802+02:00']
  Group /general/MPTPMetaData (TurnerLabMetaData) 
  Group /general/devices/DeviceEcephys (Device) TDT recording
  experiment_description: This dataset contains recordings of single-unit activity from from multiple cortical areas, 
  including globus pallidus-internus (GPi), ventrolateral nucleus of the thalamus (VLa and VLp) and 
  the arm-related regions of primary motor cortex, including sulcus (M1-S) and gyrus (M1-G) subregions, in MPTP (1-methyl-4-phenyl-1,2,3,6-tetrahydropyridine)-induced parkinsonian monkeys performing a choice
  reaction time reaching task. Small numbers of recordings were also obtained from supplementary motor area (SMA),
  external globus pallidus (GPe), the thalamic reticular nucleus (RTN), striatum (STR) and the region between RTN
  and VL thalamus (R-V).
  The neuronal activity was recorded using 16-contact linear probes (0.5–1.0 MΩ, V-probe, Plexon) or glass-insulated
  tungsten microelectrodes (0.5–1.5 MΩ, Alpha Omega). The neuronal data were amplified (4×, 2 Hz–7.5 kHz) and
  digitized at 24.414 kHz (approx., 16-bit resolution; Tucker Davis Technologies).
  The neuronal data were high-pass filtered (Fpass: 200 Hz, Matlab FIRPM) and thresholded, and candidate action
  potentials were sorted into clusters in principal components space (Off-line Sorter, Plexon).
  
  experimenter: ['Kase, Daisuke' 'Zimnik, Andrew']
  Group /general/extracellular_ephys/Group GPi (ElectrodeGroup) Group new V-prove electrodes.
  Group /general/extracellular_ephys/Group GPi/device (Device) TDT recording
  Group /general/extracellular_ephys/Group VL (ElectrodeGroup) Group old V-prove electrodes.
  Group /general/extracellular_ephys/Group VL/device (Device) TDT recording
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/acx_x (VectorData) Medio-lateral coordinate relative to the anterior commissure crossing, lateral positive, in millimeters. | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/acx_y (VectorData) Antero-posterior coordinate relative to the anterior commissure crossing, posterior negative, in millimeters. | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/acx_z (VectorData) Dorso-ventral coordinate relative to the anterior commissure crossing, ventral positive, in millimeters. | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/chamber_type (VectorData) The type of the chamber (either Sagittal or Coronal). | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/chamber_x (VectorData) The medio-lateral coordinate relative to the chamber center, lateral positive, in millimeters. | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/chamber_y (VectorData) The antero-posterior coordinate relative to the chamber center, posterior negative, in millimeters. | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/chamber_z (VectorData) The dorso-ventral coordinate relative to the chamber center, ventral positive, in millimeters. | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/channel_ids (VectorData) The identifier of the channels. | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/channel_name (VectorData) The channel names from TDT. | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/electrode_type (VectorData) The type of electrode. | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/gain_to_uV (VectorData) The gain to apply to the traces to convert to microvolts. | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (32,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/offset_to_uV (VectorData) The offset to apply to the traces to convert to microvolts. | shape = (32,) | dtype = float64
  institution: University of Pittsburgh
  keywords: ['extracellular electrophysiology' 'single-unit activity'
   'globus pallidus-internus' 'ventrolateral anterior nucleus'
   'primary motor cortex' 'reaching task' "Parkinson's disease" 'macaque'
   'MPTP']
  lab: Turner
  pharmacology: MPTP (1-methyl-4-phenyl-1,2,3,6-tetrahydropyridine; the chemical compound that induces parkinsonism) administration date 2015-02-09 (ICA; internal carotid artery injection)
  related_publications: ['https://doi.org/10.1101/2023.09.08.556120']
  session_id: post-MPTP-G-161117-2
  Group /general/subject (Subject) 
  identifier: 07a160bb-d9b0-4b46-9e27-d45ec70f5827
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/cue_onset_time (VectorData) The times of the target and go-cue instruction (reach target and go-cue were instructed simulatneously in this task). | shape = (100,) | dtype = float64
  Dataset /intervals/trials/error_onset_time (VectorData) The times of the error onset. | shape = (100,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (100,) | dtype = int64
  Dataset /intervals/trials/movement_start_time (VectorData) The times of the hand sensor at the home-position off (= onset of the movement). | shape = (100,) | dtype = float64
  Dataset /intervals/trials/movement_stop_time (VectorData) The times of the hand sensor at the reach target on (= end of the movement). | shape = (100,) | dtype = float64
  Dataset /intervals/trials/return_start_time (VectorData) The times of the hand sensor at the reach target off (= onset of the return movement) | shape = (100,) | dtype = float64
  Dataset /intervals/trials/return_stop_time (VectorData) The times of the hand sensor at the home-position on (= end of the return movement) | shape = (100,) | dtype = float64
  Dataset /intervals/trials/reward_start_time (VectorData) The times of the reward onset. | shape = (100,) | dtype = float64
  Dataset /intervals/trials/reward_stop_time (VectorData) The times of the reward offset. | shape = (100,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (100,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (100,) | dtype = float64
  Dataset /intervals/trials/target (VectorData) Defines whether the target was on the left or right side. | shape = (100,) | dtype = object
  Group /processing/ecephys (ProcessingModule) Intermediate data from extracellular electrophysiology recordings, e.g., LFP.
  Group /processing/ecephys/Processed (FilteredEphys) 
  Group /processing/ecephys/Processed/ElectricalSeriesProcessedGPi (ElectricalSeries) High-pass filtered traces (200 Hz) from GPi region.
  Dataset /processing/ecephys/Processed/ElectricalSeriesProcessedGPi/electrodes (DynamicTableRegion) electrode_table_region | shape = (16,) | dtype = int64
  Group /processing/ecephys/Processed/ElectricalSeriesProcessedVL (ElectricalSeries) High-pass filtered traces (200 Hz) from VL region.
  Dataset /processing/ecephys/Processed/ElectricalSeriesProcessedVL/electrodes (DynamicTableRegion) electrode_table_region | shape = (16,) | dtype = int64
  Group /processing/ecephys/units (Units) The units were sorted using the Plexon Offline Sorter v3.
  Dataset /processing/ecephys/units/id (ElementIdentifiers)  | shape = (29,) | dtype = int64
  Dataset /processing/ecephys/units/location (VectorData) The brain region for each unit. | shape = (29,) | dtype = object
  Dataset /processing/ecephys/units/spike_times (VectorData) the spike times for each unit | shape = (2192732,) | dtype = float64
  Dataset /processing/ecephys/units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (29,) | dtype = uint32
  Dataset /processing/ecephys/units/unit_name (VectorData) Unique reference for each unit. | shape = (29,) | dtype = object
  session_description: This session contains raw and high-pass filtered (200 Hz) extracellular data from multiple cortical areas,
  including the globus pallidus-internus (GPi) and ventrolateral nucleus of the thalamus (VLa and VLp) in 
  parkinsonian macaque performing a choice reaction time reaching task.
  
  session_start_time: 2016-11-19T14:18:33-08:00
  timestamps_reference_time: 2016-11-19T14:18:33-08:00
  Group /units (Units) The curated single-units from the Plexon Offline Sorter v3, selected based on the quality of spike sorting.
  Dataset /units/channel_ids (VectorData) The electrode channel ids for each unit. | shape = (9,) | dtype = float64
  Dataset /units/id (ElementIdentifiers)  | shape = (9,) | dtype = int64
  Dataset /units/location (VectorData) The brain region for each unit. | shape = (9,) | dtype = object
  Dataset /units/sort_label (VectorData) The sorting label for each unit. | shape = (9,) | dtype = object
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (269273,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (9,) | dtype = uint32
  Dataset /units/unit_name (VectorData) Unique reference for each unit. | shape = (9,) | dtype = object
  Dataset /units/unit_quality_post_sorting (VectorData) The quality of the unit after sorting. | shape = (9,) | dtype = object
