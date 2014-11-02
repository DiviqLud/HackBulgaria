import unittest
from magic_square import check_main_diagonal


class TestRowsInMagicSquare(unittest.TestCase):

    def test_if_rows_sum_is_equal_to_first_row(self):
        self.assertTrue(check_main_diagonal(15, [[4, 9, 2], [3, 5, 7], [8, 1, 6]]))

    def test_if_rows_sum_is_not_equal_to_first_row(self):
        self.assertFalse(check_main_diagonal(14, [[4, 9, 2], [3, 5, 7], [8, 1, 6]]))


if __name__ == '__main__':
    unittest.main()
