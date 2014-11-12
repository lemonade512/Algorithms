#!/usr/bin/python

from node import Node
import math

class FibonacciHeap(object):
    """
    NOTE: this implements a minimum heap where the minimum
          always at the top.
    """

    def __init__(self):
        self.min_idx = None
        self.n = 0 # This is how many nodes we have
        # TODO Should really store tree objects in this list instead of nodes
        self.trees = []

    def __str__(self):
        return str(self.trees)

    def insert(self, val):
        self.trees.append(Node(val))
        if self.min_idx == None:
            self.min_idx = len(self.trees) - 1
        elif val < self.trees[self.min_idx].value:
            self.min_idx = len(self.trees) - 1

        # Update node count
        self.n += 1

    def pop(self):
        """
        Also called delete minimum or extract minimum
        """
        assert(self._heap_property())
        # Get minimum value, remove root, use root's children as new roots
        output = self.trees[self.min_idx].value
        for child in self.trees[self.min_idx].children:
            self.trees.append(child)

        del self.trees[self.min_idx]

        self._consolidate()

        # Update the min index
        min_idx = 0
        for i, _ in enumerate(self.trees):
            if self.trees[i].value < self.trees[min_idx].value:
                min_idx = i
        self.min_idx = min_idx

        assert(self._heap_property())
        return output

    def _consolidate(self):
        # Link roots with the same degree until every root has different degree
        #TODO fix this so you only need log(n) space
        max_degree=int(math.ceil(math.log(self.n, 2)))
        degree_array = [[] for i in range(max_degree)] # Initialize a big enough array
        for root in self.trees:
            degree = self._degree(root)
            degree_array[degree].append(root)

        #TODO this is duplicated below
        if len(degree_array) > 0:
            m = max([len(x) for x in degree_array])
        else:
            m = 0

        while m > 1:
            for tree_list in degree_array:
                if len(tree_list) > 1:
                    t1 = tree_list[0]
                    t2 = tree_list[1]

                    min_t = None
                    if t1.value > t2.value:
                        min_t = t2
                        t2.children.append(t1)
                    else:
                        min_t = t1
                        t1.children.append(t2)

                    del tree_list[0]
                    del tree_list[0]

                    degree = self._degree(min_t)
                    degree_array[degree].append(min_t)

            if len(degree_array) > 0:
                m = max([len(x) for x in degree_array])
            else:
                m = 0

        self.trees = []
        for t in degree_array:
            if len(t) > 0:
                self.trees.append(t[0])

    def _heap_property(self):
        #TODO I don't know if this function works. Even if it does
        #     it has shitty time complexity
        for t in self.trees:
            n = t
            # WARNING: Do not remove the list() this copies the n.children instead
            #          of creating a new reference
            queue = list(n.children)
            while queue:
                for child in n.children:
                    queue.append(child)
                    if child.value < n.value:
                        return False
                n = queue.pop()
        return True
