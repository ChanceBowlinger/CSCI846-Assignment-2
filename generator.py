import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# ==========================================
# 1. EXPERIMENTAL DATA
# ==========================================
TTL = [1, 2, 3, 5, 10, 15, 25]
TTL_HIT_RATES = [0.4226, 0.4939, 0.5739, 0.6723, 0.8189, 0.8846, 0.9200]
TTL_PINGS_GENERATED = [13440, 18041, 22063, 26038, 33237, 39928, 51451]
MIN_NEIGHBORS = [1, 2, 3, 5, 10, 15, 20, 25]
MIN_NEIGHBORS_HIT_RATES = [0.1128, 0.3119, 0.5126, 0.6867, 0.8847, 0.9332, 0.9484, 0.9718]
MIN_NEIGHBORS_PINGS_GENERATED = [8602, 18165, 20226, 25342, 33012, 36175, 36981, 39158]
KNOWN_WORDS_RATIO = [0.01, 0.02, 0.03, 0.05, 0.1, 0.15, 0.2, 0.25]
KNOWN_WORDS_HIT_RATES = [0.2000, 0.3622, 0.4650, 0.6939, 0.8722, 0.9681, 0.9797, 0.9850]



# ==========================================
# 2. PLOTTING FUNCTION
# ==========================================
class ExperimentPlotter:
    def __init__(self, data_dict):
        """
        Initializes the plotter with experimental data.
        :param data_dict: Dictionary containing lists for all experimental metrics.
        """
        self.data = data_dict

    def _setup_plot(self, title, xlabel, ylabel):
        """Internal helper to apply consistent styling."""
        plt.figure(figsize=(8, 5))
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid(True, linestyle='--', alpha=0.6)

    def plot_ttl_vs_hit_rate(self):
        self._setup_plot('TTL vs Hit Rate', 'TTL', 'Hit Rate')
        plt.plot(self.data['ttl'], self.data['ttl_hit'], marker='o', color='b', label='Hit Rate')
        plt.show()

    def plot_ttl_vs_pings(self):
        self._setup_plot('TTL vs Message Broadcasted', 'TTL', 'Messages Broadcasted')
        plt.plot(self.data['ttl'], self.data['ttl_pings'], marker='s', color='r', label='Pings')
        plt.show()

    def plot_min_neighbors_vs_hit_rate(self):
        self._setup_plot('Min-Neighbors vs Hit Rate', 'Min-Neighbors', 'Hit Rate')
        plt.plot(self.data['min_neighbors'], self.data['min_neighbors_hit'], marker='^', color='g')
        plt.show()

    def plot_min_neighbors_vs_pings(self):
        self._setup_plot('Min-Neighbors vs Message Broadcasted', 'Min-Neighbors', 'Message Broadcasted')
        plt.plot(self.data['min_neighbors'], self.data['min_neighbors_pings'], marker='v', color='orange')
        plt.show()

    def plot_word_ratio_vs_hit_rate(self):
        self._setup_plot('Known-Word-Ratio vs Hit Rate', 'Known-Word-Ratio', 'Hit Rate')
        plt.plot(self.data['word_ratio'], self.data['word_hit'], marker='x', color='purple')
        plt.show()

# ==========================================
# 3. EXECUTION
# ==========================================
if __name__ == "__main__":
    experiment_results = {
        'ttl': TTL,
        'ttl_hit': TTL_HIT_RATES,
        'ttl_pings': TTL_PINGS_GENERATED,
        'min_neighbors': MIN_NEIGHBORS,
        'min_neighbors_hit': MIN_NEIGHBORS_HIT_RATES,
        'min_neighbors_pings': MIN_NEIGHBORS_PINGS_GENERATED,
        'word_ratio': KNOWN_WORDS_RATIO,
        'word_hit': KNOWN_WORDS_HIT_RATES
    }

    # Instantiate the class
    plotter = ExperimentPlotter(experiment_results)

    # Call specific plotting functions
    plotter.plot_ttl_vs_hit_rate()
    plotter.plot_ttl_vs_pings()
    plotter.plot_min_neighbors_vs_hit_rate()
    plotter.plot_min_neighbors_vs_pings()
    plotter.plot_word_ratio_vs_hit_rate()