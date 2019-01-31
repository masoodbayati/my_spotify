from models.jsonable import Jsonable


class Song(Jsonable):
    def __init__(self,name,artist,file_id,type,keywords,avatar):
        self.name = name
        self.artist = artist
        self.file_id = file_id
        self.type = type
        self.keywords = keywords
        self.avatar = avatar

    def get_name(self):
        return self.name

    def get_artist(self):
        return self.artist

    def get_file_id(self):
        return self.file_id

    def get_type(self):
        return self.type

    def get_keywords(self):
        return self.keywords

    def get_avatar(self):
        return self.avatar

    def set_name(self,name):
        self.name = name

    def set_artist(self,artist):
        self.artist = artist

    def set_file_id(self,file_id):
        self.file_id = file_id

    def set_type(self,type):
        self.type = type

    def set_keywords(self,keywords):
        self.keywords = keywords

    def set_avatar(self,avatar):
        self.avatar = avatar

        
