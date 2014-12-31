#!/usr/bin/env python

from Algorithms.LinkedLists.Python.linked_list import LinkedList

class QueueEmptyError(Exception):
    def __init__(self, value="queue is empty"):
        self.value = value

class LinkedListQueue:

    def __init__(self):
        self.queue = LinkedList()
        self.size = 0

    def __repr__(self):
        return repr(self.queue)

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.queue.prepend(value)
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise QueueEmptyError

        value = self.queue.get_bottom()
        self.queue.delete(value)
        self.size -= 1
        return value

class ArrayQueue:

    def __init__(self):
        self.queue = []

    def __repr__(self):
        return repr(self.queue)

    def __len__(self):
        return len(self.queue)

    def enqueue(self, value):
        self.queue.insert(0, value)

    def dequeue(self):
        if self.size == 0:
            raise QueueEmptyError

        value = self.queue.pop()
        return value
