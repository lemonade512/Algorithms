#!/usr/bin/python

def IndexOf(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i

    return -1

if __name__ == "__main__":
    array = [1,5,2,3,17,4,15,16]
    print array
    print "Index of 5: " + str(IndexOf(array, 5))
    print "Index of 7: " + str(IndexOf(array, 7))
