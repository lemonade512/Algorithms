#!/usr/bin/env python

from math import sqrt

def divisors(n):
    """ Calculates the divisors of `n` and returns the list.

    Args:
        n (int): The number to find the divisors of.

    Returns:
        A list of integers that n is divisible by including the integer
        itself.

    Example:
        >>> divisors(28)
        [1, 2, 4, 7, 14, 28]
        >>> divisors(144)
        [1, 2, 3, 4, 6, 8, 9, 12, 16, 18, 24, 36, 48, 72, 144]

    """
    output = list()
    for i in range(1, int(sqrt(n))+1):
        if n % i == 0:
            if i * i == n:
                output.append(i)
            else:
                output.append(i)
                output.append(n/i)

    return sorted(output)
