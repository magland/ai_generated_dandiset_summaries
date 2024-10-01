
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000122/draft
name: Human fNIRS recordings of motor cortex during finger-tapping task
contributor: [{'name': 'Erat Sleiter, Darin', 'email': 'darin@ae.studio', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}]
description: This experiment examines how the motor cortex is activated during a finger-tapping task. Participants are asked to either tap their left thumb to fingers, tap their right thumb to fingers, or no cue is given (control). Tapping lasts for 5 seconds and is prompted by an auditory cue. Sensors are placed over the motor cortex as described in the montage section in the link below, short channels are attached to the scalp too. Further details about the experiment (including presentation code) can be found at https://github.com/rob-luke/experiment-fNIRS-tapping.
assetsSummary: {'species': [], 'approach': [], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 49898320, 'numberOfFiles': 5, 'numberOfSubjects': 5, 'variableMeasured': [], 'measurementTechnique': []}

Dandiset 000122 has 5 NWB files.
5 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/nirs_data (NIRSSeries) The raw NIRS channel data
  Dataset /acquisition/nirs_data/channels (DynamicTableRegion) an ordered map to the channels in this NIRS series | shape = (56,) | dtype = int64
  file_create_date: ['2021-08-11T17:46:12.951969+10:00']
  Group /general/devices/nirs_device (NIRSDevice) Information about the NIRS device used in this session
  Group /general/devices/nirs_device/channels (NIRSChannelsTable) A table describing optical channels of a NIRS device
  Dataset /general/devices/nirs_device/channels/detector (DynamicTableRegion) A reference to the optical detector for this channel in NIRSDetectorsTable | shape = (56,) | dtype = int64
  Dataset /general/devices/nirs_device/channels/id (ElementIdentifiers)  | shape = (56,) | dtype = int64
  Dataset /general/devices/nirs_device/channels/label (VectorData) The label of the channel | shape = (56,) | dtype = object
  Dataset /general/devices/nirs_device/channels/source (DynamicTableRegion) A reference to the optical source for this channel in NIRSSourcesTable | shape = (56,) | dtype = int64
  Dataset /general/devices/nirs_device/channels/source_wavelength (VectorData) The wavelength of light in nm emitted by the source for this channel. | shape = (56,) | dtype = float64
  Group /general/devices/nirs_device/detectors (NIRSDetectorsTable) A table describing optical detectors of a NIRS device
  Dataset /general/devices/nirs_device/detectors/id (ElementIdentifiers)  | shape = (16,) | dtype = int64
  Dataset /general/devices/nirs_device/detectors/label (VectorData) The label of the optical detector | shape = (16,) | dtype = object
  Dataset /general/devices/nirs_device/detectors/x (VectorData) The x coordinate of the optical detector | shape = (16,) | dtype = float64
  Dataset /general/devices/nirs_device/detectors/y (VectorData) The y coordinate of the optical detector | shape = (16,) | dtype = float64
  Dataset /general/devices/nirs_device/detectors/z (VectorData) The z coordinate of the optical detector | shape = (16,) | dtype = float64
  Group /general/devices/nirs_device/sources (NIRSSourcesTable) A table describing optical sources of a NIRS device
  Dataset /general/devices/nirs_device/sources/id (ElementIdentifiers)  | shape = (8,) | dtype = int64
  Dataset /general/devices/nirs_device/sources/label (VectorData) The label of the optical source | shape = (8,) | dtype = object
  Dataset /general/devices/nirs_device/sources/x (VectorData) The x coordinate of the optical source | shape = (8,) | dtype = float64
  Dataset /general/devices/nirs_device/sources/y (VectorData) The y coordinate of the optical source | shape = (8,) | dtype = float64
  Dataset /general/devices/nirs_device/sources/z (VectorData) The z coordinate of the optical source | shape = (8,) | dtype = float64
  experiment_description: This experiment examines how the motor cortex is activated
  during a finger tapping task. Participants are asked to either tap their left thumb to
  fingers, tap their right thumb to fingers, or no cue is given (control). Tapping lasts
  for 5 seconds and is prompted by an auditory cue. Sensors are placed over the motor
  cortex as described in the montage section in the link below, short channels are
  attached to the scalp too. Further details about the experiment (including presentation
  code) can be found at https://github.com/rob-luke/experiment-fNIRS-tapping.
  
  experimenter: ['Robert Luke']
  institution: Macquarie University
  keywords: ['fNIRS' 'Haemodynamics' 'Motor Cortex' 'Finger Tapping Task']
  notes: Source file SNIRF version: 1.0
  Source dataset BIDS version: 1.6.0
  Conversion script: convert_tapping_dataset_to_nirs.py
  Conversion codebase version: 0.1.0
  NIRSCoordinateSystem: CapTrak
  NIRSCoordinateSystemDescription: The X-axis goes from the left preauricular point (LPA) through the right preauricular point (RPA). The Y-axis goes orthogonally to the X-axis through the nasion (NAS). The Z-axis goes orthogonally to the XY-plane through the vertex of the head. This corresponds to a "RAS" orientation with the origin of the coordinate system approximately between the ears. See Appendix VIII in the BIDS specification.
  NIRSCoordinateUnits: m
  TaskName: tapping
  PowerLineFrequency: 50
  related_publications: ['']
  Group /general/subject (Subject) 
  identifier: sub-01_task-tapping_nirs
  session_description: fNIRS recording data for a finger-tapping task for subject sub-01
  session_start_time: 2020-01-01T02:16:16+00:00
  Group /stimulus/presentation/auditory (TimeSeries) Auditory stimuli presented to the subject. The three data columns represent: 1. description of the stimulus, 2. duration of the stimulus (in seconds), and 3. the id representing the stimulus
  timestamps_reference_time: 2020-01-01T02:16:16+00:00
