## Abstract

This dataset comprises electrochemical impedance spectroscopy (EIS) data collected to probe the impedance characteristics of various electrodes in a potentiostatic setup. The experiments were conducted to analyze the electrochemical properties by measuring the frequency response of the impedance (both real and imaginary components) across a range of frequencies from 0.01 to 5 MHz. The data collection was facilitated using a GAMRY device, tailored for precise impedance measurements. The experiments, performed by Cynthia Ezeh, aim to provide insights into the underlying electrochemical behaviors which could be critical for understanding material properties and optimizing electrode configurations.

The dataset contains records of multiple EIS experiments detailing the technical specifications, frequency, and impedance values. Metadata about the electrodes, including material, location, and associated electrode groups, are encapsulated within the dataset, providing a comprehensive overview of the experimental setup and conditions. This information can be pivotal for researchers aiming to replicate the experiments or apply the findings to related studies in electrochemistry and material science.

## NWB File Data Description

The NWB files in this dataset store extensive EIS data in structured formats. Specific datasets include:

1. **Frequency Data**: A vector array containing 88 frequency values (dtype: float64).
2. **Impedance Data**:
   - Z-real (Real component of impedance): Vector array with 88 float64 data points.
   - Z-imaginary (Imaginary component of impedance): Vector array with 88 float64 data points.
3. **Electrode Metadata**: Information on electrodes including their area, material, location, and group affiliations. This metadata is encoded in dynamic tables providing referenceable identifiers and object data types.

Additionally, each file makes provision for general metadata such as the device name (GAMRY), session ID, experiment description, experimenter details, and timestamps. The files also incorporate more specialized metadata, relevant to the extracellular electrophysiology of the electrodes used.

## Keywords

- Electrochemical Impedance Spectroscopy
- EIS
- Potentiostatic
- GAMRY Device
- Impedance Measurement
- Electrodes
- Material Science
- Electrophysiology
- Frequency Response
- Electrode Metadata