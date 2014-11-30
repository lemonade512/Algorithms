#!/usr/bin/env python

import nose
import unittest
import random
import sys

from Algorithms.Heaps.Python.fibonacci_heap import FibonacciHeap
from Algorithms.Heaps.Python.node import HeapNode

SEED = 4694115875039644586


class TestHeapNode(unittest.TestCase):

    def test_node_mark(self):
        node = HeapNode(10, 10)
        node.mark()
        self.assertTrue(node.marked)

    def test_invalid_heap(self):
        node = HeapNode(1, 1)
        node2 = HeapNode(3, 3)
        node.add_child(node2)
        node2.add_child(HeapNode(0, 0))
        self.assertFalse(node.valid_heap())

    def test_to_string(self):
        node1 = HeapNode(1, 1)
        self.assertEqual(node1._to_string(), "\nNode: 1")

    def test_to_string_connected(self):
        root = HeapNode(1)
        n2 = HeapNode(2)
        root.add_child(n2)
        string = root._to_string()
        self.assertEqual("\nNode: 1\n--->Node: 2", string)

    def test_to_string_recursive_loop(self):
        node = HeapNode(1)
        node.children = [node]
        actual = node._to_string()
        expected = "Recursive loop"

        self.assertEqual(actual, expected)

    def test_compare_to_none(self):
        node = HeapNode(1)
        self.assertFalse(None == node)


class TestFibonacciHeap(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global SEED
        if SEED == -1:
            SEED = random.randint(0, sys.maxint)
            cls.rand = random.Random(SEED)
        else:
            cls.rand = random.Random(SEED)
        print "SEED: " + str(SEED)

    def test_pop_1_element(self):
        fib_heap = FibonacciHeap()
        result = fib_heap.insert(5, 5)
        self.assertEqual(result.data, 5)
        self.assertEqual(result.key, 5)

    def test_pop_500_random_elements(self):
        fib_heap = FibonacciHeap()
        item_list = []
        for i in xrange(500):
            key = self.rand.randint(0, 50000)
            val = self.rand.randint(0, 50000)
            # Make sure the key is unique to make testing easier
            while (key in [k for k, data in item_list]):
                key = self.rand.randint(0, 50000)
                val = self.rand.randint(0, 50000)
            fib_heap.insert(key, val)
            item_list.append((key, val))

        item_list.sort(key=lambda tup: tup[0])
        for i,item in enumerate(item_list):
            fib_node = fib_heap.pop()
            self.assertEqual(fib_node.key, item[0])
            self.assertEqual(fib_node.data, item[1])

    def test_pop_50_random_elements_len(self):
        fib_heap = FibonacciHeap()
        for i in xrange(50):
            self.assertEqual(i, len(fib_heap))
            key = self.rand.randint(0, 50000)
            val = self.rand.randint(0, 50000)
            fib_heap.insert(key, val)

        heap_len = len(fib_heap)
        for fib_node in fib_heap:
            heap_len -= 1
            self.assertEqual(len(fib_heap), heap_len)

    def test_merge_heap_100_items_pop(self):
        items_list = []

        fib_heap1 = FibonacciHeap()
        for i in xrange(50):
            key = self.rand.randint(0, 50000)
            val = self.rand.randint(0, 50000)
            fib_heap1.insert(key, val)
            items_list.append((key, val))

        fib_heap2 = FibonacciHeap()
        for i in xrange(50):
            key = self.rand.randint(0, 50000)
            val = self.rand.randint(0, 50000)
            fib_heap2.insert(key, val)
            items_list.append((key, val))

        items_list.sort(key=lambda tup: tup[0])
        fib_heap = fib_heap1.merge(fib_heap2)
        for item in items_list:
            fib_node = fib_heap.pop()
            self.assertEqual(fib_node.key, item[0])
            self.assertEqual(fib_node.data, item[1])

    def test_decrease_key_then_pop(self):
        fib_heap = FibonacciHeap()
        for i in xrange(500):
            key = self.rand.randint(5, 50000)
            val = self.rand.randint(0, 50000)
            fib_heap.insert(key, val)

        key = self.rand.randint(5, 50000)
        val = self.rand.randint(0, 50000)
        node = fib_heap.insert(key, val)
        fib_heap.decrease_key(node, 3)
        popped_node = fib_heap.pop()
        self.assertEqual(node, popped_node)

    def test_delete_node_maintain_len(self):
        fib_heap = FibonacciHeap()
        for i in xrange(500):
            key = self.rand.randint(5, 50000)
            val = self.rand.randint(0, 50000)
            fib_heap.insert(key, val)

        key = self.rand.randint(5, 50000)
        val = self.rand.randint(0, 50000)
        node = fib_heap.insert(key, val)
        fib_heap_len = len(fib_heap)
        fib_heap.delete(node)
        self.assertEqual(fib_heap_len, len(fib_heap)+1)

    def test_decrease_key_after_pop(self):
        # Decrease after pop because pop consolidates
        key_list = []

        fib_heap = FibonacciHeap()
        for i in xrange(200):
            key = self.rand.randint(5, 50000)
            val = self.rand.randint(0, 50000)
            # Make sure the key is unique to make testing easier
            while (key in key_list):
                key = self.rand.randint(0, 50000)
                val = self.rand.randint(0, 50000)
            fib_heap.insert(key, val)
            key_list.append(key)

        node = fib_heap.insert(20000, 15)

        for i in xrange(200):
            key = self.rand.randint(5, 50000)
            val = self.rand.randint(0, 50000)
            # Make sure the key is unique to make testing easier
            while (key in key_list):
                key = self.rand.randint(0, 50000)
                val = self.rand.randint(0, 50000)
            fib_heap.insert(key, val)
            key_list.append(key)

        fib_heap.pop()
        fib_heap.decrease_key(node, 0)
        n = fib_heap.pop()
        self.assertEqual(n, node)

    def test_peek(self):
        fib_heap = FibonacciHeap()
        fib_heap.insert(10, 10)
        n = fib_heap.insert(1, 15)
        self.assertEqual(fib_heap.peek(), n)

    def test_fib_heap_str(self):
        fib_heap = FibonacciHeap()
        fib_heap.insert(1)
        fib_heap.insert(2)
        string = str(fib_heap)
        self.assertEqual("[\nNode: 1, \nNode: 2]", string)

    def test_invalid_min_item_returns_false(self):
        fib_heap = FibonacciHeap()
        fib_heap.trees.append(HeapNode(10))
        fib_heap.trees.append(HeapNode(1))
        fib_heap.min_idx = 0
        self.assertFalse(fib_heap._min_item_prop())

    def test_marked_heap_root_is_invalid(self):
        fib_heap = FibonacciHeap()
        node = HeapNode(1)
        node.mark()
        fib_heap.trees.append(node)
        self.assertFalse(fib_heap._heap_property())

    def test_heap_iterates_values(self):
        fib_heap = FibonacciHeap()
        fib_heap.insert(1)
        fib_heap.insert(9)
        fib_heap.insert(3)
        fib_heap.insert(2)
        fib_heap.insert(7)
        fib_heap.insert(25)
        fib_heap.insert(21)
        fib_heap.insert(14)

        expected = [1, 2, 3, 7, 9, 14, 21, 25]
        actual = [e for e in fib_heap]

        self.assertEqual(actual, expected)

    def test_heapify(self):
        l = [1,2,3,4,5]
        heap = FibonacciHeap.heapify(l)

        expected = l
        actual = [n for n in heap]

        self.assertEqual(actual, expected)


if __name__ == "__main__":
    nose.main()
