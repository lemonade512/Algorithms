#!/usr/bin/python
'''
Date Created: 5/18/14
Author: Phillip Lemons
Modified on: 5/18/14
'''

from LinkedList import LinkedList, Cell

class QueueEmptyError(Exception):
    def __init__(self, value="queue is empty"):
        self.value = value
    def __str__(self):
        return repr(self.value)

class LinkedListQueue:

    def __init__(self):
        self.queue = LinkedList()
        self.size = 0

    def __repr__(self):
        return repr(self.queue)

    def __len__(self):
        return self.size

    def Enqueue(self, value):
        self.queue.AddAtBeginning(Cell(value))
        self.size += 1

    def Dequeue(self):
        if self.size == 0:
            raise QueueEmptyError()

        value = self.queue.GetBottom()
        self.queue.Delete(value)
        self.size -= 1
        return value

if __name__ == "__main__":
    my_queue = LinkedListQueue()
    print "Adding values 1-4 to queue"
    for i in range(1,5):
        my_queue.Enqueue(i)
    print my_queue
    print "Dequeue = " + str(my_queue.Dequeue())
    print "Dequeue = " + str(my_queue.Dequeue())
    print my_queue
