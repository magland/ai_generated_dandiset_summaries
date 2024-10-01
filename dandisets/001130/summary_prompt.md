
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001130/draft
name: Aberrant Striatal Activity in Parkinsonism and Levodopa-Induced Dyskinesia
contributor: [{'url': 'http://www.ninds.nih.gov/', 'name': 'National Institute of Neurological Disorders and Stroke (NINDS)', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01s5ya894', 'awardNumber': 'K08 NS081001 and F31 NS106827', 'includeInCitation': False}, {'name': 'Parkinson’s Disease Foundation', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': 'PDF-JFA-1688', 'includeInCitation': False}, {'name': 'Ryan, Michael B.', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-2650-0690', 'includeInCitation': True}, {'name': 'Bair-Marshall, Chloe', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0001-6458-3266', 'includeInCitation': True}, {'name': 'Nelson, Alexandra B.', 'email': 'alexandra.nelson@ucsf.edu', 'roleName': ['dcite:Author', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'includeInCitation': True}]
description: Action selection relies on the coordinated activity of striatal direct and indirect pathway medium spiny neurons (dMSNs and iMSNs, respectively). Loss of dopamine in Parkinson’s disease is thought to disrupt this balance. While dopamine replacement
with levodopa may restore normal function, the development of involuntary movements (levodopa-induced dyskinesia [LID]) limits therapy. How chronic dopamine loss and replacement with levodopa modulate the firing of identified MSNs in behaving
animals is unknown. Using optogenetically labeled striatal single-unit recordings, we assess circuit dysfunction in parkinsonism and LID. Counter to current models, we found that following dopamine depletion, iMSN firing was elevated only during periods of immobility, while dMSN firing was dramatically and persistently reduced. Most notably, we identified a subpopulation of dMSNs with abnormally high levodopa-evoked firing rates, which correlated specifically with dyskinesia. These findings provide key insights into the circuit mechanisms underlying parkinsonism and LID, with implications for developing targeted therapies.
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}, {'name': 'optogenetic approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 677262221, 'numberOfFiles': 1, 'numberOfSubjects': 1, 'variableMeasured': ['ElectricalSeries', 'LFP', 'ProcessingModule', 'OptogeneticSeries', 'Units', 'ElectrodeGroup'], 'measurementTechnique': [{'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'signal filtering technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 001130 has 1 NWB files.
1 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2024-07-22T15:50:47.334347+02:00']
  Group /general/devices/150mW DPSS 473nm Blue Laser (Device) 473nm laser
  Group /general/devices/DeviceEcephys (Device) no description
  experimenter: ['Creed, Rose']
  Group /general/extracellular_ephys/0 (ElectrodeGroup) no description
  Group /general/extracellular_ephys/0/device (Device) no description
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/channel_name (VectorData) no description | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (32,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/rel_x (VectorData) rel_x | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_y (VectorData) rel_y | shape = (32,) | dtype = float64
  institution: University of California San Francisco
  lab: Nelson Lab
  Group /general/optogenetics/OptogeneticStimulusSite (OptogeneticStimulusSite) 
  Group /general/optogenetics/OptogeneticStimulusSite/device (Device) 473nm laser
  source_script: Created using NeuroConv v0.4.12
  Group /general/subject (Subject) 
  identifier: 6a31260c-0e98-4f65-bdc6-1f15e4461cfa
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (4000,) | dtype = int64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (4000,) | dtype = float64
  Dataset /intervals/trials/stimulus_amplitude (VectorData) Amplitude of the optogenetic stimulus | shape = (4000,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (4000,) | dtype = float64
  Group /processing/behavior (ProcessingModule) Processed behavioral data
  Group /processing/behavior/Distance moved (TimeSeries) no description
  Group /processing/behavior/Elongation (TimeSeries) no description
  Group /processing/behavior/Rotation (TimeSeries) no description
  Group /processing/behavior/Velocity (TimeSeries) no description
  Group /processing/behavior/aims (TimeSeries) no description
  Group /processing/ecephys (ProcessingModule) Intermediate data from extracellular electrophysiology recordings, e.g., LFP.
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/ElectricalSeries (ElectricalSeries) Acquisition traces for the ElectricalSeries.
  Dataset /processing/ecephys/LFP/ElectricalSeries/electrodes (DynamicTableRegion) electrode_table_region | shape = (32,) | dtype = int64
  session_description: D1-Cre, 6OHDA in left MFB, 32Ch +DIO-ChR1 in left DLS.\r\nDOB: 2/19/15. L-dopa (5mg/kg) at 30 mins.\r\n4000 light pulses 0.5,1,2,4m
  
  session_start_time: 2000-07-23T00:00:00-07:00
  Group /stimulus/presentation/OptogeneticSeries (OptogeneticSeries) no description
  Group /stimulus/presentation/OptogeneticSeries/site (OptogeneticStimulusSite) 
  Group /stimulus/presentation/OptogeneticSeries/site/device (Device) 473nm laser
  timestamps_reference_time: 2000-07-23T00:00:00-07:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/id (ElementIdentifiers)  | shape = (52,) | dtype = int64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (14719673,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (52,) | dtype = uint32
  Dataset /units/waveform_mean (VectorData) the spike waveform mean for each spike unit | shape = (52, 56) | dtype = float32
