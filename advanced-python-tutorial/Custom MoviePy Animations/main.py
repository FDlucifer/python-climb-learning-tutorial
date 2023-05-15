# pip install moviepy numpy

import math
import numpy as np
from moviepy.editor import *

video_clip = VideoFileClip("video.mp4")
image_clip = ImageClip("image.png").set_duration(video_clip.duration)

center_x = video_clip.size[0] / 2 - image_clip.size[0] / 2
center_y = video_clip.size[1] / 2 - image_clip.size[1] / 2

radius = 400


def circular_motion(t):
    return center_x + radius * np.cos(
        (t / video_clip.duration) * 2 * math.pi
    ), center_y + radius * np.sin((t / video_clip.duration) * 2 * math.pi)


image_clip = image_clip.set_position(circular_motion)
final_clip = CompositeVideoClip([video_clip, image_clip])
final_clip.write_videofile("output_simple.mp4", fps=video_clip.fps)
