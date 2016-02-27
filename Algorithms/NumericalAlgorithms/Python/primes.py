#!/usr/bin/env python

"""
This module contains a number of numerical algorithms relating to
prime numbers.
"""

import math
import random

def is_prime(p, max_tests):
    """ A probablistic algorithm to determine if a number is prime.

    If the number p passes k tests, then there is a (1/2)^k chance that p is a
    composite number. If you run 100 tests, the chance of a false positive is
    7.8*10^-31.

    Args:
        p: The number in question
        max_tests: Number of tests to perform

    Returns:
        A boolean value saying if p is prime or not. If p is prime then the
        function returns True, otherwise the function returns false.
    """
    if p == 1:
        return False

    for test in range(max_tests):
        n = random.randint(1, p-1)
        if (n**(p-1) % p != 1):
            return False

    return True

def find_prime(num_digits, max_tests):
    """ Finds a prime number with the specified number of digits.

    Args:
        num_digits: How many digits we want the prime number to be
        max_tests: How many tests to perform using the probablistic
                   function is_prime

    Returns:
        A number with num_digits that is most likely prime
    """
    while True:
        rand = random_with_n_digits(num_digits)
        if is_prime(rand, max_tests):
            return rand

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

def prime_sieve(limit):
    a = [True] * limit
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):
                a[n] = False

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

def random_with_n_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return random.randint(range_start, range_end)

