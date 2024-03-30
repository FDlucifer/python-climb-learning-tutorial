# multi video download
import pytube
from pytube import streams

video_list = []

print("Enter URLs (Terminate by 'STOP')")
while True:
    url = input("")
    if url == 'STOP':
        break
    video_list.append(url)

for x, video in enumerate(video_list):
    v = pytube.YouTube(video)
    stream = v.streams.get_by_itag(137)
    print(f"Downloading video {x}...")
    stream.download()
    print("Done")