import spotipy # Spotify Web API library
from spotipy.oauth2 import SpotifyOAuth # handles logging in
import os # to read environment variables
from dotenv import load_dotenv # to load .env file

load_dotenv() # reads the .env file


# Authenticate and create Spotify client

# few notes for myself:
# os.getenv reads the environment variables from the .env file

# basically, SpotifyOAuth logs in to Spotify using the provided credentials
# and the "scope" defines what permissions the app is requesting

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("SPOTIFY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIFY_REDIRECT_URI"),
    scope="playlist-read-private"
))

# this just basically prints out all the playlists you have
playlists = sp.current_user_playlists()
for playlist in playlists['items']:
    print(playlist['name'])
