
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001277/draft
name: NG-CANCAN Remote Targeting Electroporation: Impact of Pulse Duration and Protocol Delivery Frequency
contributor: [{'name': 'Silkuniene, Giedre', 'email': 'giedre.silkuniene@gmail.com', 'roleName': ['dcite:ContactPerson', 'dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0001-8436-9718', 'affiliation': [], 'includeInCitation': True}, {'name': 'Silkunas, Mantas', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-4568-9265', 'includeInCitation': True}, {'name': 'Pakhomov, Andrei', 'roleName': ['dcite:ProjectLeader'], 'schemaKey': 'Person', 'identifier': '0000-0003-3816-3860', 'includeInCitation': True}, {'name': 'National Institutes of Health', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': '1R21EY034258', 'includeInCitation': False}]
description: Experiments were conducted using a four-electrode array with an inter-electrode spacing of 10 mm. The electrode array was positioned at the bottom of the well plate (0 mm). Pulse durations of 300 ns, 600 ns, and 900 ns were tested. Depending on the pulse duration, the protocol consisted of 18 packets for 300 ns pulses, 9 packets for 600 ns pulses, or 6 packets for 900 ns pulses, delivered at frequencies of 0.4 MHz, 0.2 MHz, and 0.14 MHz, respectively. Each protocol was repeated twice at a frequency of 1 Hz. Cell monolayer integrity was assessed using Hoechst staining, while membrane permeability was evaluated with YoPro-1. This work was partially supported by NIH grant 1R21EY034258.
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 23224948092, 'numberOfFiles': 49, 'numberOfSubjects': 18, 'variableMeasured': [], 'measurementTechnique': []}

Dandiset 001277 has 49 NWB files.
13 of these NWB files are of type 1.
18 of these NWB files are of type 2.
18 of these NWB files are of type 3.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Imaging_Cy3-DAPI (ImageSeries) Cy3-DAPI channels: Combined imaging 2 hours after exposure. Propidium iodide (PI) visualized with Cy3 channel to evaluate dead cells. Nuclei staining (Hoechst) used for identifying all cells and assessing monolayer integrity (DAPI channel).********************File Metadata: OME metadata: <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
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
  	<OME:Image ID="Image:0" Name="Cy3, DAPI">
  		<OME:AcquisitionDate>2024-09-25T22:22:45Z</OME:AcquisitionDate>
  		<OME:ExperimenterRef ID="Experimenter:0"/>
  		<OME:InstrumentRef ID="Instrument:0"/>
  		<OME:ObjectiveSettings ID="Objective:0" Medium="Air" RefractiveIndex="1"/>
  		<OME:Pixels ID="Pixels:0" DimensionOrder="XYCZT" Type="uint16" SignificantBits="12" Interleaved="false" SizeX="19190" SizeY="19190" SizeC="2" SizeZ="1" SizeT="1" PhysicalSizeX="1.6250000000000002" PhysicalSizeXUnit="µm" PhysicalSizeY="1.6250000000000002" PhysicalSizeYUnit="µm">
  			<OME:Channel ID="Channel:0" Name="Cy3" SamplesPerPixel="1" ContrastMethod="Fluorescence" EmissionWavelength="565" EmissionWavelengthUnit="nm" Color="-16774913">
  				<LightSourceSettings ID="LightSource:0"/>
  				<DetectorSettings ID="Detector:0" Binning="1x1"/>
  			</OME:Channel>
  			<OME:Channel ID="Channel:1" Name="DAPI" SamplesPerPixel="1" ContrastMethod="Fluorescence" EmissionWavelength="455" EmissionWavelengthUnit="nm" Color="65535">
  				<LightSourceSettings ID="LightSource:0"/>
  				<DetectorSettings ID="Detector:0" Binning="1x1"/>
  			</OME:Channel>
  			<OME:TiffData IFD="0" FirstZ="0" FirstT="0" FirstC="0" PlaneCount="2"/>
  			<OME:Plane TheZ="0" TheT="0" TheC="0" DeltaT="1736.827" DeltaTUnit="s" PositionZ="6908.0600000000004" PositionZUnit="µm" PositionX="98763.663618344784" PositionXUnit="µm" PositionY="59120.785324152377" PositionYUnit="µm" ExposureTime="200" ExposureTimeUnit="ms"/>
  			<OME:Plane TheZ="0" TheT="0" TheC="1" DeltaT="1738.425" DeltaTUnit="s" PositionZ="6908.0600000000004" PositionZUnit="µm" PositionX="98763.663618344784" PositionXUnit="µm" PositionY="59120.785324152377" PositionYUnit="µm" ExposureTime="200" ExposureTimeUnit="ms"/>
  		</OME:Pixels>
  	</OME:Image>
  	<SA:StructuredAnnotations/>
  </OME>
  file_create_date: ['2025-01-08T12:39:13.215510-05:00']
  Group /general/TIFF_Metadata (LabMetaData) 
  experimenter: ['Giedre Silkuniene, Mantas Silkunas']
  institution: Old Dominion University
  lab: Pakhomov Lab
  session_id: single_time_point
  Group /general/subject (Subject) 
  identifier: 70476523-f84c-4fcc-b6d3-a1b6471ab017
  session_description: ***Subject-Specific Description*** Subject ID: P1_20240926_A1. Fluorescent Channel(s) used: Cy3-DAPI.Image taken 2 hours after pulse exposure. Protocol: CanCan (with canceling pulses).. Pulse duration - 900 ns. Protocol consisted of 9 packets of pulses delivered at 0.2MHz frequency. Protocol repeated 2 time(s) at 1Hz frequency.. ***General Protocol Description (Subject-Independent)*** Experiments were conducted using a four-electrode stainless steel setup with an inter-electrode distance of 10.0 mm. The CanCan exposure protocol involved delivering packets of 300/600/900 ns pulses from four electrodes. Initially, a single 300/600/900 ns pulse (7.2 kV) was applied from one electrode (e.g., electrode 1), constituting phase 1. Subsequently, simultaneous pulses with an amplitude reduced by 12.5% were delivered from two electrodes (e.g., electrodes 2 and 4), followed by another set of simultaneous pulses with an additional 12.5% amplitude reduction from electrodes 1 and 3. These simultaneous pulses represented phases 2, 3, and continued up to phase 8, with the amplitude reduced by 12.5% at each phase. After completing one packet of pulses, the sequence was repeated 9 times at a defined frequency. Upon completing these 9 repetitions, the protocol was either repeated 2, 4, or 6 times at a 1 Hz frequency or initiated anew from another electrode (e.g., electrode 2), ensuring that all four electrodes eventually served as the initiating electrode. Control protocols followed identical frequency and repetition schemes but lacked the subsequent, reduced-amplitude pulses delivered from the other electrodes. The number of protocol repetitions, pulse duration, and protocol type applied are noted under the Subject-Specific description.Before exposure, the growth medium was replaced with a physiological solution (in mM: 140 NaCl, 5.4 KCl, 2 CaCl2, 1.5 MgCl2, 10 D-glucose, and 10 HEPES; pH 7.3, 290–300 mOsm/kg) containing 1 µg/mL Hoechst and 1 µM YoPro-1 (YP). Hoechst, visualized via the DAPI channel, stained all cell nuclei. Thirty minutes post-exposure, the dye-containing solution was replaced with dye-free physiological solution, and YP uptake, serving as a semi-quantitative marker of membrane permeabilization induced by electroporation, was visualized via the FITC channel. For some experiments (indicated by the Cy3 channel), cell death was evaluated using propidium iodide staining two hours after exposure. More details about the methods are available in the related manuscript.
  session_start_time: 2025-01-08T12:39:13.214551-05:00
  timestamps_reference_time: 2025-01-08T12:39:13.214551-05:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Imaging_DAPI (ImageSeries) DAPI channel: nuclei staining (Hoechst). Used for identifying all cells, evaluating monolayer integrity. Images taken beffore exposure.
  file_create_date: ['2025-01-08T12:31:11.107889-05:00']
  Group /general/TIFF_Metadata (LabMetaData) 
  experimenter: ['Giedre Silkuniene, Mantas Silkunas']
  institution: Old Dominion University
  lab: Pakhomov Lab
  session_id: single_time_point
  Group /general/subject (Subject) 
  identifier: 2cb32298-ee3b-408a-9aca-f90a70b9de2b
  session_description: ***Subject-Specific Description*** Subject ID: P1_20240926_A1. Fluorescent Channel(s) used: DAPI.Image taken before pulse exposure. Protocol: CanCan (with canceling pulses).. Pulse duration - 900 ns. Protocol consisted of 9 packets of pulses delivered at 0.2MHz frequency. Protocol repeated 2 time(s) at 1Hz frequency.. ***General Protocol Description (Subject-Independent)*** Experiments were conducted using a four-electrode stainless steel setup with an inter-electrode distance of 10.0 mm. The CanCan exposure protocol involved delivering packets of 300/600/900 ns pulses from four electrodes. Initially, a single 300/600/900 ns pulse (7.2 kV) was applied from one electrode (e.g., electrode 1), constituting phase 1. Subsequently, simultaneous pulses with an amplitude reduced by 12.5% were delivered from two electrodes (e.g., electrodes 2 and 4), followed by another set of simultaneous pulses with an additional 12.5% amplitude reduction from electrodes 1 and 3. These simultaneous pulses represented phases 2, 3, and continued up to phase 8, with the amplitude reduced by 12.5% at each phase. After completing one packet of pulses, the sequence was repeated 9 times at a defined frequency. Upon completing these 9 repetitions, the protocol was either repeated 2, 4, or 6 times at a 1 Hz frequency or initiated anew from another electrode (e.g., electrode 2), ensuring that all four electrodes eventually served as the initiating electrode. Control protocols followed identical frequency and repetition schemes but lacked the subsequent, reduced-amplitude pulses delivered from the other electrodes. The number of protocol repetitions, pulse duration, and protocol type applied are noted under the Subject-Specific description.Before exposure, the growth medium was replaced with a physiological solution (in mM: 140 NaCl, 5.4 KCl, 2 CaCl2, 1.5 MgCl2, 10 D-glucose, and 10 HEPES; pH 7.3, 290–300 mOsm/kg) containing 1 µg/mL Hoechst and 1 µM YoPro-1 (YP). Hoechst, visualized via the DAPI channel, stained all cell nuclei. Thirty minutes post-exposure, the dye-containing solution was replaced with dye-free physiological solution, and YP uptake, serving as a semi-quantitative marker of membrane permeabilization induced by electroporation, was visualized via the FITC channel. For some experiments (indicated by the Cy3 channel), cell death was evaluated using propidium iodide staining two hours after exposure. More details about the methods are available in the related manuscript.
  session_start_time: 2025-01-08T12:31:11.107889-05:00
  timestamps_reference_time: 2025-01-08T12:31:11.107889-05:00


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Imaging_FITC (ImageSeries) FITC channel: YO-PRO-1 uptake to assess membrane permeabilization 30 minutes after exposure.
  file_create_date: ['2025-01-08T12:33:44.995017-05:00']
  Group /general/TIFF_Metadata (LabMetaData) 
  experimenter: ['Giedre Silkuniene, Mantas Silkunas']
  institution: Old Dominion University
  lab: Pakhomov Lab
  session_id: single_time_point
  Group /general/subject (Subject) 
  identifier: 1d424019-ad10-4b33-b3b6-22efb83fefd1
  session_description: ***Subject-Specific Description*** Subject ID: P1_20240926_A1. Fluorescent Channel(s) used: FITC.Image taken 30min after pulse exposure. Protocol: CanCan (with canceling pulses).. Pulse duration - 900 ns. Protocol consisted of 9 packets of pulses delivered at 0.2MHz frequency. Protocol repeated 2 time(s) at 1Hz frequency.. ***General Protocol Description (Subject-Independent)*** Experiments were conducted using a four-electrode stainless steel setup with an inter-electrode distance of 10.0 mm. The CanCan exposure protocol involved delivering packets of 300/600/900 ns pulses from four electrodes. Initially, a single 300/600/900 ns pulse (7.2 kV) was applied from one electrode (e.g., electrode 1), constituting phase 1. Subsequently, simultaneous pulses with an amplitude reduced by 12.5% were delivered from two electrodes (e.g., electrodes 2 and 4), followed by another set of simultaneous pulses with an additional 12.5% amplitude reduction from electrodes 1 and 3. These simultaneous pulses represented phases 2, 3, and continued up to phase 8, with the amplitude reduced by 12.5% at each phase. After completing one packet of pulses, the sequence was repeated 9 times at a defined frequency. Upon completing these 9 repetitions, the protocol was either repeated 2, 4, or 6 times at a 1 Hz frequency or initiated anew from another electrode (e.g., electrode 2), ensuring that all four electrodes eventually served as the initiating electrode. Control protocols followed identical frequency and repetition schemes but lacked the subsequent, reduced-amplitude pulses delivered from the other electrodes. The number of protocol repetitions, pulse duration, and protocol type applied are noted under the Subject-Specific description.Before exposure, the growth medium was replaced with a physiological solution (in mM: 140 NaCl, 5.4 KCl, 2 CaCl2, 1.5 MgCl2, 10 D-glucose, and 10 HEPES; pH 7.3, 290–300 mOsm/kg) containing 1 µg/mL Hoechst and 1 µM YoPro-1 (YP). Hoechst, visualized via the DAPI channel, stained all cell nuclei. Thirty minutes post-exposure, the dye-containing solution was replaced with dye-free physiological solution, and YP uptake, serving as a semi-quantitative marker of membrane permeabilization induced by electroporation, was visualized via the FITC channel. For some experiments (indicated by the Cy3 channel), cell death was evaluated using propidium iodide staining two hours after exposure. More details about the methods are available in the related manuscript.
  session_start_time: 2025-01-08T12:33:44.995017-05:00
  timestamps_reference_time: 2025-01-08T12:33:44.995017-05:00
