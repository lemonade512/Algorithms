#!/usr/bin/env python

import sys
sys.path.insert(0, "../..")

import nose
import unittest
import random

from Algorithms.NumericalAlgorithms.Python.fast_exponentiation import exponentiate
from Algorithms.NumericalAlgorithms.Python.gcd import gcd
from Algorithms.NumericalAlgorithms.Python.numerical_integration import rectangle_rule, trapezoid_rule, adaptive_trapezoid_rule, my_func
from Algorithms.NumericalAlgorithms.Python.primes import is_prime, find_prime, find_primes, find_factors_fast, find_factors_slow
from Algorithms.NumericalAlgorithms.Python.division import long_division


class TestExponentiate(unittest.TestCase):

    def test_0_power(self):
        self.assertEqual(exponentiate(5, 0), 1)

    def test_1_base(self):
        self.assertEqual(exponentiate(1, 10), 1)
        self.assertEqual(exponentiate(1, 1000), 1)

    def test_0_base(self):
        self.assertEqual(exponentiate(0, 4), 0)

    def test_0_base_0_power(self):
        self.assertEqual(exponentiate(0, 0), 1)

    def test_large_numbers(self):
        self.assertEqual(exponentiate(12, 30), 237376313799769806328950291431424)


class TestGCD(unittest.TestCase):

    def test_gcd_0_and_0(self):
        self.assertEqual(gcd(0, 0), 0)

    def test_gcd_25_and_30(self):
        self.assertEqual(gcd(25, 30), 5)

    def test_gcd_4851_and_3003(self):
        self.assertEqual(gcd(4851, 3003), 231)


class TestIntegration(unittest.TestCase):
    """ NOTE: For all of the following test functions, the variable 'expected' is
    used to hold the true value of the computation. Most of these were obtained
    using wolfram alpha and are kept here to analyze accuracy.

    The 'expected_actual' variable holds the value we expect the algorithm to come
    up with.
    """

    def test_rectangle_rule_zero_length(self):
        actual = rectangle_rule(my_func, 0, 0, 10)
        self.assertEqual(actual, 0)

    def test_rectangle_rule_10_intervals(self):
        expected = 18.41953576453822622612943

        expected_actual = 17.2276047411
        actual = rectangle_rule(my_func, 0, 5, 10)
        self.assertAlmostEqual(actual, expected_actual)

    def test_rectangle_rule_50_intervals(self):
        expected = 18.41953576453822622612943

        expected_actual = 18.1936696555
        actual = rectangle_rule(my_func, 0, 5, 50)
        self.assertAlmostEqual(actual, expected_actual)

    def test_trapezoid_rule_10_intervals(self):
        expected = 18.41953576453822622612943

        expected_actual = 18.3415994633
        actual = trapezoid_rule(my_func, 0, 5, 10)
        self.assertAlmostEqual(actual, expected_actual)

    def test_trapezoid_rule_20_intervals(self):
        expected = 18.41953576453822622612943

        expected_actual = 18.40029847051851
        actual = trapezoid_rule(my_func, 0, 5, 20)
        self.assertAlmostEqual(actual, expected_actual)

    def test_adaptive_trapezoid_rule_20_intervals(self):
        expected = 18.41953576453822622612943

        expected_actual = 18.4131591489
        actual = adaptive_trapezoid_rule(my_func, 0, 5, 2, 0.01)
        self.assertAlmostEqual(actual, expected_actual)

    def test_adaptive_trapezoid_rule_2000_intervals(self):
        expected = 18.41953576453822622612943
        actual = adaptive_trapezoid_rule(my_func, 0, 5, 2000, 0.000000001)
        self.assertAlmostEqual(expected, actual)


class TestPrimes(unittest.TestCase):

    def setUp(self):
        random.seed(50)

    def test_is_prime(self):
        self.assertTrue(is_prime(5, 10))
        self.assertTrue(is_prime(3, 10))
        self.assertTrue(is_prime(7, 10))
        self.assertTrue(is_prime(5011, 10))
        self.assertFalse(is_prime(4, 10))
        self.assertFalse(is_prime(9, 10))
        self.assertFalse(is_prime(25, 10))
        self.assertFalse(is_prime(532010, 10))

    def test_find_prime_num_digits_correct(self):
        TESTS = 20
        for _ in xrange(TESTS):
            for i in xrange(1, 4):
                self.assertEqual(i, len(str(find_prime(i, 20))))

    def test_find_primes_to_100(self):
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
                    59, 61, 67, 71, 73, 79, 83, 89, 97]
        actual = find_primes(100)
        self.assertEqual(actual, expected)

    def test_find_factors_slow(self):
        actual = find_factors_slow(110)
        expected = [2, 5, 11]
        self.assertEqual(actual, expected)

        actual = find_factors_slow(504)
        expected = [2, 2, 2, 3, 3, 7]
        self.assertEqual(actual, expected)

    def test_find_factors_fast(self):
        actual = find_factors_fast(99999999999999999999)
        expected = [3, 3, 11, 41, 101, 271, 3541, 9091, 27961]
        self.assertEqual(actual, expected)

        actual = find_factors_fast(9007199254740993)
        expected = [3, 107, 28059810762433]
        self.assertEqual(actual, expected)

        actual = find_factors_fast(2**12 * 3**6 * 5)
        expected = [2] * 12 + [3] * 6 + [5]
        self.assertEqual(actual, expected)


class TestDivision(unittest.TestCase):

    def test_long_division_integer_result(self):
        actual = long_division(21, 7)
        self.assertEqual(actual, (3, None, None))

    def test_long_division_non_repeating(self):
        actual = long_division(1, 8)
        self.assertEqual(actual, (0, 125, None))

    def test_long_division_repeating_only(self):
        actual = long_division(1,7)
        self.assertEqual(actual, (0, None, 142857))

    def test_long_division_repeating_and_non_repeating(self):
        actual = long_division(1, 6)
        self.assertEqual(actual, (0, 1, 6))


if __name__ == "__main__":
    nose.main()
