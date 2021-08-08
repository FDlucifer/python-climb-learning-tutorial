# single youtube vedio download
import pytube

url = '' # enter the youtube url

video = pytube.YouTube(url)

stream = video.streams.get_by_itag(299)
print("Downloading...")
stream.download(filename="142")
print("Done")