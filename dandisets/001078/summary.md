### Abstract

This study presents the NeuroTask dataset, a comprehensive benchmark aimed at advancing the analysis of multi-session, multi-task, and multi-subject neural data. Encompassing six datasets derived from motor cortical regions, NeuroTask covers seven distinct tasks distributed among seventeen subjects. The dataset is particularly designed to foster the development of methods that can efficiently and accurately process complex neural data across various sessions and tasks. The experiment evaluated the performance of monkeys executing both straight reaches and reaches that navigated around one or more intervening barriers, generating rich behavioral and neural recordings intended to serve as a versatile resource for computational neuroscience research.

The NeuroTask dataset integrates neural recordings from two rhesus monkeys (Macaca mulatta) captured during tasks designed to challenge their motor control and planning capabilities. Recordings were acquired from the primary motor cortex (M1) and the dorsal premotor cortex (PMd). Behavioral data, including hand and cursor position, velocity, and force, were also meticulously recorded along with event timestamps associated with task execution. The overarching objective is to enable the development and benchmarking of algorithms capable of handling the intricate and multi-faceted nature of neural datasets extracted from varied experimental conditions.

### Available Data in NWB Files

The NWB files from the NeuroTask dataset include:
- Spike counts per unit, recorded from channels in motor cortical areas M1 and PMd, sorted offline into putative single units.
- Behavioral data including hand and cursor positions in both x and y coordinates, hand and cursor velocities, and the number and position of maze barriers and targets.
- Event indications and timestamps marking key moments in the task, such as go cues, movement starts, and movement ends.
- Indices for filtering data per session, animal, and trial, facilitating the segmentation of data for specific analyses.

### Keywords

- Multi-task learning
- Neural data analysis
- Motor control
- Behavioral neuroscience
- Maze navigation
- Rhesus monkey
- Spike sorting
- Motor cortex
- Premotor cortex
- Neurodata Without Borders (NWB)