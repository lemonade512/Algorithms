#!/usr/bin/env python

from Algorithms.Arrays.Python.matrix import Matrix

class SparseMatrix(Matrix):
    """ A sparse matrix used to save space with large matrices.

    Attributes:
        num_rows: The number of rows in the matrix.
        num_cols: The number of columns in the matrix.
        default: The default value to return when accessing elements
                 that have not yet been set.
        sentinel: The first dummy row of the matrix. This makes some
                  operations a little bit easier.
    """

    class MatrixRow(object):
        """ Class representing a row of values. """

        def __init__(self):
            """ Initializes this row with default values and a sentinel entry. """
            self.row_number = -1
            self.next_row = None
            self.row_sentinel = SparseMatrix.MatrixEntry()

    class MatrixEntry(object):
        """ Class representing a singular entry in a row. """

        def __init__(self, value = None):
            """ Initializes the entry with default values. """
            self.column_number = -1
            self.value = value
            self.next_entry = None

    def __init__(self, rows, cols, default_val=0):
        """ Initializes the matrix with a size, a default value, and a row sentinel. """
        self.num_rows = rows
        self.num_cols = cols
        self.default = default_val

        self.sentinel = SparseMatrix.MatrixRow()

    def __getitem__(self, idx):
        """ Allows accessing the matrix like an array.

        Raises:
            IndexError: If the index is out of bounds an IndexError will be raised

        Example:
            >>> m = SparseMatrix(5, 5)
            >>> m[1, 2] = 3
            >>> m[1, 2]
            3
            >>> m[3, 4]
            0

        """
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
        """ Allows setting an item like an array.

        Raises:
            IndexError: If the index is out of bounds an IndexError will be raised

        Example:
            >>> m = SparseMatrix(3, 3)
            >>> m[1, 2]
            0
            >>> m[1, 2] = 5
            >>> m[1, 2]
            5

        """
        row, col = idx

        if row < 0 or row >= self.num_rows:
            raise IndexError("Row out of bounds")

        if col < 0 or col >= self.num_cols:
            raise IndexError("Col out of bounds")

        if value == self.default:
            del self[row, col]
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

    def __delitem__(self, idx):
        """ Allows removing an item using the del keyword.

        Example:
            >>> m = SparseMatrix(2, 2)
            >>> m[0, 0]
            0
            >>> m[0, 0] = 2
            >>> m[0, 0]
            2
            >>> del m[0, 0]
            >>> m[0, 0]
            0

        """
        row, col = idx

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

