class Node:
    def __init__(self, id, central_hub, bag_of_words):
        self.id = id
        self.central_hub = central_hub
        self.bag_of_words = bag_of_words
        self.active = True
        self.neighbors = []
        self.message_queue = []

        self.get_new_neighbors()

    def get_new_neighbors(self):
        self.neighbors = self.central_hub.get_neighbors(self.id, self.neighbors)

