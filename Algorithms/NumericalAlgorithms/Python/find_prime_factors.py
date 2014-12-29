#!/usr/bin/python

import math

def find_factors_slow(number):
    """ Finds the prime factorization of a number.

    Examples:
        >>> find_factors_slow(6)
        [2, 3]
        >>> find_factors_slow(110)
        [2, 5, 11]
        >>> find_factors_slow(504)
        [2, 2, 2, 3, 3, 7]

    """
    factors = []
    for i in range(2,number):
        while(number % i == 0):
            factors.append(i)
            number = number / i
    return factors

def find_factors_fast(number):
    """ Finds the prime factorization of a number.

    This method is much faster than find_factors_slow.

    Examples:
        >>> find_factors_fast(6)
        [2, 3]
        >>> find_factors_fast(110)
        [2, 5, 11]
        >>> find_factors_fast(504)
        [2, 2, 2, 3, 3, 7]

    """
    factors = []

    # Pull out factors of 2
    while (number % 2 == 0):
        factors.append(2)
        number = number / 2

    # Look for odd factors
    i = 3
    max_factor = math.sqrt(number)
    while (i <= max_factor):
        while number % i == 0:
            factors.append(i)
            number = number / i

            max_factor = math.sqrt(number)
        i += 2

    # If there is anything left of the number it is also a factor
    if number > 1:
        factors.append(number)
    return factors

if __name__ == "__main__":
    print "Factors of 5: " + str(find_factors_slow(6))
    print "Factors of 110: " + str(find_factors_slow(110))
    print "Factors of 254: " + str(find_factors_slow(254))
    print "Factors of 504: " + str(find_factors_fast(504))
    print "Factors of 50230492: " + str(find_factors_fast(50230492))
    print "Factors of 5023949230290: " + str(find_factors_fast(5023949230290))
