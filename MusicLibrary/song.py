class Song():
    def __init__(self, title, artist, album, rating, length, bitrate):
        self.title = title
        self.artist = artist
        self.album = album
        self.rating = rating
        self.length = length
        self.bitrate = bitrate

    def rate(self, rate):
        self.rating = rate
        if self.rating < 0 or self.rating > 5:
            raise ValueError("Your rate is not in range. Try again from 1 to 5")