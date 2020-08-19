"""Spotify songs downloader script with GUI"""

import spotdl
import urllib.request as ur
import tkinter as tk
import tkinter.messagebox as messagebox
def download_song():
    song_full_name = song_artist_name_entry.get() + ' - ' + song_name_entry.get()
    s.download_track(song_full_name)
    song_artist_name_entry.insert(0,'')
    song_name_entry.insert(0,'')
    messagebox.showinfo(title='Success',message='Song Downloaded in root directory of application')





if __name__ == '__main__':

    s = spotdl.Spotdl()
    root = tk.Tk()
    root.geometry('1280x760')
    root.title('Spotify Downloader')
    try:
        if not (ur.urlopen('https://www.google.com')):
            raise ConnectionError()
    except:
        root.destroy()
        exit(-1)

    song_artist_name_label = tk.Label(master=root,text='Song Artist Name: ')
    song_artist_name_label.grid(row=0,column=0)

    song_name_label = tk.Label(master=root,text='Song Name: ')
    song_name_label.grid(row=1,column=0)

    song_artist_name_entry = tk.Entry(master=root)
    song_artist_name_entry.grid(row=0,column=1)


    song_name_entry = tk.Entry(master=root)
    song_name_entry.grid(row=1,column=1)

    btn_download = tk.Button(master=root,text='Download',command=download_song)
    btn_download.grid(row=2,column=0)
    root.mainloop()
