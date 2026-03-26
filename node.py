import random


class Message:
    TOTAL_MESSAGES = 0
    def __init__(self, id, sender_id, query, ttl):
        self.id = id
        self.is_active = True
        self.sender_id = sender_id
        self.query = query
        self.ttl = ttl
        Message.TOTAL_MESSAGES += 1


class Node:
    MESSEGE_FOUND_COUNT = 0
    PINGS_GENERATED = 0
    def __init__(self, id, central_hubs, bag_of_words):
        self.id = id
        self.central_hubs = central_hubs
        self.MAX_ACTIONS_PER_TURN = self.central_hubs.network.max_actions_per_turn
        self.bag_of_words = bag_of_words
        self.active = True
        self.neighbors = []
        # Message: {
        #   "sender": sender_id,
        #   "query": keyword,
        #   "ttl": ttl}
        self.message_queue = []
        self.action_this_turn = 0

    def get_new_neighbors(self):
        self.neighbors = self.central_hubs.get_new_neighbors(self.id, self.neighbors)

    def handle_ping(self, message):
        if message.is_active == False:
            return
        
        Node.PINGS_GENERATED += 1
        if message.query in self.bag_of_words:
            print(f"Node {self.id} found the keyword {message.query} in message {message.id} from sender {message.sender_id}")
            message.is_active = False
            Node.MESSEGE_FOUND_COUNT += 1
        elif message.ttl > 0:
            message.ttl -= 1
            self.message_queue.append(message)

    def ping(self, message):
        new_neighbors = []
        for neighbor in self.neighbors:
            if neighbor.active:
                new_neighbors.append(neighbor) # if neighbor inactive remove him from list  
        self.neighbors = new_neighbors

        for neighbor in self.neighbors:
            neighbor.handle_ping(message)


    def pong(self):
        return
    
    def take_turn(self):
        self.action_this_turn = 0
        active_probab = random.random() # this generates 0.0 to 1.0

        if self.active == False:
            if active_probab < 0.3:
                self.active = True
                self.get_new_neighbors() # get new neighbors when node becomes active again
                self.action_this_turn += 1
        else:
            if active_probab < 0.1:
                self.active = False
                self.message_queue.clear() # clear message queue here
                self.neighbors.clear() # clear neighbors here
                return
            elif active_probab < 0.3:
                
                while (query := f"word_{random.randint(1,100)}") in self.bag_of_words:
                    pass

                new_message = Message(
                    id=self.central_hubs.mesage_id_counter + 1, 
                    sender_id=self.id, 
                    query=query, 
                    ttl=self.central_hubs.network.max_ttl
                )
                self.central_hubs.mesage_id_counter += 1
                self.ping(new_message)
                self.action_this_turn += 1 

        
        
        while self.action_this_turn < self.MAX_ACTIONS_PER_TURN:
            self.action_this_turn += 1
            if len(self.message_queue) == 0:
                break
            message = self.message_queue.pop()
            message.sender_id = self.id # Changes sender id

            self.ping(message)
