import spotipy
from spotipy.oauth2 import SpotifyOAuth

class Spotify:
    def __init__(self, client_id=None, client_secret=None, redirect_uri=None, scope=None):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.scope = scope

    def get_top_liked_songs(self, nb_track_to_get:int = 20, offset:int = 0):
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=self.client_id,
                                                client_secret=self.client_secret,
                                                redirect_uri=self.redirect_uri,
                                                scope=self.scope))
        
        songs_title = []
        results = sp.current_user_saved_tracks(nb_track_to_get, offset)
        
        #Get the name of the artist and song to appned in a list, return a list of string
        for item in results['items']:
            track = item['track']
            songs_title.append(track['artists'][0]['name'] + " – " + track['name'])

        return songs_title