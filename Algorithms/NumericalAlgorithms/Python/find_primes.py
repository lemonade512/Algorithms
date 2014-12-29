#!/usr/bin/python

import math

def find_primes(max_number):
    """ Returns a list of all the primes less than the given number. """
    is_composite = []
    for j in xrange(0, max_number + 1):
        is_composite.append(False)

    i1 = 4
    while i1 <= max_number:
        is_composite[i1] = True
        i1+=2

    next_prime = 3
    stop_at = math.sqrt(max_number)
    while next_prime < stop_at:
        for i2 in xrange(next_prime*next_prime,max_number,next_prime):
            is_composite[i2] = True

        next_prime += 2
        while next_prime <= max_number and is_composite[next_prime]:
            next_prime += 2

    primes = []
    for j in range(2, max_number + 1):
        if not is_composite[j]:
            primes.append(j)

    return primes

if __name__ == "__main__":
    #print str(find_primes(101))
    print str(find_primes(10000))
