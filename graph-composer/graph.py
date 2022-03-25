# This is our Markov Chain representation
import random

# Define the graph in terms of vertices

class Vertex:
    def __init__(self, value):
        self.value = value
        self.adjacent = {}  # nodes that have an edge

    def add_edge_to(self, vertex, weight=0):
        # this is adding an edge to the vertex we input with weight
        self.adjacent[vertex] = weight

    def increment_edge(self, vertex):
        # this is incrementing the weight of the edge
        self.adjacent[vertex] = self.adjacent.get(vertex, 0) + 1
