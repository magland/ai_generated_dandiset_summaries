
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001047/0.240610.2022
name: Use of MHz Compression ns Electric Pulse NG-CanCan Protocols to Minimize Near Electrode Ablation
contributor: [{'name': 'Silkuniene, Giedre', 'email': 'giedre.silkuniene@gmail.com', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0001-8436-9718', 'affiliation': [], 'includeInCitation': True}, {'name': 'Silkunas, Mantas', 'schemaKey': 'Person', 'identifier': '0000-0002-4568-9265', 'includeInCitation': True}, {'name': 'Pakhomov, Andrei', 'roleName': ['dcite:ProjectLeader'], 'schemaKey': 'Person', 'identifier': '0000-0003-3816-3860', 'includeInCitation': True}, {'name': 'National Institutes of Health', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': '1R21EY034258', 'includeInCitation': False}]
description: This study enhanced the Next Generation (NG) CanCan protocols using MHz compression for electric pulse packet delivery. The NG CanCan protocol's packets were delivered at  0.2 MHz. Compared to the same protocol delivered at a 1 Hz frequency, the MHz compression significantly reduced the cell ablation area near the electrodes while maintaining the same level of effect at the center. The experimental setup utilized a four-electrode array. For cell permeabilization evaluation, YoPro-1 was used, and to assess cell death two hours post-protocol delivery, Propidium Iodide was used. This study was supported by NIH grant 1R21EY034258.
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 14156734169, 'numberOfFiles': 54, 'numberOfSubjects': 12, 'variableMeasured': [], 'measurementTechnique': []}

Dandiset 001047 has 54 NWB files.
54 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/SingleTimePointImaging (ImageSeries) Single time point imaging using fluorescence microscopy. Additional metadata: Microscope: Olympus IX83 P2ZF. Detector: Hamamatsu Hamamatsu ORCA-Flash4.0. Objective: Olympus IX3 Nosepiece NA=0.16 Mag=4. Channels: FITC.
  file_create_date: ['2024-06-06T15:05:53.974912-04:00']
  experimenter: ['Giedre SIlkuniene, Mantas Silkunas']
  institution: Old Dominion University
  lab: Pakhomov Lab
  session_id: single_time_point
  Group /general/subject (Subject) 
  identifier: f1a3f6e7-9335-4df2-baca-4b2b3c998c42
  session_description: Subject 1: 011C_x5: 9 packets of pulses delivered at 0.2MHz frequency, Unknown protocol type, repeated 5 times at 1Hz frequency. Subject 2: 013Control_x1: 9 packets of pulses delivered at 1Hz frequency, Unknown protocol type, Unknown repetitions. Channel used: FITC. Each image contains 2 exposure areas. Subject 1 is on the left side of the image, and subject 2 is on the right side of the image. Each exposure area protocols are described in Subject 1 and 2 descriptions, and the overall protocol description is given below.Experiments were conducted using a four stainless steel electrode setup. The distance between adjacent electrodes was 3.8 mm. The CanCan exposure protocol consisted of packets of pulses delivered from four electrodes (channels). The first pulse (600 ns) in each packet was delivered from one electrode (e.g., electrode 1) at a 3.2 kV amplitude. Subsequent pulses (600 ns) were delivered simultaneously from two electrodes (electrodes 2 and 4) at 75% of the first pulse's amplitude. The same amplitude pulses were then applied from electrodes 1 and 3. Following this, 50% amplitude pulses were applied from electrodes 2 and 4, followed by the same amplitude pulses from electrodes 1 and 3. The final round of pulses from each electrode pair was at 25% of the first pulse's amplitude. After one packet was applied, it was repeated nine times at a defined frequency rate. Upon completion of the protocol, it was either repeated 2, 3, or 5 times at a 1 Hz frequency or switched to another starting active electrode (e.g., electrode 2). Sequences were repeated in the same manner until all four electrodes acted as active electrodes.Control protocols were applied in the same manner, frequencies, and repetitions as the CanCan protocols, but without the subsequent CanCan pulses from two electrodes.Before exposure, the growth media was replaced with a physiological solution (in mM: 140 NaCl, 5.4 KCl, 2 CaCl2, 1.5 MgCl2, 10 D-glucose, and 10 HEPES; pH 7.3, 290-300 mOsm/kg) containing 1 µg/mL Hoechst and 1 µM YoPro-1 (YP). The cell-permeable Hoechst dye labeled the nuclei of all cells (detected using the DAPI channel). YP, which has limited permeability into intact cells, was used as a semi-quantitative marker of plasma membrane permeabilization by electroporation (detected using the FITC channel). Thirty minutes post-exposure, the media containing dyes was replaced with physiological solution without dyes. The cell monolayer was then scanned for YP uptake. Two hours after exposure, Propidium Iodide (PI) was added to the media, incubated for 15 minutes, and then removed by changing the media to one without PI. PI was used to evaluate dead cells after electric pulses (detected using the Cy3 channel). Microscope: Unknown. Detector: Unknown. Objective: Unknown. Channels: .
  session_start_time: 2024-05-23T13:35:09-04:00
  timestamps_reference_time: 2024-05-23T13:35:09-04:00
