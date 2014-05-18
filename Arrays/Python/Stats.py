#!/usr/bin/python

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
    return total / len(array)

if __name__ == "__main__":
    array = [1,4,5,23,6,6,3,2,43]
    print array
    print "Maximum: " + str(FindMaximum(array))
    print "Minimum: " + str(FindMinimum(array))
    print "Average: " + str(FindAverage(array))
