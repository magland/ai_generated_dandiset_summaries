## Experiment Summary

This dataset was collected from a human participant with an intracortical brain-computer interface (iBCI) as part of an early feasibility study conducted under an Investigational Device Exemption from the FDA. The primary aim of the study was to evaluate the safety and efficacy of the iBCI for long-term neural recording and stimulation. Neural activity was captured using two 96-channel intracortical electrode arrays implanted in the "hand knob" area of the brain. During each trial, audiovisual cues guided the participant to attempt specific reach and grasp movements involving seven degrees of freedom: 3D translation (x, y, z), 1D orientation (roll), and 3D grasp (flexion/extension of thumb, index, ring, and pinky fingers, as well as thumb abduction).

The dataset serves as part of the FALCON benchmark challenge and is made available in three formats: "held-in-calib" for decoder calibration, "held-in-minival" for submission format validation, and "held-out-calib" for few-shot recalibration. The data includes 7D kinematics, trial numbers, an evaluation mask for FALCON models, and multi-unit spiking activity. Researchers utilizing this dataset must adhere strictly to the Data Use Agreement, which prohibits attempts to identify subjects or redistribute the data.

## Available Data in NWB Files

The NWB files associated with this dataset contain various forms of data critical to the assessment of the iBCI. The `acquisition` group includes:

- **OpenLoopKinematics**: The positions and orientations (tx, ty, tz, rx) and grasp angles (g1, g2, g3) recorded during the trials.
- **OpenLoopKinematicsVelocity**: The velocities corresponding to the kinematic data.
- **TrialNum**: The specific trial number indicating the sequence of trials.
- **eval_mask**: Timesteps that should be ignored for training and evaluation purposes.

Additional metadata includes `experimental epochs`, a description of the experiment, and identifiers for the session and subject. The `units` group contains multi-unit spike data, such as spike times and spike time indices for each neural unit recorded during the session.

## Keywords

- Brain-Computer Interface (BCI)
- Intracortical Electrode Array
- Neural Recording
- Motor Control
- Human Participant
- 7 Degrees of Freedom (7DoF)
- Kinematics
- FALCON Benchmark
- Electrophysiology
- Spike Sorting

