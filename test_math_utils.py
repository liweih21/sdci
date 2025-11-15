import unittest
import math_utils

class TestMathUtils(unittest.TestCase):

    def test_add(self):
        self.assertEqual(math_utils.add(2, 3), 5)
        self.assertEqual(math_utils.add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(math_utils.subtract(10, 5), 5)
        self.assertEqual(math_utils.subtract(0, 7), -7)

    def test_multiply(self):
        self.assertEqual(math_utils.multiply(4, 5), 20)
        self.assertEqual(math_utils.multiply(-2, 3), -6)

    def test_divide(self):
        self.assertEqual(math_utils.divide(10, 2), 5)
        self.assertAlmostEqual(math_utils.divide(5, 2), 2.5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            math_utils.divide(10, 0)

if __name__ == "__main__":
    unittest.main()
