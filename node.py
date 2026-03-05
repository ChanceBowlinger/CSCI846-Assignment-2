class Node:
    def __init__(self, id, central_hubs, bag_of_words):

        self.id = id
        self.central_hubs = central_hubs
        self.bag_of_words = bag_of_words
        self.active = True
        self.neighbors = []

        self.get_new_neighbors()

    def get_new_neighbors(self):
        self.neighbors = self.central_hubs.get_neighbors(self.id, self.neighbors)

