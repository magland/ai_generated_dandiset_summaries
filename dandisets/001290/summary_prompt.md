
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001290/draft
name: Neuropixels pulsation datasets
contributor: [{'name': 'Windolf, Charlie', 'email': 'charliexwindolf@gmail.com', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}]
description: Neuropixels datasets recorded in non-human primates by RT Raghavan in the Movshon lab at NYU. Studied in Supp. Fig. 3 of Windolf et al., "DREDge: robust motion correction for high-density extracellular recordings across species", to appear in Nature Methods.
assetsSummary: {'schemaKey': 'AssetsSummary', 'numberOfBytes': 0, 'numberOfFiles': 0}

Dandiset 001290 has 1 NWB files.
1 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeriesAPImec (ElectricalSeries) Acquisition traces for the ElectricalSeriesAPImec.
  Dataset /acquisition/ElectricalSeriesAPImec/electrodes (DynamicTableRegion) electrode_table_region | shape = (384,) | dtype = int64
  Group /acquisition/ElectricalSeriesLFImec (ElectricalSeries) Acquisition traces for the ElectricalSeriesLFImec.
  Dataset /acquisition/ElectricalSeriesLFImec/electrodes (DynamicTableRegion) electrode_table_region | shape = (384,) | dtype = int64
  file_create_date: ['2025-01-16T17:43:31.232666-05:00']
  Group /general/devices/NeuropixelImec (Device) A Neuropixel probe of unknown subtype.
  experimenter: ['RT Raghavan' 'JG Kelly' 'MJ Hasse' 'M Bohlen' 'S Saraf']
  Group /general/extracellular_ephys/Imec. (ElectrodeGroup) A group representing probe/shank 'Imec.'.
  Group /general/extracellular_ephys/Imec./device (Device) A Neuropixel probe of unknown subtype.
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/channel_name (VectorData) unique channel reference | shape = (768,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/contact_ids (VectorData) The id of the contact on the electrode | shape = (768,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/contact_shapes (VectorData) The shape of the electrode | shape = (768,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (768,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (768,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (768,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/inter_sample_shift (VectorData) no description | shape = (768,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (768,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/rel_x (VectorData) rel_x | shape = (768,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_y (VectorData) rel_y | shape = (768,) | dtype = float64
  institution: New York University
  lab: Movshon lab
  source_script: Created using NeuroConv v0.6.6
  Group /general/subject (Subject) 
  surgery: 5 mm craniotomy made posterior to lunate sulcus over the operculum
  identifier: 2557b744-eee4-4807-b413-9b40d4dd1e40
  session_description: recording in macaque primary visual cortex during presentation of static gratings at 8 different orientations
  session_start_time: 2018-08-09T10:00:00-05:00
  timestamps_reference_time: 2018-08-09T10:00:00-05:00
