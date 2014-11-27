#!/usr/bin/env python

DEFAULT = 0

class SparseArray(object):

    class ArrayRow(object):
        """ Class representing a row of values. """

        def __init__(self):
            self.row_number = -1
            self.next_row = None
            self.row_sentinel = SparseArray.ArrayEntry()

        def __repr__(self):
            result = "Row #" + str(self.row_number) + ":: "
            top = self.row_sentinel
            if top.next_entry != None:
                top = top.next_entry
            else:
                print "Row Empty"
                return

            while top != None:
                result += str(top) + " "
                top = top.next_entry
            return result

    class ArrayEntry(object):
        """ Class representing a singular entry in a row. """

        def __init__(self, value = None):
            self.column_number = -1
            self.value = value
            self.next_entry = None

        def __repr__(self):
            return "(" + str(self.column_number) + ", " + str(self.value) + ")"

    def __init__(self):
        self.sentinel = SparseArray.ArrayRow()

    def __str__(self):
        row_sentinel = self.sentinel
        if row_sentinel.next_row != None:
            row_sentinel = row_sentinel.next_row
        else:
            return "Array Empty"

        string = ""
        while row_sentinel != None:
            string += "\n" + str(row_sentinel)
            row_sentinel = row_sentinel.next_row
        return string

    def find_row_before(self, row):
        array_row = self.sentinel
        while (array_row.next_row != None and
               array_row.next_row.row_number < row):
            array_row = array_row.next_row

        return array_row

    def get(self, row, col):
        assert row >= 0
        assert col >= 0

        array_row = self.find_row_before(row)
        array_row = array_row.next_row
        if array_row == None:
            return DEFAULT
        if array_row.row_number > row:
            return DEFAULT

        array_entry = self.find_column_before(array_row, col)
        array_entry = array_entry.next_entry
        if array_entry == None:
            return DEFAULT
        if array_entry.column_number > col:
            return DEFAULT
        return array_entry.value

    def set(self, row, col, value):
        assert row >= 0
        assert col >= 0

        if value == DEFAULT:
            self.delete_entry(row, col)
            return

        array_row = self.find_row_before(row)

        if (array_row.next_row == None or array_row.next_row.row_number > row):
            new_row = SparseArray.ArrayRow()
            new_row.row_number = row
            new_row.next_row = array_row.next_row
            array_row.next_row = new_row

            sentinel_entry = SparseArray.ArrayEntry()
            new_row.row_sentinel = sentinel_entry

        array_row = array_row.next_row
        array_entry = self.find_column_before(array_row, col)

        if (array_entry == None or array_entry.next_entry == None or
                array_entry.next_entry.column_number > col):
            new_entry = SparseArray.ArrayEntry()
            new_entry.column_number = col
            if array_entry == None:
                new_entry.next_entry = None
            else:
                new_entry.next_entry = array_entry.next_entry
                array_entry.next_entry = new_entry

        array_entry = array_entry.next_entry
        array_entry.value = value

    def delete_entry(self, row, col):
        array_row = self.find_row_before(row)

        if (array_row.next_row == None or array_row.next_row.row_number > row):
            return

        target_row = array_row.next_row
        array_entry = self.find_column_before(target_row, col)

        if (array_entry.next_entry == None or array_entry.next_entry.column_number > col):
            return

        array_entry.next_entry = array_entry.next_entry.next_entry

        if target_row.row_sentinel.next_entry != None:
            return

        array_row.next_row = array_row.next_row.next_row

if __name__ == "__main__":
    sparse_array = SparseArray()
    sparse_array.set_value(0, 1, 10)
    sparse_array.set_value(0, 4, 5)
    sparse_array.set_value(3, 5, 4)
    sparse_array.set_value(3, 2, 0)
    print sparse_array
