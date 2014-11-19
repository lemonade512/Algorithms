#!/usr/bin/env python
import unittest

from Algorithms.Heaps.Python.node import TreeNode, RecursiveTreeError

class TestNode(unittest.TestCase):

    def test_to_string(self):
        node = TreeNode(1)
        self.assertEqual(node._to_string(), "\nNode: 1")

    def test_recursive_degree(self):
        n = TreeNode(1)
        n.children = [n]
        self.assertRaises(RecursiveTreeError, n.degree)

    def test_add_node_to_children_raises_error(self):
        n = TreeNode(1)
        self.assertRaises(RecursiveTreeError, n.add_child, n)

    def test_recursive_node_to_string(self):
        # NOTE a recursive node should never actually happen if the
        #      client uses the add_child function
        n = TreeNode(1)
        n.children = [n]
        self.assertEqual("Recursive loop", n._to_string())

    def test_node_with_children_to_string(self):
        n = TreeNode(1)
        n2 = TreeNode(2)
        n.add_child(n2)
        self.assertEqual("\nNode: 1\n--->Node: 2", str(n))
