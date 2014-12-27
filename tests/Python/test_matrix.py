#!/usr/bin/env python

import nose
import unittest
import operator

from Algorithms.Arrays.Python.matrix import Matrix


class TestMatrix(unittest.TestCase):

    def test_initialize(self):
        m = Matrix(3, 4)
        actual_rows = m.rows
        expected_rows = [[0, 0, 0, 0],
                         [0, 0, 0, 0],
                         [0, 0, 0, 0]]
        self.assertEqual(actual_rows, expected_rows)

    def test_initialize_with_default_val(self):
        m = Matrix(3, 4, default_val=None)
        actual_rows = m.rows
        expected_rows = [[None, None, None, None],
                         [None, None, None, None],
                         [None, None, None, None]]
        self.assertEqual(actual_rows, expected_rows)

    def test_length(self):
        a = Matrix(3, 4)
        self.assertEqual(len(a), 12)

    def test_set_item(self):
        m = Matrix(2, 2)
        m[0, 0] = 1
        m[0, 1] = 2
        m[1, 0] = 3
        m[1, 1] = 4

        actual_rows = m.rows
        expected_rows = [[1, 2],
                         [3, 4]]
        self.assertEqual(actual_rows, expected_rows)

    def test_set_item_index_out_of_bounds(self):
        m = Matrix(2, 2)
        self.assertRaises(IndexError, m.__setitem__, (2, 1), 1)
        self.assertRaises(IndexError, m.__setitem__, (1, 2), 1)

    def test_get_item(self):
        m = Matrix(2, 2, default_val=None)
        self.assertIsNone(m[0, 0])
        m[0, 0] = 1
        self.assertEqual(m[0, 0], 1)

    def test_add_matrices(self):
        mat = [[1, 2, 1],
               [2, 4, 6],
               [3, 1, 1]]
        m1 = Matrix.from_list(mat)

        mat = [[1, 1, 1],
               [-2, 3, -5],
               [0, 0, 3]]
        m2 = Matrix.from_list(mat)

        expected = Matrix.from_list([[2, 3, 2],
                                     [0, 7, 1],
                                     [3, 1, 4]])

        self.assertEqual(m1 + m2, expected)
        self.assertEqual(m2 + m1, expected)

    def test_add_uneven_matrices_cols(self):
        m1 = Matrix(3, 4)
        m2 = Matrix(3, 3)
        self.assertRaises(ValueError, m1.__add__, m2)

    def test_add_uneven_matrices_rows(self):
        m1 = Matrix(4, 3)
        m2 = Matrix(3, 3)
        self.assertRaises(ValueError, m1.__add__, m2)

    def test_add_raises_type_error(self):
        m = Matrix(2, 2)
        self.assertRaises(TypeError, operator.add, m, 5)

    def test_mult_matrices(self):
        m1 = Matrix.from_list([[2, 3],
                               [1, -5]])

        m2 = Matrix.from_list([[4, 3, 6],
                               [1, -2, 3]])

        expected = [[11, 0, 21],
                    [-1, 13, -9]]

        self.assertEqual((m1 * m2).rows, expected)

    def test_mult_raises_value_error(self):
        m1 = Matrix(3, 1)
        m2 = Matrix(3, 1)
        self.assertRaises(ValueError, operator.mul, m1, m2)

    def test_mult_raises_type_error(self):
        m1 = Matrix(4, 3)
        self.assertRaises(TypeError, operator.mul, m1, 5)

    def test_matrix_equals_int_false(self):
        m = Matrix.from_list([[1, 2, 3],
                              [1, 3, 4]])
        self.assertFalse(m == 5)


if __name__ == "__main__":
    nose.main()
