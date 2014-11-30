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
        self.front_index = 0
        self.back_index = size-1

    def __repr__(self):
        return self.stack.__repr__()

    def push_front(self, value):
        if self.front_index > self.back_index:
            raise StackFullError

        self.stack[self.front_index] = value
        self.front_index += 1

    def push_back(self, value):
        if self.front_index > self.back_index:
            raise StackFullError

        self.stack[self.back_index] = value
        self.back_index -= 1

    def pop_front(self):
        if self.front_index == 0:
            print "Stack is empty"
            return None

        self.front_index -= 1
        return self.stack[self.front_index]

    def pop_back(self):
        if self.back_index == self.cap - 1:
            print "Stack is empty"
            return None

        self.back_index += 1
        return self.stack[self.back_index]

