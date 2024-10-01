# Experiment Summary

The purpose of this dataset is to serve as a test example for using the DANDI archive, akin to a "hello world" program. The dataset focuses on neural data recordings from a single subject, a house mouse (Mus musculus), using an electrophysiological approach. Specifically, the experiment utilizes multi-electrode extracellular electrophysiology recording techniques to capture electrical activities, facilitated by surgical procedures for electrode implantation.

The experiment was conducted by Dr. Bilbo Baggins at the Bag End Laboratory of the University of Middle Earth at the Shire. The session identifier for the recording is "LONELYMTN," and the data collection process started on February 14, 2023. The primary objective appears to demonstrate the setup and recording capabilities of a new experimental rig, capturing the data in NWB format.

# Data Description

The dataset comprises a single NWB file containing the electrical recordings and associated metadata. The key components include:

- **/acquisition/ElectricalSeries**: Captures the electrical activity recorded during the session.
- **/general/devices/array**: Describes the device used, labeled as "the best array."
- **/general/extracellular_ephys/electrodes**: Metadata about the extracellular electrodes, including their group references, names, IDs, labels, and locations within the brain.
- **/general/extracellular_ephys/shank0 to shank4**: Details multiple electrode groups for the shanks with their associated devices.
- **/general/subject**: Contains the subject's information.
- **identifier**: A unique identifier for the subject, "EXAMPLE_ID."
- **session_description**: A brief description indicating this is a synthetic recording.
- **session_start_time**: The start time of the session.
- **timestamps_reference_time**: The reference time for all timestamps in the file.

# Keywords

- Electrophysiology
- Extracellular Recording
- Multi-Electrode Array
- Neural Data
- House Mouse (Mus musculus)
- Brain Electrode Mapping
- NWB (Neurodata Without Borders)
- Test Dataset
- Synthetic Recording
- Data Archival

