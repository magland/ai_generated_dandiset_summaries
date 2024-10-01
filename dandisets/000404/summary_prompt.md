
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000404/0.230605.2024
name: Monkey 2D cursor BMI
contributor: [{'name': 'Athalye, Vivek R', 'email': 'va2371@columbia.edu', 'roleName': ['dcite:ContactPerson', 'dcite:Author', 'dcite:FormalAnalysis'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Khanna, Preeya', 'email': 'pkhanna@berkeley.edu', 'roleName': ['dcite:ContactPerson', 'dcite:DataCollector', 'dcite:Author', 'dcite:FormalAnalysis'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Gowda, Suraj', 'email': 'surajgowda@berkeley.edu', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Orsborn, Amy L', 'email': 'aorsborn@uw.edu', 'roleName': ['dcite:Author', 'dcite:DataCollector'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Costa, Rui M', 'email': 'rc3031@columbia.edu', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Carmena, Jose M', 'email': 'jcarmena@berkeley.edu', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'NIH NINDS', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01s5ya894', 'awardNumber': '1K99NS128250-01 ', 'contactPoint': [], 'includeInCitation': False}, {'name': 'NIH NINDS', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01s5ya894', 'awardNumber': '1K99NS124748-01 ', 'contactPoint': [], 'includeInCitation': False}, {'name': 'NIH NIMH', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/04xeg9z08', 'awardNumber': '1F32MH118714-01', 'contactPoint': [], 'includeInCitation': False}, {'name': 'NIH NIMH', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/04xeg9z08', 'awardNumber': '1F32MH120891-01', 'contactPoint': [], 'includeInCitation': False}, {'name': 'NIH NINDS', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01s5ya894', 'awardNumber': 'U19 NS104649', 'contactPoint': [], 'includeInCitation': False}, {'name': 'NIH NINDS', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01s5ya894', 'awardNumber': 'R01 NS106094', 'contactPoint': [], 'includeInCitation': False}, {'name': 'Simons-Emory International Consortium on Motor Control', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01cmst727', 'awardNumber': '#717104', 'contactPoint': [], 'includeInCitation': False}]
description: This dataset includes binned spike count data (chronic microwire arrays in PMd/M1) and brain-machine-interface behavioral data (2D cursor kinematics, target locations, trials) from Athalye, V*, Khanna, P*, Gowda S, Orsborn, AL, Costa RM**, Carmena, JC**, (2023) "Invariant neural dynamics drive commands to control different movements": https://www.biorxiv.org/content/10.1101/2021.08.27.457931v2. 

For more information about this data, please contact Vivek Athalye and/or Preeya Khanna. 

Code for analyzing this data and re-creating manuscript figures is located: https://github.com/pkhanna104/bmi_dynamics_code and archived at https://zenodo.org/record/8006653
assetsSummary: {'species': [{'name': 'Macaca mulatta - Rhesus monkey', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9544'}], 'approach': [], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 1046740856, 'numberOfFiles': 13, 'numberOfSubjects': 2, 'variableMeasured': ['ProcessingModule'], 'measurementTechnique': [{'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000404 has 13 NWB files.
13 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  file_create_date: ['2023-01-20T09:47:18.604380-08:00']
  experiment_description: Single unit recordings from chronically implanted microwire                 electrode array in PMd/M1 used for BMI control using Kalman filter decoder. File includes BMI-unit spike counts,                 BMI task parameters, and BMI cursor data used for analysis. TimeSeries are reported at 60 hz, BMI update rate was 10 Hz.                 Raw electrophysiolgy data files are not included
  experimenter: ['Khanna, Preeya']
  institution: UC Berkeley
  keywords: ['BMI control' 'kalman filter' 'chronic electrophysiolgy' 'motor cortex'
   'premotor cortex' 'microwire arrays' 'monkey']
  lab: Carmena lab
  session_id: session0
  Group /general/subject (Subject) 
  identifier: MonkeyG_session0
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (287,) | dtype = int64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (287,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (287,) | dtype = float64
  Group /processing/behavior (ProcessingModule) BMI spike counts and behavior
  Group /processing/behavior/cursor (TimeSeries) 2D cursor position (x, y) 
  Group /processing/behavior/decoder_state (TimeSeries) decoder state (2d-pos, 2d-vel, offset)
  Group /processing/behavior/obs_details (TimeSeries) description of obstacle shape (square, and side length of square in cm, is "na" if no obstacle
  Group /processing/behavior/obstacle_position (TimeSeries) position of obstacle (center of square, is (0,0) if no obstacle)
  Group /processing/behavior/spike_counts (TimeSeries) binned spike counts used for BMI control
  Group /processing/behavior/target_state (TimeSeries) target state (2d-pos, 2d-vel, offset) -- location of target
  Group /processing/behavior/te_num (TimeSeries) task entry number for trials (corresponds to task ID in bmi3d db.sql file
  Group /processing/behavior/update_bmi (TimeSeries) binary variable where "1" indicates bins which BMI was updated (10 hz, task runs at 60 hz)
  session_description: Monkey performing 2D cursor BMI
  session_start_time: 2016-03-02T00:00:00-08:00
  timestamps_reference_time: 2016-03-02T00:00:00-08:00
