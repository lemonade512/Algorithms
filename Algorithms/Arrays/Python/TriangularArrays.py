#!/usr/bin/python

def initialize_array(rows):
    array = [0 for x in range(((rows**2)+rows)/2)]
    return array

def map_index(r, c):
    return ((r)*(r)+(r))/2+c

if __name__ == "__main__":
    array = initialize_array(3)
    print "Before: " + str(array)
    array[map_index(0,0)] = 0
    array[map_index(1,0)] = 1
    array[map_index(1,1)] = 2
    array[map_index(2,0)] = 3
    print "After: " + str(array)
