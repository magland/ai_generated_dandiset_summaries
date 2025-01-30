
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001280/0.241218.2300
name: Closed-loop modulation of remote hippocampal representations with neurofeedback
contributor: [{'name': 'Simons Foundation', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': '542981', 'includeInCitation': False}, {'name': 'Howard Hughes Medical Institute', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'includeInCitation': False}, {'name': 'Coulter, Michael', 'email': 'michael.coulter@ucsf.edu', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'Frank, Loren', 'email': 'loren.frank@ucsf.edu', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'includeInCitation': True}, {'name': 'National Institutes of Health', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': 'F32MH123003', 'includeInCitation': False}]
description: Dorsal hippocampus CA1 extracellular recordings from male, Long Evans rats. Rats were engaged in a neurofeedback task during recording. This data was collected as part of the manuscript entitled "Closed-loop modulation of remote hippocampal representations with neurofeedback." Link to manuscript: https://www.biorxiv.org/content/10.1101/2024.05.08.593085v2.
assetsSummary: {'species': [{'name': 'Rattus norvegicus - Norway rat', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10116'}], 'approach': [{'name': 'behavioral approach', 'schemaKey': 'ApproachType'}, {'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 26002918955080, 'numberOfFiles': 120, 'numberOfSubjects': 6, 'variableMeasured': ['Position', 'SpatialSeries', 'ElectricalSeries', 'BehavioralEvents', 'ProcessingModule'], 'measurementTechnique': [{'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 001280 has 5 NWB files.
1 of these NWB files are of type 1.
1 of these NWB files are of type 2.
1 of these NWB files are of type 3.
1 of these NWB files are of type 4.
1 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/e-series (ElectricalSeries) no description
  Dataset /acquisition/e-series/electrodes (DynamicTableRegion) electrodes used in raw e-series recording | shape = (256,) | dtype = int64
  file_create_date: ['2024-01-30T09:56:51.512221-08:00']
  Group /general/devices/camera_device 0 (CameraDevice) 
  Group /general/devices/camera_device 1 (CameraDevice) 
  Group /general/devices/dataacq_device0 (DataAcqDevice) 
  Group /general/devices/header_device (HeaderDevice) 
  Group /general/devices/probe 0 (Probe) 
  Group /general/devices/probe 0/0 (Shank) 
  Group /general/devices/probe 0/0/0 (ShanksElectrode) 
  Group /general/devices/probe 0/0/1 (ShanksElectrode) 
  Group /general/devices/probe 0/0/2 (ShanksElectrode) 
  Group /general/devices/probe 0/0/3 (ShanksElectrode) 
  Group /general/devices/probe 1 (Probe) 
  Group /general/devices/probe 1/0 (Shank) 
  Group /general/devices/probe 1/0/0 (ShanksElectrode) 
  Group /general/devices/probe 1/0/1 (ShanksElectrode) 
  Group /general/devices/probe 1/0/2 (ShanksElectrode) 
  Group /general/devices/probe 1/0/3 (ShanksElectrode) 
  Group /general/devices/probe 10 (Probe) 
  Group /general/devices/probe 10/0 (Shank) 
  Group /general/devices/probe 10/0/0 (ShanksElectrode) 
  Group /general/devices/probe 10/0/1 (ShanksElectrode) 
  Group /general/devices/probe 10/0/2 (ShanksElectrode) 
  Group /general/devices/probe 10/0/3 (ShanksElectrode) 
  Group /general/devices/probe 11 (Probe) 
  Group /general/devices/probe 11/0 (Shank) 
  Group /general/devices/probe 11/0/0 (ShanksElectrode) 
  Group /general/devices/probe 11/0/1 (ShanksElectrode) 
  Group /general/devices/probe 11/0/2 (ShanksElectrode) 
  Group /general/devices/probe 11/0/3 (ShanksElectrode) 
  Group /general/devices/probe 12 (Probe) 
  Group /general/devices/probe 12/0 (Shank) 
  Group /general/devices/probe 12/0/0 (ShanksElectrode) 
  Group /general/devices/probe 12/0/1 (ShanksElectrode) 
  Group /general/devices/probe 12/0/2 (ShanksElectrode) 
  Group /general/devices/probe 12/0/3 (ShanksElectrode) 
  Group /general/devices/probe 13 (Probe) 
  Group /general/devices/probe 13/0 (Shank) 
  Group /general/devices/probe 13/0/0 (ShanksElectrode) 
  Group /general/devices/probe 13/0/1 (ShanksElectrode) 
  Group /general/devices/probe 13/0/2 (ShanksElectrode) 
  Group /general/devices/probe 13/0/3 (ShanksElectrode) 
  Group /general/devices/probe 14 (Probe) 
  Group /general/devices/probe 14/0 (Shank) 
  Group /general/devices/probe 14/0/0 (ShanksElectrode) 
  Group /general/devices/probe 14/0/1 (ShanksElectrode) 
  Group /general/devices/probe 14/0/2 (ShanksElectrode) 
  Group /general/devices/probe 14/0/3 (ShanksElectrode) 
  Group /general/devices/probe 15 (Probe) 
  Group /general/devices/probe 15/0 (Shank) 
  Group /general/devices/probe 15/0/0 (ShanksElectrode) 
  Group /general/devices/probe 15/0/1 (ShanksElectrode) 
  Group /general/devices/probe 15/0/2 (ShanksElectrode) 
  Group /general/devices/probe 15/0/3 (ShanksElectrode) 
  Group /general/devices/probe 16 (Probe) 
  Group /general/devices/probe 16/0 (Shank) 
  Group /general/devices/probe 16/0/0 (ShanksElectrode) 
  Group /general/devices/probe 16/0/1 (ShanksElectrode) 
  Group /general/devices/probe 16/0/2 (ShanksElectrode) 
  Group /general/devices/probe 16/0/3 (ShanksElectrode) 
  Group /general/devices/probe 17 (Probe) 
  Group /general/devices/probe 17/0 (Shank) 
  Group /general/devices/probe 17/0/0 (ShanksElectrode) 
  Group /general/devices/probe 17/0/1 (ShanksElectrode) 
  Group /general/devices/probe 17/0/2 (ShanksElectrode) 
  Group /general/devices/probe 17/0/3 (ShanksElectrode) 
  Group /general/devices/probe 18 (Probe) 
  Group /general/devices/probe 18/0 (Shank) 
  Group /general/devices/probe 18/0/0 (ShanksElectrode) 
  Group /general/devices/probe 18/0/1 (ShanksElectrode) 
  Group /general/devices/probe 18/0/2 (ShanksElectrode) 
  Group /general/devices/probe 18/0/3 (ShanksElectrode) 
  Group /general/devices/probe 19 (Probe) 
  Group /general/devices/probe 19/0 (Shank) 
  Group /general/devices/probe 19/0/0 (ShanksElectrode) 
  Group /general/devices/probe 19/0/1 (ShanksElectrode) 
  Group /general/devices/probe 19/0/2 (ShanksElectrode) 
  Group /general/devices/probe 19/0/3 (ShanksElectrode) 
  Group /general/devices/probe 2 (Probe) 
  Group /general/devices/probe 2/0 (Shank) 
  Group /general/devices/probe 2/0/0 (ShanksElectrode) 
  Group /general/devices/probe 2/0/1 (ShanksElectrode) 
  Group /general/devices/probe 2/0/2 (ShanksElectrode) 
  Group /general/devices/probe 2/0/3 (ShanksElectrode) 
  Group /general/devices/probe 20 (Probe) 
  Group /general/devices/probe 20/0 (Shank) 
  Group /general/devices/probe 20/0/0 (ShanksElectrode) 
  Group /general/devices/probe 20/0/1 (ShanksElectrode) 
  Group /general/devices/probe 20/0/2 (ShanksElectrode) 
  Group /general/devices/probe 20/0/3 (ShanksElectrode) 
  Group /general/devices/probe 21 (Probe) 
  Group /general/devices/probe 21/0 (Shank) 
  Group /general/devices/probe 21/0/0 (ShanksElectrode) 
  Group /general/devices/probe 21/0/1 (ShanksElectrode) 
  Group /general/devices/probe 21/0/2 (ShanksElectrode) 
  Group /general/devices/probe 21/0/3 (ShanksElectrode) 
  Group /general/devices/probe 22 (Probe) 
  Group /general/devices/probe 22/0 (Shank) 
  Group /general/devices/probe 22/0/0 (ShanksElectrode) 
  Group /general/devices/probe 22/0/1 (ShanksElectrode) 
  Group /general/devices/probe 22/0/2 (ShanksElectrode) 
  Group /general/devices/probe 22/0/3 (ShanksElectrode) 
  Group /general/devices/probe 23 (Probe) 
  Group /general/devices/probe 23/0 (Shank) 
  Group /general/devices/probe 23/0/0 (ShanksElectrode) 
  Group /general/devices/probe 23/0/1 (ShanksElectrode) 
  Group /general/devices/probe 23/0/2 (ShanksElectrode) 
  Group /general/devices/probe 23/0/3 (ShanksElectrode) 
  Group /general/devices/probe 24 (Probe) 
  Group /general/devices/probe 24/0 (Shank) 
  Group /general/devices/probe 24/0/0 (ShanksElectrode) 
  Group /general/devices/probe 24/0/1 (ShanksElectrode) 
  Group /general/devices/probe 24/0/2 (ShanksElectrode) 
  Group /general/devices/probe 24/0/3 (ShanksElectrode) 
  Group /general/devices/probe 25 (Probe) 
  Group /general/devices/probe 25/0 (Shank) 
  Group /general/devices/probe 25/0/0 (ShanksElectrode) 
  Group /general/devices/probe 25/0/1 (ShanksElectrode) 
  Group /general/devices/probe 25/0/2 (ShanksElectrode) 
  Group /general/devices/probe 25/0/3 (ShanksElectrode) 
  Group /general/devices/probe 26 (Probe) 
  Group /general/devices/probe 26/0 (Shank) 
  Group /general/devices/probe 26/0/0 (ShanksElectrode) 
  Group /general/devices/probe 26/0/1 (ShanksElectrode) 
  Group /general/devices/probe 26/0/2 (ShanksElectrode) 
  Group /general/devices/probe 26/0/3 (ShanksElectrode) 
  Group /general/devices/probe 27 (Probe) 
  Group /general/devices/probe 27/0 (Shank) 
  Group /general/devices/probe 27/0/0 (ShanksElectrode) 
  Group /general/devices/probe 27/0/1 (ShanksElectrode) 
  Group /general/devices/probe 27/0/2 (ShanksElectrode) 
  Group /general/devices/probe 27/0/3 (ShanksElectrode) 
  Group /general/devices/probe 28 (Probe) 
  Group /general/devices/probe 28/0 (Shank) 
  Group /general/devices/probe 28/0/0 (ShanksElectrode) 
  Group /general/devices/probe 28/0/1 (ShanksElectrode) 
  Group /general/devices/probe 28/0/2 (ShanksElectrode) 
  Group /general/devices/probe 28/0/3 (ShanksElectrode) 
  Group /general/devices/probe 29 (Probe) 
  Group /general/devices/probe 29/0 (Shank) 
  Group /general/devices/probe 29/0/0 (ShanksElectrode) 
  Group /general/devices/probe 29/0/1 (ShanksElectrode) 
  Group /general/devices/probe 29/0/2 (ShanksElectrode) 
  Group /general/devices/probe 29/0/3 (ShanksElectrode) 
  Group /general/devices/probe 3 (Probe) 
  Group /general/devices/probe 3/0 (Shank) 
  Group /general/devices/probe 3/0/0 (ShanksElectrode) 
  Group /general/devices/probe 3/0/1 (ShanksElectrode) 
  Group /general/devices/probe 3/0/2 (ShanksElectrode) 
  Group /general/devices/probe 3/0/3 (ShanksElectrode) 
  Group /general/devices/probe 30 (Probe) 
  Group /general/devices/probe 30/0 (Shank) 
  Group /general/devices/probe 30/0/0 (ShanksElectrode) 
  Group /general/devices/probe 30/0/1 (ShanksElectrode) 
  Group /general/devices/probe 30/0/2 (ShanksElectrode) 
  Group /general/devices/probe 30/0/3 (ShanksElectrode) 
  Group /general/devices/probe 31 (Probe) 
  Group /general/devices/probe 31/0 (Shank) 
  Group /general/devices/probe 31/0/0 (ShanksElectrode) 
  Group /general/devices/probe 31/0/1 (ShanksElectrode) 
  Group /general/devices/probe 31/0/2 (ShanksElectrode) 
  Group /general/devices/probe 31/0/3 (ShanksElectrode) 
  Group /general/devices/probe 32 (Probe) 
  Group /general/devices/probe 32/0 (Shank) 
  Group /general/devices/probe 32/0/0 (ShanksElectrode) 
  Group /general/devices/probe 32/0/1 (ShanksElectrode) 
  Group /general/devices/probe 32/0/2 (ShanksElectrode) 
  Group /general/devices/probe 32/0/3 (ShanksElectrode) 
  Group /general/devices/probe 33 (Probe) 
  Group /general/devices/probe 33/0 (Shank) 
  Group /general/devices/probe 33/0/0 (ShanksElectrode) 
  Group /general/devices/probe 33/0/1 (ShanksElectrode) 
  Group /general/devices/probe 33/0/2 (ShanksElectrode) 
  Group /general/devices/probe 33/0/3 (ShanksElectrode) 
  Group /general/devices/probe 34 (Probe) 
  Group /general/devices/probe 34/0 (Shank) 
  Group /general/devices/probe 34/0/0 (ShanksElectrode) 
  Group /general/devices/probe 34/0/1 (ShanksElectrode) 
  Group /general/devices/probe 34/0/2 (ShanksElectrode) 
  Group /general/devices/probe 34/0/3 (ShanksElectrode) 
  Group /general/devices/probe 35 (Probe) 
  Group /general/devices/probe 35/0 (Shank) 
  Group /general/devices/probe 35/0/0 (ShanksElectrode) 
  Group /general/devices/probe 35/0/1 (ShanksElectrode) 
  Group /general/devices/probe 35/0/2 (ShanksElectrode) 
  Group /general/devices/probe 35/0/3 (ShanksElectrode) 
  Group /general/devices/probe 36 (Probe) 
  Group /general/devices/probe 36/0 (Shank) 
  Group /general/devices/probe 36/0/0 (ShanksElectrode) 
  Group /general/devices/probe 36/0/1 (ShanksElectrode) 
  Group /general/devices/probe 36/0/2 (ShanksElectrode) 
  Group /general/devices/probe 36/0/3 (ShanksElectrode) 
  Group /general/devices/probe 37 (Probe) 
  Group /general/devices/probe 37/0 (Shank) 
  Group /general/devices/probe 37/0/0 (ShanksElectrode) 
  Group /general/devices/probe 37/0/1 (ShanksElectrode) 
  Group /general/devices/probe 37/0/2 (ShanksElectrode) 
  Group /general/devices/probe 37/0/3 (ShanksElectrode) 
  Group /general/devices/probe 38 (Probe) 
  Group /general/devices/probe 38/0 (Shank) 
  Group /general/devices/probe 38/0/0 (ShanksElectrode) 
  Group /general/devices/probe 38/0/1 (ShanksElectrode) 
  Group /general/devices/probe 38/0/2 (ShanksElectrode) 
  Group /general/devices/probe 38/0/3 (ShanksElectrode) 
  Group /general/devices/probe 39 (Probe) 
  Group /general/devices/probe 39/0 (Shank) 
  Group /general/devices/probe 39/0/0 (ShanksElectrode) 
  Group /general/devices/probe 39/0/1 (ShanksElectrode) 
  Group /general/devices/probe 39/0/2 (ShanksElectrode) 
  Group /general/devices/probe 39/0/3 (ShanksElectrode) 
  Group /general/devices/probe 4 (Probe) 
  Group /general/devices/probe 4/0 (Shank) 
  Group /general/devices/probe 4/0/0 (ShanksElectrode) 
  Group /general/devices/probe 4/0/1 (ShanksElectrode) 
  Group /general/devices/probe 4/0/2 (ShanksElectrode) 
  Group /general/devices/probe 4/0/3 (ShanksElectrode) 
  Group /general/devices/probe 40 (Probe) 
  Group /general/devices/probe 40/0 (Shank) 
  Group /general/devices/probe 40/0/0 (ShanksElectrode) 
  Group /general/devices/probe 40/0/1 (ShanksElectrode) 
  Group /general/devices/probe 40/0/2 (ShanksElectrode) 
  Group /general/devices/probe 40/0/3 (ShanksElectrode) 
  Group /general/devices/probe 41 (Probe) 
  Group /general/devices/probe 41/0 (Shank) 
  Group /general/devices/probe 41/0/0 (ShanksElectrode) 
  Group /general/devices/probe 41/0/1 (ShanksElectrode) 
  Group /general/devices/probe 41/0/2 (ShanksElectrode) 
  Group /general/devices/probe 41/0/3 (ShanksElectrode) 
  Group /general/devices/probe 42 (Probe) 
  Group /general/devices/probe 42/0 (Shank) 
  Group /general/devices/probe 42/0/0 (ShanksElectrode) 
  Group /general/devices/probe 42/0/1 (ShanksElectrode) 
  Group /general/devices/probe 42/0/2 (ShanksElectrode) 
  Group /general/devices/probe 42/0/3 (ShanksElectrode) 
  Group /general/devices/probe 43 (Probe) 
  Group /general/devices/probe 43/0 (Shank) 
  Group /general/devices/probe 43/0/0 (ShanksElectrode) 
  Group /general/devices/probe 43/0/1 (ShanksElectrode) 
  Group /general/devices/probe 43/0/2 (ShanksElectrode) 
  Group /general/devices/probe 43/0/3 (ShanksElectrode) 
  Group /general/devices/probe 44 (Probe) 
  Group /general/devices/probe 44/0 (Shank) 
  Group /general/devices/probe 44/0/0 (ShanksElectrode) 
  Group /general/devices/probe 44/0/1 (ShanksElectrode) 
  Group /general/devices/probe 44/0/2 (ShanksElectrode) 
  Group /general/devices/probe 44/0/3 (ShanksElectrode) 
  Group /general/devices/probe 45 (Probe) 
  Group /general/devices/probe 45/0 (Shank) 
  Group /general/devices/probe 45/0/0 (ShanksElectrode) 
  Group /general/devices/probe 45/0/1 (ShanksElectrode) 
  Group /general/devices/probe 45/0/2 (ShanksElectrode) 
  Group /general/devices/probe 45/0/3 (ShanksElectrode) 
  Group /general/devices/probe 46 (Probe) 
  Group /general/devices/probe 46/0 (Shank) 
  Group /general/devices/probe 46/0/0 (ShanksElectrode) 
  Group /general/devices/probe 46/0/1 (ShanksElectrode) 
  Group /general/devices/probe 46/0/2 (ShanksElectrode) 
  Group /general/devices/probe 46/0/3 (ShanksElectrode) 
  Group /general/devices/probe 47 (Probe) 
  Group /general/devices/probe 47/0 (Shank) 
  Group /general/devices/probe 47/0/0 (ShanksElectrode) 
  Group /general/devices/probe 47/0/1 (ShanksElectrode) 
  Group /general/devices/probe 47/0/2 (ShanksElectrode) 
  Group /general/devices/probe 47/0/3 (ShanksElectrode) 
  Group /general/devices/probe 48 (Probe) 
  Group /general/devices/probe 48/0 (Shank) 
  Group /general/devices/probe 48/0/0 (ShanksElectrode) 
  Group /general/devices/probe 48/0/1 (ShanksElectrode) 
  Group /general/devices/probe 48/0/2 (ShanksElectrode) 
  Group /general/devices/probe 48/0/3 (ShanksElectrode) 
  Group /general/devices/probe 49 (Probe) 
  Group /general/devices/probe 49/0 (Shank) 
  Group /general/devices/probe 49/0/0 (ShanksElectrode) 
  Group /general/devices/probe 49/0/1 (ShanksElectrode) 
  Group /general/devices/probe 49/0/2 (ShanksElectrode) 
  Group /general/devices/probe 49/0/3 (ShanksElectrode) 
  Group /general/devices/probe 5 (Probe) 
  Group /general/devices/probe 5/0 (Shank) 
  Group /general/devices/probe 5/0/0 (ShanksElectrode) 
  Group /general/devices/probe 5/0/1 (ShanksElectrode) 
  Group /general/devices/probe 5/0/2 (ShanksElectrode) 
  Group /general/devices/probe 5/0/3 (ShanksElectrode) 
  Group /general/devices/probe 50 (Probe) 
  Group /general/devices/probe 50/0 (Shank) 
  Group /general/devices/probe 50/0/0 (ShanksElectrode) 
  Group /general/devices/probe 50/0/1 (ShanksElectrode) 
  Group /general/devices/probe 50/0/2 (ShanksElectrode) 
  Group /general/devices/probe 50/0/3 (ShanksElectrode) 
  Group /general/devices/probe 51 (Probe) 
  Group /general/devices/probe 51/0 (Shank) 
  Group /general/devices/probe 51/0/0 (ShanksElectrode) 
  Group /general/devices/probe 51/0/1 (ShanksElectrode) 
  Group /general/devices/probe 51/0/2 (ShanksElectrode) 
  Group /general/devices/probe 51/0/3 (ShanksElectrode) 
  Group /general/devices/probe 52 (Probe) 
  Group /general/devices/probe 52/0 (Shank) 
  Group /general/devices/probe 52/0/0 (ShanksElectrode) 
  Group /general/devices/probe 52/0/1 (ShanksElectrode) 
  Group /general/devices/probe 52/0/2 (ShanksElectrode) 
  Group /general/devices/probe 52/0/3 (ShanksElectrode) 
  Group /general/devices/probe 53 (Probe) 
  Group /general/devices/probe 53/0 (Shank) 
  Group /general/devices/probe 53/0/0 (ShanksElectrode) 
  Group /general/devices/probe 53/0/1 (ShanksElectrode) 
  Group /general/devices/probe 53/0/2 (ShanksElectrode) 
  Group /general/devices/probe 53/0/3 (ShanksElectrode) 
  Group /general/devices/probe 54 (Probe) 
  Group /general/devices/probe 54/0 (Shank) 
  Group /general/devices/probe 54/0/0 (ShanksElectrode) 
  Group /general/devices/probe 54/0/1 (ShanksElectrode) 
  Group /general/devices/probe 54/0/2 (ShanksElectrode) 
  Group /general/devices/probe 54/0/3 (ShanksElectrode) 
  Group /general/devices/probe 55 (Probe) 
  Group /general/devices/probe 55/0 (Shank) 
  Group /general/devices/probe 55/0/0 (ShanksElectrode) 
  Group /general/devices/probe 55/0/1 (ShanksElectrode) 
  Group /general/devices/probe 55/0/2 (ShanksElectrode) 
  Group /general/devices/probe 55/0/3 (ShanksElectrode) 
  Group /general/devices/probe 56 (Probe) 
  Group /general/devices/probe 56/0 (Shank) 
  Group /general/devices/probe 56/0/0 (ShanksElectrode) 
  Group /general/devices/probe 56/0/1 (ShanksElectrode) 
  Group /general/devices/probe 56/0/2 (ShanksElectrode) 
  Group /general/devices/probe 56/0/3 (ShanksElectrode) 
  Group /general/devices/probe 57 (Probe) 
  Group /general/devices/probe 57/0 (Shank) 
  Group /general/devices/probe 57/0/0 (ShanksElectrode) 
  Group /general/devices/probe 57/0/1 (ShanksElectrode) 
  Group /general/devices/probe 57/0/2 (ShanksElectrode) 
  Group /general/devices/probe 57/0/3 (ShanksElectrode) 
  Group /general/devices/probe 58 (Probe) 
  Group /general/devices/probe 58/0 (Shank) 
  Group /general/devices/probe 58/0/0 (ShanksElectrode) 
  Group /general/devices/probe 58/0/1 (ShanksElectrode) 
  Group /general/devices/probe 58/0/2 (ShanksElectrode) 
  Group /general/devices/probe 58/0/3 (ShanksElectrode) 
  Group /general/devices/probe 59 (Probe) 
  Group /general/devices/probe 59/0 (Shank) 
  Group /general/devices/probe 59/0/0 (ShanksElectrode) 
  Group /general/devices/probe 59/0/1 (ShanksElectrode) 
  Group /general/devices/probe 59/0/2 (ShanksElectrode) 
  Group /general/devices/probe 59/0/3 (ShanksElectrode) 
  Group /general/devices/probe 6 (Probe) 
  Group /general/devices/probe 6/0 (Shank) 
  Group /general/devices/probe 6/0/0 (ShanksElectrode) 
  Group /general/devices/probe 6/0/1 (ShanksElectrode) 
  Group /general/devices/probe 6/0/2 (ShanksElectrode) 
  Group /general/devices/probe 6/0/3 (ShanksElectrode) 
  Group /general/devices/probe 60 (Probe) 
  Group /general/devices/probe 60/0 (Shank) 
  Group /general/devices/probe 60/0/0 (ShanksElectrode) 
  Group /general/devices/probe 60/0/1 (ShanksElectrode) 
  Group /general/devices/probe 60/0/2 (ShanksElectrode) 
  Group /general/devices/probe 60/0/3 (ShanksElectrode) 
  Group /general/devices/probe 61 (Probe) 
  Group /general/devices/probe 61/0 (Shank) 
  Group /general/devices/probe 61/0/0 (ShanksElectrode) 
  Group /general/devices/probe 61/0/1 (ShanksElectrode) 
  Group /general/devices/probe 61/0/2 (ShanksElectrode) 
  Group /general/devices/probe 61/0/3 (ShanksElectrode) 
  Group /general/devices/probe 62 (Probe) 
  Group /general/devices/probe 62/0 (Shank) 
  Group /general/devices/probe 62/0/0 (ShanksElectrode) 
  Group /general/devices/probe 62/0/1 (ShanksElectrode) 
  Group /general/devices/probe 62/0/2 (ShanksElectrode) 
  Group /general/devices/probe 62/0/3 (ShanksElectrode) 
  Group /general/devices/probe 63 (Probe) 
  Group /general/devices/probe 63/0 (Shank) 
  Group /general/devices/probe 63/0/0 (ShanksElectrode) 
  Group /general/devices/probe 63/0/1 (ShanksElectrode) 
  Group /general/devices/probe 63/0/2 (ShanksElectrode) 
  Group /general/devices/probe 63/0/3 (ShanksElectrode) 
  Group /general/devices/probe 7 (Probe) 
  Group /general/devices/probe 7/0 (Shank) 
  Group /general/devices/probe 7/0/0 (ShanksElectrode) 
  Group /general/devices/probe 7/0/1 (ShanksElectrode) 
  Group /general/devices/probe 7/0/2 (ShanksElectrode) 
  Group /general/devices/probe 7/0/3 (ShanksElectrode) 
  Group /general/devices/probe 8 (Probe) 
  Group /general/devices/probe 8/0 (Shank) 
  Group /general/devices/probe 8/0/0 (ShanksElectrode) 
  Group /general/devices/probe 8/0/1 (ShanksElectrode) 
  Group /general/devices/probe 8/0/2 (ShanksElectrode) 
  Group /general/devices/probe 8/0/3 (ShanksElectrode) 
  Group /general/devices/probe 9 (Probe) 
  Group /general/devices/probe 9/0 (Shank) 
  Group /general/devices/probe 9/0/0 (ShanksElectrode) 
  Group /general/devices/probe 9/0/1 (ShanksElectrode) 
  Group /general/devices/probe 9/0/2 (ShanksElectrode) 
  Group /general/devices/probe 9/0/3 (ShanksElectrode) 
  experiment_description: Hippocampus content feedback
  experimenter: ['Coulter, Michael']
  Group /general/extracellular_ephys/0 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/0/device (Probe) 
  Group /general/extracellular_ephys/0/device/0 (Shank) 
  Group /general/extracellular_ephys/0/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/0/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/0/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/0/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/1 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/1/device (Probe) 
  Group /general/extracellular_ephys/1/device/0 (Shank) 
  Group /general/extracellular_ephys/1/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/1/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/1/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/1/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/10 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/10/device (Probe) 
  Group /general/extracellular_ephys/10/device/0 (Shank) 
  Group /general/extracellular_ephys/10/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/10/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/10/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/10/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/11 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/11/device (Probe) 
  Group /general/extracellular_ephys/11/device/0 (Shank) 
  Group /general/extracellular_ephys/11/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/11/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/11/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/11/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/12 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/12/device (Probe) 
  Group /general/extracellular_ephys/12/device/0 (Shank) 
  Group /general/extracellular_ephys/12/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/12/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/12/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/12/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/13 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/13/device (Probe) 
  Group /general/extracellular_ephys/13/device/0 (Shank) 
  Group /general/extracellular_ephys/13/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/13/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/13/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/13/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/14 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/14/device (Probe) 
  Group /general/extracellular_ephys/14/device/0 (Shank) 
  Group /general/extracellular_ephys/14/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/14/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/14/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/14/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/15 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/15/device (Probe) 
  Group /general/extracellular_ephys/15/device/0 (Shank) 
  Group /general/extracellular_ephys/15/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/15/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/15/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/15/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/16 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/16/device (Probe) 
  Group /general/extracellular_ephys/16/device/0 (Shank) 
  Group /general/extracellular_ephys/16/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/16/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/16/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/16/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/17 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/17/device (Probe) 
  Group /general/extracellular_ephys/17/device/0 (Shank) 
  Group /general/extracellular_ephys/17/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/17/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/17/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/17/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/18 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/18/device (Probe) 
  Group /general/extracellular_ephys/18/device/0 (Shank) 
  Group /general/extracellular_ephys/18/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/18/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/18/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/18/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/19 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/19/device (Probe) 
  Group /general/extracellular_ephys/19/device/0 (Shank) 
  Group /general/extracellular_ephys/19/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/19/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/19/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/19/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/2 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/2/device (Probe) 
  Group /general/extracellular_ephys/2/device/0 (Shank) 
  Group /general/extracellular_ephys/2/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/2/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/2/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/2/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/20 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/20/device (Probe) 
  Group /general/extracellular_ephys/20/device/0 (Shank) 
  Group /general/extracellular_ephys/20/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/20/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/20/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/20/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/21 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/21/device (Probe) 
  Group /general/extracellular_ephys/21/device/0 (Shank) 
  Group /general/extracellular_ephys/21/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/21/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/21/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/21/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/22 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/22/device (Probe) 
  Group /general/extracellular_ephys/22/device/0 (Shank) 
  Group /general/extracellular_ephys/22/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/22/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/22/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/22/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/23 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/23/device (Probe) 
  Group /general/extracellular_ephys/23/device/0 (Shank) 
  Group /general/extracellular_ephys/23/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/23/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/23/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/23/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/24 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/24/device (Probe) 
  Group /general/extracellular_ephys/24/device/0 (Shank) 
  Group /general/extracellular_ephys/24/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/24/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/24/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/24/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/25 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/25/device (Probe) 
  Group /general/extracellular_ephys/25/device/0 (Shank) 
  Group /general/extracellular_ephys/25/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/25/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/25/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/25/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/26 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/26/device (Probe) 
  Group /general/extracellular_ephys/26/device/0 (Shank) 
  Group /general/extracellular_ephys/26/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/26/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/26/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/26/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/27 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/27/device (Probe) 
  Group /general/extracellular_ephys/27/device/0 (Shank) 
  Group /general/extracellular_ephys/27/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/27/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/27/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/27/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/28 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/28/device (Probe) 
  Group /general/extracellular_ephys/28/device/0 (Shank) 
  Group /general/extracellular_ephys/28/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/28/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/28/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/28/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/29 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/29/device (Probe) 
  Group /general/extracellular_ephys/29/device/0 (Shank) 
  Group /general/extracellular_ephys/29/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/29/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/29/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/29/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/3 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/3/device (Probe) 
  Group /general/extracellular_ephys/3/device/0 (Shank) 
  Group /general/extracellular_ephys/3/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/3/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/3/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/3/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/30 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/30/device (Probe) 
  Group /general/extracellular_ephys/30/device/0 (Shank) 
  Group /general/extracellular_ephys/30/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/30/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/30/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/30/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/31 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/31/device (Probe) 
  Group /general/extracellular_ephys/31/device/0 (Shank) 
  Group /general/extracellular_ephys/31/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/31/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/31/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/31/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/32 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/32/device (Probe) 
  Group /general/extracellular_ephys/32/device/0 (Shank) 
  Group /general/extracellular_ephys/32/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/32/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/32/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/32/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/33 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/33/device (Probe) 
  Group /general/extracellular_ephys/33/device/0 (Shank) 
  Group /general/extracellular_ephys/33/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/33/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/33/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/33/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/34 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/34/device (Probe) 
  Group /general/extracellular_ephys/34/device/0 (Shank) 
  Group /general/extracellular_ephys/34/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/34/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/34/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/34/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/35 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/35/device (Probe) 
  Group /general/extracellular_ephys/35/device/0 (Shank) 
  Group /general/extracellular_ephys/35/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/35/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/35/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/35/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/36 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/36/device (Probe) 
  Group /general/extracellular_ephys/36/device/0 (Shank) 
  Group /general/extracellular_ephys/36/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/36/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/36/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/36/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/37 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/37/device (Probe) 
  Group /general/extracellular_ephys/37/device/0 (Shank) 
  Group /general/extracellular_ephys/37/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/37/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/37/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/37/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/38 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/38/device (Probe) 
  Group /general/extracellular_ephys/38/device/0 (Shank) 
  Group /general/extracellular_ephys/38/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/38/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/38/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/38/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/39 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/39/device (Probe) 
  Group /general/extracellular_ephys/39/device/0 (Shank) 
  Group /general/extracellular_ephys/39/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/39/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/39/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/39/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/4 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/4/device (Probe) 
  Group /general/extracellular_ephys/4/device/0 (Shank) 
  Group /general/extracellular_ephys/4/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/4/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/4/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/4/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/40 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/40/device (Probe) 
  Group /general/extracellular_ephys/40/device/0 (Shank) 
  Group /general/extracellular_ephys/40/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/40/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/40/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/40/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/41 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/41/device (Probe) 
  Group /general/extracellular_ephys/41/device/0 (Shank) 
  Group /general/extracellular_ephys/41/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/41/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/41/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/41/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/42 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/42/device (Probe) 
  Group /general/extracellular_ephys/42/device/0 (Shank) 
  Group /general/extracellular_ephys/42/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/42/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/42/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/42/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/43 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/43/device (Probe) 
  Group /general/extracellular_ephys/43/device/0 (Shank) 
  Group /general/extracellular_ephys/43/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/43/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/43/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/43/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/44 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/44/device (Probe) 
  Group /general/extracellular_ephys/44/device/0 (Shank) 
  Group /general/extracellular_ephys/44/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/44/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/44/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/44/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/45 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/45/device (Probe) 
  Group /general/extracellular_ephys/45/device/0 (Shank) 
  Group /general/extracellular_ephys/45/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/45/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/45/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/45/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/46 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/46/device (Probe) 
  Group /general/extracellular_ephys/46/device/0 (Shank) 
  Group /general/extracellular_ephys/46/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/46/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/46/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/46/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/47 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/47/device (Probe) 
  Group /general/extracellular_ephys/47/device/0 (Shank) 
  Group /general/extracellular_ephys/47/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/47/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/47/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/47/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/48 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/48/device (Probe) 
  Group /general/extracellular_ephys/48/device/0 (Shank) 
  Group /general/extracellular_ephys/48/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/48/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/48/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/48/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/49 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/49/device (Probe) 
  Group /general/extracellular_ephys/49/device/0 (Shank) 
  Group /general/extracellular_ephys/49/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/49/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/49/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/49/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/5 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/5/device (Probe) 
  Group /general/extracellular_ephys/5/device/0 (Shank) 
  Group /general/extracellular_ephys/5/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/5/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/5/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/5/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/50 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/50/device (Probe) 
  Group /general/extracellular_ephys/50/device/0 (Shank) 
  Group /general/extracellular_ephys/50/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/50/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/50/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/50/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/51 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/51/device (Probe) 
  Group /general/extracellular_ephys/51/device/0 (Shank) 
  Group /general/extracellular_ephys/51/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/51/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/51/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/51/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/52 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/52/device (Probe) 
  Group /general/extracellular_ephys/52/device/0 (Shank) 
  Group /general/extracellular_ephys/52/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/52/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/52/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/52/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/53 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/53/device (Probe) 
  Group /general/extracellular_ephys/53/device/0 (Shank) 
  Group /general/extracellular_ephys/53/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/53/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/53/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/53/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/54 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/54/device (Probe) 
  Group /general/extracellular_ephys/54/device/0 (Shank) 
  Group /general/extracellular_ephys/54/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/54/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/54/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/54/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/55 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/55/device (Probe) 
  Group /general/extracellular_ephys/55/device/0 (Shank) 
  Group /general/extracellular_ephys/55/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/55/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/55/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/55/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/56 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/56/device (Probe) 
  Group /general/extracellular_ephys/56/device/0 (Shank) 
  Group /general/extracellular_ephys/56/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/56/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/56/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/56/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/57 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/57/device (Probe) 
  Group /general/extracellular_ephys/57/device/0 (Shank) 
  Group /general/extracellular_ephys/57/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/57/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/57/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/57/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/58 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/58/device (Probe) 
  Group /general/extracellular_ephys/58/device/0 (Shank) 
  Group /general/extracellular_ephys/58/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/58/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/58/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/58/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/59 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/59/device (Probe) 
  Group /general/extracellular_ephys/59/device/0 (Shank) 
  Group /general/extracellular_ephys/59/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/59/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/59/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/59/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/6 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/6/device (Probe) 
  Group /general/extracellular_ephys/6/device/0 (Shank) 
  Group /general/extracellular_ephys/6/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/6/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/6/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/6/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/60 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/60/device (Probe) 
  Group /general/extracellular_ephys/60/device/0 (Shank) 
  Group /general/extracellular_ephys/60/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/60/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/60/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/60/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/61 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/61/device (Probe) 
  Group /general/extracellular_ephys/61/device/0 (Shank) 
  Group /general/extracellular_ephys/61/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/61/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/61/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/61/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/62 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/62/device (Probe) 
  Group /general/extracellular_ephys/62/device/0 (Shank) 
  Group /general/extracellular_ephys/62/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/62/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/62/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/62/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/63 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/63/device (Probe) 
  Group /general/extracellular_ephys/63/device/0 (Shank) 
  Group /general/extracellular_ephys/63/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/63/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/63/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/63/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/7 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/7/device (Probe) 
  Group /general/extracellular_ephys/7/device/0 (Shank) 
  Group /general/extracellular_ephys/7/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/7/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/7/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/7/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/8 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/8/device (Probe) 
  Group /general/extracellular_ephys/8/device/0 (Shank) 
  Group /general/extracellular_ephys/8/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/8/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/8/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/8/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/9 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/9/device (Probe) 
  Group /general/extracellular_ephys/9/device/0 (Shank) 
  Group /general/extracellular_ephys/9/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/9/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/9/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/9/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/bad_channel (VectorData) True if noisy or disconnected | shape = (256,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/channel_id (VectorData) Channel number of electrode within the probe | shape = (256,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering, including the filter name and frequency cutoffs | shape = (256,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (256,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (256,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/hwChan (VectorData) SpikeGadgets Hardware channel | shape = (256,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (256,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the electrode, in ohms | shape = (256,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (256,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/ntrode_id (VectorData) Experimenter defined ID for this probe | shape = (256,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/probe_electrode (VectorData) the number of this electrode with respect to the probe | shape = (256,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/probe_shank (VectorData) The shank of the probe this channel is located on | shape = (256,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/ref_elect_id (VectorData) Experimenter selected reference electrode id | shape = (256,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/rel_x (VectorData) the x coordinate within the electrode group | shape = (256,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_y (VectorData) the y coordinate within the electrode group | shape = (256,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_z (VectorData) the z coordinate within the electrode group | shape = (256,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the position (+x is posterior) | shape = (256,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the position (+y is inferior) | shape = (256,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the position (+z is right) | shape = (256,) | dtype = float64
  institution: University of California, San Francisco
  lab: Loren Frank
  session_id: arthur_20220314
  source_script: trodes_to_nwb 0.1.2.dev15+gbe9a4d7.d20231115
  Group /general/subject (Subject) 
  identifier: f23a8a3c-bf98-11ee-919a-ac1f6b0f717e
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (7,) | dtype = int64
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (7,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (7,) | dtype = float64
  Dataset /intervals/epochs/tags (VectorData) user-defined tags | shape = (7,) | dtype = object
  Dataset /intervals/epochs/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (7,) | dtype = uint8
  Group /processing/analog (ProcessingModule) Contains all analog data
  Group /processing/analog/analog (BehavioralEvents) 
  Group /processing/analog/analog/analog (TimeSeries) ECU_Ain1   ECU_Ain2   ECU_Ain3   ECU_Ain4   ECU_Ain5   ECU_Ain6   ECU_Ain7   ECU_Ain8   ECU_Aout1   ECU_Aout2   ECU_Aout3   ECU_Aout4   Headstage_AccelX   Headstage_AccelY   Headstage_AccelZ   Headstage_GyroX   Headstage_GyroY   Headstage_GyroZ   Headstage_MagX   Headstage_MagY   Headstage_MagZ   Controller_Ain1   
  Group /processing/associated_files (ProcessingModule) Contains all associated files data
  Group /processing/associated_files/statescript_r1 (AssociatedFiles) Statescript log run 1
  Group /processing/associated_files/statescript_r2 (AssociatedFiles) Statescript log run 2
  Group /processing/associated_files/statescript_r3 (AssociatedFiles) Statescript log run 3
  Group /processing/behavior (ProcessingModule) Contains all behavior-related data
  Group /processing/behavior/behavioral_events (BehavioralEvents) 
  Group /processing/behavior/behavioral_events/Arm1_light (TimeSeries) Dout13
  Group /processing/behavior/behavioral_events/Arm1_milk_pump (TimeSeries) Dout11
  Group /processing/behavior/behavioral_events/Arm1_poke (TimeSeries) Din13
  Group /processing/behavior/behavioral_events/Arm2_light (TimeSeries) Dout9
  Group /processing/behavior/behavioral_events/Arm2_milk_pump (TimeSeries) Dout12
  Group /processing/behavior/behavioral_events/Arm2_poke (TimeSeries) Din9
  Group /processing/behavior/behavioral_events/BackWell_light (TimeSeries) Dout10
  Group /processing/behavior/behavioral_events/BackWell_milk_pump (TimeSeries) Dout8
  Group /processing/behavior/behavioral_events/BackWell_poke (TimeSeries) Din10
  Group /processing/behavior/behavioral_events/CenterWell_light (TimeSeries) Dout7
  Group /processing/behavior/behavioral_events/CenterWell_milk_pump (TimeSeries) Dout14
  Group /processing/behavior/behavioral_events/CenterWell_poke (TimeSeries) Din7
  Group /processing/behavior/behavioral_events/camera ticks Run (TimeSeries) Din15
  Group /processing/behavior/behavioral_events/camera ticks Sleep (TimeSeries) Din16
  Group /processing/behavior/position (Position) 
  Group /processing/behavior/position/led_0_series_1 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_0_series_2 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_0_series_4 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_0_series_5 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_0_series_6 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_0_series_7 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_1_series_1 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_1_series_2 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_1_series_4 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_1_series_5 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_1_series_6 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_1_series_7 (SpatialSeries) xloc, yloc
  Group /processing/non_repeat_timestamp_labels (ProcessingModule) stores non_repeat_labels for each position timestep
  Group /processing/non_repeat_timestamp_labels/series_1 (TimeSeries) no description
  Group /processing/non_repeat_timestamp_labels/series_2 (TimeSeries) no description
  Group /processing/non_repeat_timestamp_labels/series_4 (TimeSeries) no description
  Group /processing/non_repeat_timestamp_labels/series_5 (TimeSeries) no description
  Group /processing/non_repeat_timestamp_labels/series_6 (TimeSeries) no description
  Group /processing/non_repeat_timestamp_labels/series_7 (TimeSeries) no description
  Group /processing/position_frame_index (ProcessingModule) stores video frame index for each position timestep
  Group /processing/position_frame_index/series_1 (TimeSeries) no description
  Group /processing/position_frame_index/series_2 (TimeSeries) no description
  Group /processing/position_frame_index/series_4 (TimeSeries) no description
  Group /processing/position_frame_index/series_5 (TimeSeries) no description
  Group /processing/position_frame_index/series_6 (TimeSeries) no description
  Group /processing/position_frame_index/series_7 (TimeSeries) no description
  Group /processing/sample_count (ProcessingModule) corespondence between sample count and timestamps
  Group /processing/sample_count/sample_count (TimeSeries) acquisition system sample count
  Group /processing/tasks (ProcessingModule) Contains all tasks information
  Group /processing/tasks/task_0 (DynamicTable) 
  Dataset /processing/tasks/task_0/camera_id (VectorData) the ID number of the camera used for video | shape = (1, 1) | dtype = int64
  Dataset /processing/tasks/task_0/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /processing/tasks/task_0/task_description (VectorData) a description of the task | shape = (1,) | dtype = object
  Dataset /processing/tasks/task_0/task_environment (VectorData) the environment in which the animal performed the task | shape = (1,) | dtype = object
  Dataset /processing/tasks/task_0/task_epochs (VectorData) the temporal epochs where the animal was exposed to this task | shape = (1, 3) | dtype = int64
  Dataset /processing/tasks/task_0/task_name (VectorData) the name of the task | shape = (1,) | dtype = object
  Group /processing/tasks/task_1 (DynamicTable) 
  Dataset /processing/tasks/task_1/camera_id (VectorData) the ID number of the camera used for video | shape = (1, 1) | dtype = int64
  Dataset /processing/tasks/task_1/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /processing/tasks/task_1/task_description (VectorData) a description of the task | shape = (1,) | dtype = object
  Dataset /processing/tasks/task_1/task_environment (VectorData) the environment in which the animal performed the task | shape = (1,) | dtype = object
  Dataset /processing/tasks/task_1/task_epochs (VectorData) the temporal epochs where the animal was exposed to this task | shape = (1, 4) | dtype = int64
  Dataset /processing/tasks/task_1/task_name (VectorData) the name of the task | shape = (1,) | dtype = object
  Group /processing/video_files (ProcessingModule) Contains all associated video files data
  Group /processing/video_files/video (BehavioralEvents) 
  Group /processing/video_files/video/20220314_arthur_01_s1.1.h264 (ImageSeries) video of animal behavior from epoch
  Group /processing/video_files/video/20220314_arthur_01_s1.1.h264/device (CameraDevice) 
  Group /processing/video_files/video/20220314_arthur_02_r1.1.h264 (ImageSeries) video of animal behavior from epoch
  Group /processing/video_files/video/20220314_arthur_02_r1.1.h264/device (CameraDevice) 
  Group /processing/video_files/video/20220314_arthur_03_s2.1.h264 (ImageSeries) video of animal behavior from epoch
  Group /processing/video_files/video/20220314_arthur_03_s2.1.h264/device (CameraDevice) 
  Group /processing/video_files/video/20220314_arthur_04_r2.1.h264 (ImageSeries) video of animal behavior from epoch
  Group /processing/video_files/video/20220314_arthur_04_r2.1.h264/device (CameraDevice) 
  Group /processing/video_files/video/20220314_arthur_05_s3.1.h264 (ImageSeries) video of animal behavior from epoch
  Group /processing/video_files/video/20220314_arthur_05_s3.1.h264/device (CameraDevice) 
  Group /processing/video_files/video/20220314_arthur_06_r3.1.h264 (ImageSeries) video of animal behavior from epoch
  Group /processing/video_files/video/20220314_arthur_06_r3.1.h264/device (CameraDevice) 
  Group /processing/video_files/video/20220314_arthur_07_s3.1.h264 (ImageSeries) video of animal behavior from epoch
  Group /processing/video_files/video/20220314_arthur_07_s3.1.h264/device (CameraDevice) 
  session_description: Hippocampus content feedback
  session_start_time: 2022-03-14T10:19:36.082000-07:00
  timestamps_reference_time: 1970-01-01T00:00:00+00:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/e-series (ElectricalSeries) Recording of extracellular voltage
  Dataset /acquisition/e-series/electrodes (DynamicTableRegion) - | shape = (256,) | dtype = int64
  file_create_date: ['2022-09-11T16:43:24.976932-07:00']
  Group /general/devices/camera_device 0 (CameraDevice) 
  Group /general/devices/camera_device 1 (CameraDevice) 
  Group /general/devices/dataacq_device0 (DataAcqDevice) 
  Group /general/devices/header_device (HeaderDevice) 
  Group /general/devices/probe 0 (Probe) 
  Group /general/devices/probe 0/0 (Shank) 
  Group /general/devices/probe 0/0/0 (ShanksElectrode) 
  Group /general/devices/probe 0/0/1 (ShanksElectrode) 
  Group /general/devices/probe 0/0/2 (ShanksElectrode) 
  Group /general/devices/probe 0/0/3 (ShanksElectrode) 
  experiment_description: Hippocampus content feedback
  experimenter: ['Michael Coulter']
  Group /general/extracellular_ephys/0 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/0/device (Probe) 
  Group /general/extracellular_ephys/0/device/0 (Shank) 
  Group /general/extracellular_ephys/0/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/0/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/0/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/0/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/1 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/1/device (Probe) 
  Group /general/extracellular_ephys/1/device/0 (Shank) 
  Group /general/extracellular_ephys/1/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/1/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/1/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/1/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/10 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/10/device (Probe) 
  Group /general/extracellular_ephys/10/device/0 (Shank) 
  Group /general/extracellular_ephys/10/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/10/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/10/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/10/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/11 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/11/device (Probe) 
  Group /general/extracellular_ephys/11/device/0 (Shank) 
  Group /general/extracellular_ephys/11/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/11/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/11/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/11/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/12 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/12/device (Probe) 
  Group /general/extracellular_ephys/12/device/0 (Shank) 
  Group /general/extracellular_ephys/12/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/12/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/12/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/12/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/13 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/13/device (Probe) 
  Group /general/extracellular_ephys/13/device/0 (Shank) 
  Group /general/extracellular_ephys/13/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/13/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/13/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/13/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/14 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/14/device (Probe) 
  Group /general/extracellular_ephys/14/device/0 (Shank) 
  Group /general/extracellular_ephys/14/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/14/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/14/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/14/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/15 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/15/device (Probe) 
  Group /general/extracellular_ephys/15/device/0 (Shank) 
  Group /general/extracellular_ephys/15/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/15/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/15/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/15/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/16 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/16/device (Probe) 
  Group /general/extracellular_ephys/16/device/0 (Shank) 
  Group /general/extracellular_ephys/16/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/16/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/16/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/16/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/17 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/17/device (Probe) 
  Group /general/extracellular_ephys/17/device/0 (Shank) 
  Group /general/extracellular_ephys/17/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/17/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/17/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/17/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/18 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/18/device (Probe) 
  Group /general/extracellular_ephys/18/device/0 (Shank) 
  Group /general/extracellular_ephys/18/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/18/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/18/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/18/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/19 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/19/device (Probe) 
  Group /general/extracellular_ephys/19/device/0 (Shank) 
  Group /general/extracellular_ephys/19/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/19/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/19/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/19/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/2 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/2/device (Probe) 
  Group /general/extracellular_ephys/2/device/0 (Shank) 
  Group /general/extracellular_ephys/2/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/2/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/2/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/2/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/20 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/20/device (Probe) 
  Group /general/extracellular_ephys/20/device/0 (Shank) 
  Group /general/extracellular_ephys/20/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/20/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/20/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/20/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/21 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/21/device (Probe) 
  Group /general/extracellular_ephys/21/device/0 (Shank) 
  Group /general/extracellular_ephys/21/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/21/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/21/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/21/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/22 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/22/device (Probe) 
  Group /general/extracellular_ephys/22/device/0 (Shank) 
  Group /general/extracellular_ephys/22/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/22/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/22/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/22/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/23 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/23/device (Probe) 
  Group /general/extracellular_ephys/23/device/0 (Shank) 
  Group /general/extracellular_ephys/23/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/23/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/23/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/23/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/24 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/24/device (Probe) 
  Group /general/extracellular_ephys/24/device/0 (Shank) 
  Group /general/extracellular_ephys/24/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/24/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/24/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/24/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/25 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/25/device (Probe) 
  Group /general/extracellular_ephys/25/device/0 (Shank) 
  Group /general/extracellular_ephys/25/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/25/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/25/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/25/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/26 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/26/device (Probe) 
  Group /general/extracellular_ephys/26/device/0 (Shank) 
  Group /general/extracellular_ephys/26/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/26/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/26/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/26/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/27 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/27/device (Probe) 
  Group /general/extracellular_ephys/27/device/0 (Shank) 
  Group /general/extracellular_ephys/27/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/27/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/27/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/27/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/28 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/28/device (Probe) 
  Group /general/extracellular_ephys/28/device/0 (Shank) 
  Group /general/extracellular_ephys/28/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/28/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/28/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/28/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/29 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/29/device (Probe) 
  Group /general/extracellular_ephys/29/device/0 (Shank) 
  Group /general/extracellular_ephys/29/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/29/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/29/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/29/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/3 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/3/device (Probe) 
  Group /general/extracellular_ephys/3/device/0 (Shank) 
  Group /general/extracellular_ephys/3/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/3/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/3/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/3/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/30 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/30/device (Probe) 
  Group /general/extracellular_ephys/30/device/0 (Shank) 
  Group /general/extracellular_ephys/30/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/30/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/30/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/30/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/31 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/31/device (Probe) 
  Group /general/extracellular_ephys/31/device/0 (Shank) 
  Group /general/extracellular_ephys/31/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/31/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/31/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/31/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/32 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/32/device (Probe) 
  Group /general/extracellular_ephys/32/device/0 (Shank) 
  Group /general/extracellular_ephys/32/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/32/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/32/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/32/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/33 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/33/device (Probe) 
  Group /general/extracellular_ephys/33/device/0 (Shank) 
  Group /general/extracellular_ephys/33/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/33/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/33/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/33/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/34 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/34/device (Probe) 
  Group /general/extracellular_ephys/34/device/0 (Shank) 
  Group /general/extracellular_ephys/34/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/34/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/34/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/34/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/35 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/35/device (Probe) 
  Group /general/extracellular_ephys/35/device/0 (Shank) 
  Group /general/extracellular_ephys/35/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/35/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/35/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/35/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/36 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/36/device (Probe) 
  Group /general/extracellular_ephys/36/device/0 (Shank) 
  Group /general/extracellular_ephys/36/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/36/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/36/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/36/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/37 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/37/device (Probe) 
  Group /general/extracellular_ephys/37/device/0 (Shank) 
  Group /general/extracellular_ephys/37/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/37/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/37/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/37/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/38 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/38/device (Probe) 
  Group /general/extracellular_ephys/38/device/0 (Shank) 
  Group /general/extracellular_ephys/38/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/38/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/38/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/38/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/39 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/39/device (Probe) 
  Group /general/extracellular_ephys/39/device/0 (Shank) 
  Group /general/extracellular_ephys/39/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/39/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/39/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/39/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/4 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/4/device (Probe) 
  Group /general/extracellular_ephys/4/device/0 (Shank) 
  Group /general/extracellular_ephys/4/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/4/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/4/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/4/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/40 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/40/device (Probe) 
  Group /general/extracellular_ephys/40/device/0 (Shank) 
  Group /general/extracellular_ephys/40/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/40/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/40/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/40/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/41 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/41/device (Probe) 
  Group /general/extracellular_ephys/41/device/0 (Shank) 
  Group /general/extracellular_ephys/41/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/41/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/41/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/41/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/42 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/42/device (Probe) 
  Group /general/extracellular_ephys/42/device/0 (Shank) 
  Group /general/extracellular_ephys/42/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/42/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/42/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/42/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/43 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/43/device (Probe) 
  Group /general/extracellular_ephys/43/device/0 (Shank) 
  Group /general/extracellular_ephys/43/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/43/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/43/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/43/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/44 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/44/device (Probe) 
  Group /general/extracellular_ephys/44/device/0 (Shank) 
  Group /general/extracellular_ephys/44/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/44/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/44/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/44/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/45 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/45/device (Probe) 
  Group /general/extracellular_ephys/45/device/0 (Shank) 
  Group /general/extracellular_ephys/45/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/45/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/45/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/45/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/46 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/46/device (Probe) 
  Group /general/extracellular_ephys/46/device/0 (Shank) 
  Group /general/extracellular_ephys/46/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/46/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/46/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/46/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/47 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/47/device (Probe) 
  Group /general/extracellular_ephys/47/device/0 (Shank) 
  Group /general/extracellular_ephys/47/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/47/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/47/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/47/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/48 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/48/device (Probe) 
  Group /general/extracellular_ephys/48/device/0 (Shank) 
  Group /general/extracellular_ephys/48/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/48/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/48/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/48/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/49 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/49/device (Probe) 
  Group /general/extracellular_ephys/49/device/0 (Shank) 
  Group /general/extracellular_ephys/49/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/49/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/49/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/49/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/5 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/5/device (Probe) 
  Group /general/extracellular_ephys/5/device/0 (Shank) 
  Group /general/extracellular_ephys/5/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/5/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/5/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/5/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/50 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/50/device (Probe) 
  Group /general/extracellular_ephys/50/device/0 (Shank) 
  Group /general/extracellular_ephys/50/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/50/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/50/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/50/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/51 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/51/device (Probe) 
  Group /general/extracellular_ephys/51/device/0 (Shank) 
  Group /general/extracellular_ephys/51/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/51/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/51/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/51/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/52 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/52/device (Probe) 
  Group /general/extracellular_ephys/52/device/0 (Shank) 
  Group /general/extracellular_ephys/52/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/52/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/52/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/52/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/53 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/53/device (Probe) 
  Group /general/extracellular_ephys/53/device/0 (Shank) 
  Group /general/extracellular_ephys/53/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/53/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/53/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/53/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/54 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/54/device (Probe) 
  Group /general/extracellular_ephys/54/device/0 (Shank) 
  Group /general/extracellular_ephys/54/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/54/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/54/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/54/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/55 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/55/device (Probe) 
  Group /general/extracellular_ephys/55/device/0 (Shank) 
  Group /general/extracellular_ephys/55/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/55/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/55/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/55/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/56 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/56/device (Probe) 
  Group /general/extracellular_ephys/56/device/0 (Shank) 
  Group /general/extracellular_ephys/56/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/56/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/56/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/56/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/57 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/57/device (Probe) 
  Group /general/extracellular_ephys/57/device/0 (Shank) 
  Group /general/extracellular_ephys/57/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/57/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/57/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/57/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/58 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/58/device (Probe) 
  Group /general/extracellular_ephys/58/device/0 (Shank) 
  Group /general/extracellular_ephys/58/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/58/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/58/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/58/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/59 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/59/device (Probe) 
  Group /general/extracellular_ephys/59/device/0 (Shank) 
  Group /general/extracellular_ephys/59/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/59/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/59/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/59/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/6 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/6/device (Probe) 
  Group /general/extracellular_ephys/6/device/0 (Shank) 
  Group /general/extracellular_ephys/6/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/6/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/6/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/6/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/60 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/60/device (Probe) 
  Group /general/extracellular_ephys/60/device/0 (Shank) 
  Group /general/extracellular_ephys/60/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/60/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/60/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/60/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/61 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/61/device (Probe) 
  Group /general/extracellular_ephys/61/device/0 (Shank) 
  Group /general/extracellular_ephys/61/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/61/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/61/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/61/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/62 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/62/device (Probe) 
  Group /general/extracellular_ephys/62/device/0 (Shank) 
  Group /general/extracellular_ephys/62/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/62/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/62/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/62/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/63 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/63/device (Probe) 
  Group /general/extracellular_ephys/63/device/0 (Shank) 
  Group /general/extracellular_ephys/63/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/63/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/63/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/63/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/7 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/7/device (Probe) 
  Group /general/extracellular_ephys/7/device/0 (Shank) 
  Group /general/extracellular_ephys/7/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/7/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/7/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/7/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/8 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/8/device (Probe) 
  Group /general/extracellular_ephys/8/device/0 (Shank) 
  Group /general/extracellular_ephys/8/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/8/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/8/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/8/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/9 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/9/device (Probe) 
  Group /general/extracellular_ephys/9/device/0 (Shank) 
  Group /general/extracellular_ephys/9/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/9/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/9/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/9/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/bad_channel (VectorData) True if noisy or disconnected | shape = (256,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/channel_id (VectorData) None | shape = (256,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (256,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (256,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (256,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/hwChan (VectorData) SpikeGadgets Hardware channel | shape = (256,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (256,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (256,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (256,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/ntrode_id (VectorData) Experimenter defined ID for this probe | shape = (256,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/probe_electrode (VectorData) the number of this electrode with respect to the probe | shape = (256,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/probe_shank (VectorData) The shank of the probe this channel is located on | shape = (256,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/ref_elect_id (VectorData) “Experimenter selected reference electrode id” | shape = (256,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/rel_x (VectorData) None | shape = (256,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_y (VectorData) None | shape = (256,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_z (VectorData) None | shape = (256,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (256,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (256,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (256,) | dtype = float64
  institution: University of California, San Francisco
  lab: Loren Frank
  session_id: arthur_20220315
  Group /general/subject (Subject) 
  identifier: 8716b696-322b-11ed-8093-95633ab0fc90
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (7,) | dtype = int64
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (7,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (7,) | dtype = float64
  Dataset /intervals/epochs/tags (VectorData) user-defined tags | shape = (7,) | dtype = object
  Dataset /intervals/epochs/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (7,) | dtype = uint8
  Group /processing/analog (ProcessingModule) Contains all analog data
  Group /processing/analog/analog (BehavioralEvents) 
  Group /processing/analog/analog/analog (TimeSeries) Headstage_GyroX   Headstage_AccelX   Headstage_AccelY   Headstage_GyroY   Headstage_AccelZ   Headstage_GyroZ   timestamps   
  Group /processing/associated_files (ProcessingModule) Contains all associated files data
  Group /processing/associated_files/statescript_r1 (AssociatedFiles) Statescript log run 1
  Group /processing/associated_files/statescript_r2 (AssociatedFiles) Statescript log run 2
  Group /processing/associated_files/statescript_r3 (AssociatedFiles) Statescript log run 3
  Group /processing/behavior (ProcessingModule) Contains all behavior-related data
  Group /processing/behavior/behavioral_events (BehavioralEvents) 
  Group /processing/behavior/behavioral_events/Arm1_light (TimeSeries) Dout13
  Group /processing/behavior/behavioral_events/Arm1_milk_pump (TimeSeries) Dout11
  Group /processing/behavior/behavioral_events/Arm1_poke (TimeSeries) Din13
  Group /processing/behavior/behavioral_events/Arm2_light (TimeSeries) Dout9
  Group /processing/behavior/behavioral_events/Arm2_milk_pump (TimeSeries) Dout12
  Group /processing/behavior/behavioral_events/Arm2_poke (TimeSeries) Din9
  Group /processing/behavior/behavioral_events/BackWell_light (TimeSeries) Dout10
  Group /processing/behavior/behavioral_events/BackWell_milk_pump (TimeSeries) Dout8
  Group /processing/behavior/behavioral_events/BackWell_poke (TimeSeries) Din10
  Group /processing/behavior/behavioral_events/CamerasyncRun (TimeSeries) Din15
  Group /processing/behavior/behavioral_events/CamerasyncSleep (TimeSeries) Din16
  Group /processing/behavior/behavioral_events/CenterWell_light (TimeSeries) Dout7
  Group /processing/behavior/behavioral_events/CenterWell_milk_pump (TimeSeries) Dout14
  Group /processing/behavior/behavioral_events/CenterWell_poke (TimeSeries) Din7
  Group /processing/behavior/position (Position) 
  Group /processing/behavior/position/led_0_series_0 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_0_series_1 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_0_series_2 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_0_series_3 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_0_series_4 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_0_series_5 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_0_series_6 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_1_series_0 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_1_series_1 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_1_series_2 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_1_series_3 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_1_series_4 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_1_series_5 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_1_series_6 (SpatialSeries) xloc, yloc
  Group /processing/camera_sample_frame_counts (ProcessingModule) Camera Sample Frame Counts
  Group /processing/camera_sample_frame_counts/camera_frame_counts (TimeSeries) hardware frame count
  Group /processing/sample_count (ProcessingModule) corespondence between sample count and timestamps
  Group /processing/sample_count/sample_count (TimeSeries) acquisition system sample count
  Group /processing/tasks (ProcessingModule) Contains all tasks information
  Group /processing/tasks/task_0 (DynamicTable) 
  Dataset /processing/tasks/task_0/camera_id (VectorData) the ID number of the camera used for video | shape = (1, 1) | dtype = int64
  Dataset /processing/tasks/task_0/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /processing/tasks/task_0/task_description (VectorData) a description of the task | shape = (1,) | dtype = object
  Dataset /processing/tasks/task_0/task_environment (VectorData) the environment in which the animal performed the task | shape = (1,) | dtype = object
  Dataset /processing/tasks/task_0/task_epochs (VectorData) the temporal epochs where the animal was exposed to this task | shape = (1, 3) | dtype = int64
  Dataset /processing/tasks/task_0/task_name (VectorData) the name of the task | shape = (1,) | dtype = object
  Group /processing/tasks/task_1 (DynamicTable) 
  Dataset /processing/tasks/task_1/camera_id (VectorData) the ID number of the camera used for video | shape = (1, 1) | dtype = int64
  Dataset /processing/tasks/task_1/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /processing/tasks/task_1/task_description (VectorData) a description of the task | shape = (1,) | dtype = object
  Dataset /processing/tasks/task_1/task_environment (VectorData) the environment in which the animal performed the task | shape = (1,) | dtype = object
  Dataset /processing/tasks/task_1/task_epochs (VectorData) the temporal epochs where the animal was exposed to this task | shape = (1, 4) | dtype = int64
  Dataset /processing/tasks/task_1/task_name (VectorData) the name of the task | shape = (1,) | dtype = object
  Group /processing/video_files (ProcessingModule) Contains all associated video files data
  Group /processing/video_files/video (BehavioralEvents) 
  Group /processing/video_files/video/20220315_arthur_01_s1.1.h264 (ImageSeries) video of animal behavior from epoch
  Group /processing/video_files/video/20220315_arthur_01_s1.1.h264/device (CameraDevice) 
  Group /processing/video_files/video/20220315_arthur_02_r1.1.h264 (ImageSeries) video of animal behavior from epoch
  Group /processing/video_files/video/20220315_arthur_02_r1.1.h264/device (CameraDevice) 
  Group /processing/video_files/video/20220315_arthur_03_s2.1.h264 (ImageSeries) video of animal behavior from epoch
  Group /processing/video_files/video/20220315_arthur_03_s2.1.h264/device (CameraDevice) 
  Group /processing/video_files/video/20220315_arthur_04_r2.1.h264 (ImageSeries) video of animal behavior from epoch
  Group /processing/video_files/video/20220315_arthur_04_r2.1.h264/device (CameraDevice) 
  Group /processing/video_files/video/20220315_arthur_05_s3.1.h264 (ImageSeries) video of animal behavior from epoch
  Group /processing/video_files/video/20220315_arthur_05_s3.1.h264/device (CameraDevice) 
  Group /processing/video_files/video/20220315_arthur_06_r3.1.h264 (ImageSeries) video of animal behavior from epoch
  Group /processing/video_files/video/20220315_arthur_06_r3.1.h264/device (CameraDevice) 
  Group /processing/video_files/video/20220315_arthur_07_s4.1.h264 (ImageSeries) video of animal behavior from epoch
  Group /processing/video_files/video/20220315_arthur_07_s4.1.h264/device (CameraDevice) 
  session_description: Hippocampus content feedback
  session_start_time: 2022-03-15T10:12:08.886000-07:00
  timestamps_reference_time: 1970-01-01T00:00:00+00:00


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/e-series (ElectricalSeries) Recording of extracellular voltage
  Dataset /acquisition/e-series/electrodes (DynamicTableRegion) - | shape = (256,) | dtype = int64
  file_create_date: ['2022-09-11T18:22:35.608335-07:00']
  Group /general/devices/camera_device 0 (CameraDevice) 
  Group /general/devices/camera_device 1 (CameraDevice) 
  Group /general/devices/dataacq_device0 (DataAcqDevice) 
  Group /general/devices/header_device (HeaderDevice) 
  Group /general/devices/probe 0 (Probe) 
  Group /general/devices/probe 0/0 (Shank) 
  Group /general/devices/probe 0/0/0 (ShanksElectrode) 
  Group /general/devices/probe 0/0/1 (ShanksElectrode) 
  Group /general/devices/probe 0/0/2 (ShanksElectrode) 
  Group /general/devices/probe 0/0/3 (ShanksElectrode) 
  experiment_description: Hippocampus content feedback
  experimenter: ['Michael Coulter']
  Group /general/extracellular_ephys/0 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/0/device (Probe) 
  Group /general/extracellular_ephys/0/device/0 (Shank) 
  Group /general/extracellular_ephys/0/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/0/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/0/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/0/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/1 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/1/device (Probe) 
  Group /general/extracellular_ephys/1/device/0 (Shank) 
  Group /general/extracellular_ephys/1/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/1/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/1/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/1/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/10 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/10/device (Probe) 
  Group /general/extracellular_ephys/10/device/0 (Shank) 
  Group /general/extracellular_ephys/10/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/10/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/10/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/10/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/11 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/11/device (Probe) 
  Group /general/extracellular_ephys/11/device/0 (Shank) 
  Group /general/extracellular_ephys/11/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/11/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/11/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/11/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/12 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/12/device (Probe) 
  Group /general/extracellular_ephys/12/device/0 (Shank) 
  Group /general/extracellular_ephys/12/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/12/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/12/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/12/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/13 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/13/device (Probe) 
  Group /general/extracellular_ephys/13/device/0 (Shank) 
  Group /general/extracellular_ephys/13/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/13/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/13/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/13/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/14 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/14/device (Probe) 
  Group /general/extracellular_ephys/14/device/0 (Shank) 
  Group /general/extracellular_ephys/14/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/14/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/14/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/14/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/15 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/15/device (Probe) 
  Group /general/extracellular_ephys/15/device/0 (Shank) 
  Group /general/extracellular_ephys/15/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/15/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/15/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/15/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/16 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/16/device (Probe) 
  Group /general/extracellular_ephys/16/device/0 (Shank) 
  Group /general/extracellular_ephys/16/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/16/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/16/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/16/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/17 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/17/device (Probe) 
  Group /general/extracellular_ephys/17/device/0 (Shank) 
  Group /general/extracellular_ephys/17/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/17/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/17/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/17/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/18 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/18/device (Probe) 
  Group /general/extracellular_ephys/18/device/0 (Shank) 
  Group /general/extracellular_ephys/18/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/18/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/18/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/18/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/19 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/19/device (Probe) 
  Group /general/extracellular_ephys/19/device/0 (Shank) 
  Group /general/extracellular_ephys/19/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/19/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/19/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/19/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/2 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/2/device (Probe) 
  Group /general/extracellular_ephys/2/device/0 (Shank) 
  Group /general/extracellular_ephys/2/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/2/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/2/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/2/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/20 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/20/device (Probe) 
  Group /general/extracellular_ephys/20/device/0 (Shank) 
  Group /general/extracellular_ephys/20/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/20/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/20/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/20/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/21 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/21/device (Probe) 
  Group /general/extracellular_ephys/21/device/0 (Shank) 
  Group /general/extracellular_ephys/21/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/21/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/21/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/21/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/22 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/22/device (Probe) 
  Group /general/extracellular_ephys/22/device/0 (Shank) 
  Group /general/extracellular_ephys/22/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/22/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/22/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/22/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/23 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/23/device (Probe) 
  Group /general/extracellular_ephys/23/device/0 (Shank) 
  Group /general/extracellular_ephys/23/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/23/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/23/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/23/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/24 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/24/device (Probe) 
  Group /general/extracellular_ephys/24/device/0 (Shank) 
  Group /general/extracellular_ephys/24/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/24/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/24/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/24/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/25 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/25/device (Probe) 
  Group /general/extracellular_ephys/25/device/0 (Shank) 
  Group /general/extracellular_ephys/25/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/25/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/25/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/25/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/26 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/26/device (Probe) 
  Group /general/extracellular_ephys/26/device/0 (Shank) 
  Group /general/extracellular_ephys/26/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/26/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/26/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/26/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/27 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/27/device (Probe) 
  Group /general/extracellular_ephys/27/device/0 (Shank) 
  Group /general/extracellular_ephys/27/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/27/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/27/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/27/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/28 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/28/device (Probe) 
  Group /general/extracellular_ephys/28/device/0 (Shank) 
  Group /general/extracellular_ephys/28/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/28/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/28/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/28/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/29 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/29/device (Probe) 
  Group /general/extracellular_ephys/29/device/0 (Shank) 
  Group /general/extracellular_ephys/29/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/29/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/29/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/29/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/3 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/3/device (Probe) 
  Group /general/extracellular_ephys/3/device/0 (Shank) 
  Group /general/extracellular_ephys/3/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/3/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/3/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/3/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/30 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/30/device (Probe) 
  Group /general/extracellular_ephys/30/device/0 (Shank) 
  Group /general/extracellular_ephys/30/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/30/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/30/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/30/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/31 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/31/device (Probe) 
  Group /general/extracellular_ephys/31/device/0 (Shank) 
  Group /general/extracellular_ephys/31/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/31/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/31/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/31/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/32 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/32/device (Probe) 
  Group /general/extracellular_ephys/32/device/0 (Shank) 
  Group /general/extracellular_ephys/32/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/32/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/32/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/32/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/33 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/33/device (Probe) 
  Group /general/extracellular_ephys/33/device/0 (Shank) 
  Group /general/extracellular_ephys/33/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/33/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/33/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/33/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/34 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/34/device (Probe) 
  Group /general/extracellular_ephys/34/device/0 (Shank) 
  Group /general/extracellular_ephys/34/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/34/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/34/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/34/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/35 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/35/device (Probe) 
  Group /general/extracellular_ephys/35/device/0 (Shank) 
  Group /general/extracellular_ephys/35/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/35/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/35/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/35/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/36 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/36/device (Probe) 
  Group /general/extracellular_ephys/36/device/0 (Shank) 
  Group /general/extracellular_ephys/36/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/36/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/36/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/36/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/37 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/37/device (Probe) 
  Group /general/extracellular_ephys/37/device/0 (Shank) 
  Group /general/extracellular_ephys/37/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/37/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/37/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/37/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/38 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/38/device (Probe) 
  Group /general/extracellular_ephys/38/device/0 (Shank) 
  Group /general/extracellular_ephys/38/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/38/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/38/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/38/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/39 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/39/device (Probe) 
  Group /general/extracellular_ephys/39/device/0 (Shank) 
  Group /general/extracellular_ephys/39/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/39/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/39/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/39/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/4 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/4/device (Probe) 
  Group /general/extracellular_ephys/4/device/0 (Shank) 
  Group /general/extracellular_ephys/4/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/4/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/4/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/4/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/40 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/40/device (Probe) 
  Group /general/extracellular_ephys/40/device/0 (Shank) 
  Group /general/extracellular_ephys/40/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/40/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/40/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/40/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/41 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/41/device (Probe) 
  Group /general/extracellular_ephys/41/device/0 (Shank) 
  Group /general/extracellular_ephys/41/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/41/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/41/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/41/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/42 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/42/device (Probe) 
  Group /general/extracellular_ephys/42/device/0 (Shank) 
  Group /general/extracellular_ephys/42/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/42/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/42/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/42/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/43 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/43/device (Probe) 
  Group /general/extracellular_ephys/43/device/0 (Shank) 
  Group /general/extracellular_ephys/43/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/43/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/43/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/43/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/44 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/44/device (Probe) 
  Group /general/extracellular_ephys/44/device/0 (Shank) 
  Group /general/extracellular_ephys/44/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/44/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/44/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/44/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/45 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/45/device (Probe) 
  Group /general/extracellular_ephys/45/device/0 (Shank) 
  Group /general/extracellular_ephys/45/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/45/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/45/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/45/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/46 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/46/device (Probe) 
  Group /general/extracellular_ephys/46/device/0 (Shank) 
  Group /general/extracellular_ephys/46/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/46/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/46/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/46/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/47 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/47/device (Probe) 
  Group /general/extracellular_ephys/47/device/0 (Shank) 
  Group /general/extracellular_ephys/47/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/47/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/47/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/47/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/48 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/48/device (Probe) 
  Group /general/extracellular_ephys/48/device/0 (Shank) 
  Group /general/extracellular_ephys/48/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/48/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/48/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/48/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/49 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/49/device (Probe) 
  Group /general/extracellular_ephys/49/device/0 (Shank) 
  Group /general/extracellular_ephys/49/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/49/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/49/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/49/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/5 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/5/device (Probe) 
  Group /general/extracellular_ephys/5/device/0 (Shank) 
  Group /general/extracellular_ephys/5/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/5/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/5/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/5/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/50 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/50/device (Probe) 
  Group /general/extracellular_ephys/50/device/0 (Shank) 
  Group /general/extracellular_ephys/50/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/50/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/50/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/50/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/51 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/51/device (Probe) 
  Group /general/extracellular_ephys/51/device/0 (Shank) 
  Group /general/extracellular_ephys/51/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/51/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/51/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/51/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/52 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/52/device (Probe) 
  Group /general/extracellular_ephys/52/device/0 (Shank) 
  Group /general/extracellular_ephys/52/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/52/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/52/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/52/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/53 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/53/device (Probe) 
  Group /general/extracellular_ephys/53/device/0 (Shank) 
  Group /general/extracellular_ephys/53/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/53/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/53/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/53/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/54 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/54/device (Probe) 
  Group /general/extracellular_ephys/54/device/0 (Shank) 
  Group /general/extracellular_ephys/54/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/54/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/54/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/54/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/55 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/55/device (Probe) 
  Group /general/extracellular_ephys/55/device/0 (Shank) 
  Group /general/extracellular_ephys/55/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/55/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/55/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/55/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/56 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/56/device (Probe) 
  Group /general/extracellular_ephys/56/device/0 (Shank) 
  Group /general/extracellular_ephys/56/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/56/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/56/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/56/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/57 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/57/device (Probe) 
  Group /general/extracellular_ephys/57/device/0 (Shank) 
  Group /general/extracellular_ephys/57/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/57/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/57/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/57/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/58 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/58/device (Probe) 
  Group /general/extracellular_ephys/58/device/0 (Shank) 
  Group /general/extracellular_ephys/58/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/58/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/58/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/58/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/59 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/59/device (Probe) 
  Group /general/extracellular_ephys/59/device/0 (Shank) 
  Group /general/extracellular_ephys/59/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/59/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/59/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/59/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/6 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/6/device (Probe) 
  Group /general/extracellular_ephys/6/device/0 (Shank) 
  Group /general/extracellular_ephys/6/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/6/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/6/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/6/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/60 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/60/device (Probe) 
  Group /general/extracellular_ephys/60/device/0 (Shank) 
  Group /general/extracellular_ephys/60/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/60/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/60/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/60/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/61 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/61/device (Probe) 
  Group /general/extracellular_ephys/61/device/0 (Shank) 
  Group /general/extracellular_ephys/61/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/61/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/61/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/61/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/62 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/62/device (Probe) 
  Group /general/extracellular_ephys/62/device/0 (Shank) 
  Group /general/extracellular_ephys/62/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/62/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/62/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/62/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/63 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/63/device (Probe) 
  Group /general/extracellular_ephys/63/device/0 (Shank) 
  Group /general/extracellular_ephys/63/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/63/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/63/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/63/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/7 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/7/device (Probe) 
  Group /general/extracellular_ephys/7/device/0 (Shank) 
  Group /general/extracellular_ephys/7/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/7/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/7/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/7/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/8 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/8/device (Probe) 
  Group /general/extracellular_ephys/8/device/0 (Shank) 
  Group /general/extracellular_ephys/8/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/8/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/8/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/8/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/9 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/9/device (Probe) 
  Group /general/extracellular_ephys/9/device/0 (Shank) 
  Group /general/extracellular_ephys/9/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/9/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/9/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/9/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/bad_channel (VectorData) True if noisy or disconnected | shape = (256,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/channel_id (VectorData) None | shape = (256,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (256,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (256,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (256,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/hwChan (VectorData) SpikeGadgets Hardware channel | shape = (256,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (256,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (256,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (256,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/ntrode_id (VectorData) Experimenter defined ID for this probe | shape = (256,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/probe_electrode (VectorData) the number of this electrode with respect to the probe | shape = (256,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/probe_shank (VectorData) The shank of the probe this channel is located on | shape = (256,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/ref_elect_id (VectorData) “Experimenter selected reference electrode id” | shape = (256,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/rel_x (VectorData) None | shape = (256,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_y (VectorData) None | shape = (256,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_z (VectorData) None | shape = (256,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (256,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (256,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (256,) | dtype = float64
  institution: University of California, San Francisco
  lab: Loren Frank
  session_id: arthur_20220316
  Group /general/subject (Subject) 
  identifier: 61f11556-3239-11ed-8093-95633ab0fc90
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (7,) | dtype = int64
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (7,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (7,) | dtype = float64
  Dataset /intervals/epochs/tags (VectorData) user-defined tags | shape = (7,) | dtype = object
  Dataset /intervals/epochs/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (7,) | dtype = uint8
  Group /processing/analog (ProcessingModule) Contains all analog data
  Group /processing/analog/analog (BehavioralEvents) 
  Group /processing/analog/analog/analog (TimeSeries) timestamps   Headstage_AccelX   Headstage_GyroY   Headstage_GyroX   Headstage_AccelY   Headstage_AccelZ   Headstage_GyroZ   
  Group /processing/associated_files (ProcessingModule) Contains all associated files data
  Group /processing/associated_files/statescript_r1 (AssociatedFiles) Statescript log run 1
  Group /processing/associated_files/statescript_r2 (AssociatedFiles) Statescript log run 2
  Group /processing/associated_files/statescript_r3 (AssociatedFiles) Statescript log run 3
  Group /processing/behavior (ProcessingModule) Contains all behavior-related data
  Group /processing/behavior/behavioral_events (BehavioralEvents) 
  Group /processing/behavior/behavioral_events/Arm1_light (TimeSeries) Dout13
  Group /processing/behavior/behavioral_events/Arm1_milk_pump (TimeSeries) Dout11
  Group /processing/behavior/behavioral_events/Arm1_poke (TimeSeries) Din13
  Group /processing/behavior/behavioral_events/Arm2_light (TimeSeries) Dout9
  Group /processing/behavior/behavioral_events/Arm2_milk_pump (TimeSeries) Dout12
  Group /processing/behavior/behavioral_events/Arm2_poke (TimeSeries) Din9
  Group /processing/behavior/behavioral_events/BackWell_light (TimeSeries) Dout10
  Group /processing/behavior/behavioral_events/BackWell_milk_pump (TimeSeries) Dout8
  Group /processing/behavior/behavioral_events/BackWell_poke (TimeSeries) Din10
  Group /processing/behavior/behavioral_events/CamerasyncRun (TimeSeries) Din15
  Group /processing/behavior/behavioral_events/CamerasyncSleep (TimeSeries) Din16
  Group /processing/behavior/behavioral_events/CenterWell_light (TimeSeries) Dout7
  Group /processing/behavior/behavioral_events/CenterWell_milk_pump (TimeSeries) Dout14
  Group /processing/behavior/behavioral_events/CenterWell_poke (TimeSeries) Din7
  Group /processing/behavior/position (Position) 
  Group /processing/behavior/position/led_0_series_0 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_0_series_1 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_0_series_2 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_0_series_3 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_0_series_4 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_0_series_5 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_0_series_6 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_1_series_0 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_1_series_1 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_1_series_2 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_1_series_3 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_1_series_4 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_1_series_5 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_1_series_6 (SpatialSeries) xloc, yloc
  Group /processing/camera_sample_frame_counts (ProcessingModule) Camera Sample Frame Counts
  Group /processing/camera_sample_frame_counts/camera_frame_counts (TimeSeries) hardware frame count
  Group /processing/sample_count (ProcessingModule) corespondence between sample count and timestamps
  Group /processing/sample_count/sample_count (TimeSeries) acquisition system sample count
  Group /processing/tasks (ProcessingModule) Contains all tasks information
  Group /processing/tasks/task_0 (DynamicTable) 
  Dataset /processing/tasks/task_0/camera_id (VectorData) the ID number of the camera used for video | shape = (1, 1) | dtype = int64
  Dataset /processing/tasks/task_0/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /processing/tasks/task_0/task_description (VectorData) a description of the task | shape = (1,) | dtype = object
  Dataset /processing/tasks/task_0/task_environment (VectorData) the environment in which the animal performed the task | shape = (1,) | dtype = object
  Dataset /processing/tasks/task_0/task_epochs (VectorData) the temporal epochs where the animal was exposed to this task | shape = (1, 3) | dtype = int64
  Dataset /processing/tasks/task_0/task_name (VectorData) the name of the task | shape = (1,) | dtype = object
  Group /processing/tasks/task_1 (DynamicTable) 
  Dataset /processing/tasks/task_1/camera_id (VectorData) the ID number of the camera used for video | shape = (1, 1) | dtype = int64
  Dataset /processing/tasks/task_1/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /processing/tasks/task_1/task_description (VectorData) a description of the task | shape = (1,) | dtype = object
  Dataset /processing/tasks/task_1/task_environment (VectorData) the environment in which the animal performed the task | shape = (1,) | dtype = object
  Dataset /processing/tasks/task_1/task_epochs (VectorData) the temporal epochs where the animal was exposed to this task | shape = (1, 4) | dtype = int64
  Dataset /processing/tasks/task_1/task_name (VectorData) the name of the task | shape = (1,) | dtype = object
  Group /processing/video_files (ProcessingModule) Contains all associated video files data
  Group /processing/video_files/video (BehavioralEvents) 
  Group /processing/video_files/video/20220316_arthur_01_s1.1.h264 (ImageSeries) video of animal behavior from epoch
  Group /processing/video_files/video/20220316_arthur_01_s1.1.h264/device (CameraDevice) 
  Group /processing/video_files/video/20220316_arthur_02_r1.1.h264 (ImageSeries) video of animal behavior from epoch
  Group /processing/video_files/video/20220316_arthur_02_r1.1.h264/device (CameraDevice) 
  Group /processing/video_files/video/20220316_arthur_03_s2.1.h264 (ImageSeries) video of animal behavior from epoch
  Group /processing/video_files/video/20220316_arthur_03_s2.1.h264/device (CameraDevice) 
  Group /processing/video_files/video/20220316_arthur_04_r2.1.h264 (ImageSeries) video of animal behavior from epoch
  Group /processing/video_files/video/20220316_arthur_04_r2.1.h264/device (CameraDevice) 
  Group /processing/video_files/video/20220316_arthur_05_s3.1.h264 (ImageSeries) video of animal behavior from epoch
  Group /processing/video_files/video/20220316_arthur_05_s3.1.h264/device (CameraDevice) 
  Group /processing/video_files/video/20220316_arthur_06_r3.1.h264 (ImageSeries) video of animal behavior from epoch
  Group /processing/video_files/video/20220316_arthur_06_r3.1.h264/device (CameraDevice) 
  Group /processing/video_files/video/20220316_arthur_07_s4.1.h264 (ImageSeries) video of animal behavior from epoch
  Group /processing/video_files/video/20220316_arthur_07_s4.1.h264/device (CameraDevice) 
  session_description: Hippocampus content feedback
  session_start_time: 2022-03-16T10:03:05.857000-07:00
  timestamps_reference_time: 1970-01-01T00:00:00+00:00


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/e-series (ElectricalSeries) Recording of extracellular voltage
  Dataset /acquisition/e-series/electrodes (DynamicTableRegion) - | shape = (256,) | dtype = int64
  file_create_date: ['2022-09-11T19:57:09.507320-07:00']
  Group /general/devices/camera_device 0 (CameraDevice) 
  Group /general/devices/camera_device 1 (CameraDevice) 
  Group /general/devices/dataacq_device0 (DataAcqDevice) 
  Group /general/devices/header_device (HeaderDevice) 
  Group /general/devices/probe 0 (Probe) 
  Group /general/devices/probe 0/0 (Shank) 
  Group /general/devices/probe 0/0/0 (ShanksElectrode) 
  Group /general/devices/probe 0/0/1 (ShanksElectrode) 
  Group /general/devices/probe 0/0/2 (ShanksElectrode) 
  Group /general/devices/probe 0/0/3 (ShanksElectrode) 
  experiment_description: Hippocampus content feedback
  experimenter: ['Michael Coulter']
  Group /general/extracellular_ephys/0 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/0/device (Probe) 
  Group /general/extracellular_ephys/0/device/0 (Shank) 
  Group /general/extracellular_ephys/0/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/0/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/0/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/0/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/1 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/1/device (Probe) 
  Group /general/extracellular_ephys/1/device/0 (Shank) 
  Group /general/extracellular_ephys/1/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/1/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/1/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/1/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/10 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/10/device (Probe) 
  Group /general/extracellular_ephys/10/device/0 (Shank) 
  Group /general/extracellular_ephys/10/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/10/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/10/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/10/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/11 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/11/device (Probe) 
  Group /general/extracellular_ephys/11/device/0 (Shank) 
  Group /general/extracellular_ephys/11/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/11/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/11/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/11/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/12 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/12/device (Probe) 
  Group /general/extracellular_ephys/12/device/0 (Shank) 
  Group /general/extracellular_ephys/12/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/12/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/12/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/12/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/13 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/13/device (Probe) 
  Group /general/extracellular_ephys/13/device/0 (Shank) 
  Group /general/extracellular_ephys/13/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/13/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/13/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/13/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/14 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/14/device (Probe) 
  Group /general/extracellular_ephys/14/device/0 (Shank) 
  Group /general/extracellular_ephys/14/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/14/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/14/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/14/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/15 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/15/device (Probe) 
  Group /general/extracellular_ephys/15/device/0 (Shank) 
  Group /general/extracellular_ephys/15/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/15/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/15/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/15/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/16 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/16/device (Probe) 
  Group /general/extracellular_ephys/16/device/0 (Shank) 
  Group /general/extracellular_ephys/16/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/16/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/16/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/16/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/17 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/17/device (Probe) 
  Group /general/extracellular_ephys/17/device/0 (Shank) 
  Group /general/extracellular_ephys/17/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/17/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/17/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/17/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/18 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/18/device (Probe) 
  Group /general/extracellular_ephys/18/device/0 (Shank) 
  Group /general/extracellular_ephys/18/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/18/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/18/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/18/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/19 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/19/device (Probe) 
  Group /general/extracellular_ephys/19/device/0 (Shank) 
  Group /general/extracellular_ephys/19/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/19/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/19/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/19/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/2 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/2/device (Probe) 
  Group /general/extracellular_ephys/2/device/0 (Shank) 
  Group /general/extracellular_ephys/2/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/2/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/2/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/2/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/20 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/20/device (Probe) 
  Group /general/extracellular_ephys/20/device/0 (Shank) 
  Group /general/extracellular_ephys/20/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/20/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/20/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/20/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/21 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/21/device (Probe) 
  Group /general/extracellular_ephys/21/device/0 (Shank) 
  Group /general/extracellular_ephys/21/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/21/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/21/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/21/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/22 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/22/device (Probe) 
  Group /general/extracellular_ephys/22/device/0 (Shank) 
  Group /general/extracellular_ephys/22/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/22/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/22/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/22/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/23 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/23/device (Probe) 
  Group /general/extracellular_ephys/23/device/0 (Shank) 
  Group /general/extracellular_ephys/23/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/23/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/23/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/23/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/24 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/24/device (Probe) 
  Group /general/extracellular_ephys/24/device/0 (Shank) 
  Group /general/extracellular_ephys/24/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/24/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/24/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/24/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/25 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/25/device (Probe) 
  Group /general/extracellular_ephys/25/device/0 (Shank) 
  Group /general/extracellular_ephys/25/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/25/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/25/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/25/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/26 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/26/device (Probe) 
  Group /general/extracellular_ephys/26/device/0 (Shank) 
  Group /general/extracellular_ephys/26/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/26/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/26/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/26/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/27 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/27/device (Probe) 
  Group /general/extracellular_ephys/27/device/0 (Shank) 
  Group /general/extracellular_ephys/27/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/27/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/27/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/27/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/28 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/28/device (Probe) 
  Group /general/extracellular_ephys/28/device/0 (Shank) 
  Group /general/extracellular_ephys/28/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/28/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/28/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/28/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/29 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/29/device (Probe) 
  Group /general/extracellular_ephys/29/device/0 (Shank) 
  Group /general/extracellular_ephys/29/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/29/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/29/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/29/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/3 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/3/device (Probe) 
  Group /general/extracellular_ephys/3/device/0 (Shank) 
  Group /general/extracellular_ephys/3/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/3/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/3/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/3/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/30 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/30/device (Probe) 
  Group /general/extracellular_ephys/30/device/0 (Shank) 
  Group /general/extracellular_ephys/30/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/30/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/30/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/30/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/31 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/31/device (Probe) 
  Group /general/extracellular_ephys/31/device/0 (Shank) 
  Group /general/extracellular_ephys/31/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/31/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/31/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/31/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/32 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/32/device (Probe) 
  Group /general/extracellular_ephys/32/device/0 (Shank) 
  Group /general/extracellular_ephys/32/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/32/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/32/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/32/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/33 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/33/device (Probe) 
  Group /general/extracellular_ephys/33/device/0 (Shank) 
  Group /general/extracellular_ephys/33/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/33/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/33/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/33/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/34 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/34/device (Probe) 
  Group /general/extracellular_ephys/34/device/0 (Shank) 
  Group /general/extracellular_ephys/34/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/34/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/34/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/34/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/35 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/35/device (Probe) 
  Group /general/extracellular_ephys/35/device/0 (Shank) 
  Group /general/extracellular_ephys/35/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/35/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/35/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/35/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/36 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/36/device (Probe) 
  Group /general/extracellular_ephys/36/device/0 (Shank) 
  Group /general/extracellular_ephys/36/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/36/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/36/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/36/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/37 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/37/device (Probe) 
  Group /general/extracellular_ephys/37/device/0 (Shank) 
  Group /general/extracellular_ephys/37/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/37/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/37/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/37/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/38 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/38/device (Probe) 
  Group /general/extracellular_ephys/38/device/0 (Shank) 
  Group /general/extracellular_ephys/38/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/38/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/38/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/38/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/39 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/39/device (Probe) 
  Group /general/extracellular_ephys/39/device/0 (Shank) 
  Group /general/extracellular_ephys/39/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/39/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/39/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/39/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/4 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/4/device (Probe) 
  Group /general/extracellular_ephys/4/device/0 (Shank) 
  Group /general/extracellular_ephys/4/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/4/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/4/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/4/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/40 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/40/device (Probe) 
  Group /general/extracellular_ephys/40/device/0 (Shank) 
  Group /general/extracellular_ephys/40/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/40/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/40/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/40/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/41 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/41/device (Probe) 
  Group /general/extracellular_ephys/41/device/0 (Shank) 
  Group /general/extracellular_ephys/41/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/41/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/41/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/41/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/42 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/42/device (Probe) 
  Group /general/extracellular_ephys/42/device/0 (Shank) 
  Group /general/extracellular_ephys/42/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/42/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/42/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/42/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/43 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/43/device (Probe) 
  Group /general/extracellular_ephys/43/device/0 (Shank) 
  Group /general/extracellular_ephys/43/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/43/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/43/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/43/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/44 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/44/device (Probe) 
  Group /general/extracellular_ephys/44/device/0 (Shank) 
  Group /general/extracellular_ephys/44/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/44/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/44/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/44/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/45 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/45/device (Probe) 
  Group /general/extracellular_ephys/45/device/0 (Shank) 
  Group /general/extracellular_ephys/45/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/45/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/45/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/45/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/46 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/46/device (Probe) 
  Group /general/extracellular_ephys/46/device/0 (Shank) 
  Group /general/extracellular_ephys/46/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/46/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/46/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/46/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/47 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/47/device (Probe) 
  Group /general/extracellular_ephys/47/device/0 (Shank) 
  Group /general/extracellular_ephys/47/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/47/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/47/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/47/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/48 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/48/device (Probe) 
  Group /general/extracellular_ephys/48/device/0 (Shank) 
  Group /general/extracellular_ephys/48/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/48/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/48/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/48/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/49 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/49/device (Probe) 
  Group /general/extracellular_ephys/49/device/0 (Shank) 
  Group /general/extracellular_ephys/49/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/49/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/49/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/49/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/5 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/5/device (Probe) 
  Group /general/extracellular_ephys/5/device/0 (Shank) 
  Group /general/extracellular_ephys/5/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/5/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/5/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/5/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/50 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/50/device (Probe) 
  Group /general/extracellular_ephys/50/device/0 (Shank) 
  Group /general/extracellular_ephys/50/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/50/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/50/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/50/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/51 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/51/device (Probe) 
  Group /general/extracellular_ephys/51/device/0 (Shank) 
  Group /general/extracellular_ephys/51/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/51/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/51/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/51/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/52 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/52/device (Probe) 
  Group /general/extracellular_ephys/52/device/0 (Shank) 
  Group /general/extracellular_ephys/52/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/52/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/52/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/52/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/53 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/53/device (Probe) 
  Group /general/extracellular_ephys/53/device/0 (Shank) 
  Group /general/extracellular_ephys/53/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/53/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/53/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/53/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/54 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/54/device (Probe) 
  Group /general/extracellular_ephys/54/device/0 (Shank) 
  Group /general/extracellular_ephys/54/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/54/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/54/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/54/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/55 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/55/device (Probe) 
  Group /general/extracellular_ephys/55/device/0 (Shank) 
  Group /general/extracellular_ephys/55/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/55/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/55/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/55/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/56 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/56/device (Probe) 
  Group /general/extracellular_ephys/56/device/0 (Shank) 
  Group /general/extracellular_ephys/56/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/56/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/56/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/56/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/57 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/57/device (Probe) 
  Group /general/extracellular_ephys/57/device/0 (Shank) 
  Group /general/extracellular_ephys/57/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/57/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/57/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/57/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/58 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/58/device (Probe) 
  Group /general/extracellular_ephys/58/device/0 (Shank) 
  Group /general/extracellular_ephys/58/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/58/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/58/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/58/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/59 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/59/device (Probe) 
  Group /general/extracellular_ephys/59/device/0 (Shank) 
  Group /general/extracellular_ephys/59/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/59/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/59/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/59/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/6 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/6/device (Probe) 
  Group /general/extracellular_ephys/6/device/0 (Shank) 
  Group /general/extracellular_ephys/6/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/6/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/6/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/6/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/60 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/60/device (Probe) 
  Group /general/extracellular_ephys/60/device/0 (Shank) 
  Group /general/extracellular_ephys/60/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/60/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/60/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/60/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/61 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/61/device (Probe) 
  Group /general/extracellular_ephys/61/device/0 (Shank) 
  Group /general/extracellular_ephys/61/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/61/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/61/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/61/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/62 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/62/device (Probe) 
  Group /general/extracellular_ephys/62/device/0 (Shank) 
  Group /general/extracellular_ephys/62/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/62/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/62/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/62/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/63 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/63/device (Probe) 
  Group /general/extracellular_ephys/63/device/0 (Shank) 
  Group /general/extracellular_ephys/63/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/63/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/63/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/63/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/7 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/7/device (Probe) 
  Group /general/extracellular_ephys/7/device/0 (Shank) 
  Group /general/extracellular_ephys/7/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/7/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/7/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/7/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/8 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/8/device (Probe) 
  Group /general/extracellular_ephys/8/device/0 (Shank) 
  Group /general/extracellular_ephys/8/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/8/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/8/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/8/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/9 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/9/device (Probe) 
  Group /general/extracellular_ephys/9/device/0 (Shank) 
  Group /general/extracellular_ephys/9/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/9/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/9/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/9/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/bad_channel (VectorData) True if noisy or disconnected | shape = (256,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/channel_id (VectorData) None | shape = (256,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (256,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (256,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (256,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/hwChan (VectorData) SpikeGadgets Hardware channel | shape = (256,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (256,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (256,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (256,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/ntrode_id (VectorData) Experimenter defined ID for this probe | shape = (256,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/probe_electrode (VectorData) the number of this electrode with respect to the probe | shape = (256,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/probe_shank (VectorData) The shank of the probe this channel is located on | shape = (256,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/ref_elect_id (VectorData) “Experimenter selected reference electrode id” | shape = (256,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/rel_x (VectorData) None | shape = (256,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_y (VectorData) None | shape = (256,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_z (VectorData) None | shape = (256,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (256,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (256,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (256,) | dtype = float64
  institution: University of California, San Francisco
  lab: Loren Frank
  session_id: arthur_20220317
  Group /general/subject (Subject) 
  identifier: 97d95b8a-3246-11ed-8093-95633ab0fc90
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (7,) | dtype = int64
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (7,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (7,) | dtype = float64
  Dataset /intervals/epochs/tags (VectorData) user-defined tags | shape = (7,) | dtype = object
  Dataset /intervals/epochs/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (7,) | dtype = uint8
  Group /processing/analog (ProcessingModule) Contains all analog data
  Group /processing/analog/analog (BehavioralEvents) 
  Group /processing/analog/analog/analog (TimeSeries) Headstage_GyroZ   Headstage_AccelX   Headstage_AccelY   Headstage_GyroX   Headstage_AccelZ   timestamps   Headstage_GyroY   
  Group /processing/associated_files (ProcessingModule) Contains all associated files data
  Group /processing/associated_files/statescript_r1 (AssociatedFiles) Statescript log run 1
  Group /processing/associated_files/statescript_r2 (AssociatedFiles) Statescript log run 2
  Group /processing/associated_files/statescript_r3 (AssociatedFiles) Statescript log run 3
  Group /processing/behavior (ProcessingModule) Contains all behavior-related data
  Group /processing/behavior/behavioral_events (BehavioralEvents) 
  Group /processing/behavior/behavioral_events/Arm1_light (TimeSeries) Dout13
  Group /processing/behavior/behavioral_events/Arm1_milk_pump (TimeSeries) Dout11
  Group /processing/behavior/behavioral_events/Arm1_poke (TimeSeries) Din13
  Group /processing/behavior/behavioral_events/Arm2_light (TimeSeries) Dout9
  Group /processing/behavior/behavioral_events/Arm2_milk_pump (TimeSeries) Dout12
  Group /processing/behavior/behavioral_events/Arm2_poke (TimeSeries) Din9
  Group /processing/behavior/behavioral_events/BackWell_light (TimeSeries) Dout10
  Group /processing/behavior/behavioral_events/BackWell_milk_pump (TimeSeries) Dout8
  Group /processing/behavior/behavioral_events/BackWell_poke (TimeSeries) Din10
  Group /processing/behavior/behavioral_events/CamerasyncRun (TimeSeries) Din15
  Group /processing/behavior/behavioral_events/CamerasyncSleep (TimeSeries) Din16
  Group /processing/behavior/behavioral_events/CenterWell_light (TimeSeries) Dout7
  Group /processing/behavior/behavioral_events/CenterWell_milk_pump (TimeSeries) Dout14
  Group /processing/behavior/behavioral_events/CenterWell_poke (TimeSeries) Din7
  Group /processing/behavior/position (Position) 
  Group /processing/behavior/position/led_0_series_0 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_0_series_1 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_0_series_2 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_0_series_3 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_0_series_4 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_0_series_5 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_0_series_6 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_1_series_0 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_1_series_1 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_1_series_2 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_1_series_3 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_1_series_4 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_1_series_5 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_1_series_6 (SpatialSeries) xloc, yloc
  Group /processing/camera_sample_frame_counts (ProcessingModule) Camera Sample Frame Counts
  Group /processing/camera_sample_frame_counts/camera_frame_counts (TimeSeries) hardware frame count
  Group /processing/sample_count (ProcessingModule) corespondence between sample count and timestamps
  Group /processing/sample_count/sample_count (TimeSeries) acquisition system sample count
  Group /processing/tasks (ProcessingModule) Contains all tasks information
  Group /processing/tasks/task_0 (DynamicTable) 
  Dataset /processing/tasks/task_0/camera_id (VectorData) the ID number of the camera used for video | shape = (1, 1) | dtype = int64
  Dataset /processing/tasks/task_0/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /processing/tasks/task_0/task_description (VectorData) a description of the task | shape = (1,) | dtype = object
  Dataset /processing/tasks/task_0/task_environment (VectorData) the environment in which the animal performed the task | shape = (1,) | dtype = object
  Dataset /processing/tasks/task_0/task_epochs (VectorData) the temporal epochs where the animal was exposed to this task | shape = (1, 3) | dtype = int64
  Dataset /processing/tasks/task_0/task_name (VectorData) the name of the task | shape = (1,) | dtype = object
  Group /processing/tasks/task_1 (DynamicTable) 
  Dataset /processing/tasks/task_1/camera_id (VectorData) the ID number of the camera used for video | shape = (1, 1) | dtype = int64
  Dataset /processing/tasks/task_1/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /processing/tasks/task_1/task_description (VectorData) a description of the task | shape = (1,) | dtype = object
  Dataset /processing/tasks/task_1/task_environment (VectorData) the environment in which the animal performed the task | shape = (1,) | dtype = object
  Dataset /processing/tasks/task_1/task_epochs (VectorData) the temporal epochs where the animal was exposed to this task | shape = (1, 4) | dtype = int64
  Dataset /processing/tasks/task_1/task_name (VectorData) the name of the task | shape = (1,) | dtype = object
  Group /processing/video_files (ProcessingModule) Contains all associated video files data
  Group /processing/video_files/video (BehavioralEvents) 
  Group /processing/video_files/video/20220317_arthur_01_s1.1.h264 (ImageSeries) video of animal behavior from epoch
  Group /processing/video_files/video/20220317_arthur_01_s1.1.h264/device (CameraDevice) 
  Group /processing/video_files/video/20220317_arthur_02_r1.1.h264 (ImageSeries) video of animal behavior from epoch
  Group /processing/video_files/video/20220317_arthur_02_r1.1.h264/device (CameraDevice) 
  Group /processing/video_files/video/20220317_arthur_03_s2.1.h264 (ImageSeries) video of animal behavior from epoch
  Group /processing/video_files/video/20220317_arthur_03_s2.1.h264/device (CameraDevice) 
  Group /processing/video_files/video/20220317_arthur_04_r2.1.h264 (ImageSeries) video of animal behavior from epoch
  Group /processing/video_files/video/20220317_arthur_04_r2.1.h264/device (CameraDevice) 
  Group /processing/video_files/video/20220317_arthur_05_s3.1.h264 (ImageSeries) video of animal behavior from epoch
  Group /processing/video_files/video/20220317_arthur_05_s3.1.h264/device (CameraDevice) 
  Group /processing/video_files/video/20220317_arthur_06_r3.1.h264 (ImageSeries) video of animal behavior from epoch
  Group /processing/video_files/video/20220317_arthur_06_r3.1.h264/device (CameraDevice) 
  Group /processing/video_files/video/20220317_arthur_07_s4.1.h264 (ImageSeries) video of animal behavior from epoch
  Group /processing/video_files/video/20220317_arthur_07_s4.1.h264/device (CameraDevice) 
  session_description: Hippocampus content feedback
  session_start_time: 2022-03-17T10:18:59.078000-07:00
  timestamps_reference_time: 1970-01-01T00:00:00+00:00


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  Group /acquisition/e-series (ElectricalSeries) Recording of extracellular voltage
  Dataset /acquisition/e-series/electrodes (DynamicTableRegion) - | shape = (256,) | dtype = int64
  file_create_date: ['2022-09-12T00:51:05.010306-07:00']
  Group /general/devices/camera_device 0 (CameraDevice) 
  Group /general/devices/camera_device 1 (CameraDevice) 
  Group /general/devices/dataacq_device0 (DataAcqDevice) 
  Group /general/devices/header_device (HeaderDevice) 
  Group /general/devices/probe 0 (Probe) 
  Group /general/devices/probe 0/0 (Shank) 
  Group /general/devices/probe 0/0/0 (ShanksElectrode) 
  Group /general/devices/probe 0/0/1 (ShanksElectrode) 
  Group /general/devices/probe 0/0/2 (ShanksElectrode) 
  Group /general/devices/probe 0/0/3 (ShanksElectrode) 
  experiment_description: Hippocampus content feedback
  experimenter: ['Michael Coulter']
  Group /general/extracellular_ephys/0 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/0/device (Probe) 
  Group /general/extracellular_ephys/0/device/0 (Shank) 
  Group /general/extracellular_ephys/0/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/0/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/0/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/0/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/1 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/1/device (Probe) 
  Group /general/extracellular_ephys/1/device/0 (Shank) 
  Group /general/extracellular_ephys/1/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/1/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/1/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/1/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/10 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/10/device (Probe) 
  Group /general/extracellular_ephys/10/device/0 (Shank) 
  Group /general/extracellular_ephys/10/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/10/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/10/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/10/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/11 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/11/device (Probe) 
  Group /general/extracellular_ephys/11/device/0 (Shank) 
  Group /general/extracellular_ephys/11/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/11/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/11/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/11/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/12 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/12/device (Probe) 
  Group /general/extracellular_ephys/12/device/0 (Shank) 
  Group /general/extracellular_ephys/12/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/12/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/12/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/12/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/13 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/13/device (Probe) 
  Group /general/extracellular_ephys/13/device/0 (Shank) 
  Group /general/extracellular_ephys/13/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/13/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/13/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/13/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/14 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/14/device (Probe) 
  Group /general/extracellular_ephys/14/device/0 (Shank) 
  Group /general/extracellular_ephys/14/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/14/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/14/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/14/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/15 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/15/device (Probe) 
  Group /general/extracellular_ephys/15/device/0 (Shank) 
  Group /general/extracellular_ephys/15/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/15/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/15/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/15/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/16 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/16/device (Probe) 
  Group /general/extracellular_ephys/16/device/0 (Shank) 
  Group /general/extracellular_ephys/16/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/16/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/16/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/16/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/17 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/17/device (Probe) 
  Group /general/extracellular_ephys/17/device/0 (Shank) 
  Group /general/extracellular_ephys/17/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/17/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/17/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/17/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/18 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/18/device (Probe) 
  Group /general/extracellular_ephys/18/device/0 (Shank) 
  Group /general/extracellular_ephys/18/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/18/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/18/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/18/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/19 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/19/device (Probe) 
  Group /general/extracellular_ephys/19/device/0 (Shank) 
  Group /general/extracellular_ephys/19/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/19/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/19/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/19/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/2 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/2/device (Probe) 
  Group /general/extracellular_ephys/2/device/0 (Shank) 
  Group /general/extracellular_ephys/2/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/2/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/2/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/2/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/20 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/20/device (Probe) 
  Group /general/extracellular_ephys/20/device/0 (Shank) 
  Group /general/extracellular_ephys/20/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/20/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/20/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/20/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/21 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/21/device (Probe) 
  Group /general/extracellular_ephys/21/device/0 (Shank) 
  Group /general/extracellular_ephys/21/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/21/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/21/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/21/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/22 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/22/device (Probe) 
  Group /general/extracellular_ephys/22/device/0 (Shank) 
  Group /general/extracellular_ephys/22/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/22/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/22/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/22/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/23 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/23/device (Probe) 
  Group /general/extracellular_ephys/23/device/0 (Shank) 
  Group /general/extracellular_ephys/23/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/23/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/23/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/23/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/24 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/24/device (Probe) 
  Group /general/extracellular_ephys/24/device/0 (Shank) 
  Group /general/extracellular_ephys/24/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/24/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/24/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/24/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/25 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/25/device (Probe) 
  Group /general/extracellular_ephys/25/device/0 (Shank) 
  Group /general/extracellular_ephys/25/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/25/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/25/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/25/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/26 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/26/device (Probe) 
  Group /general/extracellular_ephys/26/device/0 (Shank) 
  Group /general/extracellular_ephys/26/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/26/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/26/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/26/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/27 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/27/device (Probe) 
  Group /general/extracellular_ephys/27/device/0 (Shank) 
  Group /general/extracellular_ephys/27/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/27/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/27/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/27/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/28 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/28/device (Probe) 
  Group /general/extracellular_ephys/28/device/0 (Shank) 
  Group /general/extracellular_ephys/28/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/28/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/28/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/28/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/29 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/29/device (Probe) 
  Group /general/extracellular_ephys/29/device/0 (Shank) 
  Group /general/extracellular_ephys/29/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/29/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/29/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/29/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/3 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/3/device (Probe) 
  Group /general/extracellular_ephys/3/device/0 (Shank) 
  Group /general/extracellular_ephys/3/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/3/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/3/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/3/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/30 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/30/device (Probe) 
  Group /general/extracellular_ephys/30/device/0 (Shank) 
  Group /general/extracellular_ephys/30/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/30/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/30/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/30/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/31 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/31/device (Probe) 
  Group /general/extracellular_ephys/31/device/0 (Shank) 
  Group /general/extracellular_ephys/31/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/31/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/31/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/31/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/32 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/32/device (Probe) 
  Group /general/extracellular_ephys/32/device/0 (Shank) 
  Group /general/extracellular_ephys/32/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/32/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/32/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/32/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/33 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/33/device (Probe) 
  Group /general/extracellular_ephys/33/device/0 (Shank) 
  Group /general/extracellular_ephys/33/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/33/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/33/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/33/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/34 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/34/device (Probe) 
  Group /general/extracellular_ephys/34/device/0 (Shank) 
  Group /general/extracellular_ephys/34/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/34/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/34/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/34/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/35 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/35/device (Probe) 
  Group /general/extracellular_ephys/35/device/0 (Shank) 
  Group /general/extracellular_ephys/35/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/35/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/35/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/35/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/36 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/36/device (Probe) 
  Group /general/extracellular_ephys/36/device/0 (Shank) 
  Group /general/extracellular_ephys/36/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/36/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/36/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/36/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/37 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/37/device (Probe) 
  Group /general/extracellular_ephys/37/device/0 (Shank) 
  Group /general/extracellular_ephys/37/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/37/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/37/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/37/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/38 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/38/device (Probe) 
  Group /general/extracellular_ephys/38/device/0 (Shank) 
  Group /general/extracellular_ephys/38/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/38/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/38/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/38/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/39 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/39/device (Probe) 
  Group /general/extracellular_ephys/39/device/0 (Shank) 
  Group /general/extracellular_ephys/39/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/39/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/39/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/39/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/4 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/4/device (Probe) 
  Group /general/extracellular_ephys/4/device/0 (Shank) 
  Group /general/extracellular_ephys/4/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/4/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/4/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/4/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/40 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/40/device (Probe) 
  Group /general/extracellular_ephys/40/device/0 (Shank) 
  Group /general/extracellular_ephys/40/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/40/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/40/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/40/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/41 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/41/device (Probe) 
  Group /general/extracellular_ephys/41/device/0 (Shank) 
  Group /general/extracellular_ephys/41/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/41/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/41/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/41/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/42 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/42/device (Probe) 
  Group /general/extracellular_ephys/42/device/0 (Shank) 
  Group /general/extracellular_ephys/42/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/42/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/42/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/42/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/43 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/43/device (Probe) 
  Group /general/extracellular_ephys/43/device/0 (Shank) 
  Group /general/extracellular_ephys/43/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/43/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/43/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/43/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/44 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/44/device (Probe) 
  Group /general/extracellular_ephys/44/device/0 (Shank) 
  Group /general/extracellular_ephys/44/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/44/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/44/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/44/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/45 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/45/device (Probe) 
  Group /general/extracellular_ephys/45/device/0 (Shank) 
  Group /general/extracellular_ephys/45/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/45/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/45/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/45/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/46 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/46/device (Probe) 
  Group /general/extracellular_ephys/46/device/0 (Shank) 
  Group /general/extracellular_ephys/46/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/46/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/46/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/46/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/47 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/47/device (Probe) 
  Group /general/extracellular_ephys/47/device/0 (Shank) 
  Group /general/extracellular_ephys/47/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/47/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/47/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/47/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/48 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/48/device (Probe) 
  Group /general/extracellular_ephys/48/device/0 (Shank) 
  Group /general/extracellular_ephys/48/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/48/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/48/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/48/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/49 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/49/device (Probe) 
  Group /general/extracellular_ephys/49/device/0 (Shank) 
  Group /general/extracellular_ephys/49/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/49/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/49/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/49/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/5 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/5/device (Probe) 
  Group /general/extracellular_ephys/5/device/0 (Shank) 
  Group /general/extracellular_ephys/5/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/5/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/5/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/5/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/50 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/50/device (Probe) 
  Group /general/extracellular_ephys/50/device/0 (Shank) 
  Group /general/extracellular_ephys/50/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/50/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/50/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/50/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/51 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/51/device (Probe) 
  Group /general/extracellular_ephys/51/device/0 (Shank) 
  Group /general/extracellular_ephys/51/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/51/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/51/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/51/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/52 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/52/device (Probe) 
  Group /general/extracellular_ephys/52/device/0 (Shank) 
  Group /general/extracellular_ephys/52/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/52/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/52/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/52/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/53 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/53/device (Probe) 
  Group /general/extracellular_ephys/53/device/0 (Shank) 
  Group /general/extracellular_ephys/53/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/53/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/53/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/53/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/54 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/54/device (Probe) 
  Group /general/extracellular_ephys/54/device/0 (Shank) 
  Group /general/extracellular_ephys/54/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/54/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/54/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/54/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/55 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/55/device (Probe) 
  Group /general/extracellular_ephys/55/device/0 (Shank) 
  Group /general/extracellular_ephys/55/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/55/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/55/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/55/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/56 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/56/device (Probe) 
  Group /general/extracellular_ephys/56/device/0 (Shank) 
  Group /general/extracellular_ephys/56/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/56/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/56/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/56/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/57 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/57/device (Probe) 
  Group /general/extracellular_ephys/57/device/0 (Shank) 
  Group /general/extracellular_ephys/57/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/57/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/57/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/57/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/58 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/58/device (Probe) 
  Group /general/extracellular_ephys/58/device/0 (Shank) 
  Group /general/extracellular_ephys/58/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/58/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/58/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/58/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/59 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/59/device (Probe) 
  Group /general/extracellular_ephys/59/device/0 (Shank) 
  Group /general/extracellular_ephys/59/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/59/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/59/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/59/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/6 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/6/device (Probe) 
  Group /general/extracellular_ephys/6/device/0 (Shank) 
  Group /general/extracellular_ephys/6/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/6/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/6/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/6/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/60 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/60/device (Probe) 
  Group /general/extracellular_ephys/60/device/0 (Shank) 
  Group /general/extracellular_ephys/60/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/60/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/60/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/60/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/61 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/61/device (Probe) 
  Group /general/extracellular_ephys/61/device/0 (Shank) 
  Group /general/extracellular_ephys/61/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/61/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/61/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/61/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/62 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/62/device (Probe) 
  Group /general/extracellular_ephys/62/device/0 (Shank) 
  Group /general/extracellular_ephys/62/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/62/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/62/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/62/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/63 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/63/device (Probe) 
  Group /general/extracellular_ephys/63/device/0 (Shank) 
  Group /general/extracellular_ephys/63/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/63/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/63/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/63/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/7 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/7/device (Probe) 
  Group /general/extracellular_ephys/7/device/0 (Shank) 
  Group /general/extracellular_ephys/7/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/7/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/7/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/7/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/8 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/8/device (Probe) 
  Group /general/extracellular_ephys/8/device/0 (Shank) 
  Group /general/extracellular_ephys/8/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/8/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/8/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/8/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/9 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/9/device (Probe) 
  Group /general/extracellular_ephys/9/device/0 (Shank) 
  Group /general/extracellular_ephys/9/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/9/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/9/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/9/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/electrodes (DynamicTable) metadata about extracellular electrodes
  Dataset /general/extracellular_ephys/electrodes/bad_channel (VectorData) True if noisy or disconnected | shape = (256,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/channel_id (VectorData) None | shape = (256,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (256,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (256,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (256,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/hwChan (VectorData) SpikeGadgets Hardware channel | shape = (256,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (256,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (256,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (256,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/ntrode_id (VectorData) Experimenter defined ID for this probe | shape = (256,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/probe_electrode (VectorData) the number of this electrode with respect to the probe | shape = (256,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/probe_shank (VectorData) The shank of the probe this channel is located on | shape = (256,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/ref_elect_id (VectorData) “Experimenter selected reference electrode id” | shape = (256,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/rel_x (VectorData) None | shape = (256,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_y (VectorData) None | shape = (256,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_z (VectorData) None | shape = (256,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (256,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (256,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (256,) | dtype = float64
  institution: University of California, San Francisco
  lab: Loren Frank
  session_id: arthur_20220318
  Group /general/subject (Subject) 
  identifier: a76d8ed0-326f-11ed-8093-95633ab0fc90
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (7,) | dtype = int64
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (7,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (7,) | dtype = float64
  Dataset /intervals/epochs/tags (VectorData) user-defined tags | shape = (7,) | dtype = object
  Dataset /intervals/epochs/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (7,) | dtype = uint8
  Group /processing/analog (ProcessingModule) Contains all analog data
  Group /processing/analog/analog (BehavioralEvents) 
  Group /processing/analog/analog/analog (TimeSeries) Headstage_AccelY   Headstage_GyroZ   Headstage_AccelX   Headstage_GyroY   timestamps   Headstage_AccelZ   Headstage_GyroX   
  Group /processing/associated_files (ProcessingModule) Contains all associated files data
  Group /processing/associated_files/statescript_r1 (AssociatedFiles) Statescript log run 1
  Group /processing/associated_files/statescript_r2 (AssociatedFiles) Statescript log run 2
  Group /processing/associated_files/statescript_r3 (AssociatedFiles) Statescript log run 3
  Group /processing/behavior (ProcessingModule) Contains all behavior-related data
  Group /processing/behavior/behavioral_events (BehavioralEvents) 
  Group /processing/behavior/behavioral_events/Arm1_light (TimeSeries) Dout13
  Group /processing/behavior/behavioral_events/Arm1_milk_pump (TimeSeries) Dout11
  Group /processing/behavior/behavioral_events/Arm1_poke (TimeSeries) Din13
  Group /processing/behavior/behavioral_events/Arm2_light (TimeSeries) Dout9
  Group /processing/behavior/behavioral_events/Arm2_milk_pump (TimeSeries) Dout12
  Group /processing/behavior/behavioral_events/Arm2_poke (TimeSeries) Din9
  Group /processing/behavior/behavioral_events/BackWell_light (TimeSeries) Dout10
  Group /processing/behavior/behavioral_events/BackWell_milk_pump (TimeSeries) Dout8
  Group /processing/behavior/behavioral_events/BackWell_poke (TimeSeries) Din10
  Group /processing/behavior/behavioral_events/CamerasyncRun (TimeSeries) Din15
  Group /processing/behavior/behavioral_events/CamerasyncSleep (TimeSeries) Din16
  Group /processing/behavior/behavioral_events/CenterWell_light (TimeSeries) Dout7
  Group /processing/behavior/behavioral_events/CenterWell_milk_pump (TimeSeries) Dout14
  Group /processing/behavior/behavioral_events/CenterWell_poke (TimeSeries) Din7
  Group /processing/behavior/position (Position) 
  Group /processing/behavior/position/led_0_series_0 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_0_series_1 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_0_series_2 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_0_series_3 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_0_series_4 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_0_series_5 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_0_series_6 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_1_series_0 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_1_series_1 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_1_series_2 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_1_series_3 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_1_series_4 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_1_series_5 (SpatialSeries) xloc, yloc
  Group /processing/behavior/position/led_1_series_6 (SpatialSeries) xloc, yloc
  Group /processing/camera_sample_frame_counts (ProcessingModule) Camera Sample Frame Counts
  Group /processing/camera_sample_frame_counts/camera_frame_counts (TimeSeries) hardware frame count
  Group /processing/sample_count (ProcessingModule) corespondence between sample count and timestamps
  Group /processing/sample_count/sample_count (TimeSeries) acquisition system sample count
  Group /processing/tasks (ProcessingModule) Contains all tasks information
  Group /processing/tasks/task_0 (DynamicTable) 
  Dataset /processing/tasks/task_0/camera_id (VectorData) the ID number of the camera used for video | shape = (1, 1) | dtype = int64
  Dataset /processing/tasks/task_0/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /processing/tasks/task_0/task_description (VectorData) a description of the task | shape = (1,) | dtype = object
  Dataset /processing/tasks/task_0/task_environment (VectorData) the environment in which the animal performed the task | shape = (1,) | dtype = object
  Dataset /processing/tasks/task_0/task_epochs (VectorData) the temporal epochs where the animal was exposed to this task | shape = (1, 3) | dtype = int64
  Dataset /processing/tasks/task_0/task_name (VectorData) the name of the task | shape = (1,) | dtype = object
  Group /processing/tasks/task_1 (DynamicTable) 
  Dataset /processing/tasks/task_1/camera_id (VectorData) the ID number of the camera used for video | shape = (1, 1) | dtype = int64
  Dataset /processing/tasks/task_1/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /processing/tasks/task_1/task_description (VectorData) a description of the task | shape = (1,) | dtype = object
  Dataset /processing/tasks/task_1/task_environment (VectorData) the environment in which the animal performed the task | shape = (1,) | dtype = object
  Dataset /processing/tasks/task_1/task_epochs (VectorData) the temporal epochs where the animal was exposed to this task | shape = (1, 4) | dtype = int64
  Dataset /processing/tasks/task_1/task_name (VectorData) the name of the task | shape = (1,) | dtype = object
  Group /processing/video_files (ProcessingModule) Contains all associated video files data
  Group /processing/video_files/video (BehavioralEvents) 
  Group /processing/video_files/video/20220318_arthur_01_s1.1.h264 (ImageSeries) video of animal behavior from epoch
  Group /processing/video_files/video/20220318_arthur_01_s1.1.h264/device (CameraDevice) 
  Group /processing/video_files/video/20220318_arthur_02_r1.1.h264 (ImageSeries) video of animal behavior from epoch
  Group /processing/video_files/video/20220318_arthur_02_r1.1.h264/device (CameraDevice) 
  Group /processing/video_files/video/20220318_arthur_03_s2.1.h264 (ImageSeries) video of animal behavior from epoch
  Group /processing/video_files/video/20220318_arthur_03_s2.1.h264/device (CameraDevice) 
  Group /processing/video_files/video/20220318_arthur_04_r2.1.h264 (ImageSeries) video of animal behavior from epoch
  Group /processing/video_files/video/20220318_arthur_04_r2.1.h264/device (CameraDevice) 
  Group /processing/video_files/video/20220318_arthur_05_s3.1.h264 (ImageSeries) video of animal behavior from epoch
  Group /processing/video_files/video/20220318_arthur_05_s3.1.h264/device (CameraDevice) 
  Group /processing/video_files/video/20220318_arthur_06_r3.1.h264 (ImageSeries) video of animal behavior from epoch
  Group /processing/video_files/video/20220318_arthur_06_r3.1.h264/device (CameraDevice) 
  Group /processing/video_files/video/20220318_arthur_07_s4.1.h264 (ImageSeries) video of animal behavior from epoch
  Group /processing/video_files/video/20220318_arthur_07_s4.1.h264/device (CameraDevice) 
  session_description: Hippocampus content feedback
  session_start_time: 2022-03-18T10:29:57.612000-07:00
  timestamps_reference_time: 1970-01-01T00:00:00+00:00
