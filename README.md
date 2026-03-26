# Peer-to-Peer Network Simulator

The aim of this project is to simulate a peer-to-peer network in varying configurations.

## Components

1. **Network** - A sandbox environment for the simulations
2. **Central Hub** - A central server that maintains the network by providing neighbors for the nodes.
3. **Node** - A computation unit representing a user in a network.

## Quick Setup

Clone the repository

```
git clone https://github.com/ChanceBowlinger/CSCI846-Assignment-2.git
```

Chage the directory using the command: `cd CSCI846-Assignment-2`

`experiment_config.py` contains basic configuration for the simulation

- Total Number of Words: 100
- Number of Nodes in the network: 100
- Number of Turns in the simulation: 100
- Actions taken by each node per turn: 5
- Message TTL: 5
- Minimum Number of Neighbors per Node: 5

**To simulate the network with different configuration, instead of changing the base configuration uncomment the lines 10-12 based on the selected prameter.**

Run main.py to start simulation using the command: `python3 main.py`

## Visualization

To visualize the metrics of the simullations, popullate the experimental data with the metrics captured in each simulation

- TTL
- TTL_HIT_RATES,
- TTL_PINGS_GENERATED
- MIN_NEIGHBORS
- MIN_NEIGHBORS_HIT_RATES
- MIN_NEIGHBORS_PINGS_GENERATED
- KNOWN_WORDS_RATIO
- KNOWN_WORDS_HIT_RATES

And then run generator script using the commad: `python3 generator.py`
