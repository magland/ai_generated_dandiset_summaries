## Experiment Summary

The experiment conducted for Dandiset 000529 employs an electrophysiological approach to evaluate the impedance profiles of various electrode coatings using Electrochemical Impedance Spectroscopy (EIS). The investigation aims to understand the electrochemical properties of electrodes with different surface treatments: RuOx (Sputtered Ruthenium Oxide), AIROF (Activated Iridium Oxide), and SIROF (Sputtered Iridium Oxide). Each electrode's performance is characterized by its impedance at a given frequency, Z-real, and Z-imaginary values. The data helps ascertain which electrode coating provides optimal performance for extracellular electrophysiological recordings.

EIS experiments were conducted in vitro, eliminating the involvement of live animals. The data sets include comprehensive metadata on electrode specifics, such as the electrode area, group, and location. Various devices, notably GAMRY potentiostats, were deployed to measure the impedance values under different experimental conditions. These measurements are essential for developing high-fidelity neural interfaces, aiming to improve the signal quality and longevity of neural recording electrodes.

## Data Description

The NWB files store all relevant data acquired during the EIS experiments. Each file includes a DynamicTable under the `acquisition` group, listing frequency, Z-real, and Z-imaginary values. Specific device information and metadata are detailed under the `general` group, including the type of electrode coating, the electrode group, and the location of electrodes. Additional metadata includes the date and time of each session, the experimenter, and session-specific details, such as session ID and description.

### Available Data in NWB Files:
- **DynamicTable /acquisition/EIS_Impedance**
  - Frequency
  - Z-real
  - Z-imaginary
- **General Metadata**
  - Devices (e.g., GAMRY potentiostat)
  - Electrode groups and properties
  - Subject information (identifier, session details)
- **Electrode Details**
  - Area
  - Electrode name
  - Group and location
  - Measurement units

## Keywords
- Electrochemical Impedance Spectroscopy (EIS)
- Extracellular electrophysiology
- Electrode coating
- Impedance measurement
- RuOx
- AIROF
- SIROF
- Potentiostatic measurements
- Neural interfaces
- In vitro experiment