# YouTube Audio Downloader

This Python script allows you to download audio from YouTube videos and save them in MP3 format, using the top liked song of a Spotify account.

## Prerequisites

Before running the script, ensure you have the following installed on your system:

- Python 3.x
- FFmpeg
- A Spotify account
- A Google account

## Installation

1. Clone the repository or download the `spotify_dl_song.py` file.

2. Install the required Python libraries using pip:

3. Make sure you have FFmpeg installed on your system. If not, download and install it from the official website: https://www.ffmpeg.org/download.html

4. Make sure to create a Spotify app : https://developer.spotify.com/

5. Make sure to create a Google app to use Youtube Data v3 API : https://cloud.google.com/?hl=en

6. Create a .env file and add the credentials needed by the script

## Usage

1. Open a terminal or command prompt.

2. Navigate to the directory where `spotify_dl_song.py` is located.

3. To download the audio of a YouTube video, run the script followed by the video's URL or video ID:

python spotify_dl_song.py

4. The script will automatically find the top 50 latest songs liked by the user, search them on Youtube and download them if it found it in the same directory as the script, in mp3 format.

## Notes

- By default, the script downloads the highest quality audio available for the video. The audio will be saved in MP3 format with a bitrate of 192 kbps. You can modify the script to adjust the quality settings as needed.

- The script uses the `youtube_dl` library to download YouTube videos. If you encounter any issues with the script or YouTube changes its website structure, please check for updates or report issues on the [youtube_dl GitHub repository](https://github.com/ytdl-org/youtube-dl).


