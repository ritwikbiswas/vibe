'''
Description: Pipeline for data collection from spotify api. Collects song metadata and mp3s. 
Author: Ritwik
'''
# Default imports
import math
import string
import json
import pandas as pd

#Import and initiate spotify credentials
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
client_credentials_manager = SpotifyClientCredentials('23f5b5ae10874e0d9db993f3e9d532ec','68407a217ae24d57b888c4e1ba6a2f29')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
#import keras

class DataFlow:
    '''
    Class to collect and manage raw data from spotify api
    '''
    def __init__(self, data_path='raw_data/'):
        ''' Initialize internal processing variables '''
        self.data_path = data_path
        self.songs_processed = 0
        self.playlists_processed = 0
        columns = ["title","artist","playlist_id","duration","mode","time_sig","danceability","energy","instrumental","liveness","loudness","speechiness","valence","tempo","mp3_path"]
        self.df = pd.DataFrame(columns=columns) #create columns for each metadata piece, title, artist, playlist id, mp3 path

    def process_playlist(self,playlist_id=''):
        '''
        Given a playlist, collects all data for songs in playlist
        '''
        pass

    def process_all(self,playlist_file_path=''):
        '''
        Process and collect data from multiple playlists specified in a file
        '''
        pass
    

def get_user_playlists(username='ritwikbiswas'):
    '''
    Collect top songs from top playlists of a given user
    '''
    playlists = sp.user_playlists(username,limit=10)
    # for i, playlist in enumerate(playlists['items']):
    #     print(playlist)
    results = sp.user_playlist(username, playlists['items'][3]['id'],fields='tracks')
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
    # get_user_playlists()
    #print("hello")

if __name__== "__main__":
  main()