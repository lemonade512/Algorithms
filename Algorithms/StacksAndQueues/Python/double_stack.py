#!/usr/bin/env python
'''
Date Created: 5/18/14
Author: Phillip Lemons
Modified On:
'''

class StackFullError(Exception):
    def __init__(self, value="stack is full"):
        self.value = value
    def __str__(self):
        return repr(self.value)

class DoubleStack:

    def __init__(self, size=50):
        self.stack = [None for i in range(size)]
        self.cap = size
        self.size = 0
        self.NextIndex1 = 0
        self.NextIndex2 = size-1

    def __repr__(self):
        return self.stack.__repr__()

    def Push1(self, value):
        if self.NextIndex1 > self.NextIndex2:
            raise StackFullError()

        self.stack[self.NextIndex1] = value
        self.NextIndex1 += 1

    def Push2(self, value):
        if self.NextIndex1 > self.NextIndex2:
            raise StackFullError()

        self.stack[self.NextIndex2] = value
        self.NextIndex2 -= 1

    def Pop1(self):
        if self.NextIndex1 == 0:
            print "Stack is empty"
            return None

        self.NextIndex1 -= 1
        return self.stack[self.NextIndex1]

    def Pop2(self):
        if self.NextIndex2 == self.cap - 1:
            print "Stack is empty"
            return None

        self.NextIndex2 += 1
        return self.stack[self.NextIndex2]


if __name__ == "__main__":
    my_stack = DoubleStack(20)
    print "Pushing values 1-4 to first stack"
    for i in range(1,5):
        my_stack.Push1(i)
    print my_stack
    print "Pushing values 1-4 to second stack"
    for i in range (1,5):
        my_stack.Push2(i)
    print my_stack

    print "\nTesting StackFullError"
    new_stack = DoubleStack(10)
    for i in range(1,14):
        new_stack.Push1(i)
