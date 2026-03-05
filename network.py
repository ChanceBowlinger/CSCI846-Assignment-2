class Network:
    def __init__(self, max_ttl, max_actions_per_turn, min_neighbors):
        self.max_ttl = max_ttl
        self.max_actions_per_turn = max_actions_per_turn
        self.min_neighbors = min_neighbors
        self.central_hubs = None

    def set_central_hubs(self, central_hubs):
        self.central_hubs = central_hubs


    