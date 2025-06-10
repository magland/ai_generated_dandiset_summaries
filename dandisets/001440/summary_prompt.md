
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001440/0.250509.1913
name: Bright-Field Images of Rat Nerves at Different Regeneration Stages with Axon and Myelin Segmentations
contributor: [{'name': 'Däschler, Simeon', 'roleName': ['dcite:Author', 'dcite:DataCollector', 'dcite:Researcher', 'dcite:Conceptualization', 'dcite:ProjectMember'], 'schemaKey': 'Person', 'identifier': '0000-0001-8130-7714', 'includeInCitation': True}, {'name': 'Bourget, Marie-Hélène', 'roleName': ['dcite:Author', 'dcite:DataCollector', 'dcite:DataCurator', 'dcite:Researcher', 'dcite:ProjectMember'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Collin, Armand', 'email': 'armand.collin@polymtl.ca', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0009-0005-3258-122X', 'affiliation': [], 'includeInCitation': True}, {'name': 'Derakhshan, Dorsa', 'roleName': ['dcite:DataCollector'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Sharma, Vasudev', 'roleName': ['dcite:DataCurator'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Asenov, Stoyan', 'roleName': ['dcite:DataCurator'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Gordon, Tessa', 'roleName': ['dcite:DataCollector'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Cohen-Adad, Julien', 'email': 'jcohen@polymtl.ca', 'roleName': ['dcite:Author', 'dcite:ContactPerson', 'dcite:DataCurator', 'dcite:DataManager', 'dcite:Maintainer', 'dcite:Supervision'], 'schemaKey': 'Person', 'identifier': '0000-0003-3662-9532', 'includeInCitation': True}, {'name': 'Borschel, Gregory Howard', 'roleName': ['dcite:Author', 'dcite:Conceptualization', 'dcite:DataCollector', 'dcite:FundingAcquisition', 'dcite:Supervision'], 'schemaKey': 'Person', 'identifier': '0000-0001-7691-5264', 'includeInCitation': True}]
description: - Bright-Field Optical Microscopy (BF) dataset for AxonDeepSeg (https://axondeepseg.readthedocs.io/)

- Rat peripheral nerves across different axonal regeneration stages.

- Data collected from adult rats in experimental nerve repair studies.

- 8 samples cropped to ROI used as training data.
    - sub-uoftRat02
    - sub-uoftRat04
    - sub-uoftRat07
    - sub-uoftRat08
    - sub-uoftRat09
    - sub-uoftRat10
    - sub-uoftRat16
    - sub-uoftRat17

- Corresponding axon, myelin, axonmyelin manual segmentation "labels" in derivatives.

- This dataset is a subset of the full dataset used in this publication:

    - https://www.nature.com/articles/s41598-022-10066-6

    - training set for the AxonDeepSeg model developed and validated in the article

assetsSummary: {'species': [], 'approach': [], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Brain Imaging Data Structure (BIDS)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_016124'}], 'numberOfBytes': 144123090, 'numberOfFiles': 48, 'numberOfSamples': 8, 'numberOfSubjects': 8, 'variableMeasured': [], 'measurementTechnique': []}

Dandiset 001440 has 0 NWB files.
