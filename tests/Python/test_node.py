#!/usr/bin/env python
import unittest

from Algorithms.Heaps.Python.node import Node

class TestNode(unittest.TestCase):

    def test_to_string(self):
        node = Node(1)
        self.assertEqual(node._to_string(), "\nNode: 1")

    def test_recursive_to_string(self):
        node = Node(1)
        node.add_child(node)
        self.assertEqual(node._to_string(), "Recursive loop")
