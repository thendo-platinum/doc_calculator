import unittest

from calculator.add import Add


class TestAdd(unittest.TestCase):
    def setUp(self):
        self.add = Add(5, 10)

    def test_run(self):
        self.add.v1 = 5
        self.add.v2 = 10
        result = self.add.run()
        self.assertEqual(result.result, 15)


if __name__ == "__main__":
    unittest.main()
