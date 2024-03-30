import subprocess
import os


def convert_video_to_mp3(input_file, output_file):
    ffmpeg_cmd = [
        "ffmpeg",
        "-i",
        input_file,
        "-vn",
        "-acodec",
        "libmp3lame",
        "-ab",
        "192k",
        "-ar",
        "44100",
        "-y",
        output_file,
    ]

    try:
        subprocess.run(ffmpeg_cmd, check=True)
        print("successfully converted!")
    except subprocess.CalledProcessError as e:
        print("conversion failed!")


for i, filename in enumerate(os.listdir(".")):
    if filename.endswith(".mov"):
        convert_video_to_mp3(filename, f"audio_{i}.mp3")
