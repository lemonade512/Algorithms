#!/usr/bin/env python

import nose
import unittest
import random
import sys

from Algorithms.Sorting.Python.sorting_algs import mergesort, heapsort, quicksort, rand_quicksort

import Algorithms.Sorting.Python.sorting_algs as sorting

SEED = 4694115875039644586


class TestSortingAlgorithms(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global SEED
        if SEED == -1:
            SEED = random.randint(0, sys.maxint)
            cls.rand = random.Random(SEED)
        else:
            cls.rand = random.Random(SEED)
        print "SEED: " + str(SEED)

    def test_mergesort_100_random_ints(self):
        l = [self.rand.randint(0, 50000) for i in range(100)]
        expected = sorted(l)
        mergesort(l, 0, len(l)-1)
        actual = l

        self.assertEqual(actual, expected)

    def test_heapsort_100_random_ints(self):
        l = [self.rand.randint(0, 50000) for i in range(100)]
        expected = sorted(l)
        actual = heapsort(l)

        self.assertEqual(actual, expected)

    def test_quicksort_100_random_ints(self):
        l = [self.rand.randint(0, 50000) for i in range(100)]
        expected = sorted(l)
        quicksort(l, 0, len(l)-1)
        actual = l

        self.assertEqual(actual, expected)

    def test_quicksort_randomize_partition_100_random_ints(self):
        l = [self.rand.randint(0, 50000) for i in range(100)]
        expected = sorted(l)
        rand_quicksort(l, 0, len(l)-1)
        actual = l

        self.assertEqual(actual, expected)


if __name__ == "__main__":
    nose.main()
