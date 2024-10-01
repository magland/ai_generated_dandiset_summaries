## Experimental Summary

This study investigates the invariant neural dynamics underlying brain-machine interface (BMI) control in Rhesus monkeys (Macaca mulatta). Specifically, the research explores how chronically implanted microwire electrode arrays in the primary motor cortex (M1) and dorsal premotor cortex (PMd) facilitate BMI-based control of a 2D cursor. The study employs a Kalman filter decoder to translate neural spike counts into cursor movements, providing insights into the neural mechanisms enabling consistent control across varying tasks. The dataset encapsulates detailed behavioral and neural recordings, offering a comprehensive understanding of BMI control processes.

The recordings include spike count data from the implant arrays, along with corresponding behavioral data such as 2D cursor kinematics, target locations, and trial specifics. By analyzing the invariant properties of neural activity during BMI control, the research aims to contribute to the development of more effective neural prosthetics. The data were collected by a collaborative team of researchers, with detailed methodologies and analytical code available for further exploration and replication.

## NWB File Data Description

Thirteen NWB files contain comprehensive recordings from the BMI experiments. Key datasets in these files include binned spike counts from single-unit recordings and behavioral metrics such as cursor position, target state, and trial conditions. Specifically, the data are structured as follows:

- **Subject**: Identifier for the subject monkey.
- **Trials**: Start and stop times for 287 experimental trials.
- **Behavior**:
  - **Cursor Position**: 2D coordinates (x, y) of the cursor.
  - **Decoder State**: Includes 2D position and velocity, and offset.
  - **Obstacle Details and Position**: Shape, size, and center position of obstacles.
  - **Spike Counts**: Binned spike counts used for BMI control.
  - **Target State**: 2D position and velocity of the target.
  - **Task Entry Number**: Corresponding task ID for each trial.
  - **BMI Update Indicators**: Binary variable indicating when the BMI was updated (at 10 Hz).
  
The data provide a rich framework for analyzing the dynamics of BMI control and the neural activity driving these processes.

## Keywords

- Brain-machine interface (BMI)
- Kalman filter
- Chronic electrophysiology
- Motor cortex (M1)
- Premotor cortex (PMd)
- Microwire arrays
- 2D cursor kinematics
- Neural dynamics
- Rhesus monkey (Macaca mulatta)
- Neural prosthetics
