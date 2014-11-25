#!/usr/bin/python

class LinkedList:

    class Cell:
        """ Class used to store data and links in a linked list. """

        def __init__(self, value):
            self.value = value
            self.next_ = None
            self.visited = False

        def __str__(self):
            return str(self.value)

        def __repr__(self):
            return repr(self.value)

    def __init__(self):
        """ Initializes a linked list with a sentinel cell. """
        self.top = self.Cell(None)
        self.bottom = self.top

    def __len__(self):
        """ Calculates the length of the linked list. """
        top = self.top
        length = 0
        while top.next_ != None:
            length += 1
            top = top.next_
        return length

    def __repr__(self):
        """ Returns a string representing the linked list. """
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
        """ Iterates through each value of the linked list. Returns a generator. """
        top = self.top
        while top != None:
            yield top.value
            top = top.next_

    def copy(self):
        """ Returns a copy of the linked list. """
        new_list = LinkedList()
        old_cell = self.top.next_

        while old_cell != None:
            new_list.append(old_cell.value)
            old_cell = old_cell.next_

        return new_list

    def get_bottom(self):
        """ Returns the bottom value. """
        return self.bottom.value

    def find(self, target):
        """ Searches for the cell with the given value.

        If there are duplicates in the list this returns the first cell
        with the target value.

        Args:
            target: value to search for

        Returns:
            The cell with the target value.
        """
        top = self.top
        while top != None:
            if top.value == target:
                return top
            top = top.next_

        return None

    def find_cell_before(self, target):
        """ Searches for the cell before the given value.

        Args:
            target: value to search for

        Returns:
            The cell preceding the cell with the target value.
        """
        top = self.top
        while top.next_ != None:
            if top.next_.value == target:
                return top
            top = top.next_

        return None

    def prepend(self, new_value):
        """ Adds a new cell to the beginning of the list.

        Args:
            new_value: The value to add at the beginning.
        """
        new_cell = self.Cell(new_value)

        if self.top == self.bottom:
            self.bottom = new_cell
        new_cell.next_ = self.top.next_
        self.top.next_ = new_cell

    def append(self, new_value):
        """ Adds a new cell to the end of the list.

        Args:
            new_value: The value to add to the list.
        """
        new_cell = self.Cell(new_value)

        top = self.top
        while top.next_ != None:
            top = top.next_

        top.next_ = new_cell
        new_cell.next_ = None
        self.bottom = new_cell

    def insert(self, after_me, new_cell):
        """ Inserts new_cell after after_me.

        If the list is sorted and has duplicates the new_cell will be inserted
        after the last cell with the same value as after_me.

        Args:
        after_me (Cell): The cell to insert after
        new_cell (Cell): The new cell to insert
        """
        while after_me.next_.value == after_me.value:
            after_me = after_me.next_

        if after_me.next_ == None:
            self.bottom = new_cell
        new_cell.next_ = after_me.next_
        after_me.next_ = new_cell

    def insert_sorted(self, new_value):
        """ Inserts a new cell into a sorted list.

        This allows you to keep a linked list sorted.

        Args:
            new_value: The value to insert.
        """
        new_cell = self.Cell(new_value)

        top = self.top
        while top.next_ != None and top.next_.value < new_cell.value:
            top = top.next_

        if top.next_ == None:
            self.bottom = new_cell
        new_cell.next_ = top.next_
        top.next_ = new_cell

    def delete(self, target):
        """ Deletes the target cell from the list. """
        top = self.top
        while (top.next_ != target):
            if top.next_ == None:
                print str(target) + " is not in list"
                return
            top = top.next_

        self.delete_after(top)

    def delete_after(self, after_me):
        """ Deletes the cell after the target cell in the list.

        Args:
            after_me (Cell): The cell to delete after
        """
        if after_me.next_.next_ == None:
            self.bottom = after_me
        if after_me.next_ != None:
            after_me.next_ = after_me.next_.next_
        else:
            print "Could not delete cell"

    def insertion_sort(self):
        """ Returns a sorted list. """
        sorted_list = LinkedList()
        input_ = self.top.next_

        while input_ != None:
            next_cell = self.Cell(input_.value)

            # increment input_
            input_ = input_.next_

            after_me = sorted_list.top
            while after_me.next_ != None and after_me.next_.value < next_cell.value:
                after_me = after_me.next_

            sorted_list.insert(after_me, next_cell)

        return sorted_list

    def selection_sort(self):
        """ Returns a sorted list. """
        sorted_list = LinkedList()

        new_list = self.copy()
        input_ = new_list.top
        while input_.next_ != None:
            best_after_me = input_
            best_value = best_after_me.next_.value

            after_me = input_.next_
            while after_me.next_ != None:
                if after_me.next_.value > best_value:
                    best_after_me = after_me
                    best_value = after_me.next_.value
                after_me = after_me.next_

            best_cell = best_after_me.next_
            best_after_me.next_ = best_cell.next_

            sorted_list.prepend(best_cell)
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

    print "\nInsertion sort"
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

    print "\nSelection sort"
    list1 = LinkedList()
    list1.append(3)
    list1.append(14)
    list1.append(7)
    list1.append(9)
    list1.append(12)
    list1.append(1)
    print "Unsorted List: ", list1
    list2 = list1.selection_sort()
    print "Sorted List: ", list2
