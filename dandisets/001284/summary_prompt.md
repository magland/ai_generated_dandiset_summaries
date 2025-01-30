
Below is an auto-generated summary of the contents of a Dandiset. It includes both metadata and a summary of the contents of the NWB files.

Please summarize the experiment in two or three paragraphs in the style of a scientific abstract touching on the likely purpose of the experiment.

Then give a description of what data are available in the NWB files.

Finally provide a list of up to ten keywords.

You should not refer to "Type X" since these are just internal labels used for communicating the breakdown of NWB files.

The summaries are from representative NWB files for each type, so keep that in mind when making your description. So for example, the timestamp or session ID is not going to be representative of all NWB files of that type.

Please provide your response in raw markdown suitable for copy/paste into a .md document.


id: DANDI:001284/draft
name: NG-CANCAN Remote Targeting Electroporation: Focused Cell Electroporation and Ablation in a Pseudo-3D Model
contributor: [{'name': 'Silkuniene, Giedre', 'email': 'giedre.silkuniene@gmail.com', 'roleName': ['dcite:Author', 'dcite:ContactPerson'], 'schemaKey': 'Person', 'identifier': '0000-0001-8436-9718', 'affiliation': [], 'includeInCitation': True}, {'name': 'Silkunas, Mantas', 'roleName': ['dcite:Author'], 'schemaKey': 'Person', 'identifier': '0000-0002-4568-9265', 'includeInCitation': True}, {'name': 'Pakhomov, Andrei', 'roleName': ['dcite:ProjectLeader'], 'schemaKey': 'Person', 'identifier': '0000-0003-3816-3860', 'includeInCitation': True}, {'name': 'National Institutes of Health', 'roleName': ['dcite:Funder'], 'schemaKey': 'Organization', 'awardNumber': '1R21EY034258', 'includeInCitation': False}]
description: Experiments were conducted using a four-electrode array with an inter-electrode spacing of 10 mm. A pseudo-3D model was created by elevating the electrode array 0 mm, 1 mm, or 2 mm above the monolayer. Each pulse was 600 ns in duration, and the protocol consisted of nine packets of pulses delivered at 0.2 MHz, repeated twice at 1 Hz. Cell monolayer integrity was assessed with Hoechst staining, and membrane permeability was evaluated using YoPro-1. After 2 hours, cells were stained with propidium iodide to assess cell death. This work was partially supported by NIH grant 1R21EY034258.
assetsSummary: {'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 36377439788, 'numberOfFiles': 84, 'numberOfSubjects': 35, 'variableMeasured': [], 'measurementTechnique': []}

Dandiset 001284 has 84 NWB files.
35 of these NWB files are of type 1.
35 of these NWB files are of type 2.
14 of these NWB files are of type 3.


Here is a summary of the type 1 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Imaging_DAPI (ImageSeries) DAPI channel: nuclei staining (Hoechst). Used for identifying all cells, evaluating monolayer integrity. Images taken beffore exposure.********************File Metadata:
  ===== OME Metadata =====
  <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
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
  		<OME:AcquisitionDate>2024-08-20T17:05:31Z</OME:AcquisitionDate>
  		<OME:ExperimenterRef ID="Experimenter:0"/>
  		<OME:InstrumentRef ID="Instrument:0"/>
  		<OME:ObjectiveSettings ID="Objective:0" Medium="Air" RefractiveIndex="1"/>
  		<OME:Pixels ID="Pixels:0" DimensionOrder="XYCZT" Type="uint16" SignificantBits="13" Interleaved="false" SizeX="19190" SizeY="19190" SizeC="1" SizeZ="1" SizeT="1" PhysicalSizeX="1.6250000000000002" PhysicalSizeXUnit="µm" PhysicalSizeY="1.6250000000000002" PhysicalSizeYUnit="µm">
  			<OME:Channel ID="Channel:0" Name="DAPI" SamplesPerPixel="1" ContrastMethod="Fluorescence" EmissionWavelength="455" EmissionWavelengthUnit="nm" Color="65535">
  				<LightSourceSettings ID="LightSource:0"/>
  				<DetectorSettings ID="Detector:0" Binning="1x1"/>
  			</OME:Channel>
  			<OME:TiffData IFD="0" FirstZ="0" FirstT="0" FirstC="0" PlaneCount="1"/>
  			<OME:Plane TheZ="0" TheT="0" TheC="0" DeltaT="19.949999999999999" DeltaTUnit="s" PositionZ="7825.4899999999998" PositionZUnit="µm" PositionX="19924.651468215841" PositionXUnit="µm" PositionY="19870.989391479248" PositionYUnit="µm" ExposureTime="600" ExposureTimeUnit="ms"/>
  		</OME:Pixels>
  	</OME:Image>
  	<SA:StructuredAnnotations/>
  </OME>
  
  ===== TIFF Tags (first page) =====
  ImageWidth = 19190
  ImageLength = 19190
  BitsPerSample = 16
  Compression = 1
  PhotometricInterpretation = 1
  ImageDescription = <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
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
  		<OME:AcquisitionDate>2024-08-20T17:05:31Z</OME:AcquisitionDate>
  		<OME:ExperimenterRef ID="Experimenter:0"/>
  		<OME:InstrumentRef ID="Instrument:0"/>
  		<OME:ObjectiveSettings ID="Objective:0" Medium="Air" RefractiveIndex="1"/>
  		<OME:Pixels ID="Pixels:0" DimensionOrder="XYCZT" Type="uint16" SignificantBits="13" Interleaved="false" SizeX="19190" SizeY="19190" SizeC="1" SizeZ="1" SizeT="1" PhysicalSizeX="1.6250000000000002" PhysicalSizeXUnit="µm" PhysicalSizeY="1.6250000000000002" PhysicalSizeYUnit="µm">
  			<OME:Channel ID="Channel:0" Name="DAPI" SamplesPerPixel="1" ContrastMethod="Fluorescence" EmissionWavelength="455" EmissionWavelengthUnit="nm" Color="65535">
  				<LightSourceSettings ID="LightSource:0"/>
  				<DetectorSettings ID="Detector:0" Binning="1x1"/>
  			</OME:Channel>
  			<OME:TiffData IFD="0" FirstZ="0" FirstT="0" FirstC="0" PlaneCount="1"/>
  			<OME:Plane TheZ="0" TheT="0" TheC="0" DeltaT="19.949999999999999" DeltaTUnit="s" PositionZ="7825.4899999999998" PositionZUnit="µm" PositionX="19924.651468215841" PositionXUnit="µm" PositionY="19870.989391479248" PositionYUnit="µm" ExposureTime="600" ExposureTimeUnit="ms"/>
  		</OME:Pixels>
  	</OME:Image>
  	<SA:StructuredAnnotations/>
  </OME>
  Make = Hamamatsu
  Model = Hamamatsu ORCA-Flash4.0
  StripOffsets = (29086, 2485406, 4941726, 7398046, 9854366, 12310686, 14767006, 17223326, 19679646, 22135966, 24592286, 27048606, 29504926, 31961246, 34417566, 36873886, 39330206, 41786526, 44242846, 46699166, 49155486, 51611806, 54068126, 56524446, 58980766, 61437086, 63893406, 66349726, 68806046, 71262366, 73718686, 76175006, 78631326, 81087646, 83543966, 86000286, 88456606, 90912926, 93369246, 95825566, 98281886, 100738206, 103194526, 105650846, 108107166, 110563486, 113019806, 115476126, 117932446, 120388766, 122845086, 125301406, 127757726, 130214046, 132670366, 135126686, 137583006, 140039326, 142495646, 144951966, 147408286, 149864606, 152320926, 154777246, 157233566, 159689886, 162146206, 164602526, 167058846, 169515166, 171971486, 174427806, 176884126, 179340446, 181796766, 184253086, 186709406, 189165726, 191622046, 194078366, 196534686, 198991006, 201447326, 203903646, 206359966, 208816286, 211272606, 213728926, 216185246, 218641566, 221097886, 223554206, 226010526, 228466846, 230923166, 233379486, 235835806, 238292126, 240748446, 243204766, 245661086, 248117406, 250573726, 253030046, 255486366, 257942686, 260399006, 262855326, 265311646, 267767966, 270224286, 272680606, 275136926, 277593246, 280049566, 282505886, 284962206, 287418526, 289874846, 292331166, 294787486, 297243806, 299700126, 302156446, 304612766, 307069086, 309525406, 311981726, 314438046, 316894366, 319350686, 321807006, 324263326, 326719646, 329175966, 331632286, 334088606, 336544926, 339001246, 341457566, 343913886, 346370206, 348826526, 351282846, 353739166, 356195486, 358651806, 361108126, 363564446, 366020766, 368477086, 370933406, 373389726, 375846046, 378302366, 380758686, 383215006, 385671326, 388127646, 390583966, 393040286, 395496606, 397952926, 400409246, 402865566, 405321886, 407778206, 410234526, 412690846, 415147166, 417603486, 420059806, 422516126, 424972446, 427428766, 429885086, 432341406, 434797726, 437254046, 439710366, 442166686, 444623006, 447079326, 449535646, 451991966, 454448286, 456904606, 459360926, 461817246, 464273566, 466729886, 469186206, 471642526, 474098846, 476555166, 479011486, 481467806, 483924126, 486380446, 488836766, 491293086, 493749406, 496205726, 498662046, 501118366, 503574686, 506031006, 508487326, 510943646, 513399966, 515856286, 518312606, 520768926, 523225246, 525681566, 528137886, 530594206, 533050526, 535506846, 537963166, 540419486, 542875806, 545332126, 547788446, 550244766, 552701086, 555157406, 557613726, 560070046, 562526366, 564982686, 567439006, 569895326, 572351646, 574807966, 577264286, 579720606, 582176926, 584633246, 587089566, 589545886, 592002206, 594458526, 596914846, 599371166, 601827486, 604283806, 606740126, 609196446, 611652766, 614109086, 616565406, 619021726, 621478046, 623934366, 626390686, 628847006, 631303326, 633759646, 636215966, 638672286, 641128606, 643584926, 646041246, 648497566, 650953886, 653410206, 655866526, 658322846, 660779166, 663235486, 665691806, 668148126, 670604446, 673060766, 675517086, 677973406, 680429726, 682886046, 685342366, 687798686, 690255006, 692711326, 695167646, 697623966, 700080286, 702536606, 704992926, 707449246, 709905566, 712361886, 714818206, 717274526, 719730846, 722187166, 724643486, 727099806, 729556126, 732012446, 734468766)
  Orientation = 1
  SamplesPerPixel = 1
  RowsPerStrip = 64
  StripByteCounts = (2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320)
  XResolution = (96, 1)
  YResolution = (96, 1)
  PlanarConfiguration = 1
  ResolutionUnit = 2
  DateTime = 2024:08:20 12:05:10
  Artist = OlympusIX83
  OlympusSIS = {'name': '', 'datetime': datetime.datetime(2024, 8, 20, 12, 5), 'pixelsizex': 1.6250000000000001e-06, 'pixelsizey': 1.6250000000000001e-06, 'magnification': 4.0, 'cameraname': '', 'picturetype': ''}
  ExifTag = {'ExifVersion': '0210', 'DateTimeDigitized': '2024:08:20 12:05:31', 'ApertureValue': (4, 25), 'SubjectDistance': (13, 1000), 'FlashpixVersion': '0100', 'ColorSpace': 1, 'PixelXDimension': 19190, 'PixelYDimension': 19190}
  
  file_create_date: ['2025-01-15T12:53:57.372623-05:00']
  Group /general/TIFF_Metadata (LabMetaData) 
  experimenter: ['Giedre Silkuniene, Mantas Silkunas']
  institution: Old Dominion University
  lab: Pakhomov Lab
  session_id: single_time_point
  Group /general/subject (Subject) 
  identifier: 49e6433b-9a87-4e34-a650-d0f078566ccd
  session_description: ***Subject-Specific Description*** Subject ID: P1_20240820_A1. Fluorescent Channel(s) used: DAPI. 0 mm electrode elevation. Image taken before pulse exposure. Protocol: CanCan (with canceling pulses). Pulse duration - 600 ns. Protocol consisted of 9 packets of pulses delivered at 0.2MHz frequency. Protocol repeated 2 time(s) at 1Hz frequency.. ***General Protocol Description (Subject-Independent)*** Experiments were conducted using a four-electrode stainless steel setup with an inter-electrode distance of 10.0 mm. The electrodes were positioned either at the bottom of the plate (0 mm) or elevated 1 or 2 mm above the plate surface. The CanCan exposure protocol involved delivering packets of 300/600/900 ns pulses from four electrodes. Initially, a single 300/600/900 ns pulse (7.2 kV) was applied from one electrode (e.g., electrode 1), constituting phase 1. Subsequently, simultaneous pulses with an amplitude reduced by 12.5% were delivered from two electrodes (e.g., electrodes 2 and 4), followed by another set of simultaneous pulses with an additional 12.5% amplitude reduction from electrodes 1 and 3. These simultaneous pulses represented phases 2, 3, and continued up to phase 8, with the amplitude reduced by 12.5% at each phase. After completing one packet of pulses, the sequence was repeated 9 times at a defined frequency. Upon completing these 9 repetitions, the protocol was either repeated 2, 4, or 6 times at a 1 Hz frequency or initiated anew from another electrode (e.g., electrode 2), ensuring that all four electrodes eventually served as the initiating electrode. Control protocols followed identical frequency and repetition schemes but lacked the subsequent, reduced-amplitude pulses delivered from the other electrodes. The number of protocol repetitions, pulse duration, and protocol type applied are noted under the Subject-Specific description.Before exposure, the growth medium was replaced with a physiological solution (in mM: 140 NaCl, 5.4 KCl, 2 CaCl2, 1.5 MgCl2, 10 D-glucose, and 10 HEPES; pH 7.3, 290–300 mOsm/kg) containing 1 µg/mL Hoechst and 1 µM YoPro-1 (YP). Hoechst, visualized via the DAPI channel, stained all cell nuclei. Thirty minutes post-exposure, the dye-containing solution was replaced with dye-free physiological solution, and YP uptake, serving as a semi-quantitative marker of membrane permeabilization induced by electroporation, was visualized via the FITC channel. For some experiments (indicated by the Cy3 channel), cell death was evaluated using propidium iodide staining two hours after exposure. More details about the methods are available in the related manuscript.
  session_start_time: 2025-01-15T12:53:57.372623-05:00
  timestamps_reference_time: 2025-01-15T12:53:57.372623-05:00


Here is a summary of the type 2 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Imaging_FITC (ImageSeries) FITC channel: YO-PRO-1 uptake to assess membrane permeabilization 30 minutes after exposure.********************File Metadata:
  ===== OME Metadata =====
  <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
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
  	<OME:Image ID="Image:0" Name="FITC">
  		<OME:AcquisitionDate>2024-08-20T18:23:01Z</OME:AcquisitionDate>
  		<OME:ExperimenterRef ID="Experimenter:0"/>
  		<OME:InstrumentRef ID="Instrument:0"/>
  		<OME:ObjectiveSettings ID="Objective:0" Medium="Air" RefractiveIndex="1"/>
  		<OME:Pixels ID="Pixels:0" DimensionOrder="XYCZT" Type="uint16" SignificantBits="13" Interleaved="false" SizeX="19190" SizeY="19190" SizeC="1" SizeZ="1" SizeT="1" PhysicalSizeX="1.6250000000000002" PhysicalSizeXUnit="µm" PhysicalSizeY="1.6250000000000002" PhysicalSizeYUnit="µm">
  			<OME:Channel ID="Channel:0" Name="FITC" SamplesPerPixel="1" ContrastMethod="Fluorescence" EmissionWavelength="518" EmissionWavelengthUnit="nm" Color="16712447">
  				<LightSourceSettings ID="LightSource:0"/>
  				<DetectorSettings ID="Detector:0" Binning="1x1"/>
  			</OME:Channel>
  			<OME:TiffData IFD="0" FirstZ="0" FirstT="0" FirstC="0" PlaneCount="1"/>
  			<OME:Plane TheZ="0" TheT="0" TheC="0" DeltaT="7.0469999999999997" DeltaTUnit="s" PositionZ="7825.4899999999998" PositionZUnit="µm" PositionX="19924.651468215841" PositionXUnit="µm" PositionY="19870.989391479248" PositionYUnit="µm" ExposureTime="200" ExposureTimeUnit="ms"/>
  		</OME:Pixels>
  	</OME:Image>
  	<SA:StructuredAnnotations/>
  </OME>
  
  ===== TIFF Tags (first page) =====
  ImageWidth = 19190
  ImageLength = 19190
  BitsPerSample = 16
  Compression = 1
  PhotometricInterpretation = 1
  ImageDescription = <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
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
  	<OME:Image ID="Image:0" Name="FITC">
  		<OME:AcquisitionDate>2024-08-20T18:23:01Z</OME:AcquisitionDate>
  		<OME:ExperimenterRef ID="Experimenter:0"/>
  		<OME:InstrumentRef ID="Instrument:0"/>
  		<OME:ObjectiveSettings ID="Objective:0" Medium="Air" RefractiveIndex="1"/>
  		<OME:Pixels ID="Pixels:0" DimensionOrder="XYCZT" Type="uint16" SignificantBits="13" Interleaved="false" SizeX="19190" SizeY="19190" SizeC="1" SizeZ="1" SizeT="1" PhysicalSizeX="1.6250000000000002" PhysicalSizeXUnit="µm" PhysicalSizeY="1.6250000000000002" PhysicalSizeYUnit="µm">
  			<OME:Channel ID="Channel:0" Name="FITC" SamplesPerPixel="1" ContrastMethod="Fluorescence" EmissionWavelength="518" EmissionWavelengthUnit="nm" Color="16712447">
  				<LightSourceSettings ID="LightSource:0"/>
  				<DetectorSettings ID="Detector:0" Binning="1x1"/>
  			</OME:Channel>
  			<OME:TiffData IFD="0" FirstZ="0" FirstT="0" FirstC="0" PlaneCount="1"/>
  			<OME:Plane TheZ="0" TheT="0" TheC="0" DeltaT="7.0469999999999997" DeltaTUnit="s" PositionZ="7825.4899999999998" PositionZUnit="µm" PositionX="19924.651468215841" PositionXUnit="µm" PositionY="19870.989391479248" PositionYUnit="µm" ExposureTime="200" ExposureTimeUnit="ms"/>
  		</OME:Pixels>
  	</OME:Image>
  	<SA:StructuredAnnotations/>
  </OME>
  Make = Hamamatsu
  Model = Hamamatsu ORCA-Flash4.0
  StripOffsets = (29090, 2485410, 4941730, 7398050, 9854370, 12310690, 14767010, 17223330, 19679650, 22135970, 24592290, 27048610, 29504930, 31961250, 34417570, 36873890, 39330210, 41786530, 44242850, 46699170, 49155490, 51611810, 54068130, 56524450, 58980770, 61437090, 63893410, 66349730, 68806050, 71262370, 73718690, 76175010, 78631330, 81087650, 83543970, 86000290, 88456610, 90912930, 93369250, 95825570, 98281890, 100738210, 103194530, 105650850, 108107170, 110563490, 113019810, 115476130, 117932450, 120388770, 122845090, 125301410, 127757730, 130214050, 132670370, 135126690, 137583010, 140039330, 142495650, 144951970, 147408290, 149864610, 152320930, 154777250, 157233570, 159689890, 162146210, 164602530, 167058850, 169515170, 171971490, 174427810, 176884130, 179340450, 181796770, 184253090, 186709410, 189165730, 191622050, 194078370, 196534690, 198991010, 201447330, 203903650, 206359970, 208816290, 211272610, 213728930, 216185250, 218641570, 221097890, 223554210, 226010530, 228466850, 230923170, 233379490, 235835810, 238292130, 240748450, 243204770, 245661090, 248117410, 250573730, 253030050, 255486370, 257942690, 260399010, 262855330, 265311650, 267767970, 270224290, 272680610, 275136930, 277593250, 280049570, 282505890, 284962210, 287418530, 289874850, 292331170, 294787490, 297243810, 299700130, 302156450, 304612770, 307069090, 309525410, 311981730, 314438050, 316894370, 319350690, 321807010, 324263330, 326719650, 329175970, 331632290, 334088610, 336544930, 339001250, 341457570, 343913890, 346370210, 348826530, 351282850, 353739170, 356195490, 358651810, 361108130, 363564450, 366020770, 368477090, 370933410, 373389730, 375846050, 378302370, 380758690, 383215010, 385671330, 388127650, 390583970, 393040290, 395496610, 397952930, 400409250, 402865570, 405321890, 407778210, 410234530, 412690850, 415147170, 417603490, 420059810, 422516130, 424972450, 427428770, 429885090, 432341410, 434797730, 437254050, 439710370, 442166690, 444623010, 447079330, 449535650, 451991970, 454448290, 456904610, 459360930, 461817250, 464273570, 466729890, 469186210, 471642530, 474098850, 476555170, 479011490, 481467810, 483924130, 486380450, 488836770, 491293090, 493749410, 496205730, 498662050, 501118370, 503574690, 506031010, 508487330, 510943650, 513399970, 515856290, 518312610, 520768930, 523225250, 525681570, 528137890, 530594210, 533050530, 535506850, 537963170, 540419490, 542875810, 545332130, 547788450, 550244770, 552701090, 555157410, 557613730, 560070050, 562526370, 564982690, 567439010, 569895330, 572351650, 574807970, 577264290, 579720610, 582176930, 584633250, 587089570, 589545890, 592002210, 594458530, 596914850, 599371170, 601827490, 604283810, 606740130, 609196450, 611652770, 614109090, 616565410, 619021730, 621478050, 623934370, 626390690, 628847010, 631303330, 633759650, 636215970, 638672290, 641128610, 643584930, 646041250, 648497570, 650953890, 653410210, 655866530, 658322850, 660779170, 663235490, 665691810, 668148130, 670604450, 673060770, 675517090, 677973410, 680429730, 682886050, 685342370, 687798690, 690255010, 692711330, 695167650, 697623970, 700080290, 702536610, 704992930, 707449250, 709905570, 712361890, 714818210, 717274530, 719730850, 722187170, 724643490, 727099810, 729556130, 732012450, 734468770)
  Orientation = 1
  SamplesPerPixel = 1
  RowsPerStrip = 64
  StripByteCounts = (2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320)
  XResolution = (96, 1)
  YResolution = (96, 1)
  PlanarConfiguration = 1
  ResolutionUnit = 2
  DateTime = 2024:08:20 13:22:53
  Artist = OlympusIX83
  OlympusSIS = {'name': '', 'datetime': datetime.datetime(2024, 8, 20, 13, 22), 'pixelsizex': 1.6250000000000001e-06, 'pixelsizey': 1.6250000000000001e-06, 'magnification': 4.0, 'cameraname': '', 'picturetype': ''}
  ExifTag = {'ExifVersion': '0210', 'DateTimeDigitized': '2024:08:20 13:23:01', 'ApertureValue': (4, 25), 'SubjectDistance': (13, 1000), 'FlashpixVersion': '0100', 'ColorSpace': 1, 'PixelXDimension': 19190, 'PixelYDimension': 19190}
  
  file_create_date: ['2025-01-15T12:56:23.743314-05:00']
  Group /general/TIFF_Metadata (LabMetaData) 
  experimenter: ['Giedre Silkuniene, Mantas Silkunas']
  institution: Old Dominion University
  lab: Pakhomov Lab
  session_id: single_time_point
  Group /general/subject (Subject) 
  identifier: 4482a62f-8598-40e9-805f-657cf9440911
  session_description: ***Subject-Specific Description*** Subject ID: P1_20240820_A1. Fluorescent Channel(s) used: FITC. 0 mm electrode elevation. Image taken 30min after pulse exposure. Protocol: CanCan (with canceling pulses). Pulse duration - 600 ns. Protocol consisted of 9 packets of pulses delivered at 0.2MHz frequency. Protocol repeated 2 time(s) at 1Hz frequency.. ***General Protocol Description (Subject-Independent)*** Experiments were conducted using a four-electrode stainless steel setup with an inter-electrode distance of 10.0 mm. The electrodes were positioned either at the bottom of the plate (0 mm) or elevated 1 or 2 mm above the plate surface. The CanCan exposure protocol involved delivering packets of 300/600/900 ns pulses from four electrodes. Initially, a single 300/600/900 ns pulse (7.2 kV) was applied from one electrode (e.g., electrode 1), constituting phase 1. Subsequently, simultaneous pulses with an amplitude reduced by 12.5% were delivered from two electrodes (e.g., electrodes 2 and 4), followed by another set of simultaneous pulses with an additional 12.5% amplitude reduction from electrodes 1 and 3. These simultaneous pulses represented phases 2, 3, and continued up to phase 8, with the amplitude reduced by 12.5% at each phase. After completing one packet of pulses, the sequence was repeated 9 times at a defined frequency. Upon completing these 9 repetitions, the protocol was either repeated 2, 4, or 6 times at a 1 Hz frequency or initiated anew from another electrode (e.g., electrode 2), ensuring that all four electrodes eventually served as the initiating electrode. Control protocols followed identical frequency and repetition schemes but lacked the subsequent, reduced-amplitude pulses delivered from the other electrodes. The number of protocol repetitions, pulse duration, and protocol type applied are noted under the Subject-Specific description.Before exposure, the growth medium was replaced with a physiological solution (in mM: 140 NaCl, 5.4 KCl, 2 CaCl2, 1.5 MgCl2, 10 D-glucose, and 10 HEPES; pH 7.3, 290–300 mOsm/kg) containing 1 µg/mL Hoechst and 1 µM YoPro-1 (YP). Hoechst, visualized via the DAPI channel, stained all cell nuclei. Thirty minutes post-exposure, the dye-containing solution was replaced with dye-free physiological solution, and YP uptake, serving as a semi-quantitative marker of membrane permeabilization induced by electroporation, was visualized via the FITC channel. For some experiments (indicated by the Cy3 channel), cell death was evaluated using propidium iodide staining two hours after exposure. More details about the methods are available in the related manuscript.
  session_start_time: 2025-01-15T12:56:23.743314-05:00
  timestamps_reference_time: 2025-01-15T12:56:23.743314-05:00


Here is a summary of the type 3 NWB files:
  Group / (NWBFile) 
  Group /acquisition/Imaging_Cy3-DAPI (ImageSeries) Cy3-DAPI channels: Combined imaging 2 hours after exposure. Propidium iodide (PI) visualized with Cy3 channel to evaluate dead cells. Nuclei staining (Hoechst) used for identifying all cells and assessing monolayer integrity (DAPI channel).********************File Metadata:
  ===== OME Metadata =====
  <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
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
  		<OME:AcquisitionDate>2024-10-02T21:01:28Z</OME:AcquisitionDate>
  		<OME:ExperimenterRef ID="Experimenter:0"/>
  		<OME:InstrumentRef ID="Instrument:0"/>
  		<OME:ObjectiveSettings ID="Objective:0" Medium="Air" RefractiveIndex="1"/>
  		<OME:Pixels ID="Pixels:0" DimensionOrder="XYCZT" Type="uint16" SignificantBits="11" Interleaved="false" SizeX="19190" SizeY="19190" SizeC="2" SizeZ="1" SizeT="1" PhysicalSizeX="1.6250000000000002" PhysicalSizeXUnit="µm" PhysicalSizeY="1.6250000000000002" PhysicalSizeYUnit="µm">
  			<OME:Channel ID="Channel:0" Name="Cy3" SamplesPerPixel="1" ContrastMethod="Fluorescence" EmissionWavelength="565" EmissionWavelengthUnit="nm" Color="-16774913">
  				<LightSourceSettings ID="LightSource:0"/>
  				<DetectorSettings ID="Detector:0" Binning="1x1"/>
  			</OME:Channel>
  			<OME:Channel ID="Channel:1" Name="DAPI" SamplesPerPixel="1" ContrastMethod="Fluorescence" EmissionWavelength="455" EmissionWavelengthUnit="nm" Color="65535">
  				<LightSourceSettings ID="LightSource:0"/>
  				<DetectorSettings ID="Detector:0" Binning="1x1"/>
  			</OME:Channel>
  			<OME:TiffData IFD="0" FirstZ="0" FirstT="0" FirstC="0" PlaneCount="2"/>
  			<OME:Plane TheZ="0" TheT="0" TheC="0" DeltaT="9.3100000000000005" DeltaTUnit="s" PositionZ="6865.8400000000001" PositionZUnit="µm" PositionX="19924.651468215841" PositionXUnit="µm" PositionY="19870.989391479248" PositionYUnit="µm" ExposureTime="200" ExposureTimeUnit="ms"/>
  			<OME:Plane TheZ="0" TheT="0" TheC="1" DeltaT="11.109" DeltaTUnit="s" PositionZ="6865.8400000000001" PositionZUnit="µm" PositionX="19924.651468215841" PositionXUnit="µm" PositionY="19870.989391479248" PositionYUnit="µm" ExposureTime="600" ExposureTimeUnit="ms"/>
  		</OME:Pixels>
  	</OME:Image>
  	<SA:StructuredAnnotations/>
  </OME>
  
  ===== TIFF Tags (first page) =====
  ImageWidth = 19190
  ImageLength = 19190
  BitsPerSample = 16
  Compression = 1
  PhotometricInterpretation = 1
  ImageDescription = <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
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
  		<OME:AcquisitionDate>2024-10-02T21:01:28Z</OME:AcquisitionDate>
  		<OME:ExperimenterRef ID="Experimenter:0"/>
  		<OME:InstrumentRef ID="Instrument:0"/>
  		<OME:ObjectiveSettings ID="Objective:0" Medium="Air" RefractiveIndex="1"/>
  		<OME:Pixels ID="Pixels:0" DimensionOrder="XYCZT" Type="uint16" SignificantBits="11" Interleaved="false" SizeX="19190" SizeY="19190" SizeC="2" SizeZ="1" SizeT="1" PhysicalSizeX="1.6250000000000002" PhysicalSizeXUnit="µm" PhysicalSizeY="1.6250000000000002" PhysicalSizeYUnit="µm">
  			<OME:Channel ID="Channel:0" Name="Cy3" SamplesPerPixel="1" ContrastMethod="Fluorescence" EmissionWavelength="565" EmissionWavelengthUnit="nm" Color="-16774913">
  				<LightSourceSettings ID="LightSource:0"/>
  				<DetectorSettings ID="Detector:0" Binning="1x1"/>
  			</OME:Channel>
  			<OME:Channel ID="Channel:1" Name="DAPI" SamplesPerPixel="1" ContrastMethod="Fluorescence" EmissionWavelength="455" EmissionWavelengthUnit="nm" Color="65535">
  				<LightSourceSettings ID="LightSource:0"/>
  				<DetectorSettings ID="Detector:0" Binning="1x1"/>
  			</OME:Channel>
  			<OME:TiffData IFD="0" FirstZ="0" FirstT="0" FirstC="0" PlaneCount="2"/>
  			<OME:Plane TheZ="0" TheT="0" TheC="0" DeltaT="9.3100000000000005" DeltaTUnit="s" PositionZ="6865.8400000000001" PositionZUnit="µm" PositionX="19924.651468215841" PositionXUnit="µm" PositionY="19870.989391479248" PositionYUnit="µm" ExposureTime="200" ExposureTimeUnit="ms"/>
  			<OME:Plane TheZ="0" TheT="0" TheC="1" DeltaT="11.109" DeltaTUnit="s" PositionZ="6865.8400000000001" PositionZUnit="µm" PositionX="19924.651468215841" PositionXUnit="µm" PositionY="19870.989391479248" PositionYUnit="µm" ExposureTime="600" ExposureTimeUnit="ms"/>
  		</OME:Pixels>
  	</OME:Image>
  	<SA:StructuredAnnotations/>
  </OME>
  Make = Hamamatsu
  Model = Hamamatsu ORCA-Flash4.0
  StripOffsets = (29118, 2485438, 4941758, 7398078, 9854398, 12310718, 14767038, 17223358, 19679678, 22135998, 24592318, 27048638, 29504958, 31961278, 34417598, 36873918, 39330238, 41786558, 44242878, 46699198, 49155518, 51611838, 54068158, 56524478, 58980798, 61437118, 63893438, 66349758, 68806078, 71262398, 73718718, 76175038, 78631358, 81087678, 83543998, 86000318, 88456638, 90912958, 93369278, 95825598, 98281918, 100738238, 103194558, 105650878, 108107198, 110563518, 113019838, 115476158, 117932478, 120388798, 122845118, 125301438, 127757758, 130214078, 132670398, 135126718, 137583038, 140039358, 142495678, 144951998, 147408318, 149864638, 152320958, 154777278, 157233598, 159689918, 162146238, 164602558, 167058878, 169515198, 171971518, 174427838, 176884158, 179340478, 181796798, 184253118, 186709438, 189165758, 191622078, 194078398, 196534718, 198991038, 201447358, 203903678, 206359998, 208816318, 211272638, 213728958, 216185278, 218641598, 221097918, 223554238, 226010558, 228466878, 230923198, 233379518, 235835838, 238292158, 240748478, 243204798, 245661118, 248117438, 250573758, 253030078, 255486398, 257942718, 260399038, 262855358, 265311678, 267767998, 270224318, 272680638, 275136958, 277593278, 280049598, 282505918, 284962238, 287418558, 289874878, 292331198, 294787518, 297243838, 299700158, 302156478, 304612798, 307069118, 309525438, 311981758, 314438078, 316894398, 319350718, 321807038, 324263358, 326719678, 329175998, 331632318, 334088638, 336544958, 339001278, 341457598, 343913918, 346370238, 348826558, 351282878, 353739198, 356195518, 358651838, 361108158, 363564478, 366020798, 368477118, 370933438, 373389758, 375846078, 378302398, 380758718, 383215038, 385671358, 388127678, 390583998, 393040318, 395496638, 397952958, 400409278, 402865598, 405321918, 407778238, 410234558, 412690878, 415147198, 417603518, 420059838, 422516158, 424972478, 427428798, 429885118, 432341438, 434797758, 437254078, 439710398, 442166718, 444623038, 447079358, 449535678, 451991998, 454448318, 456904638, 459360958, 461817278, 464273598, 466729918, 469186238, 471642558, 474098878, 476555198, 479011518, 481467838, 483924158, 486380478, 488836798, 491293118, 493749438, 496205758, 498662078, 501118398, 503574718, 506031038, 508487358, 510943678, 513399998, 515856318, 518312638, 520768958, 523225278, 525681598, 528137918, 530594238, 533050558, 535506878, 537963198, 540419518, 542875838, 545332158, 547788478, 550244798, 552701118, 555157438, 557613758, 560070078, 562526398, 564982718, 567439038, 569895358, 572351678, 574807998, 577264318, 579720638, 582176958, 584633278, 587089598, 589545918, 592002238, 594458558, 596914878, 599371198, 601827518, 604283838, 606740158, 609196478, 611652798, 614109118, 616565438, 619021758, 621478078, 623934398, 626390718, 628847038, 631303358, 633759678, 636215998, 638672318, 641128638, 643584958, 646041278, 648497598, 650953918, 653410238, 655866558, 658322878, 660779198, 663235518, 665691838, 668148158, 670604478, 673060798, 675517118, 677973438, 680429758, 682886078, 685342398, 687798718, 690255038, 692711358, 695167678, 697623998, 700080318, 702536638, 704992958, 707449278, 709905598, 712361918, 714818238, 717274558, 719730878, 722187198, 724643518, 727099838, 729556158, 732012478, 734468798)
  Orientation = 1
  SamplesPerPixel = 1
  RowsPerStrip = 64
  StripByteCounts = (2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320, 2456320)
  XResolution = (96, 1)
  YResolution = (96, 1)
  PlanarConfiguration = 1
  ResolutionUnit = 2
  DateTime = 2024:10:02 16:01:17
  Artist = OlympusIX83
  OlympusSIS = {'name': '', 'datetime': datetime.datetime(2024, 10, 2, 16, 1), 'pixelsizex': 1.6250000000000001e-06, 'pixelsizey': 1.6250000000000001e-06, 'magnification': 4.0, 'cameraname': '', 'picturetype': ''}
  ExifTag = {'ExifVersion': '0210', 'DateTimeDigitized': '2024:10:02 16:01:28', 'ApertureValue': (4, 25), 'SubjectDistance': (13, 1000), 'FlashpixVersion': '0100', 'ColorSpace': 1, 'PixelXDimension': 19190, 'PixelYDimension': 19190}
  
  file_create_date: ['2025-01-15T13:07:31.691205-05:00']
  Group /general/TIFF_Metadata (LabMetaData) 
  experimenter: ['Giedre Silkuniene, Mantas Silkunas']
  institution: Old Dominion University
  lab: Pakhomov Lab
  session_id: single_time_point
  Group /general/subject (Subject) 
  identifier: 351edcc9-f4f7-41dc-aa71-813ba1f3bab6
  session_description: ***Subject-Specific Description*** Subject ID: P1_20241002_A1. Fluorescent Channel(s) used: Cy3-DAPI. 0 mm electrode elevation. Image taken 2 hours after pulse exposure. Protocol: CanCan (with canceling pulses). Pulse duration - 600 ns. Protocol consisted of 9 packets of pulses delivered at 0.2MHz frequency. Protocol repeated 2 time(s) at 1Hz frequency.. ***General Protocol Description (Subject-Independent)*** Experiments were conducted using a four-electrode stainless steel setup with an inter-electrode distance of 10.0 mm. The electrodes were positioned either at the bottom of the plate (0 mm) or elevated 1 or 2 mm above the plate surface. The CanCan exposure protocol involved delivering packets of 300/600/900 ns pulses from four electrodes. Initially, a single 300/600/900 ns pulse (7.2 kV) was applied from one electrode (e.g., electrode 1), constituting phase 1. Subsequently, simultaneous pulses with an amplitude reduced by 12.5% were delivered from two electrodes (e.g., electrodes 2 and 4), followed by another set of simultaneous pulses with an additional 12.5% amplitude reduction from electrodes 1 and 3. These simultaneous pulses represented phases 2, 3, and continued up to phase 8, with the amplitude reduced by 12.5% at each phase. After completing one packet of pulses, the sequence was repeated 9 times at a defined frequency. Upon completing these 9 repetitions, the protocol was either repeated 2, 4, or 6 times at a 1 Hz frequency or initiated anew from another electrode (e.g., electrode 2), ensuring that all four electrodes eventually served as the initiating electrode. Control protocols followed identical frequency and repetition schemes but lacked the subsequent, reduced-amplitude pulses delivered from the other electrodes. The number of protocol repetitions, pulse duration, and protocol type applied are noted under the Subject-Specific description.Before exposure, the growth medium was replaced with a physiological solution (in mM: 140 NaCl, 5.4 KCl, 2 CaCl2, 1.5 MgCl2, 10 D-glucose, and 10 HEPES; pH 7.3, 290–300 mOsm/kg) containing 1 µg/mL Hoechst and 1 µM YoPro-1 (YP). Hoechst, visualized via the DAPI channel, stained all cell nuclei. Thirty minutes post-exposure, the dye-containing solution was replaced with dye-free physiological solution, and YP uptake, serving as a semi-quantitative marker of membrane permeabilization induced by electroporation, was visualized via the FITC channel. For some experiments (indicated by the Cy3 channel), cell death was evaluated using propidium iodide staining two hours after exposure. More details about the methods are available in the related manuscript.
  session_start_time: 2025-01-15T13:07:31.691205-05:00
  timestamps_reference_time: 2025-01-15T13:07:31.691205-05:00
