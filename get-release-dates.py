# Based off: https://stackoverflow.com/questions/40737168/get-track-release-date-in-spotify

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
import yaml
import click
from modules.playlists import get_playlist_tracks, pretty_print_track_info

config = yaml.safe_load(open("config.yml"))

def startup_checks():
    # check config file exists
    if not os.path.exists('config.yml'):
        print('No config.yml file found')
        exit()

    # exit if playlist is empty
    if not config['playlists'] or config['playlists'] == []:
        print('No playlists found in config.yml')
        exit()

    # exit if no auth details
    if not config['client_id'] or not config['client_secret']:
        print('No client_id or client_secret found in config.yml')
        exit()

@click.command()
@click.option("--playlist", is_flag=True)
@click.option("--year", is_flag=False)
def get_release_dates(playlist, year):
    as_playlist = playlist
    release_year = year
    print('Playlist:', as_playlist)
    print('Filter by release year:', release_year)

    # load .env file
    auth_manager = SpotifyClientCredentials(client_id=config['client_id'], client_secret=config['client_secret'])
    sp = spotipy.Spotify(client_credentials_manager=auth_manager)

    # get all tracks from playlist
    all_tracks = []
    for i in config['playlists']:
        all_tracks += get_playlist_tracks(sp, config['username'], i)

    # print + export all tracks
    pretty_print_track_info(all_tracks, as_playlist, release_year)

if __name__ == '__main__':
    startup_checks()
    get_release_dates()
