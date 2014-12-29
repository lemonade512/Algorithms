#!/usr/bin/env python

import nose
import unittest
import operator

from Algorithms.Arrays.Python.sparse_matrix import SparseMatrix


class TestSparseMatrix(unittest.TestCase):

    def test_length(self):
        a = SparseMatrix(3, 4)
        self.assertEqual(len(a), 12)

    def test_set_and_get_item(self):
        m = SparseMatrix(2, 2)
        m[0, 0] = 1
        self.assertEqual(m[0, 0], 1)
        m[0, 1] = 2
        self.assertEqual(m[0, 1], 2)
        m[1, 0] = 3
        self.assertEqual(m[1, 0], 3)
        m[1, 1] = 4
        self.assertEqual(m[1, 1], 4)

    def test_set_item_index_out_of_bounds(self):
        m = SparseMatrix(2, 2)
        self.assertRaises(IndexError, m.__setitem__, (2, 1), 1)
        self.assertRaises(IndexError, m.__setitem__, (1, 2), 1)

    def test_get_item(self):
        m = SparseMatrix(2, 2, default_val=None)
        self.assertIsNone(m[0, 0])
        m[0, 0] = 1
        self.assertEqual(m[0, 0], 1)

    def test_add_matrices(self):
        mat = [[1, 2, 1],
               [2, 4, 6],
               [3, 1, 1]]
        m1 = SparseMatrix.from_list(mat)

        mat = [[1, 1, 1],
               [-2, 3, -5],
               [0, 0, 3]]
        m2 = SparseMatrix.from_list(mat)

        expected = SparseMatrix.from_list([[2, 3, 2],
                                           [0, 7, 1],
                                           [3, 1, 4]])

        self.assertEqual(m1 + m2, expected)
        self.assertEqual(m2 + m1, expected)

    def test_add_uneven_matrices_cols(self):
        m1 = SparseMatrix(3, 4)
        m2 = SparseMatrix(3, 3)
        self.assertRaises(ValueError, m1.__add__, m2)

    def test_add_uneven_matrices_rows(self):
        m1 = SparseMatrix(4, 3)
        m2 = SparseMatrix(3, 3)
        self.assertRaises(ValueError, m1.__add__, m2)

    def test_add_raises_type_error(self):
        m = SparseMatrix(2, 2)
        self.assertRaises(TypeError, operator.add, m, 5)

    def test_mult_matrices(self):
        m1 = SparseMatrix.from_list([[2, 3],
                                     [1, -5]])

        m2 = SparseMatrix.from_list([[4, 3, 6],
                                     [1, -2, 3]])

        expected = SparseMatrix.from_list([[11, 0, 21],
                                           [-1, 13, -9]])

        self.assertEqual(m1 * m2, expected)

    def test_mult_raises_value_error(self):
        m1 = SparseMatrix(3, 1)
        m2 = SparseMatrix(3, 1)
        self.assertRaises(ValueError, operator.mul, m1, m2)

    def test_mult_raises_type_error(self):
        m1 = SparseMatrix(4, 3)
        self.assertRaises(TypeError, operator.mul, m1, 5)

    def test_delete_entry_in_multi_entry_row(self):
        m = SparseMatrix.from_list([[1, 2],
                                    [4, 5, 6]])
        del m[1, 0]
        expected = SparseMatrix.from_list([[1, 2],
                                           [0, 5, 6]])

        self.assertTrue(m, expected)

    def test_delete_entry_in_single_entry_row(self):
        m = SparseMatrix.from_list([[1, 2],
                                    [1]])
        del m[1, 0]
        expected = SparseMatrix.from_list([[1, 2],
                                           [0]])

        self.assertEqual(m, expected)


if __name__ == "__main__":
    nose.main()
