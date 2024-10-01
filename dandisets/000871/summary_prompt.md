
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000871/draft
name: Allen Institute Openscope - Predictive Learning and Somato-dendritic Coupling
contributor: [{'name': 'National Institutes of Health (NIH)', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': '1 U24 NS 113646-02', 'contactPoint': [], 'includeInCitation': False}, {'name': 'Pina, Jason', 'email': 'Jay.e.pina@gmail.com', 'roleName': ['dcite:ContactPerson', 'dcite:ProjectMember'], 'schemaKey': 'Person', 'identifier': '0000-0003-1385-8762', 'affiliation': [], 'includeInCitation': True}, {'name': 'Henley, Tim', 'email': 'thenleyt@yorku.ca', 'roleName': ['dcite:ProjectManager'], 'schemaKey': 'Person', 'identifier': '0000-0001-7327-9055', 'affiliation': [], 'includeInCitation': True}, {'name': 'Tindall, Josh', 'email': 'joshua.tindall@mail.mcgill.ca', 'roleName': ['dcite:ProjectMember'], 'schemaKey': 'Person', 'identifier': '0000-0001-7327-9055', 'affiliation': [], 'includeInCitation': True}, {'name': 'Richards, Blake', 'email': 'blake.richards@mila.quebec', 'roleName': [], 'schemaKey': 'Person', 'identifier': '0000-0001-9662-2151', 'affiliation': [], 'includeInCitation': True}, {'name': 'Zylberberg, Joel', 'email': 'joel.zylberberg@gmail.com', 'roleName': ['dcite:ContactPerson', 'dcite:ProjectMember'], 'schemaKey': 'Person', 'identifier': '0000-0002-8208-5698', 'affiliation': [], 'includeInCitation': True}, {'name': 'York University', 'roleName': [], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/05fq50484', 'contactPoint': [], 'includeInCitation': False}, {'name': 'McGill University', 'roleName': [], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01pxwe438', 'contactPoint': [], 'includeInCitation': False}, {'name': 'Vector University', 'roleName': [], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/03kqdja62', 'contactPoint': [], 'includeInCitation': False}, {'name': 'MILA', 'roleName': [], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/05c22rx21', 'contactPoint': [], 'includeInCitation': False}, {'name': 'Allen Institute ', 'roleName': [], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/03cpe7c52', 'contactPoint': [], 'includeInCitation': False}]
description: This dataset was collected for the Dendritic Coupling project, as part of the Allen Institute's OpenScope project. 
Predictive coding hypotheses posit that perception is an active process whereby brain regions predict incoming sensory inputs, against which they are compared by other neural populations.  Mismatches between predictions and inputs result in error signals that can then be used to update the predictive model encoded in synaptic weights, thereby driving plasticity. Although increasing amounts of evidence are consistent with the general framework, many different algorithmic implementations have been proposed, requiring further experiments to test specific corollaries of these varied approaches.  One important, testable implication distinguishing some current theories involves the coupling strength in L2/3 and L5 pyramidal neurons between distal apical dendrites, which tend to receive top-down inputs that may include sensory prediction data, and their conjoined somata, which are often driven by bottom-up inputs. In particular, error signals are computed or else collocated in apical dendrites in some implementations, resulting in a quiescent subunit when the prediction matches inputs—zero error—and, thus, reduced dendro-somatic coupling during such times. In contrast, a separate proposal implies the opposite: Since many apical dendritic voltage signals can only reach their electrotonically segregated soma when facilitated by bursting induced by concurrent somatic sensory inputs, dendro-somatic coupling would instead be strongest when top-down predictions match bottom-up signals.

Our experiment seeks to test these hypotheses by near-simultaneously imaging L2/3 and L5 somata and distal apical dendrites in mouse V1, LM, PM, and AM in transgenic lines that express GCaMP6f.  Imaging four distinct areas allows us to also examine the consistency of the coupling rules, further putting the notion of a cortical canonical microcircuit to the test.  By habituating animals to sets of visual stimuli with spatiotemporal patterns that are subsequently violated, we can evaluate the neural responses across the visual cortical hierarchy to help in adjudicating these important neuroscientific questions.

assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 6263867545400, 'numberOfFiles': 284, 'numberOfSubjects': 2, 'variableMeasured': ['ImagingPlane', 'ProcessingModule', 'OpticalChannel', 'TwoPhotonSeries', 'PlaneSegmentation'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'two-photon microscopy technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000871 has 61 NWB files.
13 of these NWB files are of type 1.
13 of these NWB files are of type 2.
13 of these NWB files are of type 3.
11 of these NWB files are of type 4.
11 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/EyeTracking (EllipseEyeTracking) 
  Group /acquisition/EyeTracking/corneal_reflection_tracking (EllipseSeries) no description
  Group /acquisition/EyeTracking/eye_tracking (EllipseSeries) no description
  Group /acquisition/EyeTracking/likely_blink (TimeSeries) blinks
  Group /acquisition/EyeTracking/pupil_tracking (EllipseSeries) no description
  Group /acquisition/denoised_suite2p_motion_corrected (TwoPhotonSeries) no description
  Group /acquisition/denoised_suite2p_motion_corrected/imaging_plane (ImagingPlane) 
  Group /acquisition/denoised_suite2p_motion_corrected/imaging_plane/channel_1 (OpticalChannel) 
  Group /acquisition/denoised_suite2p_motion_corrected/imaging_plane/device (Device) Allen Brain Observatory - Mesoscope 2P Rig
  Group /acquisition/raw_suite2p_motion_corrected (TwoPhotonSeries) no description
  Group /acquisition/raw_suite2p_motion_corrected/imaging_plane (ImagingPlane) 
  Group /acquisition/raw_suite2p_motion_corrected/imaging_plane/channel_1 (OpticalChannel) 
  Group /acquisition/raw_suite2p_motion_corrected/imaging_plane/device (Device) Allen Brain Observatory - Mesoscope 2P Rig
  Group /acquisition/v_in (TimeSeries) The theoretical maximum voltage that the running wheel encoder will reach prior to "wrapping". This should theoretically be 5V (after crossing 5V goes to 0V, or vice versa). In practice the encoder does not always reach this value before wrapping, which can cause transient spikes in speed at the voltage "wraps".
  Group /acquisition/v_sig (TimeSeries) Voltage signal from the running wheel encoder
  file_create_date: ['2024-01-21T18:31:22.932627+00:00']
  Group /general/devices/MESO.2 (Device) Allen Brain Observatory - Mesoscope 2P Rig
  experiment_description: ophys session
  institution: Allen Institute for Brain Science
  keywords: ['2-photon' 'calcium imaging' 'visual cortex' 'behavior' 'task']
  Group /general/metadata (OphysMetadata) 
  Group /general/optophysiology/imaging_plane_1 (ImagingPlane) 
  Group /general/optophysiology/imaging_plane_1/channel_1 (OpticalChannel) 
  Group /general/optophysiology/imaging_plane_1/device (Device) Allen Brain Observatory - Mesoscope 2P Rig
  Group /general/subject (Subject) 
  surgery:  Structure: VISp
  identifier: 1237345890
  Group /intervals/fixed_gabors_presentations (TimeIntervals) Presentation times and stimuli details for 'fixed_gabors' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/fixed_gabors_presentations/OriSurp (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/PosSizesAll (VectorData) No description | shape = (3000,) | dtype = float64
  Dataset /intervals/fixed_gabors_presentations/colors (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/contrs (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/depths (VectorData) No description | shape = (3000,) | dtype = float64
  Dataset /intervals/fixed_gabors_presentations/elementMask (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/elementTex (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/fieldDepth (VectorData) No description | shape = (3000,) | dtype = float64
  Dataset /intervals/fixed_gabors_presentations/fieldPos (VectorData) Position of moving dot field | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/fieldShape (VectorData) Shape of moving dot field | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/fieldSize (VectorData) Size of moving dot field | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/id (ElementIdentifiers)  | shape = (3000,) | dtype = int64
  Dataset /intervals/fixed_gabors_presentations/nElements (VectorData) No description | shape = (3000,) | dtype = float64
  Dataset /intervals/fixed_gabors_presentations/opacities (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/oris (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/phases (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/rgbs (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/sfs (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/sizes (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (3000,) | dtype = float64
  Dataset /intervals/fixed_gabors_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (3000,) | dtype = float64
  Dataset /intervals/fixed_gabors_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (3000,) | dtype = float64
  Dataset /intervals/fixed_gabors_presentations/stimulus_name (VectorData) Name of stimulus | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (3000,) | dtype = float64
  Dataset /intervals/fixed_gabors_presentations/tags (VectorData) user-defined tags | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (3000,) | dtype = uint16
  Dataset /intervals/fixed_gabors_presentations/timeseries (VectorData) index into a TimeSeries object | shape = (3000,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/fixed_gabors_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (3000,) | dtype = uint16
  Dataset /intervals/fixed_gabors_presentations/units (VectorData) Units of stimulus size | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/xys (VectorData) No description | shape = (3000,) | dtype = object
  Group /intervals/gratings_presentations (TimeIntervals) Presentation times and stimuli details for 'gratings' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/gratings_presentations/color (VectorData) No description | shape = (624,) | dtype = object
  Dataset /intervals/gratings_presentations/contrast (VectorData) Contrast of stimulus | shape = (624,) | dtype = float64
  Dataset /intervals/gratings_presentations/id (ElementIdentifiers)  | shape = (624,) | dtype = int64
  Dataset /intervals/gratings_presentations/mask (VectorData) Shape of mask applied to stimulus | shape = (624,) | dtype = object
  Dataset /intervals/gratings_presentations/opacity (VectorData) Opacity of stimulus | shape = (624,) | dtype = float64
  Dataset /intervals/gratings_presentations/orientation (VectorData) Orientation of stimulus | shape = (624,) | dtype = float64
  Dataset /intervals/gratings_presentations/phase (VectorData) Phase of grating stimulus | shape = (624,) | dtype = float64
  Dataset /intervals/gratings_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (624,) | dtype = object
  Dataset /intervals/gratings_presentations/spatial_frequency (VectorData) Spatial frequency of stimulus | shape = (624,) | dtype = float64
  Dataset /intervals/gratings_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (624,) | dtype = float64
  Dataset /intervals/gratings_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (624,) | dtype = float64
  Dataset /intervals/gratings_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (624,) | dtype = float64
  Dataset /intervals/gratings_presentations/stimulus_name (VectorData) Name of stimulus | shape = (624,) | dtype = object
  Dataset /intervals/gratings_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (624,) | dtype = float64
  Dataset /intervals/gratings_presentations/tags (VectorData) user-defined tags | shape = (624,) | dtype = object
  Dataset /intervals/gratings_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (624,) | dtype = uint16
  Dataset /intervals/gratings_presentations/timeseries (VectorData) index into a TimeSeries object | shape = (624,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/gratings_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (624,) | dtype = uint16
  Dataset /intervals/gratings_presentations/units (VectorData) Units of stimulus size | shape = (624,) | dtype = object
  Group /intervals/movie_flower_fwd_presentations (TimeIntervals) Presentation times and stimuli details for 'movie_flower_fwd' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/movie_flower_fwd_presentations/color (VectorData) No description | shape = (16200,) | dtype = object
  Dataset /intervals/movie_flower_fwd_presentations/contrast (VectorData) Contrast of stimulus | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_flower_fwd_presentations/frame (VectorData) Frame of movie stimulus | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_flower_fwd_presentations/id (ElementIdentifiers)  | shape = (16200,) | dtype = int64
  Dataset /intervals/movie_flower_fwd_presentations/opacity (VectorData) Opacity of stimulus | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_flower_fwd_presentations/orientation (VectorData) Orientation of stimulus | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_flower_fwd_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (16200,) | dtype = object
  Dataset /intervals/movie_flower_fwd_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_flower_fwd_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_flower_fwd_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_flower_fwd_presentations/stimulus_name (VectorData) Name of stimulus | shape = (16200,) | dtype = object
  Dataset /intervals/movie_flower_fwd_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_flower_fwd_presentations/tags (VectorData) user-defined tags | shape = (16200,) | dtype = object
  Dataset /intervals/movie_flower_fwd_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (16200,) | dtype = uint16
  Dataset /intervals/movie_flower_fwd_presentations/timeseries (VectorData) index into a TimeSeries object | shape = (16200,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/movie_flower_fwd_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (16200,) | dtype = uint16
  Dataset /intervals/movie_flower_fwd_presentations/units (VectorData) Units of stimulus size | shape = (16200,) | dtype = object
  Group /intervals/movie_touch_of_evil_fwd_presentations (TimeIntervals) Presentation times and stimuli details for 'movie_touch_of_evil_fwd' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/color (VectorData) No description | shape = (16200,) | dtype = object
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/contrast (VectorData) Contrast of stimulus | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/frame (VectorData) Frame of movie stimulus | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/id (ElementIdentifiers)  | shape = (16200,) | dtype = int64
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/opacity (VectorData) Opacity of stimulus | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/orientation (VectorData) Orientation of stimulus | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (16200,) | dtype = object
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/stimulus_name (VectorData) Name of stimulus | shape = (16200,) | dtype = object
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/tags (VectorData) user-defined tags | shape = (16200,) | dtype = object
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (16200,) | dtype = uint16
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/timeseries (VectorData) index into a TimeSeries object | shape = (16200,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (16200,) | dtype = uint16
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/units (VectorData) Units of stimulus size | shape = (16200,) | dtype = object
  Group /intervals/movie_worms_fwd_presentations (TimeIntervals) Presentation times and stimuli details for 'movie_worms_fwd' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/movie_worms_fwd_presentations/color (VectorData) No description | shape = (16200,) | dtype = object
  Dataset /intervals/movie_worms_fwd_presentations/contrast (VectorData) Contrast of stimulus | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_worms_fwd_presentations/frame (VectorData) Frame of movie stimulus | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_worms_fwd_presentations/id (ElementIdentifiers)  | shape = (16200,) | dtype = int64
  Dataset /intervals/movie_worms_fwd_presentations/opacity (VectorData) Opacity of stimulus | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_worms_fwd_presentations/orientation (VectorData) Orientation of stimulus | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_worms_fwd_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (16200,) | dtype = object
  Dataset /intervals/movie_worms_fwd_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_worms_fwd_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_worms_fwd_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_worms_fwd_presentations/stimulus_name (VectorData) Name of stimulus | shape = (16200,) | dtype = object
  Dataset /intervals/movie_worms_fwd_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_worms_fwd_presentations/tags (VectorData) user-defined tags | shape = (16200,) | dtype = object
  Dataset /intervals/movie_worms_fwd_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (16200,) | dtype = uint16
  Dataset /intervals/movie_worms_fwd_presentations/timeseries (VectorData) index into a TimeSeries object | shape = (16200,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/movie_worms_fwd_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (16200,) | dtype = uint16
  Dataset /intervals/movie_worms_fwd_presentations/units (VectorData) Units of stimulus size | shape = (16200,) | dtype = object
  Group /intervals/rotate_gabors_presentations (TimeIntervals) Presentation times and stimuli details for 'rotate_gabors' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/rotate_gabors_presentations/OriSurp (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/PosSizesAll (VectorData) No description | shape = (3000,) | dtype = float64
  Dataset /intervals/rotate_gabors_presentations/colors (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/contrs (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/depths (VectorData) No description | shape = (3000,) | dtype = float64
  Dataset /intervals/rotate_gabors_presentations/elementMask (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/elementTex (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/fieldDepth (VectorData) No description | shape = (3000,) | dtype = float64
  Dataset /intervals/rotate_gabors_presentations/fieldPos (VectorData) Position of moving dot field | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/fieldShape (VectorData) Shape of moving dot field | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/fieldSize (VectorData) Size of moving dot field | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/id (ElementIdentifiers)  | shape = (3000,) | dtype = int64
  Dataset /intervals/rotate_gabors_presentations/nElements (VectorData) No description | shape = (3000,) | dtype = float64
  Dataset /intervals/rotate_gabors_presentations/opacities (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/oris (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/phases (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/rgbs (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/sfs (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/sizes (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (3000,) | dtype = float64
  Dataset /intervals/rotate_gabors_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (3000,) | dtype = float64
  Dataset /intervals/rotate_gabors_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (3000,) | dtype = float64
  Dataset /intervals/rotate_gabors_presentations/stimulus_name (VectorData) Name of stimulus | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (3000,) | dtype = float64
  Dataset /intervals/rotate_gabors_presentations/tags (VectorData) user-defined tags | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (3000,) | dtype = uint16
  Dataset /intervals/rotate_gabors_presentations/timeseries (VectorData) index into a TimeSeries object | shape = (3000,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/rotate_gabors_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (3000,) | dtype = uint16
  Dataset /intervals/rotate_gabors_presentations/units (VectorData) Units of stimulus size | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/xys (VectorData) No description | shape = (3000,) | dtype = object
  Group /intervals/spontaneous_presentations (TimeIntervals) Presentation times and stimuli details for 'spontaneous' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/spontaneous_presentations/id (ElementIdentifiers)  | shape = (183,) | dtype = int64
  Dataset /intervals/spontaneous_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (183,) | dtype = float64
  Dataset /intervals/spontaneous_presentations/stimulus_name (VectorData) Name of stimulus | shape = (183,) | dtype = object
  Dataset /intervals/spontaneous_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (183,) | dtype = float64
  Dataset /intervals/spontaneous_presentations/tags (VectorData) user-defined tags | shape = (183,) | dtype = object
  Dataset /intervals/spontaneous_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (183,) | dtype = uint8
  Dataset /intervals/spontaneous_presentations/timeseries (VectorData) index into a TimeSeries object | shape = (183,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/spontaneous_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (183,) | dtype = uint8
  Group /processing/ophys (ProcessingModule) Ophys processing module
  Group /processing/ophys/corrected_fluorescence (Fluorescence) 
  Group /processing/ophys/corrected_fluorescence/traces (RoiResponseSeries) no description
  Dataset /processing/ophys/corrected_fluorescence/traces/rois (DynamicTableRegion) segmented cells labeled by cell_specimen_id | shape = (3,) | dtype = int64
  Group /processing/ophys/dff (DfOverF) 
  Group /processing/ophys/dff/traces (RoiResponseSeries) no description
  Dataset /processing/ophys/dff/traces/rois (DynamicTableRegion) segmented cells labeled by cell_specimen_id | shape = (3,) | dtype = int64
  Group /processing/ophys/event_detection (OphysEventDetection) no description
  Dataset /processing/ophys/event_detection/rois (DynamicTableRegion) Cells with detected events | shape = (3,) | dtype = int64
  Group /processing/ophys/image_segmentation (ImageSegmentation) 
  Group /processing/ophys/image_segmentation/cell_specimen_table (PlaneSegmentation) Segmented rois
  Dataset /processing/ophys/image_segmentation/cell_specimen_table/cell_specimen_id (VectorData) Unified id of segmented cell across experiments (after cell matching) | shape = (3,) | dtype = int64
  Dataset /processing/ophys/image_segmentation/cell_specimen_table/height (VectorData) Height of ROI in pixels | shape = (3,) | dtype = int64
  Dataset /processing/ophys/image_segmentation/cell_specimen_table/id (ElementIdentifiers)  | shape = (3,) | dtype = int64
  Dataset /processing/ophys/image_segmentation/cell_specimen_table/image_mask (VectorData) Image masks for each ROI | shape = (3, 512, 512) | dtype = bool
  Group /processing/ophys/image_segmentation/cell_specimen_table/imaging_plane (ImagingPlane) 
  Group /processing/ophys/image_segmentation/cell_specimen_table/imaging_plane/channel_1 (OpticalChannel) 
  Group /processing/ophys/image_segmentation/cell_specimen_table/imaging_plane/device (Device) Allen Brain Observatory - Mesoscope 2P Rig
  Dataset /processing/ophys/image_segmentation/cell_specimen_table/mask_image_plane (VectorData) Which image plane an ROI resides on. Overlapping ROIs are stored on different mask image planes. | shape = (3,) | dtype = int64
  Dataset /processing/ophys/image_segmentation/cell_specimen_table/max_correction_down (VectorData) Max motion correction in down direction in pixels | shape = (3,) | dtype = float64
  Dataset /processing/ophys/image_segmentation/cell_specimen_table/max_correction_left (VectorData) Max motion correction in left direction in pixels | shape = (3,) | dtype = float64
  Dataset /processing/ophys/image_segmentation/cell_specimen_table/max_correction_right (VectorData) Max motion correction in right direction in pixels | shape = (3,) | dtype = float64
  Dataset /processing/ophys/image_segmentation/cell_specimen_table/max_correction_up (VectorData) Max motion correction in up direction in pixels | shape = (3,) | dtype = float64
  Dataset /processing/ophys/image_segmentation/cell_specimen_table/valid_roi (VectorData) Indicates if cell classification found the ROI to be a cell or not | shape = (3,) | dtype = bool
  Dataset /processing/ophys/image_segmentation/cell_specimen_table/width (VectorData) Width of ROI in pixels | shape = (3,) | dtype = int64
  Dataset /processing/ophys/image_segmentation/cell_specimen_table/x (VectorData) x position of ROI in Image Plane in pixels (top left corner) | shape = (3,) | dtype = int64
  Dataset /processing/ophys/image_segmentation/cell_specimen_table/y (VectorData) y position of ROI in Image Plane in pixels (top left corner) | shape = (3,) | dtype = int64
  Group /processing/ophys/images (Images) no description
  Dataset /processing/ophys/images/average_image (GrayscaleImage) average_image image at pixels/cm resolution | shape = (512, 512) | dtype = uint8
  Dataset /processing/ophys/images/max_projection (GrayscaleImage) max_projection image at pixels/cm resolution | shape = (512, 512) | dtype = uint8
  Dataset /processing/ophys/images/segmentation_mask_image (GrayscaleImage) segmentation_mask_image image at pixels/cm resolution | shape = (512, 512) | dtype = int64
  Group /processing/ophys/neuropil_trace (Fluorescence) 
  Group /processing/ophys/neuropil_trace/traces (RoiResponseSeries) no description
  Dataset /processing/ophys/neuropil_trace/traces/rois (DynamicTableRegion) segmented cells labeled by cell_specimen_id | shape = (3,) | dtype = int64
  Group /processing/ophys/ophys_motion_correction_x (TimeSeries) no description
  Group /processing/ophys/ophys_motion_correction_y (TimeSeries) no description
  Group /processing/running (ProcessingModule) Running speed processing module
  Group /processing/running/dx (TimeSeries) Running wheel angular change, computed during data collection
  Group /processing/running/speed (TimeSeries) no description
  Group /processing/running/speed_unfiltered (TimeSeries) no description
  Group /processing/stimulus (ProcessingModule) Stimulus Times processing
  Group /processing/stimulus/timestamps (TimeSeries) no description
  Group /processing/stimulus_ophys (ProcessingModule) Stimulus Times processing
  Group /processing/stimulus_ophys/timestamps (TimeSeries) no description
  session_description: Ophys Session
  session_start_time: 2023-01-03T17:03:30.439000+00:00
  Group /stimulus/templates/flower_fwd (ImageSeries) no description
  Group /stimulus/templates/touch_of_evil_fwd (ImageSeries) no description
  Group /stimulus/templates/worms_fwd (ImageSeries) no description
  timestamps_reference_time: 2023-01-03T17:03:30.439000+00:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/EyeTracking (EllipseEyeTracking) 
  Group /acquisition/EyeTracking/corneal_reflection_tracking (EllipseSeries) no description
  Group /acquisition/EyeTracking/eye_tracking (EllipseSeries) no description
  Group /acquisition/EyeTracking/likely_blink (TimeSeries) blinks
  Group /acquisition/EyeTracking/pupil_tracking (EllipseSeries) no description
  Group /acquisition/raw_suite2p_motion_corrected (TwoPhotonSeries) no description
  Group /acquisition/raw_suite2p_motion_corrected/imaging_plane (ImagingPlane) 
  Group /acquisition/raw_suite2p_motion_corrected/imaging_plane/channel_1 (OpticalChannel) 
  Group /acquisition/raw_suite2p_motion_corrected/imaging_plane/device (Device) Allen Brain Observatory - Mesoscope 2P Rig
  Group /acquisition/v_in (TimeSeries) The theoretical maximum voltage that the running wheel encoder will reach prior to "wrapping". This should theoretically be 5V (after crossing 5V goes to 0V, or vice versa). In practice the encoder does not always reach this value before wrapping, which can cause transient spikes in speed at the voltage "wraps".
  Group /acquisition/v_sig (TimeSeries) Voltage signal from the running wheel encoder
  file_create_date: ['2024-01-21T18:31:22.932627+00:00']
  Group /general/devices/MESO.2 (Device) Allen Brain Observatory - Mesoscope 2P Rig
  experiment_description: ophys session
  institution: Allen Institute for Brain Science
  keywords: ['2-photon' 'calcium imaging' 'visual cortex' 'behavior' 'task']
  Group /general/metadata (OphysMetadata) 
  Group /general/optophysiology/imaging_plane_1 (ImagingPlane) 
  Group /general/optophysiology/imaging_plane_1/channel_1 (OpticalChannel) 
  Group /general/optophysiology/imaging_plane_1/device (Device) Allen Brain Observatory - Mesoscope 2P Rig
  Group /general/subject (Subject) 
  surgery:  Structure: VISp
  identifier: 1237345890
  Group /intervals/fixed_gabors_presentations (TimeIntervals) Presentation times and stimuli details for 'fixed_gabors' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/fixed_gabors_presentations/OriSurp (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/PosSizesAll (VectorData) No description | shape = (3000,) | dtype = float64
  Dataset /intervals/fixed_gabors_presentations/colors (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/contrs (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/depths (VectorData) No description | shape = (3000,) | dtype = float64
  Dataset /intervals/fixed_gabors_presentations/elementMask (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/elementTex (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/fieldDepth (VectorData) No description | shape = (3000,) | dtype = float64
  Dataset /intervals/fixed_gabors_presentations/fieldPos (VectorData) Position of moving dot field | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/fieldShape (VectorData) Shape of moving dot field | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/fieldSize (VectorData) Size of moving dot field | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/id (ElementIdentifiers)  | shape = (3000,) | dtype = int64
  Dataset /intervals/fixed_gabors_presentations/nElements (VectorData) No description | shape = (3000,) | dtype = float64
  Dataset /intervals/fixed_gabors_presentations/opacities (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/oris (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/phases (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/rgbs (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/sfs (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/sizes (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (3000,) | dtype = float64
  Dataset /intervals/fixed_gabors_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (3000,) | dtype = float64
  Dataset /intervals/fixed_gabors_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (3000,) | dtype = float64
  Dataset /intervals/fixed_gabors_presentations/stimulus_name (VectorData) Name of stimulus | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (3000,) | dtype = float64
  Dataset /intervals/fixed_gabors_presentations/tags (VectorData) user-defined tags | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (3000,) | dtype = uint16
  Dataset /intervals/fixed_gabors_presentations/timeseries (VectorData) index into a TimeSeries object | shape = (3000,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/fixed_gabors_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (3000,) | dtype = uint16
  Dataset /intervals/fixed_gabors_presentations/units (VectorData) Units of stimulus size | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/xys (VectorData) No description | shape = (3000,) | dtype = object
  Group /intervals/gratings_presentations (TimeIntervals) Presentation times and stimuli details for 'gratings' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/gratings_presentations/color (VectorData) No description | shape = (624,) | dtype = object
  Dataset /intervals/gratings_presentations/contrast (VectorData) Contrast of stimulus | shape = (624,) | dtype = float64
  Dataset /intervals/gratings_presentations/id (ElementIdentifiers)  | shape = (624,) | dtype = int64
  Dataset /intervals/gratings_presentations/mask (VectorData) Shape of mask applied to stimulus | shape = (624,) | dtype = object
  Dataset /intervals/gratings_presentations/opacity (VectorData) Opacity of stimulus | shape = (624,) | dtype = float64
  Dataset /intervals/gratings_presentations/orientation (VectorData) Orientation of stimulus | shape = (624,) | dtype = float64
  Dataset /intervals/gratings_presentations/phase (VectorData) Phase of grating stimulus | shape = (624,) | dtype = float64
  Dataset /intervals/gratings_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (624,) | dtype = object
  Dataset /intervals/gratings_presentations/spatial_frequency (VectorData) Spatial frequency of stimulus | shape = (624,) | dtype = float64
  Dataset /intervals/gratings_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (624,) | dtype = float64
  Dataset /intervals/gratings_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (624,) | dtype = float64
  Dataset /intervals/gratings_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (624,) | dtype = float64
  Dataset /intervals/gratings_presentations/stimulus_name (VectorData) Name of stimulus | shape = (624,) | dtype = object
  Dataset /intervals/gratings_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (624,) | dtype = float64
  Dataset /intervals/gratings_presentations/tags (VectorData) user-defined tags | shape = (624,) | dtype = object
  Dataset /intervals/gratings_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (624,) | dtype = uint16
  Dataset /intervals/gratings_presentations/timeseries (VectorData) index into a TimeSeries object | shape = (624,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/gratings_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (624,) | dtype = uint16
  Dataset /intervals/gratings_presentations/units (VectorData) Units of stimulus size | shape = (624,) | dtype = object
  Group /intervals/movie_flower_fwd_presentations (TimeIntervals) Presentation times and stimuli details for 'movie_flower_fwd' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/movie_flower_fwd_presentations/color (VectorData) No description | shape = (16200,) | dtype = object
  Dataset /intervals/movie_flower_fwd_presentations/contrast (VectorData) Contrast of stimulus | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_flower_fwd_presentations/frame (VectorData) Frame of movie stimulus | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_flower_fwd_presentations/id (ElementIdentifiers)  | shape = (16200,) | dtype = int64
  Dataset /intervals/movie_flower_fwd_presentations/opacity (VectorData) Opacity of stimulus | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_flower_fwd_presentations/orientation (VectorData) Orientation of stimulus | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_flower_fwd_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (16200,) | dtype = object
  Dataset /intervals/movie_flower_fwd_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_flower_fwd_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_flower_fwd_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_flower_fwd_presentations/stimulus_name (VectorData) Name of stimulus | shape = (16200,) | dtype = object
  Dataset /intervals/movie_flower_fwd_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_flower_fwd_presentations/tags (VectorData) user-defined tags | shape = (16200,) | dtype = object
  Dataset /intervals/movie_flower_fwd_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (16200,) | dtype = uint16
  Dataset /intervals/movie_flower_fwd_presentations/timeseries (VectorData) index into a TimeSeries object | shape = (16200,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/movie_flower_fwd_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (16200,) | dtype = uint16
  Dataset /intervals/movie_flower_fwd_presentations/units (VectorData) Units of stimulus size | shape = (16200,) | dtype = object
  Group /intervals/movie_touch_of_evil_fwd_presentations (TimeIntervals) Presentation times and stimuli details for 'movie_touch_of_evil_fwd' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/color (VectorData) No description | shape = (16200,) | dtype = object
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/contrast (VectorData) Contrast of stimulus | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/frame (VectorData) Frame of movie stimulus | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/id (ElementIdentifiers)  | shape = (16200,) | dtype = int64
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/opacity (VectorData) Opacity of stimulus | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/orientation (VectorData) Orientation of stimulus | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (16200,) | dtype = object
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/stimulus_name (VectorData) Name of stimulus | shape = (16200,) | dtype = object
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/tags (VectorData) user-defined tags | shape = (16200,) | dtype = object
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (16200,) | dtype = uint16
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/timeseries (VectorData) index into a TimeSeries object | shape = (16200,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (16200,) | dtype = uint16
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/units (VectorData) Units of stimulus size | shape = (16200,) | dtype = object
  Group /intervals/movie_worms_fwd_presentations (TimeIntervals) Presentation times and stimuli details for 'movie_worms_fwd' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/movie_worms_fwd_presentations/color (VectorData) No description | shape = (16200,) | dtype = object
  Dataset /intervals/movie_worms_fwd_presentations/contrast (VectorData) Contrast of stimulus | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_worms_fwd_presentations/frame (VectorData) Frame of movie stimulus | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_worms_fwd_presentations/id (ElementIdentifiers)  | shape = (16200,) | dtype = int64
  Dataset /intervals/movie_worms_fwd_presentations/opacity (VectorData) Opacity of stimulus | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_worms_fwd_presentations/orientation (VectorData) Orientation of stimulus | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_worms_fwd_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (16200,) | dtype = object
  Dataset /intervals/movie_worms_fwd_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_worms_fwd_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_worms_fwd_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_worms_fwd_presentations/stimulus_name (VectorData) Name of stimulus | shape = (16200,) | dtype = object
  Dataset /intervals/movie_worms_fwd_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_worms_fwd_presentations/tags (VectorData) user-defined tags | shape = (16200,) | dtype = object
  Dataset /intervals/movie_worms_fwd_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (16200,) | dtype = uint16
  Dataset /intervals/movie_worms_fwd_presentations/timeseries (VectorData) index into a TimeSeries object | shape = (16200,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/movie_worms_fwd_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (16200,) | dtype = uint16
  Dataset /intervals/movie_worms_fwd_presentations/units (VectorData) Units of stimulus size | shape = (16200,) | dtype = object
  Group /intervals/rotate_gabors_presentations (TimeIntervals) Presentation times and stimuli details for 'rotate_gabors' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/rotate_gabors_presentations/OriSurp (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/PosSizesAll (VectorData) No description | shape = (3000,) | dtype = float64
  Dataset /intervals/rotate_gabors_presentations/colors (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/contrs (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/depths (VectorData) No description | shape = (3000,) | dtype = float64
  Dataset /intervals/rotate_gabors_presentations/elementMask (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/elementTex (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/fieldDepth (VectorData) No description | shape = (3000,) | dtype = float64
  Dataset /intervals/rotate_gabors_presentations/fieldPos (VectorData) Position of moving dot field | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/fieldShape (VectorData) Shape of moving dot field | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/fieldSize (VectorData) Size of moving dot field | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/id (ElementIdentifiers)  | shape = (3000,) | dtype = int64
  Dataset /intervals/rotate_gabors_presentations/nElements (VectorData) No description | shape = (3000,) | dtype = float64
  Dataset /intervals/rotate_gabors_presentations/opacities (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/oris (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/phases (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/rgbs (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/sfs (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/sizes (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (3000,) | dtype = float64
  Dataset /intervals/rotate_gabors_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (3000,) | dtype = float64
  Dataset /intervals/rotate_gabors_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (3000,) | dtype = float64
  Dataset /intervals/rotate_gabors_presentations/stimulus_name (VectorData) Name of stimulus | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (3000,) | dtype = float64
  Dataset /intervals/rotate_gabors_presentations/tags (VectorData) user-defined tags | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (3000,) | dtype = uint16
  Dataset /intervals/rotate_gabors_presentations/timeseries (VectorData) index into a TimeSeries object | shape = (3000,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/rotate_gabors_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (3000,) | dtype = uint16
  Dataset /intervals/rotate_gabors_presentations/units (VectorData) Units of stimulus size | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/xys (VectorData) No description | shape = (3000,) | dtype = object
  Group /intervals/spontaneous_presentations (TimeIntervals) Presentation times and stimuli details for 'spontaneous' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/spontaneous_presentations/id (ElementIdentifiers)  | shape = (183,) | dtype = int64
  Dataset /intervals/spontaneous_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (183,) | dtype = float64
  Dataset /intervals/spontaneous_presentations/stimulus_name (VectorData) Name of stimulus | shape = (183,) | dtype = object
  Dataset /intervals/spontaneous_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (183,) | dtype = float64
  Dataset /intervals/spontaneous_presentations/tags (VectorData) user-defined tags | shape = (183,) | dtype = object
  Dataset /intervals/spontaneous_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (183,) | dtype = uint8
  Dataset /intervals/spontaneous_presentations/timeseries (VectorData) index into a TimeSeries object | shape = (183,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/spontaneous_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (183,) | dtype = uint8
  Group /processing/ophys (ProcessingModule) Ophys processing module
  Group /processing/ophys/corrected_fluorescence (Fluorescence) 
  Group /processing/ophys/corrected_fluorescence/traces (RoiResponseSeries) no description
  Dataset /processing/ophys/corrected_fluorescence/traces/rois (DynamicTableRegion) segmented cells labeled by cell_specimen_id | shape = (3,) | dtype = int64
  Group /processing/ophys/dff (DfOverF) 
  Group /processing/ophys/dff/traces (RoiResponseSeries) no description
  Dataset /processing/ophys/dff/traces/rois (DynamicTableRegion) segmented cells labeled by cell_specimen_id | shape = (3,) | dtype = int64
  Group /processing/ophys/event_detection (OphysEventDetection) no description
  Dataset /processing/ophys/event_detection/rois (DynamicTableRegion) Cells with detected events | shape = (3,) | dtype = int64
  Group /processing/ophys/image_segmentation (ImageSegmentation) 
  Group /processing/ophys/image_segmentation/cell_specimen_table (PlaneSegmentation) Segmented rois
  Dataset /processing/ophys/image_segmentation/cell_specimen_table/cell_specimen_id (VectorData) Unified id of segmented cell across experiments (after cell matching) | shape = (3,) | dtype = int64
  Dataset /processing/ophys/image_segmentation/cell_specimen_table/height (VectorData) Height of ROI in pixels | shape = (3,) | dtype = int64
  Dataset /processing/ophys/image_segmentation/cell_specimen_table/id (ElementIdentifiers)  | shape = (3,) | dtype = int64
  Dataset /processing/ophys/image_segmentation/cell_specimen_table/image_mask (VectorData) Image masks for each ROI | shape = (3, 512, 512) | dtype = bool
  Group /processing/ophys/image_segmentation/cell_specimen_table/imaging_plane (ImagingPlane) 
  Group /processing/ophys/image_segmentation/cell_specimen_table/imaging_plane/channel_1 (OpticalChannel) 
  Group /processing/ophys/image_segmentation/cell_specimen_table/imaging_plane/device (Device) Allen Brain Observatory - Mesoscope 2P Rig
  Dataset /processing/ophys/image_segmentation/cell_specimen_table/mask_image_plane (VectorData) Which image plane an ROI resides on. Overlapping ROIs are stored on different mask image planes. | shape = (3,) | dtype = int64
  Dataset /processing/ophys/image_segmentation/cell_specimen_table/max_correction_down (VectorData) Max motion correction in down direction in pixels | shape = (3,) | dtype = float64
  Dataset /processing/ophys/image_segmentation/cell_specimen_table/max_correction_left (VectorData) Max motion correction in left direction in pixels | shape = (3,) | dtype = float64
  Dataset /processing/ophys/image_segmentation/cell_specimen_table/max_correction_right (VectorData) Max motion correction in right direction in pixels | shape = (3,) | dtype = float64
  Dataset /processing/ophys/image_segmentation/cell_specimen_table/max_correction_up (VectorData) Max motion correction in up direction in pixels | shape = (3,) | dtype = float64
  Dataset /processing/ophys/image_segmentation/cell_specimen_table/valid_roi (VectorData) Indicates if cell classification found the ROI to be a cell or not | shape = (3,) | dtype = bool
  Dataset /processing/ophys/image_segmentation/cell_specimen_table/width (VectorData) Width of ROI in pixels | shape = (3,) | dtype = int64
  Dataset /processing/ophys/image_segmentation/cell_specimen_table/x (VectorData) x position of ROI in Image Plane in pixels (top left corner) | shape = (3,) | dtype = int64
  Dataset /processing/ophys/image_segmentation/cell_specimen_table/y (VectorData) y position of ROI in Image Plane in pixels (top left corner) | shape = (3,) | dtype = int64
  Group /processing/ophys/images (Images) no description
  Dataset /processing/ophys/images/average_image (GrayscaleImage) average_image image at pixels/cm resolution | shape = (512, 512) | dtype = uint8
  Dataset /processing/ophys/images/max_projection (GrayscaleImage) max_projection image at pixels/cm resolution | shape = (512, 512) | dtype = uint8
  Dataset /processing/ophys/images/segmentation_mask_image (GrayscaleImage) segmentation_mask_image image at pixels/cm resolution | shape = (512, 512) | dtype = int64
  Group /processing/ophys/neuropil_trace (Fluorescence) 
  Group /processing/ophys/neuropil_trace/traces (RoiResponseSeries) no description
  Dataset /processing/ophys/neuropil_trace/traces/rois (DynamicTableRegion) segmented cells labeled by cell_specimen_id | shape = (3,) | dtype = int64
  Group /processing/ophys/ophys_motion_correction_x (TimeSeries) no description
  Group /processing/ophys/ophys_motion_correction_y (TimeSeries) no description
  Group /processing/running (ProcessingModule) Running speed processing module
  Group /processing/running/dx (TimeSeries) Running wheel angular change, computed during data collection
  Group /processing/running/speed (TimeSeries) no description
  Group /processing/running/speed_unfiltered (TimeSeries) no description
  Group /processing/stimulus (ProcessingModule) Stimulus Times processing
  Group /processing/stimulus/timestamps (TimeSeries) no description
  Group /processing/stimulus_ophys (ProcessingModule) Stimulus Times processing
  Group /processing/stimulus_ophys/timestamps (TimeSeries) no description
  session_description: Ophys Session
  session_start_time: 2023-01-03T17:03:30.439000+00:00
  Group /stimulus/templates/flower_fwd (ImageSeries) no description
  Group /stimulus/templates/touch_of_evil_fwd (ImageSeries) no description
  Group /stimulus/templates/worms_fwd (ImageSeries) no description
  timestamps_reference_time: 2023-01-03T17:03:30.439000+00:00


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/EyeTracking (EllipseEyeTracking) 
  Group /acquisition/EyeTracking/corneal_reflection_tracking (EllipseSeries) no description
  Group /acquisition/EyeTracking/eye_tracking (EllipseSeries) no description
  Group /acquisition/EyeTracking/likely_blink (TimeSeries) blinks
  Group /acquisition/EyeTracking/pupil_tracking (EllipseSeries) no description
  Group /acquisition/v_in (TimeSeries) The theoretical maximum voltage that the running wheel encoder will reach prior to "wrapping". This should theoretically be 5V (after crossing 5V goes to 0V, or vice versa). In practice the encoder does not always reach this value before wrapping, which can cause transient spikes in speed at the voltage "wraps".
  Group /acquisition/v_sig (TimeSeries) Voltage signal from the running wheel encoder
  file_create_date: ['2024-01-21T19:09:06.120969+00:00']
  Group /general/devices/MESO.2 (Device) Allen Brain Observatory - Mesoscope 2P Rig
  experiment_description: ophys session
  institution: Allen Institute for Brain Science
  keywords: ['2-photon' 'calcium imaging' 'visual cortex' 'behavior' 'task']
  Group /general/metadata (OphysMetadata) 
  Group /general/optophysiology/imaging_plane_1 (ImagingPlane) 
  Group /general/optophysiology/imaging_plane_1/channel_1 (OpticalChannel) 
  Group /general/optophysiology/imaging_plane_1/device (Device) Allen Brain Observatory - Mesoscope 2P Rig
  Group /general/subject (Subject) 
  surgery:  Structure: VISp
  identifier: 1237345890
  Group /intervals/fixed_gabors_presentations (TimeIntervals) Presentation times and stimuli details for 'fixed_gabors' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/fixed_gabors_presentations/OriSurp (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/PosSizesAll (VectorData) No description | shape = (3000,) | dtype = float64
  Dataset /intervals/fixed_gabors_presentations/colors (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/contrs (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/depths (VectorData) No description | shape = (3000,) | dtype = float64
  Dataset /intervals/fixed_gabors_presentations/elementMask (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/elementTex (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/fieldDepth (VectorData) No description | shape = (3000,) | dtype = float64
  Dataset /intervals/fixed_gabors_presentations/fieldPos (VectorData) Position of moving dot field | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/fieldShape (VectorData) Shape of moving dot field | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/fieldSize (VectorData) Size of moving dot field | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/id (ElementIdentifiers)  | shape = (3000,) | dtype = int64
  Dataset /intervals/fixed_gabors_presentations/nElements (VectorData) No description | shape = (3000,) | dtype = float64
  Dataset /intervals/fixed_gabors_presentations/opacities (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/oris (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/phases (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/rgbs (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/sfs (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/sizes (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (3000,) | dtype = float64
  Dataset /intervals/fixed_gabors_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (3000,) | dtype = float64
  Dataset /intervals/fixed_gabors_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (3000,) | dtype = float64
  Dataset /intervals/fixed_gabors_presentations/stimulus_name (VectorData) Name of stimulus | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (3000,) | dtype = float64
  Dataset /intervals/fixed_gabors_presentations/tags (VectorData) user-defined tags | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (3000,) | dtype = uint16
  Dataset /intervals/fixed_gabors_presentations/timeseries (VectorData) index into a TimeSeries object | shape = (3000,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/fixed_gabors_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (3000,) | dtype = uint16
  Dataset /intervals/fixed_gabors_presentations/units (VectorData) Units of stimulus size | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/xys (VectorData) No description | shape = (3000,) | dtype = object
  Group /intervals/gratings_presentations (TimeIntervals) Presentation times and stimuli details for 'gratings' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/gratings_presentations/color (VectorData) No description | shape = (624,) | dtype = object
  Dataset /intervals/gratings_presentations/contrast (VectorData) Contrast of stimulus | shape = (624,) | dtype = float64
  Dataset /intervals/gratings_presentations/id (ElementIdentifiers)  | shape = (624,) | dtype = int64
  Dataset /intervals/gratings_presentations/mask (VectorData) Shape of mask applied to stimulus | shape = (624,) | dtype = object
  Dataset /intervals/gratings_presentations/opacity (VectorData) Opacity of stimulus | shape = (624,) | dtype = float64
  Dataset /intervals/gratings_presentations/orientation (VectorData) Orientation of stimulus | shape = (624,) | dtype = float64
  Dataset /intervals/gratings_presentations/phase (VectorData) Phase of grating stimulus | shape = (624,) | dtype = float64
  Dataset /intervals/gratings_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (624,) | dtype = object
  Dataset /intervals/gratings_presentations/spatial_frequency (VectorData) Spatial frequency of stimulus | shape = (624,) | dtype = float64
  Dataset /intervals/gratings_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (624,) | dtype = float64
  Dataset /intervals/gratings_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (624,) | dtype = float64
  Dataset /intervals/gratings_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (624,) | dtype = float64
  Dataset /intervals/gratings_presentations/stimulus_name (VectorData) Name of stimulus | shape = (624,) | dtype = object
  Dataset /intervals/gratings_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (624,) | dtype = float64
  Dataset /intervals/gratings_presentations/tags (VectorData) user-defined tags | shape = (624,) | dtype = object
  Dataset /intervals/gratings_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (624,) | dtype = uint16
  Dataset /intervals/gratings_presentations/timeseries (VectorData) index into a TimeSeries object | shape = (624,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/gratings_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (624,) | dtype = uint16
  Dataset /intervals/gratings_presentations/units (VectorData) Units of stimulus size | shape = (624,) | dtype = object
  Group /intervals/movie_flower_fwd_presentations (TimeIntervals) Presentation times and stimuli details for 'movie_flower_fwd' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/movie_flower_fwd_presentations/color (VectorData) No description | shape = (16200,) | dtype = object
  Dataset /intervals/movie_flower_fwd_presentations/contrast (VectorData) Contrast of stimulus | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_flower_fwd_presentations/frame (VectorData) Frame of movie stimulus | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_flower_fwd_presentations/id (ElementIdentifiers)  | shape = (16200,) | dtype = int64
  Dataset /intervals/movie_flower_fwd_presentations/opacity (VectorData) Opacity of stimulus | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_flower_fwd_presentations/orientation (VectorData) Orientation of stimulus | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_flower_fwd_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (16200,) | dtype = object
  Dataset /intervals/movie_flower_fwd_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_flower_fwd_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_flower_fwd_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_flower_fwd_presentations/stimulus_name (VectorData) Name of stimulus | shape = (16200,) | dtype = object
  Dataset /intervals/movie_flower_fwd_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_flower_fwd_presentations/tags (VectorData) user-defined tags | shape = (16200,) | dtype = object
  Dataset /intervals/movie_flower_fwd_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (16200,) | dtype = uint16
  Dataset /intervals/movie_flower_fwd_presentations/timeseries (VectorData) index into a TimeSeries object | shape = (16200,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/movie_flower_fwd_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (16200,) | dtype = uint16
  Dataset /intervals/movie_flower_fwd_presentations/units (VectorData) Units of stimulus size | shape = (16200,) | dtype = object
  Group /intervals/movie_touch_of_evil_fwd_presentations (TimeIntervals) Presentation times and stimuli details for 'movie_touch_of_evil_fwd' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/color (VectorData) No description | shape = (16200,) | dtype = object
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/contrast (VectorData) Contrast of stimulus | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/frame (VectorData) Frame of movie stimulus | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/id (ElementIdentifiers)  | shape = (16200,) | dtype = int64
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/opacity (VectorData) Opacity of stimulus | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/orientation (VectorData) Orientation of stimulus | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (16200,) | dtype = object
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/stimulus_name (VectorData) Name of stimulus | shape = (16200,) | dtype = object
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/tags (VectorData) user-defined tags | shape = (16200,) | dtype = object
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (16200,) | dtype = uint16
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/timeseries (VectorData) index into a TimeSeries object | shape = (16200,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (16200,) | dtype = uint16
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/units (VectorData) Units of stimulus size | shape = (16200,) | dtype = object
  Group /intervals/movie_worms_fwd_presentations (TimeIntervals) Presentation times and stimuli details for 'movie_worms_fwd' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/movie_worms_fwd_presentations/color (VectorData) No description | shape = (16200,) | dtype = object
  Dataset /intervals/movie_worms_fwd_presentations/contrast (VectorData) Contrast of stimulus | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_worms_fwd_presentations/frame (VectorData) Frame of movie stimulus | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_worms_fwd_presentations/id (ElementIdentifiers)  | shape = (16200,) | dtype = int64
  Dataset /intervals/movie_worms_fwd_presentations/opacity (VectorData) Opacity of stimulus | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_worms_fwd_presentations/orientation (VectorData) Orientation of stimulus | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_worms_fwd_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (16200,) | dtype = object
  Dataset /intervals/movie_worms_fwd_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_worms_fwd_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_worms_fwd_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_worms_fwd_presentations/stimulus_name (VectorData) Name of stimulus | shape = (16200,) | dtype = object
  Dataset /intervals/movie_worms_fwd_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_worms_fwd_presentations/tags (VectorData) user-defined tags | shape = (16200,) | dtype = object
  Dataset /intervals/movie_worms_fwd_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (16200,) | dtype = uint16
  Dataset /intervals/movie_worms_fwd_presentations/timeseries (VectorData) index into a TimeSeries object | shape = (16200,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/movie_worms_fwd_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (16200,) | dtype = uint16
  Dataset /intervals/movie_worms_fwd_presentations/units (VectorData) Units of stimulus size | shape = (16200,) | dtype = object
  Group /intervals/rotate_gabors_presentations (TimeIntervals) Presentation times and stimuli details for 'rotate_gabors' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/rotate_gabors_presentations/OriSurp (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/PosSizesAll (VectorData) No description | shape = (3000,) | dtype = float64
  Dataset /intervals/rotate_gabors_presentations/colors (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/contrs (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/depths (VectorData) No description | shape = (3000,) | dtype = float64
  Dataset /intervals/rotate_gabors_presentations/elementMask (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/elementTex (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/fieldDepth (VectorData) No description | shape = (3000,) | dtype = float64
  Dataset /intervals/rotate_gabors_presentations/fieldPos (VectorData) Position of moving dot field | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/fieldShape (VectorData) Shape of moving dot field | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/fieldSize (VectorData) Size of moving dot field | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/id (ElementIdentifiers)  | shape = (3000,) | dtype = int64
  Dataset /intervals/rotate_gabors_presentations/nElements (VectorData) No description | shape = (3000,) | dtype = float64
  Dataset /intervals/rotate_gabors_presentations/opacities (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/oris (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/phases (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/rgbs (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/sfs (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/sizes (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (3000,) | dtype = float64
  Dataset /intervals/rotate_gabors_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (3000,) | dtype = float64
  Dataset /intervals/rotate_gabors_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (3000,) | dtype = float64
  Dataset /intervals/rotate_gabors_presentations/stimulus_name (VectorData) Name of stimulus | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (3000,) | dtype = float64
  Dataset /intervals/rotate_gabors_presentations/tags (VectorData) user-defined tags | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (3000,) | dtype = uint16
  Dataset /intervals/rotate_gabors_presentations/timeseries (VectorData) index into a TimeSeries object | shape = (3000,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/rotate_gabors_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (3000,) | dtype = uint16
  Dataset /intervals/rotate_gabors_presentations/units (VectorData) Units of stimulus size | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/xys (VectorData) No description | shape = (3000,) | dtype = object
  Group /intervals/spontaneous_presentations (TimeIntervals) Presentation times and stimuli details for 'spontaneous' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/spontaneous_presentations/id (ElementIdentifiers)  | shape = (183,) | dtype = int64
  Dataset /intervals/spontaneous_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (183,) | dtype = float64
  Dataset /intervals/spontaneous_presentations/stimulus_name (VectorData) Name of stimulus | shape = (183,) | dtype = object
  Dataset /intervals/spontaneous_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (183,) | dtype = float64
  Dataset /intervals/spontaneous_presentations/tags (VectorData) user-defined tags | shape = (183,) | dtype = object
  Dataset /intervals/spontaneous_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (183,) | dtype = uint8
  Dataset /intervals/spontaneous_presentations/timeseries (VectorData) index into a TimeSeries object | shape = (183,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/spontaneous_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (183,) | dtype = uint8
  Group /processing/ophys (ProcessingModule) Ophys processing module
  Group /processing/ophys/corrected_fluorescence (Fluorescence) 
  Group /processing/ophys/corrected_fluorescence/traces (RoiResponseSeries) no description
  Dataset /processing/ophys/corrected_fluorescence/traces/rois (DynamicTableRegion) segmented cells labeled by cell_specimen_id | shape = (3,) | dtype = int64
  Group /processing/ophys/dff (DfOverF) 
  Group /processing/ophys/dff/traces (RoiResponseSeries) no description
  Dataset /processing/ophys/dff/traces/rois (DynamicTableRegion) segmented cells labeled by cell_specimen_id | shape = (3,) | dtype = int64
  Group /processing/ophys/event_detection (OphysEventDetection) no description
  Dataset /processing/ophys/event_detection/rois (DynamicTableRegion) Cells with detected events | shape = (3,) | dtype = int64
  Group /processing/ophys/image_segmentation (ImageSegmentation) 
  Group /processing/ophys/image_segmentation/cell_specimen_table (PlaneSegmentation) Segmented rois
  Dataset /processing/ophys/image_segmentation/cell_specimen_table/cell_specimen_id (VectorData) Unified id of segmented cell across experiments (after cell matching) | shape = (3,) | dtype = int64
  Dataset /processing/ophys/image_segmentation/cell_specimen_table/height (VectorData) Height of ROI in pixels | shape = (3,) | dtype = int64
  Dataset /processing/ophys/image_segmentation/cell_specimen_table/id (ElementIdentifiers)  | shape = (3,) | dtype = int64
  Dataset /processing/ophys/image_segmentation/cell_specimen_table/image_mask (VectorData) Image masks for each ROI | shape = (3, 512, 512) | dtype = bool
  Group /processing/ophys/image_segmentation/cell_specimen_table/imaging_plane (ImagingPlane) 
  Group /processing/ophys/image_segmentation/cell_specimen_table/imaging_plane/channel_1 (OpticalChannel) 
  Group /processing/ophys/image_segmentation/cell_specimen_table/imaging_plane/device (Device) Allen Brain Observatory - Mesoscope 2P Rig
  Dataset /processing/ophys/image_segmentation/cell_specimen_table/mask_image_plane (VectorData) Which image plane an ROI resides on. Overlapping ROIs are stored on different mask image planes. | shape = (3,) | dtype = int64
  Dataset /processing/ophys/image_segmentation/cell_specimen_table/max_correction_down (VectorData) Max motion correction in down direction in pixels | shape = (3,) | dtype = float64
  Dataset /processing/ophys/image_segmentation/cell_specimen_table/max_correction_left (VectorData) Max motion correction in left direction in pixels | shape = (3,) | dtype = float64
  Dataset /processing/ophys/image_segmentation/cell_specimen_table/max_correction_right (VectorData) Max motion correction in right direction in pixels | shape = (3,) | dtype = float64
  Dataset /processing/ophys/image_segmentation/cell_specimen_table/max_correction_up (VectorData) Max motion correction in up direction in pixels | shape = (3,) | dtype = float64
  Dataset /processing/ophys/image_segmentation/cell_specimen_table/valid_roi (VectorData) Indicates if cell classification found the ROI to be a cell or not | shape = (3,) | dtype = bool
  Dataset /processing/ophys/image_segmentation/cell_specimen_table/width (VectorData) Width of ROI in pixels | shape = (3,) | dtype = int64
  Dataset /processing/ophys/image_segmentation/cell_specimen_table/x (VectorData) x position of ROI in Image Plane in pixels (top left corner) | shape = (3,) | dtype = int64
  Dataset /processing/ophys/image_segmentation/cell_specimen_table/y (VectorData) y position of ROI in Image Plane in pixels (top left corner) | shape = (3,) | dtype = int64
  Group /processing/ophys/images (Images) no description
  Dataset /processing/ophys/images/average_image (GrayscaleImage) average_image image at pixels/cm resolution | shape = (512, 512) | dtype = uint8
  Dataset /processing/ophys/images/max_projection (GrayscaleImage) max_projection image at pixels/cm resolution | shape = (512, 512) | dtype = uint8
  Dataset /processing/ophys/images/segmentation_mask_image (GrayscaleImage) segmentation_mask_image image at pixels/cm resolution | shape = (512, 512) | dtype = int64
  Group /processing/ophys/neuropil_trace (Fluorescence) 
  Group /processing/ophys/neuropil_trace/traces (RoiResponseSeries) no description
  Dataset /processing/ophys/neuropil_trace/traces/rois (DynamicTableRegion) segmented cells labeled by cell_specimen_id | shape = (3,) | dtype = int64
  Group /processing/ophys/ophys_motion_correction_x (TimeSeries) no description
  Group /processing/ophys/ophys_motion_correction_y (TimeSeries) no description
  Group /processing/running (ProcessingModule) Running speed processing module
  Group /processing/running/dx (TimeSeries) Running wheel angular change, computed during data collection
  Group /processing/running/speed (TimeSeries) no description
  Group /processing/running/speed_unfiltered (TimeSeries) no description
  Group /processing/stimulus (ProcessingModule) Stimulus Times processing
  Group /processing/stimulus/timestamps (TimeSeries) no description
  Group /processing/stimulus_ophys (ProcessingModule) Stimulus Times processing
  Group /processing/stimulus_ophys/timestamps (TimeSeries) no description
  session_description: Ophys Session
  session_start_time: 2023-01-03T17:03:30.439000+00:00
  Group /stimulus/templates/flower_fwd (ImageSeries) no description
  Group /stimulus/templates/touch_of_evil_fwd (ImageSeries) no description
  Group /stimulus/templates/worms_fwd (ImageSeries) no description
  timestamps_reference_time: 2023-01-03T17:03:30.439000+00:00


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/EyeTracking (EllipseEyeTracking) 
  Group /acquisition/EyeTracking/corneal_reflection_tracking (EllipseSeries) no description
  Group /acquisition/EyeTracking/eye_tracking (EllipseSeries) no description
  Group /acquisition/EyeTracking/likely_blink (TimeSeries) blinks
  Group /acquisition/EyeTracking/pupil_tracking (EllipseSeries) no description
  Group /acquisition/denoised_suite2p_motion_corrected (TwoPhotonSeries) no description
  Group /acquisition/denoised_suite2p_motion_corrected/imaging_plane (ImagingPlane) 
  Group /acquisition/denoised_suite2p_motion_corrected/imaging_plane/channel_1 (OpticalChannel) 
  Group /acquisition/denoised_suite2p_motion_corrected/imaging_plane/device (Device) Allen Brain Observatory - Mesoscope 2P Rig
  Group /acquisition/raw_suite2p_motion_corrected (TwoPhotonSeries) no description
  Group /acquisition/raw_suite2p_motion_corrected/imaging_plane (ImagingPlane) 
  Group /acquisition/raw_suite2p_motion_corrected/imaging_plane/device (Device) Allen Brain Observatory - Mesoscope 2P Rig
  Group /acquisition/raw_suite2p_motion_corrected/imaging_plane/place_holder Channel (OpticalChannel) 
  Group /acquisition/v_in (TimeSeries) The theoretical maximum voltage that the running wheel encoder will reach prior to "wrapping". This should theoretically be 5V (after crossing 5V goes to 0V, or vice versa). In practice the encoder does not always reach this value before wrapping, which can cause transient spikes in speed at the voltage "wraps".
  Group /acquisition/v_sig (TimeSeries) Voltage signal from the running wheel encoder
  file_create_date: ['2024-01-21T18:31:19.852317+00:00']
  Group /general/devices/MESO.2 (Device) Allen Brain Observatory - Mesoscope 2P Rig
  experiment_description: ophys session
  institution: Allen Institute for Brain Science
  keywords: ['2-photon' 'calcium imaging' 'visual cortex' 'behavior' 'task']
  Group /general/metadata (OphysMetadata) 
  Group /general/optophysiology/imaging_plane (ImagingPlane) 
  Group /general/optophysiology/imaging_plane/device (Device) Allen Brain Observatory - Mesoscope 2P Rig
  Group /general/optophysiology/imaging_plane/place_holder Channel (OpticalChannel) 
  Group /general/optophysiology/imaging_plane_1 (ImagingPlane) 
  Group /general/optophysiology/imaging_plane_1/channel_1 (OpticalChannel) 
  Group /general/optophysiology/imaging_plane_1/device (Device) Allen Brain Observatory - Mesoscope 2P Rig
  Group /general/subject (Subject) 
  surgery:  Structure: VISam
  identifier: 1237345893
  Group /intervals/fixed_gabors_presentations (TimeIntervals) Presentation times and stimuli details for 'fixed_gabors' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/fixed_gabors_presentations/OriSurp (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/PosSizesAll (VectorData) No description | shape = (3000,) | dtype = float64
  Dataset /intervals/fixed_gabors_presentations/colors (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/contrs (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/depths (VectorData) No description | shape = (3000,) | dtype = float64
  Dataset /intervals/fixed_gabors_presentations/elementMask (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/elementTex (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/fieldDepth (VectorData) No description | shape = (3000,) | dtype = float64
  Dataset /intervals/fixed_gabors_presentations/fieldPos (VectorData) Position of moving dot field | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/fieldShape (VectorData) Shape of moving dot field | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/fieldSize (VectorData) Size of moving dot field | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/id (ElementIdentifiers)  | shape = (3000,) | dtype = int64
  Dataset /intervals/fixed_gabors_presentations/nElements (VectorData) No description | shape = (3000,) | dtype = float64
  Dataset /intervals/fixed_gabors_presentations/opacities (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/oris (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/phases (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/rgbs (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/sfs (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/sizes (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (3000,) | dtype = float64
  Dataset /intervals/fixed_gabors_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (3000,) | dtype = float64
  Dataset /intervals/fixed_gabors_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (3000,) | dtype = float64
  Dataset /intervals/fixed_gabors_presentations/stimulus_name (VectorData) Name of stimulus | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (3000,) | dtype = float64
  Dataset /intervals/fixed_gabors_presentations/tags (VectorData) user-defined tags | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (3000,) | dtype = uint16
  Dataset /intervals/fixed_gabors_presentations/timeseries (VectorData) index into a TimeSeries object | shape = (3000,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/fixed_gabors_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (3000,) | dtype = uint16
  Dataset /intervals/fixed_gabors_presentations/units (VectorData) Units of stimulus size | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/xys (VectorData) No description | shape = (3000,) | dtype = object
  Group /intervals/gratings_presentations (TimeIntervals) Presentation times and stimuli details for 'gratings' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/gratings_presentations/color (VectorData) No description | shape = (624,) | dtype = object
  Dataset /intervals/gratings_presentations/contrast (VectorData) Contrast of stimulus | shape = (624,) | dtype = float64
  Dataset /intervals/gratings_presentations/id (ElementIdentifiers)  | shape = (624,) | dtype = int64
  Dataset /intervals/gratings_presentations/mask (VectorData) Shape of mask applied to stimulus | shape = (624,) | dtype = object
  Dataset /intervals/gratings_presentations/opacity (VectorData) Opacity of stimulus | shape = (624,) | dtype = float64
  Dataset /intervals/gratings_presentations/orientation (VectorData) Orientation of stimulus | shape = (624,) | dtype = float64
  Dataset /intervals/gratings_presentations/phase (VectorData) Phase of grating stimulus | shape = (624,) | dtype = float64
  Dataset /intervals/gratings_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (624,) | dtype = object
  Dataset /intervals/gratings_presentations/spatial_frequency (VectorData) Spatial frequency of stimulus | shape = (624,) | dtype = float64
  Dataset /intervals/gratings_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (624,) | dtype = float64
  Dataset /intervals/gratings_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (624,) | dtype = float64
  Dataset /intervals/gratings_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (624,) | dtype = float64
  Dataset /intervals/gratings_presentations/stimulus_name (VectorData) Name of stimulus | shape = (624,) | dtype = object
  Dataset /intervals/gratings_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (624,) | dtype = float64
  Dataset /intervals/gratings_presentations/tags (VectorData) user-defined tags | shape = (624,) | dtype = object
  Dataset /intervals/gratings_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (624,) | dtype = uint16
  Dataset /intervals/gratings_presentations/timeseries (VectorData) index into a TimeSeries object | shape = (624,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/gratings_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (624,) | dtype = uint16
  Dataset /intervals/gratings_presentations/units (VectorData) Units of stimulus size | shape = (624,) | dtype = object
  Group /intervals/movie_flower_fwd_presentations (TimeIntervals) Presentation times and stimuli details for 'movie_flower_fwd' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/movie_flower_fwd_presentations/color (VectorData) No description | shape = (16200,) | dtype = object
  Dataset /intervals/movie_flower_fwd_presentations/contrast (VectorData) Contrast of stimulus | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_flower_fwd_presentations/frame (VectorData) Frame of movie stimulus | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_flower_fwd_presentations/id (ElementIdentifiers)  | shape = (16200,) | dtype = int64
  Dataset /intervals/movie_flower_fwd_presentations/opacity (VectorData) Opacity of stimulus | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_flower_fwd_presentations/orientation (VectorData) Orientation of stimulus | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_flower_fwd_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (16200,) | dtype = object
  Dataset /intervals/movie_flower_fwd_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_flower_fwd_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_flower_fwd_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_flower_fwd_presentations/stimulus_name (VectorData) Name of stimulus | shape = (16200,) | dtype = object
  Dataset /intervals/movie_flower_fwd_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_flower_fwd_presentations/tags (VectorData) user-defined tags | shape = (16200,) | dtype = object
  Dataset /intervals/movie_flower_fwd_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (16200,) | dtype = uint16
  Dataset /intervals/movie_flower_fwd_presentations/timeseries (VectorData) index into a TimeSeries object | shape = (16200,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/movie_flower_fwd_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (16200,) | dtype = uint16
  Dataset /intervals/movie_flower_fwd_presentations/units (VectorData) Units of stimulus size | shape = (16200,) | dtype = object
  Group /intervals/movie_touch_of_evil_fwd_presentations (TimeIntervals) Presentation times and stimuli details for 'movie_touch_of_evil_fwd' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/color (VectorData) No description | shape = (16200,) | dtype = object
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/contrast (VectorData) Contrast of stimulus | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/frame (VectorData) Frame of movie stimulus | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/id (ElementIdentifiers)  | shape = (16200,) | dtype = int64
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/opacity (VectorData) Opacity of stimulus | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/orientation (VectorData) Orientation of stimulus | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (16200,) | dtype = object
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/stimulus_name (VectorData) Name of stimulus | shape = (16200,) | dtype = object
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/tags (VectorData) user-defined tags | shape = (16200,) | dtype = object
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (16200,) | dtype = uint16
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/timeseries (VectorData) index into a TimeSeries object | shape = (16200,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (16200,) | dtype = uint16
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/units (VectorData) Units of stimulus size | shape = (16200,) | dtype = object
  Group /intervals/movie_worms_fwd_presentations (TimeIntervals) Presentation times and stimuli details for 'movie_worms_fwd' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/movie_worms_fwd_presentations/color (VectorData) No description | shape = (16200,) | dtype = object
  Dataset /intervals/movie_worms_fwd_presentations/contrast (VectorData) Contrast of stimulus | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_worms_fwd_presentations/frame (VectorData) Frame of movie stimulus | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_worms_fwd_presentations/id (ElementIdentifiers)  | shape = (16200,) | dtype = int64
  Dataset /intervals/movie_worms_fwd_presentations/opacity (VectorData) Opacity of stimulus | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_worms_fwd_presentations/orientation (VectorData) Orientation of stimulus | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_worms_fwd_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (16200,) | dtype = object
  Dataset /intervals/movie_worms_fwd_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_worms_fwd_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_worms_fwd_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_worms_fwd_presentations/stimulus_name (VectorData) Name of stimulus | shape = (16200,) | dtype = object
  Dataset /intervals/movie_worms_fwd_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_worms_fwd_presentations/tags (VectorData) user-defined tags | shape = (16200,) | dtype = object
  Dataset /intervals/movie_worms_fwd_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (16200,) | dtype = uint16
  Dataset /intervals/movie_worms_fwd_presentations/timeseries (VectorData) index into a TimeSeries object | shape = (16200,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/movie_worms_fwd_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (16200,) | dtype = uint16
  Dataset /intervals/movie_worms_fwd_presentations/units (VectorData) Units of stimulus size | shape = (16200,) | dtype = object
  Group /intervals/rotate_gabors_presentations (TimeIntervals) Presentation times and stimuli details for 'rotate_gabors' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/rotate_gabors_presentations/OriSurp (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/PosSizesAll (VectorData) No description | shape = (3000,) | dtype = float64
  Dataset /intervals/rotate_gabors_presentations/colors (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/contrs (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/depths (VectorData) No description | shape = (3000,) | dtype = float64
  Dataset /intervals/rotate_gabors_presentations/elementMask (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/elementTex (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/fieldDepth (VectorData) No description | shape = (3000,) | dtype = float64
  Dataset /intervals/rotate_gabors_presentations/fieldPos (VectorData) Position of moving dot field | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/fieldShape (VectorData) Shape of moving dot field | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/fieldSize (VectorData) Size of moving dot field | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/id (ElementIdentifiers)  | shape = (3000,) | dtype = int64
  Dataset /intervals/rotate_gabors_presentations/nElements (VectorData) No description | shape = (3000,) | dtype = float64
  Dataset /intervals/rotate_gabors_presentations/opacities (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/oris (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/phases (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/rgbs (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/sfs (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/sizes (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (3000,) | dtype = float64
  Dataset /intervals/rotate_gabors_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (3000,) | dtype = float64
  Dataset /intervals/rotate_gabors_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (3000,) | dtype = float64
  Dataset /intervals/rotate_gabors_presentations/stimulus_name (VectorData) Name of stimulus | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (3000,) | dtype = float64
  Dataset /intervals/rotate_gabors_presentations/tags (VectorData) user-defined tags | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (3000,) | dtype = uint16
  Dataset /intervals/rotate_gabors_presentations/timeseries (VectorData) index into a TimeSeries object | shape = (3000,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/rotate_gabors_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (3000,) | dtype = uint16
  Dataset /intervals/rotate_gabors_presentations/units (VectorData) Units of stimulus size | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/xys (VectorData) No description | shape = (3000,) | dtype = object
  Group /intervals/spontaneous_presentations (TimeIntervals) Presentation times and stimuli details for 'spontaneous' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/spontaneous_presentations/id (ElementIdentifiers)  | shape = (183,) | dtype = int64
  Dataset /intervals/spontaneous_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (183,) | dtype = float64
  Dataset /intervals/spontaneous_presentations/stimulus_name (VectorData) Name of stimulus | shape = (183,) | dtype = object
  Dataset /intervals/spontaneous_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (183,) | dtype = float64
  Dataset /intervals/spontaneous_presentations/tags (VectorData) user-defined tags | shape = (183,) | dtype = object
  Dataset /intervals/spontaneous_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (183,) | dtype = uint8
  Dataset /intervals/spontaneous_presentations/timeseries (VectorData) index into a TimeSeries object | shape = (183,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/spontaneous_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (183,) | dtype = uint8
  Group /processing/ophys (ProcessingModule) Ophys processing module
  Group /processing/ophys/images (Images) no description
  Dataset /processing/ophys/images/average_image (GrayscaleImage) average_image image at pixels/cm resolution | shape = (512, 512) | dtype = uint8
  Dataset /processing/ophys/images/max_projection (GrayscaleImage) max_projection image at pixels/cm resolution | shape = (512, 512) | dtype = uint8
  Group /processing/ophys/ophys_motion_correction_x (TimeSeries) no description
  Group /processing/ophys/ophys_motion_correction_y (TimeSeries) no description
  Group /processing/running (ProcessingModule) Running speed processing module
  Group /processing/running/dx (TimeSeries) Running wheel angular change, computed during data collection
  Group /processing/running/speed (TimeSeries) no description
  Group /processing/running/speed_unfiltered (TimeSeries) no description
  Group /processing/stimulus (ProcessingModule) Stimulus Times processing
  Group /processing/stimulus/timestamps (TimeSeries) no description
  Group /processing/stimulus_ophys (ProcessingModule) Stimulus Times processing
  Group /processing/stimulus_ophys/timestamps (TimeSeries) no description
  session_description: Ophys Session
  session_start_time: 2023-01-03T17:03:30.439000+00:00
  Group /stimulus/templates/flower_fwd (ImageSeries) no description
  Group /stimulus/templates/touch_of_evil_fwd (ImageSeries) no description
  Group /stimulus/templates/worms_fwd (ImageSeries) no description
  timestamps_reference_time: 2023-01-03T17:03:30.439000+00:00


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  Group /acquisition/EyeTracking (EllipseEyeTracking) 
  Group /acquisition/EyeTracking/corneal_reflection_tracking (EllipseSeries) no description
  Group /acquisition/EyeTracking/eye_tracking (EllipseSeries) no description
  Group /acquisition/EyeTracking/likely_blink (TimeSeries) blinks
  Group /acquisition/EyeTracking/pupil_tracking (EllipseSeries) no description
  Group /acquisition/raw_suite2p_motion_corrected (TwoPhotonSeries) no description
  Group /acquisition/raw_suite2p_motion_corrected/imaging_plane (ImagingPlane) 
  Group /acquisition/raw_suite2p_motion_corrected/imaging_plane/device (Device) Allen Brain Observatory - Mesoscope 2P Rig
  Group /acquisition/raw_suite2p_motion_corrected/imaging_plane/place_holder Channel (OpticalChannel) 
  Group /acquisition/v_in (TimeSeries) The theoretical maximum voltage that the running wheel encoder will reach prior to "wrapping". This should theoretically be 5V (after crossing 5V goes to 0V, or vice versa). In practice the encoder does not always reach this value before wrapping, which can cause transient spikes in speed at the voltage "wraps".
  Group /acquisition/v_sig (TimeSeries) Voltage signal from the running wheel encoder
  file_create_date: ['2024-01-21T18:31:19.852317+00:00']
  Group /general/devices/MESO.2 (Device) Allen Brain Observatory - Mesoscope 2P Rig
  experiment_description: ophys session
  institution: Allen Institute for Brain Science
  keywords: ['2-photon' 'calcium imaging' 'visual cortex' 'behavior' 'task']
  Group /general/metadata (OphysMetadata) 
  Group /general/optophysiology/imaging_plane (ImagingPlane) 
  Group /general/optophysiology/imaging_plane/device (Device) Allen Brain Observatory - Mesoscope 2P Rig
  Group /general/optophysiology/imaging_plane/place_holder Channel (OpticalChannel) 
  Group /general/optophysiology/imaging_plane_1 (ImagingPlane) 
  Group /general/optophysiology/imaging_plane_1/channel_1 (OpticalChannel) 
  Group /general/optophysiology/imaging_plane_1/device (Device) Allen Brain Observatory - Mesoscope 2P Rig
  Group /general/subject (Subject) 
  surgery:  Structure: VISam
  identifier: 1237345893
  Group /intervals/fixed_gabors_presentations (TimeIntervals) Presentation times and stimuli details for 'fixed_gabors' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/fixed_gabors_presentations/OriSurp (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/PosSizesAll (VectorData) No description | shape = (3000,) | dtype = float64
  Dataset /intervals/fixed_gabors_presentations/colors (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/contrs (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/depths (VectorData) No description | shape = (3000,) | dtype = float64
  Dataset /intervals/fixed_gabors_presentations/elementMask (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/elementTex (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/fieldDepth (VectorData) No description | shape = (3000,) | dtype = float64
  Dataset /intervals/fixed_gabors_presentations/fieldPos (VectorData) Position of moving dot field | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/fieldShape (VectorData) Shape of moving dot field | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/fieldSize (VectorData) Size of moving dot field | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/id (ElementIdentifiers)  | shape = (3000,) | dtype = int64
  Dataset /intervals/fixed_gabors_presentations/nElements (VectorData) No description | shape = (3000,) | dtype = float64
  Dataset /intervals/fixed_gabors_presentations/opacities (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/oris (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/phases (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/rgbs (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/sfs (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/sizes (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (3000,) | dtype = float64
  Dataset /intervals/fixed_gabors_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (3000,) | dtype = float64
  Dataset /intervals/fixed_gabors_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (3000,) | dtype = float64
  Dataset /intervals/fixed_gabors_presentations/stimulus_name (VectorData) Name of stimulus | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (3000,) | dtype = float64
  Dataset /intervals/fixed_gabors_presentations/tags (VectorData) user-defined tags | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (3000,) | dtype = uint16
  Dataset /intervals/fixed_gabors_presentations/timeseries (VectorData) index into a TimeSeries object | shape = (3000,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/fixed_gabors_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (3000,) | dtype = uint16
  Dataset /intervals/fixed_gabors_presentations/units (VectorData) Units of stimulus size | shape = (3000,) | dtype = object
  Dataset /intervals/fixed_gabors_presentations/xys (VectorData) No description | shape = (3000,) | dtype = object
  Group /intervals/gratings_presentations (TimeIntervals) Presentation times and stimuli details for 'gratings' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/gratings_presentations/color (VectorData) No description | shape = (624,) | dtype = object
  Dataset /intervals/gratings_presentations/contrast (VectorData) Contrast of stimulus | shape = (624,) | dtype = float64
  Dataset /intervals/gratings_presentations/id (ElementIdentifiers)  | shape = (624,) | dtype = int64
  Dataset /intervals/gratings_presentations/mask (VectorData) Shape of mask applied to stimulus | shape = (624,) | dtype = object
  Dataset /intervals/gratings_presentations/opacity (VectorData) Opacity of stimulus | shape = (624,) | dtype = float64
  Dataset /intervals/gratings_presentations/orientation (VectorData) Orientation of stimulus | shape = (624,) | dtype = float64
  Dataset /intervals/gratings_presentations/phase (VectorData) Phase of grating stimulus | shape = (624,) | dtype = float64
  Dataset /intervals/gratings_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (624,) | dtype = object
  Dataset /intervals/gratings_presentations/spatial_frequency (VectorData) Spatial frequency of stimulus | shape = (624,) | dtype = float64
  Dataset /intervals/gratings_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (624,) | dtype = float64
  Dataset /intervals/gratings_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (624,) | dtype = float64
  Dataset /intervals/gratings_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (624,) | dtype = float64
  Dataset /intervals/gratings_presentations/stimulus_name (VectorData) Name of stimulus | shape = (624,) | dtype = object
  Dataset /intervals/gratings_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (624,) | dtype = float64
  Dataset /intervals/gratings_presentations/tags (VectorData) user-defined tags | shape = (624,) | dtype = object
  Dataset /intervals/gratings_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (624,) | dtype = uint16
  Dataset /intervals/gratings_presentations/timeseries (VectorData) index into a TimeSeries object | shape = (624,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/gratings_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (624,) | dtype = uint16
  Dataset /intervals/gratings_presentations/units (VectorData) Units of stimulus size | shape = (624,) | dtype = object
  Group /intervals/movie_flower_fwd_presentations (TimeIntervals) Presentation times and stimuli details for 'movie_flower_fwd' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/movie_flower_fwd_presentations/color (VectorData) No description | shape = (16200,) | dtype = object
  Dataset /intervals/movie_flower_fwd_presentations/contrast (VectorData) Contrast of stimulus | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_flower_fwd_presentations/frame (VectorData) Frame of movie stimulus | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_flower_fwd_presentations/id (ElementIdentifiers)  | shape = (16200,) | dtype = int64
  Dataset /intervals/movie_flower_fwd_presentations/opacity (VectorData) Opacity of stimulus | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_flower_fwd_presentations/orientation (VectorData) Orientation of stimulus | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_flower_fwd_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (16200,) | dtype = object
  Dataset /intervals/movie_flower_fwd_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_flower_fwd_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_flower_fwd_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_flower_fwd_presentations/stimulus_name (VectorData) Name of stimulus | shape = (16200,) | dtype = object
  Dataset /intervals/movie_flower_fwd_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_flower_fwd_presentations/tags (VectorData) user-defined tags | shape = (16200,) | dtype = object
  Dataset /intervals/movie_flower_fwd_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (16200,) | dtype = uint16
  Dataset /intervals/movie_flower_fwd_presentations/timeseries (VectorData) index into a TimeSeries object | shape = (16200,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/movie_flower_fwd_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (16200,) | dtype = uint16
  Dataset /intervals/movie_flower_fwd_presentations/units (VectorData) Units of stimulus size | shape = (16200,) | dtype = object
  Group /intervals/movie_touch_of_evil_fwd_presentations (TimeIntervals) Presentation times and stimuli details for 'movie_touch_of_evil_fwd' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/color (VectorData) No description | shape = (16200,) | dtype = object
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/contrast (VectorData) Contrast of stimulus | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/frame (VectorData) Frame of movie stimulus | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/id (ElementIdentifiers)  | shape = (16200,) | dtype = int64
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/opacity (VectorData) Opacity of stimulus | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/orientation (VectorData) Orientation of stimulus | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (16200,) | dtype = object
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/stimulus_name (VectorData) Name of stimulus | shape = (16200,) | dtype = object
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/tags (VectorData) user-defined tags | shape = (16200,) | dtype = object
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (16200,) | dtype = uint16
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/timeseries (VectorData) index into a TimeSeries object | shape = (16200,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (16200,) | dtype = uint16
  Dataset /intervals/movie_touch_of_evil_fwd_presentations/units (VectorData) Units of stimulus size | shape = (16200,) | dtype = object
  Group /intervals/movie_worms_fwd_presentations (TimeIntervals) Presentation times and stimuli details for 'movie_worms_fwd' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/movie_worms_fwd_presentations/color (VectorData) No description | shape = (16200,) | dtype = object
  Dataset /intervals/movie_worms_fwd_presentations/contrast (VectorData) Contrast of stimulus | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_worms_fwd_presentations/frame (VectorData) Frame of movie stimulus | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_worms_fwd_presentations/id (ElementIdentifiers)  | shape = (16200,) | dtype = int64
  Dataset /intervals/movie_worms_fwd_presentations/opacity (VectorData) Opacity of stimulus | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_worms_fwd_presentations/orientation (VectorData) Orientation of stimulus | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_worms_fwd_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (16200,) | dtype = object
  Dataset /intervals/movie_worms_fwd_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_worms_fwd_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_worms_fwd_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_worms_fwd_presentations/stimulus_name (VectorData) Name of stimulus | shape = (16200,) | dtype = object
  Dataset /intervals/movie_worms_fwd_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (16200,) | dtype = float64
  Dataset /intervals/movie_worms_fwd_presentations/tags (VectorData) user-defined tags | shape = (16200,) | dtype = object
  Dataset /intervals/movie_worms_fwd_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (16200,) | dtype = uint16
  Dataset /intervals/movie_worms_fwd_presentations/timeseries (VectorData) index into a TimeSeries object | shape = (16200,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/movie_worms_fwd_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (16200,) | dtype = uint16
  Dataset /intervals/movie_worms_fwd_presentations/units (VectorData) Units of stimulus size | shape = (16200,) | dtype = object
  Group /intervals/rotate_gabors_presentations (TimeIntervals) Presentation times and stimuli details for 'rotate_gabors' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/rotate_gabors_presentations/OriSurp (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/PosSizesAll (VectorData) No description | shape = (3000,) | dtype = float64
  Dataset /intervals/rotate_gabors_presentations/colors (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/contrs (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/depths (VectorData) No description | shape = (3000,) | dtype = float64
  Dataset /intervals/rotate_gabors_presentations/elementMask (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/elementTex (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/fieldDepth (VectorData) No description | shape = (3000,) | dtype = float64
  Dataset /intervals/rotate_gabors_presentations/fieldPos (VectorData) Position of moving dot field | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/fieldShape (VectorData) Shape of moving dot field | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/fieldSize (VectorData) Size of moving dot field | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/id (ElementIdentifiers)  | shape = (3000,) | dtype = int64
  Dataset /intervals/rotate_gabors_presentations/nElements (VectorData) No description | shape = (3000,) | dtype = float64
  Dataset /intervals/rotate_gabors_presentations/opacities (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/oris (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/phases (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/rgbs (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/sfs (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/sizes (VectorData) No description | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (3000,) | dtype = float64
  Dataset /intervals/rotate_gabors_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (3000,) | dtype = float64
  Dataset /intervals/rotate_gabors_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (3000,) | dtype = float64
  Dataset /intervals/rotate_gabors_presentations/stimulus_name (VectorData) Name of stimulus | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (3000,) | dtype = float64
  Dataset /intervals/rotate_gabors_presentations/tags (VectorData) user-defined tags | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (3000,) | dtype = uint16
  Dataset /intervals/rotate_gabors_presentations/timeseries (VectorData) index into a TimeSeries object | shape = (3000,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/rotate_gabors_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (3000,) | dtype = uint16
  Dataset /intervals/rotate_gabors_presentations/units (VectorData) Units of stimulus size | shape = (3000,) | dtype = object
  Dataset /intervals/rotate_gabors_presentations/xys (VectorData) No description | shape = (3000,) | dtype = object
  Group /intervals/spontaneous_presentations (TimeIntervals) Presentation times and stimuli details for 'spontaneous' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/spontaneous_presentations/id (ElementIdentifiers)  | shape = (183,) | dtype = int64
  Dataset /intervals/spontaneous_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (183,) | dtype = float64
  Dataset /intervals/spontaneous_presentations/stimulus_name (VectorData) Name of stimulus | shape = (183,) | dtype = object
  Dataset /intervals/spontaneous_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (183,) | dtype = float64
  Dataset /intervals/spontaneous_presentations/tags (VectorData) user-defined tags | shape = (183,) | dtype = object
  Dataset /intervals/spontaneous_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (183,) | dtype = uint8
  Dataset /intervals/spontaneous_presentations/timeseries (VectorData) index into a TimeSeries object | shape = (183,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/spontaneous_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (183,) | dtype = uint8
  Group /processing/ophys (ProcessingModule) Ophys processing module
  Group /processing/ophys/images (Images) no description
  Dataset /processing/ophys/images/average_image (GrayscaleImage) average_image image at pixels/cm resolution | shape = (512, 512) | dtype = uint8
  Dataset /processing/ophys/images/max_projection (GrayscaleImage) max_projection image at pixels/cm resolution | shape = (512, 512) | dtype = uint8
  Group /processing/ophys/ophys_motion_correction_x (TimeSeries) no description
  Group /processing/ophys/ophys_motion_correction_y (TimeSeries) no description
  Group /processing/running (ProcessingModule) Running speed processing module
  Group /processing/running/dx (TimeSeries) Running wheel angular change, computed during data collection
  Group /processing/running/speed (TimeSeries) no description
  Group /processing/running/speed_unfiltered (TimeSeries) no description
  Group /processing/stimulus (ProcessingModule) Stimulus Times processing
  Group /processing/stimulus/timestamps (TimeSeries) no description
  Group /processing/stimulus_ophys (ProcessingModule) Stimulus Times processing
  Group /processing/stimulus_ophys/timestamps (TimeSeries) no description
  session_description: Ophys Session
  session_start_time: 2023-01-03T17:03:30.439000+00:00
  Group /stimulus/templates/flower_fwd (ImageSeries) no description
  Group /stimulus/templates/touch_of_evil_fwd (ImageSeries) no description
  Group /stimulus/templates/worms_fwd (ImageSeries) no description
  timestamps_reference_time: 2023-01-03T17:03:30.439000+00:00
