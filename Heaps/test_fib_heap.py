#!/usr/bin/python

from fibonacci_heap import FibonacciHeap

if __name__ == "__main__":
    fib = FibonacciHeap()
    fib.insert(5, 5)
    fib.insert(3, 3)
    fib.insert(8, 8)
    fib.insert(2, 2)
    fib.insert(1, 1)
    fib.insert(9, 9)

    n = fib.pop()
    print "Popped:", n.data
    #print "Min: " + str(fib.trees[fib.min_idx].value)
    #print fib
    n = fib.pop()
    print "Popped:", n.data
    #print fib
    n = fib.pop()
    print "Popped:", n.data
    #print fib
    n = fib.pop()
    print "Popped:", n.data
    n = fib.pop()
    print "Popped:", n.data
    n = fib.pop()
    print "Popped:", n.data

    fib = FibonacciHeap()
    fib.insert(5, 5)
    fib.insert(3, 3)
    n = fib.insert(8, 8)
    fib.insert(2, 2)
    fib.insert(1, 1)
    fib.insert(9, 9)

    fib.pop()
    fib.decrease_key(n, 2)
    n = fib.delete(n)
    print 'deleted', n.data
