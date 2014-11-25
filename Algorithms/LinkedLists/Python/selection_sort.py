#!/usr/bin/python

from LinkedList import LinkedList, Cell
from CopyLinkedList import CopyList

def SelectionSort(old_list):
    sorted_list = LinkedList()

    new_list = CopyList(old_list)
    input = new_list.top
    while input.next != None:
        best_after_me = input
        best_value = best_after_me.next.value

        after_me = input.next
        while after_me.next != None:
            if after_me.next.value > best_value:
                best_after_me = after_me
                best_value = after_me.next.value
            after_me = after_me.next

        best_cell = best_after_me.next
        best_after_me.next = best_cell.next

        sorted_list.prepend(best_cell)
    return sorted_list

if __name__ == "__main__":
    list1 = LinkedList()
    list1.append(3)
    list1.append(14)
    list1.append(7)
    list1.append(9)
    list1.append(12)
    list1.append(1)
    print "Unsorted List: ", list1
    list2 = SelectionSort(list1)
    print "Sorted List: ", list2
