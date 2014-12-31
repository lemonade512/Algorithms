#!/usr/bin/env python

from Algorithms.LinkedLists.Python.linked_list import LinkedList as LL

def has_loop_marking(start):
    has_loop = False

    cell = start
    cell.visited = True
    while cell.next_ is not None:
        if cell.next_.visited:
            cell.next_ = None
            has_loop = True
            break

        cell.visited = True
        cell = cell.next_

    cell = start
    cell.visited = False
    while cell.next_ is not None:
        cell.visited = False
        cell = cell.next_

    return has_loop

if __name__ == "__main__":
    c1 = LL.Cell(1)
    c2 = LL.Cell(2)
    c3 = LL.Cell(3)
    c4 = LL.Cell(4)
    c1.next_ = c2
    c2.next_ = c3
    c3.next_ = c4
    c4.next_ = c2
    print has_loop_marking(c1)
