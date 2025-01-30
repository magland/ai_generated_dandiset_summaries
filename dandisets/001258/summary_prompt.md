
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001258/draft
name: Nucleus accumbens dopamine release reflects Bayesian inference during instrumental learning
contributor: [{'name': 'Qu, Albert Jiaxu', 'email': 'albert_qu@berkeley.edu', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}]
description: Dataset associated with https://www.biorxiv.org/content/10.1101/2023.11.10.566306v2
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 192918232, 'numberOfFiles': 69, 'numberOfSubjects': 5, 'variableMeasured': [], 'measurementTechnique': []}

Dandiset 001258 has 69 NWB files.
48 of these NWB files are of type 1.
21 of these NWB files are of type 2.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/fp_series_415nm (FiberPhotometryResponseSeries) 415nm series
  Dataset /acquisition/fp_series_415nm/fiber_photometry_table_region (DynamicTableRegion) 415nm | shape = (1,) | dtype = int32
  Group /acquisition/fp_series_470nm (FiberPhotometryResponseSeries) 470nm series
  Dataset /acquisition/fp_series_470nm/fiber_photometry_table_region (DynamicTableRegion) 470nm | shape = (1,) | dtype = int32
  file_create_date: ['2024-11-19T17:55:35.629447-08:00']
  Group /general/devices/band_optical_filter_0 (BandOpticalFilter) check Neurophotometry docs
  Group /general/devices/band_optical_filter_1 (BandOpticalFilter) check Neurophotometry docs
  Group /general/devices/dichroic_mirror_0 (DichroicMirror) Dichroic mirror for red indicator
  Group /general/devices/dichroic_mirror_1 (DichroicMirror) Dichroic mirror for red indicator
  Group /general/devices/dual-color fiber photometry (Device) Neurophotonics fiber photometry system
  Group /general/devices/excitation_source_0 (ExcitationSource) excitation sources for 415nm
  Group /general/devices/excitation_source_1 (ExcitationSource) excitation sources for 470nm
  Group /general/devices/indicator (Indicator) Calcium indicator at 470nm and isosbestic point at 415nm
  Group /general/devices/optical_fiber (OpticalFiber) 
  Group /general/devices/photodetector_0 (Photodetector) CMOS detector
  Group /general/devices/photodetector_1 (Photodetector) CMOS detector
  Group /general/fiber_photometry (FiberPhotometry) 
  Group /general/fiber_photometry/fiber_photometry_table (FiberPhotometryTable) fiber photometry table
  Dataset /general/fiber_photometry/fiber_photometry_table/coordinates (VectorData) Fiber placement in stereotactic coordinates (AP, ML, DV) mm relative to Bregma. | shape = (2, 3) | dtype = float64
  Dataset /general/fiber_photometry/fiber_photometry_table/dichroic_mirror (VectorData) Link to the dichroic mirror device. | shape = (2,) | dtype = object
  Dataset /general/fiber_photometry/fiber_photometry_table/emission_filter (VectorData) Link to the emission filter device. | shape = (2,) | dtype = object
  Dataset /general/fiber_photometry/fiber_photometry_table/excitation_source (VectorData) Link to the excitation source device. | shape = (2,) | dtype = object
  Dataset /general/fiber_photometry/fiber_photometry_table/id (ElementIdentifiers)  | shape = (2,) | dtype = int32
  Dataset /general/fiber_photometry/fiber_photometry_table/indicator (VectorData) Link to the indicator object. | shape = (2,) | dtype = object
  Dataset /general/fiber_photometry/fiber_photometry_table/location (VectorData) Location of fiber. | shape = (2,) | dtype = object
  Dataset /general/fiber_photometry/fiber_photometry_table/optical_fiber (VectorData) Link to the optical fiber device. | shape = (2,) | dtype = object
  Dataset /general/fiber_photometry/fiber_photometry_table/photodetector (VectorData) Link to the photodetector device. | shape = (2,) | dtype = object
  institution: UC Berkeley
  keywords: ['2ABT' 'bayesian' 'dopamine']
  lab: Wilbrecht Lab
  related_publications: ['https://www.biorxiv.org/content/10.1101/2023.11.10.566306v2']
  session_id: p148
  Group /general/subject (Subject) 
  identifier: 050ab2a2-3c3d-459a-b1fe-0ae74e8dfa71
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/action (VectorData) left or right | shape = (577,) | dtype = object
  Dataset /intervals/trials/animal (VectorData) mouse in task | shape = (577,) | dtype = object
  Dataset /intervals/trials/block_num (VectorData) block number | shape = (577,) | dtype = int32
  Dataset /intervals/trials/center_in (VectorData) time (relative to session start) when mouse pokes in center port to start a new trial | shape = (577,) | dtype = float64
  Dataset /intervals/trials/center_out (VectorData) time (relative to session start) when mouse leaves the center port | shape = (577,) | dtype = float64
  Dataset /intervals/trials/first_side_out (VectorData) time (relative to session start) when mouse leaves the side port for the first time after outcome | shape = (577,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (577,) | dtype = int32
  Dataset /intervals/trials/last_side_out (VectorData) time (relative to session start) right before mouse pokes in center port to start a new trial | shape = (577,) | dtype = float64
  Dataset /intervals/trials/last_side_out_side (VectorData) left or right | shape = (577,) | dtype = object
  Dataset /intervals/trials/outcome (VectorData) time (relative to session start) of the outcome | shape = (577,) | dtype = float64
  Dataset /intervals/trials/prebswitch_num (VectorData) number of trials prior to block switch | shape = (577,) | dtype = float64
  Dataset /intervals/trials/rewarded (VectorData) rewarded or not | shape = (577,) | dtype = float64
  Dataset /intervals/trials/session (VectorData) session names as pXX for postnatal date | shape = (577,) | dtype = object
  Dataset /intervals/trials/side_in (VectorData) time (relative to session start) when mouse pokes in side port | shape = (577,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (577,) | dtype = float64
  Dataset /intervals/trials/state (VectorData) true block state | shape = (577,) | dtype = object
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (577,) | dtype = float64
  Dataset /intervals/trials/tmax (VectorData) max time (relative to session start) in session | shape = (577,) | dtype = float64
  Dataset /intervals/trials/trial (VectorData) trial number | shape = (577,) | dtype = int32
  Dataset /intervals/trials/trial_in_block (VectorData) trial number in block | shape = (577,) | dtype = int32
  Dataset /intervals/trials/zeroth_side_out (VectorData) time (relative to session start) when mouse triggers first IR beam after outcome | shape = (577,) | dtype = float64
  session_description: Probswitch experiment for 2ABT
  session_start_time: 2021-08-06T17:25:00-07:53
  timestamps_reference_time: 2021-08-06T17:25:00-07:53


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2024-11-19T17:55:38.460529-08:00']
  Group /general/devices/dual-color fiber photometry (Device) Neurophotonics fiber photometry system
  institution: UC Berkeley
  keywords: ['2ABT' 'bayesian' 'dopamine']
  lab: Wilbrecht Lab
  related_publications: ['https://www.biorxiv.org/content/10.1101/2023.11.10.566306v2']
  session_id: p106
  Group /general/subject (Subject) 
  identifier: 84da768a-073e-430f-a945-c8afd24f97a9
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/action (VectorData) left or right | shape = (1098,) | dtype = object
  Dataset /intervals/trials/animal (VectorData) mouse in task | shape = (1098,) | dtype = object
  Dataset /intervals/trials/block_num (VectorData) block number | shape = (1098,) | dtype = int32
  Dataset /intervals/trials/center_in (VectorData) time (relative to session start) when mouse pokes in center port to start a new trial | shape = (1098,) | dtype = float64
  Dataset /intervals/trials/center_out (VectorData) time (relative to session start) when mouse leaves the center port | shape = (1098,) | dtype = float64
  Dataset /intervals/trials/first_side_out (VectorData) time (relative to session start) when mouse leaves the side port for the first time after outcome | shape = (1098,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (1098,) | dtype = int32
  Dataset /intervals/trials/last_side_out (VectorData) time (relative to session start) right before mouse pokes in center port to start a new trial | shape = (1098,) | dtype = float64
  Dataset /intervals/trials/last_side_out_side (VectorData) left or right | shape = (1098,) | dtype = object
  Dataset /intervals/trials/outcome (VectorData) time (relative to session start) of the outcome | shape = (1098,) | dtype = float64
  Dataset /intervals/trials/prebswitch_num (VectorData) number of trials prior to block switch | shape = (1098,) | dtype = float64
  Dataset /intervals/trials/rewarded (VectorData) rewarded or not | shape = (1098,) | dtype = float64
  Dataset /intervals/trials/session (VectorData) session names as pXX for postnatal date | shape = (1098,) | dtype = object
  Dataset /intervals/trials/side_in (VectorData) time (relative to session start) when mouse pokes in side port | shape = (1098,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (1098,) | dtype = float64
  Dataset /intervals/trials/state (VectorData) true block state | shape = (1098,) | dtype = object
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1098,) | dtype = float64
  Dataset /intervals/trials/tmax (VectorData) max time (relative to session start) in session | shape = (1098,) | dtype = float64
  Dataset /intervals/trials/trial (VectorData) trial number | shape = (1098,) | dtype = int32
  Dataset /intervals/trials/trial_in_block (VectorData) trial number in block | shape = (1098,) | dtype = int32
  Dataset /intervals/trials/zeroth_side_out (VectorData) time (relative to session start) when mouse triggers first IR beam after outcome | shape = (1098,) | dtype = float64
  session_description: Probswitch experiment for 2ABT
  session_start_time: 2022-02-24T14:47:00-07:53
  timestamps_reference_time: 2022-02-24T14:47:00-07:53
