
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000249/0.230423.1416
name: Innate and plastic mechanisms for maternal behaviour in auditory cortex
contributor: [{'name': 'Dichter, Ben', 'email': 'ben.dichter@gmail.com', 'roleName': [], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': False}, {'name': 'Schiavo, Jennifer K.', 'roleName': ['dcite:Author', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Valtcheva, Silvana', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Bair-Marshall, Chloe J.', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Song, Soomin C.', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Martin, Kathleen A.', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Froemke, Robert C.', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'NINDS', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01s5ya894', 'awardNumber': '5U19NS107616', 'contactPoint': [], 'includeInCitation': False}]
description: Infant cries evoke powerful responses in parents. Whether parental animals are intrinsically sensitive to neonatal vocalizations, or instead learn about vocal cues for parenting responses is unclear. In mice, pup-naive virgin females do not recognize the meaning of pup distress calls, but retrieve isolated pups to the nest after having been co-housed with a mother and litte. Distress calls are variable, and require co-caring virgin mice to generalize across calls for reliable retrieval. Here we show that the onset of maternal behaviour in mice results from interactions between intrinsic mechanisms and experience-dependent plasticity in the auditory cortex. In maternal females, calls with inter-syllable intervals (ISIs) from 75 to 375 milliseconds elicited pup retrieval, and cortical responses were generalized across these ISIs. By contrast, naive virgins were neuronally and behaviourally sensitized to the most common (‘prototypical’) ISIs. Inhibitory and excitatory neural responses were initially mismatched in the cortex of naive mice, with untuned inhibition and overly narrow excitation. During co-housing experiments, excitatory responses broadened to represent a wider range of ISIs, whereas inhibitory tuning sharpened to form a perceptual boundary. We presented synthetic calls during co-housing and observed that neurobehavioural responses adjusted to match these statistics, a process that required cortical activity and the hypothalamic oxytocin system. Neuroplastic mechanisms therefore build on an intrinsic sensitivity in the mouse auditory cortex, and enable rapid plasticity for reliable parenting behaviour.
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 97968237237, 'numberOfFiles': 777, 'numberOfSubjects': 54, 'variableMeasured': ['OpticalChannel', 'ImagingPlane', 'TwoPhotonSeries'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'two-photon microscopy technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000249 has 100 NWB files.
100 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/TwoPhotonSeries (TwoPhotonSeries) no description
  Group /acquisition/TwoPhotonSeries/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeries/imaging_plane/channel_0 (OpticalChannel) 
  Group /acquisition/TwoPhotonSeries/imaging_plane/device (Device) 
  file_create_date: ['2022-05-25T21:28:07.441156-04:00']
  Group /general/devices/Microscope (Device) 
  Group /general/devices/Ti:Sapphire laser (Device) 
  Group /general/devices/multiphoton imaging system (Device) 
  experiment_description: <div>Calcium imaging videos for V06 (excitatory neurons). Experienced virgin (cohoused) - left auditory cortex.</div><div><br></div><div>PC=pup call circuit</div><div>prototypes=71b,j6a,61f,j5b</div><div>non-prototypes=j1a</div><div><br></div>
  Group /general/optophysiology/ImagingPlane (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane/channel_0 (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane/device (Device) 
  Group /general/subject (Subject) 
  identifier: cb2b640d-68a0-46c4-99f4-4b3994097417
  session_description: s1_r1_tones_half_001
  session_start_time: 2019-01-21T20:23:04.753000-05:00
  timestamps_reference_time: 2019-01-21T20:23:04.753000-05:00
