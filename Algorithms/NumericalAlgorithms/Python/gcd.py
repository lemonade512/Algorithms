#!/usr/bin/python

def gcd(a, b, *args):
    """ Finds the greatest common denominator of two numbers.

    Implemented using the Euclidian algorithm.
    """
    if len(args) > 0:
        return gcd(gcd(a, b), args[0], *args[1:])
    while(b != 0):
        remainder = a % b
        a, b = b, remainder
    return a

