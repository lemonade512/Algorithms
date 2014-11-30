#!/usr/bin/env python

#TODO Should this really be a value error?
class RecursiveTreeError(ValueError):
    pass

class TreeNode(object):

    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def __repr__(self):
        return self._to_string()

    def add_child(self, child):
        """ Adds a child to the node's children.

        Args:
            child: The child to add to the nodes children.
        """
        if child is self:
            raise RecursiveTreeError("A tree node cannot be a child of itself.")

        self.children.append(child)
        child.parent = self

    def cut(self, child):
        #TODO test this cuts proper child
        """
        Cuts child from the nodes children
        """
        for i, c in enumerate(self.children):
            if c is child:
                del self.children[i]
                child.parent = None
                return child

        return None

    def degree(self):
        if len(self.children) == 0:
            return 0

        values = []
        for child in self.children:
            if child is self:
                raise RecursiveTreeError("A tree node cannot be a child of itself.")
            values.append(child.degree())

        return max(values) + 1

    def _to_string(self, prefix=""):
        if "\n" not in prefix:
            prefix = "\n" + prefix

        string = prefix + "Node: " + str(self.data)
        for c in self.children:
            if c is self:
                return "Recursive loop"
            string += c._to_string(prefix + "--->")

        return string

class HeapNode(TreeNode):
    #TODO make this a HeapNode and use it in binary heap
    def __init__(self, key, data=None):
        if data is None:
            data = key

        super(HeapNode, self).__init__(data)
        self.key = key
        self.marked = False

    def __cmp__(self, other):
        if isinstance(other, HeapNode):
            if self.key < other.key:
                return -1
            elif self.key == other.key:
                return 0
            else:
                return 1
        else:
            return NotImplemented

    def mark(self):
        self.marked = True

    def valid_heap(self):
        if len(self.children) == 0:
            return True

        for child in self.children:
            if child.key < self.key:
                return False

            if not child.valid_heap():
                return False

        return True

    def _to_string(self, prefix=""):
        if "\n" not in prefix:
            prefix = "\n" + prefix

        string = prefix + "Node: " + str(self.key)
        for c in self.children:
            if c is self:
                return "Recursive loop"
            string += c._to_string(prefix + "--->")

        return string
