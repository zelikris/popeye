"""This module provides the vector class.

IMPORTANT NOTICE: Don't use vector, cross, etc. as variable names
We have lowercase classes for sake of usability

"""

from math import sqrt
from numbers import Number


class vector(object):
    """vector class.

    Attributes:
        values (Number[]): vector values
    """

    def __init__(self, *args):
        """
        Constructs a vector.

        Initialized with one of the following sets of args:
            Series of Numbers
            List of Numbers
        """
        self.values = []
        # Return [] if no args
        if len(args) > 0:
            # If the first arg is a list, parse that list
            if isinstance(args[0], list):
                # If args[0] is a list of lists, unpack it
                if any(isinstance(arg, list) or isinstance(arg, vector) for arg in args[0]):
                    args = args[0]
                for arg in args[0]:
                    if not isinstance(arg, Number):
                        raise TypeError(str(arg) + ' is not a Number')
                self.values = args[0]
            elif isinstance(args[0], vector):
                self.values = args[0]
            # Otherwise, parse each arg
            else:
                # If there are three args, return a range
                if len(args) == 2:
                    if args[0] <= args[1]:
                        val = args[0]
                        while (val <= args[1]):
                            self.values.append(val)
                            val += 1
                # If there are three args, return a range with delta args[1]
                elif len(args) == 3:
                    if args[0] <= args[2]:
                        val = args[0]
                        while (val <= args[2]):
                            self.values.append(val)
                            val += args[1]
                else:
                    for arg in args:
                        if not isinstance(arg, Number):
                            raise TypeError(str(arg) + ' is not a Number')
                        self.values = args

    def __add__(self, other):
        """Overloads + operator.

        Args:
            other (vector, Number): vector or Number to be added to self

        Returns:
            vector: the sum of self and other
        """
        if isinstance(other, vector):
            # Checks that self and other are the same length
            if len(self.values) == len(other.values):
                return vector(
                    [a + b for a, b in zip(self.values, other.values)])
            else:
                raise IndexError("vectors aren't the same length")
        elif isinstance(other, Number):
            return vector([x + other for x in self.values])
        else:
            raise TypeError('only vectors or Numbers can be added to vectors')

    def __div__(self, other):
        """ Overloads / operator.

        Performs division on all elements of self using a numeric other.

        Args:
            other (Number): A non zero number to divide self

        Returns:
            vector: self divided by other
        """
        if isinstance(other, Number):
            if other != 0:
                return vector([x / other for x in self])
            else:
                raise ZeroDivisionError('Division by zero detected')
        else:
            raise TypeError('Divisor must be a Number')

    def __eq__(self, other):
        """Overloads == operator.

        Args:
            other (vector): vector to compare self to

        Returns:
            bool: if self and other are equal
        """
        if isinstance(other, vector):
            # Checks that self and other are the same length
            if len(self.values) == len(other.values):
                # Compares each value in self to each value in other
                for i in range(len(self.values)):
                    if self.values[i] != other.values[i]:
                        return False
                return True
            else:
                raise IndexError("vectors aren't the same length")
        else:
            raise TypeError('vectors can only be compared to other vectors')

    def __getitem__(self, index):
        """Gets a single entry in the vector by index.

        Args:
            index (Number): index of entry to get

        Returns:
            Number: entry found in self at index
        """
        if isinstance(index, int):
            if index < len(self.values) and index >= 0:
                return self.values[index]
            else:
                raise IndexError('index is out of bounds')
        else:
            raise TypeError('index must be an integer')

    def __iter__(self):
        for x in self.values:
            yield x

    def __len__(self):
        """Returns the number of elements in self.

        Returns:
            int: number of elements
        """
        return len(self.values)

    def __mul__(self, other):
        """Overloads * operator.

        Checks if other is a number or vector, and performs product or
        dot product as appropriate.

        Args:
            other (vector, Number): vector or Number by which to
                                    multiply self

        Returns:
            vector: self multiplied by other
        """
        if isinstance(other, vector):
            # Checks that self and other are the same length
            if len(self.values) == len(other.values):
                # Dot product
                return sum(
                    a * b for a,
                    b in zip(self.values, other.values))
            else:
                raise IndexError("vectors aren't the same length")
        # Normal product
        elif isinstance(other, Number):
            return vector([x * other for x in self.values])
        else:
            raise TypeError('only vectors or Numbers can multiply vectors')

    def __ne__(self, other):
        """Overloads != operator

        Args:
            other (vector): vector to compare self to

        Returns:
            bool: if self and other are not equal
        """
        return not self == other

    def __pow__(self, num):
        """Overloads ** operator.

        Args:
            num (Number): Power to which self will be raised

        Returns:
            vector: self raised to power of num
        """
        if isinstance(num, Number):
            return vector([x**num for x in self.values])
        else:
            raise TypeError('vectors can only be raised to Numbers')

    def __radd__(self, other):
        """Implements reflective addition.

        Args:
            other(vector, Number): vector or Number to be added to self

        Returns:
            vector: The sum of self and other
        """
        return self + other

    def __repr__(self):
        """Returns a simple string representation of self.

        Returns:
            string: simple representation of self
        """
        return 'vector: ' + str(self.values)

    def __rmul__(self, other):
        """Implements reflective multiplication.

        Args:
            other (vector, Number): vector or Number by which to
                                    multiply self

        Returns:
            vector: self multiplied by other
        """
        return self * other

    def __setitem__(self, index, val):
        """Sets a single entry in the vector by index.

        Args:
            index (int): index of entry to set
            val (Number): value to set entry to
        """
        if isinstance(index, int):
            if index < len(self.values) and index >= 0:
                if isinstance(val, Number):
                    lst = list(self.values)
                    lst[index] = val
                    self.values = tuple(lst)
                else:
                    raise TypeError('value must be a number')
            else:
                raise IndexError('index is out of bounds')
        else:
            raise TypeError('index must be an integer')

    def __str__(self):
        """Returns a pretty representation of self

        Returns:
            string: pretty representation of self
        """
        return str(self.values).replace('(', '[').replace(')', ']')

    def __sub__(self, other):
        """Overloads - operator.

        Args:
            other (vector, Number): vector or Number to be subtracted
                                    from self

        Returns:
            vector: The difference of self and other
        """
        if isinstance(other, vector):
            # Checks that self and other are the same length
            if len(self.values) == len(other.values):
                return vector(
                    [a - b for a, b in zip(self.values, other.values)])
            else:
                raise IndexError("vectors aren't the same length")
        elif isinstance(other, Number):
            return vector([x - other for x in self.values])
        else:
            raise TypeError(
                'only vectors or Numbers can be subtracted from vectors')


def cross(vec1, vec2):
    """Calculates the cross product of two vectors.

    Args:
        vec1 (vector): the first vector in the cross product
        vec2 (vector): the second vector in the cross product

    Returns:
        vector: cross product of vec1 and vec2
    """
    if isinstance(vec1, vector) and isinstance(vec2, vector):
        if len(vec1) == 3 and len(vec2) == 3:
            a = vec1.values
            b = vec2.values
            # this is not the most beautiful solution, but: 1. the
            # vector product is only defined for r3 and second with
            # this way we need no additional library.
            return vector([a[1] * b[2] - a[2] * b[1],
                           a[2] * b[0] - a[0] * b[2],
                           a[0] * b[1] - a[1] * b[0]])
        else:
            raise ArithmeticError('both vectors must be length 3')
    else:
        raise TypeError('arguments must be vectors')


def length(vec):
    """Calculates the length of the vector.

    Args:
        vec (vector): vector to calculate length of

    Returns:
        Number: length of vector
    """
    if isinstance(vec, vector):
        vlength = 0
        for value in vec:
            vlength += value * value
        return sqrt(vlength)
    else:
        raise TypeError('argument must be a vector')


def normalize(vec):
    """Returns a normalized vector.

    A normalized vector is a vector whose length is 1

    Args:
        vec (vector): vector to normalize

    Returns:
        vector: normalized vector
    """
    if isinstance(vec, vector):
        vlength = 0
        # Check for zero vector
        if vec != vector(0, 0, 0):
            vlength = length(vec)
            normal = vec / vlength
            return normal.values
        else:
            raise ValueError(
                'cannot normalize a zero vector (division by zero)')
    else:
        raise TypeError('argument must be a vector')
