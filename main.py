from experiment_config import get_experiment_config
from network import Network
from central_hubs import CentralHubs
from node import Node

def main():
    # Read in config variables
    config = get_experiment_config()

    network = Network(
        max_ttl=config["message_ttl"], 
        max_actions_per_turn=config["num_actions_per_turn"], 
        min_neighbors=config["min_neighbors"]
    )

    # Set central hubs
    central_hubs = CentralHubs(network)
    network.set_central_hubs(central_hubs)

    # Initialize nodes
    nodes = []
    for i in range(config["num_nodes"]):
        # TODO - add random bag of words
        node = Node(id=i, centralHubs=central_hubs, bagOfWords=[])
        nodes.append(node)
    central_hubs.set_known_nodes(nodes)

    # Run simulation for specified number of turns
    for turn in range(config["num_turns"]):
        print(f"Turn {turn + 1}")
        # TODO - implement message sending and node actions
        for node in nodes:
            pass # TODO - implement node actions
    

if __name__ == "__main__":
    main()