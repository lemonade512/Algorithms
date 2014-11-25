#!/usr/bin/python

from LinkedList import LinkedList, IntegerCell

def HasLoopMarking(sentinel):
    has_loop = False

    cell = sentinel
    while cell.next_ != None:
        if cell.next_.visited:
            cell.next_ = None
            print cell.value
            print cell.next_
            has_loop = True
            break

        cell.visited = True
        cell = cell.next_

    cell = sentinel
    while cell.next_ != None:
        cell.visited = False
        cell = cell.next_

    return has_loop

if __name__ == "__main__":
    c1 = IntegerCell(1)
    c2 = IntegerCell(2)
    c3 = IntegerCell(3)
    c4 = IntegerCell(4)
    c1.next_ = c2
    c2.next_ = c3
    c3.next_ = c4
    c4.next_ = c2
    print HasLoopMarking(c1)
    print c4.next_
