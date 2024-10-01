## Abstract

The dataset titled "Encoding of female mating dynamics by a hypothalamic line attractor" presents neural and behavioral data aimed at understanding how mating behaviors in female mice are encoded within the brain. This study leverages calcium imaging techniques to capture the activity patterns in the ventromedial hypothalamus (VMHvl) associated with various female mating behaviors. The data encompasses GCaMP traces, behavioral annotations, and low-dimensional latent factors derived from dynamical models, providing a comprehensive view of the neural correlates underlying these behaviors.

Longitudinal imaging experiments were conducted using a one-photon (1-p) miniscope to monitor neural activity in the VMHvl. Various behavioral epochs and their timings were meticulously annotated, including actions such as mounting, intromission, sniffing, and more. The aim is to decode how these behaviors are dynamically represented in the hypothalamus and to identify key neural factors contributing to these behavioral expressions.

## NWB Files Description

The dataset includes two NWB files featuring:

- **Behavioral Data**: Processed at 30 Hz, with timestamps in seconds. This data includes intervals for various behaviors such as into_male_cage, intromission, male_sniff, mount, approach, dart, lordose, sniff, stay, top_up, turn, and others.

- **Calcium Imaging Data (ophys)**: Preprocessed neural traces capturing calcium activity in the VMHvl. This includes motion correction and CNMFE (Constrained Non-negative Matrix Factorization for Endoscopic data) processed data.

- **DynamicTable**: Contains the weights contributed by each cell to particular latent factors, along with corresponding identifiers and values for latent factors 1 and 2.

## Keywords

1. Hypothalamus
2. Calcium Imaging
3. Female Mating Behavior
4. Neural Activity
5. Behavioral Annotation
6. Latent Factors
7. VMHvl
8. GCaMP
9. Longitudinal Imaging
10. Resident-Intruder Assay