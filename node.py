import random

class Node:
    MAX_ACTIONS_PER_TURN = 10 # TODO: Change this
    def __init__(self, id, central_hub, bag_of_words):
        self.id = id
        self.central_hub = central_hub
        self.bag_of_words = bag_of_words
        self.active = True
        self.neighbors = []
        self.message_queue = []
        self.action_this_turn = 0

        self.get_new_neighbors()

    def get_new_neighbors(self):
        self.neighbors = self.central_hub.get_neighbors(self.id, self.neighbors)

    
    def takeTurn(self):
        active_probab = random.random() # this generates 0.0 to 1.0

        if self.active == False:
            if active_probab < 0.3:
                self.active = True
        else:
            if active_probab < 0.3:
                self.active = False
                # TODO: clear message queue here
                return
        
        while self.action_this_turn < self.MAX_ACTIONS_PER_TURN:
            message = self.message_queue.pop()
            message[0]