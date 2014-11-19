#!/usr/bin/env python

import nose
import unittest

from Algorithms.Graphs.Python.graph import Graph
from Algorithms.Graphs.Python.graph_node import GraphNode


class TestGraph(unittest.TestCase):

    def test_node_equals_none(self):
        g = GraphNode(1)
        self.assertFalse(g == None)

    def test_node_to_string(self):
        g = GraphNode(1)
        self.assertEqual(str(g), "1 connected to: []")

    def test_get_single_item(self):
        g = Graph()
        g.add_node(1, data="hello")
        node = g[1]
        self.assertEqual(node.data, "hello")
        self.assertEqual(node.key, 1)

        g = Graph()
        g.add_node("hello", data=1)
        node = g["hello"]
        self.assertEqual(node.key, "hello")
        self.assertEqual(node.data, 1)

    def test_get_item_raises_key_error(self):
        g = Graph()
        g.add_node(1, data="hello")
        self.assertRaises(KeyError, g.__getitem__, "hello")

    def test_graph_contains_single_item(self):
        g = Graph()
        g.add_node(1)
        self.assertTrue(1 in g)
        self.assertFalse("hello" in g)

    def test_graph_contains_single_item_with_data(self):
        g = Graph()
        g.add_node(1, data="hello")
        self.assertTrue(1 in g)
        self.assertFalse("hello" in g)

    def test_graph_add_node_length_increased(self):
        g = Graph()
        self.assertEqual(len(g), 0)
        g.add_node(1)
        self.assertEqual(len(g), 1)

    def test_graph_add_node_raise_key_error(self):
        g = Graph()
        g.add_node(1)
        self.assertRaises(KeyError, g.add_node, 1)

    def test_bfs_touches_all_connected_items(self):
        g = Graph()
        g.add_edge(1, 2)
        g.add_edge(2, 1)
        g.add_edge(2, 3)
        g.add_edge(3, 2)
        g.add_edge(3, 4)
        g.add_edge(4, 3)
        g.add_edge(1, 7)
        g.add_edge(7, 1)

        g_list = [1, 2, 3, 4, 7]
        bfs_list = []
        for n in g.bfs(3):
            bfs_list.append(n)

        bfs_list.sort()
        self.assertEqual(bfs_list, g_list)

    def test_bfs_returns_data_of_items(self):
        pass

    def test_dfs_touches_all_connected_items(self):
        g = Graph()
        g.add_edge(1, 2)
        g.add_edge(2, 1)
        g.add_edge(2, 3)
        g.add_edge(3, 2)
        g.add_edge(3, 4)
        g.add_edge(4, 3)
        g.add_edge(1, 7)
        g.add_edge(7, 1)

        g_list = [1, 2, 3, 4, 7]
        dfs_list = []
        for n in g.dfs(3):
            dfs_list.append(n)

        dfs_list.sort()
        self.assertEqual(dfs_list, g_list)

    def test_dfs_returns_data_of_items(self):
        pass

    def test_dijkstra(self):
        #NOTE graph taken from https://www.youtube.com/watch?v=UG7VmPWkJmA
        g = Graph(directed=False)
        g.add_edge("a", "b", cost=3)
        g.add_edge("a", "e", cost=5)
        g.add_edge("a", "h", cost=4)
        g.add_edge("b", "e", cost=5)
        g.add_edge("b", "f", cost=7)
        g.add_edge("b", "c", cost=2)
        g.add_edge("c", "f", cost=2)
        g.add_edge("c", "g", cost=6)
        g.add_edge("c", "d", cost=3)
        g.add_edge("d", "g", cost=7)
        g.add_edge("d", "z", cost=2)
        g.add_edge("e", "h", cost=7)
        g.add_edge("e", "f", cost=4)
        g.add_edge("f", "h", cost=5)
        g.add_edge("f", "i", cost=4)
        g.add_edge("f", "j", cost=3)
        g.add_edge("f", "g", cost=4)
        g.add_edge("g", "j", cost=4)
        g.add_edge("g", "z", cost=6)
        g.add_edge("h", "i", cost=2)
        g.add_edge("i", "j", cost=6)
        g.add_edge("j", "z", cost=5)
        # Comes up as [a, b, c, d, z]
        output = g.dijkstra("a", "z")
        expected_output = (["a", "b", "c", "d", "z"], 10)
        print output
        self.assertEqual(output, expected_output)
