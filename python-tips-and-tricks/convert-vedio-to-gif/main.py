from moviepy.editor import VideoClip
from moviepy.video.io.VideoFileClip import VideoFileClip

clip = VideoFileClip("video.mp4")
clip.write_gif("mygif.gif")