#!/usr/bin/python

from LinkedList import LinkedList, IntegerCell

def CopyList(old_list):
    new_list = LinkedList()
    old_cell = old_list.top.next

    while old_cell != None:
        new_cell = IntegerCell(old_cell.value)
        new_list.AddAtEnd(new_cell)
        old_cell = old_cell.next

    return new_list

if __name__ == "__main__":
    list1 = LinkedList()
    list1.AddAtEnd(IntegerCell(1))
    list1.AddAtEnd(IntegerCell(2))
    list1.AddAtEnd(IntegerCell(3))
    print list1
    list2 = CopyList(list1)
    list2.Iterate()
