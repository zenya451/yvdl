import argparse
from pytube import YouTube

parser = argparse.ArgumentParser()
parser.add_argument("link", help="enter link to video")
args = parser.parse_args()

yt = YouTube(args.link)
yt = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()
yt.download()

print("Downloaded successfully !")
