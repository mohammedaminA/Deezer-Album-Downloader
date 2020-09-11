from pydeezer import Deezer
from pydeezer.constants import track_formats


def download_album(album_name):
    arl = "cf9134857a1ccdf2d081bef2f1c69cf54446ee1869ffa0cbf6182577f2b1ff9bf45fbd5721bcadf7456dc3b357354a2475abed97cfde0111934e74ecb0f0841d4c24e55e69a8977617bfa40c29f0df5f0c48bc1a73fb5c90e6afd38d6a05bc4a "
    deezer = Deezer(arl=arl)
    user_info = deezer.user

    album_search_results = deezer.search_albums(album_name, limit=5)

    album_id = album_search_results[0]['id']
    album = deezer.get_album(album_id)
    track = album['tracks']
    data = track['data']
    number_tracks = album['nb_tracks']
    title = album['title']
    download_dir = "/music1/" + title
    track_list = []
    x = 0

    while x < number_tracks:
        track_list.append(data[x]['id'])
        x += 1

    y = 0

    while y < number_tracks:
        song = deezer.get_track(track_list[y])
        song["download"](download_dir, quality=track_formats.MP3_320)
        y += 1


download_album("Detroit 2")
