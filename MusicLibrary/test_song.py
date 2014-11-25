import unittest
import song


class TestSong(unittest.TestCase):
    def setUp(self):
        self.new_song = song.Song("Lonely", "Akon", "Forever", 5, 220, 64)

    def test_song_init(self):
        self.assertEqual(self.new_song.title, "Lonely")
        self.assertEqual(self.new_song.artist, "Akon")
        self.assertEqual(self.new_song.album, "Forever")
        self.assertEqual(self.new_song.rating, 5)
        self.assertEqual(self.new_song.length, 220)
        self.assertEqual(self.new_song.bitrate, 64)

    def test_rate(self):
        self.new_song.rate(4)
        self.assertEqual(self.new_song.rating, 4)

    def test_rate_out_of_bound(self):
        with self.assertRaises(ValueError):
            self.assertEqual(self.new_song.rate(6), "Your rate is not in range. Try again from 1 to 5")

if __name__ == '__main__':
    unittest.main() 
