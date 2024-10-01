
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000568/0.230705.1633
name: Probing subthreshold dynamics of hippocampal neurons by pulsed optogenetics
contributor: [{'url': 'https://valeroneuroscience.com/', 'name': 'Valero, Manuel', 'email': 'valegarman@gmail.com', 'roleName': ['dcite:Author', 'dcite:ContactPerson', 'dcite:Researcher', 'dcite:Conceptualization', 'dcite:DataCurator', 'dcite:FundingAcquisition', 'dcite:Investigation', 'dcite:Methodology', 'dcite:ProjectAdministration', 'dcite:FormalAnalysis', 'dcite:Software', 'dcite:Validation', 'dcite:Visualization'], 'schemaKey': 'Person', 'identifier': '0000-0001-7860-577X', 'affiliation': [], 'includeInCitation': True}, {'name': ' Zutshi, Ipshita', 'roleName': ['dcite:Methodology', 'dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0001-8180-0816', 'affiliation': [], 'includeInCitation': True}, {'name': 'Yoon, Euisik', 'roleName': ['dcite:Author', 'dcite:FundingAcquisition', 'dcite:Supervision', 'dcite:ProjectAdministration'], 'schemaKey': 'Person', 'identifier': '0000-0002-2127-1200', 'affiliation': [], 'includeInCitation': True}, {'name': 'Buzsáki, György', 'email': 'gyorgy.buzsaki@nyumc.org', 'roleName': ['dcite:Author', 'dcite:Conceptualization', 'dcite:FundingAcquisition', 'dcite:Methodology', 'dcite:ProjectAdministration', 'dcite:Supervision', 'dcite:Researcher'], 'schemaKey': 'Person', 'identifier': '0000-0002-3100-4800', 'affiliation': [], 'includeInCitation': True}, {'url': 'http://www.hfsp.org/', 'name': 'International Human Frontier Science Program Organization', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/02ebx7v45', 'awardNumber': ' LT0000717/2018, NIH MH107396, NS 090583 NSF PIRE, 1545858, U19 NS107616, U19 NS104590, LT0000717/2018', 'contactPoint': [], 'includeInCitation': False}, {'url': 'http://www.nih.gov/', 'name': 'National Institutes of Health', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01cwqze88', 'awardNumber': 'MH107396, U19NS107616', 'contactPoint': [], 'includeInCitation': False}, {'url': 'https://www.nimh.nih.gov/', 'name': 'National Institute of Mental Health', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/04xeg9z08', 'awardNumber': 'NS107616', 'contactPoint': [], 'includeInCitation': False}, {'url': 'https://www.embo.org/', 'name': 'European Molecular Biology Organization', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/04wfr2810', 'awardNumber': 'EMBO ALTF 1161-2017', 'contactPoint': [], 'includeInCitation': False}, {'url': 'http://www.nsf.gov/', 'name': 'National Science Foundation', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/021nxhr62', 'awardNumber': 'NeuroNex MINT grant 1707316', 'contactPoint': [], 'includeInCitation': False}, {'url': 'http://leonlevyfoundation.org/', 'name': 'Leon Levy Foundation', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/033hnyq61', 'awardNumber': 'NIH MH107396,  NS 090583 NSF PIRE, 1545858, U19 NS107616', 'contactPoint': [], 'includeInCitation': False}, {'name': 'Mayorquin, Heberto', 'email': 'h.mayorquin@gmail.com', 'roleName': ['dcite:DataCurator'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': False}]
description: Understanding how excitatory (E) and inhibitory (I) inputs are integrated by neurons requires monitoring their subthreshold behavior. We probed the subthreshold dynamics using optogenetic depolarizing pulses in hippocampal neuronal assemblies in freely moving mice. Excitability decreased during sharp- wave ripples coupled with increased I. In contrast to this “negative gain,” optogenetic probing showed increased within-field excitability in place cells by weakening I and unmasked stable place fields in initially non–place cells. Neuronal assemblies active during sharp-wave ripples in the home cage predicted spatial overlap and sequences of place fields of both place cells and unmasked preexisting place fields of non–place cells during track running. Thus, indirect probing of subthreshold dynamics in neuronal populations permits the disclosing of preexisting assemblies and modes of neuronal operations.
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'behavioral approach', 'schemaKey': 'ApproachType'}, {'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}, {'name': 'optogenetic approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 904756915175, 'numberOfFiles': 138, 'numberOfSubjects': 4, 'variableMeasured': ['LFP', 'Units', 'SpatialSeries', 'ElectrodeGroup', 'ElectricalSeries', 'Position', 'ProcessingModule', 'OptogeneticSeries'], 'measurementTechnique': [{'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'signal filtering technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000568 has 16 NWB files.
1 of these NWB files are of type 1.
1 of these NWB files are of type 2.
1 of these NWB files are of type 3.
1 of these NWB files are of type 4.
12 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ImageSeriesTrackingVideo1 (ImageSeries) Video recorded with Basler camera.
  file_create_date: ['2023-07-04T16:49:10.326659+02:00']
  Group /general/devices/N1-F21-O36 | 18 (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  experiment_description: Probing subthreshold dynamics of hippocampal neurons by pulsed optogenetics
  experimenter: ['Valero, Manuel' 'Zutshi, Ipshita' 'Yoon, Euisik' 'Buzsáki, György']
  Group /general/extracellular_ephys/Group 1 (ElectrodeGroup) no description
  Group /general/extracellular_ephys/Group 1/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  Group /general/extracellular_ephys/Group 2 (ElectrodeGroup) no description
  Group /general/extracellular_ephys/Group 2/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  Group /general/extracellular_ephys/Group 3 (ElectrodeGroup) no description
  Group /general/extracellular_ephys/Group 3/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  Group /general/extracellular_ephys/Group 4 (ElectrodeGroup) no description
  Group /general/extracellular_ephys/Group 4/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/channel_name (VectorData) unique channel reference | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/gain_to_uV (VectorData) no description | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (32,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/rel_x (VectorData) rel_x | shape = (32,) | dtype = float32
  Dataset /general/extracellular_ephys/electrodes/rel_y (VectorData) rel_y | shape = (32,) | dtype = float32
  institution: Princeton
  keywords: ['Development of the nervous system' 'Hippocampus' 'Neural circuits']
  lab: Buzsaki
  Group /general/optogenetics/OptogeneticStimulusSite3 (OptogeneticStimulusSite) 
  Group /general/optogenetics/OptogeneticStimulusSite3/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  Group /general/optogenetics/OptogeneticStimulusSite4 (OptogeneticStimulusSite) 
  Group /general/optogenetics/OptogeneticStimulusSite4/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  Group /general/optogenetics/OptogeneticStimulusSite5 (OptogeneticStimulusSite) 
  Group /general/optogenetics/OptogeneticStimulusSite5/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  Group /general/optogenetics/OptogeneticStimulusSite6 (OptogeneticStimulusSite) 
  Group /general/optogenetics/OptogeneticStimulusSite6/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  Group /general/optogenetics/OptogeneticStimulusSite7 (OptogeneticStimulusSite) 
  Group /general/optogenetics/OptogeneticStimulusSite7/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  Group /general/optogenetics/OptogeneticStimulusSite8 (OptogeneticStimulusSite) 
  Group /general/optogenetics/OptogeneticStimulusSite8/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  related_publications: ['https://doi.org/10.1126/science.abm1891']
  session_id: fCamk1_200827_sess9_no_raw_data
  Group /general/subject (Subject) 
  identifier: d725048f-8c8b-423f-8ccd-671aa9c719b8
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/behavioral_paradigm (VectorData) The behavioral paradigm of the epoch | shape = (5,) | dtype = object
  Dataset /intervals/epochs/environment (VectorData) The environment in the epoch | shape = (5,) | dtype = object
  Dataset /intervals/epochs/epoch_name (VectorData) The name of the epoch | shape = (5,) | dtype = object
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (5,) | dtype = int64
  Dataset /intervals/epochs/manipulation (VectorData) The stimulus in the epoch | shape = (5,) | dtype = object
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (5,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (5,) | dtype = float64
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (111,) | dtype = int64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (111,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (111,) | dtype = float64
  Dataset /intervals/trials/visited_arm (VectorData) Which side of the linear track was visited | shape = (111,) | dtype = uint8
  Group /processing/behavior (ProcessingModule) Tracking data obtained from positional tracking in video
  Group /processing/behavior/LinearMazePositionTracking (Position) 
  Group /processing/behavior/LinearMazePositionTracking/SpatiaLSeriesLinearized (SpatialSeries) Linearized position of the subject on the track.
  Group /processing/behavior/LinearMazePositionTracking/SpatialSeriesRaw (SpatialSeries) (x,y) coordinates tracking subject movement from above with camera on a PVC linear track (110 cm long, 6.35 cm wide)
  Group /processing/behavior/RewardEventsLinearTrack (LabeledEvents) rewards in the linear track
  Group /processing/behavior/SleepStates (TimeIntervals) Description of states : {
      "WAKEstate": "Waked and in locomotion",
      "NREMstate": "Non-REM sleep",
      "REMstate": "Rapid eye movement sleep",
      "WAKEtheta": "Wake with theta",
      "WAKEnontheta": "Wake without theta",
      "WAKEtheta_ThDt": "Wake with theta, estimated with higher theta/delta ratio",
      "REMtheta_ThDt": "REM sleep with theta, estimated with higher theta/delta ratio",
      "QWake_ThDt": "Quiet wakefulness esimated with higher theta/delta ratio",
      "QWake_noRipples_ThDt": "Quite wakefulness without ripples, estimated with higher theta/delta ratio",
      "NREM_ThDt": "Non-REM sleep, estimated with higher theta/delta ratio",
      "NREM_noRipples_ThDt": "Non-REM sleep without ripples, estimated with higher theta/delta ratio"
  }
  Dataset /processing/behavior/SleepStates/id (ElementIdentifiers)  | shape = (6702,) | dtype = int64
  Dataset /processing/behavior/SleepStates/label (VectorData) Sleep state. | shape = (6702,) | dtype = object
  Dataset /processing/behavior/SleepStates/start_time (VectorData) Start time of epoch, in seconds | shape = (6702,) | dtype = float64
  Dataset /processing/behavior/SleepStates/stop_time (VectorData) Stop time of epoch, in seconds | shape = (6702,) | dtype = float64
  Group /processing/behavior/UpDownStatesTimeIntervals (TimeIntervals) Up and Down states are a phenomenon observed in neurons, predominantly in the cerebral cortex, where they spontaneously fluctuate between periods of high (Up state) and low (Down state) activity. The Up state is characterized by a high rate of neuronal firing and depolarized membrane potentials, indicating active information processing. Conversely, the Down state is associated with a low rate of neuronal firing and hyperpolarized membrane potentials, suggesting a resting or inactive phase.
  
  Detection parameters:
  {
      "ch": 26,
      "spikeThreshold": 0.25,
      "gamm_thr": 0.5,
      "down_thr": 0,
      "deltaWaveThreshold": 0
  }
  Dataset /processing/behavior/UpDownStatesTimeIntervals/id (ElementIdentifiers)  | shape = (5421,) | dtype = int64
  Dataset /processing/behavior/UpDownStatesTimeIntervals/start_time (VectorData) Start time of epoch, in seconds | shape = (5421,) | dtype = float64
  Dataset /processing/behavior/UpDownStatesTimeIntervals/state (VectorData) UP or DOWN state | shape = (5421,) | dtype = object
  Dataset /processing/behavior/UpDownStatesTimeIntervals/stop_time (VectorData) Stop time of epoch, in seconds | shape = (5421,) | dtype = float64
  Group /processing/ecephys (ProcessingModule) No description.
  Group /processing/ecephys/HSETimeIntervals (TimeIntervals) High synchrony events
  Dataset /processing/ecephys/HSETimeIntervals/center_time (VectorData) The time of the center | shape = (3952,) | dtype = float64
  Dataset /processing/ecephys/HSETimeIntervals/id (ElementIdentifiers)  | shape = (3952,) | dtype = int64
  Dataset /processing/ecephys/HSETimeIntervals/peak_time (VectorData) The time of the peak | shape = (3952,) | dtype = float64
  Dataset /processing/ecephys/HSETimeIntervals/start_time (VectorData) Start time of epoch, in seconds | shape = (3952,) | dtype = float64
  Dataset /processing/ecephys/HSETimeIntervals/stop_time (VectorData) Stop time of epoch, in seconds | shape = (3952,) | dtype = float64
  Group /processing/ecephys/RippleTimeIntervals (TimeIntervals) Ripples and their metrics
  Dataset /processing/ecephys/RippleTimeIntervals/id (ElementIdentifiers)  | shape = (4315,) | dtype = int64
  Dataset /processing/ecephys/RippleTimeIntervals/peak_amplitudes (VectorData) Peak amplitude of the ripple. | shape = (4315,) | dtype = float64
  Dataset /processing/ecephys/RippleTimeIntervals/peak_frequencies (VectorData) Peak frequency of the ripple. | shape = (4315,) | dtype = float64
  Dataset /processing/ecephys/RippleTimeIntervals/peak_normed_power (VectorData) Normed power of the peak. | shape = (4315,) | dtype = float64
  Dataset /processing/ecephys/RippleTimeIntervals/peak_time (VectorData) Time at which the ripple peaked. | shape = (4315,) | dtype = float64
  Dataset /processing/ecephys/RippleTimeIntervals/ripple_amplitudes (VectorData) Amplitude of each point on the ripple. | shape = (4315, 187) | dtype = float64
  Dataset /processing/ecephys/RippleTimeIntervals/ripple_amplitudes_index (VectorIndex) Index for VectorData 'ripple_amplitudes' | shape = (4315,) | dtype = uint16
  Dataset /processing/ecephys/RippleTimeIntervals/ripple_durations (VectorData) Duration of the ripple event. | shape = (4315,) | dtype = float64
  Dataset /processing/ecephys/RippleTimeIntervals/ripple_frequencies (VectorData) Frequency of each point on the ripple. | shape = (4315, 187) | dtype = float64
  Dataset /processing/ecephys/RippleTimeIntervals/ripple_frequencies_index (VectorIndex) Index for VectorData 'ripple_frequencies' | shape = (4315,) | dtype = uint16
  Dataset /processing/ecephys/RippleTimeIntervals/ripple_phases (VectorData) Phase of each point on the ripple. | shape = (4315, 187) | dtype = float64
  Dataset /processing/ecephys/RippleTimeIntervals/ripple_phases_index (VectorIndex) Index for VectorData 'ripple_phases' | shape = (4315,) | dtype = uint16
  Dataset /processing/ecephys/RippleTimeIntervals/ripple_raw (VectorData) Extracted ripple data. | shape = (4315, 187) | dtype = int16
  Dataset /processing/ecephys/RippleTimeIntervals/ripple_raw_index (VectorIndex) Index for VectorData 'ripple_raw' | shape = (4315,) | dtype = uint16
  Dataset /processing/ecephys/RippleTimeIntervals/start_time (VectorData) Start time of epoch, in seconds | shape = (4315,) | dtype = float64
  Dataset /processing/ecephys/RippleTimeIntervals/stop_time (VectorData) Stop time of epoch, in seconds | shape = (4315,) | dtype = float64
  session_description: Understanding how excitatory (E) and inhibitory (I) inputs are integrated by neurons requires monitoring their subthreshold behavior. We probed the subthreshold dynamics using optogenetic depolarizing pulses in hippocampal neuronal assemblies in freely moving mice. Excitability decreased during sharp-wave ripples coupled with increased I. In contrast to this “negative gain,” optogenetic probing showed increased within-field excitability in place cells by weakening I and unmasked stable place fields in initially non–place cells. Neuronal assemblies active during sharp-wave ripples in the home cage predicted spatial overlap and sequences of place fields of both place cells and unmasked preexisting place fields of non–place cells during track running. Thus, indirect probing of subthreshold dynamics in neuronal populations permits the disclosing of preexisting assemblies and modes of neuronal operations.
  session_start_time: 2016-03-15T00:00:00-04:00
  Group /stimulus/presentation/OptogeneticSeriesSite3 (OptogeneticSeries) μLEDs were controlled with current (2-4.5 μA generating 0.02-0.1μW of total light power;ref (15)) provided by a 12-channel current generator (OSC1Lite, NeuroNex Michigan Hub)driven by an Arduino, which delivered trapezoid (1ms rise time)blue light (centered emission at 460 nm, emission surface area = 150 mm2) 20 ms pulses atrandom sites with a randomly variable (40-60ms) offset
  Group /stimulus/presentation/OptogeneticSeriesSite3/site (OptogeneticStimulusSite) 
  Group /stimulus/presentation/OptogeneticSeriesSite3/site/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  Group /stimulus/presentation/OptogeneticSeriesSite4 (OptogeneticSeries) μLEDs were controlled with current (2-4.5 μA generating 0.02-0.1μW of total light power;ref (15)) provided by a 12-channel current generator (OSC1Lite, NeuroNex Michigan Hub)driven by an Arduino, which delivered trapezoid (1ms rise time)blue light (centered emission at 460 nm, emission surface area = 150 mm2) 20 ms pulses atrandom sites with a randomly variable (40-60ms) offset
  Group /stimulus/presentation/OptogeneticSeriesSite4/site (OptogeneticStimulusSite) 
  Group /stimulus/presentation/OptogeneticSeriesSite4/site/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  Group /stimulus/presentation/OptogeneticSeriesSite5 (OptogeneticSeries) μLEDs were controlled with current (2-4.5 μA generating 0.02-0.1μW of total light power;ref (15)) provided by a 12-channel current generator (OSC1Lite, NeuroNex Michigan Hub)driven by an Arduino, which delivered trapezoid (1ms rise time)blue light (centered emission at 460 nm, emission surface area = 150 mm2) 20 ms pulses atrandom sites with a randomly variable (40-60ms) offset
  Group /stimulus/presentation/OptogeneticSeriesSite5/site (OptogeneticStimulusSite) 
  Group /stimulus/presentation/OptogeneticSeriesSite5/site/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  Group /stimulus/presentation/OptogeneticSeriesSite6 (OptogeneticSeries) μLEDs were controlled with current (2-4.5 μA generating 0.02-0.1μW of total light power;ref (15)) provided by a 12-channel current generator (OSC1Lite, NeuroNex Michigan Hub)driven by an Arduino, which delivered trapezoid (1ms rise time)blue light (centered emission at 460 nm, emission surface area = 150 mm2) 20 ms pulses atrandom sites with a randomly variable (40-60ms) offset
  Group /stimulus/presentation/OptogeneticSeriesSite6/site (OptogeneticStimulusSite) 
  Group /stimulus/presentation/OptogeneticSeriesSite6/site/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  Group /stimulus/presentation/OptogeneticSeriesSite7 (OptogeneticSeries) μLEDs were controlled with current (2-4.5 μA generating 0.02-0.1μW of total light power;ref (15)) provided by a 12-channel current generator (OSC1Lite, NeuroNex Michigan Hub)driven by an Arduino, which delivered trapezoid (1ms rise time)blue light (centered emission at 460 nm, emission surface area = 150 mm2) 20 ms pulses atrandom sites with a randomly variable (40-60ms) offset
  Group /stimulus/presentation/OptogeneticSeriesSite7/site (OptogeneticStimulusSite) 
  Group /stimulus/presentation/OptogeneticSeriesSite7/site/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  Group /stimulus/presentation/OptogeneticSeriesSite8 (OptogeneticSeries) μLEDs were controlled with current (2-4.5 μA generating 0.02-0.1μW of total light power;ref (15)) provided by a 12-channel current generator (OSC1Lite, NeuroNex Michigan Hub)driven by an Arduino, which delivered trapezoid (1ms rise time)blue light (centered emission at 460 nm, emission surface area = 150 mm2) 20 ms pulses atrandom sites with a randomly variable (40-60ms) offset
  Group /stimulus/presentation/OptogeneticSeriesSite8/site (OptogeneticStimulusSite) 
  Group /stimulus/presentation/OptogeneticSeriesSite8/site/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  timestamps_reference_time: 2016-03-15T00:00:00-04:00
  Group /units (Units) Autogenerated by neuroconv.
  Dataset /units/clu_id (VectorData) 0-indexed id of cluster identified from the shank. | shape = (57,) | dtype = float64
  Dataset /units/group_id (VectorData) The electrode group ID that each unit was identified by. | shape = (57,) | dtype = object
  Dataset /units/id (ElementIdentifiers)  | shape = (57,) | dtype = int64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (2259343,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (57,) | dtype = uint32
  Dataset /units/unit_name (VectorData) Unique reference for each unit. | shape = (57,) | dtype = object


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeries (ElectricalSeries) Acquisition traces for the ElectricalSeries.
  Dataset /acquisition/ElectricalSeries/electrodes (DynamicTableRegion) electrode_table_region | shape = (32,) | dtype = int64
  Group /acquisition/ImageSeriesTrackingVideo1 (ImageSeries) Video recorded with Basler camera.
  file_create_date: ['2023-06-28T19:02:22.407431+02:00']
  Group /general/devices/N1-F21-O36 | 18 (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  experiment_description: Probing subthreshold dynamics of hippocampal neurons by pulsed optogenetics
  experimenter: ['Valero, Manuel' 'Zutshi, Ipshita' 'Yoon, Euisik' 'Buzsáki, György']
  Group /general/extracellular_ephys/Group 1 (ElectrodeGroup) no description
  Group /general/extracellular_ephys/Group 1/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  Group /general/extracellular_ephys/Group 2 (ElectrodeGroup) no description
  Group /general/extracellular_ephys/Group 2/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  Group /general/extracellular_ephys/Group 3 (ElectrodeGroup) no description
  Group /general/extracellular_ephys/Group 3/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  Group /general/extracellular_ephys/Group 4 (ElectrodeGroup) no description
  Group /general/extracellular_ephys/Group 4/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/channel_name (VectorData) unique channel reference | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/gain_to_uV (VectorData) no description | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (32,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/rel_x (VectorData) rel_x | shape = (32,) | dtype = float32
  Dataset /general/extracellular_ephys/electrodes/rel_y (VectorData) rel_y | shape = (32,) | dtype = float32
  institution: Princeton
  keywords: ['Development of the nervous system' 'Hippocampus' 'Neural circuits']
  lab: Buzsaki
  Group /general/optogenetics/OptogeneticStimulusSite3 (OptogeneticStimulusSite) 
  Group /general/optogenetics/OptogeneticStimulusSite3/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  Group /general/optogenetics/OptogeneticStimulusSite4 (OptogeneticStimulusSite) 
  Group /general/optogenetics/OptogeneticStimulusSite4/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  Group /general/optogenetics/OptogeneticStimulusSite5 (OptogeneticStimulusSite) 
  Group /general/optogenetics/OptogeneticStimulusSite5/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  Group /general/optogenetics/OptogeneticStimulusSite6 (OptogeneticStimulusSite) 
  Group /general/optogenetics/OptogeneticStimulusSite6/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  Group /general/optogenetics/OptogeneticStimulusSite7 (OptogeneticStimulusSite) 
  Group /general/optogenetics/OptogeneticStimulusSite7/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  Group /general/optogenetics/OptogeneticStimulusSite8 (OptogeneticStimulusSite) 
  Group /general/optogenetics/OptogeneticStimulusSite8/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  related_publications: ['https://doi.org/10.1126/science.abm1891']
  session_id: fCamk1_200827_sess9
  Group /general/subject (Subject) 
  identifier: cb989d60-2819-4cd5-ac25-1488cabe270f
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/behavioral_paradigm (VectorData) The behavioral paradigm of the epoch | shape = (5,) | dtype = object
  Dataset /intervals/epochs/environment (VectorData) The environment in the epoch | shape = (5,) | dtype = object
  Dataset /intervals/epochs/epoch_name (VectorData) The name of the epoch | shape = (5,) | dtype = object
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (5,) | dtype = int64
  Dataset /intervals/epochs/manipulation (VectorData) The stimulus in the epoch | shape = (5,) | dtype = object
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (5,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (5,) | dtype = float64
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (111,) | dtype = int64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (111,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (111,) | dtype = float64
  Dataset /intervals/trials/visited_arm (VectorData) Which side of the linear track was visited | shape = (111,) | dtype = uint8
  Group /processing/behavior (ProcessingModule) Tracking data obtained from positional tracking in video
  Group /processing/behavior/LinearMazePositionTracking (Position) 
  Group /processing/behavior/LinearMazePositionTracking/SpatiaLSeriesLinearized (SpatialSeries) Linearized position of the subject on the track.
  Group /processing/behavior/LinearMazePositionTracking/SpatialSeriesRaw (SpatialSeries) (x,y) coordinates tracking subject movement from above with camera on a PVC linear track (110 cm long, 6.35 cm wide)
  Group /processing/behavior/RewardEventsLinearTrack (LabeledEvents) rewards in the linear track
  Group /processing/behavior/SleepStates (TimeIntervals) Description of states : {
      "WAKEstate": "Waked and in locomotion",
      "NREMstate": "Non-REM sleep",
      "REMstate": "Rapid eye movement sleep",
      "WAKEtheta": "Wake with theta",
      "WAKEnontheta": "Wake without theta",
      "WAKEtheta_ThDt": "Wake with theta, estimated with higher theta/delta ratio",
      "REMtheta_ThDt": "REM sleep with theta, estimated with higher theta/delta ratio",
      "QWake_ThDt": "Quiet wakefulness esimated with higher theta/delta ratio",
      "QWake_noRipples_ThDt": "Quite wakefulness without ripples, estimated with higher theta/delta ratio",
      "NREM_ThDt": "Non-REM sleep, estimated with higher theta/delta ratio",
      "NREM_noRipples_ThDt": "Non-REM sleep without ripples, estimated with higher theta/delta ratio"
  }
  Dataset /processing/behavior/SleepStates/id (ElementIdentifiers)  | shape = (6702,) | dtype = int64
  Dataset /processing/behavior/SleepStates/label (VectorData) Sleep state. | shape = (6702,) | dtype = object
  Dataset /processing/behavior/SleepStates/start_time (VectorData) Start time of epoch, in seconds | shape = (6702,) | dtype = float64
  Dataset /processing/behavior/SleepStates/stop_time (VectorData) Stop time of epoch, in seconds | shape = (6702,) | dtype = float64
  Group /processing/behavior/UpDownStatesTimeIntervals (TimeIntervals) Up and Down states are a phenomenon observed in neurons, predominantly in the cerebral cortex, where they spontaneously fluctuate between periods of high (Up state) and low (Down state) activity. The Up state is characterized by a high rate of neuronal firing and depolarized membrane potentials, indicating active information processing. Conversely, the Down state is associated with a low rate of neuronal firing and hyperpolarized membrane potentials, suggesting a resting or inactive phase.
  
  Detection parameters:
  {
      "ch": 26,
      "spikeThreshold": 0.25,
      "gamm_thr": 0.5,
      "down_thr": 0,
      "deltaWaveThreshold": 0
  }
  Dataset /processing/behavior/UpDownStatesTimeIntervals/id (ElementIdentifiers)  | shape = (5421,) | dtype = int64
  Dataset /processing/behavior/UpDownStatesTimeIntervals/start_time (VectorData) Start time of epoch, in seconds | shape = (5421,) | dtype = float64
  Dataset /processing/behavior/UpDownStatesTimeIntervals/state (VectorData) UP or DOWN state | shape = (5421,) | dtype = object
  Dataset /processing/behavior/UpDownStatesTimeIntervals/stop_time (VectorData) Stop time of epoch, in seconds | shape = (5421,) | dtype = float64
  Group /processing/ecephys (ProcessingModule) Intermediate data from extracellular electrophysiology recordings, e.g., LFP.
  Group /processing/ecephys/HSETimeIntervals (TimeIntervals) High synchrony events
  Dataset /processing/ecephys/HSETimeIntervals/center_time (VectorData) The time of the center | shape = (3952,) | dtype = float64
  Dataset /processing/ecephys/HSETimeIntervals/id (ElementIdentifiers)  | shape = (3952,) | dtype = int64
  Dataset /processing/ecephys/HSETimeIntervals/peak_time (VectorData) The time of the peak | shape = (3952,) | dtype = float64
  Dataset /processing/ecephys/HSETimeIntervals/start_time (VectorData) Start time of epoch, in seconds | shape = (3952,) | dtype = float64
  Dataset /processing/ecephys/HSETimeIntervals/stop_time (VectorData) Stop time of epoch, in seconds | shape = (3952,) | dtype = float64
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/ElectricalSeriesLFP (ElectricalSeries) Acquisition traces for the ElectricalSeriesLFP.
  Dataset /processing/ecephys/LFP/ElectricalSeriesLFP/electrodes (DynamicTableRegion) electrode_table_region | shape = (32,) | dtype = int64
  Group /processing/ecephys/RippleTimeIntervals (TimeIntervals) Ripples and their metrics
  Dataset /processing/ecephys/RippleTimeIntervals/id (ElementIdentifiers)  | shape = (4315,) | dtype = int64
  Dataset /processing/ecephys/RippleTimeIntervals/peak_amplitudes (VectorData) Peak amplitude of the ripple. | shape = (4315,) | dtype = float64
  Dataset /processing/ecephys/RippleTimeIntervals/peak_frequencies (VectorData) Peak frequency of the ripple. | shape = (4315,) | dtype = float64
  Dataset /processing/ecephys/RippleTimeIntervals/peak_normed_power (VectorData) Normed power of the peak. | shape = (4315,) | dtype = float64
  Dataset /processing/ecephys/RippleTimeIntervals/peak_time (VectorData) Time at which the ripple peaked. | shape = (4315,) | dtype = float64
  Dataset /processing/ecephys/RippleTimeIntervals/ripple_amplitudes (VectorData) Amplitude of each point on the ripple. | shape = (4315, 187) | dtype = float64
  Dataset /processing/ecephys/RippleTimeIntervals/ripple_amplitudes_index (VectorIndex) Index for VectorData 'ripple_amplitudes' | shape = (4315,) | dtype = uint16
  Dataset /processing/ecephys/RippleTimeIntervals/ripple_durations (VectorData) Duration of the ripple event. | shape = (4315,) | dtype = float64
  Dataset /processing/ecephys/RippleTimeIntervals/ripple_frequencies (VectorData) Frequency of each point on the ripple. | shape = (4315, 187) | dtype = float64
  Dataset /processing/ecephys/RippleTimeIntervals/ripple_frequencies_index (VectorIndex) Index for VectorData 'ripple_frequencies' | shape = (4315,) | dtype = uint16
  Dataset /processing/ecephys/RippleTimeIntervals/ripple_phases (VectorData) Phase of each point on the ripple. | shape = (4315, 187) | dtype = float64
  Dataset /processing/ecephys/RippleTimeIntervals/ripple_phases_index (VectorIndex) Index for VectorData 'ripple_phases' | shape = (4315,) | dtype = uint16
  Dataset /processing/ecephys/RippleTimeIntervals/ripple_raw (VectorData) Extracted ripple data. | shape = (4315, 187) | dtype = int16
  Dataset /processing/ecephys/RippleTimeIntervals/ripple_raw_index (VectorIndex) Index for VectorData 'ripple_raw' | shape = (4315,) | dtype = uint16
  Dataset /processing/ecephys/RippleTimeIntervals/start_time (VectorData) Start time of epoch, in seconds | shape = (4315,) | dtype = float64
  Dataset /processing/ecephys/RippleTimeIntervals/stop_time (VectorData) Stop time of epoch, in seconds | shape = (4315,) | dtype = float64
  session_description: Understanding how excitatory (E) and inhibitory (I) inputs are integrated by neurons requires monitoring their subthreshold behavior. We probed the subthreshold dynamics using optogenetic depolarizing pulses in hippocampal neuronal assemblies in freely moving mice. Excitability decreased during sharp-wave ripples coupled with increased I. In contrast to this “negative gain,” optogenetic probing showed increased within-field excitability in place cells by weakening I and unmasked stable place fields in initially non–place cells. Neuronal assemblies active during sharp-wave ripples in the home cage predicted spatial overlap and sequences of place fields of both place cells and unmasked preexisting place fields of non–place cells during track running. Thus, indirect probing of subthreshold dynamics in neuronal populations permits the disclosing of preexisting assemblies and modes of neuronal operations.
  session_start_time: 2016-03-15T00:00:00-04:00
  Group /stimulus/presentation/OptogeneticSeriesSite3 (OptogeneticSeries) μLEDs were controlled with current (2-4.5 μA generating 0.02-0.1μW of total light power;ref (15)) provided by a 12-channel current generator (OSC1Lite, NeuroNex Michigan Hub)driven by an Arduino, which delivered trapezoid (1ms rise time)blue light (centered emission at 460 nm, emission surface area = 150 mm2) 20 ms pulses atrandom sites with a randomly variable (40-60ms) offset
  Group /stimulus/presentation/OptogeneticSeriesSite3/site (OptogeneticStimulusSite) 
  Group /stimulus/presentation/OptogeneticSeriesSite3/site/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  Group /stimulus/presentation/OptogeneticSeriesSite4 (OptogeneticSeries) μLEDs were controlled with current (2-4.5 μA generating 0.02-0.1μW of total light power;ref (15)) provided by a 12-channel current generator (OSC1Lite, NeuroNex Michigan Hub)driven by an Arduino, which delivered trapezoid (1ms rise time)blue light (centered emission at 460 nm, emission surface area = 150 mm2) 20 ms pulses atrandom sites with a randomly variable (40-60ms) offset
  Group /stimulus/presentation/OptogeneticSeriesSite4/site (OptogeneticStimulusSite) 
  Group /stimulus/presentation/OptogeneticSeriesSite4/site/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  Group /stimulus/presentation/OptogeneticSeriesSite5 (OptogeneticSeries) μLEDs were controlled with current (2-4.5 μA generating 0.02-0.1μW of total light power;ref (15)) provided by a 12-channel current generator (OSC1Lite, NeuroNex Michigan Hub)driven by an Arduino, which delivered trapezoid (1ms rise time)blue light (centered emission at 460 nm, emission surface area = 150 mm2) 20 ms pulses atrandom sites with a randomly variable (40-60ms) offset
  Group /stimulus/presentation/OptogeneticSeriesSite5/site (OptogeneticStimulusSite) 
  Group /stimulus/presentation/OptogeneticSeriesSite5/site/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  Group /stimulus/presentation/OptogeneticSeriesSite6 (OptogeneticSeries) μLEDs were controlled with current (2-4.5 μA generating 0.02-0.1μW of total light power;ref (15)) provided by a 12-channel current generator (OSC1Lite, NeuroNex Michigan Hub)driven by an Arduino, which delivered trapezoid (1ms rise time)blue light (centered emission at 460 nm, emission surface area = 150 mm2) 20 ms pulses atrandom sites with a randomly variable (40-60ms) offset
  Group /stimulus/presentation/OptogeneticSeriesSite6/site (OptogeneticStimulusSite) 
  Group /stimulus/presentation/OptogeneticSeriesSite6/site/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  Group /stimulus/presentation/OptogeneticSeriesSite7 (OptogeneticSeries) μLEDs were controlled with current (2-4.5 μA generating 0.02-0.1μW of total light power;ref (15)) provided by a 12-channel current generator (OSC1Lite, NeuroNex Michigan Hub)driven by an Arduino, which delivered trapezoid (1ms rise time)blue light (centered emission at 460 nm, emission surface area = 150 mm2) 20 ms pulses atrandom sites with a randomly variable (40-60ms) offset
  Group /stimulus/presentation/OptogeneticSeriesSite7/site (OptogeneticStimulusSite) 
  Group /stimulus/presentation/OptogeneticSeriesSite7/site/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  Group /stimulus/presentation/OptogeneticSeriesSite8 (OptogeneticSeries) μLEDs were controlled with current (2-4.5 μA generating 0.02-0.1μW of total light power;ref (15)) provided by a 12-channel current generator (OSC1Lite, NeuroNex Michigan Hub)driven by an Arduino, which delivered trapezoid (1ms rise time)blue light (centered emission at 460 nm, emission surface area = 150 mm2) 20 ms pulses atrandom sites with a randomly variable (40-60ms) offset
  Group /stimulus/presentation/OptogeneticSeriesSite8/site (OptogeneticStimulusSite) 
  Group /stimulus/presentation/OptogeneticSeriesSite8/site/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  timestamps_reference_time: 2016-03-15T00:00:00-04:00
  Group /units (Units) Autogenerated by neuroconv.
  Dataset /units/clu_id (VectorData) 0-indexed id of cluster identified from the shank. | shape = (57,) | dtype = float64
  Dataset /units/group_id (VectorData) The electrode group ID that each unit was identified by. | shape = (57,) | dtype = object
  Dataset /units/id (ElementIdentifiers)  | shape = (57,) | dtype = int64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (2259343,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (57,) | dtype = uint32
  Dataset /units/unit_name (VectorData) Unique reference for each unit. | shape = (57,) | dtype = object


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ImageSeriesTrackingVideo1 (ImageSeries) Video recorded with Basler camera.
  file_create_date: ['2023-07-04T16:49:31.509575+02:00']
  Group /general/devices/N1-F21-O36 | 18 (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  experiment_description: Probing subthreshold dynamics of hippocampal neurons by pulsed optogenetics
  experimenter: ['Valero, Manuel' 'Zutshi, Ipshita' 'Yoon, Euisik' 'Buzsáki, György']
  Group /general/extracellular_ephys/Group 1 (ElectrodeGroup) no description
  Group /general/extracellular_ephys/Group 1/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  Group /general/extracellular_ephys/Group 2 (ElectrodeGroup) no description
  Group /general/extracellular_ephys/Group 2/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  Group /general/extracellular_ephys/Group 3 (ElectrodeGroup) no description
  Group /general/extracellular_ephys/Group 3/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  Group /general/extracellular_ephys/Group 4 (ElectrodeGroup) no description
  Group /general/extracellular_ephys/Group 4/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/channel_name (VectorData) unique channel reference | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/gain_to_uV (VectorData) no description | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (32,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/rel_x (VectorData) rel_x | shape = (32,) | dtype = float32
  Dataset /general/extracellular_ephys/electrodes/rel_y (VectorData) rel_y | shape = (32,) | dtype = float32
  institution: Princeton
  keywords: ['Development of the nervous system' 'Hippocampus' 'Neural circuits']
  lab: Buzsaki
  Group /general/optogenetics/OptogeneticStimulusSite3 (OptogeneticStimulusSite) 
  Group /general/optogenetics/OptogeneticStimulusSite3/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  Group /general/optogenetics/OptogeneticStimulusSite4 (OptogeneticStimulusSite) 
  Group /general/optogenetics/OptogeneticStimulusSite4/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  Group /general/optogenetics/OptogeneticStimulusSite5 (OptogeneticStimulusSite) 
  Group /general/optogenetics/OptogeneticStimulusSite5/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  Group /general/optogenetics/OptogeneticStimulusSite6 (OptogeneticStimulusSite) 
  Group /general/optogenetics/OptogeneticStimulusSite6/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  Group /general/optogenetics/OptogeneticStimulusSite7 (OptogeneticStimulusSite) 
  Group /general/optogenetics/OptogeneticStimulusSite7/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  Group /general/optogenetics/OptogeneticStimulusSite8 (OptogeneticStimulusSite) 
  Group /general/optogenetics/OptogeneticStimulusSite8/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  related_publications: ['https://doi.org/10.1126/science.abm1891']
  session_id: fCamk1_200901_sess12_no_raw_data
  Group /general/subject (Subject) 
  identifier: 155b9d4d-ef37-4e28-ad9e-09ed41da976f
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/behavioral_paradigm (VectorData) The behavioral paradigm of the epoch | shape = (5,) | dtype = object
  Dataset /intervals/epochs/environment (VectorData) The environment in the epoch | shape = (5,) | dtype = object
  Dataset /intervals/epochs/epoch_name (VectorData) The name of the epoch | shape = (5,) | dtype = object
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (5,) | dtype = int64
  Dataset /intervals/epochs/manipulation (VectorData) The stimulus in the epoch | shape = (5,) | dtype = object
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (5,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (5,) | dtype = float64
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (132,) | dtype = int64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (132,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (132,) | dtype = float64
  Dataset /intervals/trials/visited_arm (VectorData) Which side of the linear track was visited | shape = (132,) | dtype = uint8
  Group /processing/behavior (ProcessingModule) Tracking data obtained from positional tracking in video
  Group /processing/behavior/LinearMazePositionTracking (Position) 
  Group /processing/behavior/LinearMazePositionTracking/SpatiaLSeriesLinearized (SpatialSeries) Linearized position of the subject on the track.
  Group /processing/behavior/LinearMazePositionTracking/SpatialSeriesRaw (SpatialSeries) (x,y) coordinates tracking subject movement from above with camera on a PVC linear track (110 cm long, 6.35 cm wide)
  Group /processing/behavior/RewardEventsLinearTrack (LabeledEvents) rewards in the linear track
  Group /processing/behavior/SleepStates (TimeIntervals) Description of states : {
      "WAKEstate": "Waked and in locomotion",
      "NREMstate": "Non-REM sleep",
      "REMstate": "Rapid eye movement sleep",
      "WAKEtheta": "Wake with theta",
      "WAKEnontheta": "Wake without theta",
      "WAKEtheta_ThDt": "Wake with theta, estimated with higher theta/delta ratio",
      "REMtheta_ThDt": "REM sleep with theta, estimated with higher theta/delta ratio",
      "QWake_ThDt": "Quiet wakefulness esimated with higher theta/delta ratio",
      "QWake_noRipples_ThDt": "Quite wakefulness without ripples, estimated with higher theta/delta ratio",
      "NREM_ThDt": "Non-REM sleep, estimated with higher theta/delta ratio",
      "NREM_noRipples_ThDt": "Non-REM sleep without ripples, estimated with higher theta/delta ratio"
  }
  Dataset /processing/behavior/SleepStates/id (ElementIdentifiers)  | shape = (5602,) | dtype = int64
  Dataset /processing/behavior/SleepStates/label (VectorData) Sleep state. | shape = (5602,) | dtype = object
  Dataset /processing/behavior/SleepStates/start_time (VectorData) Start time of epoch, in seconds | shape = (5602,) | dtype = float64
  Dataset /processing/behavior/SleepStates/stop_time (VectorData) Stop time of epoch, in seconds | shape = (5602,) | dtype = float64
  Group /processing/ecephys (ProcessingModule) No description.
  Group /processing/ecephys/RippleTimeIntervals (TimeIntervals) Ripples and their metrics
  Dataset /processing/ecephys/RippleTimeIntervals/id (ElementIdentifiers)  | shape = (1796,) | dtype = int64
  Dataset /processing/ecephys/RippleTimeIntervals/peak_amplitudes (VectorData) Peak amplitude of the ripple. | shape = (1796,) | dtype = float64
  Dataset /processing/ecephys/RippleTimeIntervals/peak_frequencies (VectorData) Peak frequency of the ripple. | shape = (1796,) | dtype = float64
  Dataset /processing/ecephys/RippleTimeIntervals/peak_normed_power (VectorData) Normed power of the peak. | shape = (1796,) | dtype = float64
  Dataset /processing/ecephys/RippleTimeIntervals/peak_time (VectorData) Time at which the ripple peaked. | shape = (1796,) | dtype = float64
  Dataset /processing/ecephys/RippleTimeIntervals/ripple_amplitudes (VectorData) Amplitude of each point on the ripple. | shape = (1796, 187) | dtype = float64
  Dataset /processing/ecephys/RippleTimeIntervals/ripple_amplitudes_index (VectorIndex) Index for VectorData 'ripple_amplitudes' | shape = (1796,) | dtype = uint16
  Dataset /processing/ecephys/RippleTimeIntervals/ripple_durations (VectorData) Duration of the ripple event. | shape = (1796,) | dtype = float64
  Dataset /processing/ecephys/RippleTimeIntervals/ripple_frequencies (VectorData) Frequency of each point on the ripple. | shape = (1796, 187) | dtype = float64
  Dataset /processing/ecephys/RippleTimeIntervals/ripple_frequencies_index (VectorIndex) Index for VectorData 'ripple_frequencies' | shape = (1796,) | dtype = uint16
  Dataset /processing/ecephys/RippleTimeIntervals/ripple_phases (VectorData) Phase of each point on the ripple. | shape = (1796, 187) | dtype = float64
  Dataset /processing/ecephys/RippleTimeIntervals/ripple_phases_index (VectorIndex) Index for VectorData 'ripple_phases' | shape = (1796,) | dtype = uint16
  Dataset /processing/ecephys/RippleTimeIntervals/ripple_raw (VectorData) Extracted ripple data. | shape = (1796, 187) | dtype = int16
  Dataset /processing/ecephys/RippleTimeIntervals/ripple_raw_index (VectorIndex) Index for VectorData 'ripple_raw' | shape = (1796,) | dtype = uint16
  Dataset /processing/ecephys/RippleTimeIntervals/start_time (VectorData) Start time of epoch, in seconds | shape = (1796,) | dtype = float64
  Dataset /processing/ecephys/RippleTimeIntervals/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1796,) | dtype = float64
  session_description: Understanding how excitatory (E) and inhibitory (I) inputs are integrated by neurons requires monitoring their subthreshold behavior. We probed the subthreshold dynamics using optogenetic depolarizing pulses in hippocampal neuronal assemblies in freely moving mice. Excitability decreased during sharp-wave ripples coupled with increased I. In contrast to this “negative gain,” optogenetic probing showed increased within-field excitability in place cells by weakening I and unmasked stable place fields in initially non–place cells. Neuronal assemblies active during sharp-wave ripples in the home cage predicted spatial overlap and sequences of place fields of both place cells and unmasked preexisting place fields of non–place cells during track running. Thus, indirect probing of subthreshold dynamics in neuronal populations permits the disclosing of preexisting assemblies and modes of neuronal operations.
  session_start_time: 2016-03-15T00:00:00-04:00
  Group /stimulus/presentation/OptogeneticSeriesSite3 (OptogeneticSeries) μLEDs were controlled with current (2-4.5 μA generating 0.02-0.1μW of total light power;ref (15)) provided by a 12-channel current generator (OSC1Lite, NeuroNex Michigan Hub)driven by an Arduino, which delivered trapezoid (1ms rise time)blue light (centered emission at 460 nm, emission surface area = 150 mm2) 20 ms pulses atrandom sites with a randomly variable (40-60ms) offset
  Group /stimulus/presentation/OptogeneticSeriesSite3/site (OptogeneticStimulusSite) 
  Group /stimulus/presentation/OptogeneticSeriesSite3/site/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  Group /stimulus/presentation/OptogeneticSeriesSite4 (OptogeneticSeries) μLEDs were controlled with current (2-4.5 μA generating 0.02-0.1μW of total light power;ref (15)) provided by a 12-channel current generator (OSC1Lite, NeuroNex Michigan Hub)driven by an Arduino, which delivered trapezoid (1ms rise time)blue light (centered emission at 460 nm, emission surface area = 150 mm2) 20 ms pulses atrandom sites with a randomly variable (40-60ms) offset
  Group /stimulus/presentation/OptogeneticSeriesSite4/site (OptogeneticStimulusSite) 
  Group /stimulus/presentation/OptogeneticSeriesSite4/site/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  Group /stimulus/presentation/OptogeneticSeriesSite5 (OptogeneticSeries) μLEDs were controlled with current (2-4.5 μA generating 0.02-0.1μW of total light power;ref (15)) provided by a 12-channel current generator (OSC1Lite, NeuroNex Michigan Hub)driven by an Arduino, which delivered trapezoid (1ms rise time)blue light (centered emission at 460 nm, emission surface area = 150 mm2) 20 ms pulses atrandom sites with a randomly variable (40-60ms) offset
  Group /stimulus/presentation/OptogeneticSeriesSite5/site (OptogeneticStimulusSite) 
  Group /stimulus/presentation/OptogeneticSeriesSite5/site/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  Group /stimulus/presentation/OptogeneticSeriesSite6 (OptogeneticSeries) μLEDs were controlled with current (2-4.5 μA generating 0.02-0.1μW of total light power;ref (15)) provided by a 12-channel current generator (OSC1Lite, NeuroNex Michigan Hub)driven by an Arduino, which delivered trapezoid (1ms rise time)blue light (centered emission at 460 nm, emission surface area = 150 mm2) 20 ms pulses atrandom sites with a randomly variable (40-60ms) offset
  Group /stimulus/presentation/OptogeneticSeriesSite6/site (OptogeneticStimulusSite) 
  Group /stimulus/presentation/OptogeneticSeriesSite6/site/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  Group /stimulus/presentation/OptogeneticSeriesSite7 (OptogeneticSeries) μLEDs were controlled with current (2-4.5 μA generating 0.02-0.1μW of total light power;ref (15)) provided by a 12-channel current generator (OSC1Lite, NeuroNex Michigan Hub)driven by an Arduino, which delivered trapezoid (1ms rise time)blue light (centered emission at 460 nm, emission surface area = 150 mm2) 20 ms pulses atrandom sites with a randomly variable (40-60ms) offset
  Group /stimulus/presentation/OptogeneticSeriesSite7/site (OptogeneticStimulusSite) 
  Group /stimulus/presentation/OptogeneticSeriesSite7/site/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  Group /stimulus/presentation/OptogeneticSeriesSite8 (OptogeneticSeries) μLEDs were controlled with current (2-4.5 μA generating 0.02-0.1μW of total light power;ref (15)) provided by a 12-channel current generator (OSC1Lite, NeuroNex Michigan Hub)driven by an Arduino, which delivered trapezoid (1ms rise time)blue light (centered emission at 460 nm, emission surface area = 150 mm2) 20 ms pulses atrandom sites with a randomly variable (40-60ms) offset
  Group /stimulus/presentation/OptogeneticSeriesSite8/site (OptogeneticStimulusSite) 
  Group /stimulus/presentation/OptogeneticSeriesSite8/site/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  timestamps_reference_time: 2016-03-15T00:00:00-04:00
  Group /units (Units) Autogenerated by neuroconv.
  Dataset /units/clu_id (VectorData) 0-indexed id of cluster identified from the shank. | shape = (47,) | dtype = float64
  Dataset /units/group_id (VectorData) The electrode group ID that each unit was identified by. | shape = (47,) | dtype = object
  Dataset /units/id (ElementIdentifiers)  | shape = (47,) | dtype = int64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (1800735,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (47,) | dtype = uint32
  Dataset /units/unit_name (VectorData) Unique reference for each unit. | shape = (47,) | dtype = object


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeries (ElectricalSeries) Acquisition traces for the ElectricalSeries.
  Dataset /acquisition/ElectricalSeries/electrodes (DynamicTableRegion) electrode_table_region | shape = (32,) | dtype = int64
  Group /acquisition/ImageSeriesTrackingVideo1 (ImageSeries) Video recorded with Basler camera.
  file_create_date: ['2023-06-28T19:02:23.427171+02:00']
  Group /general/devices/N1-F21-O36 | 18 (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  experiment_description: Probing subthreshold dynamics of hippocampal neurons by pulsed optogenetics
  experimenter: ['Valero, Manuel' 'Zutshi, Ipshita' 'Yoon, Euisik' 'Buzsáki, György']
  Group /general/extracellular_ephys/Group 1 (ElectrodeGroup) no description
  Group /general/extracellular_ephys/Group 1/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  Group /general/extracellular_ephys/Group 2 (ElectrodeGroup) no description
  Group /general/extracellular_ephys/Group 2/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  Group /general/extracellular_ephys/Group 3 (ElectrodeGroup) no description
  Group /general/extracellular_ephys/Group 3/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  Group /general/extracellular_ephys/Group 4 (ElectrodeGroup) no description
  Group /general/extracellular_ephys/Group 4/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/channel_name (VectorData) unique channel reference | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/gain_to_uV (VectorData) no description | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (32,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/rel_x (VectorData) rel_x | shape = (32,) | dtype = float32
  Dataset /general/extracellular_ephys/electrodes/rel_y (VectorData) rel_y | shape = (32,) | dtype = float32
  institution: Princeton
  keywords: ['Development of the nervous system' 'Hippocampus' 'Neural circuits']
  lab: Buzsaki
  Group /general/optogenetics/OptogeneticStimulusSite3 (OptogeneticStimulusSite) 
  Group /general/optogenetics/OptogeneticStimulusSite3/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  Group /general/optogenetics/OptogeneticStimulusSite4 (OptogeneticStimulusSite) 
  Group /general/optogenetics/OptogeneticStimulusSite4/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  Group /general/optogenetics/OptogeneticStimulusSite5 (OptogeneticStimulusSite) 
  Group /general/optogenetics/OptogeneticStimulusSite5/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  Group /general/optogenetics/OptogeneticStimulusSite6 (OptogeneticStimulusSite) 
  Group /general/optogenetics/OptogeneticStimulusSite6/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  Group /general/optogenetics/OptogeneticStimulusSite7 (OptogeneticStimulusSite) 
  Group /general/optogenetics/OptogeneticStimulusSite7/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  Group /general/optogenetics/OptogeneticStimulusSite8 (OptogeneticStimulusSite) 
  Group /general/optogenetics/OptogeneticStimulusSite8/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  related_publications: ['https://doi.org/10.1126/science.abm1891']
  session_id: fCamk1_200901_sess12
  Group /general/subject (Subject) 
  identifier: 1d30c75b-ed02-492c-8389-f4c7b3b26034
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/behavioral_paradigm (VectorData) The behavioral paradigm of the epoch | shape = (5,) | dtype = object
  Dataset /intervals/epochs/environment (VectorData) The environment in the epoch | shape = (5,) | dtype = object
  Dataset /intervals/epochs/epoch_name (VectorData) The name of the epoch | shape = (5,) | dtype = object
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (5,) | dtype = int64
  Dataset /intervals/epochs/manipulation (VectorData) The stimulus in the epoch | shape = (5,) | dtype = object
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (5,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (5,) | dtype = float64
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (132,) | dtype = int64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (132,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (132,) | dtype = float64
  Dataset /intervals/trials/visited_arm (VectorData) Which side of the linear track was visited | shape = (132,) | dtype = uint8
  Group /processing/behavior (ProcessingModule) Tracking data obtained from positional tracking in video
  Group /processing/behavior/LinearMazePositionTracking (Position) 
  Group /processing/behavior/LinearMazePositionTracking/SpatiaLSeriesLinearized (SpatialSeries) Linearized position of the subject on the track.
  Group /processing/behavior/LinearMazePositionTracking/SpatialSeriesRaw (SpatialSeries) (x,y) coordinates tracking subject movement from above with camera on a PVC linear track (110 cm long, 6.35 cm wide)
  Group /processing/behavior/RewardEventsLinearTrack (LabeledEvents) rewards in the linear track
  Group /processing/behavior/SleepStates (TimeIntervals) Description of states : {
      "WAKEstate": "Waked and in locomotion",
      "NREMstate": "Non-REM sleep",
      "REMstate": "Rapid eye movement sleep",
      "WAKEtheta": "Wake with theta",
      "WAKEnontheta": "Wake without theta",
      "WAKEtheta_ThDt": "Wake with theta, estimated with higher theta/delta ratio",
      "REMtheta_ThDt": "REM sleep with theta, estimated with higher theta/delta ratio",
      "QWake_ThDt": "Quiet wakefulness esimated with higher theta/delta ratio",
      "QWake_noRipples_ThDt": "Quite wakefulness without ripples, estimated with higher theta/delta ratio",
      "NREM_ThDt": "Non-REM sleep, estimated with higher theta/delta ratio",
      "NREM_noRipples_ThDt": "Non-REM sleep without ripples, estimated with higher theta/delta ratio"
  }
  Dataset /processing/behavior/SleepStates/id (ElementIdentifiers)  | shape = (5602,) | dtype = int64
  Dataset /processing/behavior/SleepStates/label (VectorData) Sleep state. | shape = (5602,) | dtype = object
  Dataset /processing/behavior/SleepStates/start_time (VectorData) Start time of epoch, in seconds | shape = (5602,) | dtype = float64
  Dataset /processing/behavior/SleepStates/stop_time (VectorData) Stop time of epoch, in seconds | shape = (5602,) | dtype = float64
  Group /processing/ecephys (ProcessingModule) Intermediate data from extracellular electrophysiology recordings, e.g., LFP.
  Group /processing/ecephys/LFP (LFP) 
  Group /processing/ecephys/LFP/ElectricalSeriesLFP (ElectricalSeries) Acquisition traces for the ElectricalSeriesLFP.
  Dataset /processing/ecephys/LFP/ElectricalSeriesLFP/electrodes (DynamicTableRegion) electrode_table_region | shape = (32,) | dtype = int64
  Group /processing/ecephys/RippleTimeIntervals (TimeIntervals) Ripples and their metrics
  Dataset /processing/ecephys/RippleTimeIntervals/id (ElementIdentifiers)  | shape = (1796,) | dtype = int64
  Dataset /processing/ecephys/RippleTimeIntervals/peak_amplitudes (VectorData) Peak amplitude of the ripple. | shape = (1796,) | dtype = float64
  Dataset /processing/ecephys/RippleTimeIntervals/peak_frequencies (VectorData) Peak frequency of the ripple. | shape = (1796,) | dtype = float64
  Dataset /processing/ecephys/RippleTimeIntervals/peak_normed_power (VectorData) Normed power of the peak. | shape = (1796,) | dtype = float64
  Dataset /processing/ecephys/RippleTimeIntervals/peak_time (VectorData) Time at which the ripple peaked. | shape = (1796,) | dtype = float64
  Dataset /processing/ecephys/RippleTimeIntervals/ripple_amplitudes (VectorData) Amplitude of each point on the ripple. | shape = (1796, 187) | dtype = float64
  Dataset /processing/ecephys/RippleTimeIntervals/ripple_amplitudes_index (VectorIndex) Index for VectorData 'ripple_amplitudes' | shape = (1796,) | dtype = uint16
  Dataset /processing/ecephys/RippleTimeIntervals/ripple_durations (VectorData) Duration of the ripple event. | shape = (1796,) | dtype = float64
  Dataset /processing/ecephys/RippleTimeIntervals/ripple_frequencies (VectorData) Frequency of each point on the ripple. | shape = (1796, 187) | dtype = float64
  Dataset /processing/ecephys/RippleTimeIntervals/ripple_frequencies_index (VectorIndex) Index for VectorData 'ripple_frequencies' | shape = (1796,) | dtype = uint16
  Dataset /processing/ecephys/RippleTimeIntervals/ripple_phases (VectorData) Phase of each point on the ripple. | shape = (1796, 187) | dtype = float64
  Dataset /processing/ecephys/RippleTimeIntervals/ripple_phases_index (VectorIndex) Index for VectorData 'ripple_phases' | shape = (1796,) | dtype = uint16
  Dataset /processing/ecephys/RippleTimeIntervals/ripple_raw (VectorData) Extracted ripple data. | shape = (1796, 187) | dtype = int16
  Dataset /processing/ecephys/RippleTimeIntervals/ripple_raw_index (VectorIndex) Index for VectorData 'ripple_raw' | shape = (1796,) | dtype = uint16
  Dataset /processing/ecephys/RippleTimeIntervals/start_time (VectorData) Start time of epoch, in seconds | shape = (1796,) | dtype = float64
  Dataset /processing/ecephys/RippleTimeIntervals/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1796,) | dtype = float64
  session_description: Understanding how excitatory (E) and inhibitory (I) inputs are integrated by neurons requires monitoring their subthreshold behavior. We probed the subthreshold dynamics using optogenetic depolarizing pulses in hippocampal neuronal assemblies in freely moving mice. Excitability decreased during sharp-wave ripples coupled with increased I. In contrast to this “negative gain,” optogenetic probing showed increased within-field excitability in place cells by weakening I and unmasked stable place fields in initially non–place cells. Neuronal assemblies active during sharp-wave ripples in the home cage predicted spatial overlap and sequences of place fields of both place cells and unmasked preexisting place fields of non–place cells during track running. Thus, indirect probing of subthreshold dynamics in neuronal populations permits the disclosing of preexisting assemblies and modes of neuronal operations.
  session_start_time: 2016-03-15T00:00:00-04:00
  Group /stimulus/presentation/OptogeneticSeriesSite3 (OptogeneticSeries) μLEDs were controlled with current (2-4.5 μA generating 0.02-0.1μW of total light power;ref (15)) provided by a 12-channel current generator (OSC1Lite, NeuroNex Michigan Hub)driven by an Arduino, which delivered trapezoid (1ms rise time)blue light (centered emission at 460 nm, emission surface area = 150 mm2) 20 ms pulses atrandom sites with a randomly variable (40-60ms) offset
  Group /stimulus/presentation/OptogeneticSeriesSite3/site (OptogeneticStimulusSite) 
  Group /stimulus/presentation/OptogeneticSeriesSite3/site/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  Group /stimulus/presentation/OptogeneticSeriesSite4 (OptogeneticSeries) μLEDs were controlled with current (2-4.5 μA generating 0.02-0.1μW of total light power;ref (15)) provided by a 12-channel current generator (OSC1Lite, NeuroNex Michigan Hub)driven by an Arduino, which delivered trapezoid (1ms rise time)blue light (centered emission at 460 nm, emission surface area = 150 mm2) 20 ms pulses atrandom sites with a randomly variable (40-60ms) offset
  Group /stimulus/presentation/OptogeneticSeriesSite4/site (OptogeneticStimulusSite) 
  Group /stimulus/presentation/OptogeneticSeriesSite4/site/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  Group /stimulus/presentation/OptogeneticSeriesSite5 (OptogeneticSeries) μLEDs were controlled with current (2-4.5 μA generating 0.02-0.1μW of total light power;ref (15)) provided by a 12-channel current generator (OSC1Lite, NeuroNex Michigan Hub)driven by an Arduino, which delivered trapezoid (1ms rise time)blue light (centered emission at 460 nm, emission surface area = 150 mm2) 20 ms pulses atrandom sites with a randomly variable (40-60ms) offset
  Group /stimulus/presentation/OptogeneticSeriesSite5/site (OptogeneticStimulusSite) 
  Group /stimulus/presentation/OptogeneticSeriesSite5/site/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  Group /stimulus/presentation/OptogeneticSeriesSite6 (OptogeneticSeries) μLEDs were controlled with current (2-4.5 μA generating 0.02-0.1μW of total light power;ref (15)) provided by a 12-channel current generator (OSC1Lite, NeuroNex Michigan Hub)driven by an Arduino, which delivered trapezoid (1ms rise time)blue light (centered emission at 460 nm, emission surface area = 150 mm2) 20 ms pulses atrandom sites with a randomly variable (40-60ms) offset
  Group /stimulus/presentation/OptogeneticSeriesSite6/site (OptogeneticStimulusSite) 
  Group /stimulus/presentation/OptogeneticSeriesSite6/site/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  Group /stimulus/presentation/OptogeneticSeriesSite7 (OptogeneticSeries) μLEDs were controlled with current (2-4.5 μA generating 0.02-0.1μW of total light power;ref (15)) provided by a 12-channel current generator (OSC1Lite, NeuroNex Michigan Hub)driven by an Arduino, which delivered trapezoid (1ms rise time)blue light (centered emission at 460 nm, emission surface area = 150 mm2) 20 ms pulses atrandom sites with a randomly variable (40-60ms) offset
  Group /stimulus/presentation/OptogeneticSeriesSite7/site (OptogeneticStimulusSite) 
  Group /stimulus/presentation/OptogeneticSeriesSite7/site/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  Group /stimulus/presentation/OptogeneticSeriesSite8 (OptogeneticSeries) μLEDs were controlled with current (2-4.5 μA generating 0.02-0.1μW of total light power;ref (15)) provided by a 12-channel current generator (OSC1Lite, NeuroNex Michigan Hub)driven by an Arduino, which delivered trapezoid (1ms rise time)blue light (centered emission at 460 nm, emission surface area = 150 mm2) 20 ms pulses atrandom sites with a randomly variable (40-60ms) offset
  Group /stimulus/presentation/OptogeneticSeriesSite8/site (OptogeneticStimulusSite) 
  Group /stimulus/presentation/OptogeneticSeriesSite8/site/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  timestamps_reference_time: 2016-03-15T00:00:00-04:00
  Group /units (Units) Autogenerated by neuroconv.
  Dataset /units/clu_id (VectorData) 0-indexed id of cluster identified from the shank. | shape = (47,) | dtype = float64
  Dataset /units/group_id (VectorData) The electrode group ID that each unit was identified by. | shape = (47,) | dtype = object
  Dataset /units/id (ElementIdentifiers)  | shape = (47,) | dtype = int64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (1800735,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (47,) | dtype = uint32
  Dataset /units/unit_name (VectorData) Unique reference for each unit. | shape = (47,) | dtype = object


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ImageSeriesTrackingVideo1 (ImageSeries) Video recorded with Basler camera.
  file_create_date: ['2023-07-04T16:49:21.983726+02:00']
  Group /general/devices/N1-F21-O36 | 18 (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  experiment_description: Probing subthreshold dynamics of hippocampal neurons by pulsed optogenetics
  experimenter: ['Valero, Manuel' 'Zutshi, Ipshita' 'Yoon, Euisik' 'Buzsáki, György']
  Group /general/extracellular_ephys/Group 1 (ElectrodeGroup) no description
  Group /general/extracellular_ephys/Group 1/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  Group /general/extracellular_ephys/Group 2 (ElectrodeGroup) no description
  Group /general/extracellular_ephys/Group 2/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  Group /general/extracellular_ephys/Group 3 (ElectrodeGroup) no description
  Group /general/extracellular_ephys/Group 3/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  Group /general/extracellular_ephys/Group 4 (ElectrodeGroup) no description
  Group /general/extracellular_ephys/Group 4/device (Device) 12 µLEDs, 10 x 15 µm each, 3 per shank
  Emission Peak λ = 460 nm and FWHM = 40 nm
  Typical irradiance of 33 mW/mm² (@ max operating current of 100 µA)
  32 recording channels, 8 per shank
  Electrode impedance of 1000 - 1500 kΩ at 1 kHz
  
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/channel_name (VectorData) unique channel reference | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/gain_to_uV (VectorData) no description | shape = (32,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (32,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/rel_x (VectorData) rel_x | shape = (32,) | dtype = float32
  Dataset /general/extracellular_ephys/electrodes/rel_y (VectorData) rel_y | shape = (32,) | dtype = float32
  institution: Princeton
  keywords: ['Development of the nervous system' 'Hippocampus' 'Neural circuits']
  lab: Buzsaki
  related_publications: ['https://doi.org/10.1126/science.abm1891']
  session_id: fCamk1_200902_sess13_no_raw_data
  Group /general/subject (Subject) 
  identifier: 48fa6cf9-5e3e-420a-9b8c-354a5dfde774
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/behavioral_paradigm (VectorData) The behavioral paradigm of the epoch | shape = (5,) | dtype = object
  Dataset /intervals/epochs/environment (VectorData) The environment in the epoch | shape = (5,) | dtype = object
  Dataset /intervals/epochs/epoch_name (VectorData) The name of the epoch | shape = (5,) | dtype = object
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (5,) | dtype = int64
  Dataset /intervals/epochs/manipulation (VectorData) The stimulus in the epoch | shape = (5,) | dtype = object
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (5,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (5,) | dtype = float64
  Group /processing/behavior (ProcessingModule) Tracking data obtained from positional tracking in video
  Group /processing/behavior/LinearMazePositionTracking (Position) 
  Group /processing/behavior/LinearMazePositionTracking/SpatiaLSeriesLinearized (SpatialSeries) Linearized position of the subject on the track.
  Group /processing/behavior/LinearMazePositionTracking/SpatialSeriesRaw (SpatialSeries) (x,y) coordinates tracking subject movement from above with camera on a PVC linear track (110 cm long, 6.35 cm wide)
  Group /processing/behavior/RewardEventsLinearTrack (LabeledEvents) rewards in the linear track
  Group /processing/behavior/SleepStates (TimeIntervals) Description of states : {
      "WAKEstate": "Waked and in locomotion",
      "NREMstate": "Non-REM sleep",
      "REMstate": "Rapid eye movement sleep"
  }
  Dataset /processing/behavior/SleepStates/id (ElementIdentifiers)  | shape = (139,) | dtype = int64
  Dataset /processing/behavior/SleepStates/label (VectorData) Sleep state. | shape = (139,) | dtype = object
  Dataset /processing/behavior/SleepStates/start_time (VectorData) Start time of epoch, in seconds | shape = (139,) | dtype = float64
  Dataset /processing/behavior/SleepStates/stop_time (VectorData) Stop time of epoch, in seconds | shape = (139,) | dtype = float64
  Group /processing/behavior/UpDownStatesTimeIntervals (TimeIntervals) Up and Down states are a phenomenon observed in neurons, predominantly in the cerebral cortex, where they spontaneously fluctuate between periods of high (Up state) and low (Down state) activity. The Up state is characterized by a high rate of neuronal firing and depolarized membrane potentials, indicating active information processing. Conversely, the Down state is associated with a low rate of neuronal firing and hyperpolarized membrane potentials, suggesting a resting or inactive phase.
  
  Detection parameters:
  {
      "ch": 21,
      "spikeThreshold": 0.25,
      "gamm_thr": 0.5,
      "down_thr": 0,
      "deltaWaveThreshold": 0
  }
  Dataset /processing/behavior/UpDownStatesTimeIntervals/id (ElementIdentifiers)  | shape = (3759,) | dtype = int64
  Dataset /processing/behavior/UpDownStatesTimeIntervals/start_time (VectorData) Start time of epoch, in seconds | shape = (3759,) | dtype = float64
  Dataset /processing/behavior/UpDownStatesTimeIntervals/state (VectorData) UP or DOWN state | shape = (3759,) | dtype = object
  Dataset /processing/behavior/UpDownStatesTimeIntervals/stop_time (VectorData) Stop time of epoch, in seconds | shape = (3759,) | dtype = float64
  Group /processing/ecephys (ProcessingModule) No description.
  Group /processing/ecephys/RippleTimeIntervals (TimeIntervals) Ripples and their metrics
  Dataset /processing/ecephys/RippleTimeIntervals/id (ElementIdentifiers)  | shape = (7196,) | dtype = int64
  Dataset /processing/ecephys/RippleTimeIntervals/peak_normed_power (VectorData) Normed power of the peak. | shape = (7196,) | dtype = float64
  Dataset /processing/ecephys/RippleTimeIntervals/peak_time (VectorData) Time at which the ripple peaked. | shape = (7196,) | dtype = float64
  Dataset /processing/ecephys/RippleTimeIntervals/start_time (VectorData) Start time of epoch, in seconds | shape = (7196,) | dtype = float64
  Dataset /processing/ecephys/RippleTimeIntervals/stop_time (VectorData) Stop time of epoch, in seconds | shape = (7196,) | dtype = float64
  session_description: Understanding how excitatory (E) and inhibitory (I) inputs are integrated by neurons requires monitoring their subthreshold behavior. We probed the subthreshold dynamics using optogenetic depolarizing pulses in hippocampal neuronal assemblies in freely moving mice. Excitability decreased during sharp-wave ripples coupled with increased I. In contrast to this “negative gain,” optogenetic probing showed increased within-field excitability in place cells by weakening I and unmasked stable place fields in initially non–place cells. Neuronal assemblies active during sharp-wave ripples in the home cage predicted spatial overlap and sequences of place fields of both place cells and unmasked preexisting place fields of non–place cells during track running. Thus, indirect probing of subthreshold dynamics in neuronal populations permits the disclosing of preexisting assemblies and modes of neuronal operations.
  session_start_time: 2016-03-15T00:00:00-04:00
  timestamps_reference_time: 2016-03-15T00:00:00-04:00
  Group /units (Units) Autogenerated by neuroconv.
  Dataset /units/clu_id (VectorData) 0-indexed id of cluster identified from the shank. | shape = (37,) | dtype = float64
  Dataset /units/group_id (VectorData) The electrode group ID that each unit was identified by. | shape = (37,) | dtype = object
  Dataset /units/id (ElementIdentifiers)  | shape = (37,) | dtype = int64
  Dataset /units/spike_times (VectorData) the spike times for each unit | shape = (2230994,) | dtype = float64
  Dataset /units/spike_times_index (VectorIndex) Index for VectorData 'spike_times' | shape = (37,) | dtype = uint32
  Dataset /units/unit_name (VectorData) Unique reference for each unit. | shape = (37,) | dtype = object
