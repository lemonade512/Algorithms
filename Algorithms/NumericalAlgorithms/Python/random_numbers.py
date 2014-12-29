#!/usr/bin/python

import sys
import random
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def random_generator(max_num, seed=0):
    """ Uses a linear congruential generator to generate random numbers in the range[0, max_num)

    The constants in this generator are taken from Donald Knuth's MMIX listed on
    http://en.wikipedia.org/wiki/Linear_congruential_generator

    One important thing to note is that with a LCG the numbers flip between odd
    and even. If you want an even distribution of numbers us the FairRandom function
    below.

    Args:
        max_num: The maximum number + 1 (i.e. if max_num = 10 then the generator
                 will produce 0 through 9)
        seed: What number to start the generator on

    Returns:
        A generator that creates random integers in the range [0, max_num)

    Example:
        >>> r = random_generator(100, seed=50)
        >>> next(r)
        85
        >>> next(r)
        96
        >>> next(r)
        11

    """
    a = 6364136223846793005
    b = 1442695040888963407
    m = 18446744073709551616 # 2**64
    num = seed
    while True:
        num = (a * num + b) % m
        yield int(num % max_num)

def fair_generator(min_num, max_num, seed=0):
    """ Provides fair generation of numbers in the given range [min_num, max_num).

    Args:
        min_num: The beginning of the range (inclusive)
        max_num: The end of the range (exclusive)
        seed: The number to start the generator with

    Returns:
        A generator that creates random integers in the range [min_num, max_num)

    Example:
        >>> f_gen = fair_generator(10, 20, seed=5)
        >>> next(f_gen)
        18
        >>> next(f_gen)
        11
        >>> next(f_gen)
        18
        >>> next(f_gen)
        13
        >>> next(f_gen)
        14
        >>> next(f_gen)
        12

    """
    M = 18446744073709551616 # 2**64
    rand = random_generator(M, seed)
    num = seed
    while True:
        num = int(min_num + (float(next(rand))/M)*(max_num-min_num))
        assert num <= max_num
        assert num >= min_num
        yield num

def randomize_array(array):
    """ Takes an array and scrambles it. """
    for i in array:
        j = random.randint(0, len(array)-1)
        array[i], array[j] = array[j], array[i]

def plot(array):
    """ Takes an array of numbers and plots a bar graph of the count of each number. """
    min_num = min(array)
    max_num = max(array)
    x = np.arange(min_num, max_num+1)
    print x
    y = [array.count(i) for i in x]
    labels = [str(i) for i in x]
    width = 2.0 / 3.0
    bar1 = plt.bar(x, y, width, color="red")
    plt.ylabel('Occurences')
    plt.xticks(x + width/2.0, labels)
    plt.show()

def roll_dice(trials, rolls=2, sides=6):
    SIDES = sides # number of sides on the dice (i.e. 6 for d6, 8 for d8)
    ROLLS = rolls
    MAX_NUM = SIDES * ROLLS
    roll_list = []
    f_gen = fair_generator(1, SIDES+1)
    for i in range(trials):
        #rolls = np.random.randint(1,SIDES+1,ROLLS)
        rolls = [next(f_gen) for _ in xrange(ROLLS)]
        total = sum(rolls)
        roll_list.append(total)
    return roll_list

if __name__ == "__main__":
    roll_list = roll_dice(100000)
    plot(roll_list)

    fair_gen = fair_generator(0, 100000)
    num_list = [next(fair_gen) % 2 for _ in xrange(50000)]
    plot(num_list)

    rand = random_generator(sys.maxint, seed=2321)
    print "Pseudo Random Number Generator::"
    print "    - Seed: 2321"
    print "    - Max: sys.maxint"
    print "    - Prints 10 numbers"
    for i in range(10):
        print next(rand)
    print ""

    print "Fair Pseudo Random Number Generator::"
    print "    - Seed: 3521"
    print "    - Range: 0 - 50"
    print "    - Prints 15 numbers"
    fair_random_generator = fair_generator(0, 50, seed=3521)
    for i in range(15):
        print next(fair_random_generator)
    print ""

    print "Randomize array::"
    print "    - array = [0,1,2,3,4,5,6,7,8,9,10]"
    array = [0,1,2,3,4,5,6,7,8,9,10]
    randomize_array(array)
    print array
