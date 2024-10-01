## Scientific Abstract

This dataset includes electrocorticography (ECoG) recordings captured from pigs and rats, with the principal focus on employing a 1024-channel intracranial electroencephalography (iEEG) microdisplay to visualize neuronal activity on the brain surface. The study is detailed in the accompanying paper titled "An electroencephalogram microdisplay to visualize neuronal activity on the brain surface." The primary aim of this experiment appears to be exploring the efficacy of high-density iEEG arrays in monitoring and mapping neuronal activities over the cortical surface, potentially providing novel insights into brain functionalities and applications in neuroprosthetics or neurological disorder treatments.

The recordings were achieved using multi-electrode extracellular electrophysiology recording techniques involving intricate surgical methods. The dataset features recordings from ten subjects, which include both domestic pigs (Sus scrofa domesticus) and Norway rats (Rattus norvegicus). The data files contain raw voltage measurements, auxiliary inputs, and supply voltage data compiled with an Intan Technologies system. While the recordings do contain noise, the accompanying journal article includes guidelines on data filtering and preprocessing.

## Data Available in NWB Files

The NWB files provided in the dataset encompass a range of data types and metadata:
- **Voltage Data**: Recorded from amplifiers of an Intan Technologies chip through acquisition groups under `ElectricalSeries`.
- **Analog Input Data**: Captured from Intan Technologies systems, recorded in `TimeSeries_analog_input`.
- **Auxiliary Input Data**: Voltage data from auxiliary input of the Intan Technologies chip stored in `TimeSeries_aux_input`.
- **Supply Voltage Data**: Monitored from the Intan chip as part of the `TimeSeries_supply_voltage` recordings.
- **Metadata**: Includes device descriptions (Intan Recording Controller) and electrode group information for ports A to H under the `general` group.
- **Electrode Details**: Detailed electrode metadata such as custom names, impedance, phase, location, and native channel names provided in the `extracellular_ephys/electrodes` table.
- **Subject Information**: Contains identifiers and additional details consistent with the acquisition sessions.

## Keywords

1. Electrocorticography (ECoG)
2. Intracranial Electroencephalography (iEEG)
3. Neuronal Activity Visualization
4. High-density Electrode Arrays
5. Multi-electrode Extracellular Recording
6. Neuroprosthetics
7. Pigs and Rats
8. Intan Technologies
9. Electrophysiological Recording
10. Brain Surface Mapping