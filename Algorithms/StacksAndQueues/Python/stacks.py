#!/usr/bin/env python

from Algorithms.LinkedLists.Python.linked_list import LinkedList

class StackFullError(Exception):
    def __init__(self, value="stack is full"):
        self.value = value

class LinkedListStack:

    def __init__(self):
        self.stack = LinkedList()

    def __len__(self):
        """ Returns the length of the stack. """
        return len(self.stack)

    def __repr__(self):
        """ Returns a string representing the stack. """
        return repr(self.stack)

    def __iter__(self):
        """ Iterates through the stack py popping all the items. """
        while len(self) > 0:
            yield self.pop()

    def push(self, value):
        """ Pushes an item onto the top of the stack. """
        self.stack.append(value)

    def pop(self):
        """ Pops the next value off the stack.

        Raises:
            IndexError: When the list is empty.

        Returns:
            The value on the top of the stack.
        """
        if len(self) == 0:
            raise IndexError("The stack is empty")
        value = self.stack.get_bottom()
        self.stack.delete(value)
        return value

    def is_empty(self):
        """ Returns whether the stack is empty or not. """
        return len(self) == 0

class ArrayStack:

    def __init__(self):
        self.stack = []

    def __repr__(self):
        """ Returns a string representation of the stack. """
        return repr(self.stack)

    def __len__(self):
        """ Returns the number of elements in the stack. """
        return len(self.stack)

    def push(self, value):
        """ Pushes a value to the top of the stack. """
        self.stack.append(value)

    def pop(self):
        """ Pops the value off the top of the stack. """
        value = self.stack[-1]
        del self.stack[-1]
        return value

class DoubleStack:

    def __init__(self, size=50):
        self.stack = [None for i in range(size)]
        self.cap = size
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
            raise IndexError("Front of stack is empty")

        self.front_index -= 1
        return self.stack[self.front_index]

    def pop_back(self):
        if self.back_index == self.cap - 1:
            raise IndexError("Back of stack is empty")

        self.back_index += 1
        return self.stack[self.back_index]
