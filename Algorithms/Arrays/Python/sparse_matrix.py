#!/usr/bin/env python

from Algorithms.Arrays.Python.matrix import Matrix

class SparseMatrix(Matrix):

    class MatrixRow(object):
        """ Class representing a row of values. """

        def __init__(self):
            self.row_number = -1
            self.next_row = None
            self.row_sentinel = SparseMatrix.MatrixEntry()

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

    class MatrixEntry(object):
        """ Class representing a singular entry in a row. """

        def __init__(self, value = None):
            self.column_number = -1
            self.value = value
            self.next_entry = None

        def __repr__(self):
            return "(" + str(self.column_number) + ", " + str(self.value) + ")"

    def __init__(self, rows, cols, default_val=0):
        self.num_rows = rows
        self.num_cols = cols
        self.default = default_val

        self.sentinel = SparseMatrix.MatrixRow()

    def __str__(self):
        row_sentinel = self.sentinel
        if row_sentinel.next_row != None:
            row_sentinel = row_sentinel.next_row
        else:
            return "Matrix Empty"

        string = ""
        while row_sentinel != None:
            string += "\n" + str(row_sentinel)
            row_sentinel = row_sentinel.next_row
        return string

    def __getitem__(self, idx):
        row, col = idx

        if row < 0 or row >= self.num_rows:
            raise IndexError("Row out of bounds")

        if col < 0 or col >= self.num_cols:
            raise IndexError("Col out of bounds")

        array_row = self._find_row_before(row)
        array_row = array_row.next_row
        if array_row == None:
            return self.default
        if array_row.row_number > row:
            return self.default

        array_entry = self._find_column_before(array_row, col)
        array_entry = array_entry.next_entry
        if array_entry == None:
            return self.default
        if array_entry.column_number > col:
            return self.default
        return array_entry.value

    def __setitem__(self, idx, value):
        row, col = idx

        if row < 0 or row >= self.num_rows:
            raise IndexError("Row out of bounds")

        if col < 0 or col >= self.num_cols:
            raise IndexError("Col out of bounds")

        if value == self.default:
            self.delete_idx(row, col)
            return

        array_row = self._find_row_before(row)

        if (array_row.next_row == None or array_row.next_row.row_number > row):
            new_row = SparseMatrix.MatrixRow()
            new_row.row_number = row
            new_row.next_row = array_row.next_row
            array_row.next_row = new_row

            sentinel_entry = SparseMatrix.MatrixEntry()
            new_row.row_sentinel = sentinel_entry

        array_row = array_row.next_row
        array_entry = self._find_column_before(array_row, col)

        if (array_entry == None or array_entry.next_entry == None or
                array_entry.next_entry.column_number > col):
            new_entry = SparseMatrix.MatrixEntry()
            new_entry.column_number = col
            if array_entry == None:
                new_entry.next_entry = None
            else:
                new_entry.next_entry = array_entry.next_entry
                array_entry.next_entry = new_entry

        array_entry = array_entry.next_entry
        array_entry.value = value

    def delete_idx(self, row, col):
        array_row = self._find_row_before(row)

        if (array_row.next_row == None or array_row.next_row.row_number > row):
            return

        target_row = array_row.next_row
        array_entry = self._find_column_before(target_row, col)

        if (array_entry.next_entry == None or array_entry.next_entry.column_number > col):
            return

        array_entry.next_entry = array_entry.next_entry.next_entry

        # If this row still has entries in it we are finished
        if target_row.row_sentinel.next_entry != None:
            return

        array_row.next_row = array_row.next_row.next_row

    def _find_row_before(self, row):
        array_row = self.sentinel
        while (array_row.next_row != None and
               array_row.next_row.row_number < row):
            array_row = array_row.next_row

        return array_row

    def _find_column_before(self, row, col):
        entry = row.row_sentinel
        while (entry.next_entry != None and
               entry.next_entry.column_number < col):
            entry = entry.next_entry

        return entry

if __name__ == "__main__":
    sparse_matrix = SparseMatrix()
    sparse_matrix[0, 1] = 10
    sparse_matrix[0, 4] = 5
    sparse_matrix[3, 5] = 4
    sparse_matrix[3, 2] = 0
    print sparse_matrix
