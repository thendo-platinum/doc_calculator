import unittest

from calculator.subtract import Subtract


class TestSubtract(unittest.TestCase):
    def setUp(self):
        self.subtract = Subtract(10, 2)

    def test_run(self):
        self.subtract.v1 = 10
        self.subtract.v2 = 2
        result = self.subtract.run()
        self.assertEqual(result.result, 8)

    def test_run_negative_result(self):
        self.subtract.v1 = 5
        self.subtract.v2 = 10
        result = self.subtract.run()
        self.assertEqual(result.result, -5)


if __name__ == "__main__":
    unittest.main()
