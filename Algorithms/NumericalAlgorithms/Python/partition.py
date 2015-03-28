#!/usr/bin/env python

def partitions(n):
    """ Finds all of the partitions of a given number.

    Found at http://code.activestate.com/recipes/218332/

    Args:
        n (int): The number to partition.

    Yields:
        Lists of integers that represent partitions of `n`.

        For example, the number 4 will yield the following partitions:
            [1,1,1,1], [1,1,2], [2,2], [1,3], [4]
    """
    if n == 0:
        yield []
        return

    for p in partitions(n-1):
        yield [1] + p
        if p and (len(p) < 2 or p[1] > p[0]):
            yield [p[0] + 1] + p[1:]
