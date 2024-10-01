
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000149/draft
name: IBL ephys data
contributor: [{'url': 'http://internationalbrainlab.com', 'name': 'International Brain Laboratory', 'email': 'ibldata@internationalbrainlab.org', 'roleName': ['dcite:ContactPerson', 'dcite:Author'], 'schemaKey': 'Organization', 'contactPoint': [], 'includeInCitation': True}]
description: This dataset is a result of a multi-institution, cross country collaboration of labs, called International Brain Laboratory conducting standardized experiments on decision-making in mice.  This dataset contains contains data similar to the dandiset https://dandiarchive.org/dandiset/000045 with additional ephys data.
assetsSummary: {'species': [{'name': 'House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}, {'name': 'behavioral approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 1980839948948, 'numberOfFiles': 4, 'numberOfSubjects': 4, 'variableMeasured': ['Position', 'Units', 'BehavioralTimeSeries', 'ElectrodeGroup'], 'measurementTechnique': [{'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000149 has 4 NWB files.
1 of these NWB files are of type 1.
1 of these NWB files are of type 2.
1 of these NWB files are of type 3.
1 of these NWB files are of type 4.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Video: _iblrig_bodyCamera.raw (ImageSeries) Video recorded by camera.
  Group /acquisition/Video: _iblrig_leftCamera.raw (ImageSeries) Video recorded by camera.
  Group /acquisition/Video: _iblrig_rightCamera.raw (ImageSeries) Video recorded by camera.
  Group /acquisition/probe00_spikeglx_ephysData_g0_t0.imec0.ap.cbin (ElectricalSeries) no description
  Dataset /acquisition/probe00_spikeglx_ephysData_g0_t0.imec0.ap.cbin/electrodes (DynamicTableRegion) probe00 | shape = (374,) | dtype = int64
  Group /acquisition/probe00_spikeglx_ephysData_g0_t0.imec0.lf.cbin (ElectricalSeries) no description
  Dataset /acquisition/probe00_spikeglx_ephysData_g0_t0.imec0.lf.cbin/electrodes (DynamicTableRegion) probe00 | shape = (374,) | dtype = int64
  file_create_date: ['2021-10-22T02:01:56.391111-04:00']
  Group /general/Ibl_session_data (IblSessionData) 
  Group /general/devices/NeuroPixels probe (Device) NeuroPixels probe
  Group /general/devices/probe00 (IblProbes) 
  experiment_description: ibl_neuropixel_brainwide_01
  experimenter: ['97d59a70' 'afb0fdad' 'root']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (374,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (374,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (374,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (374,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (374,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (374,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/rawInd.npy (VectorData) [nch] Each channel's row in its home file (look up via probes.rawFileName), counting from zero. Note some rows don't have a channel, for example if they were sync pulses | shape = (374,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (374,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (374,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (374,) | dtype = float64
  Group /general/extracellular_ephys/probe00 (ElectrodeGroup) model 3B2
  Group /general/extracellular_ephys/probe00/device (Device) NeuroPixels probe
  institution: Sainsbury Wellcome Centre
  keywords: ['97d59a70,afb0fdad,root' 'hoferlab' 'IBL']
  lab: hoferlab
  notes: 
  protocol: _iblrig_tasks_ephysChoiceWorld6.4.2
  session_id: 4ecb5d24-f5cc-402c-be28-9d0f7cb14b3a
  Group /general/subject (IblSubject) 
  surgery: none
  identifier: 4ecb5d24-f5cc-402c-be28-9d0f7cb14b3a
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/choice.npy (VectorData) which choice was made in choiceworld: -1 (turn CCW), +1 (turn CW), or 0 (nogo) | shape = (529,) | dtype = int64
  Dataset /intervals/trials/contrastLeft.npy (VectorData) contrast of left-side stimulus (0...1) nan if trial is on other side | shape = (529,) | dtype = float64
  Dataset /intervals/trials/contrastRight.npy (VectorData) contrast of right-side stimulus (0...1) nan if trial is on other side | shape = (529,) | dtype = float64
  Dataset /intervals/trials/feedbackType.npy (VectorData) Whether feedback is positive or negative in choiceworld (-1 for negative, +1 for positive) | shape = (529,) | dtype = int64
  Dataset /intervals/trials/feedback_times.npy (VectorData) Times of stimulus onset trigger command | shape = (529,) | dtype = float64
  Dataset /intervals/trials/firstMovement_times.npy (VectorData) Times of stimulus onset trigger command | shape = (529,) | dtype = float64
  Dataset /intervals/trials/goCueTrigger_times.npy (VectorData) Times of stimulus onset trigger command | shape = (529,) | dtype = float64
  Dataset /intervals/trials/goCue_times.npy (VectorData) Times of stimulus onset trigger command | shape = (529,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (529,) | dtype = int64
  Dataset /intervals/trials/intervals_bpod.npy (VectorData) 2 column array giving each trials start (i.e. beginning of quiescent period) and stop (i.e. end of iti) times of trials in universal seconds | shape = (529,) | dtype = float64
  Dataset /intervals/trials/probabilityLeft.npy (VectorData) Probability of stimulation to be turned on within the trial | shape = (529,) | dtype = float64
  Dataset /intervals/trials/response_times.npy (VectorData) Times of stimulus onset trigger command | shape = (529,) | dtype = float64
  Dataset /intervals/trials/rewardVolume.npy (VectorData) volume of reward given each trial in µl | shape = (529,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (529,) | dtype = float64
  Dataset /intervals/trials/stimOff_times.npy (VectorData) Times of stimulus onset trigger command | shape = (529,) | dtype = float64
  Dataset /intervals/trials/stimOn_times.npy (VectorData) Times of stimulus onset trigger command | shape = (529,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (529,) | dtype = float64
  Group /processing/behavior (ProcessingModule) behavior
  Group /processing/behavior/BehavioralEpochs (TimeIntervals) experimental intervals
  Dataset /processing/behavior/BehavioralEpochs/id (ElementIdentifiers)  | shape = (1655,) | dtype = int64
  Dataset /processing/behavior/BehavioralEpochs/peakAmplitude.npy (VectorData) amplitude of the wheel move | shape = (1655,) | dtype = float64
  Dataset /processing/behavior/BehavioralEpochs/start_time (VectorData) Start time of epoch, in seconds | shape = (1655,) | dtype = float64
  Dataset /processing/behavior/BehavioralEpochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1655,) | dtype = float64
  Group /processing/behavior/BehavioralTimeSeries (BehavioralTimeSeries) 
  Group /processing/behavior/BehavioralTimeSeries/position.npy (TimeSeries) Absolute position of wheel.
  Group /processing/behavior/Position (Position) 
  Group /processing/behavior/Position/nose_tip_leftCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/nose_tip_rightCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/paw_l_leftCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/paw_l_rightCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/paw_r_leftCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/paw_r_rightCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/pupil_bottom_r_leftCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/pupil_bottom_r_rightCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/pupil_left_r_leftCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/pupil_left_r_rightCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/pupil_right_r_leftCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/pupil_right_r_rightCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/pupil_top_r_leftCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/pupil_top_r_rightCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/tail_start_bodyCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/tongue_end_l_leftCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/tongue_end_l_rightCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/tongue_end_r_leftCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/tongue_end_r_rightCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/tube_bottom_leftCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/tube_bottom_rightCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/tube_top_leftCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/tube_top_rightCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/nose_tip_likelihood_leftCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/nose_tip_likelihood_rightCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/paw_l_likelihood_leftCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/paw_l_likelihood_rightCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/paw_r_likelihood_leftCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/paw_r_likelihood_rightCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/pupil_bottom_r_likelihood_leftCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/pupil_bottom_r_likelihood_rightCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/pupil_left_r_likelihood_leftCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/pupil_left_r_likelihood_rightCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/pupil_right_r_likelihood_leftCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/pupil_right_r_likelihood_rightCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/pupil_top_r_likelihood_leftCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/pupil_top_r_likelihood_rightCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/tail_start_likelihood_bodyCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/tongue_end_l_likelihood_leftCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/tongue_end_l_likelihood_rightCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/tongue_end_r_likelihood_leftCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/tongue_end_r_likelihood_rightCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/tube_bottom_likelihood_leftCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/tube_bottom_likelihood_rightCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/tube_top_likelihood_leftCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/tube_top_likelihood_rightCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/ecephys (ProcessingModule) Processed electrophysiology data of IBL
  Group /processing/ecephys/probe00_iblqc_ephysSpectralDensityAP.power.npy (Spectrum) 
  Group /processing/ecephys/probe00_iblqc_ephysSpectralDensityLF.power.npy (Spectrum) 
  Group /processing/ecephys/probe00_iblqc_ephysTimeRmsAP.rms.npy (ElectricalSeries) RMS amplitude as a function of time (V)
  Dataset /processing/ecephys/probe00_iblqc_ephysTimeRmsAP.rms.npy/electrodes (DynamicTableRegion) probe00 | shape = (374,) | dtype = int64
  Group /processing/ecephys/probe00_iblqc_ephysTimeRmsLF.rms.npy (ElectricalSeries) RMS amplitude as a function of time (V)
  Dataset /processing/ecephys/probe00_iblqc_ephysTimeRmsLF.rms.npy/electrodes (DynamicTableRegion) probe00 | shape = (374,) | dtype = int64
  session_description: Ephys recording with acute probe(s)
  session_start_time: 2020-09-21T19:02:16+00:00
  timestamps_reference_time: 2020-09-21T19:02:16+00:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/amp_max (VectorData) Statistical indicators for amplitude | shape = (794,) | dtype = float64
  Dataset /units/amp_median (VectorData) Statistical indicators for amplitude | shape = (794,) | dtype = float64
  Dataset /units/amp_min (VectorData) Statistical indicators for amplitude | shape = (794,) | dtype = float64
  Dataset /units/amp_std_dB (VectorData) Statistical indicators for amplitude | shape = (794,) | dtype = float64
  Dataset /units/amps.npy (VectorData) Mean amplitude of each cluster (V) | shape = (794,) | dtype = float64
  Dataset /units/cluster_id (VectorData) unit identifier | shape = (794,) | dtype = int64
  Dataset /units/contamination (VectorData) An estimate of the contamination of the unit (i.e. a pseudo false positive measure) based on the number of spikes, number of isi violations, and time between the first and last spike. (see Hill et al. (2011) J Neurosci 31: 8699-8705) Fraction of isi violations over total number of spikes. | shape = (794,) | dtype = float64
  Dataset /units/contamination_alt (VectorData) uses a quadratic solver and may be unstable, contamination uses a simpler algorithm | shape = (794,) | dtype = float64
  Dataset /units/depths.npy (VectorData) [nc] Depth of mean cluster waveform on probe (µm). 0 means deepest site, positive means above this. | shape = (794,) | dtype = float64
  Dataset /units/drift (VectorData) cum drift of a spike feature (e.g. depth or amplitude) on the channel of max amplitude for all spikes in a unit. The sum of the diffs of the feature normalized by the total number of spikes.  | shape = (794,) | dtype = float64
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (794,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex) Index for VectorData 'electrodes' | shape = (794,) | dtype = uint16
  Dataset /units/firing_rate (VectorData) firing_rate | shape = (794,) | dtype = float64
  Dataset /units/id (ElementIdentifiers)  | shape = (794,) | dtype = int64
  Dataset /units/ks2_label (VectorData)  | shape = (794,) | dtype = object
  Dataset /units/label (VectorData)  | shape = (794,) | dtype = float64
  Dataset /units/missed_spikes_est (VectorData) Neurons are assumed stationary so only the random additive noise would cause a deviation. The distribution around the peak is assumed Gaussian in this case | shape = (794,) | dtype = float64
  Dataset /units/noise_cutoff (VectorData) etric describing whether an amplitude distribution is cut off, without a Gaussian assumption (also see above, missed_spikes_est). Takes a histogram of amplitude distribution and computes how many standard deviations the low tail lies outside of the mean number of spikes in the top quantile (high tail).  | shape = (794,) | dtype = float64
  Dataset /units/peakToTrough.npy (VectorData) Waveforms length in ms | shape = (794,) | dtype = float64
  Dataset /units/presence_ratio (VectorData) The fraction of bins where there is at least one spike, over the total number of bins, given a specified bin width. | shape = (794,) | dtype = float64
  Dataset /units/presence_ratio_std (VectorData) Standard deviation of the numbers of spikes within time bins over the recording. | shape = (794,) | dtype = float64
  Dataset /units/slidingRP_viol (VectorData) False positive estimate without a fixed refractory period. Computes the maximum allowed refractory period violations for all possible refractory periods (in 0.25 ms bins), and compares each value to the actual number of violations for that length of refractory period. Returns 1 if a unit passes, 0 if a unit does not pass.  | shape = (794,) | dtype = float64
  Dataset /units/spike_count (VectorData) spike_count | shape = (794,) | dtype = float64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (20096230,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (794,) | dtype = uint32
  Dataset /units/waveform_mean (VectorData) the spike waveform mean for each spike unit | shape = (794, 82) | dtype = float32
  Dataset /units/waveformsChannels.npy (VectorData) Waveform from spike sorting templates (stored as a sparse array, only for a subset of channels closest to the peak channel) | shape = (794, 32) | dtype = int64


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Video: _iblrig_bodyCamera.raw (ImageSeries) Video recorded by camera.
  Group /acquisition/Video: _iblrig_leftCamera.raw (ImageSeries) Video recorded by camera.
  Group /acquisition/Video: _iblrig_rightCamera.raw (ImageSeries) Video recorded by camera.
  Group /acquisition/probe01_spikeglx_ephysData_g0_t0.imec1.ap.cbin (ElectricalSeries) no description
  Dataset /acquisition/probe01_spikeglx_ephysData_g0_t0.imec1.ap.cbin/electrodes (DynamicTableRegion) probe01 | shape = (374,) | dtype = int64
  Group /acquisition/probe01_spikeglx_ephysData_g0_t0.imec1.lf.cbin (ElectricalSeries) no description
  Dataset /acquisition/probe01_spikeglx_ephysData_g0_t0.imec1.lf.cbin/electrodes (DynamicTableRegion) probe01 | shape = (374,) | dtype = int64
  file_create_date: ['2021-10-22T02:01:56.113988-04:00']
  Group /general/Ibl_session_data (IblSessionData) 
  Group /general/devices/NeuroPixels probe (Device) NeuroPixels probe
  Group /general/devices/probe01 (IblProbes) 
  experiment_description: ibl_neuropixel_brainwide_01
  experimenter: ['7339a9d0' '97d59a70' 'afb0fdad' 'root']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/brainLocationIds_ccf_2017.npy (VectorData) Array of integers saying which index in Phy the channel corresponds to (counting from zero). | shape = (374,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (374,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (374,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (374,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (374,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (374,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (374,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/mlapdv.npy (VectorData) 3d location of the channels relative to bregma following ephys alignment - mediolateral; anterior-posterior; dorsoventral coordinates (um) | shape = (374, 3) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/rawInd.npy (VectorData) [nch] Each channel's row in its home file (look up via probes.rawFileName), counting from zero. Note some rows don't have a channel, for example if they were sync pulses | shape = (374,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (374,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (374,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (374,) | dtype = float64
  Group /general/extracellular_ephys/probe01 (ElectrodeGroup) model 3B2
  Group /general/extracellular_ephys/probe01/device (Device) NeuroPixels probe
  institution: Cold Spring Harbor Laboratory
  keywords: ['7339a9d0,97d59a70,afb0fdad,root' 'zadorlab' 'IBL']
  lab: zadorlab
  notes: 
  protocol: _iblrig_tasks_ephysChoiceWorld6.4.2
  session_id: c7bd79c9-c47e-4ea5-aea3-74dda991b48e
  Group /general/subject (IblSubject) 
  surgery: none
  identifier: c7bd79c9-c47e-4ea5-aea3-74dda991b48e
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/choice.npy (VectorData) which choice was made in choiceworld: -1 (turn CCW), +1 (turn CW), or 0 (nogo) | shape = (1213,) | dtype = int64
  Dataset /intervals/trials/contrastLeft.npy (VectorData) contrast of left-side stimulus (0...1) nan if trial is on other side | shape = (1213,) | dtype = float64
  Dataset /intervals/trials/contrastRight.npy (VectorData) contrast of right-side stimulus (0...1) nan if trial is on other side | shape = (1213,) | dtype = float64
  Dataset /intervals/trials/feedbackType.npy (VectorData) Whether feedback is positive or negative in choiceworld (-1 for negative, +1 for positive) | shape = (1213,) | dtype = int64
  Dataset /intervals/trials/feedback_times.npy (VectorData) Times of stimulus onset trigger command | shape = (1213,) | dtype = float64
  Dataset /intervals/trials/firstMovement_times.npy (VectorData) Times of stimulus onset trigger command | shape = (1213,) | dtype = float64
  Dataset /intervals/trials/goCueTrigger_times.npy (VectorData) Times of stimulus onset trigger command | shape = (1213,) | dtype = float64
  Dataset /intervals/trials/goCue_times.npy (VectorData) Times of stimulus onset trigger command | shape = (1213,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (1213,) | dtype = int64
  Dataset /intervals/trials/intervals_bpod.npy (VectorData) 2 column array giving each trials start (i.e. beginning of quiescent period) and stop (i.e. end of iti) times of trials in universal seconds | shape = (1213,) | dtype = float64
  Dataset /intervals/trials/probabilityLeft.npy (VectorData) Probability of stimulation to be turned on within the trial | shape = (1213,) | dtype = float64
  Dataset /intervals/trials/response_times.npy (VectorData) Times of stimulus onset trigger command | shape = (1213,) | dtype = float64
  Dataset /intervals/trials/rewardVolume.npy (VectorData) volume of reward given each trial in µl | shape = (1213,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (1213,) | dtype = float64
  Dataset /intervals/trials/stimOff_times.npy (VectorData) Times of stimulus onset trigger command | shape = (1213,) | dtype = float64
  Dataset /intervals/trials/stimOn_times.npy (VectorData) Times of stimulus onset trigger command | shape = (1213,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1213,) | dtype = float64
  Group /processing/behavior (ProcessingModule) behavior
  Group /processing/behavior/BehavioralEpochs (TimeIntervals) experimental intervals
  Dataset /processing/behavior/BehavioralEpochs/id (ElementIdentifiers)  | shape = (1527,) | dtype = int64
  Dataset /processing/behavior/BehavioralEpochs/peakAmplitude.npy (VectorData) amplitude of the wheel move | shape = (1527,) | dtype = float64
  Dataset /processing/behavior/BehavioralEpochs/start_time (VectorData) Start time of epoch, in seconds | shape = (1527,) | dtype = float64
  Dataset /processing/behavior/BehavioralEpochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1527,) | dtype = float64
  Group /processing/behavior/BehavioralTimeSeries (BehavioralTimeSeries) 
  Group /processing/behavior/BehavioralTimeSeries/position.npy (TimeSeries) Absolute position of wheel.
  Group /processing/behavior/Position (Position) 
  Group /processing/behavior/Position/nose_tip_leftCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/nose_tip_rightCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/paw_l_leftCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/paw_l_rightCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/paw_r_leftCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/paw_r_rightCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/pupil_bottom_r_leftCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/pupil_bottom_r_rightCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/pupil_left_r_leftCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/pupil_left_r_rightCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/pupil_right_r_leftCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/pupil_right_r_rightCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/pupil_top_r_leftCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/pupil_top_r_rightCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/tail_start_bodyCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/tongue_end_l_leftCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/tongue_end_l_rightCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/tongue_end_r_leftCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/tongue_end_r_rightCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/tube_bottom_leftCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/tube_bottom_rightCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/tube_top_leftCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/tube_top_rightCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/nose_tip_likelihood_leftCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/nose_tip_likelihood_rightCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/paw_l_likelihood_leftCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/paw_l_likelihood_rightCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/paw_r_likelihood_leftCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/paw_r_likelihood_rightCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/pupil_bottom_r_likelihood_leftCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/pupil_bottom_r_likelihood_rightCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/pupil_left_r_likelihood_leftCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/pupil_left_r_likelihood_rightCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/pupil_right_r_likelihood_leftCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/pupil_right_r_likelihood_rightCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/pupil_top_r_likelihood_leftCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/pupil_top_r_likelihood_rightCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/tail_start_likelihood_bodyCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/tongue_end_l_likelihood_leftCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/tongue_end_l_likelihood_rightCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/tongue_end_r_likelihood_leftCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/tongue_end_r_likelihood_rightCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/tube_bottom_likelihood_leftCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/tube_bottom_likelihood_rightCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/tube_top_likelihood_leftCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/tube_top_likelihood_rightCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/ecephys (ProcessingModule) Processed electrophysiology data of IBL
  Group /processing/ecephys/probe01_iblqc_ephysSpectralDensityAP.power.npy (Spectrum) 
  Group /processing/ecephys/probe01_iblqc_ephysSpectralDensityLF.power.npy (Spectrum) 
  Group /processing/ecephys/probe01_iblqc_ephysTimeRmsAP.rms.npy (ElectricalSeries) RMS amplitude as a function of time (V)
  Dataset /processing/ecephys/probe01_iblqc_ephysTimeRmsAP.rms.npy/electrodes (DynamicTableRegion) probe01 | shape = (374,) | dtype = int64
  Group /processing/ecephys/probe01_iblqc_ephysTimeRmsLF.rms.npy (ElectricalSeries) RMS amplitude as a function of time (V)
  Dataset /processing/ecephys/probe01_iblqc_ephysTimeRmsLF.rms.npy/electrodes (DynamicTableRegion) probe01 | shape = (374,) | dtype = int64
  session_description: Ephys recording with acute probe(s)
  session_start_time: 2020-09-19T08:16:08+00:00
  timestamps_reference_time: 2020-09-19T08:16:08+00:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/amp_max (VectorData) Statistical indicators for amplitude | shape = (591,) | dtype = float64
  Dataset /units/amp_median (VectorData) Statistical indicators for amplitude | shape = (591,) | dtype = float64
  Dataset /units/amp_min (VectorData) Statistical indicators for amplitude | shape = (591,) | dtype = float64
  Dataset /units/amp_std_dB (VectorData) Statistical indicators for amplitude | shape = (591,) | dtype = float64
  Dataset /units/amps.npy (VectorData) Mean amplitude of each cluster (V) | shape = (591,) | dtype = float64
  Dataset /units/brainLocationAcronyms_ccf_2017.npy (VectorData) Brain location id of channels following ephys alignment obtained from 25um resolution 2017 Allen Common Coordinate Framework | shape = (591,) | dtype = object
  Dataset /units/brainLocationIds_ccf_2017.npy (VectorData) Array of integers saying which index in Phy the channel corresponds to (counting from zero). | shape = (591,) | dtype = int64
  Dataset /units/cluster_id (VectorData) unit identifier | shape = (591,) | dtype = int64
  Dataset /units/contamination (VectorData) An estimate of the contamination of the unit (i.e. a pseudo false positive measure) based on the number of spikes, number of isi violations, and time between the first and last spike. (see Hill et al. (2011) J Neurosci 31: 8699-8705) Fraction of isi violations over total number of spikes. | shape = (591,) | dtype = float64
  Dataset /units/contamination_alt (VectorData) uses a quadratic solver and may be unstable, contamination uses a simpler algorithm | shape = (591,) | dtype = float64
  Dataset /units/depths.npy (VectorData) [nc] Depth of mean cluster waveform on probe (µm). 0 means deepest site, positive means above this. | shape = (591,) | dtype = float64
  Dataset /units/drift (VectorData) cum drift of a spike feature (e.g. depth or amplitude) on the channel of max amplitude for all spikes in a unit. The sum of the diffs of the feature normalized by the total number of spikes.  | shape = (591,) | dtype = float64
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (591,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex) Index for VectorData 'electrodes' | shape = (591,) | dtype = uint16
  Dataset /units/firing_rate (VectorData) firing_rate | shape = (591,) | dtype = float64
  Dataset /units/id (ElementIdentifiers)  | shape = (591,) | dtype = int64
  Dataset /units/ks2_label (VectorData)  | shape = (591,) | dtype = object
  Dataset /units/label (VectorData)  | shape = (591,) | dtype = float64
  Dataset /units/missed_spikes_est (VectorData) Neurons are assumed stationary so only the random additive noise would cause a deviation. The distribution around the peak is assumed Gaussian in this case | shape = (591,) | dtype = float64
  Dataset /units/mlapdv.npy (VectorData) 3d location of the cluster relative to bregma following ephys alignment - mediolateral; anterior-posterior; dorsoventral coordinates (um) | shape = (591, 3) | dtype = int64
  Dataset /units/noise_cutoff (VectorData) etric describing whether an amplitude distribution is cut off, without a Gaussian assumption (also see above, missed_spikes_est). Takes a histogram of amplitude distribution and computes how many standard deviations the low tail lies outside of the mean number of spikes in the top quantile (high tail).  | shape = (591,) | dtype = float64
  Dataset /units/peakToTrough.npy (VectorData) Waveforms length in ms | shape = (591,) | dtype = float64
  Dataset /units/presence_ratio (VectorData) The fraction of bins where there is at least one spike, over the total number of bins, given a specified bin width. | shape = (591,) | dtype = float64
  Dataset /units/presence_ratio_std (VectorData) Standard deviation of the numbers of spikes within time bins over the recording. | shape = (591,) | dtype = float64
  Dataset /units/slidingRP_viol (VectorData) False positive estimate without a fixed refractory period. Computes the maximum allowed refractory period violations for all possible refractory periods (in 0.25 ms bins), and compares each value to the actual number of violations for that length of refractory period. Returns 1 if a unit passes, 0 if a unit does not pass.  | shape = (591,) | dtype = float64
  Dataset /units/spike_count (VectorData) spike_count | shape = (591,) | dtype = float64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (13428058,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (591,) | dtype = uint32
  Dataset /units/waveform_mean (VectorData) the spike waveform mean for each spike unit | shape = (591, 82) | dtype = float32
  Dataset /units/waveformsChannels.npy (VectorData) Waveform from spike sorting templates (stored as a sparse array, only for a subset of channels closest to the peak channel) | shape = (591, 32) | dtype = int64


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Video: _iblrig_bodyCamera.raw (ImageSeries) Video recorded by camera.
  Group /acquisition/Video: _iblrig_leftCamera.raw (ImageSeries) Video recorded by camera.
  Group /acquisition/Video: _iblrig_rightCamera.raw (ImageSeries) Video recorded by camera.
  file_create_date: ['2021-10-22T02:01:55.880827-04:00']
  Group /general/Ibl_session_data (IblSessionData) 
  Group /general/devices/NeuroPixels probe (Device) NeuroPixels probe
  Group /general/devices/probe00 (IblProbes) 
  experiment_description: ibl_neuropixel_brainwide_01
  experimenter: ['12da3001' '5d38cdd5' '97d59a70' 'bd2cd700' 'root']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/brainLocationIds_ccf_2017.npy (VectorData) Array of integers saying which index in Phy the channel corresponds to (counting from zero). | shape = (374,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (374,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (374,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (374,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (374,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (374,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (374,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/mlapdv.npy (VectorData) 3d location of the channels relative to bregma following ephys alignment - mediolateral; anterior-posterior; dorsoventral coordinates (um) | shape = (374, 3) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/rawInd.npy (VectorData) [nch] Each channel's row in its home file (look up via probes.rawFileName), counting from zero. Note some rows don't have a channel, for example if they were sync pulses | shape = (374,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (374,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (374,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (374,) | dtype = float64
  Group /general/extracellular_ephys/probe00 (ElectrodeGroup) model 3A
  Group /general/extracellular_ephys/probe00/device (Device) NeuroPixels probe
  institution: Cold Spring Harbor Laboratory
  keywords: ['12da3001,5d38cdd5,97d59a70,bd2cd700,root' 'churchlandlab' 'IBL']
  lab: churchlandlab
  notes: User:5d38cdd5, User:5d38cdd5, User:5d38cdd5, User:5d38cdd5post-session, User:5d38cdd5frontal cranio, User:5d38cdd5video sync, User:5d38cdd5, User:5d38cdd5, User:5d38cdd5, User:5d38cdd5
  protocol: _iblrig_tasks_ephysChoiceWorld6.2.5
  session_id: 4b7fbad4-f6de-43b4-9b15-c7c7ef44db4b
  Group /general/subject (IblSubject) 
  surgery: none
  identifier: 4b7fbad4-f6de-43b4-9b15-c7c7ef44db4b
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/choice.npy (VectorData) which choice was made in choiceworld: -1 (turn CCW), +1 (turn CW), or 0 (nogo) | shape = (842,) | dtype = int64
  Dataset /intervals/trials/contrastLeft.npy (VectorData) contrast of left-side stimulus (0...1) nan if trial is on other side | shape = (842,) | dtype = float64
  Dataset /intervals/trials/contrastRight.npy (VectorData) contrast of right-side stimulus (0...1) nan if trial is on other side | shape = (842,) | dtype = float64
  Dataset /intervals/trials/feedbackType.npy (VectorData) Whether feedback is positive or negative in choiceworld (-1 for negative, +1 for positive) | shape = (842,) | dtype = int64
  Dataset /intervals/trials/feedback_times.npy (VectorData) Times of stimulus onset trigger command | shape = (842,) | dtype = float64
  Dataset /intervals/trials/firstMovement_times.npy (VectorData) Times of stimulus onset trigger command | shape = (842,) | dtype = float64
  Dataset /intervals/trials/goCueTrigger_times.npy (VectorData) Times of stimulus onset trigger command | shape = (842,) | dtype = float64
  Dataset /intervals/trials/goCue_times.npy (VectorData) Times of stimulus onset trigger command | shape = (842,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (842,) | dtype = int64
  Dataset /intervals/trials/intervals_bpod.npy (VectorData) 2 column array giving each trials start (i.e. beginning of quiescent period) and stop (i.e. end of iti) times of trials in universal seconds | shape = (842,) | dtype = float64
  Dataset /intervals/trials/itiDuration.npy (VectorData) Intertrial interval duration for each trial | shape = (842,) | dtype = float64
  Dataset /intervals/trials/probabilityLeft.npy (VectorData) Probability of stimulation to be turned on within the trial | shape = (842,) | dtype = float64
  Dataset /intervals/trials/response_times.npy (VectorData) Times of stimulus onset trigger command | shape = (842,) | dtype = float64
  Dataset /intervals/trials/rewardVolume.npy (VectorData) volume of reward given each trial in µl | shape = (842,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (842,) | dtype = float64
  Dataset /intervals/trials/stimOff_times.npy (VectorData) Times of stimulus onset trigger command | shape = (842,) | dtype = float64
  Dataset /intervals/trials/stimOn_times.npy (VectorData) Times of stimulus onset trigger command | shape = (842,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (842,) | dtype = float64
  Group /processing/behavior (ProcessingModule) behavior
  Group /processing/behavior/BehavioralEpochs (TimeIntervals) experimental intervals
  Dataset /processing/behavior/BehavioralEpochs/id (ElementIdentifiers)  | shape = (1659,) | dtype = int64
  Dataset /processing/behavior/BehavioralEpochs/peakAmplitude.npy (VectorData) amplitude of the wheel move | shape = (1659,) | dtype = float64
  Dataset /processing/behavior/BehavioralEpochs/start_time (VectorData) Start time of epoch, in seconds | shape = (1659,) | dtype = float64
  Dataset /processing/behavior/BehavioralEpochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1659,) | dtype = float64
  Group /processing/behavior/BehavioralTimeSeries (BehavioralTimeSeries) 
  Group /processing/behavior/BehavioralTimeSeries/position.npy (TimeSeries) Absolute position of wheel.
  Group /processing/behavior/Position (Position) 
  Group /processing/behavior/Position/nose_tip_leftCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/nose_tip_rightCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/paw_l_leftCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/paw_l_rightCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/paw_r_leftCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/paw_r_rightCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/pupil_bottom_r_leftCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/pupil_bottom_r_rightCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/pupil_left_r_leftCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/pupil_left_r_rightCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/pupil_right_r_leftCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/pupil_right_r_rightCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/pupil_top_r_leftCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/pupil_top_r_rightCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/tail_start_bodyCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/tongue_end_l_leftCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/tongue_end_l_rightCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/tongue_end_r_leftCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/tongue_end_r_rightCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/tube_bottom_leftCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/tube_bottom_rightCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/tube_top_leftCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/Position/tube_top_rightCamera (SpatialSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/nose_tip_likelihood_leftCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/nose_tip_likelihood_rightCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/paw_l_likelihood_leftCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/paw_l_likelihood_rightCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/paw_r_likelihood_leftCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/paw_r_likelihood_rightCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/pupil_bottom_r_likelihood_leftCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/pupil_bottom_r_likelihood_rightCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/pupil_left_r_likelihood_leftCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/pupil_left_r_likelihood_rightCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/pupil_right_r_likelihood_leftCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/pupil_right_r_likelihood_rightCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/pupil_top_r_likelihood_leftCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/pupil_top_r_likelihood_rightCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/tail_start_likelihood_bodyCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/tongue_end_l_likelihood_leftCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/tongue_end_l_likelihood_rightCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/tongue_end_r_likelihood_leftCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/tongue_end_r_likelihood_rightCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/tube_bottom_likelihood_leftCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/tube_bottom_likelihood_rightCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/tube_top_likelihood_leftCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/behavior/tube_top_likelihood_rightCamera (TimeSeries) Raw DLC output for Camera as numpy array
  Group /processing/ecephys (ProcessingModule) Processed electrophysiology data of IBL
  Group /processing/ecephys/probe00_iblqc_ephysSpectralDensityAP.power.npy (Spectrum) 
  Group /processing/ecephys/probe00_iblqc_ephysSpectralDensityLF.power.npy (Spectrum) 
  Group /processing/ecephys/probe00_iblqc_ephysTimeRmsAP.rms.npy (ElectricalSeries) RMS amplitude as a function of time (V)
  Dataset /processing/ecephys/probe00_iblqc_ephysTimeRmsAP.rms.npy/electrodes (DynamicTableRegion) probe00 | shape = (374,) | dtype = int64
  Group /processing/ecephys/probe00_iblqc_ephysTimeRmsLF.rms.npy (ElectricalSeries) RMS amplitude as a function of time (V)
  Dataset /processing/ecephys/probe00_iblqc_ephysTimeRmsLF.rms.npy/electrodes (DynamicTableRegion) probe00 | shape = (374,) | dtype = int64
  session_description: Ephys recording with acute probe(s)
  session_start_time: 2020-01-08T15:52:42+00:00
  timestamps_reference_time: 2020-01-08T15:52:42+00:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/amp_max (VectorData) Statistical indicators for amplitude | shape = (303,) | dtype = float64
  Dataset /units/amp_median (VectorData) Statistical indicators for amplitude | shape = (303,) | dtype = float64
  Dataset /units/amp_min (VectorData) Statistical indicators for amplitude | shape = (303,) | dtype = float64
  Dataset /units/amp_std_dB (VectorData) Statistical indicators for amplitude | shape = (303,) | dtype = float64
  Dataset /units/amps.npy (VectorData) Mean amplitude of each cluster (V) | shape = (303,) | dtype = float64
  Dataset /units/brainLocationAcronyms_ccf_2017.npy (VectorData) Brain location id of channels following ephys alignment obtained from 25um resolution 2017 Allen Common Coordinate Framework | shape = (303,) | dtype = object
  Dataset /units/brainLocationIds_ccf_2017.npy (VectorData) Array of integers saying which index in Phy the channel corresponds to (counting from zero). | shape = (303,) | dtype = int64
  Dataset /units/cluster_id (VectorData) unit identifier | shape = (303,) | dtype = int64
  Dataset /units/contamination (VectorData) An estimate of the contamination of the unit (i.e. a pseudo false positive measure) based on the number of spikes, number of isi violations, and time between the first and last spike. (see Hill et al. (2011) J Neurosci 31: 8699-8705) Fraction of isi violations over total number of spikes. | shape = (303,) | dtype = float64
  Dataset /units/contamination_alt (VectorData) uses a quadratic solver and may be unstable, contamination uses a simpler algorithm | shape = (303,) | dtype = float64
  Dataset /units/depths.npy (VectorData) [nc] Depth of mean cluster waveform on probe (µm). 0 means deepest site, positive means above this. | shape = (303,) | dtype = float64
  Dataset /units/drift (VectorData) cum drift of a spike feature (e.g. depth or amplitude) on the channel of max amplitude for all spikes in a unit. The sum of the diffs of the feature normalized by the total number of spikes.  | shape = (303,) | dtype = float64
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (303,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex) Index for VectorData 'electrodes' | shape = (303,) | dtype = uint16
  Dataset /units/firing_rate (VectorData) firing_rate | shape = (303,) | dtype = float64
  Dataset /units/id (ElementIdentifiers)  | shape = (303,) | dtype = int64
  Dataset /units/ks2_label (VectorData)  | shape = (303,) | dtype = object
  Dataset /units/label (VectorData)  | shape = (303,) | dtype = float64
  Dataset /units/missed_spikes_est (VectorData) Neurons are assumed stationary so only the random additive noise would cause a deviation. The distribution around the peak is assumed Gaussian in this case | shape = (303,) | dtype = float64
  Dataset /units/mlapdv.npy (VectorData) 3d location of the cluster relative to bregma following ephys alignment - mediolateral; anterior-posterior; dorsoventral coordinates (um) | shape = (303, 3) | dtype = int64
  Dataset /units/noise_cutoff (VectorData) etric describing whether an amplitude distribution is cut off, without a Gaussian assumption (also see above, missed_spikes_est). Takes a histogram of amplitude distribution and computes how many standard deviations the low tail lies outside of the mean number of spikes in the top quantile (high tail).  | shape = (303,) | dtype = float64
  Dataset /units/peakToTrough.npy (VectorData) Waveforms length in ms | shape = (303,) | dtype = float64
  Dataset /units/presence_ratio (VectorData) The fraction of bins where there is at least one spike, over the total number of bins, given a specified bin width. | shape = (303,) | dtype = float64
  Dataset /units/presence_ratio_std (VectorData) Standard deviation of the numbers of spikes within time bins over the recording. | shape = (303,) | dtype = float64
  Dataset /units/slidingRP_viol (VectorData) False positive estimate without a fixed refractory period. Computes the maximum allowed refractory period violations for all possible refractory periods (in 0.25 ms bins), and compares each value to the actual number of violations for that length of refractory period. Returns 1 if a unit passes, 0 if a unit does not pass.  | shape = (303,) | dtype = float64
  Dataset /units/spike_count (VectorData) spike_count | shape = (303,) | dtype = float64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (7787449,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (303,) | dtype = uint32
  Dataset /units/waveform_mean (VectorData) the spike waveform mean for each spike unit | shape = (303, 82) | dtype = float32
  Dataset /units/waveformsChannels.npy (VectorData) Waveform from spike sorting templates (stored as a sparse array, only for a subset of channels closest to the peak channel) | shape = (303, 32) | dtype = int64


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Video: _iblrig_bodyCamera.raw (ImageSeries) Video recorded by camera.
  Group /acquisition/Video: _iblrig_leftCamera.raw (ImageSeries) Video recorded by camera.
  Group /acquisition/Video: _iblrig_rightCamera.raw (ImageSeries) Video recorded by camera.
  Group /acquisition/probe01_spikeglx_ephysData_g0_t0.imec1.ap.cbin (ElectricalSeries) no description
  Dataset /acquisition/probe01_spikeglx_ephysData_g0_t0.imec1.ap.cbin/electrodes (DynamicTableRegion) probe01 | shape = (374,) | dtype = int64
  Group /acquisition/probe01_spikeglx_ephysData_g0_t0.imec1.lf.cbin (ElectricalSeries) no description
  Dataset /acquisition/probe01_spikeglx_ephysData_g0_t0.imec1.lf.cbin/electrodes (DynamicTableRegion) probe01 | shape = (374,) | dtype = int64
  file_create_date: ['2021-11-11T01:01:19.335346-05:00']
  Group /general/Ibl_session_data (IblSessionData) 
  Group /general/devices/NeuroPixels probe (Device) NeuroPixels probe
  Group /general/devices/probe01 (IblProbes) 
  experiment_description: ibl_neuropixel_brainwide_01
  experimenter: ['11502f35']
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/brainLocationIds_ccf_2017.npy (VectorData) Array of integers saying which index in Phy the channel corresponds to (counting from zero). | shape = (374,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (374,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (374,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (374,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (374,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (374,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (374,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/mlapdv.npy (VectorData) 3d location of the channels relative to bregma following ephys alignment - mediolateral; anterior-posterior; dorsoventral coordinates (um) | shape = (374, 3) | dtype = int32
  Dataset /general/extracellular_ephys/electrodes/rawInd.npy (VectorData) [nch] Each channel's row in its home file (look up via probes.rawFileName), counting from zero. Note some rows don't have a channel, for example if they were sync pulses | shape = (374,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (374,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (374,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (374,) | dtype = float64
  Group /general/extracellular_ephys/probe01 (ElectrodeGroup) model 3B2
  Group /general/extracellular_ephys/probe01/device (Device) NeuroPixels probe
  institution: University College London
  keywords: ['11502f35' 'cortexlab' 'IBL']
  lab: cortexlab
  notes: User:11502f35amps_patching_local_server2: probe01: completed, User:11502f35amps_patching_local_server: completed, User:11502f35amps_patching_local_server2: probe00: completed, User:11502f35amps_patching_local_server: completed
  protocol: _iblrig_tasks_ephysChoiceWorld6.1.3
  session_id: aad23144-0e52-4eac-80c5-c4ee2decb198
  Group /general/subject (IblSubject) 
  surgery: none
  identifier: aad23144-0e52-4eac-80c5-c4ee2decb198
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/choice.npy (VectorData) which choice was made in choiceworld: -1 (turn CCW), +1 (turn CW), or 0 (nogo) | shape = (641,) | dtype = int64
  Dataset /intervals/trials/contrastLeft.npy (VectorData) contrast of left-side stimulus (0...1) nan if trial is on other side | shape = (641,) | dtype = float64
  Dataset /intervals/trials/contrastRight.npy (VectorData) contrast of right-side stimulus (0...1) nan if trial is on other side | shape = (641,) | dtype = float64
  Dataset /intervals/trials/feedbackType.npy (VectorData) Whether feedback is positive or negative in choiceworld (-1 for negative, +1 for positive) | shape = (641,) | dtype = int64
  Dataset /intervals/trials/feedback_times.npy (VectorData) Times of stimulus onset trigger command | shape = (641,) | dtype = float64
  Dataset /intervals/trials/firstMovement_times.npy (VectorData) Times of stimulus onset trigger command | shape = (641,) | dtype = float64
  Dataset /intervals/trials/goCueTrigger_times.npy (VectorData) Times of stimulus onset trigger command | shape = (641,) | dtype = float64
  Dataset /intervals/trials/goCue_times.npy (VectorData) Times of stimulus onset trigger command | shape = (641,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (641,) | dtype = int64
  Dataset /intervals/trials/intervals_bpod.npy (VectorData) 2 column array giving each trials start (i.e. beginning of quiescent period) and stop (i.e. end of iti) times of trials in universal seconds | shape = (641,) | dtype = float64
  Dataset /intervals/trials/itiDuration.npy (VectorData) Intertrial interval duration for each trial | shape = (641,) | dtype = float64
  Dataset /intervals/trials/probabilityLeft.npy (VectorData) Probability of stimulation to be turned on within the trial | shape = (641,) | dtype = float64
  Dataset /intervals/trials/response_times.npy (VectorData) Times of stimulus onset trigger command | shape = (641,) | dtype = float64
  Dataset /intervals/trials/rewardVolume.npy (VectorData) volume of reward given each trial in µl | shape = (641,) | dtype = float64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (641,) | dtype = float64
  Dataset /intervals/trials/stimOff_times.npy (VectorData) Times of stimulus onset trigger command | shape = (641,) | dtype = float64
  Dataset /intervals/trials/stimOn_times.npy (VectorData) Times of stimulus onset trigger command | shape = (641,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (641,) | dtype = float64
  Group /processing/behavior (ProcessingModule) behavior
  Group /processing/behavior/BehavioralEpochs (TimeIntervals) experimental intervals
  Dataset /processing/behavior/BehavioralEpochs/id (ElementIdentifiers)  | shape = (997,) | dtype = int64
  Dataset /processing/behavior/BehavioralEpochs/peakAmplitude.npy (VectorData) amplitude of the wheel move | shape = (997,) | dtype = float64
  Dataset /processing/behavior/BehavioralEpochs/start_time (VectorData) Start time of epoch, in seconds | shape = (997,) | dtype = float64
  Dataset /processing/behavior/BehavioralEpochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (997,) | dtype = float64
  Group /processing/behavior/BehavioralTimeSeries (BehavioralTimeSeries) 
  Group /processing/behavior/BehavioralTimeSeries/position.npy (TimeSeries) Absolute position of wheel.
  Group /processing/behavior/Position (Position) 
  Group /processing/ecephys (ProcessingModule) Processed electrophysiology data of IBL
  Group /processing/ecephys/probe01_iblqc_ephysSpectralDensityAP.power.npy (Spectrum) 
  Group /processing/ecephys/probe01_iblqc_ephysSpectralDensityLF.power.npy (Spectrum) 
  Group /processing/ecephys/probe01_iblqc_ephysTimeRmsAP.rms.npy (ElectricalSeries) RMS amplitude as a function of time (V)
  Dataset /processing/ecephys/probe01_iblqc_ephysTimeRmsAP.rms.npy/electrodes (DynamicTableRegion) probe01 | shape = (374,) | dtype = int64
  Group /processing/ecephys/probe01_iblqc_ephysTimeRmsLF.rms.npy (ElectricalSeries) RMS amplitude as a function of time (V)
  Dataset /processing/ecephys/probe01_iblqc_ephysTimeRmsLF.rms.npy/electrodes (DynamicTableRegion) probe01 | shape = (374,) | dtype = int64
  session_description: Behavior training/tasks
  session_start_time: 2019-12-10T16:44:12+00:00
  timestamps_reference_time: 2019-12-10T16:44:12+00:00
  Group /units (Units) Autogenerated by NWBFile
  Dataset /units/amp_max (VectorData) Statistical indicators for amplitude | shape = (388,) | dtype = float64
  Dataset /units/amp_median (VectorData) Statistical indicators for amplitude | shape = (388,) | dtype = float64
  Dataset /units/amp_min (VectorData) Statistical indicators for amplitude | shape = (388,) | dtype = float64
  Dataset /units/amp_std_dB (VectorData) Statistical indicators for amplitude | shape = (388,) | dtype = float64
  Dataset /units/amps.npy (VectorData) Mean amplitude of each cluster (V) | shape = (388,) | dtype = float64
  Dataset /units/brainLocationAcronyms_ccf_2017.npy (VectorData) Brain location id of channels following ephys alignment obtained from 25um resolution 2017 Allen Common Coordinate Framework | shape = (388,) | dtype = object
  Dataset /units/brainLocationIds_ccf_2017.npy (VectorData) Array of integers saying which index in Phy the channel corresponds to (counting from zero). | shape = (388,) | dtype = int64
  Dataset /units/cluster_id (VectorData) unit identifier | shape = (388,) | dtype = int64
  Dataset /units/contamination (VectorData) An estimate of the contamination of the unit (i.e. a pseudo false positive measure) based on the number of spikes, number of isi violations, and time between the first and last spike. (see Hill et al. (2011) J Neurosci 31: 8699-8705) Fraction of isi violations over total number of spikes. | shape = (388,) | dtype = float64
  Dataset /units/contamination_alt (VectorData) uses a quadratic solver and may be unstable, contamination uses a simpler algorithm | shape = (388,) | dtype = float64
  Dataset /units/depths.npy (VectorData) [nc] Depth of mean cluster waveform on probe (µm). 0 means deepest site, positive means above this. | shape = (388,) | dtype = float64
  Dataset /units/drift (VectorData) cum drift of a spike feature (e.g. depth or amplitude) on the channel of max amplitude for all spikes in a unit. The sum of the diffs of the feature normalized by the total number of spikes.  | shape = (388,) | dtype = float64
  Dataset /units/electrodes (DynamicTableRegion) the electrodes that each spike unit came from | shape = (388,) | dtype = int64
  Dataset /units/electrodes_index (VectorIndex) Index for VectorData 'electrodes' | shape = (388,) | dtype = uint16
  Dataset /units/firing_rate (VectorData) firing_rate | shape = (388,) | dtype = float64
  Dataset /units/id (ElementIdentifiers)  | shape = (388,) | dtype = int64
  Dataset /units/ks2_label (VectorData)  | shape = (388,) | dtype = object
  Dataset /units/label (VectorData)  | shape = (388,) | dtype = float64
  Dataset /units/missed_spikes_est (VectorData) Neurons are assumed stationary so only the random additive noise would cause a deviation. The distribution around the peak is assumed Gaussian in this case | shape = (388,) | dtype = float64
  Dataset /units/mlapdv.npy (VectorData) 3d location of the cluster relative to bregma following ephys alignment - mediolateral; anterior-posterior; dorsoventral coordinates (um) | shape = (388, 3) | dtype = int64
  Dataset /units/noise_cutoff (VectorData) etric describing whether an amplitude distribution is cut off, without a Gaussian assumption (also see above, missed_spikes_est). Takes a histogram of amplitude distribution and computes how many standard deviations the low tail lies outside of the mean number of spikes in the top quantile (high tail).  | shape = (388,) | dtype = float64
  Dataset /units/peakToTrough.npy (VectorData) Waveforms length in ms | shape = (388,) | dtype = float64
  Dataset /units/presence_ratio (VectorData) The fraction of bins where there is at least one spike, over the total number of bins, given a specified bin width. | shape = (388,) | dtype = float64
  Dataset /units/presence_ratio_std (VectorData) Standard deviation of the numbers of spikes within time bins over the recording. | shape = (388,) | dtype = float64
  Dataset /units/slidingRP_viol (VectorData) False positive estimate without a fixed refractory period. Computes the maximum allowed refractory period violations for all possible refractory periods (in 0.25 ms bins), and compares each value to the actual number of violations for that length of refractory period. Returns 1 if a unit passes, 0 if a unit does not pass.  | shape = (388,) | dtype = float64
  Dataset /units/spike_count (VectorData) spike_count | shape = (388,) | dtype = float64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (5025800,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (388,) | dtype = uint32
  Dataset /units/waveform_mean (VectorData) the spike waveform mean for each spike unit | shape = (388, 82) | dtype = float32
  Dataset /units/waveformsChannels.npy (VectorData) Waveform from spike sorting templates (stored as a sparse array, only for a subset of channels closest to the peak channel) | shape = (388, 32) | dtype = int64
