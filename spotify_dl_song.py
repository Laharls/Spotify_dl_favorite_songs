from spotify import Spotify
from environnement_config import EnvironnementVariable
from youtube_audio_dl import YoutubeAudioDownloader

def main():
    NB_SONG_TO_DL = 20
    OFFSET = 50

    #Check env variable are valid
    env_variable = EnvironnementVariable()
    env_variable.check_valid_variable()

    spotify = Spotify(env_variable.required_variables['SPOTIFY_CLIENT_ID'], 
                      env_variable.required_variables['SPOTIFY_CLIENT_SECRET'], 
                      env_variable.required_variables['SPOTIFY_APP_REDIRECT_URI'], 
                      env_variable.required_variables['SPOTIFY_SCOPE'])
    
    songs_title = spotify.get_top_liked_songs(NB_SONG_TO_DL, OFFSET)

    downloader = YoutubeAudioDownloader()

    # #Get the id of a youtube video corresponding to the song, and tries to download it
    for song in range(len(songs_title)):
        video_id = downloader.get_youtube_video_id(downloader.youtube, songs_title[song])
        if video_id:
            try:
                downloader.download_audio(video_id)
            except Exception as e:
                print(f"An error occured: {e}")
        else:
            print(f"Could not find {song} on Youtube")

if __name__ == "__main__":
    main()