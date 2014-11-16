#!/usr/bin/python

def Insert(array, value, position):
    array.insert(position, value)

def Remove(array, position):
    del array[position]

if __name__ == "__main__":
    array = [1,2,3]
    print array
    Insert(array, 0, 0)
    Insert(array, 4, 4)
    print array
    Remove(array, 1)
    print array
