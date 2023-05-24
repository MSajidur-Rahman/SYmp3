# SYmp3

Downloads the mp3 version of tracks from a spotify playlist from youtube


## Setting up

### Spotify IDs

- Go to [Spotify's dev website](https://developer.spotify.com/), log in, go to dashboard, and create an app
- Fill the required info with anything, go to settings, and find both your client ID and client secret

### Setting the env vars

- Create a new environment and activate it
- Create an env var called "SPOTIPY_CLIENT_ID" and set your client ID to it
- Repeat with "SPOTIPY_CLIENT_SECRET" and your client secret
- View [this video](https://www.youtube.com/watch?v=kaBVN8uP358&t=0s&ab_channel=DanArwady) for help

### Installing the required libs

- pip install spotipy 
  - [github url](https://github.com/spotipy-dev/spotipy)
- pip install youtube-search-python 
  - [github url](https://github.com/alexmercerind/youtube-search-python)
- pip install pytube 
  - [github url](https://github.com/pytube/pytube)

## How to use

- Clone this repo and open SYmp3.py
>  $ git clone https://github.com/MSajidur-Rahman/SYmp3.git
- Go to spotify 
- Copy the link of any playlist or album 
> https://open.spotify.com/playlist/0FpcTWSefFG3Ive4BNbawj?si=40cbd2b471c84e2b
- Copy the playlist ID which is the part between the last '/' and '?' in the link
> 0FpcTWSefFG3Ive4BNbawj
- Replace '{INSERT_YOUR_SPOTIFY_PLAYLIST_ID}' in line 12 of SYmp3.py with your playlist ID
- Replace '{SELECT_A_PATH}' in line 13 with the path of where you would like the downloaded songs
- Run code
