from controller.dbHandler.db_handler import DbHandler
from controller.media_management.recommendation import Recommendation

db_handler = DbHandler()
class SimpleRecommendation(Recommendation):
    def recommend(self,playlist,recent_played,favorite_songs,favorite_albums,favorite_artists):
        return db_handler.get_recommendation(playlist,recent_played,favorite_songs,favorite_albums,favorite_artists)