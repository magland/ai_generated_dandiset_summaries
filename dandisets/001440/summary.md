## Abstract

The dataset titled "Bright-Field Images of Rat Nerves at Different Regeneration Stages with Axon and Myelin Segmentations" provides a detailed collection of bright-field optical microscopy images capturing various stages of axonal regeneration in rat peripheral nerves. This research effort aimed to support nerve repair studies by generating and utilizing high-quality imaging data as a training set for the AxonDeepSeg model, which was developed and validated in a published study (https://www.nature.com/articles/s41598-022-10066-6). Specifically, the dataset comprises data collected from adult rats, focusing on eight samples that were meticulously cropped to regions of interest, thereby serving as critical training data to enhance AxonDeepSeg's segmentation capabilities for axons and myelin.

The primary objective of this experiment was to facilitate the development of accurate automated segmentation tools for nerve regeneration research. By providing an annotated dataset with manual segmentation labels of axons and myelin layers, researchers sought to train and validate machine learning models, such as AxonDeepSeg, which can significantly aid in the analysis of nerve repair and regeneration processes. This resource not only contributes to the advancement of neuroimaging methods but also supports studies aiming to improve therapeutic strategies for nerve injuries.

## Data Description

The Dandiset includes bright-field microscopy images of rat nerve samples at various stages of regeneration, specifically tailored for use in AxonDeepSeg model training. Each of the eight samples (sub-uoftRat02, sub-uoftRat04, sub-uoftRat07, sub-uoftRat08, sub-uoftRat09, sub-uoftRat10, sub-uoftRat16, and sub-uoftRat17) comes with manually segmented "labels" identifying axon, myelin, and combined axonmyelin structures. Although there are no NWB files in the dataset, the available data adhere to the Brain Imaging Data Structure (BIDS) standard, ensuring consistent formatting and metadata structure across the 48 files encompassing a total size of approximately 144 MB.

## Keywords

- Bright-field microscopy
- Axonal regeneration
- Rat peripheral nerves
- AxonDeepSeg
- Myelin segmentation
- Neural repair
- Cropped regions of interest (ROI)
- Machine learning model training
- Neuroimaging dataset
- BIDS compliance