# Spotify Release Dates
Quick and dirty way to loop over multiple playlists and extract release dates + optionally filter by specific year + sort tracks by date added.

## Get Started
1. `git clone git@github.com:mike-sheppard/spotify-release-dates.git && cd spotify-release-dates && pip install -r requirements.txt`
1. Create a Spotify Developer account and create a new app to get your client ID and client secret - [quick youtube guide here](https://www.youtube.com/watch?v=kaBVN8uP358)
1. Set your Spotify username, playlist ID's, client ID and secret in `config.yml` (see + copy `config.example.yml`)
1. Run the script:
    - `python get-release-dates.py` show all tracks in playlists with release dates
    - `--playlist` generate a playlist you can copy & paste directly into Spotify
    - `--year=1972` filter by track/album release year

### CLI Output/Preview
![Preview playlist CLI output](./docs/preview-tracks.png)

![Preview playlist CLI output](./docs/preview-playlist.png)

## API/Docs
- [Spotipy](https://spotipy.readthedocs.io/en/2.22.1/#examples)
- [Spotify Web API](https://developer.spotify.com/documentation/web-api/)

## Credits
Nabbed and mutated from this super helpful [Stack Overflow post](https://stackoverflow.com/a/77714867)
