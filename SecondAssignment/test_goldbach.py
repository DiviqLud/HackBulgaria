import unittest

from goldbach import goldbach


class TestGoldbach(unittest.TestCase):

    def test_if_number_is_less_then_2(self):
        self.assertFalse(goldbach(1))

    def test_if_number_is_odd(self):
        self.assertFalse(goldbach(5))

    def test_if_number_is_even(self):
        self.assertTrue(goldbach(6))

    def test_if_number_is_goldbach(self):
        self.assertEqual([(2, 2)], goldbach(4))

if __name__ == '__main__':
    unittest.main()
