
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000563/0.250311.2145
name: Allen Institute Openscope - Barcoding
contributor: [{'name': 'National Institutes of Health (NIH)', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': '1 U24 NS 113646-03'}, {'url': 'http://www.ratrix.org', 'name': 'Reinagel, Pamela', 'email': 'preinagel@ucsd.edu', 'roleName': ['dcite:Author', 'dcite:Conceptualization', 'dcite:ContactPerson', 'dcite:FormalAnalysis', 'dcite:Investigation', 'dcite:ProjectLeader'], 'schemaKey': 'Person', 'identifier': '0000-0002-6338-2611', 'includeInCitation': True}, {'name': 'Lecoq, Jérôme', 'email': 'jeromel@alleninstitute.org', 'roleName': ['dcite:Author', 'dcite:ContactPerson', 'dcite:DataManager', 'dcite:ProjectLeader', 'dcite:ProjectManager', 'dcite:Software', 'dcite:Supervision'], 'schemaKey': 'Person', 'identifier': '0000-0002-0131-0938', 'includeInCitation': True}, {'name': 'Durand, Séverine', 'roleName': ['dcite:Supervision', 'dcite:DataCurator'], 'schemaKey': 'Person', 'identifier': '0000-0001-7788-0200', 'includeInCitation': True}, {'name': 'Gillis, Ryan', 'roleName': ['dcite:DataCollector'], 'schemaKey': 'Person', 'identifier': '0009-0000-1879-6519', 'includeInCitation': True}, {'name': 'Carlson, Mikayla', 'roleName': ['dcite:DataCollector'], 'schemaKey': 'Person', 'identifier': '0009-0003-7019-2781', 'includeInCitation': True}, {'name': 'Peene, Carter', 'roleName': ['dcite:DataCurator', 'dcite:DataManager'], 'schemaKey': 'Person', 'identifier': '0009-0000-6660-2264', 'includeInCitation': True}, {'name': 'Bawany, Ahad', 'roleName': ['dcite:DataManager'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Johnson, Tye', 'roleName': ['dcite:DataCollector'], 'schemaKey': 'Person', 'identifier': '0009-0006-7239-7571', 'includeInCitation': True}, {'name': 'Amaya, Avalon', 'roleName': ['dcite:DataCollector'], 'schemaKey': 'Person', 'identifier': '0000-0003-2274-2892', 'includeInCitation': True}, {'name': 'Han, Warren', 'roleName': ['dcite:DataCollector'], 'schemaKey': 'Person', 'identifier': '0009-0006-0104-0380', 'includeInCitation': True}, {'name': 'Wilkes, Josh', 'roleName': ['dcite:DataCollector'], 'schemaKey': 'Person', 'identifier': '0009-0005-4858-2219', 'includeInCitation': True}, {'name': 'Nguyen, Katrina', 'roleName': ['dcite:DataCollector'], 'schemaKey': 'Person', 'identifier': '0009-0009-8547-9703', 'includeInCitation': True}, {'name': 'Suarez, Lucas', 'roleName': ['dcite:DataCollector'], 'schemaKey': 'Person', 'identifier': '0009-0002-0121-3334', 'includeInCitation': True}, {'name': 'Naidoo, Robyn', 'roleName': ['dcite:DataCollector'], 'schemaKey': 'Person', 'identifier': '0009-0004-0996-8808', 'includeInCitation': True}, {'name': 'Ouellette, Ben', 'roleName': ['dcite:DataCollector'], 'schemaKey': 'Person', 'identifier': '0000-0003-4913-554X', 'includeInCitation': True}, {'name': 'Grasso, Conor ', 'roleName': ['dcite:DataCollector'], 'schemaKey': 'Person', 'identifier': '0009-0003-6384-4075', 'includeInCitation': True}, {'name': 'Loeffler, Henry', 'roleName': ['dcite:DataCollector'], 'schemaKey': 'Person', 'identifier': '0009-0007-3935-6863', 'includeInCitation': True}, {'name': 'Belski, Hannah', 'roleName': ['dcite:DataCollector'], 'schemaKey': 'Person', 'identifier': '0009-0001-5422-5964', 'includeInCitation': True}, {'name': 'Williford, Ali', 'roleName': ['dcite:ProjectManager'], 'schemaKey': 'Person', 'identifier': '0009-0000-7282-7515', 'includeInCitation': True}, {'name': 'Swapp, Jackie', 'roleName': ['dcite:ProjectManager'], 'schemaKey': 'Person', 'identifier': '0009-0008-4965-6242', 'includeInCitation': True}, {'name': 'Howard, Robert', 'roleName': ['dcite:DataCollector'], 'schemaKey': 'Person', 'identifier': '0009-0008-5499-549X', 'includeInCitation': True}]
description: Some visual neurons have been shown to respond to white noise flicker visual stimuli with high temporal precision, particularly retinal ganglion cells and LGN relay cells. Responses to white noise stimulation are useful for a variety of analyses, including information theoretic measures and generative models of precise spike timing. However the literature was lacking data on responses to white noise in cortical visual areas, or in the visual stream flowing through the superior colliculus.

This experiment used the OpenScope Neuropixels passive viewing protocol, and displayed visual stimuli modulated in time by a short, repeated white noise sequence. The visual stimulus was either a spatially uniform field whose luminance was modulated in time (Full Field Flicker), or a standing sinusoidal grating whose contrast was modulated in time (Static Gratings). Perhaps surprisingly, most cortical visual neurons responded well to full-field flicker white noise.  To obtain large populations of neurons in subcortical areas, roughly half of the mice were recorded in a novel electrode configuration. 

When white noise visual stimuli are presented repeatedly and the neural responses displayed as spike rasters, the rasters look remarkably like UPC codes or bar codes. The same bar-code-like patterns have been found in neurons recorded in different individual animals, and even neurons in different species. We speculated that these barcodes could be used as identifiers of discrete cell types. The Temporal Barcode Dataset provides "barcodes" for visually responsive neurons throughout the mouse brain, enabling a test of this hypothesis.
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}, {'name': 'optogenetic approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 200169653509, 'numberOfFiles': 94, 'numberOfSubjects': 14, 'variableMeasured': ['LFP', 'ElectricalSeries', 'ProcessingModule', 'OptogeneticSeries', 'Units'], 'measurementTechnique': [{'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'signal filtering technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000563 has 63 NWB files.
12 of these NWB files are of type 1.
14 of these NWB files are of type 2.
13 of these NWB files are of type 3.
12 of these NWB files are of type 4.
12 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/EyeTracking (EllipseEyeTracking) 
  Group /acquisition/EyeTracking/corneal_reflection_tracking (EllipseSeries) no description
  Group /acquisition/EyeTracking/eye_tracking (EllipseSeries) no description
  Group /acquisition/EyeTracking/likely_blink (TimeSeries) blinks
  Group /acquisition/EyeTracking/pupil_tracking (EllipseSeries) no description
  Group /acquisition/raw_running_wheel_rotation (TimeSeries) no description
  Group /acquisition/running_wheel_signal_voltage (TimeSeries) no description
  Group /acquisition/running_wheel_supply_voltage (TimeSeries) no description
  file_create_date: ['2024-02-22T21:53:24.741881-08:00']
  Group /general/devices/OptogeneticStimulusDevice (Device) 
  Group /general/devices/probeA (EcephysProbe) Neuropixels 1.0 Probe
  Group /general/devices/probeB (EcephysProbe) Neuropixels 1.0 Probe
  Group /general/devices/probeC (EcephysProbe) Neuropixels 1.0 Probe
  Group /general/devices/probeD (EcephysProbe) Neuropixels 1.0 Probe
  Group /general/devices/probeE (EcephysProbe) Neuropixels 1.0 Probe
  Group /general/devices/probeF (EcephysProbe) Neuropixels 1.0 Probe
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering, including the filter name and frequency cutoffs | shape = (2304,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (2304,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (2304,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (2304,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the electrode, in ohms | shape = (2304,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/local_index (VectorData) The local index of electrode/channel on device | shape = (2304,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (2304,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/probe_horizontal_position (VectorData) Width-wise position of electrode/channel on device (microns) | shape = (2304,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/probe_id (VectorData) The unique id of this electrode's/channel's device | shape = (2304,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/probe_vertical_position (VectorData) Length-wise position of electrode/channel on device (microns) | shape = (2304,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/valid_data (VectorData) Whether data from this electrode/channel is usable | shape = (2304,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the position (+x is posterior) | shape = (2304,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the position (+y is inferior) | shape = (2304,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the position (+z is right) | shape = (2304,) | dtype = float64
  Group /general/extracellular_ephys/probeA (EcephysElectrodeGroup) Ecephys Electrode Group
  Group /general/extracellular_ephys/probeA/device (EcephysProbe) Neuropixels 1.0 Probe
  Group /general/extracellular_ephys/probeB (EcephysElectrodeGroup) Ecephys Electrode Group
  Group /general/extracellular_ephys/probeB/device (EcephysProbe) Neuropixels 1.0 Probe
  Group /general/extracellular_ephys/probeC (EcephysElectrodeGroup) Ecephys Electrode Group
  Group /general/extracellular_ephys/probeC/device (EcephysProbe) Neuropixels 1.0 Probe
  Group /general/extracellular_ephys/probeD (EcephysElectrodeGroup) Ecephys Electrode Group
  Group /general/extracellular_ephys/probeD/device (EcephysProbe) Neuropixels 1.0 Probe
  Group /general/extracellular_ephys/probeE (EcephysElectrodeGroup) Ecephys Electrode Group
  Group /general/extracellular_ephys/probeE/device (EcephysProbe) Neuropixels 1.0 Probe
  Group /general/extracellular_ephys/probeF (EcephysElectrodeGroup) Ecephys Electrode Group
  Group /general/extracellular_ephys/probeF/device (EcephysProbe) Neuropixels 1.0 Probe
  institution: Allen Institute
  Group /general/optogenetics/OptogeneticStimulusSite (OptogeneticStimulusSite) 
  Group /general/optogenetics/OptogeneticStimulusSite/device (Device) 
  session_id: 1290510496
  stimulus: OpenScopeTemporalBarcode
  Group /general/subject (EcephysSpecimen) 
  identifier: 1290510496
  Group /intervals/RepeatFFF_presentations (TimeIntervals) Presentation times and stimuli details for 'RepeatFFF' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/RepeatFFF_presentations/color (VectorData) No description | shape = (43200,) | dtype = object
  Dataset /intervals/RepeatFFF_presentations/contrast (VectorData) Contrast of stimulus | shape = (43200,) | dtype = float64
  Dataset /intervals/RepeatFFF_presentations/id (ElementIdentifiers)  | shape = (43200,) | dtype = int64
  Dataset /intervals/RepeatFFF_presentations/index_repeat (VectorData) No description | shape = (43200,) | dtype = float64
  Dataset /intervals/RepeatFFF_presentations/mask (VectorData) Shape of mask applied to stimulus | shape = (43200,) | dtype = object
  Dataset /intervals/RepeatFFF_presentations/opacity (VectorData) Opacity of stimulus | shape = (43200,) | dtype = float64
  Dataset /intervals/RepeatFFF_presentations/orientation (VectorData) Orientation of stimulus | shape = (43200,) | dtype = float64
  Dataset /intervals/RepeatFFF_presentations/phase (VectorData) Phase of grating stimulus | shape = (43200,) | dtype = object
  Dataset /intervals/RepeatFFF_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (43200,) | dtype = object
  Dataset /intervals/RepeatFFF_presentations/spatial_frequency (VectorData) Spatial frequency of stimulus | shape = (43200,) | dtype = object
  Dataset /intervals/RepeatFFF_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (43200,) | dtype = float64
  Dataset /intervals/RepeatFFF_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (43200,) | dtype = float64
  Dataset /intervals/RepeatFFF_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (43200,) | dtype = float64
  Dataset /intervals/RepeatFFF_presentations/stimulus_name (VectorData) Name of stimulus | shape = (43200,) | dtype = object
  Dataset /intervals/RepeatFFF_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (43200,) | dtype = float64
  Dataset /intervals/RepeatFFF_presentations/tags (VectorData) user-defined tags | shape = (43200,) | dtype = object
  Dataset /intervals/RepeatFFF_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (43200,) | dtype = uint16
  Dataset /intervals/RepeatFFF_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (43200,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/RepeatFFF_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (43200,) | dtype = uint16
  Dataset /intervals/RepeatFFF_presentations/units (VectorData) Units of stimulus size | shape = (43200,) | dtype = object
  Group /intervals/UniqueFFF_presentations (TimeIntervals) Presentation times and stimuli details for 'UniqueFFF' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/UniqueFFF_presentations/color (VectorData) No description | shape = (14400,) | dtype = object
  Dataset /intervals/UniqueFFF_presentations/contrast (VectorData) Contrast of stimulus | shape = (14400,) | dtype = float64
  Dataset /intervals/UniqueFFF_presentations/id (ElementIdentifiers)  | shape = (14400,) | dtype = int64
  Dataset /intervals/UniqueFFF_presentations/index_repeat (VectorData) No description | shape = (14400,) | dtype = float64
  Dataset /intervals/UniqueFFF_presentations/mask (VectorData) Shape of mask applied to stimulus | shape = (14400,) | dtype = object
  Dataset /intervals/UniqueFFF_presentations/opacity (VectorData) Opacity of stimulus | shape = (14400,) | dtype = float64
  Dataset /intervals/UniqueFFF_presentations/orientation (VectorData) Orientation of stimulus | shape = (14400,) | dtype = float64
  Dataset /intervals/UniqueFFF_presentations/phase (VectorData) Phase of grating stimulus | shape = (14400,) | dtype = object
  Dataset /intervals/UniqueFFF_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (14400,) | dtype = object
  Dataset /intervals/UniqueFFF_presentations/spatial_frequency (VectorData) Spatial frequency of stimulus | shape = (14400,) | dtype = object
  Dataset /intervals/UniqueFFF_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (14400,) | dtype = float64
  Dataset /intervals/UniqueFFF_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (14400,) | dtype = float64
  Dataset /intervals/UniqueFFF_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (14400,) | dtype = float64
  Dataset /intervals/UniqueFFF_presentations/stimulus_name (VectorData) Name of stimulus | shape = (14400,) | dtype = object
  Dataset /intervals/UniqueFFF_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (14400,) | dtype = float64
  Dataset /intervals/UniqueFFF_presentations/tags (VectorData) user-defined tags | shape = (14400,) | dtype = object
  Dataset /intervals/UniqueFFF_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (14400,) | dtype = uint16
  Dataset /intervals/UniqueFFF_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (14400,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/UniqueFFF_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (14400,) | dtype = uint16
  Dataset /intervals/UniqueFFF_presentations/units (VectorData) Units of stimulus size | shape = (14400,) | dtype = object
  Group /intervals/invalid_times (TimeIntervals) experimental intervals
  Dataset /intervals/invalid_times/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /intervals/invalid_times/start_time (VectorData) Start time of epoch, in seconds | shape = (1,) | dtype = float64
  Dataset /intervals/invalid_times/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1,) | dtype = float64
  Dataset /intervals/invalid_times/tags (VectorData) user-defined tags | shape = (3,) | dtype = object
  Dataset /intervals/invalid_times/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (1,) | dtype = uint8
  Group /intervals/receptive_field_block_presentations (TimeIntervals) Presentation times and stimuli details for 'receptive_field_block' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/receptive_field_block_presentations/color (VectorData) No description | shape = (1920,) | dtype = object
  Dataset /intervals/receptive_field_block_presentations/contrast (VectorData) Contrast of stimulus | shape = (1920,) | dtype = float64
  Dataset /intervals/receptive_field_block_presentations/id (ElementIdentifiers)  | shape = (1920,) | dtype = int64
  Dataset /intervals/receptive_field_block_presentations/mask (VectorData) Shape of mask applied to stimulus | shape = (1920,) | dtype = object
  Dataset /intervals/receptive_field_block_presentations/opacity (VectorData) Opacity of stimulus | shape = (1920,) | dtype = float64
  Dataset /intervals/receptive_field_block_presentations/orientation (VectorData) Orientation of stimulus | shape = (1920,) | dtype = float64
  Dataset /intervals/receptive_field_block_presentations/phase (VectorData) Phase of grating stimulus | shape = (1920,) | dtype = object
  Dataset /intervals/receptive_field_block_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (1920,) | dtype = object
  Dataset /intervals/receptive_field_block_presentations/spatial_frequency (VectorData) Spatial frequency of stimulus | shape = (1920,) | dtype = float64
  Dataset /intervals/receptive_field_block_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (1920,) | dtype = float64
  Dataset /intervals/receptive_field_block_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (1920,) | dtype = float64
  Dataset /intervals/receptive_field_block_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (1920,) | dtype = float64
  Dataset /intervals/receptive_field_block_presentations/stimulus_name (VectorData) Name of stimulus | shape = (1920,) | dtype = object
  Dataset /intervals/receptive_field_block_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1920,) | dtype = float64
  Dataset /intervals/receptive_field_block_presentations/tags (VectorData) user-defined tags | shape = (1920,) | dtype = object
  Dataset /intervals/receptive_field_block_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (1920,) | dtype = uint16
  Dataset /intervals/receptive_field_block_presentations/temporal_frequency (VectorData) Temporal frequency of stimulus | shape = (1920,) | dtype = float64
  Dataset /intervals/receptive_field_block_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (1920,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/receptive_field_block_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (1920,) | dtype = uint16
  Dataset /intervals/receptive_field_block_presentations/units (VectorData) Units of stimulus size | shape = (1920,) | dtype = object
  Dataset /intervals/receptive_field_block_presentations/x_position (VectorData) Horizontal position of stimulus on screen | shape = (1920,) | dtype = float64
  Dataset /intervals/receptive_field_block_presentations/y_position (VectorData) Vertical position of stimulus on screen | shape = (1920,) | dtype = float64
  Group /intervals/static_block_presentations (TimeIntervals) Presentation times and stimuli details for 'static_block' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/static_block_presentations/color (VectorData) No description | shape = (345600,) | dtype = object
  Dataset /intervals/static_block_presentations/contrast (VectorData) Contrast of stimulus | shape = (345600,) | dtype = float64
  Dataset /intervals/static_block_presentations/id (ElementIdentifiers)  | shape = (345600,) | dtype = int64
  Dataset /intervals/static_block_presentations/index_repeat (VectorData) No description | shape = (345600,) | dtype = float64
  Dataset /intervals/static_block_presentations/mask (VectorData) Shape of mask applied to stimulus | shape = (345600,) | dtype = object
  Dataset /intervals/static_block_presentations/opacity (VectorData) Opacity of stimulus | shape = (345600,) | dtype = float64
  Dataset /intervals/static_block_presentations/orientation (VectorData) Orientation of stimulus | shape = (345600,) | dtype = float64
  Dataset /intervals/static_block_presentations/phase (VectorData) Phase of grating stimulus | shape = (345600,) | dtype = object
  Dataset /intervals/static_block_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (345600,) | dtype = object
  Dataset /intervals/static_block_presentations/spatial_frequency (VectorData) Spatial frequency of stimulus | shape = (345600,) | dtype = object
  Dataset /intervals/static_block_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (345600,) | dtype = float64
  Dataset /intervals/static_block_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (345600,) | dtype = float64
  Dataset /intervals/static_block_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (345600,) | dtype = float64
  Dataset /intervals/static_block_presentations/stimulus_name (VectorData) Name of stimulus | shape = (345600,) | dtype = object
  Dataset /intervals/static_block_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (345600,) | dtype = float64
  Dataset /intervals/static_block_presentations/tags (VectorData) user-defined tags | shape = (345600,) | dtype = object
  Dataset /intervals/static_block_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (345600,) | dtype = uint32
  Dataset /intervals/static_block_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (345600,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/static_block_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (345600,) | dtype = uint32
  Dataset /intervals/static_block_presentations/units (VectorData) Units of stimulus size | shape = (345600,) | dtype = object
  Group /processing/optotagging (ProcessingModule) optogenetic stimulution data
  Group /processing/optotagging/optogenetic_stimulation (TimeIntervals) 
  Dataset /processing/optotagging/optogenetic_stimulation/condition (VectorData) no description | shape = (450,) | dtype = object
  Dataset /processing/optotagging/optogenetic_stimulation/duration (VectorData) no description | shape = (450,) | dtype = float64
  Dataset /processing/optotagging/optogenetic_stimulation/id (ElementIdentifiers)  | shape = (450,) | dtype = int64
  Dataset /processing/optotagging/optogenetic_stimulation/level (VectorData) no description | shape = (450,) | dtype = float64
  Dataset /processing/optotagging/optogenetic_stimulation/start_time (VectorData) Start time of epoch, in seconds | shape = (450,) | dtype = float64
  Dataset /processing/optotagging/optogenetic_stimulation/stimulus_name (VectorData) no description | shape = (450,) | dtype = object
  Dataset /processing/optotagging/optogenetic_stimulation/stop_time (VectorData) Stop time of epoch, in seconds | shape = (450,) | dtype = float64
  Dataset /processing/optotagging/optogenetic_stimulation/tags (VectorData) user-defined tags | shape = (450,) | dtype = object
  Dataset /processing/optotagging/optogenetic_stimulation/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (450,) | dtype = uint16
  Dataset /processing/optotagging/optogenetic_stimulation/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (450,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /processing/optotagging/optogenetic_stimulation/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (450,) | dtype = uint16
  Group /processing/optotagging/optotagging (OptogeneticSeries) no description
  Group /processing/optotagging/optotagging/site (OptogeneticStimulusSite) 
  Group /processing/optotagging/optotagging/site/device (Device) 
  Group /processing/running (ProcessingModule) running speed data
  Group /processing/running/running_speed (TimeSeries) no description
  Group /processing/running/running_speed_end_times (TimeSeries) no description
  Group /processing/running/running_wheel_rotation (TimeSeries) no description
  Group /processing/stimulus (ProcessingModule) Stimulus Times processing
  Group /processing/stimulus/timestamps (TimeSeries) no description
  session_description: Data and metadata for an Ecephys session
  session_start_time: 2023-08-16T00:00:00-07:00
  timestamps_reference_time: 2023-08-16T00:00:00-07:00
  Group /units (Units) 
  Dataset /units/PT_ratio (VectorData) no description | shape = (2572,) | dtype = float64
  Dataset /units/amplitude (VectorData) no description | shape = (2572,) | dtype = float64
  Dataset /units/amplitude_cutoff (VectorData) no description | shape = (2572,) | dtype = float64
  Dataset /units/cluster_id (VectorData) no description | shape = (2572,) | dtype = int64
  Dataset /units/cumulative_drift (VectorData) no description | shape = (2572,) | dtype = float64
  Dataset /units/d_prime (VectorData) no description | shape = (2572,) | dtype = float64
  Dataset /units/firing_rate (VectorData) no description | shape = (2572,) | dtype = float64
  Dataset /units/id (ElementIdentifiers)  | shape = (2572,) | dtype = int64
  Dataset /units/isi_violations (VectorData) no description | shape = (2572,) | dtype = float64
  Dataset /units/isolation_distance (VectorData) no description | shape = (2572,) | dtype = float64
  Dataset /units/l_ratio (VectorData) no description | shape = (2572,) | dtype = float64
  Dataset /units/local_index (VectorData) no description | shape = (2572,) | dtype = int64
  Dataset /units/max_drift (VectorData) no description | shape = (2572,) | dtype = float64
  Dataset /units/nn_hit_rate (VectorData) no description | shape = (2572,) | dtype = float64
  Dataset /units/nn_miss_rate (VectorData) no description | shape = (2572,) | dtype = float64
  Dataset /units/peak_channel_id (VectorData) no description | shape = (2572,) | dtype = int64
  Dataset /units/presence_ratio (VectorData) no description | shape = (2572,) | dtype = float64
  Dataset /units/quality (VectorData) no description | shape = (2572,) | dtype = object
  Dataset /units/recovery_slope (VectorData) no description | shape = (2572,) | dtype = float64
  Dataset /units/repolarization_slope (VectorData) no description | shape = (2572,) | dtype = float64
  Dataset /units/silhouette_score (VectorData) no description | shape = (2572,) | dtype = float64
  Dataset /units/snr (VectorData) no description | shape = (2572,) | dtype = float64
  Dataset /units/spike_amplitudes (VectorData) amplitude (s) of detected spiking events | shape = (96936164,) | dtype = float64
  Dataset /units/spike_amplitudes_index (VectorIndex) Index for VectorData 'spike_amplitudes' | shape = (2572,) | dtype = uint32
  Dataset /units/spike_times (VectorData) times (s) of detected spiking events | shape = (96936164,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (2572,) | dtype = uint32
  Dataset /units/spread (VectorData) no description | shape = (2572,) | dtype = float64
  Dataset /units/velocity_above (VectorData) no description | shape = (2572,) | dtype = float64
  Dataset /units/velocity_below (VectorData) no description | shape = (2572,) | dtype = float64
  Dataset /units/waveform_duration (VectorData) no description | shape = (2572,) | dtype = float64
  Dataset /units/waveform_halfwidth (VectorData) no description | shape = (2572,) | dtype = float64
  Dataset /units/waveform_mean (VectorData) mean waveforms on peak channels (over samples) | shape = (987648, 82) | dtype = float64
  Dataset /units/waveform_mean_index (VectorIndex) Index for VectorData 'waveform_mean' | shape = (2572,) | dtype = uint32


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/probe_0_lfp (LFP) 
  Group /acquisition/probe_0_lfp/probe_0_lfp_data (ElectricalSeries) no description
  Dataset /acquisition/probe_0_lfp/probe_0_lfp_data/electrodes (DynamicTableRegion) lfp channels on probe 0 | shape = (73,) | dtype = int64
  Group /acquisition/probe_0_lfp_data (ElectricalSeries) no description
  Dataset /acquisition/probe_0_lfp_data/electrodes (DynamicTableRegion) lfp channels on probe 0 | shape = (73,) | dtype = int64
  file_create_date: ['2024-02-22T21:57:24.803516-08:00']
  Group /general/devices/probeA (EcephysProbe) Neuropixels 1.0 Probe
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering, including the filter name and frequency cutoffs | shape = (73,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (73,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (73,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (73,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the electrode, in ohms | shape = (73,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/local_index (VectorData) The local index of electrode/channel on device | shape = (73,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (73,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/probe_horizontal_position (VectorData) Width-wise position of electrode/channel on device (microns) | shape = (73,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/probe_id (VectorData) The unique id of this electrode's/channel's device | shape = (73,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/probe_vertical_position (VectorData) Length-wise position of electrode/channel on device (microns) | shape = (73,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/valid_data (VectorData) Whether data from this electrode/channel is usable | shape = (73,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the position (+x is posterior) | shape = (73,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the position (+y is inferior) | shape = (73,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the position (+z is right) | shape = (73,) | dtype = float64
  Group /general/extracellular_ephys/probeA (EcephysElectrodeGroup) Ecephys Electrode Group
  Group /general/extracellular_ephys/probeA/device (EcephysProbe) Neuropixels 1.0 Probe
  institution: Allen Institute for Brain Science
  session_id: 1290510496
  stimulus: OpenScopeTemporalBarcode
  Group /general/subject (EcephysSpecimen) 
  identifier: 0
  session_description: LFP data and associated info for one probe
  session_start_time: 2023-08-16T00:00:00-07:00
  timestamps_reference_time: 2023-08-16T00:00:00-07:00


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/probe_1_lfp (LFP) 
  Group /acquisition/probe_1_lfp/probe_1_lfp_data (ElectricalSeries) no description
  Dataset /acquisition/probe_1_lfp/probe_1_lfp_data/electrodes (DynamicTableRegion) lfp channels on probe 1 | shape = (91,) | dtype = int64
  Group /acquisition/probe_1_lfp_data (ElectricalSeries) no description
  Dataset /acquisition/probe_1_lfp_data/electrodes (DynamicTableRegion) lfp channels on probe 1 | shape = (91,) | dtype = int64
  file_create_date: ['2024-02-22T21:57:24.806308-08:00']
  Group /general/devices/probeB (EcephysProbe) Neuropixels 1.0 Probe
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering, including the filter name and frequency cutoffs | shape = (91,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (91,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (91,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (91,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the electrode, in ohms | shape = (91,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/local_index (VectorData) The local index of electrode/channel on device | shape = (91,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (91,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/probe_horizontal_position (VectorData) Width-wise position of electrode/channel on device (microns) | shape = (91,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/probe_id (VectorData) The unique id of this electrode's/channel's device | shape = (91,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/probe_vertical_position (VectorData) Length-wise position of electrode/channel on device (microns) | shape = (91,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/valid_data (VectorData) Whether data from this electrode/channel is usable | shape = (91,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the position (+x is posterior) | shape = (91,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the position (+y is inferior) | shape = (91,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the position (+z is right) | shape = (91,) | dtype = float64
  Group /general/extracellular_ephys/probeB (EcephysElectrodeGroup) Ecephys Electrode Group
  Group /general/extracellular_ephys/probeB/device (EcephysProbe) Neuropixels 1.0 Probe
  institution: Allen Institute for Brain Science
  session_id: 1290510496
  stimulus: OpenScopeTemporalBarcode
  Group /general/subject (EcephysSpecimen) 
  identifier: 1
  session_description: LFP data and associated info for one probe
  session_start_time: 2023-08-16T00:00:00-07:00
  timestamps_reference_time: 2023-08-16T00:00:00-07:00


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/probe_2_lfp (LFP) 
  Group /acquisition/probe_2_lfp/probe_2_lfp_data (ElectricalSeries) no description
  Dataset /acquisition/probe_2_lfp/probe_2_lfp_data/electrodes (DynamicTableRegion) lfp channels on probe 2 | shape = (75,) | dtype = int64
  Group /acquisition/probe_2_lfp_data (ElectricalSeries) no description
  Dataset /acquisition/probe_2_lfp_data/electrodes (DynamicTableRegion) lfp channels on probe 2 | shape = (75,) | dtype = int64
  file_create_date: ['2024-02-22T21:57:24.806974-08:00']
  Group /general/devices/probeC (EcephysProbe) Neuropixels 1.0 Probe
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering, including the filter name and frequency cutoffs | shape = (75,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (75,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (75,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (75,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the electrode, in ohms | shape = (75,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/local_index (VectorData) The local index of electrode/channel on device | shape = (75,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (75,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/probe_horizontal_position (VectorData) Width-wise position of electrode/channel on device (microns) | shape = (75,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/probe_id (VectorData) The unique id of this electrode's/channel's device | shape = (75,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/probe_vertical_position (VectorData) Length-wise position of electrode/channel on device (microns) | shape = (75,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/valid_data (VectorData) Whether data from this electrode/channel is usable | shape = (75,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the position (+x is posterior) | shape = (75,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the position (+y is inferior) | shape = (75,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the position (+z is right) | shape = (75,) | dtype = float64
  Group /general/extracellular_ephys/probeC (EcephysElectrodeGroup) Ecephys Electrode Group
  Group /general/extracellular_ephys/probeC/device (EcephysProbe) Neuropixels 1.0 Probe
  institution: Allen Institute for Brain Science
  session_id: 1290510496
  stimulus: OpenScopeTemporalBarcode
  Group /general/subject (EcephysSpecimen) 
  identifier: 2
  session_description: LFP data and associated info for one probe
  session_start_time: 2023-08-16T00:00:00-07:00
  timestamps_reference_time: 2023-08-16T00:00:00-07:00


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  Group /acquisition/probe_3_lfp (LFP) 
  Group /acquisition/probe_3_lfp/probe_3_lfp_data (ElectricalSeries) no description
  Dataset /acquisition/probe_3_lfp/probe_3_lfp_data/electrodes (DynamicTableRegion) lfp channels on probe 3 | shape = (65,) | dtype = int64
  Group /acquisition/probe_3_lfp_data (ElectricalSeries) no description
  Dataset /acquisition/probe_3_lfp_data/electrodes (DynamicTableRegion) lfp channels on probe 3 | shape = (65,) | dtype = int64
  file_create_date: ['2024-02-22T22:02:14.948190-08:00']
  Group /general/devices/probeD (EcephysProbe) Neuropixels 1.0 Probe
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering, including the filter name and frequency cutoffs | shape = (65,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (65,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (65,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (65,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the electrode, in ohms | shape = (65,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/local_index (VectorData) The local index of electrode/channel on device | shape = (65,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (65,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/probe_horizontal_position (VectorData) Width-wise position of electrode/channel on device (microns) | shape = (65,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/probe_id (VectorData) The unique id of this electrode's/channel's device | shape = (65,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/probe_vertical_position (VectorData) Length-wise position of electrode/channel on device (microns) | shape = (65,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/valid_data (VectorData) Whether data from this electrode/channel is usable | shape = (65,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the position (+x is posterior) | shape = (65,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the position (+y is inferior) | shape = (65,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the position (+z is right) | shape = (65,) | dtype = float64
  Group /general/extracellular_ephys/probeD (EcephysElectrodeGroup) Ecephys Electrode Group
  Group /general/extracellular_ephys/probeD/device (EcephysProbe) Neuropixels 1.0 Probe
  institution: Allen Institute for Brain Science
  session_id: 1290510496
  stimulus: OpenScopeTemporalBarcode
  Group /general/subject (EcephysSpecimen) 
  identifier: 3
  session_description: LFP data and associated info for one probe
  session_start_time: 2023-08-16T00:00:00-07:00
  timestamps_reference_time: 2023-08-16T00:00:00-07:00
