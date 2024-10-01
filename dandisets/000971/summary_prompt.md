
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000971/0.240802.2004
name: Dopamine signaling in the dorsomedial striatum promotes compulsive behavior
contributor: [{'name': 'Seiler, Jillian L.', 'email': 'jillian.seiler@northwestern.edu', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0003-4430-4797', 'includeInCitation': True}, {'name': 'Cosme, Caitlin V.', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-8024-7841', 'includeInCitation': True}, {'name': 'Sherathiya, Venus N.', 'email': 'venus.sherathiya@northwestern.edu', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0003-0143-9771', 'includeInCitation': True}, {'name': 'Schaid, Michael D.', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Bianco, Joseph M.', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-8598-0604', 'includeInCitation': True}, {'name': 'Bridgemohan, Abigael S.', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Lerner, Talia N.', 'email': 'talia.lerner@northwestern.edu', 'roleName': ['dcite:Author', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0002-3875-0654', 'includeInCitation': True}, {'url': 'http://www.nih.gov/', 'name': 'National Institutes of Health', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01cwqze88', 'awardNumber': 'R00MH109569', 'includeInCitation': False}, {'url': 'http://www.nih.gov/', 'name': 'National Institutes of Health', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01cwqze88', 'awardNumber': 'R00MH109569-04S1', 'includeInCitation': False}, {'name': 'Brain and Behavior Research Foundation', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/03a63f080', 'includeInCitation': False}, {'name': 'National Institutes of Health', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01cwqze88', 'awardNumber': 'R00MH109569-04S1', 'includeInCitation': False}, {'name': 'Palissery, Gates', 'roleName': ['dcite:DataCollector'], 'schemaKey': 'Person', 'includeInCitation': False}, {'name': 'Van Camp, Louis', 'roleName': ['dcite:DataCollector'], 'schemaKey': 'Person', 'includeInCitation': False}, {'name': 'Sikora, Hayden', 'roleName': ['dcite:DataCollector'], 'schemaKey': 'Person', 'includeInCitation': False}, {'name': 'Holla, Meghana', 'roleName': ['dcite:DataCollector'], 'schemaKey': 'Person', 'includeInCitation': False}, {'name': 'Adkisson, Paul', 'email': 'paul.wesley.adkisson@gmail.com', 'roleName': ['dcite:DataCurator'], 'schemaKey': 'Person', 'identifier': '0009-0005-8943-5450', 'affiliation': [], 'includeInCitation': False}]
description: Compulsive behavior is a defining feature of disorders such as substance use disorders. Current evidence
suggests that corticostriatal circuits control the expression of established compulsions, but little is known
about the mechanisms regulating the development of compulsions. We hypothesized that dopamine, a critical modulator of striatal synaptic plasticity, could control alterations in corticostriatal circuits leading to the
development of compulsions (defined here as continued reward seeking in the face of punishment). We used
dual-site fiber photometry to measure dopamine axon activity in the dorsomedial striatum (DMS) and the
dorsolateral striatum (DLS) as compulsions emerged. Individual variability in the speed with which compulsions emerged was predicted by DMS dopamine axon activity. Amplifying this dopamine signal accelerated
animals’ transitions to compulsion, whereas inhibition delayed it. In contrast, amplifying DLS dopamine
signaling had no effect on the emergence of compulsions. These results establish DMS dopamine signaling
as a key controller of the development of compulsive reward seeking.
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'behavioral approach', 'schemaKey': 'ApproachType'}, {'name': 'optogenetic approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 23491138657, 'numberOfFiles': 4139, 'numberOfSubjects': 313, 'variableMeasured': ['ProcessingModule', 'BehavioralEpochs', 'OptogeneticSeries'], 'measurementTechnique': [{'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000971 has 33 NWB files.
7 of these NWB files are of type 1.
19 of these NWB files are of type 2.
2 of these NWB files are of type 3.
1 of these NWB files are of type 4.
4 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2024-06-17T18:23:59.830498-07:00']
  experiment_description: Compulsive behavior is a defining feature of disorders such as substance use disorders. Current evidence suggests that corticostriatal circuits control the expression of established compulsions, but little is known about the mechanisms regulating the development of compulsions. We hypothesized that dopamine, a critical modulator of striatal synaptic plasticity, could control alterations in corticostriatal circuits leading to the development of compulsions (defined here as continued reward seeking in the face of punishment). We used dual-site fiber photometry to measure dopamine axon activity in the dorsomedial striatum (DMS) and the dorsolateral striatum (DLS) as compulsions emerged. Individual variability in the speed with which compulsions emerged was predicted by DMS dopamine axon activity. Amplifying this dopamine signal accelerated animals' transitions to compulsion, whereas inhibition delayed it. In contrast, amplifying DLS dopamine signaling had no effect on the emergence of compulsions. These results establish DMS dopamine signaling as a key controller of the development of compulsive reward seeking.
  experimenter: ['Seiler, Jillian L.' 'Cosme, Caitlin V.' 'Sherathiya, Venus N.'
   'Schaid, Michael D.' 'Bianco, Joseph M.' 'Bridgemohan, Abigael S.'
   'Lerner, Talia N.']
  institution: Northwestern Unitersity
  keywords: ['dorsal striatum' 'dopamine' 'substantia nigra' 'reward learning'
   'habit formation' 'compulsive behavior'
   'punishment-resistant reward seeking' 'fiber photometry' 'optogenetics']
  lab: Lerner
  notes: Hemisphere with DMS: Left
  Experiment: Fiber Photometry
  Behavior: RI60
  Punishment Group: Punishment Resistant
  Did Not Learn: False
  
  related_publications: ['https://doi.org/10.1016/j.cub.2022.01.055']
  session_id: FP_PR_2020-06-16T13-05-50
  source_script: Created using NeuroConv v0.4.11
  Group /general/subject (Subject) 
  surgery: GCaMP7b in DMS & DLS projecting SNc, fiber photometry probes in DMS & DLS
  virus: AAV5-CAG-FLEX-jGCaMP7b-WPRE
  identifier: a1113c1a-edc5-463a-94ee-6a52fc8ed2f3
  Group /processing/behavior (ProcessingModule) Operant behavioral data from MedPC.
  MSN = FOOD_FR1 HT TTL (Both) 
  Box = 3
  Group /processing/behavior/reward_port_entry_times (Events) Reward port entry times
  Group /processing/behavior/right_nose_poke_times (Events) Right nose poke times
  Group /processing/behavior/right_reward_times (Events) Right reward times
  session_description: FR1 Habit Training with concurrent fiber photometry, rewards delivered on both left and right nose pokes
  session_start_time: 2020-06-16T13:05:50-05:51
  timestamps_reference_time: 2020-06-16T13:05:50-05:51


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2024-06-17T18:24:00.684366-07:00']
  experiment_description: Compulsive behavior is a defining feature of disorders such as substance use disorders. Current evidence suggests that corticostriatal circuits control the expression of established compulsions, but little is known about the mechanisms regulating the development of compulsions. We hypothesized that dopamine, a critical modulator of striatal synaptic plasticity, could control alterations in corticostriatal circuits leading to the development of compulsions (defined here as continued reward seeking in the face of punishment). We used dual-site fiber photometry to measure dopamine axon activity in the dorsomedial striatum (DMS) and the dorsolateral striatum (DLS) as compulsions emerged. Individual variability in the speed with which compulsions emerged was predicted by DMS dopamine axon activity. Amplifying this dopamine signal accelerated animals' transitions to compulsion, whereas inhibition delayed it. In contrast, amplifying DLS dopamine signaling had no effect on the emergence of compulsions. These results establish DMS dopamine signaling as a key controller of the development of compulsive reward seeking.
  experimenter: ['Seiler, Jillian L.' 'Cosme, Caitlin V.' 'Sherathiya, Venus N.'
   'Schaid, Michael D.' 'Bianco, Joseph M.' 'Bridgemohan, Abigael S.'
   'Lerner, Talia N.']
  institution: Northwestern Unitersity
  keywords: ['dorsal striatum' 'dopamine' 'substantia nigra' 'reward learning'
   'habit formation' 'compulsive behavior'
   'punishment-resistant reward seeking' 'fiber photometry' 'optogenetics']
  lab: Lerner
  notes: Hemisphere with DMS: Left
  Experiment: Fiber Photometry
  Behavior: RI60
  Punishment Group: Punishment Resistant
  Did Not Learn: False
  
  related_publications: ['https://doi.org/10.1016/j.cub.2022.01.055']
  session_id: FP_PR_2020-06-17T13-09-45
  source_script: Created using NeuroConv v0.4.11
  Group /general/subject (Subject) 
  surgery: GCaMP7b in DMS & DLS projecting SNc, fiber photometry probes in DMS & DLS
  virus: AAV5-CAG-FLEX-jGCaMP7b-WPRE
  identifier: 9a689057-40b0-40a6-9637-d376c1314a06
  Group /processing/behavior (ProcessingModule) Operant behavioral data from MedPC.
  MSN = FOOD_FR1 TTL Right 
  Box = 2
  Group /processing/behavior/left_nose_poke_times (Events) Left nose poke times
  Group /processing/behavior/reward_port_entry_times (Events) Reward port entry times
  Group /processing/behavior/right_nose_poke_times (Events) Right nose poke times
  Group /processing/behavior/right_reward_times (Events) Right reward times
  session_description: FR1 Training with concurrent fiber photometry, rewards delivered on right nose pokes
  session_start_time: 2020-06-17T13:09:45-05:51
  timestamps_reference_time: 2020-06-17T13:09:45-05:51


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/commanded_voltage_series_dls_calcium_signal (CommandedVoltageSeries) The commanded voltage for the DLS calcium signal.
  Group /acquisition/commanded_voltage_series_dls_isosbestic_control (CommandedVoltageSeries) The commanded voltage for the DLS isosbestic control.
  Group /acquisition/commanded_voltage_series_dms_calcium_signal (CommandedVoltageSeries) The commanded voltage for the DMS calcium signal.
  Group /acquisition/commanded_voltage_series_dms_isosbestic_control (CommandedVoltageSeries) The commanded voltage for the DMS isosbestic control.
  Group /acquisition/fiber_photometry_response_series (FiberPhotometryResponseSeries) The fluorescence from the DMS calcium signal, DMS isosbestic control, DLS calcium signal, and DLS isosbestic control.
  Dataset /acquisition/fiber_photometry_response_series/fiber_photometry_table_region (DynamicTableRegion) The region of the FiberPhotometryTable corresponding to the DMS calcium signal, DMS isosbestic control, DLS calcium signal, and DLS isosbestic control. | shape = (4,) | dtype = int64
  file_create_date: ['2024-06-17T18:06:54.590806-07:00']
  Group /general/devices/dichroic_mirror (DichroicMirror) Dual excitation band fiber photometry measurements use a Fluorescence Mini Cube with 4 ports: one port for the functional fluorescence excitation light, one for the isosbestic excitation, one for the fluorescence detection, and one for the sample. The cube has dichroic mirrors to combine isosbestic and fluorescence excitations and separate the fluorescence emission and narrow bandpass filters limiting the excitation fluorescence spectrum.
  Group /general/devices/dls_green_fluorophore (Indicator) Mice for fiber photometry experiments received infusions of 1ml of AAV5-CAG-FLEX-jGCaMP7b-WPRE (1.02e13 vg/mL, Addgene, lot 18-429) into lateral SNc (AP 3.1, ML 1.3, DV 4.2) in one hemisphere and medial SNc (AP 3.1, ML 0.8, DV 4.7) in the other. Hemispheres were counterbalanced between mice.
  Group /general/devices/dms_green_fluorophore (Indicator) Mice for fiber photometry experiments received infusions of 1ml of AAV5-CAG-FLEX-jGCaMP7b-WPRE (1.02e13 vg/mL, Addgene, lot 18-429) into lateral SNc (AP 3.1, ML 1.3, DV 4.2) in one hemisphere and medial SNc (AP 3.1, ML 0.8, DV 4.7) in the other. Hemispheres were counterbalanced between mice.
  Group /general/devices/emission_filter (BandOpticalFilter) Dual excitation band fiber photometry measurements use a Fluorescence Mini Cube with 4 ports: one port for the functional fluorescence excitation light, one for the isosbestic excitation, one for the fluorescence detection, and one for the sample. The cube has dichroic mirrors to combine isosbestic and fluorescence excitations and separate the fluorescence emission and narrow bandpass filters limiting the excitation fluorescence spectrum.
  Group /general/devices/excitation_filter (BandOpticalFilter) Dual excitation band fiber photometry measurements use a Fluorescence Mini Cube with 4 ports: one port for the functional fluorescence excitation light, one for the isosbestic excitation, one for the fluorescence detection, and one for the sample. The cube has dichroic mirrors to combine isosbestic and fluorescence excitations and separate the fluorescence emission and narrow bandpass filters limiting the excitation fluorescence spectrum.
  Group /general/devices/excitation_source_calcium_signal (ExcitationSource) 465nm and 405nm LEDs were modulated at 211 Hz and 330 Hz, respectively, for DMS probes. 465nm and 405nm LEDs were modulated at 450 Hz and 270 Hz, respectively for DLS probes. LED currents were adjusted in order to return a voltage between 150-200mV for each signal, were offset by 5 mA, were demodulated using a 4 Hz lowpass frequency filter.
  Group /general/devices/excitation_source_isosbestic_control (ExcitationSource) 465nm and 405nm LEDs were modulated at 211 Hz and 330 Hz, respectively, for DMS probes. 465nm and 405nm LEDs were modulated at 450 Hz and 270 Hz, respectively for DLS probes. LED currents were adjusted in order to return a voltage between 150-200mV for each signal, were offset by 5 mA, were demodulated using a 4 Hz lowpass frequency filter.
  Group /general/devices/isosbestic_excitation_filter (BandOpticalFilter) Dual excitation band fiber photometry measurements use a Fluorescence Mini Cube with 4 ports: one port for the functional fluorescence excitation light, one for the isosbestic excitation, one for the fluorescence detection, and one for the sample. The cube has dichroic mirrors to combine isosbestic and fluorescence excitations and separate the fluorescence emission and narrow bandpass filters limiting the excitation fluorescence spectrum.
  Group /general/devices/optical_fiber (OpticalFiber) Fiber optic implants (Doric Lenses; 400 um, 0.48 NA) were placed above DMS (AP 0.8, ML 1.5, DV 2.8) and DLS (AP 0.1, ML 2.8, DV 3.5). The DMS implant was placed in the hemisphere receiving a medial SNc viral injection, while the DLS implant was placed in the hemisphere receiving a lateral SNc viral injection. Calcium signals from dopamine terminals in DMS and DLS were recorded during RI30, on the first and last days of RI60/RR20 training as well as on both footshock probes for each mouse. All recordings were done using a fiber photometry rig with optical components from Doric lenses controlled by a real-time processor from Tucker Davis Technologies (TDT; RZ5P). TDT Synapse software was used for data acquisition.
  Group /general/devices/photodetector (Photodetector) This battery-operated photoreceiver has high gain and detects CW light signals in the sub-picowatt to nanowatt range. When used in conjunction with a modulated light source and a lock-in amplifier to reduce the measurement bandwidth, it achieves sensitivity levels in the femtowatt range. Doric offer this Newport product with add-on fiber optic adapter that improves coupling efficiency between the large core, high NA optical fibers used in Fiber Photometry and relatively small detector area. Its output analog voltage (0-5 V) can be monitored with an oscilloscope or with a DAQ board to record the data with a computer.
  experiment_description: Compulsive behavior is a defining feature of disorders such as substance use disorders. Current evidence suggests that corticostriatal circuits control the expression of established compulsions, but little is known about the mechanisms regulating the development of compulsions. We hypothesized that dopamine, a critical modulator of striatal synaptic plasticity, could control alterations in corticostriatal circuits leading to the development of compulsions (defined here as continued reward seeking in the face of punishment). We used dual-site fiber photometry to measure dopamine axon activity in the dorsomedial striatum (DMS) and the dorsolateral striatum (DLS) as compulsions emerged. Individual variability in the speed with which compulsions emerged was predicted by DMS dopamine axon activity. Amplifying this dopamine signal accelerated animals' transitions to compulsion, whereas inhibition delayed it. In contrast, amplifying DLS dopamine signaling had no effect on the emergence of compulsions. These results establish DMS dopamine signaling as a key controller of the development of compulsive reward seeking.
  experimenter: ['Seiler, Jillian L.' 'Cosme, Caitlin V.' 'Sherathiya, Venus N.'
   'Schaid, Michael D.' 'Bianco, Joseph M.' 'Bridgemohan, Abigael S.'
   'Lerner, Talia N.']
  Group /general/fiber_photometry (FiberPhotometry) 
  Group /general/fiber_photometry/fiber_photometry_table (FiberPhotometryTable) Fiber optic implants (Doric Lenses; 400 um, 0.48 NA) were placed above DMS (AP 0.8, ML 1.5, DV 2.8) and DLS (AP 0.1, ML 2.8, DV 3.5). The DMS implant was placed in the hemisphere receiving a medial SNc viral injection, while the DLS implant was placed in the hemisphere receiving a lateral SNc viral injection. Calcium signals from dopamine terminals in DMS and DLS were recorded during RI30, on the first and last days of RI60/RR20 training as well as on both footshock probes for each mouse. All recordings were done using a fiber photometry rig with optical components from Doric lenses controlled by a real-time processor from Tucker Davis Technologies (TDT; RZ5P). TDT Synapse software was used for data acquisition.
  Dataset /general/fiber_photometry/fiber_photometry_table/commanded_voltage_series (VectorData) Link to the commanded voltage series. | shape = (4,) | dtype = object
  Dataset /general/fiber_photometry/fiber_photometry_table/coordinates (VectorData) Fiber placement in stereotactic coordinates (AP, ML, DV) mm relative to Bregma. | shape = (4, 3) | dtype = float64
  Dataset /general/fiber_photometry/fiber_photometry_table/dichroic_mirror (VectorData) Link to the dichroic mirror device. | shape = (4,) | dtype = object
  Dataset /general/fiber_photometry/fiber_photometry_table/emission_filter (VectorData) Link to the emission filter device. | shape = (4,) | dtype = object
  Dataset /general/fiber_photometry/fiber_photometry_table/excitation_filter (VectorData) Link to the excitation filter device. | shape = (4,) | dtype = object
  Dataset /general/fiber_photometry/fiber_photometry_table/excitation_source (VectorData) Link to the excitation source device. | shape = (4,) | dtype = object
  Dataset /general/fiber_photometry/fiber_photometry_table/id (ElementIdentifiers)  | shape = (4,) | dtype = int64
  Dataset /general/fiber_photometry/fiber_photometry_table/indicator (VectorData) Link to the indicator object. | shape = (4,) | dtype = object
  Dataset /general/fiber_photometry/fiber_photometry_table/location (VectorData) Location of fiber. | shape = (4,) | dtype = object
  Dataset /general/fiber_photometry/fiber_photometry_table/optical_fiber (VectorData) Link to the optical fiber device. | shape = (4,) | dtype = object
  Dataset /general/fiber_photometry/fiber_photometry_table/photodetector (VectorData) Link to the photodetector device. | shape = (4,) | dtype = object
  institution: Northwestern Unitersity
  keywords: ['dorsal striatum' 'dopamine' 'substantia nigra' 'reward learning'
   'habit formation' 'compulsive behavior'
   'punishment-resistant reward seeking' 'fiber photometry' 'optogenetics']
  lab: Lerner
  notes: Hemisphere with DMS: Left
  Experiment: Fiber Photometry
  Behavior: RI60
  Punishment Group: Punishment Resistant
  Did Not Learn: False
  
  related_publications: ['https://doi.org/10.1016/j.cub.2022.01.055']
  session_id: FP_PR_2020-07-09T13-01-26
  source_script: Created using NeuroConv v0.4.11
  Group /general/subject (Subject) 
  surgery: GCaMP7b in DMS & DLS projecting SNc, fiber photometry probes in DMS & DLS
  virus: AAV5-CAG-FLEX-jGCaMP7b-WPRE
  identifier: 801759b8-d08a-4ce7-acca-839ba99ddfc3
  Group /processing/behavior (ProcessingModule) Operant behavioral data from MedPC.
  MSN = FOOD_RI 60 RIGHT TTL 
  Box = 2
  Group /processing/behavior/left_nose_poke_times (Events) Left nose poke times
  Group /processing/behavior/reward_port_entry_times (Events) Reward port entry times
  Group /processing/behavior/right_nose_poke_times (Events) Right nose poke times
  Group /processing/behavior/right_reward_times (Events) Right reward times
  session_description: RI60 Training with concurrent fiber photometry, rewards delivered on right nose pokes
  session_start_time: 2020-07-09T13:01:26-05:51
  timestamps_reference_time: 2020-07-09T13:01:26-05:51


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2024-06-17T18:24:05.986626-07:00']
  experiment_description: Compulsive behavior is a defining feature of disorders such as substance use disorders. Current evidence suggests that corticostriatal circuits control the expression of established compulsions, but little is known about the mechanisms regulating the development of compulsions. We hypothesized that dopamine, a critical modulator of striatal synaptic plasticity, could control alterations in corticostriatal circuits leading to the development of compulsions (defined here as continued reward seeking in the face of punishment). We used dual-site fiber photometry to measure dopamine axon activity in the dorsomedial striatum (DMS) and the dorsolateral striatum (DLS) as compulsions emerged. Individual variability in the speed with which compulsions emerged was predicted by DMS dopamine axon activity. Amplifying this dopamine signal accelerated animals' transitions to compulsion, whereas inhibition delayed it. In contrast, amplifying DLS dopamine signaling had no effect on the emergence of compulsions. These results establish DMS dopamine signaling as a key controller of the development of compulsive reward seeking.
  experimenter: ['Seiler, Jillian L.' 'Cosme, Caitlin V.' 'Sherathiya, Venus N.'
   'Schaid, Michael D.' 'Bianco, Joseph M.' 'Bridgemohan, Abigael S.'
   'Lerner, Talia N.']
  institution: Northwestern Unitersity
  keywords: ['dorsal striatum' 'dopamine' 'substantia nigra' 'reward learning'
   'habit formation' 'compulsive behavior'
   'punishment-resistant reward seeking' 'fiber photometry' 'optogenetics']
  lab: Lerner
  notes: Hemisphere with DMS: Left
  Experiment: Fiber Photometry
  Behavior: RI60
  Punishment Group: Punishment Resistant
  Did Not Learn: False
  
  related_publications: ['https://doi.org/10.1016/j.cub.2022.01.055']
  session_id: FP_PR_2020-07-10T12-50-36
  source_script: Created using NeuroConv v0.4.11
  Group /general/subject (Subject) 
  surgery: GCaMP7b in DMS & DLS projecting SNc, fiber photometry probes in DMS & DLS
  virus: AAV5-CAG-FLEX-jGCaMP7b-WPRE
  identifier: 2c2fed3b-75b7-472a-abfc-f25ade4879ca
  Group /processing/behavior (ProcessingModule) Operant behavioral data from MedPC.
  MSN = Footshock Degradation right 
  Box = 2
  Group /processing/behavior/footshock_times (Events) Footshock times
  Group /processing/behavior/reward_port_entry_times (Events) Reward port entry times
  Group /processing/behavior/right_nose_poke_times (Events) Right nose poke times
  Group /processing/behavior/right_reward_times (Events) Right reward times
  session_description: Footshock Probe, shocks delivered on right nose pokes
  session_start_time: 2020-07-10T12:50:36-05:51
  timestamps_reference_time: 2020-07-10T12:50:36-05:51


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2024-06-17T18:24:06.239080-07:00']
  experiment_description: Compulsive behavior is a defining feature of disorders such as substance use disorders. Current evidence suggests that corticostriatal circuits control the expression of established compulsions, but little is known about the mechanisms regulating the development of compulsions. We hypothesized that dopamine, a critical modulator of striatal synaptic plasticity, could control alterations in corticostriatal circuits leading to the development of compulsions (defined here as continued reward seeking in the face of punishment). We used dual-site fiber photometry to measure dopamine axon activity in the dorsomedial striatum (DMS) and the dorsolateral striatum (DLS) as compulsions emerged. Individual variability in the speed with which compulsions emerged was predicted by DMS dopamine axon activity. Amplifying this dopamine signal accelerated animals' transitions to compulsion, whereas inhibition delayed it. In contrast, amplifying DLS dopamine signaling had no effect on the emergence of compulsions. These results establish DMS dopamine signaling as a key controller of the development of compulsive reward seeking.
  experimenter: ['Seiler, Jillian L.' 'Cosme, Caitlin V.' 'Sherathiya, Venus N.'
   'Schaid, Michael D.' 'Bianco, Joseph M.' 'Bridgemohan, Abigael S.'
   'Lerner, Talia N.']
  institution: Northwestern Unitersity
  keywords: ['dorsal striatum' 'dopamine' 'substantia nigra' 'reward learning'
   'habit formation' 'compulsive behavior'
   'punishment-resistant reward seeking' 'fiber photometry' 'optogenetics']
  lab: Lerner
  notes: Hemisphere with DMS: Left
  Experiment: Fiber Photometry
  Behavior: RI60
  Punishment Group: Punishment Resistant
  Did Not Learn: False
  
  related_publications: ['https://doi.org/10.1016/j.cub.2022.01.055']
  session_id: FP_PR_2020-07-10T13-51-37
  source_script: Created using NeuroConv v0.4.11
  Group /general/subject (Subject) 
  surgery: GCaMP7b in DMS & DLS projecting SNc, fiber photometry probes in DMS & DLS
  virus: AAV5-CAG-FLEX-jGCaMP7b-WPRE
  identifier: a87d55cb-770d-4fa3-be81-336c4b62d6aa
  Group /processing/behavior (ProcessingModule) Operant behavioral data from MedPC.
  MSN = Probe Test Habit Training TTL 
  Box = 2
  Group /processing/behavior/reward_port_entry_times (Events) Reward port entry times
  Group /processing/behavior/right_nose_poke_times (Events) Right nose poke times
  session_description: Probe Test
  session_start_time: 2020-07-10T13:51:37-05:51
  timestamps_reference_time: 2020-07-10T13:51:37-05:51
