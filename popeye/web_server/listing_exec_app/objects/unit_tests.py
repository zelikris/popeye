""" Formal unit tests for vector class """

import unittest
from vector import *
from matrix import *

class TestMatrixMethods(unittest.TestCase):

    global DELTA
    DELTA = 0.00001

    def test_matrix_init(self):
        mat = matrix(4, 7, 5, 12)
        self.assertEqual(mat[0,0], 4)
        self.assertEqual(mat[0,1], 7)
        self.assertEqual(mat[0,2], 5)
        self.assertEqual(mat[0,3], 12)

        mat = matrix([1,2,3], [4,5,6])
        self.assertEqual(mat[0,0], 1)
        self.assertEqual(mat[0,1], 2)
        self.assertEqual(mat[0,2], 3)
        self.assertEqual(mat[1,0], 4)
        self.assertEqual(mat[1,1], 5)
        self.assertEqual(mat[1,2], 6)

        mat = matrix([[4, 5, 8], [1, 9, 200]])
        self.assertEqual(mat[0,0], 4)
        self.assertEqual(mat[0,1], 5)
        self.assertEqual(mat[0,2], 8)
        self.assertEqual(mat[1,0], 1)
        self.assertEqual(mat[1,1], 9)
        self.assertEqual(mat[1,2], 200)

        # Error checking
        with self.assertRaises(TypeError):
            mat = matrix([1,2,3], "4,5,6", [7,8,9])
        with self.assertRaises(IndexError):
            mat = matrix([1,2,3], [4,5,6,7,8,9])
        
class TestVectorMethods(unittest.TestCase):

    global DELTA
    DELTA = 0.00001

    def test_vector_init(self):
        vec = vector(2.1, 3.9, -1.47)
        self.assertEqual(vec[0], 2.1)
        self.assertEqual(vec[1], 3.9)
        self.assertEqual(vec[2], -1.47)

    def test_vector_indexing(self):
        vec = vector(2.1, 3.9, -1.47)

        # Error checking
        with self.assertRaises(IndexError):
            x = vec[-1]
        with self.assertRaises(IndexError):
            x = vec[3]
        with self.assertRaises(IndexError):
            vec[-1] = -1.0
        with self.assertRaises(IndexError):
            vec[3] = 3.0
        with self.assertRaises(TypeError):
            x = vec[2.5]
        with self.assertRaises(TypeError):
            x = vec['this is bogus']
        with self.assertRaises(TypeError):
            vec[0] = 'this is also bogus'

        # check getitem
        self.assertEqual(vec[0], 2.1)
        self.assertEqual(vec[1], 3.9)
        self.assertEqual(vec[2], -1.47)

        # check setitem
        vec[0] = 1
        self.assertEqual(vec, vector(1, 3.9, -1.47))
        vec[1] = 1
        self.assertEqual(vec, vector(1, 1, -1.47))
        vec[2] = 1
        self.assertEqual(vec, vector(1, 1, 1))

    def test_vector_pemdas(self):
        a = vector(1, 0, 3)
        b = vector(0, 1, 0)
        value1 = 2
        value2 = 0

        # exponentiation
        self.assertEqual(a ** value1, vector(a[0] ** value1,
                                             a[1] ** value1,
                                             a[2] ** value1))
        self.assertEqual(b ** value2, vector(b[0] ** value2,
                                             b[1] ** value2,
                                             b[2] ** value2))

        # multiplication (against constant)
        self.assertEqual(a * value1, vector(a[0] * value1,
                                            a[1] * value1,
                                            a[2] * value1))

        # division
        self.assertEqual(a / value1, vector(a[0] / value1,
                                            a[1] / value1,
                                            a[2] / value1))
        with self.assertRaises(ZeroDivisionError):
            a = a / value2

        # Addition
        self.assertEqual(a + b, vector(a[0] + b[0],
                                       a[1] + b[1],
                                       a[2] + b[2]))

        # Subtraction
        self.assertEqual(a - b, vector(a[0] - b[0],
                                       a[1] - b[1],
                                       a[2] - b[2]))

    def test_vector_length(self):
        zero = vector(0, 0, 0)
        normalized_x = vector(1, 0, 0)
        len_three = vector(1.7320508, 1.7320508, 1.7320508)

        # Error checking
        with self.assertRaises(TypeError):
            length("This is not a vector")

        # Run against zero, normalized, and simple vector
        self.assertEqual(length(zero), 0)
        self.assertEqual(length(normalized_x), 1)
        self.assertAlmostEqual(length(len_three), 3,
                               msg="Not close enough: " + str(length(len_three)),
                               delta=DELTA)

    def test_vector_normalize(self):
        zero = vector(0, 0, 0)
        normalized_x = vector(1, 0, 0)
        len_three = vector(1.7320508, 1.7320508, 1.7320508)

        # Error checking
        with self.assertRaises(ValueError):
            normalize(zero)  # Cannot normalize the zero vector
        with self.assertRaises(TypeError):
            normalize("This is not a vector")

        # Already normalized vector
        norm1 = normalize(normalized_x)
        self.assertAlmostEqual(norm1[0], normalized_x[0],
                               msg="Not close enough: " + str(norm1[0] - normalized_x[0]),
                               delta=DELTA)
        self.assertAlmostEqual(norm1[1], normalized_x[1],
                               msg="Not close enough: " + str(norm1[1] - normalized_x[1]),
                               delta=DELTA)
        self.assertAlmostEqual(norm1[2], normalized_x[2],
                               msg="Not close enough: " + str(norm1[2] - normalized_x[2]),
                               delta=DELTA)

        # Expect aprox vector of [0.57735, 0.57735, 0.57735]
        norm2 = normalize(len_three)
        expect_val = 0.57735
        self.assertAlmostEqual(norm2[0], expect_val,
                               msg="Not close enough: " + str(norm2[0] - expect_val),
                               delta=DELTA)
        self.assertAlmostEqual(norm2[1], expect_val,
                               msg="Not close enough: " + str(norm2[1] - expect_val),
                               delta=DELTA)
        self.assertAlmostEqual(norm2[2], expect_val,
                               msg="Not close enough: " + str(norm2[2] - expect_val),
                               delta=DELTA)

    def test_vector_crossproduct(self):

        # Error checking
        with self.assertRaises(ArithmeticError):
            cross(vector(2, 2), vector(3, 3, 3))
            cross(vector(3, 3, 3), vector(4, 4, 4, 4))
            cross(vector(2, 2), vector(4, 4, 4, 4))

        # Test values from wolfram alpha
        self.assertEqual(cross(vector(1,0,0), vector(1,0,0)), vector(0,0,0))
        self.assertEqual(cross(vector(0,1,0), vector(0,0,1)), vector(1,0,0))
        self.assertEqual(cross(vector(1,2,3), vector(3,2,1)), vector(-4,8,-4))
        self.assertEqual(cross(vector(22,2,12), vector(13,33,23)), vector(-350,-350,700))

if __name__ == '__main__':
    unittest.main()
