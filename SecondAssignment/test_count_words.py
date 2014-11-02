import unittest

from count_words import count_words


class TestCountWords(unittest.TestCase):

    def test_count_one_word(self):
        self.assertEqual({"apple": 1}, count_words(["apple"]))

    def test_count_more_then_one_word(self):
        self.assertEqual({"apple": 2}, count_words(["apple", "apple"]))

    def test_count_more_different_word(self):
        self.assertEqual({"apple": 1, "ass": 1}, count_words(["apple", "ass"]))

    def test_no_word(self):
        self.assertEqual({}, count_words([]))

if __name__ == '__main__':
    unittest.main()