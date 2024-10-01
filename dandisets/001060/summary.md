### Abstract
The NeuroTask dataset has been curated to support the advancement of methodologies for analyzing multi-session, multi-task, and multi-subject neural data. This benchmark dataset collects data from motor cortical regions over 17 subjects performing seven distinct tasks. The experiment primarily focuses on recording neural activities and corresponding behavioral responses to evaluate and enhance computational techniques in neural analysis.

Specifically, one representative dataset involves a Rhesus monkey engaged in an isometric wrist task. The monkey operates a cursor by exerting forces on a padded box, with measurements captured by a 6 DOF load cell. Flexion and extension forces move the cursor horizontally, while radial and ulnar forces move it vertically. The data encompass spike counts, hand and cursor positions, velocities, forces, and event markers, providing a comprehensive view of the motor control mechanisms.

### Data Description
The available NWB files include detailed neural and behavioral recordings. Key metrics captured are spike counts per unit, with recordings processed to detect and sort spikes into single units. Behavioral data cover hand and cursor positions, velocities, and forces. Event markers denote critical points such as go cues and target onsets, while indices facilitate filtering by session, animal, and trial IDs.

Files provide time-series data for various metrics:
- Cursor acceleration (x and y)
- Cursor position (x and y)
- Cursor velocity (x and y)
- Force exertion (x and y)
- Target direction
- Event indicators for go cues, target onsets, and trial results.

Additionally, indices include filtering identifiers such as animal, dataset ID, session, and trial ID.

### Keywords
- NeuroTask
- Multi-Subject Neural Data
- Motor Cortical Regions
- Isometric Wrist Task
- Cursor Control
- Spike Counts
- Behavioral Measurements
- Neural Analysis
- Rhesus Monkey
- Data Benchmark