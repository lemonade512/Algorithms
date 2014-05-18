#!/usr/bin/python

def GCD(a, b):
    while(b != 0):
        remainder = a % b
        a = b
        b = remainder
    return a

if __name__ == "__main__":
    print "GCD(25,30) = " + str(GCD(25,30))
    print "GCD(4851,3003) = " + str(GCD(4851,3003))
    print "GCD(9232,3920) = " + str(GCD(9232,3920))
    print "GCD(13,295) = " + str(GCD(13,295))
