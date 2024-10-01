## Abstract
We present an electrophysiological dataset obtained from nine epilepsy patients during a verbal working memory task. These individuals were undergoing intracranial monitoring for the localization of epileptic seizures. Using a modified Sternberg task, the experiment temporally separated the stages of encoding memory items, maintenance, and recall. The dataset includes scalp EEG recordings using the 10-20 system, intracranial EEG (iEEG) from depth electrodes, waveforms, and spike times from 1526 neurons in the medial temporal lobe. Additionally, the dataset provides detailed metadata such as MNI coordinates and anatomical labels of all intracranial electrodes, alongside subject characteristics and session-specific information (e.g., set size, match/mismatch status, response accuracy, and response time for each trial).

The primary purpose of this study was to investigate the neural mechanisms underlying verbal working memory by leveraging simultaneous scalp EEG, iEEG recordings, and unit recordings from the human medial temporal lobe. This comprehensive dataset enables advanced connectivity analyses and could provide insights into the neural dynamics of working memory in the context of epilepsy. It also includes sessions with different set sizes, presented randomly, with a unique rule that a trial with an incorrect response is always followed by a trial with a set size of four.

## Data Description
The dataset comprises 45 NWB files, divided into two main categories. Each file includes:

1. **Type 1 NWB Files**:
   - Scalp EEG data and electrode positions.
   - Intracranial EEG (iEEG) data and electrode positions.
   - Detailed metadata for electrodes including location, seizure onset zone (SOZ), and referencing scheme.
   - Spike times and waveforms for multiple neuronal units.
   - LFP data from iEEG electrodes.
   - Behavioral data for all trials, including responses and related time intervals.
   - Metadata pertaining to the EEG and iEEG recording systems used (ATLAS Neurophysiology System and NicoletOne EEG System).
   - Experimental epochs and trials data, including start and stop times, set sizes, probe letters, and responses.
   
2. **Type 2 NWB Files**:
   - Similar to Type 1 but may represent different session data or individual trials.
   - Acquisition of both EEG and iEEG data alongside detailed metadata on electrodes.
   - Behavioral data and LFP data, much like Type 1.
   - Experiment description, task details, and relevant publication references.
   
### Keywords
- Neuroscience
- Electrophysiology
- Human
- Awake
- Local field potential
- Neuronal action potential
- Spikes
- Medial temporal lobe
- Cognitive task
- Verbal working memory