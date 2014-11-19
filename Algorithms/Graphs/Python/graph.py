#!/usr/bin/env python

from Algorithms.Graphs.Python.graph_node import GraphNode
from Algorithms.Heaps.Python.fibonacci_heap import FibonacciHeap

#NOTE cannot have a node connected to itself

class Graph(object):

    def __init__(self, directed=True):
        self.nodes = dict()
        self.directed = directed

    def __getitem__(self, key):
        """ Allows access like a dictionary using the node's key """
        for node in self.nodes:
            if node.key == key:
                return node

        raise KeyError("Could not find node with key '{0}'".format(key))

    def __contains__(self, key):
        """ Checks to see if the graph contains a node with key.

        Args:
            key: The key to check for in the graph.

        Returns:
            True if the key is in the graph.
        """
        for node in self.nodes:
            if node.key == key:
                return True
        return False

    def __len__(self):
        return len(self.nodes)

    def add_node(self, key, data=None):
        """ Adds a node to the graph with a key and data.

        Args:
            key: The key to refer to the added node. This should be a
                 unique, hashable value. If you need duplicate data use
                 the val keyword. If val is not input then the data of
                 the node will be the same as the key.

            data: The data of the newly added node. If this is left blank
                 then the data of the newly created node will be the same
                 as the key.

        Raises:
            ValueError if a node with key is already in the graph.
        """
        if key in self:
            raise KeyError("Duplicate key '{0}' found.".format(key))

        new_node = GraphNode(key, data=data)
        self.nodes[new_node] = {}

    def add_edge(self, f_key, t_key, f_data=None, t_data=None, cost=0):
        """ Adds an edge between the nodes with keys f_key and t_key

        If the graph is directed the new edge will be directed from f_key
        to t_key. If the graph is not directed then the edge is not directed.

        Args:
            f_key: The key of the from node
            t_key: The key of the to node

        KWargs:
            f_val: The data of the node with key 'f_key'. This defaults to whatever
                   the node's key is.
            t_val: The data of the node with key 't_key'. This defaults to whatever
                   the nod'es key is.
            cost: The cost of the the edge connecting the two nodes
        """
        if f_key not in self:
            self.add_node(f_key, data=f_data)
        if t_key not in self:
            self.add_node(t_key, data=t_data)
        f_node, t_node = self[f_key], self[t_key]
        self.nodes[f_node][t_node] = cost
        f_node.add_connection(t_node, cost)

        if not self.directed:
            self.nodes[t_node][f_node] = cost
            t_node.add_connection(f_node, cost)

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
        for n in self.bfs(start.key):
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
        """ Iterates through the graph breadth first using a generator.

        Args:
            start: The key of the node to start the search from.

        Yields:
            Each node's data as you search through the graph.

        Raises:
            ValueError: If start cannot be found a ValueError is raised.
        """
        # Find the node with start as the key
        start = self[start]

        visited = []
        queue = [start]
        while queue:
            current_node = queue.pop(0)
            visited.append(current_node)
            yield current_node.data
            for n in self.nodes[current_node]:
                if n not in visited:
                    queue.append(n)

    def dfs(self, start):
        """ Iterates through the graph depth first using a generator.

        Args:
            start: The key of the node to start the search from.

        Yields:
            Each node's data as you search through the graph.

        Raises:
            ValueError: If start cannot be found a ValueError is raised.
        """
        # Find the node based on the given key
        start = self[start]

        visited = []
        queue = [start]
        while queue:
            current_node = queue.pop()
            visited.append(current_node)
            yield current_node.data
            for n in self.nodes[current_node]:
                if n not in visited:
                    queue.append(n)

    def dijkstra(self, start, finish):
        """ Finds the shortest path from start to finish.

        Args:
            start: The key of the starting node.

            finish: The key of the end node.

        Returns:
            A list of keys making up the shortest path from start to finish and
            the length of the path (path, length). If there are multiple least
            cost paths then this algorithm returns one of them.  (You could modify
            to return a subset of the current graph that contains all the least
            cost paths). If there is no path this function returns None.
        """
        # attr_dict contains any information we need to store about nodes for the
        # algorithm. Example: distance to the node
        attr_dict = {}
        queue = FibonacciHeap()
        for node in self.nodes:
            attr_dict[node] = dict()
            attr_dict[node]['dist'] = float("inf")
            attr_dict[node]['heap_node'] = queue.insert(float("inf"), node)
            attr_dict[node]['visited'] = False
            attr_dict[node]['previous'] = None

        attr_dict[self[start]]['dist'] = 0
        queue.insert(0, self[start])

        while len(queue) > 0:
            node = queue.pop().data
            attr_dict[node]['visited'] = True
            for neighbor in self.nodes[node]:
                if not attr_dict[neighbor]['visited']:
                    alt = attr_dict[node]['dist'] + self.nodes[node][neighbor]
                    if alt < attr_dict[neighbor]['dist']:
                        attr_dict[neighbor]['dist'] = alt
                        queue.decrease_key(attr_dict[neighbor]['heap_node'], alt)
                        attr_dict[neighbor]['previous'] = node

        # NOTE previous contains the shortest path from start to any
        #      node in the graph
        output = []
        end_node = self[finish]
        while attr_dict[end_node]['previous'] is not None:
            output.insert(0, end_node.key)
            end_node = attr_dict[end_node]['previous']
        output.insert(0, start)
        if attr_dict[self[finish]]['dist'] != float('inf'):
            return output, attr_dict[self[finish]]['dist']
        else:
            return None
