# Simulation Extension Example Dataset (DANDI:000064/0.221025.1735)

## Experiment Summary

This dataset presents the results of a simulated hippocampal network generated using the NeuroH5 software developed by the Soltesz Lab. The simulation leverages the NeuroH5 platform to model the electrophysiological properties of hippocampal neurons, focusing specifically on the somatic potentials within a network containing 1136 neuronal compartments. The primary aim of this simulation is likely to understand the intricate dynamics of hippocampal activity, potentially in relation to specific stimuli or experimental conditions, thereby offering insights into the functional roles of different cell types within the hippocampus.

The data have been meticulously converted to the Neurodata Without Borders (NWB) format using the ndx-simulation-output extension to ensure compatibility and standardization across neural data analysis platforms. As a result, researchers can efficiently access and analyze this simulation data for computational neuroscience studies, enabling further exploration of hippocampal network behaviors and potential applications in neurological research.

## NWB File Data Description

The available NWB file includes detailed simulation data subdivided into various groups and datasets. Key components of the file are:

- **Soma Potentials**: Stored in the `/acquisition/soma_potential` group as a `CompartmentSeries`. This dataset includes a corresponding `DynamicTableRegion` for soma compartments, encompassing all 1136 compartments.
- **Simulation Metadata**: Contains comprehensive metadata about the simulation within the `/general/simulation` group. This group includes a `Compartments` subgroup with detailed information such as cell type abbreviations, compartment IDs, and a column index for these data.
- **Subject Information**: Located under the `/general/subject` group, the subject is identified with the tag `Full_Scale_GC_Exc_Sat_LN_results_9600226.bw`, providing context for the session, which is described as a "simulated hippocampal network".

## Keywords

1. Hippocampal Network
2. Somatic Potential
3. NeuroH5
4. Computational Neuroscience
5. Neural Simulation
6. Electrophysiology
7. NWB (Neurodata Without Borders)
8. Cell Compartments
9. Data Conversion
10. Simulation Metadata