#!/usr/bin/env python

# TODO can we use the node class in graphs?
class Node:

    def __init__(self, val):
        self.value = val
        self.children = []

    def __repr__(self):
        return self._to_string()

    def _degree(self):
        if len(self.children) == 0:
            return 0

        values = []
        for child in self.children:
            if child == self:
                #TODO add an error here
                print "Recursive tree!"
                exit()
            values.append(child._degree())

        return max(values) + 1

    def _to_string(self, prefix=""):
        if "\n" not in prefix:
            prefix = "\n" + prefix

        string = prefix + "Node: " + str(self.value)
        for c in self.children:
            if c == self:
                print "Recursive loop"
                return ""
            string += c._to_string(prefix + "--->")

        return string

if __name__ == "__main__":
    #TODO do I want to use Node for trees or make a Tree class?
    tree_root = Node(1)
    n2 = Node(2)
    tree_root.children.append(n2)
    n3 = Node(3)
    tree_root.children.append(n3)

    n4 = Node(4)
    n3.children.append(n4)
    n5 = Node(5)
    n3.children.append(n5)

    n6 = Node(6)
    n2.children.append(n6)
    n7 = Node(7)
    n2.children.append(n7)

    print tree_root

    print ""
    print "Degree of 1:", tree_root._degree()
    print "Degree of 2:", n2._degree()
    print "Degree of 3:", n3._degree()
    print "Degree of 6:", n6._degree()
