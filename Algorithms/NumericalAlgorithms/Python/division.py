#!/usr/bin/env python

def long_division(n, d):
    """ Calculates the decimal representation of a fractional number n/d.

    Args:
        n (int): The numerator of the fraction.
        d (int): The denominator of the fracction.

    Returns:
        A tuple of three values is returned (i, d, r) such that the number
        represented by the fraction is 'i.dr' where r repeats.
    """
    fractional = None
    repeat = None

    integral = n // d
    r = n % d

    fractional_str = ""
    # A dictionary of past states with numerator as key and idx as value
    past_states = {}
    while r != 0:

        n = r * 10

        if n in past_states:
            non_repeating = fractional_str[:past_states[n]]
            if non_repeating != '':
                fractional = int(non_repeating)
            else:
                fractional = None
            repeat = int(fractional_str[past_states[n]:])
            break
        past_states[n] = len(fractional_str)

        q = n // d
        r = n % d
        fractional_str += str(q)
        fractional = int(fractional_str)

    return integral, fractional, repeat
