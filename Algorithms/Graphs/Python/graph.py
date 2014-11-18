#!/usr/bin/env python

#TODO combine this with the node.py in Heaps?

class Node(object):
    """
    Each node keeps track of its neighbors in a dictionary with
    the keys being the neighbor nodes and the values being the
    weight of that connection.
    """

    def __init__(self, key, data=None):
        self.key = key
        if data is None:
            self.data = key
        else:
            self.data = data
        self.connections = dict()

    def __str__(self):
        return str(self.key) + " connected to: " +\
                str([x.key for x in self.connections])
    __repr__ = __str__

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.key == other.key
        else:
            return NotImplemented

    def add_connection(self, neighbor, weight):
        self.connections[neighbor] = weight

#TODO should I just have everything expect a key? I could make it so that
#     the user can get a node by refering to it's key but otherwise nothing
#     will take a node as input.
#TODO could be improved by having a DirectedGraph object?
class Graph(object):

    def __init__(self):
        self.nodes = dict()

    def __getitem__(self, item):
        """ Allows access like a dictionary """
        for node in self.nodes:
            if node.key == key:
                return node

        #TODO should this raise a key error?
        return None

    def __contains__(self, key):
        """ Checks to see if the graph contains a node with key.

        Args:
            key: The key to check for in the graph.

        Returns:
            True if the key is in the graph.
        """
        for node in self.nodes:
            if node.key == n:
                return True
        return False

    def add_node(self, key, val=None):
        """ Adds a node to the graph with a key and val.

        Args:
            key: The key to refer to the added node. This should be a
                 unique, hashable value. If you need duplicate data use
                 the val keyword. If val is not input then the data of
                 the node will be the same as the key.

            val: The data of the newly added node. If this is left blank
                 then the data of the newly created node will be the same
                 as the key.

        Raises:
            ValueError if a node with key is already in the graph.
        """
        new_node = Node(key, data=val)

        if new_node not in self.nodes:
            self.nodes[new_node] = {}
        else:
            raise ValueError("Duplicate key '{0}' found.".format(key))

    def add_edge(self, f_key, t_key, f_val=None, t_val=None, cost=0):
        """
        """
        if f_key not in self:
            self.add_node(f_key, data=f_val)
        if t_key not in self:
            self.add_node(t_key, data=t_val)
        self.nodes[n1][n2] = cost
        from_node.add_connection(t, 0)

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

        if start not in self:
            # This is bad data
            raise ValueError("Could not find node: " + str(start))

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

        if start not in self:
            raise ValueError("Could not find node: " + str(start))

        visited = []
        queue = [start]
        while queue:
            current_node = queue.pop()
            visited.append(current_node)
            yield current_node.data
            for n in self.nodes[current_node]:
                if n not in visited:
                    queue.append(n)
