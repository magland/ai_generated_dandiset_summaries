
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001033/0.240527.1432
name: Characterization of Neuron Action Potential Triggering Using Sine Wave Electrostimulation at Varying Frequencies_part2
contributor: [{'name': 'Silkuniene, Giedre', 'email': 'giedre.silkuniene@gmail.com', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0001-8436-9718', 'affiliation': [], 'includeInCitation': True}, {'name': 'Semenov, Iurii', 'schemaKey': 'Person', 'identifier': '0000-0002-0302-1355', 'includeInCitation': True}, {'name': 'Pakhomov, Andrei', 'roleName': ['dcite:ProjectLeader'], 'schemaKey': 'Person', 'identifier': '0000-0003-3816-3860', 'includeInCitation': True}, {'name': 'National Institutes of Health', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': '5R21EY034803', 'includeInCitation': False}]
description: This experimental series aimed to characterize the triggering of action potentials (APs) in neurons using sine waves and modulated sine waves at varying frequencies. The experiments were conducted on E18 Sprague Dawley rat hippocampal neurons (BrainBits, Springfield, IL), employing the voltage-sensitive dye FluoVolt (Thermo Fisher Scientific, Waltham, MA) as the AP reporter.
assetsSummary: {'species': [{'name': 'Rattus norvegicus - Norway rat', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10116'}], 'approach': [], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 134723619, 'numberOfFiles': 193, 'numberOfSubjects': 10, 'variableMeasured': [], 'measurementTechnique': []}

Dandiset 001033 has 100 NWB files.
100 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/TimeLapseImaging (ImageSeries) TimeLapseImaging method utilizes fluorescence microscopy. Cells are loaded with a voltage-sensitive FluoVolt dye, which responds to Transmembrane Membrane Potential (TMP) changes within nanoseconds, allowing optical time-lapse recording of induced action potentials. For the visualization an IX71 microscope (Olympus America, Center Valley, PA, USA), and a PlanApo N 60x, 1.42 NA objective (Olympus) was used. Time-lapse image (16x16 pixels) stacks (3,086.4 frames/s) were acquired using an iXon Ultra 897 back-illuminated CCD camera (Andor Technology, Belfast, UK) with the Solis interface (Andor).Recording durations varied, but most stacks consisted of 1200 images (total recording time 388.47 ms). The camera sensor area outside the region of interest was shielded with an Optomask (Andor).Additional metadata: Andor SOLIS
  file_create_date: ['2024-05-25T16:55:14.201919-04:00']
  experimenter: ['Iurii, Semenov']
  institution: Old Dominion University
  lab: Pakhomov Lab
  session_id: 20Hz_sine_stimulation_3V
  Group /general/subject (Subject) 
  identifier: 81d04abd-c51b-4241-a800-92332fc39e64
  session_description: Subject ID: 1_2. A sine wave stimulation applied at 20Hz using 3V (peak-to-peak) amplitude. Note: this is not the actual amplitude measured on the oscilloscope, which will be somewhat smaller (calibration factors are frequency-dependent and will be reported separately after the calibration is completed). For the employed electrode configuration, 1V translates into 36 V/cm at the location of neurons. Neuron action potentials were visualized using the voltage-sensitive fluorescent dye, FluoVolt. All experiments were performed in a standard physiological solution containing (in mM): 140 NaCl, 5.4 KCl, 2 CaCl2, 1.5 MgCl2, 10 D-glucose, and 10 HEPES (pH 7.3, 290-300 mOsm/kg). The exposure system comprised a Siglent SDG1032X waveform generator (Siglent Technologies, Solon, OH), the 'EasywaveX' software, and a pair of tungsten electrodes (100 μm diameter, 140 μm inter-electrode gap) precisely positioned 50 µm above a chosen neuron using a robotic micromanipulator MPC-200 (Sutter Instrument, Novato, CA). Sine waves and modulated sine waves were generated using Excel software, uploaded to the Siglent generator, and exposure parameters (frequency, amplitude, and duration) were set. Exposure was triggered 50 ms after the start of fluorescence time-lapse recording. The applied electric field between electrodes was determined using a finite element method simulation (Sim4Life V5.2, Zurich Med Tech). Exposure duration was kept at 250 ms regardless of the sine wave carrier and modulation frequency. Waveform, amplitude, and synchronization were monitored with a TDS3052C oscilloscope (Tektronix, Beaverton, OR). Exposures were synchronized with image acquisitions via a TTL pulse protocol using a Digidata 1440A board and Clampex v. 10.2 software (Molecular Devices, Sunnyvale, CA).
  session_start_time: 2024-05-13T18:08:17-04:00
  timestamps_reference_time: 2024-05-13T18:08:17-04:00
