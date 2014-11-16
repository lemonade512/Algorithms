#!/usr/bin/python

import math
import random

# This is a probabilistic algorithm.
# If p passes k tests then there is a (1/2)^k chance that p is
# actually a composite number. If you run 100 tests that chance
# is 7.8*10^-31.
def IsPrime(p, max_tests):
    for test in range(max_tests):
        rand = random.randint(1, p-1)
        if (rand**(p-1) % p != 1):
            return False

    return True

def FindPrime(num_digits, max_tests):
    while True:
        rand = random_with_n_digits(num_digits)
        if IsPrime(rand, max_tests):
            return rand

def random_with_n_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return random.randint(range_start, range_end)

if __name__ == "__main__":
    print "1377 is prime: " + str(IsPrime(1377, 100))
    print "1523 is prime: " + str(IsPrime(1523, 100))
    print "1277 is prime: " + str(IsPrime(1277, 100))
    print ""
    print "3 digit prime: " + str(FindPrime(3, 10))
    print "5 digit prime: " + str(FindPrime(5, 10))
