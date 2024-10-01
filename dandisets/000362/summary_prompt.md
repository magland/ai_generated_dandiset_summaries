
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:000362/draft
name: Simultaneous loose seal cell-attached recordings and two-photon imaging of GCaMP8 expressing mouse V1 neurons with drifting gratings visual stimuli  - RAW movies
contributor: [{'name': 'Rózsa, Márton', 'email': 'qtyush@gmail.com', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}]
description: We tested the jGCaMP8 sensors in L2/3 pyramidal neurons of mouse primary visual cortex. We made a craniotomy over V1 and infected neurons with adeno-associated virus (AAV2/1-hSynapsin-1) encoding jGCaMP8 variants (s/m/f), jGCaMP7f, or XCaMP-Gf. 18-80 days after the virus injection, the mouse was anesthetized, and we surgically removed the cranial window and performed durotomy. The craniotomy was filled with 10-15 μL of 1.5% agarose, and a D-shaped coverslip was secured on top to suppress brain motion and leave access to the brain on the lateral side of the craniotomy. Then mice were lightly anesthetized and mounted under a custom two-photon microscope. Full-field, high-contrast drifting gratings were presented in each of eight directions to the contralateral eye. Two-photon imaging (122 Hz) was performed of L2/3 somata and neuropil combined with loose-seal, cell-attached electrophysiological recording of a single neuron in the field of view. 
This dataset contains the raw 2-photon videos, for registered movies see: https://dandiarchive.org/dandiset/000168/
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'microscopy approach; cell population imaging', 'schemaKey': 'ApproachType'}, {'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 397456462638, 'numberOfFiles': 52, 'numberOfSubjects': 11, 'variableMeasured': ['ProcessingModule', 'OpticalChannel', 'ImagingPlane', 'TwoPhotonSeries', 'PlaneSegmentation', 'CurrentClampStimulusSeries', 'CurrentClampSeries', 'VoltageClampSeries', 'VoltageClampStimulusSeries'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'current clamp technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'two-photon microscopy technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'voltage clamp technique', 'schemaKey': 'MeasurementTechniqueType'}]}

Dandiset 000362 has 6 NWB files.
1 of these NWB files are of type 1.
1 of these NWB files are of type 2.
1 of these NWB files are of type 3.
2 of these NWB files are of type 4.
1 of these NWB files are of type 5.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Raw movie 0 (TwoPhotonSeries) no description
  Group /acquisition/Raw movie 0/imaging_plane (ImagingPlane) 
  Group /acquisition/Raw movie 0/imaging_plane/device (Device) 
  Group /acquisition/Raw movie 0/imaging_plane/green (OpticalChannel) 
  Group /acquisition/Raw movie 1 (TwoPhotonSeries) no description
  Group /acquisition/Raw movie 1/imaging_plane (ImagingPlane) 
  Group /acquisition/Raw movie 1/imaging_plane/device (Device) 
  Group /acquisition/Raw movie 1/imaging_plane/green (OpticalChannel) 
  Group /acquisition/Raw movie 2 (TwoPhotonSeries) no description
  Group /acquisition/Raw movie 2/imaging_plane (ImagingPlane) 
  Group /acquisition/Raw movie 2/imaging_plane/device (Device) 
  Group /acquisition/Raw movie 2/imaging_plane/green (OpticalChannel) 
  Group /acquisition/Raw movie 3 (TwoPhotonSeries) no description
  Group /acquisition/Raw movie 3/imaging_plane (ImagingPlane) 
  Group /acquisition/Raw movie 3/imaging_plane/device (Device) 
  Group /acquisition/Raw movie 3/imaging_plane/green (OpticalChannel) 
  Group /acquisition/Raw movie 4 (TwoPhotonSeries) no description
  Group /acquisition/Raw movie 4/imaging_plane (ImagingPlane) 
  Group /acquisition/Raw movie 4/imaging_plane/device (Device) 
  Group /acquisition/Raw movie 4/imaging_plane/green (OpticalChannel) 
  Group /acquisition/loose seal recording for movie 0 (VoltageClampSeries) no description
  Group /acquisition/loose seal recording for movie 0/electrode (IntracellularElectrode) 
  Group /acquisition/loose seal recording for movie 0/electrode/device (Device) Multiclamp 700B with 20 kHz low-pass filter
  Group /acquisition/loose seal recording for movie 1 (VoltageClampSeries) no description
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
  Dataset /analysis/responses/ap_snr (VectorData) signal to noise ratio of detected loose-seal action potential | shape = (619,) | dtype = float64
  Dataset /analysis/responses/ap_time (VectorData) peak time of detected loose-seal action potential | shape = (619,) | dtype = float64
  Dataset /analysis/responses/id (ElementIdentifiers)  | shape = (619,) | dtype = int64
  Dataset /analysis/responses/response (TimeSeriesReferenceVectorData) Column storing the reference to the recorded response for the recording (rows) | shape = (619,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  file_create_date: ['2022-11-28T17:06:14.815363-08:00']
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
  session_id: jGCaMP8f_ANM471993_cell01
  Group /general/subject (Subject) 
  surgery: [{"surgery_id": "1", "start_time": "2020-03-08 12:00:00", "end_time": "2020-03-08 12:50:00", "surgery_description": "headbar, craniotomy, virus injection, window:-: comments: nan"}, {"surgery_id": "2", "start_time": "2020-05-08 16:20:00", "end_time": "2020-05-08 17:25:00", "surgery_description": "window removal:-: comments: boneflap and dura removed, light swelling, bleeding"}]
  virus: [{"surgery_id": "1", "injection_id": "1", "virus_id": "10250", "skull_reference": "Lambda", "ml_location": "2300.000", "ap_location": "0.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-6xHis-noRSET-1NIW_Q315L_N19T_S24I_S26R_Q88E_LKI_GCaMP6s-WPRE.547.456", "titer": "32600000000000.0", "order_date": "2020-01-27", "remarks": "Ultrafast GCaMP456 ref: 1-1001-1"}, {"surgery_id": "1", "injection_id": "2", "virus_id": "10250", "skull_reference": "Lambda", "ml_location": "2800.000", "ap_location": "0.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-6xHis-noRSET-1NIW_Q315L_N19T_S24I_S26R_Q88E_LKI_GCaMP6s-WPRE.547.456", "titer": "32600000000000.0", "order_date": "2020-01-27", "remarks": "Ultrafast GCaMP456 ref: 1-1001-1"}, {"surgery_id": "1", "injection_id": "3", "virus_id": "10250", "skull_reference": "Lambda", "ml_location": "2800.000", "ap_location": "500.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-6xHis-noRSET-1NIW_Q315L_N19T_S24I_S26R_Q88E_LKI_GCaMP6s-WPRE.547.456", "titer": "32600000000000.0", "order_date": "2020-01-27", "remarks": "Ultrafast GCaMP456 ref: 1-1001-1"}, {"surgery_id": "1", "injection_id": "4", "virus_id": "10250", "skull_reference": "Lambda", "ml_location": "2300.000", "ap_location": "500.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-6xHis-noRSET-1NIW_Q315L_N19T_S24I_S26R_Q88E_LKI_GCaMP6s-WPRE.547.456", "titer": "32600000000000.0", "order_date": "2020-01-27", "remarks": "Ultrafast GCaMP456 ref: 1-1001-1"}, {"surgery_id": "1", "injection_id": "5", "virus_id": "10250", "skull_reference": "Lambda", "ml_location": "2300.000", "ap_location": "0.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-6xHis-noRSET-1NIW_Q315L_N19T_S24I_S26R_Q88E_LKI_GCaMP6s-WPRE.547.456", "titer": "32600000000000.0", "order_date": "2020-01-27", "remarks": "Ultrafast GCaMP456 ref: 1-1001-1"}, {"surgery_id": "1", "injection_id": "6", "virus_id": "10250", "skull_reference": "Lambda", "ml_location": "2800.000", "ap_location": "0.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-6xHis-noRSET-1NIW_Q315L_N19T_S24I_S26R_Q88E_LKI_GCaMP6s-WPRE.547.456", "titer": "32600000000000.0", "order_date": "2020-01-27", "remarks": "Ultrafast GCaMP456 ref: 1-1001-1"}, {"surgery_id": "1", "injection_id": "7", "virus_id": "10250", "skull_reference": "Lambda", "ml_location": "2800.000", "ap_location": "500.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-6xHis-noRSET-1NIW_Q315L_N19T_S24I_S26R_Q88E_LKI_GCaMP6s-WPRE.547.456", "titer": "32600000000000.0", "order_date": "2020-01-27", "remarks": "Ultrafast GCaMP456 ref: 1-1001-1"}, {"surgery_id": "1", "injection_id": "8", "virus_id": "10250", "skull_reference": "Lambda", "ml_location": "2300.000", "ap_location": "500.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-6xHis-noRSET-1NIW_Q315L_N19T_S24I_S26R_Q88E_LKI_GCaMP6s-WPRE.547.456", "titer": "32600000000000.0", "order_date": "2020-01-27", "remarks": "Ultrafast GCaMP456 ref: 1-1001-1"}, {"surgery_id": "1", "injection_id": "9", "virus_id": "10250", "skull_reference": "Lambda", "ml_location": "2300.000", "ap_location": "0.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-6xHis-noRSET-1NIW_Q315L_N19T_S24I_S26R_Q88E_LKI_GCaMP6s-WPRE.547.456", "titer": "32600000000000.0", "order_date": "2020-01-27", "remarks": "Ultrafast GCaMP456 ref: 1-1001-1"}, {"surgery_id": "1", "injection_id": "10", "virus_id": "10250", "skull_reference": "Lambda", "ml_location": "2800.000", "ap_location": "0.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-6xHis-noRSET-1NIW_Q315L_N19T_S24I_S26R_Q88E_LKI_GCaMP6s-WPRE.547.456", "titer": "32600000000000.0", "order_date": "2020-01-27", "remarks": "Ultrafast GCaMP456 ref: 1-1001-1"}, {"surgery_id": "1", "injection_id": "11", "virus_id": "10250", "skull_reference": "Lambda", "ml_location": "2800.000", "ap_location": "500.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-6xHis-noRSET-1NIW_Q315L_N19T_S24I_S26R_Q88E_LKI_GCaMP6s-WPRE.547.456", "titer": "32600000000000.0", "order_date": "2020-01-27", "remarks": "Ultrafast GCaMP456 ref: 1-1001-1"}, {"surgery_id": "1", "injection_id": "12", "virus_id": "10250", "skull_reference": "Lambda", "ml_location": "2300.000", "ap_location": "500.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-6xHis-noRSET-1NIW_Q315L_N19T_S24I_S26R_Q88E_LKI_GCaMP6s-WPRE.547.456", "titer": "32600000000000.0", "order_date": "2020-01-27", "remarks": "Ultrafast GCaMP456 ref: 1-1001-1"}]
  identifier: jGCaMP8f_ANM471993_cell01
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (5,) | dtype = int64
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (5,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (5,) | dtype = float64
  Dataset /intervals/epochs/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (15,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
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
  Dataset /processing/ophys of movie 0/Fluorescence/NeuropilResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (6,) | dtype = int64
  Group /processing/ophys of movie 0/Fluorescence/RoiResponseSeries (RoiResponseSeries) weighted average fluorescence of roi
  Dataset /processing/ophys of movie 0/Fluorescence/RoiResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (6,) | dtype = int64
  Group /processing/ophys of movie 0/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation (PlaneSegmentation) output from segmenting with Suite2p, ROI 0 is the neuron recorded with electrophysiology
  Dataset /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/cell_type (VectorData) pyr for putative pyramidal cells, int for putative interneurons, based on average loose-seal spike shape | shape = (6,) | dtype = object
  Dataset /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/id (ElementIdentifiers)  | shape = (6,) | dtype = int64
  Dataset /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (6, 512, 128) | dtype = float64
  Group /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/imaging_plane/device (Device) 
  Group /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/imaging_plane/green (OpticalChannel) 
  Dataset /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/neuropil_mask (VectorData) mask of neuropil surrounding this roi | shape = (6, 512, 128) | dtype = bool
  Dataset /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/recorded_with_ephys (VectorData) whether this ROI is simultaneously loose-seal recorded | shape = (6,) | dtype = bool
  Group /processing/ophys of movie 0/mean images of movie 0 (Images) Structural images of a scanning
  Dataset /processing/ophys of movie 0/mean images of movie 0/Alexa Fluor 594 in pipette (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Dataset /processing/ophys of movie 0/mean images of movie 0/jGCaMP8f at 940nm (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Group /processing/ophys of movie 1 (ProcessingModule) Processing result of imaging
  Group /processing/ophys of movie 1/Fluorescence (Fluorescence) 
  Group /processing/ophys of movie 1/Fluorescence/NeuropilResponseSeries (RoiResponseSeries) average fluorescence of the neuropil surrounding the roi
  Dataset /processing/ophys of movie 1/Fluorescence/NeuropilResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (3,) | dtype = int64
  Group /processing/ophys of movie 1/Fluorescence/RoiResponseSeries (RoiResponseSeries) weighted average fluorescence of roi
  Dataset /processing/ophys of movie 1/Fluorescence/RoiResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (3,) | dtype = int64
  Group /processing/ophys of movie 1/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation (PlaneSegmentation) output from segmenting with Suite2p, ROI 0 is the neuron recorded with electrophysiology
  Dataset /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation/cell_type (VectorData) pyr for putative pyramidal cells, int for putative interneurons, based on average loose-seal spike shape | shape = (3,) | dtype = object
  Dataset /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation/id (ElementIdentifiers)  | shape = (3,) | dtype = int64
  Dataset /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (3, 512, 128) | dtype = float64
  Group /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation/imaging_plane/device (Device) 
  Group /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation/imaging_plane/green (OpticalChannel) 
  Dataset /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation/neuropil_mask (VectorData) mask of neuropil surrounding this roi | shape = (3, 512, 128) | dtype = bool
  Dataset /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation/recorded_with_ephys (VectorData) whether this ROI is simultaneously loose-seal recorded | shape = (3,) | dtype = bool
  Group /processing/ophys of movie 1/mean images of movie 1 (Images) Structural images of a scanning
  Dataset /processing/ophys of movie 1/mean images of movie 1/Alexa Fluor 594 in pipette (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Dataset /processing/ophys of movie 1/mean images of movie 1/jGCaMP8f at 940nm (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Group /processing/ophys of movie 2 (ProcessingModule) Processing result of imaging
  Group /processing/ophys of movie 2/Fluorescence (Fluorescence) 
  Group /processing/ophys of movie 2/Fluorescence/NeuropilResponseSeries (RoiResponseSeries) average fluorescence of the neuropil surrounding the roi
  Dataset /processing/ophys of movie 2/Fluorescence/NeuropilResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (4,) | dtype = int64
  Group /processing/ophys of movie 2/Fluorescence/RoiResponseSeries (RoiResponseSeries) weighted average fluorescence of roi
  Dataset /processing/ophys of movie 2/Fluorescence/RoiResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (4,) | dtype = int64
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
  Dataset /processing/ophys of movie 2/mean images of movie 2/jGCaMP8f at 940nm (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Group /processing/ophys of movie 3 (ProcessingModule) Processing result of imaging
  Group /processing/ophys of movie 3/Fluorescence (Fluorescence) 
  Group /processing/ophys of movie 3/Fluorescence/NeuropilResponseSeries (RoiResponseSeries) average fluorescence of the neuropil surrounding the roi
  Dataset /processing/ophys of movie 3/Fluorescence/NeuropilResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (4,) | dtype = int64
  Group /processing/ophys of movie 3/Fluorescence/RoiResponseSeries (RoiResponseSeries) weighted average fluorescence of roi
  Dataset /processing/ophys of movie 3/Fluorescence/RoiResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (4,) | dtype = int64
  Group /processing/ophys of movie 3/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys of movie 3/ImageSegmentation/MovieSegmentation (PlaneSegmentation) output from segmenting with Suite2p, ROI 0 is the neuron recorded with electrophysiology
  Dataset /processing/ophys of movie 3/ImageSegmentation/MovieSegmentation/cell_type (VectorData) pyr for putative pyramidal cells, int for putative interneurons, based on average loose-seal spike shape | shape = (4,) | dtype = object
  Dataset /processing/ophys of movie 3/ImageSegmentation/MovieSegmentation/id (ElementIdentifiers)  | shape = (4,) | dtype = int64
  Dataset /processing/ophys of movie 3/ImageSegmentation/MovieSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (4, 512, 128) | dtype = float64
  Group /processing/ophys of movie 3/ImageSegmentation/MovieSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys of movie 3/ImageSegmentation/MovieSegmentation/imaging_plane/device (Device) 
  Group /processing/ophys of movie 3/ImageSegmentation/MovieSegmentation/imaging_plane/green (OpticalChannel) 
  Dataset /processing/ophys of movie 3/ImageSegmentation/MovieSegmentation/neuropil_mask (VectorData) mask of neuropil surrounding this roi | shape = (4, 512, 128) | dtype = bool
  Dataset /processing/ophys of movie 3/ImageSegmentation/MovieSegmentation/recorded_with_ephys (VectorData) whether this ROI is simultaneously loose-seal recorded | shape = (4,) | dtype = bool
  Group /processing/ophys of movie 3/mean images of movie 3 (Images) Structural images of a scanning
  Dataset /processing/ophys of movie 3/mean images of movie 3/Alexa Fluor 594 in pipette (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Dataset /processing/ophys of movie 3/mean images of movie 3/jGCaMP8f at 940nm (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Group /processing/ophys of movie 4 (ProcessingModule) Processing result of imaging
  Group /processing/ophys of movie 4/Fluorescence (Fluorescence) 
  Group /processing/ophys of movie 4/Fluorescence/NeuropilResponseSeries (RoiResponseSeries) average fluorescence of the neuropil surrounding the roi
  Dataset /processing/ophys of movie 4/Fluorescence/NeuropilResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (5,) | dtype = int64
  Group /processing/ophys of movie 4/Fluorescence/RoiResponseSeries (RoiResponseSeries) weighted average fluorescence of roi
  Dataset /processing/ophys of movie 4/Fluorescence/RoiResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (5,) | dtype = int64
  Group /processing/ophys of movie 4/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys of movie 4/ImageSegmentation/MovieSegmentation (PlaneSegmentation) output from segmenting with Suite2p, ROI 0 is the neuron recorded with electrophysiology
  Dataset /processing/ophys of movie 4/ImageSegmentation/MovieSegmentation/cell_type (VectorData) pyr for putative pyramidal cells, int for putative interneurons, based on average loose-seal spike shape | shape = (5,) | dtype = object
  Dataset /processing/ophys of movie 4/ImageSegmentation/MovieSegmentation/id (ElementIdentifiers)  | shape = (5,) | dtype = int64
  Dataset /processing/ophys of movie 4/ImageSegmentation/MovieSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (5, 512, 128) | dtype = float64
  Group /processing/ophys of movie 4/ImageSegmentation/MovieSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys of movie 4/ImageSegmentation/MovieSegmentation/imaging_plane/device (Device) 
  Group /processing/ophys of movie 4/ImageSegmentation/MovieSegmentation/imaging_plane/green (OpticalChannel) 
  Dataset /processing/ophys of movie 4/ImageSegmentation/MovieSegmentation/neuropil_mask (VectorData) mask of neuropil surrounding this roi | shape = (5, 512, 128) | dtype = bool
  Dataset /processing/ophys of movie 4/ImageSegmentation/MovieSegmentation/recorded_with_ephys (VectorData) whether this ROI is simultaneously loose-seal recorded | shape = (5,) | dtype = bool
  Group /processing/ophys of movie 4/mean images of movie 4 (Images) Structural images of a scanning
  Dataset /processing/ophys of movie 4/mean images of movie 4/Alexa Fluor 594 in pipette (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Dataset /processing/ophys of movie 4/mean images of movie 4/jGCaMP8f at 940nm (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  session_description: 
  session_start_time: 2020-05-08T20:17:26-07:00
  timestamps_reference_time: 2020-05-08T20:17:26-07:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Raw movie 0 (TwoPhotonSeries) no description
  Group /acquisition/Raw movie 0/imaging_plane (ImagingPlane) 
  Group /acquisition/Raw movie 0/imaging_plane/device (Device) 
  Group /acquisition/Raw movie 0/imaging_plane/green (OpticalChannel) 
  Group /acquisition/Raw movie 1 (TwoPhotonSeries) no description
  Group /acquisition/Raw movie 1/imaging_plane (ImagingPlane) 
  Group /acquisition/Raw movie 1/imaging_plane/device (Device) 
  Group /acquisition/Raw movie 1/imaging_plane/green (OpticalChannel) 
  Group /acquisition/Raw movie 2 (TwoPhotonSeries) no description
  Group /acquisition/Raw movie 2/imaging_plane (ImagingPlane) 
  Group /acquisition/Raw movie 2/imaging_plane/device (Device) 
  Group /acquisition/Raw movie 2/imaging_plane/green (OpticalChannel) 
  Group /acquisition/Raw movie 3 (TwoPhotonSeries) no description
  Group /acquisition/Raw movie 3/imaging_plane (ImagingPlane) 
  Group /acquisition/Raw movie 3/imaging_plane/device (Device) 
  Group /acquisition/Raw movie 3/imaging_plane/green (OpticalChannel) 
  Group /acquisition/Raw movie 4 (TwoPhotonSeries) no description
  Group /acquisition/Raw movie 4/imaging_plane (ImagingPlane) 
  Group /acquisition/Raw movie 4/imaging_plane/device (Device) 
  Group /acquisition/Raw movie 4/imaging_plane/green (OpticalChannel) 
  Group /acquisition/Raw movie 5 (TwoPhotonSeries) no description
  Group /acquisition/Raw movie 5/imaging_plane (ImagingPlane) 
  Group /acquisition/Raw movie 5/imaging_plane/device (Device) 
  Group /acquisition/Raw movie 5/imaging_plane/green (OpticalChannel) 
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
  Group /acquisition/loose seal recording for movie 5 (CurrentClampSeries) no description
  Group /acquisition/loose seal recording for movie 5/electrode (IntracellularElectrode) 
  Group /acquisition/loose seal recording for movie 5/electrode/device (Device) Multiclamp 700B with 20 kHz low-pass filter
  Group /analysis/responses (IntracellularResponsesTable) Table for storing intracellular response related metadata.
  Dataset /analysis/responses/ap_snr (VectorData) signal to noise ratio of detected loose-seal action potential | shape = (481,) | dtype = float64
  Dataset /analysis/responses/ap_time (VectorData) peak time of detected loose-seal action potential | shape = (481,) | dtype = float64
  Dataset /analysis/responses/id (ElementIdentifiers)  | shape = (481,) | dtype = int64
  Dataset /analysis/responses/response (TimeSeriesReferenceVectorData) Column storing the reference to the recorded response for the recording (rows) | shape = (481,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  file_create_date: ['2022-11-28T17:24:55.182431-08:00']
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
  Group /general/optophysiology/Movie_3 (ImagingPlane) 
  Group /general/optophysiology/Movie_3/device (Device) 
  Group /general/optophysiology/Movie_3/green (OpticalChannel) 
  Group /general/optophysiology/Movie_4 (ImagingPlane) 
  Group /general/optophysiology/Movie_4/device (Device) 
  Group /general/optophysiology/Movie_4/green (OpticalChannel) 
  Group /general/optophysiology/Movie_5 (ImagingPlane) 
  Group /general/optophysiology/Movie_5/device (Device) 
  Group /general/optophysiology/Movie_5/green (OpticalChannel) 
  related_publications: ['10.25378/janelia.13148243' '10.1101/2021.11.08.467793']
  session_id: jGCaMP8f_ANM471993_cell02
  Group /general/subject (Subject) 
  surgery: [{"surgery_id": "1", "start_time": "2020-03-08 12:00:00", "end_time": "2020-03-08 12:50:00", "surgery_description": "headbar, craniotomy, virus injection, window:-: comments: nan"}, {"surgery_id": "2", "start_time": "2020-05-08 16:20:00", "end_time": "2020-05-08 17:25:00", "surgery_description": "window removal:-: comments: boneflap and dura removed, light swelling, bleeding"}]
  virus: [{"surgery_id": "1", "injection_id": "1", "virus_id": "10250", "skull_reference": "Lambda", "ml_location": "2300.000", "ap_location": "0.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-6xHis-noRSET-1NIW_Q315L_N19T_S24I_S26R_Q88E_LKI_GCaMP6s-WPRE.547.456", "titer": "32600000000000.0", "order_date": "2020-01-27", "remarks": "Ultrafast GCaMP456 ref: 1-1001-1"}, {"surgery_id": "1", "injection_id": "2", "virus_id": "10250", "skull_reference": "Lambda", "ml_location": "2800.000", "ap_location": "0.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-6xHis-noRSET-1NIW_Q315L_N19T_S24I_S26R_Q88E_LKI_GCaMP6s-WPRE.547.456", "titer": "32600000000000.0", "order_date": "2020-01-27", "remarks": "Ultrafast GCaMP456 ref: 1-1001-1"}, {"surgery_id": "1", "injection_id": "3", "virus_id": "10250", "skull_reference": "Lambda", "ml_location": "2800.000", "ap_location": "500.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-6xHis-noRSET-1NIW_Q315L_N19T_S24I_S26R_Q88E_LKI_GCaMP6s-WPRE.547.456", "titer": "32600000000000.0", "order_date": "2020-01-27", "remarks": "Ultrafast GCaMP456 ref: 1-1001-1"}, {"surgery_id": "1", "injection_id": "4", "virus_id": "10250", "skull_reference": "Lambda", "ml_location": "2300.000", "ap_location": "500.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-6xHis-noRSET-1NIW_Q315L_N19T_S24I_S26R_Q88E_LKI_GCaMP6s-WPRE.547.456", "titer": "32600000000000.0", "order_date": "2020-01-27", "remarks": "Ultrafast GCaMP456 ref: 1-1001-1"}, {"surgery_id": "1", "injection_id": "5", "virus_id": "10250", "skull_reference": "Lambda", "ml_location": "2300.000", "ap_location": "0.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-6xHis-noRSET-1NIW_Q315L_N19T_S24I_S26R_Q88E_LKI_GCaMP6s-WPRE.547.456", "titer": "32600000000000.0", "order_date": "2020-01-27", "remarks": "Ultrafast GCaMP456 ref: 1-1001-1"}, {"surgery_id": "1", "injection_id": "6", "virus_id": "10250", "skull_reference": "Lambda", "ml_location": "2800.000", "ap_location": "0.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-6xHis-noRSET-1NIW_Q315L_N19T_S24I_S26R_Q88E_LKI_GCaMP6s-WPRE.547.456", "titer": "32600000000000.0", "order_date": "2020-01-27", "remarks": "Ultrafast GCaMP456 ref: 1-1001-1"}, {"surgery_id": "1", "injection_id": "7", "virus_id": "10250", "skull_reference": "Lambda", "ml_location": "2800.000", "ap_location": "500.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-6xHis-noRSET-1NIW_Q315L_N19T_S24I_S26R_Q88E_LKI_GCaMP6s-WPRE.547.456", "titer": "32600000000000.0", "order_date": "2020-01-27", "remarks": "Ultrafast GCaMP456 ref: 1-1001-1"}, {"surgery_id": "1", "injection_id": "8", "virus_id": "10250", "skull_reference": "Lambda", "ml_location": "2300.000", "ap_location": "500.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-6xHis-noRSET-1NIW_Q315L_N19T_S24I_S26R_Q88E_LKI_GCaMP6s-WPRE.547.456", "titer": "32600000000000.0", "order_date": "2020-01-27", "remarks": "Ultrafast GCaMP456 ref: 1-1001-1"}, {"surgery_id": "1", "injection_id": "9", "virus_id": "10250", "skull_reference": "Lambda", "ml_location": "2300.000", "ap_location": "0.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-6xHis-noRSET-1NIW_Q315L_N19T_S24I_S26R_Q88E_LKI_GCaMP6s-WPRE.547.456", "titer": "32600000000000.0", "order_date": "2020-01-27", "remarks": "Ultrafast GCaMP456 ref: 1-1001-1"}, {"surgery_id": "1", "injection_id": "10", "virus_id": "10250", "skull_reference": "Lambda", "ml_location": "2800.000", "ap_location": "0.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-6xHis-noRSET-1NIW_Q315L_N19T_S24I_S26R_Q88E_LKI_GCaMP6s-WPRE.547.456", "titer": "32600000000000.0", "order_date": "2020-01-27", "remarks": "Ultrafast GCaMP456 ref: 1-1001-1"}, {"surgery_id": "1", "injection_id": "11", "virus_id": "10250", "skull_reference": "Lambda", "ml_location": "2800.000", "ap_location": "500.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-6xHis-noRSET-1NIW_Q315L_N19T_S24I_S26R_Q88E_LKI_GCaMP6s-WPRE.547.456", "titer": "32600000000000.0", "order_date": "2020-01-27", "remarks": "Ultrafast GCaMP456 ref: 1-1001-1"}, {"surgery_id": "1", "injection_id": "12", "virus_id": "10250", "skull_reference": "Lambda", "ml_location": "2300.000", "ap_location": "500.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-6xHis-noRSET-1NIW_Q315L_N19T_S24I_S26R_Q88E_LKI_GCaMP6s-WPRE.547.456", "titer": "32600000000000.0", "order_date": "2020-01-27", "remarks": "Ultrafast GCaMP456 ref: 1-1001-1"}]
  identifier: jGCaMP8f_ANM471993_cell02
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (6,) | dtype = int64
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (6,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (6,) | dtype = float64
  Dataset /intervals/epochs/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (18,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/epochs/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (6,) | dtype = uint8
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/amplitude (VectorData) amplitude of drifting grating stimulus | shape = (240,) | dtype = float64
  Dataset /intervals/trials/angle (VectorData) angle of drifting grating stimulus in degrees | shape = (240,) | dtype = int64
  Dataset /intervals/trials/cycles_per_degree (VectorData) cycles per degree of drifting grating stimulus | shape = (240,) | dtype = float64
  Dataset /intervals/trials/cycles_per_second (VectorData) cycles per second of drifting grating stimulus | shape = (240,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (240,) | dtype = int64
  Dataset /intervals/trials/movie_number (VectorData) during which movie this visual stimulus happened | shape = (240,) | dtype = int64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (240,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (240,) | dtype = float64
  Group /processing/ophys of movie 0 (ProcessingModule) Processing result of imaging
  Group /processing/ophys of movie 0/Fluorescence (Fluorescence) 
  Group /processing/ophys of movie 0/Fluorescence/NeuropilResponseSeries (RoiResponseSeries) average fluorescence of the neuropil surrounding the roi
  Dataset /processing/ophys of movie 0/Fluorescence/NeuropilResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (3,) | dtype = int64
  Group /processing/ophys of movie 0/Fluorescence/RoiResponseSeries (RoiResponseSeries) weighted average fluorescence of roi
  Dataset /processing/ophys of movie 0/Fluorescence/RoiResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (3,) | dtype = int64
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
  Dataset /processing/ophys of movie 0/mean images of movie 0/jGCaMP8f at 940nm (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Group /processing/ophys of movie 1 (ProcessingModule) Processing result of imaging
  Group /processing/ophys of movie 1/Fluorescence (Fluorescence) 
  Group /processing/ophys of movie 1/Fluorescence/NeuropilResponseSeries (RoiResponseSeries) average fluorescence of the neuropil surrounding the roi
  Dataset /processing/ophys of movie 1/Fluorescence/NeuropilResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (3,) | dtype = int64
  Group /processing/ophys of movie 1/Fluorescence/RoiResponseSeries (RoiResponseSeries) weighted average fluorescence of roi
  Dataset /processing/ophys of movie 1/Fluorescence/RoiResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (3,) | dtype = int64
  Group /processing/ophys of movie 1/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation (PlaneSegmentation) output from segmenting with Suite2p, ROI 0 is the neuron recorded with electrophysiology
  Dataset /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation/cell_type (VectorData) pyr for putative pyramidal cells, int for putative interneurons, based on average loose-seal spike shape | shape = (3,) | dtype = object
  Dataset /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation/id (ElementIdentifiers)  | shape = (3,) | dtype = int64
  Dataset /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (3, 512, 128) | dtype = float64
  Group /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation/imaging_plane/device (Device) 
  Group /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation/imaging_plane/green (OpticalChannel) 
  Dataset /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation/neuropil_mask (VectorData) mask of neuropil surrounding this roi | shape = (3, 512, 128) | dtype = bool
  Dataset /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation/recorded_with_ephys (VectorData) whether this ROI is simultaneously loose-seal recorded | shape = (3,) | dtype = bool
  Group /processing/ophys of movie 1/mean images of movie 1 (Images) Structural images of a scanning
  Dataset /processing/ophys of movie 1/mean images of movie 1/Alexa Fluor 594 in pipette (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Dataset /processing/ophys of movie 1/mean images of movie 1/jGCaMP8f at 940nm (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Group /processing/ophys of movie 2 (ProcessingModule) Processing result of imaging
  Group /processing/ophys of movie 2/Fluorescence (Fluorescence) 
  Group /processing/ophys of movie 2/Fluorescence/NeuropilResponseSeries (RoiResponseSeries) average fluorescence of the neuropil surrounding the roi
  Dataset /processing/ophys of movie 2/Fluorescence/NeuropilResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (5,) | dtype = int64
  Group /processing/ophys of movie 2/Fluorescence/RoiResponseSeries (RoiResponseSeries) weighted average fluorescence of roi
  Dataset /processing/ophys of movie 2/Fluorescence/RoiResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (5,) | dtype = int64
  Group /processing/ophys of movie 2/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation (PlaneSegmentation) output from segmenting with Suite2p, ROI 0 is the neuron recorded with electrophysiology
  Dataset /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation/cell_type (VectorData) pyr for putative pyramidal cells, int for putative interneurons, based on average loose-seal spike shape | shape = (5,) | dtype = object
  Dataset /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation/id (ElementIdentifiers)  | shape = (5,) | dtype = int64
  Dataset /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (5, 512, 128) | dtype = float64
  Group /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation/imaging_plane/device (Device) 
  Group /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation/imaging_plane/green (OpticalChannel) 
  Dataset /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation/neuropil_mask (VectorData) mask of neuropil surrounding this roi | shape = (5, 512, 128) | dtype = bool
  Dataset /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation/recorded_with_ephys (VectorData) whether this ROI is simultaneously loose-seal recorded | shape = (5,) | dtype = bool
  Group /processing/ophys of movie 2/mean images of movie 2 (Images) Structural images of a scanning
  Dataset /processing/ophys of movie 2/mean images of movie 2/Alexa Fluor 594 in pipette (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Dataset /processing/ophys of movie 2/mean images of movie 2/jGCaMP8f at 940nm (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Group /processing/ophys of movie 3 (ProcessingModule) Processing result of imaging
  Group /processing/ophys of movie 3/Fluorescence (Fluorescence) 
  Group /processing/ophys of movie 3/Fluorescence/NeuropilResponseSeries (RoiResponseSeries) average fluorescence of the neuropil surrounding the roi
  Dataset /processing/ophys of movie 3/Fluorescence/NeuropilResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (3,) | dtype = int64
  Group /processing/ophys of movie 3/Fluorescence/RoiResponseSeries (RoiResponseSeries) weighted average fluorescence of roi
  Dataset /processing/ophys of movie 3/Fluorescence/RoiResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (3,) | dtype = int64
  Group /processing/ophys of movie 3/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys of movie 3/ImageSegmentation/MovieSegmentation (PlaneSegmentation) output from segmenting with Suite2p, ROI 0 is the neuron recorded with electrophysiology
  Dataset /processing/ophys of movie 3/ImageSegmentation/MovieSegmentation/cell_type (VectorData) pyr for putative pyramidal cells, int for putative interneurons, based on average loose-seal spike shape | shape = (3,) | dtype = object
  Dataset /processing/ophys of movie 3/ImageSegmentation/MovieSegmentation/id (ElementIdentifiers)  | shape = (3,) | dtype = int64
  Dataset /processing/ophys of movie 3/ImageSegmentation/MovieSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (3, 512, 128) | dtype = float64
  Group /processing/ophys of movie 3/ImageSegmentation/MovieSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys of movie 3/ImageSegmentation/MovieSegmentation/imaging_plane/device (Device) 
  Group /processing/ophys of movie 3/ImageSegmentation/MovieSegmentation/imaging_plane/green (OpticalChannel) 
  Dataset /processing/ophys of movie 3/ImageSegmentation/MovieSegmentation/neuropil_mask (VectorData) mask of neuropil surrounding this roi | shape = (3, 512, 128) | dtype = bool
  Dataset /processing/ophys of movie 3/ImageSegmentation/MovieSegmentation/recorded_with_ephys (VectorData) whether this ROI is simultaneously loose-seal recorded | shape = (3,) | dtype = bool
  Group /processing/ophys of movie 3/mean images of movie 3 (Images) Structural images of a scanning
  Dataset /processing/ophys of movie 3/mean images of movie 3/Alexa Fluor 594 in pipette (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Dataset /processing/ophys of movie 3/mean images of movie 3/jGCaMP8f at 940nm (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Group /processing/ophys of movie 4 (ProcessingModule) Processing result of imaging
  Group /processing/ophys of movie 4/Fluorescence (Fluorescence) 
  Group /processing/ophys of movie 4/Fluorescence/NeuropilResponseSeries (RoiResponseSeries) average fluorescence of the neuropil surrounding the roi
  Dataset /processing/ophys of movie 4/Fluorescence/NeuropilResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (3,) | dtype = int64
  Group /processing/ophys of movie 4/Fluorescence/RoiResponseSeries (RoiResponseSeries) weighted average fluorescence of roi
  Dataset /processing/ophys of movie 4/Fluorescence/RoiResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (3,) | dtype = int64
  Group /processing/ophys of movie 4/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys of movie 4/ImageSegmentation/MovieSegmentation (PlaneSegmentation) output from segmenting with Suite2p, ROI 0 is the neuron recorded with electrophysiology
  Dataset /processing/ophys of movie 4/ImageSegmentation/MovieSegmentation/cell_type (VectorData) pyr for putative pyramidal cells, int for putative interneurons, based on average loose-seal spike shape | shape = (3,) | dtype = object
  Dataset /processing/ophys of movie 4/ImageSegmentation/MovieSegmentation/id (ElementIdentifiers)  | shape = (3,) | dtype = int64
  Dataset /processing/ophys of movie 4/ImageSegmentation/MovieSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (3, 512, 128) | dtype = float64
  Group /processing/ophys of movie 4/ImageSegmentation/MovieSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys of movie 4/ImageSegmentation/MovieSegmentation/imaging_plane/device (Device) 
  Group /processing/ophys of movie 4/ImageSegmentation/MovieSegmentation/imaging_plane/green (OpticalChannel) 
  Dataset /processing/ophys of movie 4/ImageSegmentation/MovieSegmentation/neuropil_mask (VectorData) mask of neuropil surrounding this roi | shape = (3, 512, 128) | dtype = bool
  Dataset /processing/ophys of movie 4/ImageSegmentation/MovieSegmentation/recorded_with_ephys (VectorData) whether this ROI is simultaneously loose-seal recorded | shape = (3,) | dtype = bool
  Group /processing/ophys of movie 4/mean images of movie 4 (Images) Structural images of a scanning
  Dataset /processing/ophys of movie 4/mean images of movie 4/Alexa Fluor 594 in pipette (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Dataset /processing/ophys of movie 4/mean images of movie 4/jGCaMP8f at 940nm (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Group /processing/ophys of movie 5 (ProcessingModule) Processing result of imaging
  Group /processing/ophys of movie 5/Fluorescence (Fluorescence) 
  Group /processing/ophys of movie 5/Fluorescence/NeuropilResponseSeries (RoiResponseSeries) average fluorescence of the neuropil surrounding the roi
  Dataset /processing/ophys of movie 5/Fluorescence/NeuropilResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (6,) | dtype = int64
  Group /processing/ophys of movie 5/Fluorescence/RoiResponseSeries (RoiResponseSeries) weighted average fluorescence of roi
  Dataset /processing/ophys of movie 5/Fluorescence/RoiResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (6,) | dtype = int64
  Group /processing/ophys of movie 5/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys of movie 5/ImageSegmentation/MovieSegmentation (PlaneSegmentation) output from segmenting with Suite2p, ROI 0 is the neuron recorded with electrophysiology
  Dataset /processing/ophys of movie 5/ImageSegmentation/MovieSegmentation/cell_type (VectorData) pyr for putative pyramidal cells, int for putative interneurons, based on average loose-seal spike shape | shape = (6,) | dtype = object
  Dataset /processing/ophys of movie 5/ImageSegmentation/MovieSegmentation/id (ElementIdentifiers)  | shape = (6,) | dtype = int64
  Dataset /processing/ophys of movie 5/ImageSegmentation/MovieSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (6, 512, 128) | dtype = float64
  Group /processing/ophys of movie 5/ImageSegmentation/MovieSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys of movie 5/ImageSegmentation/MovieSegmentation/imaging_plane/device (Device) 
  Group /processing/ophys of movie 5/ImageSegmentation/MovieSegmentation/imaging_plane/green (OpticalChannel) 
  Dataset /processing/ophys of movie 5/ImageSegmentation/MovieSegmentation/neuropil_mask (VectorData) mask of neuropil surrounding this roi | shape = (6, 512, 128) | dtype = bool
  Dataset /processing/ophys of movie 5/ImageSegmentation/MovieSegmentation/recorded_with_ephys (VectorData) whether this ROI is simultaneously loose-seal recorded | shape = (6,) | dtype = bool
  Group /processing/ophys of movie 5/mean images of movie 5 (Images) Structural images of a scanning
  Dataset /processing/ophys of movie 5/mean images of movie 5/Alexa Fluor 594 in pipette (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Dataset /processing/ophys of movie 5/mean images of movie 5/jGCaMP8f at 940nm (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  session_description: 
  session_start_time: 2020-05-08T20:43:52-07:00
  timestamps_reference_time: 2020-05-08T20:43:52-07:00


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Raw movie 0 (TwoPhotonSeries) no description
  Group /acquisition/Raw movie 0/imaging_plane (ImagingPlane) 
  Group /acquisition/Raw movie 0/imaging_plane/device (Device) 
  Group /acquisition/Raw movie 0/imaging_plane/green (OpticalChannel) 
  Group /acquisition/Raw movie 1 (TwoPhotonSeries) no description
  Group /acquisition/Raw movie 1/imaging_plane (ImagingPlane) 
  Group /acquisition/Raw movie 1/imaging_plane/device (Device) 
  Group /acquisition/Raw movie 1/imaging_plane/green (OpticalChannel) 
  Group /acquisition/Raw movie 2 (TwoPhotonSeries) no description
  Group /acquisition/Raw movie 2/imaging_plane (ImagingPlane) 
  Group /acquisition/Raw movie 2/imaging_plane/device (Device) 
  Group /acquisition/Raw movie 2/imaging_plane/green (OpticalChannel) 
  Group /acquisition/Raw movie 3 (TwoPhotonSeries) no description
  Group /acquisition/Raw movie 3/imaging_plane (ImagingPlane) 
  Group /acquisition/Raw movie 3/imaging_plane/device (Device) 
  Group /acquisition/Raw movie 3/imaging_plane/green (OpticalChannel) 
  Group /acquisition/Raw movie 4 (TwoPhotonSeries) no description
  Group /acquisition/Raw movie 4/imaging_plane (ImagingPlane) 
  Group /acquisition/Raw movie 4/imaging_plane/device (Device) 
  Group /acquisition/Raw movie 4/imaging_plane/green (OpticalChannel) 
  Group /acquisition/Raw movie 5 (TwoPhotonSeries) no description
  Group /acquisition/Raw movie 5/imaging_plane (ImagingPlane) 
  Group /acquisition/Raw movie 5/imaging_plane/device (Device) 
  Group /acquisition/Raw movie 5/imaging_plane/green (OpticalChannel) 
  Group /acquisition/Raw movie 6 (TwoPhotonSeries) no description
  Group /acquisition/Raw movie 6/imaging_plane (ImagingPlane) 
  Group /acquisition/Raw movie 6/imaging_plane/device (Device) 
  Group /acquisition/Raw movie 6/imaging_plane/green (OpticalChannel) 
  Group /acquisition/Raw movie 7 (TwoPhotonSeries) no description
  Group /acquisition/Raw movie 7/imaging_plane (ImagingPlane) 
  Group /acquisition/Raw movie 7/imaging_plane/device (Device) 
  Group /acquisition/Raw movie 7/imaging_plane/green (OpticalChannel) 
  Group /acquisition/Raw movie 8 (TwoPhotonSeries) no description
  Group /acquisition/Raw movie 8/imaging_plane (ImagingPlane) 
  Group /acquisition/Raw movie 8/imaging_plane/device (Device) 
  Group /acquisition/Raw movie 8/imaging_plane/green (OpticalChannel) 
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
  Group /acquisition/loose seal recording for movie 5 (CurrentClampSeries) no description
  Group /acquisition/loose seal recording for movie 5/electrode (IntracellularElectrode) 
  Group /acquisition/loose seal recording for movie 5/electrode/device (Device) Multiclamp 700B with 20 kHz low-pass filter
  Group /acquisition/loose seal recording for movie 6 (CurrentClampSeries) no description
  Group /acquisition/loose seal recording for movie 6/electrode (IntracellularElectrode) 
  Group /acquisition/loose seal recording for movie 6/electrode/device (Device) Multiclamp 700B with 20 kHz low-pass filter
  Group /acquisition/loose seal recording for movie 7 (CurrentClampSeries) no description
  Group /acquisition/loose seal recording for movie 7/electrode (IntracellularElectrode) 
  Group /acquisition/loose seal recording for movie 7/electrode/device (Device) Multiclamp 700B with 20 kHz low-pass filter
  Group /acquisition/loose seal recording for movie 8 (CurrentClampSeries) no description
  Group /acquisition/loose seal recording for movie 8/electrode (IntracellularElectrode) 
  Group /acquisition/loose seal recording for movie 8/electrode/device (Device) Multiclamp 700B with 20 kHz low-pass filter
  Group /analysis/responses (IntracellularResponsesTable) Table for storing intracellular response related metadata.
  Dataset /analysis/responses/ap_snr (VectorData) signal to noise ratio of detected loose-seal action potential | shape = (1975,) | dtype = float64
  Dataset /analysis/responses/ap_time (VectorData) peak time of detected loose-seal action potential | shape = (1975,) | dtype = float64
  Dataset /analysis/responses/id (ElementIdentifiers)  | shape = (1975,) | dtype = int64
  Dataset /analysis/responses/response (TimeSeriesReferenceVectorData) Column storing the reference to the recorded response for the recording (rows) | shape = (1975,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  file_create_date: ['2022-11-27T22:39:29.406410-08:00']
  Group /general/devices/MMIMS: custom-built two-photon microscope with a resonant scanner (Device) 
  Group /general/devices/Multiclamp 700B (Device) Multiclamp 700B with 20 kHz low-pass filter
  experiment_description: Simultaneous loose-seal cell-attached recordings and two-photon imaging of GCaMP (jGCaMP8s/m/f, jGCaMP7f, XCaMPgf) expressing mouse visual cortex neurons (pyramidal cells and FS interneurons) with drifting gratings visual stimuli
  experimenter: ['Marton Rozsa']
  institution: GENIE project, HHMI Janelia Research Campus
  Group /general/intracellular_ephys/Micropipette (IntracellularElectrode) 
  Group /general/intracellular_ephys/Micropipette/device (Device) Multiclamp 700B with 20 kHz low-pass filter
  Group /general/intracellular_ephys/sweep_table (SweepTable) A sweep table groups different PatchClampSeries together.
  Dataset /general/intracellular_ephys/sweep_table/id (ElementIdentifiers)  | shape = (9,) | dtype = int64
  Dataset /general/intracellular_ephys/sweep_table/series (VectorData) PatchClampSeries with the same sweep number | shape = (9,) | dtype = object
  Dataset /general/intracellular_ephys/sweep_table/series_index (VectorIndex) Index for VectorData 'series' | shape = (9,) | dtype = uint8
  Dataset /general/intracellular_ephys/sweep_table/sweep_number (VectorData) Sweep number of the entries in that row | shape = (9,) | dtype = uint64
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
  Group /general/optophysiology/Movie_5 (ImagingPlane) 
  Group /general/optophysiology/Movie_5/device (Device) 
  Group /general/optophysiology/Movie_5/green (OpticalChannel) 
  Group /general/optophysiology/Movie_6 (ImagingPlane) 
  Group /general/optophysiology/Movie_6/device (Device) 
  Group /general/optophysiology/Movie_6/green (OpticalChannel) 
  Group /general/optophysiology/Movie_7 (ImagingPlane) 
  Group /general/optophysiology/Movie_7/device (Device) 
  Group /general/optophysiology/Movie_7/green (OpticalChannel) 
  Group /general/optophysiology/Movie_8 (ImagingPlane) 
  Group /general/optophysiology/Movie_8/device (Device) 
  Group /general/optophysiology/Movie_8/green (OpticalChannel) 
  related_publications: ['10.25378/janelia.13148243' '10.1101/2021.11.08.467793']
  session_id: jGCaMP8f_ANM471993_cell03
  Group /general/subject (Subject) 
  surgery: [{"surgery_id": "1", "start_time": "2020-03-08 12:00:00", "end_time": "2020-03-08 12:50:00", "surgery_description": "headbar, craniotomy, virus injection, window:-: comments: nan"}, {"surgery_id": "2", "start_time": "2020-05-08 16:20:00", "end_time": "2020-05-08 17:25:00", "surgery_description": "window removal:-: comments: boneflap and dura removed, light swelling, bleeding"}]
  virus: [{"surgery_id": "1", "injection_id": "1", "virus_id": "10250", "skull_reference": "Lambda", "ml_location": "2300.000", "ap_location": "0.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-6xHis-noRSET-1NIW_Q315L_N19T_S24I_S26R_Q88E_LKI_GCaMP6s-WPRE.547.456", "titer": "32600000000000.0", "order_date": "2020-01-27", "remarks": "Ultrafast GCaMP456 ref: 1-1001-1"}, {"surgery_id": "1", "injection_id": "2", "virus_id": "10250", "skull_reference": "Lambda", "ml_location": "2800.000", "ap_location": "0.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-6xHis-noRSET-1NIW_Q315L_N19T_S24I_S26R_Q88E_LKI_GCaMP6s-WPRE.547.456", "titer": "32600000000000.0", "order_date": "2020-01-27", "remarks": "Ultrafast GCaMP456 ref: 1-1001-1"}, {"surgery_id": "1", "injection_id": "3", "virus_id": "10250", "skull_reference": "Lambda", "ml_location": "2800.000", "ap_location": "500.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-6xHis-noRSET-1NIW_Q315L_N19T_S24I_S26R_Q88E_LKI_GCaMP6s-WPRE.547.456", "titer": "32600000000000.0", "order_date": "2020-01-27", "remarks": "Ultrafast GCaMP456 ref: 1-1001-1"}, {"surgery_id": "1", "injection_id": "4", "virus_id": "10250", "skull_reference": "Lambda", "ml_location": "2300.000", "ap_location": "500.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-6xHis-noRSET-1NIW_Q315L_N19T_S24I_S26R_Q88E_LKI_GCaMP6s-WPRE.547.456", "titer": "32600000000000.0", "order_date": "2020-01-27", "remarks": "Ultrafast GCaMP456 ref: 1-1001-1"}, {"surgery_id": "1", "injection_id": "5", "virus_id": "10250", "skull_reference": "Lambda", "ml_location": "2300.000", "ap_location": "0.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-6xHis-noRSET-1NIW_Q315L_N19T_S24I_S26R_Q88E_LKI_GCaMP6s-WPRE.547.456", "titer": "32600000000000.0", "order_date": "2020-01-27", "remarks": "Ultrafast GCaMP456 ref: 1-1001-1"}, {"surgery_id": "1", "injection_id": "6", "virus_id": "10250", "skull_reference": "Lambda", "ml_location": "2800.000", "ap_location": "0.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-6xHis-noRSET-1NIW_Q315L_N19T_S24I_S26R_Q88E_LKI_GCaMP6s-WPRE.547.456", "titer": "32600000000000.0", "order_date": "2020-01-27", "remarks": "Ultrafast GCaMP456 ref: 1-1001-1"}, {"surgery_id": "1", "injection_id": "7", "virus_id": "10250", "skull_reference": "Lambda", "ml_location": "2800.000", "ap_location": "500.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-6xHis-noRSET-1NIW_Q315L_N19T_S24I_S26R_Q88E_LKI_GCaMP6s-WPRE.547.456", "titer": "32600000000000.0", "order_date": "2020-01-27", "remarks": "Ultrafast GCaMP456 ref: 1-1001-1"}, {"surgery_id": "1", "injection_id": "8", "virus_id": "10250", "skull_reference": "Lambda", "ml_location": "2300.000", "ap_location": "500.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-6xHis-noRSET-1NIW_Q315L_N19T_S24I_S26R_Q88E_LKI_GCaMP6s-WPRE.547.456", "titer": "32600000000000.0", "order_date": "2020-01-27", "remarks": "Ultrafast GCaMP456 ref: 1-1001-1"}, {"surgery_id": "1", "injection_id": "9", "virus_id": "10250", "skull_reference": "Lambda", "ml_location": "2300.000", "ap_location": "0.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-6xHis-noRSET-1NIW_Q315L_N19T_S24I_S26R_Q88E_LKI_GCaMP6s-WPRE.547.456", "titer": "32600000000000.0", "order_date": "2020-01-27", "remarks": "Ultrafast GCaMP456 ref: 1-1001-1"}, {"surgery_id": "1", "injection_id": "10", "virus_id": "10250", "skull_reference": "Lambda", "ml_location": "2800.000", "ap_location": "0.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-6xHis-noRSET-1NIW_Q315L_N19T_S24I_S26R_Q88E_LKI_GCaMP6s-WPRE.547.456", "titer": "32600000000000.0", "order_date": "2020-01-27", "remarks": "Ultrafast GCaMP456 ref: 1-1001-1"}, {"surgery_id": "1", "injection_id": "11", "virus_id": "10250", "skull_reference": "Lambda", "ml_location": "2800.000", "ap_location": "500.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-6xHis-noRSET-1NIW_Q315L_N19T_S24I_S26R_Q88E_LKI_GCaMP6s-WPRE.547.456", "titer": "32600000000000.0", "order_date": "2020-01-27", "remarks": "Ultrafast GCaMP456 ref: 1-1001-1"}, {"surgery_id": "1", "injection_id": "12", "virus_id": "10250", "skull_reference": "Lambda", "ml_location": "2300.000", "ap_location": "500.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-6xHis-noRSET-1NIW_Q315L_N19T_S24I_S26R_Q88E_LKI_GCaMP6s-WPRE.547.456", "titer": "32600000000000.0", "order_date": "2020-01-27", "remarks": "Ultrafast GCaMP456 ref: 1-1001-1"}]
  identifier: jGCaMP8f_ANM471993_cell03
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (9,) | dtype = int64
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (9,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (9,) | dtype = float64
  Dataset /intervals/epochs/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (27,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  Dataset /intervals/epochs/timeseries_index (VectorIndex) Index for VectorData 'timeseries' | shape = (9,) | dtype = uint8
  Group /intervals/trials (TimeIntervals) experimental trials
  Dataset /intervals/trials/amplitude (VectorData) amplitude of drifting grating stimulus | shape = (360,) | dtype = float64
  Dataset /intervals/trials/angle (VectorData) angle of drifting grating stimulus in degrees | shape = (360,) | dtype = int64
  Dataset /intervals/trials/cycles_per_degree (VectorData) cycles per degree of drifting grating stimulus | shape = (360,) | dtype = float64
  Dataset /intervals/trials/cycles_per_second (VectorData) cycles per second of drifting grating stimulus | shape = (360,) | dtype = float64
  Dataset /intervals/trials/id (ElementIdentifiers)  | shape = (360,) | dtype = int64
  Dataset /intervals/trials/movie_number (VectorData) during which movie this visual stimulus happened | shape = (360,) | dtype = int64
  Dataset /intervals/trials/start_time (VectorData) Start time of epoch, in seconds | shape = (360,) | dtype = float64
  Dataset /intervals/trials/stop_time (VectorData) Stop time of epoch, in seconds | shape = (360,) | dtype = float64
  Group /processing/ophys of movie 0 (ProcessingModule) Processing result of imaging
  Group /processing/ophys of movie 0/Fluorescence (Fluorescence) 
  Group /processing/ophys of movie 0/Fluorescence/NeuropilResponseSeries (RoiResponseSeries) average fluorescence of the neuropil surrounding the roi
  Dataset /processing/ophys of movie 0/Fluorescence/NeuropilResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (2,) | dtype = int64
  Group /processing/ophys of movie 0/Fluorescence/RoiResponseSeries (RoiResponseSeries) weighted average fluorescence of roi
  Dataset /processing/ophys of movie 0/Fluorescence/RoiResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (2,) | dtype = int64
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
  Dataset /processing/ophys of movie 0/mean images of movie 0/jGCaMP8f at 940nm (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Group /processing/ophys of movie 1 (ProcessingModule) Processing result of imaging
  Group /processing/ophys of movie 1/Fluorescence (Fluorescence) 
  Group /processing/ophys of movie 1/Fluorescence/NeuropilResponseSeries (RoiResponseSeries) average fluorescence of the neuropil surrounding the roi
  Dataset /processing/ophys of movie 1/Fluorescence/NeuropilResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (2,) | dtype = int64
  Group /processing/ophys of movie 1/Fluorescence/RoiResponseSeries (RoiResponseSeries) weighted average fluorescence of roi
  Dataset /processing/ophys of movie 1/Fluorescence/RoiResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (2,) | dtype = int64
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
  Dataset /processing/ophys of movie 1/mean images of movie 1/jGCaMP8f at 940nm (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Group /processing/ophys of movie 2 (ProcessingModule) Processing result of imaging
  Group /processing/ophys of movie 2/Fluorescence (Fluorescence) 
  Group /processing/ophys of movie 2/Fluorescence/NeuropilResponseSeries (RoiResponseSeries) average fluorescence of the neuropil surrounding the roi
  Dataset /processing/ophys of movie 2/Fluorescence/NeuropilResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (2,) | dtype = int64
  Group /processing/ophys of movie 2/Fluorescence/RoiResponseSeries (RoiResponseSeries) weighted average fluorescence of roi
  Dataset /processing/ophys of movie 2/Fluorescence/RoiResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (2,) | dtype = int64
  Group /processing/ophys of movie 2/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation (PlaneSegmentation) output from segmenting with Suite2p, ROI 0 is the neuron recorded with electrophysiology
  Dataset /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation/cell_type (VectorData) pyr for putative pyramidal cells, int for putative interneurons, based on average loose-seal spike shape | shape = (2,) | dtype = object
  Dataset /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation/id (ElementIdentifiers)  | shape = (2,) | dtype = int64
  Dataset /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (2, 512, 128) | dtype = float64
  Group /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation/imaging_plane/device (Device) 
  Group /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation/imaging_plane/green (OpticalChannel) 
  Dataset /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation/neuropil_mask (VectorData) mask of neuropil surrounding this roi | shape = (2, 512, 128) | dtype = bool
  Dataset /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation/recorded_with_ephys (VectorData) whether this ROI is simultaneously loose-seal recorded | shape = (2,) | dtype = bool
  Group /processing/ophys of movie 2/mean images of movie 2 (Images) Structural images of a scanning
  Dataset /processing/ophys of movie 2/mean images of movie 2/Alexa Fluor 594 in pipette (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Dataset /processing/ophys of movie 2/mean images of movie 2/jGCaMP8f at 940nm (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Group /processing/ophys of movie 3 (ProcessingModule) Processing result of imaging
  Group /processing/ophys of movie 3/Fluorescence (Fluorescence) 
  Group /processing/ophys of movie 3/Fluorescence/NeuropilResponseSeries (RoiResponseSeries) average fluorescence of the neuropil surrounding the roi
  Dataset /processing/ophys of movie 3/Fluorescence/NeuropilResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (2,) | dtype = int64
  Group /processing/ophys of movie 3/Fluorescence/RoiResponseSeries (RoiResponseSeries) weighted average fluorescence of roi
  Dataset /processing/ophys of movie 3/Fluorescence/RoiResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (2,) | dtype = int64
  Group /processing/ophys of movie 3/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys of movie 3/ImageSegmentation/MovieSegmentation (PlaneSegmentation) output from segmenting with Suite2p, ROI 0 is the neuron recorded with electrophysiology
  Dataset /processing/ophys of movie 3/ImageSegmentation/MovieSegmentation/cell_type (VectorData) pyr for putative pyramidal cells, int for putative interneurons, based on average loose-seal spike shape | shape = (2,) | dtype = object
  Dataset /processing/ophys of movie 3/ImageSegmentation/MovieSegmentation/id (ElementIdentifiers)  | shape = (2,) | dtype = int64
  Dataset /processing/ophys of movie 3/ImageSegmentation/MovieSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (2, 512, 128) | dtype = float64
  Group /processing/ophys of movie 3/ImageSegmentation/MovieSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys of movie 3/ImageSegmentation/MovieSegmentation/imaging_plane/device (Device) 
  Group /processing/ophys of movie 3/ImageSegmentation/MovieSegmentation/imaging_plane/green (OpticalChannel) 
  Dataset /processing/ophys of movie 3/ImageSegmentation/MovieSegmentation/neuropil_mask (VectorData) mask of neuropil surrounding this roi | shape = (2, 512, 128) | dtype = bool
  Dataset /processing/ophys of movie 3/ImageSegmentation/MovieSegmentation/recorded_with_ephys (VectorData) whether this ROI is simultaneously loose-seal recorded | shape = (2,) | dtype = bool
  Group /processing/ophys of movie 3/mean images of movie 3 (Images) Structural images of a scanning
  Dataset /processing/ophys of movie 3/mean images of movie 3/Alexa Fluor 594 in pipette (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Dataset /processing/ophys of movie 3/mean images of movie 3/jGCaMP8f at 940nm (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Group /processing/ophys of movie 4 (ProcessingModule) Processing result of imaging
  Group /processing/ophys of movie 4/Fluorescence (Fluorescence) 
  Group /processing/ophys of movie 4/Fluorescence/NeuropilResponseSeries (RoiResponseSeries) average fluorescence of the neuropil surrounding the roi
  Dataset /processing/ophys of movie 4/Fluorescence/NeuropilResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (1,) | dtype = int64
  Group /processing/ophys of movie 4/Fluorescence/RoiResponseSeries (RoiResponseSeries) weighted average fluorescence of roi
  Dataset /processing/ophys of movie 4/Fluorescence/RoiResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (1,) | dtype = int64
  Group /processing/ophys of movie 4/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys of movie 4/ImageSegmentation/MovieSegmentation (PlaneSegmentation) output from segmenting with Suite2p, ROI 0 is the neuron recorded with electrophysiology
  Dataset /processing/ophys of movie 4/ImageSegmentation/MovieSegmentation/cell_type (VectorData) pyr for putative pyramidal cells, int for putative interneurons, based on average loose-seal spike shape | shape = (1,) | dtype = object
  Dataset /processing/ophys of movie 4/ImageSegmentation/MovieSegmentation/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /processing/ophys of movie 4/ImageSegmentation/MovieSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (1, 512, 128) | dtype = float64
  Group /processing/ophys of movie 4/ImageSegmentation/MovieSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys of movie 4/ImageSegmentation/MovieSegmentation/imaging_plane/device (Device) 
  Group /processing/ophys of movie 4/ImageSegmentation/MovieSegmentation/imaging_plane/green (OpticalChannel) 
  Dataset /processing/ophys of movie 4/ImageSegmentation/MovieSegmentation/neuropil_mask (VectorData) mask of neuropil surrounding this roi | shape = (1, 512, 128) | dtype = bool
  Dataset /processing/ophys of movie 4/ImageSegmentation/MovieSegmentation/recorded_with_ephys (VectorData) whether this ROI is simultaneously loose-seal recorded | shape = (1,) | dtype = bool
  Group /processing/ophys of movie 4/mean images of movie 4 (Images) Structural images of a scanning
  Dataset /processing/ophys of movie 4/mean images of movie 4/Alexa Fluor 594 in pipette (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Dataset /processing/ophys of movie 4/mean images of movie 4/jGCaMP8f at 940nm (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Group /processing/ophys of movie 5 (ProcessingModule) Processing result of imaging
  Group /processing/ophys of movie 5/Fluorescence (Fluorescence) 
  Group /processing/ophys of movie 5/Fluorescence/NeuropilResponseSeries (RoiResponseSeries) average fluorescence of the neuropil surrounding the roi
  Dataset /processing/ophys of movie 5/Fluorescence/NeuropilResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (3,) | dtype = int64
  Group /processing/ophys of movie 5/Fluorescence/RoiResponseSeries (RoiResponseSeries) weighted average fluorescence of roi
  Dataset /processing/ophys of movie 5/Fluorescence/RoiResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (3,) | dtype = int64
  Group /processing/ophys of movie 5/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys of movie 5/ImageSegmentation/MovieSegmentation (PlaneSegmentation) output from segmenting with Suite2p, ROI 0 is the neuron recorded with electrophysiology
  Dataset /processing/ophys of movie 5/ImageSegmentation/MovieSegmentation/cell_type (VectorData) pyr for putative pyramidal cells, int for putative interneurons, based on average loose-seal spike shape | shape = (3,) | dtype = object
  Dataset /processing/ophys of movie 5/ImageSegmentation/MovieSegmentation/id (ElementIdentifiers)  | shape = (3,) | dtype = int64
  Dataset /processing/ophys of movie 5/ImageSegmentation/MovieSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (3, 512, 128) | dtype = float64
  Group /processing/ophys of movie 5/ImageSegmentation/MovieSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys of movie 5/ImageSegmentation/MovieSegmentation/imaging_plane/device (Device) 
  Group /processing/ophys of movie 5/ImageSegmentation/MovieSegmentation/imaging_plane/green (OpticalChannel) 
  Dataset /processing/ophys of movie 5/ImageSegmentation/MovieSegmentation/neuropil_mask (VectorData) mask of neuropil surrounding this roi | shape = (3, 512, 128) | dtype = bool
  Dataset /processing/ophys of movie 5/ImageSegmentation/MovieSegmentation/recorded_with_ephys (VectorData) whether this ROI is simultaneously loose-seal recorded | shape = (3,) | dtype = bool
  Group /processing/ophys of movie 5/mean images of movie 5 (Images) Structural images of a scanning
  Dataset /processing/ophys of movie 5/mean images of movie 5/Alexa Fluor 594 in pipette (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Dataset /processing/ophys of movie 5/mean images of movie 5/jGCaMP8f at 940nm (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Group /processing/ophys of movie 6 (ProcessingModule) Processing result of imaging
  Group /processing/ophys of movie 6/Fluorescence (Fluorescence) 
  Group /processing/ophys of movie 6/Fluorescence/NeuropilResponseSeries (RoiResponseSeries) average fluorescence of the neuropil surrounding the roi
  Dataset /processing/ophys of movie 6/Fluorescence/NeuropilResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (3,) | dtype = int64
  Group /processing/ophys of movie 6/Fluorescence/RoiResponseSeries (RoiResponseSeries) weighted average fluorescence of roi
  Dataset /processing/ophys of movie 6/Fluorescence/RoiResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (3,) | dtype = int64
  Group /processing/ophys of movie 6/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys of movie 6/ImageSegmentation/MovieSegmentation (PlaneSegmentation) output from segmenting with Suite2p, ROI 0 is the neuron recorded with electrophysiology
  Dataset /processing/ophys of movie 6/ImageSegmentation/MovieSegmentation/cell_type (VectorData) pyr for putative pyramidal cells, int for putative interneurons, based on average loose-seal spike shape | shape = (3,) | dtype = object
  Dataset /processing/ophys of movie 6/ImageSegmentation/MovieSegmentation/id (ElementIdentifiers)  | shape = (3,) | dtype = int64
  Dataset /processing/ophys of movie 6/ImageSegmentation/MovieSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (3, 512, 128) | dtype = float64
  Group /processing/ophys of movie 6/ImageSegmentation/MovieSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys of movie 6/ImageSegmentation/MovieSegmentation/imaging_plane/device (Device) 
  Group /processing/ophys of movie 6/ImageSegmentation/MovieSegmentation/imaging_plane/green (OpticalChannel) 
  Dataset /processing/ophys of movie 6/ImageSegmentation/MovieSegmentation/neuropil_mask (VectorData) mask of neuropil surrounding this roi | shape = (3, 512, 128) | dtype = bool
  Dataset /processing/ophys of movie 6/ImageSegmentation/MovieSegmentation/recorded_with_ephys (VectorData) whether this ROI is simultaneously loose-seal recorded | shape = (3,) | dtype = bool
  Group /processing/ophys of movie 6/mean images of movie 6 (Images) Structural images of a scanning
  Dataset /processing/ophys of movie 6/mean images of movie 6/Alexa Fluor 594 in pipette (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Dataset /processing/ophys of movie 6/mean images of movie 6/jGCaMP8f at 940nm (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Group /processing/ophys of movie 7 (ProcessingModule) Processing result of imaging
  Group /processing/ophys of movie 7/Fluorescence (Fluorescence) 
  Group /processing/ophys of movie 7/Fluorescence/NeuropilResponseSeries (RoiResponseSeries) average fluorescence of the neuropil surrounding the roi
  Dataset /processing/ophys of movie 7/Fluorescence/NeuropilResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (1,) | dtype = int64
  Group /processing/ophys of movie 7/Fluorescence/RoiResponseSeries (RoiResponseSeries) weighted average fluorescence of roi
  Dataset /processing/ophys of movie 7/Fluorescence/RoiResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (1,) | dtype = int64
  Group /processing/ophys of movie 7/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys of movie 7/ImageSegmentation/MovieSegmentation (PlaneSegmentation) output from segmenting with Suite2p, ROI 0 is the neuron recorded with electrophysiology
  Dataset /processing/ophys of movie 7/ImageSegmentation/MovieSegmentation/cell_type (VectorData) pyr for putative pyramidal cells, int for putative interneurons, based on average loose-seal spike shape | shape = (1,) | dtype = object
  Dataset /processing/ophys of movie 7/ImageSegmentation/MovieSegmentation/id (ElementIdentifiers)  | shape = (1,) | dtype = int64
  Dataset /processing/ophys of movie 7/ImageSegmentation/MovieSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (1, 512, 128) | dtype = float64
  Group /processing/ophys of movie 7/ImageSegmentation/MovieSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys of movie 7/ImageSegmentation/MovieSegmentation/imaging_plane/device (Device) 
  Group /processing/ophys of movie 7/ImageSegmentation/MovieSegmentation/imaging_plane/green (OpticalChannel) 
  Dataset /processing/ophys of movie 7/ImageSegmentation/MovieSegmentation/neuropil_mask (VectorData) mask of neuropil surrounding this roi | shape = (1, 512, 128) | dtype = bool
  Dataset /processing/ophys of movie 7/ImageSegmentation/MovieSegmentation/recorded_with_ephys (VectorData) whether this ROI is simultaneously loose-seal recorded | shape = (1,) | dtype = bool
  Group /processing/ophys of movie 7/mean images of movie 7 (Images) Structural images of a scanning
  Dataset /processing/ophys of movie 7/mean images of movie 7/Alexa Fluor 594 in pipette (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Dataset /processing/ophys of movie 7/mean images of movie 7/jGCaMP8f at 940nm (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Group /processing/ophys of movie 8 (ProcessingModule) Processing result of imaging
  Group /processing/ophys of movie 8/Fluorescence (Fluorescence) 
  Group /processing/ophys of movie 8/Fluorescence/NeuropilResponseSeries (RoiResponseSeries) average fluorescence of the neuropil surrounding the roi
  Dataset /processing/ophys of movie 8/Fluorescence/NeuropilResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (3,) | dtype = int64
  Group /processing/ophys of movie 8/Fluorescence/RoiResponseSeries (RoiResponseSeries) weighted average fluorescence of roi
  Dataset /processing/ophys of movie 8/Fluorescence/RoiResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (3,) | dtype = int64
  Group /processing/ophys of movie 8/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys of movie 8/ImageSegmentation/MovieSegmentation (PlaneSegmentation) output from segmenting with Suite2p, ROI 0 is the neuron recorded with electrophysiology
  Dataset /processing/ophys of movie 8/ImageSegmentation/MovieSegmentation/cell_type (VectorData) pyr for putative pyramidal cells, int for putative interneurons, based on average loose-seal spike shape | shape = (3,) | dtype = object
  Dataset /processing/ophys of movie 8/ImageSegmentation/MovieSegmentation/id (ElementIdentifiers)  | shape = (3,) | dtype = int64
  Dataset /processing/ophys of movie 8/ImageSegmentation/MovieSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (3, 512, 128) | dtype = float64
  Group /processing/ophys of movie 8/ImageSegmentation/MovieSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys of movie 8/ImageSegmentation/MovieSegmentation/imaging_plane/device (Device) 
  Group /processing/ophys of movie 8/ImageSegmentation/MovieSegmentation/imaging_plane/green (OpticalChannel) 
  Dataset /processing/ophys of movie 8/ImageSegmentation/MovieSegmentation/neuropil_mask (VectorData) mask of neuropil surrounding this roi | shape = (3, 512, 128) | dtype = bool
  Dataset /processing/ophys of movie 8/ImageSegmentation/MovieSegmentation/recorded_with_ephys (VectorData) whether this ROI is simultaneously loose-seal recorded | shape = (3,) | dtype = bool
  Group /processing/ophys of movie 8/mean images of movie 8 (Images) Structural images of a scanning
  Dataset /processing/ophys of movie 8/mean images of movie 8/Alexa Fluor 594 in pipette (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Dataset /processing/ophys of movie 8/mean images of movie 8/jGCaMP8f at 940nm (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  session_description: 
  session_start_time: 2020-05-08T21:38:42-07:00
  timestamps_reference_time: 2020-05-08T21:38:42-07:00


Here is a summary of the type 4 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Raw movie 0 (TwoPhotonSeries) no description
  Group /acquisition/Raw movie 0/imaging_plane (ImagingPlane) 
  Group /acquisition/Raw movie 0/imaging_plane/device (Device) 
  Group /acquisition/Raw movie 0/imaging_plane/green (OpticalChannel) 
  Group /acquisition/Raw movie 1 (TwoPhotonSeries) no description
  Group /acquisition/Raw movie 1/imaging_plane (ImagingPlane) 
  Group /acquisition/Raw movie 1/imaging_plane/device (Device) 
  Group /acquisition/Raw movie 1/imaging_plane/green (OpticalChannel) 
  Group /acquisition/Raw movie 2 (TwoPhotonSeries) no description
  Group /acquisition/Raw movie 2/imaging_plane (ImagingPlane) 
  Group /acquisition/Raw movie 2/imaging_plane/device (Device) 
  Group /acquisition/Raw movie 2/imaging_plane/green (OpticalChannel) 
  Group /acquisition/Raw movie 3 (TwoPhotonSeries) no description
  Group /acquisition/Raw movie 3/imaging_plane (ImagingPlane) 
  Group /acquisition/Raw movie 3/imaging_plane/device (Device) 
  Group /acquisition/Raw movie 3/imaging_plane/green (OpticalChannel) 
  Group /acquisition/Raw movie 4 (TwoPhotonSeries) no description
  Group /acquisition/Raw movie 4/imaging_plane (ImagingPlane) 
  Group /acquisition/Raw movie 4/imaging_plane/device (Device) 
  Group /acquisition/Raw movie 4/imaging_plane/green (OpticalChannel) 
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
  Dataset /analysis/responses/ap_snr (VectorData) signal to noise ratio of detected loose-seal action potential | shape = (1688,) | dtype = float64
  Dataset /analysis/responses/ap_time (VectorData) peak time of detected loose-seal action potential | shape = (1688,) | dtype = float64
  Dataset /analysis/responses/id (ElementIdentifiers)  | shape = (1688,) | dtype = int64
  Dataset /analysis/responses/response (TimeSeriesReferenceVectorData) Column storing the reference to the recorded response for the recording (rows) | shape = (1688,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  file_create_date: ['2022-11-27T23:14:04.868996-08:00']
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
  session_id: jGCaMP8f_ANM471994_cell01
  Group /general/subject (Subject) 
  surgery: [{"surgery_id": "1", "start_time": "2020-03-08 12:00:00", "end_time": "2020-03-08 12:50:00", "surgery_description": "headbar, craniotomy, virus injection, window:-: comments: nan"}, {"surgery_id": "2", "start_time": "2020-05-09 16:10:00", "end_time": "2020-05-09 17:00:00", "surgery_description": "window removal:-: comments: nice prep"}]
  virus: [{"surgery_id": "1", "injection_id": "1", "virus_id": "10250", "skull_reference": "Lambda", "ml_location": "2200.000", "ap_location": "0.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-6xHis-noRSET-1NIW_Q315L_N19T_S24I_S26R_Q88E_LKI_GCaMP6s-WPRE.547.456", "titer": "32600000000000.0", "order_date": "2020-01-27", "remarks": "Ultrafast GCaMP456 ref: 1-1001-1"}, {"surgery_id": "1", "injection_id": "2", "virus_id": "10250", "skull_reference": "Lambda", "ml_location": "2800.000", "ap_location": "0.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-6xHis-noRSET-1NIW_Q315L_N19T_S24I_S26R_Q88E_LKI_GCaMP6s-WPRE.547.456", "titer": "32600000000000.0", "order_date": "2020-01-27", "remarks": "Ultrafast GCaMP456 ref: 1-1001-1"}, {"surgery_id": "1", "injection_id": "3", "virus_id": "10250", "skull_reference": "Lambda", "ml_location": "2800.000", "ap_location": "600.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-6xHis-noRSET-1NIW_Q315L_N19T_S24I_S26R_Q88E_LKI_GCaMP6s-WPRE.547.456", "titer": "32600000000000.0", "order_date": "2020-01-27", "remarks": "Ultrafast GCaMP456 ref: 1-1001-1"}, {"surgery_id": "1", "injection_id": "4", "virus_id": "10250", "skull_reference": "Lambda", "ml_location": "2300.000", "ap_location": "600.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-6xHis-noRSET-1NIW_Q315L_N19T_S24I_S26R_Q88E_LKI_GCaMP6s-WPRE.547.456", "titer": "32600000000000.0", "order_date": "2020-01-27", "remarks": "Ultrafast GCaMP456 ref: 1-1001-1"}, {"surgery_id": "1", "injection_id": "5", "virus_id": "10250", "skull_reference": "Lambda", "ml_location": "2200.000", "ap_location": "0.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-6xHis-noRSET-1NIW_Q315L_N19T_S24I_S26R_Q88E_LKI_GCaMP6s-WPRE.547.456", "titer": "32600000000000.0", "order_date": "2020-01-27", "remarks": "Ultrafast GCaMP456 ref: 1-1001-1"}, {"surgery_id": "1", "injection_id": "6", "virus_id": "10250", "skull_reference": "Lambda", "ml_location": "2800.000", "ap_location": "0.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-6xHis-noRSET-1NIW_Q315L_N19T_S24I_S26R_Q88E_LKI_GCaMP6s-WPRE.547.456", "titer": "32600000000000.0", "order_date": "2020-01-27", "remarks": "Ultrafast GCaMP456 ref: 1-1001-1"}, {"surgery_id": "1", "injection_id": "7", "virus_id": "10250", "skull_reference": "Lambda", "ml_location": "2800.000", "ap_location": "600.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-6xHis-noRSET-1NIW_Q315L_N19T_S24I_S26R_Q88E_LKI_GCaMP6s-WPRE.547.456", "titer": "32600000000000.0", "order_date": "2020-01-27", "remarks": "Ultrafast GCaMP456 ref: 1-1001-1"}, {"surgery_id": "1", "injection_id": "8", "virus_id": "10250", "skull_reference": "Lambda", "ml_location": "2300.000", "ap_location": "600.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-6xHis-noRSET-1NIW_Q315L_N19T_S24I_S26R_Q88E_LKI_GCaMP6s-WPRE.547.456", "titer": "32600000000000.0", "order_date": "2020-01-27", "remarks": "Ultrafast GCaMP456 ref: 1-1001-1"}, {"surgery_id": "1", "injection_id": "9", "virus_id": "10250", "skull_reference": "Lambda", "ml_location": "2200.000", "ap_location": "0.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-6xHis-noRSET-1NIW_Q315L_N19T_S24I_S26R_Q88E_LKI_GCaMP6s-WPRE.547.456", "titer": "32600000000000.0", "order_date": "2020-01-27", "remarks": "Ultrafast GCaMP456 ref: 1-1001-1"}, {"surgery_id": "1", "injection_id": "10", "virus_id": "10250", "skull_reference": "Lambda", "ml_location": "2800.000", "ap_location": "0.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-6xHis-noRSET-1NIW_Q315L_N19T_S24I_S26R_Q88E_LKI_GCaMP6s-WPRE.547.456", "titer": "32600000000000.0", "order_date": "2020-01-27", "remarks": "Ultrafast GCaMP456 ref: 1-1001-1"}, {"surgery_id": "1", "injection_id": "11", "virus_id": "10250", "skull_reference": "Lambda", "ml_location": "2800.000", "ap_location": "600.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-6xHis-noRSET-1NIW_Q315L_N19T_S24I_S26R_Q88E_LKI_GCaMP6s-WPRE.547.456", "titer": "32600000000000.0", "order_date": "2020-01-27", "remarks": "Ultrafast GCaMP456 ref: 1-1001-1"}, {"surgery_id": "1", "injection_id": "12", "virus_id": "10250", "skull_reference": "Lambda", "ml_location": "2300.000", "ap_location": "600.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-6xHis-noRSET-1NIW_Q315L_N19T_S24I_S26R_Q88E_LKI_GCaMP6s-WPRE.547.456", "titer": "32600000000000.0", "order_date": "2020-01-27", "remarks": "Ultrafast GCaMP456 ref: 1-1001-1"}]
  identifier: jGCaMP8f_ANM471994_cell01
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (5,) | dtype = int64
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (5,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (5,) | dtype = float64
  Dataset /intervals/epochs/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (15,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
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
  Dataset /processing/ophys of movie 0/Fluorescence/NeuropilResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (10,) | dtype = int64
  Group /processing/ophys of movie 0/Fluorescence/RoiResponseSeries (RoiResponseSeries) weighted average fluorescence of roi
  Dataset /processing/ophys of movie 0/Fluorescence/RoiResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (10,) | dtype = int64
  Group /processing/ophys of movie 0/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation (PlaneSegmentation) output from segmenting with Suite2p, ROI 0 is the neuron recorded with electrophysiology
  Dataset /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/cell_type (VectorData) pyr for putative pyramidal cells, int for putative interneurons, based on average loose-seal spike shape | shape = (10,) | dtype = object
  Dataset /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/id (ElementIdentifiers)  | shape = (10,) | dtype = int64
  Dataset /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (10, 512, 128) | dtype = float64
  Group /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/imaging_plane/device (Device) 
  Group /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/imaging_plane/green (OpticalChannel) 
  Dataset /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/neuropil_mask (VectorData) mask of neuropil surrounding this roi | shape = (10, 512, 128) | dtype = bool
  Dataset /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/recorded_with_ephys (VectorData) whether this ROI is simultaneously loose-seal recorded | shape = (10,) | dtype = bool
  Group /processing/ophys of movie 0/mean images of movie 0 (Images) Structural images of a scanning
  Dataset /processing/ophys of movie 0/mean images of movie 0/Alexa Fluor 594 in pipette (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Dataset /processing/ophys of movie 0/mean images of movie 0/jGCaMP8f at 940nm (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Group /processing/ophys of movie 1 (ProcessingModule) Processing result of imaging
  Group /processing/ophys of movie 1/Fluorescence (Fluorescence) 
  Group /processing/ophys of movie 1/Fluorescence/NeuropilResponseSeries (RoiResponseSeries) average fluorescence of the neuropil surrounding the roi
  Dataset /processing/ophys of movie 1/Fluorescence/NeuropilResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (2,) | dtype = int64
  Group /processing/ophys of movie 1/Fluorescence/RoiResponseSeries (RoiResponseSeries) weighted average fluorescence of roi
  Dataset /processing/ophys of movie 1/Fluorescence/RoiResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (2,) | dtype = int64
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
  Dataset /processing/ophys of movie 1/mean images of movie 1/jGCaMP8f at 940nm (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Group /processing/ophys of movie 2 (ProcessingModule) Processing result of imaging
  Group /processing/ophys of movie 2/Fluorescence (Fluorescence) 
  Group /processing/ophys of movie 2/Fluorescence/NeuropilResponseSeries (RoiResponseSeries) average fluorescence of the neuropil surrounding the roi
  Dataset /processing/ophys of movie 2/Fluorescence/NeuropilResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (4,) | dtype = int64
  Group /processing/ophys of movie 2/Fluorescence/RoiResponseSeries (RoiResponseSeries) weighted average fluorescence of roi
  Dataset /processing/ophys of movie 2/Fluorescence/RoiResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (4,) | dtype = int64
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
  Dataset /processing/ophys of movie 2/mean images of movie 2/jGCaMP8f at 940nm (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Group /processing/ophys of movie 3 (ProcessingModule) Processing result of imaging
  Group /processing/ophys of movie 3/Fluorescence (Fluorescence) 
  Group /processing/ophys of movie 3/Fluorescence/NeuropilResponseSeries (RoiResponseSeries) average fluorescence of the neuropil surrounding the roi
  Dataset /processing/ophys of movie 3/Fluorescence/NeuropilResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (2,) | dtype = int64
  Group /processing/ophys of movie 3/Fluorescence/RoiResponseSeries (RoiResponseSeries) weighted average fluorescence of roi
  Dataset /processing/ophys of movie 3/Fluorescence/RoiResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (2,) | dtype = int64
  Group /processing/ophys of movie 3/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys of movie 3/ImageSegmentation/MovieSegmentation (PlaneSegmentation) output from segmenting with Suite2p, ROI 0 is the neuron recorded with electrophysiology
  Dataset /processing/ophys of movie 3/ImageSegmentation/MovieSegmentation/cell_type (VectorData) pyr for putative pyramidal cells, int for putative interneurons, based on average loose-seal spike shape | shape = (2,) | dtype = object
  Dataset /processing/ophys of movie 3/ImageSegmentation/MovieSegmentation/id (ElementIdentifiers)  | shape = (2,) | dtype = int64
  Dataset /processing/ophys of movie 3/ImageSegmentation/MovieSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (2, 512, 128) | dtype = float64
  Group /processing/ophys of movie 3/ImageSegmentation/MovieSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys of movie 3/ImageSegmentation/MovieSegmentation/imaging_plane/device (Device) 
  Group /processing/ophys of movie 3/ImageSegmentation/MovieSegmentation/imaging_plane/green (OpticalChannel) 
  Dataset /processing/ophys of movie 3/ImageSegmentation/MovieSegmentation/neuropil_mask (VectorData) mask of neuropil surrounding this roi | shape = (2, 512, 128) | dtype = bool
  Dataset /processing/ophys of movie 3/ImageSegmentation/MovieSegmentation/recorded_with_ephys (VectorData) whether this ROI is simultaneously loose-seal recorded | shape = (2,) | dtype = bool
  Group /processing/ophys of movie 3/mean images of movie 3 (Images) Structural images of a scanning
  Dataset /processing/ophys of movie 3/mean images of movie 3/Alexa Fluor 594 in pipette (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Dataset /processing/ophys of movie 3/mean images of movie 3/jGCaMP8f at 940nm (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Group /processing/ophys of movie 4 (ProcessingModule) Processing result of imaging
  Group /processing/ophys of movie 4/Fluorescence (Fluorescence) 
  Group /processing/ophys of movie 4/Fluorescence/NeuropilResponseSeries (RoiResponseSeries) average fluorescence of the neuropil surrounding the roi
  Dataset /processing/ophys of movie 4/Fluorescence/NeuropilResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (2,) | dtype = int64
  Group /processing/ophys of movie 4/Fluorescence/RoiResponseSeries (RoiResponseSeries) weighted average fluorescence of roi
  Dataset /processing/ophys of movie 4/Fluorescence/RoiResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (2,) | dtype = int64
  Group /processing/ophys of movie 4/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys of movie 4/ImageSegmentation/MovieSegmentation (PlaneSegmentation) output from segmenting with Suite2p, ROI 0 is the neuron recorded with electrophysiology
  Dataset /processing/ophys of movie 4/ImageSegmentation/MovieSegmentation/cell_type (VectorData) pyr for putative pyramidal cells, int for putative interneurons, based on average loose-seal spike shape | shape = (2,) | dtype = object
  Dataset /processing/ophys of movie 4/ImageSegmentation/MovieSegmentation/id (ElementIdentifiers)  | shape = (2,) | dtype = int64
  Dataset /processing/ophys of movie 4/ImageSegmentation/MovieSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (2, 512, 128) | dtype = float64
  Group /processing/ophys of movie 4/ImageSegmentation/MovieSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys of movie 4/ImageSegmentation/MovieSegmentation/imaging_plane/device (Device) 
  Group /processing/ophys of movie 4/ImageSegmentation/MovieSegmentation/imaging_plane/green (OpticalChannel) 
  Dataset /processing/ophys of movie 4/ImageSegmentation/MovieSegmentation/neuropil_mask (VectorData) mask of neuropil surrounding this roi | shape = (2, 512, 128) | dtype = bool
  Dataset /processing/ophys of movie 4/ImageSegmentation/MovieSegmentation/recorded_with_ephys (VectorData) whether this ROI is simultaneously loose-seal recorded | shape = (2,) | dtype = bool
  Group /processing/ophys of movie 4/mean images of movie 4 (Images) Structural images of a scanning
  Dataset /processing/ophys of movie 4/mean images of movie 4/Alexa Fluor 594 in pipette (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Dataset /processing/ophys of movie 4/mean images of movie 4/jGCaMP8f at 940nm (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  session_description: 
  session_start_time: 2020-05-09T18:25:40-07:00
  timestamps_reference_time: 2020-05-09T18:25:40-07:00


Here is a summary of the type 5 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Raw movie 0 (TwoPhotonSeries) no description
  Group /acquisition/Raw movie 0/imaging_plane (ImagingPlane) 
  Group /acquisition/Raw movie 0/imaging_plane/device (Device) 
  Group /acquisition/Raw movie 0/imaging_plane/green (OpticalChannel) 
  Group /acquisition/Raw movie 1 (TwoPhotonSeries) no description
  Group /acquisition/Raw movie 1/imaging_plane (ImagingPlane) 
  Group /acquisition/Raw movie 1/imaging_plane/device (Device) 
  Group /acquisition/Raw movie 1/imaging_plane/green (OpticalChannel) 
  Group /acquisition/Raw movie 2 (TwoPhotonSeries) no description
  Group /acquisition/Raw movie 2/imaging_plane (ImagingPlane) 
  Group /acquisition/Raw movie 2/imaging_plane/device (Device) 
  Group /acquisition/Raw movie 2/imaging_plane/green (OpticalChannel) 
  Group /acquisition/loose seal recording for movie 0 (CurrentClampSeries) no description
  Group /acquisition/loose seal recording for movie 0/electrode (IntracellularElectrode) 
  Group /acquisition/loose seal recording for movie 0/electrode/device (Device) Multiclamp 700B with 20 kHz low-pass filter
  Group /acquisition/loose seal recording for movie 1 (CurrentClampSeries) no description
  Group /acquisition/loose seal recording for movie 1/electrode (IntracellularElectrode) 
  Group /acquisition/loose seal recording for movie 1/electrode/device (Device) Multiclamp 700B with 20 kHz low-pass filter
  Group /acquisition/loose seal recording for movie 2 (CurrentClampSeries) no description
  Group /acquisition/loose seal recording for movie 2/electrode (IntracellularElectrode) 
  Group /acquisition/loose seal recording for movie 2/electrode/device (Device) Multiclamp 700B with 20 kHz low-pass filter
  Group /analysis/responses (IntracellularResponsesTable) Table for storing intracellular response related metadata.
  Dataset /analysis/responses/ap_snr (VectorData) signal to noise ratio of detected loose-seal action potential | shape = (75,) | dtype = float64
  Dataset /analysis/responses/ap_time (VectorData) peak time of detected loose-seal action potential | shape = (75,) | dtype = float64
  Dataset /analysis/responses/id (ElementIdentifiers)  | shape = (75,) | dtype = int64
  Dataset /analysis/responses/response (TimeSeriesReferenceVectorData) Column storing the reference to the recorded response for the recording (rows) | shape = (75,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
  file_create_date: ['2022-11-27T23:33:24.859772-08:00']
  Group /general/devices/MMIMS: custom-built two-photon microscope with a resonant scanner (Device) 
  Group /general/devices/Multiclamp 700B (Device) Multiclamp 700B with 20 kHz low-pass filter
  experiment_description: Simultaneous loose-seal cell-attached recordings and two-photon imaging of GCaMP (jGCaMP8s/m/f, jGCaMP7f, XCaMPgf) expressing mouse visual cortex neurons (pyramidal cells and FS interneurons) with drifting gratings visual stimuli
  experimenter: ['Marton Rozsa']
  institution: GENIE project, HHMI Janelia Research Campus
  Group /general/intracellular_ephys/Micropipette (IntracellularElectrode) 
  Group /general/intracellular_ephys/Micropipette/device (Device) Multiclamp 700B with 20 kHz low-pass filter
  Group /general/intracellular_ephys/sweep_table (SweepTable) A sweep table groups different PatchClampSeries together.
  Dataset /general/intracellular_ephys/sweep_table/id (ElementIdentifiers)  | shape = (3,) | dtype = int64
  Dataset /general/intracellular_ephys/sweep_table/series (VectorData) PatchClampSeries with the same sweep number | shape = (3,) | dtype = object
  Dataset /general/intracellular_ephys/sweep_table/series_index (VectorIndex) Index for VectorData 'series' | shape = (3,) | dtype = uint8
  Dataset /general/intracellular_ephys/sweep_table/sweep_number (VectorData) Sweep number of the entries in that row | shape = (3,) | dtype = uint64
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
  session_id: jGCaMP8f_ANM471994_cell02
  Group /general/subject (Subject) 
  surgery: [{"surgery_id": "1", "start_time": "2020-03-08 12:00:00", "end_time": "2020-03-08 12:50:00", "surgery_description": "headbar, craniotomy, virus injection, window:-: comments: nan"}, {"surgery_id": "2", "start_time": "2020-05-09 16:10:00", "end_time": "2020-05-09 17:00:00", "surgery_description": "window removal:-: comments: nice prep"}]
  virus: [{"surgery_id": "1", "injection_id": "1", "virus_id": "10250", "skull_reference": "Lambda", "ml_location": "2200.000", "ap_location": "0.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-6xHis-noRSET-1NIW_Q315L_N19T_S24I_S26R_Q88E_LKI_GCaMP6s-WPRE.547.456", "titer": "32600000000000.0", "order_date": "2020-01-27", "remarks": "Ultrafast GCaMP456 ref: 1-1001-1"}, {"surgery_id": "1", "injection_id": "2", "virus_id": "10250", "skull_reference": "Lambda", "ml_location": "2800.000", "ap_location": "0.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-6xHis-noRSET-1NIW_Q315L_N19T_S24I_S26R_Q88E_LKI_GCaMP6s-WPRE.547.456", "titer": "32600000000000.0", "order_date": "2020-01-27", "remarks": "Ultrafast GCaMP456 ref: 1-1001-1"}, {"surgery_id": "1", "injection_id": "3", "virus_id": "10250", "skull_reference": "Lambda", "ml_location": "2800.000", "ap_location": "600.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-6xHis-noRSET-1NIW_Q315L_N19T_S24I_S26R_Q88E_LKI_GCaMP6s-WPRE.547.456", "titer": "32600000000000.0", "order_date": "2020-01-27", "remarks": "Ultrafast GCaMP456 ref: 1-1001-1"}, {"surgery_id": "1", "injection_id": "4", "virus_id": "10250", "skull_reference": "Lambda", "ml_location": "2300.000", "ap_location": "600.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-6xHis-noRSET-1NIW_Q315L_N19T_S24I_S26R_Q88E_LKI_GCaMP6s-WPRE.547.456", "titer": "32600000000000.0", "order_date": "2020-01-27", "remarks": "Ultrafast GCaMP456 ref: 1-1001-1"}, {"surgery_id": "1", "injection_id": "5", "virus_id": "10250", "skull_reference": "Lambda", "ml_location": "2200.000", "ap_location": "0.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-6xHis-noRSET-1NIW_Q315L_N19T_S24I_S26R_Q88E_LKI_GCaMP6s-WPRE.547.456", "titer": "32600000000000.0", "order_date": "2020-01-27", "remarks": "Ultrafast GCaMP456 ref: 1-1001-1"}, {"surgery_id": "1", "injection_id": "6", "virus_id": "10250", "skull_reference": "Lambda", "ml_location": "2800.000", "ap_location": "0.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-6xHis-noRSET-1NIW_Q315L_N19T_S24I_S26R_Q88E_LKI_GCaMP6s-WPRE.547.456", "titer": "32600000000000.0", "order_date": "2020-01-27", "remarks": "Ultrafast GCaMP456 ref: 1-1001-1"}, {"surgery_id": "1", "injection_id": "7", "virus_id": "10250", "skull_reference": "Lambda", "ml_location": "2800.000", "ap_location": "600.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-6xHis-noRSET-1NIW_Q315L_N19T_S24I_S26R_Q88E_LKI_GCaMP6s-WPRE.547.456", "titer": "32600000000000.0", "order_date": "2020-01-27", "remarks": "Ultrafast GCaMP456 ref: 1-1001-1"}, {"surgery_id": "1", "injection_id": "8", "virus_id": "10250", "skull_reference": "Lambda", "ml_location": "2300.000", "ap_location": "600.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-6xHis-noRSET-1NIW_Q315L_N19T_S24I_S26R_Q88E_LKI_GCaMP6s-WPRE.547.456", "titer": "32600000000000.0", "order_date": "2020-01-27", "remarks": "Ultrafast GCaMP456 ref: 1-1001-1"}, {"surgery_id": "1", "injection_id": "9", "virus_id": "10250", "skull_reference": "Lambda", "ml_location": "2200.000", "ap_location": "0.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-6xHis-noRSET-1NIW_Q315L_N19T_S24I_S26R_Q88E_LKI_GCaMP6s-WPRE.547.456", "titer": "32600000000000.0", "order_date": "2020-01-27", "remarks": "Ultrafast GCaMP456 ref: 1-1001-1"}, {"surgery_id": "1", "injection_id": "10", "virus_id": "10250", "skull_reference": "Lambda", "ml_location": "2800.000", "ap_location": "0.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-6xHis-noRSET-1NIW_Q315L_N19T_S24I_S26R_Q88E_LKI_GCaMP6s-WPRE.547.456", "titer": "32600000000000.0", "order_date": "2020-01-27", "remarks": "Ultrafast GCaMP456 ref: 1-1001-1"}, {"surgery_id": "1", "injection_id": "11", "virus_id": "10250", "skull_reference": "Lambda", "ml_location": "2800.000", "ap_location": "600.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-6xHis-noRSET-1NIW_Q315L_N19T_S24I_S26R_Q88E_LKI_GCaMP6s-WPRE.547.456", "titer": "32600000000000.0", "order_date": "2020-01-27", "remarks": "Ultrafast GCaMP456 ref: 1-1001-1"}, {"surgery_id": "1", "injection_id": "12", "virus_id": "10250", "skull_reference": "Lambda", "ml_location": "2300.000", "ap_location": "600.000", "dv_location": "300.000", "volume": "30.000", "dilution": "8.00", "description": "virus injection: -", "virus_source": "Janelia", "serotype": "AAV2/1", "virus_name": "pGP-AAV-syn-6xHis-noRSET-1NIW_Q315L_N19T_S24I_S26R_Q88E_LKI_GCaMP6s-WPRE.547.456", "titer": "32600000000000.0", "order_date": "2020-01-27", "remarks": "Ultrafast GCaMP456 ref: 1-1001-1"}]
  identifier: jGCaMP8f_ANM471994_cell02
  Group /intervals/epochs (TimeIntervals) experimental epochs
  Dataset /intervals/epochs/id (ElementIdentifiers)  | shape = (3,) | dtype = int64
  Dataset /intervals/epochs/start_time (VectorData) Start time of epoch, in seconds | shape = (3,) | dtype = float64
  Dataset /intervals/epochs/stop_time (VectorData) Stop time of epoch, in seconds | shape = (3,) | dtype = float64
  Dataset /intervals/epochs/timeseries (TimeSeriesReferenceVectorData) index into a TimeSeries object | shape = (9,) | dtype = [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')]
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
  Dataset /processing/ophys of movie 0/Fluorescence/NeuropilResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (9,) | dtype = int64
  Group /processing/ophys of movie 0/Fluorescence/RoiResponseSeries (RoiResponseSeries) weighted average fluorescence of roi
  Dataset /processing/ophys of movie 0/Fluorescence/RoiResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (9,) | dtype = int64
  Group /processing/ophys of movie 0/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation (PlaneSegmentation) output from segmenting with Suite2p, ROI 0 is the neuron recorded with electrophysiology
  Dataset /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/cell_type (VectorData) pyr for putative pyramidal cells, int for putative interneurons, based on average loose-seal spike shape | shape = (9,) | dtype = object
  Dataset /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/id (ElementIdentifiers)  | shape = (9,) | dtype = int64
  Dataset /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (9, 512, 128) | dtype = float64
  Group /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/imaging_plane/device (Device) 
  Group /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/imaging_plane/green (OpticalChannel) 
  Dataset /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/neuropil_mask (VectorData) mask of neuropil surrounding this roi | shape = (9, 512, 128) | dtype = bool
  Dataset /processing/ophys of movie 0/ImageSegmentation/MovieSegmentation/recorded_with_ephys (VectorData) whether this ROI is simultaneously loose-seal recorded | shape = (9,) | dtype = bool
  Group /processing/ophys of movie 0/mean images of movie 0 (Images) Structural images of a scanning
  Dataset /processing/ophys of movie 0/mean images of movie 0/Alexa Fluor 594 in pipette (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Dataset /processing/ophys of movie 0/mean images of movie 0/jGCaMP8f at 940nm (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Group /processing/ophys of movie 1 (ProcessingModule) Processing result of imaging
  Group /processing/ophys of movie 1/Fluorescence (Fluorescence) 
  Group /processing/ophys of movie 1/Fluorescence/NeuropilResponseSeries (RoiResponseSeries) average fluorescence of the neuropil surrounding the roi
  Dataset /processing/ophys of movie 1/Fluorescence/NeuropilResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (10,) | dtype = int64
  Group /processing/ophys of movie 1/Fluorescence/RoiResponseSeries (RoiResponseSeries) weighted average fluorescence of roi
  Dataset /processing/ophys of movie 1/Fluorescence/RoiResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (10,) | dtype = int64
  Group /processing/ophys of movie 1/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation (PlaneSegmentation) output from segmenting with Suite2p, ROI 0 is the neuron recorded with electrophysiology
  Dataset /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation/cell_type (VectorData) pyr for putative pyramidal cells, int for putative interneurons, based on average loose-seal spike shape | shape = (10,) | dtype = object
  Dataset /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation/id (ElementIdentifiers)  | shape = (10,) | dtype = int64
  Dataset /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (10, 512, 128) | dtype = float64
  Group /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation/imaging_plane/device (Device) 
  Group /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation/imaging_plane/green (OpticalChannel) 
  Dataset /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation/neuropil_mask (VectorData) mask of neuropil surrounding this roi | shape = (10, 512, 128) | dtype = bool
  Dataset /processing/ophys of movie 1/ImageSegmentation/MovieSegmentation/recorded_with_ephys (VectorData) whether this ROI is simultaneously loose-seal recorded | shape = (10,) | dtype = bool
  Group /processing/ophys of movie 1/mean images of movie 1 (Images) Structural images of a scanning
  Dataset /processing/ophys of movie 1/mean images of movie 1/Alexa Fluor 594 in pipette (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Dataset /processing/ophys of movie 1/mean images of movie 1/jGCaMP8f at 940nm (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Group /processing/ophys of movie 2 (ProcessingModule) Processing result of imaging
  Group /processing/ophys of movie 2/Fluorescence (Fluorescence) 
  Group /processing/ophys of movie 2/Fluorescence/NeuropilResponseSeries (RoiResponseSeries) average fluorescence of the neuropil surrounding the roi
  Dataset /processing/ophys of movie 2/Fluorescence/NeuropilResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (8,) | dtype = int64
  Group /processing/ophys of movie 2/Fluorescence/RoiResponseSeries (RoiResponseSeries) weighted average fluorescence of roi
  Dataset /processing/ophys of movie 2/Fluorescence/RoiResponseSeries/rois (DynamicTableRegion) table region for rois in this segmentation | shape = (8,) | dtype = int64
  Group /processing/ophys of movie 2/ImageSegmentation (ImageSegmentation) 
  Group /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation (PlaneSegmentation) output from segmenting with Suite2p, ROI 0 is the neuron recorded with electrophysiology
  Dataset /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation/cell_type (VectorData) pyr for putative pyramidal cells, int for putative interneurons, based on average loose-seal spike shape | shape = (8,) | dtype = object
  Dataset /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation/id (ElementIdentifiers)  | shape = (8,) | dtype = int64
  Dataset /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation/image_mask (VectorData) Image masks for each ROI | shape = (8, 512, 128) | dtype = float64
  Group /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation/imaging_plane (ImagingPlane) 
  Group /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation/imaging_plane/device (Device) 
  Group /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation/imaging_plane/green (OpticalChannel) 
  Dataset /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation/neuropil_mask (VectorData) mask of neuropil surrounding this roi | shape = (8, 512, 128) | dtype = bool
  Dataset /processing/ophys of movie 2/ImageSegmentation/MovieSegmentation/recorded_with_ephys (VectorData) whether this ROI is simultaneously loose-seal recorded | shape = (8,) | dtype = bool
  Group /processing/ophys of movie 2/mean images of movie 2 (Images) Structural images of a scanning
  Dataset /processing/ophys of movie 2/mean images of movie 2/Alexa Fluor 594 in pipette (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  Dataset /processing/ophys of movie 2/mean images of movie 2/jGCaMP8f at 940nm (GrayscaleImage)  | shape = (512, 128) | dtype = float64
  session_description: 
  session_start_time: 2020-05-09T19:02:04-07:00
  timestamps_reference_time: 2020-05-09T19:02:04-07:00
