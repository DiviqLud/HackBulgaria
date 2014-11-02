from song import Song
import playlist
import os
from mutagen.mp3 import MP3
from pprint import pprint
import glob

class MusicCrawler():

    def __init__(self, filepath):
        self.filepath = filepath
        self.my_playlist = playlist.Playlist("Rammstein")

    def generate_playlist(self):
        songs_in_dir = sorted(glob.glob('/home/galin/Downloads/Rammstein/Singles/2011 - Mein Land/*.mp3'))
        for song in songs_in_dir:
            audio = MP3(song)
            #print(audio["TIT2"])
            title = audio["TIT2"]
            album = audio["TALB"]
            artist = audio["TPE1"]
            length = audio.info.length
            bitrate = audio.info.bitrate
            self.my_playlist.songs.append(Song(str(title), str(artist), str(album), 3, length, bitrate))
        self.my_playlist.save("music_crawler.txt")
        return self.my_playlist.load("music_crawler.txt")