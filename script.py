from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Load environment variables from .env file
load_dotenv()

# Your Spotify API credentials
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REDIRECT_URI = 'https://localhost:3000'

# Playlist IDs you want to combine
playlist_ids = [
    '3pxPNS0FuqZUjRYKniA2hC', # Friday on the 49th Street
    '6aNiOmDI0j3o6GPWJpYIJp', # Palmwine Papi's NMF playlist
    '43NXxATYOdAJnYaUInt14c', # TUE's Catch UP
    '5LFeu7fiMYumn7NSMGlGao', # Tolu Daniels' Picks
    '37i9dQZF1DXbTop77dnX35' # Spotify's New Music Friday Naija
]

# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope='playlist-modify-private playlist-modify-public',
                                               open_browser=True))

# Create a set to store track IDs already added to the new playlist
added_tracks = set()

# Function to add tracks to the new playlist
def add_tracks_to_playlist(playlist_id):
    results = sp.playlist_tracks(playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])

    for item in tracks:
        # Check if the item has a track and the track has an ID
        if item.get('track') and item['track'].get('id'):
            track_id = item['track']['id']
            if track_id and track_id not in added_tracks:
                added_tracks.add(track_id)
                sp.playlist_add_items(new_playlist['id'], [track_id])
        else:
            print("Skipping track - no ID found:", item['track'])

# Create a new playlist and add tracks to it
user_id = sp.me()['id']
playlist_name = 'New Music Playlist for Sam'
new_playlist = sp.user_playlist_create(user_id, playlist_name, public=True)

# Add tracks from each specified playlist to the new playlist
for playlist_id in playlist_ids:
    add_tracks_to_playlist(playlist_id)

print(f"The playlists have been combined into a new playlist named '{playlist_name}'.")
