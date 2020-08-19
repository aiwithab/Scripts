"""Spotify songs downloader script
	install spotdl using pip install spotdl
"""

import spotdl
import urllib.request as ur


def download_song_from_songname(song_name):
    s.download_track(song_name)
    print('song downloaded in root directory')


def download_song_from_url(song_url):
    s.download_track(song_url)
    print('song downloaded in root directory')


if __name__ == '__main__':
    try:
        if not (ur.urlopen('https://www.google.com')):
            raise ConnectionError()
    except:
        print('No internet found!')
        exit(-1)

    s = spotdl.Spotdl()

    print('Choose option:\n1.Song name\n2.Song Url')
    choice = input()
    if choice == str(1):
        print('enter the song name in the form (artist - song_name)')
        song_name = input()
        download_song_from_songname(song_name)
    elif choice == str(2):
        print('Enter the URL')
        song_url = input()
        download_song_from_url(song_url)
