import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add_numbers_returns_sum(self):
        result = self.calculator.add(20, 60)
        self.assertEqual(20 + 60, result)

        result = self.calculator.add(20.56, 60.89)
        self.assertEqual(20.56 + 60.89, result)

    def test_add_non_numbers_raises_type_error(self):
        self.assertRaises(TypeError, self.calculator.add, "hello", "world")
        self.assertRaises(TypeError, self.calculator.add, 20, "world")
        self.assertRaises(TypeError, self.calculator.add, "hello", 20)
        self.assertRaises(TypeError, self.calculator.add, "60.10.20.3", 20)

    def test_add_string_numbers_returns_sum(self):
        result = self.calculator.add("50", "60.7")
        self.assertEqual(50 + 60.7, result)

        result = self.calculator.add(50, "60.7")
        self.assertEqual(50 + 60.7, result)

        result = self.calculator.add("50", 60.7)
        self.assertEqual(50 + 60.7, result)


    def test_add_string_negative_numbers_returns_sum(self):
        result = self.calculator.add("-50", "60.7")
        self.assertEqual(-50 + 60.7, result)

        result = self.calculator.add(50, "-60.7")
        self.assertEqual(50 + -60.7, result)

        result = self.calculator.add("-50", 60.7)
        self.assertEqual(-50 + 60.7, result)

