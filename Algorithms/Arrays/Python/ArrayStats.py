#!/usr/bin/env python

from math import sqrt

def find_minimum(array):
    minimum = array[0]
    for i in array:
        if i < minimum:
            minimum = i
    return minimum

def find_maximum(array):
    maximum = array[0]
    for i in array:
        if i > maximum:
            maximum = i
    return maximum

def find_average(array):
    total = 0
    for i in array:
        total += i
    return float(total) / len(array)

def find_sample_variance(array):
    average = FindAverage(array)

    arr_sum = 0
    for num in array:
        arr_sum += (num - average)**2

    return arr_sum / len(array)

def find_std_deviation(array):
    smpl_var = FindSampleVariance(array)

    return sqrt(smpl_var)

if __name__ == "__main__":
    array = [1,4,5,23,6,6,3,2,43]
    print array
    print "Maximum: " + str(find_maximum(array))
    print "Minimum: " + str(find_minimum(array))
    print "Average: " + str(find_average(array))
    print "Sample Variance: " + str(find_sample_variance(array))
    print "Standard Deviation: " + str(find_std_deviation(array))
