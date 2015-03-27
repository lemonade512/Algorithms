#!/usr/bin/env python

import nose
import unittest

import Algorithms.NumericalAlgorithms.Python.divisors as alg


class TestDivisors(unittest.TestCase):

    def test_divisors_of_one(self):
        divisors = alg.divisors(1)
        self.assertEqual(divisors, [1])

    def test_divisors_of_small_num(self):
        divisors = alg.divisors(28)
        self.assertEqual(divisors, [1,2,4,7,14,28])

    def test_divisors_of_large_num(self):
        divisors = alg.divisors(4532532)
        self.assertEqual(divisors, [1, 2, 3, 4, 6, 12, 377711, 755422, 1133133,
                                    1510844, 2266266, 4532532])

if __name__ == "__main__":
    nose.main()
