### Neural Organoid Ephys Trace

This study aimed to investigate neural activity in the primary motor cortex (M1) and premotor cortex (PMd) of a Rhesus monkey engaged in a brain-machine interface (BMI) task. Single-unit recordings were obtained from chronically implanted microwire electrode arrays, facilitating BMI control through a Kalman filter decoder. The primary focus was to capture BMI-unit spike counts, task parameters, and cursor data, offering insights into neural encoding and control dynamics within the BMI framework. The collected data include various behavioral and task-related parameters, enabling a comprehensive analysis of the monkey's interaction with the BMI system.

The data were gathered using a MaxWell BioSystems CMOS-based high-density microelectrode array and reflect a sophisticated integration of neural recording technology with BMI control algorithms. The experimental sessions involved the monkey operating a 2D cursor, navigated through neural signals decoded in real-time. The Kalman filter decoder played a crucial role in translating neural activity into cursor movements. The investigation contributes to understanding the neural mechanisms underlying motor control and the potential of BMI systems in neuroprosthetic applications.

#### Available Data in NWB Files

The NWB files contain detailed information on the experimental setup and collected data:
- Time intervals for experimental trials, including start and stop times
- Detailed behavioral data 
  - 2D cursor position (x, y)
  - Decoder state (2D position, 2D velocity, offset)
  - Obstacle details and positions
  - Binned spike counts for BMI control
  - Target state (2D position, 2D velocity, offset)
  - Task entry numbers for trials
  - Cursor and target radius data
- Kalman filter decoder matrices (A, C, Q, W, steady-state F and K)
- Plant type information related to the BMI3D code
- Reward times (how long the juicer was open to deliver rewards)
- Binary variables indicating bins during BMI updates

#### Keywords

1. Brain-Machine Interface (BMI)
2. Kalman Filter
3. Electrophysiology
4. Motor Cortex
5. Premotor Cortex
6. Microwire Arrays
7. Spike Counts
8. Cursor Control
9. Neural Decoding
10. Rhesus Monkey