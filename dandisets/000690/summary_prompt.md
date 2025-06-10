
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000690/0.250326.0015
name: Allen Institute Openscope - Vision2Hippocampus project
contributor: [{'name': 'National Institutes of Health (NIH)', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': '1 U24 NS 113646-03'}, {'name': 'Allen Institute', 'schemaKey': 'Organization', 'identifier': 'https://ror.org/03cpe7c52', 'includeInCitation': False}, {'name': 'Mehta, Mayank R', 'email': 'mayankmehta@ucla.edu', 'roleName': ['dcite:Conceptualization', 'dcite:ContactPerson', 'dcite:FormalAnalysis', 'dcite:Investigation', 'dcite:ProjectManager', 'dcite:ProjectLeader', 'dcite:Researcher'], 'schemaKey': 'Person', 'identifier': '0000-0003-2005-2468', 'includeInCitation': True}, {'name': 'Purandare, Chinmay', 'email': 'chinmay.purandare@gmail.com', 'roleName': ['dcite:Conceptualization', 'dcite:FormalAnalysis', 'dcite:Investigation', 'dcite:ProjectMember', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0001-9225-0186', 'includeInCitation': True}, {'name': 'Jha, Siddharth', 'roleName': ['dcite:FormalAnalysis', 'dcite:Investigation', 'dcite:Researcher'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Lecoq, Jérôme', 'email': 'jeromel@alleninstitute.org', 'roleName': ['dcite:ContactPerson', 'dcite:FundingAcquisition', 'dcite:ProjectLeader', 'dcite:ProjectManager', 'dcite:ProjectAdministration', 'dcite:Software', 'dcite:Supervision'], 'schemaKey': 'Person', 'identifier': '0000-0002-0131-0938', 'includeInCitation': True}, {'name': 'Durand, Séverine', 'roleName': ['dcite:DataManager', 'dcite:FormalAnalysis', 'dcite:Supervision', 'dcite:DataCurator'], 'schemaKey': 'Person', 'identifier': '0000-0001-7788-0200', 'includeInCitation': True}, {'name': 'Gillis, Ryan', 'roleName': ['dcite:DataCollector'], 'schemaKey': 'Person', 'identifier': '0009-0000-1879-6519', 'includeInCitation': True}, {'name': 'Belski, Hannah', 'roleName': ['dcite:DataCollector'], 'schemaKey': 'Person', 'identifier': '0009-0001-5422-5964', 'includeInCitation': True}, {'name': 'Bawany, Ahad', 'roleName': ['dcite:DataCurator', 'dcite:DataManager'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Carlson, Mikayla', 'roleName': ['dcite:DataCollector'], 'schemaKey': 'Person', 'identifier': '0009-0003-7019-2781', 'includeInCitation': True}, {'name': 'Peene, Carter', 'roleName': ['dcite:DataCurator', 'dcite:DataManager'], 'schemaKey': 'Person', 'identifier': '0009-0000-6660-2264', 'includeInCitation': True}, {'name': 'Wilkes, Josh', 'roleName': ['dcite:DataCollector'], 'schemaKey': 'Person', 'identifier': '0009-0005-4858-2219', 'includeInCitation': True}, {'name': 'Johnson, Tye', 'roleName': ['dcite:DataCollector'], 'schemaKey': 'Person', 'identifier': '0009-0006-7239-7571', 'includeInCitation': True}, {'name': 'Naidoo, Robyn', 'roleName': ['dcite:DataCollector'], 'schemaKey': 'Person', 'identifier': '0009-0004-0996-8808', 'includeInCitation': True}, {'name': 'Suarez, Lucas', 'roleName': ['dcite:DataCollector'], 'schemaKey': 'Person', 'identifier': '0009-0002-0121-3334', 'includeInCitation': True}, {'name': 'Han, Warren', 'roleName': ['dcite:DataCollector'], 'schemaKey': 'Person', 'identifier': '0009-0006-0104-0380', 'includeInCitation': True}, {'name': 'Amaya, Avalon', 'roleName': ['dcite:DataCollector'], 'schemaKey': 'Person', 'identifier': '0000-0003-2274-2892', 'includeInCitation': True}, {'name': 'Nguyen, Katrina', 'roleName': ['dcite:DataCollector'], 'schemaKey': 'Person', 'identifier': '0009-0009-8547-9703', 'includeInCitation': True}, {'name': 'Ouellette, Ben', 'roleName': ['dcite:DataCollector'], 'schemaKey': 'Person', 'identifier': '0000-0003-4913-554X', 'includeInCitation': True}, {'name': 'Swapp, Jackie', 'roleName': ['dcite:Supervision'], 'schemaKey': 'Person', 'identifier': '0009-0008-4965-6242', 'includeInCitation': True}, {'name': 'Williford, Ali', 'roleName': ['dcite:Supervision'], 'schemaKey': 'Person', 'identifier': '0009-0000-7282-7515', 'includeInCitation': True}]
description: Extensive research shows that visual cortical neurons respond to specific stimuli, e.g. the primary visual cortical neurons respond to bars of light with specific orientation. In contrast, the hippocampal neurons are thought to encode not specific stimuli but instead represent abstract concepts such as space, time and events. How is this abstraction computed in the mouse brain? Specifically, how does the representation of simple visual stimuli evolve from the thalamus, which is a synapse away from the retina, through primary visual cortex, higher order visual areas and all the way to hippocampus, that is farthest removed from the retina?

The current OpenScope project aims to understand how the neural representations of simple and natural stimuli evolve from the LGN through V1, and most hippocampal regions, as well as some of the frontal areas. 

Stimuli presented
Two main categories of visual stimuli were presented–
1.	Simple visual motion, elicited by basic stimuli, like bars of light.
2.	Complex, potentially ethologically valid visual stimuli, elicited by movies involving eagles (and squirrels).
To parametrize the stimulus properties which might be affecting neural responses, mice were shown variants of the vertical bar of light as follows:
A(o) – The bar of light was white, moving on a black background, 15 degrees wide, and moved at a fixed speed, covered the entire width of the screen in 2 seconds. It covered both movement directions consecutively (naso-temporal, then temporo-nasal).
A(i) – Similar to A(o), but the bar was now thrice as wide (45o)
A(ii) – Similar to A(o), but the bar was thrice as slow (covering the width of the screen in 6 seconds).
A(iii) – Similar to A(o), but the contrast was flipped, i.e. a black bar of light on a white background.
A(iv) - Similar to A(o), but instead of a simple white bar, the stimulus was striped, and each stripe changed color as the stimulus moved through the width of the screen. This was called “disco” bar of light
A(v) – In a subset of mice, A(o) was appended by frames corresponding to the bar of light “vanishing” at either of the edges. Two vanishing protocols were attempted, the bar of light is fully absorbed by the boundary, before reemerging. Another protocol had the bar of light vanish for ~1 second in addition to smoothly being absorbed by the boundary, before reemerging.
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 600243449691, 'numberOfFiles': 156, 'numberOfSubjects': 25, 'variableMeasured': ['ElectricalSeries', 'LFP', 'ProcessingModule', 'Units'], 'measurementTechnique': [{'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'signal filtering technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000690 has 34 NWB files.
1 of these NWB files are of type 1.
1 of these NWB files are of type 2.
16 of these NWB files are of type 3.
15 of these NWB files are of type 4.
1 of these NWB files are of type 5.


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
  file_create_date: ['2025-02-25T16:36:10.235851-08:00']
  Group /general/devices/probeA (EcephysProbe) Neuropixels 1.0 Probe
  Group /general/devices/probeB (EcephysProbe) Neuropixels 1.0 Probe
  Group /general/devices/probeE (EcephysProbe) Neuropixels 1.0 Probe
  Group /general/devices/probeF (EcephysProbe) Neuropixels 1.0 Probe
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering, including the filter name and frequency cutoffs | shape = (1536,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (1536,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (1536,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (1536,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the electrode, in ohms | shape = (1536,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/local_index (VectorData) The local index of electrode/channel on device | shape = (1536,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (1536,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/probe_horizontal_position (VectorData) Width-wise position of electrode/channel on device (microns) | shape = (1536,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/probe_id (VectorData) The unique id of this electrode's/channel's device | shape = (1536,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/probe_vertical_position (VectorData) Length-wise position of electrode/channel on device (microns) | shape = (1536,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/valid_data (VectorData) Whether data from this electrode/channel is usable | shape = (1536,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the position (+x is posterior) | shape = (1536,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the position (+y is inferior) | shape = (1536,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the position (+z is right) | shape = (1536,) | dtype = float64
  Group /general/extracellular_ephys/probeA (EcephysElectrodeGroup) Ecephys Electrode Group
  Group /general/extracellular_ephys/probeA/device (EcephysProbe) Neuropixels 1.0 Probe
  Group /general/extracellular_ephys/probeB (EcephysElectrodeGroup) Ecephys Electrode Group
  Group /general/extracellular_ephys/probeB/device (EcephysProbe) Neuropixels 1.0 Probe
  Group /general/extracellular_ephys/probeE (EcephysElectrodeGroup) Ecephys Electrode Group
  Group /general/extracellular_ephys/probeE/device (EcephysProbe) Neuropixels 1.0 Probe
  Group /general/extracellular_ephys/probeF (EcephysElectrodeGroup) Ecephys Electrode Group
  Group /general/extracellular_ephys/probeF/device (EcephysProbe) Neuropixels 1.0 Probe
  institution: Allen Institute
  session_id: 1298465622
  stimulus: OpenScopeVision2Hippocampus
  Group /general/subject (EcephysSpecimen) 
  identifier: 1298465622
  Group /intervals/Disco2SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations (TimeIntervals) Presentation times and stimuli details for 'Disco2SAC_Wd15_Vel2_Bndry1_Cntst0_loop' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/Disco2SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/color (VectorData) No description | shape = (28800,) | dtype = object
  Dataset /intervals/Disco2SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/contrast (VectorData) Contrast of stimulus | shape = (28800,) | dtype = float64
  Dataset /intervals/Disco2SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/frame (VectorData) Frame of movie stimulus | shape = (28800,) | dtype = float64
  Dataset /intervals/Disco2SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/id (ElementIdentifiers)  | shape = (28800,) | dtype = int64
  Dataset /intervals/Disco2SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/opacity (VectorData) Opacity of stimulus | shape = (28800,) | dtype = float64
  Dataset /intervals/Disco2SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/orientation (VectorData) Orientation of stimulus | shape = (28800,) | dtype = float64
  Dataset /intervals/Disco2SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (28800,) | dtype = object
  Dataset /intervals/Disco2SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (28800,) | dtype = float64
  Dataset /intervals/Disco2SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (28800,) | dtype = float64
  Dataset /intervals/Disco2SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (28800,) | dtype = float64
  Dataset /intervals/Disco2SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/stimulus_name (VectorData) Name of stimulus | shape = (28800,) | dtype = object
  Dataset /intervals/Disco2SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (28800,) | dtype = float64
  Dataset /intervals/Disco2SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/tags (VectorData) user-defined tags | shape = (28800,) | dtype = object
  Dataset /intervals/Disco2SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (28800,) | dtype = uint16
  Dataset /intervals/Disco2SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (28800,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/Disco2SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (28800,) | dtype = uint16
  Dataset /intervals/Disco2SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/units (VectorData) Units of stimulus size | shape = (28800,) | dtype = object
  Group /intervals/Disk_Wd15_Vel2_Bndry1_Cntst0_loop_presentations (TimeIntervals) Presentation times and stimuli details for 'Disk_Wd15_Vel2_Bndry1_Cntst0_loop' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/Disk_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/color (VectorData) No description | shape = (14400,) | dtype = object
  Dataset /intervals/Disk_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/contrast (VectorData) Contrast of stimulus | shape = (14400,) | dtype = float64
  Dataset /intervals/Disk_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/frame (VectorData) Frame of movie stimulus | shape = (14400,) | dtype = float64
  Dataset /intervals/Disk_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/id (ElementIdentifiers)  | shape = (14400,) | dtype = int64
  Dataset /intervals/Disk_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/opacity (VectorData) Opacity of stimulus | shape = (14400,) | dtype = float64
  Dataset /intervals/Disk_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/orientation (VectorData) Orientation of stimulus | shape = (14400,) | dtype = float64
  Dataset /intervals/Disk_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (14400,) | dtype = object
  Dataset /intervals/Disk_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (14400,) | dtype = float64
  Dataset /intervals/Disk_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (14400,) | dtype = float64
  Dataset /intervals/Disk_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (14400,) | dtype = float64
  Dataset /intervals/Disk_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/stimulus_name (VectorData) Name of stimulus | shape = (14400,) | dtype = object
  Dataset /intervals/Disk_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (14400,) | dtype = float64
  Dataset /intervals/Disk_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/tags (VectorData) user-defined tags | shape = (14400,) | dtype = object
  Dataset /intervals/Disk_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (14400,) | dtype = uint16
  Dataset /intervals/Disk_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (14400,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/Disk_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (14400,) | dtype = uint16
  Dataset /intervals/Disk_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/units (VectorData) Units of stimulus size | shape = (14400,) | dtype = object
  Group /intervals/GreenSAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations (TimeIntervals) Presentation times and stimuli details for 'GreenSAC_Wd15_Vel2_Bndry1_Cntst0_loop' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/GreenSAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/color (VectorData) No description | shape = (14400,) | dtype = object
  Dataset /intervals/GreenSAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/contrast (VectorData) Contrast of stimulus | shape = (14400,) | dtype = float64
  Dataset /intervals/GreenSAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/frame (VectorData) Frame of movie stimulus | shape = (14400,) | dtype = float64
  Dataset /intervals/GreenSAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/id (ElementIdentifiers)  | shape = (14400,) | dtype = int64
  Dataset /intervals/GreenSAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/opacity (VectorData) Opacity of stimulus | shape = (14400,) | dtype = float64
  Dataset /intervals/GreenSAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/orientation (VectorData) Orientation of stimulus | shape = (14400,) | dtype = float64
  Dataset /intervals/GreenSAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (14400,) | dtype = object
  Dataset /intervals/GreenSAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (14400,) | dtype = float64
  Dataset /intervals/GreenSAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (14400,) | dtype = float64
  Dataset /intervals/GreenSAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (14400,) | dtype = float64
  Dataset /intervals/GreenSAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/stimulus_name (VectorData) Name of stimulus | shape = (14400,) | dtype = object
  Dataset /intervals/GreenSAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (14400,) | dtype = float64
  Dataset /intervals/GreenSAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/tags (VectorData) user-defined tags | shape = (14400,) | dtype = object
  Dataset /intervals/GreenSAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (14400,) | dtype = uint16
  Dataset /intervals/GreenSAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (14400,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/GreenSAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (14400,) | dtype = uint16
  Dataset /intervals/GreenSAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/units (VectorData) Units of stimulus size | shape = (14400,) | dtype = object
  Group /intervals/Ring_Wd15_Vel2_Bndry1_Cntst0_loop_presentations (TimeIntervals) Presentation times and stimuli details for 'Ring_Wd15_Vel2_Bndry1_Cntst0_loop' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/Ring_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/color (VectorData) No description | shape = (28800,) | dtype = object
  Dataset /intervals/Ring_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/contrast (VectorData) Contrast of stimulus | shape = (28800,) | dtype = float64
  Dataset /intervals/Ring_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/frame (VectorData) Frame of movie stimulus | shape = (28800,) | dtype = float64
  Dataset /intervals/Ring_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/id (ElementIdentifiers)  | shape = (28800,) | dtype = int64
  Dataset /intervals/Ring_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/opacity (VectorData) Opacity of stimulus | shape = (28800,) | dtype = float64
  Dataset /intervals/Ring_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/orientation (VectorData) Orientation of stimulus | shape = (28800,) | dtype = float64
  Dataset /intervals/Ring_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (28800,) | dtype = object
  Dataset /intervals/Ring_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (28800,) | dtype = float64
  Dataset /intervals/Ring_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (28800,) | dtype = float64
  Dataset /intervals/Ring_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (28800,) | dtype = float64
  Dataset /intervals/Ring_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/stimulus_name (VectorData) Name of stimulus | shape = (28800,) | dtype = object
  Dataset /intervals/Ring_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (28800,) | dtype = float64
  Dataset /intervals/Ring_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/tags (VectorData) user-defined tags | shape = (28800,) | dtype = object
  Dataset /intervals/Ring_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (28800,) | dtype = uint16
  Dataset /intervals/Ring_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (28800,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/Ring_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (28800,) | dtype = uint16
  Dataset /intervals/Ring_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/units (VectorData) Units of stimulus size | shape = (28800,) | dtype = object
  Group /intervals/SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations (TimeIntervals) Presentation times and stimuli details for 'SAC_Wd15_Vel2_Bndry1_Cntst0_loop' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/color (VectorData) No description | shape = (28800,) | dtype = object
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/contrast (VectorData) Contrast of stimulus | shape = (28800,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/frame (VectorData) Frame of movie stimulus | shape = (28800,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/id (ElementIdentifiers)  | shape = (28800,) | dtype = int64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/opacity (VectorData) Opacity of stimulus | shape = (28800,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/orientation (VectorData) Orientation of stimulus | shape = (28800,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (28800,) | dtype = object
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (28800,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (28800,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (28800,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/stimulus_name (VectorData) Name of stimulus | shape = (28800,) | dtype = object
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (28800,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/tags (VectorData) user-defined tags | shape = (28800,) | dtype = object
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (28800,) | dtype = uint16
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (28800,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (28800,) | dtype = uint16
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/units (VectorData) Units of stimulus size | shape = (28800,) | dtype = object
  Group /intervals/SAC_Wd15_Vel2_Bndry1_Cntst1_loop_presentations (TimeIntervals) Presentation times and stimuli details for 'SAC_Wd15_Vel2_Bndry1_Cntst1_loop' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst1_loop_presentations/color (VectorData) No description | shape = (14400,) | dtype = object
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst1_loop_presentations/contrast (VectorData) Contrast of stimulus | shape = (14400,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst1_loop_presentations/frame (VectorData) Frame of movie stimulus | shape = (14400,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst1_loop_presentations/id (ElementIdentifiers)  | shape = (14400,) | dtype = int64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst1_loop_presentations/opacity (VectorData) Opacity of stimulus | shape = (14400,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst1_loop_presentations/orientation (VectorData) Orientation of stimulus | shape = (14400,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst1_loop_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (14400,) | dtype = object
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst1_loop_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (14400,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst1_loop_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (14400,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst1_loop_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (14400,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst1_loop_presentations/stimulus_name (VectorData) Name of stimulus | shape = (14400,) | dtype = object
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst1_loop_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (14400,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst1_loop_presentations/tags (VectorData) user-defined tags | shape = (14400,) | dtype = object
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst1_loop_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (14400,) | dtype = uint16
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst1_loop_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (14400,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst1_loop_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (14400,) | dtype = uint16
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst1_loop_presentations/units (VectorData) Units of stimulus size | shape = (14400,) | dtype = object
  Group /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_loop_presentations (TimeIntervals) Presentation times and stimuli details for 'SAC_Wd15_Vel2_Bndry2_Cntst0_loop' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_loop_presentations/color (VectorData) No description | shape = (17040,) | dtype = object
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_loop_presentations/contrast (VectorData) Contrast of stimulus | shape = (17040,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_loop_presentations/frame (VectorData) Frame of movie stimulus | shape = (17040,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_loop_presentations/id (ElementIdentifiers)  | shape = (17040,) | dtype = int64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_loop_presentations/opacity (VectorData) Opacity of stimulus | shape = (17040,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_loop_presentations/orientation (VectorData) Orientation of stimulus | shape = (17040,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_loop_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (17040,) | dtype = object
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_loop_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (17040,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_loop_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (17040,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_loop_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (17040,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_loop_presentations/stimulus_name (VectorData) Name of stimulus | shape = (17040,) | dtype = object
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_loop_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (17040,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_loop_presentations/tags (VectorData) user-defined tags | shape = (17040,) | dtype = object
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_loop_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (17040,) | dtype = uint16
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_loop_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (17040,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_loop_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (17040,) | dtype = uint16
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_loop_presentations/units (VectorData) Units of stimulus size | shape = (17040,) | dtype = object
  Group /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_oneway_presentations (TimeIntervals) Presentation times and stimuli details for 'SAC_Wd15_Vel2_Bndry2_Cntst0_oneway' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_oneway_presentations/color (VectorData) No description | shape = (8520,) | dtype = object
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_oneway_presentations/contrast (VectorData) Contrast of stimulus | shape = (8520,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_oneway_presentations/frame (VectorData) Frame of movie stimulus | shape = (8520,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_oneway_presentations/id (ElementIdentifiers)  | shape = (8520,) | dtype = int64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_oneway_presentations/opacity (VectorData) Opacity of stimulus | shape = (8520,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_oneway_presentations/orientation (VectorData) Orientation of stimulus | shape = (8520,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_oneway_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (8520,) | dtype = object
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_oneway_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (8520,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_oneway_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (8520,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_oneway_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (8520,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_oneway_presentations/stimulus_name (VectorData) Name of stimulus | shape = (8520,) | dtype = object
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_oneway_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (8520,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_oneway_presentations/tags (VectorData) user-defined tags | shape = (8520,) | dtype = object
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_oneway_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (8520,) | dtype = uint16
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_oneway_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (8520,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_oneway_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (8520,) | dtype = uint16
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_oneway_presentations/units (VectorData) Units of stimulus size | shape = (8520,) | dtype = object
  Group /intervals/SAC_Wd15_Vel2_Bndry3_Cntst0_loop_presentations (TimeIntervals) Presentation times and stimuli details for 'SAC_Wd15_Vel2_Bndry3_Cntst0_loop' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/SAC_Wd15_Vel2_Bndry3_Cntst0_loop_presentations/color (VectorData) No description | shape = (22320,) | dtype = object
  Dataset /intervals/SAC_Wd15_Vel2_Bndry3_Cntst0_loop_presentations/contrast (VectorData) Contrast of stimulus | shape = (22320,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry3_Cntst0_loop_presentations/frame (VectorData) Frame of movie stimulus | shape = (22320,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry3_Cntst0_loop_presentations/id (ElementIdentifiers)  | shape = (22320,) | dtype = int64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry3_Cntst0_loop_presentations/opacity (VectorData) Opacity of stimulus | shape = (22320,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry3_Cntst0_loop_presentations/orientation (VectorData) Orientation of stimulus | shape = (22320,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry3_Cntst0_loop_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (22320,) | dtype = object
  Dataset /intervals/SAC_Wd15_Vel2_Bndry3_Cntst0_loop_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (22320,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry3_Cntst0_loop_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (22320,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry3_Cntst0_loop_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (22320,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry3_Cntst0_loop_presentations/stimulus_name (VectorData) Name of stimulus | shape = (22320,) | dtype = object
  Dataset /intervals/SAC_Wd15_Vel2_Bndry3_Cntst0_loop_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (22320,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry3_Cntst0_loop_presentations/tags (VectorData) user-defined tags | shape = (22320,) | dtype = object
  Dataset /intervals/SAC_Wd15_Vel2_Bndry3_Cntst0_loop_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (22320,) | dtype = uint16
  Dataset /intervals/SAC_Wd15_Vel2_Bndry3_Cntst0_loop_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (22320,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/SAC_Wd15_Vel2_Bndry3_Cntst0_loop_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (22320,) | dtype = uint16
  Dataset /intervals/SAC_Wd15_Vel2_Bndry3_Cntst0_loop_presentations/units (VectorData) Units of stimulus size | shape = (22320,) | dtype = object
  Group /intervals/SAC_Wd15_Vel8_Bndry1_Cntst0_loop_presentations (TimeIntervals) Presentation times and stimuli details for 'SAC_Wd15_Vel8_Bndry1_Cntst0_loop' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/SAC_Wd15_Vel8_Bndry1_Cntst0_loop_presentations/color (VectorData) No description | shape = (57600,) | dtype = object
  Dataset /intervals/SAC_Wd15_Vel8_Bndry1_Cntst0_loop_presentations/contrast (VectorData) Contrast of stimulus | shape = (57600,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel8_Bndry1_Cntst0_loop_presentations/frame (VectorData) Frame of movie stimulus | shape = (57600,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel8_Bndry1_Cntst0_loop_presentations/id (ElementIdentifiers)  | shape = (57600,) | dtype = int64
  Dataset /intervals/SAC_Wd15_Vel8_Bndry1_Cntst0_loop_presentations/opacity (VectorData) Opacity of stimulus | shape = (57600,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel8_Bndry1_Cntst0_loop_presentations/orientation (VectorData) Orientation of stimulus | shape = (57600,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel8_Bndry1_Cntst0_loop_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (57600,) | dtype = object
  Dataset /intervals/SAC_Wd15_Vel8_Bndry1_Cntst0_loop_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (57600,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel8_Bndry1_Cntst0_loop_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (57600,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel8_Bndry1_Cntst0_loop_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (57600,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel8_Bndry1_Cntst0_loop_presentations/stimulus_name (VectorData) Name of stimulus | shape = (57600,) | dtype = object
  Dataset /intervals/SAC_Wd15_Vel8_Bndry1_Cntst0_loop_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (57600,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel8_Bndry1_Cntst0_loop_presentations/tags (VectorData) user-defined tags | shape = (57600,) | dtype = object
  Dataset /intervals/SAC_Wd15_Vel8_Bndry1_Cntst0_loop_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (57600,) | dtype = uint16
  Dataset /intervals/SAC_Wd15_Vel8_Bndry1_Cntst0_loop_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (57600,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/SAC_Wd15_Vel8_Bndry1_Cntst0_loop_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (57600,) | dtype = uint16
  Dataset /intervals/SAC_Wd15_Vel8_Bndry1_Cntst0_loop_presentations/units (VectorData) Units of stimulus size | shape = (57600,) | dtype = object
  Group /intervals/SAC_Wd45_Vel2_Bndry1_Cntst0_loop_presentations (TimeIntervals) Presentation times and stimuli details for 'SAC_Wd45_Vel2_Bndry1_Cntst0_loop' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/SAC_Wd45_Vel2_Bndry1_Cntst0_loop_presentations/color (VectorData) No description | shape = (14400,) | dtype = object
  Dataset /intervals/SAC_Wd45_Vel2_Bndry1_Cntst0_loop_presentations/contrast (VectorData) Contrast of stimulus | shape = (14400,) | dtype = float64
  Dataset /intervals/SAC_Wd45_Vel2_Bndry1_Cntst0_loop_presentations/frame (VectorData) Frame of movie stimulus | shape = (14400,) | dtype = float64
  Dataset /intervals/SAC_Wd45_Vel2_Bndry1_Cntst0_loop_presentations/id (ElementIdentifiers)  | shape = (14400,) | dtype = int64
  Dataset /intervals/SAC_Wd45_Vel2_Bndry1_Cntst0_loop_presentations/opacity (VectorData) Opacity of stimulus | shape = (14400,) | dtype = float64
  Dataset /intervals/SAC_Wd45_Vel2_Bndry1_Cntst0_loop_presentations/orientation (VectorData) Orientation of stimulus | shape = (14400,) | dtype = float64
  Dataset /intervals/SAC_Wd45_Vel2_Bndry1_Cntst0_loop_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (14400,) | dtype = object
  Dataset /intervals/SAC_Wd45_Vel2_Bndry1_Cntst0_loop_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (14400,) | dtype = float64
  Dataset /intervals/SAC_Wd45_Vel2_Bndry1_Cntst0_loop_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (14400,) | dtype = float64
  Dataset /intervals/SAC_Wd45_Vel2_Bndry1_Cntst0_loop_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (14400,) | dtype = float64
  Dataset /intervals/SAC_Wd45_Vel2_Bndry1_Cntst0_loop_presentations/stimulus_name (VectorData) Name of stimulus | shape = (14400,) | dtype = object
  Dataset /intervals/SAC_Wd45_Vel2_Bndry1_Cntst0_loop_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (14400,) | dtype = float64
  Dataset /intervals/SAC_Wd45_Vel2_Bndry1_Cntst0_loop_presentations/tags (VectorData) user-defined tags | shape = (14400,) | dtype = object
  Dataset /intervals/SAC_Wd45_Vel2_Bndry1_Cntst0_loop_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (14400,) | dtype = uint16
  Dataset /intervals/SAC_Wd45_Vel2_Bndry1_Cntst0_loop_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (14400,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/SAC_Wd45_Vel2_Bndry1_Cntst0_loop_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (14400,) | dtype = uint16
  Dataset /intervals/SAC_Wd45_Vel2_Bndry1_Cntst0_loop_presentations/units (VectorData) Units of stimulus size | shape = (14400,) | dtype = object
  Group /intervals/UD_Wd15_Vel2_Bndry1_Cntst0_loop_presentations (TimeIntervals) Presentation times and stimuli details for 'UD_Wd15_Vel2_Bndry1_Cntst0_loop' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/UD_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/color (VectorData) No description | shape = (28800,) | dtype = object
  Dataset /intervals/UD_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/contrast (VectorData) Contrast of stimulus | shape = (28800,) | dtype = float64
  Dataset /intervals/UD_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/frame (VectorData) Frame of movie stimulus | shape = (28800,) | dtype = float64
  Dataset /intervals/UD_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/id (ElementIdentifiers)  | shape = (28800,) | dtype = int64
  Dataset /intervals/UD_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/opacity (VectorData) Opacity of stimulus | shape = (28800,) | dtype = float64
  Dataset /intervals/UD_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/orientation (VectorData) Orientation of stimulus | shape = (28800,) | dtype = float64
  Dataset /intervals/UD_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (28800,) | dtype = object
  Dataset /intervals/UD_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (28800,) | dtype = float64
  Dataset /intervals/UD_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (28800,) | dtype = float64
  Dataset /intervals/UD_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (28800,) | dtype = float64
  Dataset /intervals/UD_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/stimulus_name (VectorData) Name of stimulus | shape = (28800,) | dtype = object
  Dataset /intervals/UD_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (28800,) | dtype = float64
  Dataset /intervals/UD_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/tags (VectorData) user-defined tags | shape = (28800,) | dtype = object
  Dataset /intervals/UD_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (28800,) | dtype = uint16
  Dataset /intervals/UD_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (28800,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/UD_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (28800,) | dtype = uint16
  Dataset /intervals/UD_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/units (VectorData) Units of stimulus size | shape = (28800,) | dtype = object
  Group /intervals/acurl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations (TimeIntervals) Presentation times and stimuli details for 'acurl_Wd15_Vel2_Bndry1_Cntst0_oneway' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/acurl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/color (VectorData) No description | shape = (7200,) | dtype = object
  Dataset /intervals/acurl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/contrast (VectorData) Contrast of stimulus | shape = (7200,) | dtype = float64
  Dataset /intervals/acurl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/frame (VectorData) Frame of movie stimulus | shape = (7200,) | dtype = float64
  Dataset /intervals/acurl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/id (ElementIdentifiers)  | shape = (7200,) | dtype = int64
  Dataset /intervals/acurl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/opacity (VectorData) Opacity of stimulus | shape = (7200,) | dtype = float64
  Dataset /intervals/acurl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/orientation (VectorData) Orientation of stimulus | shape = (7200,) | dtype = float64
  Dataset /intervals/acurl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (7200,) | dtype = object
  Dataset /intervals/acurl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (7200,) | dtype = float64
  Dataset /intervals/acurl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (7200,) | dtype = float64
  Dataset /intervals/acurl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (7200,) | dtype = float64
  Dataset /intervals/acurl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/stimulus_name (VectorData) Name of stimulus | shape = (7200,) | dtype = object
  Dataset /intervals/acurl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (7200,) | dtype = float64
  Dataset /intervals/acurl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/tags (VectorData) user-defined tags | shape = (7200,) | dtype = object
  Dataset /intervals/acurl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (7200,) | dtype = uint16
  Dataset /intervals/acurl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (7200,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/acurl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (7200,) | dtype = uint16
  Dataset /intervals/acurl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/units (VectorData) Units of stimulus size | shape = (7200,) | dtype = object
  Group /intervals/curl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations (TimeIntervals) Presentation times and stimuli details for 'curl_Wd15_Vel2_Bndry1_Cntst0_oneway' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/curl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/color (VectorData) No description | shape = (7200,) | dtype = object
  Dataset /intervals/curl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/contrast (VectorData) Contrast of stimulus | shape = (7200,) | dtype = float64
  Dataset /intervals/curl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/frame (VectorData) Frame of movie stimulus | shape = (7200,) | dtype = float64
  Dataset /intervals/curl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/id (ElementIdentifiers)  | shape = (7200,) | dtype = int64
  Dataset /intervals/curl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/opacity (VectorData) Opacity of stimulus | shape = (7200,) | dtype = float64
  Dataset /intervals/curl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/orientation (VectorData) Orientation of stimulus | shape = (7200,) | dtype = float64
  Dataset /intervals/curl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (7200,) | dtype = object
  Dataset /intervals/curl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (7200,) | dtype = float64
  Dataset /intervals/curl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (7200,) | dtype = float64
  Dataset /intervals/curl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (7200,) | dtype = float64
  Dataset /intervals/curl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/stimulus_name (VectorData) Name of stimulus | shape = (7200,) | dtype = object
  Dataset /intervals/curl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (7200,) | dtype = float64
  Dataset /intervals/curl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/tags (VectorData) user-defined tags | shape = (7200,) | dtype = object
  Dataset /intervals/curl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (7200,) | dtype = uint16
  Dataset /intervals/curl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (7200,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/curl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (7200,) | dtype = uint16
  Dataset /intervals/curl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/units (VectorData) Units of stimulus size | shape = (7200,) | dtype = object
  Group /intervals/invalid_times (TimeIntervals) experimental intervals
  Dataset /intervals/invalid_times/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /intervals/invalid_times/start_time (VectorData) Start time of epoch, in seconds | shape = (1,) | dtype = float64
  Dataset /intervals/invalid_times/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1,) | dtype = float64
  Dataset /intervals/invalid_times/tags (VectorData) user-defined tags | shape = (3,) | dtype = object
  Dataset /intervals/invalid_times/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (1,) | dtype = uint8
  Group /intervals/natmovie_CricketsOnARock_540x960Full_584x460Active_presentations (TimeIntervals) Presentation times and stimuli details for 'natmovie_CricketsOnARock_540x960Full_584x460Active' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/natmovie_CricketsOnARock_540x960Full_584x460Active_presentations/color (VectorData) No description | shape = (14400,) | dtype = object
  Dataset /intervals/natmovie_CricketsOnARock_540x960Full_584x460Active_presentations/contrast (VectorData) Contrast of stimulus | shape = (14400,) | dtype = float64
  Dataset /intervals/natmovie_CricketsOnARock_540x960Full_584x460Active_presentations/frame (VectorData) Frame of movie stimulus | shape = (14400,) | dtype = float64
  Dataset /intervals/natmovie_CricketsOnARock_540x960Full_584x460Active_presentations/id (ElementIdentifiers)  | shape = (14400,) | dtype = int64
  Dataset /intervals/natmovie_CricketsOnARock_540x960Full_584x460Active_presentations/opacity (VectorData) Opacity of stimulus | shape = (14400,) | dtype = float64
  Dataset /intervals/natmovie_CricketsOnARock_540x960Full_584x460Active_presentations/orientation (VectorData) Orientation of stimulus | shape = (14400,) | dtype = float64
  Dataset /intervals/natmovie_CricketsOnARock_540x960Full_584x460Active_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (14400,) | dtype = object
  Dataset /intervals/natmovie_CricketsOnARock_540x960Full_584x460Active_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (14400,) | dtype = float64
  Dataset /intervals/natmovie_CricketsOnARock_540x960Full_584x460Active_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (14400,) | dtype = float64
  Dataset /intervals/natmovie_CricketsOnARock_540x960Full_584x460Active_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (14400,) | dtype = float64
  Dataset /intervals/natmovie_CricketsOnARock_540x960Full_584x460Active_presentations/stimulus_name (VectorData) Name of stimulus | shape = (14400,) | dtype = object
  Dataset /intervals/natmovie_CricketsOnARock_540x960Full_584x460Active_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (14400,) | dtype = float64
  Dataset /intervals/natmovie_CricketsOnARock_540x960Full_584x460Active_presentations/tags (VectorData) user-defined tags | shape = (14400,) | dtype = object
  Dataset /intervals/natmovie_CricketsOnARock_540x960Full_584x460Active_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (14400,) | dtype = uint16
  Dataset /intervals/natmovie_CricketsOnARock_540x960Full_584x460Active_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (14400,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/natmovie_CricketsOnARock_540x960Full_584x460Active_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (14400,) | dtype = uint16
  Dataset /intervals/natmovie_CricketsOnARock_540x960Full_584x460Active_presentations/units (VectorData) Units of stimulus size | shape = (14400,) | dtype = object
  Group /intervals/natmovie_EagleSwooping1_540x960Full_584x460Active_presentations (TimeIntervals) Presentation times and stimuli details for 'natmovie_EagleSwooping1_540x960Full_584x460Active' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/natmovie_EagleSwooping1_540x960Full_584x460Active_presentations/color (VectorData) No description | shape = (14400,) | dtype = object
  Dataset /intervals/natmovie_EagleSwooping1_540x960Full_584x460Active_presentations/contrast (VectorData) Contrast of stimulus | shape = (14400,) | dtype = float64
  Dataset /intervals/natmovie_EagleSwooping1_540x960Full_584x460Active_presentations/frame (VectorData) Frame of movie stimulus | shape = (14400,) | dtype = float64
  Dataset /intervals/natmovie_EagleSwooping1_540x960Full_584x460Active_presentations/id (ElementIdentifiers)  | shape = (14400,) | dtype = int64
  Dataset /intervals/natmovie_EagleSwooping1_540x960Full_584x460Active_presentations/opacity (VectorData) Opacity of stimulus | shape = (14400,) | dtype = float64
  Dataset /intervals/natmovie_EagleSwooping1_540x960Full_584x460Active_presentations/orientation (VectorData) Orientation of stimulus | shape = (14400,) | dtype = float64
  Dataset /intervals/natmovie_EagleSwooping1_540x960Full_584x460Active_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (14400,) | dtype = object
  Dataset /intervals/natmovie_EagleSwooping1_540x960Full_584x460Active_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (14400,) | dtype = float64
  Dataset /intervals/natmovie_EagleSwooping1_540x960Full_584x460Active_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (14400,) | dtype = float64
  Dataset /intervals/natmovie_EagleSwooping1_540x960Full_584x460Active_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (14400,) | dtype = float64
  Dataset /intervals/natmovie_EagleSwooping1_540x960Full_584x460Active_presentations/stimulus_name (VectorData) Name of stimulus | shape = (14400,) | dtype = object
  Dataset /intervals/natmovie_EagleSwooping1_540x960Full_584x460Active_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (14400,) | dtype = float64
  Dataset /intervals/natmovie_EagleSwooping1_540x960Full_584x460Active_presentations/tags (VectorData) user-defined tags | shape = (14400,) | dtype = object
  Dataset /intervals/natmovie_EagleSwooping1_540x960Full_584x460Active_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (14400,) | dtype = uint16
  Dataset /intervals/natmovie_EagleSwooping1_540x960Full_584x460Active_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (14400,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/natmovie_EagleSwooping1_540x960Full_584x460Active_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (14400,) | dtype = uint16
  Dataset /intervals/natmovie_EagleSwooping1_540x960Full_584x460Active_presentations/units (VectorData) Units of stimulus size | shape = (14400,) | dtype = object
  Group /intervals/natmovie_EagleSwooping2_540x960Full_584x460Active_presentations (TimeIntervals) Presentation times and stimuli details for 'natmovie_EagleSwooping2_540x960Full_584x460Active' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/natmovie_EagleSwooping2_540x960Full_584x460Active_presentations/color (VectorData) No description | shape = (14400,) | dtype = object
  Dataset /intervals/natmovie_EagleSwooping2_540x960Full_584x460Active_presentations/contrast (VectorData) Contrast of stimulus | shape = (14400,) | dtype = float64
  Dataset /intervals/natmovie_EagleSwooping2_540x960Full_584x460Active_presentations/frame (VectorData) Frame of movie stimulus | shape = (14400,) | dtype = float64
  Dataset /intervals/natmovie_EagleSwooping2_540x960Full_584x460Active_presentations/id (ElementIdentifiers)  | shape = (14400,) | dtype = int64
  Dataset /intervals/natmovie_EagleSwooping2_540x960Full_584x460Active_presentations/opacity (VectorData) Opacity of stimulus | shape = (14400,) | dtype = float64
  Dataset /intervals/natmovie_EagleSwooping2_540x960Full_584x460Active_presentations/orientation (VectorData) Orientation of stimulus | shape = (14400,) | dtype = float64
  Dataset /intervals/natmovie_EagleSwooping2_540x960Full_584x460Active_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (14400,) | dtype = object
  Dataset /intervals/natmovie_EagleSwooping2_540x960Full_584x460Active_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (14400,) | dtype = float64
  Dataset /intervals/natmovie_EagleSwooping2_540x960Full_584x460Active_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (14400,) | dtype = float64
  Dataset /intervals/natmovie_EagleSwooping2_540x960Full_584x460Active_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (14400,) | dtype = float64
  Dataset /intervals/natmovie_EagleSwooping2_540x960Full_584x460Active_presentations/stimulus_name (VectorData) Name of stimulus | shape = (14400,) | dtype = object
  Dataset /intervals/natmovie_EagleSwooping2_540x960Full_584x460Active_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (14400,) | dtype = float64
  Dataset /intervals/natmovie_EagleSwooping2_540x960Full_584x460Active_presentations/tags (VectorData) user-defined tags | shape = (14400,) | dtype = object
  Dataset /intervals/natmovie_EagleSwooping2_540x960Full_584x460Active_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (14400,) | dtype = uint16
  Dataset /intervals/natmovie_EagleSwooping2_540x960Full_584x460Active_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (14400,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/natmovie_EagleSwooping2_540x960Full_584x460Active_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (14400,) | dtype = uint16
  Dataset /intervals/natmovie_EagleSwooping2_540x960Full_584x460Active_presentations/units (VectorData) Units of stimulus size | shape = (14400,) | dtype = object
  Group /intervals/natmovie_SnakeOnARoad_540x960Full_584x460Active_presentations (TimeIntervals) Presentation times and stimuli details for 'natmovie_SnakeOnARoad_540x960Full_584x460Active' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/natmovie_SnakeOnARoad_540x960Full_584x460Active_presentations/color (VectorData) No description | shape = (14400,) | dtype = object
  Dataset /intervals/natmovie_SnakeOnARoad_540x960Full_584x460Active_presentations/contrast (VectorData) Contrast of stimulus | shape = (14400,) | dtype = float64
  Dataset /intervals/natmovie_SnakeOnARoad_540x960Full_584x460Active_presentations/frame (VectorData) Frame of movie stimulus | shape = (14400,) | dtype = float64
  Dataset /intervals/natmovie_SnakeOnARoad_540x960Full_584x460Active_presentations/id (ElementIdentifiers)  | shape = (14400,) | dtype = int64
  Dataset /intervals/natmovie_SnakeOnARoad_540x960Full_584x460Active_presentations/opacity (VectorData) Opacity of stimulus | shape = (14400,) | dtype = float64
  Dataset /intervals/natmovie_SnakeOnARoad_540x960Full_584x460Active_presentations/orientation (VectorData) Orientation of stimulus | shape = (14400,) | dtype = float64
  Dataset /intervals/natmovie_SnakeOnARoad_540x960Full_584x460Active_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (14400,) | dtype = object
  Dataset /intervals/natmovie_SnakeOnARoad_540x960Full_584x460Active_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (14400,) | dtype = float64
  Dataset /intervals/natmovie_SnakeOnARoad_540x960Full_584x460Active_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (14400,) | dtype = float64
  Dataset /intervals/natmovie_SnakeOnARoad_540x960Full_584x460Active_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (14400,) | dtype = float64
  Dataset /intervals/natmovie_SnakeOnARoad_540x960Full_584x460Active_presentations/stimulus_name (VectorData) Name of stimulus | shape = (14400,) | dtype = object
  Dataset /intervals/natmovie_SnakeOnARoad_540x960Full_584x460Active_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (14400,) | dtype = float64
  Dataset /intervals/natmovie_SnakeOnARoad_540x960Full_584x460Active_presentations/tags (VectorData) user-defined tags | shape = (14400,) | dtype = object
  Dataset /intervals/natmovie_SnakeOnARoad_540x960Full_584x460Active_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (14400,) | dtype = uint16
  Dataset /intervals/natmovie_SnakeOnARoad_540x960Full_584x460Active_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (14400,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/natmovie_SnakeOnARoad_540x960Full_584x460Active_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (14400,) | dtype = uint16
  Dataset /intervals/natmovie_SnakeOnARoad_540x960Full_584x460Active_presentations/units (VectorData) Units of stimulus size | shape = (14400,) | dtype = object
  Group /intervals/natmovie_Squirreland3Mice_540x960Full_584x460Active_presentations (TimeIntervals) Presentation times and stimuli details for 'natmovie_Squirreland3Mice_540x960Full_584x460Active' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/natmovie_Squirreland3Mice_540x960Full_584x460Active_presentations/color (VectorData) No description | shape = (14400,) | dtype = object
  Dataset /intervals/natmovie_Squirreland3Mice_540x960Full_584x460Active_presentations/contrast (VectorData) Contrast of stimulus | shape = (14400,) | dtype = float64
  Dataset /intervals/natmovie_Squirreland3Mice_540x960Full_584x460Active_presentations/frame (VectorData) Frame of movie stimulus | shape = (14400,) | dtype = float64
  Dataset /intervals/natmovie_Squirreland3Mice_540x960Full_584x460Active_presentations/id (ElementIdentifiers)  | shape = (14400,) | dtype = int64
  Dataset /intervals/natmovie_Squirreland3Mice_540x960Full_584x460Active_presentations/opacity (VectorData) Opacity of stimulus | shape = (14400,) | dtype = float64
  Dataset /intervals/natmovie_Squirreland3Mice_540x960Full_584x460Active_presentations/orientation (VectorData) Orientation of stimulus | shape = (14400,) | dtype = float64
  Dataset /intervals/natmovie_Squirreland3Mice_540x960Full_584x460Active_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (14400,) | dtype = object
  Dataset /intervals/natmovie_Squirreland3Mice_540x960Full_584x460Active_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (14400,) | dtype = float64
  Dataset /intervals/natmovie_Squirreland3Mice_540x960Full_584x460Active_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (14400,) | dtype = float64
  Dataset /intervals/natmovie_Squirreland3Mice_540x960Full_584x460Active_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (14400,) | dtype = float64
  Dataset /intervals/natmovie_Squirreland3Mice_540x960Full_584x460Active_presentations/stimulus_name (VectorData) Name of stimulus | shape = (14400,) | dtype = object
  Dataset /intervals/natmovie_Squirreland3Mice_540x960Full_584x460Active_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (14400,) | dtype = float64
  Dataset /intervals/natmovie_Squirreland3Mice_540x960Full_584x460Active_presentations/tags (VectorData) user-defined tags | shape = (14400,) | dtype = object
  Dataset /intervals/natmovie_Squirreland3Mice_540x960Full_584x460Active_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (14400,) | dtype = uint16
  Dataset /intervals/natmovie_Squirreland3Mice_540x960Full_584x460Active_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (14400,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/natmovie_Squirreland3Mice_540x960Full_584x460Active_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (14400,) | dtype = uint16
  Dataset /intervals/natmovie_Squirreland3Mice_540x960Full_584x460Active_presentations/units (VectorData) Units of stimulus size | shape = (14400,) | dtype = object
  Group /intervals/receptive_field_block_presentations (TimeIntervals) Presentation times and stimuli details for 'receptive_field_block' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/receptive_field_block_presentations/color (VectorData) No description | shape = (3840,) | dtype = object
  Dataset /intervals/receptive_field_block_presentations/contrast (VectorData) Contrast of stimulus | shape = (3840,) | dtype = float64
  Dataset /intervals/receptive_field_block_presentations/id (ElementIdentifiers)  | shape = (3840,) | dtype = int64
  Dataset /intervals/receptive_field_block_presentations/mask (VectorData) Shape of mask applied to stimulus | shape = (3840,) | dtype = object
  Dataset /intervals/receptive_field_block_presentations/opacity (VectorData) Opacity of stimulus | shape = (3840,) | dtype = float64
  Dataset /intervals/receptive_field_block_presentations/orientation (VectorData) Orientation of stimulus | shape = (3840,) | dtype = float64
  Dataset /intervals/receptive_field_block_presentations/phase (VectorData) Phase of grating stimulus | shape = (3840,) | dtype = object
  Dataset /intervals/receptive_field_block_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (3840,) | dtype = object
  Dataset /intervals/receptive_field_block_presentations/spatial_frequency (VectorData) Spatial frequency of stimulus | shape = (3840,) | dtype = float64
  Dataset /intervals/receptive_field_block_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (3840,) | dtype = float64
  Dataset /intervals/receptive_field_block_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (3840,) | dtype = float64
  Dataset /intervals/receptive_field_block_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (3840,) | dtype = float64
  Dataset /intervals/receptive_field_block_presentations/stimulus_name (VectorData) Name of stimulus | shape = (3840,) | dtype = object
  Dataset /intervals/receptive_field_block_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (3840,) | dtype = float64
  Dataset /intervals/receptive_field_block_presentations/tags (VectorData) user-defined tags | shape = (3840,) | dtype = object
  Dataset /intervals/receptive_field_block_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (3840,) | dtype = uint16
  Dataset /intervals/receptive_field_block_presentations/temporal_frequency (VectorData) Temporal frequency of stimulus | shape = (3840,) | dtype = float64
  Dataset /intervals/receptive_field_block_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (3840,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/receptive_field_block_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (3840,) | dtype = uint16
  Dataset /intervals/receptive_field_block_presentations/units (VectorData) Units of stimulus size | shape = (3840,) | dtype = object
  Dataset /intervals/receptive_field_block_presentations/x_position (VectorData) Horizontal position of stimulus on screen | shape = (3840,) | dtype = float64
  Dataset /intervals/receptive_field_block_presentations/y_position (VectorData) Vertical position of stimulus on screen | shape = (3840,) | dtype = float64
  Group /processing/running (ProcessingModule) running speed data
  Group /processing/running/running_speed (TimeSeries) no description
  Group /processing/running/running_speed_end_times (TimeSeries) no description
  Group /processing/running/running_wheel_rotation (TimeSeries) no description
  Group /processing/stimulus (ProcessingModule) Stimulus Times processing
  Group /processing/stimulus/timestamps (TimeSeries) no description
  session_description: Data and metadata for an Ecephys session
  session_start_time: 2023-09-21T00:00:00-07:00
  timestamps_reference_time: 2023-09-21T00:00:00-07:00
  Group /units (Units) 
  Dataset /units/PT_ratio (VectorData) no description | shape = (2764,) | dtype = float64
  Dataset /units/amplitude (VectorData) no description | shape = (2764,) | dtype = float64
  Dataset /units/amplitude_cutoff (VectorData) no description | shape = (2764,) | dtype = float64
  Dataset /units/cluster_id (VectorData) no description | shape = (2764,) | dtype = int64
  Dataset /units/cumulative_drift (VectorData) no description | shape = (2764,) | dtype = float64
  Dataset /units/d_prime (VectorData) no description | shape = (2764,) | dtype = float64
  Dataset /units/firing_rate (VectorData) no description | shape = (2764,) | dtype = float64
  Dataset /units/id (ElementIdentifiers)  | shape = (2764,) | dtype = int64
  Dataset /units/isi_violations (VectorData) no description | shape = (2764,) | dtype = float64
  Dataset /units/isolation_distance (VectorData) no description | shape = (2764,) | dtype = float64
  Dataset /units/l_ratio (VectorData) no description | shape = (2764,) | dtype = float64
  Dataset /units/local_index (VectorData) no description | shape = (2764,) | dtype = int64
  Dataset /units/max_drift (VectorData) no description | shape = (2764,) | dtype = float64
  Dataset /units/nn_hit_rate (VectorData) no description | shape = (2764,) | dtype = float64
  Dataset /units/nn_miss_rate (VectorData) no description | shape = (2764,) | dtype = float64
  Dataset /units/peak_channel_id (VectorData) no description | shape = (2764,) | dtype = int64
  Dataset /units/presence_ratio (VectorData) no description | shape = (2764,) | dtype = float64
  Dataset /units/quality (VectorData) no description | shape = (2764,) | dtype = object
  Dataset /units/recovery_slope (VectorData) no description | shape = (2764,) | dtype = float64
  Dataset /units/repolarization_slope (VectorData) no description | shape = (2764,) | dtype = float64
  Dataset /units/silhouette_score (VectorData) no description | shape = (2764,) | dtype = float64
  Dataset /units/snr (VectorData) no description | shape = (2764,) | dtype = float64
  Dataset /units/spike_amplitudes (VectorData) amplitude (s) of detected spiking events | shape = (82194349,) | dtype = float64
  Dataset /units/spike_amplitudes_index (VectorIndex) Index for VectorData 'spike_amplitudes' | shape = (2764,) | dtype = uint32
  Dataset /units/spike_times (VectorData) times (s) of detected spiking events | shape = (82194349,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (2764,) | dtype = uint32
  Dataset /units/spread (VectorData) no description | shape = (2764,) | dtype = float64
  Dataset /units/velocity_above (VectorData) no description | shape = (2764,) | dtype = float64
  Dataset /units/velocity_below (VectorData) no description | shape = (2764,) | dtype = float64
  Dataset /units/waveform_duration (VectorData) no description | shape = (2764,) | dtype = float64
  Dataset /units/waveform_halfwidth (VectorData) no description | shape = (2764,) | dtype = float64
  Dataset /units/waveform_mean (VectorData) mean waveforms on peak channels (over samples) | shape = (1061376, 82) | dtype = float64
  Dataset /units/waveform_mean_index (VectorIndex) Index for VectorData 'waveform_mean' | shape = (2764,) | dtype = uint32


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/EyeTracking (EllipseEyeTracking) 
  Group /acquisition/EyeTracking/corneal_reflection_tracking (EllipseSeries) no description
  Group /acquisition/EyeTracking/eye_tracking (EllipseSeries) no description
  Group /acquisition/EyeTracking/likely_blink (TimeSeries) blinks
  Group /acquisition/EyeTracking/pupil_tracking (EllipseSeries) no description
  Group /acquisition/raw_running_wheel_rotation (TimeSeries) no description
  Group /acquisition/running_wheel_signal_voltage (TimeSeries) no description
  Group /acquisition/running_wheel_supply_voltage (TimeSeries) no description
  file_create_date: ['2023-11-16T01:39:22.812106-08:00']
  Group /general/devices/probeA (EcephysProbe) Neuropixels 1.0 Probe
  Group /general/devices/probeB (EcephysProbe) Neuropixels 1.0 Probe
  Group /general/devices/probeE (EcephysProbe) Neuropixels 1.0 Probe
  Group /general/devices/probeF (EcephysProbe) Neuropixels 1.0 Probe
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering, including the filter name and frequency cutoffs | shape = (1536,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (1536,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (1536,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (1536,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the electrode, in ohms | shape = (1536,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/local_index (VectorData) The local index of electrode/channel on device | shape = (1536,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (1536,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/probe_horizontal_position (VectorData) Width-wise position of electrode/channel on device (microns) | shape = (1536,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/probe_id (VectorData) The unique id of this electrode's/channel's device | shape = (1536,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/probe_vertical_position (VectorData) Length-wise position of electrode/channel on device (microns) | shape = (1536,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/valid_data (VectorData) Whether data from this electrode/channel is usable | shape = (1536,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the position (+x is posterior) | shape = (1536,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the position (+y is inferior) | shape = (1536,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the position (+z is right) | shape = (1536,) | dtype = float64
  Group /general/extracellular_ephys/probeA (EcephysElectrodeGroup) Ecephys Electrode Group
  Group /general/extracellular_ephys/probeA/device (EcephysProbe) Neuropixels 1.0 Probe
  Group /general/extracellular_ephys/probeB (EcephysElectrodeGroup) Ecephys Electrode Group
  Group /general/extracellular_ephys/probeB/device (EcephysProbe) Neuropixels 1.0 Probe
  Group /general/extracellular_ephys/probeE (EcephysElectrodeGroup) Ecephys Electrode Group
  Group /general/extracellular_ephys/probeE/device (EcephysProbe) Neuropixels 1.0 Probe
  Group /general/extracellular_ephys/probeF (EcephysElectrodeGroup) Ecephys Electrode Group
  Group /general/extracellular_ephys/probeF/device (EcephysProbe) Neuropixels 1.0 Probe
  institution: Allen Institute
  session_id: 1298465622
  stimulus: OpenScopeVision2Hippocampus
  Group /general/subject (EcephysSpecimen) 
  identifier: 1298465622
  Group /intervals/Disco2SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations (TimeIntervals) Presentation times and stimuli details for 'Disco2SAC_Wd15_Vel2_Bndry1_Cntst0_loop' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/Disco2SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/Image (VectorData) No description | shape = (57600,) | dtype = float64
  Dataset /intervals/Disco2SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/color (VectorData) No description | shape = (57600,) | dtype = object
  Dataset /intervals/Disco2SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/contrast (VectorData) Contrast of stimulus | shape = (57600,) | dtype = float64
  Dataset /intervals/Disco2SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/id (ElementIdentifiers)  | shape = (57600,) | dtype = int64
  Dataset /intervals/Disco2SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/opacity (VectorData) Opacity of stimulus | shape = (57600,) | dtype = float64
  Dataset /intervals/Disco2SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/orientation (VectorData) Orientation of stimulus | shape = (57600,) | dtype = float64
  Dataset /intervals/Disco2SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (57600,) | dtype = object
  Dataset /intervals/Disco2SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (57600,) | dtype = float64
  Dataset /intervals/Disco2SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (57600,) | dtype = float64
  Dataset /intervals/Disco2SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (57600,) | dtype = float64
  Dataset /intervals/Disco2SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/stimulus_name (VectorData) Name of stimulus | shape = (57600,) | dtype = object
  Dataset /intervals/Disco2SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (57600,) | dtype = float64
  Dataset /intervals/Disco2SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/tags (VectorData) user-defined tags | shape = (57600,) | dtype = object
  Dataset /intervals/Disco2SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (57600,) | dtype = uint16
  Dataset /intervals/Disco2SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (57600,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/Disco2SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (57600,) | dtype = uint16
  Dataset /intervals/Disco2SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/units (VectorData) Units of stimulus size | shape = (57600,) | dtype = object
  Group /intervals/Disk_Wd15_Vel2_Bndry1_Cntst0_loop_presentations (TimeIntervals) Presentation times and stimuli details for 'Disk_Wd15_Vel2_Bndry1_Cntst0_loop' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/Disk_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/Image (VectorData) No description | shape = (28800,) | dtype = float64
  Dataset /intervals/Disk_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/color (VectorData) No description | shape = (28800,) | dtype = object
  Dataset /intervals/Disk_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/contrast (VectorData) Contrast of stimulus | shape = (28800,) | dtype = float64
  Dataset /intervals/Disk_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/id (ElementIdentifiers)  | shape = (28800,) | dtype = int64
  Dataset /intervals/Disk_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/opacity (VectorData) Opacity of stimulus | shape = (28800,) | dtype = float64
  Dataset /intervals/Disk_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/orientation (VectorData) Orientation of stimulus | shape = (28800,) | dtype = float64
  Dataset /intervals/Disk_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (28800,) | dtype = object
  Dataset /intervals/Disk_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (28800,) | dtype = float64
  Dataset /intervals/Disk_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (28800,) | dtype = float64
  Dataset /intervals/Disk_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (28800,) | dtype = float64
  Dataset /intervals/Disk_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/stimulus_name (VectorData) Name of stimulus | shape = (28800,) | dtype = object
  Dataset /intervals/Disk_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (28800,) | dtype = float64
  Dataset /intervals/Disk_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/tags (VectorData) user-defined tags | shape = (28800,) | dtype = object
  Dataset /intervals/Disk_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (28800,) | dtype = uint16
  Dataset /intervals/Disk_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (28800,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/Disk_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (28800,) | dtype = uint16
  Dataset /intervals/Disk_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/units (VectorData) Units of stimulus size | shape = (28800,) | dtype = object
  Group /intervals/GreenSAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations (TimeIntervals) Presentation times and stimuli details for 'GreenSAC_Wd15_Vel2_Bndry1_Cntst0_loop' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/GreenSAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/Image (VectorData) No description | shape = (28800,) | dtype = float64
  Dataset /intervals/GreenSAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/color (VectorData) No description | shape = (28800,) | dtype = object
  Dataset /intervals/GreenSAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/contrast (VectorData) Contrast of stimulus | shape = (28800,) | dtype = float64
  Dataset /intervals/GreenSAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/id (ElementIdentifiers)  | shape = (28800,) | dtype = int64
  Dataset /intervals/GreenSAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/opacity (VectorData) Opacity of stimulus | shape = (28800,) | dtype = float64
  Dataset /intervals/GreenSAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/orientation (VectorData) Orientation of stimulus | shape = (28800,) | dtype = float64
  Dataset /intervals/GreenSAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (28800,) | dtype = object
  Dataset /intervals/GreenSAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (28800,) | dtype = float64
  Dataset /intervals/GreenSAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (28800,) | dtype = float64
  Dataset /intervals/GreenSAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (28800,) | dtype = float64
  Dataset /intervals/GreenSAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/stimulus_name (VectorData) Name of stimulus | shape = (28800,) | dtype = object
  Dataset /intervals/GreenSAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (28800,) | dtype = float64
  Dataset /intervals/GreenSAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/tags (VectorData) user-defined tags | shape = (28800,) | dtype = object
  Dataset /intervals/GreenSAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (28800,) | dtype = uint16
  Dataset /intervals/GreenSAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (28800,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/GreenSAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (28800,) | dtype = uint16
  Dataset /intervals/GreenSAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/units (VectorData) Units of stimulus size | shape = (28800,) | dtype = object
  Group /intervals/Ring_Wd15_Vel2_Bndry1_Cntst0_loop_presentations (TimeIntervals) Presentation times and stimuli details for 'Ring_Wd15_Vel2_Bndry1_Cntst0_loop' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/Ring_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/Image (VectorData) No description | shape = (57600,) | dtype = float64
  Dataset /intervals/Ring_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/color (VectorData) No description | shape = (57600,) | dtype = object
  Dataset /intervals/Ring_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/contrast (VectorData) Contrast of stimulus | shape = (57600,) | dtype = float64
  Dataset /intervals/Ring_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/id (ElementIdentifiers)  | shape = (57600,) | dtype = int64
  Dataset /intervals/Ring_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/opacity (VectorData) Opacity of stimulus | shape = (57600,) | dtype = float64
  Dataset /intervals/Ring_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/orientation (VectorData) Orientation of stimulus | shape = (57600,) | dtype = float64
  Dataset /intervals/Ring_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (57600,) | dtype = object
  Dataset /intervals/Ring_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (57600,) | dtype = float64
  Dataset /intervals/Ring_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (57600,) | dtype = float64
  Dataset /intervals/Ring_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (57600,) | dtype = float64
  Dataset /intervals/Ring_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/stimulus_name (VectorData) Name of stimulus | shape = (57600,) | dtype = object
  Dataset /intervals/Ring_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (57600,) | dtype = float64
  Dataset /intervals/Ring_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/tags (VectorData) user-defined tags | shape = (57600,) | dtype = object
  Dataset /intervals/Ring_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (57600,) | dtype = uint16
  Dataset /intervals/Ring_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (57600,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/Ring_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (57600,) | dtype = uint16
  Dataset /intervals/Ring_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/units (VectorData) Units of stimulus size | shape = (57600,) | dtype = object
  Group /intervals/SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations (TimeIntervals) Presentation times and stimuli details for 'SAC_Wd15_Vel2_Bndry1_Cntst0_loop' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/Image (VectorData) No description | shape = (57600,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/color (VectorData) No description | shape = (57600,) | dtype = object
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/contrast (VectorData) Contrast of stimulus | shape = (57600,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/id (ElementIdentifiers)  | shape = (57600,) | dtype = int64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/opacity (VectorData) Opacity of stimulus | shape = (57600,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/orientation (VectorData) Orientation of stimulus | shape = (57600,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (57600,) | dtype = object
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (57600,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (57600,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (57600,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/stimulus_name (VectorData) Name of stimulus | shape = (57600,) | dtype = object
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (57600,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/tags (VectorData) user-defined tags | shape = (57600,) | dtype = object
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (57600,) | dtype = uint16
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (57600,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (57600,) | dtype = uint16
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/units (VectorData) Units of stimulus size | shape = (57600,) | dtype = object
  Group /intervals/SAC_Wd15_Vel2_Bndry1_Cntst1_loop_presentations (TimeIntervals) Presentation times and stimuli details for 'SAC_Wd15_Vel2_Bndry1_Cntst1_loop' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst1_loop_presentations/Image (VectorData) No description | shape = (28800,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst1_loop_presentations/color (VectorData) No description | shape = (28800,) | dtype = object
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst1_loop_presentations/contrast (VectorData) Contrast of stimulus | shape = (28800,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst1_loop_presentations/id (ElementIdentifiers)  | shape = (28800,) | dtype = int64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst1_loop_presentations/opacity (VectorData) Opacity of stimulus | shape = (28800,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst1_loop_presentations/orientation (VectorData) Orientation of stimulus | shape = (28800,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst1_loop_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (28800,) | dtype = object
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst1_loop_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (28800,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst1_loop_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (28800,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst1_loop_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (28800,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst1_loop_presentations/stimulus_name (VectorData) Name of stimulus | shape = (28800,) | dtype = object
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst1_loop_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (28800,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst1_loop_presentations/tags (VectorData) user-defined tags | shape = (28800,) | dtype = object
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst1_loop_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (28800,) | dtype = uint16
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst1_loop_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (28800,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst1_loop_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (28800,) | dtype = uint16
  Dataset /intervals/SAC_Wd15_Vel2_Bndry1_Cntst1_loop_presentations/units (VectorData) Units of stimulus size | shape = (28800,) | dtype = object
  Group /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_loop_presentations (TimeIntervals) Presentation times and stimuli details for 'SAC_Wd15_Vel2_Bndry2_Cntst0_loop' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_loop_presentations/Image (VectorData) No description | shape = (34080,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_loop_presentations/color (VectorData) No description | shape = (34080,) | dtype = object
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_loop_presentations/contrast (VectorData) Contrast of stimulus | shape = (34080,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_loop_presentations/id (ElementIdentifiers)  | shape = (34080,) | dtype = int64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_loop_presentations/opacity (VectorData) Opacity of stimulus | shape = (34080,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_loop_presentations/orientation (VectorData) Orientation of stimulus | shape = (34080,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_loop_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (34080,) | dtype = object
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_loop_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (34080,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_loop_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (34080,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_loop_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (34080,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_loop_presentations/stimulus_name (VectorData) Name of stimulus | shape = (34080,) | dtype = object
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_loop_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (34080,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_loop_presentations/tags (VectorData) user-defined tags | shape = (34080,) | dtype = object
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_loop_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (34080,) | dtype = uint16
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_loop_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (34080,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_loop_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (34080,) | dtype = uint16
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_loop_presentations/units (VectorData) Units of stimulus size | shape = (34080,) | dtype = object
  Group /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_oneway_presentations (TimeIntervals) Presentation times and stimuli details for 'SAC_Wd15_Vel2_Bndry2_Cntst0_oneway' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_oneway_presentations/Image (VectorData) No description | shape = (17040,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_oneway_presentations/color (VectorData) No description | shape = (17040,) | dtype = object
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_oneway_presentations/contrast (VectorData) Contrast of stimulus | shape = (17040,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_oneway_presentations/id (ElementIdentifiers)  | shape = (17040,) | dtype = int64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_oneway_presentations/opacity (VectorData) Opacity of stimulus | shape = (17040,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_oneway_presentations/orientation (VectorData) Orientation of stimulus | shape = (17040,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_oneway_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (17040,) | dtype = object
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_oneway_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (17040,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_oneway_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (17040,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_oneway_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (17040,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_oneway_presentations/stimulus_name (VectorData) Name of stimulus | shape = (17040,) | dtype = object
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_oneway_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (17040,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_oneway_presentations/tags (VectorData) user-defined tags | shape = (17040,) | dtype = object
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_oneway_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (17040,) | dtype = uint16
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_oneway_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (17040,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_oneway_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (17040,) | dtype = uint16
  Dataset /intervals/SAC_Wd15_Vel2_Bndry2_Cntst0_oneway_presentations/units (VectorData) Units of stimulus size | shape = (17040,) | dtype = object
  Group /intervals/SAC_Wd15_Vel2_Bndry3_Cntst0_loop_presentations (TimeIntervals) Presentation times and stimuli details for 'SAC_Wd15_Vel2_Bndry3_Cntst0_loop' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/SAC_Wd15_Vel2_Bndry3_Cntst0_loop_presentations/Image (VectorData) No description | shape = (44640,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry3_Cntst0_loop_presentations/color (VectorData) No description | shape = (44640,) | dtype = object
  Dataset /intervals/SAC_Wd15_Vel2_Bndry3_Cntst0_loop_presentations/contrast (VectorData) Contrast of stimulus | shape = (44640,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry3_Cntst0_loop_presentations/id (ElementIdentifiers)  | shape = (44640,) | dtype = int64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry3_Cntst0_loop_presentations/opacity (VectorData) Opacity of stimulus | shape = (44640,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry3_Cntst0_loop_presentations/orientation (VectorData) Orientation of stimulus | shape = (44640,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry3_Cntst0_loop_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (44640,) | dtype = object
  Dataset /intervals/SAC_Wd15_Vel2_Bndry3_Cntst0_loop_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (44640,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry3_Cntst0_loop_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (44640,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry3_Cntst0_loop_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (44640,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry3_Cntst0_loop_presentations/stimulus_name (VectorData) Name of stimulus | shape = (44640,) | dtype = object
  Dataset /intervals/SAC_Wd15_Vel2_Bndry3_Cntst0_loop_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (44640,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel2_Bndry3_Cntst0_loop_presentations/tags (VectorData) user-defined tags | shape = (44640,) | dtype = object
  Dataset /intervals/SAC_Wd15_Vel2_Bndry3_Cntst0_loop_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (44640,) | dtype = uint16
  Dataset /intervals/SAC_Wd15_Vel2_Bndry3_Cntst0_loop_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (44640,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/SAC_Wd15_Vel2_Bndry3_Cntst0_loop_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (44640,) | dtype = uint16
  Dataset /intervals/SAC_Wd15_Vel2_Bndry3_Cntst0_loop_presentations/units (VectorData) Units of stimulus size | shape = (44640,) | dtype = object
  Group /intervals/SAC_Wd15_Vel8_Bndry1_Cntst0_loop_presentations (TimeIntervals) Presentation times and stimuli details for 'SAC_Wd15_Vel8_Bndry1_Cntst0_loop' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/SAC_Wd15_Vel8_Bndry1_Cntst0_loop_presentations/Image (VectorData) No description | shape = (115200,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel8_Bndry1_Cntst0_loop_presentations/color (VectorData) No description | shape = (115200,) | dtype = object
  Dataset /intervals/SAC_Wd15_Vel8_Bndry1_Cntst0_loop_presentations/contrast (VectorData) Contrast of stimulus | shape = (115200,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel8_Bndry1_Cntst0_loop_presentations/id (ElementIdentifiers)  | shape = (115200,) | dtype = int64
  Dataset /intervals/SAC_Wd15_Vel8_Bndry1_Cntst0_loop_presentations/opacity (VectorData) Opacity of stimulus | shape = (115200,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel8_Bndry1_Cntst0_loop_presentations/orientation (VectorData) Orientation of stimulus | shape = (115200,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel8_Bndry1_Cntst0_loop_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (115200,) | dtype = object
  Dataset /intervals/SAC_Wd15_Vel8_Bndry1_Cntst0_loop_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (115200,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel8_Bndry1_Cntst0_loop_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (115200,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel8_Bndry1_Cntst0_loop_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (115200,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel8_Bndry1_Cntst0_loop_presentations/stimulus_name (VectorData) Name of stimulus | shape = (115200,) | dtype = object
  Dataset /intervals/SAC_Wd15_Vel8_Bndry1_Cntst0_loop_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (115200,) | dtype = float64
  Dataset /intervals/SAC_Wd15_Vel8_Bndry1_Cntst0_loop_presentations/tags (VectorData) user-defined tags | shape = (115200,) | dtype = object
  Dataset /intervals/SAC_Wd15_Vel8_Bndry1_Cntst0_loop_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (115200,) | dtype = uint32
  Dataset /intervals/SAC_Wd15_Vel8_Bndry1_Cntst0_loop_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (115200,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/SAC_Wd15_Vel8_Bndry1_Cntst0_loop_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (115200,) | dtype = uint32
  Dataset /intervals/SAC_Wd15_Vel8_Bndry1_Cntst0_loop_presentations/units (VectorData) Units of stimulus size | shape = (115200,) | dtype = object
  Group /intervals/SAC_Wd45_Vel2_Bndry1_Cntst0_loop_presentations (TimeIntervals) Presentation times and stimuli details for 'SAC_Wd45_Vel2_Bndry1_Cntst0_loop' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/SAC_Wd45_Vel2_Bndry1_Cntst0_loop_presentations/Image (VectorData) No description | shape = (28800,) | dtype = float64
  Dataset /intervals/SAC_Wd45_Vel2_Bndry1_Cntst0_loop_presentations/color (VectorData) No description | shape = (28800,) | dtype = object
  Dataset /intervals/SAC_Wd45_Vel2_Bndry1_Cntst0_loop_presentations/contrast (VectorData) Contrast of stimulus | shape = (28800,) | dtype = float64
  Dataset /intervals/SAC_Wd45_Vel2_Bndry1_Cntst0_loop_presentations/id (ElementIdentifiers)  | shape = (28800,) | dtype = int64
  Dataset /intervals/SAC_Wd45_Vel2_Bndry1_Cntst0_loop_presentations/opacity (VectorData) Opacity of stimulus | shape = (28800,) | dtype = float64
  Dataset /intervals/SAC_Wd45_Vel2_Bndry1_Cntst0_loop_presentations/orientation (VectorData) Orientation of stimulus | shape = (28800,) | dtype = float64
  Dataset /intervals/SAC_Wd45_Vel2_Bndry1_Cntst0_loop_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (28800,) | dtype = object
  Dataset /intervals/SAC_Wd45_Vel2_Bndry1_Cntst0_loop_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (28800,) | dtype = float64
  Dataset /intervals/SAC_Wd45_Vel2_Bndry1_Cntst0_loop_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (28800,) | dtype = float64
  Dataset /intervals/SAC_Wd45_Vel2_Bndry1_Cntst0_loop_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (28800,) | dtype = float64
  Dataset /intervals/SAC_Wd45_Vel2_Bndry1_Cntst0_loop_presentations/stimulus_name (VectorData) Name of stimulus | shape = (28800,) | dtype = object
  Dataset /intervals/SAC_Wd45_Vel2_Bndry1_Cntst0_loop_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (28800,) | dtype = float64
  Dataset /intervals/SAC_Wd45_Vel2_Bndry1_Cntst0_loop_presentations/tags (VectorData) user-defined tags | shape = (28800,) | dtype = object
  Dataset /intervals/SAC_Wd45_Vel2_Bndry1_Cntst0_loop_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (28800,) | dtype = uint16
  Dataset /intervals/SAC_Wd45_Vel2_Bndry1_Cntst0_loop_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (28800,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/SAC_Wd45_Vel2_Bndry1_Cntst0_loop_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (28800,) | dtype = uint16
  Dataset /intervals/SAC_Wd45_Vel2_Bndry1_Cntst0_loop_presentations/units (VectorData) Units of stimulus size | shape = (28800,) | dtype = object
  Group /intervals/UD_Wd15_Vel2_Bndry1_Cntst0_loop_presentations (TimeIntervals) Presentation times and stimuli details for 'UD_Wd15_Vel2_Bndry1_Cntst0_loop' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/UD_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/Image (VectorData) No description | shape = (57600,) | dtype = float64
  Dataset /intervals/UD_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/color (VectorData) No description | shape = (57600,) | dtype = object
  Dataset /intervals/UD_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/contrast (VectorData) Contrast of stimulus | shape = (57600,) | dtype = float64
  Dataset /intervals/UD_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/id (ElementIdentifiers)  | shape = (57600,) | dtype = int64
  Dataset /intervals/UD_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/opacity (VectorData) Opacity of stimulus | shape = (57600,) | dtype = float64
  Dataset /intervals/UD_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/orientation (VectorData) Orientation of stimulus | shape = (57600,) | dtype = float64
  Dataset /intervals/UD_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (57600,) | dtype = object
  Dataset /intervals/UD_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (57600,) | dtype = float64
  Dataset /intervals/UD_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (57600,) | dtype = float64
  Dataset /intervals/UD_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (57600,) | dtype = float64
  Dataset /intervals/UD_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/stimulus_name (VectorData) Name of stimulus | shape = (57600,) | dtype = object
  Dataset /intervals/UD_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (57600,) | dtype = float64
  Dataset /intervals/UD_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/tags (VectorData) user-defined tags | shape = (57600,) | dtype = object
  Dataset /intervals/UD_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (57600,) | dtype = uint16
  Dataset /intervals/UD_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (57600,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/UD_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (57600,) | dtype = uint16
  Dataset /intervals/UD_Wd15_Vel2_Bndry1_Cntst0_loop_presentations/units (VectorData) Units of stimulus size | shape = (57600,) | dtype = object
  Group /intervals/acurl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations (TimeIntervals) Presentation times and stimuli details for 'acurl_Wd15_Vel2_Bndry1_Cntst0_oneway' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/acurl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/Image (VectorData) No description | shape = (14400,) | dtype = float64
  Dataset /intervals/acurl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/color (VectorData) No description | shape = (14400,) | dtype = object
  Dataset /intervals/acurl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/contrast (VectorData) Contrast of stimulus | shape = (14400,) | dtype = float64
  Dataset /intervals/acurl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/id (ElementIdentifiers)  | shape = (14400,) | dtype = int64
  Dataset /intervals/acurl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/opacity (VectorData) Opacity of stimulus | shape = (14400,) | dtype = float64
  Dataset /intervals/acurl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/orientation (VectorData) Orientation of stimulus | shape = (14400,) | dtype = float64
  Dataset /intervals/acurl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (14400,) | dtype = object
  Dataset /intervals/acurl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (14400,) | dtype = float64
  Dataset /intervals/acurl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (14400,) | dtype = float64
  Dataset /intervals/acurl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (14400,) | dtype = float64
  Dataset /intervals/acurl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/stimulus_name (VectorData) Name of stimulus | shape = (14400,) | dtype = object
  Dataset /intervals/acurl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (14400,) | dtype = float64
  Dataset /intervals/acurl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/tags (VectorData) user-defined tags | shape = (14400,) | dtype = object
  Dataset /intervals/acurl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (14400,) | dtype = uint16
  Dataset /intervals/acurl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (14400,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/acurl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (14400,) | dtype = uint16
  Dataset /intervals/acurl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/units (VectorData) Units of stimulus size | shape = (14400,) | dtype = object
  Group /intervals/curl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations (TimeIntervals) Presentation times and stimuli details for 'curl_Wd15_Vel2_Bndry1_Cntst0_oneway' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/curl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/Image (VectorData) No description | shape = (14400,) | dtype = float64
  Dataset /intervals/curl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/color (VectorData) No description | shape = (14400,) | dtype = object
  Dataset /intervals/curl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/contrast (VectorData) Contrast of stimulus | shape = (14400,) | dtype = float64
  Dataset /intervals/curl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/id (ElementIdentifiers)  | shape = (14400,) | dtype = int64
  Dataset /intervals/curl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/opacity (VectorData) Opacity of stimulus | shape = (14400,) | dtype = float64
  Dataset /intervals/curl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/orientation (VectorData) Orientation of stimulus | shape = (14400,) | dtype = float64
  Dataset /intervals/curl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (14400,) | dtype = object
  Dataset /intervals/curl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (14400,) | dtype = float64
  Dataset /intervals/curl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (14400,) | dtype = float64
  Dataset /intervals/curl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (14400,) | dtype = float64
  Dataset /intervals/curl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/stimulus_name (VectorData) Name of stimulus | shape = (14400,) | dtype = object
  Dataset /intervals/curl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (14400,) | dtype = float64
  Dataset /intervals/curl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/tags (VectorData) user-defined tags | shape = (14400,) | dtype = object
  Dataset /intervals/curl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (14400,) | dtype = uint16
  Dataset /intervals/curl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (14400,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/curl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (14400,) | dtype = uint16
  Dataset /intervals/curl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations/units (VectorData) Units of stimulus size | shape = (14400,) | dtype = object
  Group /intervals/invalid_times (TimeIntervals) experimental intervals
  Dataset /intervals/invalid_times/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /intervals/invalid_times/start_time (VectorData) Start time of epoch, in seconds | shape = (1,) | dtype = float64
  Dataset /intervals/invalid_times/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1,) | dtype = float64
  Dataset /intervals/invalid_times/tags (VectorData) user-defined tags | shape = (3,) | dtype = object
  Dataset /intervals/invalid_times/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (1,) | dtype = uint8
  Group /intervals/natmovie_CricketsOnARock_540x960Full_584x460Active_presentations (TimeIntervals) Presentation times and stimuli details for 'natmovie_CricketsOnARock_540x960Full_584x460Active' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/natmovie_CricketsOnARock_540x960Full_584x460Active_presentations/Image (VectorData) No description | shape = (28800,) | dtype = float64
  Dataset /intervals/natmovie_CricketsOnARock_540x960Full_584x460Active_presentations/color (VectorData) No description | shape = (28800,) | dtype = object
  Dataset /intervals/natmovie_CricketsOnARock_540x960Full_584x460Active_presentations/contrast (VectorData) Contrast of stimulus | shape = (28800,) | dtype = float64
  Dataset /intervals/natmovie_CricketsOnARock_540x960Full_584x460Active_presentations/id (ElementIdentifiers)  | shape = (28800,) | dtype = int64
  Dataset /intervals/natmovie_CricketsOnARock_540x960Full_584x460Active_presentations/opacity (VectorData) Opacity of stimulus | shape = (28800,) | dtype = float64
  Dataset /intervals/natmovie_CricketsOnARock_540x960Full_584x460Active_presentations/orientation (VectorData) Orientation of stimulus | shape = (28800,) | dtype = float64
  Dataset /intervals/natmovie_CricketsOnARock_540x960Full_584x460Active_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (28800,) | dtype = object
  Dataset /intervals/natmovie_CricketsOnARock_540x960Full_584x460Active_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (28800,) | dtype = float64
  Dataset /intervals/natmovie_CricketsOnARock_540x960Full_584x460Active_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (28800,) | dtype = float64
  Dataset /intervals/natmovie_CricketsOnARock_540x960Full_584x460Active_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (28800,) | dtype = float64
  Dataset /intervals/natmovie_CricketsOnARock_540x960Full_584x460Active_presentations/stimulus_name (VectorData) Name of stimulus | shape = (28800,) | dtype = object
  Dataset /intervals/natmovie_CricketsOnARock_540x960Full_584x460Active_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (28800,) | dtype = float64
  Dataset /intervals/natmovie_CricketsOnARock_540x960Full_584x460Active_presentations/tags (VectorData) user-defined tags | shape = (28800,) | dtype = object
  Dataset /intervals/natmovie_CricketsOnARock_540x960Full_584x460Active_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (28800,) | dtype = uint16
  Dataset /intervals/natmovie_CricketsOnARock_540x960Full_584x460Active_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (28800,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/natmovie_CricketsOnARock_540x960Full_584x460Active_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (28800,) | dtype = uint16
  Dataset /intervals/natmovie_CricketsOnARock_540x960Full_584x460Active_presentations/units (VectorData) Units of stimulus size | shape = (28800,) | dtype = object
  Group /intervals/natmovie_EagleSwooping1_540x960Full_584x460Active_presentations (TimeIntervals) Presentation times and stimuli details for 'natmovie_EagleSwooping1_540x960Full_584x460Active' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/natmovie_EagleSwooping1_540x960Full_584x460Active_presentations/Image (VectorData) No description | shape = (28800,) | dtype = float64
  Dataset /intervals/natmovie_EagleSwooping1_540x960Full_584x460Active_presentations/color (VectorData) No description | shape = (28800,) | dtype = object
  Dataset /intervals/natmovie_EagleSwooping1_540x960Full_584x460Active_presentations/contrast (VectorData) Contrast of stimulus | shape = (28800,) | dtype = float64
  Dataset /intervals/natmovie_EagleSwooping1_540x960Full_584x460Active_presentations/id (ElementIdentifiers)  | shape = (28800,) | dtype = int64
  Dataset /intervals/natmovie_EagleSwooping1_540x960Full_584x460Active_presentations/opacity (VectorData) Opacity of stimulus | shape = (28800,) | dtype = float64
  Dataset /intervals/natmovie_EagleSwooping1_540x960Full_584x460Active_presentations/orientation (VectorData) Orientation of stimulus | shape = (28800,) | dtype = float64
  Dataset /intervals/natmovie_EagleSwooping1_540x960Full_584x460Active_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (28800,) | dtype = object
  Dataset /intervals/natmovie_EagleSwooping1_540x960Full_584x460Active_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (28800,) | dtype = float64
  Dataset /intervals/natmovie_EagleSwooping1_540x960Full_584x460Active_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (28800,) | dtype = float64
  Dataset /intervals/natmovie_EagleSwooping1_540x960Full_584x460Active_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (28800,) | dtype = float64
  Dataset /intervals/natmovie_EagleSwooping1_540x960Full_584x460Active_presentations/stimulus_name (VectorData) Name of stimulus | shape = (28800,) | dtype = object
  Dataset /intervals/natmovie_EagleSwooping1_540x960Full_584x460Active_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (28800,) | dtype = float64
  Dataset /intervals/natmovie_EagleSwooping1_540x960Full_584x460Active_presentations/tags (VectorData) user-defined tags | shape = (28800,) | dtype = object
  Dataset /intervals/natmovie_EagleSwooping1_540x960Full_584x460Active_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (28800,) | dtype = uint16
  Dataset /intervals/natmovie_EagleSwooping1_540x960Full_584x460Active_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (28800,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/natmovie_EagleSwooping1_540x960Full_584x460Active_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (28800,) | dtype = uint16
  Dataset /intervals/natmovie_EagleSwooping1_540x960Full_584x460Active_presentations/units (VectorData) Units of stimulus size | shape = (28800,) | dtype = object
  Group /intervals/natmovie_EagleSwooping2_540x960Full_584x460Active_presentations (TimeIntervals) Presentation times and stimuli details for 'natmovie_EagleSwooping2_540x960Full_584x460Active' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/natmovie_EagleSwooping2_540x960Full_584x460Active_presentations/Image (VectorData) No description | shape = (28800,) | dtype = float64
  Dataset /intervals/natmovie_EagleSwooping2_540x960Full_584x460Active_presentations/color (VectorData) No description | shape = (28800,) | dtype = object
  Dataset /intervals/natmovie_EagleSwooping2_540x960Full_584x460Active_presentations/contrast (VectorData) Contrast of stimulus | shape = (28800,) | dtype = float64
  Dataset /intervals/natmovie_EagleSwooping2_540x960Full_584x460Active_presentations/id (ElementIdentifiers)  | shape = (28800,) | dtype = int64
  Dataset /intervals/natmovie_EagleSwooping2_540x960Full_584x460Active_presentations/opacity (VectorData) Opacity of stimulus | shape = (28800,) | dtype = float64
  Dataset /intervals/natmovie_EagleSwooping2_540x960Full_584x460Active_presentations/orientation (VectorData) Orientation of stimulus | shape = (28800,) | dtype = float64
  Dataset /intervals/natmovie_EagleSwooping2_540x960Full_584x460Active_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (28800,) | dtype = object
  Dataset /intervals/natmovie_EagleSwooping2_540x960Full_584x460Active_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (28800,) | dtype = float64
  Dataset /intervals/natmovie_EagleSwooping2_540x960Full_584x460Active_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (28800,) | dtype = float64
  Dataset /intervals/natmovie_EagleSwooping2_540x960Full_584x460Active_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (28800,) | dtype = float64
  Dataset /intervals/natmovie_EagleSwooping2_540x960Full_584x460Active_presentations/stimulus_name (VectorData) Name of stimulus | shape = (28800,) | dtype = object
  Dataset /intervals/natmovie_EagleSwooping2_540x960Full_584x460Active_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (28800,) | dtype = float64
  Dataset /intervals/natmovie_EagleSwooping2_540x960Full_584x460Active_presentations/tags (VectorData) user-defined tags | shape = (28800,) | dtype = object
  Dataset /intervals/natmovie_EagleSwooping2_540x960Full_584x460Active_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (28800,) | dtype = uint16
  Dataset /intervals/natmovie_EagleSwooping2_540x960Full_584x460Active_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (28800,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/natmovie_EagleSwooping2_540x960Full_584x460Active_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (28800,) | dtype = uint16
  Dataset /intervals/natmovie_EagleSwooping2_540x960Full_584x460Active_presentations/units (VectorData) Units of stimulus size | shape = (28800,) | dtype = object
  Group /intervals/natmovie_SnakeOnARoad_540x960Full_584x460Active_presentations (TimeIntervals) Presentation times and stimuli details for 'natmovie_SnakeOnARoad_540x960Full_584x460Active' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/natmovie_SnakeOnARoad_540x960Full_584x460Active_presentations/Image (VectorData) No description | shape = (28800,) | dtype = float64
  Dataset /intervals/natmovie_SnakeOnARoad_540x960Full_584x460Active_presentations/color (VectorData) No description | shape = (28800,) | dtype = object
  Dataset /intervals/natmovie_SnakeOnARoad_540x960Full_584x460Active_presentations/contrast (VectorData) Contrast of stimulus | shape = (28800,) | dtype = float64
  Dataset /intervals/natmovie_SnakeOnARoad_540x960Full_584x460Active_presentations/id (ElementIdentifiers)  | shape = (28800,) | dtype = int64
  Dataset /intervals/natmovie_SnakeOnARoad_540x960Full_584x460Active_presentations/opacity (VectorData) Opacity of stimulus | shape = (28800,) | dtype = float64
  Dataset /intervals/natmovie_SnakeOnARoad_540x960Full_584x460Active_presentations/orientation (VectorData) Orientation of stimulus | shape = (28800,) | dtype = float64
  Dataset /intervals/natmovie_SnakeOnARoad_540x960Full_584x460Active_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (28800,) | dtype = object
  Dataset /intervals/natmovie_SnakeOnARoad_540x960Full_584x460Active_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (28800,) | dtype = float64
  Dataset /intervals/natmovie_SnakeOnARoad_540x960Full_584x460Active_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (28800,) | dtype = float64
  Dataset /intervals/natmovie_SnakeOnARoad_540x960Full_584x460Active_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (28800,) | dtype = float64
  Dataset /intervals/natmovie_SnakeOnARoad_540x960Full_584x460Active_presentations/stimulus_name (VectorData) Name of stimulus | shape = (28800,) | dtype = object
  Dataset /intervals/natmovie_SnakeOnARoad_540x960Full_584x460Active_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (28800,) | dtype = float64
  Dataset /intervals/natmovie_SnakeOnARoad_540x960Full_584x460Active_presentations/tags (VectorData) user-defined tags | shape = (28800,) | dtype = object
  Dataset /intervals/natmovie_SnakeOnARoad_540x960Full_584x460Active_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (28800,) | dtype = uint16
  Dataset /intervals/natmovie_SnakeOnARoad_540x960Full_584x460Active_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (28800,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/natmovie_SnakeOnARoad_540x960Full_584x460Active_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (28800,) | dtype = uint16
  Dataset /intervals/natmovie_SnakeOnARoad_540x960Full_584x460Active_presentations/units (VectorData) Units of stimulus size | shape = (28800,) | dtype = object
  Group /intervals/natmovie_Squirreland3Mice_540x960Full_584x460Active_presentations (TimeIntervals) Presentation times and stimuli details for 'natmovie_Squirreland3Mice_540x960Full_584x460Active' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/natmovie_Squirreland3Mice_540x960Full_584x460Active_presentations/Image (VectorData) No description | shape = (28800,) | dtype = float64
  Dataset /intervals/natmovie_Squirreland3Mice_540x960Full_584x460Active_presentations/color (VectorData) No description | shape = (28800,) | dtype = object
  Dataset /intervals/natmovie_Squirreland3Mice_540x960Full_584x460Active_presentations/contrast (VectorData) Contrast of stimulus | shape = (28800,) | dtype = float64
  Dataset /intervals/natmovie_Squirreland3Mice_540x960Full_584x460Active_presentations/id (ElementIdentifiers)  | shape = (28800,) | dtype = int64
  Dataset /intervals/natmovie_Squirreland3Mice_540x960Full_584x460Active_presentations/opacity (VectorData) Opacity of stimulus | shape = (28800,) | dtype = float64
  Dataset /intervals/natmovie_Squirreland3Mice_540x960Full_584x460Active_presentations/orientation (VectorData) Orientation of stimulus | shape = (28800,) | dtype = float64
  Dataset /intervals/natmovie_Squirreland3Mice_540x960Full_584x460Active_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (28800,) | dtype = object
  Dataset /intervals/natmovie_Squirreland3Mice_540x960Full_584x460Active_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (28800,) | dtype = float64
  Dataset /intervals/natmovie_Squirreland3Mice_540x960Full_584x460Active_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (28800,) | dtype = float64
  Dataset /intervals/natmovie_Squirreland3Mice_540x960Full_584x460Active_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (28800,) | dtype = float64
  Dataset /intervals/natmovie_Squirreland3Mice_540x960Full_584x460Active_presentations/stimulus_name (VectorData) Name of stimulus | shape = (28800,) | dtype = object
  Dataset /intervals/natmovie_Squirreland3Mice_540x960Full_584x460Active_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (28800,) | dtype = float64
  Dataset /intervals/natmovie_Squirreland3Mice_540x960Full_584x460Active_presentations/tags (VectorData) user-defined tags | shape = (28800,) | dtype = object
  Dataset /intervals/natmovie_Squirreland3Mice_540x960Full_584x460Active_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (28800,) | dtype = uint16
  Dataset /intervals/natmovie_Squirreland3Mice_540x960Full_584x460Active_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (28800,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/natmovie_Squirreland3Mice_540x960Full_584x460Active_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (28800,) | dtype = uint16
  Dataset /intervals/natmovie_Squirreland3Mice_540x960Full_584x460Active_presentations/units (VectorData) Units of stimulus size | shape = (28800,) | dtype = object
  Group /intervals/receptive_field_block_presentations (TimeIntervals) Presentation times and stimuli details for 'receptive_field_block' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/receptive_field_block_presentations/Pos_x (VectorData) No description | shape = (7680,) | dtype = float64
  Dataset /intervals/receptive_field_block_presentations/Pos_y (VectorData) No description | shape = (7680,) | dtype = float64
  Dataset /intervals/receptive_field_block_presentations/SF (VectorData) No description | shape = (7680,) | dtype = float64
  Dataset /intervals/receptive_field_block_presentations/TF (VectorData) No description | shape = (7680,) | dtype = float64
  Dataset /intervals/receptive_field_block_presentations/color (VectorData) No description | shape = (7680,) | dtype = object
  Dataset /intervals/receptive_field_block_presentations/contrast (VectorData) Contrast of stimulus | shape = (7680,) | dtype = float64
  Dataset /intervals/receptive_field_block_presentations/id (ElementIdentifiers)  | shape = (7680,) | dtype = int64
  Dataset /intervals/receptive_field_block_presentations/mask (VectorData) Shape of mask applied to stimulus | shape = (7680,) | dtype = object
  Dataset /intervals/receptive_field_block_presentations/opacity (VectorData) Opacity of stimulus | shape = (7680,) | dtype = float64
  Dataset /intervals/receptive_field_block_presentations/orientation (VectorData) Orientation of stimulus | shape = (7680,) | dtype = float64
  Dataset /intervals/receptive_field_block_presentations/phase (VectorData) Phase of grating stimulus | shape = (7680,) | dtype = object
  Dataset /intervals/receptive_field_block_presentations/size (VectorData) Size of stimulus (see ‘units’ field for units) | shape = (7680,) | dtype = object
  Dataset /intervals/receptive_field_block_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (7680,) | dtype = float64
  Dataset /intervals/receptive_field_block_presentations/stimulus_block (VectorData) Index of contiguous presentations of one stimulus type | shape = (7680,) | dtype = float64
  Dataset /intervals/receptive_field_block_presentations/stimulus_index (VectorData) Index of stimulus type | shape = (7680,) | dtype = float64
  Dataset /intervals/receptive_field_block_presentations/stimulus_name (VectorData) Name of stimulus | shape = (7680,) | dtype = object
  Dataset /intervals/receptive_field_block_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (7680,) | dtype = float64
  Dataset /intervals/receptive_field_block_presentations/tags (VectorData) user-defined tags | shape = (7680,) | dtype = object
  Dataset /intervals/receptive_field_block_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (7680,) | dtype = uint16
  Dataset /intervals/receptive_field_block_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (7680,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/receptive_field_block_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (7680,) | dtype = uint16
  Dataset /intervals/receptive_field_block_presentations/units (VectorData) Units of stimulus size | shape = (7680,) | dtype = object
  Group /intervals/spontaneous_presentations (TimeIntervals) Presentation times and stimuli details for 'spontaneous' stimuli. 
  Note: image_name references control_description in stimulus/templates
  Dataset /intervals/spontaneous_presentations/id (ElementIdentifiers)  | shape = (21,) | dtype = int64
  Dataset /intervals/spontaneous_presentations/start_time (VectorData) Start time of epoch, in seconds | shape = (21,) | dtype = float64
  Dataset /intervals/spontaneous_presentations/stimulus_name (VectorData) Name of stimulus | shape = (21,) | dtype = object
  Dataset /intervals/spontaneous_presentations/stop_time (VectorData) Stop time of epoch, in seconds | shape = (21,) | dtype = float64
  Dataset /intervals/spontaneous_presentations/tags (VectorData) user-defined tags | shape = (21,) | dtype = object
  Dataset /intervals/spontaneous_presentations/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (21,) | dtype = uint8
  Dataset /intervals/spontaneous_presentations/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (21,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/spontaneous_presentations/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (21,) | dtype = uint8
  Group /processing/running (ProcessingModule) running speed data
  Group /processing/running/running_speed (TimeSeries) no description
  Group /processing/running/running_speed_end_times (TimeSeries) no description
  Group /processing/running/running_wheel_rotation (TimeSeries) no description
  Group /processing/stimulus (ProcessingModule) Stimulus Times processing
  Group /processing/stimulus/timestamps (TimeSeries) no description
  session_description: Data and metadata for an Ecephys session
  session_start_time: 2023-09-21T00:00:00-07:00
  Group /stimulus/templates/Disco2SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations (ImageSeries) no description
  Group /stimulus/templates/Disk_Wd15_Vel2_Bndry1_Cntst0_loop_presentations (ImageSeries) no description
  Group /stimulus/templates/GreenSAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations (ImageSeries) no description
  Group /stimulus/templates/Ring_Wd15_Vel2_Bndry1_Cntst0_loop_presentations (ImageSeries) no description
  Group /stimulus/templates/SAC_Wd15_Vel2_Bndry1_Cntst0_loop_presentations (ImageSeries) no description
  Group /stimulus/templates/SAC_Wd15_Vel2_Bndry1_Cntst1_loop_presentations (ImageSeries) no description
  Group /stimulus/templates/SAC_Wd15_Vel2_Bndry2_Cntst0_loop_presentations (ImageSeries) no description
  Group /stimulus/templates/SAC_Wd15_Vel2_Bndry2_Cntst0_oneway_presentations (ImageSeries) no description
  Group /stimulus/templates/SAC_Wd15_Vel2_Bndry3_Cntst0_loop_presentations (ImageSeries) no description
  Group /stimulus/templates/SAC_Wd15_Vel8_Bndry1_Cntst0_loop_presentations (ImageSeries) no description
  Group /stimulus/templates/SAC_Wd45_Vel2_Bndry1_Cntst0_loop_presentations (ImageSeries) no description
  Group /stimulus/templates/UD_Wd15_Vel2_Bndry1_Cntst0_loop_presentations (ImageSeries) no description
  Group /stimulus/templates/acurl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations (ImageSeries) no description
  Group /stimulus/templates/curl_Wd15_Vel2_Bndry1_Cntst0_oneway_presentations (ImageSeries) no description
  Group /stimulus/templates/natmovie_CricketsOnARock_540x960Full_584x460Active_presentations (ImageSeries) no description
  Group /stimulus/templates/natmovie_EagleSwooping1_540x960Full_584x460Active_presentations (ImageSeries) no description
  Group /stimulus/templates/natmovie_EagleSwooping2_540x960Full_584x460Active_presentations (ImageSeries) no description
  Group /stimulus/templates/natmovie_SnakeOnARoad_540x960Full_584x460Active_presentations (ImageSeries) no description
  Group /stimulus/templates/natmovie_Squirreland3Mice_540x960Full_584x460Active_presentations (ImageSeries) no description
  timestamps_reference_time: 2023-09-21T00:00:00-07:00
  Group /units (Units) 
  Dataset /units/PT_ratio (VectorData) no description | shape = (2764,) | dtype = float64
  Dataset /units/amplitude (VectorData) no description | shape = (2764,) | dtype = float64
  Dataset /units/amplitude_cutoff (VectorData) no description | shape = (2764,) | dtype = float64
  Dataset /units/cluster_id (VectorData) no description | shape = (2764,) | dtype = int64
  Dataset /units/cumulative_drift (VectorData) no description | shape = (2764,) | dtype = float64
  Dataset /units/d_prime (VectorData) no description | shape = (2764,) | dtype = float64
  Dataset /units/firing_rate (VectorData) no description | shape = (2764,) | dtype = float64
  Dataset /units/id (ElementIdentifiers)  | shape = (2764,) | dtype = int64
  Dataset /units/isi_violations (VectorData) no description | shape = (2764,) | dtype = float64
  Dataset /units/isolation_distance (VectorData) no description | shape = (2764,) | dtype = float64
  Dataset /units/l_ratio (VectorData) no description | shape = (2764,) | dtype = float64
  Dataset /units/local_index (VectorData) no description | shape = (2764,) | dtype = int64
  Dataset /units/max_drift (VectorData) no description | shape = (2764,) | dtype = float64
  Dataset /units/nn_hit_rate (VectorData) no description | shape = (2764,) | dtype = float64
  Dataset /units/nn_miss_rate (VectorData) no description | shape = (2764,) | dtype = float64
  Dataset /units/peak_channel_id (VectorData) no description | shape = (2764,) | dtype = int64
  Dataset /units/presence_ratio (VectorData) no description | shape = (2764,) | dtype = float64
  Dataset /units/quality (VectorData) no description | shape = (2764,) | dtype = object
  Dataset /units/recovery_slope (VectorData) no description | shape = (2764,) | dtype = float64
  Dataset /units/repolarization_slope (VectorData) no description | shape = (2764,) | dtype = float64
  Dataset /units/silhouette_score (VectorData) no description | shape = (2764,) | dtype = float64
  Dataset /units/snr (VectorData) no description | shape = (2764,) | dtype = float64
  Dataset /units/spike_amplitudes (VectorData) amplitude (s) of detected spiking events | shape = (82194349,) | dtype = float64
  Dataset /units/spike_amplitudes_index (VectorIndex) Index for VectorData 'spike_amplitudes' | shape = (2764,) | dtype = uint32
  Dataset /units/spike_times (VectorData) times (s) of detected spiking events | shape = (82194349,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (2764,) | dtype = uint32
  Dataset /units/spread (VectorData) no description | shape = (2764,) | dtype = float64
  Dataset /units/velocity_above (VectorData) no description | shape = (2764,) | dtype = float64
  Dataset /units/velocity_below (VectorData) no description | shape = (2764,) | dtype = float64
  Dataset /units/waveform_duration (VectorData) no description | shape = (2764,) | dtype = float64
  Dataset /units/waveform_halfwidth (VectorData) no description | shape = (2764,) | dtype = float64
  Dataset /units/waveform_mean (VectorData) mean waveforms on peak channels (over samples) | shape = (1061376, 82) | dtype = float64
  Dataset /units/waveform_mean_index (VectorIndex) Index for VectorData 'waveform_mean' | shape = (2764,) | dtype = uint32


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/probe_0_lfp (LFP) 
  Group /acquisition/probe_0_lfp/probe_0_lfp_data (ElectricalSeries) no description
  Dataset /acquisition/probe_0_lfp/probe_0_lfp_data/electrodes (DynamicTableRegion) lfp channels on probe 0 | shape = (95,) | dtype = int64
  Group /acquisition/probe_0_lfp_data (ElectricalSeries) no description
  Dataset /acquisition/probe_0_lfp_data/electrodes (DynamicTableRegion) lfp channels on probe 0 | shape = (95,) | dtype = int64
  file_create_date: ['2025-02-25T16:39:27.896345-08:00']
  Group /general/devices/probeA (EcephysProbe) Neuropixels 1.0 Probe
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering, including the filter name and frequency cutoffs | shape = (95,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (95,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (95,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (95,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the electrode, in ohms | shape = (95,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/local_index (VectorData) The local index of electrode/channel on device | shape = (95,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (95,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/probe_horizontal_position (VectorData) Width-wise position of electrode/channel on device (microns) | shape = (95,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/probe_id (VectorData) The unique id of this electrode's/channel's device | shape = (95,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/probe_vertical_position (VectorData) Length-wise position of electrode/channel on device (microns) | shape = (95,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/valid_data (VectorData) Whether data from this electrode/channel is usable | shape = (95,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the position (+x is posterior) | shape = (95,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the position (+y is inferior) | shape = (95,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the position (+z is right) | shape = (95,) | dtype = float64
  Group /general/extracellular_ephys/probeA (EcephysElectrodeGroup) Ecephys Electrode Group
  Group /general/extracellular_ephys/probeA/device (EcephysProbe) Neuropixels 1.0 Probe
  institution: Allen Institute for Brain Science
  session_id: 1298465622
  stimulus: OpenScopeVision2Hippocampus
  Group /general/subject (EcephysSpecimen) 
  identifier: 0
  session_description: LFP data and associated info for one probe
  session_start_time: 2023-09-21T00:00:00-07:00
  timestamps_reference_time: 2023-09-21T00:00:00-07:00


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/probe_1_lfp (LFP) 
  Group /acquisition/probe_1_lfp/probe_1_lfp_data (ElectricalSeries) no description
  Dataset /acquisition/probe_1_lfp/probe_1_lfp_data/electrodes (DynamicTableRegion) lfp channels on probe 1 | shape = (73,) | dtype = int64
  Group /acquisition/probe_1_lfp_data (ElectricalSeries) no description
  Dataset /acquisition/probe_1_lfp_data/electrodes (DynamicTableRegion) lfp channels on probe 1 | shape = (73,) | dtype = int64
  file_create_date: ['2025-02-25T16:39:27.898747-08:00']
  Group /general/devices/probeB (EcephysProbe) Neuropixels 1.0 Probe
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
  Group /general/extracellular_ephys/probeB (EcephysElectrodeGroup) Ecephys Electrode Group
  Group /general/extracellular_ephys/probeB/device (EcephysProbe) Neuropixels 1.0 Probe
  institution: Allen Institute for Brain Science
  session_id: 1298465622
  stimulus: OpenScopeVision2Hippocampus
  Group /general/subject (EcephysSpecimen) 
  identifier: 1
  session_description: LFP data and associated info for one probe
  session_start_time: 2023-09-21T00:00:00-07:00
  timestamps_reference_time: 2023-09-21T00:00:00-07:00


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  Group /acquisition/probe_2_lfp (LFP) 
  Group /acquisition/probe_2_lfp/probe_2_lfp_data (ElectricalSeries) no description
  Dataset /acquisition/probe_2_lfp/probe_2_lfp_data/electrodes (DynamicTableRegion) lfp channels on probe 2 | shape = (87,) | dtype = int64
  Group /acquisition/probe_2_lfp_data (ElectricalSeries) no description
  Dataset /acquisition/probe_2_lfp_data/electrodes (DynamicTableRegion) lfp channels on probe 2 | shape = (87,) | dtype = int64
  file_create_date: ['2025-02-25T16:39:27.898461-08:00']
  Group /general/devices/probeE (EcephysProbe) Neuropixels 1.0 Probe
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering, including the filter name and frequency cutoffs | shape = (87,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (87,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (87,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (87,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the electrode, in ohms | shape = (87,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/local_index (VectorData) The local index of electrode/channel on device | shape = (87,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (87,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/probe_horizontal_position (VectorData) Width-wise position of electrode/channel on device (microns) | shape = (87,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/probe_id (VectorData) The unique id of this electrode's/channel's device | shape = (87,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/probe_vertical_position (VectorData) Length-wise position of electrode/channel on device (microns) | shape = (87,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/valid_data (VectorData) Whether data from this electrode/channel is usable | shape = (87,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the position (+x is posterior) | shape = (87,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the position (+y is inferior) | shape = (87,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the position (+z is right) | shape = (87,) | dtype = float64
  Group /general/extracellular_ephys/probeE (EcephysElectrodeGroup) Ecephys Electrode Group
  Group /general/extracellular_ephys/probeE/device (EcephysProbe) Neuropixels 1.0 Probe
  institution: Allen Institute for Brain Science
  session_id: 1298465622
  stimulus: OpenScopeVision2Hippocampus
  Group /general/subject (EcephysSpecimen) 
  identifier: 2
  session_description: LFP data and associated info for one probe
  session_start_time: 2023-09-21T00:00:00-07:00
  timestamps_reference_time: 2023-09-21T00:00:00-07:00
