import networkx as nx
import matplotlib.pyplot as plt


class AntennaGraph:
    def __init__(self, num_antennas, color_palette=None):
        self.adjacency_list = {i: [] for i in range(1, num_antennas + 1)}
        self.antenna_colors = {}
        self.color_palette = color_palette or ['skyblue', 'lightcoral', 'palegreen', 'lightgoldenrodyellow',
                                               'lightsteelblue', 'lightpink', 'lightcyan', 'plum', 'palegreen',
                                               'thistle', 'lightseagreen', 'burlywood', 'wheat', 'lightgray']

    def add_connection(self, antenna1, antenna2):
        self.adjacency_list[antenna1].append(antenna2)
        self.adjacency_list[antenna2].append(antenna1)

    def add_connections(self, connections):
        for antenna1, antenna2 in connections:
            if antenna1 not in self.adjacency_list or antenna2 not in self.adjacency_list:
                raise ValueError("Antenna not found in the adjacency list.")
            self.add_connection(antenna1, antenna2)

    def assign_colors(self, color_patterns):
        for idx, color_pattern in enumerate(color_patterns):
            for i, color_bit in enumerate(color_pattern):
                if color_bit == '1':
                    self.antenna_colors[i + 1] = self.color_palette[idx]

    def print_graph(self):
        G = self.create_networkx_graph()
        node_colors = [self.antenna_colors.get(antenna, 'lightgray') for antenna in G.nodes()]
        self.draw_graph(G, node_colors)

    def create_networkx_graph(self):
        G = nx.Graph()
        for antenna, neighbors in self.adjacency_list.items():
            G.add_node(antenna)
            for neighbor in neighbors:
                G.add_edge(antenna, neighbor)
        return G

    def draw_graph(self, G, node_colors):
        nx.draw(G, with_labels=True, node_size=2000, node_color=node_colors, font_size=20, width=2, edge_color="gray")
        plt.show()