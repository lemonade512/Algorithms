#!/usr/bin/python

import sys
import random

# m = maximum number
# seed defines starting point
# a and b are constants
def Random(m, seed = 0):
    a = 7
    b = 5
    num = seed
    while True:
        num = (a * num + b) % m
        yield num

def FairRandom(min_num, max_num, seed):
    rand = Random(500, seed)
    num = seed
    while True:
        num = int(min_num + (float(next(rand))/500)*(max_num-min_num))
        assert num <= max_num
        assert num >= min_num
        yield num

def RandomizeArray(array):
    for i in array:
        j = random.randint(0, len(array)-1)
        temp = array[i]
        array[i] = array[j]
        array[j] = temp

if __name__ == "__main__":
    random_generator = Random(sys.maxint, 2321)
    print "Pseudo Random Number Generator::"
    print "    - Seed: 2321"
    print "    - Max: sys.maxint"
    print "    - Prints 10 numbers"
    for i in range(10):
        print next(random_generator)
    print ""

    print "Fair Pseudo Random Number Generator::"
    print "    - Seed: 3521"
    print "    - Range: 0 - 50"
    print "    - Prints 15 numbers"
    fair_random_generator = FairRandom(0, 50, 3521)
    for i in range(15):
        print next(fair_random_generator)
    print ""

    print "Randomize array::"
    print "    - array = [0,1,2,3,4,5,6,7,8,9,10]"
    array = [0,1,2,3,4,5,6,7,8,9,10]
    RandomizeArray(array)
    print array
