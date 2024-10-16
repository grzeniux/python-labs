# Zadanie 7
# Napisz unit testy (z użyciem pakietu unittest) testujące podstawową funkcjonalność klasy

import math
import unittest

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Nie można dzielić przez zero.")
        return a / b

    def power(self, base, exponent):
        return base ** exponent

    def sqrt(self, a):
        if a < 0:
            raise ValueError("Nie można obliczyć pierwiastka kwadratowego z liczby ujemnej.")
        return math.sqrt(a)

    def percentage(self, total, percent):
        return (total * percent) / 100

    def sin(self, angle):
        return math.sin(math.radians(angle))

    def cos(self, angle):
        return math.cos(math.radians(angle))

    def tan(self, angle):
        return math.tan(math.radians(angle))



class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(-1, 1), -2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(0, 100), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-10, 2), -5)
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

    def test_power(self):
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 0), 1)
        self.assertEqual(self.calc.power(10, 2), 100)

    def test_sqrt(self):
        self.assertEqual(self.calc.sqrt(9), 3)
        self.assertEqual(self.calc.sqrt(16), 4)
        with self.assertRaises(ValueError):
            self.calc.sqrt(-1)

    def test_percentage(self):
        self.assertEqual(self.calc.percentage(200, 50), 100)
        self.assertEqual(self.calc.percentage(1000, 25), 250)

    def test_trigonometry(self):
        self.assertAlmostEqual(self.calc.sin(30), 0.5, places=5)
        self.assertAlmostEqual(self.calc.cos(60), 0.5, places=5)
        self.assertAlmostEqual(self.calc.tan(45), 1.0, places=5)

if __name__ == '__main__':
    unittest.main()
