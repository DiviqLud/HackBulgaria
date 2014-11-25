import unittest
import my_playlist
import music_crawler


class TestMusicCrawler(unittest.TestCase):
    def setUp(self):
        self.awesome_playlist = music_crawler.MusicCrawler("/home/galin/Downloads/Rammstein/Singles/2011 - Mein Land")

    def test_generate_playlist(self):
        self.awesome_playlist.generate_playlist()

if __name__ == '__main__':
    unittest.main()
