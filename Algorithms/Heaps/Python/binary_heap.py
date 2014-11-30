#!/usr/bin/env python

# NOTE currently implements a MAX heap

from math import floor

from Algorithms.Heaps.Python.node import HeapNode

class BinaryHeap(object):

    def __init__(self):
        self._len = 0
        self.nodes = []

    def __str__(self):
        return str(self.nodes)

    def __len__(self):
        return self._len

    def __iter__(self):
        """ Iterates through all nodes by popping them. """
        while len(self.nodes) > 0:
            node = self.pop()
            yield node.data

    def insert(self, key, data=None):
        """ Inserts a node into the heap.

        Args:
            key: The key of the node to insert. This determines in what
                 order the nodes will be popped.

            data: The value of the node to insert into the heap. If left
                  blank the data will be equal to the key.
        """
        new_node = HeapNode(key, data)
        idx = len(self.nodes)
        self.nodes.append(new_node)

        parent = self._parent_idx(idx)
        while parent is not None and self.nodes[parent] < self.nodes[idx]:
            self.nodes[parent], self.nodes[idx] = self.nodes[idx], self.nodes[parent]
            idx = parent
            parent = self._parent_idx(idx)
        self._len += 1

    def pop(self):
        """ Pops the minimum node off the heap.

        Returns:
            The minimum node in the heap.
        """
        output = self.nodes[0]
        smallest = self.nodes.pop()
        self._len -= 1
        if len(self.nodes) == 0:
            return output

        self.nodes[0] = smallest

        idx = 0
        left, right = self._child_indices(idx)
        if right is None:
            right = left
        if left is None:
            return output

        while self.nodes[idx] < self.nodes[left] or self.nodes[idx] < self.nodes[right]:
            if self.nodes[left] > self.nodes[right]:
                max_idx = left
            else:
                max_idx = right

            self.nodes[max_idx], self.nodes[idx] = self.nodes[idx], self.nodes[max_idx]
            idx = max_idx
            left, right = self._child_indices(idx)

            #TODO is there a better way to do this?
            if right is None:
                right = left
            if left is None:
                break

        return output

    def _parent_idx(self, idx):
        if idx < 0:
            raise IndexError(str(idx) + " is an invalid index.")

        if idx == 0:
            return None
        else:
            return (idx-1)//2

    def _child_indices(self, idx):
        if idx < 0:
            raise IndexError(str(idx) + " is an invalid index.")

        if len(self.nodes) > 2*idx + 1:
            child1 = 2*idx + 1
        else:
            child1 = None

        if len(self.nodes) > 2*idx + 2:
            child2 = 2*idx + 2
        else:
            child2 = None

        return (child1, child2)
