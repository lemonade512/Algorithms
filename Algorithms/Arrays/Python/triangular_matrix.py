#!/usr/bin/env python

from Algorithms.Arrays.Python.matrix import Matrix

class TriangularMatrix(Matrix):
    """ A lower triangular matrix that allows for saving space on large
    matrices.

    Example:
        1 0 0 0 0
        2 5 0 0 0
        3 7 1 0 0
        9 2 5 6 0
        1 1 3 2 9
    """

    def __init__(self, rows, default_val=0):
        """ Initialize a triangular matrix with a given number of rows.

        Args:
            rows: The number of rows this matrix has. This matrix is a
                  square matrix so this is also the number of columns in
                  the matrix.
            default_val: The value to return if the client accesses indices
                         in the top half of the matrix
        """
        self.default_val = default_val
        self.num_rows = self.num_cols = rows
        self.array = [default_val for x in range(((rows**2) + rows) / 2)]

    def __getitem__(self, idx):
        """ Allows accessing the matrix like an array.

        Args:
            idx (tuple): The coordinates of the item to retrieve.

        Example
            >>> t = TriangularMatrix(2)
            >>> t[0, 0] = 1
            >>> t[0, 0]
            1
            >>> t[0, 1]
            0

        """
        row, col = idx

        if col > row:
            return self.default_val
        else:
            return self.array[TriangularMatrix._map_index(row, col)]

    def __setitem__(self, idx, val):
        """ Allows setting an item like an array.

        Args:
            idx (tuple): The coordinates of the item to set.

        Example
            >>> t = TriangularMatrix(2)
            >>> t[0, 0] = 1
            >>> t[0, 0]
            1
            >>> t[0, 1]
            0

        """
        row, col = idx

        if col > row:
            raise IndexError, "Invalid location for a triangular matrix"

        self.array[TriangularMatrix._map_index(row, col)] = val

    def __add__(self, other):
        """ Adds two matrices together.

        Returns:
            If a TriangularMatrix is added to another TriangularMatrix then a
            TriangularMatrix will be returned. If a TriangularMatrix is added with
            a SparseMatrix or a Matrix, a Matrix will be returned.
        """
        # NOTE this could be changed to also allow adding a Matrix object but that becomes too
        # complicated to implement for now
        if not isinstance(other, TriangularMatrix):
            print "Returning not implemented"
            return NotImplemented

        new_mat = TriangularMatrix(self.num_rows)
        new_arr = [x + y for x, y in zip(self.array, other.array)]
        new_mat.array = new_arr
        return new_mat

    @classmethod
    def from_list(cls, l):
        """ Creates a TriangularMatrix from a list of lists.

        Example:
            >>> t = TriangularMatrix.from_list([[1], [1, 2], [1, 2, 3]])
            >>> print t
            1 0 0
            1 2 0
            1 2 3

        """
        new_mat = cls(len(l))
        for i, row in enumerate(l):
            if len(row) > i+1:
                raise ValueError("Invalid triangular matrix: " + str(l))
            for j, elem in enumerate(row):
                new_mat[i, j] = elem

        return new_mat

    @staticmethod
    def _map_index(r, c):
        """ Maps the indices (r, c) to the corresponding index in self.array.

        Preconditions:
            c <= r

        Args:
            r: The row to access
            c: The column to access

        Returns:
            Index corresponding to (r, c)
        """
        return ((r)*(r)+(r))/2+c

