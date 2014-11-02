import unittest
from magic_square import magic_square


class TestMagicSquare(unittest.TestCase):
    def test_if_magic_square_work(self):
        self.assertFalse(magic_square([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

    def test_magic_square_success(self):
        self.assertTrue(magic_square([[4, 9, 2], [3, 5, 7], [8, 1, 6]]))


if __name__ == '__main__':
    unittest.main()
