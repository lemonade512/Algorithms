#!/usr/bin/env python

import random
import math

from Algorithms.Heaps.Python.fibonacci_heap import FibonacciHeap

def heapsort(arr):
    """ Sorts an iterable data structure and returns an array. """
    heap = FibonacciHeap.heapify(arr)
    output = [e for e in heap]
    return output

def mergesort(arr, p, r):
    # Base case is when there is one element then everything is sorted
    if p < r:
        # q is the mid point of the array
        q = int(math.floor((p + r) / 2))
        # Sort left half
        mergesort(arr, p, q)
        # Sort right half
        mergesort(arr, q+1, r)
        # Merge left and right halve
        _merge(arr, p, q, r)

def _merge(arr, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    # Initialize arrays
    left = [0] * (n1 + 1)
    right = [0] * (n2 + 1)

    # Create the left and right half arrays
    for i in range(n1):
        left[i] = arr[p+i]
    for j in range(n2):
        right[j] = arr[q+j+1]

    left[n1] = float("inf")
    right[n2] = float("inf")

    i = 0
    j = 0
    for k in range(p, r+1):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1

def quicksort(arr, p, r):
    if p < r:
        #q = _partition(arr, p, r)
        q = _randomized_partition(arr, p, r)
        quicksort(arr, p, q - 1)
        quicksort(arr, q + 1, r)

def _partition(arr, p, r):
    x = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i+1

def _randomized_partition(arr, p, r):
    i = random.choice(range(p, r+1))
    arr[r], arr[i] = arr[i], arr[r]
    return _partition(arr, p, r)

if __name__ == "__main__":
    print "Heapsort"
    arr = [1, 5, 2, 7, 919, 24, 25, 12, 43]
    print "Before:", arr
    sorted_arr = heapsort(arr)
    print "After:", sorted_arr

    print

    print "Quicksort"
    sorted_arr = [e for e in arr]
    print "Before:", sorted_arr
    quicksort(sorted_arr, 0, len(sorted_arr)-1)
    print "After:", sorted_arr

    print

    print "Mergesort"
    sorted_arr = [e for e in arr]
    print "Before:", sorted_arr
    mergesort(sorted_arr, 0, len(sorted_arr)-1)
    print "After:", sorted_arr
