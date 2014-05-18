#!/usr/bin/python

def InitializeArray(rows):
    array = [0 for x in range(((rows**2)+rows)/2)]
    return array

def MapIndex(r, c):
    return ((r)*(r)+(r))/2+c

if __name__ == "__main__":
    array = InitializeArray(3)
    print "Before: " + str(array)
    array[MapIndex(0,0)] = 0
    array[MapIndex(1,0)] = 1
    array[MapIndex(1,1)] = 2
    array[MapIndex(2,0)] = 3
    print "After: " + str(array)
