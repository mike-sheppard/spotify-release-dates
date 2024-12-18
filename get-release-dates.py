import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv, dotenv_values
import click
from modules.playlists import get_playlist_tracks, pretty_print_track_info

# TODO: add this to a config file/CLI option
all_playlists = [
    'ABC',
    'XYZ',
]

@click.command()
@click.option("--playlist", is_flag=True)
@click.option("--year", is_flag=False)
def get_release_dates(playlist, year):
    as_playlist = playlist
    release_year = year
    print('Playlist:', as_playlist)
    print('Filter by release year:', release_year)

    # load .env file
    config = dotenv_values(".env")
    load_dotenv()
    auth_manager = SpotifyClientCredentials(client_id=os.getenv('CLIENT_ID'), client_secret=os.getenv('CLIENT_SECRET'))
    sp = spotipy.Spotify(client_credentials_manager=auth_manager)

    # get all tracks from playlist
    all_tracks = []
    for i in all_playlists:
        all_tracks += get_playlist_tracks(sp, os.getenv('USERNAME'), i)

    # print + export all tracks
    pretty_print_track_info(all_tracks, as_playlist, release_year)

if __name__ == '__main__':
    get_release_dates()
