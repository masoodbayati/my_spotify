from models.jsonable import Jsonable


class Album(Jsonable):
    def __init__(self,songs,name,avatar):
        self.songs = songs
        self.name = name
        self.avatar = avatar

    def get_songs(self):
        return self.songs

    def set_songs(self,songs):
        self.songs = songs

    def get_name(self):
        return self.name

    def set_name(self,name):
        self.name = name

    def get_avatar(self):
        return self.avatar

    def set_avatar(self,avatar):
        self.avatar = avatar

    def add_song(self,song):
        self.songs.add(song)

    def del_song(self,song):
        self.songs.remove(song)

