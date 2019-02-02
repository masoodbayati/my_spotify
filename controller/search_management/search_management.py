import json as json_handler

from controller.search_management.search_in_songs import SearchInSongs
from models.song import Song


class SearchManagement():
    def search(self,query,search_types):
        keywords = self.prepare_query(query)
        searcher = SearchInSongs()
        return searcher.find(keywords)


    def prepare_query(self,query):
        return query.split(" ")

    def get_json_string(self, search_result):
        data = {"result": []}
        for item in search_result:
             data["result"].append(item.get_json_object())
        return json_handler.dumps(data)

