
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001371/draft
name: New information triggers prospective codes to adapt for flexible navigation
contributor: [{'name': 'Prince, Stephanie', 'email': 'stephprince16@gmail.com', 'roleName': ['dcite:ContactPerson', 'dcite:Author', 'dcite:DataCollector', 'dcite:Conceptualization', 'dcite:FormalAnalysis', 'dcite:DataCurator'], 'schemaKey': 'Person', 'identifier': '0000-0002-3083-6955', 'affiliation': [], 'includeInCitation': True}, {'name': 'Cushing, Danielle Sarah', 'roleName': ['dcite:Author', 'dcite:FormalAnalysis'], 'schemaKey': 'Person', 'identifier': '0000-0003-3730-8220', 'includeInCitation': True}, {'name': 'Yassine, Teema', 'roleName': ['dcite:Author', 'dcite:DataCollector', 'dcite:DataCurator'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Katragadda, Navya', 'roleName': ['dcite:Author', 'dcite:DataCollector'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Roberts, Tyler', 'roleName': ['dcite:Author', 'dcite:DataCollector'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Singer, Annabelle', 'email': 'asinger@gatech.edu', 'roleName': ['dcite:Author', 'dcite:ContactPerson', 'dcite:Conceptualization', 'dcite:FundingAcquisition', 'dcite:Supervision'], 'schemaKey': 'Person', 'identifier': '0000-0001-6003-0488', 'includeInCitation': True}, {'name': 'National Science Foundation', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/021nxhr62', 'awardNumber': 'DGE-1444932', 'includeInCitation': False}, {'name': 'National Institute of Neurological Disorders and Stroke ', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01s5ya894', 'awardNumber': 'NS109226', 'includeInCitation': False}, {'name': 'National Institute of Neurological Disorders and Stroke', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01s5ya894', 'awardNumber': 'T32NS096050-22', 'includeInCitation': False}, {'name': 'National Institute of Aging', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/049v75w11', 'awardNumber': 'RF1AG078736-01', 'includeInCitation': False}]
description: This dataset includes the electrophysiological and behavioral data from hippocampal CA1 and medial prefrontal cortex in mice performing a virtual reality spatial navigation task. Data are described in Prince et al., 2025, “New information triggers prospective codes to adapt for flexible navigation”, Nature Communications. Head-fixed mice were trained to perform a memory-based decision-making task in virtual reality (the 'update task'). In this y-maze task, animals were required to navigate between two possible paths using visual cues. On most trials, the first original cue indicated the final reward location and was followed by a delay period during which mice had to maintain the memory of the correct goal arm. However on a subset of trials, a second visual cue appeared when mice reached a specific location after a shortened delay period. During the second cue, the visual patterns appeared on the opposite wall from the original cue indicating that the reward location switched from the initial arm, and animals must switch from their initial decision maintained in memory to the opposite choice. After several phases of behavioral training, electrophysiological data was recorded from hippocampal CA1 and medial prefrontal cortex (mPFC) during the task.
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}, {'name': 'behavioral approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 14536769171479, 'numberOfFiles': 66, 'numberOfSubjects': 7, 'variableMeasured': ['SpatialSeries', 'Units', 'ProcessingModule', 'BehavioralEvents', 'LFP', 'CompassDirection', 'DecompositionSeries', 'ElectricalSeries', 'Position', 'ElectrodeGroup'], 'measurementTechnique': [{'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'fourier analysis technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'signal filtering technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 001371 has 66 NWB files.
5 of these NWB files are of type 1.
61 of these NWB files are of type 2.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/licks (TimeSeries) signal from photointerrupter circuit, values of 5V indicate the mouse tongue is has broken through the laser beam, values of 0V indicate baseline
  Group /acquisition/raw_ecephys (ElectricalSeries) Raw unfiltered data acquired with spikegadgets acquisition system
  Dataset /acquisition/raw_ecephys/electrodes (DynamicTableRegion) neuronexus_probes | shape = (128,) | dtype = int64
  Group /acquisition/rotational_velocity (TimeSeries) movement of the spherical treadmill along the roll axis as measured by an optical gaming mouse and filtered through a lab view function, maximum values of -10 and 10V
  Group /acquisition/translational_velocity (TimeSeries) movement of the spherical treadmill along the pitch axis as measured by an optical gaming mouse and filtered through a lab view function, maximum values of -10 and 10V
  file_create_date: ['2025-05-08T00:01:26.970015-04:00']
  Group /general/devices/spikegadgets_ecu (Device) Analog and digital inputs of SpikeGadgets system. Max -10 to 10V for analog channels.
  Group /general/devices/spikegadgets_mcu (Device) Two NeuroNexus silicon probes with 2 (shanks) x 32 (channels) on each probe were inserted into hippocampal CA1 and medial prefrontal cortex. Probes were 64-chan, poly5 Takahashi probe formats. Electrophysiological data were acquired using a SpikeGadgets MCU system digitized with 30 kHz rate. Analog and digital channels were acquired using the SpikeGadgets ECU system.
  experiment_description: Head-fixed mice were trained to perform a memory-based decision-making task in virtual reality (the 'update task'). In this y-maze task, animals were required to navigate between two possible paths using visual cues. On most trials, the first original cue indicated the final reward location and was followed by a delay period. However on a subset of trials, a second visual cue appeared when mice reached a specific location after a shortened delay period, and animals had to update their initial choice. After several phases of behavioral training, electrophysiological data was recorded from hippocampal CA1 and medial prefrontal cortex (mPFC) during the task.
  experimenter: ['Prince, Stephanie']
  Group /general/extracellular_ephys/analog_inputs (ElectrodeGroup) analog inputs to SpikeGadgets system. Channel IDs are unique to the project and task.
  Group /general/extracellular_ephys/analog_inputs/device (Device) Analog and digital inputs of SpikeGadgets system. Max -10 to 10V for analog channels.
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering, including the filter name and frequency cutoffs | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/hardware_channel (VectorData) channel ID from hardware wiring, used as folder names for singer lab preprocessed mat data | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/reference (VectorData) Description of the reference electrode and/or reference scheme used for this                         electrode, e.g.,"stainless steel skull screw" or "online common average referencing". | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/rel_x (VectorData) the x coordinate within the electrode group | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_y (VectorData) the y coordinate within the electrode group | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_z (VectorData) the z coordinate within the electrode group | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/ripple_channel (VectorData) channel with the largest mean power in the ripple band, used as channel for detecting | shape = (128,) | dtype = float64
  Group /general/extracellular_ephys/probe0 (ElectrodeGroup) probe0 of NeuroNexus probes.  Channels 0-31 belong to shank 1 and channels 32-64 belong to shank 2
  Group /general/extracellular_ephys/probe0/device (Device) Two NeuroNexus silicon probes with 2 (shanks) x 32 (channels) on each probe were inserted into hippocampal CA1 and medial prefrontal cortex. Probes were 64-chan, poly5 Takahashi probe formats. Electrophysiological data were acquired using a SpikeGadgets MCU system digitized with 30 kHz rate. Analog and digital channels were acquired using the SpikeGadgets ECU system.
  Group /general/extracellular_ephys/probe1 (ElectrodeGroup) probe1 of NeuroNexus probes.  Channels 0-31 belong to shank 1 and channels 32-64 belong to shank 2
  Group /general/extracellular_ephys/probe1/device (Device) Two NeuroNexus silicon probes with 2 (shanks) x 32 (channels) on each probe were inserted into hippocampal CA1 and medial prefrontal cortex. Probes were 64-chan, poly5 Takahashi probe formats. Electrophysiological data were acquired using a SpikeGadgets MCU system digitized with 30 kHz rate. Analog and digital channels were acquired using the SpikeGadgets ECU system.
  institution: Georgia Institute of Technology
  keywords: ['memory' 'spatial navigation' 'decision-making']
  lab: Singer
  session_id: S20_210517
  source_script: File created with git repo https://github.com/stephprince/singer-lab-to-nwb/tree/42fd8e172e
  Group /general/subject (Subject) 
  identifier: ae7f7056-2349-4216-9d4c-1f87a743033f
  Group /intervals/behavior_epochs (TimeIntervals) Indicates the start and stop times in which behavior data was both collected AND synchronized to ephys data.
  Dataset /intervals/behavior_epochs/id (ElementIdentifiers)  | shape = (2,) | dtype = int64
  Dataset /intervals/behavior_epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (2,) | dtype = float64
  Dataset /intervals/behavior_epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (2,) | dtype = float64
  Group /intervals/delay (TimeIntervals) indicates whether the delay cue is on or not, from spikegadgets digital signals
  Dataset /intervals/delay/id (ElementIdentifiers)  | shape = (156,) | dtype = int64
  Dataset /intervals/delay/start_time (VectorData) Start time of epoch, in seconds | shape = (156,) | dtype = float64
  Dataset /intervals/delay/stop_time (VectorData) Stop time of epoch, in seconds | shape = (156,) | dtype = float64
  Group /intervals/recording_epochs (TimeIntervals) During one recording session, the acquisition is stopped and restarted for switching behavioral periods, refilling with saline, etc. Electrophysiological files are stitched together and these epochs indicate the start and stop times within a recording session. These epochs are NOT continuous and there is a short interval of approx 1-5 min between them.
  Dataset /intervals/recording_epochs/behavior_task (VectorData) indicates whether VR task was displayed on the screen (1), or if the screen was left covered/blank as a baseline period (0) | shape = (3,) | dtype = int64
  Dataset /intervals/recording_epochs/id (ElementIdentifiers)  | shape = (3,) | dtype = int64
  Dataset /intervals/recording_epochs/recording_number (VectorData) what the original recording file number this epoch was (as saved in theraw spikegadgets and .mat file names), 1-based indexing | shape = (3,) | dtype = object
  Dataset /intervals/recording_epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (3,) | dtype = float64
  Dataset /intervals/recording_epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (3,) | dtype = float64
  Group /intervals/sync (TimeIntervals) synchronizing pulse sent from virmen software, from spikegadgets digital signals
  Dataset /intervals/sync/id (ElementIdentifiers)  | shape = (95064,) | dtype = int64
  Dataset /intervals/sync/start_time (VectorData) Start time of epoch, in seconds | shape = (95064,) | dtype = float64
  Dataset /intervals/sync/stop_time (VectorData) Stop time of epoch, in seconds | shape = (95064,) | dtype = float64
  Group /intervals/trial (TimeIntervals) indicates when trial is occurring vs inter trial, from spikegadgets digital signals
  Dataset /intervals/trial/id (ElementIdentifiers)  | shape = (139,) | dtype = int64
  Dataset /intervals/trial/start_time (VectorData) Start time of epoch, in seconds | shape = (139,) | dtype = float64
  Dataset /intervals/trial/stop_time (VectorData) Stop time of epoch, in seconds | shape = (139,) | dtype = float64
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/choice (VectorData) choice animal made | shape = (137,) | dtype = int64
  Dataset /intervals/trials/correct (VectorData) whether trial was correct or not | shape = (137,) | dtype = float64
  Dataset /intervals/trials/delay2_location (VectorData) y-position on track where delay 2 occurred | shape = (137,) | dtype = float64
  Dataset /intervals/trials/delay_location (VectorData) y-position on track where delay occurred | shape = (137,) | dtype = float64
  Dataset /intervals/trials/duration (VectorData) duration in seconds | shape = (137,) | dtype = float64
  Dataset /intervals/trials/i_choice_made (VectorData) index when choice made | shape = (137,) | dtype = int64
  Dataset /intervals/trials/i_delay (VectorData) index when delay started | shape = (137,) | dtype = float64
  Dataset /intervals/trials/i_delay2 (VectorData) index when second delay started | shape = (137,) | dtype = float64
  Dataset /intervals/trials/i_update (VectorData) index when update started | shape = (137,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (137,) | dtype = int64
  Dataset /intervals/trials/iterations (VectorData) number of samples/vr frames | shape = (137,) | dtype = int64
  Dataset /intervals/trials/maze_id (VectorData) {'linear': 1, 'ymaze_short': 2, 'ymaze_long': 3, 'ymaze_delay': 4} | shape = (137,) | dtype = int64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (137,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (137,) | dtype = float64
  Dataset /intervals/trials/t_choice_made (VectorData) time when choice made | shape = (137,) | dtype = float64
  Dataset /intervals/trials/t_delay (VectorData) time when delay started | shape = (137,) | dtype = float64
  Dataset /intervals/trials/t_delay2 (VectorData) time when second delay started | shape = (137,) | dtype = float64
  Dataset /intervals/trials/t_update (VectorData) time when update started | shape = (137,) | dtype = float64
  Dataset /intervals/trials/turn_type (VectorData) {'right': 1, 'left': 2} | shape = (137,) | dtype = int64
  Dataset /intervals/trials/update_location (VectorData) y-position on track where update occurred | shape = (137,) | dtype = float64
  Dataset /intervals/trials/update_type (VectorData) {'nan': 1, 'switch': 2, 'stay': 3} | shape = (137,) | dtype = int64
  Group /intervals/update (TimeIntervals) indicates when the update cue is on or not, from spikegadgets digital signals
  Dataset /intervals/update/id (ElementIdentifiers)  | shape = (31,) | dtype = int64
  Dataset /intervals/update/start_time (VectorData) Start time of epoch, in seconds | shape = (31,) | dtype = float64
  Dataset /intervals/update/stop_time (VectorData) Stop time of epoch, in seconds | shape = (31,) | dtype = float64
  Group /processing/behavior (ProcessingModule) contains processed behavioral data
  Group /processing/behavior/licks (BehavioralEvents) 
  Group /processing/behavior/licks/licks (TimeSeries) licking events detected by photointerrupter
  Group /processing/behavior/position (Position) 
  Group /processing/behavior/position/position (SpatialSeries) the x and y position values for the mouse in the virtual-reality environment. X is the first column and Y is the second
  Group /processing/behavior/rewards (BehavioralEvents) 
  Group /processing/behavior/rewards/rewards (TimeSeries) reward delivery times
  Group /processing/behavior/rotational_velocity (TimeSeries) sideways velocity in the virtual reality environment. The roll axis as tracked by the optical mouse.
  Group /processing/behavior/time (TimeSeries) time recorded by virmen software since session state time
  Group /processing/behavior/translational_velocity (TimeSeries) forward and backwards velocity in the virtual reality environment. The pitch axis as tracked by the optical mouse.
  Group /processing/behavior/view_angle (CompassDirection) 
  Group /processing/behavior/view_angle/view_angle (SpatialSeries) direction of mouse in the virtual reality environment
  Group /processing/ecephys (ProcessingModule) contains processed extracellular electrophysiology data
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/LFP (ElectricalSeries) local field potential data generated by singer lab preprocessing pipeline - eeg data
  Dataset /processing/ecephys/LFP/LFP/electrodes (DynamicTableRegion) neuronexus_probes | shape = (128,) | dtype = int64
  Group /processing/ecephys/decomposition_amplitude (DecompositionSeries) filtered ephys amplitude data generated by singer lab preprocessing pipeline
  delta eeg data filtered through: 1 - 4 Hz Delta FIR Equiripple Filter 1 Hz sidebands, 40 dB rolloff
  theta eeg data filtered through: 4 - 12 Hz FIR equiripple theta filter 1 Hz sidebands 50 dB roll off
  beta eeg data filtered through: 12 - 30 Hz Beta FIR Equiripple Filter 1 Hz sidebands, 40 dB rolloff
  lowgamma eeg data filtered through: 20-50Hz bandpass FIR equiripple filter 5Hz sidebands. 60dB roll-off
  ripple eeg data filtered through: 150-250Hz bandpass FIR equiripple filter 10Hz sidebands, 40dB roll-off resampled to 2000 from 1500 sr filter
  Group /processing/ecephys/decomposition_amplitude/bands (DynamicTable) data about the frequency bands that the signal was decomposed into
  Dataset /processing/ecephys/decomposition_amplitude/bands/band_limits (VectorData) low and high frequencies of bandpass filter in Hz | shape = (5, 2) | dtype = float64
  Dataset /processing/ecephys/decomposition_amplitude/bands/band_name (VectorData) the name of the frequency band (recommended: 'alpha', 'beta', 'gamma', 'delta', 'high gamma' | shape = (5,) | dtype = object
  Dataset /processing/ecephys/decomposition_amplitude/bands/id (ElementIdentifiers)  | shape = (5,) | dtype = int64
  Group /processing/ecephys/decomposition_amplitude/source_timeseries (ElectricalSeries) local field potential data generated by singer lab preprocessing pipeline - eeg data
  Dataset /processing/ecephys/decomposition_amplitude/source_timeseries/electrodes (DynamicTableRegion) neuronexus_probes | shape = (128,) | dtype = int64
  Group /processing/ecephys/decomposition_envelope (DecompositionSeries) filtered ephys envelope data generated by singer lab preprocessing pipeline
  delta eeg data filtered through: 1 - 4 Hz Delta FIR Equiripple Filter 1 Hz sidebands, 40 dB rolloff
  theta eeg data filtered through: 4 - 12 Hz FIR equiripple theta filter 1 Hz sidebands 50 dB roll off
  beta eeg data filtered through: 12 - 30 Hz Beta FIR Equiripple Filter 1 Hz sidebands, 40 dB rolloff
  lowgamma eeg data filtered through: 20-50Hz bandpass FIR equiripple filter 5Hz sidebands. 60dB roll-off
  ripple eeg data filtered through: 150-250Hz bandpass FIR equiripple filter 10Hz sidebands, 40dB roll-off resampled to 2000 from 1500 sr filter
  Group /processing/ecephys/decomposition_envelope/bands (DynamicTable) data about the frequency bands that the signal was decomposed into
  Dataset /processing/ecephys/decomposition_envelope/bands/band_limits (VectorData) low and high frequencies of bandpass filter in Hz | shape = (5, 2) | dtype = float64
  Dataset /processing/ecephys/decomposition_envelope/bands/band_name (VectorData) the name of the frequency band (recommended: 'alpha', 'beta', 'gamma', 'delta', 'high gamma' | shape = (5,) | dtype = object
  Dataset /processing/ecephys/decomposition_envelope/bands/id (ElementIdentifiers)  | shape = (5,) | dtype = int64
  Group /processing/ecephys/decomposition_envelope/source_timeseries (ElectricalSeries) local field potential data generated by singer lab preprocessing pipeline - eeg data
  Dataset /processing/ecephys/decomposition_envelope/source_timeseries/electrodes (DynamicTableRegion) neuronexus_probes | shape = (128,) | dtype = int64
  Group /processing/ecephys/decomposition_phase (DecompositionSeries) filtered ephys phase data generated by singer lab preprocessing pipeline
  delta eeg data filtered through: 1 - 4 Hz Delta FIR Equiripple Filter 1 Hz sidebands, 40 dB rolloff
  theta eeg data filtered through: 4 - 12 Hz FIR equiripple theta filter 1 Hz sidebands 50 dB roll off
  beta eeg data filtered through: 12 - 30 Hz Beta FIR Equiripple Filter 1 Hz sidebands, 40 dB rolloff
  lowgamma eeg data filtered through: 20-50Hz bandpass FIR equiripple filter 5Hz sidebands. 60dB roll-off
  ripple eeg data filtered through: 150-250Hz bandpass FIR equiripple filter 10Hz sidebands, 40dB roll-off resampled to 2000 from 1500 sr filter
  Group /processing/ecephys/decomposition_phase/bands (DynamicTable) data about the frequency bands that the signal was decomposed into
  Dataset /processing/ecephys/decomposition_phase/bands/band_limits (VectorData) low and high frequencies of bandpass filter in Hz | shape = (5, 2) | dtype = float64
  Dataset /processing/ecephys/decomposition_phase/bands/band_name (VectorData) the name of the frequency band (recommended: 'alpha', 'beta', 'gamma', 'delta', 'high gamma' | shape = (5,) | dtype = object
  Dataset /processing/ecephys/decomposition_phase/bands/id (ElementIdentifiers)  | shape = (5,) | dtype = int64
  Group /processing/ecephys/decomposition_phase/source_timeseries (ElectricalSeries) local field potential data generated by singer lab preprocessing pipeline - eeg data
  Dataset /processing/ecephys/decomposition_phase/source_timeseries/electrodes (DynamicTableRegion) neuronexus_probes | shape = (128,) | dtype = int64
  Group /processing/ecephys/nonthetas (TimeIntervals) events identified from filtered lfp signals
  Dataset /processing/ecephys/nonthetas/baseline (VectorData) baseline value for event detection | shape = (154,) | dtype = float64
  Dataset /processing/ecephys/nonthetas/energy (VectorData) total sum squared energy of the waveform | shape = (154,) | dtype = float64
  Dataset /processing/ecephys/nonthetas/excluded (VectorData) any post-event detection exclusion criteria applied | shape = (154,) | dtype = float64
  Dataset /processing/ecephys/nonthetas/id (ElementIdentifiers)  | shape = (154,) | dtype = int64
  Dataset /processing/ecephys/nonthetas/max_thresh (VectorData) the largest threshold in stdev units at which this ripple would be detected | shape = (154,) | dtype = float64
  Dataset /processing/ecephys/nonthetas/mid_ind (VectorData) index of middle time in lfp timeseries | shape = (154,) | dtype = float64
  Dataset /processing/ecephys/nonthetas/mid_time (VectorData) middle of lfp event | shape = (154,) | dtype = float64
  Dataset /processing/ecephys/nonthetas/min_duration (VectorData) time (in seconds) signal must be above threshold for event detection | shape = (154,) | dtype = float64
  Dataset /processing/ecephys/nonthetas/peak (VectorData) peak height/energy of the waveform | shape = (154,) | dtype = float64
  Dataset /processing/ecephys/nonthetas/start_ind (VectorData) index of start time in lfp timeseries | shape = (154,) | dtype = float64
  Dataset /processing/ecephys/nonthetas/start_time (VectorData) Start time of epoch, in seconds | shape = (154,) | dtype = float64
  Dataset /processing/ecephys/nonthetas/std (VectorData) standard deviation value used to generate threshold value | shape = (154,) | dtype = float64
  Dataset /processing/ecephys/nonthetas/stop_ind (VectorData) index of stop time in lfp timeseries | shape = (154,) | dtype = float64
  Dataset /processing/ecephys/nonthetas/stop_time (VectorData) Stop time of epoch, in seconds | shape = (154,) | dtype = float64
  Dataset /processing/ecephys/nonthetas/threshold (VectorData) baseline value with X number of std above the mean for event detection | shape = (154,) | dtype = float64
  Group /processing/ecephys/ripples (TimeIntervals) events identified from filtered lfp signals
  Dataset /processing/ecephys/ripples/baseline (VectorData) baseline value for event detection | shape = (8,) | dtype = float64
  Dataset /processing/ecephys/ripples/energy (VectorData) total sum squared energy of the waveform | shape = (8,) | dtype = float64
  Dataset /processing/ecephys/ripples/excluded (VectorData) any post-event detection exclusion criteria applied | shape = (8,) | dtype = float64
  Dataset /processing/ecephys/ripples/id (ElementIdentifiers)  | shape = (8,) | dtype = int64
  Dataset /processing/ecephys/ripples/max_thresh (VectorData) the largest threshold in stdev units at which this ripple would be detected | shape = (8,) | dtype = float64
  Dataset /processing/ecephys/ripples/mid_ind (VectorData) index of middle time in lfp timeseries | shape = (8,) | dtype = float64
  Dataset /processing/ecephys/ripples/mid_time (VectorData) middle of lfp event | shape = (8,) | dtype = float64
  Dataset /processing/ecephys/ripples/min_duration (VectorData) time (in seconds) signal must be above threshold for event detection | shape = (8,) | dtype = float64
  Dataset /processing/ecephys/ripples/peak (VectorData) peak height/energy of the waveform | shape = (8,) | dtype = float64
  Dataset /processing/ecephys/ripples/start_ind (VectorData) index of start time in lfp timeseries | shape = (8,) | dtype = float64
  Dataset /processing/ecephys/ripples/start_time (VectorData) Start time of epoch, in seconds | shape = (8,) | dtype = float64
  Dataset /processing/ecephys/ripples/std (VectorData) standard deviation value used to generate threshold value | shape = (8,) | dtype = float64
  Dataset /processing/ecephys/ripples/stop_ind (VectorData) index of stop time in lfp timeseries | shape = (8,) | dtype = float64
  Dataset /processing/ecephys/ripples/stop_time (VectorData) Stop time of epoch, in seconds | shape = (8,) | dtype = float64
  Dataset /processing/ecephys/ripples/threshold (VectorData) baseline value with X number of std above the mean for event detection | shape = (8,) | dtype = float64
  Group /processing/ecephys/thetas (TimeIntervals) events identified from filtered lfp signals
  Dataset /processing/ecephys/thetas/baseline (VectorData) baseline value for event detection | shape = (47,) | dtype = float64
  Dataset /processing/ecephys/thetas/energy (VectorData) total sum squared energy of the waveform | shape = (47,) | dtype = float64
  Dataset /processing/ecephys/thetas/excluded (VectorData) any post-event detection exclusion criteria applied | shape = (47,) | dtype = float64
  Dataset /processing/ecephys/thetas/id (ElementIdentifiers)  | shape = (47,) | dtype = int64
  Dataset /processing/ecephys/thetas/max_thresh (VectorData) the largest threshold in stdev units at which this ripple would be detected | shape = (47,) | dtype = float64
  Dataset /processing/ecephys/thetas/mid_ind (VectorData) index of middle time in lfp timeseries | shape = (47,) | dtype = float64
  Dataset /processing/ecephys/thetas/mid_time (VectorData) middle of lfp event | shape = (47,) | dtype = float64
  Dataset /processing/ecephys/thetas/min_duration (VectorData) time (in seconds) signal must be above threshold for event detection | shape = (47,) | dtype = float64
  Dataset /processing/ecephys/thetas/peak (VectorData) peak height/energy of the waveform | shape = (47,) | dtype = float64
  Dataset /processing/ecephys/thetas/start_ind (VectorData) index of start time in lfp timeseries | shape = (47,) | dtype = float64
  Dataset /processing/ecephys/thetas/start_time (VectorData) Start time of epoch, in seconds | shape = (47,) | dtype = float64
  Dataset /processing/ecephys/thetas/std (VectorData) standard deviation value used to generate threshold value | shape = (47,) | dtype = float64
  Dataset /processing/ecephys/thetas/stop_ind (VectorData) index of stop time in lfp timeseries | shape = (47,) | dtype = float64
  Dataset /processing/ecephys/thetas/stop_time (VectorData) Stop time of epoch, in seconds | shape = (47,) | dtype = float64
  Dataset /processing/ecephys/thetas/threshold (VectorData) baseline value with X number of std above the mean for event detection | shape = (47,) | dtype = float64
  session_description: Electrophysiological recording session of mice performing the update task
  session_start_time: 2021-05-17T14:41:05.809433-04:00
  timestamps_reference_time: 2021-05-17T14:41:05.809433-04:00
  Group /units (Units) Autogenerated by nwb_conversion_tools.
  Dataset /units/Amplitude (VectorData) amplitude imported from phy | shape = (138,) | dtype = float64
  Dataset /units/ContamPct (VectorData) contampct imported from phy | shape = (138,) | dtype = float64
  Dataset /units/KSLabel (VectorData) auto-label (pre phy curation) | shape = (138,) | dtype = object
  Dataset /units/amp (VectorData) amplitude imported from phy | shape = (138,) | dtype = float64
  Dataset /units/ch (VectorData) channel number impoted from phy | shape = (138,) | dtype = float64
  Dataset /units/depth (VectorData) depth imported from phy | shape = (138,) | dtype = float64
  Dataset /units/fr (VectorData) firing rate imported from phy | shape = (138,) | dtype = float64
  Dataset /units/id (ElementIdentifiers)  | shape = (138,) | dtype = int64
  Dataset /units/n_spikes (VectorData) number of spikes imported from phy | shape = (138,) | dtype = float64
  Dataset /units/original_cluster_id (VectorData) original cluster id imported from phy | shape = (138,) | dtype = float64
  Dataset /units/quality (VectorData) manual-label (post phy curation) | shape = (138,) | dtype = object
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (3985213,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (138,) | dtype = uint32
  Dataset /units/unit_name (VectorData) Unique reference for each unit. | shape = (138,) | dtype = object


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/licks (TimeSeries) signal from photointerrupter circuit, values of 5V indicate the mouse tongue is has broken through the laser beam, values of 0V indicate baseline
  Group /acquisition/raw_ecephys (ElectricalSeries) Raw unfiltered data acquired with spikegadgets acquisition system
  Dataset /acquisition/raw_ecephys/electrodes (DynamicTableRegion) neuronexus_probes | shape = (128,) | dtype = int64
  Group /acquisition/rotational_velocity (TimeSeries) movement of the spherical treadmill along the roll axis as measured by an optical gaming mouse and filtered through a lab view function, maximum values of -10 and 10V
  Group /acquisition/translational_velocity (TimeSeries) movement of the spherical treadmill along the pitch axis as measured by an optical gaming mouse and filtered through a lab view function, maximum values of -10 and 10V
  file_create_date: ['2025-04-11T03:50:24.749090-04:00']
  Group /general/devices/spikegadgets_ecu (Device) Analog and digital inputs of SpikeGadgets system. Max -10 to 10V for analog channels.
  Group /general/devices/spikegadgets_mcu (Device) Two NeuroNexus silicon probes with 2 (shanks) x 32 (channels) on each probe were inserted into hippocampal CA1 and medial prefrontal cortex. Probes were 64-chan, poly5 Takahashi probe formats. Electrophysiological data were acquired using a SpikeGadgets MCU system digitized with 30 kHz rate. Analog and digital channels were acquired using the SpikeGadgets ECU system.
  experiment_description: Head-fixed mice were trained to perform a memory-based decision-making task in virtual reality (the 'update task'). In this y-maze task, animals were required to navigate between two possible paths using visual cues. On most trials, the first original cue indicated the final reward location and was followed by a delay period. However on a subset of trials, a second visual cue appeared when mice reached a specific location after a shortened delay period, and animals had to update their initial choice. After several phases of behavioral training, electrophysiological data was recorded from hippocampal CA1 and medial prefrontal cortex (mPFC) during the task.
  experimenter: ['Prince, Stephanie']
  Group /general/extracellular_ephys/analog_inputs (ElectrodeGroup) analog inputs to SpikeGadgets system. Channel IDs are unique to the project and task.
  Group /general/extracellular_ephys/analog_inputs/device (Device) Analog and digital inputs of SpikeGadgets system. Max -10 to 10V for analog channels.
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering, including the filter name and frequency cutoffs | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/hardware_channel (VectorData) channel ID from hardware wiring, used as folder names for singer lab preprocessed mat data | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/reference (VectorData) Description of the reference electrode and/or reference scheme used for this                         electrode, e.g.,"stainless steel skull screw" or "online common average referencing". | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/rel_x (VectorData) the x coordinate within the electrode group | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_y (VectorData) the y coordinate within the electrode group | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_z (VectorData) the z coordinate within the electrode group | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/ripple_channel (VectorData) channel with the largest mean power in the ripple band, used as channel for detecting | shape = (128,) | dtype = float64
  Group /general/extracellular_ephys/probe0 (ElectrodeGroup) probe0 of NeuroNexus probes.  Channels 0-31 belong to shank 1 and channels 32-64 belong to shank 2
  Group /general/extracellular_ephys/probe0/device (Device) Two NeuroNexus silicon probes with 2 (shanks) x 32 (channels) on each probe were inserted into hippocampal CA1 and medial prefrontal cortex. Probes were 64-chan, poly5 Takahashi probe formats. Electrophysiological data were acquired using a SpikeGadgets MCU system digitized with 30 kHz rate. Analog and digital channels were acquired using the SpikeGadgets ECU system.
  Group /general/extracellular_ephys/probe1 (ElectrodeGroup) probe1 of NeuroNexus probes.  Channels 0-31 belong to shank 1 and channels 32-64 belong to shank 2
  Group /general/extracellular_ephys/probe1/device (Device) Two NeuroNexus silicon probes with 2 (shanks) x 32 (channels) on each probe were inserted into hippocampal CA1 and medial prefrontal cortex. Probes were 64-chan, poly5 Takahashi probe formats. Electrophysiological data were acquired using a SpikeGadgets MCU system digitized with 30 kHz rate. Analog and digital channels were acquired using the SpikeGadgets ECU system.
  institution: Georgia Institute of Technology
  keywords: ['memory' 'spatial navigation' 'decision-making']
  lab: Singer
  session_id: S17_210407
  source_script: File created with git repo https://github.com/stephprince/singer-lab-to-nwb/tree/bed20ac732
  Group /general/subject (Subject) 
  identifier: 0587b9a3-fa8c-42cd-b1f0-de22f7055bb7
  Group /intervals/behavior_epochs (TimeIntervals) Indicates the start and stop times in which behavior data was both collected AND synchronized to ephys data.
  Dataset /intervals/behavior_epochs/id (ElementIdentifiers)  | shape = (2,) | dtype = int64
  Dataset /intervals/behavior_epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (2,) | dtype = float64
  Dataset /intervals/behavior_epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (2,) | dtype = float64
  Group /intervals/delay (TimeIntervals) indicates whether the delay cue is on or not, from spikegadgets digital signals
  Dataset /intervals/delay/id (ElementIdentifiers)  | shape = (114,) | dtype = int64
  Dataset /intervals/delay/start_time (VectorData) Start time of epoch, in seconds | shape = (114,) | dtype = float64
  Dataset /intervals/delay/stop_time (VectorData) Stop time of epoch, in seconds | shape = (114,) | dtype = float64
  Group /intervals/recording_epochs (TimeIntervals) During one recording session, the acquisition is stopped and restarted for switching behavioral periods, refilling with saline, etc. Electrophysiological files are stitched together and these epochs indicate the start and stop times within a recording session. These epochs are NOT continuous and there is a short interval of approx 1-5 min between them.
  Dataset /intervals/recording_epochs/behavior_task (VectorData) indicates whether VR task was displayed on the screen (1), or if the screen was left covered/blank as a baseline period (0) | shape = (3,) | dtype = int64
  Dataset /intervals/recording_epochs/id (ElementIdentifiers)  | shape = (3,) | dtype = int64
  Dataset /intervals/recording_epochs/recording_number (VectorData) what the original recording file number this epoch was (as saved in theraw spikegadgets and .mat file names), 1-based indexing | shape = (3,) | dtype = object
  Dataset /intervals/recording_epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (3,) | dtype = float64
  Dataset /intervals/recording_epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (3,) | dtype = float64
  Group /intervals/sync (TimeIntervals) synchronizing pulse sent from virmen software, from spikegadgets digital signals
  Dataset /intervals/sync/id (ElementIdentifiers)  | shape = (46699,) | dtype = int64
  Dataset /intervals/sync/start_time (VectorData) Start time of epoch, in seconds | shape = (46699,) | dtype = float64
  Dataset /intervals/sync/stop_time (VectorData) Stop time of epoch, in seconds | shape = (46699,) | dtype = float64
  Group /intervals/trial (TimeIntervals) indicates when trial is occurring vs inter trial, from spikegadgets digital signals
  Dataset /intervals/trial/id (ElementIdentifiers)  | shape = (92,) | dtype = int64
  Dataset /intervals/trial/start_time (VectorData) Start time of epoch, in seconds | shape = (92,) | dtype = float64
  Dataset /intervals/trial/stop_time (VectorData) Stop time of epoch, in seconds | shape = (92,) | dtype = float64
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/choice (VectorData) choice animal made | shape = (92,) | dtype = int64
  Dataset /intervals/trials/correct (VectorData) whether trial was correct or not | shape = (92,) | dtype = float64
  Dataset /intervals/trials/delay2_location (VectorData) y-position on track where delay 2 occurred | shape = (92,) | dtype = float64
  Dataset /intervals/trials/delay_location (VectorData) y-position on track where delay occurred | shape = (92,) | dtype = float64
  Dataset /intervals/trials/duration (VectorData) duration in seconds | shape = (92,) | dtype = float64
  Dataset /intervals/trials/i_choice_made (VectorData) index when choice made | shape = (92,) | dtype = int64
  Dataset /intervals/trials/i_delay (VectorData) index when delay started | shape = (92,) | dtype = int64
  Dataset /intervals/trials/i_delay2 (VectorData) index when second delay started | shape = (92,) | dtype = float64
  Dataset /intervals/trials/i_update (VectorData) index when update started | shape = (92,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (92,) | dtype = int64
  Dataset /intervals/trials/iterations (VectorData) number of samples/vr frames | shape = (92,) | dtype = int64
  Dataset /intervals/trials/maze_id (VectorData) {'linear': 1, 'ymaze_short': 2, 'ymaze_long': 3, 'ymaze_delay': 4} | shape = (92,) | dtype = int64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (92,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (92,) | dtype = float64
  Dataset /intervals/trials/t_choice_made (VectorData) time when choice made | shape = (92,) | dtype = float64
  Dataset /intervals/trials/t_delay (VectorData) time when delay started | shape = (92,) | dtype = float64
  Dataset /intervals/trials/t_delay2 (VectorData) time when second delay started | shape = (92,) | dtype = float64
  Dataset /intervals/trials/t_update (VectorData) time when update started | shape = (92,) | dtype = float64
  Dataset /intervals/trials/turn_type (VectorData) {'right': 1, 'left': 2} | shape = (92,) | dtype = int64
  Dataset /intervals/trials/update_location (VectorData) y-position on track where update occurred | shape = (92,) | dtype = float64
  Dataset /intervals/trials/update_type (VectorData) {'nan': 1, 'switch': 2, 'stay': 3} | shape = (92,) | dtype = int64
  Group /intervals/update (TimeIntervals) indicates when the update cue is on or not, from spikegadgets digital signals
  Dataset /intervals/update/id (ElementIdentifiers)  | shape = (20,) | dtype = int64
  Dataset /intervals/update/start_time (VectorData) Start time of epoch, in seconds | shape = (20,) | dtype = float64
  Dataset /intervals/update/stop_time (VectorData) Stop time of epoch, in seconds | shape = (20,) | dtype = float64
  Group /processing/behavior (ProcessingModule) contains processed behavioral data
  Group /processing/behavior/licks (BehavioralEvents) 
  Group /processing/behavior/licks/licks (TimeSeries) licking events detected by photointerrupter
  Group /processing/behavior/position (Position) 
  Group /processing/behavior/position/position (SpatialSeries) the x and y position values for the mouse in the virtual-reality environment. X is the first column and Y is the second
  Group /processing/behavior/rewards (BehavioralEvents) 
  Group /processing/behavior/rewards/rewards (TimeSeries) reward delivery times
  Group /processing/behavior/rotational_velocity (TimeSeries) sideways velocity in the virtual reality environment. The roll axis as tracked by the optical mouse.
  Group /processing/behavior/time (TimeSeries) time recorded by virmen software since session state time
  Group /processing/behavior/translational_velocity (TimeSeries) forward and backwards velocity in the virtual reality environment. The pitch axis as tracked by the optical mouse.
  Group /processing/behavior/view_angle (CompassDirection) 
  Group /processing/behavior/view_angle/view_angle (SpatialSeries) direction of mouse in the virtual reality environment
  Group /processing/ecephys (ProcessingModule) contains processed extracellular electrophysiology data
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/LFP (ElectricalSeries) local field potential data generated by singer lab preprocessing pipeline - eeg data
  Dataset /processing/ecephys/LFP/LFP/electrodes (DynamicTableRegion) neuronexus_probes | shape = (128,) | dtype = int64
  Group /processing/ecephys/decomposition_amplitude (DecompositionSeries) filtered ephys amplitude data generated by singer lab preprocessing pipeline
  delta eeg data filtered through: 1 - 4 Hz Delta FIR Equiripple Filter 1 Hz sidebands, 40 dB rolloff
  theta eeg data filtered through: 4 - 12 Hz FIR equiripple theta filter 1 Hz sidebands 50 dB roll off
  beta eeg data filtered through: 12 - 30 Hz Beta FIR Equiripple Filter 1 Hz sidebands, 40 dB rolloff
  lowgamma eeg data filtered through: 20-50Hz bandpass FIR equiripple filter 5Hz sidebands. 60dB roll-off
  ripple eeg data filtered through: 150-250Hz bandpass FIR equiripple filter 10Hz sidebands, 40dB roll-off resampled to 2000 from 1500 sr filter
  Group /processing/ecephys/decomposition_amplitude/bands (DynamicTable) data about the frequency bands that the signal was decomposed into
  Dataset /processing/ecephys/decomposition_amplitude/bands/band_limits (VectorData) low and high frequencies of bandpass filter in Hz | shape = (5, 2) | dtype = float64
  Dataset /processing/ecephys/decomposition_amplitude/bands/band_name (VectorData) the name of the frequency band (recommended: 'alpha', 'beta', 'gamma', 'delta', 'high gamma' | shape = (5,) | dtype = object
  Dataset /processing/ecephys/decomposition_amplitude/bands/id (ElementIdentifiers)  | shape = (5,) | dtype = int64
  Group /processing/ecephys/decomposition_amplitude/source_timeseries (ElectricalSeries) local field potential data generated by singer lab preprocessing pipeline - eeg data
  Dataset /processing/ecephys/decomposition_amplitude/source_timeseries/electrodes (DynamicTableRegion) neuronexus_probes | shape = (128,) | dtype = int64
  Group /processing/ecephys/decomposition_envelope (DecompositionSeries) filtered ephys envelope data generated by singer lab preprocessing pipeline
  delta eeg data filtered through: 1 - 4 Hz Delta FIR Equiripple Filter 1 Hz sidebands, 40 dB rolloff
  theta eeg data filtered through: 4 - 12 Hz FIR equiripple theta filter 1 Hz sidebands 50 dB roll off
  beta eeg data filtered through: 12 - 30 Hz Beta FIR Equiripple Filter 1 Hz sidebands, 40 dB rolloff
  lowgamma eeg data filtered through: 20-50Hz bandpass FIR equiripple filter 5Hz sidebands. 60dB roll-off
  ripple eeg data filtered through: 150-250Hz bandpass FIR equiripple filter 10Hz sidebands, 40dB roll-off resampled to 2000 from 1500 sr filter
  Group /processing/ecephys/decomposition_envelope/bands (DynamicTable) data about the frequency bands that the signal was decomposed into
  Dataset /processing/ecephys/decomposition_envelope/bands/band_limits (VectorData) low and high frequencies of bandpass filter in Hz | shape = (5, 2) | dtype = float64
  Dataset /processing/ecephys/decomposition_envelope/bands/band_name (VectorData) the name of the frequency band (recommended: 'alpha', 'beta', 'gamma', 'delta', 'high gamma' | shape = (5,) | dtype = object
  Dataset /processing/ecephys/decomposition_envelope/bands/id (ElementIdentifiers)  | shape = (5,) | dtype = int64
  Group /processing/ecephys/decomposition_envelope/source_timeseries (ElectricalSeries) local field potential data generated by singer lab preprocessing pipeline - eeg data
  Dataset /processing/ecephys/decomposition_envelope/source_timeseries/electrodes (DynamicTableRegion) neuronexus_probes | shape = (128,) | dtype = int64
  Group /processing/ecephys/decomposition_phase (DecompositionSeries) filtered ephys phase data generated by singer lab preprocessing pipeline
  delta eeg data filtered through: 1 - 4 Hz Delta FIR Equiripple Filter 1 Hz sidebands, 40 dB rolloff
  theta eeg data filtered through: 4 - 12 Hz FIR equiripple theta filter 1 Hz sidebands 50 dB roll off
  beta eeg data filtered through: 12 - 30 Hz Beta FIR Equiripple Filter 1 Hz sidebands, 40 dB rolloff
  lowgamma eeg data filtered through: 20-50Hz bandpass FIR equiripple filter 5Hz sidebands. 60dB roll-off
  ripple eeg data filtered through: 150-250Hz bandpass FIR equiripple filter 10Hz sidebands, 40dB roll-off resampled to 2000 from 1500 sr filter
  Group /processing/ecephys/decomposition_phase/bands (DynamicTable) data about the frequency bands that the signal was decomposed into
  Dataset /processing/ecephys/decomposition_phase/bands/band_limits (VectorData) low and high frequencies of bandpass filter in Hz | shape = (5, 2) | dtype = float64
  Dataset /processing/ecephys/decomposition_phase/bands/band_name (VectorData) the name of the frequency band (recommended: 'alpha', 'beta', 'gamma', 'delta', 'high gamma' | shape = (5,) | dtype = object
  Dataset /processing/ecephys/decomposition_phase/bands/id (ElementIdentifiers)  | shape = (5,) | dtype = int64
  Group /processing/ecephys/decomposition_phase/source_timeseries (ElectricalSeries) local field potential data generated by singer lab preprocessing pipeline - eeg data
  Dataset /processing/ecephys/decomposition_phase/source_timeseries/electrodes (DynamicTableRegion) neuronexus_probes | shape = (128,) | dtype = int64
  Group /processing/ecephys/nonthetas (TimeIntervals) events identified from filtered lfp signals
  Dataset /processing/ecephys/nonthetas/baseline (VectorData) baseline value for event detection | shape = (31,) | dtype = float64
  Dataset /processing/ecephys/nonthetas/energy (VectorData) total sum squared energy of the waveform | shape = (31,) | dtype = float64
  Dataset /processing/ecephys/nonthetas/excluded (VectorData) any post-event detection exclusion criteria applied | shape = (31,) | dtype = float64
  Dataset /processing/ecephys/nonthetas/id (ElementIdentifiers)  | shape = (31,) | dtype = int64
  Dataset /processing/ecephys/nonthetas/max_thresh (VectorData) the largest threshold in stdev units at which this ripple would be detected | shape = (31,) | dtype = float64
  Dataset /processing/ecephys/nonthetas/mid_ind (VectorData) index of middle time in lfp timeseries | shape = (31,) | dtype = float64
  Dataset /processing/ecephys/nonthetas/mid_time (VectorData) middle of lfp event | shape = (31,) | dtype = float64
  Dataset /processing/ecephys/nonthetas/min_duration (VectorData) time (in seconds) signal must be above threshold for event detection | shape = (31,) | dtype = float64
  Dataset /processing/ecephys/nonthetas/peak (VectorData) peak height/energy of the waveform | shape = (31,) | dtype = float64
  Dataset /processing/ecephys/nonthetas/start_ind (VectorData) index of start time in lfp timeseries | shape = (31,) | dtype = float64
  Dataset /processing/ecephys/nonthetas/start_time (VectorData) Start time of epoch, in seconds | shape = (31,) | dtype = float64
  Dataset /processing/ecephys/nonthetas/std (VectorData) standard deviation value used to generate threshold value | shape = (31,) | dtype = float64
  Dataset /processing/ecephys/nonthetas/stop_ind (VectorData) index of stop time in lfp timeseries | shape = (31,) | dtype = float64
  Dataset /processing/ecephys/nonthetas/stop_time (VectorData) Stop time of epoch, in seconds | shape = (31,) | dtype = float64
  Dataset /processing/ecephys/nonthetas/threshold (VectorData) baseline value with X number of std above the mean for event detection | shape = (31,) | dtype = float64
  Group /processing/ecephys/ripples (TimeIntervals) events identified from filtered lfp signals
  Dataset /processing/ecephys/ripples/baseline (VectorData) baseline value for event detection | shape = (14,) | dtype = float64
  Dataset /processing/ecephys/ripples/energy (VectorData) total sum squared energy of the waveform | shape = (14,) | dtype = float64
  Dataset /processing/ecephys/ripples/excluded (VectorData) any post-event detection exclusion criteria applied | shape = (14,) | dtype = float64
  Dataset /processing/ecephys/ripples/id (ElementIdentifiers)  | shape = (14,) | dtype = int64
  Dataset /processing/ecephys/ripples/max_thresh (VectorData) the largest threshold in stdev units at which this ripple would be detected | shape = (14,) | dtype = float64
  Dataset /processing/ecephys/ripples/mid_ind (VectorData) index of middle time in lfp timeseries | shape = (14,) | dtype = float64
  Dataset /processing/ecephys/ripples/mid_time (VectorData) middle of lfp event | shape = (14,) | dtype = float64
  Dataset /processing/ecephys/ripples/min_duration (VectorData) time (in seconds) signal must be above threshold for event detection | shape = (14,) | dtype = float64
  Dataset /processing/ecephys/ripples/peak (VectorData) peak height/energy of the waveform | shape = (14,) | dtype = float64
  Dataset /processing/ecephys/ripples/start_ind (VectorData) index of start time in lfp timeseries | shape = (14,) | dtype = float64
  Dataset /processing/ecephys/ripples/start_time (VectorData) Start time of epoch, in seconds | shape = (14,) | dtype = float64
  Dataset /processing/ecephys/ripples/std (VectorData) standard deviation value used to generate threshold value | shape = (14,) | dtype = float64
  Dataset /processing/ecephys/ripples/stop_ind (VectorData) index of stop time in lfp timeseries | shape = (14,) | dtype = float64
  Dataset /processing/ecephys/ripples/stop_time (VectorData) Stop time of epoch, in seconds | shape = (14,) | dtype = float64
  Dataset /processing/ecephys/ripples/threshold (VectorData) baseline value with X number of std above the mean for event detection | shape = (14,) | dtype = float64
  Group /processing/ecephys/thetas (TimeIntervals) events identified from filtered lfp signals
  Dataset /processing/ecephys/thetas/baseline (VectorData) baseline value for event detection | shape = (13,) | dtype = float64
  Dataset /processing/ecephys/thetas/energy (VectorData) total sum squared energy of the waveform | shape = (13,) | dtype = float64
  Dataset /processing/ecephys/thetas/excluded (VectorData) any post-event detection exclusion criteria applied | shape = (13,) | dtype = float64
  Dataset /processing/ecephys/thetas/id (ElementIdentifiers)  | shape = (13,) | dtype = int64
  Dataset /processing/ecephys/thetas/max_thresh (VectorData) the largest threshold in stdev units at which this ripple would be detected | shape = (13,) | dtype = float64
  Dataset /processing/ecephys/thetas/mid_ind (VectorData) index of middle time in lfp timeseries | shape = (13,) | dtype = float64
  Dataset /processing/ecephys/thetas/mid_time (VectorData) middle of lfp event | shape = (13,) | dtype = float64
  Dataset /processing/ecephys/thetas/min_duration (VectorData) time (in seconds) signal must be above threshold for event detection | shape = (13,) | dtype = float64
  Dataset /processing/ecephys/thetas/peak (VectorData) peak height/energy of the waveform | shape = (13,) | dtype = float64
  Dataset /processing/ecephys/thetas/start_ind (VectorData) index of start time in lfp timeseries | shape = (13,) | dtype = float64
  Dataset /processing/ecephys/thetas/start_time (VectorData) Start time of epoch, in seconds | shape = (13,) | dtype = float64
  Dataset /processing/ecephys/thetas/std (VectorData) standard deviation value used to generate threshold value | shape = (13,) | dtype = float64
  Dataset /processing/ecephys/thetas/stop_ind (VectorData) index of stop time in lfp timeseries | shape = (13,) | dtype = float64
  Dataset /processing/ecephys/thetas/stop_time (VectorData) Stop time of epoch, in seconds | shape = (13,) | dtype = float64
  Dataset /processing/ecephys/thetas/threshold (VectorData) baseline value with X number of std above the mean for event detection | shape = (13,) | dtype = float64
  session_description: Electrophysiological recording session of mice performing the update task
  session_start_time: 2021-04-07T14:36:32.953400-04:00
  timestamps_reference_time: 2021-04-07T14:36:32.953400-04:00
  Group /units (Units) Autogenerated by nwb_conversion_tools.
  Dataset /units/Amplitude (VectorData) amplitude imported from phy | shape = (116,) | dtype = float64
  Dataset /units/ContamPct (VectorData) contampct imported from phy | shape = (116,) | dtype = float64
  Dataset /units/KSLabel (VectorData) auto-label (pre phy curation) | shape = (116,) | dtype = object
  Dataset /units/ab_ratio (VectorData) waveform asymmetry, ratio between positive peaks | shape = (116,) | dtype = float64
  Dataset /units/acg_tau_rise (VectorData) autocorrelogram metric used for classification | shape = (116,) | dtype = float64
  Dataset /units/amp (VectorData) amplitude imported from phy | shape = (116,) | dtype = float64
  Dataset /units/cell_explorer_label (VectorData) classification as good or bad from cell explorer manual curation | shape = (116,) | dtype = object
  Dataset /units/cell_type (VectorData) cell type classification | shape = (116,) | dtype = object
  Dataset /units/ch (VectorData) channel number impoted from phy | shape = (116,) | dtype = float64
  Dataset /units/depth (VectorData) depth imported from phy | shape = (116,) | dtype = float64
  Dataset /units/electrode_group (VectorData) electrode group unit was identified on | shape = (116,) | dtype = object
  Dataset /units/firing_rate (VectorData) Spike count normalized by interval btwn first and last spike | shape = (116,) | dtype = float64
  Dataset /units/firing_rate_instability (VectorData) Mean of absolute differential firing rate across time | shape = (116,) | dtype = float64
  Dataset /units/fr (VectorData) firing rate imported from phy | shape = (116,) | dtype = float64
  Dataset /units/id (ElementIdentifiers)  | shape = (116,) | dtype = int64
  Dataset /units/isi_violation (VectorData) proportion of ISIs less than 2 ms long | shape = (116,) | dtype = float64
  Dataset /units/location_on_electrode_x (VectorData) x coordinate in um of unit on probe | shape = (116,) | dtype = float64
  Dataset /units/location_on_electrode_y (VectorData) y coordinate in um of unit on probe | shape = (116,) | dtype = float64
  Dataset /units/main_channel (VectorData) 0-based recording channel with largest waveform | shape = (116,) | dtype = int64
  Dataset /units/main_channel_phy (VectorData) 0-based main recording channel from phy | shape = (116,) | dtype = int64
  Dataset /units/n_spikes (VectorData) number of spikes imported from phy | shape = (116,) | dtype = float64
  Dataset /units/original_cluster_id (VectorData) original cluster id imported from phy | shape = (116,) | dtype = float64
  Dataset /units/polarity (VectorData) average voltage of spike vs baseline used to flip positive waveforms for metrics | shape = (116,) | dtype = float64
  Dataset /units/quality (VectorData) manual-label (post phy curation) | shape = (116,) | dtype = object
  Dataset /units/region (VectorData) brain region where each unit was detected | shape = (116,) | dtype = object
  Dataset /units/shank_id (VectorData) electrode shank unit was identified on | shape = (116,) | dtype = uint8
  Dataset /units/spike_amplitude (VectorData) peak voltage from main channel (max-min of waveform) | shape = (116,) | dtype = float64
  Dataset /units/spike_count (VectorData) Spike count for entire session, cell explorer removes spikes within 0.5ms so this value will be smaller than the length of the phy spike_times column | shape = (116,) | dtype = int32
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (1762580,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (116,) | dtype = uint32
  Dataset /units/spike_width (VectorData) trough to peak waveform width used for classification | shape = (116,) | dtype = float64
  Dataset /units/unit_name (VectorData) Unique reference for each unit. | shape = (116,) | dtype = object
  Dataset /units/waveform_mean (VectorData) mean filtered waveform | shape = (116, 48) | dtype = float64
  Dataset /units/waveform_rate_cell_explorer (VectorData) time values around the waveform peak | shape = (116,) | dtype = float64
  Dataset /units/waveform_sd (VectorData) std filtered waveform | shape = (116, 48) | dtype = float64
