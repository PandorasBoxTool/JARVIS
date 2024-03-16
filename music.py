from youtube_search import YoutubeSearch
from pytube import YouTube
from pydub import AudioSegment
import random
import os

def download_audio_from_youtube(video_url, output_path):
    yt = YouTube(video_url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_file_path = audio_stream.download(output_path=output_path)
    return audio_file_path

def convert_to_mp3(mp4_file_path):
    mp3_file_path = os.path.splitext(mp4_file_path)[0] + '.mp3'
    audio = AudioSegment.from_file(mp4_file_path)
    audio.export(mp3_file_path, format="mp3")
    return mp3_file_path

def play_music(song_name, artist_name=None):
    # Suchanfrage auf YouTube durchführen
    search_query = f"{song_name} {artist_name}" if artist_name else song_name
    results = YoutubeSearch(search_query, max_results=5).to_dict()

    # Zufälliges Video aus den Suchergebnissen auswählen
    random_video = random.choice(results)
    video_id = random_video['id']
    video_url = f"https://www.youtube.com/watch?v={video_id}"

    # Audio herunterladen und konvertieren
    audio_file_path = download_audio_from_youtube(video_url, output_path=r"YOUR_PATH")
    mp3_file_path = convert_to_mp3(audio_file_path)

    # Audio abspielen
    os.system(f"start {mp3_file_path}")
