#!/usr/bin/env python

import nose
import unittest
import operator

from Algorithms.Arrays.Python.triangular_matrix import TriangularMatrix
from Algorithms.Arrays.Python.matrix import Matrix


class TestTriangularMatrix(unittest.TestCase):

    def test_initialize(self):
        m = TriangularMatrix(3)
        expected_array = [0, 0, 0, 0, 0, 0]
        self.assertEqual(m.array, expected_array)

    def test_initialize_with_default_val(self):
        m = TriangularMatrix(3, default_val=None)
        expected_array = [None, None, None, None, None, None]
        self.assertEqual(m.array, expected_array)

    def test_length(self):
        a = TriangularMatrix(3)
        self.assertEqual(len(a), 9)

    def test_set_item(self):
        m = TriangularMatrix(2)
        m[0, 0] = 1
        m[1, 0] = 3
        m[1, 1] = 4

        expected_array = [1, 3, 4]
        self.assertEqual(m.array, expected_array)

    def test_cannot_set_upper_half(self):
        m = TriangularMatrix(2)
        self.assertRaises(IndexError, m.__setitem__, (0, 1), 1)

    def test_set_item_index_out_of_bounds(self):
        m = TriangularMatrix(2)
        self.assertRaises(IndexError, m.__setitem__, (2, 1), 1)
        self.assertRaises(IndexError, m.__setitem__, (1, 2), 1)

    def test_get_item(self):
        m = TriangularMatrix(2, default_val=None)
        self.assertIsNone(m[0, 0])
        m[0, 0] = 1
        self.assertEqual(m[0, 0], 1)

    def test_get_item_from_upper_half(self):
        m = TriangularMatrix(2)
        self.assertEqual(m[0, 1], 0)
        self.assertRaises(IndexError, m.__setitem__, (0, 1), 1)

    def test_add_matrices(self):
        mat = [[1],
               [2, 4],
               [3, 1, 1]]
        m1 = TriangularMatrix.from_list(mat)

        mat = [[1],
               [-2, 3],
               [0, 0, 3]]
        m2 = TriangularMatrix.from_list(mat)

        expected = TriangularMatrix.from_list([[2],
                                               [0, 7],
                                               [3, 1, 4]])

        self.assertEqual(m1 + m2, expected)
        self.assertEqual(m2 + m1, expected)

    def test_add_raises_type_error(self):
        m = TriangularMatrix(2)
        self.assertRaises(TypeError, operator.add, m, 5)

    def test_mult_matrices(self):
        m1 = TriangularMatrix.from_list([[1],
                                         [2, 1],
                                         [3, 2, 1]])

        m2 = TriangularMatrix.from_list([[1],
                                         [-2, 1],
                                         [1, -2, 1]])

        expected = TriangularMatrix.from_list([[1],
                                               [0, 1],
                                               [0, 0, 1]])

        self.assertEqual((m1 * m2), expected)

    def test_mult_raises_type_error(self):
        m1 = TriangularMatrix(4)
        self.assertRaises(TypeError, operator.mul, m1, 5)

    def test_str(self):
        m = TriangularMatrix.from_list([[1],
                                        [2, 2],
                                        [1, 4, 8]])

        actual = str(m)
        expected = "1 0 0\n2 2 0\n1 4 8"
        self.assertEqual(actual, expected)

    def test_invalid_string_to_matrix_raises_value_error(self):
        l = [[1, 2], [2, 2]]
        self.assertRaises(ValueError, TriangularMatrix.from_list, l)

    def test_add_to_matrix(self):
        m1 = Matrix.from_list([[1, 2, 1],
                               [2, 1, 1],
                               [0, 0, 1]])
        m2 = TriangularMatrix.from_list([[1],
                                         [1, 1],
                                         [1, 1, 1]])
        expected = Matrix.from_list([[2, 2, 1],
                                     [3, 2, 1],
                                     [1, 1, 2]])

        self.assertEqual(m1 + m2, expected)
        self.assertEqual(m2 + m1, expected)


if __name__ == "__main__":
    nose.main()
