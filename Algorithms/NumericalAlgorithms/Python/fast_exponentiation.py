#!/usr/bin/python

import math

def exponentiate(value, exponent):
    """ Raises a value to some power.

    After a small amount of testing, this method is actually slower
    than the builtin python ** operator.

    Args:
        value: The base value
        exponent: The number to raise value to
    """
    powers = []
    value_to_powers = []

    last_power = 1
    last_value = value
    powers.append(last_power)
    value_to_powers.append(last_value)

    while last_power < exponent:
        last_power = last_power * 2
        last_value = last_value * last_value
        powers.append(last_power)
        value_to_powers.append(last_value)

    result = 1

    power_index = len(powers) - 1
    while power_index >= 0:
        if powers[power_index] <= exponent:
            exponent = exponent - powers[power_index]
            result = result * value_to_powers[power_index]
        power_index -= 1

    return result

if __name__ == "__main__":
    print str(exponentiate(5, 7))
    print str(5**7)
    print ""
    print str(exponentiate(728, 6))
    print str(728**6)
