
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000115/0.210914.1732
name: Gillespie et al (2021) Hippocampal replay reflects specific past experiences rather than a plan for subsequent choice
contributor: [{'name': 'Gillespie, Anna', 'email': 'akgillespie8@gmail.com', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0003-0980-2408', 'affiliation': [{'name': 'University of California, San Francisco', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/043mz5j54'}], 'awardNumber': 'Brain Initiative K99AG068425', 'includeInCitation': True}, {'name': 'Astudillo Maya, Daniela', 'email': 'daniela.astudillo@ucsf.edu', 'roleName': ['dcite:DataCollector'], 'schemaKey': 'Person', 'affiliation': [{'name': 'University of California, San Francisco', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/043mz5j54'}], 'includeInCitation': True}, {'name': 'Denovellis, Eric', 'email': 'eric.denovellis@ucsf.edu', 'roleName': ['dcite:Methodology', 'dcite:FormalAnalysis'], 'schemaKey': 'Person', 'identifier': '0000-0003-4606-087X', 'affiliation': [{'name': 'University of California, San Francisco', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/043mz5j54'}], 'includeInCitation': True}, {'name': 'Liu, Daniel', 'email': 'daniel.liu@ucsf.edu', 'roleName': ['dcite:Methodology'], 'schemaKey': 'Person', 'affiliation': [{'name': 'University of California, San Francisco', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/043mz5j54'}], 'includeInCitation': True}, {'name': 'Kastner, David', 'email': 'david.kastner2@ucsf.edu', 'roleName': ['dcite:Methodology'], 'schemaKey': 'Person', 'affiliation': [{'name': 'University of California, San Francisco', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/043mz5j54'}], 'includeInCitation': True}, {'name': 'Coulter, Michael', 'email': 'michael.coulter@ucsf.edu', 'roleName': ['dcite:Methodology'], 'schemaKey': 'Person', 'affiliation': [{'name': 'University of California, San Francisco', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/043mz5j54'}], 'includeInCitation': True}, {'name': 'Roumis, Demetris', 'email': 'roumis.d@gmail.com', 'roleName': ['dcite:Methodology'], 'schemaKey': 'Person', 'affiliation': [{'name': 'University of California, San Francisco', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/043mz5j54'}], 'includeInCitation': True}, {'name': 'Frank, Loren', 'email': 'loren@phy.ucsf.edu', 'roleName': ['dcite:DataManager', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [{'name': 'HHMI', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/006w34k90'}], 'includeInCitation': True}]
description: This dataset includes the electrophysiological (dorsal CA1 tetrodes) and behavioral (port triggers, reward delivery, and position tracking) data from Gillespie et al, Neuron 2021: "Hippocampal replay reflects specific past experiences rather than a plan for subsequent choice". For more information about this data, please contact Anna Gillespie or Loren Frank. 
assetsSummary: {'species': [{'name': 'Rat; norway rat; rats; brown rat', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10116'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}, {'name': 'behavioral approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 9103697961133, 'numberOfFiles': 57, 'numberOfSubjects': 4, 'variableMeasured': ['ElectricalSeries', 'Position'], 'measurementTechnique': [{'name': 'behavioral technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000115 has 5 NWB files.
1 of these NWB files are of type 1.
1 of these NWB files are of type 2.
1 of these NWB files are of type 3.
1 of these NWB files are of type 4.
1 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/e-series (ElectricalSeries) Recording of extracellular voltage
  Dataset /acquisition/e-series/electrodes (DynamicTableRegion) - | shape = (128,) | dtype = int64
  file_create_date: ['2021-06-26T01:54:39.419691-07:00']
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
  experiment_description: Eight arm flexible spatial task
  experimenter: ['Anna Gillespie']
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
  Group /general/extracellular_ephys/4 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/4/device (Probe) 
  Group /general/extracellular_ephys/4/device/0 (Shank) 
  Group /general/extracellular_ephys/4/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/4/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/4/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/4/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/5 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/5/device (Probe) 
  Group /general/extracellular_ephys/5/device/0 (Shank) 
  Group /general/extracellular_ephys/5/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/5/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/5/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/5/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/6 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/6/device (Probe) 
  Group /general/extracellular_ephys/6/device/0 (Shank) 
  Group /general/extracellular_ephys/6/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/6/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/6/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/6/device/0/3 (ShanksElectrode) 
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
  Dataset /general/extracellular_ephys/electrodes/bad_channel (VectorData) True if noisy or disconnected | shape = (128,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/channel_id (VectorData) None | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/hwChan (VectorData) SpikeGadgets Hardware channel | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/ntrode_id (VectorData) Experimenter defined ID for this probe | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/probe_electrode (VectorData) the number of this electrode with respect to the probe | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/probe_shank (VectorData) The shank of the probe this channel is located on | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/ref_elect_id (VectorData) “Experimenter selected reference electrode id” | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/rel_x (VectorData) None | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_y (VectorData) None | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_z (VectorData) None | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (128,) | dtype = float64
  institution: University of California, San Francisco
  lab: Loren Frank
  session_id: despereaux_03
  Group /general/subject (Subject) 
  identifier: 23ff03d2-d65c-11eb-ad55-6db614e01e37
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (5,) | dtype = int64
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (5,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (5,) | dtype = float64
  Dataset /intervals/epochs/tags (VectorData) user-defined tags | shape = (5,) | dtype = object
  Dataset /intervals/epochs/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (5,) | dtype = uint8
  Group /processing/analog (ProcessingModule) Contains all analog data
  Group /processing/analog/analog (BehavioralEvents) 
  Group /processing/analog/analog/analog (TimeSeries) AccelX   AccelY   AccelZ   GyroX   GyroY   GyroZ   MagX   MagY   MagZ   timestamps   
  Group /processing/associated_files (ProcessingModule) Contains all associated files data
  Group /processing/associated_files/statescript_r1 (AssociatedFiles) Statescript log r1
  Group /processing/associated_files/statescript_r2 (AssociatedFiles) Statescript log r2
  Group /processing/associated_files/statescript_s1 (AssociatedFiles) Statescript log s1
  Group /processing/associated_files/statescript_s2 (AssociatedFiles) Statescript log s2
  Group /processing/associated_files/statescript_s3 (AssociatedFiles) Statescript log s3
  Group /processing/behavior (ProcessingModule) Contains all behavior-related data
  Group /processing/behavior/behavioral_events (BehavioralEvents) 
  Group /processing/behavior/behavioral_events/Rbeam (TimeSeries) Din11
  Group /processing/behavior/behavioral_events/Rlight (TimeSeries) Dout11
  Group /processing/behavior/behavioral_events/Rpump (TimeSeries) Dout26
  Group /processing/behavior/behavioral_events/Wbeam (TimeSeries) Din12
  Group /processing/behavior/behavioral_events/Wlight (TimeSeries) Dout12
  Group /processing/behavior/behavioral_events/Wpump (TimeSeries) Dout27
  Group /processing/behavior/behavioral_events/arm1beam (TimeSeries) Din1
  Group /processing/behavior/behavioral_events/arm1light (TimeSeries) Dout1
  Group /processing/behavior/behavioral_events/arm1pump (TimeSeries) Dout17
  Group /processing/behavior/behavioral_events/arm2beam (TimeSeries) Din2
  Group /processing/behavior/behavioral_events/arm2light (TimeSeries) Dout2
  Group /processing/behavior/behavioral_events/arm2pump (TimeSeries) Dout18
  Group /processing/behavior/behavioral_events/arm3beam (TimeSeries) Din3
  Group /processing/behavior/behavioral_events/arm3light (TimeSeries) Dout3
  Group /processing/behavior/behavioral_events/arm3pump (TimeSeries) Dout19
  Group /processing/behavior/behavioral_events/arm4beam (TimeSeries) Din4
  Group /processing/behavior/behavioral_events/arm4light (TimeSeries) Dout4
  Group /processing/behavior/behavioral_events/arm4pump (TimeSeries) Dout20
  Group /processing/behavior/behavioral_events/arm5beam (TimeSeries) Din5
  Group /processing/behavior/behavioral_events/arm5light (TimeSeries) Dout5
  Group /processing/behavior/behavioral_events/arm5pump (TimeSeries) Dout21
  Group /processing/behavior/behavioral_events/arm6beam (TimeSeries) Din6
  Group /processing/behavior/behavioral_events/arm6light (TimeSeries) Dout6
  Group /processing/behavior/behavioral_events/arm6pump (TimeSeries) Dout22
  Group /processing/behavior/behavioral_events/arm7beam (TimeSeries) Din7
  Group /processing/behavior/behavioral_events/arm7light (TimeSeries) Dout7
  Group /processing/behavior/behavioral_events/arm7pump (TimeSeries) Dout23
  Group /processing/behavior/behavioral_events/arm8beam (TimeSeries) Din8
  Group /processing/behavior/behavioral_events/arm8light (TimeSeries) Dout8
  Group /processing/behavior/behavioral_events/arm8pump (TimeSeries) Dout24
  Group /processing/behavior/behavioral_events/camsync_run (TimeSeries) Din32
  Group /processing/behavior/behavioral_events/camsync_sleep (TimeSeries) Din31
  Group /processing/behavior/behavioral_events/homebeam (TimeSeries) Din10
  Group /processing/behavior/behavioral_events/homelight (TimeSeries) Dout10
  Group /processing/behavior/behavioral_events/homepump (TimeSeries) Dout25
  Group /processing/behavior/position (Position) 
  Group /processing/behavior/position/series_0 (SpatialSeries) xloc, yloc, xloc2, yloc2
  Group /processing/behavior/position/series_1 (SpatialSeries) xloc, yloc, xloc2, yloc2
  Group /processing/behavior/position/series_2 (SpatialSeries) xloc, yloc, xloc2, yloc2
  Group /processing/behavior/position/series_3 (SpatialSeries) xloc, yloc, xloc2, yloc2
  Group /processing/behavior/position/series_4 (SpatialSeries) xloc, yloc, xloc2, yloc2
  Group /processing/camera_sample_frame_counts (ProcessingModule) Camera Sample Frame Counts
  Group /processing/camera_sample_frame_counts/camera_frame_counts (TimeSeries) hardware frame count
  Group /processing/sample_count (ProcessingModule) corespondence between sample count and timestamps
  Group /processing/sample_count/sample_count (TimeSeries) acquisition system sample count
  Group /processing/tasks (ProcessingModule) Contains all tasks information
  Group /processing/tasks/task_0 (DynamicTable) 
  Dataset /processing/tasks/task_0/camera_id (VectorData) the ID number of the camera used for video | shape = (1, 1) | dtype = int64
  Dataset /processing/tasks/task_0/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /processing/tasks/task_0/task_description (VectorData) a description of the task | shape = (1,) | dtype = object
  Dataset /processing/tasks/task_0/task_epochs (VectorData) the temporal epochs where the animal was exposed to this task | shape = (1, 3) | dtype = int64
  Dataset /processing/tasks/task_0/task_name (VectorData) the name of the task | shape = (1,) | dtype = object
  Group /processing/tasks/task_1 (DynamicTable) 
  Dataset /processing/tasks/task_1/camera_id (VectorData) the ID number of the camera used for video | shape = (1, 1) | dtype = int64
  Dataset /processing/tasks/task_1/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /processing/tasks/task_1/task_description (VectorData) a description of the task | shape = (1,) | dtype = object
  Dataset /processing/tasks/task_1/task_epochs (VectorData) the temporal epochs where the animal was exposed to this task | shape = (1, 2) | dtype = int64
  Dataset /processing/tasks/task_1/task_name (VectorData) the name of the task | shape = (1,) | dtype = object
  Group /processing/video_files (ProcessingModule) Contains all associated video files data
  Group /processing/video_files/video (BehavioralEvents) 
  Group /processing/video_files/video/20191124_despereaux_01_s1.1.h264 (NwbImageSeries) video of animal behavior from epoch
  Group /processing/video_files/video/20191124_despereaux_01_s1.1.h264/camera_device 1 (CameraDevice) 
  Group /processing/video_files/video/20191124_despereaux_02_r1.1.h264 (NwbImageSeries) video of animal behavior from epoch
  Group /processing/video_files/video/20191124_despereaux_02_r1.1.h264/camera_device 0 (CameraDevice) 
  Group /processing/video_files/video/20191124_despereaux_03_s2.1.h264 (NwbImageSeries) video of animal behavior from epoch
  Group /processing/video_files/video/20191124_despereaux_03_s2.1.h264/camera_device 1 (CameraDevice) 
  Group /processing/video_files/video/20191124_despereaux_04_r2.1.h264 (NwbImageSeries) video of animal behavior from epoch
  Group /processing/video_files/video/20191124_despereaux_04_r2.1.h264/camera_device 0 (CameraDevice) 
  Group /processing/video_files/video/20191124_despereaux_05_s3.1.h264 (NwbImageSeries) video of animal behavior from epoch
  Group /processing/video_files/video/20191124_despereaux_05_s3.1.h264/camera_device 1 (CameraDevice) 
  session_description: Eight arm flexible spatial task
  session_start_time: 2019-11-24T10:18:34.912000-08:00
  timestamps_reference_time: 1970-01-01T00:00:00+00:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/e-series (ElectricalSeries) Recording of extracellular voltage
  Dataset /acquisition/e-series/electrodes (DynamicTableRegion) - | shape = (128,) | dtype = int64
  file_create_date: ['2021-06-26T03:05:16.804953-07:00']
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
  experiment_description: Eight arm flexible spatial task
  experimenter: ['Anna Gillespie']
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
  Group /general/extracellular_ephys/4 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/4/device (Probe) 
  Group /general/extracellular_ephys/4/device/0 (Shank) 
  Group /general/extracellular_ephys/4/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/4/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/4/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/4/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/5 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/5/device (Probe) 
  Group /general/extracellular_ephys/5/device/0 (Shank) 
  Group /general/extracellular_ephys/5/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/5/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/5/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/5/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/6 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/6/device (Probe) 
  Group /general/extracellular_ephys/6/device/0 (Shank) 
  Group /general/extracellular_ephys/6/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/6/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/6/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/6/device/0/3 (ShanksElectrode) 
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
  Dataset /general/extracellular_ephys/electrodes/bad_channel (VectorData) True if noisy or disconnected | shape = (128,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/channel_id (VectorData) None | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/hwChan (VectorData) SpikeGadgets Hardware channel | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/ntrode_id (VectorData) Experimenter defined ID for this probe | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/probe_electrode (VectorData) the number of this electrode with respect to the probe | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/probe_shank (VectorData) The shank of the probe this channel is located on | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/ref_elect_id (VectorData) “Experimenter selected reference electrode id” | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/rel_x (VectorData) None | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_y (VectorData) None | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_z (VectorData) None | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (128,) | dtype = float64
  institution: University of California, San Francisco
  lab: Loren Frank
  session_id: despereaux_04
  Group /general/subject (Subject) 
  identifier: 01acba72-d666-11eb-ad55-6db614e01e37
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (7,) | dtype = int64
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (7,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (7,) | dtype = float64
  Dataset /intervals/epochs/tags (VectorData) user-defined tags | shape = (7,) | dtype = object
  Dataset /intervals/epochs/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (7,) | dtype = uint8
  Group /processing/analog (ProcessingModule) Contains all analog data
  Group /processing/analog/analog (BehavioralEvents) 
  Group /processing/analog/analog/analog (TimeSeries) AccelX   AccelY   AccelZ   GyroX   GyroY   GyroZ   MagX   MagY   MagZ   timestamps   
  Group /processing/associated_files (ProcessingModule) Contains all associated files data
  Group /processing/associated_files/statescript_r1 (AssociatedFiles) Statescript log r1
  Group /processing/associated_files/statescript_r2 (AssociatedFiles) Statescript log r2
  Group /processing/associated_files/statescript_r3 (AssociatedFiles) Statescript log r3
  Group /processing/associated_files/statescript_s2 (AssociatedFiles) Statescript log s2
  Group /processing/associated_files/statescript_s3 (AssociatedFiles) Statescript log s3
  Group /processing/associated_files/statescript_s4 (AssociatedFiles) Statescript log s4
  Group /processing/behavior (ProcessingModule) Contains all behavior-related data
  Group /processing/behavior/behavioral_events (BehavioralEvents) 
  Group /processing/behavior/behavioral_events/Rbeam (TimeSeries) Din11
  Group /processing/behavior/behavioral_events/Rlight (TimeSeries) Dout11
  Group /processing/behavior/behavioral_events/Rpump (TimeSeries) Dout26
  Group /processing/behavior/behavioral_events/Wbeam (TimeSeries) Din12
  Group /processing/behavior/behavioral_events/Wlight (TimeSeries) Dout12
  Group /processing/behavior/behavioral_events/Wpump (TimeSeries) Dout27
  Group /processing/behavior/behavioral_events/arm1beam (TimeSeries) Din1
  Group /processing/behavior/behavioral_events/arm1light (TimeSeries) Dout1
  Group /processing/behavior/behavioral_events/arm1pump (TimeSeries) Dout17
  Group /processing/behavior/behavioral_events/arm2beam (TimeSeries) Din2
  Group /processing/behavior/behavioral_events/arm2light (TimeSeries) Dout2
  Group /processing/behavior/behavioral_events/arm2pump (TimeSeries) Dout18
  Group /processing/behavior/behavioral_events/arm3beam (TimeSeries) Din3
  Group /processing/behavior/behavioral_events/arm3light (TimeSeries) Dout3
  Group /processing/behavior/behavioral_events/arm3pump (TimeSeries) Dout19
  Group /processing/behavior/behavioral_events/arm4beam (TimeSeries) Din4
  Group /processing/behavior/behavioral_events/arm4light (TimeSeries) Dout4
  Group /processing/behavior/behavioral_events/arm4pump (TimeSeries) Dout20
  Group /processing/behavior/behavioral_events/arm5beam (TimeSeries) Din5
  Group /processing/behavior/behavioral_events/arm5light (TimeSeries) Dout5
  Group /processing/behavior/behavioral_events/arm5pump (TimeSeries) Dout21
  Group /processing/behavior/behavioral_events/arm6beam (TimeSeries) Din6
  Group /processing/behavior/behavioral_events/arm6light (TimeSeries) Dout6
  Group /processing/behavior/behavioral_events/arm6pump (TimeSeries) Dout22
  Group /processing/behavior/behavioral_events/arm7beam (TimeSeries) Din7
  Group /processing/behavior/behavioral_events/arm7light (TimeSeries) Dout7
  Group /processing/behavior/behavioral_events/arm7pump (TimeSeries) Dout23
  Group /processing/behavior/behavioral_events/arm8beam (TimeSeries) Din8
  Group /processing/behavior/behavioral_events/arm8light (TimeSeries) Dout8
  Group /processing/behavior/behavioral_events/arm8pump (TimeSeries) Dout24
  Group /processing/behavior/behavioral_events/camsync_run (TimeSeries) Din32
  Group /processing/behavior/behavioral_events/camsync_sleep (TimeSeries) Din31
  Group /processing/behavior/behavioral_events/homebeam (TimeSeries) Din10
  Group /processing/behavior/behavioral_events/homelight (TimeSeries) Dout10
  Group /processing/behavior/behavioral_events/homepump (TimeSeries) Dout25
  Group /processing/behavior/position (Position) 
  Group /processing/behavior/position/series_0 (SpatialSeries) xloc, yloc, xloc2, yloc2
  Group /processing/behavior/position/series_1 (SpatialSeries) xloc, yloc, xloc2, yloc2
  Group /processing/behavior/position/series_2 (SpatialSeries) xloc, yloc, xloc2, yloc2
  Group /processing/behavior/position/series_3 (SpatialSeries) xloc, yloc, xloc2, yloc2
  Group /processing/behavior/position/series_4 (SpatialSeries) xloc, yloc, xloc2, yloc2
  Group /processing/behavior/position/series_5 (SpatialSeries) xloc, yloc, xloc2, yloc2
  Group /processing/behavior/position/series_6 (SpatialSeries) xloc, yloc, xloc2, yloc2
  Group /processing/camera_sample_frame_counts (ProcessingModule) Camera Sample Frame Counts
  Group /processing/camera_sample_frame_counts/camera_frame_counts (TimeSeries) hardware frame count
  Group /processing/sample_count (ProcessingModule) corespondence between sample count and timestamps
  Group /processing/sample_count/sample_count (TimeSeries) acquisition system sample count
  Group /processing/tasks (ProcessingModule) Contains all tasks information
  Group /processing/tasks/task_0 (DynamicTable) 
  Dataset /processing/tasks/task_0/camera_id (VectorData) the ID number of the camera used for video | shape = (1, 1) | dtype = int64
  Dataset /processing/tasks/task_0/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /processing/tasks/task_0/task_description (VectorData) a description of the task | shape = (1,) | dtype = object
  Dataset /processing/tasks/task_0/task_epochs (VectorData) the temporal epochs where the animal was exposed to this task | shape = (1, 4) | dtype = int64
  Dataset /processing/tasks/task_0/task_name (VectorData) the name of the task | shape = (1,) | dtype = object
  Group /processing/tasks/task_1 (DynamicTable) 
  Dataset /processing/tasks/task_1/camera_id (VectorData) the ID number of the camera used for video | shape = (1, 1) | dtype = int64
  Dataset /processing/tasks/task_1/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /processing/tasks/task_1/task_description (VectorData) a description of the task | shape = (1,) | dtype = object
  Dataset /processing/tasks/task_1/task_epochs (VectorData) the temporal epochs where the animal was exposed to this task | shape = (1, 3) | dtype = int64
  Dataset /processing/tasks/task_1/task_name (VectorData) the name of the task | shape = (1,) | dtype = object
  Group /processing/video_files (ProcessingModule) Contains all associated video files data
  Group /processing/video_files/video (BehavioralEvents) 
  Group /processing/video_files/video/20191125_despereaux_01_s1.1.h264 (NwbImageSeries) video of animal behavior from epoch
  Group /processing/video_files/video/20191125_despereaux_01_s1.1.h264/camera_device 1 (CameraDevice) 
  Group /processing/video_files/video/20191125_despereaux_02_r1.1.h264 (NwbImageSeries) video of animal behavior from epoch
  Group /processing/video_files/video/20191125_despereaux_02_r1.1.h264/camera_device 0 (CameraDevice) 
  Group /processing/video_files/video/20191125_despereaux_03_s2.1.h264 (NwbImageSeries) video of animal behavior from epoch
  Group /processing/video_files/video/20191125_despereaux_03_s2.1.h264/camera_device 1 (CameraDevice) 
  Group /processing/video_files/video/20191125_despereaux_04_r2.1.h264 (NwbImageSeries) video of animal behavior from epoch
  Group /processing/video_files/video/20191125_despereaux_04_r2.1.h264/camera_device 0 (CameraDevice) 
  Group /processing/video_files/video/20191125_despereaux_05_s3.1.h264 (NwbImageSeries) video of animal behavior from epoch
  Group /processing/video_files/video/20191125_despereaux_05_s3.1.h264/camera_device 1 (CameraDevice) 
  Group /processing/video_files/video/20191125_despereaux_06_r3.1.h264 (NwbImageSeries) video of animal behavior from epoch
  Group /processing/video_files/video/20191125_despereaux_06_r3.1.h264/camera_device 0 (CameraDevice) 
  Group /processing/video_files/video/20191125_despereaux_07_s4.1.h264 (NwbImageSeries) video of animal behavior from epoch
  Group /processing/video_files/video/20191125_despereaux_07_s4.1.h264/camera_device 1 (CameraDevice) 
  session_description: Eight arm flexible spatial task
  session_start_time: 2019-11-25T10:17:28.899000-08:00
  timestamps_reference_time: 1970-01-01T00:00:00+00:00


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/e-series (ElectricalSeries) Recording of extracellular voltage
  Dataset /acquisition/e-series/electrodes (DynamicTableRegion) - | shape = (128,) | dtype = int64
  file_create_date: ['2021-07-12T19:18:23.754275-07:00']
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
  experiment_description: Eight arm flexible spatial task
  experimenter: ['Anna Gillespie']
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
  Group /general/extracellular_ephys/4 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/4/device (Probe) 
  Group /general/extracellular_ephys/4/device/0 (Shank) 
  Group /general/extracellular_ephys/4/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/4/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/4/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/4/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/5 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/5/device (Probe) 
  Group /general/extracellular_ephys/5/device/0 (Shank) 
  Group /general/extracellular_ephys/5/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/5/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/5/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/5/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/6 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/6/device (Probe) 
  Group /general/extracellular_ephys/6/device/0 (Shank) 
  Group /general/extracellular_ephys/6/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/6/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/6/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/6/device/0/3 (ShanksElectrode) 
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
  Dataset /general/extracellular_ephys/electrodes/bad_channel (VectorData) True if noisy or disconnected | shape = (128,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/channel_id (VectorData) None | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/hwChan (VectorData) SpikeGadgets Hardware channel | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/ntrode_id (VectorData) Experimenter defined ID for this probe | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/probe_electrode (VectorData) the number of this electrode with respect to the probe | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/probe_shank (VectorData) The shank of the probe this channel is located on | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/ref_elect_id (VectorData) “Experimenter selected reference electrode id” | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/rel_x (VectorData) None | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_y (VectorData) None | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_z (VectorData) None | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (128,) | dtype = float64
  institution: University of California, San Francisco
  lab: Loren Frank
  session_id: despereaux_05
  Group /general/subject (Subject) 
  identifier: 999e1ae8-e380-11eb-82d7-c51bccff95d6
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (5,) | dtype = int64
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (5,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (5,) | dtype = float64
  Dataset /intervals/epochs/tags (VectorData) user-defined tags | shape = (5,) | dtype = object
  Dataset /intervals/epochs/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (5,) | dtype = uint8
  Group /processing/analog (ProcessingModule) Contains all analog data
  Group /processing/analog/analog (BehavioralEvents) 
  Group /processing/analog/analog/analog (TimeSeries) AccelX   AccelY   AccelZ   GyroX   GyroY   GyroZ   MagX   MagY   MagZ   timestamps   
  Group /processing/associated_files (ProcessingModule) Contains all associated files data
  Group /processing/associated_files/statescript_r1 (AssociatedFiles) Statescript log r1
  Group /processing/associated_files/statescript_r2 (AssociatedFiles) Statescript log r2
  Group /processing/associated_files/statescript_s2 (AssociatedFiles) Statescript log s2
  Group /processing/associated_files/statescript_s3 (AssociatedFiles) Statescript log s3
  Group /processing/behavior (ProcessingModule) Contains all behavior-related data
  Group /processing/behavior/behavioral_events (BehavioralEvents) 
  Group /processing/behavior/behavioral_events/Rbeam (TimeSeries) Din11
  Group /processing/behavior/behavioral_events/Rlight (TimeSeries) Dout11
  Group /processing/behavior/behavioral_events/Rpump (TimeSeries) Dout26
  Group /processing/behavior/behavioral_events/Wbeam (TimeSeries) Din12
  Group /processing/behavior/behavioral_events/Wlight (TimeSeries) Dout12
  Group /processing/behavior/behavioral_events/Wpump (TimeSeries) Dout27
  Group /processing/behavior/behavioral_events/arm1beam (TimeSeries) Din1
  Group /processing/behavior/behavioral_events/arm1light (TimeSeries) Dout1
  Group /processing/behavior/behavioral_events/arm1pump (TimeSeries) Dout17
  Group /processing/behavior/behavioral_events/arm2beam (TimeSeries) Din2
  Group /processing/behavior/behavioral_events/arm2light (TimeSeries) Dout2
  Group /processing/behavior/behavioral_events/arm2pump (TimeSeries) Dout18
  Group /processing/behavior/behavioral_events/arm3beam (TimeSeries) Din3
  Group /processing/behavior/behavioral_events/arm3light (TimeSeries) Dout3
  Group /processing/behavior/behavioral_events/arm3pump (TimeSeries) Dout19
  Group /processing/behavior/behavioral_events/arm4beam (TimeSeries) Din4
  Group /processing/behavior/behavioral_events/arm4light (TimeSeries) Dout4
  Group /processing/behavior/behavioral_events/arm4pump (TimeSeries) Dout20
  Group /processing/behavior/behavioral_events/arm5beam (TimeSeries) Din5
  Group /processing/behavior/behavioral_events/arm5light (TimeSeries) Dout5
  Group /processing/behavior/behavioral_events/arm5pump (TimeSeries) Dout21
  Group /processing/behavior/behavioral_events/arm6beam (TimeSeries) Din6
  Group /processing/behavior/behavioral_events/arm6light (TimeSeries) Dout6
  Group /processing/behavior/behavioral_events/arm6pump (TimeSeries) Dout22
  Group /processing/behavior/behavioral_events/arm7beam (TimeSeries) Din7
  Group /processing/behavior/behavioral_events/arm7light (TimeSeries) Dout7
  Group /processing/behavior/behavioral_events/arm7pump (TimeSeries) Dout23
  Group /processing/behavior/behavioral_events/arm8beam (TimeSeries) Din8
  Group /processing/behavior/behavioral_events/arm8light (TimeSeries) Dout8
  Group /processing/behavior/behavioral_events/arm8pump (TimeSeries) Dout24
  Group /processing/behavior/behavioral_events/camsync_run (TimeSeries) Din32
  Group /processing/behavior/behavioral_events/camsync_sleep (TimeSeries) Din31
  Group /processing/behavior/behavioral_events/homebeam (TimeSeries) Din10
  Group /processing/behavior/behavioral_events/homelight (TimeSeries) Dout10
  Group /processing/behavior/behavioral_events/homepump (TimeSeries) Dout25
  Group /processing/behavior/position (Position) 
  Group /processing/behavior/position/series_0 (SpatialSeries) xloc, yloc, xloc2, yloc2
  Group /processing/behavior/position/series_1 (SpatialSeries) xloc, yloc, xloc2, yloc2
  Group /processing/behavior/position/series_2 (SpatialSeries) xloc, yloc, xloc2, yloc2
  Group /processing/behavior/position/series_3 (SpatialSeries) xloc, yloc, xloc2, yloc2
  Group /processing/behavior/position/series_4 (SpatialSeries) xloc, yloc, xloc2, yloc2
  Group /processing/camera_sample_frame_counts (ProcessingModule) Camera Sample Frame Counts
  Group /processing/camera_sample_frame_counts/camera_frame_counts (TimeSeries) hardware frame count
  Group /processing/sample_count (ProcessingModule) corespondence between sample count and timestamps
  Group /processing/sample_count/sample_count (TimeSeries) acquisition system sample count
  Group /processing/tasks (ProcessingModule) Contains all tasks information
  Group /processing/tasks/task_0 (DynamicTable) 
  Dataset /processing/tasks/task_0/camera_id (VectorData) the ID number of the camera used for video | shape = (1, 1) | dtype = int64
  Dataset /processing/tasks/task_0/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /processing/tasks/task_0/task_description (VectorData) a description of the task | shape = (1,) | dtype = object
  Dataset /processing/tasks/task_0/task_epochs (VectorData) the temporal epochs where the animal was exposed to this task | shape = (1, 3) | dtype = int64
  Dataset /processing/tasks/task_0/task_name (VectorData) the name of the task | shape = (1,) | dtype = object
  Group /processing/tasks/task_1 (DynamicTable) 
  Dataset /processing/tasks/task_1/camera_id (VectorData) the ID number of the camera used for video | shape = (1, 1) | dtype = int64
  Dataset /processing/tasks/task_1/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /processing/tasks/task_1/task_description (VectorData) a description of the task | shape = (1,) | dtype = object
  Dataset /processing/tasks/task_1/task_epochs (VectorData) the temporal epochs where the animal was exposed to this task | shape = (1, 2) | dtype = int64
  Dataset /processing/tasks/task_1/task_name (VectorData) the name of the task | shape = (1,) | dtype = object
  Group /processing/video_files (ProcessingModule) Contains all associated video files data
  Group /processing/video_files/video (BehavioralEvents) 
  Group /processing/video_files/video/20191126_despereaux_01_s1.1.h264 (NwbImageSeries) video of animal behavior from epoch
  Group /processing/video_files/video/20191126_despereaux_01_s1.1.h264/camera_device 1 (CameraDevice) 
  Group /processing/video_files/video/20191126_despereaux_02_r1.1.h264 (NwbImageSeries) video of animal behavior from epoch
  Group /processing/video_files/video/20191126_despereaux_02_r1.1.h264/camera_device 0 (CameraDevice) 
  Group /processing/video_files/video/20191126_despereaux_03_s2.1.h264 (NwbImageSeries) video of animal behavior from epoch
  Group /processing/video_files/video/20191126_despereaux_03_s2.1.h264/camera_device 1 (CameraDevice) 
  Group /processing/video_files/video/20191126_despereaux_04_r2.1.h264 (NwbImageSeries) video of animal behavior from epoch
  Group /processing/video_files/video/20191126_despereaux_04_r2.1.h264/camera_device 0 (CameraDevice) 
  Group /processing/video_files/video/20191126_despereaux_05_s3.1.h264 (NwbImageSeries) video of animal behavior from epoch
  Group /processing/video_files/video/20191126_despereaux_05_s3.1.h264/camera_device 1 (CameraDevice) 
  session_description: Eight arm flexible spatial task
  session_start_time: 2019-11-26T10:10:32.807000-08:00
  timestamps_reference_time: 1970-01-01T00:00:00+00:00


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/e-series (ElectricalSeries) Recording of extracellular voltage
  Dataset /acquisition/e-series/electrodes (DynamicTableRegion) - | shape = (128,) | dtype = int64
  file_create_date: ['2021-06-26T10:38:37.622923-07:00']
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
  experiment_description: Eight arm flexible spatial task
  experimenter: ['Anna Gillespie']
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
  Group /general/extracellular_ephys/4 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/4/device (Probe) 
  Group /general/extracellular_ephys/4/device/0 (Shank) 
  Group /general/extracellular_ephys/4/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/4/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/4/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/4/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/5 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/5/device (Probe) 
  Group /general/extracellular_ephys/5/device/0 (Shank) 
  Group /general/extracellular_ephys/5/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/5/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/5/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/5/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/6 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/6/device (Probe) 
  Group /general/extracellular_ephys/6/device/0 (Shank) 
  Group /general/extracellular_ephys/6/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/6/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/6/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/6/device/0/3 (ShanksElectrode) 
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
  Dataset /general/extracellular_ephys/electrodes/bad_channel (VectorData) True if noisy or disconnected | shape = (128,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/channel_id (VectorData) None | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/hwChan (VectorData) SpikeGadgets Hardware channel | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/ntrode_id (VectorData) Experimenter defined ID for this probe | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/probe_electrode (VectorData) the number of this electrode with respect to the probe | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/probe_shank (VectorData) The shank of the probe this channel is located on | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/ref_elect_id (VectorData) “Experimenter selected reference electrode id” | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/rel_x (VectorData) None | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_y (VectorData) None | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_z (VectorData) None | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (128,) | dtype = float64
  institution: University of California, San Francisco
  lab: Loren Frank
  session_id: despereaux_06
  Group /general/subject (Subject) 
  identifier: 56a028e0-d6a5-11eb-8d1b-6dbea9d56730
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (5,) | dtype = int64
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (5,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (5,) | dtype = float64
  Dataset /intervals/epochs/tags (VectorData) user-defined tags | shape = (5,) | dtype = object
  Dataset /intervals/epochs/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (5,) | dtype = uint8
  Group /processing/analog (ProcessingModule) Contains all analog data
  Group /processing/analog/analog (BehavioralEvents) 
  Group /processing/analog/analog/analog (TimeSeries) AccelX   AccelY   AccelZ   GyroX   GyroY   GyroZ   MagX   MagY   MagZ   timestamps   
  Group /processing/associated_files (ProcessingModule) Contains all associated files data
  Group /processing/associated_files/statescript_r1 (AssociatedFiles) Statescript log r1
  Group /processing/associated_files/statescript_r2 (AssociatedFiles) Statescript log r2
  Group /processing/associated_files/statescript_s1 (AssociatedFiles) Statescript log s1
  Group /processing/associated_files/statescript_s2 (AssociatedFiles) Statescript log s2
  Group /processing/associated_files/statescript_s3 (AssociatedFiles) Statescript log s3
  Group /processing/behavior (ProcessingModule) Contains all behavior-related data
  Group /processing/behavior/behavioral_events (BehavioralEvents) 
  Group /processing/behavior/behavioral_events/Rbeam (TimeSeries) Din11
  Group /processing/behavior/behavioral_events/Rlight (TimeSeries) Dout11
  Group /processing/behavior/behavioral_events/Rpump (TimeSeries) Dout26
  Group /processing/behavior/behavioral_events/Wbeam (TimeSeries) Din12
  Group /processing/behavior/behavioral_events/Wlight (TimeSeries) Dout12
  Group /processing/behavior/behavioral_events/Wpump (TimeSeries) Dout27
  Group /processing/behavior/behavioral_events/arm1beam (TimeSeries) Din1
  Group /processing/behavior/behavioral_events/arm1light (TimeSeries) Dout1
  Group /processing/behavior/behavioral_events/arm1pump (TimeSeries) Dout17
  Group /processing/behavior/behavioral_events/arm2beam (TimeSeries) Din2
  Group /processing/behavior/behavioral_events/arm2light (TimeSeries) Dout2
  Group /processing/behavior/behavioral_events/arm2pump (TimeSeries) Dout18
  Group /processing/behavior/behavioral_events/arm3beam (TimeSeries) Din3
  Group /processing/behavior/behavioral_events/arm3light (TimeSeries) Dout3
  Group /processing/behavior/behavioral_events/arm3pump (TimeSeries) Dout19
  Group /processing/behavior/behavioral_events/arm4beam (TimeSeries) Din4
  Group /processing/behavior/behavioral_events/arm4light (TimeSeries) Dout4
  Group /processing/behavior/behavioral_events/arm4pump (TimeSeries) Dout20
  Group /processing/behavior/behavioral_events/arm5beam (TimeSeries) Din5
  Group /processing/behavior/behavioral_events/arm5light (TimeSeries) Dout5
  Group /processing/behavior/behavioral_events/arm5pump (TimeSeries) Dout21
  Group /processing/behavior/behavioral_events/arm6beam (TimeSeries) Din6
  Group /processing/behavior/behavioral_events/arm6light (TimeSeries) Dout6
  Group /processing/behavior/behavioral_events/arm6pump (TimeSeries) Dout22
  Group /processing/behavior/behavioral_events/arm7beam (TimeSeries) Din7
  Group /processing/behavior/behavioral_events/arm7light (TimeSeries) Dout7
  Group /processing/behavior/behavioral_events/arm7pump (TimeSeries) Dout23
  Group /processing/behavior/behavioral_events/arm8beam (TimeSeries) Din8
  Group /processing/behavior/behavioral_events/arm8light (TimeSeries) Dout8
  Group /processing/behavior/behavioral_events/arm8pump (TimeSeries) Dout24
  Group /processing/behavior/behavioral_events/camsync_run (TimeSeries) Din32
  Group /processing/behavior/behavioral_events/camsync_sleep (TimeSeries) Din31
  Group /processing/behavior/behavioral_events/homebeam (TimeSeries) Din10
  Group /processing/behavior/behavioral_events/homelight (TimeSeries) Dout10
  Group /processing/behavior/behavioral_events/homepump (TimeSeries) Dout25
  Group /processing/behavior/position (Position) 
  Group /processing/behavior/position/series_0 (SpatialSeries) xloc, yloc, xloc2, yloc2
  Group /processing/behavior/position/series_1 (SpatialSeries) xloc, yloc, xloc2, yloc2
  Group /processing/behavior/position/series_2 (SpatialSeries) xloc, yloc, xloc2, yloc2
  Group /processing/behavior/position/series_3 (SpatialSeries) xloc, yloc, xloc2, yloc2
  Group /processing/behavior/position/series_4 (SpatialSeries) xloc, yloc, xloc2, yloc2
  Group /processing/camera_sample_frame_counts (ProcessingModule) Camera Sample Frame Counts
  Group /processing/camera_sample_frame_counts/camera_frame_counts (TimeSeries) hardware frame count
  Group /processing/sample_count (ProcessingModule) corespondence between sample count and timestamps
  Group /processing/sample_count/sample_count (TimeSeries) acquisition system sample count
  Group /processing/tasks (ProcessingModule) Contains all tasks information
  Group /processing/tasks/task_0 (DynamicTable) 
  Dataset /processing/tasks/task_0/camera_id (VectorData) the ID number of the camera used for video | shape = (1, 1) | dtype = int64
  Dataset /processing/tasks/task_0/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /processing/tasks/task_0/task_description (VectorData) a description of the task | shape = (1,) | dtype = object
  Dataset /processing/tasks/task_0/task_epochs (VectorData) the temporal epochs where the animal was exposed to this task | shape = (1, 3) | dtype = int64
  Dataset /processing/tasks/task_0/task_name (VectorData) the name of the task | shape = (1,) | dtype = object
  Group /processing/tasks/task_1 (DynamicTable) 
  Dataset /processing/tasks/task_1/camera_id (VectorData) the ID number of the camera used for video | shape = (1, 1) | dtype = int64
  Dataset /processing/tasks/task_1/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /processing/tasks/task_1/task_description (VectorData) a description of the task | shape = (1,) | dtype = object
  Dataset /processing/tasks/task_1/task_epochs (VectorData) the temporal epochs where the animal was exposed to this task | shape = (1, 2) | dtype = int64
  Dataset /processing/tasks/task_1/task_name (VectorData) the name of the task | shape = (1,) | dtype = object
  Group /processing/video_files (ProcessingModule) Contains all associated video files data
  Group /processing/video_files/video (BehavioralEvents) 
  Group /processing/video_files/video/20191127_despereaux_01_s1.1.h264 (NwbImageSeries) video of animal behavior from epoch
  Group /processing/video_files/video/20191127_despereaux_01_s1.1.h264/camera_device 1 (CameraDevice) 
  Group /processing/video_files/video/20191127_despereaux_02_r1.1.h264 (NwbImageSeries) video of animal behavior from epoch
  Group /processing/video_files/video/20191127_despereaux_02_r1.1.h264/camera_device 0 (CameraDevice) 
  Group /processing/video_files/video/20191127_despereaux_03_s2.1.h264 (NwbImageSeries) video of animal behavior from epoch
  Group /processing/video_files/video/20191127_despereaux_03_s2.1.h264/camera_device 1 (CameraDevice) 
  Group /processing/video_files/video/20191127_despereaux_04_r2.1.h264 (NwbImageSeries) video of animal behavior from epoch
  Group /processing/video_files/video/20191127_despereaux_04_r2.1.h264/camera_device 0 (CameraDevice) 
  Group /processing/video_files/video/20191127_despereaux_05_s3.1.h264 (NwbImageSeries) video of animal behavior from epoch
  Group /processing/video_files/video/20191127_despereaux_05_s3.1.h264/camera_device 1 (CameraDevice) 
  session_description: Eight arm flexible spatial task
  session_start_time: 2019-11-27T10:14:13.844000-08:00
  timestamps_reference_time: 1970-01-01T00:00:00+00:00


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  Group /acquisition/e-series (ElectricalSeries) Recording of extracellular voltage
  Dataset /acquisition/e-series/electrodes (DynamicTableRegion) - | shape = (128,) | dtype = int64
  file_create_date: ['2021-06-26T11:51:34.391158-07:00']
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
  experiment_description: Eight arm flexible spatial task
  experimenter: ['Anna Gillespie']
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
  Group /general/extracellular_ephys/4 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/4/device (Probe) 
  Group /general/extracellular_ephys/4/device/0 (Shank) 
  Group /general/extracellular_ephys/4/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/4/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/4/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/4/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/5 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/5/device (Probe) 
  Group /general/extracellular_ephys/5/device/0 (Shank) 
  Group /general/extracellular_ephys/5/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/5/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/5/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/5/device/0/3 (ShanksElectrode) 
  Group /general/extracellular_ephys/6 (NwbElectrodeGroup) tetrode
  Group /general/extracellular_ephys/6/device (Probe) 
  Group /general/extracellular_ephys/6/device/0 (Shank) 
  Group /general/extracellular_ephys/6/device/0/0 (ShanksElectrode) 
  Group /general/extracellular_ephys/6/device/0/1 (ShanksElectrode) 
  Group /general/extracellular_ephys/6/device/0/2 (ShanksElectrode) 
  Group /general/extracellular_ephys/6/device/0/3 (ShanksElectrode) 
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
  Dataset /general/extracellular_ephys/electrodes/bad_channel (VectorData) True if noisy or disconnected | shape = (128,) | dtype = bool
  Dataset /general/extracellular_ephys/electrodes/channel_id (VectorData) None | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/filtering (VectorData) description of hardware filtering | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group (VectorData) a reference to the ElectrodeGroup this electrode is a part of | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/group_name (VectorData) the name of the ElectrodeGroup this electrode is a part of | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/hwChan (VectorData) SpikeGadgets Hardware channel | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/id (ElementIdentifiers)  | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/imp (VectorData) the impedance of the channel | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/location (VectorData) the location of channel within the subject e.g. brain region | shape = (128,) | dtype = object
  Dataset /general/extracellular_ephys/electrodes/ntrode_id (VectorData) Experimenter defined ID for this probe | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/probe_electrode (VectorData) the number of this electrode with respect to the probe | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/probe_shank (VectorData) The shank of the probe this channel is located on | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/ref_elect_id (VectorData) “Experimenter selected reference electrode id” | shape = (128,) | dtype = int64
  Dataset /general/extracellular_ephys/electrodes/rel_x (VectorData) None | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_y (VectorData) None | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/rel_z (VectorData) None | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/x (VectorData) the x coordinate of the channel location | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/y (VectorData) the y coordinate of the channel location | shape = (128,) | dtype = float64
  Dataset /general/extracellular_ephys/electrodes/z (VectorData) the z coordinate of the channel location | shape = (128,) | dtype = float64
  institution: University of California, San Francisco
  lab: Loren Frank
  session_id: despereaux_07
  Group /general/subject (Subject) 
  identifier: 876216fa-d6af-11eb-8d1b-6dbea9d56730
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (3,) | dtype = int64
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (3,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (3,) | dtype = float64
  Dataset /intervals/epochs/tags (VectorData) user-defined tags | shape = (3,) | dtype = object
  Dataset /intervals/epochs/tags_index (VectorIndex) Index for VectorData 'tags' | shape = (3,) | dtype = uint8
  Group /processing/analog (ProcessingModule) Contains all analog data
  Group /processing/analog/analog (BehavioralEvents) 
  Group /processing/analog/analog/analog (TimeSeries) AccelX   AccelY   AccelZ   GyroX   GyroY   GyroZ   MagX   MagY   MagZ   timestamps   
  Group /processing/associated_files (ProcessingModule) Contains all associated files data
  Group /processing/associated_files/statescript_r1 (AssociatedFiles) Statescript log r1
  Group /processing/associated_files/statescript_s1 (AssociatedFiles) Statescript log s1
  Group /processing/associated_files/statescript_s2 (AssociatedFiles) Statescript log s2
  Group /processing/behavior (ProcessingModule) Contains all behavior-related data
  Group /processing/behavior/behavioral_events (BehavioralEvents) 
  Group /processing/behavior/behavioral_events/Rbeam (TimeSeries) Din11
  Group /processing/behavior/behavioral_events/Rlight (TimeSeries) Dout11
  Group /processing/behavior/behavioral_events/Rpump (TimeSeries) Dout26
  Group /processing/behavior/behavioral_events/Wbeam (TimeSeries) Din12
  Group /processing/behavior/behavioral_events/Wlight (TimeSeries) Dout12
  Group /processing/behavior/behavioral_events/Wpump (TimeSeries) Dout27
  Group /processing/behavior/behavioral_events/arm1beam (TimeSeries) Din1
  Group /processing/behavior/behavioral_events/arm1light (TimeSeries) Dout1
  Group /processing/behavior/behavioral_events/arm1pump (TimeSeries) Dout17
  Group /processing/behavior/behavioral_events/arm2beam (TimeSeries) Din2
  Group /processing/behavior/behavioral_events/arm2light (TimeSeries) Dout2
  Group /processing/behavior/behavioral_events/arm2pump (TimeSeries) Dout18
  Group /processing/behavior/behavioral_events/arm3beam (TimeSeries) Din3
  Group /processing/behavior/behavioral_events/arm3light (TimeSeries) Dout3
  Group /processing/behavior/behavioral_events/arm3pump (TimeSeries) Dout19
  Group /processing/behavior/behavioral_events/arm4beam (TimeSeries) Din4
  Group /processing/behavior/behavioral_events/arm4light (TimeSeries) Dout4
  Group /processing/behavior/behavioral_events/arm4pump (TimeSeries) Dout20
  Group /processing/behavior/behavioral_events/arm5beam (TimeSeries) Din5
  Group /processing/behavior/behavioral_events/arm5light (TimeSeries) Dout5
  Group /processing/behavior/behavioral_events/arm5pump (TimeSeries) Dout21
  Group /processing/behavior/behavioral_events/arm6beam (TimeSeries) Din6
  Group /processing/behavior/behavioral_events/arm6light (TimeSeries) Dout6
  Group /processing/behavior/behavioral_events/arm6pump (TimeSeries) Dout22
  Group /processing/behavior/behavioral_events/arm7beam (TimeSeries) Din7
  Group /processing/behavior/behavioral_events/arm7light (TimeSeries) Dout7
  Group /processing/behavior/behavioral_events/arm7pump (TimeSeries) Dout23
  Group /processing/behavior/behavioral_events/arm8beam (TimeSeries) Din8
  Group /processing/behavior/behavioral_events/arm8light (TimeSeries) Dout8
  Group /processing/behavior/behavioral_events/arm8pump (TimeSeries) Dout24
  Group /processing/behavior/behavioral_events/camsync_run (TimeSeries) Din32
  Group /processing/behavior/behavioral_events/camsync_sleep (TimeSeries) Din31
  Group /processing/behavior/behavioral_events/homebeam (TimeSeries) Din10
  Group /processing/behavior/behavioral_events/homelight (TimeSeries) Dout10
  Group /processing/behavior/behavioral_events/homepump (TimeSeries) Dout25
  Group /processing/behavior/position (Position) 
  Group /processing/behavior/position/series_0 (SpatialSeries) xloc, yloc, xloc2, yloc2
  Group /processing/behavior/position/series_1 (SpatialSeries) xloc, yloc, xloc2, yloc2
  Group /processing/behavior/position/series_2 (SpatialSeries) xloc, yloc, xloc2, yloc2
  Group /processing/camera_sample_frame_counts (ProcessingModule) Camera Sample Frame Counts
  Group /processing/camera_sample_frame_counts/camera_frame_counts (TimeSeries) hardware frame count
  Group /processing/sample_count (ProcessingModule) corespondence between sample count and timestamps
  Group /processing/sample_count/sample_count (TimeSeries) acquisition system sample count
  Group /processing/tasks (ProcessingModule) Contains all tasks information
  Group /processing/tasks/task_0 (DynamicTable) 
  Dataset /processing/tasks/task_0/camera_id (VectorData) the ID number of the camera used for video | shape = (1, 1) | dtype = int64
  Dataset /processing/tasks/task_0/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /processing/tasks/task_0/task_description (VectorData) a description of the task | shape = (1,) | dtype = object
  Dataset /processing/tasks/task_0/task_epochs (VectorData) the temporal epochs where the animal was exposed to this task | shape = (1, 2) | dtype = int64
  Dataset /processing/tasks/task_0/task_name (VectorData) the name of the task | shape = (1,) | dtype = object
  Group /processing/tasks/task_1 (DynamicTable) 
  Dataset /processing/tasks/task_1/camera_id (VectorData) the ID number of the camera used for video | shape = (1, 1) | dtype = int64
  Dataset /processing/tasks/task_1/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /processing/tasks/task_1/task_description (VectorData) a description of the task | shape = (1,) | dtype = object
  Dataset /processing/tasks/task_1/task_epochs (VectorData) the temporal epochs where the animal was exposed to this task | shape = (1, 1) | dtype = int64
  Dataset /processing/tasks/task_1/task_name (VectorData) the name of the task | shape = (1,) | dtype = object
  Group /processing/video_files (ProcessingModule) Contains all associated video files data
  Group /processing/video_files/video (BehavioralEvents) 
  Group /processing/video_files/video/20191128_despereaux_01_s1.1.h264 (NwbImageSeries) video of animal behavior from epoch
  Group /processing/video_files/video/20191128_despereaux_01_s1.1.h264/camera_device 1 (CameraDevice) 
  Group /processing/video_files/video/20191128_despereaux_02_r1.1.h264 (NwbImageSeries) video of animal behavior from epoch
  Group /processing/video_files/video/20191128_despereaux_02_r1.1.h264/camera_device 0 (CameraDevice) 
  Group /processing/video_files/video/20191128_despereaux_03_s2.1.h264 (NwbImageSeries) video of animal behavior from epoch
  Group /processing/video_files/video/20191128_despereaux_03_s2.1.h264/camera_device 1 (CameraDevice) 
  session_description: Eight arm flexible spatial task
  session_start_time: 2019-11-28T09:51:03.422000-08:00
  timestamps_reference_time: 1970-01-01T00:00:00+00:00
