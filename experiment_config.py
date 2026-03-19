def get_experiment_config():
    config = {
        "message_ttl": 5,
        "num_nodes": 100,
        "num_actions_per_turn": 5,
        "num_turns": 100,
        "min_neighbors": 3,
        "known_words_per_node": 5
    }
    return config

def get_known_words():
    # return known list of 100 words for bag of words representation
    return [f"word_{i}" for i in range(100)]
