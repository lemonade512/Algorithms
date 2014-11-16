#!/usr/bin/env python

from math import floor

class BinaryHeap(object):

    def __init__(self):
        self.nodes = []

    def __str__(self):
        return str(self.nodes)

    def insert(self, val):
        assert(self._heap_property())
        print "\nInserting:", val
        idx = len(self.nodes)
        self.nodes.append(val)
        print self

        parent = self._parent_idx(idx)
        while parent != None and self.nodes[parent] < self.nodes[idx]:
            print "Switching:", self.nodes[parent], self.nodes[idx]
            self.nodes[parent], self.nodes[idx] = self.nodes[idx], self.nodes[parent]
            print self
            idx = parent
            parent = self._parent_idx(idx)
        assert(self._heap_property())

    def pop(self):
        # TODO test this by making a large random list, heapifying it, popping everything off,
        #      and making sure the sorted random list and popped list are the same
        assert(self._heap_property())
        output = self.nodes[0]
        smallest = self.nodes.pop()
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

        assert(self._heap_property())
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

    def _heap_property(self):
        """
        Returns true if the all child elements are less than their parents.
        This is the max heap property as opposed to the min heap property
        """
        for i, node in enumerate(self.nodes):
            c1_idx, c2_idx = self._child_indices(i)
            if c1_idx is not None and c1_idx < len(self.nodes) and self.nodes[c1_idx] >= node:
                return False
            if c2_idx is not None and c2_idx < len(self.nodes) and self.nodes[c2_idx] >= node:
                print self.nodes
                return False

        return True
