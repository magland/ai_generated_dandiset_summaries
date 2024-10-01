## Abstract

This dataset supports research on the neural mechanisms underlying affective states, specifically aiming to provide causal evidence of a line attractor encoding such states. The experiments were conducted on male Mus musculus (house mice) using behavioral observation methodologies complemented with GCaMP-based calcium imaging. Key focus areas include aggressive interactions observed through resident-intruder assays. Neural data were captured from the ventromedial hypothalamus, ventrolateral part (VMHvl), which is associated with aggression and social behaviors.

Calcium imaging data were collected using both two-photon and one-photon miniscopes. The data analysis incorporated latent dynamical models to identify low-dimensional neural representations of the observed behaviors. Key measurements included both behavioral time stamps and neural activity traces, allowing for the investigation of neural correlates of specific behavioral epochs.

## Data Description

The NWB files contain various data structures including:
- **/analysis/rSLDS**: Dynamic table providing weights contributed by each cell for specific latent factors.
- **/general/devices**: Device descriptions including two-photon microscopes and one-photon miniscopes.
- **/processing/behavior**: Processed behavioral data including timestamps and intervals of specific behaviors such as 'Balc in cage' and 'attack'.
- **/processing/ophys**: Preprocessed calcium imaging data, including motion-corrected neural traces.
- **/general/subject**: Metadata for individual subjects, providing unique identifiers.
- **/session**: Metadata for experimental sessions including descriptions, start times, and reference times.

## Keywords

- Neural mechanisms
- Affective states
- Calcium imaging
- Behavior
- Resident-intruder assay
- Mus musculus
- VMHvl
- Two-photon microscopy
- Miniscopes
- Latent dynamical models
