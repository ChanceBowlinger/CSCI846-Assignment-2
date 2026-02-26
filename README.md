846 Project 2:

Node:
Contains some words of common dictionary
Queue that intakes messages; can only process some (variable)
May have min/max number of neighbors (variable)
Probabilities to query, leave on every tick
Probability to join?
Reference to central hub

Per node metrics:
Messages per node
Messages in queue per node
Number of neighbors per node

Network:
Contains some number of nodes
Each message has specified TTL (variable)
Known host/hub

Each turn possibilities:
Respond to messages
Send messages
Go inactive
Leave (do not send/respond)
If not in network, join
