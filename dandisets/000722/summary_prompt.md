
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000722/draft
name: sOCT of the Human Somatosensory Cortex and Vessel Segmentation
contributor: [{'name': 'Chollet, Etienne', 'email': 'echollet@mgh.harvard.edu', 'roleName': ['dcite:ContactPerson', 'dcite:Author'], 'schemaKey': 'Person', 'identifier': '0009-0006-4730-525X', 'affiliation': [{'name': 'Massachussets General Hospital', 'schemaKey': 'Affiliation'}], 'includeInCitation': True}, {'name': 'Yaël Balbastre', 'email': 'y.balbastre@ucl.ac.uk', 'schemaKey': 'Person', 'identifier': '0000-0001-8758-9978', 'awardNumber': 'NIF\\R1\\232460', 'includeInCitation': True}, {'name': 'Mauri, Chiara', 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Magnain, Caroline', 'schemaKey': 'Person', 'awardNumber': 'CZI (2019- 198101, 2021-244261)', 'includeInCitation': True}, {'name': 'Fischl, Bruce', 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Wang, Hui', 'schemaKey': 'Person', 'includeInCitation': True}]
description: This dataset contains a 3.4 x 2.9 x 1.1 cm block of Human somatosensory cortex imaged by Serial-sectionning Optical Coherence Tomography (sOCT) at 20 µm isotropic resolution. Vessels in a 6 x 6 x 6 mm region of interest (ROI) were manually labeled and used to validate a machine-learning segmentation method.The output of the automatic segmentation method are also provided, both for the small ROI and large block.

In details, the dataset contains:

- `sub-I46/micr/sub-I46_sample-somatosensory_chunk-01_OCT.ome.zarr` - Image of the full block of tissue
- `sub-I46/micr/sub-I46_sample-somatosensory_chunk-02_OCT.ome.zarr` - Image of the smaller region of interest
- `derivatives/annotations/sub-I46/micr/sub-I46_sample-somatosensory_chunk-01_label-tissue_mask.ome.zarr` - Manually labeled tissue
- `derivatives/annotations/sub-I46/micr/sub-I46_sample-somatosensory_chunk-01_label-vessels_mask.ome.zarr` - Manually labeled vessels
- `derivatives/predictions/sub-I46/micr/sub-I46_sample-somatosensory_chunk-01_label-vessels_mask.ome.zarr` - Vessel maximum-likelihood map (large block)
- `derivatives/predictions/sub-I46/micr/sub-I46_sample-somatosensory_chunk-02_label-vessels_mask.ome.zarr` - Vessel maximum-likelihood map (small block)
- `derivatives/predictions/sub-I46/micr/sub-I46_sample-somatosensory_chunk-01_label-vessels_probseg.ome.zarr` - Vessel probability map (large block)
- `derivatives/predictions/sub-I46/micr/sub-I46_sample-somatosensory_chunk-02_label-vessels_probseg.ome.zarr` - Vessel probability map (small block)
assetsSummary: {'schemaKey': 'AssetsSummary', 'numberOfBytes': 0, 'numberOfFiles': 0}

Dandiset 000722 has 0 NWB files.
