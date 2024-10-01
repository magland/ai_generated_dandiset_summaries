## Abstract

The NeuroTask dataset is designed as a benchmark to advance methods for analyzing neurophysiological data across multiple sessions, tasks, and subjects. The dataset encompasses recordings from motor cortical regions in rhesus monkeys (Macaca mulatta), engaging in seven different motor tasks across 17 subjects. One of the tasks, the Two Workspace Random Target (TRT), involves monkeys reaching for visually presented targets positioned either close to the body or further away, providing a diverse range of neural and behavioral data. The experiment aims to foster the development of precise and efficient neural data analysis techniques applicable in a variety of experimental contexts.

In the TRT task, neural activity and behavioral measures such as hand and cursor position, velocity, and applied force were recorded while monkeys reached for sequential targets in distinct workspaces. The dataset includes spike counts per neural unit, capturing the electrophysiological responses during task performance. Events like trial starts and target onsets were also logged, aiding in the correlation of neural activities with specific behavioral events. By integrating comprehensive data from multiple subjects performing varied tasks, NeuroTask serves as a robust platform for exploring neural dynamics in relation to complex motor behaviors.

## Data Available in NWB Files

The NeuroTask dataset comprises various types of data stored in Neurodata Without Borders (NWB) files. Specifically, the TRT task files contain information on:

- Behavioral data: Hand and cursor positions (x and y coordinates), hand velocity (x and y components), measured in cm and mm, respectively.
- Event timestamps: Indications of trial starts, target onsets, go cues, and trial ends.
- Neural data: Spike counts per unit, indicating the neural firing rates of recorded neurons during the task.
- Indices for filtering: Indices to filter data based on session, subject, and trial specifics.
- Metadata: Session descriptions, session start times, and experiment details.

## Keywords

- Neural data analysis
- Multi-session
- Multi-task
- Multi-subject
- Motor cortical regions
- Rhesus monkey
- Behavioral data
- Neural spikes
- Reaching task
- Event indications