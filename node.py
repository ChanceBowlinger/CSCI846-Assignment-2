class Node:
    def __init__(self, id, centralHubs, bagOfWords):
        self.id = id
        self.centralHubs = centralHubs
        self.bagOfWords = bagOfWords
        self.active = True
        self.neighbors = []

        self.get_new_neighbors()

    def get_new_neighbors(self):
        self.neighbors = self.centralHubs.get_neighbors(self.id, self.neighbors)

