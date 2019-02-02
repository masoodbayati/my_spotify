from controller.dbHandler.db_handler import DbHandler
from controller.search_management.searcher import Searcher


class SearchInSongs(Searcher):
    def find(self,keywords):
        db_handler = DbHandler()
        return db_handler.get_songs_contains_key_words(keywords)
