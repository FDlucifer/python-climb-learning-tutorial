# youtube playlists download
import pytube
from pytube.streams import Stream

url = '' # Enter the youtube playlists url

playlist = pytube.Playlist(url)
for url in playlist:
    video = pytube.YouTube(url)
    stream = video.streams.get_by_itag(137)
    stream.download()