from pydeezer import Deezer
from pydeezer.constants import track_formats
from twilio.rest import Client


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
   def twilio():
        client = Client(account_sid, auth_token)

        client.api.account.messages.create(
            to='phone number',
            from_='phone number from twilio',
            body=f'A user just downloaded {album_title} by ' + artist
        )

    twilio()
    
def download_playlist(playlist_name):
    search_results = deezer.search_playlists(playlist_name, limit=5)
    playlist_id = search_results[0]['id']
    playlist = deezer.get_playlist(playlist_id)
    number_songs = playlist['DATA']['NB_SONG']
    download_dir = "/music1/" + playlist_name
    songs = playlist['SONGS']
    data = songs['data']
    print(data)
    song_id = []

    x = 0
    while x < number_songs:
        song_id.append(data[9]['SNG_ID'])
        x += 1

    y = 0
    while y < number_songs:
        song = deezer.get_track(song_id[y])
        song['download'](download_dir, quality=track_formats.MP3_320)
        y = + 1


def main(action=int(input(" Choose from the following: 1. Download an album 2. download a playlist : "))):
    print(action)
    if action == 1:
        album_name = input(" Tell me the Album Name: ")
        download_album(album_name)
    elif action == 2:
        playlist_name = input(" Tell me the playlist name : ")
        download_playlist(playlist_name)
    else:
        print("You haven't selected a correct option")


main()



