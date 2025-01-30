
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001276/draft
name: NG-CANCAN Remote Targeting Electroporation: Impact of Burst Number Variation on Permeabilization Distribution in Confluent Cell Monolayers
contributor: [{'name': 'Silkuniene, Giedre', 'email': 'giedre.silkuniene@gmail.com', 'roleName': ['dcite:ContactPerson', 'dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0001-8436-9718', 'affiliation': [], 'includeInCitation': True}, {'name': 'Silkunas, Mantas', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-4568-9265', 'includeInCitation': True}, {'name': 'National Institutes of Heath', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': '1R21EY034258', 'includeInCitation': False}, {'name': 'Pakhomov, Andrei', 'roleName': ['dcite:ProjectLeader'], 'schemaKey': 'Person', 'identifier': '0000-0003-3816-3860', 'includeInCitation': True}, {}]
description: Experiments were conducted using a four-electrode array with an inter-electrode distance of 10.0 mm. The study focused on optimizing the CANCAN protocol and investigating the effect of varying burst numbers on permeabilization distribution across confluent cell monolayers. The CANCAN protocols utilized canceling pulses to minimize cell damage near the electrodes while targeting cells in the center of the electrode array. Each single pulse in the protocol had a duration of 600 ns. The protocol consisted of nine packets of pulses delivered at a frequency of 0.2 MHz and was repeated 1, 2, 4, or 6 times at a frequency of 1 Hz. Cell monolayer integrity was assessed using Hoechst staining, while membrane permeability was evaluated using YoPro-1. This work was partially supported by NIH grant 1R21EY034258.
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}, {'name': 'Cricetulus griseus - Cricetulus aureus', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10029'}], 'approach': [], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 43187902872, 'numberOfFiles': 108, 'numberOfSubjects': 54, 'variableMeasured': [], 'measurementTechnique': []}

Dandiset 001276 has 100 NWB files.
100 of these NWB files are of type 1.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/SingleTimePointImaging (ImageSeries) Acquisition Description (Subject-Specific): Subject ID: P1_20240627_A2, Fluorescent Channel: DAPI, Phase: pre (where 'pre' indicates imaging prior to exposure and 'post' indicates imaging of the same well after exposure).  CanCan protocol (with canceling pulses),011: Protocol consisted of 9 packets of pulses delivered at 0.2MHz frequency, protocol repeated 2 times at 1Hz frequency. General Protocol Description (Subject-Independent): Experiments were conducted using a four-electrode stainless steel setup with an inter-electrode distance of 10.0 mm. The CanCan exposure protocol involved delivering packets of 600 ns pulses from four electrodes. Initially, a single 600 ns pulse (7.2 kV) was applied from one electrode (e.g., electrode 1), constituting phase 1. Subsequently, simultaneous 600 ns pulses with an amplitude reduced by 12.5% were delivered from two electrodes (e.g., electrodes 2 and 4), followed by another set of simultaneous pulses with an additional 12.5% amplitude reduction from electrodes 1 and 3. These simultaneous pulses represented phases 2, 3, and continued up to phase 8, with the amplitude reduced by 12.5% at each phase. After completing one packet of pulses, the sequence was repeated 9 times at a defined frequency. Upon completing these 9 repetitions, the protocol was either repeated 2, 4, or 6 times at a 1 Hz frequency or initiated anew from another electrode (e.g., electrode 2), ensuring that all four electrodes eventually served as the initiating electrode.Control protocols followed identical frequency and repetition schemes but lacked the subsequent, reduced-amplitude pulses delivered from the other electrodes. Before exposure, the growth medium was replaced with a physiological solution (in mM: 140 NaCl, 5.4 KCl, 2 CaCl2, 1.5 MgCl2, 10 D-glucose, and 10 HEPES; pH 7.3, 290–300 mOsm/kg) containing 1 µg/mL Hoechst and 1 µM YoPro-1 (YP). Hoechst, visualized via the DAPI channel, stained the nuclei of all cells. YP, visualized via the FITC channel, served as a semi-quantitative marker of membrane permeabilization induced by electroporation, as it has limited permeability into intact cells. Thirty minutes post-exposure, the dye-containing solution was replaced with dye-free physiological solution, and the monolayer was imaged to assess YP uptake.  OME metadata: <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
  <OME xmlns="http://www.openmicroscopy.org/Schemas/OME/2015-01" xmlns:OME="http://www.openmicroscopy.org/Schemas/OME/2015-01" xmlns:ROI="http://www.openmicroscopy.org/Schemas/ROI/2015-01" xmlns:BIN="http://www.openmicroscopy.org/Schemas/BinaryFile/2015-01" xmlns:SA="http://www.openmicroscopy.org/Schemas/SA/2015-01" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.openmicroscopy.org/Schemas/OME/2015-01 http://www.openmicroscopy.org/Schemas/OME/2015-01/ome.xsd" Creator="HP Inc., XV - (4.1)">
  	<OME:Experimenter ID="Experimenter:0" UserName="OlympusIX83"/>
  	<OME:Instrument ID="Instrument:0">
  		<OME:Microscope Manufacturer="Olympus" Model="IX83 P2ZF"/>
  		<OME:LightSource Manufacturer="Olympus" Model="IX3 LED" ID="LightSource:0">
  			<OME:GenericExcitationSource/>
  		</OME:LightSource>
  		<OME:Detector Manufacturer="Hamamatsu" Model="Hamamatsu ORCA-Flash4.0" Gain="0" Offset="0" Zoom="1" ID="Detector:0"/>
  		<OME:Objective Manufacturer="Olympus" Model="IX3 Nosepiece" LensNA="0.16" NominalMagnification="4" CalibratedMagnification="4" WorkingDistance="13000" WorkingDistanceUnit="µm" ID="Objective:0"/>
  	</OME:Instrument>
  	<OME:Image ID="Image:0" Name="DAPI">
  		<OME:AcquisitionDate>2024-06-27T18:12:27Z</OME:AcquisitionDate>
  		<OME:ExperimenterRef ID="Experimenter:0"/>
  		<OME:InstrumentRef ID="Instrument:0"/>
  		<OME:ObjectiveSettings ID="Objective:0" Medium="Air" RefractiveIndex="1"/>
  		<OME:Pixels ID="Pixels:0" DimensionOrder="XYCZT" Type="uint16" SignificantBits="13" Interleaved="false" SizeX="19190" SizeY="19190" SizeC="1" SizeZ="1" SizeT="1" PhysicalSizeX="1.6250000000000002" PhysicalSizeXUnit="µm" PhysicalSizeY="1.6250000000000002" PhysicalSizeYUnit="µm">
  			<OME:Channel ID="Channel:0" Name="DAPI" SamplesPerPixel="1" ContrastMethod="Fluorescence" EmissionWavelength="455" EmissionWavelengthUnit="nm" Color="65535">
  				<LightSourceSettings ID="LightSource:0"/>
  				<DetectorSettings ID="Detector:0" Binning="1x1"/>
  			</OME:Channel>
  			<OME:TiffData IFD="0" FirstZ="0" FirstT="0" FirstC="0" PlaneCount="1"/>
  			<OME:Plane TheZ="0" TheT="0" TheC="0" DeltaT="218.24000000000001" DeltaTUnit="s" PositionZ="6652.5100000000002" PositionZUnit="µm" PositionX="59255.531106488983" PositionXUnit="µm" PositionY="19879.826007724529" PositionYUnit="µm" ExposureTime="600" ExposureTimeUnit="ms"/>
  		</OME:Pixels>
  	</OME:Image>
  	<SA:StructuredAnnotations/>
  </OME>
  file_create_date: ['2024-12-12T14:41:58.197275-05:00']
  experimenter: ['Giedre Silkuniene, Mantas Silkunas']
  institution: Old Dominion University
  lab: Pakhomov Lab
  session_id: single_time_point
  Group /general/subject (Subject) 
  identifier: 441cb2b5-170d-4539-8f1f-731a5d1b3759
  session_description: Acquisition Description (Subject-Specific): Subject ID: P1_20240627_A2, Fluorescent Channel: DAPI, Phase: pre (where 'pre' indicates imaging prior to exposure and 'post' indicates imaging of the same well after exposure).  CanCan protocol (with canceling pulses),011: Protocol consisted of 9 packets of pulses delivered at 0.2MHz frequency, protocol repeated 2 times at 1Hz frequency. General Protocol Description (Subject-Independent): Experiments were conducted using a four-electrode stainless steel setup with an inter-electrode distance of 10.0 mm. The CanCan exposure protocol involved delivering packets of 600 ns pulses from four electrodes. Initially, a single 600 ns pulse (7.2 kV) was applied from one electrode (e.g., electrode 1), constituting phase 1. Subsequently, simultaneous 600 ns pulses with an amplitude reduced by 12.5% were delivered from two electrodes (e.g., electrodes 2 and 4), followed by another set of simultaneous pulses with an additional 12.5% amplitude reduction from electrodes 1 and 3. These simultaneous pulses represented phases 2, 3, and continued up to phase 8, with the amplitude reduced by 12.5% at each phase. After completing one packet of pulses, the sequence was repeated 9 times at a defined frequency. Upon completing these 9 repetitions, the protocol was either repeated 2, 4, or 6 times at a 1 Hz frequency or initiated anew from another electrode (e.g., electrode 2), ensuring that all four electrodes eventually served as the initiating electrode.Control protocols followed identical frequency and repetition schemes but lacked the subsequent, reduced-amplitude pulses delivered from the other electrodes. Before exposure, the growth medium was replaced with a physiological solution (in mM: 140 NaCl, 5.4 KCl, 2 CaCl2, 1.5 MgCl2, 10 D-glucose, and 10 HEPES; pH 7.3, 290–300 mOsm/kg) containing 1 µg/mL Hoechst and 1 µM YoPro-1 (YP). Hoechst, visualized via the DAPI channel, stained the nuclei of all cells. YP, visualized via the FITC channel, served as a semi-quantitative marker of membrane permeabilization induced by electroporation, as it has limited permeability into intact cells. Thirty minutes post-exposure, the dye-containing solution was replaced with dye-free physiological solution, and the monolayer was imaged to assess YP uptake.  OME metadata: <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
  <OME xmlns="http://www.openmicroscopy.org/Schemas/OME/2015-01" xmlns:OME="http://www.openmicroscopy.org/Schemas/OME/2015-01" xmlns:ROI="http://www.openmicroscopy.org/Schemas/ROI/2015-01" xmlns:BIN="http://www.openmicroscopy.org/Schemas/BinaryFile/2015-01" xmlns:SA="http://www.openmicroscopy.org/Schemas/SA/2015-01" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.openmicroscopy.org/Schemas/OME/2015-01 http://www.openmicroscopy.org/Schemas/OME/2015-01/ome.xsd" Creator="HP Inc., XV - (4.1)">
  	<OME:Experimenter ID="Experimenter:0" UserName="OlympusIX83"/>
  	<OME:Instrument ID="Instrument:0">
  		<OME:Microscope Manufacturer="Olympus" Model="IX83 P2ZF"/>
  		<OME:LightSource Manufacturer="Olympus" Model="IX3 LED" ID="LightSource:0">
  			<OME:GenericExcitationSource/>
  		</OME:LightSource>
  		<OME:Detector Manufacturer="Hamamatsu" Model="Hamamatsu ORCA-Flash4.0" Gain="0" Offset="0" Zoom="1" ID="Detector:0"/>
  		<OME:Objective Manufacturer="Olympus" Model="IX3 Nosepiece" LensNA="0.16" NominalMagnification="4" CalibratedMagnification="4" WorkingDistance="13000" WorkingDistanceUnit="µm" ID="Objective:0"/>
  	</OME:Instrument>
  	<OME:Image ID="Image:0" Name="DAPI">
  		<OME:AcquisitionDate>2024-06-27T18:12:27Z</OME:AcquisitionDate>
  		<OME:ExperimenterRef ID="Experimenter:0"/>
  		<OME:InstrumentRef ID="Instrument:0"/>
  		<OME:ObjectiveSettings ID="Objective:0" Medium="Air" RefractiveIndex="1"/>
  		<OME:Pixels ID="Pixels:0" DimensionOrder="XYCZT" Type="uint16" SignificantBits="13" Interleaved="false" SizeX="19190" SizeY="19190" SizeC="1" SizeZ="1" SizeT="1" PhysicalSizeX="1.6250000000000002" PhysicalSizeXUnit="µm" PhysicalSizeY="1.6250000000000002" PhysicalSizeYUnit="µm">
  			<OME:Channel ID="Channel:0" Name="DAPI" SamplesPerPixel="1" ContrastMethod="Fluorescence" EmissionWavelength="455" EmissionWavelengthUnit="nm" Color="65535">
  				<LightSourceSettings ID="LightSource:0"/>
  				<DetectorSettings ID="Detector:0" Binning="1x1"/>
  			</OME:Channel>
  			<OME:TiffData IFD="0" FirstZ="0" FirstT="0" FirstC="0" PlaneCount="1"/>
  			<OME:Plane TheZ="0" TheT="0" TheC="0" DeltaT="218.24000000000001" DeltaTUnit="s" PositionZ="6652.5100000000002" PositionZUnit="µm" PositionX="59255.531106488983" PositionXUnit="µm" PositionY="19879.826007724529" PositionYUnit="µm" ExposureTime="600" ExposureTimeUnit="ms"/>
  		</OME:Pixels>
  	</OME:Image>
  	<SA:StructuredAnnotations/>
  </OME>
  session_start_time: 2024-12-12T14:41:58.197201-05:00
  timestamps_reference_time: 2024-12-12T14:41:58.197201-05:00
