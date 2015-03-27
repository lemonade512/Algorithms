#!/usr/bin/env python

import sys
sys.path.insert(0, "../..")

import nose
import unittest

import Algorithms.NumericalAlgorithms.Python.divisors as alg

#TODO move this to test_numerical_algorithms.py?
class TestDivisors(unittest.TestCase):

    def test_divisors_of_one(self):
        divisors = alg.divisors(1)
        self.assertEqual(divisors, [1])

    def test_divisors_of_small_num(self):
        divisors = alg.divisors(28)
        self.assertEqual(divisors, [1,2,4,7,14,28])

    def test_divisors_of_twelve(self):
        divisors = alg.divisors(12)
        self.assertEqual(divisors, [1,2,3,4,6,12])

    def test_divisors_of_num_with_sqrt_as_divsor(self):
        divisors = alg.divisors(196)
        self.assertEqual(divisors, [1,2,4,7,14,28,49,98,196])

    def test_divisors_of_large_num(self):
        divisors = alg.divisors(4532532)
        self.assertEqual(divisors, [1, 2, 3, 4, 6, 12, 377711, 755422, 1133133,
                                    1510844, 2266266, 4532532])

if __name__ == "__main__":
    nose.main()
