# Experiment Summary

This dataset documents an electrochemical impedance spectroscopy (EIS) experiment aimed at understanding the impedance characteristics of electrodes under various frequencies. The primary purpose seems to be to gather impedance data, including both real and imaginary components, as a function of frequency. The study involved the utilization of a potentiostatic EIS setup, specifically employing a GAMRY device to measure the impedance values across a range of frequencies.

Electrodes used in the experiment were documented in detail, with metadata specifying their material, location, and grouping. The experiment was conducted by researcher Yupeng Wu, with the dataset containing information about the electrodes' properties and their organization within the experimental setup. The session took place on November 20, 2023, and was logged methodically to facilitate further analysis and reproduction of results.

# Data Description

The available data in the NWB files includes:
- **Dynamic Table**: `EIS_Impedance` containing frequency, Z-real, and Z-imaginary values.
  - **Datasets**:
    - `frequency` (shape = 57, dtype = float64)
    - `id` (shape = 57, dtype = int32)
    - `zimaginary` (shape = 57, dtype = float64)
    - `zreal` (shape = 57, dtype = float64)
  
- **Device Information**: Details about the GAMRY device used for impedance measurement.
- **Extracellular Electrode Metadata**:
  - **Tables**: Information about the physical and positional properties of the electrodes.
  - **Datasets**: 
    - `area` (shape = 1, dtype = object)
    - `electrode_name` (shape = 1, dtype = object)
    - `group` (shape = 1, dtype = object)
    - `group_name` (shape = 1, dtype = object)
    - `id` (shape = 1, dtype = int32)
    - `location` (shape = 1, dtype = object)
    - `material` (shape = 1, dtype = object)
    - `units` (shape = 1, dtype = object)

# Keywords

1. Electrochemical Impedance Spectroscopy (EIS)
2. Impedance Measurement
3. Potentiostatic EIS
4. Frequency Response
5. Z-real
6. Z-imaginary
7. Electrode Metadata
8. GAMRY Device
9. Electrode Properties
10. Scientific Experiment Data