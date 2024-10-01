
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000618/draft
name: SpikeForest ground truth datasets
contributor: [{'name': 'Magland, Jeremy', 'email': 'jmagland@flatironinstitute.org', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Jun, James J', 'roleName': [], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Lovero, Elizabeth', 'roleName': [], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Morley, Alexander J', 'roleName': [], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Hurwitz, Cole Lincoln', 'roleName': [], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Buccino, Alessio Paolo', 'roleName': [], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Garcia, Samuel', 'roleName': [], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Barnett, Alex H', 'roleName': [], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'English, Daniel', 'roleName': [], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}]
description: The SpikeForest project contains a collection of electrophysiological recordings together with ground truth spiking information for the purpose of benchmarking the performance of spike sorting algorithms. In this dandiset we provide a subset of these recordings together with ground truth.

This dataset was prepared using the following script: https://github.com/flatironinstitute/spikeforest/blob/main/devel/dandiset/prepare_dandiset.py

For more information, see https://elifesciences.org/articles/55167
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}, {'name': 'Rattus norvegicus - Norway rat', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10116'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 145521718882, 'numberOfFiles': 124, 'numberOfSubjects': 4, 'variableMeasured': ['Units', 'ElectricalSeries', 'ElectrodeGroup', 'ProcessingModule'], 'measurementTechnique': [{'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000618 has 100 NWB files.
20 of these NWB files are of type 1.
60 of these NWB files are of type 2.
1 of these NWB files are of type 3.
19 of these NWB files are of type 4.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeries (ElectricalSeries) Raw acquisition traces
  Dataset /acquisition/ElectricalSeries/electrodes (DynamicTableRegion) all electrodes | shape = (32,) | dtype = int64
  file_create_date: ['2023-08-04T11:17:22.864532-04:00']
  Group /general/devices/Neuronexus (Device) Neuronexus silicon probe
  experiment_description: # Silicon-juxtacellular hybrid probes
  This studyset consists of 29 paired recordings from Silicon-juxtacellular hybrid probes. Juxtacellular electrodes are pulled from 1 mm OD 0.7 mm ID borosilicate glass and have impedances of 8-10 MOhm when filled with 130 mM potassium acetate. These juxtacellular electrodes are glued to 32 channel silicon probes (A1-32-Poly3, Neuronexus) using light-cure dental acrylic. Using the inter-site spacing of the silicon probe as a visual distance guide, the tip of the juxtacellular is fixed at a distance of ~20 micrometers from the nearest silicon probe recording site. The closest site is selected as a site in the middle (top to bottom) of an outer column of recording sites. The close distance between the juxtacellular tip and the recording sites results in both devices recording the same neuron at high probability. 
  
  #  Recording ground truth data in awake behaving mice
  Mice are placed in the head-fixed treadmill apparatus and the protective silicon elastomer is removed from the craniotomy, the juxtacellular-silicon hybrid prove is inserted 0.1 mm into the brain, and the craniotomy is covered with silicon fluid to prevent drying and improve stability. The probe is advanced into the brain at ~1-2 micrometers until action potentials are observed on the juxtacellular electrode, at which point movement is ceased and data collection begins.  Electrical signals from the juxtacellular electrode are recorded and amplified through an analog microelectrode amplifier (Cygnus IR-183), then digitized via an Intan RHD2000 system. Signals from the silicon probe are amplified and digitized through the same RHD2000 system, which results in hardware synchronization of the two signals. By converting the digital signals in the RHD2000 to analog voltage and outputting them to a digital microprocessor (CED Power1401), we calculated online the juxtacellular spike triggered average of each channel of the extracellular electrode, and discard recordings in which the triggered average does not contain a spike waveform on any channel.
  
  experimenter: ['English, D. F.']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (32,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/label (VectorData) electrode label | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) x coordinate | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) y coordinate | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) z coordinate | shape = (32,) | dtype = float64
  Group /general/extracellular_ephys/main (ElectrodeGroup) main electrode group
  Group /general/extracellular_ephys/main/device (Device) Neuronexus silicon probe
  institution: Virginia Tech
  keywords: ['silicon probe' 'juxtacellular' 'ground truth']
  lab: English Lab
  session_id: paired_english/m108_191125_163508
  Group /general/subject (Subject) 
  identifier: 1e95bd5a-532b-4413-b6e2-3f2b96adc404
  session_description: SpikeForest recording: PAIRED_ENGLISH/paired_english/m108_191125_163508
  session_start_time: 1970-01-01T00:00:00-05:00
  timestamps_reference_time: 1970-01-01T00:00:00-05:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (15490,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (1,) | dtype = uint16


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeries (ElectricalSeries) Raw acquisition traces
  Dataset /acquisition/ElectricalSeries/electrodes (DynamicTableRegion) all electrodes | shape = (16,) | dtype = int64
  file_create_date: ['2023-08-07T13:21:46.569579-04:00']
  Group /general/devices/Simulation (Device) Simulation
  experiment_description: # Hybrid janelia
  Hybrid recording with a sinusoidal probe drift.
  Drift was generated using 2D interpolation (Modified Akima).
  Waveform templates were recorded using 5 um spaced electrodes, see Kampff lab Ultradense Survey, and later subsampled to match the Neuropixels electrode spacing.
  Background noise was generated using ~1/f random noise that matches experimental neural recordings.
  Generated by Kilosort2\eMouse_drift code available on Github.
  Two sine wave periods were present in the drift (20 um amplitude) for the full recording duration (1200 s).
  
  Recording format:
  int16 raw format (channels x time order).
  1200s recording was divided to various length (600s, 1200s).
  64 channels were divided to various sub channels (4, 16, 32, 64) at various probe locations.
  
  References:
  https://github.com/MouseLand/Kilosort2
  https://github.com/MouseLand/Kilosort2/wiki/4.-eMouse-simulator-with-drift
  Kampff lab Ultradense Survey
  
  experimenter: ['Simulated']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (16,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (16,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (16,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/label (VectorData) electrode label | shape = (16,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (16,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) x coordinate | shape = (16,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) y coordinate | shape = (16,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) z coordinate | shape = (16,) | dtype = float64
  Group /general/extracellular_ephys/main (ElectrodeGroup) main electrode group
  Group /general/extracellular_ephys/main/device (Device) Simulation
  institution: Janelia Research Campus
  keywords: ['ground truth' 'simulation']
  lab: Janelia Research Campus
  session_id: hybrid_drift_siprobe/rec_16c_1200s_11
  Group /general/subject (Subject) 
  identifier: 1d2f363e-b56e-4e8b-ac7f-3b2c7fa2f93d
  session_description: SpikeForest recording: HYBRID_JANELIA/hybrid_drift_siprobe/rec_16c_1200s_11
  session_start_time: 1970-01-01T00:00:00-05:00
  timestamps_reference_time: 1970-01-01T00:00:00-05:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/id (ElementIdentifiers)  | shape = (74,) | dtype = int64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (482868,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (74,) | dtype = uint32


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2023-08-09T15:50:45.087075-04:00']
  experiment_description: # Silicon-juxtacellular hybrid probes
  This studyset consists of 29 paired recordings from Silicon-juxtacellular hybrid probes. Juxtacellular electrodes are pulled from 1 mm OD 0.7 mm ID borosilicate glass and have impedances of 8-10 MOhm when filled with 130 mM potassium acetate. These juxtacellular electrodes are glued to 32 channel silicon probes (A1-32-Poly3, Neuronexus) using light-cure dental acrylic. Using the inter-site spacing of the silicon probe as a visual distance guide, the tip of the juxtacellular is fixed at a distance of ~20 micrometers from the nearest silicon probe recording site. The closest site is selected as a site in the middle (top to bottom) of an outer column of recording sites. The close distance between the juxtacellular tip and the recording sites results in both devices recording the same neuron at high probability. 
  
  #  Recording ground truth data in awake behaving mice
  Mice are placed in the head-fixed treadmill apparatus and the protective silicon elastomer is removed from the craniotomy, the juxtacellular-silicon hybrid prove is inserted 0.1 mm into the brain, and the craniotomy is covered with silicon fluid to prevent drying and improve stability. The probe is advanced into the brain at ~1-2 micrometers until action potentials are observed on the juxtacellular electrode, at which point movement is ceased and data collection begins.  Electrical signals from the juxtacellular electrode are recorded and amplified through an analog microelectrode amplifier (Cygnus IR-183), then digitized via an Intan RHD2000 system. Signals from the silicon probe are amplified and digitized through the same RHD2000 system, which results in hardware synchronization of the two signals. By converting the digital signals in the RHD2000 to analog voltage and outputting them to a digital microprocessor (CED Power1401), we calculated online the juxtacellular spike triggered average of each channel of the extracellular electrode, and discard recordings in which the triggered average does not contain a spike waveform on any channel.
  
  experimenter: ['English, D. F.']
  institution: Virginia Tech
  keywords: ['silicon probe' 'juxtacellular' 'ground truth']
  lab: English Lab
  session_id: paired_english/m139_200114_222743
  Group /general/subject (Subject) 
  identifier: f6552ffb-3ac9-4e7f-a901-8130583ed514
  Group /processing/ecephys (ProcessingModule) ground_truth_units
  Group /processing/ecephys/ground_truth_units (Units) data on spiking units
  Dataset /processing/ecephys/ground_truth_units/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /processing/ecephys/ground_truth_units/spike_times (VectorData) the spike times for each unit | shape = (3401,) | dtype = float64
  Dataset /processing/ecephys/ground_truth_units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (1,) | dtype = uint16
  session_description: SpikeForest recording: PAIRED_ENGLISH/paired_english/m139_200114_222743
  session_start_time: 1970-01-01T00:00:00-05:00
  timestamps_reference_time: 1970-01-01T00:00:00-05:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/id (ElementIdentifiers)  | shape = (62,) | dtype = int32
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (87281,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (62,) | dtype = uint32


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeries (ElectricalSeries) Raw acquisition traces
  Dataset /acquisition/ElectricalSeries/electrodes (DynamicTableRegion) all electrodes | shape = (32,) | dtype = int64
  file_create_date: ['2023-08-07T12:57:19.257137-04:00']
  Group /general/devices/Neuronexus polytrode (Device) Neuronexus polytrode (32 channels)
  experiment_description: Automated in vivo patch clamp evaluation of extracellular multielectrode array spike recording capability
  experimenter: ['Allen, Brian D.' 'Moore-Kochlacs, Caroline' 'Gold Bernstein, Jacob'
   'Kinney, Justin' 'Scholvin, Jorg' 'Seoane, Luis' 'Chronopoulos, Chris'
   'Lamantia, Charlie' 'Kodandaramaiah, Suhasa B' 'Tegmark, Max'
   'Boyden, Edward S.']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (32,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/label (VectorData) electrode label | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) x coordinate | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) y coordinate | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) z coordinate | shape = (32,) | dtype = float64
  Group /general/extracellular_ephys/main (ElectrodeGroup) main electrode group
  Group /general/extracellular_ephys/main/device (Device) Neuronexus polytrode (32 channels)
  institution: Massachusetts Institute of Technology
  keywords: ['action potential' 'bursting' 'multielectrode array' 'patch clamp'
   'spike sorting']
  lab: Boyden Lab
  session_id: paired_boyden32c/1103_1_1
  Group /general/subject (Subject) 
  identifier: fd7875a6-1a38-4a50-80d4-ba2f051d6d9a
  session_description: SpikeForest recording: PAIRED_BOYDEN/paired_boyden32c/1103_1_1
  session_start_time: 1970-01-01T00:00:00-05:00
  timestamps_reference_time: 1970-01-01T00:00:00-05:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (1029,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (1,) | dtype = uint16
