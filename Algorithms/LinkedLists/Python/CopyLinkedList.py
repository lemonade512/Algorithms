#!/usr/bin/python

from LinkedList import LinkedList, Cell

def CopyList(old_list):
    new_list = LinkedList()
    old_cell = old_list.top.next

    while old_cell != None:
        new_list.append(old_cell.value)
        old_cell = old_cell.next

    return new_list

if __name__ == "__main__":
    list1 = LinkedList()
    list1.append(1)
    list1.append(2)
    list1.append(3)
    print "List 1:"
    print list1
    print "\nList 2:"
    list2 = CopyList(list1)
    print list2
