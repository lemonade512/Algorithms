#!/usr/bin/env python

import nose
import unittest
import random
import sys

from Algorithms.StacksAndQueues.Python.stacks import LinkedListStack, ArrayStack, DoubleStack, StackFullError


class TestLinkedListStack(unittest.TestCase):

    def test_length_after_1_push(self):
        stack = LinkedListStack()
        self.assertEqual(len(stack), 0)
        stack.push(1)
        self.assertEqual(len(stack), 1)

    def test_pop_after_1_push(self):
        stack = LinkedListStack()
        stack.push(4)
        self.assertEqual(stack.pop(), 4)

    def test_stack_repr(self):
        stack = LinkedListStack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(str(stack), "1 --> 2")

    def test_stack_iter(self):
        stack = LinkedListStack()
        stack.push(2)
        stack.push(5)
        stack.push(1)

        actual = [n for n in stack]
        expected = [1, 5, 2]

        self.assertEqual(actual, expected)

    def test_raise_index_error_when_empty(self):
        stack = LinkedListStack()
        stack.push(2)
        stack.pop()
        self.assertRaises(IndexError, stack.pop)

    def test_is_empty(self):
        stack = LinkedListStack()
        self.assertTrue(stack.is_empty())


class TestArrayStack(unittest.TestCase):

    def test_length_after_1_push(self):
        stack = ArrayStack()
        self.assertEqual(len(stack), 0)
        stack.push(1)
        self.assertEqual(len(stack), 1)

    def test_pop_after_1_push(self):
        stack = ArrayStack()
        stack.push(1)
        self.assertEqual(stack.pop(), 1)

    def test_stack_repr(self):
        stack = ArrayStack()
        stack.push(1)
        stack.push(2)

        actual = repr(stack)
        expected = "[1, 2]"

        self.assertEqual(actual, expected)


class TestDoubleStack(unittest.TestCase):

    def test_push_front(self):
        s = DoubleStack(10)
        s.push_front(1)
        s.push_front(2)
        s.push_front(3)
        s.push_front(4)
        s.push_front(5)

        expected = [5, 4, 3, 2, 1]
        actual = [s.pop_front() for n in range(5)]

        self.assertEqual(actual, expected)

    def test_push_back(self):
        s = DoubleStack(10)
        s.push_back(1)
        s.push_back(2)
        s.push_back(3)
        s.push_back(4)
        s.push_back(5)

        expected = [5, 4, 3, 2, 1]
        actual = [s.pop_back() for n in range(5)]

        self.assertEqual(actual, expected)

    def test_push_front_and_back(self):
        s = DoubleStack(10)
        s.push_back(1)
        s.push_back(2)
        s.push_back(3)

        s.push_front(4)
        s.push_front(5)

        actual_back = [s.pop_back() for n in range(3)]
        actual_front = [s.pop_front() for n in range(2)]
        expected_back = [3, 2, 1]
        expected_front = [5, 4]

        self.assertEqual(actual_back, expected_back)
        self.assertEqual(actual_front, expected_front)

    def test_stack_full_error(self):
        s = DoubleStack(3)
        s.push_back(1)
        s.push_back(2)
        s.push_front(3)

        self.assertRaises(StackFullError, s.push_front, 4)
        self.assertRaises(StackFullError, s.push_back, 4)

    def test_pop_front_empty(self):
        s = DoubleStack()
        self.assertRaises(IndexError, s.pop_front)

    def test_pop_back_empty(self):
        s = DoubleStack()
        self.assertRaises(IndexError, s.pop_back)

    def test_repr(self):
        s = DoubleStack(5)
        s.push_front(1)
        s.push_front(2)
        s.push_front(3)
        s.push_back(4)
        s.push_back(5)

        expected = '[1, 2, 3, 5, 4]'
        actual = str(s)

        self.assertEqual(actual, expected)

