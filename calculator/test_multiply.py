import unittest

from calculator.multiply import Multiply


class TestMultiply(unittest.TestCase):
    def setUp(self):
        self.multiply = Multiply(2, 3)

    def test_run(self):
        self.multiply.v1 = 2
        self.multiply.v2 = 3
        result = self.multiply.run()
        self.assertEqual(result.result, 6)

    def test_run_zero_value(self):
        self.multiply.v1 = 5
        self.multiply.v2 = 0
        result = self.multiply.run()
        self.assertEqual(result.result, 0)

    def test_run_negative_values(self):
        self.multiply.v1 = -4
        self.multiply.v2 = 2
        result = self.multiply.run()
        self.assertEqual(result.result, -8)


if __name__ == "__main__":
    unittest.main()
