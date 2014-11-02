import unittest

from goldbach import is_prime


class TestIsPrime(unittest.TestCase):

    def test_when_number_is_1(self):
        self.assertFalse(is_prime(1))

    def test_when_number_is_different_from_1_and_is_prime(self):
        self.assertTrue(is_prime(3))

    def test_when_number_is_different_from_1_and_is_not_prime_(self):
        self.assertFalse(is_prime(4))

if __name__ == '__main__':
    unittest.main()