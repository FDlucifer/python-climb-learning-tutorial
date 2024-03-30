# pip install pytube colorama

from pytube import YouTube

def on_complete(stream, file_path):
    print(stream)
    print(file_path)

def on_progress(stream, chunk, bytes_remaining):
    print(100 - (bytes_remaining / stream.filesize * 100))

video_object = YouTube('https://www.youtube.com/watch?v=dQw4w9WgXcQ', on_complete_callback=on_complete, on_progress_callback=on_progress)

# video information
print(video_object.title)
print(f"{video_object.length / 60} minutes")
print(video_object.views)
print(video_object.author)
print(video_object.description)

# video streams
print(video_object.streams.get_highest_resolution())
print(video_object.streams.get_lowest_resolution())
print(video_object.streams.get_audio_only())

# download
video_object.streams.get_highest_resolution().download()