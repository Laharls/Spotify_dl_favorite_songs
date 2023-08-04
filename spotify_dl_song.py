import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv
from googleapiclient.discovery import build
import youtube_dl

load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.getenv('SPOTIFY_CLIENT_ID'),
                                               client_secret=os.getenv('SPOTIFY_CLIENT_SECRET'),
                                               redirect_uri=os.getenv("REDIRECT_URI"),
                                               scope=os.getenv('SCOPE')))

songs_title = []
results = sp.current_user_saved_tracks(50)
for idx, item in enumerate(results['items']):
    track = item['track']
    songs_title.append(track['artists'][0]['name'] + " – " + track['name'])
    print(idx, track['artists'][0]['name'], " – ", track['name'])

# Replace 'YOUR_API_KEY' with your actual YouTube Data API key
API_KEY = os.getenv('YOUTUBE_API_KEY')
youtube = build('youtube', 'v3', developerKey=API_KEY)
print(f"This is the Youtube API key: {API_KEY}")
def get_youtube_video_id(song_title):
    search_response = youtube.search().list(
        q=song_title,
        part='id',
        maxResults=1,  # You can set this to get multiple results if needed
        type='video'
    ).execute()

    if 'items' in search_response:
        return search_response['items'][0]['id']['videoId']
    else:
        return None
    
def download_audio(video_id):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(['https://www.youtube.com/watch?v=' + video_id])

for song in range(len(songs_title)):
    video_id = get_youtube_video_id(songs_title[song])
    if video_id:
        download_audio(video_id)
    else:
        print(f"Could not find {song} on Youtube")