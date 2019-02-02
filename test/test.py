import unittest
from unittest.mock import MagicMock

from controller.dbHandler.db_handler import DbHandler
from controller.file_management.file_manager import FileManager
from controller.media_management.media_management import MediaManagement
from controller.search_management.search_management import SearchManagement
from controller.user_management.user_management import UserMangement
from models.client import Client
from models.client_status import ClientStatus
from models.client_type import ClientType


class test_spotify(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.file_manager = FileManager()
        self.seach_management = SearchManagement()
        self.db_handler = DbHandler()
        self.user_management = UserMangement()
        self.media_management =MediaManagement()
        self.user = MagicMock()
        self.user.user_id = 123
        self.client = Client("ASDFWERVKWNFJWEURHBSDFKU",ClientType.android,ClientStatus.online)
        self.playlist = MagicMock()
        self.recent_played = MagicMock()
        self.favorite_songs = MagicMock()
        self.favorite_albums = MagicMock()
        self.favorite_artists = MagicMock()

    def test_check_file(self):
        self.assertEqual(self.file_manager.check_file(123,123).file_id,self.db_handler.get_file_info_from_db(123).file_id)

    def test_search(self):
        self.assertEqual(self.seach_management.search("asd",["pop"]).__len__(),
                         self.db_handler.get_songs_contains_key_words(["asd"]).__len__())

    def test_get_all_client_online(self):
        self.assertEqual(self.user_management.get_online_clients_of_user(self.user).__len__()+1,
                         self.db_handler.get_all_clients_of_user(self.user).__len__())

    def test_set_status(self):
        self.assertEqual(self.user_management.set_client_as_primary(self.user,self.client),ClientStatus.primary)

    def test_media_recommendation(self):
        self.assertEqual(len(self.media_management.recommend(self.playlist,self.recent_played,self.favorite_songs,self.favorite_albums,self.favorite_artists)), 2)