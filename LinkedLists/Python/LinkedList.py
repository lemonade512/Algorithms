#!/usr/bin/python

class IntegerCell:

    def __init__(self, value):
        self.value = value
        self.next = None
        self.visited = False

class LinkedList:

    def __init__(self):
        self.top = IntegerCell(None)
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

    def Iterate(self):
        top = self.top
        while top != None:
            print top.value
            top = top.next

    def FindCell(self, target):
        top = self.top
        while top != None:
            if top.value == target:
                return top
            top = top.next

        return None

    def FindCellBefore(self, target):
        top = self.top
        while top.next != None:
            if top.next.value == target:
                return top
            top = top.next

        return None

    def AddAtBeginning(self, new_cell):
        if self.top == self.bottom:
            self.bottom = new_cell
        new_cell.next = self.top.next
        self.top.next = new_cell

    def AddAtEnd(self, new_cell):
        top = self.top
        while top.next != None:
            top = top.next

        top.next = new_cell
        new_cell.next = None
        self.bottom = new_cell

    def InsertCell(self, after_me, new_cell):
        if after_me.next == None:
            self.bottom = new_cell
        new_cell.next = after_me.next
        after_me.next = new_cell

    # Inserts new_cell into a sorted linked list
    def InsertSorted(self, new_cell):
        top = self.top
        while top.next != None and top.next.value < new_cell.value:
            top = top.next
        
        if top.next == None:
            self.bottom = new_cell
        new_cell.next = top.next
        top.next = new_cell

    def DeleteAfter(self, after_me):
        if after_me.next.next == None:
            self.bottom = after_me
        if after_me.next != None:
            after_me.next = after_me.next.next
        else:
            print "Could not delete cell"
