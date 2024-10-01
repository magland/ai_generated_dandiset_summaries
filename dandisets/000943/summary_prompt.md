
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000943/0.240614.0754
name: Clark and Nolan (2024) Task-anchored grid cell firing is selectively associated with successful path integration-dependent behaviour
contributor: [{'name': 'Clark, Harry', 'email': 'harrydclark91@gmail.com', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}]
description: This dataset contains electrophysiological recordings alongside the synchronised behavioural data for mice running in an open field and virtual linear track environments. Movable tetrodes were targeted to the medial entorhinal cortex. Further details can be found here (https://doi.org/10.7554/eLife.89356.2).
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 976205947390, 'numberOfFiles': 734, 'numberOfSubjects': 12, 'variableMeasured': ['ElectrodeGroup', 'ElectricalSeries'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000943 has 100 NWB files.
100 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeries (ElectricalSeries) see data collection
  Dataset /acquisition/ElectricalSeries/electrodes (DynamicTableRegion) electrode_table_region | shape = (16,) | dtype = int64
  Group /acquisition/position (TimeSeries) position: cm, speed: cm/s, angle: degrees, trials: non-zero indexed, trial types: 0-beaconed, 1-nonbeaconed, 2-probe
  file_create_date: ['2024-04-17T13:42:56.579864+00:00']
  data_collection: Electrophysiological signals were acquired using an Intan headstage connected via an SPI cable (Intan Technologies, RHD2000 6-ft (1.8 m) standard SPI interface cable) attached to an Open Ephys acquisition board. For the location memory task, behavioural variables including position, trial number and trial type were calculated in Blender3D at 60 Hz and sent via a data acquisition (DAQ) microcontroller (Arduino Due) to the OpenEphys acquisition board and was subsequently processed to provide downsampled behavioural data. In the open arena, motion and head-direction tracking used a camera (Logitech B525, 1280 x 720 pixels Webcam, RS components 795-0876) attached to the frame. Red and green polystyrene balls were attached to the sides of the headstage and were tracked using a custom script written in Bonsai (Lopes and Monteiro, 2021). Synchronisation of position and electrophysiology data used an LED attached to the side of the open arena in the field of view of the camera, with randomly timed trigger pulses sent to the LED via an Arduino board (Arduino Uno) and to the Open Ephys acquisition board via the I/O board
  Group /general/devices/Tetrode microdrive (Device) Microdrives containing 4 tetrodes were built by threading 90% platinum, 10% iridium tetrode wires (18 µm HML-coated, Neuralynx) to an EIB-16 board (Neuralynx) via an inner cannula (21 gauge 9 mm long). The board was covered in epoxy and a poor lady frame (Axona) cemented to the side. An outer cannula (17 gauge 7 mm), placed around the inner cannula, was secured temporarily using vaseline, allowing it to be lowered during the surgery. Tetrodes were trimmed to ~3 mm using ceramic scissors (Science Tools, Germany) and gold plated (Non-cyanide gold plating solution, Neuralynx) to give an impedance between 150 and 200 kΩ at 1kHz. 
  experiment_description: Extracellular recording of mice medial entorhinal cortex during free exploration in a 100 x 100 cm open field and a virtual reality location memory task
  experimenter: ['Clark, Harry']
  Group /general/extracellular_ephys/0 (ElectrodeGroup) no description
  Group /general/extracellular_ephys/0/device (Device) Microdrives containing 4 tetrodes were built by threading 90% platinum, 10% iridium tetrode wires (18 µm HML-coated, Neuralynx) to an EIB-16 board (Neuralynx) via an inner cannula (21 gauge 9 mm long). The board was covered in epoxy and a poor lady frame (Axona) cemented to the side. An outer cannula (17 gauge 7 mm), placed around the inner cannula, was secured temporarily using vaseline, allowing it to be lowered during the surgery. Tetrodes were trimmed to ~3 mm using ceramic scissors (Science Tools, Germany) and gold plated (Non-cyanide gold plating solution, Neuralynx) to give an impedance between 150 and 200 kΩ at 1kHz. 
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/channel_name (VectorData) no description | shape = (16,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/gain_to_uV (VectorData) no description | shape = (16,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (16,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (16,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (16,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (16,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/offset_to_uV (VectorData) no description | shape = (16,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_x (VectorData) rel_x | shape = (16,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_y (VectorData) rel_y | shape = (16,) | dtype = float64
  Group /general/extracellular_ephys/tetrode (ElectrodeGroup) Tetrodes lowered 1.2 - 1.4 mm into the right hemisphere of the brain, beginning at 3.4 mm lateral from Bregma and along the lambdoid suture, and at an angle of -15° in the posterior direction
  Group /general/extracellular_ephys/tetrode/device (Device) Microdrives containing 4 tetrodes were built by threading 90% platinum, 10% iridium tetrode wires (18 µm HML-coated, Neuralynx) to an EIB-16 board (Neuralynx) via an inner cannula (21 gauge 9 mm long). The board was covered in epoxy and a poor lady frame (Axona) cemented to the side. An outer cannula (17 gauge 7 mm), placed around the inner cannula, was secured temporarily using vaseline, allowing it to be lowered during the surgery. Tetrodes were trimmed to ~3 mm using ceramic scissors (Science Tools, Germany) and gold plated (Non-cyanide gold plating solution, Neuralynx) to give an impedance between 150 and 200 kΩ at 1kHz. 
  institution: University of Edinburgh
  keywords: ['vr' 'of' 'virtual reality' 'open field' 'mice']
  lab: Nolan Lab
  notes: Experimental days involved recording from mice in the open arena and then in the virtual location memory task. On a few days this order was reversed without apparent effects on the results obtained. Mice were collected from the holding room 30 - 60 minutes before recording, were handled for 5 - 10 minutes, weighed and placed for 10 - 20 minutes in a cage containing objects and a running wheel. Between recording sessions mice were placed back in the object-filled playground for 30 minutes. Tetrodes were typically lowered by 50 - 100 µm after each session. The open arena consisted of a metal box with a square floor area, removable metal walls, metal frame (Frame parts from Kanya UK, C01-1, C20-10, A33-12, B49-75, B48-75, A39-31, ALU3), and an A4-sized cue card in the middle of one of the metal walls. For the open field exploration session, mice were placed in the open arena while tethered via an ultrathin SPI cable and custom-build commutator and left unprompted for 30 minutes to freely move around. For the location memory task mice were trained to obtain rewards at a location on the virtual linear track. Mice were head-fixed using a RIVETS clamp (Ronal Tool Company, Inc) and ran on a cylindrical treadmill fitted with a rotary encoder (Pewatron). Virtual tracks, generated using Blender3D (blender.com) had a range of lengths, in the published journal article only sessions with 200cm track lengths are used. This consisted of a 60 cm track zone, a 20 cm reward zone, a second 60 cm track zone and a 60 cm black box to separate successive trials. In sessions with track lengths longer than 200cm, Xcm length tracks consisted of a Zcm length track zone, a 20 cm reward zone, a 60 cm track zone and a 60 cm black box to seperate successive trials. The length of Z can be derived from the track length using the equations Z = X-(60+60+20). In actuality, the trial starts in the middle of the blackbox region therefore it can be thought of as 2 successive 30 cm black box regions or a single 60 cm region that spans across two trials, this explains how the black box is visualised within the research article. The distance visible ahead of the mouse was 50 cm. The reward zone was either marked by distinct vertical green and black bars on beaconed trials, or was not marked by a visual cue at all on non-beaconed or probe trials. A feeding tube placed in front of the animal dispensed soy milk rewards (5 - 10 µl per reward) if the mouse stopped in the reward zone, however was not dispensed on probe trials. A stop was registered in Blender3D if the speed of the mouse dropped below 4.7 cm/s. Speed was calculated on a rolling basis from the previous 100 ms at a rate of 60 Hz. Trials were delivered in repeating blocks throughout a recording session. For example, 3 beaconed trials (B) followed by 2 non-beaconed trials (N) with the order repeating until the end of the session. To encourage learning and engagement in both beaconed and non-beaconed trials, the first day of training typically used a trial type ratio of 3 beaconed trials to 1 non-beaconed trials. As training progressed we then increased the proportion of non-beaconed trials up to a ratio of 1 beaconed trial to 4 non-beaconed trials. Examples of trial blocks include BBBBN, BBBN, BBN, BN, BNN, BNNN, BBNNN and BBNNNNNNN where each character indicates the trial type of each trial within a block. In some sessions we replaced single non-beaconed trials in trial blocks with a probe trial (P). Examples of trial blocks with probe trials include BBBBNBBBBP, BBBNBBBP, BBNBBP and BBNNNNNNNP. For more details, see https://doi.org/10.7554/eLife.89356.2
  pharmacology: Isoflurane used during surgery. Vetergesic jelly given post surgery. No further drugs given
  protocol: see https://doi.org/10.7554/eLife.89356.2
  related_publications: ['https://doi.org/10.7554/eLife.89356.2'
   'https://datashare.ed.ac.uk/handle/10283/8723'
   'https://github.com/MattNolanLab/eLife_Grid_anchoring_2024']
  session_id: M1_D1_2020-08-03_16-11-14
  slices: see https://doi.org/10.7554/eLife.89356.2
  source_script: None
  stimulus: see notes
  Group /general/subject (Subject) 
  surgery: Headpost and tetrode implant surgery into the MEC, surgeries performed by Harry Clark
  virus: none
  identifier: e9e1b53e-3790-4e82-b147-6c466afa7f25
  session_description: vr
  session_start_time: 2020-08-03T16:11:14+00:00
  timestamps_reference_time: 2020-08-03T16:11:14+00:00
