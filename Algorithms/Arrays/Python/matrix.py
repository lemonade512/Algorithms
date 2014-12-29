#!/usr/bin/env python

class Matrix(object):

    def __init__(self, rows, cols, default_val=0):
        """ Initializes a matrix with size rows x cols.

        Args:
            rows: How many rows the matrix will have
            cols: How many cols the matrix will have

        Kwargs:
            default_val: Default initial value for each element
        """
        self.num_rows = rows
        self.num_cols = cols

        # Initialize the 2-dimensional array
        self.rows = [[default_val] * cols for _ in xrange(rows)]

    def __len__(self):
        """ Returns the total number of elements. """
        return self.num_rows * self.num_cols

    def __repr__(self):
        """ Returns a string representation of the matrix. """
        result = ""
        row_prefix = ""
        for i in xrange(self.num_rows):
            result += row_prefix
            col_prefix = ""
            for j in xrange(self.num_cols):
                result += col_prefix + str(self[i, j])
                col_prefix = " "
            row_prefix = "\n"

        return result

    def __getitem__(self, idx):
        """ Allows access like an array.

        For now slicing is not supported but this would be a good
        addition for the future.

        Args:
            idx (tuple): The indices of the value to get

        Example:
            >>> m = Matrix(3, 3)
            >>> m[0, 1] = 2
            >>> m[0, 1]
            2

        """
        return self.rows[idx[0]][idx[1]]

    def __setitem__(self, idx, val):
        """ Sets an element in the matrix.

        Args:
            idx (tuple): The indices of the value to set
            val: The new value

        Example:
            >>> m = Matrix(3, 3)
            >>> m[0, 1] = 2
            >>> m[0, 1]
            2

        """
        self.rows[idx[0]][idx[1]] = val

    def __add__(self, other):
        """ Adds two matrices together.

        Preconditions:
            self.num_cols == other.num_cols
            self.num_rows == other.num_rows

        Args:
            other (Matrix): the matrix to add to self

        Returns:
            A new matrix M such that for each i = 1, 2, 3, ..., self.num_rows and
            for each j = 1, 2, 3, ..., self.num_cols, M[i, j] = self[i, j] + other[i, j]
        """
        if not isinstance(other, Matrix):
            return NotImplemented

        if self.num_cols != other.num_cols:
            raise ValueError(("A matrix with %d columns cannot be added to "
                              "a matrix with %d columns") % (self.num_cols, other.num_cols))

        if self.num_rows != other.num_rows:
            raise ValueError(("A matrix with %d rows cannot be added to "
                              "a matrix with %d rows") % (self.num_cols, other.num_cols))

        new_mat = self.__class__(self.num_rows, other.num_rows)
        for i in xrange(self.num_rows):
            for j in xrange(self.num_cols):
                new_mat[i, j] = self[i, j] + other[i, j]

        return new_mat

    def __radd__(self, other):
        """ Called when other + self returns NotImplemented.

        This function simply calls self + other when other + self cannot be
        performed.
        """
        return self + other

    def __mul__(self, other):
        """ Multiplies two matrices and returns the result.

        Preconditions:
            self.num_cols == other.num_rows

        Args:
            other (Matrix): The matrix to multiply with self

        Returns:
            A new matrix M that is equal to self * other
        """
        if not isinstance(other, Matrix):
            return NotImplemented

        if self.num_cols != other.num_rows:
            raise ValueError("self.num_cols (%d) != other.num_rows (%d)" % (self.num_cols, other.num_cols))

        new_mat = Matrix(self.num_rows, other.num_cols)

        # iterate through rows of self
        for i in range(self.num_rows):
            # iterate through columns of other
            for j in range(other.num_cols):
                # iterate through rows of other
                for k in range(other.num_rows):
                    new_mat[i, j] += self[i, k] * other[k, j]

        return new_mat

    def __eq__(self, other):
        """ Checks to see if two matrices are equal. """
        if not isinstance(other, Matrix):
            return NotImplemented

        if self.num_cols != other.num_cols:
            return False

        if self.num_rows != other.num_rows:
            return False

        for i in xrange(self.num_rows):
            for j in xrange(self.num_cols):
                if self[i, j] != other[i, j]:
                    return False

        return True

    @classmethod
    def from_list(cls, l):
        """ Takes a 2-dimensional list and turns it into a matrix.

        Args:
            l: 2-dimensional list to create the matrix with

        Returns:
            A Matrix object created from the list
        """
        max_cols = max([len(r) for r in l])
        output = cls(len(l), max_cols)

        for i, r in enumerate(l):
            for j, c in enumerate(r):
                output[i, j] = c

        return output

