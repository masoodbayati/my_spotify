import random
from sqlite3.dbapi2 import Date
import datetime
from config import Config
from models.Artist import Artist
from models.client import Client
from models.client_status import ClientStatus
from models.client_type import ClientType
from models.file import File
from models.song import Song
from models.song_types import SongTypes


class DbHandler():
    def get_file_binary_from_db(self, url):
        # todo get from db
        return Config.music_address

    def get_file_info_from_db(self, file_id):
        return  File(file_id, '/root', random.randint(1, 1000) * 5, 'mp3', None)

    def get_songs_contains_key_words(self,keywords):
        yeganeh = Artist("mohsen","yeganeh",datetime.datetime(1985,4,4))
        khaje_amiri = Artist("ehsan","kaje_amiri",datetime.datetime(1987,5,6))
        songs_list = [
            Song("akarin_bar",yeganeh,123,SongTypes.pop,["love"],None),
            Song("avalin_bar", khaje_amiri, 456, SongTypes.pop, ["love"],None)
        ]
        return songs_list

    def get_all_clients_of_user(self,user):
        client_list = [Client("ASDFWERVKWNFJWEURHBSDFKU",ClientType.android,ClientStatus.online),
                       Client("LDSFIJWFNSDFUWHEKFOV@#$UHJF", ClientType.pc, ClientStatus.offline)]
        return client_list

    def get_recommendation(self, playlist, recent_played, favorite_songs, favorite_albums, favorite_artists):
        yeganeh = Artist("mohsen", "yeganeh", datetime.datetime(1985, 4, 4))
        khaje_amiri = Artist("ehsan", "kaje_amiri", datetime.datetime(1987, 5, 6))
        songs_list = [
            Song("akarin_bar", yeganeh, 123, SongTypes.pop, ["love"], None),
            Song("avalin_bar", khaje_amiri, 456, SongTypes.pop, ["love"], None)
        ]
        return songs_list