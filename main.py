from experiment_config import get_experiment_config, get_known_words
from network import Network
from central_hubs import CentralHubs
from node import Message, Node
import random

def main():
    # Read in config variables
    config = get_experiment_config()
    # config["message_ttl"] = 25
    # config["min_neighbors"] = 25
    # config["known_words_per_node"] = 25
    known_words = get_known_words()

    network = Network(
        max_ttl=config["message_ttl"], 
        max_actions_per_turn=config["num_actions_per_turn"], 
        min_neighbors=config["min_neighbors"]
    )

    # Set central hubs
    central_hubs = CentralHubs(network)
    network.set_central_hubs(central_hubs)

    # Initialize nodes
    nodes:list[Node] = []
    for i in range(config["num_nodes"]):

        # Give each node random words in known_words
        random_words = random.sample(known_words, config["known_words_per_node"])

        node = Node(id=i, central_hubs=central_hubs, bag_of_words=random_words)
        nodes.append(node)
    central_hubs.set_known_nodes(nodes)

    # Instantiate all nodes with neighbors from central hubs
    for node in nodes:
        node.get_new_neighbors()

    # Run simulation for specified number of turns
    for turn in range(config["num_turns"]):
        print(f"Turn {turn + 1}")
        for node in nodes:
            node.take_turn()
    
    print(f"Total messages sent: {Message.TOTAL_MESSAGES}")
    print(f"Total messages found: {Node.MESSEGE_FOUND_COUNT}")
    print(f"Total pings generated: {Node.PINGS_GENERATED}")
    print(f"Hit rate: {Node.MESSEGE_FOUND_COUNT / Message.TOTAL_MESSAGES * 100:.2f}%")

if __name__ == "__main__":
    main()