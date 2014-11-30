#!/usr/bin/env python
'''
Date Created: 5/18/14
Author: Phillip Lemons
Modified on: 5/18/14
'''

class ArrayQueue:

    def __init__(self):
        self.queue = []
        self.size = 0

    def __repr__(self):
        return repr(self.queue)

    def Enqueue(self, value):
        self.queue.insert(0, value)
        self.size += 1

    def Dequeue(self):
        #TODO use error handling stuff here
        if self.size == 0:
            print "queue is empty"
            return

        value = self.queue.pop()
        self.size -= 1
        return value


if __name__ == "__main__":
    my_queue = ArrayQueue()
    print "Queueing values 1-4"
    for i in range(1,5):
        my_queue.Enqueue(i)
    print my_queue
    print "Dequeue: " + str(my_queue.Dequeue())
    print "Dequeue: " + str(my_queue.Dequeue())
    print my_queue
