from models.jsonable import Jsonable
import json as json_handler

class Artist(Jsonable):
    def __init__(self,name,last_name,birthday,avatar=None,bio=None,followers=0):
        self.name = name
        self.last_name = last_name
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

    def get_json_object(self):
        data = {
            "type": "artist",
            "name":self.name,
            "last_name":self.last_name,
            "birthday":self.birthday.strftime('%m/%d/%Y'),
            "bio" :self.bio,
            "followers":self.followers,
            "avatar":self.avatar
        }
        return data
    def get_json_str(self):
        return json_handler.dumps(self.get_json_object())