#!/usr/bin/env python
'''
Date Created: 5/18/14
Author: Phillip Lemons
'''

class ArrayStack:

    def __init__(self):
        self.stack = []

    def Push(self, value):
        self.stack.append(value)

    def Pop(self):
        value = self.stack[-1]
        del self.stack[-1]
        return value

    def __repr__(self):
        return self.stack.__repr__()

if __name__ == "__main__":
    my_stack = ArrayStack()
    print "Pushing values 1-4"
    for i in range(1,5):
        my_stack.Push(i)
    print my_stack
    print "Popping Value: " + str(my_stack.Pop())
    print "Pushing value 5"
    my_stack.Push(5)
    print my_stack

    print "\nMaking a stack of characters: hello"
    new_stack = ArrayStack()
    new_stack.Push("h")
    new_stack.Push("e")
    new_stack.Push("l")
    new_stack.Push("l")
    new_stack.Push("o")
    print new_stack
    print "Popping Value: " + str(new_stack.Pop())
    print new_stack
