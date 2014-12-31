#!/usr/bin/python

def gcd(a, b):
    """ Finds the greatest common denominator of two numbers.

    Implemented using the Euclidian algorithm.
    """
    while(b != 0):
        remainder = a % b
        a, b = b, remainder
    return a

