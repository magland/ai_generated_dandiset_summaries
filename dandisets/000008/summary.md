# Phenotypic Variation within and across Transcriptomic Cell Types in Mouse Motor Cortex

## Abstract
This study aims to elucidate the phenotypic diversity of neuronal cell types within the mouse motor cortex. By employing the Patch-seq technique, researchers performed patch-clamp recordings, biocytin staining, and single-cell RNA sequencing on over 1,300 neurons from the adult mouse motor cortex. This enabled a comprehensive morpho-electric annotation of almost all transcriptomically defined neural cell types. The resulting dataset combines detailed electrophysiological profiles with high-resolution transcriptomic data, enhancing our understanding of cellular heterogeneity in a complex cortical region.

The primary goal was to integrate morphological, electrical, and transcriptomic characteristics for a detailed phenotypic profile of distinct neuronal cell types. Intracellular electrophysiological recordings were conducted, adding a layer of functional data to the morphological and genetic characterization. This multidimensional dataset can serve as a vital resource for understanding the functional implications of transcriptomic diversity in neural populations.

## Data Description
The NWB files contain detailed intracellular electrophysiological data from the recorded neurons. The majority of the NWB files include:
- **CurrentClampSeries**: A series of current clamp recordings without descriptions, detailing various stimulus conditions and responses.
- **IntracellularElectrode** and **Device**: Metadata describing the electrode and device used for the recordings.
- **SweepTable**: A table grouping different PatchClampSeries together, providing sweep numbers, series data, and indices.

In total, there are 83 NWB files, comprising:
1. Type 1: 1 file with multiple **CurrentClampSeries**.
2. Type 2: 75 files with diverse **CurrentClampSeries**.
3. Type 3: 2 files, similar in structure to Type 2.
4. Type 4: 3 files containing **CurrentClampSeries**.
5. Type 5: 2 files with additional sweeps and series data.

The data include timestamp references, experiment descriptions, experimenter information, and session details, all associated with the Tolias lab at Baylor College of Medicine.

## Keywords
- Mouse Motor Cortex
- Patch-seq
- Electrophysiology
- Single-cell RNA Sequencing
- Intracellular Recording
- Neuronal Phenotyping
- Current Clamp
- Patch Clamp
- Transcriptomics
- Biocytin Staining