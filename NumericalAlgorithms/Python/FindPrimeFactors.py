#!/usr/bin/python

import math

def FindFactorsSlow(number):
    factors = []
    for i in range(2,number):
        while(number % i == 0):
            factors.append(i)
            number = number / i
    return factors

def FindFactorsFast(number):
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
    print "Factors of 110: " + str(FindFactorsSlow(110))
    print "Factors of 254: " + str(FindFactorsSlow(254))
    print "Factors of 504: " + str(FindFactorsFast(504))
    print "Factors of 50230492: " + str(FindFactorsFast(50230492))
    print "Factors of 5023949230290: " + str(FindFactorsFast(5023949230290))
