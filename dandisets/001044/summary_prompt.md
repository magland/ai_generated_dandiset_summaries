
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001044/0.240905.0159
name: Dataset of long-term multi-site LFP activity with spontaneous chronic seizures recorded in temporal lobe epilepsy rats.
contributor: [{'name': 'Haoqi, Ni', 'email': 'nihq@zju.edu.cn', 'roleName': ['dcite:Author', 'dcite:DataManager', 'dcite:FormalAnalysis'], 'schemaKey': 'Person', 'identifier': '0009-0003-1749-4043', 'includeInCitation': True}, {'name': 'Yufang, Yang', 'roleName': ['dcite:Author', 'dcite:DataCollector', 'dcite:Researcher'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Fang, Zhang', 'roleName': ['dcite:DataCollector', 'dcite:Researcher'], 'schemaKey': 'Person', 'identifier': '0000-0003-2585-4611', 'includeInCitation': True}, {'name': 'Yuting, Sun', 'email': 'sunyt@zju.edu.cn', 'roleName': ['dcite:DataCollector', 'dcite:Researcher'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Yongte, Zheng', 'roleName': ['dcite:DataCollector', 'dcite:Researcher'], 'schemaKey': 'Person', 'identifier': '0000-0002-2576-6796', 'includeInCitation': True}, {'name': 'Junming, Zhu', 'roleName': ['dcite:Supervision', 'dcite:Validation'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Kedi, Xu', 'email': 'xukd@zju.edu.cn', 'roleName': ['dcite:ContactPerson', 'dcite:ProjectAdministration', 'dcite:Supervision'], 'schemaKey': 'Person', 'identifier': '0000-0002-9059-3860', 'includeInCitation': True}, {'name': 'STI 2030—Major Projects', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': '2021ZD0200405', 'includeInCitation': False}, {'name': 'National Natural Science Foundation of China', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': '82272112', 'includeInCitation': False}, {'name': 'Outstanding Youth Program of Zhejiang Natural Science Foundation', 'schemaKey': 'Organization', 'awardNumber': 'LR23H180002', 'includeInCitation': False}, {'name': 'the Fundamental Research Funds for the Central Universities', 'schemaKey': 'Organization', 'awardNumber': '2021KYY600403-0001', 'includeInCitation': False}, {'name': 'the Starry Night Science Fund of Zhejiang University Shanghai Institute for Advanced Study', 'schemaKey': 'Organization', 'awardNumber': 'SN-ZJU-SIAS-002', 'includeInCitation': False}]
description: We provided a long-term brain electrophysiological dataset of 15 pilocarpine-treated temporal lobe epilepsy (TLE) rats during the development of epilepsy. The dataset was constituted by multi-site local field potential (LFP) signal recorded from 12 sites in the circuit of Papez in TLE, including spontaneous seizures and interictal fragments in the chronic period. The LFP data were saved in MATLAB, stored as the Neurodata Without Borders (NWB) standard, and published on the DANDI Archive. The dataset can be used to evaluate the alterations of seizure onset zone (SOZ), seizure onset pattern (SOP), and functional network connectivity during the development of epilepsy. We have technically validated the dataset through histology and specific signal analysis. In addition, we provided MATLAB codes for basic analyses of this dataset, including power spectral analysis, SOP identification, and interictal spike detection. The dataset is available to reveal how brain electrophysiological and epileptic network properties of chronic TLE rats change from early to late stages, and help inform the design of adaptive neuromodulation for epilepsy.
assetsSummary: {'species': [{'name': 'Rattus norvegicus - Norway rat', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10116'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 17935587444, 'numberOfFiles': 162, 'numberOfSubjects': 15, 'variableMeasured': ['ElectricalSeries', 'ElectrodeGroup'], 'measurementTechnique': [{'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 001044 has 5 NWB files.
1 of these NWB files are of type 1.
1 of these NWB files are of type 2.
1 of these NWB files are of type 3.
1 of these NWB files are of type 4.
1 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/B6_2023_5_16-non1 (ElectricalSeries) Raw acquisition at early stage
  Dataset /acquisition/B6_2023_5_16-non1/electrodes (DynamicTableRegion) all electrodes | shape = (12,) | dtype = int64
  Group /acquisition/B6_2023_5_16-non2 (ElectricalSeries) Raw acquisition at early stage
  Dataset /acquisition/B6_2023_5_16-non2/electrodes (DynamicTableRegion) all electrodes | shape = (12,) | dtype = int64
  file_create_date: ['2024-07-30T15:38:17.435592+08:00']
  Group /general/devices/implant (Device) Depth electrodes
  Group /general/extracellular_ephys/L_AMD (ElectrodeGroup) electrode group for L_AMD
  Group /general/extracellular_ephys/L_AMD/device (Device) Depth electrodes
  Group /general/extracellular_ephys/L_ANT (ElectrodeGroup) electrode group for L_ANT
  Group /general/extracellular_ephys/L_ANT/device (Device) Depth electrodes
  Group /general/extracellular_ephys/L_CA1 (ElectrodeGroup) electrode group for L_CA1
  Group /general/extracellular_ephys/L_CA1/device (Device) Depth electrodes
  Group /general/extracellular_ephys/L_CA3 (ElectrodeGroup) electrode group for L_CA3
  Group /general/extracellular_ephys/L_CA3/device (Device) Depth electrodes
  Group /general/extracellular_ephys/L_DG (ElectrodeGroup) electrode group for L_DG
  Group /general/extracellular_ephys/L_DG/device (Device) Depth electrodes
  Group /general/extracellular_ephys/L_SUB (ElectrodeGroup) electrode group for L_SUB
  Group /general/extracellular_ephys/L_SUB/device (Device) Depth electrodes
  Group /general/extracellular_ephys/R_AMD (ElectrodeGroup) electrode group for R_AMD
  Group /general/extracellular_ephys/R_AMD/device (Device) Depth electrodes
  Group /general/extracellular_ephys/R_ANT (ElectrodeGroup) electrode group for R_ANT
  Group /general/extracellular_ephys/R_ANT/device (Device) Depth electrodes
  Group /general/extracellular_ephys/R_CA1 (ElectrodeGroup) electrode group for R_CA1
  Group /general/extracellular_ephys/R_CA1/device (Device) Depth electrodes
  Group /general/extracellular_ephys/R_CA3 (ElectrodeGroup) electrode group for R_CA3
  Group /general/extracellular_ephys/R_CA3/device (Device) Depth electrodes
  Group /general/extracellular_ephys/R_DG (ElectrodeGroup) electrode group for R_DG
  Group /general/extracellular_ephys/R_DG/device (Device) Depth electrodes
  Group /general/extracellular_ephys/R_SUB (ElectrodeGroup) electrode group for R_SUB
  Group /general/extracellular_ephys/R_SUB/device (Device) Depth electrodes
  Group /general/extracellular_ephys/electrodes (DynamicTable) all electrodes
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) AUTOGENERATED description for column `group` | shape = (12,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) AUTOGENERATED description for column `group_name` | shape = (12,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (12,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/label (VectorData) AUTOGENERATED description for column `label` | shape = (12,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) AUTOGENERATED description for column `location` | shape = (12,) | dtype = object
  institution: Zhejiang University
  session_id: RatB6_2023_5_16
  Group /general/subject (Subject) 
  identifier: RatB6_2023_5_16
  session_description: Multi-site LFP activity recorded in temporal lobe epilepsy rats
  session_start_time: ['2023-05-16T00:00:00.000000+08:00']
  timestamps_reference_time: ['2023-05-16T00:00:00.000000+08:00']


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/B6_2023_5_19-ictal1 (ElectricalSeries) Raw acquisition at early stage
  Dataset /acquisition/B6_2023_5_19-ictal1/electrodes (DynamicTableRegion) all electrodes | shape = (12,) | dtype = int64
  Group /acquisition/B6_2023_5_19-ictal2 (ElectricalSeries) Raw acquisition at early stage
  Dataset /acquisition/B6_2023_5_19-ictal2/electrodes (DynamicTableRegion) all electrodes | shape = (12,) | dtype = int64
  Group /acquisition/B6_2023_5_19-ictal3 (ElectricalSeries) Raw acquisition at early stage
  Dataset /acquisition/B6_2023_5_19-ictal3/electrodes (DynamicTableRegion) all electrodes | shape = (12,) | dtype = int64
  Group /acquisition/B6_2023_5_19-ictal4 (ElectricalSeries) Raw acquisition at early stage
  Dataset /acquisition/B6_2023_5_19-ictal4/electrodes (DynamicTableRegion) all electrodes | shape = (12,) | dtype = int64
  Group /acquisition/B6_2023_5_19-ictal5 (ElectricalSeries) Raw acquisition at early stage
  Dataset /acquisition/B6_2023_5_19-ictal5/electrodes (DynamicTableRegion) all electrodes | shape = (12,) | dtype = int64
  Group /acquisition/B6_2023_5_19-ictal6 (ElectricalSeries) Raw acquisition at early stage
  Dataset /acquisition/B6_2023_5_19-ictal6/electrodes (DynamicTableRegion) all electrodes | shape = (12,) | dtype = int64
  file_create_date: ['2024-07-30T15:39:53.282462+08:00']
  Group /general/devices/implant (Device) Depth electrodes
  Group /general/extracellular_ephys/L_AMD (ElectrodeGroup) electrode group for L_AMD
  Group /general/extracellular_ephys/L_AMD/device (Device) Depth electrodes
  Group /general/extracellular_ephys/L_ANT (ElectrodeGroup) electrode group for L_ANT
  Group /general/extracellular_ephys/L_ANT/device (Device) Depth electrodes
  Group /general/extracellular_ephys/L_CA1 (ElectrodeGroup) electrode group for L_CA1
  Group /general/extracellular_ephys/L_CA1/device (Device) Depth electrodes
  Group /general/extracellular_ephys/L_CA3 (ElectrodeGroup) electrode group for L_CA3
  Group /general/extracellular_ephys/L_CA3/device (Device) Depth electrodes
  Group /general/extracellular_ephys/L_DG (ElectrodeGroup) electrode group for L_DG
  Group /general/extracellular_ephys/L_DG/device (Device) Depth electrodes
  Group /general/extracellular_ephys/L_SUB (ElectrodeGroup) electrode group for L_SUB
  Group /general/extracellular_ephys/L_SUB/device (Device) Depth electrodes
  Group /general/extracellular_ephys/R_AMD (ElectrodeGroup) electrode group for R_AMD
  Group /general/extracellular_ephys/R_AMD/device (Device) Depth electrodes
  Group /general/extracellular_ephys/R_ANT (ElectrodeGroup) electrode group for R_ANT
  Group /general/extracellular_ephys/R_ANT/device (Device) Depth electrodes
  Group /general/extracellular_ephys/R_CA1 (ElectrodeGroup) electrode group for R_CA1
  Group /general/extracellular_ephys/R_CA1/device (Device) Depth electrodes
  Group /general/extracellular_ephys/R_CA3 (ElectrodeGroup) electrode group for R_CA3
  Group /general/extracellular_ephys/R_CA3/device (Device) Depth electrodes
  Group /general/extracellular_ephys/R_DG (ElectrodeGroup) electrode group for R_DG
  Group /general/extracellular_ephys/R_DG/device (Device) Depth electrodes
  Group /general/extracellular_ephys/R_SUB (ElectrodeGroup) electrode group for R_SUB
  Group /general/extracellular_ephys/R_SUB/device (Device) Depth electrodes
  Group /general/extracellular_ephys/electrodes (DynamicTable) all electrodes
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) AUTOGENERATED description for column `group` | shape = (12,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) AUTOGENERATED description for column `group_name` | shape = (12,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (12,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/label (VectorData) AUTOGENERATED description for column `label` | shape = (12,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) AUTOGENERATED description for column `location` | shape = (12,) | dtype = object
  institution: Zhejiang University
  session_id: RatB6_2023_5_19
  Group /general/subject (Subject) 
  identifier: RatB6_2023_5_19
  session_description: Multi-site LFP activity recorded in temporal lobe epilepsy rats
  session_start_time: ['2023-05-19T00:00:00.000000+08:00']
  timestamps_reference_time: ['2023-05-19T00:00:00.000000+08:00']


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/B6_2023_5_20-ictal1 (ElectricalSeries) Raw acquisition at early stage
  Dataset /acquisition/B6_2023_5_20-ictal1/electrodes (DynamicTableRegion) all electrodes | shape = (12,) | dtype = int64
  Group /acquisition/B6_2023_5_20-ictal10 (ElectricalSeries) Raw acquisition at early stage
  Dataset /acquisition/B6_2023_5_20-ictal10/electrodes (DynamicTableRegion) all electrodes | shape = (12,) | dtype = int64
  Group /acquisition/B6_2023_5_20-ictal11 (ElectricalSeries) Raw acquisition at early stage
  Dataset /acquisition/B6_2023_5_20-ictal11/electrodes (DynamicTableRegion) all electrodes | shape = (12,) | dtype = int64
  Group /acquisition/B6_2023_5_20-ictal12 (ElectricalSeries) Raw acquisition at early stage
  Dataset /acquisition/B6_2023_5_20-ictal12/electrodes (DynamicTableRegion) all electrodes | shape = (12,) | dtype = int64
  Group /acquisition/B6_2023_5_20-ictal13 (ElectricalSeries) Raw acquisition at early stage
  Dataset /acquisition/B6_2023_5_20-ictal13/electrodes (DynamicTableRegion) all electrodes | shape = (12,) | dtype = int64
  Group /acquisition/B6_2023_5_20-ictal14 (ElectricalSeries) Raw acquisition at early stage
  Dataset /acquisition/B6_2023_5_20-ictal14/electrodes (DynamicTableRegion) all electrodes | shape = (12,) | dtype = int64
  Group /acquisition/B6_2023_5_20-ictal15 (ElectricalSeries) Raw acquisition at early stage
  Dataset /acquisition/B6_2023_5_20-ictal15/electrodes (DynamicTableRegion) all electrodes | shape = (12,) | dtype = int64
  Group /acquisition/B6_2023_5_20-ictal16 (ElectricalSeries) Raw acquisition at early stage
  Dataset /acquisition/B6_2023_5_20-ictal16/electrodes (DynamicTableRegion) all electrodes | shape = (12,) | dtype = int64
  Group /acquisition/B6_2023_5_20-ictal17 (ElectricalSeries) Raw acquisition at early stage
  Dataset /acquisition/B6_2023_5_20-ictal17/electrodes (DynamicTableRegion) all electrodes | shape = (12,) | dtype = int64
  Group /acquisition/B6_2023_5_20-ictal18 (ElectricalSeries) Raw acquisition at early stage
  Dataset /acquisition/B6_2023_5_20-ictal18/electrodes (DynamicTableRegion) all electrodes | shape = (12,) | dtype = int64
  Group /acquisition/B6_2023_5_20-ictal19 (ElectricalSeries) Raw acquisition at early stage
  Dataset /acquisition/B6_2023_5_20-ictal19/electrodes (DynamicTableRegion) all electrodes | shape = (12,) | dtype = int64
  Group /acquisition/B6_2023_5_20-ictal2 (ElectricalSeries) Raw acquisition at early stage
  Dataset /acquisition/B6_2023_5_20-ictal2/electrodes (DynamicTableRegion) all electrodes | shape = (12,) | dtype = int64
  Group /acquisition/B6_2023_5_20-ictal20 (ElectricalSeries) Raw acquisition at early stage
  Dataset /acquisition/B6_2023_5_20-ictal20/electrodes (DynamicTableRegion) all electrodes | shape = (12,) | dtype = int64
  Group /acquisition/B6_2023_5_20-ictal21 (ElectricalSeries) Raw acquisition at early stage
  Dataset /acquisition/B6_2023_5_20-ictal21/electrodes (DynamicTableRegion) all electrodes | shape = (12,) | dtype = int64
  Group /acquisition/B6_2023_5_20-ictal22 (ElectricalSeries) Raw acquisition at early stage
  Dataset /acquisition/B6_2023_5_20-ictal22/electrodes (DynamicTableRegion) all electrodes | shape = (12,) | dtype = int64
  Group /acquisition/B6_2023_5_20-ictal23 (ElectricalSeries) Raw acquisition at early stage
  Dataset /acquisition/B6_2023_5_20-ictal23/electrodes (DynamicTableRegion) all electrodes | shape = (12,) | dtype = int64
  Group /acquisition/B6_2023_5_20-ictal24 (ElectricalSeries) Raw acquisition at early stage
  Dataset /acquisition/B6_2023_5_20-ictal24/electrodes (DynamicTableRegion) all electrodes | shape = (12,) | dtype = int64
  Group /acquisition/B6_2023_5_20-ictal3 (ElectricalSeries) Raw acquisition at early stage
  Dataset /acquisition/B6_2023_5_20-ictal3/electrodes (DynamicTableRegion) all electrodes | shape = (12,) | dtype = int64
  Group /acquisition/B6_2023_5_20-ictal4 (ElectricalSeries) Raw acquisition at early stage
  Dataset /acquisition/B6_2023_5_20-ictal4/electrodes (DynamicTableRegion) all electrodes | shape = (12,) | dtype = int64
  Group /acquisition/B6_2023_5_20-ictal5 (ElectricalSeries) Raw acquisition at early stage
  Dataset /acquisition/B6_2023_5_20-ictal5/electrodes (DynamicTableRegion) all electrodes | shape = (12,) | dtype = int64
  Group /acquisition/B6_2023_5_20-ictal6 (ElectricalSeries) Raw acquisition at early stage
  Dataset /acquisition/B6_2023_5_20-ictal6/electrodes (DynamicTableRegion) all electrodes | shape = (12,) | dtype = int64
  Group /acquisition/B6_2023_5_20-ictal7 (ElectricalSeries) Raw acquisition at early stage
  Dataset /acquisition/B6_2023_5_20-ictal7/electrodes (DynamicTableRegion) all electrodes | shape = (12,) | dtype = int64
  Group /acquisition/B6_2023_5_20-ictal8 (ElectricalSeries) Raw acquisition at early stage
  Dataset /acquisition/B6_2023_5_20-ictal8/electrodes (DynamicTableRegion) all electrodes | shape = (12,) | dtype = int64
  Group /acquisition/B6_2023_5_20-ictal9 (ElectricalSeries) Raw acquisition at early stage
  Dataset /acquisition/B6_2023_5_20-ictal9/electrodes (DynamicTableRegion) all electrodes | shape = (12,) | dtype = int64
  file_create_date: ['2024-07-30T15:40:44.729339+08:00']
  Group /general/devices/implant (Device) Depth electrodes
  Group /general/extracellular_ephys/L_AMD (ElectrodeGroup) electrode group for L_AMD
  Group /general/extracellular_ephys/L_AMD/device (Device) Depth electrodes
  Group /general/extracellular_ephys/L_ANT (ElectrodeGroup) electrode group for L_ANT
  Group /general/extracellular_ephys/L_ANT/device (Device) Depth electrodes
  Group /general/extracellular_ephys/L_CA1 (ElectrodeGroup) electrode group for L_CA1
  Group /general/extracellular_ephys/L_CA1/device (Device) Depth electrodes
  Group /general/extracellular_ephys/L_CA3 (ElectrodeGroup) electrode group for L_CA3
  Group /general/extracellular_ephys/L_CA3/device (Device) Depth electrodes
  Group /general/extracellular_ephys/L_DG (ElectrodeGroup) electrode group for L_DG
  Group /general/extracellular_ephys/L_DG/device (Device) Depth electrodes
  Group /general/extracellular_ephys/L_SUB (ElectrodeGroup) electrode group for L_SUB
  Group /general/extracellular_ephys/L_SUB/device (Device) Depth electrodes
  Group /general/extracellular_ephys/R_AMD (ElectrodeGroup) electrode group for R_AMD
  Group /general/extracellular_ephys/R_AMD/device (Device) Depth electrodes
  Group /general/extracellular_ephys/R_ANT (ElectrodeGroup) electrode group for R_ANT
  Group /general/extracellular_ephys/R_ANT/device (Device) Depth electrodes
  Group /general/extracellular_ephys/R_CA1 (ElectrodeGroup) electrode group for R_CA1
  Group /general/extracellular_ephys/R_CA1/device (Device) Depth electrodes
  Group /general/extracellular_ephys/R_CA3 (ElectrodeGroup) electrode group for R_CA3
  Group /general/extracellular_ephys/R_CA3/device (Device) Depth electrodes
  Group /general/extracellular_ephys/R_DG (ElectrodeGroup) electrode group for R_DG
  Group /general/extracellular_ephys/R_DG/device (Device) Depth electrodes
  Group /general/extracellular_ephys/R_SUB (ElectrodeGroup) electrode group for R_SUB
  Group /general/extracellular_ephys/R_SUB/device (Device) Depth electrodes
  Group /general/extracellular_ephys/electrodes (DynamicTable) all electrodes
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) AUTOGENERATED description for column `group` | shape = (12,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) AUTOGENERATED description for column `group_name` | shape = (12,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (12,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/label (VectorData) AUTOGENERATED description for column `label` | shape = (12,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) AUTOGENERATED description for column `location` | shape = (12,) | dtype = object
  institution: Zhejiang University
  session_id: RatB6_2023_5_20
  Group /general/subject (Subject) 
  identifier: RatB6_2023_5_20
  session_description: Multi-site LFP activity recorded in temporal lobe epilepsy rats
  session_start_time: ['2023-05-20T00:00:00.000000+08:00']
  timestamps_reference_time: ['2023-05-20T00:00:00.000000+08:00']


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/B6_2023_5_22-non1 (ElectricalSeries) Raw acquisition at early stage
  Dataset /acquisition/B6_2023_5_22-non1/electrodes (DynamicTableRegion) all electrodes | shape = (12,) | dtype = int64
  Group /acquisition/B6_2023_5_22-non2 (ElectricalSeries) Raw acquisition at early stage
  Dataset /acquisition/B6_2023_5_22-non2/electrodes (DynamicTableRegion) all electrodes | shape = (12,) | dtype = int64
  file_create_date: ['2024-07-30T15:41:27.481822+08:00']
  Group /general/devices/implant (Device) Depth electrodes
  Group /general/extracellular_ephys/L_AMD (ElectrodeGroup) electrode group for L_AMD
  Group /general/extracellular_ephys/L_AMD/device (Device) Depth electrodes
  Group /general/extracellular_ephys/L_ANT (ElectrodeGroup) electrode group for L_ANT
  Group /general/extracellular_ephys/L_ANT/device (Device) Depth electrodes
  Group /general/extracellular_ephys/L_CA1 (ElectrodeGroup) electrode group for L_CA1
  Group /general/extracellular_ephys/L_CA1/device (Device) Depth electrodes
  Group /general/extracellular_ephys/L_CA3 (ElectrodeGroup) electrode group for L_CA3
  Group /general/extracellular_ephys/L_CA3/device (Device) Depth electrodes
  Group /general/extracellular_ephys/L_DG (ElectrodeGroup) electrode group for L_DG
  Group /general/extracellular_ephys/L_DG/device (Device) Depth electrodes
  Group /general/extracellular_ephys/L_SUB (ElectrodeGroup) electrode group for L_SUB
  Group /general/extracellular_ephys/L_SUB/device (Device) Depth electrodes
  Group /general/extracellular_ephys/R_AMD (ElectrodeGroup) electrode group for R_AMD
  Group /general/extracellular_ephys/R_AMD/device (Device) Depth electrodes
  Group /general/extracellular_ephys/R_ANT (ElectrodeGroup) electrode group for R_ANT
  Group /general/extracellular_ephys/R_ANT/device (Device) Depth electrodes
  Group /general/extracellular_ephys/R_CA1 (ElectrodeGroup) electrode group for R_CA1
  Group /general/extracellular_ephys/R_CA1/device (Device) Depth electrodes
  Group /general/extracellular_ephys/R_CA3 (ElectrodeGroup) electrode group for R_CA3
  Group /general/extracellular_ephys/R_CA3/device (Device) Depth electrodes
  Group /general/extracellular_ephys/R_DG (ElectrodeGroup) electrode group for R_DG
  Group /general/extracellular_ephys/R_DG/device (Device) Depth electrodes
  Group /general/extracellular_ephys/R_SUB (ElectrodeGroup) electrode group for R_SUB
  Group /general/extracellular_ephys/R_SUB/device (Device) Depth electrodes
  Group /general/extracellular_ephys/electrodes (DynamicTable) all electrodes
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) AUTOGENERATED description for column `group` | shape = (12,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) AUTOGENERATED description for column `group_name` | shape = (12,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (12,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/label (VectorData) AUTOGENERATED description for column `label` | shape = (12,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) AUTOGENERATED description for column `location` | shape = (12,) | dtype = object
  institution: Zhejiang University
  session_id: RatB6_2023_5_22
  Group /general/subject (Subject) 
  identifier: RatB6_2023_5_22
  session_description: Multi-site LFP activity recorded in temporal lobe epilepsy rats
  session_start_time: ['2023-05-22T00:00:00.000000+08:00']
  timestamps_reference_time: ['2023-05-22T00:00:00.000000+08:00']


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  Group /acquisition/B6_2023_7_21-non1 (ElectricalSeries) Raw acquisition at late stage
  Dataset /acquisition/B6_2023_7_21-non1/electrodes (DynamicTableRegion) all electrodes | shape = (12,) | dtype = int64
  Group /acquisition/B6_2023_7_21-non2 (ElectricalSeries) Raw acquisition at late stage
  Dataset /acquisition/B6_2023_7_21-non2/electrodes (DynamicTableRegion) all electrodes | shape = (12,) | dtype = int64
  file_create_date: ['2024-07-30T15:45:05.921130+08:00']
  Group /general/devices/implant (Device) Depth electrodes
  Group /general/extracellular_ephys/L_AMD (ElectrodeGroup) electrode group for L_AMD
  Group /general/extracellular_ephys/L_AMD/device (Device) Depth electrodes
  Group /general/extracellular_ephys/L_ANT (ElectrodeGroup) electrode group for L_ANT
  Group /general/extracellular_ephys/L_ANT/device (Device) Depth electrodes
  Group /general/extracellular_ephys/L_CA1 (ElectrodeGroup) electrode group for L_CA1
  Group /general/extracellular_ephys/L_CA1/device (Device) Depth electrodes
  Group /general/extracellular_ephys/L_CA3 (ElectrodeGroup) electrode group for L_CA3
  Group /general/extracellular_ephys/L_CA3/device (Device) Depth electrodes
  Group /general/extracellular_ephys/L_DG (ElectrodeGroup) electrode group for L_DG
  Group /general/extracellular_ephys/L_DG/device (Device) Depth electrodes
  Group /general/extracellular_ephys/L_SUB (ElectrodeGroup) electrode group for L_SUB
  Group /general/extracellular_ephys/L_SUB/device (Device) Depth electrodes
  Group /general/extracellular_ephys/R_AMD (ElectrodeGroup) electrode group for R_AMD
  Group /general/extracellular_ephys/R_AMD/device (Device) Depth electrodes
  Group /general/extracellular_ephys/R_ANT (ElectrodeGroup) electrode group for R_ANT
  Group /general/extracellular_ephys/R_ANT/device (Device) Depth electrodes
  Group /general/extracellular_ephys/R_CA1 (ElectrodeGroup) electrode group for R_CA1
  Group /general/extracellular_ephys/R_CA1/device (Device) Depth electrodes
  Group /general/extracellular_ephys/R_CA3 (ElectrodeGroup) electrode group for R_CA3
  Group /general/extracellular_ephys/R_CA3/device (Device) Depth electrodes
  Group /general/extracellular_ephys/R_DG (ElectrodeGroup) electrode group for R_DG
  Group /general/extracellular_ephys/R_DG/device (Device) Depth electrodes
  Group /general/extracellular_ephys/R_SUB (ElectrodeGroup) electrode group for R_SUB
  Group /general/extracellular_ephys/R_SUB/device (Device) Depth electrodes
  Group /general/extracellular_ephys/electrodes (DynamicTable) all electrodes
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) AUTOGENERATED description for column `group` | shape = (12,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) AUTOGENERATED description for column `group_name` | shape = (12,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (12,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/label (VectorData) AUTOGENERATED description for column `label` | shape = (12,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) AUTOGENERATED description for column `location` | shape = (12,) | dtype = object
  institution: Zhejiang University
  session_id: RatB6_2023_7_21
  Group /general/subject (Subject) 
  identifier: RatB6_2023_7_21
  session_description: Multi-site LFP activity recorded in temporal lobe epilepsy rats
  session_start_time: ['2023-07-21T00:00:00.000000+08:00']
  timestamps_reference_time: ['2023-07-21T00:00:00.000000+08:00']
