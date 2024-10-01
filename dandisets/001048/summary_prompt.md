
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001048/draft
name: Plasma membrane conductance changes in response to supraphysiological hyperpolarization
contributor: [{'name': 'Silkuniene, Giedre', 'email': 'giedre.silkuniene@gmail.com', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0001-8436-9718', 'affiliation': [], 'includeInCitation': True}, {'name': 'Silkunas, Mantas', 'schemaKey': 'Person', 'identifier': '0000-0002-4568-9265', 'includeInCitation': True}, {'name': 'Olga, Pakhomova', 'schemaKey': 'Person', 'identifier': '0000-0003-4950-4130', 'includeInCitation': True}, {'name': 'Andrei, Pakhomov', 'roleName': ['dcite:ProjectLeader'], 'schemaKey': 'Person', 'identifier': '0000-0003-3816-3860', 'includeInCitation': True}, {'name': 'National Institutes of Health', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': '1R21EY034258', 'includeInCitation': False}, {'name': 'National Institutes of Health', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': '5R21EY034803', 'includeInCitation': False}]
description: This study aimed to visualize and characterize membrane lesions caused by hyperpolarization and their protective roles against membrane overcharging. We identified three types of lesions in HEK cells, each with distinct characteristics. Hyperpolarization to specific voltages created diffuse zonal electropermeabilization, focal pores, and high-conductance pores, with adaptive conductance changes preventing membrane rupture. This study was partially supported by NIH grants 1R21EY034258 and 5R21EY034803.
assetsSummary: {'schemaKey': 'AssetsSummary', 'numberOfBytes': 0, 'numberOfFiles': 0}

Dandiset 001048 has 7 NWB files.
7 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/TIRFImaging (ImageSeries) TIRFImaging - Total Internal Reflection Fluorescent mode, cellTIRF MITICO unit (Olympus) Recordings contain 1202 frames in total. Recording speed 5.65 ms/frame. 1st and 2nd frames are artefacts. Scale: 64.9 x 64.9 nm per pixel. Pulse application: Patch clamp, voltage clamp mode, whole cell configuration with 0mV command voltage interrupted by 16 command voltage steps, 25 ms per step, applied at 350-ms intervals at 121 frame. Step voltage was escalated from -80 to -380 mV in 20-mV increments. Command voltage controlled via Multiclamp 700B amplifier and Digidata 1550B digitizer and Clampex 10.7 software (Molecular Devices, San Jose, CA).Additional metadata: ImageJ=1.53t
  images=1202
  frames=1202
  unit=micron
  loop=false
  min=102.0
  max=164.0
  file_create_date: ['2024-06-10T15:48:40.041108-04:00']
  experimenter: ['Mantas, Silkunas']
  institution: Old Dominion University
  lab: Pakhomov Lab
  session_id: session_03
  Group /general/subject (Subject) 
  identifier: 86028546-0c48-495f-9f0a-e75a3f43a789
  session_description: Subject ID: Cell03. General description of the experimental setup and conditions. Bath solution was composed of (in mM): 136 tetraethylammonium chloride (TEACl), 2 MgCl2, 10 CaCl2, 10 HEPES, and 10 glucose (pH 7.3, 300-310 mOsm/kg). Pipette solution contained (in mM): 20 TEACl, 130 CsCl, 10 HEPES, 4 Mg-ATP, 10 Cs-EGTA, and 0.12 of a fluorescent Ca2+ indicator Cal-520 (pH 7.3, 310 mOsm/kg). Pulse application: Patch clamp, voltage clamp mode, whole cell configuration with 0mV command voltage interrupted by 16 command voltage steps, 25 ms per step, applied at 350-ms intervals at 121 frame. Step voltage was escalated from -80 to -380 mV in 20-mV increments. Command voltage controlled via Multiclamp 700B amplifier and Digidata 1550B digitizer and Clampex 10.7 software (Molecular Devices, San Jose, CA).
  session_start_time: 2023-02-01T00:00:00-05:00
  timestamps_reference_time: 2023-02-01T00:00:00-05:00
