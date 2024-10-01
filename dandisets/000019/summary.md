## Experiment Summary

This dataset comprises high-density 256-channel electrocorticography (ECoG) recordings from patients undergoing treatment for epilepsy. Subjects were instructed to read aloud a series of consonant-vowel syllables from a predefined list. The primary aim of the experiment, conducted by Dr. Edward Chang and Dr. Kristofer Bouchard at the University of California, San Francisco, appears to be the investigation of neural activity associated with speech production and the transitions between consonants and vowels. The methodology involved recording electrical activity from the brain's surface while the subjects pronounced various syllable combinations, offering insights into the neural mechanisms underlying speech processing.

The collected data includes continuous voltage traces from each of the 256 channels in NWB 2.0 format. Although microphone recordings were made simultaneously, they have been removed to comply with HIPAA regulations. Detailed annotations provided indicate the specific syllable spoken as well as the timing for the start, consonant-vowel transition, and end of each syllable. These annotations also include rest periods when the subject was silent, which serve as baseline measures. Anatomical labels mark the locations of electrodes on the cortical surface, facilitating region-specific analysis.

## NWB File Data Description

Each NWB file encompasses several critical data components:
1. **Electrical Series:** Continuous voltage data captured by the 256 electrodes during each recording session.
2. **Electrode Metadata:** Information about each electrode, including its impedance, anatomical location, and any noise contamination.
3. **Experimental Epochs:** Time intervals defining the start and stop moments for each recording session.
4. **Invalid Times:** Time intervals identified as artifacts or noise, which should be excluded from analysis.
5. **Trial Information:** Detailed hand-marked annotations for each trial including the syllable spoken, the timing of consonant-vowel transitions, and whether the subject was speaking or listening during each trial.

## Keywords
- Electrocorticography (ECoG)
- Speech Production
- Consonant-Vowel Syllables
- Neural Activity
- Epilepsy Treatment
- Brain Electrophysiology
- High-Density Electrode Arrays
- Clinical Neuroscience
- Speech Processing
- Neurodata Without Borders (NWB)