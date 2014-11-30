#!/usr/bin/env python
'''
Date Created: 5/18/14
Author: Phillip Lemons
Modified on: 5/18/14
'''

from LinkedListStack import LinkedListStack

def ReverseArray(array):
    stack = LinkedListStack()
    for val in array:
        stack.Push(val)

    for i in range(len(array)):
        array[i] = stack.Pop()

def ReverseStack(stack):
    new_stack = LinkedListStack()
    for item in stack:
        new_stack.Push(item)

    return new_stack

def InsertionSort(stack):
    raise NotImplementedError()

def SelectionSort(stack):
    raise NotImplementedError()


if __name__ == "__main__":
    arr = [1,2,3,4,5,6]
    print arr
    print "Reversed array: "
    ReverseArray(arr)
    print arr

    print "\nPushing values 1-5 on a stack"
    my_stack = LinkedListStack()
    for num in range(1,6):
        my_stack.Push(num)
    print my_stack
    print "Reversing stack"
    new_stack = ReverseStack(my_stack)
    print new_stack
