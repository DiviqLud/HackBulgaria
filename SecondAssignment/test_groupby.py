import unittest
from groupby import groupby


class TestGroupby(unittest.TestCase):

    def test_if_lambda_work_for_even(self):
        self.assertEqual({0: [0, 2,], 1: [1, 3]}, groupby(lambda x: x % 2, [0, 1, 2, 3,]))

    def test_other_case_for_lambda(self):
        self.assertEqual({0: [0, 3, 6], 1: [1, 4, 7], 2: [2, 5]}, groupby(lambda x: x % 3, [0, 1, 2, 3, 4, 5, 6, 7]))

if __name__ == '__main__':
    unittest.main()

