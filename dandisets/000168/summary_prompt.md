
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000168/draft
name: Simultaneous loose seal cell-attached recordings  and two-photon imaging of GCaMP8 expressing mouse V1 neurons with drifting gratings visual stimuli
contributor: [{'name': 'Rozsa, Marton', 'email': 'neurozmar@gmail.com', 'roleName': ['dcite:Author', 'dcite:Researcher', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [{'name': 'HHMI Janelia Research Campus', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/013sk6x84'}], 'awardNumber': 'HHMI', 'includeInCitation': True}, {'name': 'Liang, Yajie', 'email': 'Yajie.Liang@som.umaryland.edu', 'roleName': ['dcite:Author', 'dcite:Researcher'], 'schemaKey': 'Person', 'affiliation': [{'name': 'HHMI Janelia Research Campus', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/013sk6x84'}], 'includeInCitation': True}, {'name': 'Zhang, Yan', 'email': 'zhangy11@janelia.hhmi.org', 'roleName': ['dcite:Author', 'dcite:Researcher'], 'schemaKey': 'Person', 'affiliation': [{'name': 'HHMI Janelia Research Campus', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/013sk6x84'}], 'includeInCitation': True}, {'name': 'Hasseman, Jeremy', 'email': 'hassemanj@janelia.hhmi.org', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [{'name': 'HHMI Janelia Research Campus', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/013sk6x84'}], 'includeInCitation': True}, {'name': 'Kolb, Ilya', 'email': 'kolbi@janelia.hhmi.org', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'affiliation': [{'name': 'HHMI Janelia Research Campus', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/013sk6x84'}], 'includeInCitation': True}, {'name': 'Looger, Loren', 'email': 'loogerl@janelia.hhmi.org', 'roleName': ['dcite:Author', 'dcite:ProjectLeader'], 'schemaKey': 'Person', 'affiliation': [{'name': 'HHMI Janelia Research Campus', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/013sk6x84'}], 'includeInCitation': True}, {'name': 'Svoboda, Karel', 'email': 'svobodak@janelia.hhmi.org', 'roleName': ['dcite:Author', 'dcite:ProjectLeader', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [{'name': 'HHMI Janelia Research Campus', 'schemaKey': 'Affiliation', 'identifier': 'https://ror.org/013sk6x84'}], 'awardNumber': 'HHMI', 'includeInCitation': True}, {'name': 'HHMI', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'identifier': 'https://ror.org/006w34k90', 'contactPoint': [], 'includeInCitation': True}]
description: We tested the jGCaMP8 sensors in L2/3 pyramidal neurons of mouse primary visual cortex. We made a craniotomy over V1 and infected neurons with adeno-associated virus (AAV2/1-hSynapsin-1) encoding jGCaMP8 variants (s/m/f), jGCaMP7f, or XCaMP-Gf. 18-80 days after the virus injection, the mouse was anesthetized, and we surgically removed the cranial window and performed durotomy. The craniotomy was filled with 10-15 μL of 1.5% agarose, and a D-shaped coverslip was secured on top to suppress brain motion and leave access to the brain on the lateral side of the craniotomy. Then mice were lightly anesthetized and mounted under a custom two-photon microscope. Full-field, high-contrast drifting gratings were presented in each of eight directions to the contralateral eye. Two-photon imaging (122 Hz) was performed of L2/3 somata and neuropil combined with loose-seal, cell-attached electrophysiological recording of a single neuron in the field of view.
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}, {'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 1379111602445, 'numberOfFiles': 170, 'numberOfSubjects': 30, 'variableMeasured': ['PlaneSegmentation', 'CurrentClampStimulusSeries', 'CurrentClampSeries', 'TwoPhotonSeries', 'ProcessingModule', 'VoltageClampStimulusSeries', 'VoltageClampSeries'], 'measurementTechnique': [{'name': 'two-photon microscopy technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'current clamp technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'voltage clamp technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000168 has 8 NWB files.
1 of these NWB files are of type 1.
1 of these NWB files are of type 2.
3 of these NWB files are of type 3.
1 of these NWB files are of type 4.
2 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Registered movie 0 (TwoPhotonSeries) no description
  Group /acquisition/Registered movie 0/imaging_plane (ImagingPlane) 
  Group /acquisition/Registered movie 0/imaging_plane/device (Device) 
  Group /acquisition/Registered movie 0/imaging_plane/green (OpticalChannel) 
  Group /acquisition/Registered movie 1 (TwoPhotonSeries) no description
  Group /acquisition/Registered movie 1/imaging_plane (ImagingPlane) 
  Group /acquisition/Registered movie 1/imaging_plane/device (Device) 
  Group /acquisition/Registered movie 1/imaging_plane/green (OpticalChannel) 
  Group /acquisition/Registered movie 2 (TwoPhotonSeries) no description
  Group /acquisition/Registered movie 2/imaging_plane (ImagingPlane) 
  Group /acquisition/Registered movie 2/imaging_plane/device (Device) 
  Group /acquisition/Registered movie 2/imaging_plane/green (OpticalChannel) 
  Group /acquisition/Registered movie 3 (TwoPhotonSeries) no description
  Group /acquisition/Registered movie 3/imaging_plane (ImagingPlane) 
  Group /acquisition/Registered movie 3/imaging_plane/device (Device) 
  Group /acquisition/Registered movie 3/imaging_plane/green (OpticalChannel) 
  Group /acquisition/Registered movie 4 (TwoPhotonSeries) no description
  Group /acquisition/Registered movie 4/imaging_plane (ImagingPlane) 
  Group /acquisition/Registered movie 4/imaging_plane/device (Device) 
  Group /acquisition/Registered movie 4/imaging_plane/green (OpticalChannel) 
  Group /acquisition/loose seal recording for movie 0 (CurrentClampSeries) no description
  Group /acquisition/loose seal recording for movie 0/electrode (IntracellularElectrode) 
  Group /acquisition/loose seal recording for movie 0/electrode/device (Device) Multiclamp 700B with 20 kHz low-pass filter
  Group /acquisition/loose seal recording for movie 1 (CurrentClampSeries) no description
  Group /acquisition/loose seal recording for movie 1/electrode (IntracellularElectrode) 
  Group /acquisition/loose seal recording for movie 1/electrode/device (Device) Multiclamp 700B with 20 kHz low-pass filter
  Group /acquisition/loose seal recording for movie 2 (CurrentClampSeries) no description
  Group /acquisition/loose seal recording for movie 2/electrode (IntracellularElectrode) 
  Group /acquisition/loose seal recording for movie 2/electrode/device (Device) Multiclamp 700B with 20 kHz low-pass filter
  Group /acquisition/loose seal recording for movie 3 (CurrentClampSeries) no description
  Group /acquisition/loose seal recording for movie 3/electrode (IntracellularElectrode) 
  Group /acquisition/loose seal recording for movie 3/electrode/device (Device) Multiclamp 700B with 20 kHz low-pass filter
  Group /acquisition/loose seal recording for movie 4 (CurrentClampSeries) no description
  Group /acquisition/loose seal recording for movie 4/electrode (IntracellularElectrode) 
  Group /acquisition/loose seal recording for movie 4/electrode/device (Device) Multiclamp 700B with 20 kHz low-pass filter
  Group /analysis/responses (IntracellularResponsesTable) Table for storing intracellular response related metadata.
  Dataset /analysis/responses/ap_snr (VectorData) signal to noise ratio of detected loose-seal action potential | shape = (8312,) | dtype = float64
  Dataset /analysis/responses/ap_time (VectorData) peak time of detected loose-seal action potential | shape = (8312,) | dtype = float64
  Dataset /analysis/responses/id (ElementIdentifiers)  | shape = (8312,) | dtype = int64
  Dataset /analysis/responses/response (TimeSeriesReferenceVectorData) Column storing the reference to the recorded response for the recording (rows) | shape = (8312,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  file_create_date: ['2022-01-19T02:10:18.618505-08:00']
  Group /general/devices/MMIMS: custom-built two-photon microscope with a resonant scanner (Device) 
  Group /general/devices/Multiclamp 700B (Device) Multiclamp 700B with 20 kHz low-pass filter
  experiment_description: Simultaneous loose-seal cell-attached recordings and two-photon imaging of GCaMP (jGCaMP8s/m/f, jGCaMP7f, XCaMPgf) expressing mouse visual cortex neurons (pyramidal cells and FS interneurons) with drifting gratings visual stimuli
  experimenter: ['Marton Rozsa']
  institution: GENIE project, HHMI Janelia Research Campus
  Group /general/intracellular_ephys/Micropipette (IntracellularElectrode) 
  Group /general/intracellular_ephys/Micropipette/device (Device) Multiclamp 700B with 20 kHz low-pass filter
  Group /general/intracellular_ephys/sweep_table (SweepTable) A sweep table groups different PatchClampSeries together.
  Dataset /general/intracellular_ephys/sweep_table/id (ElementIdentifiers)  | shape = (5,) | dtype = int64
  Dataset /general/intracellular_ephys/sweep_table/series (VectorData) PatchClampSeries with the same sweep number | shape = (5,) | dtype = object
  Dataset /general/intracellular_ephys/sweep_table/series_index (VectorIndex) Index for VectorData 'series' | shape = (5,) | dtype = uint8
  Dataset /general/intracellular_ephys/sweep_table/sweep_number (VectorData) Sweep number of the entries in that row | shape = (5,) | dtype = uint64
  keywords: ['V1' 'calcium' 'spike' 'action potential' '2-photon' 'parvalbumin'
   'layer 2' 'AAV' 'adeno-associated virus']
  lab: Lab of Karel Svoboda at HHMI Janelia Research Campus
  Group /general/optophysiology/Movie_0 (ImagingPlane) 
  Group /general/optophysiology/Movie_0/device (Device) 
  Group /general/optophysiology/Movie_0/green (OpticalChannel) 
  Group /general/optophysiology/Movie_1 (ImagingPlane) 
  Group /general/optophysiology/Movie_1/device (Device) 
  Group /general/optophysiology/Movie_1/green (OpticalChannel) 
  Group /general/optophysiology/Movie_2 (ImagingPlane) 
  Group /general/optophysiology/Movie_2/device (Device) 
  Group /general/optophysiology/Movie_2/green (OpticalChannel) 
  Group /general/optophysiology/Movie_3 (ImagingPlane) 
  Group /general/optophysiology/Movie_3/device (Device) 
  Group /general/optophysiology/Movie_3/green (OpticalChannel) 
  Group /general/optophysiology/Movie_4 (ImagingPlane) 
  Group /general/optophysiology/Movie_4/device (Device) 
  Group /general/optophysiology/Movie_4/green (OpticalChannel) 
  related_publications: ['10.25378/janelia.13148243' '10.1101/2021.11.08.467793']
  session_id: XCaMPgf_ANM471996_cell01
  Group /general/subject (Subject) 
  surgery: [{"surgery_id": "1", "start_time": "2020-02-03 12:00:00", "end_time": "2020-02-03 12:50:00", "surgery_description": "headbar, craniotomy, virus injection, window:-: comments: nan"}, {"surgery_id": "2", "start_time": "2020-04-16 17:40:00", "end_time": "2020-04-16 19:10:00", "surgery_description": "window removal:-: comments: dura removed, light swelling, ketamine-xylazine anesthesia"}]
  virus: [{"surgery_id": "1", "injection_id": "1", "virus_id": "10245", "skull_reference": "Lambda", "ml_location": "2200.000", "ap_location": "0.000", "dv_location": "300.000", "volume": "30.000", "dilution": "9.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-NES-XCaMP-Gf-WPRE.538.1", "titer": "35400000000000.0", "order_date": "2019-08-22", "remarks": "XCaMP-Gf ref:1-862-1"}, {"surgery_id": "1", "injection_id": "2", "virus_id": "10245", "skull_reference": "Lambda", "ml_location": "2800.000", "ap_location": "600.000", "dv_location": "300.000", "volume": "30.000", "dilution": "9.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-NES-XCaMP-Gf-WPRE.538.1", "titer": "35400000000000.0", "order_date": "2019-08-22", "remarks": "XCaMP-Gf ref:1-862-1"}, {"surgery_id": "1", "injection_id": "3", "virus_id": "10245", "skull_reference": "Lambda", "ml_location": "2200.000", "ap_location": "600.000", "dv_location": "300.000", "volume": "30.000", "dilution": "9.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-NES-XCaMP-Gf-WPRE.538.1", "titer": "35400000000000.0", "order_date": "2019-08-22", "remarks": "XCaMP-Gf ref:1-862-1"}, {"surgery_id": "1", "injection_id": "4", "virus_id": "10245", "skull_reference": "Lambda", "ml_location": "2800.000", "ap_location": "0.000", "dv_location": "300.000", "volume": "30.000", "dilution": "36.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-NES-XCaMP-Gf-WPRE.538.1", "titer": "35400000000000.0", "order_date": "2019-08-22", "remarks": "XCaMP-Gf ref:1-862-1"}, {"surgery_id": "1", "injection_id": "5", "virus_id": "10245", "skull_reference": "Lambda", "ml_location": "2200.000", "ap_location": "0.000", "dv_location": "300.000", "volume": "30.000", "dilution": "9.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-NES-XCaMP-Gf-WPRE.538.1", "titer": "35400000000000.0", "order_date": "2019-08-22", "remarks": "XCaMP-Gf ref:1-862-1"}, {"surgery_id": "1", "injection_id": "6", "virus_id": "10245", "skull_reference": "Lambda", "ml_location": "2800.000", "ap_location": "600.000", "dv_location": "300.000", "volume": "30.000", "dilution": "9.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-NES-XCaMP-Gf-WPRE.538.1", "titer": "35400000000000.0", "order_date": "2019-08-22", "remarks": "XCaMP-Gf ref:1-862-1"}, {"surgery_id": "1", "injection_id": "7", "virus_id": "10245", "skull_reference": "Lambda", "ml_location": "2200.000", "ap_location": "600.000", "dv_location": "300.000", "volume": "30.000", "dilution": "9.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-NES-XCaMP-Gf-WPRE.538.1", "titer": "35400000000000.0", "order_date": "2019-08-22", "remarks": "XCaMP-Gf ref:1-862-1"}, {"surgery_id": "1", "injection_id": "8", "virus_id": "10245", "skull_reference": "Lambda", "ml_location": "2800.000", "ap_location": "0.000", "dv_location": "300.000", "volume": "30.000", "dilution": "36.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-NES-XCaMP-Gf-WPRE.538.1", "titer": "35400000000000.0", "order_date": "2019-08-22", "remarks": "XCaMP-Gf ref:1-862-1"}, {"surgery_id": "1", "injection_id": "9", "virus_id": "10245", "skull_reference": "Lambda", "ml_location": "2200.000", "ap_location": "0.000", "dv_location": "300.000", "volume": "30.000", "dilution": "9.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-NES-XCaMP-Gf-WPRE.538.1", "titer": "35400000000000.0", "order_date": "2019-08-22", "remarks": "XCaMP-Gf ref:1-862-1"}, {"surgery_id": "1", "injection_id": "10", "virus_id": "10245", "skull_reference": "Lambda", "ml_location": "2800.000", "ap_location": "600.000", "dv_location": "300.000", "volume": "30.000", "dilution": "9.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-NES-XCaMP-Gf-WPRE.538.1", "titer": "35400000000000.0", "order_date": "2019-08-22", "remarks": "XCaMP-Gf ref:1-862-1"}, {"surgery_id": "1", "injection_id": "11", "virus_id": "10245", "skull_reference": "Lambda", "ml_location": "2200.000", "ap_location": "600.000", "dv_location": "300.000", "volume": "30.000", "dilution": "9.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-NES-XCaMP-Gf-WPRE.538.1", "titer": "35400000000000.0", "order_date": "2019-08-22", "remarks": "XCaMP-Gf ref:1-862-1"}, {"surgery_id": "1", "injection_id": "12", "virus_id": "10245", "skull_reference": "Lambda", "ml_location": "2800.000", "ap_location": "0.000", "dv_location": "300.000", "volume": "30.000", "dilution": "36.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-NES-XCaMP-Gf-WPRE.538.1", "titer": "35400000000000.0", "order_date": "2019-08-22", "remarks": "XCaMP-Gf ref:1-862-1"}]
  identifier: XCaMPgf_ANM471996_cell01
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (5,) | dtype = int64
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (5,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (5,) | dtype = float64
  Dataset /intervals/epochs/timeseries (VectorData) index into a TimeSeries object | shape = (20,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/epochs/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (5,) | dtype = uint8
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/amplitude (VectorData) amplitude of drifting grating stimulus | shape = (200,) | dtype = float64
  Dataset /intervals/trials/angle (VectorData) angle of drifting grating stimulus in degrees | shape = (200,) | dtype = int64
  Dataset /intervals/trials/cycles_per_degree (VectorData) cycles per degree of drifting grating stimulus | shape = (200,) | dtype = float64
  Dataset /intervals/trials/cycles_per_second (VectorData) cycles per second of drifting grating stimulus | shape = (200,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (200,) | dtype = int64
  Dataset /intervals/trials/movie_number (VectorData) during which movie this visual stimulus happened | shape = (200,) | dtype = int64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (200,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (200,) | dtype = float64
  Group /processing/ophys of movie 0 (ProcessingModule) Processing result of imaging
  Group /processing/ophys of movie 0/Fluorescence (Fluorescence) 
  Group /processing/ophys of movie 0/Fluorescence/NeuropilResponseSeries (RoiResponseSeries) average fluorescence of the neuropil surrounding the roi
  Dataset /processing/ophys of movie 0/Fluorescence/NeuropilResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (0,) | dtype = int32
  Group /processing/ophys of movie 0/Fluorescence/RoiResponseSeries (RoiResponseSeries) weighted average fluorescence of roi
  Dataset /processing/ophys of movie 0/Fluorescence/RoiResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (0,) | dtype = int32
  Group /processing/ophys of movie 0/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation (PlaneSegmentation) output from segmenting with Suite2p, ROI 0 is the neuron recorded with electrophysiology
  Dataset /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/cell_type (VectorData) pyr for putative pyramidal cells, int for putative interneurons, based on average loose-seal spike shape | shape = (1,) | dtype = object
  Dataset /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (1, 256, 128) | dtype = float64
  Group /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/imaging_plane/device (Device) 
  Group /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/imaging_plane/green (OpticalChannel) 
  Dataset /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/neuropil_mask (VectorData) mask of neuropil surrounding this roi | shape = (1, 256, 128) | dtype = bool
  Dataset /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/recorded_with_ephys (VectorData) whether this ROI is simultaneously loose-seal recorded | shape = (1,) | dtype = bool
  Group /processing/ophys of movie 0/mean images of movie 0 (Images) Structural images of a scanning
  Dataset /processing/ophys of movie 0/mean images of movie 0/Alexa Fluor 594 in pipette (GrayscaleImage)  | shape = (256, 128) | dtype = float64
  Dataset /processing/ophys of movie 0/mean images of movie 0/XCaMPgf at 940nm (GrayscaleImage)  | shape = (256, 128) | dtype = float64
  Group /processing/ophys of movie 1 (ProcessingModule) Processing result of imaging
  Group /processing/ophys of movie 1/Fluorescence (Fluorescence) 
  Group /processing/ophys of movie 1/Fluorescence/NeuropilResponseSeries (RoiResponseSeries) average fluorescence of the neuropil surrounding the roi
  Dataset /processing/ophys of movie 1/Fluorescence/NeuropilResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (0,) | dtype = int32
  Group /processing/ophys of movie 1/Fluorescence/RoiResponseSeries (RoiResponseSeries) weighted average fluorescence of roi
  Dataset /processing/ophys of movie 1/Fluorescence/RoiResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (0,) | dtype = int32
  Group /processing/ophys of movie 1/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation (PlaneSegmentation) output from segmenting with Suite2p, ROI 0 is the neuron recorded with electrophysiology
  Dataset /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation/cell_type (VectorData) pyr for putative pyramidal cells, int for putative interneurons, based on average loose-seal spike shape | shape = (1,) | dtype = object
  Dataset /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (1, 256, 128) | dtype = float64
  Group /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation/imaging_plane/device (Device) 
  Group /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation/imaging_plane/green (OpticalChannel) 
  Dataset /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation/neuropil_mask (VectorData) mask of neuropil surrounding this roi | shape = (1, 256, 128) | dtype = bool
  Dataset /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation/recorded_with_ephys (VectorData) whether this ROI is simultaneously loose-seal recorded | shape = (1,) | dtype = bool
  Group /processing/ophys of movie 1/mean images of movie 1 (Images) Structural images of a scanning
  Dataset /processing/ophys of movie 1/mean images of movie 1/Alexa Fluor 594 in pipette (GrayscaleImage)  | shape = (256, 128) | dtype = float64
  Dataset /processing/ophys of movie 1/mean images of movie 1/XCaMPgf at 940nm (GrayscaleImage)  | shape = (256, 128) | dtype = float64
  Group /processing/ophys of movie 2 (ProcessingModule) Processing result of imaging
  Group /processing/ophys of movie 2/Fluorescence (Fluorescence) 
  Group /processing/ophys of movie 2/Fluorescence/NeuropilResponseSeries (RoiResponseSeries) average fluorescence of the neuropil surrounding the roi
  Dataset /processing/ophys of movie 2/Fluorescence/NeuropilResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (0,) | dtype = int32
  Group /processing/ophys of movie 2/Fluorescence/RoiResponseSeries (RoiResponseSeries) weighted average fluorescence of roi
  Dataset /processing/ophys of movie 2/Fluorescence/RoiResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (0,) | dtype = int32
  Group /processing/ophys of movie 2/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation (PlaneSegmentation) output from segmenting with Suite2p, ROI 0 is the neuron recorded with electrophysiology
  Dataset /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation/cell_type (VectorData) pyr for putative pyramidal cells, int for putative interneurons, based on average loose-seal spike shape | shape = (1,) | dtype = object
  Dataset /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (1, 256, 128) | dtype = float64
  Group /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation/imaging_plane/device (Device) 
  Group /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation/imaging_plane/green (OpticalChannel) 
  Dataset /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation/neuropil_mask (VectorData) mask of neuropil surrounding this roi | shape = (1, 256, 128) | dtype = bool
  Dataset /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation/recorded_with_ephys (VectorData) whether this ROI is simultaneously loose-seal recorded | shape = (1,) | dtype = bool
  Group /processing/ophys of movie 2/mean images of movie 2 (Images) Structural images of a scanning
  Dataset /processing/ophys of movie 2/mean images of movie 2/Alexa Fluor 594 in pipette (GrayscaleImage)  | shape = (256, 128) | dtype = float64
  Dataset /processing/ophys of movie 2/mean images of movie 2/XCaMPgf at 940nm (GrayscaleImage)  | shape = (256, 128) | dtype = float64
  Group /processing/ophys of movie 3 (ProcessingModule) Processing result of imaging
  Group /processing/ophys of movie 3/Fluorescence (Fluorescence) 
  Group /processing/ophys of movie 3/Fluorescence/NeuropilResponseSeries (RoiResponseSeries) average fluorescence of the neuropil surrounding the roi
  Dataset /processing/ophys of movie 3/Fluorescence/NeuropilResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (0,) | dtype = int32
  Group /processing/ophys of movie 3/Fluorescence/RoiResponseSeries (RoiResponseSeries) weighted average fluorescence of roi
  Dataset /processing/ophys of movie 3/Fluorescence/RoiResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (0,) | dtype = int32
  Group /processing/ophys of movie 3/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys of movie 3/ImageSegmentation/MovieSegmentation (PlaneSegmentation) output from segmenting with Suite2p, ROI 0 is the neuron recorded with electrophysiology
  Dataset /processing/ophys of movie 3/ImageSegmentation/MovieSegmentation/cell_type (VectorData) pyr for putative pyramidal cells, int for putative interneurons, based on average loose-seal spike shape | shape = (1,) | dtype = object
  Dataset /processing/ophys of movie 3/ImageSegmentation/MovieSegmentation/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /processing/ophys of movie 3/ImageSegmentation/MovieSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (1, 256, 128) | dtype = float64
  Group /processing/ophys of movie 3/ImageSegmentation/MovieSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys of movie 3/ImageSegmentation/MovieSegmentation/imaging_plane/device (Device) 
  Group /processing/ophys of movie 3/ImageSegmentation/MovieSegmentation/imaging_plane/green (OpticalChannel) 
  Dataset /processing/ophys of movie 3/ImageSegmentation/MovieSegmentation/neuropil_mask (VectorData) mask of neuropil surrounding this roi | shape = (1, 256, 128) | dtype = bool
  Dataset /processing/ophys of movie 3/ImageSegmentation/MovieSegmentation/recorded_with_ephys (VectorData) whether this ROI is simultaneously loose-seal recorded | shape = (1,) | dtype = bool
  Group /processing/ophys of movie 3/mean images of movie 3 (Images) Structural images of a scanning
  Dataset /processing/ophys of movie 3/mean images of movie 3/Alexa Fluor 594 in pipette (GrayscaleImage)  | shape = (256, 128) | dtype = float64
  Dataset /processing/ophys of movie 3/mean images of movie 3/XCaMPgf at 940nm (GrayscaleImage)  | shape = (256, 128) | dtype = float64
  Group /processing/ophys of movie 4 (ProcessingModule) Processing result of imaging
  Group /processing/ophys of movie 4/Fluorescence (Fluorescence) 
  Group /processing/ophys of movie 4/Fluorescence/NeuropilResponseSeries (RoiResponseSeries) average fluorescence of the neuropil surrounding the roi
  Dataset /processing/ophys of movie 4/Fluorescence/NeuropilResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (0,) | dtype = int32
  Group /processing/ophys of movie 4/Fluorescence/RoiResponseSeries (RoiResponseSeries) weighted average fluorescence of roi
  Dataset /processing/ophys of movie 4/Fluorescence/RoiResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (0,) | dtype = int32
  Group /processing/ophys of movie 4/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys of movie 4/ImageSegmentation/MovieSegmentation (PlaneSegmentation) output from segmenting with Suite2p, ROI 0 is the neuron recorded with electrophysiology
  Dataset /processing/ophys of movie 4/ImageSegmentation/MovieSegmentation/cell_type (VectorData) pyr for putative pyramidal cells, int for putative interneurons, based on average loose-seal spike shape | shape = (1,) | dtype = object
  Dataset /processing/ophys of movie 4/ImageSegmentation/MovieSegmentation/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /processing/ophys of movie 4/ImageSegmentation/MovieSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (1, 256, 128) | dtype = float64
  Group /processing/ophys of movie 4/ImageSegmentation/MovieSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys of movie 4/ImageSegmentation/MovieSegmentation/imaging_plane/device (Device) 
  Group /processing/ophys of movie 4/ImageSegmentation/MovieSegmentation/imaging_plane/green (OpticalChannel) 
  Dataset /processing/ophys of movie 4/ImageSegmentation/MovieSegmentation/neuropil_mask (VectorData) mask of neuropil surrounding this roi | shape = (1, 256, 128) | dtype = bool
  Dataset /processing/ophys of movie 4/ImageSegmentation/MovieSegmentation/recorded_with_ephys (VectorData) whether this ROI is simultaneously loose-seal recorded | shape = (1,) | dtype = bool
  Group /processing/ophys of movie 4/mean images of movie 4 (Images) Structural images of a scanning
  Dataset /processing/ophys of movie 4/mean images of movie 4/Alexa Fluor 594 in pipette (GrayscaleImage)  | shape = (256, 128) | dtype = float64
  Dataset /processing/ophys of movie 4/mean images of movie 4/XCaMPgf at 940nm (GrayscaleImage)  | shape = (256, 128) | dtype = float64
  session_description: 
  session_start_time: 2020-04-16T20:53:10-07:00
  timestamps_reference_time: 2020-04-16T20:53:10-07:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Registered movie 0 (TwoPhotonSeries) no description
  Group /acquisition/Registered movie 0/imaging_plane (ImagingPlane) 
  Group /acquisition/Registered movie 0/imaging_plane/device (Device) 
  Group /acquisition/Registered movie 0/imaging_plane/green (OpticalChannel) 
  Group /acquisition/Registered movie 1 (TwoPhotonSeries) no description
  Group /acquisition/Registered movie 1/imaging_plane (ImagingPlane) 
  Group /acquisition/Registered movie 1/imaging_plane/device (Device) 
  Group /acquisition/Registered movie 1/imaging_plane/green (OpticalChannel) 
  Group /acquisition/Registered movie 2 (TwoPhotonSeries) no description
  Group /acquisition/Registered movie 2/imaging_plane (ImagingPlane) 
  Group /acquisition/Registered movie 2/imaging_plane/device (Device) 
  Group /acquisition/Registered movie 2/imaging_plane/green (OpticalChannel) 
  Group /acquisition/loose seal recording for movie 0 (CurrentClampSeries) no description
  Group /acquisition/loose seal recording for movie 0/electrode (IntracellularElectrode) 
  Group /acquisition/loose seal recording for movie 0/electrode/device (Device) Multiclamp 700B with 20 kHz low-pass filter
  Group /acquisition/loose seal recording for movie 1 (CurrentClampSeries) no description
  Group /acquisition/loose seal recording for movie 1/electrode (IntracellularElectrode) 
  Group /acquisition/loose seal recording for movie 1/electrode/device (Device) Multiclamp 700B with 20 kHz low-pass filter
  Group /acquisition/loose seal recording for movie 2 (CurrentClampSeries) no description
  Group /acquisition/loose seal recording for movie 2/electrode (IntracellularElectrode) 
  Group /acquisition/loose seal recording for movie 2/electrode/device (Device) Multiclamp 700B with 20 kHz low-pass filter
  Group /acquisition/loose seal stimulus for movie 0 (CurrentClampStimulusSeries) no description
  Group /acquisition/loose seal stimulus for movie 0/electrode (IntracellularElectrode) 
  Group /acquisition/loose seal stimulus for movie 0/electrode/device (Device) Multiclamp 700B with 20 kHz low-pass filter
  Group /acquisition/loose seal stimulus for movie 1 (CurrentClampStimulusSeries) no description
  Group /acquisition/loose seal stimulus for movie 1/electrode (IntracellularElectrode) 
  Group /acquisition/loose seal stimulus for movie 1/electrode/device (Device) Multiclamp 700B with 20 kHz low-pass filter
  Group /acquisition/loose seal stimulus for movie 2 (CurrentClampStimulusSeries) no description
  Group /acquisition/loose seal stimulus for movie 2/electrode (IntracellularElectrode) 
  Group /acquisition/loose seal stimulus for movie 2/electrode/device (Device) Multiclamp 700B with 20 kHz low-pass filter
  Group /analysis/responses (IntracellularResponsesTable) Table for storing intracellular response related metadata.
  Dataset /analysis/responses/ap_snr (VectorData) signal to noise ratio of detected loose-seal action potential | shape = (2939,) | dtype = float64
  Dataset /analysis/responses/ap_time (VectorData) peak time of detected loose-seal action potential | shape = (2939,) | dtype = float64
  Dataset /analysis/responses/id (ElementIdentifiers)  | shape = (2939,) | dtype = int64
  Dataset /analysis/responses/response (TimeSeriesReferenceVectorData) Column storing the reference to the recorded response for the recording (rows) | shape = (2939,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  file_create_date: ['2022-01-19T02:15:53.895720-08:00']
  Group /general/devices/MMIMS: custom-built two-photon microscope with a resonant scanner (Device) 
  Group /general/devices/Multiclamp 700B (Device) Multiclamp 700B with 20 kHz low-pass filter
  experiment_description: Simultaneous loose-seal cell-attached recordings and two-photon imaging of GCaMP (jGCaMP8s/m/f, jGCaMP7f, XCaMPgf) expressing mouse visual cortex neurons (pyramidal cells and FS interneurons) with drifting gratings visual stimuli
  experimenter: ['Marton Rozsa']
  institution: GENIE project, HHMI Janelia Research Campus
  Group /general/intracellular_ephys/Micropipette (IntracellularElectrode) 
  Group /general/intracellular_ephys/Micropipette/device (Device) Multiclamp 700B with 20 kHz low-pass filter
  Group /general/intracellular_ephys/sweep_table (SweepTable) A sweep table groups different PatchClampSeries together.
  Dataset /general/intracellular_ephys/sweep_table/id (ElementIdentifiers)  | shape = (6,) | dtype = int64
  Dataset /general/intracellular_ephys/sweep_table/series (VectorData) PatchClampSeries with the same sweep number | shape = (6,) | dtype = object
  Dataset /general/intracellular_ephys/sweep_table/series_index (VectorIndex) Index for VectorData 'series' | shape = (6,) | dtype = uint8
  Dataset /general/intracellular_ephys/sweep_table/sweep_number (VectorData) Sweep number of the entries in that row | shape = (6,) | dtype = uint64
  keywords: ['V1' 'calcium' 'spike' 'action potential' '2-photon' 'parvalbumin'
   'layer 2' 'AAV' 'adeno-associated virus']
  lab: Lab of Karel Svoboda at HHMI Janelia Research Campus
  Group /general/optophysiology/Movie_0 (ImagingPlane) 
  Group /general/optophysiology/Movie_0/device (Device) 
  Group /general/optophysiology/Movie_0/green (OpticalChannel) 
  Group /general/optophysiology/Movie_1 (ImagingPlane) 
  Group /general/optophysiology/Movie_1/device (Device) 
  Group /general/optophysiology/Movie_1/green (OpticalChannel) 
  Group /general/optophysiology/Movie_2 (ImagingPlane) 
  Group /general/optophysiology/Movie_2/device (Device) 
  Group /general/optophysiology/Movie_2/green (OpticalChannel) 
  related_publications: ['10.25378/janelia.13148243' '10.1101/2021.11.08.467793']
  session_id: XCaMPgf_ANM478343_cell01
  Group /general/subject (Subject) 
  surgery: [{"surgery_id": "1", "start_time": "2020-06-05 16:20:00", "end_time": "2020-06-05 17:45:00", "surgery_description": "headbar, craniotomy, virus injection, window:-: comments: nan"}, {"surgery_id": "2", "start_time": "2020-06-27 12:00:00", "end_time": "2020-06-27 12:55:00", "surgery_description": "window removal:-: comments: fine"}]
  virus: [{"surgery_id": "1", "injection_id": "1", "virus_id": "10245", "skull_reference": "Lambda", "ml_location": "2200.000", "ap_location": "250.000", "dv_location": "300.000", "volume": "35.000", "dilution": "8.00", "description": "virus injection: blood during injection 1 and 3", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-NES-XCaMP-Gf-WPRE.538.1", "titer": "35400000000000.0", "order_date": "2019-08-22", "remarks": "XCaMP-Gf ref:1-862-1"}, {"surgery_id": "1", "injection_id": "2", "virus_id": "10245", "skull_reference": "Lambda", "ml_location": "2800.000", "ap_location": "200.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: blood during injection 1 and 3", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-NES-XCaMP-Gf-WPRE.538.1", "titer": "35400000000000.0", "order_date": "2019-08-22", "remarks": "XCaMP-Gf ref:1-862-1"}, {"surgery_id": "1", "injection_id": "3", "virus_id": "10245", "skull_reference": "Lambda", "ml_location": "2800.000", "ap_location": "800.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: blood during injection 1 and 3", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-NES-XCaMP-Gf-WPRE.538.1", "titer": "35400000000000.0", "order_date": "2019-08-22", "remarks": "XCaMP-Gf ref:1-862-1"}, {"surgery_id": "1", "injection_id": "4", "virus_id": "10245", "skull_reference": "Lambda", "ml_location": "2200.000", "ap_location": "900.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: blood during injection 1 and 3", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-NES-XCaMP-Gf-WPRE.538.1", "titer": "35400000000000.0", "order_date": "2019-08-22", "remarks": "XCaMP-Gf ref:1-862-1"}, {"surgery_id": "1", "injection_id": "5", "virus_id": "10245", "skull_reference": "Lambda", "ml_location": "2200.000", "ap_location": "250.000", "dv_location": "300.000", "volume": "35.000", "dilution": "8.00", "description": "virus injection: blood during injection 1 and 3", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-NES-XCaMP-Gf-WPRE.538.1", "titer": "35400000000000.0", "order_date": "2019-08-22", "remarks": "XCaMP-Gf ref:1-862-1"}, {"surgery_id": "1", "injection_id": "6", "virus_id": "10245", "skull_reference": "Lambda", "ml_location": "2800.000", "ap_location": "200.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: blood during injection 1 and 3", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-NES-XCaMP-Gf-WPRE.538.1", "titer": "35400000000000.0", "order_date": "2019-08-22", "remarks": "XCaMP-Gf ref:1-862-1"}, {"surgery_id": "1", "injection_id": "7", "virus_id": "10245", "skull_reference": "Lambda", "ml_location": "2800.000", "ap_location": "800.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: blood during injection 1 and 3", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-NES-XCaMP-Gf-WPRE.538.1", "titer": "35400000000000.0", "order_date": "2019-08-22", "remarks": "XCaMP-Gf ref:1-862-1"}, {"surgery_id": "1", "injection_id": "8", "virus_id": "10245", "skull_reference": "Lambda", "ml_location": "2200.000", "ap_location": "900.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: blood during injection 1 and 3", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-NES-XCaMP-Gf-WPRE.538.1", "titer": "35400000000000.0", "order_date": "2019-08-22", "remarks": "XCaMP-Gf ref:1-862-1"}, {"surgery_id": "1", "injection_id": "9", "virus_id": "10245", "skull_reference": "Lambda", "ml_location": "2200.000", "ap_location": "250.000", "dv_location": "300.000", "volume": "35.000", "dilution": "8.00", "description": "virus injection: blood during injection 1 and 3", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-NES-XCaMP-Gf-WPRE.538.1", "titer": "35400000000000.0", "order_date": "2019-08-22", "remarks": "XCaMP-Gf ref:1-862-1"}, {"surgery_id": "1", "injection_id": "10", "virus_id": "10245", "skull_reference": "Lambda", "ml_location": "2800.000", "ap_location": "200.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: blood during injection 1 and 3", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-NES-XCaMP-Gf-WPRE.538.1", "titer": "35400000000000.0", "order_date": "2019-08-22", "remarks": "XCaMP-Gf ref:1-862-1"}, {"surgery_id": "1", "injection_id": "11", "virus_id": "10245", "skull_reference": "Lambda", "ml_location": "2800.000", "ap_location": "800.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: blood during injection 1 and 3", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-NES-XCaMP-Gf-WPRE.538.1", "titer": "35400000000000.0", "order_date": "2019-08-22", "remarks": "XCaMP-Gf ref:1-862-1"}, {"surgery_id": "1", "injection_id": "12", "virus_id": "10245", "skull_reference": "Lambda", "ml_location": "2200.000", "ap_location": "900.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: blood during injection 1 and 3", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-NES-XCaMP-Gf-WPRE.538.1", "titer": "35400000000000.0", "order_date": "2019-08-22", "remarks": "XCaMP-Gf ref:1-862-1"}]
  identifier: XCaMPgf_ANM478343_cell01
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (3,) | dtype = int64
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (3,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (3,) | dtype = float64
  Dataset /intervals/epochs/timeseries (VectorData) index into a TimeSeries object | shape = (12,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/epochs/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (3,) | dtype = uint8
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/amplitude (VectorData) amplitude of drifting grating stimulus | shape = (120,) | dtype = float64
  Dataset /intervals/trials/angle (VectorData) angle of drifting grating stimulus in degrees | shape = (120,) | dtype = int64
  Dataset /intervals/trials/cycles_per_degree (VectorData) cycles per degree of drifting grating stimulus | shape = (120,) | dtype = float64
  Dataset /intervals/trials/cycles_per_second (VectorData) cycles per second of drifting grating stimulus | shape = (120,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (120,) | dtype = int64
  Dataset /intervals/trials/movie_number (VectorData) during which movie this visual stimulus happened | shape = (120,) | dtype = int64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (120,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (120,) | dtype = float64
  Group /processing/ophys of movie 0 (ProcessingModule) Processing result of imaging
  Group /processing/ophys of movie 0/Fluorescence (Fluorescence) 
  Group /processing/ophys of movie 0/Fluorescence/NeuropilResponseSeries (RoiResponseSeries) average fluorescence of the neuropil surrounding the roi
  Dataset /processing/ophys of movie 0/Fluorescence/NeuropilResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (2,) | dtype = int64
  Group /processing/ophys of movie 0/Fluorescence/RoiResponseSeries (RoiResponseSeries) weighted average fluorescence of roi
  Dataset /processing/ophys of movie 0/Fluorescence/RoiResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (2,) | dtype = int64
  Group /processing/ophys of movie 0/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation (PlaneSegmentation) output from segmenting with Suite2p, ROI 0 is the neuron recorded with electrophysiology
  Dataset /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/cell_type (VectorData) pyr for putative pyramidal cells, int for putative interneurons, based on average loose-seal spike shape | shape = (3,) | dtype = object
  Dataset /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/id (ElementIdentifiers)  | shape = (3,) | dtype = int64
  Dataset /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (3, 512, 128) | dtype = float64
  Group /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/imaging_plane/device (Device) 
  Group /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/imaging_plane/green (OpticalChannel) 
  Dataset /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/neuropil_mask (VectorData) mask of neuropil surrounding this roi | shape = (3, 512, 128) | dtype = bool
  Dataset /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/recorded_with_ephys (VectorData) whether this ROI is simultaneously loose-seal recorded | shape = (3,) | dtype = bool
  Group /processing/ophys of movie 0/mean images of movie 0 (Images) Structural images of a scanning
  Dataset /processing/ophys of movie 0/mean images of movie 0/Alexa Fluor 594 in pipette (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Dataset /processing/ophys of movie 0/mean images of movie 0/XCaMPgf at 940nm (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Group /processing/ophys of movie 1 (ProcessingModule) Processing result of imaging
  Group /processing/ophys of movie 1/Fluorescence (Fluorescence) 
  Group /processing/ophys of movie 1/Fluorescence/NeuropilResponseSeries (RoiResponseSeries) average fluorescence of the neuropil surrounding the roi
  Dataset /processing/ophys of movie 1/Fluorescence/NeuropilResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (4,) | dtype = int64
  Group /processing/ophys of movie 1/Fluorescence/RoiResponseSeries (RoiResponseSeries) weighted average fluorescence of roi
  Dataset /processing/ophys of movie 1/Fluorescence/RoiResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (4,) | dtype = int64
  Group /processing/ophys of movie 1/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation (PlaneSegmentation) output from segmenting with Suite2p, ROI 0 is the neuron recorded with electrophysiology
  Dataset /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation/cell_type (VectorData) pyr for putative pyramidal cells, int for putative interneurons, based on average loose-seal spike shape | shape = (5,) | dtype = object
  Dataset /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation/id (ElementIdentifiers)  | shape = (5,) | dtype = int64
  Dataset /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (5, 512, 128) | dtype = float64
  Group /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation/imaging_plane/device (Device) 
  Group /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation/imaging_plane/green (OpticalChannel) 
  Dataset /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation/neuropil_mask (VectorData) mask of neuropil surrounding this roi | shape = (5, 512, 128) | dtype = bool
  Dataset /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation/recorded_with_ephys (VectorData) whether this ROI is simultaneously loose-seal recorded | shape = (5,) | dtype = bool
  Group /processing/ophys of movie 1/mean images of movie 1 (Images) Structural images of a scanning
  Dataset /processing/ophys of movie 1/mean images of movie 1/Alexa Fluor 594 in pipette (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Dataset /processing/ophys of movie 1/mean images of movie 1/XCaMPgf at 940nm (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Group /processing/ophys of movie 2 (ProcessingModule) Processing result of imaging
  Group /processing/ophys of movie 2/Fluorescence (Fluorescence) 
  Group /processing/ophys of movie 2/Fluorescence/NeuropilResponseSeries (RoiResponseSeries) average fluorescence of the neuropil surrounding the roi
  Dataset /processing/ophys of movie 2/Fluorescence/NeuropilResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (3,) | dtype = int64
  Group /processing/ophys of movie 2/Fluorescence/RoiResponseSeries (RoiResponseSeries) weighted average fluorescence of roi
  Dataset /processing/ophys of movie 2/Fluorescence/RoiResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (3,) | dtype = int64
  Group /processing/ophys of movie 2/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation (PlaneSegmentation) output from segmenting with Suite2p, ROI 0 is the neuron recorded with electrophysiology
  Dataset /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation/cell_type (VectorData) pyr for putative pyramidal cells, int for putative interneurons, based on average loose-seal spike shape | shape = (4,) | dtype = object
  Dataset /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation/id (ElementIdentifiers)  | shape = (4,) | dtype = int64
  Dataset /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (4, 512, 128) | dtype = float64
  Group /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation/imaging_plane/device (Device) 
  Group /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation/imaging_plane/green (OpticalChannel) 
  Dataset /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation/neuropil_mask (VectorData) mask of neuropil surrounding this roi | shape = (4, 512, 128) | dtype = bool
  Dataset /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation/recorded_with_ephys (VectorData) whether this ROI is simultaneously loose-seal recorded | shape = (4,) | dtype = bool
  Group /processing/ophys of movie 2/mean images of movie 2 (Images) Structural images of a scanning
  Dataset /processing/ophys of movie 2/mean images of movie 2/Alexa Fluor 594 in pipette (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Dataset /processing/ophys of movie 2/mean images of movie 2/XCaMPgf at 940nm (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  session_description: 
  session_start_time: 2020-06-27T15:11:36-07:00
  timestamps_reference_time: 2020-06-27T15:11:36-07:00


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Registered movie 0 (TwoPhotonSeries) no description
  Group /acquisition/Registered movie 0/imaging_plane (ImagingPlane) 
  Group /acquisition/Registered movie 0/imaging_plane/device (Device) 
  Group /acquisition/Registered movie 0/imaging_plane/green (OpticalChannel) 
  Group /acquisition/Registered movie 1 (TwoPhotonSeries) no description
  Group /acquisition/Registered movie 1/imaging_plane (ImagingPlane) 
  Group /acquisition/Registered movie 1/imaging_plane/device (Device) 
  Group /acquisition/Registered movie 1/imaging_plane/green (OpticalChannel) 
  Group /acquisition/Registered movie 2 (TwoPhotonSeries) no description
  Group /acquisition/Registered movie 2/imaging_plane (ImagingPlane) 
  Group /acquisition/Registered movie 2/imaging_plane/device (Device) 
  Group /acquisition/Registered movie 2/imaging_plane/green (OpticalChannel) 
  Group /acquisition/Registered movie 3 (TwoPhotonSeries) no description
  Group /acquisition/Registered movie 3/imaging_plane (ImagingPlane) 
  Group /acquisition/Registered movie 3/imaging_plane/device (Device) 
  Group /acquisition/Registered movie 3/imaging_plane/green (OpticalChannel) 
  Group /acquisition/loose seal recording for movie 0 (CurrentClampSeries) no description
  Group /acquisition/loose seal recording for movie 0/electrode (IntracellularElectrode) 
  Group /acquisition/loose seal recording for movie 0/electrode/device (Device) Multiclamp 700B with 20 kHz low-pass filter
  Group /acquisition/loose seal recording for movie 1 (CurrentClampSeries) no description
  Group /acquisition/loose seal recording for movie 1/electrode (IntracellularElectrode) 
  Group /acquisition/loose seal recording for movie 1/electrode/device (Device) Multiclamp 700B with 20 kHz low-pass filter
  Group /acquisition/loose seal recording for movie 2 (CurrentClampSeries) no description
  Group /acquisition/loose seal recording for movie 2/electrode (IntracellularElectrode) 
  Group /acquisition/loose seal recording for movie 2/electrode/device (Device) Multiclamp 700B with 20 kHz low-pass filter
  Group /acquisition/loose seal recording for movie 3 (CurrentClampSeries) no description
  Group /acquisition/loose seal recording for movie 3/electrode (IntracellularElectrode) 
  Group /acquisition/loose seal recording for movie 3/electrode/device (Device) Multiclamp 700B with 20 kHz low-pass filter
  Group /acquisition/loose seal stimulus for movie 0 (CurrentClampStimulusSeries) no description
  Group /acquisition/loose seal stimulus for movie 0/electrode (IntracellularElectrode) 
  Group /acquisition/loose seal stimulus for movie 0/electrode/device (Device) Multiclamp 700B with 20 kHz low-pass filter
  Group /acquisition/loose seal stimulus for movie 1 (CurrentClampStimulusSeries) no description
  Group /acquisition/loose seal stimulus for movie 1/electrode (IntracellularElectrode) 
  Group /acquisition/loose seal stimulus for movie 1/electrode/device (Device) Multiclamp 700B with 20 kHz low-pass filter
  Group /acquisition/loose seal stimulus for movie 2 (CurrentClampStimulusSeries) no description
  Group /acquisition/loose seal stimulus for movie 2/electrode (IntracellularElectrode) 
  Group /acquisition/loose seal stimulus for movie 2/electrode/device (Device) Multiclamp 700B with 20 kHz low-pass filter
  Group /acquisition/loose seal stimulus for movie 3 (CurrentClampStimulusSeries) no description
  Group /acquisition/loose seal stimulus for movie 3/electrode (IntracellularElectrode) 
  Group /acquisition/loose seal stimulus for movie 3/electrode/device (Device) Multiclamp 700B with 20 kHz low-pass filter
  Group /analysis/responses (IntracellularResponsesTable) Table for storing intracellular response related metadata.
  Dataset /analysis/responses/ap_snr (VectorData) signal to noise ratio of detected loose-seal action potential | shape = (10106,) | dtype = float64
  Dataset /analysis/responses/ap_time (VectorData) peak time of detected loose-seal action potential | shape = (10106,) | dtype = float64
  Dataset /analysis/responses/id (ElementIdentifiers)  | shape = (10106,) | dtype = int64
  Dataset /analysis/responses/response (TimeSeriesReferenceVectorData) Column storing the reference to the recorded response for the recording (rows) | shape = (10106,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  file_create_date: ['2022-01-19T02:22:53.977828-08:00']
  Group /general/devices/MMIMS: custom-built two-photon microscope with a resonant scanner (Device) 
  Group /general/devices/Multiclamp 700B (Device) Multiclamp 700B with 20 kHz low-pass filter
  experiment_description: Simultaneous loose-seal cell-attached recordings and two-photon imaging of GCaMP (jGCaMP8s/m/f, jGCaMP7f, XCaMPgf) expressing mouse visual cortex neurons (pyramidal cells and FS interneurons) with drifting gratings visual stimuli
  experimenter: ['Marton Rozsa']
  institution: GENIE project, HHMI Janelia Research Campus
  Group /general/intracellular_ephys/Micropipette (IntracellularElectrode) 
  Group /general/intracellular_ephys/Micropipette/device (Device) Multiclamp 700B with 20 kHz low-pass filter
  Group /general/intracellular_ephys/sweep_table (SweepTable) A sweep table groups different PatchClampSeries together.
  Dataset /general/intracellular_ephys/sweep_table/id (ElementIdentifiers)  | shape = (8,) | dtype = int64
  Dataset /general/intracellular_ephys/sweep_table/series (VectorData) PatchClampSeries with the same sweep number | shape = (8,) | dtype = object
  Dataset /general/intracellular_ephys/sweep_table/series_index (VectorIndex) Index for VectorData 'series' | shape = (8,) | dtype = uint8
  Dataset /general/intracellular_ephys/sweep_table/sweep_number (VectorData) Sweep number of the entries in that row | shape = (8,) | dtype = uint64
  keywords: ['V1' 'calcium' 'spike' 'action potential' '2-photon' 'parvalbumin'
   'layer 2' 'AAV' 'adeno-associated virus']
  lab: Lab of Karel Svoboda at HHMI Janelia Research Campus
  Group /general/optophysiology/Movie_0 (ImagingPlane) 
  Group /general/optophysiology/Movie_0/device (Device) 
  Group /general/optophysiology/Movie_0/green (OpticalChannel) 
  Group /general/optophysiology/Movie_1 (ImagingPlane) 
  Group /general/optophysiology/Movie_1/device (Device) 
  Group /general/optophysiology/Movie_1/green (OpticalChannel) 
  Group /general/optophysiology/Movie_2 (ImagingPlane) 
  Group /general/optophysiology/Movie_2/device (Device) 
  Group /general/optophysiology/Movie_2/green (OpticalChannel) 
  Group /general/optophysiology/Movie_3 (ImagingPlane) 
  Group /general/optophysiology/Movie_3/device (Device) 
  Group /general/optophysiology/Movie_3/green (OpticalChannel) 
  related_publications: ['10.25378/janelia.13148243' '10.1101/2021.11.08.467793']
  session_id: XCaMPgf_ANM478343_cell02
  Group /general/subject (Subject) 
  surgery: [{"surgery_id": "1", "start_time": "2020-06-05 16:20:00", "end_time": "2020-06-05 17:45:00", "surgery_description": "headbar, craniotomy, virus injection, window:-: comments: nan"}, {"surgery_id": "2", "start_time": "2020-06-27 12:00:00", "end_time": "2020-06-27 12:55:00", "surgery_description": "window removal:-: comments: fine"}]
  virus: [{"surgery_id": "1", "injection_id": "1", "virus_id": "10245", "skull_reference": "Lambda", "ml_location": "2200.000", "ap_location": "250.000", "dv_location": "300.000", "volume": "35.000", "dilution": "8.00", "description": "virus injection: blood during injection 1 and 3", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-NES-XCaMP-Gf-WPRE.538.1", "titer": "35400000000000.0", "order_date": "2019-08-22", "remarks": "XCaMP-Gf ref:1-862-1"}, {"surgery_id": "1", "injection_id": "2", "virus_id": "10245", "skull_reference": "Lambda", "ml_location": "2800.000", "ap_location": "200.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: blood during injection 1 and 3", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-NES-XCaMP-Gf-WPRE.538.1", "titer": "35400000000000.0", "order_date": "2019-08-22", "remarks": "XCaMP-Gf ref:1-862-1"}, {"surgery_id": "1", "injection_id": "3", "virus_id": "10245", "skull_reference": "Lambda", "ml_location": "2800.000", "ap_location": "800.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: blood during injection 1 and 3", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-NES-XCaMP-Gf-WPRE.538.1", "titer": "35400000000000.0", "order_date": "2019-08-22", "remarks": "XCaMP-Gf ref:1-862-1"}, {"surgery_id": "1", "injection_id": "4", "virus_id": "10245", "skull_reference": "Lambda", "ml_location": "2200.000", "ap_location": "900.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: blood during injection 1 and 3", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-NES-XCaMP-Gf-WPRE.538.1", "titer": "35400000000000.0", "order_date": "2019-08-22", "remarks": "XCaMP-Gf ref:1-862-1"}, {"surgery_id": "1", "injection_id": "5", "virus_id": "10245", "skull_reference": "Lambda", "ml_location": "2200.000", "ap_location": "250.000", "dv_location": "300.000", "volume": "35.000", "dilution": "8.00", "description": "virus injection: blood during injection 1 and 3", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-NES-XCaMP-Gf-WPRE.538.1", "titer": "35400000000000.0", "order_date": "2019-08-22", "remarks": "XCaMP-Gf ref:1-862-1"}, {"surgery_id": "1", "injection_id": "6", "virus_id": "10245", "skull_reference": "Lambda", "ml_location": "2800.000", "ap_location": "200.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: blood during injection 1 and 3", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-NES-XCaMP-Gf-WPRE.538.1", "titer": "35400000000000.0", "order_date": "2019-08-22", "remarks": "XCaMP-Gf ref:1-862-1"}, {"surgery_id": "1", "injection_id": "7", "virus_id": "10245", "skull_reference": "Lambda", "ml_location": "2800.000", "ap_location": "800.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: blood during injection 1 and 3", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-NES-XCaMP-Gf-WPRE.538.1", "titer": "35400000000000.0", "order_date": "2019-08-22", "remarks": "XCaMP-Gf ref:1-862-1"}, {"surgery_id": "1", "injection_id": "8", "virus_id": "10245", "skull_reference": "Lambda", "ml_location": "2200.000", "ap_location": "900.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: blood during injection 1 and 3", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-NES-XCaMP-Gf-WPRE.538.1", "titer": "35400000000000.0", "order_date": "2019-08-22", "remarks": "XCaMP-Gf ref:1-862-1"}, {"surgery_id": "1", "injection_id": "9", "virus_id": "10245", "skull_reference": "Lambda", "ml_location": "2200.000", "ap_location": "250.000", "dv_location": "300.000", "volume": "35.000", "dilution": "8.00", "description": "virus injection: blood during injection 1 and 3", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-NES-XCaMP-Gf-WPRE.538.1", "titer": "35400000000000.0", "order_date": "2019-08-22", "remarks": "XCaMP-Gf ref:1-862-1"}, {"surgery_id": "1", "injection_id": "10", "virus_id": "10245", "skull_reference": "Lambda", "ml_location": "2800.000", "ap_location": "200.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: blood during injection 1 and 3", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-NES-XCaMP-Gf-WPRE.538.1", "titer": "35400000000000.0", "order_date": "2019-08-22", "remarks": "XCaMP-Gf ref:1-862-1"}, {"surgery_id": "1", "injection_id": "11", "virus_id": "10245", "skull_reference": "Lambda", "ml_location": "2800.000", "ap_location": "800.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: blood during injection 1 and 3", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-NES-XCaMP-Gf-WPRE.538.1", "titer": "35400000000000.0", "order_date": "2019-08-22", "remarks": "XCaMP-Gf ref:1-862-1"}, {"surgery_id": "1", "injection_id": "12", "virus_id": "10245", "skull_reference": "Lambda", "ml_location": "2200.000", "ap_location": "900.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: blood during injection 1 and 3", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-NES-XCaMP-Gf-WPRE.538.1", "titer": "35400000000000.0", "order_date": "2019-08-22", "remarks": "XCaMP-Gf ref:1-862-1"}]
  identifier: XCaMPgf_ANM478343_cell02
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (4,) | dtype = int64
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (4,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (4,) | dtype = float64
  Dataset /intervals/epochs/timeseries (VectorData) index into a TimeSeries object | shape = (16,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/epochs/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (4,) | dtype = uint8
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/amplitude (VectorData) amplitude of drifting grating stimulus | shape = (160,) | dtype = float64
  Dataset /intervals/trials/angle (VectorData) angle of drifting grating stimulus in degrees | shape = (160,) | dtype = int64
  Dataset /intervals/trials/cycles_per_degree (VectorData) cycles per degree of drifting grating stimulus | shape = (160,) | dtype = float64
  Dataset /intervals/trials/cycles_per_second (VectorData) cycles per second of drifting grating stimulus | shape = (160,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (160,) | dtype = int64
  Dataset /intervals/trials/movie_number (VectorData) during which movie this visual stimulus happened | shape = (160,) | dtype = int64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (160,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (160,) | dtype = float64
  Group /processing/ophys of movie 0 (ProcessingModule) Processing result of imaging
  Group /processing/ophys of movie 0/Fluorescence (Fluorescence) 
  Group /processing/ophys of movie 0/Fluorescence/NeuropilResponseSeries (RoiResponseSeries) average fluorescence of the neuropil surrounding the roi
  Dataset /processing/ophys of movie 0/Fluorescence/NeuropilResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (4,) | dtype = int64
  Group /processing/ophys of movie 0/Fluorescence/RoiResponseSeries (RoiResponseSeries) weighted average fluorescence of roi
  Dataset /processing/ophys of movie 0/Fluorescence/RoiResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (4,) | dtype = int64
  Group /processing/ophys of movie 0/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation (PlaneSegmentation) output from segmenting with Suite2p, ROI 0 is the neuron recorded with electrophysiology
  Dataset /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/cell_type (VectorData) pyr for putative pyramidal cells, int for putative interneurons, based on average loose-seal spike shape | shape = (5,) | dtype = object
  Dataset /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/id (ElementIdentifiers)  | shape = (5,) | dtype = int64
  Dataset /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (5, 512, 128) | dtype = float64
  Group /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/imaging_plane/device (Device) 
  Group /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/imaging_plane/green (OpticalChannel) 
  Dataset /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/neuropil_mask (VectorData) mask of neuropil surrounding this roi | shape = (5, 512, 128) | dtype = bool
  Dataset /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/recorded_with_ephys (VectorData) whether this ROI is simultaneously loose-seal recorded | shape = (5,) | dtype = bool
  Group /processing/ophys of movie 0/mean images of movie 0 (Images) Structural images of a scanning
  Dataset /processing/ophys of movie 0/mean images of movie 0/Alexa Fluor 594 in pipette (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Dataset /processing/ophys of movie 0/mean images of movie 0/XCaMPgf at 940nm (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Group /processing/ophys of movie 1 (ProcessingModule) Processing result of imaging
  Group /processing/ophys of movie 1/Fluorescence (Fluorescence) 
  Group /processing/ophys of movie 1/Fluorescence/NeuropilResponseSeries (RoiResponseSeries) average fluorescence of the neuropil surrounding the roi
  Dataset /processing/ophys of movie 1/Fluorescence/NeuropilResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (6,) | dtype = int64
  Group /processing/ophys of movie 1/Fluorescence/RoiResponseSeries (RoiResponseSeries) weighted average fluorescence of roi
  Dataset /processing/ophys of movie 1/Fluorescence/RoiResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (6,) | dtype = int64
  Group /processing/ophys of movie 1/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation (PlaneSegmentation) output from segmenting with Suite2p, ROI 0 is the neuron recorded with electrophysiology
  Dataset /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation/cell_type (VectorData) pyr for putative pyramidal cells, int for putative interneurons, based on average loose-seal spike shape | shape = (7,) | dtype = object
  Dataset /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation/id (ElementIdentifiers)  | shape = (7,) | dtype = int64
  Dataset /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (7, 512, 128) | dtype = float64
  Group /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation/imaging_plane/device (Device) 
  Group /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation/imaging_plane/green (OpticalChannel) 
  Dataset /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation/neuropil_mask (VectorData) mask of neuropil surrounding this roi | shape = (7, 512, 128) | dtype = bool
  Dataset /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation/recorded_with_ephys (VectorData) whether this ROI is simultaneously loose-seal recorded | shape = (7,) | dtype = bool
  Group /processing/ophys of movie 1/mean images of movie 1 (Images) Structural images of a scanning
  Dataset /processing/ophys of movie 1/mean images of movie 1/Alexa Fluor 594 in pipette (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Dataset /processing/ophys of movie 1/mean images of movie 1/XCaMPgf at 940nm (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Group /processing/ophys of movie 2 (ProcessingModule) Processing result of imaging
  Group /processing/ophys of movie 2/Fluorescence (Fluorescence) 
  Group /processing/ophys of movie 2/Fluorescence/NeuropilResponseSeries (RoiResponseSeries) average fluorescence of the neuropil surrounding the roi
  Dataset /processing/ophys of movie 2/Fluorescence/NeuropilResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (8,) | dtype = int64
  Group /processing/ophys of movie 2/Fluorescence/RoiResponseSeries (RoiResponseSeries) weighted average fluorescence of roi
  Dataset /processing/ophys of movie 2/Fluorescence/RoiResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (8,) | dtype = int64
  Group /processing/ophys of movie 2/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation (PlaneSegmentation) output from segmenting with Suite2p, ROI 0 is the neuron recorded with electrophysiology
  Dataset /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation/cell_type (VectorData) pyr for putative pyramidal cells, int for putative interneurons, based on average loose-seal spike shape | shape = (9,) | dtype = object
  Dataset /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation/id (ElementIdentifiers)  | shape = (9,) | dtype = int64
  Dataset /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (9, 512, 128) | dtype = float64
  Group /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation/imaging_plane/device (Device) 
  Group /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation/imaging_plane/green (OpticalChannel) 
  Dataset /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation/neuropil_mask (VectorData) mask of neuropil surrounding this roi | shape = (9, 512, 128) | dtype = bool
  Dataset /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation/recorded_with_ephys (VectorData) whether this ROI is simultaneously loose-seal recorded | shape = (9,) | dtype = bool
  Group /processing/ophys of movie 2/mean images of movie 2 (Images) Structural images of a scanning
  Dataset /processing/ophys of movie 2/mean images of movie 2/Alexa Fluor 594 in pipette (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Dataset /processing/ophys of movie 2/mean images of movie 2/XCaMPgf at 940nm (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Group /processing/ophys of movie 3 (ProcessingModule) Processing result of imaging
  Group /processing/ophys of movie 3/Fluorescence (Fluorescence) 
  Group /processing/ophys of movie 3/Fluorescence/NeuropilResponseSeries (RoiResponseSeries) average fluorescence of the neuropil surrounding the roi
  Dataset /processing/ophys of movie 3/Fluorescence/NeuropilResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (6,) | dtype = int64
  Group /processing/ophys of movie 3/Fluorescence/RoiResponseSeries (RoiResponseSeries) weighted average fluorescence of roi
  Dataset /processing/ophys of movie 3/Fluorescence/RoiResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (6,) | dtype = int64
  Group /processing/ophys of movie 3/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys of movie 3/ImageSegmentation/MovieSegmentation (PlaneSegmentation) output from segmenting with Suite2p, ROI 0 is the neuron recorded with electrophysiology
  Dataset /processing/ophys of movie 3/ImageSegmentation/MovieSegmentation/cell_type (VectorData) pyr for putative pyramidal cells, int for putative interneurons, based on average loose-seal spike shape | shape = (7,) | dtype = object
  Dataset /processing/ophys of movie 3/ImageSegmentation/MovieSegmentation/id (ElementIdentifiers)  | shape = (7,) | dtype = int64
  Dataset /processing/ophys of movie 3/ImageSegmentation/MovieSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (7, 512, 128) | dtype = float64
  Group /processing/ophys of movie 3/ImageSegmentation/MovieSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys of movie 3/ImageSegmentation/MovieSegmentation/imaging_plane/device (Device) 
  Group /processing/ophys of movie 3/ImageSegmentation/MovieSegmentation/imaging_plane/green (OpticalChannel) 
  Dataset /processing/ophys of movie 3/ImageSegmentation/MovieSegmentation/neuropil_mask (VectorData) mask of neuropil surrounding this roi | shape = (7, 512, 128) | dtype = bool
  Dataset /processing/ophys of movie 3/ImageSegmentation/MovieSegmentation/recorded_with_ephys (VectorData) whether this ROI is simultaneously loose-seal recorded | shape = (7,) | dtype = bool
  Group /processing/ophys of movie 3/mean images of movie 3 (Images) Structural images of a scanning
  Dataset /processing/ophys of movie 3/mean images of movie 3/Alexa Fluor 594 in pipette (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Dataset /processing/ophys of movie 3/mean images of movie 3/XCaMPgf at 940nm (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  session_description: 
  session_start_time: 2020-06-27T15:48:07-07:00
  timestamps_reference_time: 2020-06-27T15:48:07-07:00


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Registered movie 0 (TwoPhotonSeries) no description
  Group /acquisition/Registered movie 0/imaging_plane (ImagingPlane) 
  Group /acquisition/Registered movie 0/imaging_plane/device (Device) 
  Group /acquisition/Registered movie 0/imaging_plane/green (OpticalChannel) 
  Group /acquisition/Registered movie 1 (TwoPhotonSeries) no description
  Group /acquisition/Registered movie 1/imaging_plane (ImagingPlane) 
  Group /acquisition/Registered movie 1/imaging_plane/device (Device) 
  Group /acquisition/Registered movie 1/imaging_plane/green (OpticalChannel) 
  Group /acquisition/Registered movie 2 (TwoPhotonSeries) no description
  Group /acquisition/Registered movie 2/imaging_plane (ImagingPlane) 
  Group /acquisition/Registered movie 2/imaging_plane/device (Device) 
  Group /acquisition/Registered movie 2/imaging_plane/green (OpticalChannel) 
  Group /acquisition/loose seal recording for movie 0 (VoltageClampSeries) no description
  Group /acquisition/loose seal recording for movie 0/electrode (IntracellularElectrode) 
  Group /acquisition/loose seal recording for movie 0/electrode/device (Device) Multiclamp 700B with 20 kHz low-pass filter
  Group /acquisition/loose seal recording for movie 1 (VoltageClampSeries) no description
  Group /acquisition/loose seal recording for movie 1/electrode (IntracellularElectrode) 
  Group /acquisition/loose seal recording for movie 1/electrode/device (Device) Multiclamp 700B with 20 kHz low-pass filter
  Group /acquisition/loose seal recording for movie 2 (VoltageClampSeries) no description
  Group /acquisition/loose seal recording for movie 2/electrode (IntracellularElectrode) 
  Group /acquisition/loose seal recording for movie 2/electrode/device (Device) Multiclamp 700B with 20 kHz low-pass filter
  Group /acquisition/loose seal stimulus for movie 0 (VoltageClampStimulusSeries) no description
  Group /acquisition/loose seal stimulus for movie 0/electrode (IntracellularElectrode) 
  Group /acquisition/loose seal stimulus for movie 0/electrode/device (Device) Multiclamp 700B with 20 kHz low-pass filter
  Group /acquisition/loose seal stimulus for movie 1 (VoltageClampStimulusSeries) no description
  Group /acquisition/loose seal stimulus for movie 1/electrode (IntracellularElectrode) 
  Group /acquisition/loose seal stimulus for movie 1/electrode/device (Device) Multiclamp 700B with 20 kHz low-pass filter
  Group /acquisition/loose seal stimulus for movie 2 (VoltageClampStimulusSeries) no description
  Group /acquisition/loose seal stimulus for movie 2/electrode (IntracellularElectrode) 
  Group /acquisition/loose seal stimulus for movie 2/electrode/device (Device) Multiclamp 700B with 20 kHz low-pass filter
  Group /analysis/responses (IntracellularResponsesTable) Table for storing intracellular response related metadata.
  Dataset /analysis/responses/ap_snr (VectorData) signal to noise ratio of detected loose-seal action potential | shape = (645,) | dtype = float64
  Dataset /analysis/responses/ap_time (VectorData) peak time of detected loose-seal action potential | shape = (645,) | dtype = float64
  Dataset /analysis/responses/id (ElementIdentifiers)  | shape = (645,) | dtype = int64
  Dataset /analysis/responses/response (TimeSeriesReferenceVectorData) Column storing the reference to the recorded response for the recording (rows) | shape = (645,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  file_create_date: ['2022-01-19T02:31:58.876822-08:00']
  Group /general/devices/MMIMS: custom-built two-photon microscope with a resonant scanner (Device) 
  Group /general/devices/Multiclamp 700B (Device) Multiclamp 700B with 20 kHz low-pass filter
  experiment_description: Simultaneous loose-seal cell-attached recordings and two-photon imaging of GCaMP (jGCaMP8s/m/f, jGCaMP7f, XCaMPgf) expressing mouse visual cortex neurons (pyramidal cells and FS interneurons) with drifting gratings visual stimuli
  experimenter: ['Marton Rozsa']
  institution: GENIE project, HHMI Janelia Research Campus
  Group /general/intracellular_ephys/Micropipette (IntracellularElectrode) 
  Group /general/intracellular_ephys/Micropipette/device (Device) Multiclamp 700B with 20 kHz low-pass filter
  Group /general/intracellular_ephys/sweep_table (SweepTable) A sweep table groups different PatchClampSeries together.
  Dataset /general/intracellular_ephys/sweep_table/id (ElementIdentifiers)  | shape = (6,) | dtype = int64
  Dataset /general/intracellular_ephys/sweep_table/series (VectorData) PatchClampSeries with the same sweep number | shape = (6,) | dtype = object
  Dataset /general/intracellular_ephys/sweep_table/series_index (VectorIndex) Index for VectorData 'series' | shape = (6,) | dtype = uint8
  Dataset /general/intracellular_ephys/sweep_table/sweep_number (VectorData) Sweep number of the entries in that row | shape = (6,) | dtype = uint64
  keywords: ['V1' 'calcium' 'spike' 'action potential' '2-photon' 'parvalbumin'
   'layer 2' 'AAV' 'adeno-associated virus']
  lab: Lab of Karel Svoboda at HHMI Janelia Research Campus
  Group /general/optophysiology/Movie_0 (ImagingPlane) 
  Group /general/optophysiology/Movie_0/device (Device) 
  Group /general/optophysiology/Movie_0/green (OpticalChannel) 
  Group /general/optophysiology/Movie_1 (ImagingPlane) 
  Group /general/optophysiology/Movie_1/device (Device) 
  Group /general/optophysiology/Movie_1/green (OpticalChannel) 
  Group /general/optophysiology/Movie_2 (ImagingPlane) 
  Group /general/optophysiology/Movie_2/device (Device) 
  Group /general/optophysiology/Movie_2/green (OpticalChannel) 
  related_publications: ['10.25378/janelia.13148243' '10.1101/2021.11.08.467793']
  session_id: XCaMPgf_ANM478343_cell03
  Group /general/subject (Subject) 
  surgery: [{"surgery_id": "1", "start_time": "2020-06-05 16:20:00", "end_time": "2020-06-05 17:45:00", "surgery_description": "headbar, craniotomy, virus injection, window:-: comments: nan"}, {"surgery_id": "2", "start_time": "2020-06-27 12:00:00", "end_time": "2020-06-27 12:55:00", "surgery_description": "window removal:-: comments: fine"}]
  virus: [{"surgery_id": "1", "injection_id": "1", "virus_id": "10245", "skull_reference": "Lambda", "ml_location": "2200.000", "ap_location": "250.000", "dv_location": "300.000", "volume": "35.000", "dilution": "8.00", "description": "virus injection: blood during injection 1 and 3", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-NES-XCaMP-Gf-WPRE.538.1", "titer": "35400000000000.0", "order_date": "2019-08-22", "remarks": "XCaMP-Gf ref:1-862-1"}, {"surgery_id": "1", "injection_id": "2", "virus_id": "10245", "skull_reference": "Lambda", "ml_location": "2800.000", "ap_location": "200.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: blood during injection 1 and 3", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-NES-XCaMP-Gf-WPRE.538.1", "titer": "35400000000000.0", "order_date": "2019-08-22", "remarks": "XCaMP-Gf ref:1-862-1"}, {"surgery_id": "1", "injection_id": "3", "virus_id": "10245", "skull_reference": "Lambda", "ml_location": "2800.000", "ap_location": "800.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: blood during injection 1 and 3", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-NES-XCaMP-Gf-WPRE.538.1", "titer": "35400000000000.0", "order_date": "2019-08-22", "remarks": "XCaMP-Gf ref:1-862-1"}, {"surgery_id": "1", "injection_id": "4", "virus_id": "10245", "skull_reference": "Lambda", "ml_location": "2200.000", "ap_location": "900.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: blood during injection 1 and 3", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-NES-XCaMP-Gf-WPRE.538.1", "titer": "35400000000000.0", "order_date": "2019-08-22", "remarks": "XCaMP-Gf ref:1-862-1"}, {"surgery_id": "1", "injection_id": "5", "virus_id": "10245", "skull_reference": "Lambda", "ml_location": "2200.000", "ap_location": "250.000", "dv_location": "300.000", "volume": "35.000", "dilution": "8.00", "description": "virus injection: blood during injection 1 and 3", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-NES-XCaMP-Gf-WPRE.538.1", "titer": "35400000000000.0", "order_date": "2019-08-22", "remarks": "XCaMP-Gf ref:1-862-1"}, {"surgery_id": "1", "injection_id": "6", "virus_id": "10245", "skull_reference": "Lambda", "ml_location": "2800.000", "ap_location": "200.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: blood during injection 1 and 3", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-NES-XCaMP-Gf-WPRE.538.1", "titer": "35400000000000.0", "order_date": "2019-08-22", "remarks": "XCaMP-Gf ref:1-862-1"}, {"surgery_id": "1", "injection_id": "7", "virus_id": "10245", "skull_reference": "Lambda", "ml_location": "2800.000", "ap_location": "800.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: blood during injection 1 and 3", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-NES-XCaMP-Gf-WPRE.538.1", "titer": "35400000000000.0", "order_date": "2019-08-22", "remarks": "XCaMP-Gf ref:1-862-1"}, {"surgery_id": "1", "injection_id": "8", "virus_id": "10245", "skull_reference": "Lambda", "ml_location": "2200.000", "ap_location": "900.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: blood during injection 1 and 3", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-NES-XCaMP-Gf-WPRE.538.1", "titer": "35400000000000.0", "order_date": "2019-08-22", "remarks": "XCaMP-Gf ref:1-862-1"}, {"surgery_id": "1", "injection_id": "9", "virus_id": "10245", "skull_reference": "Lambda", "ml_location": "2200.000", "ap_location": "250.000", "dv_location": "300.000", "volume": "35.000", "dilution": "8.00", "description": "virus injection: blood during injection 1 and 3", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-NES-XCaMP-Gf-WPRE.538.1", "titer": "35400000000000.0", "order_date": "2019-08-22", "remarks": "XCaMP-Gf ref:1-862-1"}, {"surgery_id": "1", "injection_id": "10", "virus_id": "10245", "skull_reference": "Lambda", "ml_location": "2800.000", "ap_location": "200.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: blood during injection 1 and 3", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-NES-XCaMP-Gf-WPRE.538.1", "titer": "35400000000000.0", "order_date": "2019-08-22", "remarks": "XCaMP-Gf ref:1-862-1"}, {"surgery_id": "1", "injection_id": "11", "virus_id": "10245", "skull_reference": "Lambda", "ml_location": "2800.000", "ap_location": "800.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: blood during injection 1 and 3", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-NES-XCaMP-Gf-WPRE.538.1", "titer": "35400000000000.0", "order_date": "2019-08-22", "remarks": "XCaMP-Gf ref:1-862-1"}, {"surgery_id": "1", "injection_id": "12", "virus_id": "10245", "skull_reference": "Lambda", "ml_location": "2200.000", "ap_location": "900.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: blood during injection 1 and 3", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-NES-XCaMP-Gf-WPRE.538.1", "titer": "35400000000000.0", "order_date": "2019-08-22", "remarks": "XCaMP-Gf ref:1-862-1"}]
  identifier: XCaMPgf_ANM478343_cell03
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (3,) | dtype = int64
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (3,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (3,) | dtype = float64
  Dataset /intervals/epochs/timeseries (VectorData) index into a TimeSeries object | shape = (12,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/epochs/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (3,) | dtype = uint8
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/amplitude (VectorData) amplitude of drifting grating stimulus | shape = (120,) | dtype = float64
  Dataset /intervals/trials/angle (VectorData) angle of drifting grating stimulus in degrees | shape = (120,) | dtype = int64
  Dataset /intervals/trials/cycles_per_degree (VectorData) cycles per degree of drifting grating stimulus | shape = (120,) | dtype = float64
  Dataset /intervals/trials/cycles_per_second (VectorData) cycles per second of drifting grating stimulus | shape = (120,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (120,) | dtype = int64
  Dataset /intervals/trials/movie_number (VectorData) during which movie this visual stimulus happened | shape = (120,) | dtype = int64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (120,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (120,) | dtype = float64
  Group /processing/ophys of movie 0 (ProcessingModule) Processing result of imaging
  Group /processing/ophys of movie 0/Fluorescence (Fluorescence) 
  Group /processing/ophys of movie 0/Fluorescence/NeuropilResponseSeries (RoiResponseSeries) average fluorescence of the neuropil surrounding the roi
  Dataset /processing/ophys of movie 0/Fluorescence/NeuropilResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (1,) | dtype = int64
  Group /processing/ophys of movie 0/Fluorescence/RoiResponseSeries (RoiResponseSeries) weighted average fluorescence of roi
  Dataset /processing/ophys of movie 0/Fluorescence/RoiResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (1,) | dtype = int64
  Group /processing/ophys of movie 0/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation (PlaneSegmentation) output from segmenting with Suite2p, ROI 0 is the neuron recorded with electrophysiology
  Dataset /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/cell_type (VectorData) pyr for putative pyramidal cells, int for putative interneurons, based on average loose-seal spike shape | shape = (2,) | dtype = object
  Dataset /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/id (ElementIdentifiers)  | shape = (2,) | dtype = int64
  Dataset /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (2, 512, 128) | dtype = float64
  Group /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/imaging_plane/device (Device) 
  Group /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/imaging_plane/green (OpticalChannel) 
  Dataset /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/neuropil_mask (VectorData) mask of neuropil surrounding this roi | shape = (2, 512, 128) | dtype = bool
  Dataset /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/recorded_with_ephys (VectorData) whether this ROI is simultaneously loose-seal recorded | shape = (2,) | dtype = bool
  Group /processing/ophys of movie 0/mean images of movie 0 (Images) Structural images of a scanning
  Dataset /processing/ophys of movie 0/mean images of movie 0/Alexa Fluor 594 in pipette (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Dataset /processing/ophys of movie 0/mean images of movie 0/XCaMPgf at 940nm (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Group /processing/ophys of movie 1 (ProcessingModule) Processing result of imaging
  Group /processing/ophys of movie 1/Fluorescence (Fluorescence) 
  Group /processing/ophys of movie 1/Fluorescence/NeuropilResponseSeries (RoiResponseSeries) average fluorescence of the neuropil surrounding the roi
  Dataset /processing/ophys of movie 1/Fluorescence/NeuropilResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (1,) | dtype = int64
  Group /processing/ophys of movie 1/Fluorescence/RoiResponseSeries (RoiResponseSeries) weighted average fluorescence of roi
  Dataset /processing/ophys of movie 1/Fluorescence/RoiResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (1,) | dtype = int64
  Group /processing/ophys of movie 1/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation (PlaneSegmentation) output from segmenting with Suite2p, ROI 0 is the neuron recorded with electrophysiology
  Dataset /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation/cell_type (VectorData) pyr for putative pyramidal cells, int for putative interneurons, based on average loose-seal spike shape | shape = (2,) | dtype = object
  Dataset /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation/id (ElementIdentifiers)  | shape = (2,) | dtype = int64
  Dataset /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (2, 512, 128) | dtype = float64
  Group /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation/imaging_plane/device (Device) 
  Group /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation/imaging_plane/green (OpticalChannel) 
  Dataset /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation/neuropil_mask (VectorData) mask of neuropil surrounding this roi | shape = (2, 512, 128) | dtype = bool
  Dataset /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation/recorded_with_ephys (VectorData) whether this ROI is simultaneously loose-seal recorded | shape = (2,) | dtype = bool
  Group /processing/ophys of movie 1/mean images of movie 1 (Images) Structural images of a scanning
  Dataset /processing/ophys of movie 1/mean images of movie 1/Alexa Fluor 594 in pipette (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Dataset /processing/ophys of movie 1/mean images of movie 1/XCaMPgf at 940nm (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Group /processing/ophys of movie 2 (ProcessingModule) Processing result of imaging
  Group /processing/ophys of movie 2/Fluorescence (Fluorescence) 
  Group /processing/ophys of movie 2/Fluorescence/NeuropilResponseSeries (RoiResponseSeries) average fluorescence of the neuropil surrounding the roi
  Dataset /processing/ophys of movie 2/Fluorescence/NeuropilResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (2,) | dtype = int64
  Group /processing/ophys of movie 2/Fluorescence/RoiResponseSeries (RoiResponseSeries) weighted average fluorescence of roi
  Dataset /processing/ophys of movie 2/Fluorescence/RoiResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (2,) | dtype = int64
  Group /processing/ophys of movie 2/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation (PlaneSegmentation) output from segmenting with Suite2p, ROI 0 is the neuron recorded with electrophysiology
  Dataset /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation/cell_type (VectorData) pyr for putative pyramidal cells, int for putative interneurons, based on average loose-seal spike shape | shape = (3,) | dtype = object
  Dataset /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation/id (ElementIdentifiers)  | shape = (3,) | dtype = int64
  Dataset /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (3, 512, 128) | dtype = float64
  Group /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation/imaging_plane/device (Device) 
  Group /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation/imaging_plane/green (OpticalChannel) 
  Dataset /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation/neuropil_mask (VectorData) mask of neuropil surrounding this roi | shape = (3, 512, 128) | dtype = bool
  Dataset /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation/recorded_with_ephys (VectorData) whether this ROI is simultaneously loose-seal recorded | shape = (3,) | dtype = bool
  Group /processing/ophys of movie 2/mean images of movie 2 (Images) Structural images of a scanning
  Dataset /processing/ophys of movie 2/mean images of movie 2/Alexa Fluor 594 in pipette (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Dataset /processing/ophys of movie 2/mean images of movie 2/XCaMPgf at 940nm (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  session_description: 
  session_start_time: 2020-06-27T16:05:29-07:00
  timestamps_reference_time: 2020-06-27T16:05:29-07:00


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Registered movie 0 (TwoPhotonSeries) no description
  Group /acquisition/Registered movie 0/imaging_plane (ImagingPlane) 
  Group /acquisition/Registered movie 0/imaging_plane/device (Device) 
  Group /acquisition/Registered movie 0/imaging_plane/green (OpticalChannel) 
  Group /acquisition/loose seal recording for movie 0 (CurrentClampSeries) no description
  Group /acquisition/loose seal recording for movie 0/electrode (IntracellularElectrode) 
  Group /acquisition/loose seal recording for movie 0/electrode/device (Device) Multiclamp 700B with 20 kHz low-pass filter
  Group /acquisition/loose seal stimulus for movie 0 (CurrentClampStimulusSeries) no description
  Group /acquisition/loose seal stimulus for movie 0/electrode (IntracellularElectrode) 
  Group /acquisition/loose seal stimulus for movie 0/electrode/device (Device) Multiclamp 700B with 20 kHz low-pass filter
  Group /analysis/responses (IntracellularResponsesTable) Table for storing intracellular response related metadata.
  Dataset /analysis/responses/ap_snr (VectorData) signal to noise ratio of detected loose-seal action potential | shape = (42,) | dtype = float64
  Dataset /analysis/responses/ap_time (VectorData) peak time of detected loose-seal action potential | shape = (42,) | dtype = float64
  Dataset /analysis/responses/id (ElementIdentifiers)  | shape = (42,) | dtype = int64
  Dataset /analysis/responses/response (TimeSeriesReferenceVectorData) Column storing the reference to the recorded response for the recording (rows) | shape = (42,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  file_create_date: ['2022-01-19T02:39:08.285029-08:00']
  Group /general/devices/MMIMS: custom-built two-photon microscope with a resonant scanner (Device) 
  Group /general/devices/Multiclamp 700B (Device) Multiclamp 700B with 20 kHz low-pass filter
  experiment_description: Simultaneous loose-seal cell-attached recordings and two-photon imaging of GCaMP (jGCaMP8s/m/f, jGCaMP7f, XCaMPgf) expressing mouse visual cortex neurons (pyramidal cells and FS interneurons) with drifting gratings visual stimuli
  experimenter: ['Marton Rozsa']
  institution: GENIE project, HHMI Janelia Research Campus
  Group /general/intracellular_ephys/Micropipette (IntracellularElectrode) 
  Group /general/intracellular_ephys/Micropipette/device (Device) Multiclamp 700B with 20 kHz low-pass filter
  Group /general/intracellular_ephys/sweep_table (SweepTable) A sweep table groups different PatchClampSeries together.
  Dataset /general/intracellular_ephys/sweep_table/id (ElementIdentifiers)  | shape = (2,) | dtype = int64
  Dataset /general/intracellular_ephys/sweep_table/series (VectorData) PatchClampSeries with the same sweep number | shape = (2,) | dtype = object
  Dataset /general/intracellular_ephys/sweep_table/series_index (VectorIndex) Index for VectorData 'series' | shape = (2,) | dtype = uint8
  Dataset /general/intracellular_ephys/sweep_table/sweep_number (VectorData) Sweep number of the entries in that row | shape = (2,) | dtype = uint64
  keywords: ['V1' 'calcium' 'spike' 'action potential' '2-photon' 'parvalbumin'
   'layer 2' 'AAV' 'adeno-associated virus']
  lab: Lab of Karel Svoboda at HHMI Janelia Research Campus
  Group /general/optophysiology/Movie_0 (ImagingPlane) 
  Group /general/optophysiology/Movie_0/device (Device) 
  Group /general/optophysiology/Movie_0/green (OpticalChannel) 
  related_publications: ['10.25378/janelia.13148243' '10.1101/2021.11.08.467793']
  session_id: XCaMPgf_ANM478343_cell04
  Group /general/subject (Subject) 
  surgery: [{"surgery_id": "1", "start_time": "2020-06-05 16:20:00", "end_time": "2020-06-05 17:45:00", "surgery_description": "headbar, craniotomy, virus injection, window:-: comments: nan"}, {"surgery_id": "2", "start_time": "2020-06-27 12:00:00", "end_time": "2020-06-27 12:55:00", "surgery_description": "window removal:-: comments: fine"}]
  virus: [{"surgery_id": "1", "injection_id": "1", "virus_id": "10245", "skull_reference": "Lambda", "ml_location": "2200.000", "ap_location": "250.000", "dv_location": "300.000", "volume": "35.000", "dilution": "8.00", "description": "virus injection: blood during injection 1 and 3", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-NES-XCaMP-Gf-WPRE.538.1", "titer": "35400000000000.0", "order_date": "2019-08-22", "remarks": "XCaMP-Gf ref:1-862-1"}, {"surgery_id": "1", "injection_id": "2", "virus_id": "10245", "skull_reference": "Lambda", "ml_location": "2800.000", "ap_location": "200.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: blood during injection 1 and 3", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-NES-XCaMP-Gf-WPRE.538.1", "titer": "35400000000000.0", "order_date": "2019-08-22", "remarks": "XCaMP-Gf ref:1-862-1"}, {"surgery_id": "1", "injection_id": "3", "virus_id": "10245", "skull_reference": "Lambda", "ml_location": "2800.000", "ap_location": "800.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: blood during injection 1 and 3", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-NES-XCaMP-Gf-WPRE.538.1", "titer": "35400000000000.0", "order_date": "2019-08-22", "remarks": "XCaMP-Gf ref:1-862-1"}, {"surgery_id": "1", "injection_id": "4", "virus_id": "10245", "skull_reference": "Lambda", "ml_location": "2200.000", "ap_location": "900.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: blood during injection 1 and 3", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-NES-XCaMP-Gf-WPRE.538.1", "titer": "35400000000000.0", "order_date": "2019-08-22", "remarks": "XCaMP-Gf ref:1-862-1"}, {"surgery_id": "1", "injection_id": "5", "virus_id": "10245", "skull_reference": "Lambda", "ml_location": "2200.000", "ap_location": "250.000", "dv_location": "300.000", "volume": "35.000", "dilution": "8.00", "description": "virus injection: blood during injection 1 and 3", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-NES-XCaMP-Gf-WPRE.538.1", "titer": "35400000000000.0", "order_date": "2019-08-22", "remarks": "XCaMP-Gf ref:1-862-1"}, {"surgery_id": "1", "injection_id": "6", "virus_id": "10245", "skull_reference": "Lambda", "ml_location": "2800.000", "ap_location": "200.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: blood during injection 1 and 3", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-NES-XCaMP-Gf-WPRE.538.1", "titer": "35400000000000.0", "order_date": "2019-08-22", "remarks": "XCaMP-Gf ref:1-862-1"}, {"surgery_id": "1", "injection_id": "7", "virus_id": "10245", "skull_reference": "Lambda", "ml_location": "2800.000", "ap_location": "800.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: blood during injection 1 and 3", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-NES-XCaMP-Gf-WPRE.538.1", "titer": "35400000000000.0", "order_date": "2019-08-22", "remarks": "XCaMP-Gf ref:1-862-1"}, {"surgery_id": "1", "injection_id": "8", "virus_id": "10245", "skull_reference": "Lambda", "ml_location": "2200.000", "ap_location": "900.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: blood during injection 1 and 3", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-NES-XCaMP-Gf-WPRE.538.1", "titer": "35400000000000.0", "order_date": "2019-08-22", "remarks": "XCaMP-Gf ref:1-862-1"}, {"surgery_id": "1", "injection_id": "9", "virus_id": "10245", "skull_reference": "Lambda", "ml_location": "2200.000", "ap_location": "250.000", "dv_location": "300.000", "volume": "35.000", "dilution": "8.00", "description": "virus injection: blood during injection 1 and 3", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-NES-XCaMP-Gf-WPRE.538.1", "titer": "35400000000000.0", "order_date": "2019-08-22", "remarks": "XCaMP-Gf ref:1-862-1"}, {"surgery_id": "1", "injection_id": "10", "virus_id": "10245", "skull_reference": "Lambda", "ml_location": "2800.000", "ap_location": "200.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: blood during injection 1 and 3", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-NES-XCaMP-Gf-WPRE.538.1", "titer": "35400000000000.0", "order_date": "2019-08-22", "remarks": "XCaMP-Gf ref:1-862-1"}, {"surgery_id": "1", "injection_id": "11", "virus_id": "10245", "skull_reference": "Lambda", "ml_location": "2800.000", "ap_location": "800.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: blood during injection 1 and 3", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-NES-XCaMP-Gf-WPRE.538.1", "titer": "35400000000000.0", "order_date": "2019-08-22", "remarks": "XCaMP-Gf ref:1-862-1"}, {"surgery_id": "1", "injection_id": "12", "virus_id": "10245", "skull_reference": "Lambda", "ml_location": "2200.000", "ap_location": "900.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: blood during injection 1 and 3", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-NES-XCaMP-Gf-WPRE.538.1", "titer": "35400000000000.0", "order_date": "2019-08-22", "remarks": "XCaMP-Gf ref:1-862-1"}]
  identifier: XCaMPgf_ANM478343_cell04
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (1,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (1,) | dtype = float64
  Dataset /intervals/epochs/timeseries (VectorData) index into a TimeSeries object | shape = (4,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/epochs/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (1,) | dtype = uint8
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/amplitude (VectorData) amplitude of drifting grating stimulus | shape = (40,) | dtype = float64
  Dataset /intervals/trials/angle (VectorData) angle of drifting grating stimulus in degrees | shape = (40,) | dtype = int64
  Dataset /intervals/trials/cycles_per_degree (VectorData) cycles per degree of drifting grating stimulus | shape = (40,) | dtype = float64
  Dataset /intervals/trials/cycles_per_second (VectorData) cycles per second of drifting grating stimulus | shape = (40,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (40,) | dtype = int64
  Dataset /intervals/trials/movie_number (VectorData) during which movie this visual stimulus happened | shape = (40,) | dtype = int64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (40,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (40,) | dtype = float64
  Group /processing/ophys of movie 0 (ProcessingModule) Processing result of imaging
  Group /processing/ophys of movie 0/Fluorescence (Fluorescence) 
  Group /processing/ophys of movie 0/Fluorescence/NeuropilResponseSeries (RoiResponseSeries) average fluorescence of the neuropil surrounding the roi
  Dataset /processing/ophys of movie 0/Fluorescence/NeuropilResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (0,) | dtype = int32
  Group /processing/ophys of movie 0/Fluorescence/RoiResponseSeries (RoiResponseSeries) weighted average fluorescence of roi
  Dataset /processing/ophys of movie 0/Fluorescence/RoiResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (0,) | dtype = int32
  Group /processing/ophys of movie 0/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation (PlaneSegmentation) output from segmenting with Suite2p, ROI 0 is the neuron recorded with electrophysiology
  Dataset /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/cell_type (VectorData) pyr for putative pyramidal cells, int for putative interneurons, based on average loose-seal spike shape | shape = (1,) | dtype = object
  Dataset /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (1, 512, 128) | dtype = float64
  Group /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/imaging_plane/device (Device) 
  Group /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/imaging_plane/green (OpticalChannel) 
  Dataset /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/neuropil_mask (VectorData) mask of neuropil surrounding this roi | shape = (1, 512, 128) | dtype = bool
  Dataset /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/recorded_with_ephys (VectorData) whether this ROI is simultaneously loose-seal recorded | shape = (1,) | dtype = bool
  Group /processing/ophys of movie 0/mean images of movie 0 (Images) Structural images of a scanning
  Dataset /processing/ophys of movie 0/mean images of movie 0/Alexa Fluor 594 in pipette (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Dataset /processing/ophys of movie 0/mean images of movie 0/XCaMPgf at 940nm (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  session_description: 
  session_start_time: 2020-06-27T17:43:41-07:00
  timestamps_reference_time: 2020-06-27T17:43:41-07:00
