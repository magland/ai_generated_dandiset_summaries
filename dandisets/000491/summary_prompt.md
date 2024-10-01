
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000491/0.230602.1307
name: BrainFlowZZZ
contributor: [{'name': 'Zhao, Yue', 'email': 'yuezhao@rochester.edu', 'roleName': ['dcite:ContactPerson', 'dcite:DataManager', 'dcite:Maintainer'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Boster, Kimberly', 'roleName': ['dcite:Researcher'], 'schemaKey': 'Person', 'identifier': '0000-0001-5178-128X', 'affiliation': [{'name': 'University of Rochester', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/022kthw22'}], 'includeInCitation': True}, {'name': 'Kelley, Douglas', 'email': 'd.h.kelley@rochester.edu', 'roleName': ['dcite:ContactPerson', 'dcite:ProjectLeader', 'dcite:ProjectManager'], 'schemaKey': 'Person', 'identifier': '0000-0001-9658-2954', 'affiliation': [{'name': 'University of Rochester', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/022kthw22'}], 'includeInCitation': True}, {'name': 'United States Department of the Army', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/035w1gb98', 'awardNumber': 'MURI W911NF1910280', 'contactPoint': [], 'includeInCitation': False}, {'name': 'National Institutes of Health', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/01cwqze88', 'awardNumber': 'U19NS128613 and R01AT012312', 'contactPoint': [], 'includeInCitation': False}, {'name': 'Raicevic, Nikola', 'email': 'nraicevi@u.rochester.edu', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [{'name': 'University of Rochester', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/022kthw22'}], 'includeInCitation': True}]
description: Dataset from the 2023 manuscript titled **_Sizes and Shapes of Perivascular Spaces Surrounding Murine Pial Arteries_** by Raicevic et al. DOI: 10.21203/rs.3.rs-2587250/v1.  

## Overview
The **14 datasets** from **9 subjects** include the original 3D two photon microscopy data from three channels which show tracer in the vessel, PVSs, and microspheres. Additionally, each dataset also includes the final binary segmentation of the PVS and vessel used to generate the model and statistics in the manuscript. Additional details regarding the subjects, tracer injection, image acquisition, and segmentation can be found in the manuscript at https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9949243/.

## Content
For easier navigation, below is a mapping between the NWB file names and the datasets referenced in the manuscript.
1. sub-21-07-19-b-act (Mouse 6, dataset K)
2. sub-21-09-01-b-act (Mouse 8, dataset M)
3. sub-21-09-20-b-act (Mouse 9, dataset N)
4. sub-21-10-08-b-act (Mouse 7, dataset L)
5. sub-BPN-M4 (Mouse 3, dataset E and F)
6. sub-BPN-M6 (Mouse 4, dataset G and H)
7. sub-BPN-M7 (Mouse 5, dataset I and J)
8. sub-BPN-OLD-M2 (Mouse 1, dataset A and B)
9. sub-BPN-OLD-M3 (Mouse 2, dataset C and D)

## Data Reading Instructions
The .nwb files can be viewed using PyNWB or MatNWB. To install and set up, please visit <https://www.nwb.org/how-to-use/>. Below, we show how to open and view an .nwb file using MatNWB. 
### Loading the image data
```matlab
nwb = nwbRead(PATH_TO_NWB_FILE);

% first check what color channels are present
>> nwb.acquisition
ans = 
  3×1 Set array with properties:
    TwoPhotonSeriesChanA: [types.core.TwoPhotonSeries]
    TwoPhotonSeriesChanB: [types.core.TwoPhotonSeries]
    TwoPhotonSeriesChanC: [types.core.TwoPhotonSeries]
```
The above code load the .nwb file and the output tells us that there are three channels present in the nwb file, which are ChanA, ChanB, and ChanC. Then, to load the actual data from a channel,
```matlab
% load the image data from ChanA
>> chanAdata = nwb.acquisition.get('TwoPhotonSeriesChanA').data.load();

% check its shape
>> size(chanAdata)
ans =
     1   512   512   181
```
### Loading the segmentation masks
For an overview of the mask for ChanA, for example,
```matlab
>> nwb.processing.get('ophys').nwbdatainterface.get('ImageSegmentation').planesegmentation.get('PlaneSegmentationChanA').image_mask.data
ans = 
  DataStub with properties:
    filename: '.\sub-BPN-M4_ses-20210524-m1_obj-1c8nyxo_ophys.nwb'
        path: '/processing/ophys/ImageSegmentation/PlaneSegmentationChanA/image_mask'
        dims: [512 512 181]
       ndims: 3
    dataType: 'logical'
```
To load the actual mask data into array (may take several seconds to load),
```matlab
% load mask from ChanA
>> mask = nwb.processing.get('ophys').nwbdatainterface.get('ImageSegmentation').planesegmentation.get('PlaneSegmentationChanA').image_mask.data.load();

% check its shape
>> size(mask)
ans =
   512   512   181
```
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 5324803662, 'numberOfFiles': 14, 'numberOfSubjects': 9, 'variableMeasured': ['TwoPhotonSeries', 'ImagingPlane', 'OpticalChannel', 'ProcessingModule', 'PlaneSegmentation'], 'measurementTechnique': [{'name': 'two-photon microscopy technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000491 has 14 NWB files.
11 of these NWB files are of type 1.
3 of these NWB files are of type 2.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/TwoPhotonSeriesChanA (TwoPhotonSeries) Two-photon series for Green fluorescent protein.
  Group /acquisition/TwoPhotonSeriesChanA/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeriesChanA/imaging_plane/device (Device) Bergamo II
  Group /acquisition/TwoPhotonSeriesChanA/imaging_plane/optical_channel (OpticalChannel) 
  Group /acquisition/TwoPhotonSeriesChanB (TwoPhotonSeries) Two-photon series for Alexa Fluor594/647 (tracer in PVS).
  Group /acquisition/TwoPhotonSeriesChanB/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeriesChanB/imaging_plane/device (Device) Bergamo II
  Group /acquisition/TwoPhotonSeriesChanB/imaging_plane/optical_channel (OpticalChannel) 
  Group /acquisition/TwoPhotonSeriesChanC (TwoPhotonSeries) Two-photon series for Alexa Fluor594/647 (tracer in PVS).
  Group /acquisition/TwoPhotonSeriesChanC/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeriesChanC/imaging_plane/device (Device) Bergamo II
  Group /acquisition/TwoPhotonSeriesChanC/imaging_plane/optical_channel (OpticalChannel) 
  file_create_date: ['2023-04-25T23:24:58.256494-04:00' '2023-06-01T23:15:59.292590-04:00']
  Group /general/devices/Device (Device) Bergamo II
  experiment_description: This data is labeled as location K in the 2023 manuscript, Sizes and shapes of perivascular spaces surrounding murine pial arteries  by Raicevic et al Additional details regarding the subjects, tracer injection, image acquisition, and segmentation can be found in the manuscript at https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9949243/
  experimenter: ['Ladron de Guevara, Antonio']
  institution: University of Rochester
  keywords: ['B-act Zstack']
  Group /general/optophysiology/imaging_plane1 (ImagingPlane) 
  Group /general/optophysiology/imaging_plane1/device (Device) Bergamo II
  Group /general/optophysiology/imaging_plane1/optical_channel (OpticalChannel) 
  Group /general/optophysiology/imaging_plane2 (ImagingPlane) 
  Group /general/optophysiology/imaging_plane2/device (Device) Bergamo II
  Group /general/optophysiology/imaging_plane2/optical_channel (OpticalChannel) 
  Group /general/optophysiology/imaging_plane3 (ImagingPlane) 
  Group /general/optophysiology/imaging_plane3/device (Device) Bergamo II
  Group /general/optophysiology/imaging_plane3/optical_channel (OpticalChannel) 
  session_id: 20210914-m1
  Group /general/subject (Subject) 
  identifier: 2021-07-19 12:21:54
  Group /processing/ophys (ProcessingModule) contains optical physiology data
  Group /processing/ophys/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentationChanA (PlaneSegmentation) Plane segmentation for ChanA
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentationChanA/id (ElementIdentifiers)  | shape = (234,) | dtype = int32
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentationChanA/image_mask (VectorData) Segmentation masks for blood vessel. | shape = (234, 512, 512) | dtype = bool
  Group /processing/ophys/ImageSegmentation/PlaneSegmentationChanA/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentationChanA/imaging_plane/device (Device) Bergamo II
  Group /processing/ophys/ImageSegmentation/PlaneSegmentationChanA/imaging_plane/optical_channel (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentationChanB (PlaneSegmentation) Plane segmentation for ChanB
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentationChanB/id (ElementIdentifiers)  | shape = (234,) | dtype = int32
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentationChanB/image_mask (VectorData) Segmentation masks for ChanB. | shape = (234, 512, 512) | dtype = bool
  Group /processing/ophys/ImageSegmentation/PlaneSegmentationChanB/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentationChanB/imaging_plane/device (Device) Bergamo II
  Group /processing/ophys/ImageSegmentation/PlaneSegmentationChanB/imaging_plane/optical_channel (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentationChanC (PlaneSegmentation) Plane segmentation for ChanC
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentationChanC/id (ElementIdentifiers)  | shape = (234,) | dtype = int32
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentationChanC/image_mask (VectorData) Segmentation masks for perivascular space. | shape = (234, 512, 512) | dtype = bool
  Group /processing/ophys/ImageSegmentation/PlaneSegmentationChanC/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentationChanC/imaging_plane/device (Device) Bergamo II
  Group /processing/ophys/ImageSegmentation/PlaneSegmentationChanC/imaging_plane/optical_channel (OpticalChannel) 
  session_description: Zstack (series of 2D microscopy images acquired with focal planes at various cortical depths separated by 1 micron) in the pial artery from a bAct-GFP mouse 15 min after cisterna magna injection
  session_start_time: 2021-07-19T12:21:54.000000-04:00
  timestamps_reference_time: 2021-07-19T12:21:54.000000-04:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/TwoPhotonSeriesChanA (TwoPhotonSeries) Two-photon series for Green fluorescent protein.
  Group /acquisition/TwoPhotonSeriesChanA/imaging_plane (ImagingPlane) 
  Group /acquisition/TwoPhotonSeriesChanA/imaging_plane/device (Device) Bergamo II
  Group /acquisition/TwoPhotonSeriesChanA/imaging_plane/optical_channel (OpticalChannel) 
  file_create_date: ['2023-04-25T23:21:01.714604-04:00' '2023-06-02T00:38:15.624742-04:00']
  Group /general/devices/Device (Device) Bergamo II
  experiment_description: This data is labeled as location M in the 2023 manuscript, Sizes and shapes of perivascular spaces surrounding murine pial arteries  by Raicevic et al Additional details regarding the subjects, tracer injection, image acquisition, and segmentation can be found in the manuscript at https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9949243/
  experimenter: ['Ladron de Guevara, Antonio']
  institution: University of Rochester
  keywords: ['B-act Zstack']
  Group /general/optophysiology/imaging_plane1 (ImagingPlane) 
  Group /general/optophysiology/imaging_plane1/device (Device) Bergamo II
  Group /general/optophysiology/imaging_plane1/optical_channel (OpticalChannel) 
  session_id: 20210901-m1
  Group /general/subject (Subject) 
  identifier: 2021-09-01 13:58:16
  Group /processing/ophys (ProcessingModule) contains optical physiology data
  Group /processing/ophys/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentationChanA (PlaneSegmentation) Plane segmentation for ChanA
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentationChanA/id (ElementIdentifiers)  | shape = (232,) | dtype = int32
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentationChanA/image_mask (VectorData) Segmentation masks for blood vessel. | shape = (232, 512, 512) | dtype = bool
  Group /processing/ophys/ImageSegmentation/PlaneSegmentationChanA/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentationChanA/imaging_plane/device (Device) Bergamo II
  Group /processing/ophys/ImageSegmentation/PlaneSegmentationChanA/imaging_plane/optical_channel (OpticalChannel) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentationChanC (PlaneSegmentation) Plane segmentation for ChanC
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentationChanC/id (ElementIdentifiers)  | shape = (232,) | dtype = int32
  Dataset /processing/ophys/ImageSegmentation/PlaneSegmentationChanC/image_mask (VectorData) Segmentation masks for perivascular space. | shape = (232, 512, 512) | dtype = bool
  Group /processing/ophys/ImageSegmentation/PlaneSegmentationChanC/imaging_plane (ImagingPlane) 
  Group /processing/ophys/ImageSegmentation/PlaneSegmentationChanC/imaging_plane/device (Device) Bergamo II
  Group /processing/ophys/ImageSegmentation/PlaneSegmentationChanC/imaging_plane/optical_channel (OpticalChannel) 
  session_description: Zstack (series of 2D microscopy images acquired with focal planes at various cortical depths separated by 1 micron) in the pial artery from a bAct-GFP mouse under ketamine/xylazine anesthesia and 3 min after atipamezole injection
  session_start_time: 2021-09-01T13:58:16.000000-04:00
  timestamps_reference_time: 2021-09-01T13:58:16.000000-04:00
