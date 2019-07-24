'''
Description: Pipeline for data collection from spotify api. Collects song metadata and mp3s. 
Author: Ritwik
'''

import math
import string
import json

#Import and initiate spotify credentials
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
client_credentials_manager = SpotifyClientCredentials('23f5b5ae10874e0d9db993f3e9d532ec','68407a217ae24d57b888c4e1ba6a2f29')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
#import keras

def get_playlists():
    playlists = sp.user_playlists('ritwikbiswas',limit=10)
    # for i, playlist in enumerate(playlists['items']):
    #     print(playlist)
    results = sp.user_playlist('ritwikbiswas', playlists['items'][3]['id'],fields='tracks')
    # tracks = json.loads(results)
    #load tracks
    for tracks in results['tracks']['items']:
        print(tracks['track']['name'])
        print(tracks['track']['artists'][0]['name'])
        print(tracks['track']['id'])
        print("")
        # for i in tracks:
        #     print(i)
        #     print(tracks[i])

def main():
    get_playlists()
    
if __name__== "__main__":
  main()