#!/usr/bin/python
'''
Date Created: Unknown
Author: Phillip Lemons
Modified on: 5/18/14
'''

class Cell:

    def __init__(self, value):
        self.value = value
        self.next_ = None
        self.visited = False

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return repr(self.value)

class LinkedList:

    def __init__(self):
        self.top = Cell(None)
        self.bottom = self.top

    def __len__(self):
        top = self.top
        length = 0
        while top.next_ != None:
            length += 1
            top = top.next_
        return length

    def __repr__(self):
        top = self.top
        if top.next_ != None:
            top = top.next_
        string = ''
        string += str(top.value)
        top = top.next_
        while top != None:
            string += ' --> ' + str(top.value)
            top = top.next_
        string += '\nBottom: ' + str(self.bottom.value)
        return string

    def __iter__(self):
        top = self.top
        while top != None:
            yield top
            top = top.next_

    def copy(self):
        new_list = LinkedList()
        old_cell = self.top.next_

        while old_cell != None:
            new_list.append(old_cell.value)
            old_cell = old_cell.next_

        return new_list

    def get_bottom(self):
        return self.bottom

    def find_cell(self, target):
        top = self.top
        while top != None:
            if top.value == target:
                return top
            top = top.next_

        return None

    def find_cell_before(self, target):
        top = self.top
        while top.next_ != None:
            if top.next_.value == target:
                return top
            top = top.next_

        return None

    def prepend(self, new_value):
        new_cell = Cell(new_value)

        if self.top == self.bottom:
            self.bottom = new_cell
        new_cell.next_ = self.top.next_
        self.top.next_ = new_cell

    def append(self, new_value):
        new_cell = Cell(new_value)

        top = self.top
        while top.next_ != None:
            top = top.next_

        top.next_ = new_cell
        new_cell.next_ = None
        self.bottom = new_cell

    # This currently will not work if there are duplicates of the value
    # passed into <after_me>. Perhaps this actually is better using cells
    # instead of passing values?
    def insert(self, after_me, new_cell):
        #after_me_cell = self.find_cell(after_me)
        #new_cell = Cell(new_value)

        if after_me.next_ == None:
            self.bottom = new_cell
        new_cell.next_ = after_me.next_
        after_me.next_ = new_cell

    # Inserts new_cell into a sorted linked list
    def insert_sorted(self, new_value):
        new_cell = Cell(new_value)

        top = self.top
        while top.next_ != None and top.next_.value < new_cell.value:
            top = top.next_

        if top.next_ == None:
            self.bottom = new_cell
        new_cell.next_ = top.next_
        top.next_ = new_cell

    def delete(self, target):
        top = self.top
        while (top.next_ != target):
            if top.next_ == None:
                print str(target) + " is not in list"
                return
            top = top.next_

        self.DeleteAfter(top)

    def delete_after(self, after_me):
        if after_me.next_.next_ == None:
            self.bottom = after_me
        if after_me.next_ != None:
            after_me.next_ = after_me.next_.next_
        else:
            print "Could not delete cell"

    def insertion_sort(self):
        sorted_list = LinkedList()
        input = self.top.next_

        while input != None:
            next_cell = Cell(input.value)

            # increment input
            input = input.next_

            after_me = sorted_list.top
            while after_me.next_ != None and after_me.next_.value < next_cell.value:
                after_me = after_me.next_

            sorted_list.insert(after_me, next_cell)

        return sorted_list

if __name__ == "__main__":
    list1 = LinkedList()
    list1.append(1)
    list1.append(2)
    list1.append(3)
    print "List 1:"
    print list1
    print "\nList 2:"
    list2 = list1.copy()
    print list2
    print "Changing list 2nd list"
    list2.append(4)
    print list1
    print list2

    list1 = LinkedList()
    list1.append(1)
    list1.append(12)
    list1.append(10)
    list1.append(5)
    list1.append(17)
    list1.append(5)
    print "Unsorted List: ", list1
    list2 = list1.insertion_sort()
    print "Sorted List: ", list2
