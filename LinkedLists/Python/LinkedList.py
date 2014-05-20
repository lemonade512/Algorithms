#!/usr/bin/python
'''
Date Created: Unknown
Author: Phillip Lemons
Modified on: 5/18/14
'''

class Cell:

    def __init__(self, value):
        self.value = value
        self.next = None
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
        while top.next != None:
            length += 1
            top = top.next
        return length

    def __repr__(self):
        top = self.top
        if top.next != None:
            top = top.next
        string = ''
        string += str(top.value)
        top = top.next
        while top != None:
            string += ' --> ' + str(top.value)
            top = top.next
        string += '\nBottom: ' + str(self.bottom.value)
        return string

    def __iter__(self):
        top = self.top
        while top != None:
            yield top
            top = top.next

    def get_bottom(self):
        return self.bottom

    def find_cell(self, target):
        top = self.top
        while top != None:
            if top.value == target:
                return top
            top = top.next

        return None

    def find_cell_before(self, target):
        top = self.top
        while top.next != None:
            if top.next.value == target:
                return top
            top = top.next

        return None

    def prepend(self, new_value):
        new_cell = Cell(new_value)

        if self.top == self.bottom:
            self.bottom = new_cell
        new_cell.next = self.top.next
        self.top.next = new_cell

    def append(self, new_value):
        new_cell = Cell(new_value)

        top = self.top
        while top.next != None:
            top = top.next

        top.next = new_cell
        new_cell.next = None
        self.bottom = new_cell

    # This currently will not work if there are duplicates of the value
    # passed into <after_me>. Perhaps this actually is better using cells
    # instead of passing values?
    def insert(self, after_me, new_cell):
        #after_me_cell = self.find_cell(after_me)
        #new_cell = Cell(new_value)

        if after_me.next == None:
            self.bottom = new_cell
        new_cell.next = after_me.next
        after_me.next = new_cell

    # Inserts new_cell into a sorted linked list
    def insert_sorted(self, new_value):
        new_cell = Cell(new_value)

        top = self.top
        while top.next != None and top.next.value < new_cell.value:
            top = top.next
        
        if top.next == None:
            self.bottom = new_cell
        new_cell.next = top.next
        top.next = new_cell

    def delete(self, target):
        top = self.top
        while (top.next != target):
            if top.next == None:
                print str(target) + " is not in list"
                return
            top = top.next

        self.DeleteAfter(top)

    def delete_after(self, after_me):
        if after_me.next.next == None:
            self.bottom = after_me
        if after_me.next != None:
            after_me.next = after_me.next.next
        else:
            print "Could not delete cell"
