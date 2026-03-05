from node import Node

class CentralHubs:
    def __init__(self, network):
        self.network = network

    def set_known_nodes(self, nodes):
        self.known_nodes = nodes

    def get_neighbors(self, node_id, current_neighbors: list[Node]) -> list:
        """Returns list of neighbor node IDs for a given node ID, excluding current neighbors."""
        neighbors = current_neighbors.copy()

        while len(neighbors) < self.network.min_neighbors:
            new_neighbor = self.known_nodes[(node_id + len(neighbors) + 1) % self.num_nodes]
            if new_neighbor not in neighbors and new_neighbor.id != node_id:

                # Make sure node is active before adding as neighbor
                if new_neighbor.active: # node id will equal index in known nodes list
                    neighbors.append(new_neighbor)

        return neighbors
