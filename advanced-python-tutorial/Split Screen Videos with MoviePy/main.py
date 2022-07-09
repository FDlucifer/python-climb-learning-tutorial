# pip install moviepy

from moviepy.editor import VideoFileClip, clips_array

length = 2

clip1 = VideoFileClip("vid1.mp4").subclip(0, 0 + length).margin(2)
clip2 = VideoFileClip("vid2.mp4").subclip(0, 0 + length).margin(2)
clip3 = VideoFileClip("vid3.mp4").subclip(0, 0 + length).margin(2)
clip4 = VideoFileClip("vid4.mp4").subclip(0, 0 + length).margin(2)

combined = clips_array([[clip1, clip2], [clip3, clip4]])

combined.write_videofile("test.mp4")