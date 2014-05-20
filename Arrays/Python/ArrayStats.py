#!/usr/bin/python

from math import sqrt

def FindMinimum(array):
    minimum = array[0]
    for i in array:
        if i < minimum:
            minimum = i
    return minimum

def FindMaximum(array):
    maximum = array[0]
    for i in array:
        if i > maximum:
            maximum = i
    return maximum

def FindAverage(array):
    total = 0
    for i in array:
        total += i
    return float(total) / len(array)

def FindSampleVariance(array):
    average = FindAverage(array)

    arr_sum = 0
    for num in array:
        arr_sum += (num - average)**2

    return arr_sum / len(array)

def FindStdDeviation(array):
    smpl_var = FindSampleVariance(array)

    return sqrt(smpl_var)

if __name__ == "__main__":
    array = [1,4,5,23,6,6,3,2,43]
    print array
    print "Maximum: " + str(FindMaximum(array))
    print "Minimum: " + str(FindMinimum(array))
    print "Average: " + str(FindAverage(array))
    print "Sample Variance: " + str(FindSampleVariance(array))
    print "Standard Deviation: " + str(FindStdDeviation(array))
