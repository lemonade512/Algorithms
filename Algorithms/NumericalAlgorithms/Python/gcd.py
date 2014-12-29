#!/usr/bin/python

def gcd(a, b):
    """ Finds the greatest common denominator of two numbers.

    Implemented using the Euclidian algorithm.
    """
    while(b != 0):
        remainder = a % b
        a, b = b, remainder
    return a

if __name__ == "__main__":
    print "gcd(25,30) = " + str(gcd(25,30))
    print "gcd(4851,3003) = " + str(gcd(4851,3003))
    print "gcd(9232,3920) = " + str(gcd(9232,3920))
    print "gcd(13,295) = " + str(gcd(13,295))
