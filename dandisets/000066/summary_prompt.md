
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000066/draft
name: Allen Mouse Common Coordinate Framework - Average Brain Template
contributor: [{'name': 'Ng, Lydia', 'roleName': ['dcite:ProjectLeader', 'dcite:Conceptualization', 'dcite:Author', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0002-7499-3514', 'includeInCitation': True}]
description: The reference space or brain template was constructed as a population average of 1,675 young adult C57BL/6J mice brains imaged using serial two photon tomography (STPT) for the Allen Mouse Brain Connectivity Atlas. The average template was created from tissue autofluorescence detected in the red channel. To maximize input data and create a symmetrical atlas, each dataset was reflected across the midline, for a total of 3,350 (2 x 1,675) hemisphere datasets. Creation of the template followed a two-step iterative process: (1) We deformably registered each specimen to the current iteration of the template and computed an intensity average. (2) We then computed the average deformation field, inverted it, and applied it to the intensity average created in (1). This resulted in a volume with an average unbiased shape and intensity to be used as the template in the next iteration until convergence.

The axes the average template volume is a +X=Posterior, +Y=Inferior(Ventral) and +Z=Right frame with the origin at the corner of the volume.
assetsSummary: {'species': [], 'approach': [], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Brain Imaging Data Structure (BIDS)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_016124'}], 'numberOfBytes': 381654798, 'numberOfFiles': 4, 'variableMeasured': [], 'measurementTechnique': []}

Dandiset 000066 has 0 NWB files.
