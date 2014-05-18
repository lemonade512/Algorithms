#!/usr/bin/python

from LinkedList import LinkedList, IntegerCell

if __name__ == "__main__":
    list1 = LinkedList()
    list1.AddAtBeginning(IntegerCell(1))
    list1.AddAtBeginning(IntegerCell(2))
    list1.AddAtBeginning(IntegerCell(3))
    print list1
    print list1.FindCell(3)
    print list1.FindCell(5)
    print list1.FindCellBefore(2).value

    print ""
    list2 = LinkedList()
    list2.AddAtEnd(IntegerCell(1))
    list2.AddAtEnd(IntegerCell(2))
    list2.AddAtEnd(IntegerCell(3))
    print list2
    cell = list2.FindCell(2)
    list2.InsertCell(cell, IntegerCell(7))
    print list2
    print list2.FindCell(2)
    print list2.FindCell(5)
    print list2.FindCellBefore(3).value
    cell = list2.FindCell(7)
    list2.DeleteAfter(cell)
    print list2

    print ""
    list3 = LinkedList()
    list3.AddAtEnd(IntegerCell(1))
    list3.AddAtEnd(IntegerCell(4))
    list3.AddAtEnd(IntegerCell(17))
    print list3
    list3.InsertSorted(IntegerCell(21))
    list3.InsertSorted(IntegerCell(8))
    print list3
