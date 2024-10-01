
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000022/draft
name: 20191003_AIBS_mouse_ecephys_functional_connectivity
contributor: [{'name': 'Siegle, Josh', 'email': 'joshs@alleninstitute.org', 'roleName': ['dcite:Author', 'dcite:ContactPerson', 'dcite:ProjectLeader'], 'schemaKey': 'Person', 'identifier': '0000-0002-7736-4844', 'affiliation': [{'name': 'Allen Institute for Brain Science', 'schemaKey': 'Affiliation', 'includeInCitation': False}], 'includeInCitation': True}, {'name': 'Wakeman, Wayne', 'email': 'waynew@alleninstitute.org', 'roleName': ['dcite:ContactPerson', 'dcite:DataManager'], 'schemaKey': 'Person', 'identifier': '0000-0002-3693-3609', 'affiliation': [{'name': 'Allen Institute for Brain Science', 'schemaKey': 'Affiliation', 'includeInCitation': False}], 'includeInCitation': True}, {'name': 'Jia, Xiaoxuan', 'roleName': ['dcite:Validation'], 'schemaKey': 'Person', 'identifier': '0000-0001-5484-9331', 'affiliation': [{'name': 'Allen Institute for Brain Science', 'schemaKey': 'Affiliation', 'includeInCitation': False}], 'includeInCitation': True}, {'name': 'Durand, Severine', 'roleName': ['dcite:DataCollector'], 'schemaKey': 'Person', 'identifier': '0000-0001-7788-0200', 'affiliation': [{'name': 'Allen Institute for Brain Science', 'schemaKey': 'Affiliation', 'includeInCitation': False}], 'includeInCitation': True}, {'name': 'Heller, Gregg', 'roleName': ['dcite:DataCollector'], 'schemaKey': 'Person', 'identifier': '0000-0003-3552-996X', 'affiliation': [{'name': 'Allen Institute for Brain Science', 'schemaKey': 'Affiliation', 'includeInCitation': False}], 'includeInCitation': True}, {'name': 'Ramirez, Tamina', 'roleName': ['dcite:DataCollector'], 'schemaKey': 'Person', 'identifier': '0000-0002-6569-5291', 'affiliation': [{'name': 'Allen Institute for Brain Science', 'schemaKey': 'Affiliation', 'includeInCitation': False}], 'includeInCitation': True}, {'name': 'Graddis, Nile', 'roleName': ['dcite:Software'], 'schemaKey': 'Person', 'identifier': '0000-0003-1290-3912', 'affiliation': [{'name': 'Allen Institute for Brain Science', 'schemaKey': 'Affiliation', 'includeInCitation': False}], 'includeInCitation': True}, {'name': 'Mei, Nicholas', 'roleName': ['dcite:Software'], 'schemaKey': 'Person', 'identifier': '0000-0001-8893-1763', 'affiliation': [{'name': 'Allen Institute for Brain Science', 'schemaKey': 'Affiliation', 'includeInCitation': False}], 'includeInCitation': True}]
description: Allen Institute October 2019 Mouse extracellular electrophysiology data, collected under analogous conditions to the two-photon Brain Observatory imaging experiments, with mice shown a subset of stimuli with a higher number of repeats. 

For more information, see https://portal.brain-map.org/explore/circuits/visual-coding-neuropixels

Data are subject to Allen Institute Terms of Use policy, available at: http://www.alleninstitute.org/legal/terms-use/

assetsSummary: {'species': [{'name': 'House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 374956840341, 'numberOfFiles': 169, 'numberOfSubjects': 26, 'variableMeasured': ['LFP', 'ProcessingModule', 'Units'], 'measurementTechnique': [{'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'signal filtering technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000022 has 16 NWB files.
12 of these NWB files are of type 1.
1 of these NWB files are of type 2.
1 of these NWB files are of type 3.
1 of these NWB files are of type 4.
1 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/raw_running_wheel_rotation (TimeSeries) no description
  Group /acquisition/running_wheel_signal_voltage (TimeSeries) no description
  Group /acquisition/running_wheel_supply_voltage (TimeSeries) no description
  file_create_date: ['2020-05-26T00:54:16.911338-07:00']
  Group /general/devices/probeA (EcephysProbe) 
  Group /general/devices/probeB (EcephysProbe) 
  Group /general/devices/probeC (EcephysProbe) 
  Group /general/devices/probeD (EcephysProbe) 
  Group /general/devices/probeE (EcephysProbe) 
  Group /general/devices/probeF (EcephysProbe) 
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (2304,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (2304,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (2304,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (2304,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (2304,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/local_index (VectorData) The local index of electrode/channel on device | shape = (2304,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (2304,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/probe_horizontal_position (VectorData) Width-wise position of electrode/channel on device (microns) | shape = (2304,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/probe_id (VectorData) The unique id of this electrode's/channel's device | shape = (2304,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/probe_vertical_position (VectorData) Length-wise position of electrode/channel on device (microns) | shape = (2304,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/valid_data (VectorData) Whether data from this electrode/channel is usable | shape = (2304,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (2304,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (2304,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (2304,) | dtype = float64
  Group /general/extracellular_ephys/probeA (EcephysElectrodeGroup) Ecephys Electrode Group
  Group /general/extracellular_ephys/probeA/device (EcephysProbe) 
  Group /general/extracellular_ephys/probeB (EcephysElectrodeGroup) Ecephys Electrode Group
  Group /general/extracellular_ephys/probeB/device (EcephysProbe) 
  Group /general/extracellular_ephys/probeC (EcephysElectrodeGroup) Ecephys Electrode Group
  Group /general/extracellular_ephys/probeC/device (EcephysProbe) 
  Group /general/extracellular_ephys/probeD (EcephysElectrodeGroup) Ecephys Electrode Group
  Group /general/extracellular_ephys/probeD/device (EcephysProbe) 
  Group /general/extracellular_ephys/probeE (EcephysElectrodeGroup) Ecephys Electrode Group
  Group /general/extracellular_ephys/probeE/device (EcephysProbe) 
  Group /general/extracellular_ephys/probeF (EcephysElectrodeGroup) Ecephys Electrode Group
  Group /general/extracellular_ephys/probeF/device (EcephysProbe) 
  institution: Allen Institute for Brain Science
  session_id: 766640955
  stimulus: functional_connectivity
  Group /general/subject (EcephysSpecimen) 
  identifier: 766640955
  Group /intervals/dot_motion_presentations (TimeIntervals) Presentation times and stimuli details for 'dot_motion' stimuli
  Dataset /intervals/dot_motion_presentations/Dir (VectorData) Direction of stimulus motion | shape = (495,) | dtype = float64
  Dataset /intervals/dot_motion_presentations/Speed (VectorData) Speed of moving dot field | shape = (495,) | dtype = float64
  Dataset /intervals/dot_motion_presentations/coherence (VectorData) Coherence of moving dot field | shape = (495,) | dtype = float64
  Dataset /intervals/dot_motion_presentations/color (VectorData) No description | shape = (495,) | dtype = object
  Dataset /intervals/dot_motion_presentations/contrast (VectorData) Contrast of stimulus | shape = (495,) | dtype = float64
  Dataset /intervals/dot_motion_presentations/dotLife (VectorData) Longevity of individual dots | shape = (495,) | dtype = float64
  Dataset /intervals/dot_motion_presentations/dotSize (VectorData) Size of individual dots | shape = (495,) | dtype = float64
  Dataset /intervals/dot_motion_presentations/fieldPos (VectorData) Position of moving dot field | shape = (495,) | dtype = object
  Dataset /intervals/dot_motion_presentations/fieldShape (VectorData) Shape of moving dot field | shape = (495,) | dtype = object
  Dataset /intervals/dot_motion_presentations/fieldSize (VectorData) Size of moving dot field | shape = (495,) | dtype = object
  Dataset /intervals/dot_motion_presentations/id (ElementIdentifiers)  | shape = (495,) | dtype = int64
  Dataset /intervals/dot_motion_presentations/nDots (VectorData) Number of dots in moving dot field | shape = (495,) | dtype = float64
  Dataset /intervals/dot_motion_presentations/noiseDots (VectorData) No description | shape = (495,) | dtype = object
  Dataset /intervals/dot_motion_presentations/opacity (VectorData) Opacity of stimulus | shape = (495,) | dtype = float64
  Dataset /intervals/dot_motion_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (495,) | dtype = float64
  Dataset /intervals/dot_motion_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (495,) | dtype = float64
  Dataset /intervals/dot_motion_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (495,) | dtype = float64
  Dataset /intervals/dot_motion_presentations/stimulus_name (VectorData) Name of stimulus | shape = (495,) | dtype = object
  Dataset /intervals/dot_motion_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (495,) | dtype = float64
  Dataset /intervals/dot_motion_presentations/tags (VectorData) user-defined tags | shape = (495,) | dtype = object
  Dataset /intervals/dot_motion_presentations/tags_index (VectorIndex)  | shape = (495,) | dtype = int64
  Dataset /intervals/dot_motion_presentations/timeseries (VectorData) index into a TimeSeries object | shape = (495,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/dot_motion_presentations/timeseries_index (VectorIndex)  | shape = (495,) | dtype = int64
  Dataset /intervals/dot_motion_presentations/units (VectorData) Units of stimulus size | shape = (495,) | dtype = object
  Group /intervals/drifting_gratings_75_repeats_presentations (TimeIntervals) Presentation times and stimuli details for 'drifting_gratings_75_repeats' stimuli
  Dataset /intervals/drifting_gratings_75_repeats_presentations/color (VectorData) No description | shape = (600,) | dtype = object
  Dataset /intervals/drifting_gratings_75_repeats_presentations/contrast (VectorData) Contrast of stimulus | shape = (600,) | dtype = float64
  Dataset /intervals/drifting_gratings_75_repeats_presentations/id (ElementIdentifiers)  | shape = (600,) | dtype = int64
  Dataset /intervals/drifting_gratings_75_repeats_presentations/mask (VectorData) Shape of mask applied to stimulus | shape = (600,) | dtype = object
  Dataset /intervals/drifting_gratings_75_repeats_presentations/opacity (VectorData) Opacity of stimulus | shape = (600,) | dtype = float64
  Dataset /intervals/drifting_gratings_75_repeats_presentations/orientation (VectorData) Orientation of stimulus | shape = (600,) | dtype = float64
  Dataset /intervals/drifting_gratings_75_repeats_presentations/phase (VectorData) Phase of grating stimulus | shape = (600,) | dtype = object
  Dataset /intervals/drifting_gratings_75_repeats_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (600,) | dtype = object
  Dataset /intervals/drifting_gratings_75_repeats_presentations/spatial_frequency (VectorData) Spatial frequency of stimulus | shape = (600,) | dtype = float64
  Dataset /intervals/drifting_gratings_75_repeats_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (600,) | dtype = float64
  Dataset /intervals/drifting_gratings_75_repeats_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (600,) | dtype = float64
  Dataset /intervals/drifting_gratings_75_repeats_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (600,) | dtype = float64
  Dataset /intervals/drifting_gratings_75_repeats_presentations/stimulus_name (VectorData) Name of stimulus | shape = (600,) | dtype = object
  Dataset /intervals/drifting_gratings_75_repeats_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (600,) | dtype = float64
  Dataset /intervals/drifting_gratings_75_repeats_presentations/tags (VectorData) user-defined tags | shape = (600,) | dtype = object
  Dataset /intervals/drifting_gratings_75_repeats_presentations/tags_index (VectorIndex)  | shape = (600,) | dtype = int64
  Dataset /intervals/drifting_gratings_75_repeats_presentations/temporal_frequency (VectorData) Temporal frequency of stimulus | shape = (600,) | dtype = float64
  Dataset /intervals/drifting_gratings_75_repeats_presentations/timeseries (VectorData) index into a TimeSeries object | shape = (600,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/drifting_gratings_75_repeats_presentations/timeseries_index (VectorIndex)  | shape = (600,) | dtype = int64
  Dataset /intervals/drifting_gratings_75_repeats_presentations/units (VectorData) Units of stimulus size | shape = (600,) | dtype = object
  Group /intervals/drifting_gratings_contrast_presentations (TimeIntervals) Presentation times and stimuli details for 'drifting_gratings_contrast' stimuli
  Dataset /intervals/drifting_gratings_contrast_presentations/color (VectorData) No description | shape = (540,) | dtype = object
  Dataset /intervals/drifting_gratings_contrast_presentations/contrast (VectorData) Contrast of stimulus | shape = (540,) | dtype = float64
  Dataset /intervals/drifting_gratings_contrast_presentations/id (ElementIdentifiers)  | shape = (540,) | dtype = int64
  Dataset /intervals/drifting_gratings_contrast_presentations/mask (VectorData) Shape of mask applied to stimulus | shape = (540,) | dtype = object
  Dataset /intervals/drifting_gratings_contrast_presentations/opacity (VectorData) Opacity of stimulus | shape = (540,) | dtype = float64
  Dataset /intervals/drifting_gratings_contrast_presentations/orientation (VectorData) Orientation of stimulus | shape = (540,) | dtype = float64
  Dataset /intervals/drifting_gratings_contrast_presentations/phase (VectorData) Phase of grating stimulus | shape = (540,) | dtype = object
  Dataset /intervals/drifting_gratings_contrast_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (540,) | dtype = object
  Dataset /intervals/drifting_gratings_contrast_presentations/spatial_frequency (VectorData) Spatial frequency of stimulus | shape = (540,) | dtype = object
  Dataset /intervals/drifting_gratings_contrast_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (540,) | dtype = float64
  Dataset /intervals/drifting_gratings_contrast_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (540,) | dtype = float64
  Dataset /intervals/drifting_gratings_contrast_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (540,) | dtype = float64
  Dataset /intervals/drifting_gratings_contrast_presentations/stimulus_name (VectorData) Name of stimulus | shape = (540,) | dtype = object
  Dataset /intervals/drifting_gratings_contrast_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (540,) | dtype = float64
  Dataset /intervals/drifting_gratings_contrast_presentations/tags (VectorData) user-defined tags | shape = (540,) | dtype = object
  Dataset /intervals/drifting_gratings_contrast_presentations/tags_index (VectorIndex)  | shape = (540,) | dtype = int64
  Dataset /intervals/drifting_gratings_contrast_presentations/temporal_frequency (VectorData) Temporal frequency of stimulus | shape = (540,) | dtype = float64
  Dataset /intervals/drifting_gratings_contrast_presentations/timeseries (VectorData) index into a TimeSeries object | shape = (540,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/drifting_gratings_contrast_presentations/timeseries_index (VectorIndex)  | shape = (540,) | dtype = int64
  Dataset /intervals/drifting_gratings_contrast_presentations/units (VectorData) Units of stimulus size | shape = (540,) | dtype = object
  Group /intervals/flashes_presentations (TimeIntervals) Presentation times and stimuli details for 'flashes' stimuli
  Dataset /intervals/flashes_presentations/color (VectorData) No description | shape = (150,) | dtype = object
  Dataset /intervals/flashes_presentations/contrast (VectorData) Contrast of stimulus | shape = (150,) | dtype = float64
  Dataset /intervals/flashes_presentations/id (ElementIdentifiers)  | shape = (150,) | dtype = int64
  Dataset /intervals/flashes_presentations/mask (VectorData) Shape of mask applied to stimulus | shape = (150,) | dtype = object
  Dataset /intervals/flashes_presentations/opacity (VectorData) Opacity of stimulus | shape = (150,) | dtype = float64
  Dataset /intervals/flashes_presentations/orientation (VectorData) Orientation of stimulus | shape = (150,) | dtype = float64
  Dataset /intervals/flashes_presentations/phase (VectorData) Phase of grating stimulus | shape = (150,) | dtype = object
  Dataset /intervals/flashes_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (150,) | dtype = object
  Dataset /intervals/flashes_presentations/spatial_frequency (VectorData) Spatial frequency of stimulus | shape = (150,) | dtype = object
  Dataset /intervals/flashes_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (150,) | dtype = float64
  Dataset /intervals/flashes_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (150,) | dtype = float64
  Dataset /intervals/flashes_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (150,) | dtype = float64
  Dataset /intervals/flashes_presentations/stimulus_name (VectorData) Name of stimulus | shape = (150,) | dtype = object
  Dataset /intervals/flashes_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (150,) | dtype = float64
  Dataset /intervals/flashes_presentations/tags (VectorData) user-defined tags | shape = (150,) | dtype = object
  Dataset /intervals/flashes_presentations/tags_index (VectorIndex)  | shape = (150,) | dtype = int64
  Dataset /intervals/flashes_presentations/timeseries (VectorData) index into a TimeSeries object | shape = (150,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/flashes_presentations/timeseries_index (VectorIndex)  | shape = (150,) | dtype = int64
  Dataset /intervals/flashes_presentations/units (VectorData) Units of stimulus size | shape = (150,) | dtype = object
  Group /intervals/gabors_presentations (TimeIntervals) Presentation times and stimuli details for 'gabors' stimuli
  Dataset /intervals/gabors_presentations/color (VectorData) No description | shape = (3645,) | dtype = object
  Dataset /intervals/gabors_presentations/contrast (VectorData) Contrast of stimulus | shape = (3645,) | dtype = float64
  Dataset /intervals/gabors_presentations/id (ElementIdentifiers)  | shape = (3645,) | dtype = int64
  Dataset /intervals/gabors_presentations/mask (VectorData) Shape of mask applied to stimulus | shape = (3645,) | dtype = object
  Dataset /intervals/gabors_presentations/opacity (VectorData) Opacity of stimulus | shape = (3645,) | dtype = float64
  Dataset /intervals/gabors_presentations/orientation (VectorData) Orientation of stimulus | shape = (3645,) | dtype = float64
  Dataset /intervals/gabors_presentations/phase (VectorData) Phase of grating stimulus | shape = (3645,) | dtype = object
  Dataset /intervals/gabors_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (3645,) | dtype = object
  Dataset /intervals/gabors_presentations/spatial_frequency (VectorData) Spatial frequency of stimulus | shape = (3645,) | dtype = object
  Dataset /intervals/gabors_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (3645,) | dtype = float64
  Dataset /intervals/gabors_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (3645,) | dtype = float64
  Dataset /intervals/gabors_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (3645,) | dtype = float64
  Dataset /intervals/gabors_presentations/stimulus_name (VectorData) Name of stimulus | shape = (3645,) | dtype = object
  Dataset /intervals/gabors_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (3645,) | dtype = float64
  Dataset /intervals/gabors_presentations/tags (VectorData) user-defined tags | shape = (3645,) | dtype = object
  Dataset /intervals/gabors_presentations/tags_index (VectorIndex)  | shape = (3645,) | dtype = int64
  Dataset /intervals/gabors_presentations/temporal_frequency (VectorData) Temporal frequency of stimulus | shape = (3645,) | dtype = float64
  Dataset /intervals/gabors_presentations/timeseries (VectorData) index into a TimeSeries object | shape = (3645,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/gabors_presentations/timeseries_index (VectorIndex)  | shape = (3645,) | dtype = int64
  Dataset /intervals/gabors_presentations/units (VectorData) Units of stimulus size | shape = (3645,) | dtype = object
  Dataset /intervals/gabors_presentations/x_position (VectorData) Horizontal position of stimulus on screen | shape = (3645,) | dtype = float64
  Dataset /intervals/gabors_presentations/y_position (VectorData) Vertical position of stimulus on screen | shape = (3645,) | dtype = float64
  Group /intervals/natural_movie_one_more_repeats_presentations (TimeIntervals) Presentation times and stimuli details for 'natural_movie_one_more_repeats' stimuli
  Dataset /intervals/natural_movie_one_more_repeats_presentations/color (VectorData) No description | shape = (54000,) | dtype = object
  Dataset /intervals/natural_movie_one_more_repeats_presentations/contrast (VectorData) Contrast of stimulus | shape = (54000,) | dtype = float64
  Dataset /intervals/natural_movie_one_more_repeats_presentations/frame (VectorData) Frame of movie stimulus | shape = (54000,) | dtype = float64
  Dataset /intervals/natural_movie_one_more_repeats_presentations/id (ElementIdentifiers)  | shape = (54000,) | dtype = int64
  Dataset /intervals/natural_movie_one_more_repeats_presentations/opacity (VectorData) Opacity of stimulus | shape = (54000,) | dtype = float64
  Dataset /intervals/natural_movie_one_more_repeats_presentations/orientation (VectorData) Orientation of stimulus | shape = (54000,) | dtype = float64
  Dataset /intervals/natural_movie_one_more_repeats_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (54000,) | dtype = object
  Dataset /intervals/natural_movie_one_more_repeats_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (54000,) | dtype = float64
  Dataset /intervals/natural_movie_one_more_repeats_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (54000,) | dtype = float64
  Dataset /intervals/natural_movie_one_more_repeats_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (54000,) | dtype = float64
  Dataset /intervals/natural_movie_one_more_repeats_presentations/stimulus_name (VectorData) Name of stimulus | shape = (54000,) | dtype = object
  Dataset /intervals/natural_movie_one_more_repeats_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (54000,) | dtype = float64
  Dataset /intervals/natural_movie_one_more_repeats_presentations/tags (VectorData) user-defined tags | shape = (54000,) | dtype = object
  Dataset /intervals/natural_movie_one_more_repeats_presentations/tags_index (VectorIndex)  | shape = (54000,) | dtype = int64
  Dataset /intervals/natural_movie_one_more_repeats_presentations/timeseries (VectorData) index into a TimeSeries object | shape = (54000,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/natural_movie_one_more_repeats_presentations/timeseries_index (VectorIndex)  | shape = (54000,) | dtype = int64
  Dataset /intervals/natural_movie_one_more_repeats_presentations/units (VectorData) Units of stimulus size | shape = (54000,) | dtype = object
  Group /intervals/natural_movie_one_shuffled_presentations (TimeIntervals) Presentation times and stimuli details for 'natural_movie_one_shuffled' stimuli
  Dataset /intervals/natural_movie_one_shuffled_presentations/color (VectorData) No description | shape = (18000,) | dtype = object
  Dataset /intervals/natural_movie_one_shuffled_presentations/contrast (VectorData) Contrast of stimulus | shape = (18000,) | dtype = float64
  Dataset /intervals/natural_movie_one_shuffled_presentations/frame (VectorData) Frame of movie stimulus | shape = (18000,) | dtype = float64
  Dataset /intervals/natural_movie_one_shuffled_presentations/id (ElementIdentifiers)  | shape = (18000,) | dtype = int64
  Dataset /intervals/natural_movie_one_shuffled_presentations/opacity (VectorData) Opacity of stimulus | shape = (18000,) | dtype = float64
  Dataset /intervals/natural_movie_one_shuffled_presentations/orientation (VectorData) Orientation of stimulus | shape = (18000,) | dtype = float64
  Dataset /intervals/natural_movie_one_shuffled_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (18000,) | dtype = object
  Dataset /intervals/natural_movie_one_shuffled_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (18000,) | dtype = float64
  Dataset /intervals/natural_movie_one_shuffled_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (18000,) | dtype = float64
  Dataset /intervals/natural_movie_one_shuffled_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (18000,) | dtype = float64
  Dataset /intervals/natural_movie_one_shuffled_presentations/stimulus_name (VectorData) Name of stimulus | shape = (18000,) | dtype = object
  Dataset /intervals/natural_movie_one_shuffled_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (18000,) | dtype = float64
  Dataset /intervals/natural_movie_one_shuffled_presentations/tags (VectorData) user-defined tags | shape = (18000,) | dtype = object
  Dataset /intervals/natural_movie_one_shuffled_presentations/tags_index (VectorIndex)  | shape = (18000,) | dtype = int64
  Dataset /intervals/natural_movie_one_shuffled_presentations/timeseries (VectorData) index into a TimeSeries object | shape = (18000,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/natural_movie_one_shuffled_presentations/timeseries_index (VectorIndex)  | shape = (18000,) | dtype = int64
  Dataset /intervals/natural_movie_one_shuffled_presentations/units (VectorData) Units of stimulus size | shape = (18000,) | dtype = object
  Group /intervals/spontaneous_presentations (TimeIntervals) Presentation times and stimuli details for 'spontaneous' stimuli
  Dataset /intervals/spontaneous_presentations/id (ElementIdentifiers)  | shape = (6,) | dtype = int64
  Dataset /intervals/spontaneous_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (6,) | dtype = float64
  Dataset /intervals/spontaneous_presentations/stimulus_name (VectorData) Name of stimulus | shape = (6,) | dtype = object
  Dataset /intervals/spontaneous_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (6,) | dtype = float64
  Dataset /intervals/spontaneous_presentations/tags (VectorData) user-defined tags | shape = (6,) | dtype = object
  Dataset /intervals/spontaneous_presentations/tags_index (VectorIndex)  | shape = (6,) | dtype = int64
  Dataset /intervals/spontaneous_presentations/timeseries (VectorData) index into a TimeSeries object | shape = (6,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/spontaneous_presentations/timeseries_index (VectorIndex)  | shape = (6,) | dtype = int64
  Group /processing/eye_tracking (ProcessingModule) Eye tracking processing module
  Group /processing/eye_tracking/cr_ellipse_fits (DynamicTable) 
  Dataset /processing/eye_tracking/cr_ellipse_fits/center_x (VectorData) no description | shape = (293237,) | dtype = float64
  Dataset /processing/eye_tracking/cr_ellipse_fits/center_y (VectorData) no description | shape = (293237,) | dtype = float64
  Dataset /processing/eye_tracking/cr_ellipse_fits/height (VectorData) no description | shape = (293237,) | dtype = float64
  Dataset /processing/eye_tracking/cr_ellipse_fits/id (ElementIdentifiers)  | shape = (293237,) | dtype = int64
  Dataset /processing/eye_tracking/cr_ellipse_fits/phi (VectorData) no description | shape = (293237,) | dtype = float64
  Dataset /processing/eye_tracking/cr_ellipse_fits/timestamps (VectorData) no description | shape = (293237,) | dtype = float64
  Dataset /processing/eye_tracking/cr_ellipse_fits/width (VectorData) no description | shape = (293237,) | dtype = float64
  Group /processing/eye_tracking/eye_ellipse_fits (DynamicTable) 
  Dataset /processing/eye_tracking/eye_ellipse_fits/center_x (VectorData) no description | shape = (293237,) | dtype = float64
  Dataset /processing/eye_tracking/eye_ellipse_fits/center_y (VectorData) no description | shape = (293237,) | dtype = float64
  Dataset /processing/eye_tracking/eye_ellipse_fits/height (VectorData) no description | shape = (293237,) | dtype = float64
  Dataset /processing/eye_tracking/eye_ellipse_fits/id (ElementIdentifiers)  | shape = (293237,) | dtype = int64
  Dataset /processing/eye_tracking/eye_ellipse_fits/phi (VectorData) no description | shape = (293237,) | dtype = float64
  Dataset /processing/eye_tracking/eye_ellipse_fits/timestamps (VectorData) no description | shape = (293237,) | dtype = float64
  Dataset /processing/eye_tracking/eye_ellipse_fits/width (VectorData) no description | shape = (293237,) | dtype = float64
  Group /processing/eye_tracking/pupil_ellipse_fits (DynamicTable) 
  Dataset /processing/eye_tracking/pupil_ellipse_fits/center_x (VectorData) no description | shape = (293237,) | dtype = float64
  Dataset /processing/eye_tracking/pupil_ellipse_fits/center_y (VectorData) no description | shape = (293237,) | dtype = float64
  Dataset /processing/eye_tracking/pupil_ellipse_fits/height (VectorData) no description | shape = (293237,) | dtype = float64
  Dataset /processing/eye_tracking/pupil_ellipse_fits/id (ElementIdentifiers)  | shape = (293237,) | dtype = int64
  Dataset /processing/eye_tracking/pupil_ellipse_fits/phi (VectorData) no description | shape = (293237,) | dtype = float64
  Dataset /processing/eye_tracking/pupil_ellipse_fits/timestamps (VectorData) no description | shape = (293237,) | dtype = float64
  Dataset /processing/eye_tracking/pupil_ellipse_fits/width (VectorData) no description | shape = (293237,) | dtype = float64
  Group /processing/eye_tracking_rig_metadata (ProcessingModule) Eye tracking rig metadata module
  Group /processing/eye_tracking_rig_metadata/eye_tracking_rig_metadata (EcephysEyeTrackingRigMetadata) 
  Group /processing/filtered_gaze_mapping (ProcessingModule) Gaze mapping processing module filtered outputs
  Group /processing/filtered_gaze_mapping/eye_area (TimeSeries) no description
  Group /processing/filtered_gaze_mapping/pupil_area (TimeSeries) no description
  Group /processing/filtered_gaze_mapping/screen_coordinates (TimeSeries) no description
  Group /processing/filtered_gaze_mapping/screen_coordinates_spherical (TimeSeries) no description
  Group /processing/optotagging (ProcessingModule) optogenetic stimulution data
  Group /processing/optotagging/optogenetic_stimulation (TimeIntervals) 
  Dataset /processing/optotagging/optogenetic_stimulation/condition (VectorData) no description | shape = (180,) | dtype = object
  Dataset /processing/optotagging/optogenetic_stimulation/duration (VectorData) no description | shape = (180,) | dtype = float64
  Dataset /processing/optotagging/optogenetic_stimulation/id (ElementIdentifiers)  | shape = (180,) | dtype = int64
  Dataset /processing/optotagging/optogenetic_stimulation/level (VectorData) no description | shape = (180,) | dtype = float64
  Dataset /processing/optotagging/optogenetic_stimulation/start_time (VectorData) Start time of epoch, in seconds | shape = (180,) | dtype = float64
  Dataset /processing/optotagging/optogenetic_stimulation/stimulus_name (VectorData) no description | shape = (180,) | dtype = object
  Dataset /processing/optotagging/optogenetic_stimulation/stop_time (VectorData) Stop time of epoch, in seconds | shape = (180,) | dtype = float64
  Dataset /processing/optotagging/optogenetic_stimulation/tags (VectorData) user-defined tags | shape = (180,) | dtype = object
  Dataset /processing/optotagging/optogenetic_stimulation/tags_index (VectorIndex)  | shape = (180,) | dtype = int64
  Dataset /processing/optotagging/optogenetic_stimulation/timeseries (VectorData) index into a TimeSeries object | shape = (180,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /processing/optotagging/optogenetic_stimulation/timeseries_index (VectorIndex)  | shape = (180,) | dtype = int64
  Group /processing/optotagging/optotagging (TimeSeries) no description
  Group /processing/raw_gaze_mapping (ProcessingModule) Gaze mapping processing module raw outputs
  Group /processing/raw_gaze_mapping/eye_area (TimeSeries) no description
  Group /processing/raw_gaze_mapping/pupil_area (TimeSeries) no description
  Group /processing/raw_gaze_mapping/screen_coordinates (TimeSeries) no description
  Group /processing/raw_gaze_mapping/screen_coordinates_spherical (TimeSeries) no description
  Group /processing/running (ProcessingModule) running speed data
  Group /processing/running/running_speed (TimeSeries) no description
  Group /processing/running/running_speed_end_times (TimeSeries) no description
  Group /processing/running/running_wheel_rotation (TimeSeries) no description
  Group /processing/stimulus (ProcessingModule) Stimulus Times processing
  Group /processing/stimulus/timestamps (TimeSeries) no description
  session_description: Data and metadata for an Ecephys session
  session_start_time: 2019-01-02T15:45:39-08:00
  timestamps_reference_time: 2019-01-02T15:45:39-08:00
  Group /units (Units) 
  Dataset /units/PT_ratio (VectorData) no description | shape = (2890,) | dtype = float64
  Dataset /units/amplitude (VectorData) no description | shape = (2890,) | dtype = float64
  Dataset /units/amplitude_cutoff (VectorData) no description | shape = (2890,) | dtype = float64
  Dataset /units/cluster_id (VectorData) no description | shape = (2890,) | dtype = int64
  Dataset /units/cumulative_drift (VectorData) no description | shape = (2890,) | dtype = float64
  Dataset /units/d_prime (VectorData) no description | shape = (2890,) | dtype = float64
  Dataset /units/firing_rate (VectorData) no description | shape = (2890,) | dtype = float64
  Dataset /units/id (ElementIdentifiers)  | shape = (2890,) | dtype = int64
  Dataset /units/isi_violations (VectorData) no description | shape = (2890,) | dtype = float64
  Dataset /units/isolation_distance (VectorData) no description | shape = (2890,) | dtype = float64
  Dataset /units/l_ratio (VectorData) no description | shape = (2890,) | dtype = float64
  Dataset /units/local_index (VectorData) no description | shape = (2890,) | dtype = int64
  Dataset /units/max_drift (VectorData) no description | shape = (2890,) | dtype = float64
  Dataset /units/nn_hit_rate (VectorData) no description | shape = (2890,) | dtype = float64
  Dataset /units/nn_miss_rate (VectorData) no description | shape = (2890,) | dtype = float64
  Dataset /units/peak_channel_id (VectorData) no description | shape = (2890,) | dtype = int64
  Dataset /units/presence_ratio (VectorData) no description | shape = (2890,) | dtype = float64
  Dataset /units/quality (VectorData) no description | shape = (2890,) | dtype = object
  Dataset /units/recovery_slope (VectorData) no description | shape = (2890,) | dtype = float64
  Dataset /units/repolarization_slope (VectorData) no description | shape = (2890,) | dtype = float64
  Dataset /units/silhouette_score (VectorData) no description | shape = (2890,) | dtype = float64
  Dataset /units/snr (VectorData) no description | shape = (2890,) | dtype = float64
  Dataset /units/spike_amplitudes (VectorData) amplitude (s) of detected spiking events | shape = (124754105,) | dtype = float64
  Dataset /units/spike_amplitudes_index (VectorIndex)  | shape = (2890,) | dtype = int64
  Dataset /units/spike_times (VectorData) times (s) of detected spiking events | shape = (124754105,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex)  | shape = (2890,) | dtype = int64
  Dataset /units/spread (VectorData) no description | shape = (2890,) | dtype = float64
  Dataset /units/velocity_above (VectorData) no description | shape = (2890,) | dtype = float64
  Dataset /units/velocity_below (VectorData) no description | shape = (2890,) | dtype = float64
  Dataset /units/waveform_duration (VectorData) no description | shape = (2890,) | dtype = float64
  Dataset /units/waveform_halfwidth (VectorData) no description | shape = (2890,) | dtype = float64
  Dataset /units/waveform_mean (VectorData) mean waveforms on peak channels (and over samples) | shape = (1109760, 82) | dtype = float64
  Dataset /units/waveform_mean_index (VectorIndex)  | shape = (2890,) | dtype = int64


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/probe_773592315_lfp (LFP) 
  Group /acquisition/probe_773592315_lfp/probe_773592315_lfp_data (ElectricalSeries) no description
  Dataset /acquisition/probe_773592315_lfp/probe_773592315_lfp_data/electrodes (DynamicTableRegion) lfp channels on probe 773592315 | shape = (88,) | dtype = int64
  Group /acquisition/probe_773592315_lfp_data (ElectricalSeries) no description
  Dataset /acquisition/probe_773592315_lfp_data/electrodes (DynamicTableRegion) lfp channels on probe 773592315 | shape = (88,) | dtype = int64
  file_create_date: ['2020-05-26T00:59:25.694063-07:00']
  Group /general/devices/probeA (EcephysProbe) 
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (88,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (88,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (88,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (88,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (88,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/local_index (VectorData) The local index of electrode/channel on device | shape = (88,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (88,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/probe_horizontal_position (VectorData) Width-wise position of electrode/channel on device (microns) | shape = (88,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/probe_id (VectorData) The unique id of this electrode's/channel's device | shape = (88,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/probe_vertical_position (VectorData) Length-wise position of electrode/channel on device (microns) | shape = (88,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/valid_data (VectorData) Whether data from this electrode/channel is usable | shape = (88,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (88,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (88,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (88,) | dtype = float64
  Group /general/extracellular_ephys/probeA (EcephysElectrodeGroup) Ecephys Electrode Group
  Group /general/extracellular_ephys/probeA/device (EcephysProbe) 
  institution: Allen Institute for Brain Science
  session_id: 766640955
  stimulus: functional_connectivity
  Group /general/subject (EcephysSpecimen) 
  identifier: 773592315
  Group /processing/current_source_density (ProcessingModule) Precalculated current source density from interpolated channel locations.
  Group /processing/current_source_density/ecephys_csd (EcephysCSD) 
  Group /processing/current_source_density/ecephys_csd/current_source_density (TimeSeries) no description
  session_description: LFP data and associated channel info for a single Ecephys probe
  session_start_time: 2019-01-02T15:45:39-08:00
  timestamps_reference_time: 2019-01-02T15:45:39-08:00


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/probe_773592318_lfp (LFP) 
  Group /acquisition/probe_773592318_lfp/probe_773592318_lfp_data (ElectricalSeries) no description
  Dataset /acquisition/probe_773592318_lfp/probe_773592318_lfp_data/electrodes (DynamicTableRegion) lfp channels on probe 773592318 | shape = (89,) | dtype = int64
  Group /acquisition/probe_773592318_lfp_data (ElectricalSeries) no description
  Dataset /acquisition/probe_773592318_lfp_data/electrodes (DynamicTableRegion) lfp channels on probe 773592318 | shape = (89,) | dtype = int64
  file_create_date: ['2020-05-26T00:59:25.696798-07:00']
  Group /general/devices/probeB (EcephysProbe) 
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (89,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (89,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (89,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (89,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (89,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/local_index (VectorData) The local index of electrode/channel on device | shape = (89,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (89,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/probe_horizontal_position (VectorData) Width-wise position of electrode/channel on device (microns) | shape = (89,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/probe_id (VectorData) The unique id of this electrode's/channel's device | shape = (89,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/probe_vertical_position (VectorData) Length-wise position of electrode/channel on device (microns) | shape = (89,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/valid_data (VectorData) Whether data from this electrode/channel is usable | shape = (89,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (89,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (89,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (89,) | dtype = float64
  Group /general/extracellular_ephys/probeB (EcephysElectrodeGroup) Ecephys Electrode Group
  Group /general/extracellular_ephys/probeB/device (EcephysProbe) 
  institution: Allen Institute for Brain Science
  session_id: 766640955
  stimulus: functional_connectivity
  Group /general/subject (EcephysSpecimen) 
  identifier: 773592318
  Group /processing/current_source_density (ProcessingModule) Precalculated current source density from interpolated channel locations.
  Group /processing/current_source_density/ecephys_csd (EcephysCSD) 
  Group /processing/current_source_density/ecephys_csd/current_source_density (TimeSeries) no description
  session_description: LFP data and associated channel info for a single Ecephys probe
  session_start_time: 2019-01-02T15:45:39-08:00
  timestamps_reference_time: 2019-01-02T15:45:39-08:00


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/probe_773592320_lfp (LFP) 
  Group /acquisition/probe_773592320_lfp/probe_773592320_lfp_data (ElectricalSeries) no description
  Dataset /acquisition/probe_773592320_lfp/probe_773592320_lfp_data/electrodes (DynamicTableRegion) lfp channels on probe 773592320 | shape = (82,) | dtype = int64
  Group /acquisition/probe_773592320_lfp_data (ElectricalSeries) no description
  Dataset /acquisition/probe_773592320_lfp_data/electrodes (DynamicTableRegion) lfp channels on probe 773592320 | shape = (82,) | dtype = int64
  file_create_date: ['2020-05-26T00:59:25.703606-07:00']
  Group /general/devices/probeC (EcephysProbe) 
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (82,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (82,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (82,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (82,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (82,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/local_index (VectorData) The local index of electrode/channel on device | shape = (82,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (82,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/probe_horizontal_position (VectorData) Width-wise position of electrode/channel on device (microns) | shape = (82,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/probe_id (VectorData) The unique id of this electrode's/channel's device | shape = (82,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/probe_vertical_position (VectorData) Length-wise position of electrode/channel on device (microns) | shape = (82,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/valid_data (VectorData) Whether data from this electrode/channel is usable | shape = (82,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (82,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (82,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (82,) | dtype = float64
  Group /general/extracellular_ephys/probeC (EcephysElectrodeGroup) Ecephys Electrode Group
  Group /general/extracellular_ephys/probeC/device (EcephysProbe) 
  institution: Allen Institute for Brain Science
  session_id: 766640955
  stimulus: functional_connectivity
  Group /general/subject (EcephysSpecimen) 
  identifier: 773592320
  Group /processing/current_source_density (ProcessingModule) Precalculated current source density from interpolated channel locations.
  Group /processing/current_source_density/ecephys_csd (EcephysCSD) 
  Group /processing/current_source_density/ecephys_csd/current_source_density (TimeSeries) no description
  session_description: LFP data and associated channel info for a single Ecephys probe
  session_start_time: 2019-01-02T15:45:39-08:00
  timestamps_reference_time: 2019-01-02T15:45:39-08:00


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  Group /acquisition/probe_773592324_lfp (LFP) 
  Group /acquisition/probe_773592324_lfp/probe_773592324_lfp_data (ElectricalSeries) no description
  Dataset /acquisition/probe_773592324_lfp/probe_773592324_lfp_data/electrodes (DynamicTableRegion) lfp channels on probe 773592324 | shape = (76,) | dtype = int64
  Group /acquisition/probe_773592324_lfp_data (ElectricalSeries) no description
  Dataset /acquisition/probe_773592324_lfp_data/electrodes (DynamicTableRegion) lfp channels on probe 773592324 | shape = (76,) | dtype = int64
  file_create_date: ['2020-05-26T01:04:52.167553-07:00']
  Group /general/devices/probeD (EcephysProbe) 
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (76,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (76,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (76,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (76,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (76,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/local_index (VectorData) The local index of electrode/channel on device | shape = (76,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (76,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/probe_horizontal_position (VectorData) Width-wise position of electrode/channel on device (microns) | shape = (76,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/probe_id (VectorData) The unique id of this electrode's/channel's device | shape = (76,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/probe_vertical_position (VectorData) Length-wise position of electrode/channel on device (microns) | shape = (76,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/valid_data (VectorData) Whether data from this electrode/channel is usable | shape = (76,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (76,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (76,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (76,) | dtype = float64
  Group /general/extracellular_ephys/probeD (EcephysElectrodeGroup) Ecephys Electrode Group
  Group /general/extracellular_ephys/probeD/device (EcephysProbe) 
  institution: Allen Institute for Brain Science
  session_id: 766640955
  stimulus: functional_connectivity
  Group /general/subject (EcephysSpecimen) 
  identifier: 773592324
  Group /processing/current_source_density (ProcessingModule) Precalculated current source density from interpolated channel locations.
  Group /processing/current_source_density/ecephys_csd (EcephysCSD) 
  Group /processing/current_source_density/ecephys_csd/current_source_density (TimeSeries) no description
  session_description: LFP data and associated channel info for a single Ecephys probe
  session_start_time: 2019-01-02T15:45:39-08:00
  timestamps_reference_time: 2019-01-02T15:45:39-08:00
