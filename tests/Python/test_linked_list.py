#!/usr/bin/env python

import nose
import unittest

from Algorithms.LinkedLists.Python.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):

    def test_append_cell(self):
        l = LinkedList()
        c = LinkedList.Cell(1)
        l.append(c)
        self.assertIn(1, l)

    def test_list_contains_num_after_append(self):
        l = LinkedList()
        l.append(2)
        self.assertIn(2, l)

    def test_list_length_after_append(self):
        l = LinkedList()
        self.assertEqual(len(l), 0)
        l.append(2)
        self.assertEqual(len(l), 1)

    def test_list_iter_append_values(self):
        l = LinkedList()
        l.append(1)
        l.append(2)
        l.append(3)
        l.append(4)

        expected = [1, 2, 3, 4]
        actual = [val for val in l]

        self.assertEqual(actual, expected)

    def test_list_iter_prepend_values(self):
        l = LinkedList()
        l.prepend(1)
        l.prepend(2)
        l.prepend(3)
        l.prepend(4)

        expected = [4, 3, 2, 1]
        actual = [val for val in l]

        self.assertEqual(expected, actual)

    def test_list_copy(self):
        l1 = LinkedList()
        l1.append(1)
        l1.append(2)
        l1.append(3)
        l1.append(4)

        l2 = l1.copy()

        expected = [val for val in l1]
        actual = [val for val in l2]

        self.assertEqual(expected, actual)

    def test_get_bottom(self):
        l = LinkedList()
        l.append(1)
        l.append(2)
        l.prepend(3)

        self.assertEqual(2, l.get_bottom())

    def test_find_returns_none(self):
        l = LinkedList()
        l.append(1)
        l.append(2)
        l.append(3)
        self.assertIsNone(l.find(5))

    def test_find_returns_value(self):
        l = LinkedList()
        l.append(1)
        l.append(4)
        l.append(6)
        cell = l.find(4)
        self.assertEqual(LinkedList.Cell(4), cell)

    def test_insert_sorted(self):
        l = LinkedList()
        l.insert_sorted(3)
        l.insert_sorted(1)
        l.insert_sorted(6)
        l.insert_sorted(2)

        expected = [1, 2, 3, 6]
        actual = [val for val in l]

        self.assertEqual(actual, expected)

    def test_insert_sorted_cell(self):
        l = LinkedList()
        l.append(4)
        l.append(6)
        c = LinkedList.Cell(5)
        l.insert_sorted(c)
        self.assertEqual(l.index(5), 1)

    def test_insert_cell(self):
        l = LinkedList()
        l.append(2)
        l.append(3)
        c = LinkedList.Cell(1)
        l.insert(0, c)
        self.assertEqual(l.index(1), 0)

    def test_delete_value(self):
        l = LinkedList()
        l.append(1)
        l.append(2)
        l.append(3)
        l.append(4)

        l.delete(1)

        expected = [2, 3, 4]
        actual = [e for e in l]

        self.assertEqual(actual, expected)

    def test_insertion_sort(self):
        l = LinkedList()
        l.append(5)
        l.append(9)
        l.append(2)
        l.append(7)
        l.append(25)
        l.append(14)
        l = l.insertion_sort()

        expected = [2, 5, 7, 9, 14, 25]
        actual = [e for e in l]

        self.assertEqual(actual, expected)

    def test_selection_sort(self):
        l = LinkedList()
        l.append(5)
        l.append(9)
        l.append(2)
        l.append(7)
        l.append(25)
        l.append(14)
        l = l.selection_sort()

        expected = [2, 5, 7, 9, 14, 25]
        for e in l:
            print "E:", e
        actual = [e for e in l]

        self.assertEqual(actual, expected)

    def test_index(self):
        l = LinkedList()
        l.append(1)
        l.append(3)
        l.append(12)
        l.append(5)
        idx = l.index(5)

        self.assertEqual(idx, 3)

    def test_list_repr(self):
        l = LinkedList()
        l.append(1)
        l.append(2)
        l.append(3)
        actual = repr(l)

        expected = "1 --> 2 --> 3"
        self.assertEqual(actual, expected)

    def test_cell_repr(self):
        c = LinkedList.Cell(1)
        actual = repr(c)
        expected = "1"
        self.assertEqual(actual, expected)

    def test_cell_not_equal(self):
        c1 = LinkedList.Cell(1)
        c2 = LinkedList.Cell(4)
        self.assertTrue(c1 != c2)

    def test_index_returns_negative_one(self):
        l = LinkedList()
        idx = l.index(4)
        self.assertEqual(idx, -1)

    def test_prepend_cell(self):
        l = LinkedList()
        l.append(1)
        l.append(2)
        l.append(3)
        c1 = LinkedList.Cell(4)
        l.prepend(c1)

        expected = [4, 1, 2, 3]
        actual = [e for e in l]

        self.assertEqual(actual, expected)

    def test_delete_not_in_list(self):
        l = LinkedList()
        l.append(1)
        l.append(2)
        l.append(3)
        self.assertIsNone(l.delete(5))


