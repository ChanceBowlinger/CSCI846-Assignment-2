import random

class Node:
    MAX_ACTIONS_PER_TURN = 10 # TODO: Change this
    def __init__(self, id, centralHubs, bagOfWords):
        self.id = id
        self.centralHubs = centralHubs
        self.bagOfWords = bagOfWords
        self.active = True
        self.neighbors = []
        self.action_this_turn = 0

        self.get_new_neighbors()

    def get_new_neighbors(self):
        self.neighbors = self.centralHubs.get_neighbors(self.id, self.neighbors)

    
    def takeTurn():
        active_probab = random.random()
