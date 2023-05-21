from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
from youtubesearchpython import VideosSearch
import pytube
import os


client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


playlist_id = 'spotify:playlist:{INSERT_YOUR_SPOTIFY_PLAYLIST_ID}'
path = r"{SELECT_A_PATH}"


def TrackNames(count):
    songs = []
    while True:
        results = sp.playlist_items(playlist_id,offset=count)
        if not results["items"]:
            break
        if len(songs) != results["total"]:
            for track in results["items"]:
                try:
                    songs.append(track["track"]["name"])
                    count += 1
                except TypeError:
                    count = 191
        else:
            break
    return songs

songs = list(dict.fromkeys(TrackNames(0)))

try:
    os.makedirs(path)
except FileExistsError:
    pass


for song in songs:
    url = VideosSearch(f"{song} lyrics",limit=1).resultComponents[0]["link"]
    yt = pytube.YouTube(url)
    audio = yt.streams.filter(only_audio=True)[0]
    audio.download(output_path = path, filename = f"{song}.mp3")

print("All Downloads Complete")
