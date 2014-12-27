#!/usr/bin/env python

""" This module contains a customized array class that can be used much
like a python list with a few extra methods.

This module needs to be named something other than array.py because
there is a builtin module called array in the standard library.
"""

from math import sqrt

class Array(object):
    """ A basic array data structure.

    In python this class is a bit unnecessary as most of the methods are already
    implemented using a python list. That being said, I still wanted to have an
    array class that added the properties std_deviation, average, and sample_variance.

    Also, this serves as a good baseline for what a similar class in other languages
    (like c++ or haskell) should look like.
    """

    def __init__(self, start_vals=None):
        if start_vals is None:
            self.arr = []
        else:
            self.arr = start_vals

    def __len__(self):
        """ Returns the number of elements in self. """
        return len(self.arr)

    def __str__(self):
        """ Returns a string representation of self. """
        return str(self.arr)

    def insert(self, idx, val):
        """ Inserts an item into the array pushing everything else to the right.

        If the index is larger than the array, then the new element will just be
        appended to the end.

        Args:
            idx (int): The index to insert the new value
            val: The new value to insert

        Example:
            >>> arr = Array()
            >>> arr.insert(0, 0)
            >>> arr.insert(1, 1)
            >>> print arr
            [0, 1]
            >>> arr.insert(0, -1)
            >>> print arr
            [-1, 0, 1]

        """
        self.arr.insert(idx, val)

    def remove(self, idx):
        """ Removes the item at the given index.

        Args:
            idx (int): The index of the element to delete.

        Example:
            >>> a = Array()
            >>> a.insert(0, 0)
            >>> a.insert(1, 1)
            >>> a.insert(2, 2)
            >>> print a
            [0, 1, 2]
            >>> a.remove(1)
            >>> print a
            [0, 2]

        """
        del self.arr[idx]

    def index_of(self, target):
        """ Finds the index of a target value.

        Args:
            target: The value to search for

        Returns:
            The index of the target value or -1 if the value cannot be found.
        """
        for i in range(len(self.arr)):
            if self.arr[i] == target:
                return i

        return -1

    @property
    def minimum(self):
        """ Returns the minimum element of the array.

        Example:
            >>> a = Array()
            >>> a.insert(0, 0)
            >>> a.insert(1, 1)
            >>> a.minimum
            0

        """
        minimum = self.arr[0]
        for elem in self.arr:
            if elem < minimum:
                minimum = elem
        return minimum

    @property
    def maximum(self):
        """ Returns the maximum element of the array.

        Example:
            >>> a = Array()
            >>> a.insert(0, "hello")
            >>> a.insert(1, "goodbye")
            >>> a.insert(2, "zen of python")
            >>> a.maximum
            'zen of python'

        """
        maximum = self.arr[0]
        for elem in self.arr:
            if elem > maximum:
                maximum = elem
        return maximum

    @property
    def average(self):
        """ Returns the average value of the array.

        This is only defined for arrays that contain number elements.
        """
        total = 0
        for elem in self.arr:
            total += elem
        return float(total) / len(self)

    @property
    def sample_variance(self):
        """ Finds the sample variance of the array.

        The sample variance is only defined when the array contains only numbers.

        Uses the equation :math:`\\frac{1}{n} \\sum_{i=1}^{n}(x_i - \\mu)^2`
        """
        average = self.average

        arr_sum = 0
        for num in self.arr:
            arr_sum += (num - average)**2

        return arr_sum / len(self)

    @property
    def std_deviation(self):
        """ Finds the standard deviation of the array.

        The sample variance is only defined when the array contains only numbers.

        The standard deviation is the square root of the sample variance.
        """
        smpl_var = self.sample_variance

        return sqrt(smpl_var)
