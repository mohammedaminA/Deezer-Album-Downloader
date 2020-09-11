from pydeezer import Deezer
from pydeezer.constants import track_formats


def download_album(album_name):
    # you can obtain an arl by login into your deezer account and using developer tools to check cookies
    arl = ""
    deezer = Deezer(arl=arl)
    user_info = deezer.user

    album_search_results = deezer.search_albums(album_name, limit=5)

    album_id = album_search_results[0]['id']
    album = deezer.get_album(album_id)
    track = album['tracks']
    data = track['data']
    number_tracks = album['nb_tracks']
    title = album['title']
    download_dir = "Your Dir" + title
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



