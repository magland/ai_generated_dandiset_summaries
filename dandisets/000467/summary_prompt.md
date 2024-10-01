
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000467/draft
name: Sparse and stereotyped encoding implicates a core glomerulus for ant alarm behavior
contributor: [{'name': 'National Institutes of Health (NIH)', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': '1 R01 NS 123899-02'}, {'name': 'Hart, Taylor', 'email': 'thart@rockefeller.edu', 'roleName': ['dcite:Author', 'dcite:DataCollector', 'dcite:ContactPerson', 'dcite:Conceptualization'], 'schemaKey': 'Person', 'identifier': '0000-0001-9692-8150', 'affiliation': [], 'includeInCitation': False}]
description: In these experiments, we recorded odor-evoked calcium responses in the antennal lobe of the clonal raider ant (Ooceraea biroi). Transgenic ants expressed GCaMP6s in olfactory sensory neurons, and the right antennal lobe was imaged using a two-photon microscope. A piezo device and resonant scanning galvanometer were used to image whole-antennal lobe volumes at a rate of 0.83 volumes per second. 33 z-planes were imaged at 5 micrometer intervals. In each recording, odor stimulus commenced after 3s and lasted for 5s. Negative control: paraffin oil. General odorant stimuli: isopropanol, ethylpyrazine, ethanol, 3-hexanone, propionic acid. Ant alarm pheromones: 4-methyl-3-heptanone, 4-methyl-3-heptanol, 4-methyl-3-hexanol, 6-methyl-5-hepten-2-one.

Experiment key:
General odorant experiment subjects:
sub-ant1-m10-d6-y2022
sub-ant3-m10-d6-y2022
sub-ant1-m10-d11-y2022
sub-ant2-m10-d11-y2022
sub-ant3-m10-d11-y2022
sub-ant5-m10-d11-y2022

Bilateral antennal lobe imaging experiment subjects:
sub-ant2-m2-d10-y2023
sub-ant3-m2-d10-y2023
sub-ant4-m2-d10-y2023

Unilateral alarm pheromone imaging experiment subjects:
sub-ant2-m4-d20-y2022
sub-ant4-m4-d20-y2022
sub-ant1-m4-d21-y2022
sub-ant2-m4-d21-y2022
sub-ant3-m4-d21-y2022
sub-ant1-m4-d26-y2022
sub-ant2-m4-d26-y2022
sub-ant3-m4-d26-y2022
sub-ant4-m4-d26-y2022
sub-ant5-m4-d26-y2022
sub-ant1-m4-d27-y2022
sub-ant2-m4-d27-y2022
sub-ant3-m4-d27-y2022
assetsSummary: {'species': [{'name': 'Ooceraea biroi - Clonal raider ant', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_2015173'}], 'approach': [{'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 1262490250560, 'numberOfFiles': 14685, 'numberOfSubjects': 22, 'variableMeasured': ['OpticalChannel', 'ImagingPlane', 'TwoPhotonSeries'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'two-photon microscopy technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000467 has 16 NWB files.
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
  file_create_date: ['2023-05-16T15:07:03.630296-04:00']
  Group /general/devices/Kronauer Lab two-photon microscope (Device) Investigator with Coherent Axon laser, dual GaAsP detectors, resonant scanning galvanometer, Z-piezo, 40x 0.9NA water immersion objective
  experiment_description: 40 cycle 2photon recording, 5s odor stim triggered at 3s, using 0.48x 3-hexanone at z depth 0 um in the clonal raider ant antennal lobe, transgenic line expressing GCaMP6s in olfactory sensory neurons
  experimenter: ['Hart, Taylor']
  institution: The Rockefeller University, New York
  keywords: ['antennal lobe' 'calcium imaging' 'chemosensation' 'clonal raider ant'
   'communication' 'GCaMP' 'odor coding' 'olfaction' 'Ooceraea biroi'
   'pheromone']
  lab: Laboratory of Social Evolution and Behavior
  Group /general/optophysiology/ImagingPlane at 0 um z depth (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane at 0 um z depth/Green PMT (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane at 0 um z depth/device (Device) Investigator with Coherent Axon laser, dual GaAsP detectors, resonant scanning galvanometer, Z-piezo, 40x 0.9NA water immersion objective
  session_id: m10-d11-y2022-ant1-0.48x-3-hexanone-40-t125-z0um
  Group /general/subject (Subject) 
  identifier: 5d59effa-7f88-43e1-bde7-7a9525a6eda6
  session_description: 5s odor stimulation at 33 z depths
  session_start_time: 2022-10-11T00:40:43-04:00
  timestamps_reference_time: 2022-10-11T00:40:43-04:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/TwoPhotonSeries1 (TwoPhotonSeries) two photon recording, 40 cycles total, recording time 48.0s, odor stimulus triggered at 3s with duration 5s
  Group /acquisition/TwoPhotonSeries1/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeries1/imaging_plane/Green PMT (OpticalChannel) 
  Group /acquisition/TwoPhotonSeries1/imaging_plane/device (Device) Investigator with Coherent Axon laser, dual GaAsP detectors, resonant scanning galvanometer, Z-piezo, 40x 0.9NA water immersion objective
  file_create_date: ['2023-05-16T15:08:22.367140-04:00']
  Group /general/devices/Kronauer Lab two-photon microscope (Device) Investigator with Coherent Axon laser, dual GaAsP detectors, resonant scanning galvanometer, Z-piezo, 40x 0.9NA water immersion objective
  experiment_description: 40 cycle 2photon recording, 5s odor stim triggered at 3s, using 0.48x 3-hexanone at z depth 100 um in the clonal raider ant antennal lobe, transgenic line expressing GCaMP6s in olfactory sensory neurons
  experimenter: ['Hart, Taylor']
  institution: The Rockefeller University, New York
  keywords: ['antennal lobe' 'calcium imaging' 'chemosensation' 'clonal raider ant'
   'communication' 'GCaMP' 'odor coding' 'olfaction' 'Ooceraea biroi'
   'pheromone']
  lab: Laboratory of Social Evolution and Behavior
  Group /general/optophysiology/ImagingPlane at 100 um z depth (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane at 100 um z depth/Green PMT (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane at 100 um z depth/device (Device) Investigator with Coherent Axon laser, dual GaAsP detectors, resonant scanning galvanometer, Z-piezo, 40x 0.9NA water immersion objective
  session_id: m10-d11-y2022-ant1-0.48x-3-hexanone-40-t125-z100um
  Group /general/subject (Subject) 
  identifier: b7165ce6-99a9-40ed-a5da-5bb10cb7136d
  session_description: 5s odor stimulation at 33 z depths
  session_start_time: 2022-10-11T00:40:43-04:00
  timestamps_reference_time: 2022-10-11T00:40:43-04:00


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/TwoPhotonSeries1 (TwoPhotonSeries) two photon recording, 40 cycles total, recording time 48.0s, odor stimulus triggered at 3s with duration 5s
  Group /acquisition/TwoPhotonSeries1/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeries1/imaging_plane/Green PMT (OpticalChannel) 
  Group /acquisition/TwoPhotonSeries1/imaging_plane/device (Device) Investigator with Coherent Axon laser, dual GaAsP detectors, resonant scanning galvanometer, Z-piezo, 40x 0.9NA water immersion objective
  file_create_date: ['2023-05-16T15:08:24.445028-04:00']
  Group /general/devices/Kronauer Lab two-photon microscope (Device) Investigator with Coherent Axon laser, dual GaAsP detectors, resonant scanning galvanometer, Z-piezo, 40x 0.9NA water immersion objective
  experiment_description: 40 cycle 2photon recording, 5s odor stim triggered at 3s, using 0.48x 3-hexanone at z depth 105 um in the clonal raider ant antennal lobe, transgenic line expressing GCaMP6s in olfactory sensory neurons
  experimenter: ['Hart, Taylor']
  institution: The Rockefeller University, New York
  keywords: ['antennal lobe' 'calcium imaging' 'chemosensation' 'clonal raider ant'
   'communication' 'GCaMP' 'odor coding' 'olfaction' 'Ooceraea biroi'
   'pheromone']
  lab: Laboratory of Social Evolution and Behavior
  Group /general/optophysiology/ImagingPlane at 105 um z depth (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane at 105 um z depth/Green PMT (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane at 105 um z depth/device (Device) Investigator with Coherent Axon laser, dual GaAsP detectors, resonant scanning galvanometer, Z-piezo, 40x 0.9NA water immersion objective
  session_id: m10-d11-y2022-ant1-0.48x-3-hexanone-40-t125-z105um
  Group /general/subject (Subject) 
  identifier: c4ae22bc-3176-4404-8946-8ff22283172f
  session_description: 5s odor stimulation at 33 z depths
  session_start_time: 2022-10-11T00:40:43-04:00
  timestamps_reference_time: 2022-10-11T00:40:43-04:00


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/TwoPhotonSeries1 (TwoPhotonSeries) two photon recording, 40 cycles total, recording time 48.0s, odor stimulus triggered at 3s with duration 5s
  Group /acquisition/TwoPhotonSeries1/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeries1/imaging_plane/Green PMT (OpticalChannel) 
  Group /acquisition/TwoPhotonSeries1/imaging_plane/device (Device) Investigator with Coherent Axon laser, dual GaAsP detectors, resonant scanning galvanometer, Z-piezo, 40x 0.9NA water immersion objective
  file_create_date: ['2023-05-16T15:07:19.553183-04:00']
  Group /general/devices/Kronauer Lab two-photon microscope (Device) Investigator with Coherent Axon laser, dual GaAsP detectors, resonant scanning galvanometer, Z-piezo, 40x 0.9NA water immersion objective
  experiment_description: 40 cycle 2photon recording, 5s odor stim triggered at 3s, using 0.48x 3-hexanone at z depth 10 um in the clonal raider ant antennal lobe, transgenic line expressing GCaMP6s in olfactory sensory neurons
  experimenter: ['Hart, Taylor']
  institution: The Rockefeller University, New York
  keywords: ['antennal lobe' 'calcium imaging' 'chemosensation' 'clonal raider ant'
   'communication' 'GCaMP' 'odor coding' 'olfaction' 'Ooceraea biroi'
   'pheromone']
  lab: Laboratory of Social Evolution and Behavior
  Group /general/optophysiology/ImagingPlane at 10 um z depth (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane at 10 um z depth/Green PMT (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane at 10 um z depth/device (Device) Investigator with Coherent Axon laser, dual GaAsP detectors, resonant scanning galvanometer, Z-piezo, 40x 0.9NA water immersion objective
  session_id: m10-d11-y2022-ant1-0.48x-3-hexanone-40-t125-z10um
  Group /general/subject (Subject) 
  identifier: fe968809-0f56-4d05-afbf-b0356934884d
  session_description: 5s odor stimulation at 33 z depths
  session_start_time: 2022-10-11T00:40:43-04:00
  timestamps_reference_time: 2022-10-11T00:40:43-04:00


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  Group /acquisition/TwoPhotonSeries1 (TwoPhotonSeries) two photon recording, 40 cycles total, recording time 48.0s, odor stimulus triggered at 3s with duration 5s
  Group /acquisition/TwoPhotonSeries1/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeries1/imaging_plane/Green PMT (OpticalChannel) 
  Group /acquisition/TwoPhotonSeries1/imaging_plane/device (Device) Investigator with Coherent Axon laser, dual GaAsP detectors, resonant scanning galvanometer, Z-piezo, 40x 0.9NA water immersion objective
  file_create_date: ['2023-05-16T15:08:26.837261-04:00']
  Group /general/devices/Kronauer Lab two-photon microscope (Device) Investigator with Coherent Axon laser, dual GaAsP detectors, resonant scanning galvanometer, Z-piezo, 40x 0.9NA water immersion objective
  experiment_description: 40 cycle 2photon recording, 5s odor stim triggered at 3s, using 0.48x 3-hexanone at z depth 110 um in the clonal raider ant antennal lobe, transgenic line expressing GCaMP6s in olfactory sensory neurons
  experimenter: ['Hart, Taylor']
  institution: The Rockefeller University, New York
  keywords: ['antennal lobe' 'calcium imaging' 'chemosensation' 'clonal raider ant'
   'communication' 'GCaMP' 'odor coding' 'olfaction' 'Ooceraea biroi'
   'pheromone']
  lab: Laboratory of Social Evolution and Behavior
  Group /general/optophysiology/ImagingPlane at 110 um z depth (ImagingPlane) 
  Group /general/optophysiology/ImagingPlane at 110 um z depth/Green PMT (OpticalChannel) 
  Group /general/optophysiology/ImagingPlane at 110 um z depth/device (Device) Investigator with Coherent Axon laser, dual GaAsP detectors, resonant scanning galvanometer, Z-piezo, 40x 0.9NA water immersion objective
  session_id: m10-d11-y2022-ant1-0.48x-3-hexanone-40-t125-z110um
  Group /general/subject (Subject) 
  identifier: 993f53d0-7052-4032-b611-92b5120e08e2
  session_description: 5s odor stimulation at 33 z depths
  session_start_time: 2022-10-11T00:40:43-04:00
  timestamps_reference_time: 2022-10-11T00:40:43-04:00
