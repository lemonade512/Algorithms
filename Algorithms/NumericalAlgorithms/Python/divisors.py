#!/usr/bin/env python

from math import sqrt

def divisors(n):
    output = list()
    for i in range(1, int(sqrt(n))):
        if n == (n / i) * i:
            if i * i == n or i == 1:
                output.append(i)
            else:
                output.append(i)
                output.append(n/i)
    output.append(n)

    return sorted(output)
