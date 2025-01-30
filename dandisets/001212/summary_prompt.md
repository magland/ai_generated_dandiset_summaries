
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001212/0.241023.0931
name: Individualized Target Selection of Closed-loop Electrical Stimulation for the Treatment of Spontaneous Temporal Lobe Epilepsy.
contributor: [{'name': 'Yufang, Yang', 'email': 'yufang_yangy@163.com', 'roleName': ['dcite:Author', 'dcite:DataCollector', 'dcite:Researcher'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Yuting, Sun', 'roleName': ['dcite:DataCollector', 'dcite:Researcher'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Yanjie, Xing', 'roleName': ['dcite:DataCollector', 'dcite:Researcher'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Haoqi, Ni', 'roleName': ['dcite:DataCollector', 'dcite:Researcher'], 'schemaKey': 'Person', 'identifier': '0000-0002-9059-3860', 'includeInCitation': True}, {'name': 'Chang, Wang', 'roleName': ['dcite:DataCollector', 'dcite:Researcher'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Jianmin, Zhang', 'roleName': ['dcite:Supervision', 'dcite:Validation'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Junming, Zhu', 'roleName': ['dcite:Supervision', 'dcite:Validation'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Kedi, Xu', 'email': 'xukd@zju.edu.cn', 'roleName': ['dcite:ContactPerson', 'dcite:ProjectAdministration', 'dcite:Supervision'], 'schemaKey': 'Person', 'identifier': '0000-0002-9059-3860', 'includeInCitation': True}, {'name': 'STI 2030—Major Projects', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': '2021ZD0200405', 'includeInCitation': False}, {'name': 'National Natural Science Foundation of China ', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': '82272112', 'includeInCitation': False}, {'name': 'Outstanding Youth Program of Zhejiang Natural Science Foundation ', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': 'LR23H180002', 'includeInCitation': False}, {'name': 'Key R&D Program of Zhejiang', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': '2023C03078', 'includeInCitation': False}, {'name': '5510 Project of the second affliated hospital of Zhejiang Univeristy', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': '551001852022', 'includeInCitation': False}, {'name': 'the Starry Night Science Fund of Zhejiang University Shanghai Institute for Advanced Study ', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': 'SN-ZJU-SIAS-002', 'includeInCitation': False}]
description: We provided a comprehensive dataset from a study involving 4-channel long-term brain electrophysiological recordings from 7 pilocarpine-treated rats, each subjected to 4 baseline and 4 stimulation groups. Each group was monitored over a period of 5 to 10 days, with a minimum of 6 spontaneous seizures recorded. The baseline groups captured spontaneous seizures without therapeutic stimulation, while the stimulation groups included spontaneous seizures with therapeutic intervention. Stimulation targets were randomly assigned and not repeated across groups, ensuring independent assessments of treatment effects. The LFP data were saved in MATLAB, adhering to the Neurodata Without Borders (NWB) standard, and are available on the DANDI Archive. This dataset facilitates the evaluation of brain network dynamics and the effects of different stimulation targets on individual responses throughout the study, highlighting the varying effects of stimulation across different individuals.
assetsSummary: {'species': [{'name': 'Rattus norvegicus - Norway rat', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10116'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 3611530887, 'numberOfFiles': 56, 'numberOfSubjects': 7, 'variableMeasured': ['ElectricalSeries', 'ElectrodeGroup'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 001212 has 5 NWB files.
1 of these NWB files are of type 1.
1 of these NWB files are of type 2.
1 of these NWB files are of type 3.
1 of these NWB files are of type 4.
1 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/R1_2023_6_16-ictal1 (ElectricalSeries) Raw acquisition at 00base0 stage
  Dataset /acquisition/R1_2023_6_16-ictal1/electrodes (DynamicTableRegion) all electrodes | shape = (4,) | dtype = int64
  Group /acquisition/R1_2023_6_16-ictal2 (ElectricalSeries) Raw acquisition at 00base0 stage
  Dataset /acquisition/R1_2023_6_16-ictal2/electrodes (DynamicTableRegion) all electrodes | shape = (4,) | dtype = int64
  Group /acquisition/R1_2023_6_18-ictal1 (ElectricalSeries) Raw acquisition at 00base0 stage
  Dataset /acquisition/R1_2023_6_18-ictal1/electrodes (DynamicTableRegion) all electrodes | shape = (4,) | dtype = int64
  Group /acquisition/R1_2023_6_21-ictal1 (ElectricalSeries) Raw acquisition at 00base0 stage
  Dataset /acquisition/R1_2023_6_21-ictal1/electrodes (DynamicTableRegion) all electrodes | shape = (4,) | dtype = int64
  Group /acquisition/R1_2023_6_21-ictal2 (ElectricalSeries) Raw acquisition at 00base0 stage
  Dataset /acquisition/R1_2023_6_21-ictal2/electrodes (DynamicTableRegion) all electrodes | shape = (4,) | dtype = int64
  Group /acquisition/R1_2023_6_22-ictal1 (ElectricalSeries) Raw acquisition at 00base0 stage
  Dataset /acquisition/R1_2023_6_22-ictal1/electrodes (DynamicTableRegion) all electrodes | shape = (4,) | dtype = int64
  Group /acquisition/R1_2023_6_24-ictal1 (ElectricalSeries) Raw acquisition at 00base0 stage
  Dataset /acquisition/R1_2023_6_24-ictal1/electrodes (DynamicTableRegion) all electrodes | shape = (4,) | dtype = int64
  Group /acquisition/R1_2023_6_25-ictal1 (ElectricalSeries) Raw acquisition at 00base0 stage
  Dataset /acquisition/R1_2023_6_25-ictal1/electrodes (DynamicTableRegion) all electrodes | shape = (4,) | dtype = int64
  Group /acquisition/R1_2023_6_29-ictal1 (ElectricalSeries) Raw acquisition at 00base0 stage
  Dataset /acquisition/R1_2023_6_29-ictal1/electrodes (DynamicTableRegion) all electrodes | shape = (4,) | dtype = int64
  file_create_date: ['2024-10-23T15:07:18.303032+08:00']
  Group /general/devices/implant (Device) Depth electrodes
  Group /general/extracellular_ephys/R_ANT (ElectrodeGroup) electrode group for R_ANT
  Group /general/extracellular_ephys/R_ANT/device (Device) Depth electrodes
  Group /general/extracellular_ephys/R_CA1 (ElectrodeGroup) electrode group for R_CA1
  Group /general/extracellular_ephys/R_CA1/device (Device) Depth electrodes
  Group /general/extracellular_ephys/R_CA3 (ElectrodeGroup) electrode group for R_CA3
  Group /general/extracellular_ephys/R_CA3/device (Device) Depth electrodes
  Group /general/extracellular_ephys/R_DG (ElectrodeGroup) electrode group for R_DG
  Group /general/extracellular_ephys/R_DG/device (Device) Depth electrodes
  Group /general/extracellular_ephys/electrodes (DynamicTable) all electrodes
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) AUTOGENERATED description for column `group` | shape = (4,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) AUTOGENERATED description for column `group_name` | shape = (4,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (4,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/label (VectorData) AUTOGENERATED description for column `label` | shape = (4,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) AUTOGENERATED description for column `location` | shape = (4,) | dtype = object
  institution: Zhejiang University
  session_id: RatR1_00base0
  Group /general/subject (Subject) 
  identifier: RatR1_00base0
  session_description: Multi-site LFP activity recorded in temporal lobe epilepsy rats
  session_start_time: ['2023-06-16T00:00:00.000000+08:00']
  timestamps_reference_time: ['2023-06-16T00:00:00.000000+08:00']


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/R1_2023_7_10-ictal1 (ElectricalSeries) Raw acquisition at 01CA1_stim stage
  Dataset /acquisition/R1_2023_7_10-ictal1/electrodes (DynamicTableRegion) all electrodes | shape = (4,) | dtype = int64
  Group /acquisition/R1_2023_7_19-ictal1 (ElectricalSeries) Raw acquisition at 01CA1_stim stage
  Dataset /acquisition/R1_2023_7_19-ictal1/electrodes (DynamicTableRegion) all electrodes | shape = (4,) | dtype = int64
  Group /acquisition/R1_2023_7_19-ictal2 (ElectricalSeries) Raw acquisition at 01CA1_stim stage
  Dataset /acquisition/R1_2023_7_19-ictal2/electrodes (DynamicTableRegion) all electrodes | shape = (4,) | dtype = int64
  Group /acquisition/R1_2023_7_19-ictal3 (ElectricalSeries) Raw acquisition at 01CA1_stim stage
  Dataset /acquisition/R1_2023_7_19-ictal3/electrodes (DynamicTableRegion) all electrodes | shape = (4,) | dtype = int64
  Group /acquisition/R1_2023_7_20-ictal1 (ElectricalSeries) Raw acquisition at 01CA1_stim stage
  Dataset /acquisition/R1_2023_7_20-ictal1/electrodes (DynamicTableRegion) all electrodes | shape = (4,) | dtype = int64
  Group /acquisition/R1_2023_7_20-ictal2 (ElectricalSeries) Raw acquisition at 01CA1_stim stage
  Dataset /acquisition/R1_2023_7_20-ictal2/electrodes (DynamicTableRegion) all electrodes | shape = (4,) | dtype = int64
  Group /acquisition/R1_2023_7_20-ictal3 (ElectricalSeries) Raw acquisition at 01CA1_stim stage
  Dataset /acquisition/R1_2023_7_20-ictal3/electrodes (DynamicTableRegion) all electrodes | shape = (4,) | dtype = int64
  Group /acquisition/R1_2023_7_20-ictal4 (ElectricalSeries) Raw acquisition at 01CA1_stim stage
  Dataset /acquisition/R1_2023_7_20-ictal4/electrodes (DynamicTableRegion) all electrodes | shape = (4,) | dtype = int64
  Group /acquisition/R1_2023_7_20-ictal5 (ElectricalSeries) Raw acquisition at 01CA1_stim stage
  Dataset /acquisition/R1_2023_7_20-ictal5/electrodes (DynamicTableRegion) all electrodes | shape = (4,) | dtype = int64
  Group /acquisition/R1_2023_7_20-ictal6 (ElectricalSeries) Raw acquisition at 01CA1_stim stage
  Dataset /acquisition/R1_2023_7_20-ictal6/electrodes (DynamicTableRegion) all electrodes | shape = (4,) | dtype = int64
  Group /acquisition/R1_2023_7_8-ictal1 (ElectricalSeries) Raw acquisition at 01CA1_stim stage
  Dataset /acquisition/R1_2023_7_8-ictal1/electrodes (DynamicTableRegion) all electrodes | shape = (4,) | dtype = int64
  file_create_date: ['2024-10-23T15:14:04.281234+08:00']
  Group /general/devices/implant (Device) Depth electrodes
  Group /general/extracellular_ephys/R_ANT (ElectrodeGroup) electrode group for R_ANT
  Group /general/extracellular_ephys/R_ANT/device (Device) Depth electrodes
  Group /general/extracellular_ephys/R_CA1 (ElectrodeGroup) electrode group for R_CA1
  Group /general/extracellular_ephys/R_CA1/device (Device) Depth electrodes
  Group /general/extracellular_ephys/R_CA3 (ElectrodeGroup) electrode group for R_CA3
  Group /general/extracellular_ephys/R_CA3/device (Device) Depth electrodes
  Group /general/extracellular_ephys/R_DG (ElectrodeGroup) electrode group for R_DG
  Group /general/extracellular_ephys/R_DG/device (Device) Depth electrodes
  Group /general/extracellular_ephys/electrodes (DynamicTable) all electrodes
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) AUTOGENERATED description for column `group` | shape = (4,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) AUTOGENERATED description for column `group_name` | shape = (4,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (4,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/label (VectorData) AUTOGENERATED description for column `label` | shape = (4,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) AUTOGENERATED description for column `location` | shape = (4,) | dtype = object
  institution: Zhejiang University
  session_id: RatR1_01CA1_stim
  Group /general/subject (Subject) 
  identifier: RatR1_01CA1_stim
  session_description: Multi-site LFP activity recorded in temporal lobe epilepsy rats
  session_start_time: ['2023-07-08T00:00:00.000000+08:00']
  timestamps_reference_time: ['2023-07-08T00:00:00.000000+08:00']


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/R1_2023_7_16-ictal1 (ElectricalSeries) Raw acquisition at 02base1 stage
  Dataset /acquisition/R1_2023_7_16-ictal1/electrodes (DynamicTableRegion) all electrodes | shape = (4,) | dtype = int64
  Group /acquisition/R1_2023_7_21-ictal1 (ElectricalSeries) Raw acquisition at 02base1 stage
  Dataset /acquisition/R1_2023_7_21-ictal1/electrodes (DynamicTableRegion) all electrodes | shape = (4,) | dtype = int64
  Group /acquisition/R1_2023_7_21-ictal2 (ElectricalSeries) Raw acquisition at 02base1 stage
  Dataset /acquisition/R1_2023_7_21-ictal2/electrodes (DynamicTableRegion) all electrodes | shape = (4,) | dtype = int64
  Group /acquisition/R1_2023_7_21-ictal3 (ElectricalSeries) Raw acquisition at 02base1 stage
  Dataset /acquisition/R1_2023_7_21-ictal3/electrodes (DynamicTableRegion) all electrodes | shape = (4,) | dtype = int64
  Group /acquisition/R1_2023_7_21-ictal4 (ElectricalSeries) Raw acquisition at 02base1 stage
  Dataset /acquisition/R1_2023_7_21-ictal4/electrodes (DynamicTableRegion) all electrodes | shape = (4,) | dtype = int64
  Group /acquisition/R1_2023_7_21-ictal5 (ElectricalSeries) Raw acquisition at 02base1 stage
  Dataset /acquisition/R1_2023_7_21-ictal5/electrodes (DynamicTableRegion) all electrodes | shape = (4,) | dtype = int64
  Group /acquisition/R1_2023_7_21-ictal6 (ElectricalSeries) Raw acquisition at 02base1 stage
  Dataset /acquisition/R1_2023_7_21-ictal6/electrodes (DynamicTableRegion) all electrodes | shape = (4,) | dtype = int64
  Group /acquisition/R1_2023_7_21-ictal7 (ElectricalSeries) Raw acquisition at 02base1 stage
  Dataset /acquisition/R1_2023_7_21-ictal7/electrodes (DynamicTableRegion) all electrodes | shape = (4,) | dtype = int64
  Group /acquisition/R1_2023_7_21-ictal8 (ElectricalSeries) Raw acquisition at 02base1 stage
  Dataset /acquisition/R1_2023_7_21-ictal8/electrodes (DynamicTableRegion) all electrodes | shape = (4,) | dtype = int64
  Group /acquisition/R1_2023_7_21-ictal9 (ElectricalSeries) Raw acquisition at 02base1 stage
  Dataset /acquisition/R1_2023_7_21-ictal9/electrodes (DynamicTableRegion) all electrodes | shape = (4,) | dtype = int64
  file_create_date: ['2024-10-23T15:14:38.857664+08:00']
  Group /general/devices/implant (Device) Depth electrodes
  Group /general/extracellular_ephys/R_ANT (ElectrodeGroup) electrode group for R_ANT
  Group /general/extracellular_ephys/R_ANT/device (Device) Depth electrodes
  Group /general/extracellular_ephys/R_CA1 (ElectrodeGroup) electrode group for R_CA1
  Group /general/extracellular_ephys/R_CA1/device (Device) Depth electrodes
  Group /general/extracellular_ephys/R_CA3 (ElectrodeGroup) electrode group for R_CA3
  Group /general/extracellular_ephys/R_CA3/device (Device) Depth electrodes
  Group /general/extracellular_ephys/R_DG (ElectrodeGroup) electrode group for R_DG
  Group /general/extracellular_ephys/R_DG/device (Device) Depth electrodes
  Group /general/extracellular_ephys/electrodes (DynamicTable) all electrodes
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) AUTOGENERATED description for column `group` | shape = (4,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) AUTOGENERATED description for column `group_name` | shape = (4,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (4,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/label (VectorData) AUTOGENERATED description for column `label` | shape = (4,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) AUTOGENERATED description for column `location` | shape = (4,) | dtype = object
  institution: Zhejiang University
  session_id: RatR1_02base1
  Group /general/subject (Subject) 
  identifier: RatR1_02base1
  session_description: Multi-site LFP activity recorded in temporal lobe epilepsy rats
  session_start_time: ['2023-07-16T00:00:00.000000+08:00']
  timestamps_reference_time: ['2023-07-16T00:00:00.000000+08:00']


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/R1_2023_8_16-ictal1-small (ElectricalSeries) Raw acquisition at 03CA3_stim stage
  Dataset /acquisition/R1_2023_8_16-ictal1-small/electrodes (DynamicTableRegion) all electrodes | shape = (4,) | dtype = int64
  Group /acquisition/R1_2023_8_19-ictal1 (ElectricalSeries) Raw acquisition at 03CA3_stim stage
  Dataset /acquisition/R1_2023_8_19-ictal1/electrodes (DynamicTableRegion) all electrodes | shape = (4,) | dtype = int64
  Group /acquisition/R1_2023_8_23-ictal1 (ElectricalSeries) Raw acquisition at 03CA3_stim stage
  Dataset /acquisition/R1_2023_8_23-ictal1/electrodes (DynamicTableRegion) all electrodes | shape = (4,) | dtype = int64
  Group /acquisition/R1_2023_8_24-ictal2 (ElectricalSeries) Raw acquisition at 03CA3_stim stage
  Dataset /acquisition/R1_2023_8_24-ictal2/electrodes (DynamicTableRegion) all electrodes | shape = (4,) | dtype = int64
  Group /acquisition/R1_2023_8_24-ictal3 (ElectricalSeries) Raw acquisition at 03CA3_stim stage
  Dataset /acquisition/R1_2023_8_24-ictal3/electrodes (DynamicTableRegion) all electrodes | shape = (4,) | dtype = int64
  Group /acquisition/R1_2023_8_25-ictal1 (ElectricalSeries) Raw acquisition at 03CA3_stim stage
  Dataset /acquisition/R1_2023_8_25-ictal1/electrodes (DynamicTableRegion) all electrodes | shape = (4,) | dtype = int64
  Group /acquisition/R1_2023_8_27-ictal1 (ElectricalSeries) Raw acquisition at 03CA3_stim stage
  Dataset /acquisition/R1_2023_8_27-ictal1/electrodes (DynamicTableRegion) all electrodes | shape = (4,) | dtype = int64
  file_create_date: ['2024-10-23T15:15:02.661207+08:00']
  Group /general/devices/implant (Device) Depth electrodes
  Group /general/extracellular_ephys/R_ANT (ElectrodeGroup) electrode group for R_ANT
  Group /general/extracellular_ephys/R_ANT/device (Device) Depth electrodes
  Group /general/extracellular_ephys/R_CA1 (ElectrodeGroup) electrode group for R_CA1
  Group /general/extracellular_ephys/R_CA1/device (Device) Depth electrodes
  Group /general/extracellular_ephys/R_CA3 (ElectrodeGroup) electrode group for R_CA3
  Group /general/extracellular_ephys/R_CA3/device (Device) Depth electrodes
  Group /general/extracellular_ephys/R_DG (ElectrodeGroup) electrode group for R_DG
  Group /general/extracellular_ephys/R_DG/device (Device) Depth electrodes
  Group /general/extracellular_ephys/electrodes (DynamicTable) all electrodes
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) AUTOGENERATED description for column `group` | shape = (4,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) AUTOGENERATED description for column `group_name` | shape = (4,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (4,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/label (VectorData) AUTOGENERATED description for column `label` | shape = (4,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) AUTOGENERATED description for column `location` | shape = (4,) | dtype = object
  institution: Zhejiang University
  session_id: RatR1_03CA3_stim
  Group /general/subject (Subject) 
  identifier: RatR1_03CA3_stim
  session_description: Multi-site LFP activity recorded in temporal lobe epilepsy rats
  session_start_time: ['2023-08-16T00:00:00.000000+08:00']
  timestamps_reference_time: ['2023-08-16T00:00:00.000000+08:00']


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  Group /acquisition/R1_2023_8_29-ictal1 (ElectricalSeries) Raw acquisition at 04base2 stage
  Dataset /acquisition/R1_2023_8_29-ictal1/electrodes (DynamicTableRegion) all electrodes | shape = (4,) | dtype = int64
  Group /acquisition/R1_2023_8_30-ictal1 (ElectricalSeries) Raw acquisition at 04base2 stage
  Dataset /acquisition/R1_2023_8_30-ictal1/electrodes (DynamicTableRegion) all electrodes | shape = (4,) | dtype = int64
  Group /acquisition/R1_2023_9_1-ictal1 (ElectricalSeries) Raw acquisition at 04base2 stage
  Dataset /acquisition/R1_2023_9_1-ictal1/electrodes (DynamicTableRegion) all electrodes | shape = (4,) | dtype = int64
  Group /acquisition/R1_2023_9_2-ictal1 (ElectricalSeries) Raw acquisition at 04base2 stage
  Dataset /acquisition/R1_2023_9_2-ictal1/electrodes (DynamicTableRegion) all electrodes | shape = (4,) | dtype = int64
  Group /acquisition/R1_2023_9_5-ictal1 (ElectricalSeries) Raw acquisition at 04base2 stage
  Dataset /acquisition/R1_2023_9_5-ictal1/electrodes (DynamicTableRegion) all electrodes | shape = (4,) | dtype = int64
  file_create_date: ['2024-10-23T15:15:24.470439+08:00']
  Group /general/devices/implant (Device) Depth electrodes
  Group /general/extracellular_ephys/R_ANT (ElectrodeGroup) electrode group for R_ANT
  Group /general/extracellular_ephys/R_ANT/device (Device) Depth electrodes
  Group /general/extracellular_ephys/R_CA1 (ElectrodeGroup) electrode group for R_CA1
  Group /general/extracellular_ephys/R_CA1/device (Device) Depth electrodes
  Group /general/extracellular_ephys/R_CA3 (ElectrodeGroup) electrode group for R_CA3
  Group /general/extracellular_ephys/R_CA3/device (Device) Depth electrodes
  Group /general/extracellular_ephys/R_DG (ElectrodeGroup) electrode group for R_DG
  Group /general/extracellular_ephys/R_DG/device (Device) Depth electrodes
  Group /general/extracellular_ephys/electrodes (DynamicTable) all electrodes
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) AUTOGENERATED description for column `group` | shape = (4,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) AUTOGENERATED description for column `group_name` | shape = (4,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (4,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/label (VectorData) AUTOGENERATED description for column `label` | shape = (4,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) AUTOGENERATED description for column `location` | shape = (4,) | dtype = object
  institution: Zhejiang University
  session_id: RatR1_04base2
  Group /general/subject (Subject) 
  identifier: RatR1_04base2
  session_description: Multi-site LFP activity recorded in temporal lobe epilepsy rats
  session_start_time: ['2023-08-29T00:00:00.000000+08:00']
  timestamps_reference_time: ['2023-08-29T00:00:00.000000+08:00']
