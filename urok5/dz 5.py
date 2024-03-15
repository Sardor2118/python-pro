import unittest


class Calculator:
    def plus(self, x, y):
        return x + y

    def minus(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.plus(1, 2), 3)
        self.assertEqual(self.calculator.plus(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(self.calculator.minus(5, 2), 3)
        self.assertEqual(self.calculator.minus(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(2, 3), 6)
        self.assertEqual(self.calculator.multiply(-2, 4), -8)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(6, 2), 3)
        self.assertAlmostEqual(self.calculator.divide(5, 2), 2.5)
        with self.assertRaises(ValueError):
            self.calculator.divide(5, 0)


if __name__ == '__main__':
    unittest.main()
