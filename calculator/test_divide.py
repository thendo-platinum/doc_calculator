import unittest

from calculator.divide import Divide


class TestDivide(unittest.TestCase):
    def setUp(self):
        self.divide = Divide(10, 2)

    def test_run(self):
        self.divide.v1 = 10
        self.divide.v2 = 2
        result = self.divide.run()
        self.assertEqual(result.result, 5)

    def test_run_divide_by_zero(self):
        self.divide.v1 = 10
        self.divide.v2 = 0
        with self.assertRaises(ValueError):
            self.divide.run()


if __name__ == "__main__":
    unittest.main()
