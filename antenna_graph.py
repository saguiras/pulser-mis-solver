import networkx as nx
import matplotlib.pyplot as plt

class AntennaGraph:
    def __init__(self, num_antennas, color_palette=None):
        """
        Initialize the AntennaGraph instance.

        Parameters:
        - num_antennas (int): Number of antennas in the graph.
        - color_palette (list, optional): List of colors for graph visualization.
        """
        self.adjacency_list = {i: [] for i in range(1, num_antennas + 1)}
        self.antenna_colors = {}
        self.color_palette = color_palette or ['skyblue', 'lightcoral', 'palegreen', 'lightgoldenrodyellow',
                                               'lightsteelblue', 'lightpink', 'lightcyan', 'plum', 'palegreen',
                                               'thistle', 'lightseagreen', 'burlywood', 'wheat', 'lightgray']

    def add_connection(self, antenna1, antenna2):
        """
        Add a connection between two antennas.

        Parameters:
        - antenna1 (int): Antenna identifier.
        - antenna2 (int): Antenna identifier.
        """
        self.adjacency_list[antenna1].append(antenna2)
        self.adjacency_list[antenna2].append(antenna1)

    def add_connections(self, connections):
        """
        Add connections to the graph.

        Parameters:
        - connections (list): List of antenna connections represented as tuples.
        """
        for antenna1, antenna2 in connections:
            if antenna1 not in self.adjacency_list or antenna2 not in self.adjacency_list:
                raise ValueError("Antenna not found in the adjacency list.")
            self.add_connection(antenna1, antenna2)

    def assign_colors(self, color_patterns):
        """
        Assign colors to antennas based on frequency patterns.

        Parameters:
        - color_patterns (list): List of color patterns representing antenna frequencies.
        """
        for idx, color_pattern in enumerate(color_patterns):
            for i, color_bit in enumerate(color_pattern):
                if color_bit == '1':
                    self.antenna_colors[i + 1] = self.color_palette[idx]

    def print_graph(self):
        """
        Visualize the graph.
        """
        G = self.create_networkx_graph()
        node_colors = [self.antenna_colors.get(antenna, 'lightgray') for antenna in G.nodes()]
        self.draw_graph(G, node_colors)

    def create_networkx_graph(self):
        """
        Create a NetworkX graph from the adjacency list.

        Returns:
        - nx.Graph: NetworkX graph representing the antenna connections.
        """
        G = nx.Graph()
        for antenna, neighbors in self.adjacency_list.items():
            G.add_node(antenna)
            for neighbor in neighbors:
                G.add_edge(antenna, neighbor)
        return G

    def draw_graph(self, G, node_colors):
        """
        Draw the NetworkX graph.

        Parameters:
        - G (nx.Graph): NetworkX graph.
        - node_colors (list): List of colors for nodes.
        """
        pos = nx.spring_layout(G)  # Use a spring layout for better visualization
        nx.draw(G, with_labels=True, node_size=2000, node_color=node_colors, font_size=20, width=2, edge_color="gray")
        plt.show()