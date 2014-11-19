#!/usr/bin/env python

class TreeNode(object):

    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def __repr__(self):
        return self._to_string()

    def add_child(self, child):
        # TODO check to see if child already has parent?
        self.children.append(child)
        child.parent = self

    def cut(self, child):
        """
        Cuts child from the nodes children
        """
        for i, c in enumerate(self.children):
            if c == child:
                del self.children[i]
                child.parent = None
                return child

        return None

    def degree(self):
        if len(self.children) == 0:
            return 0

        values = []
        for child in self.children:
            if child == self:
                #TODO add an error here
                print "Recursive tree!"
                exit()
            values.append(child.degree())

        return max(values) + 1

    def _to_string(self, prefix=""):
        if "\n" not in prefix:
            prefix = "\n" + prefix

        string = prefix + "Node: " + str(self.data)
        for c in self.children:
            if c == self:
                return "Recursive loop"
            string += c._to_string(prefix + "--->")

        return string
