#!/usr/bin/python

from node import Node
import math

#TODO make this generic so you can specify whether you want a max or a min heap?
# NOTE Nodes should never be marked if they are root?

class FibonacciHeapNode(Node):
    def __init__(self, key, data):
        super(FibonacciHeapNode, self).__init__(data)
        self.key = key
        self.marked = False

    def mark(self):
        self.marked = True

    def _to_string(self, prefix=""):
        if "\n" not in prefix:
            prefix = "\n" + prefix

        string = prefix + "Node: " + str(self.key)
        for c in self.children:
            if c == self:
                print "Recursive loop"
                return ""
            string += c._to_string(prefix + "--->")

        return string

class FibonacciHeap(object):
    """
    NOTE: this implements a minimum heap where the minimum
          always at the top.
    """

    def __init__(self):
        """ Initializes an empty heap. """
        self.min_idx = None
        self.count = 0 # This is how many nodes we have
        self.trees = []

    def __str__(self):
        return str(self.trees)

    def __len__(self):
        """ Returns how many nodes are in the heap. """
        return self.count

    def insert(self, key, val):
        """ Creates a new node and inserts it into the heap.

        Args:
            key: A comparable value representing the priority of the
                 new node.
            val: The value of the new node.

        Returns:
            The newly created node.
        """
        new_node = FibonacciHeapNode(key, val)
        self.trees.append(new_node)
        self._update_min_idx()

        # Update node count
        self.count += 1
        return new_node

    def decrease_key(self, node, new_key):
        """ Decreases the key of the specified node.

        Args:
            node (FibonacciHeapNode): The node to decrease the key of.

            new_key: The new key of the node. This must be less than the current
                     key of the node and comparable to other keys used in the heap.
        """
        assert(self._heap_property())

        # Decrease the key
        if node.key < new_key:
            return

        node.key = new_key
        parent = node.parent
        # Check if the heap property is invalidated
        if parent is not None and new_key <= parent.key:
            # Cut node and make it a root
            parent.cut(node)
            node.marked = False
            self.trees.append(node)

            self._cascading_cut(parent)

        # Make sure to update min_idx if need be
        if new_key < self.trees[self.min_idx].key:
            self.min_idx = len(self.trees) - 1

        assert(self._heap_property())

    def delete(self, node):
        """ Deletes the node from the heap.

        Args:
            node (FibonacciHeapNode): What node to delete.

        Returns:
            The deleted node.
        """
        self.decrease_key(node, float("-inf"))
        return self.pop()

    def merge(self, other):
        """ Merges two heaps.

        Args:
            other (FibonacciHeap): Heap to merge with self

        Returns:
            The new, merged, heap.
        """
        heap = FibonacciHeap()
        heap.trees = self.trees + other.trees
        heap.count = self.count + other.count
        return heap

    def peek(self):
        """ Returns the data of the top node in the heap. """
        return self.trees[self.min_idx].data

    def pop(self):
        """ Takes the top node off the heap and consolidates.
        (Also called delete minimum or extract minimum)

        Returns:
            Node with the minimum key
        """
        assert(self._heap_property())
        # Get minimum value, remove root, use root's children as new roots
        output = self.trees[self.min_idx]
        children = self.trees[self.min_idx].children
        while len(children) > 0:
            child = children.pop()
            self.trees[self.min_idx].cut(child)
            self.trees.append(child)

        del self.trees[self.min_idx]

        self._consolidate()
        self._update_min_idx()

        assert(self._heap_property())
        self.count -= 1
        return output

    def _cascading_cut(self, node):
        if node not in self.trees:
            parent = node.parent
            if not node.marked:
                node.mark
            else:
                parent.cut(node)
                node.marked = False
                self.trees.append(node)
                self._cascading_cut(parent)

    def _update_min_idx(self):
        min_idx = 0
        for i, _ in enumerate(self.trees):
            if self.trees[i].key < self.trees[min_idx].key:
                min_idx = i
        self.min_idx = min_idx

    def _consolidate(self):
        # Link roots with the same degree until every root has different degree
        max_degreei = int(math.ceil(math.log(self.count, 2)))
        degree_array = [[] for i in range(max_degree)] # Initialize a big enough array
        for root in self.trees:
            degree = root.degree()
            degree_array[degree].append(root)

        # Do this while m > 1. Breaks when m <= 1
        while True:
            # m is the max number of trees of a certain degree. For instance,
            # if there are 3 trees of degree 2 and 2 trees of degree 1 then
            # m == 3
            if len(degree_array) > 0:
                m = max([len(x) for x in degree_array])
            else:
                m = 0

            if m <= 1:
                break

            for tree_list in degree_array:
                if len(tree_list) > 1:
                    t1 = tree_list[0]
                    t2 = tree_list[1]

                    min_t = None
                    if t1.key > t2.key:
                        min_t = t2
                        t2.add_child(t1)
                    else:
                        min_t = t1
                        t1.add_child(t2)

                    del tree_list[0]
                    del tree_list[0]

                    degree = min_t.degree()
                    degree_array[degree].append(min_t)

        self.trees = []
        for t in degree_array:
            if len(t) > 0:
                self.trees.append(t[0])

    def _heap_property(self):
        """ Checks if the heap is a valid FibonacciHeap.

        This function is used for testing purposes.

        Returns:
            True if the heap is valid and False otherwise
        """
        for t in self.trees:
            if not self._valid_heap(t):
                return False

        # Make sure none of the root nodes are marked
        for n in self.trees:
            if n.marked:
                return False

        return True

    # TODO put this in FibonnaciHeapNode
    def _valid_heap(self, node):
        if len(node.children) == 0:
            return True

        for child in node.children:
            if child.key < node.key:
                return False

            if not self._valid_heap(child):
                return False

        return True
