## Experiment Summary

The SpikeForest ground truth datasets are meticulously curated to benchmark spike sorting algorithms. This compilation includes electrophysiological recordings from Mus musculus (house mouse) and Rattus norvegicus (Norway rat), along with simulated data. One key experiment involves silicon-juxtacellular hybrid probes in awake behaving mice, where both types of electrodes record neuronal activity with high precision. This dual recording setup ensures synchronized and accurate data capture, facilitating the verification of spike times and waveform congruence between the extracellular silicon probe and the juxtacellular electrode.

Another central experiment focuses on hybrid simulations with sinusoidal probe drift modeled using 2D interpolation techniques. These simulations generate realistic background noise and spike train data, aiding in the evaluation of algorithmic performances under controlled conditions. The dataset includes a broad array of setups and recording conditions, ensuring comprehensive validation of sorting algorithms across various scenarios.

## NWB Files Description

The NWB files in this dataset collectively include raw acquisition traces captured by multiple configurations of electrode arrays. Each file encapsulates detailed metadata about the electrodes, including their locations and identifiers. Specific files also detail the devices used, such as Neuronexus silicon probes for in vivo mice recordings and simulated devices for hybrid drift experiments. Alongside raw traces, spike times and corresponding indices for detected units are provided, essential for algorithm benchmarking and validation. Some files also contain detailed processing modules and data on spiking units, offering ground truth spike times for neuron activity detection.

## Keywords

- Electrophysiology
- Ground truth
- Spike sorting
- Silicon probe
- Juxtacellular
- Simulation
- Multielectrode array
- In vivo recording
- Hybrid probes
- Sinusoidal drift