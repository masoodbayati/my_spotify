from controller.media_management.simple_recommendation import SimpleRecommendation


class MediaManagement():
    def recommend(self,playlist,recent_played,favorite_songs,favorite_albums,favorite_artists):
            recommendation = SimpleRecommendation()
            return recommendation.recommend(playlist,recent_played,favorite_songs,favorite_albums,favorite_artists)

