from song import Song
import json
from pprint import pprint


class Playlist():

    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song_name):
        for song in self.songs:
            if song.title == song_name:
                self.songs.remove(song)

    def total_length(self):
        sum_of_length = 0
        for song in self.songs:
            sum_of_length += song.length
        return sum_of_length

    def remove_disrated(self, rating):
        for song in self.songs:
            if song.rating < rating:
                self.songs.remove(song)

    def remove_bad_quality(self):
        for song in self.songs:
            if song.bitrate < 100:
                self.songs.remove(song)

    def show_artist(self):
        list_of_artists = []
        for song in self.songs:
            list_of_artists.append(song.artist)
        return set(list_of_artists)

    def __str__(self):
        str_list = []
        for song in self.songs:
            mins = int(song.length) // 60
            sec = int(song.length) % 60
            string = "{} {} - {}:{}".format(song.artist, song.title, mins, sec)
            str_list.append(string)
        return "\n".join(str_list)

    def save(self, document):
        text = open(document, "w")
        songs = []
        for song in self.songs:
            songs.append(({"title": song.title,
                           "artist": song.artist,
                           "album": song.album,
                           "rating": song.rating,
                           "length": song.length,
                           "bitrate": song.bitrate}))
        text.write(json.dumps({"Name": "My Playlist",
                               "Songs": songs}, indent=4, sort_keys=True))
        text.write("\n")
        text.close()

    @staticmethod
    def load(document):
        json_data = open(document, "r")
        data = json.load(json_data)
        new_playlist = Playlist(data["Name"])
        for song in range(len(data["Songs"])):
            title = data["Songs"][song]["title"]
            artist = data["Songs"][song]["artist"]
            album = data["Songs"][song]["album"]
            rating = data["Songs"][song]["rating"]
            length = data["Songs"][song]["length"]
            bitrate = data["Songs"][song]["bitrate"]
            new_playlist.songs.append(Song(title, artist, album, rating, length, bitrate))
        print(new_playlist)
        json_data.close()

