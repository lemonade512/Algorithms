#!/usr/bin/python

from fibonacci_heap import FibonacciHeap

if __name__ == "__main__":
    fib = FibonacciHeap()
    fib.insert(5)
    fib.insert(3)
    fib.insert(8)
    fib.insert(2)
    fib.insert(1)
    fib.insert(9)

    n = fib.pop()
    print "Popped:", n
    #print "Min: " + str(fib.trees[fib.min_idx].value)
    #print fib
    n = fib.pop()
    print "Popped:", n
    #print fib
    n = fib.pop()
    print "Popped:", n
    #print fib
    n = fib.pop()
    print "Popped:", n
    n = fib.pop()
    print "Popped:", n
    n = fib.pop()
    print "Popped:", n
