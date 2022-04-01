# pip install moviepy

from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx, AudioFileClip, afx, CompositeAudioClip

clip1 = VideoFileClip("one.mp4").subclip(10,20).fx(vfx.fadein, 1).fx(vfx.fadeout, 1)
clip2 = VideoFileClip("two.mp4").subclip(10,20).fx(vfx.fadein, 1).fx(vfx.fadeout, 1)
clip3 = VideoFileClip("one.mp4").subclip(20,30).fx(vfx.fadein, 1).fx(vfx.fadeout, 1)
clip4 = VideoFileClip("one.mp4").subclip(10,20).fx(vfx.colorx, 1.5)\
    .fx(vfx.lum_contrast, 0, 50, 128)

audio = AudioFileClip("intro.mp4").fx(afx.audio_fadein, 1).fx(afx.volumex, 0.1)

combined = concatenate_videoclips([clip1, clip2, clip3, clip4])
combined.audio = CompositeAudioClip([audio])
combined.write_videofile("combined.mp4")