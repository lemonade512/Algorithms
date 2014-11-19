#!/usr/bin/env python


class GraphNode(object):

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
        if isinstance(other, GraphNode):
            return self.key == other.key
        else:
            return NotImplemented

    def add_connection(self, neighbor, weight):
        self.connections[neighbor] = weight

