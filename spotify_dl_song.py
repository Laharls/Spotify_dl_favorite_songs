import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv
from googleapiclient.discovery import build
from youtube_audio_dl import YoutubeAudioDownloader
import sys

def main():
    load_dotenv()

    required_variables = {
        'SPOTIFY_CLIENT_ID': os.getenv('SPOTIFY_CLIENT_ID'),
        'SPOTIFY_CLIENT_SECRET': os.getenv('SPOTIFY_CLIENT_SECRET'),
        'SPOTIFY_APP_REDIRECT_URI': os.getenv("REDIRECT_URI"),
        'SPOTIFY_SCOPE': os.getenv('SCOPE'),
        'YOUTUBE_API_KEY': os.getenv('YOUTUBE_API_KEY')
    }

    for key, value in required_variables.items():
        if not isinstance(value, str) or not value.strip():
            print(f"Error: The value for {key} must be a non-empty string")
            sys.exit(1)

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=required_variables['CLIENT_ID'],
                                                client_secret=required_variables['CLIENT_SECRET'],
                                                redirect_uri=required_variables['REDIRECT_URI'],
                                                scope=required_variables['SCOPE']))

    songs_title = []
    results = sp.current_user_saved_tracks(50)
    for idx, item in enumerate(results['items']):
        track = item['track']
        songs_title.append(track['artists'][0]['name'] + " – " + track['name'])
        print(idx, track['artists'][0]['name'], " – ", track['name'])
    
    youtube = build('youtube', 'v3', developerKey=required_variables['API_KEY'])

    downloader = YoutubeAudioDownloader()

    for song in range(len(songs_title)):
        video_id = downloader.get_youtube_video_id(youtube, songs_title[song])
        if video_id:
            try:
                downloader.download_audio(video_id)
            except Exception as e:
                print(f"An error occured: {e}")
        else:
            print(f"Could not find {song} on Youtube")

if __name__ == "__main__":
    main()