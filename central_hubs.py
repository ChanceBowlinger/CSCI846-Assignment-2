import random
from node import Node

class CentralHubs:
    def __init__(self, network):
        self.network = network
        self.mesage_id_counter = 0

    def set_known_nodes(self, nodes):
        self.known_nodes = nodes

    def get_new_neighbors(self, node_id, current_neighbors: list[Node]) -> list:
        """Returns list of neighbor node IDs for a given node ID, excluding current neighbors."""
        neighbors = current_neighbors.copy()

        while len(neighbors) < self.network.min_neighbors:
            new_neighbor = self.known_nodes[random.randint(0, len(self.known_nodes) - 1)]
            if new_neighbor not in neighbors and new_neighbor.id != node_id:

                # Make sure node is active before adding as neighbor
                if new_neighbor.active: # node id will equal index in known nodes list
                    neighbors.append(new_neighbor)

                    # Add the caller node as a neighbor to the new neighbor as well
                    # Real world network would handle thisas a ping-pong message, but we handle here for simplicity
                    new_neighbor.neighbors.append(self.known_nodes[node_id])

        return neighbors
