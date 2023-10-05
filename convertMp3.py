import os
os.environ["IMAGEIO_FFMPEG_EXE"] = "/opt/homebrew/Cellar/ffmpeg/6.0_1/bin/ffmpeg"
from pytube import YouTube
from moviepy.editor import *
link = input("url: ")
try:
    yt = YouTube(link)
    video = yt.streams.get_highest_resolution
    video = VideoFileClip(yt.title+".mp4")
    video.audio.write_audiofile(yt.title+".mp3")
except Exception as e:
    print("Download fail",e)