
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000067/0.210812.1457
name: Behavior-dependent short-term assembly dynamics in the medial prefrontal cortex
contributor: [{'name': 'Fujisawa, Shigeyoshi', 'roleName': ['dcite:Author', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Amarasingham, Asohan', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Harrison, Matthew', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Buzsáki, György', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-3100-4800', 'affiliation': [], 'includeInCitation': True}]
description: Although short-term plasticity is believed to play a fundamental role in cortical computation, empirical evidence bearing on its role during behavior is scarce. Here we looked for the signature of short-term plasticity in the fine-timescale spiking relationships of a simultaneously recorded population of physiologically identified pyramidal cells and interneurons, in the medial prefrontal cortex of the rat, in a working memory task. On broader timescales, sequentially organized and transiently active neurons reliably differentiated between different trajectories of the rat in the maze. On finer timescales, putative monosynaptic interactions reflected short-term plasticity in their dynamic and predictable modulation across various aspects of the task, beyond a statistical accounting for the effect of the neurons' co-varying firing rates. Seeking potential mechanisms for such effects, we found evidence for both firing pattern–dependent facilitation and depression, as well as for a supralinear effect of presynaptic coincidence on the firing of postsynaptic targets.
assetsSummary: {'species': [{'name': 'Brown rat', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10116'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 94565736755, 'numberOfFiles': 28, 'numberOfSubjects': 3, 'variableMeasured': ['LFP', 'ProcessingModule', 'Units', 'ElectricalSeries'], 'measurementTechnique': [{'name': 'signal filtering technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000067 has 27 NWB files.
1 of these NWB files are of type 1.
7 of these NWB files are of type 2.
9 of these NWB files are of type 3.
9 of these NWB files are of type 4.
1 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2021-04-18T19:52:06.004153-04:00']
  Group /general/devices/Device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  experimenter: ['Shigeyoshi Fujisawa']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (104,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (104,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (104,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (104,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (104,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (104,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/shank_electrode_number (VectorData) 0-indexed channel within a shank. | shape = (104,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (104,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (104,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (104,) | dtype = float64
  Group /general/extracellular_ephys/shank1 (ElectrodeGroup) shank1 electrodes
  Group /general/extracellular_ephys/shank1/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  Group /general/extracellular_ephys/shank10 (ElectrodeGroup) shank10 electrodes
  Group /general/extracellular_ephys/shank10/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  Group /general/extracellular_ephys/shank11 (ElectrodeGroup) shank11 electrodes
  Group /general/extracellular_ephys/shank11/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  Group /general/extracellular_ephys/shank12 (ElectrodeGroup) shank12 electrodes
  Group /general/extracellular_ephys/shank12/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  Group /general/extracellular_ephys/shank13 (ElectrodeGroup) shank13 electrodes
  Group /general/extracellular_ephys/shank13/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  Group /general/extracellular_ephys/shank2 (ElectrodeGroup) shank2 electrodes
  Group /general/extracellular_ephys/shank2/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  Group /general/extracellular_ephys/shank3 (ElectrodeGroup) shank3 electrodes
  Group /general/extracellular_ephys/shank3/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  Group /general/extracellular_ephys/shank4 (ElectrodeGroup) shank4 electrodes
  Group /general/extracellular_ephys/shank4/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  Group /general/extracellular_ephys/shank5 (ElectrodeGroup) shank5 electrodes
  Group /general/extracellular_ephys/shank5/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  Group /general/extracellular_ephys/shank6 (ElectrodeGroup) shank6 electrodes
  Group /general/extracellular_ephys/shank6/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  Group /general/extracellular_ephys/shank7 (ElectrodeGroup) shank7 electrodes
  Group /general/extracellular_ephys/shank7/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  Group /general/extracellular_ephys/shank8 (ElectrodeGroup) shank8 electrodes
  Group /general/extracellular_ephys/shank8/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  Group /general/extracellular_ephys/shank9 (ElectrodeGroup) shank9 electrodes
  Group /general/extracellular_ephys/shank9/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  institution: NYU
  lab: Buzsaki
  related_publications: ['Behavior-dependent short-term assembly dynamics in the medial prefrontal cortex.Fujisawa S, Amarasingham A, Harrison M, Buzsáki G, Nature Neuroscience. 2008']
  session_id: EE.042
  Group /general/subject (Subject) 
  identifier: 2c17d866-885f-4773-a1fb-64531fea7a1d
  Group /processing/ecephys (ProcessingModule) Intermediate data from extracellular electrophysiology recordings, e.g., LFP.
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/LFP (ElectricalSeries) Local field potential signal.
  Dataset /processing/ecephys/LFP/LFP/electrodes (DynamicTableRegion) electrode_table_region | shape = (104,) | dtype = int64
  session_description: Although short-term plasticity is believed to play a fundamental role in cortical computation, empirical evidence bearing on its role during behavior is scarce. Here we looked for the signature of short-term plasticity in the fine-timescale spiking relationships of a simultaneously recorded population of physiologically identified pyramidal cells and interneurons, in the medial prefrontal cortex of the rat, in a working memory task. On broader timescales, sequentially organized and transiently active neurons reliably differentiated between different trajectories of the rat in the maze. On finer timescales, putative monosynaptic interactions reflected short-term plasticity in their dynamic and predictable modulation across various aspects of the task, beyond a statistical accounting for the effect of the neurons' co-varying firing rates. Seeking potential mechanisms for such effects, we found evidence for both firing pattern-dependent facilitation and depression, as well as for a supralinear effect of presynaptic coincidence on the firing of postsynaptic targets.
  session_start_time: 2008-06-22T00:00:00-04:00
  timestamps_reference_time: 2008-06-22T00:00:00-04:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeries (ElectricalSeries) Raw acquisition traces.
  Dataset /acquisition/ElectricalSeries/electrodes (DynamicTableRegion) electrode_table_region | shape = (104,) | dtype = int64
  file_create_date: ['2021-04-18T19:52:31.819185-04:00']
  Group /general/devices/Device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  experimenter: ['Shigeyoshi Fujisawa']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (104,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (104,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (104,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (104,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (104,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (104,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/shank_electrode_number (VectorData) 0-indexed channel within a shank. | shape = (104,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (104,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (104,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (104,) | dtype = float64
  Group /general/extracellular_ephys/shank1 (ElectrodeGroup) shank1 electrodes
  Group /general/extracellular_ephys/shank1/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  Group /general/extracellular_ephys/shank10 (ElectrodeGroup) shank10 electrodes
  Group /general/extracellular_ephys/shank10/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  Group /general/extracellular_ephys/shank11 (ElectrodeGroup) shank11 electrodes
  Group /general/extracellular_ephys/shank11/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  Group /general/extracellular_ephys/shank12 (ElectrodeGroup) shank12 electrodes
  Group /general/extracellular_ephys/shank12/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  Group /general/extracellular_ephys/shank13 (ElectrodeGroup) shank13 electrodes
  Group /general/extracellular_ephys/shank13/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  Group /general/extracellular_ephys/shank2 (ElectrodeGroup) shank2 electrodes
  Group /general/extracellular_ephys/shank2/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  Group /general/extracellular_ephys/shank3 (ElectrodeGroup) shank3 electrodes
  Group /general/extracellular_ephys/shank3/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  Group /general/extracellular_ephys/shank4 (ElectrodeGroup) shank4 electrodes
  Group /general/extracellular_ephys/shank4/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  Group /general/extracellular_ephys/shank5 (ElectrodeGroup) shank5 electrodes
  Group /general/extracellular_ephys/shank5/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  Group /general/extracellular_ephys/shank6 (ElectrodeGroup) shank6 electrodes
  Group /general/extracellular_ephys/shank6/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  Group /general/extracellular_ephys/shank7 (ElectrodeGroup) shank7 electrodes
  Group /general/extracellular_ephys/shank7/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  Group /general/extracellular_ephys/shank8 (ElectrodeGroup) shank8 electrodes
  Group /general/extracellular_ephys/shank8/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  Group /general/extracellular_ephys/shank9 (ElectrodeGroup) shank9 electrodes
  Group /general/extracellular_ephys/shank9/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  institution: NYU
  lab: Buzsaki
  related_publications: ['Behavior-dependent short-term assembly dynamics in the medial prefrontal cortex.Fujisawa S, Amarasingham A, Harrison M, Buzsáki G, Nature Neuroscience. 2008']
  session_id: EE.043
  Group /general/subject (Subject) 
  identifier: a07f89cb-84d3-42a6-8e71-a16b5f1c5e0f
  Group /processing/ecephys (ProcessingModule) Intermediate data from extracellular electrophysiology recordings, e.g., LFP.
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/LFP (ElectricalSeries) Local field potential signal.
  Dataset /processing/ecephys/LFP/LFP/electrodes (DynamicTableRegion) electrode_table_region | shape = (104,) | dtype = int64
  session_description: Although short-term plasticity is believed to play a fundamental role in cortical computation, empirical evidence bearing on its role during behavior is scarce. Here we looked for the signature of short-term plasticity in the fine-timescale spiking relationships of a simultaneously recorded population of physiologically identified pyramidal cells and interneurons, in the medial prefrontal cortex of the rat, in a working memory task. On broader timescales, sequentially organized and transiently active neurons reliably differentiated between different trajectories of the rat in the maze. On finer timescales, putative monosynaptic interactions reflected short-term plasticity in their dynamic and predictable modulation across various aspects of the task, beyond a statistical accounting for the effect of the neurons' co-varying firing rates. Seeking potential mechanisms for such effects, we found evidence for both firing pattern-dependent facilitation and depression, as well as for a supralinear effect of presynaptic coincidence on the firing of postsynaptic targets.
  session_start_time: 2008-06-22T00:00:00-04:00
  timestamps_reference_time: 2008-06-22T00:00:00-04:00


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeries (ElectricalSeries) Raw acquisition traces.
  Dataset /acquisition/ElectricalSeries/electrodes (DynamicTableRegion) electrode_table_region | shape = (104,) | dtype = int64
  file_create_date: ['2021-04-18T20:30:45.758774-04:00']
  Group /general/devices/Device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  experimenter: ['Shigeyoshi Fujisawa']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (104,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (104,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (104,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (104,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (104,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (104,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/shank_electrode_number (VectorData) 0-indexed channel within a shank. | shape = (104,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (104,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (104,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (104,) | dtype = float64
  Group /general/extracellular_ephys/shank1 (ElectrodeGroup) shank1 electrodes
  Group /general/extracellular_ephys/shank1/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  Group /general/extracellular_ephys/shank10 (ElectrodeGroup) shank10 electrodes
  Group /general/extracellular_ephys/shank10/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  Group /general/extracellular_ephys/shank11 (ElectrodeGroup) shank11 electrodes
  Group /general/extracellular_ephys/shank11/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  Group /general/extracellular_ephys/shank12 (ElectrodeGroup) shank12 electrodes
  Group /general/extracellular_ephys/shank12/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  Group /general/extracellular_ephys/shank13 (ElectrodeGroup) shank13 electrodes
  Group /general/extracellular_ephys/shank13/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  Group /general/extracellular_ephys/shank2 (ElectrodeGroup) shank2 electrodes
  Group /general/extracellular_ephys/shank2/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  Group /general/extracellular_ephys/shank3 (ElectrodeGroup) shank3 electrodes
  Group /general/extracellular_ephys/shank3/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  Group /general/extracellular_ephys/shank4 (ElectrodeGroup) shank4 electrodes
  Group /general/extracellular_ephys/shank4/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  Group /general/extracellular_ephys/shank5 (ElectrodeGroup) shank5 electrodes
  Group /general/extracellular_ephys/shank5/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  Group /general/extracellular_ephys/shank6 (ElectrodeGroup) shank6 electrodes
  Group /general/extracellular_ephys/shank6/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  Group /general/extracellular_ephys/shank7 (ElectrodeGroup) shank7 electrodes
  Group /general/extracellular_ephys/shank7/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  Group /general/extracellular_ephys/shank8 (ElectrodeGroup) shank8 electrodes
  Group /general/extracellular_ephys/shank8/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  Group /general/extracellular_ephys/shank9 (ElectrodeGroup) shank9 electrodes
  Group /general/extracellular_ephys/shank9/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  institution: NYU
  lab: Buzsaki
  related_publications: ['Behavior-dependent short-term assembly dynamics in the medial prefrontal cortex.Fujisawa S, Amarasingham A, Harrison M, Buzsáki G, Nature Neuroscience. 2008']
  session_id: EE.049
  Group /general/subject (Subject) 
  identifier: 98698827-5425-49ad-ad9a-906f9e7e38cb
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (19,) | dtype = int64
  Dataset /intervals/trials/left_or_right (VectorData) Time when subject began consuming reward. | shape = (19,) | dtype = object
  Dataset /intervals/trials/reward_time (VectorData) Time when subject began consuming reward. | shape = (19,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (19,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (19,) | dtype = float64
  Group /processing/behavior (ProcessingModule) Contains processed behavioral data.
  Group /processing/behavior/LinearizedPosition (Position) 
  Group /processing/behavior/LinearizedPosition/LinearizedTimeSeries (SpatialSeries) Linearized position, with '1' defined as start position (the position at the time of last nose-poking in the trial), and d=2 being the end position (position at the tiome just before reward consumption). d=0 means subject is not performing working memory trials.
  Group /processing/behavior/Position (Position) 
  Group /processing/behavior/Position/SpatialSeries1 (SpatialSeries) (x,y) coordinates tracking subject movement through the maze.
  Group /processing/behavior/Position/SpatialSeries2 (SpatialSeries) (x,y) coordinates tracking subject movement through the maze.
  Group /processing/ecephys (ProcessingModule) Intermediate data from extracellular electrophysiology recordings, e.g., LFP.
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/LFP (ElectricalSeries) Local field potential signal.
  Dataset /processing/ecephys/LFP/LFP/electrodes (DynamicTableRegion) electrode_table_region | shape = (104,) | dtype = int64
  session_description: Although short-term plasticity is believed to play a fundamental role in cortical computation, empirical evidence bearing on its role during behavior is scarce. Here we looked for the signature of short-term plasticity in the fine-timescale spiking relationships of a simultaneously recorded population of physiologically identified pyramidal cells and interneurons, in the medial prefrontal cortex of the rat, in a working memory task. On broader timescales, sequentially organized and transiently active neurons reliably differentiated between different trajectories of the rat in the maze. On finer timescales, putative monosynaptic interactions reflected short-term plasticity in their dynamic and predictable modulation across various aspects of the task, beyond a statistical accounting for the effect of the neurons' co-varying firing rates. Seeking potential mechanisms for such effects, we found evidence for both firing pattern-dependent facilitation and depression, as well as for a supralinear effect of presynaptic coincidence on the firing of postsynaptic targets.
  session_start_time: 2008-06-22T00:00:00-04:00
  timestamps_reference_time: 2008-06-22T00:00:00-04:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/id (ElementIdentifiers)  | shape = (118,) | dtype = int64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (3246543,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (118,) | dtype = uint32


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2021-04-18T19:28:34.023641-04:00']
  Group /general/devices/Device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  experimenter: ['Shigeyoshi Fujisawa']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (104,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (104,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (104,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (104,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (104,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (104,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/shank_electrode_number (VectorData) 0-indexed channel within a shank. | shape = (104,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (104,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (104,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (104,) | dtype = float64
  Group /general/extracellular_ephys/shank1 (ElectrodeGroup) shank1 electrodes
  Group /general/extracellular_ephys/shank1/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  Group /general/extracellular_ephys/shank10 (ElectrodeGroup) shank10 electrodes
  Group /general/extracellular_ephys/shank10/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  Group /general/extracellular_ephys/shank11 (ElectrodeGroup) shank11 electrodes
  Group /general/extracellular_ephys/shank11/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  Group /general/extracellular_ephys/shank12 (ElectrodeGroup) shank12 electrodes
  Group /general/extracellular_ephys/shank12/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  Group /general/extracellular_ephys/shank13 (ElectrodeGroup) shank13 electrodes
  Group /general/extracellular_ephys/shank13/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  Group /general/extracellular_ephys/shank2 (ElectrodeGroup) shank2 electrodes
  Group /general/extracellular_ephys/shank2/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  Group /general/extracellular_ephys/shank3 (ElectrodeGroup) shank3 electrodes
  Group /general/extracellular_ephys/shank3/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  Group /general/extracellular_ephys/shank4 (ElectrodeGroup) shank4 electrodes
  Group /general/extracellular_ephys/shank4/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  Group /general/extracellular_ephys/shank5 (ElectrodeGroup) shank5 electrodes
  Group /general/extracellular_ephys/shank5/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  Group /general/extracellular_ephys/shank6 (ElectrodeGroup) shank6 electrodes
  Group /general/extracellular_ephys/shank6/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  Group /general/extracellular_ephys/shank7 (ElectrodeGroup) shank7 electrodes
  Group /general/extracellular_ephys/shank7/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  Group /general/extracellular_ephys/shank8 (ElectrodeGroup) shank8 electrodes
  Group /general/extracellular_ephys/shank8/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  Group /general/extracellular_ephys/shank9 (ElectrodeGroup) shank9 electrodes
  Group /general/extracellular_ephys/shank9/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  institution: NYU
  lab: Buzsaki
  related_publications: ['Behavior-dependent short-term assembly dynamics in the medial prefrontal cortex.Fujisawa S, Amarasingham A, Harrison M, Buzsáki G, Nature Neuroscience. 2008']
  session_id: EE.080
  Group /general/subject (Subject) 
  identifier: f64d4373-ec2e-4db8-b1c8-b37f146e2f2e
  Group /processing/ecephys (ProcessingModule) Intermediate data from extracellular electrophysiology recordings, e.g., LFP.
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/LFP (ElectricalSeries) Local field potential signal.
  Dataset /processing/ecephys/LFP/LFP/electrodes (DynamicTableRegion) electrode_table_region | shape = (104,) | dtype = int64
  session_description: Although short-term plasticity is believed to play a fundamental role in cortical computation, empirical evidence bearing on its role during behavior is scarce. Here we looked for the signature of short-term plasticity in the fine-timescale spiking relationships of a simultaneously recorded population of physiologically identified pyramidal cells and interneurons, in the medial prefrontal cortex of the rat, in a working memory task. On broader timescales, sequentially organized and transiently active neurons reliably differentiated between different trajectories of the rat in the maze. On finer timescales, putative monosynaptic interactions reflected short-term plasticity in their dynamic and predictable modulation across various aspects of the task, beyond a statistical accounting for the effect of the neurons' co-varying firing rates. Seeking potential mechanisms for such effects, we found evidence for both firing pattern-dependent facilitation and depression, as well as for a supralinear effect of presynaptic coincidence on the firing of postsynaptic targets.
  session_start_time: 2008-06-27T00:00:00-04:00
  timestamps_reference_time: 2008-06-27T00:00:00-04:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/id (ElementIdentifiers)  | shape = (362,) | dtype = int64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (567663,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (362,) | dtype = uint32


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2021-04-18T19:31:52.908609-04:00']
  Group /general/devices/Device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  experimenter: ['Shigeyoshi Fujisawa']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (104,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (104,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (104,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (104,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (104,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (104,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/shank_electrode_number (VectorData) 0-indexed channel within a shank. | shape = (104,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (104,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (104,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (104,) | dtype = float64
  Group /general/extracellular_ephys/shank1 (ElectrodeGroup) shank1 electrodes
  Group /general/extracellular_ephys/shank1/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  Group /general/extracellular_ephys/shank10 (ElectrodeGroup) shank10 electrodes
  Group /general/extracellular_ephys/shank10/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  Group /general/extracellular_ephys/shank11 (ElectrodeGroup) shank11 electrodes
  Group /general/extracellular_ephys/shank11/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  Group /general/extracellular_ephys/shank12 (ElectrodeGroup) shank12 electrodes
  Group /general/extracellular_ephys/shank12/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  Group /general/extracellular_ephys/shank13 (ElectrodeGroup) shank13 electrodes
  Group /general/extracellular_ephys/shank13/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  Group /general/extracellular_ephys/shank2 (ElectrodeGroup) shank2 electrodes
  Group /general/extracellular_ephys/shank2/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  Group /general/extracellular_ephys/shank3 (ElectrodeGroup) shank3 electrodes
  Group /general/extracellular_ephys/shank3/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  Group /general/extracellular_ephys/shank4 (ElectrodeGroup) shank4 electrodes
  Group /general/extracellular_ephys/shank4/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  Group /general/extracellular_ephys/shank5 (ElectrodeGroup) shank5 electrodes
  Group /general/extracellular_ephys/shank5/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  Group /general/extracellular_ephys/shank6 (ElectrodeGroup) shank6 electrodes
  Group /general/extracellular_ephys/shank6/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  Group /general/extracellular_ephys/shank7 (ElectrodeGroup) shank7 electrodes
  Group /general/extracellular_ephys/shank7/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  Group /general/extracellular_ephys/shank8 (ElectrodeGroup) shank8 electrodes
  Group /general/extracellular_ephys/shank8/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  Group /general/extracellular_ephys/shank9 (ElectrodeGroup) shank9 electrodes
  Group /general/extracellular_ephys/shank9/device (Device) Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).
  institution: NYU
  lab: Buzsaki
  related_publications: ['Behavior-dependent short-term assembly dynamics in the medial prefrontal cortex.Fujisawa S, Amarasingham A, Harrison M, Buzsáki G, Nature Neuroscience. 2008']
  session_id: EE.088
  Group /general/subject (Subject) 
  identifier: 518132cb-6a47-4a34-a400-b8f09fa00f90
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (31,) | dtype = int64
  Dataset /intervals/trials/left_or_right (VectorData) Time when subject began consuming reward. | shape = (31,) | dtype = object
  Dataset /intervals/trials/reward_time (VectorData) Time when subject began consuming reward. | shape = (31,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (31,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (31,) | dtype = float64
  Group /processing/behavior (ProcessingModule) Contains processed behavioral data.
  Group /processing/behavior/LinearizedPosition (Position) 
  Group /processing/behavior/LinearizedPosition/LinearizedTimeSeries (SpatialSeries) Linearized position, with '1' defined as start position (the position at the time of last nose-poking in the trial), and d=2 being the end position (position at the tiome just before reward consumption). d=0 means subject is not performing working memory trials.
  Group /processing/behavior/Position (Position) 
  Group /processing/behavior/Position/SpatialSeries1 (SpatialSeries) (x,y) coordinates tracking subject movement through the maze.
  Group /processing/behavior/Position/SpatialSeries2 (SpatialSeries) (x,y) coordinates tracking subject movement through the maze.
  Group /processing/ecephys (ProcessingModule) Intermediate data from extracellular electrophysiology recordings, e.g., LFP.
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/LFP (ElectricalSeries) Local field potential signal.
  Dataset /processing/ecephys/LFP/LFP/electrodes (DynamicTableRegion) electrode_table_region | shape = (104,) | dtype = int64
  session_description: Although short-term plasticity is believed to play a fundamental role in cortical computation, empirical evidence bearing on its role during behavior is scarce. Here we looked for the signature of short-term plasticity in the fine-timescale spiking relationships of a simultaneously recorded population of physiologically identified pyramidal cells and interneurons, in the medial prefrontal cortex of the rat, in a working memory task. On broader timescales, sequentially organized and transiently active neurons reliably differentiated between different trajectories of the rat in the maze. On finer timescales, putative monosynaptic interactions reflected short-term plasticity in their dynamic and predictable modulation across various aspects of the task, beyond a statistical accounting for the effect of the neurons' co-varying firing rates. Seeking potential mechanisms for such effects, we found evidence for both firing pattern-dependent facilitation and depression, as well as for a supralinear effect of presynaptic coincidence on the firing of postsynaptic targets.
  session_start_time: 2008-06-27T00:00:00-04:00
  timestamps_reference_time: 2008-06-27T00:00:00-04:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/id (ElementIdentifiers)  | shape = (350,) | dtype = int64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (4507778,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (350,) | dtype = uint32
