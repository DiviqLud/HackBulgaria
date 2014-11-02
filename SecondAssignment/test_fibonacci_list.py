import unittest

from fibonacci_lists import nth_fib_lists


class TestFibLists(unittest.TestCase):

    def test_fib_list_if_n_equal_to_1(self):
        self.assertEqual([1, 2, 3], nth_fib_lists([1, 2, 3], [4, 5, 6], 1))

    def test_fib_list_if_n_equal_to_2(self):
        self.assertEqual([4, 5, 6], nth_fib_lists([1, 2, 3], [4, 5, 6], 2))

    def test_fib_list_if_n_equal_to_more_than_2(self):
        self.assertEqual([4, 5, 1, 2, 4, 5], nth_fib_lists([1, 2], [4, 5], 4))

    def test_fib_list_if_one_list_is_empty(self):
        self.assertEqual([1, 2, 3], nth_fib_lists([], [1, 2, 3], 2))

    def test_fib_list_if_two_lists_are_empty(self):
        self.assertEqual([], nth_fib_lists([], [], 4))

if __name__ == '__main__':
    unittest.main()
