#!/usr/bin/env python

from math import sqrt

class Array(object):

    def __init__(self, start_vals=None):
        if start_vals is None:
            self.arr = []
        else:
            self.arr = start_vals

    def __len__(self):
        return len(self.arr)

    def __str__(self):
        return str(self.arr)

    def index_of(self, target):
        for i in range(len(self.arr)):
            if self.arr[i] == target:
                return i

        return -1

    @property
    def minimum(self):
        minimum = self.arr[0]
        for elem in self.arr:
            if elem < minimum:
                minimum = elem
        return minimum

    @property
    def maximum(self):
        maximum = self.arr[0]
        for elem in self.arr:
            if elem > maximum:
                maximum = elem
        return maximum

    @property
    def average(self):
        total = 0
        for elem in self.arr:
            total += elem
        return float(total) / len(self)

    @property
    def sample_variance(self):
        average = self.average

        arr_sum = 0
        for num in self.arr:
            arr_sum += (num - average)**2

        return arr_sum / len(self)

    @property
    def std_deviation(self):
        smpl_var = self.sample_variance

        return sqrt(smpl_var)

if __name__ == "__main__":
    array = Array([1,4,5,23,6,6,3,2,43])
    print array
    print "Maximum: " + str(array.maximum)
    print "Minimum: " + str(array.minimum)
    print "Average: " + str(array.average)
    print "Sample Variance: " + str(array.sample_variance)
    print "Standard Deviation: " + str(array.std_deviation)
