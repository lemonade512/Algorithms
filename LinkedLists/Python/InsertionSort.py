#!/usr/bin/python

from LinkedList import LinkedList, Cell

def InsertionSort(old_list):
    sorted_list = LinkedList()
    input = old_list.top.next

    while input != None:
        next_cell = Cell(input.value)

        # increment input
        input = input.next

        after_me = sorted_list.top
        while after_me.next != None and after_me.next.value < next_cell.value:
            after_me = after_me.next

        sorted_list.insert(after_me, next_cell)

    return sorted_list

if __name__ == "__main__":
    list1 = LinkedList()
    list1.append(1)
    list1.append(12)
    list1.append(10)
    list1.append(5)
    list1.append(17)
    list1.append(5)
    print "Unsorted List: ", list1
    list2 = InsertionSort(list1)
    print "Sorted List: ", list2
