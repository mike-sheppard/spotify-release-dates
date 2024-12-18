import os
import pandas as pd
import json
from datetime import datetime
from modules.utils import dtStylish

def get_playlist_tracks(sp, username, playlist_id):
    # create a folder for each user + export playlists to json
    filename = f"exports/{username}/{playlist_id}.json"
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    results = sp.user_playlist_tracks(username, playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])

    # remove available_markets from each track + albums, way too much noise! 🤫
    for i in tracks:
        if i['track']['is_local'] != True:
            i['track'].pop('available_markets', None)
            i['track']['album'].pop('available_markets', None)

    # writing the json file
    json_object = json.dumps(tracks, indent = 4)
    with open(filename, "w") as outfile:
        outfile.write(json_object)

    return tracks

def pretty_print_track_info(all_tracks, as_playlist, release_year):
    print('Total tracks:', len(all_tracks), '\n')

    all_track_names = []
    for i in all_tracks:
        if (i['track']['is_local'] != True):
            all_track_names.append([
                i['track']['artists'][0]['name'],
                i['track']['name'],
                i['track']['album']['name'],
                i['track']['album']['release_date'][:4],
                i['track']['uri'],
                datetime.fromisoformat(i['added_at']).strftime('%a'),
                dtStylish(datetime.fromisoformat(i['added_at']), '{th}'),
                datetime.fromisoformat(i['added_at']).strftime('%b'),
                datetime.fromisoformat(i['added_at']).strftime('%H:%M'),
                datetime.fromisoformat(i['added_at']),
            ])

    pd.set_option('display.max_rows', None)
    df = pd.DataFrame(all_track_names, columns=[
        'Artist',
        'Track',
        'Album',
        'Released',
        'URI',
        'Added',
        'Day',
        'Month',
        'Time',
        'Added (ISO)',
    ], index=None).sort_values(by='Added (ISO)')

    # filter all tracks by release year
    if release_year:
        df = df[df['Released'] == release_year]

    # reset index after filtering + sorting
    df.reset_index(drop=True, inplace=True)

    if as_playlist:
        df.drop(columns=[
            'Artist',
            'Track',
            'Album',
            'Released',
            'Added',
            'Day',
            'Month',
            'Time',
            'Added (ISO)',
        ], inplace=True)

    else:
        df.drop(columns=[
            'URI',
            'Added (ISO)',
        ], inplace=True)

    # print the dataframe without index if viewing as_playlist
    print(df.to_string(index = not as_playlist))
