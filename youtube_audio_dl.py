import youtube_dl
import googleapiclient.errors
from environnement_config import EnvironnementVariable
from googleapiclient.discovery import build

class YoutubeAudioDownloader:
    youtube = build('youtube', 'v3', developerKey=EnvironnementVariable().required_variables['YOUTUBE_API_KEY'])

    def __init__(self, output_dir=None):
        self.output_dir = output_dir

    def get_youtube_video_id(self, youtube, song_title):
        try:
            search_response = youtube.search().list(
                q=song_title,
                part='id',
                maxResults=1,
                type='video'
            ).execute()
        except googleapiclient.errors.HttpError as e:
            raise Exception(f"An error has occured while fetching Youtube video ID: {e}.")

        #Return the id of the video found in the previous search
        if 'items' in search_response:
            return search_response['items'][0]['id']['videoId']
        else:
            print("No items found in the API response.")
            return None
    
    def download_audio(self, video_id):
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download(['https://www.youtube.com/watch?v=' + video_id])
        except youtube_dl.utils.DownloadError as e:
            raise Exception(f"An error has occured while downloading audio : {e}")