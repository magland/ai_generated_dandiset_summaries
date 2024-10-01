
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000631/0.231012.1508
name: Effect of the electric field vector change on the electroporation efficiency of paired-pulse trains compared to single-pulse trains
contributor: [{'name': 'Silkuniene, Giedre', 'email': 'giedre.silkuniene@gmail.com', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0001-8436-9718', 'affiliation': [], 'includeInCitation': True}, {'name': 'Kim, Vitalii', 'roleName': ['dcite:Author', 'dcite:DataCollector'], 'schemaKey': 'Person', 'identifier': '0000-0003-0699-5582', 'affiliation': [], 'includeInCitation': True}, {'name': 'Semenov, Iurii', 'roleName': [], 'schemaKey': 'Person', 'identifier': '0000-0002-0302-1355', 'affiliation': [], 'includeInCitation': True}, {'name': 'Pakhomov, Andrei', 'roleName': [], 'schemaKey': 'Person', 'identifier': '0000-0003-3816-3860', 'affiliation': [], 'includeInCitation': True}, {'name': 'National Institutes of Health', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': 'NIH 1R21EY034258', 'contactPoint': [], 'includeInCitation': False}]
description: In the study, the impact of varying the electric field vector on the effectiveness of electroporation was examined, utilizing both paired-pulse trains, consisting of 5 pulses at 600 + 600 ns, and single-pulse trains with 5 pulses at 600 ns. These were applied to a BPAE cell monolayer at frequencies of either 1 Hz or 833 kHz. The focus was on assessing the alterations in electroporation efficiency, gauged through the changes in YoPro-1 emission when compared to the baseline established by a single-pulse train in the identical region of interest, which was set at 100%. The evaluation criteria included the angle at which the electric field vector direction alternated between two pulses within a pair. Introduction of pulses in pairs amplified the electroporation efficiency at smaller angles but resulted in an inhibition at larger angles, indicating a frequency-dependent relationship. The images captured during the experiments provided a comprehensive visualization of this effect, highlighting the nuanced impact of electric field vector modifications on electroporation efficiency. Supported by NIH 1R21EY034258
assetsSummary: {'species': [{'name': 'Bos taurus - Cattle', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9913'}], 'approach': [], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 18379955860, 'numberOfFiles': 15, 'numberOfSubjects': 15, 'variableMeasured': [], 'measurementTechnique': []}

Dandiset 000631 has 15 NWB files.
15 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ScaningImaging (ImageSeries) IX83 microscope used; MS-2000 scanning stage; X-Cite 110LED illuminator; ORCA-Flash4 sCMOS camera;CellSens software for automation; Channel 1 ex/em 350/460nm for MemBrite dye; ex/em 480/535nm for YOPRO-1; dark circles indicate electrode footprints; 144 images captured in a 12x12 grid from a six-well plate; 216 additional images with DAPI and FITC filter cubes; all images automatically stitched for a final composite; 10×, 0.38NA objective used for high-resolution imaging.
  file_create_date: ['2023-10-11T10:50:18.217632-04:00']
  experimenter: ['Kim Vitalii']
  institution: Old Dominion University
  lab: Pakhomov Lab
  session_id: BPAE_5xBipolar_0,83MHz
  Group /general/subject (Subject) 
  identifier: 64c4a43c-93e8-4bb3-bacd-ff6ce63b5b3d
  session_description: Cells were electroporated by a train of 5 600+600 ns bipolar pulses (amplitude of the second phase was 50% the first phase's amplitude) at 0,83 MHz.The electrodes were two parallel stainless-steel cylinders, 1.5 mm in diameter and 3 mm apart
  session_start_time: 2021-08-24T19:09:14-04:00
  timestamps_reference_time: 2021-08-24T19:09:14-04:00
