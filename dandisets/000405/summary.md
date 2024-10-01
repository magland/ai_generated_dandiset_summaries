### Abstract

This dataset comprises electrophysiological recordings and behavioral metadata collected from experiments investigating the encoding of task-relevant information by parahippocampal neurons in rats during goal-directed navigation. The experiments aimed to elucidate how neurons in the parahippocampal region contribute to spatial cognition and decision-making processes. Rats were subjected to different navigation tasks, including open-field foraging sessions and Tree-Maze sessions, allowing for a comprehensive analysis of neuronal activity in response to varying environmental contexts and behavioral demands.

The sessions captured in this dataset include neural recordings, tracking data of the animals' movements, and event timing information essential for behavioral correlation studies. By providing detailed unit matching across sessions and a nuanced behavioral performance table, this dataset supports rigorous analyses necessary for understanding the neural mechanisms underlying goal-directed navigation. The collected data are instrumental in generating the figures presented in the Gonzalez & Giocomo (2022) manuscript, which advances our comprehension of cognitive maps and spatially modulated neuron activity.

### Data Description

The dataset is organized into 100 Neurodata Without Borders (NWB) files, split into two main groups based on the type of recorded data. 

- **Type 1 Files:** These files include:
  - **Firing Rates (TimeSeries):** No explicit description is provided.
  - **Track Data (TimeSeries):** Columns capture x, y coordinates, heading direction (hd), speed (sp), and head angle (ha).
  - **Unit Table (DynamicTable):** Contains columns for unit IDs, cluster names (cl_name), unit type, and UUIDs.
  - Metadata elements such as experimenter details, session identifiers, and subject information.

- **Type 2 Files:** These files include:
  - **Event Table (DynamicTable):** Includes event durations (dur), event types, and timings (t0 and tE), with 1024 entries.
  - **Trial Table (DynamicTable):** Covers various attributes including trial correctness, cues used, decision outcomes, and goal coordinates, spanning 61 trials.
  - **Firing Rates (TimeSeries)**
  - **Track Data (TimeSeries):** Columns for x, y coordinates, and heading direction (hd).
  - **Unit Table (DynamicTable):** Contains columns for unit IDs, cluster names (cl_name), unit type, and UUIDs.
  - Metadata elements detailing experimenter identities, session descriptions, and subject information.

### Keywords

- Parahippocampal Neurons
- Goal-Directed Navigation
- Electrophysiological Recordings
- Behavioral Metadata
- Spatial Cognition
- Neural Encoding
- Rats
- Open-Field Foraging
- Tree-Maze Sessions
- Neurodata Without Borders (NWB)