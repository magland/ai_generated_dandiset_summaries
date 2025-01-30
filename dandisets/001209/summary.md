## Abstract

The present study characterizes neural and muscular activities in a macaque monkey performing a reach-to-grasp task, offering valuable contributions to the understanding of motor control. The experimental protocol involved a center-out task with a variety of objects placed in different positions, requiring the monkey to execute precise reach and grasp movements. Neural recordings were made from electrode arrays implanted in the primary motor cortex (M1), while electromyographical (EMG) data were concurrently recorded from upper limb muscles. This comprehensive dataset is a part of the FALCON (Fusing Acquisition of Limb and Neural Categories) Benchmark, which seeks to provide a standardized evaluation framework for decoding neural activity related to complex motor behaviors.

This dataset facilitates the development and calibration of neural decodings by providing extensive neural and EMG datasets through different trial categories. The data is organized into three types: `held-in-calib`, many trials for decoder calibration; `held-in-minival`, a subset for validating models; and `held-out-calib`, a limited number of trials for few-shot calibration. These datasets are integral to advancing decoding techniques in brain-machine interface applications, granting insight into the dynamics of motor planning and execution across different contexts and conditions.

## Data Description

The NWB (Neurodata Without Borders) files contain detailed recordings of preprocessed EMG data from 16 muscles, providing a rich time series for analyzing muscle activation patterns during task performance. Also included is an evaluation mask indicating the specific time points within trials used for assessing the FALCON Benchmark objectives. Each NWB file features comprehensive trial metadata, encapsulating trial onset and completion events, target positions, object identities, trials' conditions, and performance outcomes. Electrodes from various motor cortex regions offer high-resolution spike times, sampled at 30 kHz, with additional metadata on electrode groups and configurations.

## Keywords

- Reach-to-grasp task
- Primary motor cortex
- Electromyography (EMG)
- Neural spiking activity
- Macaque monkey
- Brain-machine interface
- Motor control
- Electrode arrays
- Behavioral neuroscience
- FALCON Benchmark