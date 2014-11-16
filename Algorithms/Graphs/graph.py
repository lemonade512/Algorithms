#!/usr/bin/env python

"""
This file holds two classes: Node and Graph. A Graph is made
of Nodes that are connected to each other. Another possible
implementation of this data structure would be to have an Edge
class that might be able to store extra data. You could also
change Graph to use an adjacency matrix instead of each Node
keeping track of its neighbors.
"""

class Node(object):
    """
    Each node keeps track of its neighbors in a dictionary with
    the keys being the neighbor nodes and the values being the
    weight of that connection.
    """

    def __init__(self, value):
        self.value = value
        self.connections = dict()

    def __str__(self):
        return str(self.value) + " connected to: " +\
                str([x.value for x in self.connections])
    __repr__ = __str__

    def add_connection(self, neighbor, weight):
        self.connections[neighbor] = weight

#TODO could be improved by having a DirectedGraph object?
class Graph(object):

    def __init__(self):
        self.nodes = dict()

    #TODO how to handle duplicates? should I return a list of
    # nodes with the correct value?
    def __getitem__(self, val):
        """
        Allows access like a dictionary
        """
        for node in self.nodes:
            if node.value == val:
                return node

        #TODO should this raise a key error?
        return None

    def __contains__(self, n):
        return n in self.nodes

    def add_node(self, node):
        self.nodes[node] = {}
        return node

    def add_edge(self, f, t, cost=0):
        if f not in self.nodes:
            self.add_node(f)
        if t not in self.nodes:
            self.add_node(t)
        self.nodes[f][t] = cost

        # If f has an add_connection method use it. Otherwise, ignore it.
        # This allows us to more easily store data in custom objects while
        # still allowing any type of hashable python object
        try:
            f.add_connection(t, 0)
        except:
            pass

    def is_connected(self):
        #TODO a breadth first search will only work for undirected graphs
        #TODO make test for strongly connected digraph, weakly connected digraph
        #     and of course an undirected graph. This method should work for
        #     undirected graphs and strongly connected graphs.
        #TODO doesn't properly find strongly connected graph if happens to start
        #     at the top of a tree (i.e. false positive)
        # Get the first node in the dictionary
        start = self.nodes.keys()[0]

        visited = []
        for n in self.bfs(start):
            visited.append(n)

        return len(visited) == len(self.nodes)

    def is_weakly_connected(self):
        #TODO analyze efficiency of this algorithm
        new_graph = Graph()

        # Create a new, undirected graph from self
        #TODO test this to make sure it works
        for node in self.nodes:
            for n in self.nodes[node]:
                new_graph.add_edge(n, node)
                new_graph.add_edge(node, n)

        return new_graph.is_connected()


    def bfs(self, start):
        """
        Returns a generator that goes through the graph
        in a breadth-first order.
        """

        if start not in self:
            # This is a bad value
            raise ValueError("Could not find node: " + str(start))

        visited = []
        queue = [start]
        while queue:
            current_node = queue.pop(0)
            visited.append(current_node)
            yield current_node
            for n in self.nodes[current_node]:
                if n not in visited:
                    queue.append(n)

    def dfs(self, start):
        """
        Returns a generator that goes through the graph
        in a breadth-first order.
        """

        if start not in self:
            raise ValueError("Could not find node: " + str(start))

        visited = []
        queue = [start]
        while queue:
            current_node = queue.pop()
            visited.append(current_node)
            yield current_node
            for n in self.nodes[current_node]:
                if n not in visited:
                    queue.append(n)
