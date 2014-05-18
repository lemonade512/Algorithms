#!/usr/bin/python

from LinkedList import LinkedList, IntegerCell

def HasLoopMarking(sentinel):
    has_loop = False
    
    cell = sentinel
    while cell.next != None:
        if cell.next.visited:
            cell.next = None
            print cell.value
            print cell.next
            has_loop = True
            break

        cell.visited = True
        cell = cell.next

    cell = sentinel
    while cell.next != None:
        cell.visited = False
        cell = cell.next

    return has_loop

if __name__ == "__main__":
    c1 = IntegerCell(1)
    c2 = IntegerCell(2)
    c3 = IntegerCell(3)
    c4 = IntegerCell(4)
    c1.next = c2
    c2.next = c3
    c3.next = c4
    c4.next = c2
    print HasLoopMarking(c1)
    print c4.next
