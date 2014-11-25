import unittest
import playlist
import song


class TestPlaylist(unittest.TestCase):
    def setUp(self):
        self.awesome_playlist = playlist.Playlist("My Playlist")
        self.lonely = song.Song("Lonely", "Akon", "Forever", 3, 220, 64)
        self.bad_girl = song.Song("Bad girl", "Diddy", "Truly", 4, 180, 164)
        self.last_night = song.Song("Last Night", "Snoop Dogg", "Never", 5, 210, 256)

    def test_playlist_init(self):
        self.assertEqual(self.awesome_playlist.name, "My Playlist")

    def test_add_song(self):
        lonely = song.Song("Lonely", "Akon", "Forever", 5, 220, 64)
        self.awesome_playlist.add_song(lonely)
        self.assertEqual(len(self.awesome_playlist.songs), 1)

    def test_remove_song(self):
        self.awesome_playlist.add_song(self.lonely)
        self.awesome_playlist.add_song(self.bad_girl)
        self.awesome_playlist.remove_song("Bad girl")
        self.assertFalse(self.bad_girl in self.awesome_playlist.songs)

    def test_tota_length(self):
        self.awesome_playlist.add_song(self.lonely)
        self.awesome_playlist.add_song(self.bad_girl)
        self.assertEqual(self.awesome_playlist.total_length(), 400)

    def test_remove_disrated(self):
        self.awesome_playlist.add_song(self.lonely)
        self.awesome_playlist.add_song(self.bad_girl)
        self.awesome_playlist.remove_disrated(4)
        self.assertFalse(self.lonely in self.awesome_playlist.songs)

    def test_remove_bad_quality(self):
        self.awesome_playlist.add_song(self.lonely)
        self.awesome_playlist.add_song(self.bad_girl)
        self.awesome_playlist.remove_bad_quality()
        self.assertFalse(self.lonely in self.awesome_playlist.songs)

    def test_show_artists(self):
        self.awesome_playlist.add_song(self.lonely)
        self.awesome_playlist.add_song(self.bad_girl)
        self.assertEqual(self.awesome_playlist.show_artist(), {"Akon", "Diddy"})

    def test_str(self):
        self.awesome_playlist.add_song(self.lonely)
        self.awesome_playlist.add_song(self.bad_girl)
        #print(self.awesome_playlist)

    def test_save(self):
        self.awesome_playlist.add_song(self.lonely)
        self.awesome_playlist.add_song(self.bad_girl)
        self.awesome_playlist.add_song(self.last_night)
        self.awesome_playlist.save("my_playlist.txt")

    def test_load(self):
        self.awesome_playlist.load("my_playlist.txt")

if __name__ == '__main__':
    unittest.main()
