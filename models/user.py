from models.jsonable import Jsonable


class User(Jsonable):
    def __init__(self,name,email,password_hash,clients,username,role,user_id,primary_clients,intrested_artist=None,recently_played=None,favorit_songs=None):
        self.name = name
        self.email = email
        self.password_hash = password_hash
        self.clients = clients
        self.username = username
        self.role = role
        self.user_id = user_id
        self.primary_clients = primary_clients
        self.intrested_artist = intrested_artist
        self.recently_played = recently_played
        self.favorite_songs = favorit_songs



