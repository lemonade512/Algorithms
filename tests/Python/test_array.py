#!/usr/bin/env python

import nose
import unittest

from Algorithms.Arrays.Python.custom_array import Array


class TestCustomArray(unittest.TestCase):

    def test_len_after_insert(self):
        a = Array()
        self.assertEqual(0, len(a))
        a.insert(0, 0)
        self.assertEqual(1, len(a))

        for i in xrange(5):
            a.insert(i, i)

        self.assertEqual(6, len(a))

    def test_str(self):
        a = Array()
        a.insert(0, 0)
        a.insert(0, 1)
        a.insert(0, 2)
        actual = str(a)

        expected = "[2, 1, 0]"
        self.assertEqual(actual, expected)

    def test_insert_then_index_of(self):
        a = Array(['hello', 'goodbye', 'lorem ipsum'])
        actual = a.index_of('goodbye')
        expected = 1
        self.assertEqual(actual, expected)

    def test_remove(self):
        a = Array()
        a.insert(0, 0)
        a.insert(1, 1)
        a.insert(2, 2)
        a.remove(1)
        self.assertEqual(-1, a.index_of(1))

    def test_minimum_with_strings(self):
        a = Array()
        a.insert(0, "string1")
        a.insert(1, "string2")
        a.insert(0, "z-string")
        actual = a.minimum
        expected = "string1"
        self.assertEqual(actual, expected)

    def test_maximum_with_ints(self):
        a = Array()
        a.insert(0, 1)
        a.insert(0, 10)
        a.insert(1, 25)
        a.insert(0, 12)
        self.assertEqual(a.maximum, 25)

    def test_average(self):
        a = Array()
        for i in xrange(5):
            a.insert(i, i)

        self.assertEqual(a.average, 2)

    def test_sample_variance(self):
        a = Array([1,4,5,23,6,6,3,2,43])
        self.assertAlmostEqual(a.sample_variance, 171.55555555555)

    def test_standard_deviation(self):
        a = Array([1,4,5,23,6,6,3,2,43])
        self.assertAlmostEqual(a.std_deviation, 13.0979218029)


if __name__ == "__main__":
    nose.main()
