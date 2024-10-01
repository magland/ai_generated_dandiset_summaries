
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000935/0.240319.2026
name: Interluminescence:  Selective Control of Synaptically-Connected Circuit Elements using bioluminescence
contributor: [{'name': 'National Institutes of Health (NIH)', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': '1 R01 NS 120832-21'}, {'name': 'Prakash, Mansi', 'roleName': ['dcite:Researcher'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Murphy, Jeremy', 'roleName': ['dcite:Researcher'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Friedman, Nina', 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'St Laurent, Robyn', 'schemaKey': 'Person', 'includeInCitation': False}, {'name': 'Bjorefeldt, Andreas', 'schemaKey': 'Person', 'includeInCitation': False}, {'name': 'Pal, Akash', 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Bhagat, Yuvraj', 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Kauer, Julie A.', 'schemaKey': 'Person', 'includeInCitation': False}, {'name': 'Shaner, Nathan C.', 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Lipscombe, Diane', 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Hochgeschwender, Ute', 'email': 'hochg1u@cmich.edu', 'roleName': ['dcite:ContactPerson', 'dcite:ProjectLeader'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Moore, Christopher I.', 'email': 'christopher_moore@brown.edu', 'roleName': ['dcite:ProjectLeader', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Crespo, Emmanuel L.', 'schemaKey': 'Person', 'includeInCitation': True}]
description: This is the repository for in vivo extracellular electrophysiology testing a bioluminescent-optogenetic synaptic element. In this experiment (see doi: 10.1038/s42003-021-02981-7), extracellular electrophysiology data and 1-photon bioluminescent imaging data were recorded from six PV-Cre mice under isoflurane anesthesia. There are two groups (Opsin(+) and Opsin(-), see session description and doi: 10.1038/s42003-021-02981-7 for details) of 3 animals each. For all animals a baseline of ~3 minutes of data was recorded, after which the bioluminescent luciferin Coelenterazine was infused into a saline well over an open craniotomy exposing barrel cortex. Time Intervals in the data set designate the start and stop times of Coelenterazine infusion in seconds.
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}, {'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 49105883680, 'numberOfFiles': 6, 'numberOfSubjects': 6, 'variableMeasured': ['ElectrodeGroup', 'ElectricalSeries', 'OpticalChannel', 'ImagingPlane'], 'measurementTechnique': [{'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000935 has 6 NWB files.
5 of these NWB files are of type 1.
1 of these NWB files are of type 2.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/1pInternal (OnePhotonSeries) h x w x time (1 Hz) images of bioluminescent output from barrel cortex
  Group /acquisition/1pInternal/imaging_plane (ImagingPlane) 
  Group /acquisition/1pInternal/imaging_plane/device (Device) ixon 888 Ultra EMCCD camera
  Group /acquisition/1pInternal/imaging_plane/optical_channel (OpticalChannel) 
  Group /acquisition/ElectricalSeries (ElectricalSeries) extracellular ephys acquired at 20kHz, downsampled to 10kHz.
  Dataset /acquisition/ElectricalSeries/electrodes (DynamicTableRegion) all electrodes | shape = (32,) | dtype = int64
  file_create_date: ['2024-03-19T14:29:31.826164-04:00']
  Group /general/devices/Camera (Device) ixon 888 Ultra EMCCD camera
  Group /general/devices/Ephys Acquisition Board (Device) Open Ephys Acquisition Board
  Group /general/devices/Head Stage (Device) Intan 32-Channel Recording Headstage; Part #C3314 RHD 32ch
  Group /general/devices/array (Device) A1x32-Poly2-5mm-50s-177
  experiment_description: In this experiment (see doi: 10.1038/s42003-021-02981-7), extracellular electrophysiology data and 1-photon bioluminescent imaging data were recorded from six PV-Cre mice under isoflurane anesthesia. There are two groups (Opsin(+) and Opsin(-), see session description and doi: 10.1038/s42003-021-02981-7 for details) of 3 animals each. For all animals a baseline of ~3 minutes of data was recorded, after which the bioluminescent luciferin Coelenterazine was infused into a saline well over an open craniotomy exposing barrel cortex. Time Intervals in the data set designate the start and stop times of Coelenterazine infusion in seconds.
  experimenter: ['Murphy, Jeremy']
  Group /general/extracellular_ephys/electrodes (DynamicTable) all electrodes
  Dataset /general/extracellular_ephys/electrodes/Position (VectorData) AUTOGENERATED description for column `Position` | shape = (96,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/Position_index (VectorIndex) Index into column Position | shape = (32,) | dtype = uint64
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) AUTOGENERATED description for column `group` | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) AUTOGENERATED description for column `group_name` | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (32,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/label (VectorData) AUTOGENERATED description for column `label` | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) AUTOGENERATED description for column `location` | shape = (32,) | dtype = object
  Group /general/extracellular_ephys/shank1 (ElectrodeGroup) electrode group for shank1
  Group /general/extracellular_ephys/shank1/device (Device) A1x32-Poly2-5mm-50s-177
  institution: Brown University, Providence, RI, USA
  keywords: ['Bioluminescence' 'Optogenetics']
  Group /general/optophysiology/1photonBioluminescence (ImagingPlane) 
  Group /general/optophysiology/1photonBioluminescence/device (Device) ixon 888 Ultra EMCCD camera
  Group /general/optophysiology/1photonBioluminescence/optical_channel (OpticalChannel) 
  protocol: IACUC 20-09-0003
  related_publications: ['doi: 10.1038/s42003-021-02981-7']
  Group /general/subject (Subject) 
  identifier: interlum_4
  Group /intervals/trials (TimeIntervals) time of ctz infusion
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /intervals/trials/start_time (VectorData) injection start time | shape = (1,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) injection end time | shape = (1,) | dtype = float64
  session_description: Anesthetized, bioluminescent luciferin delivered to cortex
  session_start_time: ['2019-05-15T12:00:00.000000-04:00']
  timestamps_reference_time: ['2019-05-15T12:00:00.000000-04:00']


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/ElectricalSeries (ElectricalSeries) extracellular ephys acquired at 20kHz, downsampled to 10kHz.
  Dataset /acquisition/ElectricalSeries/electrodes (DynamicTableRegion) all electrodes | shape = (32,) | dtype = int64
  file_create_date: ['2024-03-19T14:42:18.297346-04:00']
  Group /general/devices/Ephys Acquisition Board (Device) Open Ephys Acquisition Board
  Group /general/devices/Head Stage (Device) Intan 32-Channel Recording Headstage; Part #C3314 RHD 32ch
  Group /general/devices/array (Device) A1x32-Poly2-5mm-50s-177
  experiment_description: In this experiment (see doi: 10.1038/s42003-021-02981-7), extracellular electrophysiology data and 1-photon bioluminescent imaging data were recorded from six PV-Cre mice under isoflurane anesthesia. There are two groups (Opsin(+) and Opsin(-), see session description and doi: 10.1038/s42003-021-02981-7 for details) of 3 animals each. For all animals a baseline of ~3 minutes of data was recorded, after which the bioluminescent luciferin Coelenterazine was infused into a saline well over an open craniotomy exposing barrel cortex. Time Intervals in the data set designate the start and stop times of Coelenterazine infusion in seconds.
  experimenter: ['Murphy, Jeremy']
  Group /general/extracellular_ephys/electrodes (DynamicTable) all electrodes
  Dataset /general/extracellular_ephys/electrodes/Position (VectorData) AUTOGENERATED description for column `Position` | shape = (96,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/Position_index (VectorIndex) Index into column Position | shape = (32,) | dtype = uint64
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) AUTOGENERATED description for column `group` | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) AUTOGENERATED description for column `group_name` | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (32,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/label (VectorData) AUTOGENERATED description for column `label` | shape = (32,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) AUTOGENERATED description for column `location` | shape = (32,) | dtype = object
  Group /general/extracellular_ephys/shank1 (ElectrodeGroup) electrode group for shank1
  Group /general/extracellular_ephys/shank1/device (Device) A1x32-Poly2-5mm-50s-177
  institution: Brown University, Providence, RI, USA
  keywords: ['Bioluminescence' 'Optogenetics']
  protocol: IACUC 20-09-0003
  related_publications: ['doi: 10.1038/s42003-021-02981-7']
  Group /general/subject (Subject) 
  identifier: interlum_6
  Group /intervals/trials (TimeIntervals) time of ctz infusion
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /intervals/trials/start_time (VectorData) injection start time | shape = (1,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) injection end time | shape = (1,) | dtype = float64
  session_description: Anesthetized, bioluminescent luciferin delivered to cortex
  session_start_time: ['2019-06-05T12:00:00.000000-04:00']
  timestamps_reference_time: ['2019-06-05T12:00:00.000000-04:00']
