
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000773/draft
name: Age affects odor-evoked calcium responses in the ant antennal lobe
contributor: [{'name': 'National Institutes of Health (NIH)', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': '5 R01 NS 123899-02'}, {'name': 'Hart, Taylor', 'email': 'harttdp@gmail.com', 'roleName': ['dcite:Author', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0001-9692-8150', 'includeInCitation': True}]
description: Calcium imaging experiments were performed on the clonal raider ant antennal lobe to determine whether odor coding is modulated during aging. Ants were either two weeks old or two months old, corresponding to nurse-like and forager-like behavioral patterns. Ants are clonal line B with transgene insert [ie-DsRed, ObirOrco-QF2, 15xQUAS-GCaMP6s]. GCaMP6s labels all Orco-positive antennal lobe glomeruli and allows recording odor responses throughout the antennal lobe using volumetric imaging.

Associated with Hart et al. 2024. Pheromone representation in the ant antennal lobe changes with age. Current Biology 34. https://doi.org/10.1016/j.cub.2024.05.031

Ants were stimulated with 5 general odorants (3-hexanone, isopropanol, ethanol, propionic acid, ethylpyrazine) and 2 alarm pheromones (4-methyl-3-heptanone and 4-methyl-3-heptanol) all at either 3% or 48% concentration (volume/volume in paraffin oil). Experiments had a 3s lag time and a 5s stimulus time, total recording time 48s, 0.83 volumes/second. 33 Z-planes were imaged in each volume.

Ants were imaged on different days, and the following outline describes experiment conditions for the dataset.

Two weeks old experiment days:
1-18-2023 - 48% odor conc.
1-20-2023 - 48% odor conc. 
2-24-2023 - 48% odor conc.
1-17-2023 - 3% odor conc.

Two months old experiment days:
1-10-2023 - 48% odor conc.
4-6-2023 - 48% odor conc.
1-11-2023 - 3% odor conc. 

assetsSummary: {'species': [{'name': 'Ooceraea biroi - Clonal raider ant', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_2015173'}], 'approach': [{'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 1281980278656, 'numberOfFiles': 15246, 'numberOfSubjects': 21, 'variableMeasured': ['OpticalChannel', 'TwoPhotonSeries', 'ImagingPlane'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'two-photon microscopy technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000773 has 16 NWB files.
4 of these NWB files are of type 1.
3 of these NWB files are of type 2.
3 of these NWB files are of type 3.
3 of these NWB files are of type 4.
3 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/TwoPhotonSeries1 (TwoPhotonSeries) two photon recording, 40 cycles total, recording time 48.0s, odor stimulus triggered at 3s with duration 5s
  Group /acquisition/TwoPhotonSeries1/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeries1/imaging_plane/Green PMT (OpticalChannel) 
  Group /acquisition/TwoPhotonSeries1/imaging_plane/device (Device) Investigator with Coherent Axon laser, dual GaAsP detectors, resonant scanning galvanometer, Z-piezo, 40x 0.9NA water immersion objective
  file_create_date: ['2024-01-03T22:03:09.784154-05:00']
  Group /general/devices/Kronauer Lab two-photon microscope (Device) Investigator with Coherent Axon laser, dual GaAsP detectors, resonant scanning galvanometer, Z-piezo, 40x 0.9NA water immersion objective
  experiment_description: 40 cycle 2photon recording, 5s odor stim triggered at 3s, using 0.03x 3-hexanone at z depth 0 um in the clonal raider ant antennal lobe, transgenic line expressing GCaMP6s in olfactory sensory neurons
  experimenter: ['Hart, Taylor']
  institution: The Rockefeller University, New York
  keywords: ['antennal lobe' 'calcium imaging' 'chemosensation' 'clonal raider ant'
   'communication' 'GCaMP' 'odor coding' 'olfaction' 'Ooceraea biroi'
   'pheromone']
  lab: Laboratory of Social Evolution and Behavior
  Group /general/optophysiology/ImagingPlane at 0 um z depth (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane at 0 um z depth/Green PMT (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane at 0 um z depth/device (Device) Investigator with Coherent Axon laser, dual GaAsP detectors, resonant scanning galvanometer, Z-piezo, 40x 0.9NA water immersion objective
  session_id: m1-d11-y2023-ant1-0.03x-3-hexanone-40-t131-z0um
  Group /general/subject (Subject) 
  identifier: e72a1abb-56e0-4c72-a676-c338e3cd7f93
  session_description: 5s odor stimulation at 33 z depths
  session_start_time: 2023-01-11T15:07:32-05:00
  timestamps_reference_time: 2023-01-11T15:07:32-05:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/TwoPhotonSeries1 (TwoPhotonSeries) two photon recording, 40 cycles total, recording time 48.0s, odor stimulus triggered at 3s with duration 5s
  Group /acquisition/TwoPhotonSeries1/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeries1/imaging_plane/Green PMT (OpticalChannel) 
  Group /acquisition/TwoPhotonSeries1/imaging_plane/device (Device) Investigator with Coherent Axon laser, dual GaAsP detectors, resonant scanning galvanometer, Z-piezo, 40x 0.9NA water immersion objective
  file_create_date: ['2024-01-03T22:03:52.638434-05:00']
  Group /general/devices/Kronauer Lab two-photon microscope (Device) Investigator with Coherent Axon laser, dual GaAsP detectors, resonant scanning galvanometer, Z-piezo, 40x 0.9NA water immersion objective
  experiment_description: 40 cycle 2photon recording, 5s odor stim triggered at 3s, using 0.03x 3-hexanone at z depth 100 um in the clonal raider ant antennal lobe, transgenic line expressing GCaMP6s in olfactory sensory neurons
  experimenter: ['Hart, Taylor']
  institution: The Rockefeller University, New York
  keywords: ['antennal lobe' 'calcium imaging' 'chemosensation' 'clonal raider ant'
   'communication' 'GCaMP' 'odor coding' 'olfaction' 'Ooceraea biroi'
   'pheromone']
  lab: Laboratory of Social Evolution and Behavior
  Group /general/optophysiology/ImagingPlane at 100 um z depth (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane at 100 um z depth/Green PMT (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane at 100 um z depth/device (Device) Investigator with Coherent Axon laser, dual GaAsP detectors, resonant scanning galvanometer, Z-piezo, 40x 0.9NA water immersion objective
  session_id: m1-d11-y2023-ant1-0.03x-3-hexanone-40-t131-z100um
  Group /general/subject (Subject) 
  identifier: 971effd8-fe09-49d1-947b-a208aa88d29f
  session_description: 5s odor stimulation at 33 z depths
  session_start_time: 2023-01-11T15:07:32-05:00
  timestamps_reference_time: 2023-01-11T15:07:32-05:00


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/TwoPhotonSeries1 (TwoPhotonSeries) two photon recording, 40 cycles total, recording time 48.0s, odor stimulus triggered at 3s with duration 5s
  Group /acquisition/TwoPhotonSeries1/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeries1/imaging_plane/Green PMT (OpticalChannel) 
  Group /acquisition/TwoPhotonSeries1/imaging_plane/device (Device) Investigator with Coherent Axon laser, dual GaAsP detectors, resonant scanning galvanometer, Z-piezo, 40x 0.9NA water immersion objective
  file_create_date: ['2024-01-03T22:03:56.558378-05:00']
  Group /general/devices/Kronauer Lab two-photon microscope (Device) Investigator with Coherent Axon laser, dual GaAsP detectors, resonant scanning galvanometer, Z-piezo, 40x 0.9NA water immersion objective
  experiment_description: 40 cycle 2photon recording, 5s odor stim triggered at 3s, using 0.03x 3-hexanone at z depth 105 um in the clonal raider ant antennal lobe, transgenic line expressing GCaMP6s in olfactory sensory neurons
  experimenter: ['Hart, Taylor']
  institution: The Rockefeller University, New York
  keywords: ['antennal lobe' 'calcium imaging' 'chemosensation' 'clonal raider ant'
   'communication' 'GCaMP' 'odor coding' 'olfaction' 'Ooceraea biroi'
   'pheromone']
  lab: Laboratory of Social Evolution and Behavior
  Group /general/optophysiology/ImagingPlane at 105 um z depth (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane at 105 um z depth/Green PMT (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane at 105 um z depth/device (Device) Investigator with Coherent Axon laser, dual GaAsP detectors, resonant scanning galvanometer, Z-piezo, 40x 0.9NA water immersion objective
  session_id: m1-d11-y2023-ant1-0.03x-3-hexanone-40-t131-z105um
  Group /general/subject (Subject) 
  identifier: cb1c52a0-4a55-4e0e-8e4c-d077043c5d5e
  session_description: 5s odor stimulation at 33 z depths
  session_start_time: 2023-01-11T15:07:32-05:00
  timestamps_reference_time: 2023-01-11T15:07:32-05:00


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/TwoPhotonSeries1 (TwoPhotonSeries) two photon recording, 40 cycles total, recording time 48.0s, odor stimulus triggered at 3s with duration 5s
  Group /acquisition/TwoPhotonSeries1/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeries1/imaging_plane/Green PMT (OpticalChannel) 
  Group /acquisition/TwoPhotonSeries1/imaging_plane/device (Device) Investigator with Coherent Axon laser, dual GaAsP detectors, resonant scanning galvanometer, Z-piezo, 40x 0.9NA water immersion objective
  file_create_date: ['2024-01-03T22:03:12.919496-05:00']
  Group /general/devices/Kronauer Lab two-photon microscope (Device) Investigator with Coherent Axon laser, dual GaAsP detectors, resonant scanning galvanometer, Z-piezo, 40x 0.9NA water immersion objective
  experiment_description: 40 cycle 2photon recording, 5s odor stim triggered at 3s, using 0.03x 3-hexanone at z depth 10 um in the clonal raider ant antennal lobe, transgenic line expressing GCaMP6s in olfactory sensory neurons
  experimenter: ['Hart, Taylor']
  institution: The Rockefeller University, New York
  keywords: ['antennal lobe' 'calcium imaging' 'chemosensation' 'clonal raider ant'
   'communication' 'GCaMP' 'odor coding' 'olfaction' 'Ooceraea biroi'
   'pheromone']
  lab: Laboratory of Social Evolution and Behavior
  Group /general/optophysiology/ImagingPlane at 10 um z depth (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane at 10 um z depth/Green PMT (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane at 10 um z depth/device (Device) Investigator with Coherent Axon laser, dual GaAsP detectors, resonant scanning galvanometer, Z-piezo, 40x 0.9NA water immersion objective
  session_id: m1-d11-y2023-ant1-0.03x-3-hexanone-40-t131-z10um
  Group /general/subject (Subject) 
  identifier: fe36f83b-c812-46b4-a59f-3c694a78a05a
  session_description: 5s odor stimulation at 33 z depths
  session_start_time: 2023-01-11T15:07:32-05:00
  timestamps_reference_time: 2023-01-11T15:07:32-05:00


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  Group /acquisition/TwoPhotonSeries1 (TwoPhotonSeries) two photon recording, 40 cycles total, recording time 48.0s, odor stimulus triggered at 3s with duration 5s
  Group /acquisition/TwoPhotonSeries1/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeries1/imaging_plane/Green PMT (OpticalChannel) 
  Group /acquisition/TwoPhotonSeries1/imaging_plane/device (Device) Investigator with Coherent Axon laser, dual GaAsP detectors, resonant scanning galvanometer, Z-piezo, 40x 0.9NA water immersion objective
  file_create_date: ['2024-01-03T22:03:58.218076-05:00']
  Group /general/devices/Kronauer Lab two-photon microscope (Device) Investigator with Coherent Axon laser, dual GaAsP detectors, resonant scanning galvanometer, Z-piezo, 40x 0.9NA water immersion objective
  experiment_description: 40 cycle 2photon recording, 5s odor stim triggered at 3s, using 0.03x 3-hexanone at z depth 110 um in the clonal raider ant antennal lobe, transgenic line expressing GCaMP6s in olfactory sensory neurons
  experimenter: ['Hart, Taylor']
  institution: The Rockefeller University, New York
  keywords: ['antennal lobe' 'calcium imaging' 'chemosensation' 'clonal raider ant'
   'communication' 'GCaMP' 'odor coding' 'olfaction' 'Ooceraea biroi'
   'pheromone']
  lab: Laboratory of Social Evolution and Behavior
  Group /general/optophysiology/ImagingPlane at 110 um z depth (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane at 110 um z depth/Green PMT (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane at 110 um z depth/device (Device) Investigator with Coherent Axon laser, dual GaAsP detectors, resonant scanning galvanometer, Z-piezo, 40x 0.9NA water immersion objective
  session_id: m1-d11-y2023-ant1-0.03x-3-hexanone-40-t131-z110um
  Group /general/subject (Subject) 
  identifier: 2f7f795e-14a8-4e97-a132-ab6a08f0b131
  session_description: 5s odor stimulation at 33 z depths
  session_start_time: 2023-01-11T15:07:32-05:00
  timestamps_reference_time: 2023-01-11T15:07:32-05:00
