
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001433/0.250507.2356
name: Breathing rhythm and place dataset
contributor: [{'name': 'National Institutes of Health (NIH)', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': '1 R01 NS 123903-03'}, {'name': 'Smear, Matt', 'email': 'smear@uoregon.edu', 'roleName': ['dcite:ContactPerson', 'dcite:Author', 'dcite:Conceptualization', 'dcite:DataCurator', 'dcite:DataManager'], 'schemaKey': 'Person', 'identifier': '0000-0003-4689-388X'}]
description: These are behavioral and electrophysiological data from recordings of sniffing, video, and OB electrophysiology in freely-behaving mice given no stimulus, reward, or task. 1 1 R01 NS 123903
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 41430354280, 'numberOfFiles': 27, 'numberOfSubjects': 4, 'variableMeasured': ['ProcessingModule', 'ElectricalSeries', 'ElectrodeGroup'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 001433 has 27 NWB files.
27 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/LFP (ElectricalSeries) LFP signal from olfactory bulb
  Dataset /acquisition/LFP/electrodes (DynamicTableRegion) All LFP electrodes | shape = (16,) | dtype = int64
  Group /acquisition/SniffSignal (TimeSeries) Raw sniff thermistor voltage
  file_create_date: ['2025-05-07T15:29:27.359523-07:00']
  Group /general/devices/OpenEphys (Device) OpenEphys recording system
  experiment_description: LFP and sniff behavior recording
  experimenter: ['Rafilson, Sidney']
  Group /general/extracellular_ephys/LFPGroup (ElectrodeGroup) LFP recording electrodes
  Group /general/extracellular_ephys/LFPGroup/device (Device) OpenEphys recording system
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering, including the filter name and frequency cutoffs | shape = (16,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (16,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (16,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (16,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (16,) | dtype = object
  institution: University of Oregon
  keywords: ['olfactory bulb' 'LFP' 'sniffing' 'mouse' 'neuroscience']
  lab: Smear lab
  Group /general/subject (Subject) 
  identifier: 4122_4
  Group /processing/behavior (ProcessingModule) Sniff event features
  Group /processing/behavior/exhalation_time (TimeSeries) exhalation_time (s)
  Group /processing/behavior/inhalation_time (TimeSeries) inhalation_time (s)
  session_description: LFP and sniff recording
  session_start_time: 2025-05-07T15:29:27.359523-07:00
  timestamps_reference_time: 2025-05-07T15:29:27.359523-07:00
