import unittest
import calc


class Testcalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(2, 3), 5)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(calc.subtract(2, 3), -1)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(2, 3), 6)
        self.assertEqual(calc.multiply(-5, -1), 5)
        self.assertEqual(calc.multiply(-3, 3), -9)

    def test_divide(self):
        self.assertEqual(calc.divide(2, 3), 0.6666666666666666)
        self.assertEqual(calc.divide(0, 2), 0)
        self.assertEqual(calc.divide(-3, 3), -1)


if __name__ == "__main__":
    unittest.main()
