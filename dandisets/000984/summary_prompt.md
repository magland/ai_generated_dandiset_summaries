
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000984/draft
name: eis data
contributor: [{'name': 'Ezeh, Cynthia', 'email': 'ezehcynthia530@gmail.com', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}]
description: just for uploading eis
assetsSummary: {'schemaKey': 'AssetsSummary', 'numberOfBytes': 0, 'numberOfFiles': 0}

Dandiset 000984 has 3 NWB files.
3 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/EIS_Impedance (DynamicTable) This table stores frequency, Z-real, Z-imaginary values of EIS experiment
  Dataset /acquisition/EIS_Impedance/frequency (VectorData)  | shape = (57,) | dtype = float64
  Dataset /acquisition/EIS_Impedance/id (ElementIdentifiers)  | shape = (57,) | dtype = int32
  Dataset /acquisition/EIS_Impedance/zimaginary (VectorData)  | shape = (57,) | dtype = float64
  Dataset /acquisition/EIS_Impedance/zreal (VectorData)  | shape = (57,) | dtype = float64
  file_create_date: ['2024-05-02T16:57:45.528236-04:00']
  Group /general/devices/GAMRY (Device) This device is used to measure impedance values of a Potentiostatic EIS experiment
  experiment_description: EIS
  experimenter: ['Yupeng Wu']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/area (VectorData) area of electrode | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/electrode_name (VectorData) label of electrode | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (1,) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/material (VectorData) material of electrode | shape = (1,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/units (VectorData) units in which area is measured | shape = (1,) | dtype = object
  Group /general/extracellular_ephys/unkwown (ElectrodeGroup) electrode group
  Group /general/extracellular_ephys/unkwown/device (Device) This device is used to measure impedance values of a Potentiostatic EIS experiment
  session_id: EIS experiment ID
  Group /general/subject (Subject) 
  identifier: 09  G2 C19 DTA_#1.DTA
  session_description: EIS
  session_start_time: 2023-11-20T00:10:53-04:56
  timestamps_reference_time: 2023-11-20T00:10:53-04:56
