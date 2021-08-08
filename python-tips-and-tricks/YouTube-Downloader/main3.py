# get the itag info
import pytube

url = '' # enter the youtube url

video = pytube.YouTube(url)


for stream in video.streams:
    if "video" in str(stream) and "mp4" in str(stream):
        print(stream)