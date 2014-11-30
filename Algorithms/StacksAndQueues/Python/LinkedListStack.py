#!/usr/bin/env python
'''
Date Created: 5/18/14
Author: Phillip Lemons
'''

from Algorithms.LinkedLists.Python.linked_list import LinkedList

class LinkedListStack:

    def __init__(self):
        self.stack = LinkedList()
        self.size = 0

    def __len__(self):
        return self.size

    # Note: this function pops items off the stack which
    # can sometimes cause bad behavior when the client is
    # also popping items. Might want to redisgn this?
    # Definitely need to document this
    def __iter__(self):
        while self.size > 0:
            yield self.pop()

    def push(self, value):
        self.stack.AddAtEnd(Cell(value))
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise ValueError("The stack is empty")
        value = self.stack.GetBottom()
        self.stack.Delete(value)
        self.size -= 1
        return value

    def is_empty():
        return self.size == 0

    def __repr__(self):
        return self.stack.__repr__()

if __name__ == "__main__":
    my_stack = LinkedListStack()
    print "Pushing values 1-4"
    for i in range(1,5):
        my_stack.push(i)
    print my_stack
    print "Popping Value: " + str(my_stack.pop())
    print "Pushing value 5"
    my_stack.push(5)
    print my_stack

    print "\nMaking a stack of characters: hello"
    new_stack = LinkedListStack()
    new_stack.push("h")
    new_stack.push("e")
    new_stack.push("l")
    new_stack.push("l")
    new_stack.push("o")
    print new_stack
    print "Popping Value: " + str(new_stack.pop())
    print new_stack
    new_stack.pop()
    new_stack.pop()
    new_stack.pop()
    new_stack.pop()
    new_stack.pop()
