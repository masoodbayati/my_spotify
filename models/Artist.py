from models.jsonable import Jsonable


class Artist(Jsonable):
    def __init__(self,name,birthday,avatar=None,bio=None,followers=0):
        self.name = name
        self.birthday = birthday
        self.avatar = avatar
        self.bio = bio
        self.followers = followers

    def get_name(self):
        return self.name

    def set_name(self,name):
        self.name = name

    def get_birthday(self):
        return self.birthday

    def set_birthday(self,birthday):
        self.birthday = birthday

    def get_avatar(self):
        return self.avatar

    def get_bio(self):
        return self.bio

    def get_followers(self):
        return self.followers

    def set_avatar(self,avatar):
        self.avatar = avatar