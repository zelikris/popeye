"""This module provides the matrix class.

IMPORTANT NOTICE: Don't use vector, cross, etc. as variable names
We have lowercase classes for sake of usability

"""

from numbers import Number
from vector import vector


class matrix(object):
    """matrix class.

    Attirbutes:
        values (Vector[]): vector rows
    """

    def __init__(self, *args):
        """
        Constructs a matrix.

        Initialized with one of the following sets of args:
            Series of Numbers (only one row)
            Series of lists/vectors
            List of list of vectors
        """
        self.values = []
        # Returns [] if no args
        if len(args) > 0:
            # If args are a series of Numbers
            if isinstance(args[0], Number):
                self.values = [vector(*args)]
            # If args are a series of lists or vectors
            elif isinstance(args[0], list) or isinstance(args[0], vector):
                # If args[0] is a list of lists, unpack it
                if any(isinstance(arg, list) or isinstance(arg, vector) for arg in args[0]):
                    args = args[0]
                for arg in args:
                    # If args is a list of list, cast to vector
                    if isinstance(arg, list):
                        arg = vector(arg)
                    elif not isinstance(arg, vector):
                        raise TypeError(
                            str(arg) + ' is not a list or a vector')
                    if len(arg) != len(args[0]):
                        raise IndexError("args aren't the same length")
                    self.values.append(arg)
            else:
                raise TypeError(
                    str(args[0]) + ' is not a Number, list or vector')

    def __add__(self, other):
        """Overloads + operator.

        Args:
            other (matrix, Number): matrix or Number to be added to self

        Returns:
            matrix: The sum of self and other
        """
        if isinstance(other, matrix):
            my_height, my_width = dim(self)
            other_height, other_width = dim(other)
            # My width must be the other height, my height the other width
            if my_width == other_height and my_height == other_width:
                new_matrix = []
                for i in range(my_width):
                    new_matrix.append(self.values[i] + other.values[i])
                return matrix(new_matrix)
            else:
                raise ValueError("matrices have different dimensions")
        elif isinstance(other, Number):
            return matrix([other + row for row in self.values])
        else:
            raise TypeError('only matrices or Numbers can be added to matrices')

    def __eq__(self, other):
        """Overloads == operator.

        Args:
            other (matrix): matrix to compare self to

        Returns:
            bool: if self and mat are equal
        """
        if isinstance(other, matrix):
            if dim(other) == dim(self):
                for a, b in zip(other.values, self.values):
                    if a != b:
                        return False
                return True
            else:
                raise ValueError('matrices have different dimensions')
        else:
            raise TypeError('matrices can only be compared to other matrices')

    def __getitem__(self, index):
        """Gets a single entry in the matrix by (row, col).

        Args:
            index: (row, col) index of entry to get

        Returns:
            Number: entry found in self at index
        """
        row, col = index
        return self.values[row][col]

    def __iter__(self):
        for row in self.values:
            yield row

    def __len__(self):
        """Return the total number of elements in self.

        Returns:
            int: total number of elements
        """
        if len(self.values) == 0:
            return 0
        return len(self.values) * len(self.values[0])

    def __mul__(self, other):
        """Overloads * operator.

        Checks if other is a matrix or Number, and performs matrix multiply or dot product
        as appropriate.

        Args:
            other (matrix, Number): matrix or Number by which to multiply self

        Returns:
            matrix: self multiplied by other
        """
        if isinstance(other, matrix):
            my_height, my_width = dim(self)
            other_height, other_width = dim(other)
            # My width must be the other height, my height the other width
            if my_width == other_height and my_height == other_width:
                new_matrix = []
                for i in range(my_height):
                    row = []
                    for j in range(other_width):
                        msum = 0
                        for k in range(my_width):
                            msum += self[i,k] * other[k,j]
                        row.append(msum)
                    new_matrix.append(row)
                return matrix(new_matrix)
            else:
                raise ValueError("matrices have different dimensions")
        elif isinstance(other, Number):
            return matrix([other * row for row in self.values])
        else:
            raise TypeError('only matrices or Numbers can multiply matrices')

    def __ne__(self, other):
        """Overloads != operator

        Args:
            other (matrix): matrix to compare self to

        Returns:
            bool: if self and other are not equal
        """
        return not self == other

    def __radd__(self, other):
        """Implements reflective addition.

        Args:
            other (matrix, Number): matrix or Number to be added to self

        Returns:
            matrix: The sum of self and other
        """
        return self + other

    def __repr__(self):
        """Returns a simple string representation of self.

        Returns:
            string: simple representatino of self
        """
        return 'matrix: ' + str(self.values)

    def __rmul__(self, other):
        """Implements reflective multiplication

        Args:
            other (matrix, Number): matrix or Number by which to multiply self

        Returns:
            matrix: self multiplied by other
        """
        return self * other

    def __setitem__(self, index, val):
        """Sets a single entry in the matrix by index.

        Args:
            index: (row, col) index of entry to set
            val (Number): value to set entry to
        """
        row, col = index
        if isinstance(val, Number):
            if (row, col) <= dim(self):
                self.values[row][col] = val
            else:
                raise IndexError('index is out of bounds')
        else:
            raise TypeError('value must be a Number')

    def __str__(self):
        """Returns a pretty representation of self.

        Returns:
            string: pretty representation of self
        """
        out = []
        for value in self.values:
            out.append(str(value))
        return '\n'.join(out)

    def _col(self, num):
        """Returns the matrix column with the given index.

        Args:
            num (int): column index

        Returns:
            Number[]: matrix column with given index
        """
        return [row[num] for row in self.values]

    def _row(self, num):
        """Returns the matrix row with the given index.

        Args:
            num (int): row index

        Returns:
            Number[]: matrix row with given index
        """
        return self.values[num]


def dim(mat):
    """Gets matrix dimensions.

    Args:
        mat (matrix): matrix to get dimensions of

    Returns:
        list: dimensions of the matrix
    """
    return len(mat.values[0]), len(mat.values)
