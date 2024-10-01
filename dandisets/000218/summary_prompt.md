
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000218/0.220131.1608
name: Routing of Hippocampal Ripples to Subcortical Structures via the Lateral Septum
contributor: [{'name': 'Tingley, David', 'roleName': ['dcite:Author', 'dcite:DataCollector', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Buzáki, Gyórgy', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'url': 'http://www.nih.gov/', 'name': 'National Institutes of Health', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01cwqze88', 'awardNumber': 'MH54671, MH107396, U19 NS107616, U19 NS104590, and NS090583', 'contactPoint': [], 'includeInCitation': False}, {'url': 'http://www.nsf.gov/', 'name': 'National Science Foundation', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/021nxhr62', 'awardNumber': 'NSF PIRE grant (no. 1545858)', 'contactPoint': [], 'includeInCitation': False}, {'url': 'http://www.thesimonsfoundation.ca/', 'name': 'Simons Foundation', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01cmst727', 'awardNumber': '351109', 'contactPoint': [], 'includeInCitation': False}]
description: The mnemonic functions of hippocampal sharp wave ripples (SPW-Rs) have been studied extensively. Because hippocampal outputs affect not only cortical but also subcortical targets, we examined the impact of SPW-Rs on the firing patterns of lateral septal (LS) neurons in behaving rats. A large fraction of SPW-Rs were temporally locked to high-frequency oscillations (HFOs) (120–180 Hz) in LS, with strongest coupling during non-rapid eye movement (NREM) sleep, followed by waking immobility. However, coherence and spike-local field potential (LFP) coupling between the two structures were low, suggesting that HFOs are generated locally within the LS GABAergic population. This hypothesis was supported by optogenetic induction of HFOs in LS. Spiking of LS neurons was largely independent of the sequential order of spiking in SPW-Rs but instead correlated with the magnitude of excitatory synchrony of the hippocampal output. Thus, LS is strongly activated by SPW-Rs and may convey hippocampal population events to its hypothalamic and brainstem targets.
assetsSummary: {'species': [{'name': 'Rattus norvegicus - Norway rat', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10116'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}, {'name': 'behavioral approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 1512863479850, 'numberOfFiles': 98, 'numberOfSubjects': 6, 'variableMeasured': ['LFP', 'Units', 'ProcessingModule', 'Position', 'CompassDirection', 'ElectricalSeries', 'SpatialSeries'], 'measurementTechnique': [{'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'signal filtering technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000218 has 26 NWB files.
11 of these NWB files are of type 1.
1 of these NWB files are of type 2.
12 of these NWB files are of type 3.
1 of these NWB files are of type 4.
1 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeries_raw (ElectricalSeries) Raw acquisition traces.
  Dataset /acquisition/ElectricalSeries_raw/electrodes (DynamicTableRegion) electrode_table_region | shape = (30,) | dtype = int64
  file_create_date: ['2022-01-28T17:03:48.754857+00:00']
  Group /general/devices/Neuronexus probe (4 x 1) (Device) according to author thse are reference sites a few millimeters dorsal from the restrecorded from an older neuronexus probe
  Group /general/devices/Neuronexus probe (4 x 8) (Device) A 4 (shanks) x 8 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  experimenter: ['David Tingley']
  Group /general/extracellular_ephys/Group1 (ElectrodeGroup) Group1 electrodes.
  Group /general/extracellular_ephys/Group1/device (Device) according to author thse are reference sites a few millimeters dorsal from the restrecorded from an older neuronexus probe
  Group /general/extracellular_ephys/Group2 (ElectrodeGroup) Group2 electrodes.
  Group /general/extracellular_ephys/Group2/device (Device) according to author thse are reference sites a few millimeters dorsal from the restrecorded from an older neuronexus probe
  Group /general/extracellular_ephys/Group3 (ElectrodeGroup) Group3 electrodes.
  Group /general/extracellular_ephys/Group3/device (Device) according to author thse are reference sites a few millimeters dorsal from the restrecorded from an older neuronexus probe
  Group /general/extracellular_ephys/Group4 (ElectrodeGroup) Group4 electrodes.
  Group /general/extracellular_ephys/Group4/device (Device) A 4 (shanks) x 8 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group5 (ElectrodeGroup) Group5 electrodes.
  Group /general/extracellular_ephys/Group5/device (Device) according to author thse are reference sites a few millimeters dorsal from the restrecorded from an older neuronexus probe
  Group /general/extracellular_ephys/Group6 (ElectrodeGroup) Group6 electrodes.
  Group /general/extracellular_ephys/Group6/device (Device) according to author thse are reference sites a few millimeters dorsal from the restrecorded from an older neuronexus probe
  Group /general/extracellular_ephys/Group7 (ElectrodeGroup) Group7 electrodes.
  Group /general/extracellular_ephys/Group7/device (Device) according to author thse are reference sites a few millimeters dorsal from the restrecorded from an older neuronexus probe
  Group /general/extracellular_ephys/Group8 (ElectrodeGroup) Group8 electrodes.
  Group /general/extracellular_ephys/Group8/device (Device) A 4 (shanks) x 8 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (30,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/gain_to_uV (VectorData) gain_to_uV | shape = (30,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (30,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (30,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (30,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (30,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (30,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/shank_electrode_number (VectorData) 0-indexed channel within a shank. | shape = (30,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (30,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (30,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (30,) | dtype = float64
  institution: NYU
  lab: Buzsaki
  related_publications: ['Tingley, David, and György Buzsáki. "Routing of hippocampal ripples to subcortical structures via the lateral septum." Neuron 105.1 (2020) 138-149.']
  session_id: DT1_rLS_20150723_1584um
  Group /general/subject (Subject) 
  identifier: 5a1df010-00a5-49d7-bcfa-00b358d8aa7b
  Group /processing/ecephys (ProcessingModule) Intermediate data from extracellular electrophysiology recordings, e.g., LFP.
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/ElectricalSeries_lfp (ElectricalSeries) Local field potential signal.
  Dataset /processing/ecephys/LFP/ElectricalSeries_lfp/electrodes (DynamicTableRegion) electrode_table_region | shape = (30,) | dtype = int64
  session_description: The mnemonic functions of hippocampal sharp wave ripples (SPW-Rs) have been studied extensively. Because hippocampal outputs affect not only cortical but also subcortical targets, we examined the impact of SPW-Rs on the firing patterns of lateral septal (LS) neurons in behaving rats. A large fraction of SPW-Rs were temporally locked to high-frequency oscillations (HFOs) (120–180 Hz) in LS, with strongest coupling during non-rapid eye movement (NREM) sleep, followed by waking immobility. However, coherence and spike-local field potential (LFP) coupling between the two structures were low, suggesting that HFOs are generated locally within the LS GABAergic population. This hypothesis was supported by optogenetic induction of HFOs in LS. Spiking of LS neurons was largely independent of the sequential order of spiking in SPW-Rs but instead correlated with the magnitude of excitatory synchrony of the hippocampal output. Thus, LS is strongly activated by SPW-Rs and may convey hippocampal population events to its hypothalamic and brainstem targets.
  session_start_time: 2015-07-23T00:00:00-04:00
  timestamps_reference_time: 2015-07-23T00:00:00-04:00
  Group /units (Units) Autogenerated by nwb_conversion_tools.
  Dataset /units/clu_id (VectorData) 0-indexed id of cluster identified from the shank. | shape = (74,) | dtype = int64
  Dataset /units/group_id (VectorData) The electrode group ID that each unit was identified by. | shape = (74,) | dtype = object
  Dataset /units/id (ElementIdentifiers)  | shape = (74,) | dtype = int64
  Dataset /units/location (VectorData) Brain region where each unit was detected. | shape = (74,) | dtype = object
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (876627,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (74,) | dtype = uint32


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeries_raw (ElectricalSeries) Raw acquisition traces.
  Dataset /acquisition/ElectricalSeries_raw/electrodes (DynamicTableRegion) electrode_table_region | shape = (30,) | dtype = int64
  file_create_date: ['2022-01-28T16:41:05.280041+00:00']
  Group /general/devices/Device_ecephys (Device) Ecephys probe. Automatically generated.
  Group /general/devices/Neuronexus probe (4 x 1) (Device) according to author thse are reference sites a few millimeters dorsal from the restrecorded from an older neuronexus probe
  Group /general/devices/Neuronexus probe (4 x 8) (Device) A 4 (shanks) x 8 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  experimenter: ['David Tingley']
  Group /general/extracellular_ephys/Group1 (ElectrodeGroup) Group1 electrodes.
  Group /general/extracellular_ephys/Group1/device (Device) A 4 (shanks) x 8 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group2 (ElectrodeGroup) Group2 electrodes.
  Group /general/extracellular_ephys/Group2/device (Device) according to author thse are reference sites a few millimeters dorsal from the restrecorded from an older neuronexus probe
  Group /general/extracellular_ephys/Group3 (ElectrodeGroup) Group3 electrodes.
  Group /general/extracellular_ephys/Group3/device (Device) according to author thse are reference sites a few millimeters dorsal from the restrecorded from an older neuronexus probe
  Group /general/extracellular_ephys/Group4 (ElectrodeGroup) Group4 electrodes.
  Group /general/extracellular_ephys/Group4/device (Device) according to author thse are reference sites a few millimeters dorsal from the restrecorded from an older neuronexus probe
  Group /general/extracellular_ephys/Group5 (ElectrodeGroup) Group5 electrodes.
  Group /general/extracellular_ephys/Group5/device (Device) according to author thse are reference sites a few millimeters dorsal from the restrecorded from an older neuronexus probe
  Group /general/extracellular_ephys/Group6 (ElectrodeGroup) Group6 electrodes.
  Group /general/extracellular_ephys/Group6/device (Device) according to author thse are reference sites a few millimeters dorsal from the restrecorded from an older neuronexus probe
  Group /general/extracellular_ephys/Group7 (ElectrodeGroup) Group7 electrodes.
  Group /general/extracellular_ephys/Group7/device (Device) A 4 (shanks) x 8 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group8 (ElectrodeGroup) Group8 electrodes.
  Group /general/extracellular_ephys/Group8/device (Device) according to author thse are reference sites a few millimeters dorsal from the restrecorded from an older neuronexus probe
  Group /general/extracellular_ephys/Group9 (ElectrodeGroup) Group9 electrodes.
  Group /general/extracellular_ephys/Group9/device (Device) Ecephys probe. Automatically generated.
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (30,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/gain_to_uV (VectorData) gain_to_uV | shape = (30,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (30,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (30,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (30,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (30,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (30,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/shank_electrode_number (VectorData) 0-indexed channel within a shank. | shape = (30,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (30,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (30,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (30,) | dtype = float64
  institution: NYU
  lab: Buzsaki
  related_publications: ['Tingley, David, and György Buzsáki. "Routing of hippocampal ripples to subcortical structures via the lateral septum." Neuron 105.1 (2020) 138-149.']
  session_id: DT1_rLS_20150725_1944um
  Group /general/subject (Subject) 
  identifier: e52bf6ae-5c29-4dc6-8353-1c13cdf8bfcb
  Group /processing/ecephys (ProcessingModule) Intermediate data from extracellular electrophysiology recordings, e.g., LFP.
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/ElectricalSeries_lfp (ElectricalSeries) Local field potential signal.
  Dataset /processing/ecephys/LFP/ElectricalSeries_lfp/electrodes (DynamicTableRegion) electrode_table_region | shape = (30,) | dtype = int64
  session_description: The mnemonic functions of hippocampal sharp wave ripples (SPW-Rs) have been studied extensively. Because hippocampal outputs affect not only cortical but also subcortical targets, we examined the impact of SPW-Rs on the firing patterns of lateral septal (LS) neurons in behaving rats. A large fraction of SPW-Rs were temporally locked to high-frequency oscillations (HFOs) (120–180 Hz) in LS, with strongest coupling during non-rapid eye movement (NREM) sleep, followed by waking immobility. However, coherence and spike-local field potential (LFP) coupling between the two structures were low, suggesting that HFOs are generated locally within the LS GABAergic population. This hypothesis was supported by optogenetic induction of HFOs in LS. Spiking of LS neurons was largely independent of the sequential order of spiking in SPW-Rs but instead correlated with the magnitude of excitatory synchrony of the hippocampal output. Thus, LS is strongly activated by SPW-Rs and may convey hippocampal population events to its hypothalamic and brainstem targets.
  session_start_time: 2015-07-25T00:00:00-04:00
  timestamps_reference_time: 2015-07-25T00:00:00-04:00
  Group /units (Units) Autogenerated by nwb_conversion_tools.
  Dataset /units/clu_id (VectorData) 0-indexed id of cluster identified from the shank. | shape = (43,) | dtype = int64
  Dataset /units/group_id (VectorData) The electrode group ID that each unit was identified by. | shape = (43,) | dtype = object
  Dataset /units/id (ElementIdentifiers)  | shape = (43,) | dtype = int64
  Dataset /units/location (VectorData) Brain region where each unit was detected. | shape = (43,) | dtype = object
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (983431,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (43,) | dtype = uint32


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeries_raw (ElectricalSeries) Raw acquisition traces.
  Dataset /acquisition/ElectricalSeries_raw/electrodes (DynamicTableRegion) electrode_table_region | shape = (128,) | dtype = int64
  file_create_date: ['2022-01-28T16:17:21.981401+00:00']
  Group /general/devices/Neuronexus probe (4 x 1) (Device) according to author thse are reference sites a few millimeters dorsal from the restrecorded from an older neuronexus probe
  Group /general/devices/Neuronexus probe (5 x 12) (Device) A 5 (shanks) x 12 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/devices/Neuronexus probe (6 x 10) (Device) A 6 (shanks) x 10 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  experimenter: ['David Tingley']
  Group /general/extracellular_ephys/Group1 (ElectrodeGroup) Group1 electrodes.
  Group /general/extracellular_ephys/Group1/device (Device) A 5 (shanks) x 12 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group10 (ElectrodeGroup) Group10 electrodes.
  Group /general/extracellular_ephys/Group10/device (Device) A 6 (shanks) x 10 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group11 (ElectrodeGroup) Group11 electrodes.
  Group /general/extracellular_ephys/Group11/device (Device) A 6 (shanks) x 10 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group12 (ElectrodeGroup) Group12 electrodes.
  Group /general/extracellular_ephys/Group12/device (Device) A 6 (shanks) x 10 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group13 (ElectrodeGroup) Group13 electrodes.
  Group /general/extracellular_ephys/Group13/device (Device) according to author thse are reference sites a few millimeters dorsal from the restrecorded from an older neuronexus probe
  Group /general/extracellular_ephys/Group2 (ElectrodeGroup) Group2 electrodes.
  Group /general/extracellular_ephys/Group2/device (Device) A 5 (shanks) x 12 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group3 (ElectrodeGroup) Group3 electrodes.
  Group /general/extracellular_ephys/Group3/device (Device) A 5 (shanks) x 12 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group4 (ElectrodeGroup) Group4 electrodes.
  Group /general/extracellular_ephys/Group4/device (Device) A 5 (shanks) x 12 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group5 (ElectrodeGroup) Group5 electrodes.
  Group /general/extracellular_ephys/Group5/device (Device) A 5 (shanks) x 12 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group6 (ElectrodeGroup) Group6 electrodes.
  Group /general/extracellular_ephys/Group6/device (Device) according to author thse are reference sites a few millimeters dorsal from the restrecorded from an older neuronexus probe
  Group /general/extracellular_ephys/Group7 (ElectrodeGroup) Group7 electrodes.
  Group /general/extracellular_ephys/Group7/device (Device) A 6 (shanks) x 10 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group8 (ElectrodeGroup) Group8 electrodes.
  Group /general/extracellular_ephys/Group8/device (Device) A 6 (shanks) x 10 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group9 (ElectrodeGroup) Group9 electrodes.
  Group /general/extracellular_ephys/Group9/device (Device) A 6 (shanks) x 10 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/gain_to_uV (VectorData) gain_to_uV | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/shank_electrode_number (VectorData) 0-indexed channel within a shank. | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (128,) | dtype = float64
  institution: NYU
  lab: Buzsaki
  related_publications: ['Tingley, David, and György Buzsáki. "Routing of hippocampal ripples to subcortical structures via the lateral septum." Neuron 105.1 (2020) 138-149.']
  session_id: DT2_rPPC_rCCG_3036um_362um_20160215_160215_122710
  Group /general/subject (Subject) 
  identifier: 67885b52-ebb9-4b68-b5c7-8e267e7b0c8a
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (3,) | dtype = int64
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (3,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (3,) | dtype = float64
  Dataset /intervals/epochs/tags (VectorData) user-defined tags | shape = (3,) | dtype = object
  Dataset /intervals/epochs/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (3,) | dtype = uint8
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/direction (VectorData) direction of the trial | shape = (77,) | dtype = object
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (77,) | dtype = int64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (77,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (77,) | dtype = float64
  Dataset /intervals/trials/trial_type (VectorData) type of trial | shape = (77,) | dtype = object
  Group /processing/behavior (ProcessingModule) Contains behavioral data concerning position.
  Group /processing/behavior/wheel_alternation_task (Position) 
  Group /processing/behavior/wheel_alternation_task/position (SpatialSeries) (x,y,z) coordinates tracking subject movement.
  Group /processing/ecephys (ProcessingModule) Intermediate data from extracellular electrophysiology recordings, e.g., LFP.
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/ElectricalSeries_lfp (ElectricalSeries) Local field potential signal.
  Dataset /processing/ecephys/LFP/ElectricalSeries_lfp/electrodes (DynamicTableRegion) electrode_table_region | shape = (128,) | dtype = int64
  Group /processing/ecephys/sleep_states (TimeIntervals) Sleep state of the animal.
  Dataset /processing/ecephys/sleep_states/id (ElementIdentifiers)  | shape = (110,) | dtype = int64
  Dataset /processing/ecephys/sleep_states/label (VectorData) Sleep state. | shape = (110,) | dtype = object
  Dataset /processing/ecephys/sleep_states/start_time (VectorData) Start time of epoch, in seconds | shape = (110,) | dtype = float64
  Dataset /processing/ecephys/sleep_states/stop_time (VectorData) Stop time of epoch, in seconds | shape = (110,) | dtype = float64
  session_description: The mnemonic functions of hippocampal sharp wave ripples (SPW-Rs) have been studied extensively. Because hippocampal outputs affect not only cortical but also subcortical targets, we examined the impact of SPW-Rs on the firing patterns of lateral septal (LS) neurons in behaving rats. A large fraction of SPW-Rs were temporally locked to high-frequency oscillations (HFOs) (120–180 Hz) in LS, with strongest coupling during non-rapid eye movement (NREM) sleep, followed by waking immobility. However, coherence and spike-local field potential (LFP) coupling between the two structures were low, suggesting that HFOs are generated locally within the LS GABAergic population. This hypothesis was supported by optogenetic induction of HFOs in LS. Spiking of LS neurons was largely independent of the sequential order of spiking in SPW-Rs but instead correlated with the magnitude of excitatory synchrony of the hippocampal output. Thus, LS is strongly activated by SPW-Rs and may convey hippocampal population events to its hypothalamic and brainstem targets.
  session_start_time: 2016-02-15T12:27:10-05:00
  timestamps_reference_time: 2016-02-15T12:27:10-05:00
  Group /units (Units) Autogenerated by nwb_conversion_tools.
  Dataset /units/clu_id (VectorData) 0-indexed id of cluster identified from the shank. | shape = (37,) | dtype = int64
  Dataset /units/group_id (VectorData) The electrode group ID that each unit was identified by. | shape = (37,) | dtype = object
  Dataset /units/id (ElementIdentifiers)  | shape = (37,) | dtype = int64
  Dataset /units/location (VectorData) Brain region where each unit was detected. | shape = (37,) | dtype = object
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (250659,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (37,) | dtype = uint32


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeries_raw (ElectricalSeries) Raw acquisition traces.
  Dataset /acquisition/ElectricalSeries_raw/electrodes (DynamicTableRegion) electrode_table_region | shape = (128,) | dtype = int64
  file_create_date: ['2022-01-28T16:14:58.430122+00:00']
  Group /general/devices/Neuronexus probe (4 x 1) (Device) according to author thse are reference sites a few millimeters dorsal from the restrecorded from an older neuronexus probe
  Group /general/devices/Neuronexus probe (5 x 12) (Device) A 5 (shanks) x 12 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/devices/Neuronexus probe (6 x 10) (Device) A 6 (shanks) x 10 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  experimenter: ['David Tingley']
  Group /general/extracellular_ephys/Group1 (ElectrodeGroup) Group1 electrodes.
  Group /general/extracellular_ephys/Group1/device (Device) A 5 (shanks) x 12 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group10 (ElectrodeGroup) Group10 electrodes.
  Group /general/extracellular_ephys/Group10/device (Device) A 6 (shanks) x 10 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group11 (ElectrodeGroup) Group11 electrodes.
  Group /general/extracellular_ephys/Group11/device (Device) A 6 (shanks) x 10 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group12 (ElectrodeGroup) Group12 electrodes.
  Group /general/extracellular_ephys/Group12/device (Device) A 6 (shanks) x 10 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group13 (ElectrodeGroup) Group13 electrodes.
  Group /general/extracellular_ephys/Group13/device (Device) according to author thse are reference sites a few millimeters dorsal from the restrecorded from an older neuronexus probe
  Group /general/extracellular_ephys/Group2 (ElectrodeGroup) Group2 electrodes.
  Group /general/extracellular_ephys/Group2/device (Device) A 5 (shanks) x 12 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group3 (ElectrodeGroup) Group3 electrodes.
  Group /general/extracellular_ephys/Group3/device (Device) A 5 (shanks) x 12 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group4 (ElectrodeGroup) Group4 electrodes.
  Group /general/extracellular_ephys/Group4/device (Device) A 5 (shanks) x 12 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group5 (ElectrodeGroup) Group5 electrodes.
  Group /general/extracellular_ephys/Group5/device (Device) A 5 (shanks) x 12 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group6 (ElectrodeGroup) Group6 electrodes.
  Group /general/extracellular_ephys/Group6/device (Device) according to author thse are reference sites a few millimeters dorsal from the restrecorded from an older neuronexus probe
  Group /general/extracellular_ephys/Group7 (ElectrodeGroup) Group7 electrodes.
  Group /general/extracellular_ephys/Group7/device (Device) A 6 (shanks) x 10 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group8 (ElectrodeGroup) Group8 electrodes.
  Group /general/extracellular_ephys/Group8/device (Device) A 6 (shanks) x 10 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group9 (ElectrodeGroup) Group9 electrodes.
  Group /general/extracellular_ephys/Group9/device (Device) A 6 (shanks) x 10 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/gain_to_uV (VectorData) gain_to_uV | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/shank_electrode_number (VectorData) 0-indexed channel within a shank. | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (128,) | dtype = float64
  institution: NYU
  lab: Buzsaki
  related_publications: ['Tingley, David, and György Buzsáki. "Routing of hippocampal ripples to subcortical structures via the lateral septum." Neuron 105.1 (2020) 138-149.']
  session_id: DT2_rPPC_rCCG_3108um_434um_20160215_160215_161846
  Group /general/subject (Subject) 
  identifier: 9937056d-e0e2-4ece-9b02-bb3434ec24ad
  Group /processing/ecephys (ProcessingModule) Intermediate data from extracellular electrophysiology recordings, e.g., LFP.
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/ElectricalSeries_lfp (ElectricalSeries) Local field potential signal.
  Dataset /processing/ecephys/LFP/ElectricalSeries_lfp/electrodes (DynamicTableRegion) electrode_table_region | shape = (128,) | dtype = int64
  session_description: The mnemonic functions of hippocampal sharp wave ripples (SPW-Rs) have been studied extensively. Because hippocampal outputs affect not only cortical but also subcortical targets, we examined the impact of SPW-Rs on the firing patterns of lateral septal (LS) neurons in behaving rats. A large fraction of SPW-Rs were temporally locked to high-frequency oscillations (HFOs) (120–180 Hz) in LS, with strongest coupling during non-rapid eye movement (NREM) sleep, followed by waking immobility. However, coherence and spike-local field potential (LFP) coupling between the two structures were low, suggesting that HFOs are generated locally within the LS GABAergic population. This hypothesis was supported by optogenetic induction of HFOs in LS. Spiking of LS neurons was largely independent of the sequential order of spiking in SPW-Rs but instead correlated with the magnitude of excitatory synchrony of the hippocampal output. Thus, LS is strongly activated by SPW-Rs and may convey hippocampal population events to its hypothalamic and brainstem targets.
  session_start_time: 2016-02-15T16:18:46-05:00
  timestamps_reference_time: 2016-02-15T16:18:46-05:00


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2022-01-28T17:17:23.208066+00:00']
  Group /general/devices/Neuronexus probe (4 x 1) (Device) according to author thse are reference sites a few millimeters dorsal from the restrecorded from an older neuronexus probe
  Group /general/devices/Neuronexus probe (4 x 8) (Device) A 4 (shanks) x 8 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/devices/Neuronexus probe (5 x 12) (Device) A 5 (shanks) x 12 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  experimenter: ['David Tingley']
  Group /general/extracellular_ephys/Group1 (ElectrodeGroup) Group1 electrodes.
  Group /general/extracellular_ephys/Group1/device (Device) A 4 (shanks) x 8 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group10 (ElectrodeGroup) Group10 electrodes.
  Group /general/extracellular_ephys/Group10/device (Device) according to author thse are reference sites a few millimeters dorsal from the restrecorded from an older neuronexus probe
  Group /general/extracellular_ephys/Group2 (ElectrodeGroup) Group2 electrodes.
  Group /general/extracellular_ephys/Group2/device (Device) A 4 (shanks) x 8 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group3 (ElectrodeGroup) Group3 electrodes.
  Group /general/extracellular_ephys/Group3/device (Device) A 4 (shanks) x 8 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group4 (ElectrodeGroup) Group4 electrodes.
  Group /general/extracellular_ephys/Group4/device (Device) A 4 (shanks) x 8 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group5 (ElectrodeGroup) Group5 electrodes.
  Group /general/extracellular_ephys/Group5/device (Device) A 5 (shanks) x 12 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group6 (ElectrodeGroup) Group6 electrodes.
  Group /general/extracellular_ephys/Group6/device (Device) A 5 (shanks) x 12 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group7 (ElectrodeGroup) Group7 electrodes.
  Group /general/extracellular_ephys/Group7/device (Device) A 5 (shanks) x 12 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group8 (ElectrodeGroup) Group8 electrodes.
  Group /general/extracellular_ephys/Group8/device (Device) A 5 (shanks) x 12 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/Group9 (ElectrodeGroup) Group9 electrodes.
  Group /general/extracellular_ephys/Group9/device (Device) A 5 (shanks) x 12 (electrodes) silicon probe from Neuronexus. Electrophysiological data were acquired using an Intan RHD2000 system (Intan Technologies LLC) digitized with 20 kHz rate.
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/gain_to_uV (VectorData) gain_to_uV | shape = (96,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (96,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (96,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (96,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/shank_electrode_number (VectorData) 0-indexed channel within a shank. | shape = (96,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (96,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (96,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (96,) | dtype = float64
  institution: NYU
  lab: Buzsaki
  related_publications: ['Tingley, David, and György Buzsáki. "Routing of hippocampal ripples to subcortical structures via the lateral septum." Neuron 105.1 (2020) 138-149.']
  session_id: 20161007_720um_720um_merge
  Group /general/subject (Subject) 
  identifier: badac1b6-dd3d-490c-ac70-4f97efcbf725
  Group /processing/ecephys (ProcessingModule) Intermediate data from extracellular electrophysiology recordings, e.g., LFP.
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/ElectricalSeries_lfp (ElectricalSeries) Local field potential signal.
  Dataset /processing/ecephys/LFP/ElectricalSeries_lfp/electrodes (DynamicTableRegion) electrode_table_region | shape = (96,) | dtype = int64
  session_description: The mnemonic functions of hippocampal sharp wave ripples (SPW-Rs) have been studied extensively. Because hippocampal outputs affect not only cortical but also subcortical targets, we examined the impact of SPW-Rs on the firing patterns of lateral septal (LS) neurons in behaving rats. A large fraction of SPW-Rs were temporally locked to high-frequency oscillations (HFOs) (120–180 Hz) in LS, with strongest coupling during non-rapid eye movement (NREM) sleep, followed by waking immobility. However, coherence and spike-local field potential (LFP) coupling between the two structures were low, suggesting that HFOs are generated locally within the LS GABAergic population. This hypothesis was supported by optogenetic induction of HFOs in LS. Spiking of LS neurons was largely independent of the sequential order of spiking in SPW-Rs but instead correlated with the magnitude of excitatory synchrony of the hippocampal output. Thus, LS is strongly activated by SPW-Rs and may convey hippocampal population events to its hypothalamic and brainstem targets.
  session_start_time: 2016-10-07T00:00:00-04:00
  timestamps_reference_time: 2016-10-07T00:00:00-04:00
  Group /units (Units) Autogenerated by nwb_conversion_tools.
  Dataset /units/id (ElementIdentifiers)  | shape = (13,) | dtype = int64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (1046930,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (13,) | dtype = uint32
