#!/usr/bin/env python

from math import sqrt, ceil

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

    """
    output = list()
    for i in range(1, int(ceil(sqrt(n)))):
        if n == (n / i) * i:
            if i * i == n or i == 1:
                output.append(i)
            else:
                output.append(i)
                output.append(n/i)
    output.append(n)

    return sorted(output)
