#!/usr/bin/env python

import nose
import unittest
import random
import sys

from Algorithms.Heaps.Python.binary_heap import BinaryHeap

SEED = 4694115875039644586


class TestBinaryHeap(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global SEED
        if SEED == -1:
            SEED = random.randint(0, sys.maxint)
            cls.rand = random.Random(SEED)
        else:
            cls.rand = random.Random(SEED)
        print "SEED: " + str(SEED)

    def test_insert_maintains_len(self):
        bin_heap = BinaryHeap()
        self.assertEqual(len(bin_heap), 0)
        bin_heap.insert(1)
        self.assertEqual(len(bin_heap), 1)

    def test_pop_1_element(self):
        bin_heap = BinaryHeap()
        bin_heap.insert(2)
        node = bin_heap.pop()

        self.assertEqual(node.data, 2)
        self.assertEqual(node.key, 2)

    def test_pop_500_random_elements(self):
        bin_heap = BinaryHeap()
        item_list = []
        for i in xrange(500):
            key = self.rand.randint(0, 50000)
            val = self.rand.randint(0, 50000)
            # Make sure the key is unique to make testing easier
            while (key in [k for k, data in item_list]):
                key = self.rand.randint(0, 50000)
                val = self.rand.randint(0, 50000)
            bin_heap.insert(key, val)
            item_list.append((key, val))

        item_list.sort(key=lambda tup: tup[0])
        item_list = reversed(item_list)
        for i,item in enumerate(item_list):
            bin_node = bin_heap.pop()
            self.assertEqual(bin_node.key, item[0])
            self.assertEqual(bin_node.data, item[1])

    def test_pop_50_random_elements_len(self):
        bin_heap = BinaryHeap()
        for i in xrange(50):
            self.assertEqual(i, len(bin_heap))
            key = self.rand.randint(0, 50000)
            val = self.rand.randint(0, 50000)
            bin_heap.insert(key, val)

        heap_len = len(bin_heap)
        for bin_node in bin_heap:
            heap_len -= 1
            print heap_len, len(bin_heap)
            self.assertEqual(len(bin_heap), heap_len)

    def test_to_string(self):
        bin_heap = BinaryHeap()
        bin_heap.insert(2)
        bin_heap.insert(1)
        actual = str(bin_heap)
        expected = "[\nNode: 2, \nNode: 1]"

        self.assertEqual(actual, expected)


if __name__ == "__main__":
    nose.main()
