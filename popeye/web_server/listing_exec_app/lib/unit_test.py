""" Unit Tests for vector_manipulation Functions

Comparisions take place with PRECISION digit precision.
(PRECISION digits after decimal point)
"""

import unittest
import vector_manipulation as vm

OUTPUT_FILE = 'unit_test_vector_manipulation.txt'


class TestVectorManipulationFunctions(unittest.TestCase):

    global PRECISION
    PRECISION = 5

    def test_cos_exception(self):
        # cos() exception checking
        with self.assertRaises(TypeError):
            vm.cos('how on earth is this possible')

    def test_cos_number(self):
        # cos() check Number type
        self.assertAlmostEqual(vm.cos(0), 1, PRECISION)
        self.assertAlmostEqual(vm.cos(vm.np.pi / 6), 0.8660254038, PRECISION)
        self.assertAlmostEqual(vm.cos(vm.np.pi / 3), 0.5, PRECISION)

    def test_cos_vector(self):
        # cos() check vector type
        vec_input = vm.vector(10, 20, 30)
        vec_output = vm.cos(vec_input)
        self.assertAlmostEqual(vec_output[0], -0.8390715291, PRECISION)
        self.assertAlmostEqual(vec_output[1], 0.4080820618, PRECISION)
        self.assertAlmostEqual(vec_output[2], 0.1542514499, PRECISION)

    def test_cosd_exception(self):
        # cosd() exception checking
        with self.assertRaises(TypeError):
            vm.cosd('how on earth is this possible')

    def test_cosd_number(self):
        # cosd() check Number type
        self.assertAlmostEqual(vm.cosd(0), 1, PRECISION)
        self.assertAlmostEqual(vm.cosd(30), 0.8660254038, PRECISION)
        self.assertAlmostEqual(vm.cosd(60), 0.5, PRECISION)

    def test_cosd_vector(self):
        # cosd() check vector type
        vec_input = vm.vector(10, 20, 30)
        vec_output = vm.cosd(vec_input)
        self.assertAlmostEqual(vec_output[0], 0.984807753, PRECISION)
        self.assertAlmostEqual(vec_output[1], 0.9396926208, PRECISION)
        self.assertAlmostEqual(vec_output[2], 0.8660254038, PRECISION)

    def test_sin_exception(self):
        # sin() exception checking
        with self.assertRaises(TypeError):
            vm.sin('how on earth is this possible')

    def test_sin_number(self):
        # sin() check Number type
        self.assertAlmostEqual(vm.sin(0), 0, PRECISION)
        self.assertAlmostEqual(vm.sin(vm.np.pi / 6), 0.5, PRECISION)
        self.assertAlmostEqual(vm.sin(vm.np.pi / 3), 0.8660254038, PRECISION)

    def test_sin_vector(self):
        # sin() check vector type
        vec_input = vm.vector(10, 20, 30)
        vec_output = vm.sin(vec_input)
        self.assertAlmostEqual(vec_output[0], -0.5440211109, PRECISION)
        self.assertAlmostEqual(vec_output[1], 0.9129452507, PRECISION)
        self.assertAlmostEqual(vec_output[2], -0.9880316241, PRECISION)

    def test_sind_exception(self):
        # sind() exception checking
        with self.assertRaises(TypeError):
            vm.sind('how on earth is this possible')

    def test_sind_number(self):
        # sind() check Number type
        self.assertAlmostEqual(vm.sind(0), 0, PRECISION)
        self.assertAlmostEqual(vm.sind(30), 0.5, PRECISION)
        self.assertAlmostEqual(vm.sind(60), 0.8660254038, PRECISION)

    def test_sind_vector(self):
        # sind() check vector type
        vec_input = vm.vector(10, 20, 30)
        vec_output = vm.sind(vec_input)
        self.assertAlmostEqual(vec_output[0], 0.1736481777, PRECISION)
        self.assertAlmostEqual(vec_output[1], 0.3420201433, PRECISION)
        self.assertAlmostEqual(vec_output[2], 0.5, PRECISION)

    def test_tan_exception(self):
        # tan() exception checking
        with self.assertRaises(TypeError):
            vm.tan('how on earth is this possible')

    def test_tan_number(self):
        # tan() check Number type
        self.assertAlmostEqual(vm.tan(0), 0, PRECISION)
        self.assertAlmostEqual(vm.tan(vm.np.pi / 6), 0.5773502692, PRECISION)
        self.assertAlmostEqual(vm.tan(vm.np.pi / 3), 1.732050808, PRECISION)

    def test_tan_vector(self):
        # tan() check vector type
        vec_input = vm.vector(10, 20, 30)
        vec_output = vm.tan(vec_input)
        self.assertAlmostEqual(vec_output[0], 0.6483608275, PRECISION)
        self.assertAlmostEqual(vec_output[1], 2.237160944, PRECISION)
        self.assertAlmostEqual(vec_output[2], -6.405331197, PRECISION)

    def test_tand_exception(self):
        # tand() exception checking
        with self.assertRaises(TypeError):
            vm.tand('how on earth is this possible')

    def test_tand_number(self):
        # tand() check Number type
        self.assertAlmostEqual(vm.tand(0), 0, PRECISION)
        self.assertAlmostEqual(vm.tand(30), 0.5773502692, PRECISION)
        self.assertAlmostEqual(vm.tand(60), 1.732050808, PRECISION)

    def test_tand_vector(self):
        # tand() check vector type
        vec_input = vm.vector(10, 20, 30)
        vec_output = vm.tand(vec_input)
        self.assertAlmostEqual(vec_output[0], 0.1763269807, PRECISION)
        self.assertAlmostEqual(vec_output[1], 0.3639702343, PRECISION)
        self.assertAlmostEqual(vec_output[2], 0.5773502692, PRECISION)


if __name__ == '__main__':
    f = open(OUTPUT_FILE, "w")
    runner = unittest.TextTestRunner(f)
    unittest.main(testRunner=runner)
    f.close()
