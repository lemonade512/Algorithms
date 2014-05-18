#!/usr/bin/python

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

total_rolls = [0,0,0,0,0,0,0,0,0,0,0]

def plot(array):
    data = [ ("2", array[0]), ("3", array[1]),
          ("4", array[2]), ("5", array[3]),
          ("6", array[4]), ("7", array[5]),
          ("8", array[6]), ("9", array[7]),
          ("10", array[8]), ("11", array[9]),
          ("12", array[10]) ]
    N = len(data)
    x = np.arange(1, N+1)
    y = [num for (s, num) in data]
    labels = [s for (s, num) in data]
    width = 1/1.5
    bar1 = plt.bar(x, y, width, color="red")
    plt.ylabel('Occurences')
    plt.xticks(x+ width/2.0, labels)
    plt.show()

def rollDice(trials):
    for i in range(trials):
        rolls = np.random.randint(1,7,2)
        total = 0
        for j in rolls:
            total += j
        total_rolls[total-2] += 1

if __name__ == "__main__":
    rollDice(100000)
    print total_rolls
    plot(total_rolls)
